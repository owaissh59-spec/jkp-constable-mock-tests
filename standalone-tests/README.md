# Standalone tests

Topical tests that sit **outside** the plan-driven 70-day series in `mock-tests/tests/`.

Because they are not part of the plan:

- `_record_test.py` is **not** run for them, so `mock-tests/config.json` counters,
  `mock-tests/manifest.json` and the `mock-tests/history/` shards stay untouched.
- They are numbered by topic, not by test number.

They still obey the full generation ruleset in
`.kiro/steering/mock-test-prompt-constable.md`, and both quality gates apply:

```bash
python3 mock-tests/_validate.py   standalone-tests/<file>.json
python3 mock-tests/_audit_scope.py standalone-tests/<file>.json
```

## Contents

### `unesco-world-heritage-sites-india_40q.json` — 40 Q, section B

UNESCO World Heritage Sites **in India**, treated as the syllabus item
*"Famous Places in India"*.

**Scope.** Every one of the 40 questions is about sites in India. Questions about
UNESCO *the agency* — its Paris headquarters, its mandate, the Kalinga Prize —
belong to the separate syllabus item *"United Nations Organizations"* and are
deliberately excluded, as are world sites such as Machu Picchu or Petra. This is
the distinction set out in SECTION 0A of the steering prompt: a question can be
perfectly true and still be off-syllabus because it is scoped to the wrong place.

**Currency.** Facts are current as of **September 2026**: India has **45** sites
(37 cultural, 7 natural, 1 mixed), the 45th being the **Ancient Buddhist Site of
Sarnath**, Uttar Pradesh, inscribed 25 July 2026 at the 48th session of the World
Heritage Committee in Busan. The 44th was the **Maratha Military Landscapes of
India** (July 2025, 12 forts — 11 in Maharashtra and Gingee Fort in Tamil Nadu)
and the 43rd the **Moidams** of the Ahom dynasty, Assam (2024). See
`current_affairs_2026.md` section 4.

**Build.** The JSON is generated, not hand-written, so the invariants are checked
rather than hoped for:

```bash
python3 standalone-tests/_build_unesco_india.py
```

The generator asserts the question-type mix matches the 40Q column of the ruleset
(16 Single, 6 Statement, 4 Assertion-Reason, 4 Matching, 4 Multiple-Correct,
2 Fill-in-the-Blank, 2 Numerical, 2 Data Interpretation) and rotates each
question's options so the correct answer falls on positions 1/2/3/4 exactly **ten
times each**. Assertion-Reason items keep the four mandated options in fixed
order, so their position is set by the logical relationship instead — the four
AR items use one of each relationship, contributing one to each position. The
script refuses to write the file if any invariant fails.
