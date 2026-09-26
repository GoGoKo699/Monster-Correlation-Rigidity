#!/usr/bin/env python3
"""Read-only diagnostics on a separately pinned checkout; failures are findings."""
from __future__ import annotations
import argparse
import ast
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from urllib.parse import unquote, urlsplit
import zipfile
BASE = 'ecd0623e9de41b49754b6ca16dc23752443143af'
def sha(raw): return hashlib.sha256(raw).hexdigest()
def emit(kind, value): print(kind+' '+json.dumps(value,sort_keys=True),flush=True)
def git(root,*args): return subprocess.check_output(['git','-C',str(root),*args],text=True).strip()
def strip_code(text): return re.sub(r'(?ms)^([`~]{3,})[^\n]*\n.*?^\1\s*$', '', text)
def headings(text):
    counts=Counter(); result=set(re.findall(r'<a\s+(?:name|id)=[\"\']([^\"\']+)',text))
    for title in re.findall(r'^#{1,6}\s+(.+)$',strip_code(text),re.M):
        slug=re.sub(r'[^\w\- ]','',title.strip().lower()).replace(' ','-')
        count=counts[slug]; counts[slug]+=1
        result.add(slug+('-'+str(count) if count else ''))
    return result

def static(root,names):
    failures=[]
    for name in names:
        try:
            if name.endswith('.py'): ast.parse((root/name).read_text(),filename=name)
            elif name.endswith('.json'): json.loads((root/name).read_text())
        except (SyntaxError,ValueError,UnicodeError) as exc: failures.append({'path':name,'error':str(exc)})
    emit('SYNTAX',{'python':sum(n.endswith('.py') for n in names),'json':sum(n.endswith('.json') for n in names),'failures':failures})
    archives=[]
    for name in names:
        if name.endswith('.zip'):
            with zipfile.ZipFile(root/name) as z:
                archives.append({'path':name,'sha256':sha((root/name).read_bytes()),'entries':len(z.infolist()),'first_crc_failure':z.testzip()})
    emit('ARCHIVES',archives)
    manifests=[]
    for name in ['snapshot_manifest.json','results/quantitative_core_additions.json','results/final_core_integration.json','results/physics_teaching_manifest.json','results/math_rendering_changes.json','results/hopf_style_changes.json']:
        m=json.loads((root/name).read_text()); entries=m.get('files',m.get('modified',[])+m.get('added',[])); mismatches=[]
        for e in entries:
            if 'path' not in e or 'sha256' not in e: continue
            p=root/e['path']
            if not p.is_file() or sha(p.read_bytes())!=e['sha256']: mismatches.append(e['path'])
        manifests.append({'path':name,'entries':len(entries),'current_tree_mismatches':mismatches})
    emit('MANIFESTS',manifests)
    broken=[]; anchors=[]; refs=[]; macros=[]; conflict=[]; link_count=0
    for name in names:
        if not name.endswith('.md'): continue
        text=(root/name).read_text(); prose=strip_code(text)
        if re.search(r'^(?:<<<<<<< |=======\s*$|>>>>>>> )',text,re.M): conflict.append(name)
        for number,line in enumerate(text.splitlines(),1):
            if re.search(r'\\(?:operatorname|tag|newcommand|renewcommand)\b',line): macros.append({'path':name,'line':number})
            for literal in re.findall(r'(?:research/|checks/)[\w/.-]+\.(?:md|py)',line):
                if not (root/literal).is_file(): refs.append({'path':name,'line':number,'missing_literal':literal})
        for match in re.finditer(r'\[[^\]\n]+\]\(([^)\s]+)\)',prose):
            url=match.group(1); u=urlsplit(url)
            if u.scheme or u.netloc: continue
            link_count+=1
            target=((root/name).parent/unquote(u.path)).resolve() if u.path else (root/name).resolve()
            row={'path':name,'target':url}
            if not target.is_relative_to(root) or not target.exists(): broken.append(row)
            elif u.fragment and target.suffix=='.md' and unquote(u.fragment) not in headings(target.read_text()): anchors.append(row)
    emit('LINKS',{'relative_links':link_count,'broken_targets':broken,'anchor_candidates_manual_review':anchors})
    emit('MISSING_PATH_LITERALS',refs); emit('RENDERING_MACRO_OCCURRENCES',macros); emit('CONFLICT_MARKERS',conflict)
    emit('RELEASE_FILES',{p:(root/p).is_file() for p in ['LICENSE','requirements.txt','CITATION.cff','llms.txt','CHANGELOG.md','docs/RESEARCH_STATUS.md','docs/learn/README.md']})
    emit('INVENTORY',names)

