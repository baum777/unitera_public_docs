# Contributing

This repository is a public projection of UNITERA architecture. Contributions must preserve source authority and status distinctions.

## Before editing

1. Identify the owning domain and source artifact.
2. Classify the statement as `ESTABLISHED`, `MATERIALIZED`, `CANDIDATE`, or `OPEN`.
3. Prefer diagrams and summaries over copying internal source text.
4. Preserve exact technical identifiers such as `email.send.commit`, `KNOW`, `THINK`, `ACT`, and authority-domain names.
5. Never convert a candidate into a canonical claim through documentation alone.
6. Apply substantive changes to `docs/de` and `docs/en` in sync.

## Diagram style

Use GitHub-native Mermaid inside Markdown. Follow [`MERMAID.md`](../../../MERMAID.md). Prefer explicit lifecycle arrows and label trust/authority boundaries rather than relying on visual color semantics.

## Changes that require extra care

- authority ownership
- capability/grant semantics
- production activation
- tenant isolation
- external effects
- source pointer/adoption status
- security boundaries
- compliance or certification language
