#!/usr/bin/env python3
"""
Banner Image Audit Script for Anton's Daily Readings (Days 1-70)

PURPOSE
-------
Audit every individual day page (day1.htm – day70.htm) to determine the status
of its banner image against the goal of "one dedicated per-day banner image".

RECOMMENDED NAMING CONVENTION (chosen for this project)
------------------------------------------------------
    dayNN-banner.jpg

Rationale:
- Already partially adopted in s5/
- Clear, sortable, easy to script against
- .jpg is appropriate (these are photographic banners, CSS uses object-fit:cover)
- Alternative accepted during transition: dayNN.png (used in s3/s4)

Re-run the audit anytime after making changes:
    python3 daily/audit-banners.py

The CSV (daily/banner-audit.csv) is the source of truth for tracking progress.
"""

import csv
import os
import re
import sys
from pathlib import Path
from typing import Optional, List

# --- Configuration -----------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]   # DadWebsite/
DAILY_DIR = ROOT / "daily"
IMAGES_DAILY = ROOT / "images" / "daily"

SECTIONS = {
    "s1": (1, 10),
    "s2": (11, 20),
    "s3": (21, 30),
    "s4": (31, 40),
    "s5": (41, 50),
    "s6": (51, 60),
    "s7": (61, 70),
}

# Placeholder patterns to look for in *visible* (non-commented) HTML *content*.
# We deliberately ignore normal alt="Day N Banner" text.
PLACEHOLDER_PATTERNS = [
    r"\bplaceholder\b",
    r"replace with actual",
    r"generated image later",
    r"\bTODO\b",
    r"\bFIXME\b",
    r"\[insert",
    r"insert.*banner",
    r"actual generated",
]

# --- Helpers -----------------------------------------------------------------

def strip_html_comments(html: str) -> str:
    """Remove all <!-- ... --> comments so we only search visible content."""
    return re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL | re.IGNORECASE)


def extract_banner_src(html: str) -> Optional[str]:
    """
    Find the src of the banner image.
    Looks for the first <img> inside the first .banner container.
    """
    # Try to find the banner div and the first img inside it
    banner_match = re.search(
        r'<div[^>]*class=["\'][^"\']*banner[^"\']*["\'][^>]*>(.*?)</div>',
        html,
        re.DOTALL | re.IGNORECASE
    )
    if banner_match:
        banner_content = banner_match.group(1)
        img_match = re.search(
            r'<img[^>]*src=["\']([^"\']+)["\']',
            banner_content,
            re.IGNORECASE
        )
        if img_match:
            return img_match.group(1)

    # Fallback: first img that has "banner" in the alt or nearby context
    img_match = re.search(
        r'<img[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\'][^"\']*banner',
        html,
        re.IGNORECASE
    )
    if img_match:
        return img_match.group(1)

    return None


def resolve_image_path(page_path: Path, src: str) -> Path:
    """
    Resolve a banner src (as written in HTML) to an absolute filesystem path.
    Robust version that correctly handles ../../ relative references.
    """
    page_dir = page_path.parent
    # Use normpath + absolute resolution — much more reliable than raw Path arithmetic with ..
    raw = os.path.normpath(str(page_dir / src))
    return Path(raw).resolve()


def image_exists_and_size(path: Path) -> tuple[bool, Optional[int]]:
    if path.exists() and path.is_file():
        try:
            return True, path.stat().st_size
        except Exception:
            return True, None
    return False, None


def has_visible_placeholder(html: str) -> tuple[bool, List[str]]:
    """
    Return (has_placeholder, list of matched patterns) after stripping comments.
    We try to avoid false positives from normal alt="Day X Banner" text.
    """
    visible = strip_html_comments(html)

    # Remove attribute values (alt="...", title="...", src="...") to reduce noise
    visible_no_attrs = re.sub(r'\b(alt|title|src|data-[a-z-]+)=["\'][^"\']*["\']', '', visible, flags=re.IGNORECASE)

    found = []
    for pat in PLACEHOLDER_PATTERNS:
        if re.search(pat, visible_no_attrs, re.IGNORECASE):
            found.append(pat)
    return bool(found), found