def scripts(root,out):
    paths=['verify.py',*[str(p.relative_to(root)) for p in sorted((root/'checks').glob('*.py'))]]
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1'); results=[]
    for name in paths:
        modes=[]
        for opt in ([],['-O'],['-OO']):
            start=time.monotonic()
            try:
                p=subprocess.run([sys.executable,*opt,name],cwd=root,env=env,capture_output=True,timeout=90)
                stdout,stderr,code=p.stdout,p.stderr,p.returncode
            except subprocess.TimeoutExpired as exc: stdout,stderr,code=exc.stdout or b'',exc.stderr or b'',124
            label=opt[0] if opt else 'normal'; dest=out/(Path(name).stem+'_'+label.replace('-',''))
            dest.with_suffix('.out').write_bytes(stdout); dest.with_suffix('.err').write_bytes(stderr)
            row={'mode':label,'returncode':code,'stdout_sha256':sha(stdout),'seconds':round(time.monotonic()-start,2)}
            try:
                report=json.loads(stdout); row['report_status']=report.get('status')
                for key in ('checks','pages','math_expressions','display_equations','inline_expressions','negative_controls','positive_controls','teaching_checks','all_reports_byte_identical'):
                    if key in report: row[key]=report[key]
                if name.endswith('replay_portability.py'): row['different_float_leaves']=sum(r['different_float_leaves'] for r in report['reports'])
            except (ValueError,AttributeError,TypeError): pass
            if code: row['stderr_tail']=stderr.decode(errors='replace')[-1600:]
            modes.append(row)
        record={'script':name,'modes':modes,'stdout_identical_in_three_modes':len({r['stdout_sha256'] for r in modes})==1}
        results.append(record); emit('SCRIPT',record)
    reference=json.loads((root/'results/quantitative_core_reports.json').read_text())['reports']
    reference+=json.loads((root/'results/final_core_integration.json').read_text())['new_reports']
    for row in reference:
        actual=next(r for r in results if r['script']==row['script'])
        emit('EXACT_SAVED_REPORT',{'script':row['script'],'expected_checks':row['checks'],'all_modes_match':all(r['returncode']==0 and r['stdout_sha256']==row['sha256'] for r in actual['modes'])})
    return results

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',type=Path,required=True); p.add_argument('--output',type=Path,required=True); args=p.parse_args()
    root,out=args.root.resolve(),args.output.resolve()
    if git(root,'rev-parse','HEAD')!=BASE: raise RuntimeError('Wrong audit baseline')
    names=list(filter(None,git(root,'ls-files','-z').split('\0')))
    before={n:sha((root/n).read_bytes()) for n in names}; out.mkdir(parents=True,exist_ok=True)
    emit('BASELINE',{'commit':BASE,'tree':git(root,'rev-parse','HEAD^{tree}'),'initial_status':git(root,'status','--porcelain'),'tracked_files':len(names),'python':sys.version,'numpy':__import__('numpy').__version__})
    static(root,names); results=scripts(root,out); after={n:sha((root/n).read_bytes()) for n in names}
    emit('FINAL',{'baseline_unchanged':before==after,'git_status':git(root,'status','--porcelain'),'script_count':len(results),'script_executions':3*len(results),'nonzero_scripts':[r['script'] for r in results if any(m['returncode'] for m in r['modes'])],'mode_mismatches':[r['script'] for r in results if not r['stdout_identical_in_three_modes']],'mathematical_theorems_verified_by_code':False})
    (out/'summary.json').write_text(json.dumps(results,indent=2)+'\n')
    if before!=after: raise RuntimeError('Audit altered baseline source bytes')
if __name__=='__main__': main()
