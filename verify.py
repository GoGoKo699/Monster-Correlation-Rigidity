#!/usr/bin/env python3
"""Verify this recorded seed without modifying source or recorded outputs.

Tests run in temporary copies and remain active under optimized Python. The
owner's LICENSE and original seed are checked before the scientific replays.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile


def need(ok: bool, label: str) -> None:
    if not ok: raise RuntimeError(label)


def checked_path(root: Path, relative: str) -> Path:
    p=Path(relative)
    need(not p.is_absolute() and '..' not in p.parts,'Unsafe path: '+relative)
    out=root/p
    need(out.resolve().is_relative_to(root.resolve()),'Escaping path: '+relative)
    need(not out.is_symlink(),'Unexpected symbolic link: '+relative)
    return out


def check_manifest(root: Path, name: str) -> int:
    data=json.loads((root/name).read_text())
    seen=set()
    for item in data['files']:
        need(item['path'] not in seen,'Duplicate manifest entry')
        seen.add(item['path']); p=checked_path(root,item['path']); raw=p.read_bytes()
        need(len(raw)==item['bytes'],'Length mismatch: '+str(p))
        need(hashlib.sha256(raw).hexdigest()==item['sha256'],'Hash mismatch: '+str(p))
    return len(seen)


def unpack(source: Path,target: Path) -> Path:
    target.mkdir()
    with ZipFile(source) as z:
        names=set()
        for member in z.infolist():
            p=Path(member.filename)
            need(not p.is_absolute() and '..' not in p.parts,'Unsafe ZIP path')
            need(member.filename not in names,'Duplicate ZIP member')
            names.add(member.filename)
            need((member.external_attr>>16)&0o170000!=0o120000,'ZIP symlink not allowed')
        z.extractall(target)
    entries=list(target.iterdir())
    root=entries[0] if len(entries)==1 and entries[0].is_dir() else target
    if (root/'manifest.json').exists(): check_manifest(root,'manifest.json')
    return root


def replay(root: Path, script: str, expected: Path, label: str) -> dict:
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
             PYTHONDONTWRITEBYTECODE='1')
    old=expected.read_bytes(); modes=[]
    flags=[None,'-O','-OO'] if label.startswith('new ') else [None]
    for flag in flags:
        cmd=[sys.executable]+([flag] if flag else [])+[script]
        print('Checking '+label+' ['+(flag or 'normal')+']', file=sys.stderr, flush=True)
        result=subprocess.run(cmd,cwd=root,env=env,capture_output=True,timeout=35)
        need(result.returncode==0,label+' failed: '+result.stderr.decode(errors='replace'))
        need(result.stdout==old,label+' differs from recorded report under '+str(flag))
        modes.append({'mode':flag or 'normal','byte_identical':True,'exit_code':0})
    return {'label':label,'sha256':hashlib.sha256(old).hexdigest(),'modes':modes}


def main() -> None:
    root=Path(__file__).resolve().parent
    check_manifest(root,'snapshot_manifest.json')
    integrity=subprocess.run([sys.executable,str(root/'checks'/'verify_repository_integrity.py')],
        cwd=root,capture_output=True,timeout=15)
    need(integrity.returncode==0,'Repository integrity failed: '+integrity.stderr.decode(errors='replace'))
    print('Checking original license and seed integrity',file=sys.stderr,flush=True)
    imported=json.loads((root/'provenance'/'import_manifest.json').read_text())
    for item in imported['files']:
        p=checked_path(root,item['path']); raw=p.read_bytes()
        need(len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],
             'Preserved import changed: '+str(p))
    with tempfile.TemporaryDirectory(prefix='monster_normalizer_verify_') as tmp:
        tmp=Path(tmp)
        current=tmp/'current'; shutil.copytree(root,current,
            ignore=shutil.ignore_patterns('.git','__pycache__','.venv'))
        tasks=[(current,'checks/verify_normalizer.py',current/'results'/'normalizer_exact.json',
                'new exact scalar and character checks'),
               (current,'checks/verify_normalizer_toy.py',current/'results'/'normalizer_toy.json',
                'new small normalizer and tensor checks')]
        archives={}
        for stem in ['Monster_Average_Transport','Monster_Global_Rounding',
                     'Monster_Bipartite_Correlations','Monster_Correlation_Local_Rigidity']:
            archives[stem]=unpack(root/'provenance'/(stem+'_Checkpoint.zip'),tmp/stem)
        avg=archives['Monster_Average_Transport']; glob=archives['Monster_Global_Rounding']
        pair=archives['Monster_Bipartite_Correlations']; local=archives['Monster_Correlation_Local_Rigidity']
        need((avg/'previous'/'Monster_Global_Rounding_Checkpoint.zip').read_bytes()==
             (root/'provenance'/'Monster_Global_Rounding_Checkpoint.zip').read_bytes(),
             'Nested global archive differs from retained copy')
        need((glob/'previous'/'Monster_Bipartite_Correlations_Checkpoint.zip').read_bytes()==
             (root/'provenance'/'Monster_Bipartite_Correlations_Checkpoint.zip').read_bytes(),
             'Nested pair archive differs from retained copy')
        for name in ['verify_monster_local.py','verification.json','Monster_Correlation_Local_Rigidity.md']:
            need((pair/'previous'/name).read_bytes()==(local/name).read_bytes(),
                 'Nested local checkpoint differs: '+name)
        tasks += [(avg,'verify_average.py',avg/'verification_average.json','prior average exact'),
                  (avg,'verify_average_toy.py',avg/'verification_average_toy.json','prior average toy'),
                  (glob,'verify_global.py',glob/'verification_global.json','prior global exact'),
                  (pair,'verify_exact.py',pair/'verification_exact.json','prior pair exact'),
                  (pair,'verify_toy.py',pair/'verification_toy.json','prior pair toy'),
                  (local,'verify_monster_local.py',local/'verification.json','prior local exact')]
        reports=[replay(*t) for t in tasks]
    print(json.dumps({'status':'PASS within declared computational scopes',
                      'snapshot_hashes_valid':True,'preserved_imports_valid':True,
                      'scientific_verifiers':8,'new_verifier_execution_modes':3,'prior_verifier_execution_modes':1,
                      'total_successful_replays':12,'reports':reports,
                      'independent_proof_review':False,'full_monster_simulation':False,
                      'novelty_established':False},sort_keys=True,indent=2))

if __name__=='__main__': main()
