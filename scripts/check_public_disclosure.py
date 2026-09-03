#!/usr/bin/env python3
"""Fail closed when public documentation exposes restricted source detail."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RULES = {
    "commit_ref": re.compile(r"\b[0-9a-f]{7,40}\b", re.I),
    "branch_ref": re.compile(r"\brefs/heads/|\bmain@|\borigin/main\b|\b(?:main|master)\b", re.I),
    "pull_request_ref": re.compile(r"\b(?:PR|pull request)\s*#?\d+\b", re.I),
    "credential_name": re.compile(r"\b[A-Z][A-Z0-9_]*_API_KEY\b"),
    "internal_id": re.compile(r"\b(?:OD|GOV|RA|RRB|WP|PP|LRN|RCW|HAC)-[A-Z0-9-]+\b"),
    "exact_capability_id": re.compile(r"\bemail\.send\.commit\b", re.I),
    "internal_path": re.compile(r"\b(?:packages|apps|registry)/[A-Za-z0-9_.@/()-]+"),
    "exact_repository_topology": re.compile(
        r"\b(?:coreos|unitera-os|Unitera_Systems|unitera_control_plane|unitera-registry|unitera-production-interface)\b",
        re.I,
    ),
    "provider_routing_detail": re.compile(
        r"\b(?:OpenRouter|OIDC|PKCE|BFF|mTLS|RLS|CredentialBroker|Shadow Guard|R2/R3)\b",
        re.I,
    ),
}

ACCEPTANCE_LABELS = {
    "commit_ref": "PUBLIC_DOCS_EXACT_COMMIT_REFS",
    "branch_ref": "PUBLIC_DOCS_BRANCH_REFS",
    "pull_request_ref": "PUBLIC_DOCS_PR_REFS",
    "credential_name": "PUBLIC_DOCS_CREDENTIAL_NAMES",
    "internal_id": "PUBLIC_DOCS_INTERNAL_GATE_IDS",
    "exact_capability_id": "PUBLIC_DOCS_EXACT_CAPABILITY_IDS",
    "internal_path": "PUBLIC_DOCS_INTERNAL_PATHS",
    "exact_repository_topology": "PUBLIC_DOCS_EXACT_REPO_AUTHORITY_GRAPH",
    "provider_routing_detail": "PUBLIC_DOCS_PROVIDER_ROUTING_DETAIL",
}


def files():
    yield from sorted(
        path
        for path in ROOT.rglob("*")
        if path.suffix in {".md", ".yaml", ".yml"}
        and ".git" not in path.parts
    )


def main() -> int:
    findings: list[tuple[str, Path, int]] = []
    for path in files():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for rule, pattern in RULES.items():
                subject = re.sub(r"https?://\S+", "", line) if rule == "commit_ref" else line
                if pattern.search(subject):
                    findings.append((rule, path.relative_to(ROOT), number))
    counts = {rule: 0 for rule in RULES}
    for rule, _, _ in findings:
        counts[rule] += 1
    if findings:
        print("public disclosure check: FAIL")
        print("\n".join(f"{path}:{number}: {rule}" for rule, path, number in findings))
        for rule, label in ACCEPTANCE_LABELS.items():
            print(f"{label} = {counts[rule]}")
        return 1
    print("public disclosure check: PASS")
    for rule, label in ACCEPTANCE_LABELS.items():
        print(f"{label} = 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
