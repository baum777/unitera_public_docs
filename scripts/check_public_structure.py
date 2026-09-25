#!/usr/bin/env python3
"""Validate structural invariants of the public Markdown projection."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_ROOTS = (ROOT / "docs" / "de", ROOT / "docs" / "en")
INCLUDE_RE = re.compile(r'{%\s*include\s+"([^"]+)"\s*%}')
FRONTMATTER_KEYS = ("description:", "icon:", "layout:", "cover:", "tableOfContents:", "outline:")


def markdown_files():
    for root in DOC_ROOTS:
        yield from sorted(root.rglob("*.md"))


def has_frontmatter_signature(lines: list[str], start: int) -> bool:
    if lines[start].strip() != "---":
        return False
    for line in lines[start + 1 : min(start + 14, len(lines))]:
        stripped = line.strip()
        if stripped == "---":
            break
        if any(stripped.startswith(key) for key in FRONTMATTER_KEYS):
            return True
    return False


def main() -> int:
    findings: list[str] = []

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        h1_lines = [i + 1 for i, line in enumerate(lines) if re.match(r"^#\s+\S", line)]
        if len(h1_lines) != 1:
            findings.append(f"{path.relative_to(ROOT)}: expected exactly one H1, found {len(h1_lines)} at {h1_lines}")

        for i, line in enumerate(lines):
            if i == 0:
                continue
            if has_frontmatter_signature(lines, i):
                findings.append(f"{path.relative_to(ROOT)}:{i + 1}: frontmatter-like block must be the first block")

        for match in INCLUDE_RE.finditer(text):
            target = (path.parent / match.group(1)).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                findings.append(f"{path.relative_to(ROOT)}: include escapes repository: {match.group(1)}")
                continue
            if not target.is_file():
                findings.append(f"{path.relative_to(ROOT)}: missing include target: {match.group(1)}")

    for landing in (ROOT / "docs" / "de" / "README.md", ROOT / "docs" / "en" / "README.md"):
        lines = landing.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            findings.append(f"{landing.relative_to(ROOT)}: GitBook landing frontmatter must start at line 1")

    if findings:
        print("public structure check: FAIL")
        print("\n".join(findings))
        return 1

    print("public structure check: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
