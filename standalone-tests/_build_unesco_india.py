#!/usr/bin/env python3
"""Build the standalone 40-question mock test on UNESCO World Heritage Sites IN INDIA.

Why this generator exists rather than a hand-written JSON: the ruleset fixes both
the question-type mix and a balanced answer key, and both are easy to get wrong by
hand. Here the content is declared once, and the script

  * asserts the type mix matches the 40Q column of the steering prompt's table,
  * assigns each question's option order so the correct answer lands on position
    1/2/3/4 exactly ten times each,
  * refuses to write the file if any invariant fails.

Assertion-Reason items keep the four mandated options in their fixed order, so
their answer position is set by the logical relationship instead; the four AR
items deliberately use one of each relationship, contributing 1 to each position.

Scope note: every question is about sites IN INDIA, per the syllabus item
"Famous Places in India" (section B). UNESCO-the-agency questions (Paris
headquarters, mandate) belong to the separate "United Nations Organizations"
item and are deliberately NOT included here.

Facts verified as of September 2026 - see current_affairs_2026.md section 4.
Run: python3 standalone-tests/_build_unesco_india.py
"""
import json
import os
import collections

AR = [
    "Both (A) and (R) are correct and (R) is the correct explanation of (A)",
    "Both (A) and (R) are correct but (R) is NOT the correct explanation of (A)",
    "(A) is correct but (R) is not correct",
    "(A) is not correct but (R) is correct",
]

# Each entry: (type, questionText, [options in any order], correctAnswer, explanation)
# type is one of S(ingle) ST(atement) AR MC M(atching) FB N(umerical) D(ata interp)
Q = []


def add(t, text, opts, ans, expl):
    Q.append(dict(t=t, text=text, opts=opts, ans=ans, expl=expl))


# ---------------------------------------------------------------- 1 S
add("S",
    "Which site became India's 45th UNESCO World Heritage Site on its inscription in July 2026?",
    ["Ancient Buddhist Site of Sarnath", "Maratha Military Landscapes of India",
     "Moidams of the Ahom Dynasty", "Sacred Ensembles of the Hoysalas"],
    "Ancient Buddhist Site of Sarnath",
    "The Ancient Buddhist Site of Sarnath in Uttar Pradesh was inscribed on 25 July 2026 at the 48th session "
    "of the World Heritage Committee in Busan, taking India's tally to 45. The Maratha Military Landscapes of "
    "India is wrong — that was the 44th, inscribed in July 2025. The Moidams of the Ahom Dynasty is wrong — "
    "that was the 43rd, inscribed in 2024. The Sacred Ensembles of the Hoysalas is wrong — it was inscribed in "
    "2023, well before either of the others.")

# ---------------------------------------------------------------- 2 ST
add("ST",
    "Consider the following statements about India's UNESCO World Heritage Sites:\n\n"
    "(i) India has 45 World Heritage Sites as of 2026.\n"
    "(ii) Of these, 37 are cultural, 7 are natural and 1 is mixed.\n"
    "(iii) Khangchendzonga National Park is India's only mixed World Heritage Site.\n"
    "(iv) India has more World Heritage Sites than any other country in the world.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iv)", "(i), (ii) and (iii)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — the tally reached 45 with Sarnath in July 2026. (ii) is correct — the breakdown is 37 "
    "cultural, 7 natural and 1 mixed. (iii) is correct — Khangchendzonga National Park in Sikkim, inscribed in "
    "2016, is India's only site recognised for both cultural and natural value. (iv) is wrong — India ranks "
    "sixth in the world by number of sites, behind countries such as Italy and China, so every option "
    "containing (iv) must be rejected.")

# ---------------------------------------------------------------- 3 S
add("S",
    "Which of the following was among the very first Indian sites inscribed on the World Heritage List in 1983?",
    ["Khajuraho Group of Monuments", "Hampi", "Taj Mahal", "Sun Temple, Konark"],
    "Taj Mahal",
    "India's first four inscriptions all came in 1983 — the Taj Mahal, Agra Fort, the Ajanta Caves and the "
    "Ellora Caves. The Sun Temple at Konark is wrong — it followed in 1984. The Khajuraho Group of Monuments "
    "is wrong — it was inscribed in 1986. Hampi is wrong — it too was inscribed in 1986, in the same year as "
    "Khajuraho, Fatehpur Sikri and the churches and convents of Goa.")

# ---------------------------------------------------------------- 4 MC
add("MC",
    "Which of the following are natural World Heritage Sites in India?\n\n"
    "(i) Kaziranga National Park\n(ii) Keoladeo National Park\n(iii) Hampi\n(iv) Sundarbans National Park\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)", "(i), (ii) and (iv)"],
    "(i), (ii) and (iv)",
    "Kaziranga (i) and Keoladeo (ii), both inscribed in 1985, and the Sundarbans (iv), inscribed in 1987, are "
    "all natural sites, recognised for wildlife and habitat rather than for built heritage. Hampi (iii) is "
    "wrong — the ruined capital of the Vijayanagara empire in Karnataka is a cultural site, so every option "
    "containing (iii) is incorrect. India has seven natural sites in all: these three plus Nanda Devi and "
    "Valley of Flowers, the Western Ghats and the Great Himalayan National Park.")

