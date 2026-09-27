#!/usr/bin/env python3
"""Validate the active reader package, not live browser rendering or VOA axioms."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from release_integrity import ROOT, MANIFEST, verify_files, require
from verify_display import inspect_page, split_fences, negative_controls, positive_controls


def corpus_for(root: Path, pages: list[str]) -> list[dict]:
    corpus = []
    for name in pages:
        text = (root / name).read_text()
        require(all('$$' not in s for kind, s in split_fences(text, name) if kind != 'code'),
                'Active displays must use math fences: ' + name)
        corpus.extend(inspect_page(text, name, root))
    return corpus


def corpus_digest(corpus: list[dict]) -> str:
    data = json.dumps(corpus, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(data).hexdigest()


def all_links(root: Path) -> int:
    count = 0
    for path in sorted(root.rglob('*.md')):
        if any(x in path.relative_to(root).parts for x in ('.git', '.venv', 'node_modules')):
            continue
        # This file-level scan includes historical pages without rewriting them.
        text = '\n'.join(s for kind, s in split_fences(path.read_text(), str(path)) if kind == 'prose')
        for link in re.findall(r'\[[^\]]+\]\(([^)\s]+)\)', text):
            u = urlsplit(link)
            if u.scheme or u.netloc or not u.path:
                continue
            target = (path.parent / unquote(u.path)).resolve()
            require(target.is_relative_to(root.resolve()) and target.is_file(),
                    'Broken repository link: ' + str(path.relative_to(root)) + ' -> ' + link)
            count += 1
    return count


def metadata(root: Path) -> None:
    # Structural checks only; this is not an implementation of the full CFF schema.
    cff = (root / 'CITATION.cff').read_text()
    for field in ('cff-version: 1.2.0', 'authors:', 'title:', 'repository-code:', 'license: MIT'):
        require(field in cff, 'Missing citation field: ' + field)
    require('doi:' not in cff and 'date-released:' not in cff, 'Unissued DOI/release date in citation')
    about = json.loads((root / '.github/repository_metadata.json').read_text())
    require(0 < len(about['description']) <= 350, 'Invalid About description')
    require(0 < len(about['topics']) <= 20 and len(set(about['topics'])) == len(about['topics']),
            'Invalid or duplicate topics')
    require(all(re.fullmatch(r'[a-z0-9-]{1,50}', t) for t in about['topics']), 'Invalid topic syntax')
    require('numpy==2.3.5' in (root / 'requirements-reproduce.txt').read_text(), 'Missing reproduction pin')
    require('## Unreleased' in (root / 'CHANGELOG.md').read_text(), 'Missing unreleased changelog')
    source_map = (root / 'llms.txt').read_text()
    require('Gaberdiel' in source_map and 'Yamauchi' in source_map, 'Teaching anchors not retained')
    for p in ('STATUS_CURRENT.md', 'PHYSICS_STATUS.md'):
        require((root / p).read_text().startswith('> **Historical record'), 'Missing historical banner')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--export-math', type=Path)
    args = parser.parse_args()
    integrity = verify_files(baseline=args.baseline)
    m = json.loads((ROOT / MANIFEST).read_text())
    corpus = corpus_for(ROOT, m['active_pages'])
    expected = m['math_corpus']
    require(len(corpus) == expected['expressions'] and
            sum(e['display'] for e in corpus) == expected['display_equations'] and
            corpus_digest(corpus) == expected['sha256'], 'Unexpected or omitted mathematics')
    from verify_teaching import arithmetic, documents, LABELS
    LABELS.clear(); arithmetic(); documents(ROOT)
    nc, pc = negative_controls(), positive_controls()
    links = all_links(ROOT)
    metadata(ROOT)
    if args.export_math:
        require(not args.export_math.resolve().is_relative_to(ROOT.resolve()),
                'Export mathematics outside the checkout')
        args.export_math.write_text(json.dumps(corpus, indent=2) + '\n')
    print(json.dumps({'status': 'PASS current release package and active math',
                      'pages': len(m['active_pages']), 'math_expressions': len(corpus),
                      'display_equations': sum(e['display'] for e in corpus),
                      'negative_controls': nc, 'positive_controls': pc,
                      'teaching_checks': len(LABELS), 'relative_links': links,
                      'integrity': integrity, 'live_GitHub_render_verified': False,
                      'full_CFF_schema_validation': False}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
