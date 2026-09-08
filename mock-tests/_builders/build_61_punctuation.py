#!/usr/bin/env python3
"""Test 61 — Punctuation (Comma, Semicolon, Colon, Apostrophe). 30 Q, Section A.

Replaces the former "Active/Passive Voice" test. Voice is not among the ten areas
the Constable syllabus prescribes for Section A; punctuation is, and was covered
by only one earlier test, so this slot now strengthens a thin area.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _qbuild import Q, emit  # noqa: E402

q = Q()

q.single(
    "Which of the following sentences uses the comma correctly?",
    ["My brother, who lives in Jammu, is a police officer.",
     "My brother who lives in Jammu, is a police officer.",
     "My brother, who lives in Jammu is a police officer.",
     "My brother who, lives in Jammu, is a police officer."],
    "My brother, who lives in Jammu, is a police officer.",
    "A non-defining relative clause — one that adds extra information rather than identifying which "
    "brother is meant — must be enclosed by a pair of commas, so both the opening and the closing comma "
    "are required. Omitting the first comma leaves the clause half-fenced. Omitting the closing comma "
    "runs the clause into the main verb. Placing a comma after 'who' separates the subject from its own "
    "verb, which no punctuation rule permits.")

q.single(
    "Which sentence uses the apostrophe correctly?",
    ["The students' hostel was renovated last year.",
     "The students hostel was renovated last year.",
     "The student's hostel was renovated last year, for all forty of them.",
     "The students's hostel was renovated last year."],
    "The students' hostel was renovated last year.",
    "For a plural noun that already ends in -s, the possessive is formed by adding an apostrophe after "
    "the s, giving 'students''. Dropping the apostrophe altogether removes the possessive sense. "
    "'Student's' is singular and contradicts a hostel shared by forty students. 'Students's' doubles the "
    "s after a plural that already ends in one, which English never does.")

q.single(
    "Which sentence uses the semicolon correctly?",
    ["The rain stopped at noon; the match resumed an hour later.",
     "The rain stopped at noon; and the match resumed an hour later.",
     "Although the rain stopped at noon; the match was cancelled.",
     "The rain stopped at noon; because the ground was dry."],
    "The rain stopped at noon; the match resumed an hour later.",
    "A semicolon joins two closely related independent clauses without a conjunction, and each side here "
    "could stand alone as a sentence. Adding 'and' after the semicolon is redundant, since the semicolon "
    "already does the joining. Beginning with 'Although' makes the first part subordinate, so it cannot "
    "take a semicolon. 'Because the ground was dry' is likewise a subordinate clause, not an independent one.")

q.single(
    "Which sentence uses the colon correctly?",
    ["The kit contains three items: a torch, a whistle and a notebook.",
     "The kit contains: a torch, a whistle and a notebook.",
     "The kit: contains a torch, a whistle and a notebook.",
     "The kit contains three items; a torch, a whistle and a notebook."],
    "The kit contains three items: a torch, a whistle and a notebook.",
    "A colon introduces a list only after a grammatically complete clause, and 'The kit contains three "
    "items' is complete. Placing the colon directly after 'contains' interrupts the verb and its object. "
    "Placing it after 'The kit' severs the subject from its verb. A semicolon cannot introduce a list at "
    "all; that is precisely the colon's job.")

q.single(
    "Which sentence punctuates the direct speech correctly?",
    ["The officer said, \"Report at the station by six.\"",
     "The officer said \"Report at the station by six.\"",
     "The officer said, \"Report at the station by six\".",
     "The officer said: \"report at the station by six.\""],
    "The officer said, \"Report at the station by six.\"",
    "Direct speech takes a comma after the reporting verb, opens with a capital letter, and keeps the "
    "closing full stop inside the quotation marks. Omitting the comma after 'said' leaves the reporting "
    "clause unseparated. Placing the full stop outside the closing quotation mark misplaces terminal "
    "punctuation in this construction. Using a colon and a lower-case opening breaks both the standard "
    "convention and the capitalisation rule.")

q.single(
    "Choose the sentence in which 'its' and 'it's' are used correctly.",
    ["It's a long route, and the bus has lost its way twice.",
     "Its a long route, and the bus has lost it's way twice.",
     "It's a long route, and the bus has lost it's way twice.",
     "Its a long route, and the bus has lost its way twice."],
    "It's a long route, and the bus has lost its way twice.",
    "'It's' is the contraction of 'it is', which the first clause needs, while 'its' is the possessive "
    "determiner required before 'way'. The version beginning 'Its a long route' uses the possessive where "
    "a contraction belongs. The version with 'lost it's way' expands to 'lost it is way', which is "
    "meaningless. The version that gets both wrong compounds the same two errors.")

q.single(
    "Which sentence is correctly punctuated with commas in a series?",
    ["We bought pens, files, folders and staplers for the office.",
     "We bought pens files, folders and staplers for the office.",
     "We bought, pens, files, folders and staplers for the office.",
     "We bought pens, files, folders, and, staplers for the office."],
    "We bought pens, files, folders and staplers for the office.",
    "Items in a series are separated by commas, with the final pair joined by 'and' and no comma after "
    "it in British usage. Leaving out the comma between 'pens' and 'files' fails to separate the first "
    "two items. Placing a comma immediately after the verb 'bought' cuts the verb off from its object. "
    "Adding a comma after 'and' strands the conjunction between two commas.")

q.single(
    "Which sentence uses the hyphen correctly?",
    ["She is a well-known author in the region.",
     "She is a well known-author in the region.",
     "She is a well known author-in the region.",
     "She is a-well known author in the region."],
    "She is a well-known author in the region.",
    "A compound adjective placed before the noun it modifies is hyphenated, so 'well-known' joins to "
    "qualify 'author'. Hyphenating 'known-author' wrongly links the participle to the noun instead. "
    "Attaching the hyphen to 'author-in' joins a noun to a preposition, which serves no purpose. Placing "
    "it after the article in 'a-well' links a determiner to an adverb, which is never hyphenated.")

q.single(
    "Which sentence is correctly capitalised?",
    ["We travelled to Srinagar in March to meet Professor Ahmad.",
     "We travelled to srinagar in March to meet Professor Ahmad.",
     "We travelled to Srinagar in march to meet professor Ahmad.",
     "we travelled to Srinagar in March to meet Professor ahmad."],
    "We travelled to Srinagar in March to meet Professor Ahmad.",
    "Place names, month names, titles used before a name and the first word of a sentence all take "
    "capitals, and only this version applies all four rules. Writing 'srinagar' in lower case fails the "
    "place-name rule. Writing 'march' and 'professor' in lower case fails the month and title rules. "
    "Beginning with a lower-case 'we' and writing 'ahmad' fails the sentence-opening and personal-name rules.")

q.single(
    "Which of the following sentences contains a comma splice?",
    ["The siren sounded, everyone left the building.",
     "The siren sounded, and everyone left the building.",
     "When the siren sounded, everyone left the building.",
     "The siren sounded; everyone left the building."],
    "The siren sounded, everyone left the building.",
    "A comma splice is the error of joining two independent clauses with only a comma, which is exactly "
    "what the first version does. Adding the coordinating conjunction 'and' after the comma repairs it. "
    "Opening with 'When' makes the first clause subordinate, so the comma is then correct. Replacing the "
    "comma with a semicolon is the other standard repair, so that version is also correct.")

q.single(
    "Which sentence forms the possessive of a singular name ending in -s correctly?",
    ["This is Ramesh's file, not mine.",
     "This is Rameshs' file, not mine.",
     "This is Rameshs file, not mine.",
     "This is Ramesh' file, not mine."],
    "This is Ramesh's file, not mine.",
    "A singular noun takes apostrophe followed by s, so 'Ramesh's' is correct even though the name "
    "already ends in the sound of s. 'Rameshs'' treats the name as a plural, which it is not. 'Rameshs' "
    "has no apostrophe at all and so shows no possession. 'Ramesh'' uses a bare apostrophe, a form "
    "reserved for plurals that already end in s.")

q.single(
    "Which sentence uses a pair of dashes correctly to mark a parenthetical remark?",
    ["The three constables — all recent recruits — completed the drill.",
     "The three constables — all recent recruits, completed the drill.",
     "The three constables, all recent recruits — completed the drill.",
     "The three constables all recent recruits — completed the drill."],
    "The three constables — all recent recruits — completed the drill.",
    "A parenthetical insertion must be fenced by a matching pair of dashes, one before and one after. "
    "Closing with a comma instead of the second dash mismatches the pair. Opening with a comma and "
    "closing with a dash makes the same mismatch in reverse. Omitting the opening mark altogether leaves "
    "the insertion unseparated from the subject.")

q.single(
    "Which sentence is correctly punctuated?",
    ["He asked whether the report had been submitted.",
     "He asked whether the report had been submitted?",
     "He asked, whether the report had been submitted?",
     "He asked; whether the report had been submitted."],
    "He asked whether the report had been submitted.",
    "An indirect question reports a question rather than asking one, so it closes with a full stop and "
    "needs no comma before 'whether'. Ending with a question mark treats the reported statement as a "
    "direct question. Adding a comma after 'asked' as well as the question mark compounds that error. A "
    "semicolon cannot introduce a subordinate clause beginning with 'whether'.")

q.single(
    "Which sentence correctly punctuates the introductory element?",
    ["After the long march, the recruits rested for an hour.",
     "After the long march the recruits, rested for an hour.",
     "After, the long march the recruits rested for an hour.",
     "After the long march the recruits rested, for an hour."],
    "After the long march, the recruits rested for an hour.",
    "An introductory adverbial phrase is followed by a comma, which marks where the main clause begins. "
    "Placing the comma after 'recruits' separates the subject from its verb. Placing it after 'After' "
    "cuts the preposition from its own object. Placing it before 'for an hour' isolates a phrase that "
    "belongs to the verb without any need for punctuation.")

q.single(
    "Which sentence punctuates 'however' correctly when it joins two independent clauses?",
    ["The road was blocked; however, we reached on time.",
     "The road was blocked, however, we reached on time.",
     "The road was blocked however; we reached on time.",
     "The road was blocked, however we reached on time."],
    "The road was blocked; however, we reached on time.",
    "'However' is a conjunctive adverb, not a coordinating conjunction, so it cannot join two independent "
    "clauses with a comma alone; a semicolon precedes it and a comma follows it. Using commas on both "
    "sides produces a comma splice. Placing the semicolon after 'however' attaches the adverb to the "
    "wrong clause. Using a single comma before 'however' with no semicolon leaves the splice unrepaired.")

# ---------------------------------------------------------------- fill blank
q.blank(
    "Fill in the blank with the correct punctuation mark: The notice was clear__________ no vehicle may "
    "be parked beyond this point.",
    [": (colon)", ", (comma)", "; (semicolon)", "! (exclamation mark)"],
    ": (colon)",
    "A colon is used when the first clause is complete and the words that follow explain, expand or spell "
    "out what it announced, which is what the second half does here. A comma would create a comma splice "
    "between two independent clauses. A semicolon links two equal statements but does not signal that the "
    "second explains the first. An exclamation mark would end the sentence and destroy the connection "
    "altogether.")

# ---------------------------------------------------------------- statements
q.statement(
    "Consider the following statements about the use of the comma:\n\n"
    "(i) A comma alone may join two independent clauses.\n"
    "(ii) A comma is used after an introductory adverbial phrase.\n"
    "(iii) A pair of commas encloses a non-defining relative clause.\n"
    "(iv) A comma separates items in a series.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(ii), (iii) and (iv)",
    "(ii) is correct — an introductory phrase such as 'After the long march' is followed by a comma. "
    "(iii) is correct — a non-defining clause takes a comma at each end. (iv) is correct — commas "
    "separate items in a series. (i) is wrong: joining two independent clauses with a comma alone is the "
    "comma-splice error, and it requires either a coordinating conjunction, a semicolon or a full stop. "
    "Every option containing (i) is therefore incorrect.")

q.statement(
    "Consider the following statements about the apostrophe:\n\n"
    "(i) It marks the omission of letters in a contraction.\n"
    "(ii) A plural noun ending in -s takes an apostrophe after the s to show possession.\n"
    "(iii) The possessive 'its' is written with an apostrophe.\n"
    "(iv) A singular noun normally takes apostrophe followed by s.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iv)", "(i), (ii) and (iii)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i) is correct — the apostrophe stands in for the missing letters in forms such as 'can't'. (ii) is "
    "correct — 'the students' hostel' places the apostrophe after the plural s. (iv) is correct — a "
    "singular noun takes 's, as in 'the boy's cap'. (iii) is wrong: the possessive is 'its' with no "
    "apostrophe, while 'it's' is only ever the contraction of 'it is' or 'it has'. Every option "
    "containing (iii) fails.")

q.statement(
    "Consider the following statements about the semicolon and the colon:\n\n"
    "(i) A semicolon can join two independent clauses without a conjunction.\n"
    "(ii) A colon may follow an incomplete clause to introduce a list.\n"
    "(iii) A colon can introduce an explanation of the clause before it.\n"
    "(iv) A semicolon can separate items in a list that already contains commas.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "All of the above"],
    "(i), (iii) and (iv)",
    "(i) is correct — that is the semicolon's primary use. (iii) is correct — a colon can introduce an "
    "explanation or expansion of what precedes it. (iv) is correct — semicolons keep long list items "
    "apart when those items already contain internal commas. (ii) is wrong: a colon must follow a "
    "grammatically complete clause, so 'The kit contains: a torch' is faulty. Every option containing "
    "(ii) is therefore incorrect.")

q.statement(
    "Consider the following statements about quotation marks:\n\n"
    "(i) A comma normally precedes the opening quotation mark of direct speech.\n"
    "(ii) The first word of quoted speech begins with a capital letter.\n"
    "(iii) Quotation marks are used to enclose the exact words spoken.\n"
    "(iv) Quotation marks are required in indirect speech.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — a comma separates the reporting verb from the quotation, as in 'He said, \"Wait\"'. "
    "(ii) is correct — quoted speech opens with a capital. (iii) is correct — quotation marks enclose the "
    "exact words uttered. (iv) is wrong: indirect speech reports the sense rather than the exact words, "
    "so it takes no quotation marks at all. Every option containing (iv) is incorrect.")

q.statement(
    "Consider the following statements about capitalisation:\n\n"
    "(i) The first word of a sentence takes a capital letter.\n"
    "(ii) Names of months and days take capital letters.\n"
    "(iii) A title takes a capital when it appears immediately before a personal name.\n"
    "(iv) The names of the seasons take capital letters.\n\n"
    "Which of the statements given above are correct?",
    ["(ii), (iii) and (iv)", "(i), (ii) and (iv)", "(i), (ii) and (iii)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i), (ii) and (iii) are all standard rules: sentences open with a capital, months and days are "
    "capitalised, and a title such as 'Professor Ahmad' takes a capital when it sits before the name. "
    "(iv) is wrong — the seasons, 'summer', 'winter', 'spring' and 'autumn', are common nouns and stay in "
    "lower case unless they begin a sentence or form part of a proper name. Every option containing (iv) "
    "is therefore incorrect.")

# ---------------------------------------------------- assertion-reason (0,1,2)
q.ar("A comma is placed before 'and' only when it joins two independent clauses in this sentence: "
     "'The siren sounded, and everyone left the building.'",
     "'Everyone left the building' can stand on its own as a complete sentence.",
     0,
     "(A) is correct — a comma before a coordinating conjunction is appropriate precisely when the "
     "conjunction links two independent clauses. (R) is correct — 'Everyone left the building' has its own "
     "subject and verb and could stand alone. (R) also explains (A): it is the independence of the second "
     "clause that licenses the comma. The option denying the causal link is therefore wrong, and the two "
     "options rejecting either statement are wrong because both are accurate.")

q.ar("The apostrophe in 'can't' is not a mark of possession.",
     "An apostrophe placed after a plural noun ending in -s shows possession, as in 'the boys' bats'.",
     1,
     "(A) is correct — in 'can't' the apostrophe marks the letters omitted from 'cannot', not ownership. "
     "(R) is also correct — an apostrophe after a plural s does show possession. But (R) does not explain "
     "(A): it describes a different function of the same mark and gives no reason why the apostrophe in a "
     "contraction is non-possessive. Both statements stand, yet the reason fails to account for the "
     "assertion, so the options claiming an explanatory link or rejecting either statement are wrong.")

q.ar("A colon may be used to introduce a list only after a grammatically complete clause.",
     "A colon and a semicolon are interchangeable when introducing a list.",
     2,
     "(A) is correct — 'The kit contains three items: a torch…' works because the clause before the colon "
     "is complete, whereas 'The kit contains: a torch…' does not. (R) is NOT correct: the two marks have "
     "distinct functions, and a semicolon cannot introduce a list at all. Since the assertion stands and "
     "the reason falls, the options claiming both are correct are wrong, as is the option calling the "
     "assertion incorrect.")

# ---------------------------------------------------------------- matching
q.matching(
    "Match the punctuation marks in Column I with their functions in Column II:\n\n"
    "Column I:\n(a) Semicolon\n(b) Colon\n(c) Apostrophe\n(d) Hyphen\n\n"
    "Column II:\n(i) Joins the parts of a compound adjective before a noun\n"
    "(ii) Links two independent clauses without a conjunction\n"
    "(iii) Introduces a list or an explanation after a complete clause\n"
    "(iv) Marks possession or omitted letters\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)",
     "(a)-(iii), (b)-(ii), (c)-(iv), (d)-(i)",
     "(a)-(ii), (b)-(iii), (c)-(i), (d)-(iv)",
     "(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)"],
    "(a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)",
    "The semicolon links two independent clauses without a conjunction, so (a)-(ii). The colon introduces "
    "a list or an explanation after a complete clause, so (b)-(iii). The apostrophe marks possession or "
    "omitted letters, so (c)-(iv). The hyphen joins the parts of a compound adjective before a noun, so "
    "(d)-(i). The other options swap the roles of the semicolon and colon, or hand the apostrophe's job "
    "to the hyphen, and each misplaces at least two pairs.")

q.matching(
    "Match each sentence in Column I with the punctuation error it contains in Column II:\n\n"
    "Column I:\n(a) The siren sounded, everyone left.\n(b) The kit contains: a torch and a whistle.\n"
    "(c) Its a long route to Leh.\n(d) She is a well known-author.\n\n"
    "Column II:\n(i) Colon placed after an incomplete clause\n(ii) Comma splice\n"
    "(iii) Hyphen joining the wrong pair of words\n(iv) Contraction written as a possessive\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)",
     "(a)-(i), (b)-(ii), (c)-(iv), (d)-(iii)",
     "(a)-(ii), (b)-(i), (c)-(iii), (d)-(iv)",
     "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)"],
    "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)",
    "Joining 'The siren sounded' and 'everyone left' with a comma alone is a comma splice, so (a)-(ii). "
    "'The kit contains:' places a colon after an incomplete clause, so (b)-(i). 'Its a long route' needs "
    "the contraction 'It's', so (c)-(iv). 'well known-author' hyphenates the participle to the noun "
    "instead of forming the compound adjective 'well-known', so (d)-(iii). Each of the other options "
    "misassigns at least two pairs.")

q.matching(
    "Match the punctuation marks in Column I with their names in Column II:\n\n"
    "Column I:\n(a) ;\n(b) :\n(c) '\n(d) —\n\n"
    "Column II:\n(i) Dash\n(ii) Apostrophe\n(iii) Semicolon\n(iv) Colon\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)",
     "(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)",
     "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)",
     "(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)"],
    "(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)",
    "The mark ';' is the semicolon, so (a)-(iii). The mark ':' is the colon, so (b)-(iv). The raised "
    "single mark is the apostrophe, so (c)-(ii). The long horizontal rule is the dash, so (d)-(i). The "
    "remaining options confuse the semicolon with the colon, or the apostrophe with the dash, and each "
    "therefore misplaces at least two pairs. Note that the dash is longer than the hyphen and serves a "
    "different purpose.")

# ---------------------------------------------------------- multiple correct
q.multi(
    "Which of the following are correct uses of the semicolon?\n\n"
    "(i) To join two independent clauses without a conjunction\n"
    "(ii) To separate long list items that already contain commas\n"
    "(iii) To introduce a list after a complete clause\n"
    "(iv) Before a conjunctive adverb such as 'however' linking two clauses\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iv)",
    "(i), (ii) and (iv) are all standard semicolon uses: joining independent clauses, separating list "
    "items that contain internal commas, and preceding a conjunctive adverb such as 'however'. (iii) is "
    "wrong — introducing a list is the colon's function, not the semicolon's, so every option containing "
    "(iii) must be rejected. The distinction between the two marks is a favourite examination point.")

q.multi(
    "Which of the following are correctly punctuated?\n\n"
    "(i) The recruits, who had trained for months, passed easily.\n"
    "(ii) We need three things: rope, water and a map.\n"
    "(iii) He asked whether the file was ready?\n"
    "(iv) It's too late to change the roster now.\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "(i), (ii) and (iv)"],
    "(i), (ii) and (iv)",
    "(i) is correct — the non-defining clause is enclosed by a pair of commas. (ii) is correct — the colon "
    "follows a complete clause and introduces a list. (iv) is correct — 'It's' is the contraction of 'it "
    "is'. (iii) is wrong: it reports a question indirectly and so must end with a full stop, not a "
    "question mark. Every option containing (iii) is therefore incorrect.")

q.multi(
    "Which of the following are correct rules of capitalisation?\n\n"
    "(i) Names of months take capitals.\n(ii) Names of the seasons take capitals.\n"
    "(iii) Titles take capitals immediately before a personal name.\n"
    "(iv) The pronoun 'I' is always capitalised.\n\n"
    "Select the correct combination:",
    ["(i), (iii) and (iv)", "(i), (ii) and (iii)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (iii) and (iv)",
    "(i) is correct — 'March' and 'August' are capitalised. (iii) is correct — 'Professor Ahmad' takes a "
    "capital because the title precedes the name. (iv) is correct — the first-person singular pronoun is "
    "always capitalised in English. (ii) is wrong: the seasons are ordinary common nouns and stay in lower "
    "case, so every option containing (ii) is incorrect.")

emit(q, subject="A",
     topic="Punctuation (Comma, Semicolon, Colon, Apostrophe)",
     path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "tests", "61_test_A_punctuation-marks.json"))
