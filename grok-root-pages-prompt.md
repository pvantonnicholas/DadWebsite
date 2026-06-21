# Grok Build prompt — rebuild the root-directory pages in the warm-broadsheet style

This is a **reusable loop prompt**. Paste everything below the line into Grok Build
(which has access to the project folder). It rebuilds the remaining root-directory
content pages to match `home.htm` and `thefruitofprayer.htm`.

**Work ONE page at a time, in the order listed, and stop after each page for review.**
Before each page is run, two source files are prepared for it in the repo:
`content/<page>.md` (the verbatim text) and `archive/<page>-original.htm` (the current
page, kept as an image/link/counter reference). Do not start a page until both exist.

---

You are working in the root of a static HTML website — a personal Christian family
archive for Anton & Saida Nicholas. Your job is to rebuild one root-directory page at
a time so each matches the design system already established in `home.htm` and
`thefruitofprayer.htm`.

## The loop — repeat for each page in the table below

For the current page `<page>.htm`:

1. Read **`content/<page>.md`** — the complete extracted text of the page. This is the
   content source of truth.
2. Read **`home.htm`** and **`thefruitofprayer.htm`** — the style source of truth.
   Reuse their exact CSS variables, fonts and component styles. `home.htm` is the
   teaser homepage; `thefruitofprayer.htm` is the closest model for an interior
   destination page — follow it.
3. Read **`archive/<page>-original.htm`** — the current page, for reference only:
   exact image paths, link `href`s, video IDs, audio file paths, and the two visitor
   counters. Take placement and asset cues from it; take the *wording* from the `.md`.
4. Overwrite **`<page>.htm`** with one complete, self-contained HTML5 file — all CSS
   and JS inline, no frameworks. Modify **no other file**. The only external requests
   allowed are Google Fonts (EB Garamond, Playfair Display), YouTube thumbnails/embeds,
   and the two visitor counters.
5. **Stop and return the single rebuilt file for review.** Do not move on to the next
   page until told to continue.

## The single most important rule — content preservation

`content/<page>.md` contains the complete text of the page, extracted verbatim. EVERY
sentence in that file must appear in your output, word for word. Do not paraphrase,
shorten, modernise, correct, or "improve" anything — including idiosyncratic spelling,
punctuation and capitalisation (e.g. "incredible miraculous stories", "agonizing"):
it is the site owner's own voice and must be preserved exactly. British English. The
only text you may write yourself is markup-level scaffolding (kickers, aria-labels, alt
text where the source lacks it).

These are DESTINATION pages, not teaser pages. Unlike `home.htm`, there are **no
"Continue reading" expanders, pop-ups or modals** — all text is fully visible on the page.

## Design system — copy from home.htm / thefruitofprayer.htm

Reuse the exact CSS variables, fonts and component styles:

- Parchment palette: `--paper #f7f3ea`, `--paper-raised`, `--paper-inset`.
- Muted accents: terracotta `#9a4e3c`, gold `#8a7342`, sage `#5f6f56`, slate `#516878`,
  plum `#6f5a62`. Dark "depth" band `#3d352c` with gold `#bfa06a`.
- Hairline rules, raised panels, coloured small-caps kickers with a short underline
  accent, scripture blocks (italic, 3px gold left border), mounted-print photo styling
  with italic captions.
- Fonts: EB Garamond (body), Playfair Display (headlines).
- Base font `html { font-size: 22px }` desktop / `19px` mobile, line-height 1.65.
  Readability for older readers is a hard requirement.
- **Never:** shadows, border-radius (except the video play-button circle), gradients,
  icons, emoji, symmetrical card grids.

## Page structure, top to bottom (every page)

1. **Masthead — interior-page variant.** The same masthead as `thefruitofprayer.htm`:
   dateline, ANTON & SAIDA NICHOLAS nameplate, motto, and the same seven-link section
   nav (Daily Readings, Prophecy, Family Legacy, Saida's Journey, Malaysia,
   Testimonies, Updates) — copy the links and their `href`s exactly. Only set
   `aria-current="page"` (terracotta) when the page **is** one of those seven sections
   (see "Nav current" in the table); otherwise mark none current, exactly as
   `home.htm` does.
2. **Page-title band** in the dark depth style: the page title in Playfair gold caps,
   with a one-line italic subtitle drawn from the page's own content.
3. **The page's content**, laid out as newspaper rows (two- or three-column where it
   helps), each with a coloured kicker, a Playfair headline, ALL of its text from the
   content file, and its images placed as mounted prints with italic captions.
   Scripture/psalm passages use the gold-bordered scripture block. Use the per-page
   accent in the table as the dominant kicker colour.
4. **Footer** — the same footer as `thefruitofprayer.htm` (terracotta top rule, © line,
   footer links), and beneath it, centred, **retain the two visitor counters exactly as
   they appear in `archive/<page>-original.htm`**: the Flag Counter image-link
   (`https://info.flagcounter.com/oi2W`) and the StatCounter `sc_project=223118`
   script/noscript block.

All internal links from the content file must be kept with their exact `href`s.

## Media handling

- **YouTube videos — click-to-play facades only.** Never embed live iframes on load.
  Each video is a `div.video-frame` (16:9, 1px rule border) with a `<button>` whose
  background is the thumbnail `https://i.ytimg.com/vi/VIDEO_ID/hqdefault.jpg` (lazy)
  and a centred terracotta play circle (~64px, white triangle, plain CSS). On click,
  swap in the iframe with `autoplay=1` and proper `title`/`allow`/`allowfullscreen`.
  One shared vanilla-JS handler using `data-video-src` / `data-video-title`;
  `aria-label="Play: …"`. Each caption includes a plain
  `https://www.youtube.com/watch?v=VIDEO_ID` link so it works without JavaScript.
