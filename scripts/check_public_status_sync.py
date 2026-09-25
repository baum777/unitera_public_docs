#!/usr/bin/env python3
"""Keep the maintained public snapshot date synchronized across DE/EN status surfaces."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DE_MONTHS = {
    "Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6,
    "Juli": 7, "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12,
}
EN_MONTHS = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
}

SURFACES = {
    "docs/de/status/current-state.md": "de",
    "docs/de/status/capability-use-case-matrix.md": "de",
    "docs/de/status/pilot-production-readiness.md": "de",
    "docs/de/reference/source-basis.md": "de",
    "docs/en/status/current-state.md": "en",
    "docs/en/status/capability-use-case-matrix.md": "en",
    "docs/en/status/pilot-production-readiness.md": "en",
    "docs/en/reference/source-basis.md": "en",
}


def parse_manifest_date() -> date:
    text = (ROOT / "PUBLICATION_MANIFEST.yaml").read_text(encoding="utf-8")
    match = re.search(r'^\s*reviewed_at:\s*"?(\d{4})-(\d{2})-(\d{2})"?\s*$', text, re.M)
    if not match:
        raise ValueError("PUBLICATION_MANIFEST.yaml: reviewed_at not found")
    return date(*(int(part) for part in match.groups()))


def parse_surface_date(path: Path, language: str) -> date:
    text = path.read_text(encoding="utf-8")
    if language == "de":
        match = re.search(r"(\d{1,2})\.\s+(" + "|".join(DE_MONTHS) + r")\s+(\d{4})", text)
        if not match:
            raise ValueError(f"{path.relative_to(ROOT)}: German snapshot date not found")
        day, month, year = match.groups()
        return date(int(year), DE_MONTHS[month], int(day))

    match = re.search(r"(\d{1,2})\s+(" + "|".join(EN_MONTHS) + r")\s+(\d{4})", text)
    if not match:
        raise ValueError(f"{path.relative_to(ROOT)}: English snapshot date not found")
    day, month, year = match.groups()
    return date(int(year), EN_MONTHS[month], int(day))


def main() -> int:
    try:
        expected = parse_manifest_date()
        observed = {path: parse_surface_date(ROOT / path, language) for path, language in SURFACES.items()}
    except ValueError as exc:
        print(f"public status sync: FAIL\n{exc}")
        return 1

    mismatches = {path: value for path, value in observed.items() if value != expected}
    if mismatches:
        print("public status sync: FAIL")
        print(f"manifest reviewed_at = {expected.isoformat()}")
        for path, value in mismatches.items():
            print(f"{path}: {value.isoformat()}")
        return 1

    print(f"public status sync: PASS ({expected.isoformat()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
