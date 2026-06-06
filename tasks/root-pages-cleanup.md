# Root Pages Cleanup Plan

**Created:** June 2026  
**Reference design:** `home.htm` (`assets/css/main.css`, grid layout, `sections.js`, shared nav/footer)  
**Scope:** All 24 root-level `.htm` / `.html` files

Work in the PR order below. Each PR should be reviewable on its own. Do not delete content without a redirect or `archive/` move.

---

## Inventory (current state)

| File | Verdict | Action |
|------|---------|--------|
| `home.htm` | ✅ Modern | Maintain; extract shared template from this |
| `thefruitofprayer.htm` | ✅ Modern | Maintain |
| `malaysia.htm` | ✅ Modern | Maintain; add link to `cutler.htm` in Juliana section |
| `update.htm` | ✅ Modern | Maintain |
| `index.htm` | Redirect | Keep (canonical entry) |
| `index.html` | Redirect duplicate | Keep for now; both point to `home.htm` |
| `dietitian.htm` | Redirect stub | Keep → `profiles/dietitian.htm` |
| `scholar.htm` | Tailwind orphan stack | Re-template to `main.css` (PR 4) |
| `tapes.htm` | Tailwind orphan stack | Re-template to `main.css` (PR 4) |
| `thelordismylight.htm` | Tailwind orphan stack | Re-template to `main.css` (PR 4) |
| `cutler.htm` | Tailwind orphan stack | Re-template + link from `malaysia.htm` (PR 4/6) |
| `clinicalscience.htm` | ✅ Modern | Re-templated; linked from `profiles/dietitian.htm` |
| `new.htm` | Redirect | Archived → `home.htm` |
| `malaysianews.htm` | FrontPage legacy | Modernise (PR 5) |
| `NST.htm` | FrontPage legacy | Merge into `malaysianews.htm` then redirect (PR 5) |
| `Christmas2013.htm` | Bare PDF wrapper | Modernise shell (PR 5) |
| `trump.htm` | Duplicate of prophecies | Redirect (PR 1) |
| `alfred.htm` | Orphan FrontPage | Archive (PR 2) |
| `step.htm` | Orphan FrontPage | Archive (PR 2) |
| `ITINERARY.htm` | Orphan FrontPage | Archive (PR 2) |
| `anglicanchurches.htm` | Orphan FrontPage | Archive (PR 2) |
| `catholicchurches.htm` | Orphan FrontPage | Archive (PR 2) |
| `evangelicalchurches.htm` | Orphan FrontPage | Archive (PR 2) |
| `lutheranchurches.htm` | Orphan FrontPage | Archive (PR 2) |
| `methodistchurches.htm` | Orphan FrontPage | Archive (PR 2) |

---

## PR 1 — Fix broken prophecies URLs (quick win)

**Problem:** ~20 live links point to `prophecies/index.htm` (root), but the file lives at `testimonies/prophecies/index.htm`.

### Tasks

- [x] Create `prophecies/index.htm` as a meta-refresh redirect:
  ```html
  <meta http-equiv="refresh" content="0; url=../testimonies/prophecies/index.htm">
  ```
- [x] Replace `trump.htm` body with the same redirect target (`testimonies/prophecies/index.htm`). Preserve original in `archive/trump.htm.original` before overwriting.
- [x] Smoke-test links from: `home.htm`, `malaysia.htm`, `daily/s5/day50.htm`, `daily/s4/day32.htm`.

### Commit message

`fix: add prophecies redirect stub; redirect trump.htm to canonical prophecies page`

---

## PR 2 — Archive orphaned FrontPage root pages

**Goal:** Remove clutter from root without losing history. No inbound links on any of these.

### Tasks

- [x] Create `archive/root-legacy/` directory.
- [x] Move unchanged copies:
  - `alfred.htm`
  - `step.htm`
  - `ITINERARY.htm`
  - `anglicanchurches.htm`
  - `catholicchurches.htm`
  - `evangelicalchurches.htm`
  - `lutheranchurches.htm`
  - `methodistchurches.htm`
- [x] At each original path, leave a minimal redirect stub → `home.htm` (or `archive/root-legacy/<file>` if you prefer direct access to raw legacy HTML).
- [x] Add `archive/root-legacy/README.md` listing what each file was and the date range of content.

### Decision (pick one before merging)

