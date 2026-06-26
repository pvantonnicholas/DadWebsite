# Grok /goal — finish the warm-broadsheet rebuild (root + profiles)

Run this as a single autonomous **/goal** in Grok Build, with access to the project
folder. Work through every page in the list without stopping for approval; keep going
until the Definition of Done is met. Record progress in a manifest so the work can be
reviewed afterwards.

---

## GOAL

Bring every remaining content page in the project root and in the `profiles/` folder
into the same "warm-broadsheet" design system already used by `home.htm`,
`thefruitofprayer.htm` and `thelordismylight.htm` — preserving every word of each
page's existing content exactly, and fixing the legacy/broken links as you go.

**`thelordismylight.htm` is a finished, approved example of the target style. Open it
first and match its masthead, palette, components, footer and counters.** Use
`home.htm` and `thefruitofprayer.htm` as further references (interior pages follow
`thefruitofprayer.htm`).

## Definition of Done

The goal is complete when **every page in the table below** has been:

1. Archived once to `archive/<name>-original.htm` (do this **before** overwriting; never
   overwrite an existing archive).
2. Rewritten in place as one self-contained HTML5 file (all CSS/JS inline, no
   frameworks), matching the style of `thelordismylight.htm`.
3. Checked against its own acceptance criteria below.
4. Logged as a row in **`tasks/rebuild-manifest.md`** (create it) with: page name,
   done/▲needs-attention, and a one-line note of anything you could not fully preserve
   or any link you were unsure how to resolve.

Then write a short closing summary at the top of the manifest (how many pages done,
which need a human eye).

## The single most important rule — content preservation

Each page **is its own content source of truth**: the archived original holds the
complete text. EVERY sentence of visible text must reappear in your rebuilt page, word
for word — including idiosyncratic spelling, punctuation and capitalisation. Do not
paraphrase, shorten, modernise, correct, "improve", or drop anything. British English.
The only text you may write is markup-level scaffolding (kickers, aria-labels, alt text
where missing). These are destination pages: **no "Continue reading" expanders,
pop-ups or modals — all text fully visible.**

This site is a personal Christian family archive. Treat all family names, dates,
captions and photographs as sacrosanct: keep every name and caption exactly, keep each
image with the passage it belongs to, never crop/replace/recolour a photo, and never
invent or generate new imagery.

## Design system — copy from thelordismylight.htm / home.htm

- Parchment palette: `--paper #f7f3ea`, `--paper-raised`, `--paper-inset`; ink
  `#2a241c`; rules `#d5cbb8`. Muted accents: terracotta `#9a4e3c`, gold `#8a7342`,
  sage `#5f6f56`, slate `#516878`, plum `#6f5a62`. Dark depth band `#3d352c` /
  gold `#bfa06a` for the page-title band.
- Fonts: EB Garamond (body), Playfair Display (headlines), via Google Fonts.
- `html { font-size: 22px }` desktop / `19px` mobile, line-height ~1.65. Readability
  for older readers is a hard requirement.
- Components: coloured small-caps kickers with short underline accent; Playfair
  headlines; scripture/quote blocks (italic, 3px gold left border); mounted-print
  photos (1px rule border, inset background, italic captions); newspaper-style two-/
  three-column rows separated by hairline rules.
- **Never:** shadows, border-radius (except the video play-button circle), gradients,
  icons, emoji, symmetrical card grids.

## Every page, top to bottom

1. **Masthead** — copy the interior-page masthead from `thelordismylight.htm`:
   dateline, ANTON & SAIDA NICHOLAS nameplate, motto, and the seven-link section nav
   (Daily Readings, Prophecy, Family Legacy, Saida's Journey, Malaysia, Testimonies,
   Updates). Set `aria-current="page"` (terracotta) only per the "Nav current" column;
   otherwise none.
2. **Page-title band** (dark depth style): the page's title in Playfair gold caps with
   a one-line italic subtitle drawn from its own content.
3. **The content** as newspaper rows, each with a coloured kicker (dominant accent per
   the table), a Playfair headline, ALL its text, and its images as mounted prints with
   captions. Scripture/declarations use the gold-bordered block.
4. **Footer** — copy the footer from `thelordismylight.htm` (terracotta top rule, ©
   line, footer links) and, centred beneath it, the two standard visitor counters:
   the Flag Counter image-link (`https://info.flagcounter.com/oi2W`) and the StatCounter
   `sc_project=223118` script/noscript block. **Use this standard pair on every page,
   even pages whose original used a different counter (e.g. the old NeoCounter) — drop
   the old counter.**

