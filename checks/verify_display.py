#!/usr/bin/env python3
"""Check active Markdown including math fences, not live GitHub or VOA proofs.

--baseline verifies the full presentation-only delta from the pinned checkout.
--export-math includes every fenced, dollar-display, and inline expression.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

BASE = '7653d6cef036f40db2746b3379e84dc161b18f55'
MANIFEST = 'results/hopf_style_changes.json'
PROOFS = ('research/uniform_extraction_core.md',
          'research/sharpness_and_calibration.md')
LESSONS = ('01_correlations.md', '02_weight_two.md', '03_ising.md',
           '04_rounding.md', '05_worked_certificate.md')
PAGES = ('README.md', *(f'docs/learn/{p}' for p in LESSONS), *PROOFS)
MODIFIED = {*PAGES, 'checks/verify_display.py', 'snapshot_manifest.json',
            '.github/workflows/quantitative-core-review.yml'}
ROOT = Path(__file__).resolve().parents[1]
BAD_MACRO = re.compile(r'\\(?:operatorname|tag|newcommand|renewcommand|def)\b')
OPEN_FENCE = re.compile(r'^ {0,3}(`{3,}|~{3,})([^\n]*)$')
NAV = {
    PROOFS[0]: '[← Learning path](../docs/learn/README.md) · [Overview](../README.md) · [Sharpness and calibration →](sharpness_and_calibration.md)',
    PROOFS[1]: '[← Core proof](uniform_extraction_core.md) · [Learning path](../docs/learn/README.md) · [Overview](../README.md)',
}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def check_manifest(root: Path) -> dict:
    m = json.loads((root/MANIFEST).read_text())
    require(m['base_commit'] == BASE, 'Wrong style baseline')
    require({e['path'] for e in m['modified']} == MODIFIED, 'Wrong modification set')
    entries = m['modified'] + m['added']
    names = [e['path'] for e in entries]
    require(len(names) == len(set(names)) and MANIFEST not in names,
            'Duplicate or self-referential manifest')
    for e in entries:
        p = (root/e['path']).resolve()
        require(p.is_relative_to(root.resolve()), 'Escaping manifest path')
        raw = p.read_bytes()
        require(len(raw) == e['bytes'] and digest(raw) == e['sha256'],
                'Style fingerprint mismatch: ' + e['path'])
    return m


def presentation_transform(old: str, name: str) -> str:
    """Precisely the preview's presentation edits; no free-form rewriting."""
    new = re.sub(r'\$\$(.*?)\$\$',
                 lambda m: '```math\n' + m[1].strip() + '\n```', old, flags=re.S)
    if name == 'README.md':
        for a, b in [('C2-cofinite', '$C_2$-cofinite'),
                     ('Let x and y be', 'Let $x$ and $y$ be'),
                     ('let f(x) be', 'let $f(x)$ be')]:
            require(new.count(a) == 1, 'Ambiguous README transformation: ' + a)
            new = new.replace(a, b)
    if name in NAV:
        head, rest = new.split('\n\n', 1)
        new = head + '\n\n' + NAV[name] + '\n\n' + rest
    if name == PROOFS[1]:
        pair = ('M-f(x_t)=\\frac{72d}{\\sqrt{141}}t^2+O(t^3),\\qquad\n'
                '\\|x_t-a\\|^2=dt^2+O(t^4).')
        split = ('M-f(x_t)=\\frac{72d}{\\sqrt{141}}t^2+O(t^3),\n```\n\n'
                 '```math\n\\|x_t-a\\|^2=dt^2+O(t^4).')
        require(new.count(pair) == 1, 'Missing paired Taylor display')
        new = new.replace(pair, split)
    return new


