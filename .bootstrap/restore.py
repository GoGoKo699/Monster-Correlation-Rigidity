"""One-shot, hash-checked import; never writes main or replaces LICENSE."""
import base64
import hashlib
import io
import json
import lzma
from pathlib import Path, PurePosixPath
import shutil
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path.cwd()
EXPECTED = '0af097c7d97921cdcb9f19bc9c216c6ae176673de1bbb6fb6a859b986b0f3df7'


def need(ok, msg):
    if not ok:
        raise RuntimeError(msg)


def digest(b):
    return hashlib.sha256(b).hexdigest()


license = (ROOT / 'LICENSE').read_bytes()
need(hashlib.sha1(b'blob ' + str(len(license)).encode() + b'\0' + license).hexdigest()
     == 'e17a781bf47c4aadf18b68fc593846a1193b86c1', 'License mismatch')
parts = [ROOT / f'.bootstrap/part{j:02d}' for j in range(7)]
packed = b''.join(p.read_bytes() for p in parts)
need(digest(packed) == EXPECTED, 'Transport hash mismatch')
data = json.loads(lzma.decompress(packed))
cache = {}
active = set()


def build(h):
    if h in cache:
        return cache[h]
    need(h not in active, 'Cyclic transport')
    active.add(h)
    if h in data['pool']:
        b = data['pool'][h].encode('utf-8')
    else:
        spec = data['zips'][h]
        out = io.BytesIO()
        with ZipFile(out, 'w', compression=ZIP_DEFLATED, compresslevel=spec['level']) as z:
            z.comment = base64.b64decode(spec['comment'])
            for r in spec['entries']:
                info = ZipInfo(r['filename'], tuple(r['date_time']))
                for key, value in r.items():
                    if key in ['h', 'filename', 'date_time']:
                        continue
                    setattr(info, key, base64.b64decode(value) if key in ['comment', 'extra'] else value)
                z.writestr(info, build(r['h']), compresslevel=spec['level'])
        b = out.getvalue()
    need(digest(b) == h, 'Reconstructed source hash mismatch: ' + h)
    active.remove(h)
    cache[h] = b
    return b


need(len(data['files']) == 33, 'Unexpected final file count')
outputs = {}
for name, h in data['files'].items():
    path = PurePosixPath(name)
    need(not path.is_absolute() and '..' not in path.parts and '.git' not in path.parts,
         'Unsafe output path')
    need(not name.startswith(('.bootstrap/', '.github/')), 'Unexpected infrastructure output')
    outputs[name] = build(h)
need(outputs['LICENSE'] == license, 'Attempted license replacement')
for name, b in outputs.items():
    if name == 'LICENSE':
        continue
    p = ROOT / name
    need(not p.exists(), 'Refusing to overwrite: ' + name)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b)
    p.chmod(0o644)
# Delete only the known disposable transport and one-shot workflow.
shutil.rmtree(ROOT / '.bootstrap')
(ROOT / '.github/workflows/import-seed.yml').unlink()
print('Restored 33 hash-checked files; original MIT license unchanged.')