# ---------------------------------------------------------------- 5 S
add("S",
    "The Maratha Military Landscapes of India, inscribed in 2025, comprises twelve forts — eleven in "
    "Maharashtra and one in which other state?",
    ["Karnataka", "Tamil Nadu", "Goa", "Gujarat"],
    "Tamil Nadu",
    "Eleven of the twelve component forts lie in Maharashtra, including Raigad, Rajgad, Shivneri, Pratapgad, "
    "Panhala and Sindhudurg, while the twelfth is Gingee Fort in Tamil Nadu, marking the southern reach of "
    "Maratha power. Karnataka is wrong — although the Marathas campaigned there, no Karnataka fort is part of "
    "this serial property. Goa is wrong — its World Heritage listing is the separate churches and convents of "
    "Goa. Gujarat is wrong — its sites are Rani ki Vav, Champaner-Pavagadh, Dholavira and Ahmedabad.")

# ---------------------------------------------------------------- 6 AR (relationship -> position 1)
add("AR",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R).\n\n"
    "Assertion (A): The Sundarbans National Park is inscribed on the World Heritage List as a natural site.\n"
    "Reason (R): It protects the world's largest mangrove forest and is a habitat of the Royal Bengal Tiger.\n\n"
    "Choose the correct option:",
    AR, AR[0],
    "(A) is correct — the Sundarbans National Park in West Bengal was inscribed in 1987 under the natural "
    "criteria. (R) is correct — the delta holds the world's largest mangrove forest and is a stronghold of the "
    "Royal Bengal Tiger. (R) is also the explanation of (A), because it is precisely this ecological value, "
    "rather than any built heritage, that earned the natural listing. The option denying the causal link is "
    "therefore wrong, as are the two options rejecting either statement.")

# ---------------------------------------------------------------- 7 S
add("S",
    "The rock-cut Kailasa temple, carved downwards out of a single mass of rock, forms part of which World "
    "Heritage Site?",
    ["Ajanta Caves", "Elephanta Caves", "Ellora Caves", "Rock Shelters of Bhimbetka"],
    "Ellora Caves",
    "The Kailasa temple is Cave 16 of the Ellora Caves in Maharashtra, inscribed in 1983 and celebrated because "
    "it was excavated downward from the living rock rather than built up in courses. The Ajanta Caves are wrong "
    "— also inscribed in 1983, they are renowned for Buddhist mural painting, not for a monolithic temple. The "
    "Elephanta Caves are wrong — that island site near Mumbai is known for its Shiva sculptures. The Rock "
    "Shelters of Bhimbetka are wrong — they preserve prehistoric rock art in Madhya Pradesh.")

# ---------------------------------------------------------------- 8 M
add("M",
    "Match the following World Heritage Sites with the states in which they are located:\n\n"
    "Column I:\n(a) Khajuraho Group of Monuments\n(b) Sun Temple, Konark\n(c) Hampi\n(d) Rani ki Vav\n\n"
    "Column II:\n(i) Karnataka\n(ii) Madhya Pradesh\n(iii) Gujarat\n(iv) Odisha\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)", "(a)-(iv), (b)-(ii), (c)-(iii), (d)-(i)",
     "(a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)", "(a)-(i), (b)-(iv), (c)-(ii), (d)-(iii)"],
    "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)",
    "Khajuraho stands in Madhya Pradesh, so (a)-(ii). The Sun Temple at Konark is on the Odisha coast, so "
    "(b)-(iv). Hampi, the Vijayanagara capital on the Tungabhadra, is in Karnataka, so (c)-(i). Rani ki Vav, "
    "the stepwell at Patan, is in Gujarat, so (d)-(iii). The other options variously move Khajuraho to Odisha, "
    "Hampi to Gujarat or the stepwell to Karnataka, and each therefore misplaces at least two pairs.")

# ---------------------------------------------------------------- 9 S
add("S",
    "The Moidams, the mound-burial system inscribed as a World Heritage Site in 2024, belong to which dynasty?",
    ["Chola", "Kakatiya", "Hoysala", "Ahom"],
    "Ahom",
    "The Moidams at Charaideo in Assam are the royal burial mounds of the Ahom dynasty, which ruled Assam for "
    "some six centuries, and their 2024 inscription made them India's 43rd World Heritage Site and the first "
    "cultural site from the North East. Chola is wrong — the Cholas are represented by the Great Living Chola "
    "Temples of Tamil Nadu. Kakatiya is wrong — that dynasty built the Ramappa temple in Telangana, inscribed "
    "in 2021. Hoysala is wrong — the Hoysala ensembles in Karnataka were inscribed in 2023.")

# ---------------------------------------------------------------- 10 ST
add("ST",
    "Consider the following statements about the Western Ghats World Heritage Site:\n\n"
    "(i) It was inscribed on the World Heritage List in 2012.\n"
    "(ii) It is a natural site recognised for its exceptional biodiversity.\n"
    "(iii) The Western Ghats are geologically older than the Himalayas.\n"
    "(iv) The site lies entirely within the state of Kerala.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iv)", "(ii), (iii) and (iv)", "(i), (ii) and (iii)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — the Western Ghats were inscribed in 2012. (ii) is correct — the listing rests on "
    "biodiversity, the range being one of the world's recognised biodiversity hotspots. (iii) is correct — the "
    "Ghats are far older than the Himalayas, which are comparatively young fold mountains. (iv) is wrong — the "
    "serial property spans Gujarat, Maharashtra, Goa, Karnataka, Tamil Nadu and Kerala, so every option "
    "containing (iv) is incorrect.")

