#!/usr/bin/env python3
"""Regression checks for the active reading path and declared display repair.

This checks Markdown, arithmetic literals and preservation, not VOA theorems
or the live GitHub browser. --export-math emits a corpus for a TeX renderer.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

BASE = '96d3c7011645ace358844d3494eef0bef657d104'
MANIFEST = 'results/math_rendering_changes.json'
PROOFS = ('research/uniform_extraction_core.md',
          'research/sharpness_and_calibration.md')
MODIFIED = {*PROOFS, 'checks/verify_teaching.py',
            '.github/workflows/quantitative-core-review.yml'}
ROOT = Path(__file__).resolve().parents[1]


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def check_manifest(root: Path) -> dict:
    manifest = json.loads((root / MANIFEST).read_text())
    require(manifest['base_commit'] == BASE, 'Unexpected display baseline')
    require({e['path'] for e in manifest['modified']} == MODIFIED,
            'Unexpected display modification set')
    entries = manifest['modified'] + manifest['added']
    names = [e['path'] for e in entries]
    require(len(names) == len(set(names)) and MANIFEST not in names,
            'Duplicate or self-referential manifest')
    for entry in entries:
        path = (root / entry['path']).resolve()
        require(path.is_relative_to(root.resolve()), 'Manifest path escapes root')
        raw = path.read_bytes()
        require(len(raw) == entry['bytes'] and digest(raw) == entry['sha256'],
                'Display fingerprint mismatch: ' + entry['path'])
    return manifest


def check_preservation(root: Path, baseline: Path, manifest: dict) -> None:
    def git(*args: str, cwd: Path) -> str:
        return subprocess.check_output(['git', '-C', str(cwd), *args], text=True)
    require(git('rev-parse', 'HEAD', cwd=baseline).strip() == BASE,
            'Wrong pre-display baseline checkout')
    old_names = set(filter(None, git('ls-files', '-z', cwd=baseline).split('\0')))
    new_names = set(filter(None, git('ls-files', '-z', cwd=root).split('\0')))
    added = {e['path'] for e in manifest['added']} | {MANIFEST}
    require(new_names - old_names == added and not old_names - new_names,
            'Unexpected additions or deletions')
    changed = {e['path']: e for e in manifest['modified']}
    for name in sorted(old_names):
        old, new = (baseline/name).read_bytes(), (root/name).read_bytes()
        if name in changed:
            require(digest(old) == changed[name]['previous_sha256'],
                    'Previous fingerprint mismatch: ' + name)
        else:
            require(old == new, 'Unapproved change: ' + name)
    for name in PROOFS:
        old, new = (baseline/name).read_text(), (root/name).read_text()
        require(Counter(re.findall(r'\d+', old)) == Counter(re.findall(r'\d+', new)),
                'Numeric literal drift: ' + name)
        require(re.findall(r'^## .+$', old, re.M) == re.findall(r'^## .+$', new, re.M),
                'Research section anchors changed: ' + name)
    # Numeric multisets are a transcription guard, not semantic proof checking.


def inspect_page(text: str, name: str, root: Path | None = None) -> list[dict]:
    require(not any(line.rstrip() != line for line in text.splitlines()),
            'Trailing whitespace: ' + name)
    require(text.count('```') % 2 == 0, 'Unbalanced code fence: ' + name)
    require(text.count('<details>') == text.count('</details>'),
            'Unbalanced details block: ' + name)
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'`[^`]*`', '', text)
    # A known-bad macro must fail even though an unrestricted TeX engine accepts it.
    require(not re.search(r'\\(?:operatorname|tag|newcommand|renewcommand|def)\b', text),
            'Unsupported macro in active page: ' + name)
    math = re.compile(r'\$\$(.*?)\$\$|(?<!\\)\$([^\n$]*?)(?<!\\)\$', re.S)
    corpus = []
    for match in math.finditer(text):
        display = match.group(1) is not None
        expression = match.group(1) if display else match.group(2)
        require(bool(expression.strip()), 'Empty expression: ' + name)
        depth = 0
        for brace in re.findall(r'(?<!\\)[{}]', expression):
            depth += 1 if brace == '{' else -1
            require(depth >= 0, 'Extra close brace: ' + name)
        require(depth == 0, 'Missing close brace: ' + name)
        if display and name in PROOFS:
            require(expression.startswith('\n') and expression.endswith('\n'),
                    'Display delimiters must have their own lines: ' + name)
        corpus.append({'page': name, 'display': display, 'tex': expression.strip()})
    outside = math.sub('', text)
    require(not re.search(r'(?<!\\)\$', outside), 'Unmatched dollar delimiter: ' + name)
    if name in PROOFS:
        require(not re.search(r'(?:sqrt\(|\b(?:epsilon|kappa|omega|Delta)\b|<=|>=)', outside),
                'Unformatted mathematical expression: ' + name)
    if root is not None:
        for link in re.findall(r'\[[^\]]+\]\(([^)\s]+)\)', text):
            u = urlsplit(link)
            if u.scheme or u.netloc or not u.path:
                continue
            target = (root / name).parent / unquote(u.path)
            require(target.resolve().is_relative_to(root.resolve()) and target.is_file(),
                    'Broken local link: ' + name + ' -> ' + link)
    return corpus


def negative_controls() -> int:
    examples = [r'$$\operatorname{dist}(x,A)$$', r'$$x=1\tag{1}$$',
                r'$\frac{1}{2$', r'$\frac{1}{2}}$', r'$x=1',
                'A bare sqrt(141) remains.']
    for text in examples:
        try:
            inspect_page(text, PROOFS[0])
        except RuntimeError:
            continue
        raise RuntimeError('A display negative control was accepted')
    return len(examples)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--export-math', type=Path)
    args = parser.parse_args()
    manifest = check_manifest(ROOT)
    paths = [ROOT/'README.md', *sorted((ROOT/'docs/learn').glob('*.md')),
             *(ROOT/p for p in PROOFS)]
    require(len(paths) == 10, 'Expected ten active teaching/proof pages')
    corpus = []
    for path in paths:
        corpus.extend(inspect_page(path.read_text(), str(path.relative_to(ROOT)), ROOT))
    from verify_teaching import arithmetic, documents, LABELS
    arithmetic()
    documents(ROOT)
    teaching_checks = len(LABELS)
    controls = negative_controls()
    if args.baseline:
        check_preservation(ROOT, args.baseline.resolve(), manifest)
    if args.export_math:
        args.export_math.write_text(json.dumps(corpus, indent=2) + '\n')
    print(json.dumps({'status': 'PASS active Markdown and declared display-only delta',
                      'pages': len(paths), 'math_expressions': len(corpus),
                      'negative_controls': controls, 'teaching_checks': teaching_checks,
                      'baseline_comparison': args.baseline is not None,
                      'live_GitHub_render_verified': False,
                      'mathematical_proof_verified': False}, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