- **Audio (`.mp3`)** — use the native `<audio controls preload="none">` element with a
  styled label/caption; keep the original file paths. Where the original used a text
  link to the file, a text link is also fine.
- **PDF** — for the PDF page, keep the `<object data="…pdf">` viewer with an
  `<iframe>` fallback and a plain download link, framed as a mounted print inside a
  raised panel. (See `Christmas2013.htm`.)

## The pages — do them in this order, one at a time

Easiest first, so the recipe is proven before the large pages.

"Nav current" = which of the seven nav links (if any) gets `aria-current="page"`;
"—" means mark none current, like `home.htm`.

| # | Page file | Page-title band text | Nav current | Accent | Key media / notes |
|---|-----------|----------------------|-------------|--------|-------------------|
| 1 | `thelordismylight.htm` | THE LORD IS MY LIGHT | — | gold | Psalm 41 scripture block; `images/main/dove.gif`, `images/main/CDCOVER.gif`; audio `audio/lordlight.mp3`; links `book/chapter1.htm`, `mailto:anton.nicholas@btinternet.com`. **Seed/test page — done; use as the worked example.** |
| 2 | `scholar.htm` | (use the page's own title) | — | slate | `images/profiles/scholar.jpg`. Short prose page. |
| 3 | `clinicalscience.htm` | CLINICAL SCIENCE | — | slate | `VLM1.BMP` (Valerie Meilton research). Short page. |
| 4 | `cutler.htm` | (letter of recommendation title) | — | plum | `Image2.gif`, `images/main/cutler1.gif`, `images/main/juliana.jpg`; videos `3j2hBSgZMrw`, `fK6RHeq4zpo`; links `book/chapter1.htm`, `testimonies/prophecies/index.htm`, `video/antonvideomal.htm`. |
| 5 | `malaysianews.htm` | MALAYSIAN NEWS | — | terracotta | `hugs.jpg`; link `scholar.htm`. "Paul Whizzes To Cambridge". |
| 6 | `tapes.htm` | (Romans 10:17a title) | — | sage | Audio list: `audio/anoint1.mp3`, `anoint2.mp3`, `birthday.mp3`, `empm.mp3`, `global.mp3`, `mother.mp3`, `prayer.mp3`, `wedding.mp3`, `word.mp3`; `images/main/TAPE1.gif`, `dove.gif`, `theresa.jpg`; link `video/birthday.mpg`. Lay the tapes out as a tidy list of audio rows. |
| 7 | `update.htm` | (Intensive Care / answered prayer title) | Updates | terracotta | Videos `3j2hBSgZMrw`, `fK6RHeq4zpo`; images `images/daily/grandpa.jpg`, `images/main/Annette.jpg`, `Jared.jpg`, `JoyceSarojini.jpg`, `Justin08.jpg`, `edmund.jpg`, `fintan.jpg`, `justc.jpg`, `justin.gif`, `images/profiles/grad_jvn.jpg`, `grad_val.jpg`; link `book/chapter1.htm`. Longer — many family photos. |
| 8 | `malaysia.htm` | (Fintan / Deuteronomy 28 title) | Malaysia | gold | Largest page. Videos `-Idpl63I3wA`, `3j2hBSgZMrw`, `4_klvCmSa5U`, `fK6RHeq4zpo`, `kh5nvbzwX4g`, `sAV14VRAzI4`; images `images/daily/grandpa.jpg`, `images/main/Gerard.jpg`, `Lake_Gardens.jpg`, `LeadKindlyLight.jpg`, `NicholasFamily.jpg`; audio `audio/lordlight.mp3`; external links to BBC realmedia and `https://www.sonshinefm.ws`. Many sections — keep every paragraph. |
| 9 | `Christmas2013.htm` | CHRISTMAS LETTER 2013 | — | terracotta | PDF page: keep the `Christmas2013.pdf` `<object>`/`<iframe>` viewer + download link, framed in a raised panel. Subtitle from the original: "Real life testimonies with pictures of miraculous interventions of The Holy Spirit". Minimal prose. |

(The redirect-stub pages — `anglicanchurches.htm`, `catholicchurches.htm`,
`evangelicalchurches.htm`, `lutheranchurches.htm`, `methodistchurches.htm`,
`ITINERARY.htm`, `NST.htm`, `alfred.htm`, `dietitian.htm`, `new.htm`, `step.htm`,
`trump.htm`, `index.htm`, `index.html` — are tiny `<meta refresh>` redirects and must
be left untouched.)

## Verify before returning each page

- Diff your output's visible text against `content/<page>.md`: every sentence present,
  none altered.
- All image paths, `href`s, audio paths and video IDs exactly as in
  `archive/<page>-original.htm` (assets exist on the server, relative to site root).
- No expanders, pop-ups or modals: all text visible.
- Both visitor counters retained in the footer.
- Valid HTML5; works without JavaScript (thumbnails + watch links + download links
  still usable).
- Renders correctly at 380px wide (single column, 19px base font).
- Write the result to `<page>.htm` only; leave every other file untouched (including
  `content/`, `archive/`, `home.htm` and `thefruitofprayer.htm`).
