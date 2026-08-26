#!/usr/bin/env python3
"""Duplicate detector: compares a generated test file's question stems against
the existing subject history shards (exact + near-duplicate via token overlap).

Usage: python3 mock-tests/_dupcheck.py <file.json>
Exits 1 if any exact or high-overlap near-duplicate is found.
"""
import json, sys, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MT = os.path.join(ROOT, "mock-tests")

SHARED_PREAMBLES = (
    "read the following", "study the following", "consider the following table",
    "the following table", "the table below",
)


def normalize_stem(text, word_count=12):
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    if lines and lines[0].lower().startswith(SHARED_PREAMBLES):
        words = lines[-1].split()[:word_count]
    else:
        words = text.replace("\n", " ").split()[:word_count]
    return " ".join(words).lower().strip()


STOP = set("""a an the of to in on at for and or is are was were be been being with
by from as that this these those which who whom whose what how when where why
following statements statement consider given below two one labeled assertion
reason choose correct option options select combination match matching column
list fill blank word words sentence complete completing meaning most nearly
opposite similar synonym antonym which of the following are is/are classified
value find next term series what number should come correct answer his her its
question a b c d i ii iii iv v then if it he she they you we i.e e.g etc""".split())


def tokens(s):
    return set(re.findall(r"[a-z0-9]+", s.lower())) - STOP


def main():
    path = sys.argv[1]
    d = json.load(open(path))
    qs = d["questions"]
    subject = d.get("subject", "")

    # Determine which shards to load
    subs = set(q.get("subject") for q in qs)
    shard_stems = {}
    for s in subs:
        sp = os.path.join(MT, "history", f"{s}.json")
        if not os.path.exists(sp):
            continue
        data = json.load(open(sp))
        shard_stems[s] = [(x.get("stem", ""), tokens(x.get("stem", "")),
                           (x.get("key", "") or "").strip().lower())
                          for x in data["questions"]]

    AR_STEM = "given below are two statements, one labeled as assertion"

    problems = []
    # also check intra-file duplicates (ignore Assertion-Reason, which share a
    # mandated identical stem by design)
    seen = {}
    for q in qs:
        s = q.get("subject")
        stem = normalize_stem(q.get("questionText", ""))
        qtok = tokens(stem)
        qkey = (q.get("correctAnswer", "") or "").strip().lower()
        # Combo-style answers (matching/statement/multiple-correct) are shared by
        # many unrelated questions, so they are not a distinctive duplicate signal.
        combo = bool(re.search(r"\(i\)|\(a\)-|\bonly\b|\band\b.*\(", qkey)) or "-(i" in qkey
        is_ar = stem.startswith(AR_STEM)
        # intra-file
        if not is_ar:
            if stem in seen:
                problems.append(f"q{q['id']}: intra-file duplicate stem with q{seen[stem]}")
            seen[stem] = q["id"]
        if is_ar:
            continue
        # against shard: a true duplicate = very high stem overlap (near-identical
        # wording), OR moderate stem overlap AND the same answer/key.
        for hstem, htok, hkey in shard_stems.get(s, []):
            if not (qtok and htok):
                continue
            overlap = len(qtok & htok) / max(len(qtok), len(htok))
            same_key = qkey and hkey and qkey == hkey and not combo
            if (overlap >= 0.85 and len(qtok) >= 5) or (overlap >= 0.6 and same_key):
                tag = "same-answer" if same_key else "near-identical"
                problems.append(f"q{q['id']} [{s}]: {tag} dup ({overlap:.0%}) -> '{hstem}' [key={hkey}]")
                break

    if problems:
        print("DUPLICATE ISSUES FOUND:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print(f"OK - no duplicates ({len(qs)} questions checked against shards {sorted(shard_stems)})")


if __name__ == "__main__":
    main()
