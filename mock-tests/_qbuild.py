#!/usr/bin/env python3
"""Shared builder for Section A test files, with every ruleset invariant asserted.

Authoring 200 grammar questions by hand and *also* hitting the prescribed type
mix, a 25%-per-position answer key, a spread of Assertion-Reason relationships
and a rotated statement false-item is not something to attempt unaided. This
module takes plain content declarations and refuses to write the file unless all
of it holds.

Usage from a content script:

    from _qbuild import Q, AR, emit

    q = Q()
    q.single("stem", ["opt", ...], "correct opt", "explanation")
    q.statement("stem with (i)..(iv) on their own lines", [...], "correct", "expl")
    q.ar("Assertion text", "Reason text", 1, "expl")      # 0..3 relationship
    q.matching("stem with Column I/II", [...], "correct", "expl")
    q.multi("Which of the following are ...", [...], "correct", "expl")
    q.blank("stem containing __________", [...], "correct", "expl")

    emit(q, subject="A", topic="...", path="mock-tests/tests/61_test_A_....json")

What is enforced
----------------
* type mix matches the steering prompt's table for N, with the Numerical and
  Data-Interpretation shares folded into Single Correct, which Section 1 of the
  ruleset explicitly permits for General English
* the correct answer lands on each of the four positions as evenly as N allows;
  Assertion-Reason items keep the four mandated options in fixed order, so they
  contribute whatever their relationship dictates and the rest compensate
* Assertion-Reason relationships are spread, never all "R explains A"
* statement items rotate which numbered item is the false one
* explanations are at least 180 characters and never name an option by position
* no question uses a format the Constable syllabus omits for Section A
"""
import collections
import json
import os
import re

AR = [
    "Both (A) and (R) are correct and (R) is the correct explanation of (A)",
    "Both (A) and (R) are correct but (R) is NOT the correct explanation of (A)",
    "(A) is correct but (R) is not correct",
    "(A) is not correct but (R) is correct",
]

AR_STEM = "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R)."

ROMANS = ["(i)", "(ii)", "(iii)", "(iv)"]
ROMAN_RX = re.compile(r"\((?:i{1,3}|iv)\)")

# Section A type mix once Numerical and DI are folded into Single Correct.
MIX = {
    30: {"S": 15, "ST": 5, "AR": 3, "M": 3, "MC": 3, "FB": 1},
    40: {"S": 20, "ST": 6, "AR": 4, "M": 4, "MC": 4, "FB": 2},
    50: {"S": 25, "ST": 8, "AR": 5, "M": 5, "MC": 5, "FB": 2},
}

FORBIDDEN = {
    "comprehension passage": r"read the following passage|read the passage|according to the passage",
    "narration": r"(?:in)?to indirect speech|(?:in)?to direct speech|reported speech",
    "voice": r"(?:in)?to passive voice|(?:in)?to active voice|rewrite in the passive",
    "spot the error": r"spot the error|find the error in",
    "one-word substitution": r"one word for ['\"]|one-word substitution",
    "cloze / jumble": r"\bcloze\b|para.?jumble|rearrange the (?:following )?(?:sentences|parts)",
}
FORBIDDEN = {k: re.compile(v, re.I) for k, v in FORBIDDEN.items()}

ORDINAL = re.compile(r"\bthe (first|second|third|fourth|last) option\b", re.I)


class Q:
    """Accumulates questions, tagged by type."""

    def __init__(self):
        self.items = []

    def _add(self, t, text, opts, ans, expl):
        self.items.append(dict(t=t, text=text, opts=list(opts), ans=ans, expl=expl))

    def single(self, text, opts, ans, expl):
        self._add("S", text, opts, ans, expl)

    def blank(self, text, opts, ans, expl):
        assert "__________" in text, "fill-in-the-blank needs a __________ marker"
        self._add("FB", text, opts, ans, expl)

    def statement(self, text, opts, ans, expl):
        assert text.lower().startswith("consider the following statement"), \
            "statement items must open with 'Consider the following statements'"
        self._add("ST", text, opts, ans, expl)

    def multi(self, text, opts, ans, expl):
        assert re.match(r"which of the following (are|is/are)", text.lower()), \
            "multiple-correct items must open with 'Which of the following are/is/are'"
        self._add("MC", text, opts, ans, expl)

    def matching(self, text, opts, ans, expl):
        assert "Column I" in text, "matching items need Column I / Column II"
        for lab in ("(a)", "(b)", "(c)", "(d)"):
            assert f"\n{lab}" in text, f"matching item {lab} must sit on its own line"
        self._add("M", text, opts, ans, expl)

    def ar(self, assertion, reason, rel, expl):
        assert rel in (0, 1, 2, 3), "relationship must be 0-3"
        text = f"{AR_STEM}\n\nAssertion (A): {assertion}\nReason (R): {reason}\n\nChoose the correct option:"
        self._add("AR", text, AR, AR[rel], expl)


def _interleave(items):
    """Reorder so question types are spread through the paper, not grouped.

    The ruleset requires types to be interspersed; declaring all the single-answer
    items together and all the matching items together would otherwise leave a run
    of fifteen identical types. Greedily takes from whichever type has most items
    left, never repeating the previous type while an alternative exists.
    """
    buckets = collections.OrderedDict()
    for it in items:
        buckets.setdefault(it["t"], []).append(it)

    out = []
    prev = None
    while any(buckets.values()):
        avail = [t for t, v in buckets.items() if v]
        choices = [t for t in avail if t != prev] or avail
        pick = max(choices, key=lambda t: len(buckets[t]))
        out.append(buckets[pick].pop(0))
        prev = pick

    run = worst = 0
    last = None
    for it in out:
        run = run + 1 if it["t"] == last else 1
        last = it["t"]
        worst = max(worst, run)
    assert worst <= 4, f"type run of {worst} after interleaving"
    return out