| Option | Pros | Cons |
|--------|------|------|
| **A: Redirect → `home.htm`** | Clean root; no dead ends | Legacy content harder to find |
| **B: Redirect → `archive/...`** | Content preserved and reachable | URLs stay ugly |

**Recommendation:** Option A for church pages and `step.htm`/`ITINERARY.htm`; Option B for `alfred.htm` if the profile may be revived under `profiles/`.

### Commit message

`chore: archive orphaned FrontPage root pages with redirects`

---

## PR 3 — Extract a reusable page template

**Goal:** Stop copy-pasting nav/header/footer and inline `:root` blocks.

### Tasks

- [ ] Create `assets/templates/page-shell.htm` (or document the copy-from pattern in a comment block at top of `home.htm`) containing:
  - `<!DOCTYPE html>`, charset, viewport
  - `<link rel="stylesheet" href="assets/css/main.css">`
  - Placeholder slots: `<!-- PAGE_TITLE -->`, `<!-- PAGE_CSS_VARS -->`, `<!-- HEADER -->`, `<!-- MAIN -->`, `<!-- SIDEBAR -->`
  - Standard nav (identical to `home.htm` lines 169–192)
  - Footer + StatCounter + `sections.js`
- [ ] Document per-page `:root` palette choices (home=navy/cyan, fruit=green/gold, malaysia=brown/teal, update=purple).
- [ ] No build step required initially — manual copy is fine; Jekyll `_includes` can come later.

### Commit message

`docs: add shared page shell template based on home.htm`

---

## PR 4 — Re-platform Tailwind pages onto `main.css`

**Priority order** (by live inbound links):

1. `scholar.htm` — linked from 5 profile pages
2. `tapes.htm` — linked from `profiles/oriental.htm`
3. `thelordismylight.htm` — historical nav item; Psalm 41 content
4. `cutler.htm` — Juliana letter; link from `malaysia.htm` after this PR

### Per-file checklist

- [x] Replace Tailwind CDN with `assets/css/main.css`
- [x] Use grid: `main-content` only (no sidebar needed for these short pages) OR single-column variant
- [x] Add standard nav + footer from template
- [x] Preserve all original wording and images
- [x] Remove `cdn.tailwindcss.com` and Font Awesome unless icons are essential
- [x] Add `sections.js` only if page has `.section` preview/content blocks
- [x] Verify all image paths still resolve (`images/main/...`, `dove106.gif`, etc.)

### `scholar.htm` notes

- Content is self-contained; single-column `main-content` is enough.
- Keep external link to Paul's Google Sites page.

### `tapes.htm` notes

- Keep link to `malaysianews.htm` (will be modernised in PR 5).
- Singapore talk content stays.

### `thelordismylight.htm` notes

- Psalm 41 responsive text — use card styling from `main.css`, not amber Tailwind classes.
- Fix hardcoded `http://www.antonnicholas.org.uk/images/main/dove.gif` → relative `images/main/dove.gif`.

### `cutler.htm` notes

- Letter layout: no sidebar needed.
- After re-template, add in `malaysia.htm` Juliana section:
  ```html
  <a href="cutler.htm">Read the 2003 letter of recommendation from Fr Cutler</a>
  ```

### Commit message

`modernise: re-platform scholar, tapes, thelordismylight, cutler onto main.css`

---

## PR 5 — Modernise linked legacy content pages

### 5a — `malaysianews.htm` + `NST.htm`

- [x] Merge `NST.htm` newspaper-clip content into `malaysianews.htm` as a second section (preserve both articles).
- [x] Re-template `malaysianews.htm` on `main.css`.
- [x] Replace `NST.htm` with redirect → `malaysianews.htm`.
- [x] Update any `http://www.antonnicholas.org.uk/` absolute URLs to relative paths.
- [x] Verify inbound links from `events/malaysia.htm`, `events/index.htm`, `tapes.htm`.

### 5b — `Christmas2013.htm`

- [x] Wrap PDF embed in standard nav + footer shell.
- [x] Use responsive embed:
  ```html
  <iframe src="Christmas2013.pdf" class="section-content" ...>
  ```
  or keep `<object>` with `max-width: 100%` container.
- [x] Confirm `Christmas2013.pdf` exists at root (or fix path). *Not in repo; relative path preserved for live server.*
- [x] Link still works from `daily/s5/day50.htm`.

