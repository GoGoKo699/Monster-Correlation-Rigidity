#!/usr/bin/env python3
"""Current file integrity with a separate, immutable pre-release baseline.

The manifest declares an intentional delta; it is not a cryptographic proof
of the mathematical results. Historical manifests are never rewritten here.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'results/release_preparation.json'
BASE = 'ecd0623e9de41b49754b6ca16dc23752443143af'
BASE_TREE = '20c5252c0bd5e83d6a908ee226e5799e947280fc'
PROOFS = ('research/uniform_extraction_core.md', 'research/sharpness_and_calibration.md')


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def safe(root: Path, name: str) -> Path:
    relative = Path(name)
    require(not relative.is_absolute() and '..' not in relative.parts, 'Unsafe manifest path')
    path = root / relative
    require(path.resolve().is_relative_to(root.resolve()) and not path.is_symlink(),
            'Escaping or symbolic manifest path: ' + name)
    return path


def tracked(root: Path) -> set[str] | None:
    # An exported source ZIP is also a supported verification input.
    if not (root / '.git').exists():
        return None
    raw = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z'])
    return set(filter(None, raw.decode().split('\0')))


def protected(name: str) -> bool:
    return (name in ('LICENSE', 'verify.py', 'checks/replay_portability.py')
            or name.startswith('provenance/')
            or bool(re.match(r'research/\d\d_', name))
            or name.startswith('results/'))


def verify_files(root: Path = ROOT, baseline: Path | None = None) -> dict:
    root = root.resolve()
    m = json.loads((root / MANIFEST).read_text())
    require(m['base_commit'] == BASE and m['base_tree'] == BASE_TREE,
            'Unexpected release-preparation baseline')
    groups = [m[k] for k in ('modified', 'added', 'preserved')]
    entries = [item for group in groups for item in group]
    names = [e['path'] for e in entries]
    require(len(names) == len(set(names)) and MANIFEST not in names,
            'Duplicate or self-referential release manifest')
    require(not any(protected(e['path']) for e in m['modified']),
            'Protected historical source or evidence declared modified')
    for e in entries:
        raw = safe(root, e['path']).read_bytes()
        require(len(raw) == e['bytes'] and sha(raw) == e['sha256'],
                'Current fingerprint mismatch: ' + e['path'])
    index = tracked(root)
    if index is not None:
        require(index == set(names) | {MANIFEST}, 'Tracked-file inventory mismatch')
    # The seed-era snapshot is still usable by the unchanged root verifier.
    snapshot = json.loads((root / 'snapshot_manifest.json').read_text())
    for e in snapshot['files']:
        raw = safe(root, e['path']).read_bytes()
        require(len(raw) == e['bytes'] and sha(raw) == e['sha256'],
                'Current seed snapshot mismatch: ' + e['path'])
    if baseline is not None:
        baseline = baseline.resolve()
        require(baseline != root, 'The current tree cannot be its own baseline')
        old_names = {e['path'] for e in m['modified'] + m['preserved']}
        old_index = tracked(baseline)
        if old_index is not None:
            require(old_index == old_names, 'Baseline inventory mismatch')
            old_tree = subprocess.check_output(
                ['git', '-C', str(baseline), 'write-tree'], text=True).strip()
            require(old_tree == BASE_TREE, 'Wrong baseline Git tree')
        for e in m['modified']:
            require(sha(safe(baseline, e['path']).read_bytes()) == e['previous_sha256'],
                    'Pre-change source mismatch: ' + e['path'])
        for e in m['preserved']:
            require(safe(baseline, e['path']).read_bytes() == safe(root, e['path']).read_bytes(),
                    'Preserved baseline file changed: ' + e['path'])
        from verify_display import inspect_page
        for name in PROOFS:
            old = inspect_page((baseline / name).read_text(), name)
            new = inspect_page((root / name).read_text(), name)
            require(old == new, 'Canonical proof mathematics changed: ' + name)
        for name in ('STATUS.md', 'STATUS_CURRENT.md', 'PHYSICS_STATUS.md'):
            body = (root / name).read_text().split('\n\n', 1)[1]
            require(body == (baseline / name).read_text(), 'Historical ledger body changed: ' + name)
    return {'files': len(entries) + 1, 'baseline_compared': baseline is not None,
            'base_commit': BASE, 'mathematical_theorems_verified': False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    args = parser.parse_args()
    print(json.dumps({'status': 'PASS current release-source integrity',
                      **verify_files(baseline=args.baseline)}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
