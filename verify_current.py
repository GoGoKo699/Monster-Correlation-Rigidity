#!/usr/bin/env python3
"""Run current exact checks; keep historical strict replay and portability distinct.

The default requires only the standard library. --all also requires the pinned
NumPy reproduction dependency. Logs may be saved outside the checkout.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'checks'))
from release_integrity import verify_files, require

CURRENT = ('checks/verify_extraction_core.py',
           'checks/verify_calibration_and_sharpness.py',
           'checks/audit_quantitative_core.py',
           'checks/verify_calibration_scales.py',
           'checks/verify_release_package.py')
KNOWN_REPLAY = {
    'RuntimeError: prior average toy differs from recorded report under None',
    'RuntimeError: prior pair toy differs from recorded report under None',
}


def run(script: str, flags: list[str], output: Path | None) -> tuple[dict, bytes, str]:
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    command = [sys.executable, *flags, script]
    try:
        result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, timeout=120)
        code, stdout, stderr = result.returncode, result.stdout, result.stderr.decode(errors='replace')
    except subprocess.TimeoutExpired:
        code, stdout, stderr = 124, b'', 'Verification subprocess exceeded 120 seconds'
    label = flags[0] if flags else 'normal'
    row = {'mode': label, 'returncode': code, 'stdout_sha256': hashlib.sha256(stdout).hexdigest()}
    if output:
        name = script.replace('/', '__').replace('.py', '') + '-' + label.lstrip('-')
        (output / (name + '.stdout')).write_bytes(stdout)
        (output / (name + '.stderr')).write_text(stderr)
    if code:
        row['stderr_tail'] = '\n'.join(stderr.splitlines()[-3:])
    return row, stdout, stderr


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--all', action='store_true', help='all current checkers plus historical comparisons')
    parser.add_argument('--require-strict-replay', action='store_true', help='fail for any historical mismatch')
    parser.add_argument('--baseline', type=Path, help='optional pinned pre-release checkout for full delta comparison')
    parser.add_argument('--output', type=Path, help='save stdout/stderr outside the repository')
    args = parser.parse_args()
    if args.require_strict_replay and not args.all:
        parser.error('--require-strict-replay requires --all')
    if args.output:
        args.output = args.output.resolve()
        require(not args.output.is_relative_to(ROOT.resolve()), 'Output must be outside the repository')
        args.output.mkdir(parents=True, exist_ok=True)
    integrity = verify_files(baseline=args.baseline)
    manifest_before = (ROOT / 'results/release_preparation.json').read_bytes()
    expected = {r['script']: r for r in json.loads((ROOT / 'results/current_reports.json').read_text())['reports']}
    scripts = list(CURRENT)
    if args.all:
        additional = [str(p.relative_to(ROOT)) for p in sorted((ROOT / 'checks').glob('*.py'))
                      if p.name.startswith(('audit_', 'verify_'))]
        scripts = list(dict.fromkeys([*scripts, *additional]))
    rows, failures = [], []
    for script in scripts:
        runs = [run(script, opt, args.output) for opt in ([], ['-O'], ['-OO'])]
        report = {'script': script, 'modes': [r[0] for r in runs],
                  'mode_outputs_identical': all(r[1] == runs[0][1] for r in runs)}
        ok = all(r[0]['returncode'] == 0 for r in runs) and report['mode_outputs_identical']
        if script in expected:
            try:
                payload = json.loads(runs[0][1])
                matches = (runs[0][0]['stdout_sha256'] == expected[script]['sha256'] and
                           payload['checks'] == expected[script]['checks'])
            except (ValueError, KeyError):
                matches = False
            report['current_fingerprint_matches'] = matches
            ok = ok and matches
        if not ok:
            failures.append(script)
        rows.append(report)
        print(('PASS ' if ok else 'FAIL ') + script, file=sys.stderr, flush=True)
    historical = {'run': False}
    if args.all:
        strict = run('verify.py', [], args.output)
        portable = run('checks/replay_portability.py', [], args.output)
        strict_ok = strict[0]['returncode'] == 0
        error_line = strict[2].strip().splitlines()[-1] if strict[2].strip() else ''
        known = not strict_ok and error_line in KNOWN_REPLAY
        try:
            port = json.loads(portable[1])
            port_ok = portable[0]['returncode'] == 0 and port['status'].startswith('PASS')
        except (ValueError, KeyError):
            port, port_ok = {}, False
        historical = {'run': True, 'strict_byte_replay': 'PASS' if strict_ok else 'FAIL',
                      'known_float_report_mismatch': known,
                      'bounded_portability': 'PASS' if port_ok else 'FAIL',
                      'all_reports_byte_identical': port.get('all_reports_byte_identical'),
                      'different_float_leaves': sum(r.get('different_float_leaves', 0) for r in port.get('reports', [])),
                      'strict_error': error_line if not strict_ok else None}
        if not port_ok or (not strict_ok and (not known or args.require_strict_replay)):
            failures.append('historical_replay_requirement')
        print(json.dumps(historical, sort_keys=True), file=sys.stderr, flush=True)
    verify_files(baseline=args.baseline)
    require(manifest_before == (ROOT / 'results/release_preparation.json').read_bytes(),
            'Release manifest changed during verification')
    status = 'FAIL' if failures else 'PASS_CURRENT'
    if not failures and historical.get('strict_byte_replay') == 'FAIL':
        status = 'PASS_CURRENT_WITH_HISTORICAL_STRICT_FAILURE'
    summary = {'status': status, 'current_checker_count': len(rows), 'current_runs': 3*len(rows),
               'integrity': integrity, 'reports': rows, 'failures': failures,
               'historical': historical, 'source_theorems_verified': False,
               'live_GitHub_render_verified': False}
    text = json.dumps(summary, sort_keys=True, indent=2) + '\n'
    if args.output:
        (args.output / 'summary.json').write_text(text)
    print(text, end='')
    return 1 if failures else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as exc:
        print('FAIL current verification: ' + str(exc), file=sys.stderr)
        sys.exit(1)
