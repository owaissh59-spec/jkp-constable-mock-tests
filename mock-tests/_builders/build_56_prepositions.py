#!/usr/bin/env python3
"""Test 56 — Uses of Prepositions (Revision). 40 Q, Section A.

Replaces the former "Spot the Error" test. Spotting the erroneous part of a
sentence is neither one of the ten prescribed Section A areas nor one of the eight
prescribed question types. Prepositions are prescribed and had only one earlier
test, so this slot now reinforces a thin area.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _qbuild import Q, emit  # noqa: E402

q = Q()

# ------------------------------------------------------------------ singles
q.single("Choose the correct preposition: She has been living in Srinagar __________ 2015.",
         ["since", "for", "from", "by"],
         "since",
         "'Since' is used with a point in time from which an action has continued, and 2015 is such a "
         "point. 'For' is wrong because it takes a duration, as in 'for ten years'. 'From' is wrong "
         "because it needs a stated end point, as in 'from 2015 to 2020', and does not suit the present "
         "perfect continuous here. 'By' is wrong because it marks a deadline rather than a starting point.")

q.single("Choose the correct preposition: The committee will look __________ the complaint next week.",
         ["into", "after", "for", "over"],
         "into",
         "'Look into' means to investigate, which is what a committee does with a complaint. 'Look after' "
         "is wrong because it means to take care of a person or thing. 'Look for' is wrong because it "
         "means to search for something that is missing. 'Look over' is wrong because it means to inspect "
         "briefly or skim, which understates a formal inquiry.")

q.single("Choose the correct preposition: He was accused __________ negligence in handling the case.",
         ["of", "for", "with", "about"],
         "of",
         "The verb 'accuse' takes the preposition 'of' before the offence, giving 'accused of "
         "negligence'. 'For' is wrong here, though it is correct after 'blame', as in 'blamed for the "
         "delay', which is the source of the confusion. 'With' is wrong because it follows 'charge', as "
         "in 'charged with an offence'. 'About' is wrong because it does not follow 'accuse' at all.")

q.single("Choose the correct preposition: The two brothers differ __________ each other in temperament.",
         ["from", "with", "to", "against"],
         "from",
         "'Differ from' is used when comparing how two things are unlike each other. 'Differ with' is "
         "wrong in this sense, as it means to disagree in opinion, which is about dispute rather than "
         "dissimilarity. 'To' is wrong because 'differ' never takes 'to'. 'Against' is wrong because it "
         "suggests opposition or resistance, not difference of character.")

q.single("Choose the correct preposition: She is not capable __________ handling this responsibility alone.",
         ["of", "for", "to", "in"],
         "of",
         "The adjective 'capable' is always followed by 'of' and then a gerund, giving 'capable of "
         "handling'. 'For' is wrong because it follows 'fit', as in 'fit for duty'. 'To' is wrong because "
         "'capable to handle' is a common error; the infinitive follows 'able', not 'capable'. 'In' is "
         "wrong because it does not collocate with 'capable' in this construction.")

q.single("Choose the correct preposition: The train arrived __________ the station an hour late.",
         ["at", "in", "to", "on"],
         "at",
         "'Arrive at' is used with a specific point such as a station, an airport or a building. 'In' is "
         "wrong here because 'arrive in' is used with towns, cities and countries. 'To' is wrong because "
         "'arrive' never takes 'to', a frequent error influenced by 'go to'. 'On' is wrong because it "
         "would suggest arriving on top of the station.")

q.single("Choose the correct preposition: He insisted __________ paying the entire bill himself.",
         ["on", "for", "to", "about"],
         "on",
         "'Insist' takes 'on' followed by a gerund, giving 'insisted on paying'. 'For' is wrong because "
         "it does not follow 'insist', though it does follow 'ask', as in 'asked for the bill'. 'To' is "
         "wrong because 'insisted to pay' is a common error; 'insist' never takes the infinitive. 'About' "
         "is wrong because it follows verbs of speech such as 'talk', not 'insist'.")

q.single("Choose the correct preposition: The meeting has been postponed __________ Friday.",
         ["till", "since", "from", "by"],
         "till",
         "'Till' (or 'until') marks the point up to which the postponement runs, which is the sense "
         "needed. 'Since' is wrong because it looks backwards from the present to a past starting point. "
         "'From' is wrong because it marks a beginning rather than an end. 'By' is wrong because it means "
         "'not later than' and would imply the meeting happens before Friday, reversing the meaning.")

q.single("Choose the correct preposition: There is no need to discuss __________ this matter any further.",
         ["(no preposition needed)", "about", "on", "over"],
         "(no preposition needed)",
         "'Discuss' is a transitive verb and takes a direct object, so it needs no preposition: one "
         "discusses a matter. 'Discuss about' is among the commonest errors in Indian English, formed by "
         "analogy with 'talk about'. 'Discuss on' is wrong for the same reason. 'Discuss over' is wrong "
         "too, although 'discuss over a cup of tea' is possible in a quite different sense of place.")

q.single("Choose the correct preposition: She was married __________ an engineer from Jammu.",
         ["to", "with", "by", "for"],
         "to",
         "One is married 'to' a person, so 'married to an engineer' is correct. 'With' is wrong and is a "
         "frequent error carried over from other languages. 'By' is wrong because it names the person who "
         "conducts the ceremony, as in 'married by the registrar'. 'For' is wrong because it does not "
         "follow 'married' in this sense at all.")

q.single("Choose the correct preposition: The new rules will come __________ force from the first of April.",
         ["into", "in", "to", "under"],
         "into",
         "'Come into force' is the fixed collocation used of laws and rules taking effect. 'In' is wrong "
         "because 'come in force' is not idiomatic, though 'in force' alone is correct after the verb "
         "'be'. 'To' is wrong because it does not appear in this phrase. 'Under' is wrong because 'under "
         "force' would suggest compulsion rather than commencement.")

q.single("Choose the correct preposition: He apologised __________ his rude behaviour at the function.",
         ["for", "of", "on", "about"],
         "for",
         "'Apologise for' is used before the thing one is sorry about, so 'apologised for his behaviour' "
         "is correct. 'Of' is wrong because it does not follow 'apologise'. 'On' is wrong for the same "
         "reason. 'About' is wrong here, and although 'apologise to' is correct, it introduces the person "
         "receiving the apology rather than the offence itself.")

q.single("Choose the correct preposition: The bridge was built __________ the Chenab river.",
         ["across", "through", "along", "among"],
         "across",
         "'Across' expresses movement or extension from one side of something to the other, which is what "
         "a bridge does over a river. 'Through' is wrong because it implies passage inside something, as "
         "through a tunnel. 'Along' is wrong because it means following the length of something, as in "
         "walking along the bank. 'Among' is wrong because it needs three or more things surrounding.")

q.single("Choose the correct preposition: All the candidates must comply __________ the instructions given.",
         ["with", "to", "for", "on"],
         "with",
         "'Comply' takes 'with', giving 'comply with the instructions'. 'To' is wrong here, though it is "
         "correct after 'conform' in some usages and after 'adhere', which is the likely source of the "
         "confusion. 'For' is wrong because it does not follow 'comply'. 'On' is wrong for the same "
         "reason and produces no recognised collocation.")

q.single("Choose the correct preposition: The keys are __________ the drawer in the top cupboard.",
         ["in", "at", "on", "over"],
         "in",
         "'In' is used for something enclosed within a container or space, and a drawer encloses the keys. "
         "'At' is wrong because it marks a point rather than an interior, as in 'at the door'. 'On' is "
         "wrong because it would place the keys upon the drawer's surface. 'Over' is wrong because it "
         "means above without contact.")

q.single("Choose the correct preposition: He has been absent __________ duty since Monday.",
         ["from", "in", "of", "at"],
         "from",
         "'Absent from' is the fixed pairing used of a place, an occasion or a duty. 'In' is wrong because "
         "it does not follow 'absent'. 'Of' is wrong for the same reason, although 'in the absence of' is "
         "a correct noun phrase that often causes the slip. 'At' is wrong because it would mark presence "
         "at a location rather than absence from it.")

q.single("Choose the correct preposition: The shop is open __________ nine in the morning to six in the evening.",
         ["from", "since", "at", "by"],
         "from",
         "'From … to' is the standard pairing for a stretch of time with both ends stated, and 'to six' "
         "is already given. 'Since' is wrong because it looks back from the present and cannot pair with "
         "'to'. 'At' is wrong because it fixes a single point rather than a range. 'By' is wrong because "
         "it marks a deadline and cannot introduce the opening of a range.")

q.single("Choose the correct preposition: She congratulated him __________ his success in the examination.",
         ["on", "for", "about", "of"],
         "on",
         "'Congratulate' takes 'on' before the achievement, giving 'congratulated him on his success'. "
         "'For' is wrong here, although it is correct after 'thank', as in 'thanked him for his help', "
         "which is the usual source of the error. 'About' is wrong because it does not follow "
         "'congratulate'. 'Of' is wrong for the same reason.")

q.single("Choose the correct preposition: The cat jumped __________ the wall and disappeared.",
         ["over", "above", "upon", "across"],
         "over",
         "'Over' expresses movement from one side of an obstacle to the other, clearing it, which is what "
         "jumping a wall involves. 'Above' is wrong because it describes static position at a higher "
         "level, with no sense of crossing. 'Upon' is wrong because it would mean landing on top of the "
         "wall and staying there. 'Across' is wrong because it suits flat expanses such as a road.")

q.single("Choose the correct preposition: He is quite different __________ what I had expected.",
         ["from", "than", "to", "with"],
         "from",
         "'Different from' is the standard form in careful written English. 'Than' is wrong in British "
         "usage, where 'different than' is generally treated as an Americanism and avoided in examinations. "
         "'To' is wrong in formal writing, although 'different to' is heard in informal British speech. "
         "'With' is wrong because it never follows 'different' in this sense.")

# --------------------------------------------------------------- fill blanks
q.blank("Fill in the blank with the correct preposition: The candidate apologised __________ his late "
        "arrival at the interview.",
        ["for", "of", "on", "with"],
        "for",
        "'Apologise for' introduces the thing one regrets, so 'apologised for his late arrival' is "
        "correct. 'Of' is wrong because it does not follow the verb 'apologise'. 'On' is wrong for the "
        "same reason. 'With' is wrong because it too fails to collocate, and the only other correct "
        "preposition here would be 'to' before the person receiving the apology.")

q.blank("Fill in the blank with the correct preposition: The success of the mission depends __________ "
        "careful planning.",
        ["on", "of", "from", "in"],
        "on",
        "'Depend on' (or 'depend upon') is the fixed pairing, so 'depends on careful planning' is correct. "
        "'Of' is wrong because it does not follow 'depend', though it does follow the noun in phrases such "
        "as 'independent of'. 'From' is wrong because it does not collocate with 'depend'. 'In' is wrong "
        "for the same reason and produces no recognised phrase.")

# ---------------------------------------------------------------- statements
q.statement(
    "Consider the following statements about prepositions of time:\n\n"
    "(i) 'Since' is followed by a duration such as 'ten years'.\n"
    "(ii) 'At' is used with clock times, as in 'at six o'clock'.\n"
    "(iii) 'On' is used with days and dates, as in 'on Monday'.\n"
    "(iv) 'In' is used with months and years, as in 'in March'.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii), (iii) and (iv) state the standard rules: 'at' for clock times, 'on' for days and dates, 'in' "
    "for months, years and longer periods. (i) is wrong: 'since' takes a point in time, as in 'since "
    "2015', while it is 'for' that takes a duration such as 'for ten years'. Every option containing (i) "
    "is therefore incorrect.")

q.statement(
    "Consider the following statements about prepositional verbs:\n\n"
    "(i) 'Depend' is followed by 'on'.\n"
    "(ii) 'Insist' is followed by 'on'.\n"
    "(iii) 'Discuss' is followed by 'about'.\n"
    "(iv) 'Comply' is followed by 'with'.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are all correct collocations: depend on, insist on and comply with. (iii) is "
    "wrong: 'discuss' is transitive and takes a direct object with no preposition, so 'discuss the "
    "matter' is right and 'discuss about the matter' is a well-known error formed by analogy with 'talk "
    "about'. Every option containing (iii) fails.")

q.statement(
    "Consider the following statements about prepositions of place:\n\n"
    "(i) 'Arrive' is followed by 'to' before a station.\n"
    "(ii) 'In' is used for enclosed spaces, as in 'in the drawer'.\n"
    "(iii) 'At' is used for a specific point, as in 'at the gate'.\n"
    "(iv) 'Between' is used of two things and 'among' of more than two.\n\n"
    "Which of the statements given above are correct?",
    ["(ii), (iii) and (iv)", "(i), (ii) and (iii)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii), (iii) and (iv) are all correct: 'in' for enclosed spaces, 'at' for specific points, and the "
    "two-versus-many distinction between 'between' and 'among'. (i) is wrong: 'arrive' takes 'at' before "
    "a point such as a station and 'in' before a town or country, but never 'to'. Every option containing "
    "(i) is therefore incorrect.")

q.statement(
    "Consider the following statements about adjectives followed by prepositions:\n\n"
    "(i) 'Capable' is followed by 'of'.\n"
    "(ii) 'Afraid' is followed by 'of'.\n"
    "(iii) 'Absent' is followed by 'from'.\n"
    "(iv) 'Different' is followed by 'with' in careful writing.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iv)", "(ii), (iii) and (iv)", "(i), (ii) and (iii)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i), (ii) and (iii) are all standard pairings: capable of, afraid of and absent from. (iv) is wrong: "
    "the accepted form is 'different from', with 'different to' heard informally in British speech and "
    "'different than' treated as an Americanism, but 'different with' is not used at all. Every option "
    "containing (iv) is incorrect.")

q.statement(
    "Consider the following statements about the sentence 'He has been absent from duty since Monday':\n\n"
    "(i) 'From' correctly follows the adjective 'absent'.\n"
    "(ii) 'Since' correctly introduces a point in time.\n"
    "(iii) The tense used is the present perfect continuous.\n"
    "(iv) 'Since' should be replaced by 'for' before 'Monday'.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iv)", "(ii), (iii) and (iv)", "(i), (ii) and (iii)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — 'absent from' is the fixed pairing. (ii) is correct — Monday is a point in time, "
    "which is exactly what 'since' requires. (iii) is correct — 'has been' with the participle forms the "
    "present perfect continuous, the tense that naturally accompanies 'since'. (iv) is wrong: 'for' takes "
    "a duration, so 'for Monday' would be ungrammatical here. Every option containing (iv) is incorrect.")

q.statement(
    "Consider the following statements about 'in' and 'into':\n\n"
    "(i) 'Walk into the room' expresses movement from outside to inside.\n"
    "(ii) 'Sit in the room' expresses position rather than movement.\n"
    "(iii) 'Come into force' is the correct idiom for rules taking effect.\n"
    "(iv) 'Into' is used for static position and 'in' for movement.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i), (ii) and (iii) are all correct: 'into' carries the sense of entering, 'in' states where "
    "something is, and 'come into force' is the established idiom for legislation taking effect. (iv) is "
    "wrong because it reverses the two: 'into' marks movement and 'in' marks position. Every option "
    "containing (iv) is therefore incorrect.")

# ----------------------------------------------- assertion-reason (0,1,2,3)
q.ar("The sentence 'He was accused of negligence' uses the correct preposition.",
     "The verb 'accuse' is followed by 'of' before the offence alleged.",
     0,
     "(A) is correct — 'accused of negligence' is the standard construction. (R) is correct — 'accuse' "
     "does take 'of' before the offence. (R) also explains (A): it states the very rule that makes the "
     "sentence right. The option denying the explanatory link is therefore wrong, and the two options "
     "rejecting either statement are wrong because both are accurate. Contrast 'charged with' and 'blamed "
     "for', which take different prepositions.")

q.ar("The sentence 'She has been living here since 2015' is correct.",
     "The present perfect continuous tense is formed with 'has/have been' followed by the present participle.",
     1,
     "(A) is correct — 'since' properly introduces the point in time 2015. (R) is also correct as a "
     "statement about how the tense is formed. But (R) does not explain (A): the sentence is correct "
     "because 'since' takes a point in time rather than a duration, and the rule about forming the tense "
     "says nothing about the choice of preposition. Both stand, yet the reason fails to account for the "
     "assertion.")

q.ar("The sentence 'We discussed about the proposal for an hour' contains a preposition error.",
     "'Discuss' is an intransitive verb and therefore requires a preposition before its object.",
     2,
     "(A) is correct — 'discussed about' is faulty and should simply be 'discussed the proposal'. (R) is "
     "NOT correct: 'discuss' is transitive, which is exactly why it takes a direct object and needs no "
     "preposition at all. The reason states the opposite of the rule that makes the assertion true. Since "
     "the assertion stands and the reason falls, the options claiming both are correct are wrong.")

q.ar("'Between' should be used when more than two persons or things are involved.",
     "'Among' is normally used when more than two persons or things are involved.",
     3,
     "(A) is NOT correct — it inverts the rule: 'between' is used of two, as in 'between the two "
     "brothers'. (R) is correct — 'among' is the form used for more than two, as in 'among the "
     "candidates'. So the assertion states the rule backwards while the reason states it accurately, and "
     "the reason is what exposes the error. Options claiming both are correct are therefore wrong.")

# ---------------------------------------------------------------- matching
q.matching(
    "Match the verbs in Column I with the prepositions that follow them in Column II:\n\n"
    "Column I:\n(a) Depend\n(b) Comply\n(c) Apologise\n(d) Accuse\n\n"
    "Column II:\n(i) of\n(ii) on\n(iii) with\n(iv) for\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)",
     "(a)-(iii), (b)-(ii), (c)-(iv), (d)-(i)",
     "(a)-(ii), (b)-(iii), (c)-(i), (d)-(iv)",
     "(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)"],
    "(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)",
    "The fixed pairings are depend on, comply with, apologise for and accuse of, giving (a)-(ii), "
    "(b)-(iii), (c)-(iv) and (d)-(i). The other options swap 'on' and 'with' between depend and comply, "
    "or give 'of' to apologise and 'for' to accuse, and each therefore misplaces at least two pairs. Note "
    "that 'blame' takes 'for' and 'charge' takes 'with', which are the usual sources of confusion.")

q.matching(
    "Match the adjectives in Column I with the prepositions that follow them in Column II:\n\n"
    "Column I:\n(a) Absent\n(b) Capable\n(c) Similar\n(d) Superior\n\n"
    "Column II:\n(i) to\n(ii) from\n(iii) of\n(iv) to (in quality or rank)\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iii), (c)-(i), (d)-(iv)",
     "(a)-(iii), (b)-(ii), (c)-(i), (d)-(iv)",
     "(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)",
     "(a)-(i), (b)-(iii), (c)-(ii), (d)-(iv)"],
    "(a)-(ii), (b)-(iii), (c)-(i), (d)-(iv)",
    "The standard pairings are absent from, capable of, similar to and superior to, so (a)-(ii), "
    "(b)-(iii), (c)-(i) and (d)-(iv). Note that 'superior' and 'inferior' take 'to' and never 'than', a "
    "frequent error. The other options hand 'of' to 'absent' or 'from' to 'capable', and each misassigns "
    "at least two pairs.")

q.matching(
    "Match the prepositions in Column I with the sense they express in Column II:\n\n"
    "Column I:\n(a) Across\n(b) Along\n(c) Through\n(d) Above\n\n"
    "Column II:\n(i) Following the length of something\n(ii) At a higher level, without contact\n"
    "(iii) From one side to the other\n(iv) Passing inside or within something\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)",
     "(a)-(i), (b)-(iii), (c)-(iv), (d)-(ii)",
     "(a)-(iii), (b)-(i), (c)-(ii), (d)-(iv)",
     "(a)-(iv), (b)-(i), (c)-(iii), (d)-(ii)"],
    "(a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)",
    "'Across' means from one side to the other, so (a)-(iii). 'Along' means following the length of "
    "something, so (b)-(i). 'Through' means passing within something, so (c)-(iv). 'Above' means at a "
    "higher level without contact, so (d)-(ii). The other options exchange 'across' with 'along' or "
    "'through' with 'above', and each therefore misplaces at least two pairs.")

q.matching(
    "Match the time expressions in Column I with the correct preposition in Column II:\n\n"
    "Column I:\n(a) __________ Monday\n(b) __________ 2015\n(c) __________ six o'clock\n"
    "(d) __________ ten years\n\n"
    "Column II:\n(i) at\n(ii) for\n(iii) on\n(iv) in\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
     "(a)-(iv), (b)-(iii), (c)-(i), (d)-(ii)",
     "(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)",
     "(a)-(i), (b)-(iv), (c)-(iii), (d)-(ii)"],
    "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
    "Days take 'on', so (a)-(iii). Years take 'in', so (b)-(iv). Clock times take 'at', so (c)-(i). A "
    "stated duration takes 'for', so (d)-(ii). The other options give 'in' to Monday or 'at' to the year, "
    "and each misplaces at least two pairs. Remember that 'since' would replace 'in' before 2015 only "
    "when a perfect tense makes it a starting point.")

# ---------------------------------------------------------- multiple correct
q.multi(
    "Which of the following are sentences that use the preposition correctly?\n\n"
    "(i) He is married with a teacher.\n(ii) She apologised for the delay.\n"
    "(iii) They complied with the order.\n(iv) The train arrived at the station.\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii), (iii) and (iv) all use the correct collocations: apologise for, comply with and arrive at. (i) "
    "is wrong: one is married 'to' a person, not 'with', and 'married with' is a common transfer error "
    "from other languages. Every option containing (i) is therefore incorrect.")

q.multi(
    "Which of the following are correct uses of 'since' and 'for'?\n\n"
    "(i) She has worked here since 2019.\n(ii) He has waited for two hours.\n"
    "(iii) They have lived in Jammu for last March.\n(iv) I have known him since childhood.\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (ii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are all correct: 'since' takes the points 2019 and childhood, while 'for' takes "
    "the duration 'two hours'. (iii) is wrong: 'last March' is a point in time, so it requires 'since', "
    "and 'for last March' is ungrammatical. Every option containing (iii) is incorrect.")

q.multi(
    "Which of the following are verbs that take a direct object with no preposition?\n\n"
    "(i) discuss\n(ii) enter\n(iii) listen\n(iv) reach\n\n"
    "Select the correct combination:",
    ["(ii), (iii) and (iv)", "(i), (ii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are transitive and take a direct object with no preposition: discuss the matter, "
    "enter the room and reach the station. (iii) is wrong: 'listen' requires 'to' before its object, as "
    "in 'listen to the radio'. Every option containing (iii) is therefore incorrect, and 'enter into' is "
    "correct only in the abstract sense of entering into an agreement.")

q.multi(
    "Which of the following are correct pairings of adjective and preposition?\n\n"
    "(i) superior than\n(ii) afraid of\n(iii) similar to\n(iv) capable of\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii), (iii) and (iv) are all standard: afraid of, similar to and capable of. (i) is wrong: 'superior' "
    "takes 'to' and never 'than', and the same holds for 'inferior', 'senior' and 'junior', all of which "
    "are Latin comparatives that reject 'than'. Every option containing (i) is therefore incorrect.")

emit(q, subject="A", topic="Uses of Prepositions (Revision)",
     path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "tests", "56_test_A_prepositions-rev.json"))
