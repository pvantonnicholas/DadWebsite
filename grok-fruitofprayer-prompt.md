# Grok Build prompt — rebuild thefruitofprayer.htm in the warm-broadsheet style

Paste everything below the line into Grok Build (it has access to the project folder).

---

You are working in the root of a static HTML website project. Rebuild `thefruitofprayer.htm`, an inner page of a personal Christian family archive website, to match the design system of `home.htm`.

First read these three files in the project folder:

1. `content/thefruitofprayer.md` — the complete extracted text of this page (the content source of truth)
2. `home.htm` — the redesigned homepage (the style source of truth)
3. `archive/thefruitofprayer-original.htm` — the original page (image placement and link reference only)

Then overwrite `thefruitofprayer.htm` with one complete, self-contained HTML file — all CSS and JS inline, no frameworks. Modify NO other file in the project. The only external requests allowed are Google Fonts (EB Garamond, Playfair Display), YouTube thumbnails/embeds, and the two visitor counters described at the end.

## The single most important rule — content preservation

`content/thefruitofprayer.md` contains the complete text of this page, extracted verbatim. EVERY sentence in that file must appear in your output, word for word. Do not paraphrase, shorten, modernise, correct, or "improve" anything — including idiosyncratic spelling, punctuation and capitalisation (e.g. "magnificient", "Sprit", "no where"): it is the site owner's own voice and must be preserved exactly. British English. The only text you may write yourself is markup-level scaffolding (kickers, aria-labels, alt text where the markdown lacks it).

This page is a DESTINATION page, not a teaser page. Unlike `home.htm`, there are NO "Continue reading" expanders here — all text is fully visible on the page.

## Design system — copy from home.htm

Reuse the exact CSS variables, fonts, and component styles from `home.htm`: the parchment palette (`--paper #f7f3ea`, `--paper-raised`, `--paper-inset`), muted accents (terracotta `#9a4e3c`, gold `#8a7342`, sage `#5f6f56`, slate `#516878`, plum `#6f5a62`), dark depth band (`#3d352c` / gold `#bfa06a`), hairline rules, raised panels, coloured small-caps kickers with the short underline accent, scripture blocks (italic, 3px gold left border), mounted-print photo styling with italic captions, and base font `html { font-size: 22px }` desktop / `19px` mobile. Never: shadows, border-radius (except the video play button circle), gradients, icons, emoji, card grids.

## Page structure, top to bottom

### 1. Masthead — interior-page variant

Same masthead as `home.htm` (dateline, ANTON & SAIDA NICHOLAS nameplate, motto, section nav with the same seven links) but the section nav must mark Prophecy as the current page (terracotta colour, `aria-current="page"`). Below the masthead, a page-title band in the dark depth style: "THE FRUIT OF PRAYER" in Playfair gold caps with a one-line italic subtitle "Prophetic words, answered prayer, and the story of a family built on a vision."

### 2. Lead — Prophetic Word 2025/2026

Full-width lead with terracotta kicker "PROPHETIC WORD 2025 / 2026" and the headline "ENOUGH IS ENOUGH". Contains, verbatim from the content file: the 2021 origin of the declaration (Monday 6th September 2021 at 3-50 am), the prophets of 2025, the 2025/2026 Holy Spirit paragraph, Acts 19:1-2 and the A.W. Tozer passage as scripture blocks, the "Come, O Holy Sprit…" prayer set off in a gold-bordered panel, then Psalm 23:1, Psalm 91 and the Nights of Prayer paragraph.

### 3. Prophetic Word 2024 panel

Raised panel, slate accent: the full 2024 word — the shaking, the call to pray for London, the Household Cavalry horses incident of 24th April 2024.

### 4. Breaking News band

Dark-band-edged section (terracotta top rule) with the two videos side by side — `JyxWqLmmh8A` (Charlie Kirk) and `ldv_5BB01Ko` (UK prayer) — with the full Breaking News text and the "One powerful weapon…" declaration as captions/text alongside.

### 5. Story sections

Then the family sections, alternating two-column and three-column newspaper rows in this order, each with its coloured kicker, Playfair headline, ALL of its text from the content file, and its images placed as mounted prints with their captions:

