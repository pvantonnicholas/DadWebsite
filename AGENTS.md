# DadWebsite – Agent Instructions

**Project:** Personal/family website for Anton Nicholas (DadWebsite).

**Last Updated:** June 2026

## Current Focus (as of June 2026)

The **homepage (`home.htm`) redesign** is the active workstream. Daily Readings modernization (s1–s7, 70 days) is complete and paused; it should be easy to resume.

## Homepage Design Direction (June 2026 — supersedes earlier notes)

**Aesthetic: "warm broadsheet"** — a newspaper front page rendered as a quiet
archive. Parchment palette (`--paper #f7f3ea` family) with harmonised muted
accents (terracotta `#9a4e3c`, gold `#8a7342`, sage `#5f6f56`, slate `#516878`,
plum `#6f5a62`), raised panels (`--paper-raised`), hairline rules, and a dark
"depth" band (`#3d352c` / gold `#bfa06a`) reserved for the seasonal message.
Never: shadows, border-radius, gradients, icons, emoji, symmetrical card grids.

**Readability first:** base font 22px desktop / 19px mobile, line-height 1.65.
Many readers are older family and friends — when in doubt, larger and clearer.
Fonts: EB Garamond (body), Playfair Display (headlines).

**Homepage hierarchy (in order of prominence):**

1. Word for the Season — slim dark band under the masthead; one editable line
2. Latest YouTube videos — two newest, side by side, in a commented swap block
3. Prophetic Word — the lead story, with embedded videos
4. Rail: Daily Readings, Nights of Prayer, Profile previews, Bulletin
5. Story rows (Legacy, Saida, Early Life, Malaysia, Hymn, Connections,
   Church Life, Milestones) — opening + photo visible, remainder behind
   inline "Continue reading" expansion (no pop-ups, no modals)

**Content rules:** all text from the legacy homepage (`archive/home-original.htm`,
extracted in `content/home.md`) must be preserved verbatim — it is Anton's own
voice; never paraphrase or "improve" it. British English. Nothing from the old
page may be dropped without explicit agreement.

**Maintenance:** the season message and latest-video IDs live in clearly
commented blocks in `home.htm` so they can be swapped without touching
anything else. External AI builders (Grok Build, Cursor Composer) are used
via self-contained prompt files (e.g. `grok-build-prompt.md`); keep prompts
in sync with this design direction.

## Daily Readings Status

- **Banner Standardization**: Complete for s1–s7.
  - Target resolution: 1920 × 960 (2:1) preferred going forward (see `daily/BANNER-STANDARDS.md`).
  - Naming convention: `dayNN-banner.jpg`
- All per-day banners for s1–s7 have been generated or standardized.
- All HTML references in the 20 day pages and both section indexes (`s6/index.htm`, `s7/index.htm`) have been updated.
- Special handling was done for cultural accuracy on personal/family days (notably Day 51 and Day 67 – Malaysian Indian Tamil Christian family representation).
- Section hero banners (`banner.jpg`) for s6 and s7 were also created and wired up.

**Key files for Daily Readings work:**
- `daily/BANNER-STANDARDS.md` – Technical specs and style guidance.
- `daily/BANNER-PROMPT-TEMPLATE.md` – Prompt patterns and day-specific starters (especially useful for s6/s7).
- `daily/audit-banners.py` – Audit script (still useful for verification).

When resuming Daily Readings work:
- Use the standards and prompt templates above.
- Generate in small reviewable batches.
- Be especially careful with personal/family imagery and cultural/religious representation (Malaysian Indian Tamil Christian context).

## General Project Guidelines

- This is a large legacy static HTML site with a lot of personal and family content.
- Preserve original wording and intent when modernizing pages unless explicitly asked to rewrite.
- Be respectful with any imagery involving real people or family members.
- The site mixes old FrontPage-era content with newer modernized sections.
- Git is actively used. Make clear, reviewable commits.

## Working Style Preferences

- Prefer working in focused batches with review points (especially for image generation or large refactors).
- When generating images with Grok Imagine, prefer 2:1 aspect ratio at good resolution.
- Keep `AGENTS.md` and task tracking up to date when major phases shift.
- The built-in todo system can be used for session tracking; persist high-level work in `TODO.md`.

## Resuming Work After a Break

1. Read this `AGENTS.md`.
2. Check `TODO.md` for current priorities.
3. Review any area-specific notes in `tasks/`.
4. For Daily Readings specifically, re-read the two banner docs in the `daily/` folder.

## Other Notes

- The `daily/` folder now has its own modern standards. Other sections of the site are still largely legacy.
- The site contains many images. Be mindful of file sizes when adding new ones.
- There is also a `wordpress/` folder and some legacy artifacts (`_vti_cnf`, old FrontPage files, etc.).

This file should be updated whenever the project enters a new major phase.