def check_preservation(root: Path, baseline: Path, m: dict) -> None:
    def git(*args: str, cwd: Path) -> str:
        return subprocess.check_output(['git', '-C', str(cwd), *args], text=True)
    require(git('rev-parse', 'HEAD', cwd=baseline).strip() == BASE,
            'Wrong pre-style baseline checkout')
    before = set(filter(None, git('ls-files', '-z', cwd=baseline).split('\0')))
    after = set(filter(None, git('ls-files', '-z', cwd=root).split('\0')))
    require(after-before == {e['path'] for e in m['added']} | {MANIFEST}
            and not before-after, 'Unexpected additions or deletions')
    changed = {e['path']: e for e in m['modified']}
    for name in sorted(before):
        old, new = (baseline/name).read_bytes(), (root/name).read_bytes()
        if name in changed:
            require(digest(old) == changed[name]['previous_sha256'],
                    'Previous fingerprint mismatch: ' + name)
        else:
            require(old == new, 'Unapproved change: ' + name)
    for name in PAGES:
        expected = presentation_transform((baseline/name).read_text(), name)
        require(expected == (root/name).read_text(),
                'Non-presentation content change: ' + name)
    old = json.loads((baseline/'snapshot_manifest.json').read_text())
    new = json.loads((root/'snapshot_manifest.json').read_text())
    old_records = {e['path']: e for e in old['files']}
    new_records = {e['path']: e for e in new['files']}
    require(list(old_records) == list(new_records), 'Snapshot membership/order drift')
    require({p for p in old_records if old_records[p] != new_records[p]} == {'README.md'},
            'Snapshot changed outside the README record')
    for e in new['files']:
        raw = (root/e['path']).read_bytes()
        require(len(raw) == e['bytes'] and digest(raw) == e['sha256'],
                'Current snapshot mismatch: ' + e['path'])


def expression(tex: str, display: bool, name: str) -> dict:
    require(bool(tex.strip()), 'Empty math: ' + name)
    require(not BAD_MACRO.search(tex), 'Unsupported macro: ' + name)
    require(not re.search(r'(?<!\\)\$', tex), 'Nested math delimiter: ' + name)
    depth = 0
    for brace in re.findall(r'(?<!\\)[{}]', tex):
        depth += 1 if brace == '{' else -1
        require(depth >= 0, 'Extra closing brace: ' + name)
    require(depth == 0, 'Missing closing brace: ' + name)
    return {'page': name, 'display': display, 'tex': tex.strip()}


def split_fences(text: str, name: str) -> list[tuple[str, str]]:
    """Extract math before ignoring code. Reject unclosed or mistyped fences."""
    parts, prose = [], []
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        start = OPEN_FENCE.fullmatch(lines[i].rstrip('\r\n'))
        if start is None:
            prose.append(lines[i]); i += 1; continue
        parts.append(('prose', ''.join(prose))); prose = []
        fence, language = start[1], start[2].strip()
        require(not language.lower().startswith('math') or language == 'math',
                'Ambiguous math-fence language: ' + name)
        i += 1
        body = []
        closer = re.compile(r'^ {0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}\s*$')
        while i < len(lines) and not closer.fullmatch(lines[i].rstrip('\r\n')):
            body.append(lines[i]); i += 1
        require(i < len(lines), 'Unclosed code/math fence: ' + name)
        parts.append(('math' if language == 'math' else 'code', ''.join(body)))
        i += 1
    parts.append(('prose', ''.join(prose)))
    return parts


def inspect_page(text: str, name: str, root: Path | None = None) -> list[dict]:
    require(not any(s.rstrip() != s for s in text.splitlines()), 'Trailing whitespace: ' + name)
    require(text.count('<details>') == text.count('</details>'), 'Unclosed details: ' + name)
    corpus, outside = [], []
    # Math alternatives precede code spans, including GitHub's $`...`$ syntax.
    tokens = re.compile(r'\$`([^`\n]*)`\$|\$\$(.*?)\$\$|(?<!\\)\$([^\n$]*?)(?<!\\)\$|(`+)(.*?)\4', re.S)
    for kind, value in split_fences(text, name):
        if kind == 'code':
            continue
        if kind == 'math':
            corpus.append(expression(value, True, name)); continue
        position = 0
        for t in tokens.finditer(value):
            outside.append(value[position:t.start()]); position = t.end()
            if t[4] is not None:
                continue
            tex = next(g for g in t.groups()[:3] if g is not None)
            corpus.append(expression(tex, t[2] is not None, name))
        outside.append(value[position:])
    prose = ''.join(outside)
    require(not re.search(r'(?<!\\)\$', prose), 'Unmatched dollar delimiter: ' + name)
    require(not BAD_MACRO.search(prose), 'Unformatted unsupported macro: ' + name)
    if name in PROOFS:
        require(not re.search(r'(?:sqrt\(|\b(?:epsilon|kappa|omega|Delta)\b|<=|>=)', prose),
                'Unformatted mathematics: ' + name)
    if root is not None:
        for link in re.findall(r'\[[^\]]+\]\(([^)\s]+)\)', prose):
            u = urlsplit(link)
            if u.scheme or u.netloc or not u.path:
                continue
            target = ((root/name).parent/unquote(u.path)).resolve()
            require(target.is_relative_to(root.resolve()) and target.is_file(),
                    'Broken local link: ' + name + ' -> ' + link)
    return corpus


