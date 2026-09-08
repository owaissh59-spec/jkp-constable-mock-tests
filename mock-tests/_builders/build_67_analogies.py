#!/usr/bin/env python3
"""Test 67 — Analogies (Revision). 30 Q, Section A.

Replaces the former "Direct/Indirect Narration" test. Narration is not among the
ten areas the syllabus prescribes for Section A, and the steering prompt
explicitly forbids generating it. Analogies are prescribed and had only one
earlier test, so this slot now reinforces a thin area.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _qbuild import Q, emit  # noqa: E402

q = Q()

q.single(
    "SURGEON : SCALPEL :: CARPENTER : ?",
    ["Chisel", "Timber", "Workshop", "Apprentice"],
    "Chisel",
    "The relationship is worker to the tool of his trade: a surgeon works with a scalpel, so a carpenter "
    "works with a chisel. 'Timber' is wrong because it is the material worked upon, not the implement. "
    "'Workshop' is wrong because it names the place of work. 'Apprentice' is wrong because it names a "
    "person, not a tool, and so breaks the pattern entirely.")

q.single(
    "CALF : COW :: CYGNET : ?",
    ["Swan", "Goose", "Duck", "Heron"],
    "Swan",
    "The relationship is the young of an animal to its adult: a calf is a young cow, and a cygnet is a "
    "young swan. 'Goose' is wrong because its young is a gosling. 'Duck' is wrong because its young is a "
    "duckling. 'Heron' is wrong because it is not the parent of a cygnet at all, and its young is simply "
    "called a chick.")

q.single(
    "CHAPTER : BOOK :: SCENE : ?",
    ["Play", "Actor", "Theatre", "Script"],
    "Play",
    "The relationship is part to whole: a chapter is a division of a book, and a scene is a division of a "
    "play. 'Actor' is wrong because a person is not a structural division. 'Theatre' is wrong because it "
    "is the venue rather than the work. 'Script' is wrong because a scene is not a subdivision of the "
    "script itself but of the drama the script records.")

q.single(
    "OPTIMIST : HOPEFUL :: PESSIMIST : ?",
    ["Gloomy", "Generous", "Curious", "Talkative"],
    "Gloomy",
    "The relationship is a person to the quality that defines him: an optimist is characteristically "
    "hopeful, and a pessimist is characteristically gloomy. 'Generous' is wrong because generosity has no "
    "bearing on how one views the future. 'Curious' is wrong because curiosity describes an interest in "
    "knowing, not an outlook. 'Talkative' is wrong because it describes manner of speech only.")

q.single(
    "FAMINE : STARVATION :: NEGLIGENCE : ?",
    ["Accident", "Caution", "Discipline", "Diligence"],
    "Accident",
    "The relationship is cause to effect: famine leads to starvation, and negligence leads to an accident. "
    "'Caution' is wrong because it is the opposite of negligence, not its consequence. 'Discipline' is "
    "wrong for the same reason. 'Diligence' is wrong because careful effort is the antonym of negligence "
    "rather than anything it produces.")

q.single(
    "BEE : HIVE :: HORSE : ?",
    ["Stable", "Saddle", "Pasture", "Herd"],
    "Stable",
    "The relationship is animal to its dwelling: a bee lives in a hive, and a horse is housed in a "
    "stable. 'Saddle' is wrong because it is equipment placed on the animal. 'Pasture' is wrong because "
    "it is grazing land rather than a dwelling. 'Herd' is wrong because it names a group of animals, not "
    "a place where one is kept.")

q.single(
    "LETHARGIC : ENERGETIC :: TRANSPARENT : ?",
    ["Opaque", "Fragile", "Colourless", "Brittle"],
    "Opaque",
    "The relationship is one of direct antonyms: lethargic is the opposite of energetic, and transparent "
    "is the opposite of opaque. 'Fragile' is wrong because it concerns strength, not the passage of "
    "light. 'Colourless' is wrong because it is close in sense to transparent rather than opposed to it. "
    "'Brittle' is wrong because it too describes how easily something breaks.")

q.single(
    "OASIS : DESERT :: ISLAND : ?",
    ["Ocean", "Beach", "Harbour", "Peninsula"],
    "Ocean",
    "The relationship is a small contrasting area to the vast expanse surrounding it: an oasis is "
    "surrounded by desert, and an island is surrounded by ocean. 'Beach' is wrong because it is part of "
    "the island's own edge. 'Harbour' is wrong because it is a sheltered inlet, not the surrounding mass. "
    "'Peninsula' is wrong because it is joined to the mainland on one side and so is not surrounding water.")

q.single(
    "GRAIN : GRANARY :: WATER : ?",
    ["Reservoir", "River", "Pipe", "Bucket"],
    "Reservoir",
    "The relationship is a commodity to the large structure built to store it: grain is stored in a "
    "granary, and water is stored in a reservoir. 'River' is wrong because it is a natural watercourse, "
    "not a store. 'Pipe' is wrong because it conveys water rather than holding it. 'Bucket' is wrong "
    "because the scale is domestic, whereas a granary and a reservoir are both bulk stores.")

q.single(
    "AUTHOR : NOVEL :: COMPOSER : ?",
    ["Symphony", "Orchestra", "Violin", "Audience"],
    "Symphony",
    "The relationship is creator to the work created: an author writes a novel, and a composer writes a "
    "symphony. 'Orchestra' is wrong because it is the body that performs the work. 'Violin' is wrong "
    "because it is an instrument used in performance. 'Audience' is wrong because it names those who "
    "listen, not what is created.")

q.single(
    "OUNCE : WEIGHT :: KNOT : ?",
    ["Speed", "Length", "Volume", "Pressure"],
    "Speed",
    "The relationship is a unit to the quantity it measures: an ounce measures weight, and a knot "
    "measures speed at sea, being one nautical mile per hour. 'Length' is wrong because the nautical mile "
    "measures distance while the knot measures rate. 'Volume' is wrong because knots have no bearing on "
    "capacity. 'Pressure' is wrong because that is measured in units such as the pascal or bar.")

q.single(
    "TEACHER : SCHOOL :: JUDGE : ?",
    ["Court", "Verdict", "Lawyer", "Statute"],
    "Court",
    "The relationship is a professional to the institution in which he works: a teacher works in a "
    "school, and a judge sits in a court. 'Verdict' is wrong because it is the outcome of the judge's "
    "work. 'Lawyer' is wrong because it names a fellow professional, not a workplace. 'Statute' is wrong "
    "because it is the law the judge applies rather than the place of work.")

q.single(
    "SCRIBBLE : WRITE :: STAMMER : ?",
    ["Speak", "Listen", "Shout", "Whisper"],
    "Speak",
    "The relationship is a faulty or imperfect performance of an action to the action itself: to scribble "
    "is to write badly, and to stammer is to speak with difficulty. 'Listen' is wrong because it is a "
    "different faculty altogether. 'Shout' is wrong because loudness is not a defect of fluency. "
    "'Whisper' is wrong because speaking softly is a matter of volume, not impediment.")

q.single(
    "PHYSICIAN : ILLNESS :: ECONOMIST : ?",
    ["Inflation", "Currency", "Bank", "Budget"],
    "Inflation",
    "The relationship is a specialist to the problem he studies and seeks to remedy: a physician treats "
    "illness, and an economist studies problems such as inflation. 'Currency' is wrong because it is an "
    "instrument within the economy, not an ailment of it. 'Bank' is wrong because it is an institution. "
    "'Budget' is wrong because it is a planning document rather than the problem addressed.")

q.single(
    "PARE : APPLE :: SHEAR : ?",
    ["Sheep", "Scissors", "Wool", "Shepherd"],
    "Sheep",
    "The relationship is an action to the thing it is performed upon: one pares an apple, and one shears "
    "a sheep. 'Scissors' is wrong because it is an instrument, not the object acted upon. 'Wool' is wrong "
    "because it is the product removed rather than the thing sheared. 'Shepherd' is wrong because he is "
    "the agent performing the action.")

# ---------------------------------------------------------------- fill blank
q.blank(
    "Fill in the blank to complete the analogy: BOTANY is to PLANTS as ENTOMOLOGY is to __________.",
    ["insects", "birds", "reptiles", "fungi"],
    "insects",
    "The relationship is a branch of study to its subject matter: botany is the study of plants, and "
    "entomology is the study of insects. 'Birds' is wrong because that study is ornithology. 'Reptiles' "
    "is wrong because that study is herpetology. 'Fungi' is wrong because that study is mycology, and it "
    "is a common trap since fungi were once grouped with plants.")

# ---------------------------------------------------------------- statements
q.statement(
    "Consider the following statements about the analogies given below:\n\n"
    "(i) HOT : COLD is a synonym relationship.\n"
    "(ii) DOCTOR : STETHOSCOPE is a worker-to-tool relationship.\n"
    "(iii) PUPPY : DOG is a young-to-adult relationship.\n"
    "(iv) PETAL : FLOWER is a part-to-whole relationship.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii) is correct — the stethoscope is the doctor's characteristic instrument. (iii) is correct — a puppy "
    "is a young dog. (iv) is correct — a petal is one part of a flower. (i) is wrong: hot and cold are "
    "antonyms, not synonyms, so the relationship is one of opposition rather than similarity. Every option "
    "containing (i) is therefore incorrect.")

q.statement(
    "Consider the following statements about analogy types:\n\n"
    "(i) SMOKE : FIRE illustrates effect to cause.\n"
    "(ii) POET : POEM illustrates creator to creation.\n"
    "(iii) KILOGRAM : MASS illustrates unit to quantity measured.\n"
    "(iv) LIBRARY : BOOKS illustrates cause to effect.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — smoke is the visible effect and fire the cause. (ii) is correct — a poet creates a "
    "poem. (iii) is correct — the kilogram is the unit in which mass is measured. (iv) is wrong: a library "
    "houses books, which is a container-to-contents relationship, not cause and effect, since books are "
    "not produced by libraries. Every option containing (iv) fails.")

q.statement(
    "Consider the following statements about the pair SCULPTOR : STATUE:\n\n"
    "(i) The relationship is agent to product.\n"
    "(ii) A parallel pair would be CHISEL : MARBLE.\n"
    "(iii) A parallel pair would be BAKER : BREAD.\n"
    "(iv) The relationship could also be described as creator to creation.\n\n"
    "Which of the statements given above are correct?",
    ["(ii), (iii) and (iv)", "(i), (iii) and (iv)", "(i), (ii) and (iv)", "All of the above"],
    "(i), (iii) and (iv)",
    "(i) and (iv) are correct and describe the same link in different words: the sculptor is the agent who "
    "produces the statue. (iii) is correct — a baker likewise produces bread. (ii) is wrong: chisel and "
    "marble are tool and material, neither of which is an agent producing the other, so it does not "
    "parallel the given pair. Every option containing (ii) is therefore incorrect.")

q.statement(
    "Consider the following statements about the pair ARID : DESERT:\n\n"
    "(i) The relationship is a defining quality to the thing it characterises.\n"
    "(ii) A parallel pair would be HUMID : SWAMP.\n"
    "(iii) A parallel pair would be DESERT : CAMEL.\n"
    "(iv) A parallel pair would be FERTILE : DELTA.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iv)", "(i), (ii) and (iii)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i) is correct — aridity is the defining property of a desert. (ii) is correct — humidity likewise "
    "defines a swamp. (iv) is correct — fertility is characteristic of a delta. (iii) is wrong: desert and "
    "camel is a habitat-to-inhabitant pair, which reverses the direction and changes the relationship "
    "altogether. Every option containing (iii) is incorrect.")

q.statement(
    "Consider the following statements about verbal analogies:\n\n"
    "(i) The order of the terms in an analogy matters.\n"
    "(ii) OUNCE : POUND is a part-to-whole relationship of measurement.\n"
    "(iii) An analogy may rest on a synonym or an antonym relationship.\n"
    "(iv) Two words that merely belong to the same topic form a valid analogy.\n\n"
    "Which of the statements given above are correct?",
    ["(ii), (iii) and (iv)", "(i), (ii) and (iv)", "(i), (iii) and (iv)", "(i), (ii) and (iii)"],
    "(i), (ii) and (iii)",
    "(i) is correct — reversing the terms usually destroys the relationship, so direction must be "
    "preserved. (ii) is correct — an ounce is a fraction of a pound, a part-to-whole measure. (iii) is "
    "correct — synonym and antonym pairs are both standard analogy types. (iv) is wrong: mere topical "
    "association is not a relationship, and a valid analogy needs a specific, statable link. Every option "
    "containing (iv) is therefore incorrect.")

# ---------------------------------------------------- assertion-reason (0,2,3)
q.ar("In the analogy CARTOGRAPHER : MAP, the relationship is that of maker to product.",
     "A cartographer is a person who draws and compiles maps.",
     0,
     "(A) is correct — the pair links the person to the thing he produces. (R) is correct — a cartographer "
     "is by definition a maker of maps. (R) also explains (A): it is precisely the cartographer's "
     "occupation that establishes the maker-to-product link. The option denying the explanatory connection "
     "is therefore wrong, and the two options rejecting either statement are wrong because both are "
     "accurate.")

q.ar("The pair HERD : SHEEP and the pair SHOAL : FISH share the same relationship.",
     "A herd and a shoal are both terms for a single animal of the species concerned.",
     2,
     "(A) is correct — both pairs link a collective noun to the creature it groups, so the relationship is "
     "the same. (R) is NOT correct: a herd and a shoal denote groups, not single animals, so the reason "
     "misstates the very idea of a collective noun. Since the assertion stands and the reason falls, the "
     "options claiming both are correct are wrong, as is the option calling the assertion incorrect.")

q.ar("In the analogy THERMOMETER : TEMPERATURE, the first term is the quantity and the second is the "
     "instrument.",
     "A thermometer is the instrument used to measure temperature.",
     3,
     "(A) is NOT correct — it reverses the terms: the thermometer is the instrument and temperature is the "
     "quantity measured, so the description given is the wrong way round. (R) is correct — a thermometer "
     "does measure temperature, and that is exactly what exposes the error in the assertion. Since the "
     "assertion falls and the reason stands, the options claiming both are correct are wrong, as is the "
     "option calling the reason incorrect.")

# ---------------------------------------------------------------- matching
q.matching(
    "Match the analogy pairs in Column I with the relationship they illustrate in Column II:\n\n"
    "Column I:\n(a) BLACKSMITH : ANVIL\n(b) KITTEN : CAT\n(c) WING : BIRD\n(d) DROUGHT : CROP FAILURE\n\n"
    "Column II:\n(i) Part to whole\n(ii) Cause to effect\n(iii) Worker to tool\n(iv) Young to adult\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
     "(a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)",
     "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)",
     "(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)"],
    "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
    "A blacksmith works at an anvil, giving worker to tool, so (a)-(iii). A kitten is a young cat, giving "
    "young to adult, so (b)-(iv). A wing is one part of a bird, giving part to whole, so (c)-(i). Drought "
    "brings about crop failure, giving cause to effect, so (d)-(ii). The other options variously make the "
    "kitten a part of the cat or the blacksmith a cause, and each misplaces at least two pairs.")

q.matching(
    "Match the words in Column I with the field of study in Column II:\n\n"
    "Column I:\n(a) Ornithology\n(b) Cardiology\n(c) Seismology\n(d) Etymology\n\n"
    "Column II:\n(i) Word origins\n(ii) Birds\n(iii) Earthquakes\n(iv) The heart\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)",
     "(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)",
     "(a)-(i), (b)-(iv), (c)-(iii), (d)-(ii)",
     "(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)"],
    "(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)",
    "Ornithology studies birds, so (a)-(ii). Cardiology concerns the heart, so (b)-(iv). Seismology deals "
    "with earthquakes, so (c)-(iii). Etymology traces the origins of words, so (d)-(i). The other options "
    "confuse seismology with cardiology, or hand ornithology the study of word origins, and each therefore "
    "misplaces at least two pairs. Note that etymology should not be confused with entomology, the study "
    "of insects.")

q.matching(
    "Match the analogy pairs in Column I with the parallel pair in Column II:\n\n"
    "Column I:\n(a) PEN : WRITE\n(b) SHIP : HARBOUR\n(c) HUNGER : FOOD\n(d) BUD : FLOWER\n\n"
    "Column II:\n(i) Aeroplane : Hangar\n(ii) Knife : Cut\n(iii) Caterpillar : Butterfly\n"
    "(iv) Thirst : Water\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)",
     "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)",
     "(a)-(i), (b)-(ii), (c)-(iv), (d)-(iii)",
     "(a)-(ii), (b)-(i), (c)-(iii), (d)-(iv)"],
    "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)",
    "A pen is used to write as a knife is used to cut, so (a)-(ii). A ship rests in a harbour as an "
    "aeroplane rests in a hangar, so (b)-(i). Hunger is relieved by food as thirst is relieved by water, "
    "so (c)-(iv). A bud develops into a flower as a caterpillar develops into a butterfly, so (d)-(iii). "
    "Each of the other options misassigns at least two of these pairs.")

# ---------------------------------------------------------- multiple correct
q.multi(
    "Which of the following are valid worker-to-tool analogies?\n\n"
    "(i) SAILOR : OCEAN\n(ii) TAILOR : NEEDLE\n(iii) FARMER : PLOUGH\n(iv) BARBER : SCISSORS\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii), (iii) and (iv) each pair a worker with the implement of his trade: needle, plough and scissors "
    "respectively. (i) is wrong: the ocean is the sailor's place of work, not a tool he holds, so the "
    "relationship is worker to workplace and the pattern breaks. Every option containing (i) is therefore "
    "incorrect.")

q.multi(
    "Which of the following are antonym analogies?\n\n"
    "(i) ASCEND : DESCEND\n(ii) BRAVE : COURAGEOUS\n(iii) SCARCE : ABUNDANT\n(iv) CONCEAL : REVEAL\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "(i), (ii) and (iv)"],
    "(i), (iii) and (iv)",
    "(i), (iii) and (iv) are all pairs of opposites: to ascend is the reverse of to descend, scarce is the "
    "reverse of abundant, and to conceal is the reverse of to reveal. (ii) is wrong: brave and courageous "
    "mean much the same thing, so the pair is a synonym relationship rather than an antonym one. Every "
    "option containing (ii) is incorrect.")

q.multi(
    "Which of the following are part-to-whole analogies?\n\n"
    "(i) BRANCH : TREE\n(ii) PAGE : BOOK\n(iii) ROOM : HOUSE\n(iv) SUMMER : HOT\n\n"
    "Select the correct combination:",
    ["(ii), (iii) and (iv)", "(i), (ii) and (iv)", "(i), (ii) and (iii)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i), (ii) and (iii) each name a component and the larger structure it belongs to: a branch is part of "
    "a tree, a page part of a book, a room part of a house. (iv) is wrong: summer and hot pair a season "
    "with a quality it possesses, which is a thing-to-attribute relationship rather than part to whole. "
    "Every option containing (iv) is therefore incorrect.")

emit(q, subject="A", topic="Analogies (Revision)",
     path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "tests", "67_test_A_analogies-rev.json"))
