#!/usr/bin/env python3
"""Scope + currency audit for the generated mock-test corpus.

Two defects this catches, both of which slipped past `_validate.py` (which only
checks mechanical schema/type/format rules and never looks at *meaning*):

  1. SCOPE DRIFT - a question is pitched at the world when the syllabus scopes
     that area to India (section B) or to J&K (section C). The official syllabus
     says "General Knowledge and Current Affairs (India)" for B and "General
     Knowledge with special reference to J&K" for C, and several B areas name
     India explicitly ("Famous Places in India", "Important rivers & lakes in
     India", "Climate & Crops in India"). A world-scoped question in those slots
     is off-syllabus even when it is factually true.

  2. STALE FACTS - a question asserts a volatile fact (an officeholder, a count,
     a "current"/"latest" claim, a treaty status) that was true at generation
     time but is not true as of the corpus AS_OF date. These are the questions
     that actively teach a candidate something wrong.

Usage:
    python3 mock-tests/_audit_scope.py                  # audit whole corpus
    python3 mock-tests/_audit_scope.py <file.json> ...   # audit named files
    python3 mock-tests/_audit_scope.py --strict          # exit 1 if any finding

Exit code is 0 unless --strict is passed and findings exist, so this is safe to
run in a pre-commit hook or CI step.
"""
import json
import os
import re
import sys
import glob
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = os.path.join(HERE, "tests")

# The date the corpus claims to be current as of. Keep in sync with
# CURRENT_AFFAIRS.md and the steering prompt's Factual Currency rule.
AS_OF = "2026-09"

# ---------------------------------------------------------------------------
# 1. SCOPE
# ---------------------------------------------------------------------------

# Markers that anchor a question to India.
INDIA = re.compile(
    r"\b(india|indian|bharat|new delhi|delhi|mumbai|kolkata|chennai|bengaluru|hyderabad"
    r"|assam|odisha|orissa|kerala|punjab|gujarat|rajasthan|bengal|bihar|karnataka"
    r"|maharashtra|tamil nadu|telangana|andhra|haryana|himachal|uttar pradesh|uttarakhand"
    r"|madhya pradesh|chhattisgarh|jharkhand|goa|sikkim|manipur|mizoram|nagaland|tripura"
    r"|meghalaya|arunachal|puducherry|lakshadweep|andaman"
    r"|ganga|ganges|yamuna|godavari|krishna|narmada|brahmaputra|kaveri|cauvery|mahanadi|tapi"
    r"|rupee|lok sabha|rajya sabha|parliament|supreme court|constitution|president of india"
    r"|prime minister|rbi|reserve bank|isro|drdo|niti aayog|upsc|jkssb"
    r"|mughal|maurya|gupta|chola|maratha|freedom struggle|gandhi|nehru|ambedkar|patel"
    r"|padma|bharat ratna|arjuna award|jnanpith|dronacharya)\b",
    re.I,
)

