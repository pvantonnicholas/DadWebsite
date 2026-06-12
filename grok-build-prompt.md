# Grok Build Prompt — antonnicholas.org.uk homepage

Copy everything below the line into Grok Build.

---

Build a single, self-contained HTML file (`home.htm`) for a personal Christian family archive website: **antonnicholas.org.uk**. Everything — CSS and JS — must be inline in the one file. No frameworks, no build step. The only external requests allowed are Google Fonts and YouTube embeds.

## Design philosophy — "Quiet Archive"

The site is a thoughtful digital archive of faith, family legacy and personal reflection, established 1 August 2002. The design is a warm broadsheet newspaper front page: calm, spacious, contemplative. Generous spacing, excellent serif typography, restrained but warm colour. It must feel personal and human — NOT corporate, NOT like a template, no symmetrical card grids, no icons, no shadows, no rounded corners, no gradients.

### Palette (CSS variables)

- `--paper: #f8f3e7` (page background), `--paper-deep: #f2ead8` (tinted boxes)
- `--ink: #211c14` (text)
- Accents, used for section kickers so each section has its own colour: terracotta `#a8442c` (primary), gold `#96741f`, sage `#57693f`, slate `#3e617e`, plum `#6e3a52`
- `--rule: #cfc5ae` (hairlines), `--muted: #6b6151`

### Typography

- Body: 'EB Garamond', Georgia, serif — 1.06rem, line-height 1.65
- Headlines: 'Playfair Display', Georgia, serif, weight 700/900
- Kickers: small-caps, letter-spacing 0.12em, 0.7rem, coloured per section
- The lead story's first paragraph gets a terracotta drop cap
- Scripture quotes: italic, with a 3px gold left border

### Layout

Max width 1140px, centred. Newspaper rows divided by 1px hairlines (`--rule`); columns separated by vertical hairlines. Photos have a 1px rule border with 4px paper padding (like a mounted print) and italic muted captions. Fully responsive: all grids collapse to one column under 820px, vertical rules become horizontal.

## Page structure, top to bottom

### 1. Masthead

- Top dateline row (small caps, muted): left "Est. 1 August 2002 · Malaya · London · Malaysia", right "1,893,704 readers and counting"
- Nameplate between hairlines: "ANTON & SAIDA NICHOLAS" in Playfair 900, ~3.4rem, the ampersand in terracotta
- Motto line in italic gold: "The Lord is My Shepherd; I shall not want." — Psalm 23:1
- Section nav (small caps, separated by · ): Daily Readings → `daily/index.htm`, Prophecy → `thefruitofprayer.htm`, Family Legacy → `profiles/oriental.htm`, Saida's Journey → `book/chapter1.htm`, Malaysia → `malaysia.htm`, Testimonies → `testimonies/index.htm`, Updates → `update.htm`
- Bottom edge of masthead: 4px solid terracotta rule

### 2. Word for the Season band (NEW — keep it slim)

Directly under the masthead, full-width band in `--paper-deep` with a thin gold top and bottom rule. ONE line only, centred, e.g.:

> **WORD FOR THE SEASON** · Psalm 91 is a protective covering — read the verses passionately. Place your name within the Lamb's Book of Life. → [The Fruit of Prayer](thefruitofprayer.htm)

Kicker in gold small caps, message in italic Garamond ~1rem. It must NOT be a hero banner — max ~3.2rem tall on desktop. This is the editable seasonal message slot; structure it so the text can be swapped easily (a clearly commented block).

### 3. Top grid: lead story (2fr) + sidebar rail (1fr)

**Lead story** — kicker (terracotta) "THE HEART OF THIS SITE"; headline "Daily Readings: a glimpse of how closely God is involved in our lives"; deck with drop cap: "These Daily Readings are timeless. They are construed and formulated from every day living. They are applicable in every year — to get a glimpse of how closely involved God the Father is in our lives. Eight series of readings, gathered over decades, form the living heart of this archive." Scripture: "Be steadfast — in the work of the Lord, knowing that your labour is not in vain." — 1 Corinthians 15:58. Link "Begin today's reading →" to `daily/index.htm`. Photo `images/main/serve.jpg`, caption "Serve God, not man — a watchword of this household since the beginning."

**Sidebar rail** (left hairline border), three stacked boxes:

