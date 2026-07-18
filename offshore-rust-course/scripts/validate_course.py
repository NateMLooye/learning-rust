#!/usr/bin/env python3
"""Structural validator for the Rust for Offshore Backends course.

Stdlib only (pathlib + re) — no dependencies, run with:

    uv run python scripts/validate_course.py

Checks:
  1. lessons/ numbering is sequential with no gaps (0001, 0002, ...).
  2. Each lesson's <title>, <h1>, and nav-bar "Lesson N" text all agree with
     the lesson number in its own filename.
  3. Every local (non-http) href in lessons/ and reference/ resolves to a
     real file, and every #fragment resolves to a real id in its target.
  4. Every lesson links assets/course.css.
  5. Every lesson includes a tangible-win marker, a primary-source callout,
     and an ask-your-tutor callout.

This intentionally does not parse full HTML into a DOM — the course's pages
are small, hand-written, and structurally consistent, so plain regexes over
the raw text are enough and stay easy to read.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS_DIR = ROOT / "lessons"
REFERENCE_DIR = ROOT / "reference"

LESSON_FILENAME_RE = re.compile(r"^(\d{4})-.+\.html$")
TITLE_LESSON_RE = re.compile(r"<title>\s*Lesson\s+(\d+):", re.IGNORECASE)
H1_LESSON_RE = re.compile(r"<h1>\s*Lesson\s+(\d+):", re.IGNORECASE)
NAV_LESSON_RE = re.compile(r"Rust for Offshore Backends\s*\xb7\s*Lesson\s+(\d+)")
HREF_RE = re.compile(r'href="([^"]*)"')
ID_RE = re.compile(r'\bid="([^"]+)"')

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:")


def collect_ids(path: Path) -> set[str]:
    """Every `id="..."` attribute value in a page.

    A plain regex, not html.parser, on purpose: this course's HTML is small,
    hand-written, and structurally consistent, so a regex is just as
    reliable here and a lot cheaper to read than a parser subclass.
    """
    return set(ID_RE.findall(path.read_text(encoding="utf-8")))


def check_lesson_numbering(problems: list[str]) -> dict[int, Path]:
    """Returns {lesson number: path}, after checking the sequence has no gaps."""
    numbered: dict[int, Path] = {}
    for path in sorted(LESSONS_DIR.glob("*.html")):
        m = LESSON_FILENAME_RE.match(path.name)
        if not m:
            problems.append(f"lessons/{path.name}: filename doesn't match NNNN-slug.html")
            continue
        n = int(m.group(1))
        if n in numbered:
            problems.append(f"lessons/{path.name}: duplicate lesson number {n} (also {numbered[n].name})")
        numbered[n] = path

    if not numbered:
        problems.append("lessons/: no lesson files found")
        return numbered

    expected = set(range(1, max(numbered) + 1))
    missing = sorted(expected - set(numbered))
    if missing:
        problems.append(f"lessons/: gap in numbering, missing lesson(s) {missing}")
    return numbered


def check_lesson_self_consistency(numbered: dict[int, Path], problems: list[str]) -> None:
    for n, path in numbered.items():
        text = path.read_text(encoding="utf-8")

        for label, pattern in (("<title>", TITLE_LESSON_RE), ("<h1>", H1_LESSON_RE), ("nav bar", NAV_LESSON_RE)):
            m = pattern.search(text)
            if not m:
                problems.append(f"lessons/{path.name}: {label} doesn't declare a 'Lesson N' number")
            elif int(m.group(1)) != n:
                problems.append(
                    f"lessons/{path.name}: {label} says Lesson {m.group(1)}, filename says {n}"
                )

        if not re.search(r'href="[^"]*assets/course\.css"', text):
            problems.append(f"lessons/{path.name}: does not link assets/course.css")
        if "win-badge" not in text:
            problems.append(f"lessons/{path.name}: missing a tangible-win marker (win-badge)")
        if "callout--source" not in text:
            problems.append(f"lessons/{path.name}: missing a primary-source callout (callout--source)")
        if "callout--ask" not in text:
            problems.append(f"lessons/{path.name}: missing an ask-your-tutor callout (callout--ask)")


def check_links(problems: list[str]) -> None:
    pages = sorted(LESSONS_DIR.glob("*.html")) + sorted(REFERENCE_DIR.glob("*.html"))
    id_cache: dict[Path, set[str]] = {}

    def ids_of(path: Path) -> set[str]:
        if path not in id_cache:
            id_cache[path] = collect_ids(path) if path.exists() else set()
        return id_cache[path]

    for page in pages:
        text = page.read_text(encoding="utf-8")
        rel = f"{page.parent.name}/{page.name}"
        for href in HREF_RE.findall(text):
            if not href or href.startswith(EXTERNAL_PREFIXES):
                continue

            target_part, _, fragment = href.partition("#")

            if not target_part:
                # Same-page fragment, e.g. href="#rustlings-warmup".
                if fragment and fragment not in ids_of(page):
                    problems.append(f"{rel}: href=\"{href}\" — no id=\"{fragment}\" in this file")
                continue

            target = (page.parent / target_part).resolve()
            if not target.exists():
                problems.append(f"{rel}: href=\"{href}\" — target does not exist ({target_part})")
                continue

            if fragment and target.suffix == ".html" and fragment not in ids_of(target):
                problems.append(f"{rel}: href=\"{href}\" — no id=\"{fragment}\" in {target_part}")


def main() -> int:
    problems: list[str] = []

    numbered = check_lesson_numbering(problems)
    check_lesson_self_consistency(numbered, problems)
    check_links(problems)

    if problems:
        print(f"validate_course.py: {len(problems)} problem(s) found:\n")
        for p in problems:
            print(f"  - {p}")
        return 1

    print("validate_course.py: all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