# ---------------------------------------------------------------- 11 S
add("S",
    "The Great Living Chola Temples World Heritage Site is located in which state?",
    ["Tamil Nadu", "Kerala", "Andhra Pradesh", "Karnataka"],
    "Tamil Nadu",
    "The Great Living Chola Temples are in Tamil Nadu and comprise the Brihadisvara temple at Thanjavur, the "
    "Brihadisvara temple at Gangaikondacholapuram and the Airavatesvara temple at Darasuram; they are called "
    "'living' because worship continues there. Kerala is wrong — it has no World Heritage temple site, its "
    "listing being part of the Western Ghats. Andhra Pradesh is wrong — no Chola temple group there is "
    "inscribed. Karnataka is wrong — its temple listings are Pattadakal and the Hoysala ensembles.")

# ---------------------------------------------------------------- 12 MC
add("MC",
    "Which of the following are World Heritage Sites located in Delhi?\n\n"
    "(i) Humayun's Tomb\n(ii) Qutb Minar and its Monuments\n(iii) Red Fort Complex\n(iv) Fatehpur Sikri\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)"],
    "(i), (ii) and (iii)",
    "Delhi holds three World Heritage Sites: Humayun's Tomb (i) and the Qutb Minar complex (ii), both "
    "inscribed in 1993, and the Red Fort Complex (iii), inscribed in 2007. Fatehpur Sikri (iv) is wrong — the "
    "Mughal capital built by Akbar lies in Agra district of Uttar Pradesh and was inscribed separately in "
    "1986, so every option containing (iv) is incorrect. Humayun's Tomb is often described as the forerunner "
    "of the architectural tradition that culminated in the Taj Mahal.")

# ---------------------------------------------------------------- 13 FB
add("FB",
    "Fill in the blank: __________ became India's first city to be inscribed on the World Heritage List as a "
    "World Heritage City, in 2017.",
    ["Jaipur", "Ahmedabad", "Varanasi", "Hyderabad"],
    "Ahmedabad",
    "The Historic City of Ahmedabad in Gujarat was inscribed in 2017, becoming India's first World Heritage "
    "City, recognised for its walled old city, pols, mosques and Indo-Islamic architecture. Jaipur is wrong "
    "but is the closest distractor — Jaipur City followed as India's second World Heritage City in 2019. "
    "Varanasi is wrong — despite its antiquity it is not on the World Heritage List. Hyderabad is wrong — its "
    "monuments such as Golconda and the Qutb Shahi tombs remain on the tentative list only.")

# ---------------------------------------------------------------- 14 S
add("S",
    "Kaziranga National Park, a natural World Heritage Site in Assam, is best known for conserving which animal?",
    ["Asiatic lion", "One-horned rhinoceros", "Snow leopard", "Asiatic wild ass"],
    "One-horned rhinoceros",
    "Kaziranga, inscribed in 1985, holds much of the world's population of the greater one-horned rhinoceros, "
    "and that is the basis of its fame and its conservation programme. The Asiatic lion is wrong — its sole "
    "wild home is the Gir forest in Gujarat, which is not a World Heritage Site. The snow leopard is wrong — it "
    "inhabits the high Himalaya, including areas such as the Great Himalayan National Park. The Asiatic wild "
    "ass is wrong — it is found in the Rann of Kutch in Gujarat.")

# ---------------------------------------------------------------- 15 AR (relationship -> position 2)
add("AR",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R).\n\n"
    "Assertion (A): The Taj Mahal at Agra is a UNESCO World Heritage Site.\n"
    "Reason (R): The Taj Mahal stands on the right bank of the Yamuna and was built by Shah Jahan in memory of "
    "Mumtaz Mahal.\n\nChoose the correct option:",
    AR, AR[1],
    "(A) is correct — the Taj Mahal was inscribed in 1983, among India's first four sites. (R) is also correct "
    "— it stands on the bank of the Yamuna at Agra and was raised by Shah Jahan as a mausoleum for Mumtaz "
    "Mahal. But (R) does NOT explain (A): a monument's location and patron are not the grounds of "
    "inscription, which rest on outstanding universal value assessed against the Convention's criteria. Hence "
    "both statements are correct while the reason fails to account for the assertion.")

# ---------------------------------------------------------------- 16 S
add("S",
    "Which World Heritage Site in India preserves prehistoric rock paintings and shelters used by early humans?",
    ["Rock Shelters of Bhimbetka", "Pattadakal", "Champaner-Pavagadh", "Dholavira"],
    "Rock Shelters of Bhimbetka",
    "The Rock Shelters of Bhimbetka in Madhya Pradesh, inscribed in 2003, contain rock paintings and evidence "
    "of human occupation reaching back to the Palaeolithic, making them India's principal prehistoric art "
    "site. Pattadakal is wrong — it is a group of early Chalukyan temples in Karnataka. Champaner-Pavagadh is "
    "wrong — it is an archaeological park of pre-Mughal and Islamic remains in Gujarat. Dholavira is wrong — "
    "it is a Harappan city, historic rather than prehistoric, inscribed in 2021.")

