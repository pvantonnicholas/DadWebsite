# Grok prompt — three refinements to home.htm

Copy everything below the line into Grok, attaching or pasting the current `home.htm`.

---

You are editing an existing single-file HTML page (`home.htm`) for a personal Christian family archive website. Make ONLY the three changes described below. Do not redesign, restyle, reword, or "improve" anything else — every other line of HTML, CSS and text must remain byte-for-byte identical. The text is the site owner's own voice and must never be paraphrased. British English throughout.

## Change 1 — Remove duplicated text in two "Continue reading" expanders

Each story shows a visible opening (`div.deck`) followed by hidden paragraphs (`div.more`). In two stories the first hidden paragraph repeats the visible deck. Delete the duplicate hidden paragraphs only:

a) **Family Legacy** (kicker "1918–1920 · MALAYA"): inside its `div.more`, delete the paragraph beginning "It was my father's Dad, Bastianpillai Paul Nicholas between the years of 1918–1920…" — it duplicates the deck. Keep all other paragraphs in that block.

b) **Early Life** (kicker "1980 · KENNINGTON"): inside its `div.more`, delete the paragraph beginning "It was in 1980 in St. Mark's Church, Kennington, London Saida co-worked as an Evangelist…" — it duplicates the deck. Also delete the following paragraph beginning "The photograph of Saida was taken before she left Kampala, Uganda…" — it duplicates the figure caption. Keep all other paragraphs in that block.

Do not touch the `div.more` blocks of any other story.

## Change 2 — Click-to-play facades for all YouTube embeds

The page currently has five YouTube `<iframe>` embeds inside `div.video-frame` wrappers, which makes initial page load heavy. Replace each iframe with a lightweight facade that only loads the iframe when clicked:

- Keep every `div.video-frame` wrapper, its position in the document, and the captions/titles exactly as they are.
- Inside each frame, instead of the iframe, render the video's YouTube thumbnail (`https://i.ytimg.com/vi/VIDEO_ID/hqdefault.jpg`) as a full-bleed `<img loading="lazy">` (object-fit: cover), with a centred play button overlaid.
- The play button: a simple circle (~64px) in the site's terracotta `#9a4e3c` at ~90% opacity with a white triangle — plain CSS, no icon fonts, no external assets, no border-radius on anything except the circle itself (the circle is permitted), no shadows, no gradients.
- On click, swap in the original iframe with the SAME `src` plus `&autoplay=1` (or `?autoplay=1` if no query string; note one embed already has `?start=63` — preserve it), and the same `title`, `allow` and `allowfullscreen` attributes as the current code.
- Use a small vanilla JS function added next to the existing expander script at the bottom of the page; mark each facade with `data-video-src` and `data-video-title` attributes so the five embeds share one handler. Each facade must be keyboard-accessible: use a `<button>` element with an `aria-label` of "Play: " plus the video title.
- The five current embed IDs/srcs are: `JndXIOwZSy8`, `ldv_5BB01Ko`, `qXFgl9FzJPs`, `JyxWqLmmh8A?start=63`, and there are no others. Preserve the existing `<!-- LATEST VIDEOS: replace the two embed IDs below -->` comment.

## Change 3 — Replace the legacy .mpg video link

In the Milestones & Celebrations expander there is a link to `video/birthday.mpg` (.mpg does not play in modern browsers). Change the `href` to `https://www.youtube.com/watch?v=-Idpl63I3wA` and leave the link text and the surrounding sentence exactly as written.

## Verify before returning

- No visible wording changed anywhere except the deletions in Change 1.
- Page works with JavaScript disabled: each video facade's thumbnail still shows, and a plain link to `https://www.youtube.com/watch?v=VIDEO_ID` must be present in each caption or as a fallback inside the button's `<noscript>`.
- Valid HTML5, all existing CSS variables and class names untouched.
- Return the complete amended file.