a) **Nights of Prayer** box — 3px double gold border, `--paper-deep` background. Text: "With a firm instruction from Our Lord, Anton commenced and still continues his meditative whole nights of Prayer on Monday 9th August 2021. Just to touch the Throne Room. Goshen territory. A very safe and secured haven." Scripture: "You who live in the shelter of Elyon (Most High), who spends your nights in the shadow of Shaddai (Breasted One)." — Psalm 91:1

b) **Profiles** box (NEW) — plum small-caps heading "PROFILES". Five compact entries, each a row with a small square thumbnail (~52px, same mounted-print border) plus name (Playfair, links) and a one-line italic hook:
   - B. P. Nicholas — `profiles/oriental.htm` — img `images/profiles/bpnich.jpg` — "One of the first Asian bankers of British Colonial Malaya"
   - Benedict Ponniah — `profiles/benedict.htm` — img `images/profiles/benedict.jpg` — "A Triple First from Cambridge; dinner with the Prime Minister at No. 10"
   - Paul Nicholas — `https://nicholaslondon.org` — img `images/profiles/paulgrad.jpg` — "Cambridge MA; Fellow of the Institute of Actuaries"
   - Jannine Nicholas — `profiles/jannine.htm` — img `images/profiles/jannine.jpg` — "St. John's College, Cambridge; President of the Winfield Society"
   - Valerie Meilton — `profiles/dietitian.htm` — img `images/profiles/grad_val.jpg` — "'Please take care of my only daughter' — Vera's last mandate"

c) **Bulletin** box — slate heading "BULLETIN", list with small gold ✦ markers:
   - On 31st December 2020 this website received its 1st millionth hit — 1,893,704 hits so far. The millionth hit came from Rwanda.
   - There are 26 uploads on the ANTONNICHOLAS channel on YouTube. On 22nd February 2025 the channel had been seen by 258,700 viewers.
   - The site was blessed and inaugurated officially on 1 August 2002.
   - Link: "Read the latest updates →" to `update.htm`

### 4. Latest videos band (PROMINENT)

Full-width band in `--paper-deep` with 3px terracotta top rule. Kicker (terracotta) "LATEST FROM THE ANTONNICHOLAS CHANNEL". Two YouTube embeds side by side (16:9, responsive, `loading="lazy"`), each with an italic caption beneath:

1. `https://www.youtube.com/embed/JndXIOwZSy8` — "Prayer Breakthrough, Video 2: Was Charlie Kirk martyred? How Our Lord prepared me for his departure."
2. `https://www.youtube.com/embed/ldv_5BB01Ko` — "One powerful weapon left to save the United Kingdom from total destruction. Anointed prayer protects the UK. We will get the Victory."

Below the embeds, the prophetic word in two text columns: "Prophetic Word. Please prepare given the forthcoming events. A precursor to the events that are definitely unfolding and how to prepare spiritually. **Psalm 91** is a protective covering — read the verses passionately. Please do not miss the opportunity in case it passes you by. Place your name within the Lamb's Book of Life." Scriptures: Revelation 21:27b "…but only those [will be admitted] whose names have been written in the Lamb's Book of Life." and Romans 8:26 "In the same way the Spirit also comes to help us, weak as we are…". Then a short links list (✦ markers): the 2020 Marriage Prophetic video (`https://www.youtube.com/watch?v=qXFgl9FzJPs` — "a father speaking to his son on essential truths on how to pray; Paul Anton Imbaraj Nicholas, first great grandson of B P Nicholas, has emulated his great grandfather's mantle"), the Charlie Kirk prophetic word (`https://www.youtube.com/watch?v=JyxWqLmmh8A&t=63s`), Lead Kindly Light (`https://www.youtube.com/watch?v=3j2hBSgZMrw` — "seen by over 202,200 viewers"), and Dad's 95th birthday (`https://www.youtube.com/watch?v=-Idpl63I3wA`). End with "Read the full page: The Fruit of Prayer →" to `thefruitofprayer.htm`. NEW videos should be swappable: comment the block clearly (`<!-- LATEST VIDEOS: replace the two embed IDs below -->`).

### 5. Three-column row

Each story: coloured kicker, Playfair headline, opening deck, photo with caption, then a "Continue reading ↓" expander (see behaviour spec at the end) hiding the remaining paragraphs, which end with a link to the full page.