# ---------------------------------------------------------------- 17 M
add("M",
    "Match the following World Heritage Sites with the years in which they were inscribed:\n\n"
    "Column I:\n(a) Moidams of the Ahom Dynasty\n(b) Maratha Military Landscapes of India\n"
    "(c) Ancient Buddhist Site of Sarnath\n(d) Dholavira: a Harappan City\n\n"
    "Column II:\n(i) 2021\n(ii) 2026\n(iii) 2024\n(iv) 2025\n\n"
    "Choose the correct match:",
    ["(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)", "(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)",
     "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)", "(a)-(i), (b)-(iv), (c)-(ii), (d)-(iii)"],
    "(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)",
    "The Moidams were inscribed in 2024 as India's 43rd site, so (a)-(iii). The Maratha Military Landscapes "
    "followed in July 2025 as the 44th, so (b)-(iv). Sarnath came in July 2026 as the 45th, so (c)-(ii). "
    "Dholavira, the Harappan city in Gujarat, was inscribed in 2021, so (d)-(i). The other options invert the "
    "2024 and 2025 inscriptions or push Dholavira into the recent sequence, and each misplaces at least two "
    "pairs. Learning this tail of the list in order is the quickest way to answer such questions.")

# ---------------------------------------------------------------- 18 S
add("S",
    "The Kakatiya Rudreshwara or Ramappa Temple, inscribed as a World Heritage Site in 2021, is located in "
    "which state?",
    ["Odisha", "Telangana", "Karnataka", "Maharashtra"],
    "Telangana",
    "The Ramappa Temple at Palampet in Telangana, built under the Kakatiya rulers in the thirteenth century, "
    "was inscribed in 2021 and is noted for its sandbox foundation technique and lightweight bricks. Odisha is "
    "wrong — its World Heritage entry is the Sun Temple at Konark. Karnataka is wrong — its temple listings "
    "are Pattadakal, Hampi and the Hoysala ensembles. Maharashtra is wrong — its sites include Ajanta, Ellora, "
    "Elephanta and the Mumbai listings.")

# ---------------------------------------------------------------- 19 ST
add("ST",
    "Consider the following statements about the Mountain Railways of India World Heritage Site:\n\n"
    "(i) The Darjeeling Himalayan Railway was the first of the group to be inscribed, in 1999.\n"
    "(ii) The Nilgiri Mountain Railway was added to the site in 2005.\n"
    "(iii) The Kalka-Shimla Railway was added in 2008.\n"
    "(iv) The Konkan Railway is one of the components of this site.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "The Mountain Railways of India is a serial site built up in three stages: the Darjeeling Himalayan "
    "Railway in 1999 (i), the Nilgiri Mountain Railway in 2005 (ii) and the Kalka-Shimla Railway in 2008 "
    "(iii). (iv) is wrong — the Konkan Railway, though a celebrated feat of Indian engineering along the west "
    "coast, is not part of this World Heritage listing, so every option containing (iv) is incorrect. Note "
    "that Chhatrapati Shivaji Terminus in Mumbai is a separate railway-related listing, inscribed in 2004.")

# ---------------------------------------------------------------- 20 D
add("D",
    "The following data shows the number of UNESCO World Heritage Sites in India after successive "
    "inscriptions:\n\n2014 → 32\n2018 → 37\n2024 → 43\n2026 → 45\n\n"
    "How many sites were added to India's list between 2014 and 2026?",
    ["11", "13", "15", "18"],
    "13",
    "India's total rose from 32 sites in 2014 to 45 in 2026, so the number added is 45 − 32 = 13. '11' is "
    "wrong and comes from mismeasuring the interval, for instance by starting at the 2018 figure of 37 and "
    "then miscounting. '15' is wrong and overstates the gain. '18' is wrong by a wide margin. The three most "
    "recent additions were the Moidams in 2024, the Maratha Military Landscapes in 2025 and Sarnath in 2026.")

# ---------------------------------------------------------------- 21 S
add("S",
    "Which World Heritage Site in India is a stepwell built in the eleventh century at Patan?",
    ["Rani ki Vav", "Champaner-Pavagadh", "Jantar Mantar", "Hill Forts of Rajasthan"],
    "Rani ki Vav",
    "Rani ki Vav, the Queen's Stepwell at Patan in Gujarat, was inscribed in 2014 and is celebrated for its "
    "seven storeys of sculpted panels descending to the water, an inverted temple in form. "
    "Champaner-Pavagadh is wrong — it is an archaeological park in Gujarat, not a stepwell. Jantar Mantar is "
    "wrong — it is the astronomical observatory at Jaipur, inscribed in 2010. The Hill Forts of Rajasthan are "
    "wrong — that 2013 listing groups six forts including Chittorgarh and Kumbhalgarh.")

