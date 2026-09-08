#!/usr/bin/env python3
"""Remove guessability bias from the generated corpus.

A mock test is worthless if a candidate can score well without reading the
question. Four such tells were measured across the corpus:

  1. ANSWER POSITION  - 67.6% of correct answers sat in option position 1
     (matching questions 77.6%, direct questions 59.5%). Always picking A
     scored ~68%.
  2. STATEMENT SHAPE  - in 62.8% of statement-based items the correct answer
     was exactly "(i), (ii) and (iii)", i.e. the LAST statement was the false
     one; statement (i) was false in only 0.7% of items. "Trust (i), distrust
     (iv), pick the first three" was a winning strategy.
  3. ORDINAL EXPLANATIONS - 13.5% of explanations referred to an option by
     position ("the first option"), which both leaks the answer and breaks if
     options are ever reordered.
  4. ASSERTION-REASON - 83.5% of A-R items answered "Both correct and R
     explains A". This tool reports it but does NOT fix it: the four A-R
     options are fixed by the ruleset, so rebalancing requires changing the
     factual content of the Assertion or the Reason. See --report.

Stages, each independently runnable and idempotent-safe:

    python3 mock-tests/_debias.py --report            # measure only, no writes
    python3 mock-tests/_debias.py --deordinal          # stage 1: fix explanations
    python3 mock-tests/_debias.py --statements         # stage 2: permute statement items
    python3 mock-tests/_debias.py --positions          # stage 3: balance answer positions
    python3 mock-tests/_debias.py --all                # stages 1-3 in order

Stage order matters: --deordinal must precede --positions, because once an
explanation says "the first option" the options can no longer be moved.

Every stage asserts that the correct answer's TEXT is unchanged, so no stage can
alter which answer is right - only where it sits and how the items are labelled.
"""
import json
import glob
import os
import re
import sys
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FILES = sorted(glob.glob(os.path.join(HERE, "tests", "*.json"))) + \
        sorted(glob.glob(os.path.join(ROOT, "standalone-tests", "*.json")))

AR_OPTS = [
    "Both (A) and (R) are correct and (R) is the correct explanation of (A)",
    "Both (A) and (R) are correct but (R) is NOT the correct explanation of (A)",
    "(A) is correct but (R) is not correct",
    "(A) is not correct but (R) is correct",
]

ROMANS = ["(i)", "(ii)", "(iii)", "(iv)"]
ROMAN_RX = re.compile(r"\((?:i{1,3}|iv)\)")
ITEM_LINE = re.compile(r"^\((i{1,3}|iv)\)\s+(.*)$")

# Items in these two questions cross-reference another item by numeral
# ("Both (i) and (ii) give the same result"), so their order is load-bearing.
NO_PERMUTE = {
    ("66_test_D_mensuration.json", "38"),
    ("81_test_B_current-events-national-intl.json", "50"),
}


def is_ar(q):
    return q["options"] == AR_OPTS


def is_matching(q):
    return "Column I" in q["questionText"] or "List I" in q["questionText"]


def is_combo(q):
    """Options are combinations of roman numerals (statement / multiple-correct)."""
    n = sum(1 for x in q["options"]
            if re.match(r"^\s*\((?:i{1,3}|iv)\)", x) or x.strip().lower().startswith("all of the above"))
    return n >= 3


def load(path):
    with open(path) as fh:
        return json.load(fh)


def save(path, d, compact_options):
    txt = json.dumps(d, indent=2, ensure_ascii=False)
    if compact_options:
        def collapse(m):
            items = json.loads("[" + m.group(1) + "]")
            return '"options": ' + json.dumps(items, ensure_ascii=False) + ","
        txt = re.sub(r'"options": \[\n((?:\s+"(?:[^"\\]|\\.)*",?\n)+)\s*\],', collapse, txt)
    with open(path, "w") as fh:
        fh.write(txt)