**Col 1 — kicker gold "1918–1920 · MALAYA" — "The first Asian banker of British Malaya".** Deck: "It was my father's Dad, Bastianpillai Paul Nicholas, who between the years of 1918–1920 commenced his first monetary business providing financial services in Ipoh, Perak, Malaya. Due to the date references he is recognised as one of the first Asian bankers in the history of British Colonial Malaya." Photo `images/daily/grandpa.jpg`, caption "My Dad, Albert Arasaratnam Nicholas, positioned in the centre. A photograph of my late Mum can be seen in the background." Hidden: "An all consumingly passionate entrepreneur driven by a strategic vision, who single-handedly brought an idea to pass, overcoming obdurate hurdles and colonial prepotency." + "In 1936 a Colonial Licence was obtained by the visionary B. P. Nicholas under the illustrious title of Bank of Malaya Ltd. My Dad was one of the Directors and the Manager of Oriental Bank of Malaya Ltd-Klang." → `profiles/oriental.htm`

**Col 2 — kicker plum "RESTORATION" — "“Jesus showed a vision of our marriage”".** Deck: "From co-evangelist at St. Mark's Church, Kennington, to a restored life totally guided by the Holy Spirit. If not for the gracious hand of God the Holy Spirit, the narrative around Saida would be a completely different story." Photo `images/main/David_Joyce_and_Saida.jpg`, caption "From left: David Lamb, Saida, and Joyce Lamb née Amirdaratnam." Hidden: wedding video note ("It had to be a real 3-dimensional vision to convince a true blue Roman Catholic to marry a lady with strong Evangelical convictions"); Saida became a Nursing Sister via King's College and The City University, London; Canon Nicholas Rivett-Carnac's testimony of how she sacrificed her career; scripture Joel 2:25–26 "Once again you will have all the food you want… Never again will my people be disgraced." → `book/chapter1.htm`

**Col 3 — kicker slate "1980 · KENNINGTON" — "A pioneer of “tent making” at St. Mark's".** Deck: "It was in 1980 at St. Mark's Church, Kennington, that Saida co-worked as an Evangelist alongside David Lamb, when the late Canon Sir Nicholas Rivett-Carnac was Vicar. She was the first individual from a congregation of over 600 who accepted the calling to do 'tent making' — sacrificing her financial pursuits to tell the local people about Jesus." Photo `images/main/saida_young.jpg`, caption "Saida, photographed before she left Kampala, Uganda, where she completed part of her education at The Aga Khan School." Hidden: she was once a model (link `profiles/saida_modelling.htm`); she lost her father at 42 when she was sixteen months old; Anton led a well-attended early morning prayer meeting for two years in the upstairs chambers at St. Mark's; scripture Acts 6:4–5.

### 6. Two-column row

**Col 1 — kicker sage "MALAYSIA · 2008 & 2009" — "The most precious week on the mountain top in Cameron Highlands".** Deck: 25th wedding anniversary, Cameron Highlands Resort, 5,000 feet above sea level, Tanah Rata, Pahang. Photo `images/main/Lake_Gardens.jpg`, caption "High tea at the Carcosa Seri Negara Hotel, Lake Gardens, Kuala Lumpur — where Queen Elizabeth II and Prince Philip once stayed." Hidden: Pastor Roy Muttiah's prophecy to each family member, 24th August 2008, Cornerstone Glory Church, Petaling Jaya; fellowship with Pastor Reuben Seevaratnam (Penang) and Pastor Raymond Yeo (Subang Jaya); Dr. Joy Seevaratnam and Elsie's 1985 family prophecy — "every word has come to pass"; 2009 English afternoon tea at the Carcosa Seri Negara. → `malaysia.htm`

**Col 2 — kicker slate "HYMN · HYDE PARK, 2010" — "Lead, Kindly Light: sung by 80,000 kneeling in the darkness".** Deck: John Henry Newman wrote the hymn while seriously ill in Sicily, far from home, believing he was facing death — "a touch from the Lord". Photo `images/main/LeadKindlyLight.jpg`, caption "The hymn sheet from the Prayer Vigil at Hyde Park, Saturday 18th September 2010." Hidden: the Hyde Park vigil — between 8 and 8.30 pm, darkness fallen, most of the 80,000 congregants on their knees in solemn prayer as the hymn was sung; over 202,200 viewers of the video worldwide; it will minister to all facing loneliness, darkness and confusion. → `thelordismylight.htm`

