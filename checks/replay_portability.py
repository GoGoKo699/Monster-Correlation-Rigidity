#!/usr/bin/env python3
"""Inspect replay portability without changing verify.py or recorded reports.

Only floating leaves in two named historical NumPy reports may differ, with
atol=rtol=5e-12. All structure, exact leaves, and other reports match exactly.
Scripts must pass their own original checks. Strict mismatches remain visible.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ATOL=5e-12
RTOL=5e-12
ALLOW={'prior average toy','prior pair toy'}


def need(ok: bool, message: str) -> None:
    if not ok: raise RuntimeError(message)


def compare(a, b, path='$') -> list[dict]:
    need(type(a) is type(b), 'Type difference at '+path)
    if isinstance(a,dict):
        need(a.keys()==b.keys(),'Key difference at '+path)
        return [v for k in a for v in compare(a[k],b[k],path+'.'+k)]
    if isinstance(a,list):
        need(len(a)==len(b),'Length difference at '+path)
        return [v for i,(x,y) in enumerate(zip(a,b)) for v in compare(x,y,path+f'[{i}]')]
    if isinstance(a,float):
        need(math.isfinite(a) and math.isfinite(b),'Nonfinite value at '+path)
        need(math.isclose(a,b,rel_tol=RTOL,abs_tol=ATOL),'Numeric discrepancy at '+path)
        return [] if a==b else [{'path':path,'recorded':a,'observed':b,'absolute_difference':abs(a-b)}]
    need(a==b,'Exact value difference at '+path)
    return []


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args(); root=args.root.resolve()
    spec=importlib.util.spec_from_file_location('preserved_verifier',root/'verify.py')
    need(spec is not None and spec.loader is not None,'Cannot load original verifier')
    v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
    v.check_manifest(root,'snapshot_manifest.json')
    subprocess.run([sys.executable,str(root/'checks/verify_repository_integrity.py')],
                   cwd=root,check=True,capture_output=True,timeout=20)
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    reports=[]
    with tempfile.TemporaryDirectory(prefix='monster_portability_') as tmp:
        tmp=Path(tmp)
        a=v.unpack(root/'provenance/Monster_Average_Transport_Checkpoint.zip',tmp/'a')
        g=v.unpack(root/'provenance/Monster_Global_Rounding_Checkpoint.zip',tmp/'g')
        p=v.unpack(root/'provenance/Monster_Bipartite_Correlations_Checkpoint.zip',tmp/'p')
        l=v.unpack(root/'provenance/Monster_Correlation_Local_Rigidity_Checkpoint.zip',tmp/'l')
        tasks=[(root,'checks/verify_normalizer.py','results/normalizer_exact.json','new exact'),
               (root,'checks/verify_normalizer_toy.py','results/normalizer_toy.json','new toy'),
               (a,'verify_average.py','verification_average.json','prior average exact'),
               (a,'verify_average_toy.py','verification_average_toy.json','prior average toy'),
               (g,'verify_global.py','verification_global.json','prior global exact'),
               (p,'verify_exact.py','verification_exact.json','prior pair exact'),
               (p,'verify_toy.py','verification_toy.json','prior pair toy'),
               (l,'verify_monster_local.py','verification.json','prior local exact')]
        for folder,script,expected,label in tasks:
            modes=[[],['-O'],['-OO']] if label.startswith('new ') else [[]]
            for mode in modes:
                result=subprocess.run([sys.executable,*mode,script],cwd=folder,env=env,capture_output=True,timeout=35)
                need(result.returncode==0,label+' original checks failed: '+result.stderr.decode(errors='replace'))
                original=(folder/expected).read_bytes(); exact=result.stdout==original
                differences=[]
                if not exact:
                    need(label in ALLOW,'Non-allowlisted strict mismatch: '+label)
                    differences=compare(json.loads(original),json.loads(result.stdout))
                reports.append({'label':label,'mode':mode or ['normal'],'byte_identical':exact,
                                'different_float_leaves':len(differences),
                                'max_absolute_difference':max((x['absolute_difference'] for x in differences),default=0),
                                'differences':differences})
    print(json.dumps({'status':'PASS under explicitly bounded portability comparison',
        'all_reports_byte_identical':all(r['byte_identical'] for r in reports),
        'absolute_tolerance':ATOL,'relative_tolerance':RTOL,
        'allowlisted_reports':sorted(ALLOW),'reports':reports,
        'original_evidence_modified':False},sort_keys=True,indent=2))

if __name__=='__main__': main()