# ---------------------------------------------------------------- 22 MC
add("MC",
    "Which of the following are World Heritage Sites inscribed in India during 2021 and 2023?\n\n"
    "(i) Dholavira: a Harappan City\n(ii) Kakatiya Rudreshwara (Ramappa) Temple\n"
    "(iii) Sacred Ensembles of the Hoysalas\n(iv) Great Himalayan National Park\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iv)", "(ii), (iii) and (iv)", "(i), (ii) and (iii)", "(i), (iii) and (iv)"],
    "(i), (ii) and (iii)",
    "Dholavira (i) and the Ramappa Temple (ii) were both inscribed in 2021, and the Sacred Ensembles of the "
    "Hoysalas (iii) in 2023, alongside Santiniketan in the same year. (iv) is wrong — the Great Himalayan "
    "National Park in Himachal Pradesh was inscribed in 2014, not in this window, so every option containing "
    "(iv) is incorrect. Grouping recent inscriptions by year is worth memorising, since current-affairs "
    "questions cluster around the newest entries.")

# ---------------------------------------------------------------- 23 S
add("S",
    "Keoladeo National Park, a natural World Heritage Site inscribed in 1985, is located in which state?",
    ["Madhya Pradesh", "Uttar Pradesh", "Rajasthan", "Gujarat"],
    "Rajasthan",
    "Keoladeo National Park at Bharatpur in Rajasthan, formerly the Bharatpur Bird Sanctuary, was inscribed in "
    "1985 as a wetland of exceptional importance for migratory birds. Madhya Pradesh is wrong — its World "
    "Heritage Sites are Khajuraho, Sanchi and Bhimbetka, all cultural. Uttar Pradesh is wrong — its sites are "
    "the Taj Mahal, Agra Fort, Fatehpur Sikri and now Sarnath. Gujarat is wrong — its listings are Rani ki "
    "Vav, Champaner-Pavagadh, Dholavira and Ahmedabad.")

# ---------------------------------------------------------------- 24 AR (relationship -> position 3)
add("AR",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R).\n\n"
    "Assertion (A): Khangchendzonga National Park is India's only mixed World Heritage Site.\n"
    "Reason (R): It was inscribed in 2016 solely under the natural criteria of the World Heritage Convention.\n\n"
    "Choose the correct option:",
    AR, AR[2],
    "(A) is correct — Khangchendzonga National Park in Sikkim is India's single mixed site, the other 44 being "
    "37 cultural and 7 natural. (R) is NOT correct, and contradicts (A): the park was inscribed in 2016 under "
    "BOTH natural and cultural criteria, recognising its glaciers and biodiversity together with the sacred "
    "significance of the mountain in Sikkimese tradition. That dual basis is exactly what makes it 'mixed', so "
    "a reason describing a purely natural inscription cannot stand.")

# ---------------------------------------------------------------- 25 M
add("M",
    "Match the following World Heritage Sites with their defining descriptions:\n\n"
    "Column I:\n(a) Ajanta Caves\n(b) Jantar Mantar\n(c) Dholavira\n(d) Santiniketan\n\n"
    "Column II:\n(i) An astronomical observatory at Jaipur\n(ii) Buddhist caves famed for mural painting\n"
    "(iii) The site associated with Rabindranath Tagore in West Bengal\n(iv) A Harappan city in Gujarat\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)", "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)",
     "(a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)", "(a)-(ii), (b)-(i), (c)-(iii), (d)-(iv)"],
    "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)",
    "The Ajanta Caves in Maharashtra are Buddhist rock-cut caves renowned for their murals, so (a)-(ii). "
    "Jantar Mantar is the eighteenth-century astronomical observatory at Jaipur, so (b)-(i). Dholavira is the "
    "Harappan city in the Rann of Kutch in Gujarat, so (c)-(iv). Santiniketan in West Bengal, inscribed in "
    "2023, is the seat of Rabindranath Tagore's school and university, so (d)-(iii). Each of the other options "
    "misassigns at least two of these pairs.")

# ---------------------------------------------------------------- 26 S
add("S",
    "The Mahabodhi Temple Complex, a World Heritage Site associated with the Buddha's enlightenment, is "
    "located at:",
    ["Sarnath", "Bodh Gaya", "Kushinagar", "Lumbini"],
    "Bodh Gaya",
    "The Mahabodhi Temple Complex at Bodh Gaya in Bihar, inscribed in 2002, marks the place of the Buddha's "
    "enlightenment beneath the Bodhi tree. Sarnath is wrong but is closely related — it is where the Buddha "
    "preached his first sermon, and it was inscribed separately in 2026. Kushinagar is wrong — it is the site "
    "of the Buddha's parinirvana and is not itself a World Heritage Site. Lumbini is wrong — his birthplace "
    "lies in Nepal, so it is not an Indian site at all.")

# ---------------------------------------------------------------- 27 ST
add("ST",
    "Consider the following statements about the Ancient Buddhist Site of Sarnath:\n\n"
    "(i) It is located in Uttar Pradesh.\n"
    "(ii) It was inscribed at the 48th session of the World Heritage Committee held in Busan.\n"
    "(iii) It became India's 45th World Heritage Site.\n"
    "(iv) It is the place where the Buddha attained enlightenment.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — Sarnath lies near Varanasi in Uttar Pradesh. (ii) is correct — it was inscribed on 25 "
    "July 2026 at the 48th session of the World Heritage Committee in Busan, Republic of Korea. (iii) is "
    "correct — the inscription took India's total to 45. (iv) is wrong — Sarnath is where the Buddha delivered "
    "his first sermon after enlightenment; enlightenment itself came at Bodh Gaya, whose Mahabodhi Temple "
    "Complex is a separate World Heritage Site. Every option containing (iv) is therefore incorrect.")