def classify_status(
    banner_src: Optional[str],
    image_exists: bool,
    image_path: Path,
    section: str,
    day: int,
    page_path: Path
) -> tuple[str, bool, str]:
    """
    Return (status, is_dedicated_per_day, notes)
    """
    notes = []

    if not banner_src:
        return "NO_BANNER_TAG", False, "Could not locate <img> inside .banner div"

    if not image_exists:
        # Last-chance check: maybe a close variant exists (wrong extension or -banner vs no suffix)
        parent = image_path.parent
        if parent.exists():
            base_variants = [
                f"day{day}", f"day{day:02d}",
                f"day{day}-banner", f"day{day:02d}-banner"
            ]
            for variant in base_variants:
                for ext in (".jpg", ".jpeg", ".png", ".webp"):
                    candidate = parent / (variant + ext)
                    if candidate.exists():
                        notes.append(f"Correct image likely exists as {candidate.name}")
                        return "FILENAME_MISMATCH", True, "; ".join(notes)
        return "MISSING", False, f"Referenced file does not exist: {banner_src}"

    filename = image_path.name.lower()

    # Generic section banner is not dedicated per-day
    if filename in ("banner.png", "banner.jpg", "banner.jpeg"):
        return "NOT_DEDICATED", False, "Using generic section banner.png instead of per-day image"

    # Determine if the image lives in the expected section folder
    # (more robust than fragile string matching on the full path)
    expected_folder = f"images/daily/{section}"
    img_str = str(image_path).lower().replace("\\", "/")
    in_correct_section = expected_folder in img_str or f"/{section}/" in img_str.split("images/daily/")[-1] if "images/daily/" in img_str else False

    # Special legacy case for early s1 days that deliberately pull from parent daily/ folder
    if section == "s1" and "images/daily/" in img_str and f"/s1/" not in img_str:
        notes.append("Legacy: image from parent images/daily/ folder (pre per-day banners)")
        in_correct_section = True

    if not in_correct_section:
        return "WRONG_SECTION", False, f"Image resolved to different section folder"

    # Accept several reasonable dedicated per-day filename patterns
    dedicated_patterns = [
        rf"^day0?{day}[-_]banner\.(jpg|jpeg|png|webp)$",
        rf"^day0?{day}\.(jpg|jpeg|png|webp)$",
    ]
    is_dedicated = any(re.match(p, filename) for p in dedicated_patterns)

    if is_dedicated:
        return "GOOD", True, ""

    # Image exists in the right section folder but filename doesn't follow the convention
    return "NOT_DEDICATED", False, f"Exists in correct folder but non-standard name (want day{day}-banner.jpg etc): {filename}"


def get_day_pages() -> List[Path]:
    pages = []
    for section, (start, end) in SECTIONS.items():
        section_dir = DAILY_DIR / section
        for day in range(start, end + 1):
            page = section_dir / f"day{day}.htm"
            if page.exists():
                pages.append(page)
            else:
                # Some days might be .html
                alt = section_dir / f"day{day}.html"
                if alt.exists():
                    pages.append(alt)
    return pages


