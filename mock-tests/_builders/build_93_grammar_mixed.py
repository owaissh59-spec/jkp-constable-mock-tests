#!/usr/bin/env python3
"""Test 93 — Mixed Grammar Revision: Articles, Clauses, Pronouns, Tenses. 50 Q, Section A.

Replaces the former "Comprehension Passage (Revision)" test. The Constable
syllabus prescribes no comprehension passages for Section A, and the steering
prompt forbids generating them outright. This revision slot now sweeps four
prescribed areas instead.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _qbuild import Q, emit  # noqa: E402

q = Q()

# ------------------------------------------------------------ articles (6 S)
q.single("Choose the correct article: He is __________ honest officer whom everyone respects.",
         ["an", "a", "the", "no article"],
         "an",
         "The choice of article depends on the initial sound, not the initial letter, and 'honest' begins "
         "with a vowel sound because the h is silent, so 'an' is required. 'A' is wrong precisely because "
         "it follows the spelling rather than the pronunciation. 'The' is wrong because the officer is "
         "being introduced rather than identified. Omitting the article is wrong because a singular "
         "countable noun needs one.")

q.single("Choose the correct article: She plays __________ violin beautifully.",
         ["the", "a", "an", "no article"],
         "the",
         "Names of musical instruments take the definite article after 'play', so 'play the violin' is "
         "correct. 'A' is wrong because it would introduce one unspecified violin rather than the "
         "instrument as a class. 'An' is wrong on the same ground and also mismatches the consonant "
         "sound. Omitting the article is wrong here, though it is correct with games, as in 'play cricket'.")

q.single("Choose the correct article: __________ Ganga is regarded as the holiest river in India.",
         ["The", "A", "An", "No article"],
         "The",
         "Names of rivers take the definite article, so 'the Ganga' is correct. 'A' and 'An' are both "
         "wrong because a proper noun naming a unique river cannot take an indefinite article. Omitting "
         "the article is wrong for rivers, although it is right for most lakes and individual mountains, "
         "as in 'Lake Wular' and 'Mount Everest'.")

q.single("Choose the correct article: He was appointed __________ captain of the team.",
         ["no article", "a", "an", "the"],
         "no article",
         "When a title or unique office follows verbs such as 'appoint', 'elect' or 'make', the article is "
         "dropped, so 'appointed captain' is correct. 'A' and 'An' are wrong because they would treat the "
         "captaincy as one of several. 'The' is wrong in this construction, although it would be needed in "
         "a descriptive sentence such as 'He is the captain of the team'.")

q.single("Choose the correct article: __________ rich are not always happy.",
         ["The", "A", "An", "No article"],
         "The",
         "An adjective used as a plural noun to denote a whole class takes the definite article, so 'the "
         "rich' means rich people generally. 'A' and 'An' are wrong because they are singular and cannot "
         "introduce a class. Omitting the article is wrong because 'rich' alone is an adjective and cannot "
         "serve as the subject without 'the'.")

q.single("Choose the correct article: We travelled by __________ train to Katra last week.",
         ["no article", "a", "the", "an"],
         "no article",
         "Means of transport after the preposition 'by' take no article, so 'by train', 'by bus' and 'by "
         "air' are all correct. 'A' and 'An' are wrong because the phrase names the mode of travel rather "
         "than a particular vehicle. 'The' is wrong for the same reason, though 'on the train' would be "
         "acceptable when a specific train is meant.")

# ------------------------------------------------------------- pronouns (6 S)
q.single("Choose the correct pronoun: The award was shared between Rakesh and __________.",
         ["me", "I", "myself", "mine"],
         "me",
         "'Between' is a preposition, so it takes the objective form 'me'. 'I' is wrong because it is the "
         "subject form and cannot follow a preposition, even though 'between Rakesh and I' is often heard. "
         "'Myself' is wrong because a reflexive pronoun needs the same person as subject earlier in the "
         "clause. 'Mine' is wrong because it is possessive and does not name a person.")

q.single("Choose the correct pronoun: Each of the candidates must submit __________ own application.",
         ["his or her", "their", "its", "theirs"],
         "his or her",
         "'Each' is singular, so it requires a singular possessive, and 'his or her' preserves that "
         "agreement in formal writing. 'Their' is widely used in speech but breaks strict number "
         "agreement with 'each', which examinations still test. 'Its' is wrong because it refers to things "
         "rather than people. 'Theirs' is wrong because it cannot stand before a noun.")

q.single("Choose the correct pronoun: It was __________ who first reported the incident.",
         ["he", "him", "his", "himself"],
         "he",
         "After the verb 'be' English takes the subject form as the complement, so 'It was he' is the "
         "correct formal construction. 'Him' is common in speech but is the objective form and so is "
         "avoided in formal writing. 'His' is wrong because it is possessive. 'Himself' is wrong because a "
         "reflexive pronoun cannot serve as the complement of 'be' here.")

q.single("Choose the correct relative pronoun: The constable __________ courage saved the child was "
         "honoured.",
         ["whose", "who", "whom", "which"],
         "whose",
         "'Whose' is the possessive relative pronoun and is needed because the courage belongs to the "
         "constable. 'Who' is wrong because it is the subject form and cannot show possession. 'Whom' is "
         "wrong because it is the object form and equally cannot show possession. 'Which' is wrong because "
         "it refers to things and animals rather than to people.")

q.single("Choose the correct pronoun: Neither of the two brothers has finished __________ work.",
         ["his", "their", "its", "our"],
         "his",
         "'Neither' is singular and, referring to two brothers, takes the singular masculine possessive "
         "'his'. 'Their' is wrong because it is plural and clashes with the singular verb 'has' already in "
         "the sentence. 'Its' is wrong because it refers to things, not people. 'Our' is wrong because it "
         "shifts to the first person, which no earlier word in the sentence supports.")

q.single("Choose the correct pronoun: She is the girl __________ I met at the seminar.",
         ["whom", "who", "whose", "which"],
         "whom",
         "The relative pronoun is the object of 'met', so the object form 'whom' is required in formal "
         "usage. 'Who' is the subject form and is common informally but is the tested error here. 'Whose' "
         "is wrong because nothing in the clause belongs to the girl. 'Which' is wrong because it cannot "
         "refer to a person.")

# --------------------------------------------------------------- tenses (7 S)
q.single("Choose the correct verb form: He __________ in this department since 2018.",
         ["has been working", "is working", "works", "worked"],
         "has been working",
         "'Since 2018' names a point in the past from which the action continues into the present, which "
         "calls for the present perfect continuous. 'Is working' is wrong because the present continuous "
         "describes only what is happening now and cannot span from 2018. 'Works' is wrong because the "
         "simple present states a habit without duration. 'Worked' is wrong because the simple past closes "
         "the action off.")

q.single("Choose the correct verb form: By the time the ambulance arrived, the injured man __________.",
         ["had died", "died", "has died", "was dying"],
         "had died",
         "Two past events are involved, and the death came first, so the earlier one takes the past "
         "perfect 'had died'. 'Died' is wrong because the simple past would leave the sequence unmarked. "
         "'Has died' is wrong because the present perfect cannot be used with a stated past time. 'Was "
         "dying' is wrong because it describes an action in progress and contradicts the completed sense.")

q.single("Choose the correct verb form: If it __________ tomorrow, the parade will be postponed.",
         ["rains", "will rain", "rained", "would rain"],
         "rains",
         "In a first conditional the 'if' clause takes the simple present even though it refers to the "
         "future, while the main clause takes 'will'. 'Will rain' is wrong because 'will' is not used in "
         "the 'if' clause of this pattern. 'Rained' and 'would rain' are wrong because they belong to the "
         "second conditional, which pairs the past form with 'would' for hypothetical situations.")

q.single("Choose the correct verb form: She said that she __________ the report the previous day.",
         ["had submitted", "has submitted", "submitted", "submits"],
         "had submitted",
         "The reporting verb 'said' is in the past, and the action being reported happened earlier still, "
         "so the past perfect 'had submitted' is required. 'Has submitted' is wrong because the present "
         "perfect does not follow a past reporting verb. 'Submitted' is wrong because it fails to show "
         "that one past action preceded another. 'Submits' is wrong because the simple present clashes "
         "with 'the previous day'.")

q.single("Choose the correct verb form: Look at those clouds — it __________ shortly.",
         ["is going to rain", "rains", "rained", "has rained"],
         "is going to rain",
         "Present evidence pointing to a future event calls for 'going to', so 'it is going to rain' is "
         "correct. 'Rains' is wrong because the simple present states habits or timetabled events, not "
         "predictions from evidence. 'Rained' is wrong because it refers to completed past time. 'Has "
         "rained' is wrong because the present perfect looks back rather than forward.")

q.single("Choose the correct verb form: He __________ his breakfast when the telephone rang.",
         ["was having", "had", "has had", "has been having"],
         "was having",
         "An action in progress that is interrupted by a sudden past event takes the past continuous, so "
         "'was having' is correct. 'Had' is wrong because the simple past would suggest the meal was "
         "complete before the call. 'Has had' and 'has been having' are both wrong because present perfect "
         "forms cannot be used with a definite past time such as 'when the telephone rang'.")

q.single("Choose the correct verb form: The train __________ at six o'clock every morning.",
         ["leaves", "is leaving", "has left", "left"],
         "leaves",
         "Timetabled events take the simple present, so 'the train leaves at six' is correct. 'Is leaving' "
         "is wrong because the present continuous suits a single arranged occasion rather than a daily "
         "schedule. 'Has left' is wrong because the present perfect reports a completed departure. 'Left' "
         "is wrong because the simple past cannot express a repeated daily event.")

# -------------------------------------------------------------- clauses (6 S)
q.single("Identify the type of the underlined clause: 'I know THAT HE IS INNOCENT.'",
         ["Noun clause", "Adjective clause", "Adverb clause", "Main clause"],
         "Noun clause",
         "The clause answers 'what do I know?' and so functions as the object of the verb 'know', which "
         "makes it a noun clause. It is not an adjective clause because it does not describe a preceding "
         "noun. It is not an adverb clause because it gives no information about time, place, reason or "
         "manner. It is not the main clause, since 'I know' carries the principal statement.")

q.single("Identify the type of the underlined clause: 'The house WHERE I WAS BORN has been demolished.'",
         ["Adjective clause", "Noun clause", "Adverb clause", "Main clause"],
         "Adjective clause",
         "The clause modifies the noun 'house', telling us which house is meant, so it is an adjective "
         "clause introduced by the relative adverb 'where'. It is not a noun clause because it is not "
         "acting as a subject or object. It is not an adverb clause because it qualifies a noun rather "
         "than a verb. It is not the main clause, which is 'The house has been demolished'.")

q.single("Identify the type of the underlined clause: 'He left early BECAUSE HE WAS UNWELL.'",
         ["Adverb clause of reason", "Noun clause", "Adjective clause", "Adverb clause of time"],
         "Adverb clause of reason",
         "The clause explains why he left, so it is an adverb clause of reason, introduced by 'because'. "
         "It is not a noun clause because it does not fill a subject or object slot. It is not an "
         "adjective clause because it modifies the verb 'left' rather than a noun. It is not an adverb "
         "clause of time, which would answer 'when' and be introduced by words such as 'when' or 'after'.")

q.single("Choose the sentence that contains a subordinate clause.",
         ["Although he was tired, he completed the patrol.",
          "He was tired and he completed the patrol.",
          "He was tired but completed the patrol.",
          "He was tired; he completed the patrol."],
         "Although he was tired, he completed the patrol.",
         "'Although he was tired' cannot stand alone and depends on the main clause, which makes it "
         "subordinate. The version joined by 'and' contains two independent clauses of equal rank. The "
         "version with 'but completed' has a compound predicate and only one clause. The version divided "
         "by a semicolon again has two independent clauses, neither subordinate to the other.")

q.single("Identify the type of the underlined clause: 'WHOEVER BREAKS THE RULE will be punished.'",
         ["Noun clause", "Adjective clause", "Adverb clause", "Main clause"],
         "Noun clause",
         "The clause acts as the subject of 'will be punished', and a clause filling a subject slot is a "
         "noun clause. It is not an adjective clause because there is no preceding noun for it to "
         "describe. It is not an adverb clause because it does not modify the verb with circumstance. It "
         "is not the main clause, whose predicate is 'will be punished'.")

q.single("Choose the sentence in which the clause is correctly joined.",
         ["He said that he would come the next day.",
          "He said that would he come the next day.",
          "He said what he would come the next day.",
          "He said that he will come the next day."],
         "He said that he would come the next day.",
         "A noun clause after 'said' keeps normal statement order and shifts 'will' to 'would' after a "
         "past reporting verb. Inverting to 'would he come' turns the clause into a question, which a "
         "noun clause does not do. 'What' is wrong because the clause is not asking about a thing. "
         "Retaining 'will' fails the sequence of tenses after the past 'said'.")

# --------------------------------------------------------------- fill blanks
q.blank("Fill in the blank with the correct article: She bought __________ umbrella and a raincoat "
        "before the monsoon.",
        ["an", "a", "the", "no article"],
        "an",
        "'Umbrella' begins with the vowel sound /ʌ/, so it takes 'an'. 'A' is wrong because it precedes "
        "consonant sounds, and the contrast with 'a raincoat' in the same sentence makes the rule plain. "
        "'The' is wrong because the umbrella is being mentioned for the first time. Omitting the article "
        "is wrong because a singular countable noun requires one.")

q.blank("Fill in the blank with the correct verb form: They __________ for two hours before the bus "
        "finally arrived.",
        ["had been waiting", "have been waiting", "are waiting", "wait"],
        "had been waiting",
        "The waiting continued up to a point in the past, which calls for the past perfect continuous "
        "'had been waiting'. 'Have been waiting' is wrong because the present perfect continuous runs up "
        "to the present, not to a past moment. 'Are waiting' is wrong because the present continuous "
        "cannot precede a past event. 'Wait' is wrong because the simple present expresses no duration.")

# ---------------------------------------------------------------- statements
q.statement(
    "Consider the following statements about articles:\n\n"
    "(i) 'An' is used before a word beginning with a vowel letter regardless of its sound.\n"
    "(ii) Names of rivers take the definite article.\n"
    "(iii) Means of transport after 'by' take no article.\n"
    "(iv) An adjective denoting a class takes 'the', as in 'the poor'.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii), (iii) and (iv) are all correct rules. (i) is wrong because the choice depends on sound, not "
    "spelling: 'a university' takes 'a' despite the vowel letter, while 'an hour' takes 'an' despite the "
    "consonant letter. Every option containing (i) is therefore incorrect, and this sound-versus-letter "
    "distinction is the single most tested point about articles.")

q.statement(
    "Consider the following statements about pronouns:\n\n"
    "(i) A pronoun following a preposition takes the objective form.\n"
    "(ii) 'Each' and 'neither' are singular and take singular pronouns.\n"
    "(iii) 'Whose' is the possessive relative pronoun.\n"
    "(iv) 'Who' is the correct form when the relative pronoun is the object of a verb.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i), (ii) and (iii) are all correct. (iv) is wrong: when the relative pronoun is the object of a "
    "verb the formal choice is 'whom', as in 'the girl whom I met', while 'who' is the subject form. Every "
    "option containing (iv) is therefore incorrect, even though 'who' is widely used for both in "
    "conversation.")

q.statement(
    "Consider the following statements about tenses:\n\n"
    "(i) 'Will' is used in the 'if' clause of a first conditional.\n"
    "(ii) 'Since' with a perfect tense marks a point in time.\n"
    "(iii) The past perfect marks the earlier of two past actions.\n"
    "(iv) Timetabled events take the simple present.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (iii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii), (iii) and (iv) are all correct. (i) is wrong: the first conditional puts the simple present in "
    "the 'if' clause and 'will' in the main clause, so 'If it rains, the parade will be postponed' is the "
    "pattern, and 'If it will rain' is a standard error. Every option containing (i) is therefore "
    "incorrect.")

q.statement(
    "Consider the following statements about clauses:\n\n"
    "(i) A noun clause can act as the subject of a sentence.\n"
    "(ii) An adjective clause modifies a noun or pronoun.\n"
    "(iii) A subordinate clause can stand alone as a sentence.\n"
    "(iv) An adverb clause can express reason, time or condition.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (ii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are all correct descriptions. (iii) is wrong and states the defining feature "
    "backwards: a subordinate clause is precisely one that cannot stand alone and depends on a main "
    "clause, as 'Although he was tired' shows. Every option containing (iii) is therefore incorrect.")

q.statement(
    "Consider the following statements about the sentence 'By the time we reached, the train had left':\n\n"
    "(i) 'Had left' is in the past perfect tense.\n"
    "(ii) The departure happened before the arrival.\n"
    "(iii) 'Had left' should be replaced by 'has left'.\n"
    "(iv) The sentence contains two past events in sequence.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (ii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are correct: 'had left' is the past perfect, it marks the earlier of the two past "
    "events, and the sentence sets those events in sequence. (iii) is wrong because the present perfect "
    "'has left' cannot be used alongside a stated past time such as 'by the time we reached'. Every option "
    "containing (iii) is therefore incorrect.")

q.statement(
    "Consider the following statements about the sentence 'It was he who reported the incident':\n\n"
    "(i) 'He' is correct because the complement of 'be' takes the subject form.\n"
    "(ii) 'Who' correctly introduces an adjective clause.\n"
    "(iii) 'Him' would be the preferred form in formal writing.\n"
    "(iv) The sentence is grammatically complete as it stands.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are correct: after 'be' the subject form is used formally, 'who' introduces a "
    "clause describing 'he', and nothing is missing from the sentence. (iii) is wrong: 'It was him' is "
    "common in speech but is not the preferred formal choice, which is exactly the point being tested. "
    "Every option containing (iii) is therefore incorrect.")

q.statement(
    "Consider the following statements about agreement:\n\n"
    "(i) 'Each of the students has submitted the form' is correct.\n"
    "(ii) 'Neither of the brothers have arrived' is correct.\n"
    "(iii) 'The news is disturbing' is correct.\n"
    "(iv) 'Furniture' is an uncountable noun and takes a singular verb.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(i), (iii) and (iv)",
    "(i), (iii) and (iv) are correct: 'each of' takes a singular verb, 'news' is singular despite the "
    "final s, and 'furniture' is uncountable. (ii) is wrong because 'neither of' is singular and requires "
    "'has arrived', not 'have arrived'. Every option containing (ii) is therefore incorrect.")

q.statement(
    "Consider the following statements about the sentence 'He was appointed captain of the team':\n\n"
    "(i) The article is correctly omitted before 'captain'.\n"
    "(ii) Titles following 'appoint' or 'elect' drop the article.\n"
    "(iii) 'A captain' would be equally correct here.\n"
    "(iv) The sentence is in the passive voice construction of 'appoint'.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (ii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are correct: the article is rightly dropped, that omission is the rule after verbs "
    "such as 'appoint' and 'elect', and 'was appointed' is indeed a passive construction. (iii) is wrong "
    "because inserting 'a' would treat a unique office as one of several and breaks the rule stated in "
    "(ii). Every option containing (iii) is therefore incorrect.")

# --------------------------------------------- assertion-reason (0,0,1,2,3)
q.ar("'An hour' is correct although 'hour' begins with a consonant letter.",
     "The choice between 'a' and 'an' depends on the initial sound of the following word, not its initial "
     "letter.",
     0,
     "(A) is correct — the h in 'hour' is silent, so the word opens with a vowel sound and takes 'an'. (R) "
     "is correct — sound, not spelling, governs the choice. (R) also explains (A): it states the very rule "
     "that produces the form. The option denying the explanatory link is therefore wrong, and the two "
     "options rejecting either statement are wrong because both are accurate.")

q.ar("In 'The house where I was born has been demolished', the clause 'where I was born' is an adjective "
     "clause.",
     "The clause tells us which house is meant and so modifies the noun 'house'.",
     0,
     "(A) is correct — a clause that qualifies a noun is an adjective clause, whatever word introduces it. "
     "(R) is correct — the clause identifies the particular house. (R) also explains (A), because "
     "modifying a noun is precisely what makes a clause adjectival. The option denying the link is wrong, "
     "and the options rejecting either statement are wrong since both are true.")

q.ar("'Between you and me' is the correct form rather than 'between you and I'.",
     "'Me' is the first person singular pronoun in English.",
     1,
     "(A) is correct — 'between' is a preposition and takes the objective form. (R) is also correct as a "
     "bare statement of fact about 'me'. But (R) does not explain (A): the reason the objective form is "
     "needed is that prepositions govern the objective case, which the reason never mentions. Both stand, "
     "yet the reason fails to account for the assertion.")

q.ar("The past perfect tense marks the earlier of two related past actions.",
     "The past perfect is formed with 'was' or 'were' followed by the present participle.",
     2,
     "(A) is correct — 'had left' before 'we reached' shows the departure came first. (R) is NOT correct: "
     "that description belongs to the past continuous, whereas the past perfect is formed with 'had' "
     "followed by the past participle. Since the assertion stands and the reason falls, the options "
     "claiming both are correct are wrong, as is the option calling the assertion incorrect.")

q.ar("A subordinate clause can stand on its own as a complete sentence.",
     "A main clause contains a subject and a predicate and can stand on its own.",
     3,
     "(A) is NOT correct — the defining feature of a subordinate clause is that it depends on a main "
     "clause and cannot stand alone, as 'Because he was unwell' shows. (R) is correct — it is the main "
     "clause that is independent, and stating this is what exposes the error in the assertion. Since the "
     "assertion falls and the reason stands, the options claiming both are correct are wrong.")

# ---------------------------------------------------------------- matching
q.matching(
    "Match the clauses in Column I with their types in Column II:\n\n"
    "Column I:\n(a) that he is innocent\n(b) where I was born\n(c) because he was unwell\n"
    "(d) whoever breaks the rule\n\n"
    "Column II:\n(i) Adverb clause of reason\n(ii) Noun clause acting as object\n"
    "(iii) Noun clause acting as subject\n(iv) Adjective clause\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)",
     "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
     "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)",
     "(a)-(iv), (b)-(ii), (c)-(i), (d)-(iii)"],
    "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)",
    "'That he is innocent' answers 'what do I know' and so is a noun clause used as object, giving "
    "(a)-(ii). 'Where I was born' qualifies the noun 'house', so (b)-(iv). 'Because he was unwell' gives "
    "the reason, so (c)-(i). 'Whoever breaks the rule' fills the subject slot, so (d)-(iii). The other "
    "options confuse the two noun-clause functions or make the reason clause adjectival, and each "
    "misplaces at least two pairs.")

q.matching(
    "Match the tenses in Column I with the sentences in Column II:\n\n"
    "Column I:\n(a) Present perfect continuous\n(b) Past perfect\n(c) Past continuous\n"
    "(d) Simple present\n\n"
    "Column II:\n(i) The train leaves at six every morning.\n(ii) He was having breakfast when the phone rang.\n"
    "(iii) He has been working here since 2018.\n(iv) The train had left before we reached.\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)",
     "(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)",
     "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
     "(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)"],
    "(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)",
    "'Has been working … since 2018' is present perfect continuous, so (a)-(iii). 'Had left' is past "
    "perfect, so (b)-(iv). 'Was having … when the phone rang' is past continuous, so (c)-(ii). 'Leaves at "
    "six every morning' is the simple present used for a timetable, so (d)-(i). The other options swap the "
    "perfect forms or hand the timetable sentence to the continuous, and each misassigns at least two pairs.")

q.matching(
    "Match the pronouns in Column I with their types in Column II:\n\n"
    "Column I:\n(a) himself\n(b) whose\n(c) me\n(d) each\n\n"
    "Column II:\n(i) Objective personal pronoun\n(ii) Distributive pronoun\n"
    "(iii) Reflexive pronoun\n(iv) Possessive relative pronoun\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
     "(a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)",
     "(a)-(i), (b)-(iv), (c)-(iii), (d)-(ii)",
     "(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)"],
    "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
    "'Himself' is reflexive, so (a)-(iii). 'Whose' is the possessive relative pronoun, so (b)-(iv). 'Me' "
    "is the objective form of the first person pronoun, so (c)-(i). 'Each' is distributive, referring to "
    "members of a group singly, so (d)-(ii). The other options make 'me' relative or 'each' objective, "
    "and each therefore misplaces at least two pairs.")

q.matching(
    "Match the article rules in Column I with the examples in Column II:\n\n"
    "Column I:\n(a) No article with means of transport after 'by'\n(b) Definite article with rivers\n"
    "(c) 'An' before a vowel sound\n(d) No article before a unique office after 'appoint'\n\n"
    "Column II:\n(i) an hour\n(ii) He was appointed captain.\n(iii) by train\n(iv) the Ganga\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
     "(a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)",
     "(a)-(i), (b)-(iv), (c)-(iii), (d)-(ii)",
     "(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)"],
    "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
    "'By train' shows the dropped article with transport, so (a)-(iii). 'The Ganga' shows the definite "
    "article with rivers, so (b)-(iv). 'An hour' shows 'an' before a vowel sound, so (c)-(i). 'He was "
    "appointed captain' shows the dropped article before a unique office, so (d)-(ii). The other options "
    "swap 'an hour' with 'the Ganga' or with 'by train', and each misplaces at least two pairs.")

q.matching(
    "Match the sentences in Column I with the grammatical point they illustrate in Column II:\n\n"
    "Column I:\n(a) Each of the students has submitted the form.\n(b) If it rains, the parade will be postponed.\n"
    "(c) She is the girl whom I met.\n(d) The rich are not always happy.\n\n"
    "Column II:\n(i) Adjective used as a plural noun with 'the'\n(ii) Singular verb after 'each of'\n"
    "(iii) Objective relative pronoun\n(iv) First conditional\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)",
     "(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)",
     "(a)-(i), (b)-(iv), (c)-(iii), (d)-(ii)",
     "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)"],
    "(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)",
    "'Each of the students has' shows the singular verb after 'each of', so (a)-(ii). 'If it rains … will "
    "be postponed' is the first conditional, so (b)-(iv). 'Whom I met' shows the objective relative "
    "pronoun, so (c)-(iii). 'The rich' shows an adjective used as a plural noun, so (d)-(i). Each of the "
    "other options misassigns at least two of these pairs.")

# ---------------------------------------------------------- multiple correct
q.multi(
    "Which of the following are correct uses of the article?\n\n"
    "(i) He is an honest man.\n(ii) She plays the violin.\n(iii) We travelled by the train.\n"
    "(iv) The Ganga is a sacred river.\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i) is correct because 'honest' opens with a vowel sound. (ii) is correct because instruments take "
    "'the' after 'play'. (iv) is correct because rivers take the definite article. (iii) is wrong: means "
    "of transport after 'by' take no article, so it should read 'by train'. Every option containing (iii) "
    "is therefore incorrect.")

q.multi(
    "Which of the following are grammatically correct?\n\n"
    "(i) Neither of the brothers has arrived.\n(ii) Between you and I, the plan is risky.\n"
    "(iii) It was he who reported the matter.\n(iv) The constable whose courage saved the child was honoured.\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(i), (iii) and (iv)",
    "(i) is correct because 'neither of' takes a singular verb. (iii) is correct because the complement of "
    "'be' takes the subject form in formal usage. (iv) is correct because 'whose' shows possession. (ii) "
    "is wrong: 'between' is a preposition and requires 'me', so it should read 'between you and me'. Every "
    "option containing (ii) is therefore incorrect.")

q.multi(
    "Which of the following are subordinate clauses?\n\n"
    "(i) Although he was tired\n(ii) because she had already left\n(iii) he completed the patrol\n"
    "(iv) that the file was missing\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "(i), (ii) and (iv)"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) all begin with subordinating words — 'although', 'because' and 'that' — and none "
    "can stand alone as a sentence. (iii) is wrong: 'he completed the patrol' has a subject and a "
    "predicate and is perfectly complete on its own, so it is a main clause. Every option containing (iii) "
    "is therefore incorrect.")

q.multi(
    "Which of the following are correct with respect to the sequence of tenses?\n\n"
    "(i) He said that he would come the next day.\n(ii) She said that she had submitted the report.\n"
    "(iii) He said that he will come the next day.\n(iv) By the time we arrived, the train had left.\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) all observe the sequence of tenses: after a past reporting verb, 'will' becomes "
    "'would' and an earlier action takes the past perfect. (iii) is wrong because it keeps 'will' after "
    "the past 'said', which breaks the sequence and should read 'would come'. Every option containing "
    "(iii) is therefore incorrect.")

q.multi(
    "Which of the following are correct verb forms for the context given?\n\n"
    "(i) He has been working here since 2018.\n(ii) If it will rain, the parade will be postponed.\n"
    "(iii) The train leaves at six every morning.\n(iv) He was having breakfast when the phone rang.\n\n"
    "Select the correct combination:",
    ["(ii), (iii) and (iv)", "(i), (ii) and (iii)", "(i), (iii) and (iv)", "All of the above"],
    "(i), (iii) and (iv)",
    "(i) is correct because 'since' with a perfect continuous marks a point of origin. (iii) is correct "
    "because timetables take the simple present. (iv) is correct because an interrupted past action takes "
    "the past continuous. (ii) is wrong: the first conditional puts the simple present in the 'if' clause, "
    "so it should read 'If it rains'. Every option containing (ii) is therefore incorrect.")

emit(q, subject="A",
     topic="Mixed Grammar Revision — Articles, Clauses, Pronouns, Tenses",
     path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "tests", "93_test_A_grammar-mixed-rev.json"))