# Markers that anchor a question to J&K / Ladakh.
JK = re.compile(
    r"\b(j&k|jammu|kashmir|kashmiri|koshur|ladakh|srinagar|leh|kargil"
    r"|jhelum|chenab|tawi|wular|dal lake|nagin|manasbal|hokersar|lidder|sindh|marusudar"
    r"|gulmarg|pahalgam|sonamarg|sonmarg|patnitop|katra|vaishno|amarnath|yusmarg|doodhpathri"
    r"|baramulla|anantnag|anantnag|kupwara|pulwama|shopian|budgam|ganderbal|bandipora|kulgam"
    r"|doda|kishtwar|ramban|reasi|udhampur|kathua|samba|poonch|rajouri|banihal|zojila|zoji la"
    r"|dachigam|salal|baglihar|dulhasti|kishanganga|uri|pakal dul|ratle|tulbul|sopore|pampore"
    r"|saffron|pashmina|kani|gabba|namda|papier|khatamband|pheran|kangri|wazwan|noon chai"
    r"|dogra|dogri|gulab singh|hari singh|zain-ul-abidin|budshah|lalitaditya|habba khatoon"
    r"|nund rishi|lal ded|mahjoor|nadim|azad|sheikh abdullah|omar abdullah|mufti"
    r"|usbrl|chenani|nashri|jawahar tunnel|shalimar|nishat|chashma|achabal|martand|avantipora|parihaspora"
    r"|burzahom|mubarak mandi|raghunath|shankaracharya|hazratbal|charar|hari parbat"
    r"|pir panjal|karakoram|zanskar|nubra|pangong|siachen|tso moriri|amarnath"
    r"|sharada|herath|navreh|gurez|bhaderwah|sanasar|dachigam|hemis|thiksey|shey"
    r"|indus water|indus waters|instrument of accession|article 370|reorganisation act"
    r"|reorganization act|delimitation|back to village|ddc|ladakhi|balti|shina|gojri|pahari"
    r"|muslim conference|national conference|praja parishad|plebiscite|line of control|loc"
    r"|simla agreement|shimla agreement|aksai chin|gilgit|baltistan|jahangir|akbar's kashmir"
    r"|apple box|horticulture|walnut|almond|cricket bat|willow)\b"
    # J&K state undertakings and bodies are all JK-prefixed acronyms.
    r"|\bJK[A-Z]{2,}\b",
    re.I,
)

# Section B syllabus areas that ARE legitimately world-scoped. A B question is
# only flagged for scope drift when its test's topic is NOT one of these.
B_WORLD_OK = re.compile(
    r"(capital|currenc|united nations|saarc|asean|international organi[sz]ation"
    r"|first in world|firsts in world|world & india|world and india|physical division"
    r"|political division|everyday science|books? & authors?|books? and authors?"
    r"|world of sports|world famous award|world & national award|world and national award)",
    re.I,
)

# A question is "world-scoped" if it centres on a non-Indian place/entity.
WORLD_ONLY = re.compile(
    r"\b(nile|amazon|mississippi|missouri|yangtze|danube|volga|thames|seine|rhine|congo"
    r"|sahara|gobi|kalahari|atacama|mount everest|kilimanjaro|andes|alps|rockies|urals"
    r"|mariana trench|pacific|atlantic|arctic ocean|caspian|dead sea|lake victoria"
    r"|lake superior|baikal|titicaca|great barrier reef|eiffel|colosseum|machu picchu"
    r"|petra|christ the redeemer|chichen itza|great wall|pyramid of giza|stonehenge"
    r"|niagara|angel falls|victoria falls)\b",
    re.I,
)

# ---------------------------------------------------------------------------
# 2. CURRENCY / STALENESS
# ---------------------------------------------------------------------------

# Claims that only make sense relative to a date. If a question makes one of
# these claims it must either be timeless or carry an explicit as-of date.
RELATIVE_CLAIM = re.compile(
    r"\b(as of now|nowadays|latest|most recent|incumbent|till date"
    r"|recent years|recent estimates|recent data|recent trade data|recent financial year"
    r"|newest|last held|at present|presently)\b",
    re.I,
)
# Any explicit year anchors the claim well enough to be checkable, so it is not
# a silent-rot risk. Only genuinely undated claims are reported.
HAS_AS_OF_DATE = re.compile(r"\b(19|20)\d\d\b")

# Sections A (grammar), D (arithmetic) and E (computer concepts) are timeless;
# a word like "currently" there is ordinary English, not a factual claim.
FACTUAL_SECTIONS = {"B", "C"}

# ---------------------------------------------------------------------------
# 3. SYLLABUS COVERAGE (section A is a closed list)
# ---------------------------------------------------------------------------

# The official syllabus lists exactly ten areas for section A. Unlike sections
# B-E, whose areas are broad, this is a closed list, so a section A test on any
# other topic is off-syllabus however good the questions are. The steering
# prompt states the same rule in prose ("This section is grammar-driven ... do
# NOT generate them"), and the plan contradicted it for 280 questions.
A_AREAS = re.compile(
    r"article|clause|pronoun|homonym|homophone|tense|punctuation|comma|semicolon"
    r"|colon|apostrophe|synonym|antonym|analog|idiom|phrase|preposition"
    r"|agreement|general english|grammar",
    re.I,
)

