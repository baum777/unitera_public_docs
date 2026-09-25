#!/usr/bin/env python3
"""Check structural parity for public DE/EN pages with mirrored meaning."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAIRS = (
    ("docs/de/README.md", "docs/en/README.md"),
    ("docs/de/status/current-state.md", "docs/en/status/current-state.md"),
    ("docs/de/status/capability-use-case-matrix.md", "docs/en/status/capability-use-case-matrix.md"),
    ("docs/de/status/pilot-production-readiness.md", "docs/en/status/pilot-production-readiness.md"),
    ("docs/de/reference/source-basis.md", "docs/en/reference/source-basis.md"),
    ("docs/de/product/operating-surface-and-continuity.md", "docs/en/product/operating-surface-and-continuity.md"),
)


def signature(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    headings = [len(match.group(1)) for match in re.finditer(r"^(#{1,6})\\s+\\S", text, re.M)]
    table_separators = len(re.findall(r"^\\|(?:\\s*:?-+:?\\s*\\|)+\\s*$", text, re.M))
    return {
        "headings": headings,
        "tables": table_separators,
        "mermaid": text.count("```" + "mermaid"),
        "code_fences": text.count("```"),
        "includes": len(re.findall(r'{%\\s*include\\s+"[^"]+"\\s*%}', text)),
    }


def main() -> int:
    findings: list[str] = []

    for de_rel, en_rel in PAIRS:
        de_path, en_path = ROOT / de_rel, ROOT / en_rel
        if not de_path.is_file() or not en_path.is_file():
            findings.append(f"missing mirrored pair: {de_rel} <-> {en_rel}")
            continue

        de_sig, en_sig = signature(de_path), signature(en_path)
        if de_sig != en_sig:
            findings.append(f"structural drift: {de_rel} != {en_rel}\\n  DE {de_sig}\\n  EN {en_sig}")

    if findings:
        print("public language parity: FAIL")
        print("\\n".join(findings))
        return 1

    print("public language parity: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
