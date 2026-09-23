#!/usr/bin/env python3
"""Check original license, archived seed and unchanged scientific payloads.

Standard-library checks only. This is provenance verification, not proof review.
"""
from pathlib import Path, PurePosixPath
from zipfile import ZipFile
import hashlib
import json


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def main():
    root = Path(__file__).resolve().parents[1]
    record = json.loads((root / "provenance/repository_import.json").read_text())
    license = (root / "LICENSE").read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(license)).encode() + b"\0" + license).hexdigest()
    need(blob == "e17a781bf47c4aadf18b68fc593846a1193b86c1", "Owner's original LICENSE changed")
    seed = root / record["seed_archive"]
    need(hashlib.sha256(seed.read_bytes()).hexdigest() ==
         "1124a6477e3a71d43c5af08134dcd5347e253ce6fdd57aa257c88992a72661c8",
         "Original seed ZIP changed")
    prefix = record["seed_prefix"]
    entries = {item["path"]: item for item in record["original_seed_files"]}
    need(len(entries) == len(record["original_seed_files"]), "Duplicate source record")
    checked = 0
    with ZipFile(seed) as z:
        names = z.namelist()
        need(len(names) == len(set(names)), "Duplicate seed ZIP member")
        files = [name for name in names if not name.endswith("/")]
        need(set(files) == {prefix + name for name in entries}, "Seed inventory mismatch")
        for name, item in entries.items():
            p = PurePosixPath(name)
            need(not p.is_absolute() and ".." not in p.parts, "Unsafe path")
            original = z.read(prefix + name)
            need(len(original) == item["bytes"] and
                 hashlib.sha256(original).hexdigest() == item["sha256"], "Bad source record: " + name)
            if item["unchanged_in_repository"]:
                need((root / name).read_bytes() == original, "Preserved scientific file changed: " + name)
                checked += 1
            else:
                need(name in record["changed_seed_paths"], "Undeclared changed path: " + name)
    print(json.dumps({"status": "PASS provenance checks only", "license_preserved": True,
                      "original_seed_preserved": True, "seed_files": len(entries),
                      "unchanged_seed_files": checked, "independent_proof_review": False},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
