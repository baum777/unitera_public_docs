# Guide — Maintaining the UNITERA public documentation

## Purpose

Use this repository to explain reviewed UNITERA architecture and operating
concepts publicly in German and English.

## Start here

1. Read `README.md` for the publication role and language entry points.
2. Read `GOVERNANCE.md` before changing architectural or authority claims.
3. Read `CONTRIBUTING.md` for the bilingual synchronization rule.
4. Check `PUBLICATION_MANIFEST.yaml` for the reviewed source refs and status.
5. Follow `MERMAID.md` for GitHub-native diagram fences and labels.

## Content workflow

For a substantive change:

1. identify the repository that owns the claim;
2. verify the exact source ref and whether it is canonical or a candidate;
3. apply the same meaning to `docs/de/` and `docs/en/`;
4. preserve explicit status labels and authority boundaries;
5. update publication metadata when its recorded sources or scope change;
6. review both language paths and run `git diff --check`.

## Core rule

Public documentation projects verified owner state; it does not create that
state. If a public statement conflicts with an owning repository, correct the
projection from verified source evidence.
