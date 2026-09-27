"""Transfer a hash-pinned local patch into Git objects, never branch refs.

This temporary helper is not part of the candidate. The compressed segments
are transport data for a textual git diff, not executable archives. After
applying the exact diff, run current checks before uploading any Git objects.
No commits, branches, repository settings, tags or releases are changed here.
"""
from __future__ import annotations
import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from urllib.request import Request, urlopen
import zlib

BASE = 'ecd0623e9de41b49754b6ca16dc23752443143af'
BASE_TREE = '20c5252c0bd5e83d6a908ee226e5799e947280fc'
PATCH = '987b2a3d4fb60760889bb2a628d4c353bb0ea9e759e88f6c455633dcf3b5930c'
TREE = '0ef739f1af81a333f27061cdc957ec2c52ec6c33'
REPO = 'GoGoKo699/Monster-Correlation-Rigidity'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def post(endpoint: str, payload: dict) -> dict:
    # Only Git-object writes are allowed by this helper. No ref/settings API.
    need(endpoint in ('blobs', 'trees'), 'Not an object-store endpoint')
    request = Request('https://api.github.com/repos/' + REPO + '/git/' + endpoint,
                      data=json.dumps(payload).encode(), method='POST',
                      headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
                               'Accept': 'application/vnd.github+json',
                               'Content-Type': 'application/json',
                               'X-GitHub-Api-Version': '2022-11-28'})
    with urlopen(request, timeout=45) as response:
        return json.load(response)


def main() -> None:
    root = Path('subject').resolve()
    baseline = Path('base').resolve()
    need(git(root, 'rev-parse', 'HEAD') == BASE, 'Wrong starting commit')
    need(git(root, 'write-tree') == BASE_TREE, 'Wrong starting tree')
    need(not git(root, 'status', '--porcelain'), 'Subject not clean')
    parts = sorted(Path(__file__).resolve().parent.glob('*.part'))
    need(len(parts) == 11, 'Missing transport segment')
    raw = zlib.decompress(b''.join(p.read_bytes() for p in parts))
    need(len(raw) == 137361 and hashlib.sha256(raw).hexdigest() == PATCH,
         'Patch transport hash mismatch')
    patch = Path(os.environ['RUNNER_TEMP']) / 'release-preparation.patch'
    patch.write_bytes(raw)
    subprocess.run(['git', '-C', str(root), 'apply', '--check', str(patch)], check=True)
    subprocess.run(['git', '-C', str(root), 'apply', str(patch)], check=True)
    subprocess.run(['git', '-C', str(root), 'add', '.'], check=True)
    actual = git(root, 'write-tree')
    print('CANDIDATE_TREE', actual, flush=True)
    need(actual == TREE, 'Candidate differs from reviewed local files')
    subprocess.run([sys.executable, 'verify_current.py', '--baseline', str(baseline),
                    '--output', os.environ['RUNNER_TEMP'] + '/current-checks'],
                   cwd=root, check=True, timeout=300)
    need(git(root, 'write-tree') == TREE and not git(root, 'diff'),
         'Source changed during current checks')
    names = git(root, 'diff', '--cached', '--name-only', BASE).splitlines()
    need(len(names) == 33, 'Wrong change count')
    entries = []
    for name in names:
        path = root / name
        need(path.is_file() and not path.is_symlink(), 'Unexpected file kind')
        data = path.read_bytes()
        expected = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        result = post('blobs', {'content': base64.b64encode(data).decode(), 'encoding': 'base64'})
        need(result['sha'] == expected, 'Uploaded blob mismatch: ' + name)
        entries.append({'path': name, 'mode': '100644', 'type': 'blob', 'sha': expected})
        print('VERIFIED_BLOB', name, expected, flush=True)
    result = post('trees', {'base_tree': BASE_TREE, 'tree': entries})
    need(result['sha'] == TREE, 'Remote tree mismatch')
    print('PUBLISHED_CANDIDATE_TREE', TREE, flush=True)
    print('No commits, refs, settings, tags or releases were changed by this helper.', flush=True)


if __name__ == '__main__':
    main()
