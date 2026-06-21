#!/usr/bin/env bash
# Prep one root page for the Grok rebuild loop (see ../grok-root-pages-prompt.md).
#
#   ./tasks/prep-root-page.sh thelordismylight
#
# Does two things, idempotently:
#   1. Archives the current page to archive/<page>-original.htm (never overwrites).
#   2. Dumps a rough visible-text draft to content/<page>.draft.md for hand-cleaning
#      into the verbatim content/<page>.md (the loop's content source of truth).
#
# The draft is only a starting point — review it against the page and tidy it into
# content/<page>.md before running Grok on that page.

set -euo pipefail
cd "$(dirname "$0")/.."

page="${1:?usage: prep-root-page.sh <page-basename-without-.htm>}"
src="${page}.htm"
[ -f "$src" ] || { echo "no such page: $src"; exit 1; }

# 1. archive original (don't clobber an existing archive)
arch="archive/${page}-original.htm"
if [ -e "$arch" ]; then
  echo "archive exists, leaving as-is: $arch"
else
  cp "$src" "$arch"
  echo "archived -> $arch"
fi

# 2. rough text draft
draft="content/${page}.draft.md"
python3 - "$src" "$page" > "$draft" <<'PY'
import sys, re, html
path, page = sys.argv[1], sys.argv[2]
txt = open(path, encoding="utf-8", errors="replace").read()
# drop head/style/script
for tag in ("style", "script", "noscript", "head"):
    txt = re.sub(rf"<{tag}\b.*?</{tag}>", "", txt, flags=re.I | re.S)
# note images / links / videos before stripping
assets = []
for m in re.finditer(r'<img[^>]*\bsrc="([^"]+)"', txt, re.I):
    assets.append("img: " + m.group(1))
for m in re.finditer(r'<a[^>]*\bhref="([^"]+)"', txt, re.I):
    assets.append("link: " + m.group(1))
for m in re.finditer(r'(?:embed/|vi/|watch\?v=)([A-Za-z0-9_-]{11})', txt):
    assets.append("video: " + m.group(1))
# block tags -> newlines, then strip remaining tags
txt = re.sub(r"<(br|/p|/div|/h[1-6]|/li|/tr)[^>]*>", "\n", txt, flags=re.I)
txt = re.sub(r"<[^>]+>", "", txt)
txt = html.unescape(txt)
lines = [l.strip() for l in txt.splitlines()]
lines = [l for l in lines if l]
print(f"# {page}  (DRAFT — clean into content/{page}.md, verbatim)\n")
print("## Visible text\n")
print("\n\n".join(lines))
print("\n## Assets referenced in the original\n")
print("\n".join("- " + a for a in dict.fromkeys(assets)))
PY
echo "draft   -> $draft  (clean into content/${page}.md, then run Grok)"