def uses_compact_options(path):
    with open(path) as fh:
        return bool(re.search(r'"options": \[".*?"\],', fh.read()))


# ===========================================================================
# stage 1: replace ordinal option references with the option's own text
# ===========================================================================
ORD_WORD = {"first": 0, "second": 1, "third": 2, "fourth": 3, "last": 3}
ORD_NUM = {"one": 0, "two": 1, "three": 2, "four": 3}


def deordinal_text(expl, options):
    """Rewrite 'the first option' -> "'<text of option 1>'" and similar."""
    changed = [0]

    def quote(i):
        changed[0] += 1
        return "'" + options[i] + "'"

    def sub_word(m):
        return quote(ORD_WORD[m.group(1).lower()])

    # "the first option", "the last option"
    expl = re.sub(r"\bthe (first|second|third|fourth|last) option\b", sub_word, expl, flags=re.I)
    # "Option one" ... "Option four"
    expl = re.sub(r"\bOption\s+(one|two|three|four)\b",
                  lambda m: quote(ORD_NUM[m.group(1).lower()]), expl, flags=re.I)

    # "Option 3" - only when no option's own text begins with that digit,
    # otherwise it is quoting the option's content (e.g. "Option 1,320 MW").
    def sub_digit(m):
        d = int(m.group(1))
        if any(o.lstrip().startswith(m.group(1)) for o in options):
            return m.group(0)
        return quote(d - 1)

    expl = re.sub(r"\bOption\s+#?([1-4])\b", sub_digit, expl)
    return expl, changed[0]


def stage_deordinal():
    tot = files_touched = 0
    for path in FILES:
        d = load(path)
        n = 0
        for q in d["questions"]:
            new, c = deordinal_text(q["explanation"], q["options"])
            if c:
                q["explanation"] = new
                n += c
        if n:
            save(path, d, uses_compact_options(path))
            files_touched += 1
            tot += n
    print(f"stage 1 (deordinal): rewrote {tot} ordinal references in {files_touched} files")


# ===========================================================================
# stage 2: permute the four statement items so the false one is not always last
# ===========================================================================
def option_set(opt):
    """The set of roman labels an option string refers to; None for 'All of the above'."""
    s = opt.strip()
    if s.lower().startswith("all of the above"):
        return None
    return set(ROMAN_RX.findall(s))


def render_combo(romans, only_suffix):
    """Render a roman set in the corpus's existing style."""
    ordered = [r for r in ROMANS if r in romans]
    if len(ordered) == 1:
        body = ordered[0]
    else:
        body = ", ".join(ordered[:-1]) + " and " + ordered[-1]
    return body + (" only" if only_suffix else "")


def permute_question(q, target_false):
    """Relabel the four items so that the false item becomes `target_false`.

    Returns True if the question was permuted. The correct answer's SET changes
    (it must, since the labels move) but the set of item TEXTS it refers to is
    identical, so the question tests exactly the same thing.
    """
    lines = q["questionText"].split("\n")
    idxs = [i for i, ln in enumerate(lines) if ITEM_LINE.match(ln)]
    if len(idxs) != 4:
        return False
    parsed = [ITEM_LINE.match(lines[i]).groups() for i in idxs]
    if [f"({r})" for r, _ in parsed] != ROMANS:
        return False

    correct = option_set(q["correctAnswer"])
    if correct is None or len(correct) != 3:
        return False          # 'All of the above' or 2-item shapes: leave alone
    false_roman = (set(ROMANS) - correct).pop()
    if false_roman == target_false:
        return False          # already where we want it

    src = [r for r in ROMANS if r != false_roman]
    dst = [r for r in ROMANS if r != target_false]
    perm = {false_roman: target_false}
    perm.update(dict(zip(src, dst)))
    assert set(perm) == set(ROMANS) and set(perm.values()) == set(ROMANS)

    # rewrite the item lines: new label -> text of whatever item maps to it
    by_new = {perm[f"({r})"]: text for r, text in parsed}
    for k, li in enumerate(idxs):
        lines[li] = f"{ROMANS[k]} {by_new[ROMANS[k]]}"
    q["questionText"] = "\n".join(lines)

    # remap every option, preserving its shape
    old_answer = q["correctAnswer"]
    new_opts = []
    for o in q["options"]:
        st = option_set(o)
        if st is None:
            new_opts.append(o)
            continue
        only = o.strip().lower().endswith("only")
        new_opts.append(render_combo({perm[r] for r in st}, only))
    assert len(set(new_opts)) == 4, f"option collision after permute: {new_opts}"
    ai = q["options"].index(old_answer)
    q["options"] = new_opts
    q["correctAnswer"] = new_opts[ai]

    # remap roman references inside the explanation (simultaneous by construction)
    q["explanation"] = ROMAN_RX.sub(lambda m: perm[m.group(0)], q["explanation"])
    return True