# Question formats the Constable syllabus does not prescribe for section A.
A_FORBIDDEN = {
    "comprehension passage": re.compile(
        r"read the following passage|read the passage|study the passage"
        r"|according to the passage|as used in the passage", re.I),
    "direct/indirect narration": re.compile(
        r"change (?:the following sentence )?(?:in)?to indirect speech"
        r"|change (?:in)?to direct speech|into reported speech", re.I),
    "active/passive voice": re.compile(
        r"change (?:the following sentence )?(?:in)?to passive voice"
        r"|change (?:in)?to active voice|rewrite in the passive", re.I),
    "spot the error": re.compile(
        r"spot the error|find the error in|identify the part .{0,30}error", re.I),
    "one-word substitution": re.compile(
        r"one word for ['\"]|one-word substitution for", re.I),
    "cloze / para-jumble": re.compile(
        r"\bcloze\b|para.?jumble|rearrange the (?:following )?(?:sentences|parts)", re.I),
}

# Volatile facts whose value changes over time. `pattern` locates the topic;
# `stale` matches values that are known to be out of date at AS_OF; `note`
# explains the correct current position.
VOLATILE = [
    dict(
        name="UNESCO World Heritage Site count (India)",
        pattern=r"(world heritage|unesco)[^.?]{0,80}(how many|number of|total|count)"
                r"|(how many|number of|total)[^.?]{0,60}(world heritage)"
                r"|india (?:now )?has\s+\d+\s+(?:unesco\s+)?world heritage",
        stale=r"\b(3[0-9]|4[0-4])\b",
        # Citing the current total of 45 (or a series that ends there) is correct.
        ok=r"\b45\b",
        note="India has 45 World Heritage Sites (37 cultural, 7 natural, 1 mixed) "
             "after Sarnath, UP was inscribed on 25 July 2026 at the 48th session "
             "of the World Heritage Committee in Busan. The 44th was Maratha "
             "Military Landscapes (2025).",
    ),
    dict(
        name="Classical languages of India",
        pattern=r"classical language",
        stale=r"\b(six|6|eight|8|ten|10)\b\s*(classical|languages)|\bsix classical\b",
        note="India has 11 classical languages: Tamil (2004), Sanskrit (2005), "
             "Telugu and Kannada (2008), Malayalam (2013), Odia (2014), and "
             "Marathi, Pali, Prakrit, Assamese, Bengali added 3 October 2024.",
    ),
    dict(
        name="Ramsar site count (India)",
        pattern=r"ramsar[^.?]{0,80}(how many|number of|total)"
                r"|(how many|number of|total)[^.?]{0,60}ramsar",
        stale=r"\b(4[0-9]|[5-9][0-9]|100)\b",
        note="India has 101 Ramsar sites as of 4 August 2026 (101st: Glaw Lake, "
             "Arunachal Pradesh, designated 3 August 2026) - third highest in the "
             "world after the UK (176) and Mexico (144).",
    ),
    dict(
        name="Indus Waters Treaty status",
        pattern=r"indus waters? treaty",
        stale=r"(has been in force|remains in force|continues to operate|still governs"
              r"|successful water-sharing cooperation|has survived|uninterrupted)",
        # A question may legitimately describe the pre-2025 record as long as it
        # bounds the claim in time and names the abeyance.
        ok=r"(abeyance|until 2025|court of arbitration|held in abeyance)",
        note="India placed the IWT 'in abeyance' in April 2025 after the Pahalgam "
             "attack. In September 2026 the Court of Arbitration at The Hague ruled "
             "the treaty remains in force and cannot be unilaterally suspended; "
             "India rejected the award and maintains the abeyance. Any question "
             "describing the treaty as smoothly operating is out of date.",
    ),
    dict(
        name="J&K Assembly election / head of government",
        pattern=r"(j&k|jammu|kashmir)[^.?]{0,120}(assembly election|chief minister|legislative assembly)"
                r"|(assembly election|chief minister)[^.?]{0,80}(j&k|jammu|kashmir)",
        stale=r"(no assembly election|has not been held|yet to be held|delayed|awaited"
              r"|under president'?s rule|no elected government|currently has no)",
        # Fine when the item uses the outdated claim as a deliberately FALSE
        # statement and the explanation supplies the correct current position.
        ok=r"(omar abdullah|october 2024|september.october 2024)",
        note="J&K held its first UT Assembly election in September-October 2024. "
             "Omar Abdullah (JKNC) has been Chief Minister since 16 October 2024; "
             "Manoj Sinha is Lieutenant Governor. Restoration of full statehood "
             "remains under discussion.",
    ),
    dict(
        name="Chenab Bridge / USBRL completion",
        pattern=r"(chenab (?:rail(?:way)?\s*)?bridge|usbrl|udhampur.srinagar.baramulla)",
        stale=r"(under construction|being built|is expected to|when completed|once completed"
              r"|nearing completion|proposed|will connect|will provide)",
        ok=r"(inaugurated|june 2025|opened on|completed in june|fully operational since 2020)",
        note="The Chenab Bridge and the Anji Khad Bridge were inaugurated on "
             "6 June 2025, completing the 272 km USBRL. Vande Bharat services "
             "between Katra and Srinagar began 7 June 2025.",
    ),
    dict(
        name="Chenab Bridge vs Anji Khad Bridge conflation",
        # Only the *alias* construction is wrong - "Chenab Bridge (Anji Khad
        # Bridge)" presents one as another name for the other. Naming both in
        # order to contrast them is correct and must not be flagged.
        pattern=r"chenab\s*(?:rail(?:way)?\s*)?bridge['\"]?\s*\(\s*anji khad"
                r"|anji khad\s*(?:bridge)?\s*\(\s*chenab",
        stale=r".",
        note="These are TWO DIFFERENT bridges on the USBRL. Chenab Bridge is the "
             "world's highest railway arch bridge (359 m above the riverbed, Reasi). "
             "Anji Khad Bridge is India's first cable-stayed railway bridge. Never "
             "present one as an alias of the other.",
    ),
]