def negative_controls() -> int:
    invalid = [r'\operatorname{dist}(x,A)', r'x=1\tag{1}',
               r'\frac{1}{2', r'\frac{1}{2}}', r'\newcommand{\x}{1}', '']
    tests = [f'```math\n{s}\n```' for s in invalid]
    tests += [f'$${s}$$' for s in invalid]
    tests += [r'$x=1', 'A bare sqrt(141) remains.', '```math\nx=1\n',
              '```math\nx=1\n~~~', '```Math\nx=1\n```',
              '```math\n$x$\n```', '```math extra\nx=1\n```',
              '```python\nx=1\n', r'$\frac{1}{2$']
    for s in tests:
        try:
            inspect_page(s, PROOFS[0])
        except RuntimeError:
            continue
        raise RuntimeError('Bad math accepted: ' + repr(s))
    return len(tests)


def positive_controls() -> int:
    examples = [
        ('```math\nx^2+1\n```', [(True, 'x^2+1')]),
        ('~~~math\nx=1\n~~~', [(True, 'x=1')]),
        ('$x$ then\n\n```math\ny=2\n```\n\n$z$', [(False,'x'), (True,'y=2'), (False,'z')]),
        ('```python\n"$bad" # \\operatorname{bad}\n```\n\n```math\nx=1\n```', [(True,'x=1')]),
        (r'`$bad \tag{1}` and $x$', [(False,'x')]),
        (r'Price \$5; $x$ and $`y_1`$', [(False,'x'), (False,'y_1')]),
        ('$$\nx=1\n$$', [(True,'x=1')]),
        ('````text\n```math\n$bad\n```\n````\n\n$x$', [(False,'x')]),
    ]
    for s, expected in examples:
        found = [(e['display'], e['tex']) for e in inspect_page(s, 'control.md')]
        require(found == expected, 'Fence/inline/code tokenization failed')
    return len(examples)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--export-math', type=Path)
    args = parser.parse_args()
    m = check_manifest(ROOT)
    paths = [ROOT/'README.md', *sorted((ROOT/'docs/learn').glob('*.md')),
             *(ROOT/p for p in PROOFS)]
    require(len(paths) == 10, 'Expected ten active pages')
    corpus = []
    for p in paths:
        name = str(p.relative_to(ROOT)); text = p.read_text()
        require(all('$$' not in value for kind,value in split_fences(text,name) if kind != 'code'),
                'Active displays must use math fences: ' + name)
        corpus.extend(inspect_page(text, name, ROOT))
    displays = sum(e['display'] for e in corpus)
    require(len(corpus) == 445 and displays == 80, 'Dropped or unexpected math expression')
    from verify_teaching import arithmetic, documents, LABELS
    LABELS.clear(); arithmetic(); documents(ROOT)
    nc, pc = negative_controls(), positive_controls()
    if args.baseline:
        check_preservation(ROOT, args.baseline.resolve(), m)
    if args.export_math:
        args.export_math.write_text(json.dumps(corpus, indent=2) + '\n')
    print(json.dumps({'status':'PASS fenced math and exact presentation delta',
                      'pages':len(paths),'math_expressions':len(corpus),
                      'display_equations':displays,'inline_expressions':len(corpus)-displays,
                      'negative_controls':nc,'positive_controls':pc,'teaching_checks':len(LABELS),
                      'baseline_comparison':args.baseline is not None,
                      'live_GitHub_render_verified':False,
                      'mathematical_proof_verified':False},indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
