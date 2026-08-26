#!/usr/bin/env python3
"""Balance the answer-key positions of a generated test by permuting the
options of non-Assertion-Reason questions so the correct answer is spread
roughly evenly across the four positions. Assertion-Reason questions (whose
options must stay in the fixed standard order) are left untouched.

Usage: python3 mock-tests/_balance.py <file.json>
"""
import json, sys

AR_OPTS = [
    "Both (A) and (R) are correct and (R) is the correct explanation of (A)",
    "Both (A) and (R) are correct but (R) is NOT the correct explanation of (A)",
    "(A) is correct but (R) is not correct",
    "(A) is not correct but (R) is correct",
]


def main():
    path = sys.argv[1]
    d = json.load(open(path))
    qs = d["questions"]

    counts = [0, 0, 0, 0]
    # First, tally fixed AR positions.
    for q in qs:
        if q["options"] == AR_OPTS:
            counts[q["options"].index(q["correctAnswer"])] += 1

    # Greedily place each non-AR correct answer at the least-used position.
    for q in qs:
        if q["options"] == AR_OPTS:
            continue
        opts = q["options"]
        correct = q["correctAnswer"]
        cur = opts.index(correct)
        target = min(range(4), key=lambda p: counts[p])
        if target != cur:
            opts[cur], opts[target] = opts[target], opts[cur]
        counts[target] += 1
        q["options"] = opts

    with open(path, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("Balanced answer positions:", {i + 1: c for i, c in enumerate(counts)})


if __name__ == "__main__":
    main()