for v in VOLATILE:
    v["rx"] = re.compile(v["pattern"], re.I)
    v["rx_stale"] = re.compile(v["stale"], re.I)
    v["rx_ok"] = re.compile(v["ok"], re.I) if v.get("ok") else None


def blob(q, include_expl=True):
    parts = [q.get("questionText", "")] + list(q.get("options", []))
    if include_expl:
        parts.append(q.get("explanation", ""))
    return " ".join(parts)


def load_manifest():
    path = os.path.join(HERE, "manifest.json")
    if not os.path.exists(path):
        return {}
    m = json.load(open(path))
    return {t["filename"]: t for t in m.get("tests", [])}


def audit_file(path, manifest):
    findings = []
    name = os.path.basename(path)
    try:
        d = json.load(open(path))
    except Exception as exc:
        return [dict(kind="BADJSON", file=name, q="-", detail=str(exc))]

    entry = manifest.get(name, {})
    topic = str(entry.get("topics", d.get("topic", "")))
    world_ok = bool(B_WORLD_OK.search(topic))

    # --- section A topic must name a prescribed area ----------------------
    if entry.get("subject") == "A" and not A_AREAS.search(topic):
        findings.append(dict(
            kind="SYLLABUS", file=name, q="-",
            detail=f"section A test topic {topic!r} is not one of the ten areas the "
                   "syllabus prescribes (articles, clauses, pronouns, homonyms/homophones, "
                   "tenses, punctuation, synonyms/antonyms, analogies, idioms and phrases, "
                   "prepositions)",
        ))

    for q in d.get("questions", []):
        sec = q.get("subject")
        text = blob(q, include_expl=False)
        full = blob(q)
        qid = q.get("id", "?")

        # --- scope --------------------------------------------------------
        if sec == "C" and not JK.search(text):
            findings.append(dict(
                kind="SCOPE-C", file=name, q=qid,
                detail="section C question has no J&K/Ladakh anchor "
                       "(syllabus: 'special reference to J&K')",
                excerpt=q.get("questionText", "")[:110].replace("\n", " | "),
            ))
        elif sec == "B" and not world_ok:
            if WORLD_ONLY.search(text) and not INDIA.search(text):
                findings.append(dict(
                    kind="SCOPE-B", file=name, q=qid,
                    detail=f"world-scoped question in an India-scoped topic ({topic!r})",
                    excerpt=q.get("questionText", "")[:110].replace("\n", " | "),
                ))

        # --- undated relative claim --------------------------------------
        # Judged on the stem and options only: that is what the candidate reads
        # and answers, so that is what silently rots. A phrase like "the most
        # recent of the four listed" inside an explanation is ordinary
        # comparative English, not a dateable claim about the world.
        if (sec in FACTUAL_SECTIONS
                and RELATIVE_CLAIM.search(text)
                and not HAS_AS_OF_DATE.search(text)):
            findings.append(dict(
                kind="UNDATED", file=name, q=qid,
                detail="makes a time-relative claim ('currently'/'latest'/'recently') "
                       "with no as-of date, so it silently rots",
                excerpt=q.get("questionText", "")[:110].replace("\n", " | "),
            ))

        # --- forbidden section A question formats -------------------------
        if sec == "A":
            for label, rx in A_FORBIDDEN.items():
                if rx.search(text):
                    findings.append(dict(
                        kind="SYLLABUS", file=name, q=qid,
                        detail=f"section A item uses {label}, which the Constable "
                               "syllabus does not prescribe (the section is grammar-driven)",
                        excerpt=q.get("questionText", "")[:110].replace("\n", " | "),
                    ))
                    break

        # --- volatile facts ----------------------------------------------
        for v in VOLATILE:
            if v["rx_ok"] is not None and v["rx_ok"].search(full):
                continue
            if v["rx"].search(full) and v["rx_stale"].search(full):
                findings.append(dict(
                    kind="STALE", file=name, q=qid,
                    detail=f"{v['name']}: {v['note']}",
                    excerpt=q.get("questionText", "")[:110].replace("\n", " | "),
                ))

    return findings


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    manifest = load_manifest()
    files = args or sorted(glob.glob(os.path.join(TESTS_DIR, "*.json")))

    all_findings = []
    for f in files:
        all_findings.extend(audit_file(f, manifest))

    by_kind = collections.Counter(f["kind"] for f in all_findings)
    print(f"== scope + currency audit | as-of {AS_OF} | {len(files)} file(s)")
    if not all_findings:
        print("   no findings")
        return

    order = ["BADJSON", "SYLLABUS", "STALE", "SCOPE-C", "SCOPE-B", "UNDATED"]
    labels = {
        "BADJSON": "unparseable file",
        "SYLLABUS": "topic or question format the syllabus does not prescribe",
        "STALE": "asserts a fact that is out of date",
        "SCOPE-C": "section C without a J&K anchor",
        "SCOPE-B": "world-scoped item in an India-scoped topic",
        "UNDATED": "undated time-relative claim",
    }
    for kind in order:
        group = [f for f in all_findings if f["kind"] == kind]
        if not group:
            continue
        print(f"\n-- {kind}: {len(group)}  ({labels[kind]})")
        seen_note = set()
        for f in group:
            print(f"   {f['file']} q{f['q']}")
            if f.get("excerpt"):
                print(f"      {f['excerpt']}")
            note = f["detail"]
            if kind == "STALE":
                head = note.split(":")[0]
                if head in seen_note:
                    print(f"      -> {head} (see above)")
                    continue
                seen_note.add(head)
            print(f"      -> {note}")

    print(f"\n== totals: {dict(by_kind)}")
    if strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