## Links and paths — normalise everything (important)

Many legacy pages contain broken or absolute links. Rewrite every internal reference so
it resolves correctly **relative to the rebuilt page's own folder**:

- Pages in the project root link to root resources plainly (`home.htm`,
  `images/...`, `daily/index.htm`).
- Pages in `profiles/` link to root resources with `../` (`../home.htm`,
  `../images/...`, `../daily/index.htm`) and to sibling profiles by bare filename
  (`benedict.htm`).
- Replace any absolute `http://www.antonnicholas.org.uk/…`,
  `http://antonnicholas.org.uk/…`, `https://antonnicholas.org.uk/…` and **malformed
  `://…`** references with the correct site-relative path as above.
- Fix malformed media URLs: `://www.youtube.com/…` → `https://www.youtube.com/…`;
  point images at the real file under `images/…` (with the right `../` depth).
- Keep genuine external links as-is (`https://nicholaslondon.org`, Facebook, Wilberforce
  Academy, BBC, etc.). Keep `mailto:` links. Keep links to assets like `Obituary.pdf`
  and `audio/*.mp3` with the correct relative depth.

## Media handling

- **YouTube — click-to-play facades only**, never live iframes on load. Each is a
  `div.video-frame` (16:9, 1px border) with a `<button>` whose background is
  `https://i.ytimg.com/vi/VIDEO_ID/hqdefault.jpg` (lazy) and a centred terracotta play
  circle (~64px, white triangle, CSS only). On click, swap in the iframe with
  `autoplay=1` + proper `title`/`allow`/`allowfullscreen`. One shared vanilla-JS handler
  via `data-video-src`/`data-video-title`; `aria-label="Play: …"`. Every caption
  includes a plain `https://www.youtube.com/watch?v=VIDEO_ID` link so it works without
  JS. (Some legacy pages list a video ID several times or in old `/v/` form — de-dupe
  and use the facade.)
- **Audio (.mp3)** — native `<audio controls preload="none">` with a caption; keep the
  file path (correct `../` depth).
- **PDF** (Christmas2013) — keep the `<object data="…pdf">`/`<iframe>` viewer + a plain
  download link, framed in a raised panel.

## Acceptance criteria — check each page before logging it done

- Visible text matches the archived original exactly: every sentence present, none
  altered or dropped.
- All links resolve from the page's folder (no `antonnicholas.org.uk` absolutes, no
  `://` malformed URLs left); images load; videos use facades with watch-links.
- Standard Flag + StatCounter footer present.
- Valid HTML5; works with JavaScript disabled; renders as a single column at 380px.
- Only `<name>.htm` and its `archive/<name>-original.htm` and the manifest were
  written — no other file touched (do not touch `home.htm`, `thefruitofprayer.htm`,
  `thelordismylight.htm`, `content/`, `assets/`).

## Pages to rebuild

"Nav current" = which nav link gets `aria-current="page"` ("—" = none).
Accent = dominant kicker colour.

### Root (8 remaining)

| Page | Title band | Nav current | Accent | Notes |
|------|-----------|-------------|--------|-------|
| `scholar.htm` | (its own title) | — | slate | Christ's College scholar declaration (gold quote block); `images/profiles/scholar.jpg`; links `home.htm`, `https://nicholaslondon.org`. Keep `29`/`28` `<sup>th</sup>`. |
| `clinicalscience.htm` | CLINICAL SCIENCE | — | slate | Valerie Meilton research; image `VLM1.BMP`. |
| `cutler.htm` | (recommendation title) | — | plum | Juliana's Psalms; `Image2.gif`, `images/main/cutler1.gif`, `images/main/juliana.jpg`; videos `3j2hBSgZMrw`, `fK6RHeq4zpo`; links `book/chapter1.htm`, `testimonies/prophecies/index.htm`. |
| `malaysianews.htm` | MALAYSIAN NEWS | — | terracotta | "Paul Whizzes To Cambridge"; `hugs.jpg`; link `scholar.htm`. |
| `tapes.htm` | (Romans 10:17a title) | — | sage | Audio list `audio/anoint1.mp3`,`anoint2.mp3`,`birthday.mp3`,`empm.mp3`,`global.mp3`,`mother.mp3`,`prayer.mp3`,`wedding.mp3`,`word.mp3`; `images/main/TAPE1.gif`,`dove.gif`,`theresa.jpg`. Tidy list of audio rows. |
| `update.htm` | (answered-prayer title) | Updates | terracotta | Videos `3j2hBSgZMrw`,`fK6RHeq4zpo`; many family photos under `images/main/` + `images/profiles/`; link `book/chapter1.htm`. |
| `malaysia.htm` | (Fintan / Deut 28 title) | Malaysia | gold | Largest root page. Videos `-Idpl63I3wA`,`3j2hBSgZMrw`,`4_klvCmSa5U`,`fK6RHeq4zpo`,`kh5nvbzwX4g`,`sAV14VRAzI4`; images under `images/main/` + `images/daily/grandpa.jpg`; audio `audio/lordlight.mp3`; external BBC + `https://www.sonshinefm.ws`. |
| `Christmas2013.htm` | CHRISTMAS LETTER 2013 | — | terracotta | PDF page — keep the `Christmas2013.pdf` viewer + download. Subtitle: "Real life testimonies with pictures of miraculous interventions of The Holy Spirit". |