### 7. Second three-column row

**Col 1 — kicker gold "EARLY CONNECTIONS" — "Friendships that shaped and grounded our early Christian life".** Names: Alan Meyer and the late Pippa Meyer, Gerry Kearney, Steve Burton, Jonathan Gwilt, Joseph Niles, Danny John McGill. Photo `images/main/dm.jpg`, caption "Danny John McGill, who offered us accommodation at his home in Loughborough Road, Brixton, in 1986." Hidden: Pippa Meyer led Praise and Worship at St. Mark's prayer meetings; worship with Gerry Kearney at Victory Christian Centre, Hampstead; Jonathan Gwilt stayed in the basement Aug 1990–Feb 1991 completing his Chartered Accountancy exams; Steve Burton helped move from Brixton to Peckham; link "the story of Pippa Meyer's last few hours" → `daily/s1/day8.htm`. → `thefruitofprayer.htm`

**Col 2 — kicker sage "CHURCH LIFE" — "Thirteen years at All Saints, Peckham".** Deck: family worshipped at All Saints Church, Peckham for 13 years; Rev. Frog Orr-Ewing was Vicar 20th July 2003 – 23rd May 2010. Photo `images/main/ASPeckham.jpg`. Hidden: Nicholas Rivett-Carnac's Scots Guards decade — platoon commander in the fierce fighting in Malaya, mentioned in dispatches, home in time for the 1953 Coronation Procession; his father commanded the battleship Rodney and was Rear-Admiral in charge of the Normandy Beaches in 1944; Bishop Peter Walker's testimonial at the 2004 Memorial service. → `thefruitofprayer.htm`

**Col 3 — kicker plum "MILESTONES & CELEBRATIONS" — "Birthdays, anniversaries, and a millionth visitor from Rwanda".** Photo `images/main/2013bday.jpg`, caption "Anton's birthday, 2013 — celebrated in the company of family." Hidden: the millionth hit came from a Rwandan Google search for "Selwyn Hughes biography" (link `daily/s4/day37.htm`); the 25th anniversary at Cameron Highlands Resort; the 1936 Bank of Malaya Colonial Licence; Dad's 90th birthday video → `video/birthday.mpg`. → `update.htm`

### 8. Bottom strip + footer

"ALSO IN THIS EDITION" strip (sage small caps label, · separated): Tapes → `tapes.htm`, The Lord is My Light → `thelordismylight.htm`, The Book · Chapter 1 → `book/chapter1.htm`, Testimonies → `testimonies/index.htm`, Events → `events/malaysia.htm`, Prophecies → `prophecies/index.htm`, B. P. Nicholas on Facebook → `https://www.facebook.com/bpnicholasmalaysia`.

Footer: 4px terracotta top rule, centred, muted. "© Anton Nicholas · Blessed and inaugurated 1 August 2002" plus links: Daily Readings, The Fruit of Prayer, Paul Nicholas (`https://nicholaslondon.org`), `@AntonNicholas1` (`https://twitter.com/AntonNicholas1`).

## "Continue reading" behaviour

Each story's extra paragraphs sit in a hidden `div.more` after a `button.more-toggle` styled as a text link ("Continue reading ↓", terracotta, dotted-underline). Clicking toggles the div open in place (display block, separated by a dotted hairline) and the button becomes "Show less ↑"; set `aria-expanded` accordingly. NO pop-ups, NO modals, NO navigation — expansion happens inline. The last line inside each expanded block is a "Read the full story →" link to the dedicated page. Vanilla JS, ~10 lines, at the end of the body.

## Hard constraints

- One file, valid HTML5, all relative paths exactly as given (images and pages exist on the server)
- British English throughout; preserve the quoted text verbatim — it is the site owner's own voice and must not be paraphrased or "improved"
- No emoji, no icon fonts, no border-radius, no box-shadow, no gradients
- All images `loading="lazy"` except the lead photo
- YouTube iframes: `loading="lazy"`, no autoplay
- Works without JavaScript (expanders simply stay closed; all full-page links remain reachable via nav and strips)