# ---------------------------------------------------------------- 28 N
add("N",
    "India has 45 World Heritage Sites, of which 7 are natural and 1 is mixed. How many of India's World "
    "Heritage Sites are cultural sites?",
    ["35", "36", "37", "38"],
    "37",
    "Subtracting the non-cultural sites from the total gives 45 − 7 − 1 = 37 cultural sites, which matches the "
    "official breakdown of 37 cultural, 7 natural and 1 mixed. '35' is wrong and results from subtracting an "
    "inflated count of natural sites. '36' is wrong and is what you get by forgetting that the mixed site is "
    "counted separately from the cultural ones. '38' is wrong and comes from omitting the mixed site from the "
    "subtraction altogether.")

# ---------------------------------------------------------------- 29 S
add("S",
    "Which World Heritage Site in India consists of a group of six forts including Chittorgarh and "
    "Kumbhalgarh?",
    ["Hill Forts of Rajasthan", "Maratha Military Landscapes of India", "Champaner-Pavagadh", "Red Fort Complex"],
    "Hill Forts of Rajasthan",
    "The Hill Forts of Rajasthan, inscribed in 2013, is a serial site of six Rajput forts — Chittorgarh, "
    "Kumbhalgarh, Ranthambore, Gagron, Amber and Jaisalmer. The Maratha Military Landscapes of India is wrong "
    "but is the natural trap, being the other multi-fort listing, inscribed in 2025 with twelve forts in "
    "Maharashtra and Tamil Nadu. Champaner-Pavagadh is wrong — it is a single archaeological park in Gujarat. "
    "The Red Fort Complex is wrong — it is one fort, in Delhi.")

# ---------------------------------------------------------------- 30 MC
add("MC",
    "Which of the following are World Heritage Sites located in Maharashtra?\n\n"
    "(i) Ajanta Caves\n(ii) Ellora Caves\n(iii) Elephanta Caves\n(iv) Pattadakal\n\n"
    "Select the correct combination:",
    ["(i), (ii) and (iv)", "(i), (ii) and (iii)", "(ii), (iii) and (iv)", "(i), (iii) and (iv)"],
    "(i), (ii) and (iii)",
    "The Ajanta Caves (i) and Ellora Caves (ii), both inscribed in 1983, and the Elephanta Caves (iii), "
    "inscribed in 1987, are all in Maharashtra. Pattadakal (iv) is wrong — that group of Chalukyan temples is "
    "in Karnataka, so every option containing (iv) is incorrect. Maharashtra also holds Chhatrapati Shivaji "
    "Terminus, the Victorian Gothic and Art Deco Ensembles of Mumbai, and most components of the Maratha "
    "Military Landscapes.")

# ---------------------------------------------------------------- 31 S
add("S",
    "The Buddhist Monuments at Sanchi, inscribed in 1989, are located in which state?",
    ["Bihar", "Uttar Pradesh", "Madhya Pradesh", "Odisha"],
    "Madhya Pradesh",
    "Sanchi lies in Madhya Pradesh, and its Great Stupa, gateways and monasteries were inscribed in 1989 as "
    "one of the oldest surviving Buddhist complexes in India. Bihar is wrong — its Buddhist World Heritage "
    "Site is the Mahabodhi Temple Complex at Bodh Gaya, and it also has Nalanda Mahavihara. Uttar Pradesh is "
    "wrong — its Buddhist listing is Sarnath, inscribed in 2026. Odisha is wrong — its only World Heritage "
    "Site is the Sun Temple at Konark.")

# ---------------------------------------------------------------- 32 AR (relationship -> position 4)
add("AR",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R).\n\n"
    "Assertion (A): Jaipur was India's first city to be inscribed on the World Heritage List as a World "
    "Heritage City.\n"
    "Reason (R): Jaipur City was inscribed on the World Heritage List in 2019.\n\n"
    "Choose the correct option:",
    AR, AR[3],
    "(A) is NOT correct — India's first World Heritage City was the Historic City of Ahmedabad, inscribed in "
    "2017, and Jaipur was the second. (R) is correct — Jaipur City was indeed inscribed in 2019, two years "
    "after Ahmedabad. So the assertion fails on the claim of priority while the reason states an accurate "
    "date. Note that Jaipur separately contains Jantar Mantar, inscribed in 2010, which is a distinct listing "
    "from the walled city itself.")

