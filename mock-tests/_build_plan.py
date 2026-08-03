#!/usr/bin/env python3
"""
Study-plan generator for the J&K Police Constable mock-test system.

Produces (all kept in sync):
  - mock-tests/manifest.json      -> machine-readable plan (source of truth for generation)
  - STUDY_PLAN.md                 -> human-readable, printable 70-day plan
  - mock-tests/config.json        -> counters + next_test pointer
  - mock-tests/history/<A-E>.json -> empty per-subject question fingerprint shards

Run:  python3 mock-tests/_build_plan.py
This is a build tool. Re-running regenerates the plan from scratch, so only run
it before any tests have been generated (or intentionally to re-plan).

The daily schedule is the EXACT 70-day plan designed for the JKSSB Constable
(Executive Police/Armed/IRP/SDRF) written examination. Each day/session/topic
is hardcoded below from the official study plan document.
"""

import json
import os
import re
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MT = os.path.join(ROOT, "mock-tests")

SUBJECTS = "ABCDE"
NSUB = len(SUBJECTS)
EXAM_DAY = 70

SUBJECT_NAMES = {
    "A": "General English",
    "B": "General Knowledge & Current Affairs (India)",
    "C": "General Knowledge — J&K",
    "D": "Numerical and Reasoning Ability",
    "E": "Basic Concepts of Computers",
}
BLUEPRINT = {"A": 25, "B": 25, "C": 10, "D": 25, "E": 15}
FULL_RATIO_LABEL = "25:25:10:25:15"
LEVEL = {s: "10+2" for s in SUBJECTS}

SESSION_NAMES = ["Morning", "Afternoon", "Late"]

# ---------------------------------------------------------------------------
# THE 70-DAY SCHEDULE (hardcoded from the official study plan document)
#
# Each entry: (subject_letter_or_FULL, topic_string, total_questions,
#              difficulty_profile, test_type, filename_slug)
#
# Grouped by day → 3 sessions (Morning, Afternoon, Late).
# ---------------------------------------------------------------------------

