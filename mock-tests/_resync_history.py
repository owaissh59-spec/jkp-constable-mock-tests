#!/usr/bin/env python3
"""Rebuild the per-section history shards from the test files that actually exist.

The shards in `mock-tests/history/` store a fingerprint of every question ever
generated, and the generator reads them to guarantee it never repeats a stem.
That only works while the shards match the corpus. Whenever questions are
rewritten in place — as when off-syllabus items are replaced — the shards keep
fingerprinting text that is no longer there, so the generator both protects
deleted questions and fails to protect the new ones.

This rebuilds each shard from the current contents of `mock-tests/tests/`, using
the same `normalize_stem` and `extract_key_concept` helpers as `_record_test.py`
so the fingerprints are byte-for-byte what the recorder would have written.

    python3 mock-tests/_resync_history.py --dry-run   # report the differences
    python3 mock-tests/_resync_history.py             # rewrite the shards
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from _record_test import normalize_stem, extract_key_concept  # noqa: E402

SECTIONS = "ABCDE"
NAMES = {
    "A": "General English",
    "B": "General Knowledge & Current Affairs (India)",
    "C": "General Knowledge with special reference to J&K",
    "D": "Numerical and Reasoning Ability",
    "E": "Basic Concepts of Computers",
}


def test_number(path):
    m = re.match(r"(\d+)_test_", os.path.basename(path))
    return int(m.group(1)) if m else None


def build():
    shards = {s: [] for s in SECTIONS}
    files = sorted(glob.glob(os.path.join(HERE, "tests", "*.json")), key=lambda p: test_number(p) or 0)
    for path in files:
        n = test_number(path)
        if n is None:
            continue
        d = json.load(open(path))
        for q in d.get("questions", []):
            s = q.get("subject")
            if s not in shards:
                continue
            shards[s].append({
                "test": n,
                "stem": normalize_stem(q.get("questionText", "")),
                "key": extract_key_concept(q),
            })
    return shards


def main():
    dry = "--dry-run" in sys.argv
    fresh = build()
    for s in SECTIONS:
        path = os.path.join(HERE, "history", f"{s}.json")
        old = json.load(open(path)) if os.path.exists(path) else {"questions": []}
        old_q = old.get("questions", [])
        new_q = fresh[s]

        old_keys = {(e.get("test"), e.get("stem")) for e in old_q}
        new_keys = {(e.get("test"), e.get("stem")) for e in new_q}
        gone = len(old_keys - new_keys)
        added = len(new_keys - old_keys)

        print(f"  {s}.json: {len(old_q)} -> {len(new_q)} fingerprints "
              f"(stale removed {gone}, newly recorded {added})")
        if dry:
            continue
        out = {
            "subject": s,
            "subject_name": old.get("subject_name", NAMES[s]),
            "count": len(new_q),
            "questions": new_q,
        }
        with open(path, "w") as fh:
            json.dump(out, fh, indent=2, ensure_ascii=False)
    if dry:
        print("\n(dry run — nothing written)")


if __name__ == "__main__":
    main()
