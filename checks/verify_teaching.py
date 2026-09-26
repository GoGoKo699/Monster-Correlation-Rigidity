#!/usr/bin/env python3
"""Check the physics teaching layer, not the imported VOA theorems.

Uses only the standard library. --baseline additionally checks the complete
tracked-file delta against the frozen pre-teaching commit in a real checkout.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

BASE = 'a7ccd55cc729bb1643c668ec6d2085363b17096b'
MANIFEST = 'results/physics_teaching_manifest.json'
MODIFIED = {'README.md', 'snapshot_manifest.json',
            '.github/workflows/quantitative-core-review.yml'}
ROOT = Path(__file__).resolve().parents[1]
LABELS: list[str] = []


def need(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)
    LABELS.append(label)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fingerprint(root: Path, entry: dict) -> None:
    path = (root / entry['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        raise RuntimeError('Manifest path escapes checkout')
    raw = path.read_bytes()
    need(len(raw) == entry['bytes'] and sha(raw) == entry['sha256'],
         'fingerprint:' + entry['path'])


def arithmetic() -> None:
    need(Q(1,256)**2 == Q(1,32768)/2, 'arithmetic:field_radius')
    total = Q(1,128) + 2*Q(1,256)
    need(total == Q(1,64) and total < Q(3,188), 'arithmetic:passing_budget')
    need(Q(1,64)+2*Q(1,256) == Q(3,128) > Q(3,188),
         'arithmetic:inconclusive_budget')
    need(Q(47,192)*total == Q(47,12288), 'arithmetic:Ising_overlap')
    need(Q(1,256)-Q(47,12288) == Q(1,12288), 'arithmetic:strict_margin')
    need(Q(47,192)*Q(3,188) == Q(1,256), 'arithmetic:gap_conversion')
    need(Q(1,4)-2*Q(1,48)*Q(1,4)+12*Q(1,48)**2 == Q(47,192),
         'arithmetic:primary_norm')
    centered_cross = -2*Q(1,48)*Q(1,4)+12*Q(1,48)**2
    need(centered_cross/Q(47,192) == -Q(1,47), 'arithmetic:negative_overlap')
    need(Q(141,24**2) == Q(47,192), 'arithmetic:axis_scale')
    need(12-12**2/Q(12) == 0, 'arithmetic:pure_stress_not_normalizable')
    need(Q(16)-Q(12)**2/12 == 4, 'arithmetic:shifted_field_norm')
    # Algebraic identity in a formal cubic value F, not a simulated VOA.
    for F in (Q(-1,3), Q(0), Q(2), Q(17,5)):
        q = 8*F+48
        need((q-Q(12)*16/2+Q(12)**3/36)/8 == F,
             'arithmetic:stress_correction:' + str(F))
    need(2-1-1 == 0 and 2-0-1 == 1, 'arithmetic:mode_index_shift')


def documents(root: Path) -> None:
    pages = sorted((root/'docs/learn').glob('*.md'))
    need(len(pages) == 7, 'documents:seven_learning_pages')
    lessons = [p for p in pages if re.match(r'0[1-5]_', p.name)]
    need(len(lessons) == 5, 'documents:five_sequential_lessons')
    for path in [root/'README.md', *pages]:
        text = path.read_text()
        label = str(path.relative_to(root))
        need(not any(line.rstrip()!=line for line in text.splitlines()),
             'whitespace:' + label)
        need(text.count('```') % 2 == 0, 'code_fences:' + label)
        need(text.count('<details>') == text.count('</details>'),
             'details:' + label)
        stripped = re.sub(r'```.*?```', '', text, flags=re.S)
        stripped = re.sub(r'`[^`]*`', '', stripped)
        blocks = re.findall(r'\$\$(.*?)\$\$', stripped, flags=re.S)
        inline_text = re.sub(r'\$\$.*?\$\$', '', stripped, flags=re.S)
        need(len(re.findall(r'(?<!\\)\$', inline_text)) % 2 == 0,
             'math_delimiters:' + label)
        blocks += re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$', inline_text)
        for expression in blocks:
            depth=0
            for brace in re.findall(r'(?<!\\)[{}]', expression):
                depth += 1 if brace=='{' else -1
                if depth < 0:
                    raise RuntimeError('Unbalanced math braces: ' + label)
            if depth:
                raise RuntimeError('Unbalanced math braces: ' + label)
        need(True, 'math_braces:' + label)
        need(not any(token in text for token in ('\\operatorname', '\\tag{',
                                                 '\\begin{align}', '\\newcommand')),
             'math_compatibility_guard:' + label)
        for link in re.findall(r'\[[^\]]+\]\(([^)\s]+)\)', text):
            u = urlsplit(link)
            if u.scheme or u.netloc:
                continue
            target = (path.parent/unquote(u.path)).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                raise RuntimeError('Missing or escaping local link: ' + label + ' -> ' + link)
        need(True, 'local_links:' + label)
    for page in lessons:
        text=page.read_text()
        need('**1.**' in text and '**2.**' in text and
             'Answers and explanations' in text, 'self_checks:' + page.name)
    guide=(root/'docs/learn/README.md').read_text()
    need('**Primary anchor:** Matthias R. Gaberdiel' in guide and
         '**Secondary anchor:** Hiroshi Yamauchi' in guide,
         'anchors:physics_first_order')
    need('a second prerequisite course' in guide, 'anchors:secondary_is_supplement')
    need('1/12288' in (root/'docs/learn/05_worked_certificate.md').read_text(),
         'example:exact_margin_present')


def preservation(root: Path, baseline: Path, manifest: dict) -> None:
    revision=subprocess.check_output(['git','-C',str(baseline),'rev-parse','HEAD'],text=True).strip()
    need(revision == BASE, 'preservation:frozen_baseline_commit')
    def tracked(directory: Path) -> set[str]:
        return set(filter(None, subprocess.check_output(
            ['git','-C',str(directory),'ls-files','-z']).decode().split('\0')))
    old_names,new_names=tracked(baseline),tracked(root)
    changed={e['path']:e for e in manifest['modified']}
    additions={e['path'] for e in manifest['added']}
    need(set(changed)==MODIFIED, 'preservation:exact_modified_allowlist')
    need(new_names-old_names == additions|{MANIFEST} and not old_names-new_names,
         'preservation:exact_additions_and_no_deletions')
    for name in sorted(old_names):
        old,new=(baseline/name).read_bytes(),(root/name).read_bytes()
        if name in changed:
            if sha(old)!=changed[name]['previous_sha256']:
                raise RuntimeError('Previous hash mismatch: '+name)
        elif old!=new:
            raise RuntimeError('Unapproved baseline change: '+name)
    need(True, 'preservation:all_other_baseline_bytes_identical')
    old={e['path']:e for e in json.loads((baseline/'snapshot_manifest.json').read_text())['files']}
    new={e['path']:e for e in json.loads((root/'snapshot_manifest.json').read_text())['files']}
    need(set(old)==set(new) and {p for p in old if old[p]!=new[p]}=={'README.md'},
         'preservation:snapshot_only_readme_record_changed')
    previous=(baseline/'README.md').read_text()
    current=(root/'README.md').read_text()
    start=current.index("## Start here: a physicist's reading path")
    end=current.index('## The selected result')
    need(current[:start]+current[end:]==previous,
         'preservation:readme_existing_science_unchanged')


def main() -> None:
    # The historical teaching manifest remains frozen at its original commit.
    # The current display manifest explicitly covers subsequent reader changes.
    if (ROOT/'results/math_rendering_changes.json').is_file():
        from verify_display import main as current_display_check
        current_display_check()
        return
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',type=Path)
    args=parser.parse_args()
    manifest=json.loads((ROOT/MANIFEST).read_text())
    need(manifest['base_commit']==BASE, 'manifest:baseline')
    need({e['path'] for e in manifest['modified']}==MODIFIED,
         'manifest:modified_allowlist')
    entries=manifest['modified']+manifest['added']
    need(len({e['path'] for e in entries})==len(entries) and
         MANIFEST not in {e['path'] for e in entries}, 'manifest:unique_self_excluded')
    for entry in entries:
        fingerprint(ROOT,entry)
    arithmetic()
    documents(ROOT)
    if args.baseline is not None:
        preservation(ROOT,args.baseline.resolve(),manifest)
    print(json.dumps({'status':'PASS teaching arithmetic, links, and source fingerprints',
                      'checks':len(LABELS),'labels':LABELS,
                      'baseline_comparison':args.baseline is not None,
                      'imported_theorems_verified':False,
                      'full_VOA_simulated':False},indent=2,sort_keys=True))

if __name__=='__main__':
    main()