SCHEDULE = {
    # ========================== PHASE 1 (Days 1-35) ==========================
    1: [
        ("A", "Articles & Clauses", 30, "foundation", "Topic-wise", "articles-clauses"),
        ("B", "Important Dates in Indian History/Freedom Struggle", 40, "foundation", "Topic-wise", "indian-history-dates"),
        ("D", "Number System & Simplification", 50, "foundation", "Topic-wise", "number-system-simplification"),
    ],
    2: [
        ("C", "Abbreviations & Important Dates of J&K", 30, "foundation", "Topic-wise", "jk-abbrev-dates"),
        ("E", "Computer Terminology & Fundamentals", 40, "foundation", "Topic-wise", "computer-terminology"),
        ("A", "Pronouns & Tenses", 50, "foundation", "Topic-wise", "pronouns-tenses"),
    ],
    3: [
        ("D", "Number Series & Letter Series", 30, "foundation", "Topic-wise", "number-letter-series"),
        ("B", "First in World & India (Adventure, Sports, Discoveries)", 40, "foundation", "Topic-wise", "firsts-world-india"),
        ("E", "Hardware & Software", 50, "foundation", "Topic-wise", "hardware-software"),
    ],
    4: [
        ("A", "Homonyms & Homophones", 30, "foundation", "Topic-wise", "homonyms-homophones"),
        ("C", "Popular Names of J&K Personalities & Achievements", 40, "foundation", "Topic-wise", "jk-personalities"),
        ("D", "Percentage", 50, "foundation", "Topic-wise", "percentage"),
    ],
    5: [
        ("B", "Popular Names of Personalities (Religion, Politics, Science, Sports)", 30, "foundation", "Topic-wise", "popular-personalities"),
        ("E", "Input & Output Devices", 40, "foundation", "Topic-wise", "io-devices"),
        ("A", "Synonyms & Antonyms", 50, "foundation", "Topic-wise", "synonyms-antonyms"),
    ],
    6: [
        ("D", "Coding & Decoding", 30, "foundation", "Topic-wise", "coding-decoding"),
        ("C", "Weather, Climate & Crops of J&K", 40, "foundation", "Topic-wise", "jk-climate-crops"),
        ("B", "The Newspaper World & Books/Authors", 50, "foundation", "Topic-wise", "newspapers-books-authors"),
    ],
    7: [
        ("A", "Idioms & Phrases", 30, "foundation", "Topic-wise", "idioms-phrases"),
        ("D", "Average", 40, "foundation", "Topic-wise", "average"),
        ("FULL", "Cumulative Revision — Week 1 Topics (All Subjects)", 50, "standard", "Revision (cumulative)", "revision-wk1"),
    ],
    8: [
        ("B", "Famous Places in India & Languages", 30, "foundation", "Topic-wise", "famous-places-languages"),
        ("E", "MS Word", 40, "foundation", "Topic-wise", "ms-word"),
        ("D", "Profit & Loss", 50, "foundation", "Topic-wise", "profit-loss"),
    ],
    9: [
        ("A", "Analogies (Verbal)", 30, "foundation", "Topic-wise", "analogies-verbal"),
        ("C", "Means of Transport & Power Projects in J&K", 40, "foundation", "Topic-wise", "jk-transport-power"),
        ("D", "Direction Sense", 50, "foundation", "Topic-wise", "direction-sense"),
    ],
    10: [
        ("B", "Capitals & Currencies", 30, "foundation", "Topic-wise", "capitals-currencies"),
        ("D", "Ratio & Proportion", 40, "foundation", "Topic-wise", "ratio-proportion"),
        ("E", "MS Excel", 50, "foundation", "Topic-wise", "ms-excel"),
    ],
    11: [
        ("A", "Uses of Prepositions", 30, "foundation", "Topic-wise", "prepositions"),
        ("C", "Rivers & Lakes of J&K", 40, "foundation", "Topic-wise", "jk-rivers-lakes"),
        ("B", "United Nations Organizations (Veto, Members, Organs)", 50, "foundation", "Topic-wise", "united-nations"),
    ],
    12: [
        ("D", "Blood Relations", 30, "foundation", "Topic-wise", "blood-relations"),
        ("E", "Storage Devices & Operating Systems", 40, "foundation", "Topic-wise", "storage-os"),
        ("A", "Punctuation & Sentence Correction", 50, "foundation", "Topic-wise", "punctuation-correction"),
    ],
    13: [
        ("B", "SAARC, ASEAN & International Organizations", 30, "foundation", "Topic-wise", "saarc-asean-intl"),
        ("D", "Speed, Distance & Time", 40, "foundation", "Topic-wise", "speed-distance-time"),
        ("C", "Important Tourist Destinations of J&K", 50, "foundation", "Topic-wise", "jk-tourism"),
    ],
    14: [
        ("E", "Safety & Security (Cyber Security Basics)", 30, "foundation", "Topic-wise", "safety-security"),
        ("A", "Clauses (Noun, Adjective, Adverb)", 40, "foundation", "Topic-wise", "clauses-types"),
        ("FULL", "Cumulative Revision — Week 2 Topics (All Subjects)", 50, "standard", "Revision (cumulative)", "revision-wk2"),
    ],
    15: [
        ("D", "Simple & Compound Interest", 30, "foundation", "Topic-wise", "interest"),
        ("B", "Everyday Science", 40, "foundation", "Topic-wise", "everyday-science"),
        ("C", "History of J&K — Historical Places & Importance", 50, "foundation", "Topic-wise", "jk-history-places"),
    ],
    16: [
        ("A", "Comprehension Passage", 30, "foundation", "Topic-wise", "comprehension"),
        ("E", "E-mail & Internet Usage", 40, "foundation", "Topic-wise", "email-internet"),
        ("D", "Statements & Conclusions", 50, "foundation", "Topic-wise", "statements-conclusions"),
    ],
    17: [
        ("B", "World & National Awards (Science, Literature, Sports)", 30, "standard", "Topic-wise", "world-national-awards"),
        ("D", "Decimal Fractions", 40, "standard", "Topic-wise", "decimal-fractions"),
        ("A", "Fill in the Blanks", 50, "standard", "Topic-wise", "fill-blanks"),
    ],
    18: [
        ("C", "RTI Act", 30, "standard", "Topic-wise", "rti-act"),
        ("E", "Search Engines & Web Browsing", 40, "standard", "Topic-wise", "search-engines"),
        ("B", "The World of Sports", 50, "standard", "Topic-wise", "sports"),
    ],
    19: [
        ("D", "Logical Reasoning", 30, "standard", "Topic-wise", "logical-reasoning"),
        ("A", "Spot the Error", 40, "standard", "Topic-wise", "spot-error"),
        ("C", "Indus Water Treaty & Impact on Economy", 50, "standard", "Topic-wise", "indus-water-treaty"),
    ],
    20: [
        ("B", "Climate & Crops in India", 30, "standard", "Topic-wise", "climate-crops-india"),
        ("D", "Basic Algebra", 40, "standard", "Topic-wise", "algebra"),
        ("E", "Computer Terminology & Fundamentals (Revision)", 50, "standard", "Topic-wise", "computer-terminology-rev"),
    ],
    21: [
        ("A", "Active/Passive Voice", 30, "standard", "Topic-wise", "voice"),
        ("D", "Mental Reasoning & Sequential Output Tracing", 40, "standard", "Topic-wise", "mental-reasoning-seq"),
        ("FULL", "Cumulative Revision — Week 3 Topics (All Subjects)", 50, "standard", "Revision (cumulative)", "revision-wk3"),
    ],
    22: [
        ("B", "Constitution of India (Formation, Fundamental Rights, DPSP)", 30, "standard", "Topic-wise", "constitution"),
        ("C", "Agriculture & Industrialization in J&K Economy", 40, "standard", "Topic-wise", "jk-agri-industry"),
        ("D", "Mensuration", 50, "standard", "Topic-wise", "mensuration"),
    ],
    23: [
        ("A", "Direct/Indirect Narration", 30, "standard", "Topic-wise", "narration"),
        ("E", "Hardware & Software (Revision)", 40, "standard", "Topic-wise", "hardware-software-rev"),
        ("B", "Democratic Institutions & Forms of Government", 50, "standard", "Topic-wise", "democratic-institutions"),
    ],
    24: [
        ("D", "Trigonometry", 30, "standard", "Topic-wise", "trigonometry"),
        ("C", "Current Events — Local, National & International (J&K focus)", 40, "standard", "Topic-wise", "jk-current-events"),
        ("A", "One-Word Substitution", 50, "standard", "Topic-wise", "one-word-substitution"),
    ],
    25: [
        ("B", "Political & Physical Divisions of World & India", 30, "standard", "Topic-wise", "political-physical-divisions"),
        ("D", "Assertions & Reasons", 40, "standard", "Topic-wise", "assertions-reasons"),
        ("E", "MS Word (Revision)", 50, "standard", "Topic-wise", "ms-word-rev"),
    ],
    26: [
        ("A", "Articles & Clauses (Revision)", 30, "standard", "Topic-wise", "articles-clauses-rev"),
        ("B", "Important Rivers & Lakes in India", 40, "standard", "Topic-wise", "rivers-lakes-india"),
        ("D", "Arithmetical Operations", 50, "standard", "Topic-wise", "arithmetical-operations"),
    ],
    27: [
        ("C", "Abbreviations & Important Dates of J&K (Revision)", 30, "standard", "Topic-wise", "jk-abbrev-dates-rev"),
        ("E", "MS Excel (Revision)", 40, "standard", "Topic-wise", "ms-excel-rev"),
        ("B", "Current Events — National & International", 50, "standard", "Topic-wise", "current-events-national-intl"),
    ],
    28: [
        ("D", "Mathematical Reasoning", 30, "standard", "Topic-wise", "mathematical-reasoning"),
        ("A", "Synonyms & Antonyms (Revision)", 40, "standard", "Topic-wise", "synonyms-antonyms-rev"),
        ("FULL", "Cumulative Revision — Week 4 Topics (All Subjects)", 50, "standard", "Revision (cumulative)", "revision-wk4"),
    ],
    29: [
        ("B", "Agriculture & Industrialization in Economic Development", 30, "standard", "Topic-wise", "agri-industry-econ"),
        ("D", "Number System & Simplification (Revision)", 40, "standard", "Topic-wise", "number-system-rev"),
        ("E", "Safety & Security (Revision)", 50, "standard", "Topic-wise", "safety-security-rev"),
    ],
    30: [
        ("A", "Idioms & Phrases (Revision)", 30, "standard", "Topic-wise", "idioms-phrases-rev"),
        ("C", "History of J&K — Historical Places (Revision)", 40, "standard", "Topic-wise", "jk-history-places-rev"),
        ("D", "Profit & Loss (Revision)", 50, "standard", "Topic-wise", "profit-loss-rev"),
    ],
    31: [
        ("B", "Centrally Sponsored Schemes & Indian Foreign Trade", 30, "standard", "Topic-wise", "schemes-foreign-trade"),
        ("D", "Coding & Decoding (Revision)", 40, "standard", "Topic-wise", "coding-decoding-rev"),
        ("A", "Comprehension Passage (Revision)", 50, "standard", "Topic-wise", "comprehension-rev"),
    ],
    32: [
        ("E", "E-mail & Internet Usage (Revision)", 30, "standard", "Topic-wise", "email-internet-rev"),
        ("C", "Rivers & Lakes of J&K (Revision)", 40, "standard", "Topic-wise", "jk-rivers-lakes-rev"),
        ("D", "Speed, Distance & Time (Revision)", 50, "standard", "Topic-wise", "speed-distance-time-rev"),
    ],
    33: [
        ("A", "Pronouns & Tenses (Revision)", 30, "standard", "Topic-wise", "pronouns-tenses-rev"),
        ("B", "United Nations Organizations (Revision)", 40, "standard", "Topic-wise", "united-nations-rev"),
        ("D", "Blood Relations (Revision)", 50, "standard", "Topic-wise", "blood-relations-rev"),
    ],
    34: [
        ("D", "Ratio & Proportion (Revision)", 30, "standard", "Topic-wise", "ratio-proportion-rev"),
        ("E", "Storage & Operating Systems (Revision)", 40, "standard", "Topic-wise", "storage-os-rev"),
        ("B", "Everyday Science (Revision)", 50, "standard", "Topic-wise", "everyday-science-rev"),
    ],
    35: [
        ("A", "Homonyms & Homophones (Revision)", 30, "standard", "Topic-wise", "homonyms-homophones-rev"),
        ("C", "Tourist Destinations & Power Projects (Revision)", 40, "standard", "Topic-wise", "jk-tourism-power-rev"),
        ("FULL", "Cumulative Revision — Week 5 Topics (All Subjects)", 50, "standard", "Revision (cumulative)", "revision-wk5"),
    ],

    # ========================== PHASE 2 (Days 36-55) ==========================
    36: [
        ("A", "All topics of General English (mixed)", 50, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("B", "All topics of GK & Current Affairs India (mixed)", 60, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    37: [
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 50, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("C", "All topics of GK J&K (mixed)", 60, "advanced", "Subject full (multi-topic)", "C-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    38: [
        ("E", "All topics of Basic Concepts of Computers (mixed)", 50, "advanced", "Subject full (multi-topic)", "E-mixed"),
        ("A", "All topics of General English (mixed)", 60, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    39: [
        ("B", "All topics of GK & Current Affairs India (mixed)", 50, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 60, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("FULL", "Full syllabus — all subjects A-E", 100, "exam", "Full-length mock", "fulllength-1"),
    ],
    40: [
        ("C", "All topics of GK J&K (mixed)", 50, "advanced", "Subject full (multi-topic)", "C-mixed"),
        ("E", "All topics of Basic Concepts of Computers (mixed)", 60, "advanced", "Subject full (multi-topic)", "E-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    41: [
        ("A", "All topics of General English (mixed)", 50, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 60, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    42: [
        ("B", "All topics of GK & Current Affairs India (mixed)", 50, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("C", "All topics of GK J&K (mixed)", 60, "advanced", "Subject full (multi-topic)", "C-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    43: [
        ("E", "All topics of Basic Concepts of Computers (mixed)", 50, "advanced", "Subject full (multi-topic)", "E-mixed"),
        ("A", "All topics of General English (mixed)", 60, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("FULL", "Full syllabus — all subjects A-E", 100, "exam", "Full-length mock", "fulllength-2"),
    ],
    44: [
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 50, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("B", "All topics of GK & Current Affairs India (mixed)", 60, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    45: [
        ("C", "All topics of GK J&K (mixed)", 50, "advanced", "Subject full (multi-topic)", "C-mixed"),
        ("A", "All topics of General English (mixed)", 60, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    46: [
        ("E", "All topics of Basic Concepts of Computers (mixed)", 50, "advanced", "Subject full (multi-topic)", "E-mixed"),
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 60, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    47: [
        ("B", "All topics of GK & Current Affairs India (mixed)", 50, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("C", "All topics of GK J&K (mixed)", 60, "advanced", "Subject full (multi-topic)", "C-mixed"),
        ("FULL", "Full syllabus — all subjects A-E", 100, "exam", "Full-length mock", "fulllength-3"),
    ],
    48: [
        ("A", "All topics of General English (mixed)", 50, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 60, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    49: [
        ("E", "All topics of Basic Concepts of Computers (mixed)", 50, "advanced", "Subject full (multi-topic)", "E-mixed"),
        ("B", "All topics of GK & Current Affairs India (mixed)", 60, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    50: [
        ("C", "All topics of GK J&K (mixed)", 50, "advanced", "Subject full (multi-topic)", "C-mixed"),
        ("A", "All topics of General English (mixed)", 60, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    51: [
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 50, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("B", "All topics of GK & Current Affairs India (mixed)", 60, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("FULL", "Full syllabus — all subjects A-E", 100, "exam", "Full-length mock", "fulllength-4"),
    ],
    52: [
        ("A", "All topics of General English (mixed)", 50, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("E", "All topics of Basic Concepts of Computers (mixed)", 60, "advanced", "Subject full (multi-topic)", "E-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    53: [
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 50, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("C", "All topics of GK J&K (mixed)", 60, "advanced", "Subject full (multi-topic)", "C-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    54: [
        ("B", "All topics of GK & Current Affairs India (mixed)", 50, "advanced", "Subject full (multi-topic)", "B-mixed"),
        ("A", "All topics of General English (mixed)", 60, "advanced", "Subject full (multi-topic)", "A-mixed"),
        ("FULL", "Cumulative revision across all covered subjects", 50, "advanced", "Revision (cumulative)", "revision-cumulative"),
    ],
    55: [
        ("E", "All topics of Basic Concepts of Computers (mixed)", 50, "advanced", "Subject full (multi-topic)", "E-mixed"),
        ("D", "All topics of Numerical & Reasoning Ability (mixed)", 60, "advanced", "Subject full (multi-topic)", "D-mixed"),
        ("FULL", "Full syllabus — all subjects A-E", 100, "exam", "Full-length mock", "fulllength-5"),
    ],

    # ========================== PHASE 3 (Days 56-69) ==========================
    56: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-6"),
        ("A", "Sectional revision — General English", 50, "advanced", "Sectional revision", "A-revision"),
        ("B", "Rapid mixed revision & weak-area drill — GK India", 40, "advanced", "Rapid revision", "B-rapid"),
    ],
    57: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-7"),
        ("D", "Sectional revision — Numerical & Reasoning Ability", 50, "advanced", "Sectional revision", "D-revision"),
        ("C", "Rapid mixed revision & weak-area drill — GK J&K", 40, "advanced", "Rapid revision", "C-rapid"),
    ],
    58: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-8"),
        ("E", "Sectional revision — Basic Concepts of Computers", 50, "advanced", "Sectional revision", "E-revision"),
        ("A", "Rapid mixed revision & weak-area drill — General English", 40, "advanced", "Rapid revision", "A-rapid"),
    ],
    59: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-9"),
        ("B", "Sectional revision — GK & Current Affairs India", 50, "advanced", "Sectional revision", "B-revision"),
        ("D", "Rapid mixed revision & weak-area drill — Numerical & Reasoning", 40, "advanced", "Rapid revision", "D-rapid"),
    ],
    60: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-10"),
        ("C", "Sectional revision — GK J&K", 50, "advanced", "Sectional revision", "C-revision"),
        ("E", "Rapid mixed revision & weak-area drill — Computers", 40, "advanced", "Rapid revision", "E-rapid"),
    ],
    61: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-11"),
        ("A", "Sectional revision — General English", 50, "advanced", "Sectional revision", "A-revision"),
        ("B", "Rapid mixed revision & weak-area drill — GK India", 40, "advanced", "Rapid revision", "B-rapid"),
    ],
    62: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-12"),
        ("D", "Sectional revision — Numerical & Reasoning Ability", 50, "advanced", "Sectional revision", "D-revision"),
        ("C", "Rapid mixed revision & weak-area drill — GK J&K", 40, "advanced", "Rapid revision", "C-rapid"),
    ],
    63: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-13"),
        ("E", "Sectional revision — Basic Concepts of Computers", 50, "advanced", "Sectional revision", "E-revision"),
        ("A", "Rapid mixed revision & weak-area drill — General English", 40, "advanced", "Rapid revision", "A-rapid"),
    ],
    64: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-14"),
        ("B", "Sectional revision — GK & Current Affairs India", 50, "advanced", "Sectional revision", "B-revision"),
        ("D", "Rapid mixed revision & weak-area drill — Numerical & Reasoning", 40, "advanced", "Rapid revision", "D-rapid"),
    ],
    65: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-15"),
        ("C", "Sectional revision — GK J&K", 50, "advanced", "Sectional revision", "C-revision"),
        ("E", "Rapid mixed revision & weak-area drill — Computers", 40, "advanced", "Rapid revision", "E-rapid"),
    ],
    66: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-16"),
        ("A", "Sectional revision — General English", 50, "advanced", "Sectional revision", "A-revision"),
        ("B", "Rapid mixed revision & weak-area drill — GK India", 40, "advanced", "Rapid revision", "B-rapid"),
    ],
    67: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-17"),
        ("D", "Sectional revision — Numerical & Reasoning Ability", 50, "advanced", "Sectional revision", "D-revision"),
        ("C", "Rapid mixed revision & weak-area drill — GK J&K", 40, "advanced", "Rapid revision", "C-rapid"),
    ],
    68: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-18"),
        ("E", "Sectional revision — Basic Concepts of Computers", 50, "advanced", "Sectional revision", "E-revision"),
        ("A", "Rapid mixed revision & weak-area drill — General English", 40, "advanced", "Rapid revision", "A-rapid"),
    ],
    69: [
        ("FULL", "Full syllabus — all subjects A-E (exam simulation)", 100, "exam", "Full-length mock", "fulllength-19"),
        ("B", "Sectional revision — GK & Current Affairs India", 50, "advanced", "Sectional revision", "B-revision"),
        ("D", "Rapid mixed revision & weak-area drill — Numerical & Reasoning", 40, "advanced", "Rapid revision", "D-rapid"),
    ],
}

# ---------------------------------------------------------------------------
# BUILD tests list and plan_days from SCHEDULE
# ---------------------------------------------------------------------------

tests = []
plan_days = []
counter = 0

# Determine phase from day number
def get_phase(day):
    if day <= 35:
        return 1
    elif day <= 55:
        return 2
    else:
        return 3


for day in sorted(SCHEDULE.keys()):
    phase = get_phase(day)
    day_tests = []
    for session_idx, (subject, topics, qcount, difficulty, ttype, slug) in enumerate(SCHEDULE[day]):
        counter += 1
        filename = f"{counter}_test_{subject}_{slug}.json"
        subject_label = SUBJECT_NAMES.get(subject, f"Full Test (A-E, {FULL_RATIO_LABEL})")
        if subject == "FULL" and ttype == "Full-length mock":
            subject_label = f"Full Test (A-E, {FULL_RATIO_LABEL})"
        elif subject == "FULL":
            subject_label = "Mixed (cumulative revision)"

        entry = {
            "number": counter,
            "day": day,
            "phase": phase,
            "session": SESSION_NAMES[session_idx],
            "type": ttype,
            "subject": subject,
            "subject_name": subject_label,
            "level": LEVEL.get(subject, "10+2 (all sections)"),
            "topics": topics,
            "total_questions": qcount,
            "difficulty_profile": difficulty,
            "filename": filename,
            "status": "pending",
        }
        tests.append(entry)
        day_tests.append(entry)
    plan_days.append((day, phase, day_tests))


# ---------------------------------------------------------------------------
# WRITE manifest.json
# ---------------------------------------------------------------------------
manifest = {
    "project": "J&K Police Constable (Executive/Armed/IRP/SDRF) — Mock Test Plan",
    "generated_at": str(date.today()),
    "total_tests": len(tests),
    "medium": "English",
    "exam_day": EXAM_DAY,
    "blueprint": BLUEPRINT,
    "full_test_ratio": FULL_RATIO_LABEL,
    "phases": {
        "1": "Foundation / topic-wise (Days 1-35)",
        "2": "Consolidation / multi-topic + first full mocks (Days 36-55)",
        "3": f"Simulation & revision (Days 56-{EXAM_DAY - 1}); Day {EXAM_DAY} = EXAM",
    },
    "tests": tests,
}
with open(os.path.join(MT, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# WRITE config.json
# ---------------------------------------------------------------------------
config = {
    "project": "J&K Police Constable (Executive/Armed/IRP/SDRF) Mock Test System",
    "medium": "English",
    "exam_day": EXAM_DAY,
    "total_planned_tests": len(tests),
    "test_counter": 0,
    "next_test": 1,
    "last_generated": None,
    "updated_at": str(date.today()),
    "duplicate_policy": "no-exact-and-no-near-duplicate (check subject history shard)",
    "blueprint": BLUEPRINT,
    "full_test_ratio": FULL_RATIO_LABEL,
    "history_shards": {s: f"mock-tests/history/{s}.json" for s in SUBJECTS},
    "files": {
        "manifest": "mock-tests/manifest.json",
        "study_plan": "STUDY_PLAN.md",
        "syllabus": "syllabus_constable.md",
        "prompt": ".kiro/steering/mock-test-prompt-constable.md",
        "tests_dir": "mock-tests/tests/",
    },
}
with open(os.path.join(MT, "config.json"), "w") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# WRITE empty history shards
# ---------------------------------------------------------------------------
os.makedirs(os.path.join(MT, "history"), exist_ok=True)
for s in SUBJECTS:
    shard = {"subject": s, "subject_name": SUBJECT_NAMES[s], "count": 0, "questions": []}
    with open(os.path.join(MT, "history", f"{s}.json"), "w") as f:
        json.dump(shard, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# WRITE STUDY_PLAN.md
# ---------------------------------------------------------------------------
phase_titles = {
    1: "PHASE 1 — Foundation (Topic-wise Building)  ·  Days 1–35",
    2: "PHASE 2 — Consolidation (Multi-topic + First Full Mocks)  ·  Days 36–55",
    3: f"PHASE 3 — Simulation & Revision (Full-length + Weak-area)  ·  Days 56–{EXAM_DAY - 1}",
}
phase_notes = {
    1: ("3 tests every day — **Morning 30Q · Afternoon 40Q · Late 50Q**. Subjects are "
        "interleaved so no subject goes cold. Difficulty starts at *foundation* (easy-tilted) "
        "and moves to *standard* from Day 17. Every 7th day the late session is a **cumulative "
        "revision** of that week's topics."),
    2: ("3 tests every day — **Morning 50Q (full subject) · Afternoon 60Q (full subject) · "
        "Late 50Q revision or a 100Q FULL MOCK**. Difficulty is *advanced*. Full-length "
        "100-question mocks land on Days 39, 43, 47, 51, 55."),
    3: ("3 tests every day — **Morning 100Q FULL MOCK (exam simulation) · Afternoon 50Q "
        "sectional revision · Late 40Q rapid/weak-area drill**. Difficulty is *exam / advanced*. "
        f"**Day {EXAM_DAY} is the EXAM** — no new test, only light confidence revision and rest."),
}

lines = []
lines.append(f"# {EXAM_DAY}-Day Study & Mock-Test Plan — J&K Police Constable (Executive/Armed/IRP/SDRF)")
lines.append("")
lines.append(f"> **Medium:** English  ·  **Exam:** Day {EXAM_DAY}  ·  **Daily study:** 8–10 hours across 3 sessions.")
lines.append(">")
lines.append("> **Paper:** 100 MCQs · 1 mark each · 100 marks · 120 minutes · no negative marking prescribed.")
lines.append(">")
lines.append("> **Blueprint:** A General English 25 · B GK & Current Affairs (India) 25 · "
             "C GK — J&K 10 · D Numerical and Reasoning Ability 25 · E Basic Concepts of Computers 15.")
lines.append(">")
lines.append("> **How to use each day:** In the morning, revise the topic(s)/section(s) listed for that day. "
             "Then attempt the day's mock tests in order (Morning → Afternoon → Late). To generate a test, "
             'ask: *"Generate the next mock test."* The system picks the next ⬜ test below automatically.')
lines.append(">")
lines.append(f"> **Total planned tests:** {len(tests)}  ·  ⬜ = pending  ·  ✅ = generated")
lines.append("")
lines.append("**Difficulty profiles:** `foundation` (easy-tilted) · `standard` (blueprint) · "
             "`advanced` (hard-tilted) · `exam` (full-length simulation). All sections are pitched at "
             "**10+2 level** — difficulty means more steps and subtler distractors, never higher theory.")
lines.append("")

current_phase = None
for day, phase, day_tests in plan_days:
    if phase != current_phase:
        current_phase = phase
        lines.append("")
        lines.append(f"## {phase_titles[phase]}")
        lines.append("")
        lines.append(phase_notes[phase])
        lines.append("")
    lines.append(f"### Day {day}")
    lines.append("")
    lines.append("| # | Session | Section | Topic / Focus | Q | Difficulty | Type | Status |")
    lines.append("|---|---------|---------|---------------|---|------------|------|--------|")
    for t in day_tests:
        subj_disp = t["subject"] if t["subject"] == "FULL" else f'{t["subject"]} — {t["subject_name"]}'
        lines.append(
            f'| {t["number"]} | {t["session"]} | {subj_disp} | {t["topics"]} | '
            f'{t["total_questions"]} | {t["difficulty_profile"]} | {t["type"]} | ⬜ |'
        )
    lines.append("")

lines.append(f"## Day {EXAM_DAY} — EXAM DAY")
lines.append("")
lines.append("No new mock test. Light revision of formula sheets, current affairs, J&K facts, and "
             "previously-marked weak points only. Reach the exam centre early, stay calm, and — since "
             "no negative marking is prescribed — make sure **no question is left unattempted**.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Key Tips for Success")
lines.append("")
lines.append("1. Focus heavily on **D — Numerical & Reasoning (25 marks)** and **B — GK India (25 marks)** as they carry the highest weightage.")
lines.append("2. For **GK J&K (10 marks):** Focus on rivers, lakes, history, RTI Act, and Indus Water Treaty — these are frequently asked.")
lines.append("3. **Computer section (15 marks)** is scoring — MS Word, MS Excel shortcuts, and internet terms are easy to memorize.")
lines.append("4. Practice at least one full-length mock every week from Day 39 onwards to build exam stamina.")
lines.append("5. Maintain a separate **'Error Log'** — note every question you get wrong and revise it weekly.")
lines.append("6. For Current Affairs: Read daily newspapers (Greater Kashmir, Rising Kashmir) and follow J&K-specific updates.")
lines.append("7. Time management in exam: Spend ~30 sec per question. Do easy ones first, mark difficult ones for review.")
lines.append("8. Since no negative marking is prescribed — make sure **no question is left unattempted**.")
lines.append("9. Sleep 7–8 hours daily. Burnout will hurt more than extra hours of cramming.")
lines.append("10. On exam day: Carry all documents, reach early, read each question twice before answering.")
lines.append("")
lines.append("**ALL THE BEST!**")
lines.append("")

with open(os.path.join(ROOT, "STUDY_PLAN.md"), "w") as f:
    f.write("\n".join(lines))

# ---------------------------------------------------------------------------
# WRITE mock-tests/tests/.gitkeep (ensure the directory exists)
# ---------------------------------------------------------------------------
os.makedirs(os.path.join(MT, "tests"), exist_ok=True)
gitkeep = os.path.join(MT, "tests", ".gitkeep")
if not os.path.exists(gitkeep):
    open(gitkeep, "w").close()

# ---------------------------------------------------------------------------
# Summary to stdout
# ---------------------------------------------------------------------------
from collections import Counter
by_phase = Counter(t["phase"] for t in tests)
by_type = Counter(t["type"] for t in tests)
by_subject = Counter(t["subject"] for t in tests)
total_q = sum(t["total_questions"] for t in tests)
by_diff = Counter(t["difficulty_profile"] for t in tests)
print(f"Sections             : {NSUB} ({SUBJECTS})  ratio {FULL_RATIO_LABEL}")
print(f"Total tests planned  : {len(tests)}")
print(f"Total questions      : {total_q}")
print(f"By phase             : {dict(sorted(by_phase.items()))}")
print(f"By section           : {dict(sorted(by_subject.items()))}")
print(f"By difficulty        : {dict(sorted(by_diff.items()))}")
print("By type:")
for k, v in sorted(by_type.items(), key=lambda x: -x[1]):
    print(f"   {v:>3}  {k}")