# ---------------------------------------------------------------- 33 M
add("M",
    "Match the following natural World Heritage Sites of India with their states:\n\n"
    "Column I:\n(a) Manas Wildlife Sanctuary\n(b) Nanda Devi and Valley of Flowers National Parks\n"
    "(c) Great Himalayan National Park\n(d) Khangchendzonga National Park\n\n"
    "Column II:\n(i) Himachal Pradesh\n(ii) Assam\n(iii) Sikkim\n(iv) Uttarakhand\n\n"
    "Choose the correct match:",
    ["(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)", "(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)",
     "(a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)", "(a)-(iv), (b)-(ii), (c)-(i), (d)-(iii)"],
    "(a)-(ii), (b)-(iv), (c)-(i), (d)-(iii)",
    "Manas Wildlife Sanctuary is in Assam, alongside Kaziranga, so (a)-(ii). Nanda Devi and Valley of Flowers "
    "National Parks are in Uttarakhand, so (b)-(iv). The Great Himalayan National Park is in Himachal Pradesh, "
    "so (c)-(i). Khangchendzonga National Park is in Sikkim, and is India's only mixed site, so (d)-(iii). The "
    "other options swap the Himachal and Uttarakhand parks or move Manas out of Assam, and each misplaces at "
    "least two pairs.")

# ---------------------------------------------------------------- 34 S
add("S",
    "Chhatrapati Shivaji Terminus in Mumbai, inscribed as a World Heritage Site in 2004, is an example of "
    "which architectural style?",
    ["Indo-Saracenic", "Victorian Gothic Revival", "Art Deco", "Dravidian"],
    "Victorian Gothic Revival",
    "Chhatrapati Shivaji Terminus in Mumbai, designed by F. W. Stevens and completed in 1888, is a landmark of "
    "Victorian Gothic Revival architecture blended with Indian elements, and was inscribed in 2004. Art Deco "
    "is wrong but is the closest trap — Mumbai's Art Deco buildings form part of the separate Victorian Gothic "
    "and Art Deco Ensembles listing of 2018. Indo-Saracenic is wrong — that style belongs to buildings such as "
    "the Chennai and Mysore public works. Dravidian is wrong — that is a South Indian temple style.")

# ---------------------------------------------------------------- 35 ST
add("ST",
    "Consider the following statements about the Nalanda Mahavihara World Heritage Site:\n\n"
    "(i) It is located in the state of Bihar.\n"
    "(ii) It was inscribed on the World Heritage List in 2016.\n"
    "(iii) It comprises the archaeological remains of an ancient monastic and scholastic institution.\n"
    "(iv) It is a natural World Heritage Site.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — Nalanda is in Bihar. (ii) is correct — the site was inscribed in 2016, the same year as "
    "Khangchendzonga National Park and the Capitol Complex at Chandigarh. (iii) is correct — the listing "
    "covers the excavated remains of stupas, shrines and monastic dwellings of one of the ancient world's "
    "great centres of learning. (iv) is wrong — Nalanda is a cultural site, so every option containing (iv) is "
    "incorrect.")

# ---------------------------------------------------------------- 36 FB
add("FB",
    "Fill in the blank: The __________ Caves, a World Heritage Site on an island near Mumbai, are known for "
    "their monumental rock-cut sculptures of Shiva.",
    ["Ajanta", "Elephanta", "Ellora", "Karla"],
    "Elephanta",
    "The Elephanta Caves, on Gharapuri island in Mumbai harbour, were inscribed in 1987 and are celebrated for "
    "their colossal Shiva sculptures, above all the three-headed Trimurti. Ajanta is wrong — those caves are "
    "inland in Maharashtra and are Buddhist, famed for painting rather than Shaiva sculpture. Ellora is wrong "
    "— also inland, and although it includes the Kailasa temple it is not an island site. Karla is wrong — "
    "those Buddhist caves near Lonavala are not a World Heritage Site.")

# ---------------------------------------------------------------- 37 S
add("S",
    "The Group of Monuments at Mahabalipuram, inscribed in 1984, was built largely under which dynasty?",
    ["Pallava", "Chola", "Chalukya", "Rashtrakuta"],
    "Pallava",
    "Mahabalipuram, on the Coromandel coast in Tamil Nadu, was developed chiefly under the Pallavas in the "
    "seventh and eighth centuries, and its rathas, mandapas and Shore Temple were inscribed in 1984. Chola is "
    "wrong — the Cholas came later and are represented by the Great Living Chola Temples. Chalukya is wrong — "
    "the Chalukyas built Pattadakal and Aihole in Karnataka. Rashtrakuta is wrong — the Rashtrakutas are "
    "associated with the Kailasa temple at Ellora.")

# ---------------------------------------------------------------- 38 D
add("D",
    "The following data shows the number of World Heritage Sites in four Indian states:\n\n"
    "Maharashtra → 6\nUttar Pradesh → 4\nMadhya Pradesh → 3\nGujarat → 4\n\n"
    "What fraction of the sites listed above are located in Maharashtra?",
    ["6/17", "6/15", "4/17", "3/17"],
    "6/17",
    "The four states together account for 6 + 4 + 3 + 4 = 17 sites, of which Maharashtra has 6, giving a "
    "fraction of 6/17. '6/15' is wrong because the denominator omits two of the listed sites, most easily by "
    "dropping Madhya Pradesh's smaller count incorrectly. '4/17' is wrong — 4 is the figure for Uttar Pradesh "
    "or Gujarat, not Maharashtra. '3/17' is wrong — 3 is the Madhya Pradesh figure. Always total the whole "
    "series before forming the fraction.")