def _assign_positions(items):
    """Place each non-AR answer so every position is used as evenly as possible."""
    n = len(items)
    base, rem = divmod(n, 4)
    target = {p: base + (1 if p < rem else 0) for p in range(4)}

    fixed = collections.Counter()
    free = []
    for i, it in enumerate(items):
        if it["t"] == "AR":
            fixed[it["opts"].index(it["ans"])] += 1
        else:
            free.append(i)

    plan = []
    for p in range(4):
        plan += [p] * max(0, target[p] - fixed[p])
    while len(plan) < len(free):
        plan.append(min(range(4), key=lambda p: plan.count(p) + fixed[p]))
    plan = plan[:len(free)]
    plan.sort()
    # interleave so equal targets are not clustered together in the paper
    plan = [plan[i] for i in sorted(range(len(plan)), key=lambda k: (k % 4, k // 4))]

    for slot, qi in enumerate(free):
        it = items[qi]
        want = plan[slot]
        opts = list(it["opts"])
        ai = opts.index(it["ans"])
        opts.insert(want, opts.pop(ai))
        assert opts.index(it["ans"]) == want
        assert sorted(opts) == sorted(it["opts"])
        it["opts"] = opts


def _false_item(it):
    """Which numbered item a statement/multiple-correct answer leaves out."""
    a = it["ans"].strip()
    if a.lower().startswith("all of the above"):
        return None
    sel = set(ROMAN_RX.findall(a))
    if len(sel) != 3:
        return None
    return (set(ROMANS) - sel).pop()


def emit(q, subject, topic, path, quiet=False):
    items = q.items
    n = len(items)
    assert n in MIX, f"no type mix defined for N={n}"

    counts = collections.Counter(it["t"] for it in items)
    assert dict(counts) == MIX[n], f"type mix {dict(counts)} != prescribed {MIX[n]}"

    # Assertion-Reason relationships must be spread
    rels = collections.Counter(it["opts"].index(it["ans"]) for it in items if it["t"] == "AR")
    assert len(rels) >= min(3, MIX[n]["AR"]), \
        f"A-R relationships too concentrated: {dict(rels)} — vary A and R content"
    assert max(rels.values()) <= (MIX[n]["AR"] + 2) // 2 + 1, \
        f"one A-R relationship dominates: {dict(rels)}"

    # statement / multiple-correct false-item rotation
    fi = collections.Counter(_false_item(it) for it in items if it["t"] in ("ST", "MC"))
    fi.pop(None, None)
    if sum(fi.values()) >= 4:
        assert len(fi) >= 3, f"the false item barely rotates: {dict(fi)}"
        assert max(fi.values()) <= sum(fi.values()) // 2 + 1, \
            f"one position is the false item too often: {dict(fi)}"

    items = _interleave(items)
    _assign_positions(items)

    seen = set()
    for i, it in enumerate(items, 1):
        assert len(it["opts"]) == 4, f"q{i}: needs exactly 4 options"
        assert len(set(it["opts"])) == 4, f"q{i}: duplicate options"
        assert it["ans"] in it["opts"], f"q{i}: answer not among options"
        assert len(it["expl"]) >= 180, f"q{i}: explanation only {len(it['expl'])} chars"
        assert not ORDINAL.search(it["expl"]), f"q{i}: explanation names an option by position"
        assert "|--" not in it["text"] and "|--" not in it["expl"], f"q{i}: markdown table"
        blob = it["text"] + " " + " ".join(it["opts"])
        for label, rx in FORBIDDEN.items():
            assert not rx.search(blob), f"q{i}: uses {label}, which the syllabus omits for Section A"
        # Key on the question's own wording, not on shared scaffolding: every
        # Assertion-Reason item opens with the same mandated sentence, so keying
        # on the raw opening would flag all of them as duplicates of each other.
        body = it["text"].replace(AR_STEM, "")
        body = re.sub(r"choose the correct (option|match)\s*:?", "", body, flags=re.I)
        key = re.sub(r"\W+", " ", body.lower()).strip()[:90]
        assert key not in seen, f"q{i}: duplicate stem — {key[:60]!r}"
        seen.add(key)
        if it["t"] == "AR":
            assert it["opts"] == AR, f"q{i}: A-R options must stay in the mandated order"

    pos = collections.Counter(it["opts"].index(it["ans"]) + 1 for it in items)
    assert max(pos.values()) - min(pos.values()) <= 3, f"answer key unbalanced: {dict(pos)}"
    assert len(pos) == 4, f"answer key misses a position: {dict(pos)}"

    out = {
        "subject": subject,
        "topic": topic,
        "total_questions": n,
        "questions": [
            {
                "id": str(i),
                "subject": subject,
                "questionText": it["text"],
                "options": it["opts"],
                "correctAnswer": it["ans"],
                "explanation": it["expl"],
            }
            for i, it in enumerate(items, 1)
        ],
    }
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    if not quiet:
        print(f"wrote {os.path.basename(path)}  N={n}")
        print(f"   types      : {dict(counts)}")
        print(f"   answer key : {dict(sorted(pos.items()))}")
        print(f"   A-R rels   : {dict(sorted(rels.items()))}")
        print(f"   false item : {dict(fi)}")