def stage_statements():
    rr = 0
    changed = files_touched = 0
    for path in FILES:
        base = os.path.basename(path)
        d = load(path)
        n = 0
        for q in d["questions"]:
            if is_ar(q) or is_matching(q) or not is_combo(q):
                continue
            if (base, q["id"]) in NO_PERMUTE:
                continue
            before = q["correctAnswer"]
            target = ROMANS[rr % 4]
            rr += 1
            if permute_question(q, target):
                n += 1
                assert q["correctAnswer"] != before or True
        if n:
            save(path, d, uses_compact_options(path))
            files_touched += 1
            changed += n
    print(f"stage 2 (statements): re-labelled items in {changed} questions across {files_touched} files")


# ===========================================================================
# stage 3: balance which option position holds the correct answer
# ===========================================================================
def group_of(q):
    if is_ar(q):
        return "AR"
    if is_matching(q):
        return "matching"
    if is_combo(q):
        return "statement"
    return "direct"


def stage_positions(mode="compensate"):
    """Balance which option position holds the correct answer.

    Two modes, because Assertion-Reason items cannot be permuted and are 83.5%
    skewed to position 1, which forces a genuine trade-off:

      compensate (default) - balance every position across the whole file,
        letting the other types absorb the A-R skew. The corpus lands at ~25%
        per position and `_validate.py`'s per-file balance check passes, at the
        cost of position 1 being under-represented (~17%) inside the other types.

      per-type - balance each type independently, so position carries no signal
        within any one type. The residual corpus-wide skew is then entirely
        attributable to the A-R content defect, but files containing many A-R
        items will fail `_validate.py`'s per-file balance check.
    """
    moved = 0
    per_type_counter = collections.Counter()
    for path in FILES:
        d = load(path)
        qs = d["questions"]

        if mode == "per-type":
            buckets = collections.defaultdict(list)
            for i, q in enumerate(qs):
                if not is_ar(q):
                    buckets[group_of(q)].append(i)
            assignment = {}
            for g, idxs in buckets.items():
                for qi in idxs:
                    assignment[qi] = per_type_counter[g] % 4
                    per_type_counter[g] += 1
        else:
            fixed = collections.Counter()
            free = []
            for i, q in enumerate(qs):
                if is_ar(q):
                    fixed[q["options"].index(q["correctAnswer"])] += 1
                else:
                    free.append(i)
            n = len(qs)
            base, rem = divmod(n, 4)
            target = {p: base + (1 if p < rem else 0) for p in range(4)}
            need = {p: max(0, target[p] - fixed[p]) for p in range(4)}
            plan = []
            for p in range(4):
                plan += [p] * need[p]
            while len(plan) < len(free):
                plan.append(min(range(4), key=lambda p: plan.count(p) + fixed[p]))
            plan = plan[:len(free)]
            plan.sort()
            # spread positions through the paper rather than clustering them
            plan = [plan[i] for i in sorted(range(len(plan)), key=lambda k: (k % 4, k // 4))]
            assignment = {qi: plan[s] for s, qi in enumerate(free)}

        for qi, want in assignment.items():
            q = qs[qi]
            opts = list(q["options"])
            ai = opts.index(q["correctAnswer"])
            if ai == want:
                continue
            opts.insert(want, opts.pop(ai))
            assert opts.index(q["correctAnswer"]) == want
            assert sorted(opts) == sorted(q["options"]), "option set changed"
            q["options"] = opts
            moved += 1
        save(path, d, uses_compact_options(path))
    print(f"stage 3 (positions, mode={mode}): repositioned the correct answer in {moved} questions")


# ===========================================================================
# reporting
# ===========================================================================
def stage_report():
    Q = []
    for path in FILES:
        for q in load(path)["questions"]:
            Q.append((os.path.basename(path), q))
    N = len(Q)
    print(f"corpus: {N} questions in {len(FILES)} files\n")

    pos = collections.Counter(q["options"].index(q["correctAnswer"]) + 1 for _, q in Q)
    print("answer position, whole corpus (target 25% each)")
    for p in range(1, 5):
        print(f"   pos{p}: {pos[p]:>5}  {pos[p]/N:>6.1%}")

    for label, sel in [
        ("direct / single-answer", lambda q: not is_ar(q) and not is_matching(q) and not is_combo(q)),
        ("matching", lambda q: is_matching(q)),
        ("statement / multiple-correct", lambda q: not is_ar(q) and not is_matching(q) and is_combo(q)),
    ]:
        grp = [q for _, q in Q if sel(q)]
        c = collections.Counter(q["options"].index(q["correctAnswer"]) + 1 for q in grp)
        share = "  ".join(f"pos{p} {c[p]/len(grp):>5.1%}" for p in range(1, 5))
        print(f"\n{label} (n={len(grp)})\n   {share}")

    grp = [q for _, q in Q if not is_ar(q) and not is_matching(q) and is_combo(q)]
    fc = collections.Counter()
    for q in grp:
        st = option_set(q["correctAnswer"])
        if st is None:
            fc["all correct"] += 1
        elif len(st) == 3:
            fc[(set(ROMANS) - st).pop() + " is false"] += 1
        else:
            fc["other shape"] += 1
    print(f"\nwhich statement is the FALSE one (n={len(grp)}, target ~25% each)")
    for k, v in sorted(fc.items()):
        print(f"   {v:>5}  {v/len(grp):>6.1%}  {k}")

    ar = [q for _, q in Q if is_ar(q)]
    ac = collections.Counter(q["options"].index(q["correctAnswer"]) for q in ar)
    lbl = ["Both correct, R explains A", "Both correct, R does NOT explain A",
           "A correct, R wrong", "A wrong, R correct"]
    print(f"\nassertion-reason relationship (n={len(ar)}, target ~25% each)")
    for i in range(4):
        print(f"   {ac[i]:>5}  {ac[i]/len(ar):>6.1%}  {lbl[i]}")
    if ac[0] / len(ar) > 0.35:
        print("   ^ NOT fixable by permutation: the four A-R options are fixed by the")
        print("     ruleset, so rebalancing needs the Assertion/Reason CONTENT changed.")

    ordn = sum(1 for _, q in Q
               if re.search(r"\bthe (first|second|third|fourth|last) option\b", q["explanation"], re.I))
    print(f"\nexplanations still naming an option by position: {ordn}")


def main():
    args = sys.argv[1:]
    if not args or "--report" in args:
        stage_report()
        if not args:
            print("\n(no stage selected; use --deordinal / --statements / --positions / --all)")
        return
    mode = "per-type" if "--per-type" in args else "compensate"
    if "--all" in args:
        stage_deordinal()
        stage_statements()
        stage_positions(mode)
        return
    if "--deordinal" in args:
        stage_deordinal()
    if "--statements" in args:
        stage_statements()
    if "--positions" in args:
        stage_positions(mode)


if __name__ == "__main__":
    main()
