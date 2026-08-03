# Constable Mock Test System — J&K Police Constable (Executive/Armed/IRP/SDRF)

A plan-driven mock-test generation system to prepare for the **J&K Police Constable** written test in **70 days**. The AI reads a fixed study plan, generates the next mock test on demand, guarantees no repeated questions, and tracks progress — all while staying fast and within context even after hundreds of tests exist.

> This is the Constable counterpart of the Sub-Inspector series. The machinery is identical; the syllabus, sections, blueprint and topic plan are Constable-specific.

---

## How to use it (student workflow)

1. Print **`STUDY_PLAN.md`** to PDF. Each day lists the topic(s) to revise and 3 mock tests (Morning / Afternoon / Late).
2. Each morning, revise the day's listed topic(s)/section(s).
3. To get a test, start a session and say: **"Generate the next mock test."**
   - You never need to type a section or topic — the plan already knows what's next.
4. The generated test is saved as JSON in `mock-tests/tests/`. Attempt it, then repeat for the day's remaining sessions.

To generate several at once, say: *"Generate the next 3 mock tests"* (the day's set).

---

## Repository layout

```
jkp-constable-mock-tests/
├── README.md                             ← this file
├── syllabus_constable.md                 ← official Constable syllabus + exam blueprint
├── STUDY_PLAN.md                         ← printable 70-day plan (⬜ pending / ✅ done)
├── .kiro/steering/
│   └── mock-test-prompt-constable.md     ← generation ruleset (always loaded by the AI)
├── .agents/tasks/
│   └── _template-generate-tests/         ← batch-generation task template
└── mock-tests/
    ├── _build_plan.py                    ← one-off generator for the plan (build tool)
    ├── _validate.py                      ← mechanical self-check for a generated test
    ├── _record_test.py                   ← post-generation recorder (updates all state)
    ├── _normalize.py                     ← forces the exact question key schema/order
    ├── config.json                        ← counters + next_test pointer  (read FIRST, tiny)
    ├── manifest.json                      ← machine-readable plan: one spec per test
    ├── tests/                             ← generated test JSONs live here (output only)
    │   └── <N>_test_<section>_<slug>.json
    └── history/                           ← question fingerprints, SHARDED by section
        └── A.json  B.json  C.json  D.json  E.json
```

---

## The exam (fixed blueprint)

**100 MCQs · 1 mark each · 100 marks · 120 minutes · no negative marking prescribed.**

| Section | Subject | Q | Marks | Level |
|---|---|---|---|---|
| A | General English | 25 | 25 | 10+2 |
| B | General Knowledge & Current Affairs (India) | 25 | 25 | 10+2 |
| C | General Knowledge — special reference to J&K | 10 | 10 | 10+2 |
| D | Numerical and Reasoning Ability | 25 | 25 | 10+2 |
| E | Basic Concepts of Computers | 15 | 15 | 10+2 |
| | **Total** | **100** | **100** | |

Full-test subject ratio: **25 : 25 : 10 : 25 : 15**.

### Key differences from the SI series

| | Constable | Sub-Inspector |
|---|---|---|
| Sections | 5 (A–E) | 6 (A–F) |
| Marks / question | 1 | 2 |
| Negative marking | none prescribed | −0.5 |
| Level | 10+2 for all sections | Graduation (A/B/D) + 10th (C/E/F) |
| Maths & Reasoning | one combined 25Q section (D) | split across A, C, E |
| English | grammar-driven (articles, clauses, pronouns, tenses, punctuation, prepositions) — **no comprehension passages** | comprehension-driven |
| J&K GK | dedicated 10Q section (C) | folded into General Awareness |

---

## The 70-day plan at a glance

- **207 mock tests · 10,310 questions** total.
- **Phase 1 (Days 1–35):** Foundation, topic-wise. 3 tests/day (30/40/50 Q). All **87 topics** covered, with the 100 topic slots split **exactly** in blueprint proportion (A 25 · B 25 · C 10 · D 25 · E 15) and sections interleaved so none goes cold. Weekly cumulative revision on Days 7/14/21/28/35. Difficulty `foundation` → `standard`.
- **Phase 2 (Days 36–55):** Consolidation. Full-section multi-topic tests (50Q + 60Q) + the first full-length 100Q mocks (Days 39, 43, 47, 51, 55). Difficulty `advanced` / `exam`.
- **Phase 3 (Days 56–69):** Simulation. A full 100Q exam-style mock every day + sectional (50Q) and rapid weak-area (40Q) revision. Difficulty `exam` / `advanced`.
- **Day 70:** Exam day — light revision only.

---

## How the AI generates a test (every session)

Defined in `.kiro/steering/mock-test-prompt-constable.md`. Summary:

1. Read `mock-tests/config.json` → get `next_test` (N).
2. Read entry **N** in `mock-tests/manifest.json` → section, topics, question count, difficulty, filename.
3. Read only the relevant section shard(s) in `mock-tests/history/` → avoid repeats.
4. Generate the test per the ruleset (8 question types in fixed proportions, difficulty tilt, close distractors, full explanations).
5. **Post-generation:** save the test, then run the recorder:

```bash
python3 mock-tests/_validate.py mock-tests/tests/<N>_test_<section>_<slug>.json   # optional but recommended
python3 mock-tests/_record_test.py <N>
```

`_record_test.py` appends question fingerprints to the section shard, increments `config.json`, and flips the status to ✅ in `manifest.json` and `STUDY_PLAN.md`.

### Why it never runs out of context
The AI only ever reads three small things: `config.json`, the single needed `manifest.json` entry, and one section history shard. It **never** bulk-reads the growing `tests/` folder. History is split into 5 section files so each stays small.

### No repeated questions
Every generated question's fingerprint (normalized stem + core concept) is stored in its section shard. Before adding a new question the AI checks that shard and rejects both exact and near-duplicate (reworded) matches.

---

## Question format (per test JSON)

Each test file follows a fixed schema: `subject`, `topic`, `total_questions`, and a `questions[]` array where each item has `id`, `subject`, `questionText`, `options` (4), `correctAnswer` (exact copy of one option), and `explanation`. Every explanation states why the correct option is right **and** why each of the other three is wrong. Eight question types are used: Single Correct, Statement-based, Assertion–Reason, Matching, Multiple-Correct, Fill-in-the-Blank, Numerical Value, and Data Interpretation.

Run `python3 mock-tests/_normalize.py <file.json>` to force the exact key set and order if a generated file drifts.

---

## Building your own daily schedule (re-planning)

`mock-tests/_build_plan.py` regenerates `manifest.json`, `STUDY_PLAN.md`, `config.json`, and the empty history shards from scratch. Only run it **before** any tests are generated (or intentionally to rebuild the plan), as it resets counters:

```bash
python3 mock-tests/_build_plan.py
```

Three knobs control the whole schedule — edit them and re-run:

| Knob | What it controls |
|---|---|
| `TOPICS` | The topic pool per section. Drives the Phase-1 order and every filename slug. Add, remove or re-split topics freely. |
| `P1_DAY_RANGE`, `P1_SIZES`, `REVISION_EVERY` | Phase-1 length, the 3 daily question counts, and how often the late session is a week revision. Phase-1 slots are recomputed automatically and re-split in blueprint proportion. |
| `EXAM_DAY`, `full_mock_days_p2`, and the Phase 2/3 `range(...)` bounds | Where the phases start/end and which days carry a 100Q full mock. |

`BLUEPRINT` (`{"A": 25, "B": 25, "C": 10, "D": 25, "E": 15}`) is the exam pattern — leave it alone. It drives both the Phase-1 topic split and the full-test subject ratio.

Nothing else needs changing: `manifest.json` is the single source of truth the AI reads, and `_record_test.py` keeps every file in sync.