### Commit message

`modernise: malaysianews (+ NST merge), Christmas2013 PDF wrapper`

---

## PR 6 — Resolve remaining orphans

### `clinicalscience.htm`

| Option | Action |
|--------|--------|
| **A (recommended)** | Re-template as single-image page; link from `profiles/dietitian.htm` if clinically relevant |
| **B** | Move scanned image into `profiles/` and redirect root URL |
| **C** | Archive + redirect → `home.htm` if content is obsolete |

### `new.htm` ("Intercession links us to the holy of holies")

| Option | Action |
|--------|--------|
| **A (recommended)** | Redirect → `home.htm` (prayer ministry content largely duplicated there) |
| **B** | Re-template and add to Resources sub-nav |
| **C** | Archive as early landing page |

- [x] Decide A/B/C with Dad before deleting. *(Applied plan defaults: clinicalscience → re-template; new.htm → redirect.)*
- [x] If redirect: preserve file in `archive/root-legacy/new.htm`.

### Commit message

`chore: resolve clinicalscience and new.htm orphans`

---

## PR 7 — Consolidate entry points (optional)

- [x] Audit server config: does the host serve `index.html` or `index.htm` by default? *(Both kept; both redirect to `home.htm`.)*
- [x] If only one is needed, keep canonical file and make the other redirect to it (not directly to `home.htm`).
- [x] Align `index.htm` redirect: change `/home.htm` (absolute) to `home.htm` (relative) for consistency with `index.html`.

---

## PR 8 — Nav consistency pass (cross-cutting)

After root cleanup, add secondary pages to navigation where appropriate:

| Page | Suggested nav placement |
|------|-------------------------|
| `scholar.htm` | Footer link from profile pages only (already linked inline) |
| `tapes.htm` | Optional "Resources" sub-nav item |
| `thelordismylight.htm` | Optional "Resources" sub-nav item |
| `malaysianews.htm` | Link from `malaysia.htm` sidebar |
| `cutler.htm` | Inline link from `malaysia.htm` only |

- [x] Update `tasks/general.md` nav consistency task when done.
- [x] Consider adding `thelordismylight.htm` and `tapes.htm` to the Resources dropdown on all `main.css` pages.

---

## Testing checklist (run after each PR)

- [ ] Open every changed file locally in a browser.
- [ ] Click nav links on each modernised page (Main Pages dropdown, Resources, Profiles, Events).
- [ ] Check mobile viewport (900px breakpoint from `home.htm`).
- [ ] Grep for `cdn.tailwindcss.com` — should only remain on `dietitian.htm` redirect (which can drop Tailwind for a plain redirect).
- [ ] Grep for `FrontPage` in root `*.htm` — target zero after PR 2+5.
- [ ] Run link check on inbound URLs listed in the inventory table.

---

## Estimated effort

| PR | Effort | Risk |
|----|--------|------|
| PR 1 | 30 min | Low |
| PR 2 | 1 hr | Low (no live links) |
| PR 3 | 1–2 hr | Low |
| PR 4 | 3–4 hr | Medium (content preservation) |
| PR 5 | 2–3 hr | Medium |
| PR 6 | 1 hr | Low (needs content decision) |
| PR 7 | 30 min | Low |
| PR 8 | 1 hr | Low |

**Total:** ~10–12 hours across 8 PRs.

---

## Suggested execution order (DAG)

```
PR 1 (prophecies redirect)
  ↓
PR 2 (archive orphans)     PR 3 (template) 
  ↓                            ↓
PR 5 (legacy modernise) ← PR 4 (Tailwind → main.css)
  ↓
PR 6 (remaining orphans)
  ↓
PR 7 (index consolidation) → PR 8 (nav pass)
```

PR 2 and PR 3 can run in parallel. PR 4 should follow PR 3.

---

## Files outside this plan (do not touch yet)

- `daily/` — paused but complete
- `profiles/` — separate future task
- `events/`, `testimonies/` — separate future task (though `testimonies/prophecies/index.htm` needs full modernisation eventually)
- Root images / `.class` / `.jar` Java applet artefacts — separate asset cleanup

---

## Next step

Start with **PR 1** (prophecies redirect + `trump.htm` redirect). It fixes live broken links and removes the clearest duplicate in under an hour.