def main():
    pages = get_day_pages()
    if not pages:
        print("ERROR: No day pages found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(pages)} day pages. Auditing banner images...\n")

    results = []
    summary = {s: {"GOOD": 0, "MISSING": 0, "FILENAME_MISMATCH": 0,
                   "NOT_DEDICATED": 0, "WRONG_SECTION": 0, "NO_BANNER_TAG": 0}
               for s in SECTIONS}

    for page in sorted(pages, key=lambda p: (p.parent.name, int(re.search(r"day(\d+)", p.name).group(1)))):
        section = page.parent.name
        day_match = re.search(r"day(\d+)", page.name)
        day = int(day_match.group(1)) if day_match else 0

        try:
            html = page.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            results.append({
                "day": day, "section": section, "page_path": str(page.relative_to(ROOT)),
                "banner_src": "", "resolved_image_path": "", "image_exists": False,
                "image_size_bytes": "", "status": "ERROR", "is_dedicated_per_day": False,
                "has_visible_placeholder": False, "placeholder_details": str(e), "notes": ""
            })
            continue

        banner_src = extract_banner_src(html)
        resolved = resolve_image_path(page, banner_src) if banner_src else None
        exists, size = image_exists_and_size(resolved) if resolved else (False, None)

        status, is_dedicated, notes = classify_status(banner_src, exists, resolved or Path(), section, day, page)

        # Special case: treat clear filename mismatches where the correct file *does* exist nearby
        if status == "MISSING":
            # Check if a close variant exists (e.g. .jpg instead of .png)
            parent = resolved.parent if resolved else None
            if parent and parent.exists():
                base = resolved.stem  # e.g. "day41"
                for candidate in parent.glob(f"{base}*"):
                    if candidate.is_file() and candidate.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"):
                        notes = f"File exists as {candidate.name} but page references {resolved.name}"
                        status = "FILENAME_MISMATCH"
                        exists = True
                        size = candidate.stat().st_size
                        resolved = candidate
                        break

        has_ph, ph_matches = has_visible_placeholder(html)

        row = {
            "day": day,
            "section": section,
            "page_path": str(page.relative_to(ROOT)),
            "banner_src": banner_src or "",
            "resolved_image_path": str(resolved.relative_to(ROOT)) if resolved else "",
            "image_exists": exists,
            "image_size_bytes": size if size else "",
            "status": status,
            "is_dedicated_per_day": is_dedicated,
            "has_visible_placeholder": has_ph,
            "placeholder_details": "; ".join(ph_matches) if ph_matches else "",
            "notes": notes
        }
        results.append(row)

        if status in summary[section]:
            summary[section][status] += 1
        else:
            summary[section]["NOT_DEDICATED"] += 1  # fallback bucket

    # --- Write CSV -------------------------------------------------------------
    csv_path = DAILY_DIR / "banner-audit.csv"
    fieldnames = ["day", "section", "page_path", "banner_src", "resolved_image_path",
                  "image_exists", "image_size_bytes", "status", "is_dedicated_per_day",
                  "has_visible_placeholder", "placeholder_details", "notes"]

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # --- Console Summary -------------------------------------------------------
    print("=" * 80)
    print("DAILY READINGS BANNER AUDIT — SUMMARY")
    print("=" * 80)

    total_good = 0
    total_bad = 0

    for section in SECTIONS:
        s = summary[section]
        good = s.get("GOOD", 0)
        bad = sum(s.get(k, 0) for k in s if k != "GOOD")
        total_good += good
        total_bad += bad

        print(f"\n{section.upper()} (Days {SECTIONS[section][0]}-{SECTIONS[section][1]})")
        print(f"  GOOD:                {good:2d}")
        print(f"  MISSING:             {s.get('MISSING', 0):2d}")
        print(f"  FILENAME_MISMATCH:   {s.get('FILENAME_MISMATCH', 0):2d}")
        print(f"  NOT_DEDICATED:       {s.get('NOT_DEDICATED', 0):2d}")
        print(f"  WRONG_SECTION:       {s.get('WRONG_SECTION', 0):2d}")
        print(f"  NO_BANNER_TAG:       {s.get('NO_BANNER_TAG', 0):2d}")

    print("\n" + "-" * 40)
    print(f"TOTAL DEDICATED & WORKING: {total_good:2d} / 70")
    print(f"TOTAL WITH ISSUES:         {total_bad:2d} / 70")
    print("-" * 40)

    # Pages with visible (non-comment) placeholder text
    placeholders = [r for r in results if r["has_visible_placeholder"]]
    if placeholders:
        print(f"\n⚠️  Pages with VISIBLE placeholder text in HTML (not comments): {len(placeholders)}")
        for p in placeholders:
            print(f"   Day {p['day']:2d} ({p['section']}): {p['placeholder_details']}")
    else:
        print("\n✓ No visible (non-commented) placeholder text found in the 70 day pages.")

    # Critical sections
    print("\n🔴 CRITICAL SECTIONS (0 good dedicated banners):")
    for section in ["s6", "s7"]:
        if summary[section]["GOOD"] == 0:
            print(f"   {section}: All {SECTIONS[section][1]-SECTIONS[section][0]+1} days missing proper banners")

    print(f"\nCSV written to: {csv_path.relative_to(ROOT)}")
    print("=" * 80)

    return results, csv_path


if __name__ == "__main__":
    main()