1. **The Nicholas Family** (gold) — `images/main/famsch.jpg`; St. Dunstan's College history and links
2. **Saida's Background** (plum) — `images/main/agakhan_school.jpg`, `images/main/school.jpg`, `images/main/mosque.jpg`, `images/main/Baloo_family.jpg`; Kampala, the Jamat Khana, the Baloo family
3. **How We Met** (terracotta) — `images/main/St_Marks.jpg`; the July 1979 vision near the Pyrénées
4. **Our Wedding at St. Mark's** (gold) — `images/main/frgwinnell.jpg`, `images/main/wedding.gif`; 23rd April 1983; video `4_klvCmSa5U` (Anton and Saida's Wedding Ceremony)
5. **Plaque Dedication** (slate) — `images/main/plaque.jpg`, `images/main/vicars_plaque.jpg`
6. **Jannine at Alleyn's** (sage) — `images/main/alleyns.jpg`, `images/profiles/grad_jvn.jpg`
7. **Saida at Work** (plum) — `images/main/nurse.jpg`; video `a_4k0kHkSM4` (Saida at Work, BBC feature)
8. **Our Children: Paul & Jannine** (slate) — `images/main/filmsoc.jpg`
9. **Valerie Meilton** (gold) — `images/main/VAL.gif`
10. **Our Prayer Chapel** (terracotta) — `images/main/EIW_Chapel1.jpg`, `EIW_Chapel2.jpg`, `EIW_Chapel3.jpg`; video `AYGVWXs33lE`; the chapel that "arose from the dust", 21st April 2023
11. **Paul's Baptism** (slate) — video `IzDTSsX25kE`
12. **Saida's Arrival in the UK** (plum) — `images/main/Saida_Heathrow.jpg`; Heathrow, the British Nationality Act, link to `profiles/baloo.htm`
13. **Saida's Evangelism at St. Mark's** (sage) — `images/main/DavidLamb24.jpeg`, `images/main/saida_nurse.jpg`; video `qXFgl9FzJPs` (Malaysia Mission); the Crewdson Road community, the omission from the book, her nursing qualifications and sacrifice — this is the longest section; keep every paragraph
14. **Saida's Complex Trauma** (slate) — `images/daily/mumbday.jpg`
15. **Prophetic Word for 2024 / Prayer Vigil / Protection of the Lord / Global Context** (terracotta) — closing section; video `3j2hBSgZMrw` (Hyde Park, "Lead Kindly Light"); the soundproofed Chapel, Psalm 91 and Ephesians 6:10–20, Joel 2:24–26, and the Global Context reports

All internal links from the content file must be kept with their exact hrefs (`book/chapter1.htm`, `profiles/jannine.htm`, `profiles/baloo.htm`, `daily/s4/day38.htm`, `daily/s6/day54.htm`, `https://nicholaslondon.org`, etc.).

### 6. Footer

Same footer as `home.htm` (terracotta top rule, © line, footer links), but ALSO retain the two visitor counters exactly as they appear in `archive/thefruitofprayer-original.htm`: the Flag Counter image-link and the StatCounter script/noscript block. Place them beneath the footer links, centred.

## Video embeds — click-to-play facades only

Do NOT embed live YouTube iframes on page load (eight videos would make the page very heavy). Every video uses the facade pattern: a `div.video-frame` (16:9, 1px rule border) containing a `<button>` with the video's thumbnail `https://i.ytimg.com/vi/VIDEO_ID/hqdefault.jpg` as a full-bleed lazy image and a centred terracotta play circle (~64px, white triangle, plain CSS). On click, swap in the iframe with `autoplay=1` and the proper `title`/`allow`/`allowfullscreen` attributes. One shared vanilla-JS handler using `data-video-src` / `data-video-title`; buttons get `aria-label="Play: …"`. Each facade's caption must include a plain link to `https://www.youtube.com/watch?v=VIDEO_ID` so the video is reachable without JavaScript.

## Verify before returning

- Diff your output's visible text against `content/thefruitofprayer.md`: every sentence present, none altered.
- All image paths and hrefs exactly as listed (they exist on the server, relative to site root).
- No expanders, no pop-ups, no modals: all text visible.
- Valid HTML5; works without JavaScript (thumbnails + watch links still usable).
- Page renders correctly at 380px wide (single column, 19px base font).
- Write the result to `thefruitofprayer.htm` only; leave every other file untouched (including `content/thefruitofprayer.md`, `archive/`, and `home.htm`).
