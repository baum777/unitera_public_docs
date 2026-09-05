---
description: Public entry point for UNITERA contracts without exposing restricted internal contract identifiers or topology.
icon: file-signature
---

# Public contract index

`UPD-CONTRACT-INDEX-001` · `CONTRACT` · `PUBLIC_ABSTRACTED`

UNITERA's public documentation describes **contract semantics and boundaries before contract identifiers**. Internal IDs, reconstructable topology and unpublished schemas remain outside the public projection unless explicitly cleared.

{% include "../.gitbook/includes/public-projection.md" %}

## Available public contract semantics

- [Authority & Source-of-Truth model](../architecture/authority-and-source-model.md)
- [Governed external effect](../runtime/governed-effect.md)
- [Functions, capabilities and use cases](../status/capability-use-case-matrix.md)
- [Public disclosure policy](../reference/public-disclosure-policy.md)

## Publication rule

When a stable public API contract exists, this section should be **OpenAPI-first** rather than duplicating endpoints in prose. Until then, absence of an endpoint page must not be interpreted as an undocumented production API promise.
