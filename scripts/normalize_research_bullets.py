#!/usr/bin/env python3
"""Normalize research-note list markers so Distilly's merge_research.py can parse them.

merge_research.py only counts list items written as `- ` bullets. Research agents
sometimes use numbered lists (`1. `) under the same headings, which silently makes
Contradictions / Inferences / Key Findings read as zero. This script rewrites
numbered items into `- ` bullets inside the recognised research sections and
leaves every other line untouched.

Usage:
    python normalize_research_bullets.py <research_dir> [<research_dir> ...]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
NUMBERED_RE = re.compile(r"^\s*\d+[.)]\s+(.*)$")
BULLET_RE = re.compile(r"^(\s*)[-*]\s+\S")

TARGET_SECTIONS = {
    "key findings",
    "evidence",
    "patterns and repeated themes",
    "contradictions",
    "inferences",
    "inferences (clearly marked as inference, not fact)",
    "inferences (clearly marked)",
    "gaps and missing information",
    "gaps",
    "missing information",
    "source metadata",
}


def normalize_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_target = False
    changed = 0
    output: list[str] = []

    for line in lines:
        section = SECTION_RE.match(line)
        if section:
            in_target = section.group(1).strip().lower() in TARGET_SECTIONS
            output.append(line)
            continue

        if in_target and not BULLET_RE.match(line):
            numbered = NUMBERED_RE.match(line)
            if numbered:
                output.append(f"- {numbered.group(1).rstrip()}")
                changed += 1
                continue

        output.append(line)

    if changed:
        path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return changed


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    total = 0
    for raw in argv:
        directory = Path(raw).expanduser()
        files = sorted(directory.glob("*.md"))
        if not files:
            print(f"no markdown files under {directory}")
            continue
        for path in files:
            count = normalize_file(path)
            total += count
            print(f"{path.name}: {count} numbered items converted")
    print(f"total converted: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))