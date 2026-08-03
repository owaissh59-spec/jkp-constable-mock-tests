#!/usr/bin/env python3
"""Self-check helper (Section 6 of the steering prompt).

Usage: python3 mock-tests/_validate.py <file.json>

Exits 1 and lists every failure found. Run this BEFORE _record_test.py.
"""
import json, sys, collections, os, re

SUBJECTS = "ABCDE"
BLUEPRINT = {"A": 25, "B": 25, "C": 10, "D": 25, "E": 15}   # out of 100

AR_OPTS = [
    "Both (A) and (R) are correct and (R) is the correct explanation of (A)",
    "Both (A) and (R) are correct but (R) is NOT the correct explanation of (A)",
    "(A) is correct but (R) is not correct",
    "(A) is not correct but (R) is correct",
]

SHARED_PREAMBLES = (
    "read the following",
    "study the following",
    "consider the following table",
    "the following table",
    "the table below",
)


def qtype(q):
    t = q["questionText"]
    if q["options"] == AR_OPTS:
        return "AssertionReason"
    if "Column I" in t or "List I" in t:
        return "Matching"
    # Data-interpretation sets embed a table/preamble and may contain a blank
    # marker; they are not fill-in-the-blank items.
    if t.lower().startswith(SHARED_PREAMBLES):
        return "Single/Numerical/DI"
    if t.lower().startswith("consider the following statement"):
        return "Statement"
    if re.match(r"which of the following (are|is/are|is classified|are classified)", t.lower()):
        return "MultipleCorrect"
    if "__________" in t:
        return "FillBlank"
    return "Single/Numerical/DI"


def expected_ratio(n):
    """Subject-wise counts for a mixed/full test of n questions (largest-remainder)."""
    raw = {s: n * BLUEPRINT[s] / 100 for s in SUBJECTS}
    base = {s: int(raw[s]) for s in SUBJECTS}
    left = n - sum(base.values())
    for s in sorted(SUBJECTS, key=lambda x: raw[x] - base[x], reverse=True)[:left]:
        base[s] += 1
    return base


def main():
    path = sys.argv[1]
    d = json.load(open(path))
    qs = d["questions"]
    errs = []
    warns = []
    print(f"== {os.path.basename(path)} | subject={d['subject']} | declared={d['total_questions']} | actual={len(qs)}")
    if d["total_questions"] != len(qs):
        errs.append("total_questions mismatch")

    ids = [q["id"] for q in qs]
    if ids != [str(i + 1) for i in range(len(qs))]:
        errs.append("ids not sequential 1..N")

    types = collections.Counter()
    pos = collections.Counter()
    subj = collections.Counter()
    for q in qs:
        types[qtype(q)] += 1
        subj[q.get("subject", "?")] += 1
        if q.get("subject") not in SUBJECTS:
            errs.append(f"q{q['id']}: subject '{q.get('subject')}' not in A-E")
        if len(q["options"]) != 4:
            errs.append(f"q{q['id']}: not 4 options")
        if len(set(q["options"])) != 4:
            errs.append(f"q{q['id']}: duplicate options")
        if q["correctAnswer"] not in q["options"]:
            errs.append(f"q{q['id']}: correctAnswer not in options")
        else:
            pos[q["options"].index(q["correctAnswer"]) + 1] += 1
        if len(q.get("explanation", "")) < 180:
            errs.append(f"q{q['id']}: explanation too short ({len(q.get('explanation',''))} chars)")
        if qtype(q) == "Matching":
            t = q["questionText"]
            for lab in ["(a)", "(b)", "(c)", "(d)"]:
                if f"\n{lab}" not in t:
                    errs.append(f"q{q['id']}: matching item {lab} not on own line")
        if "Assertion (A):" in q["questionText"] and q["options"] != AR_OPTS:
            errs.append(f"q{q['id']}: A-R without the 4 standard options")
        # General English (A) has no comprehension/cloze/jumble items in the
        # Constable syllabus.
        if q.get("subject") == "A" and q["questionText"].lower().startswith("read the following passage"):
            errs.append(f"q{q['id']}: comprehension passage in section A (not in Constable syllabus)")

    print("  types:", dict(types))
    print("  sections:", dict(sorted(subj.items())))
    print("  answer positions:", dict(sorted(pos.items())))
    if not pos or max(pos.values()) - min(pos.values()) > 3 or len(pos) < 4:
        errs.append(f"answer key not balanced: {dict(sorted(pos.items()))}")

    # Mixed / full test: subject spread must follow the 25:25:10:25:15 blueprint.
    if len(subj) > 1:
        exp = expected_ratio(len(qs))
        print("  expected sections:", exp)
        for s in SUBJECTS:
            if abs(subj.get(s, 0) - exp[s]) > 1:
                errs.append(f"section {s}: {subj.get(s, 0)} questions, expected ~{exp[s]}")

    # grouping check: no more than 3 consecutive questions of the same type
    run, prev, worst = 0, None, 0
    for q in qs:
        t = qtype(q)
        run = run + 1 if t == prev else 1
        prev = t
        worst = max(worst, run)
    print(f"  longest same-type run: {worst}")
    if worst > 4:
        warns.append(f"{worst} consecutive questions of the same type — intersperse more")

    if warns:
        print("  WARNINGS:")
        for w in warns:
            print("   -", w)
    if errs:
        print("  FAILURES:")
        for e in errs:
            print("   -", e)
        sys.exit(1)
    print("  OK")


if __name__ == "__main__":
    main()
