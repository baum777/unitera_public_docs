# AGENTS.md — unitera_public_docs

## Repository mission

This repository publishes the bilingual public documentation projection for
UNITERA. It is an explanatory surface, not an authority source.

## Authority boundary

- The verified source in the owning repository wins on conflict.
- This repository creates no semantic, contractual, tenant, runtime, or
  execution authority.
- Registry references and imported material do not create authority.
- Candidate and non-canonical branch material must remain explicitly labeled.

## Public disclosure boundary

Public documentation is a curated, deliberately lossy projection. It explains
what UNITERA does and why; owner/internal sources define exactly how, where and
under which contract.

Every statement belongs to one disclosure class:

- `PUBLIC_CORE`: principles and product behavior suitable for direct explanation.
- `PUBLIC_ABSTRACTED`: architecture explained without reconstructable implementation topology.
- `PUBLIC_STATUS`: coarse maturity only: concept, contracted, under implementation,
  pilot preparation, limited pilot, or production.
- `RESTRICTED_SOURCE_DETAIL`: exact repositories, refs, change/review identifiers,
  internal object/schema/package names, state enums, capability identifiers,
  providers, credentials, protocols, routes, enforcement order and test topology.

Composition rule: individually acceptable facts MUST NOT be combined when their
combination reconstructs internal ownership, runtime, authority or enforcement topology.

Exact refs remain required for internal verification but MUST NOT be published.
Engineering state changes continuously; public architectural state changes deliberately.

## Change rules

Before changing substantive content:

1. verify the owning source repository and exact ref;
2. verify the status label and distinguish canonical state from candidates;
3. update the German and English editions together;
4. update `PUBLICATION_MANIFEST.yaml` when publication metadata or source refs
   change;
5. avoid unverified production, deployment, runtime, or compliance claims.

Editorial-only changes may be scoped to the affected text when they do not
change meaning.

## Diagrams

Mermaid in this repository is GitHub-native only. Follow `MERMAID.md` as the
binding contract (GitHub renderer documentation:
https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams).

- Fence every diagram as a backtick `mermaid` block, never `~~~mermaid`.
- Quote labels that contain `/`, `<br>`, or other shape/syntax characters.
- Write the product path as `["/work"]`, never `[/work]`.
- Keep German and English diagram topology identical.

## Validation

- Confirm substantive German and English content remains synchronized.
- Run `git diff --check`.
- Review `PUBLICATION_MANIFEST.yaml` whenever source-backed claims change.
- Preview every changed Mermaid block on GitHub before merge.
- Run `python3 scripts/check_public_disclosure.py` and resolve every finding.

See `README.md`, `GUIDE.md`, `MERMAID.md`, `GOVERNANCE.md`, and `CONTRIBUTING.md`.