### Profiles (7) — all mark **Family Legacy** current; use `../` for root resources

| Page | Title band | Accent | Notes |
|------|-----------|--------|-------|
| `profiles/oriental.htm` | (its own title) | gold | Largest page; B. P. Nicholas / Oriental Bank legacy. Many videos (`-Idpl63I3wA`,`3j2hBSgZMrw`,`4_klvCmSa5U`,`JUdlNpLO-l0`,`JyxWqLmmh8A`,`Owdsnk52YZ8`,`Vij9m71RS6Q`,`kh5nvbzwX4g`,`ldv_5BB01Ko`,`qXFgl9FzJPs`,`vGxWuXUAMxk`); link `Obituary.pdf`, Facebook, `https://www.karampon.com`, `mailto:contact@antonnicholas.org.uk`, `../video/birthday.mpg`. |
| `profiles/benedict.htm` | MALAYSIA BOLEH | slate | Benedict Ponniah; many `../images/profiles/*`; videos `3j2hBSgZMrw`,`HtFyguQhE4k`,`Vij9m71RS6Q`,`kh5nvbzwX4g`,`muvi2o5RrI4`. |
| `profiles/dietitian.htm` | (its own title) | sage | Valerie Meilton, Registered Dietitian; `../images/profiles/*`; link `../clinicalscience.htm`. |
| `profiles/jannine.htm` | JANNINE NICHOLAS | plum | Audio `../audio/Jannine_Psalm102.mp3`; `../images/profiles/*`; videos `4_klvCmSa5U`,`Vij9m71RS6Q`; external Wilberforce Academy. |
| `profiles/baloo.htm` | (its own title) | plum | **Legacy FrontPage page** — Saida's Grandmother. Ignore the old layout entirely; extract ALL visible text verbatim. Fix the broken `://` and `antonnicholas.org.uk` links/images (`../images/...`). Videos `Z7Ka4MCUAHg`,`boMCzWctij0`,`qXFgl9FzJPs`,`vGxWuXUAMxk`. Sensitive family history — preserve every word. |
| `profiles/kajumba.htm` | DANNY KAJUMBA | slate | **Legacy FrontPage page.** Same normalisation. Videos `kh5nvbzwX4g`,`muvi2o5RrI4`,`3j2hBSgZMrw`,`Vij9m71RS6Q` (some in old `/v/` form — convert to facades). Images `../images/profiles/kajumba.jpg`,`pope.jpg`,`grad_jvn.jpg`,`grad_val.jpg`. |
| `profiles/saida_modelling.htm` | SAIDA MODELLING | terracotta | **Legacy page.** Photos `../images/profiles/saida_modelling_1..3.jpg`,`saidaanton.jpg`; video `qXFgl9FzJPs`; link `../book/chapter1.htm`. Replace old NeoCounter with the standard footer counters. |

## Do NOT touch

- Redirect stubs (tiny `<meta refresh>` pages): `anglicanchurches.htm`,
  `catholicchurches.htm`, `evangelicalchurches.htm`, `lutheranchurches.htm`,
  `methodistchurches.htm`, `ITINERARY.htm`, `NST.htm`, `alfred.htm`, `dietitian.htm`
  (root), `new.htm`, `step.htm`, `trump.htm`, `index.htm`, `index.html`.
- Already done: `home.htm`, `thefruitofprayer.htm`, `thelordismylight.htm`.
- `profiles/prayer/requests.htm` — a frames-based legacy page; **skip it** and note in
  the manifest that it needs separate human handling.