# ---------------------------------------------------------------- 39 N
add("N",
    "Between 1983, when India's first sites were inscribed, and 2026, India's tally reached 45 World Heritage "
    "Sites. If 4 sites were inscribed in 1983, how many were added in the years after 1983?",
    ["39", "40", "41", "42"],
    "41",
    "India began with 4 sites in 1983 and reached 45 by 2026, so the number added afterwards is 45 − 4 = 41. "
    "'39' is wrong and would follow from a total of 43, that is from forgetting the 2025 and 2026 "
    "inscriptions. '40' is wrong and results from an off-by-one in the subtraction. '42' is wrong and would "
    "follow from treating only three sites as inscribed in 1983; in fact there were four — the Taj Mahal, Agra "
    "Fort, Ajanta and Ellora.")

# ---------------------------------------------------------------- 40 ST
add("ST",
    "Consider the following statements about World Heritage Sites in India:\n\n"
    "(i) The Historic City of Ahmedabad was inscribed before Jaipur City.\n"
    "(ii) The Sun Temple at Konark and the Group of Monuments at Mahabalipuram were both inscribed in 1984.\n"
    "(iii) The Red Fort Complex in Delhi was inscribed in 2007.\n"
    "(iv) The Western Ghats is a cultural World Heritage Site.\n\n"
    "Which of the statements given above are correct?",
    ["(i), (ii) and (iii)", "(i), (ii) and (iv)", "(ii), (iii) and (iv)", "All of the above"],
    "(i), (ii) and (iii)",
    "(i) is correct — Ahmedabad was inscribed in 2017 and Jaipur City in 2019. (ii) is correct — both the "
    "Konark Sun Temple and Mahabalipuram were inscribed in 1984, the year after India's first four sites. "
    "(iii) is correct — the Red Fort Complex was inscribed in 2007. (iv) is wrong — the Western Ghats, "
    "inscribed in 2012, is a NATURAL site, listed for biodiversity, so every option containing (iv) is "
    "incorrect.")

# =========================================================================
# assemble, verify invariants, assign answer positions
# =========================================================================
EXPECTED = {"S": 16, "ST": 6, "AR": 4, "M": 4, "MC": 4, "FB": 2, "N": 2, "D": 2}
counts = collections.Counter(q["t"] for q in Q)
assert len(Q) == 40, f"expected 40 questions, got {len(Q)}"
assert dict(counts) == EXPECTED, f"type mix wrong: {dict(counts)} != {EXPECTED}"

# AR items keep the mandated option order; their position is fixed by content.
ar_positions = [q["opts"].index(q["ans"]) for q in Q if q["t"] == "AR"]
assert sorted(ar_positions) == [0, 1, 2, 3], f"AR items must cover all 4 positions, got {ar_positions}"

# Every other question gets its options rotated so each position is used 10 times.
target = collections.Counter({0: 10, 1: 10, 2: 10, 3: 10})
for p in ar_positions:
    target[p] -= 1
plan = []
for pos in (0, 1, 2, 3):
    plan += [pos] * target[pos]
assert len(plan) == 36, len(plan)

non_ar = [i for i, q in enumerate(Q) if q["t"] != "AR"]
# interleave the plan so identical target positions are not clustered
plan = [plan[i] for i in sorted(range(36), key=lambda k: (k % 4, k // 4))]

for slot, qi in enumerate(non_ar):
    q = Q[qi]
    want = plan[slot]
    opts = list(q["opts"])
    ai = opts.index(q["ans"])
    opts.insert(want, opts.pop(ai))
    assert opts.index(q["ans"]) == want
    q["opts"] = opts

pos_final = collections.Counter(q["opts"].index(q["ans"]) + 1 for q in Q)
assert pos_final == collections.Counter({1: 10, 2: 10, 3: 10, 4: 10}), pos_final

for i, q in enumerate(Q, 1):
    assert len(q["opts"]) == 4 and len(set(q["opts"])) == 4, f"q{i}: options"
    assert q["ans"] in q["opts"], f"q{i}: answer missing"
    assert len(q["expl"]) >= 180, f"q{i}: explanation {len(q['expl'])} chars"
    assert "|--" not in q["text"] and "|--" not in q["expl"], f"q{i}: markdown table"
    if q["t"] == "M":
        for lab in ("(a)", "(b)", "(c)", "(d)"):
            assert f"\n{lab}" in q["text"], f"q{i}: matching item {lab} not on own line"
    if q["t"] == "FB":
        assert "__________" in q["text"], f"q{i}: no blank"
    if q["t"] == "AR":
        assert q["opts"] == AR, f"q{i}: AR options altered"

out = {
    "subject": "B",
    "topic": "UNESCO World Heritage Sites in India (Famous Places in India)",
    "total_questions": 40,
    "questions": [
        {
            "id": str(i),
            "subject": "B",
            "questionText": q["text"],
            "options": q["opts"],
            "correctAnswer": q["ans"],
            "explanation": q["expl"],
        }
        for i, q in enumerate(Q, 1)
    ],
}

dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "unesco-world-heritage-sites-india_40q.json")
with open(dest, "w") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print(f"wrote {dest}")
print(f"  type mix     : {dict(counts)}")
print(f"  answer key   : {dict(sorted(pos_final.items()))}")
