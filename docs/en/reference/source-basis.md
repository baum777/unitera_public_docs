# Public source assurance

Status: `PUBLIC_ABSTRACTED`

**Source review as of:** 18 September 2026

Public claims are checked against responsible, current owner sources before publication. Current owner sources outrank older derivations; candidates and external concepts remain clearly labeled.

## Review model

| Source class | Public assurance |
|---|---|
| Semantic and contract owners | current canonical state verified |
| Product and runtime materialization | current canonical state verified and abstracted |
| Governance and control sources | current canonical state verified and abstracted |
| Registry and cartography projections | checked for coherence; possible projection lag accounted for |
| Unmerged candidates | not counted as current state |
| Older source candidates and derivations | context only; they do not override a newer owner state |
| External concepts | separately attributed |

## Reconciliation rule

A derived projection can lag behind an already-canonical owner state. In that case:

```text
Current owner source
> derived projection
> older source candidate
> historical summary
```

The time lag of a registry, cartography or documentation projection is therefore an audit signal, but not new authority and not a reason to downgrade a verified owner state.

Conversely, open or unmerged changes are not promoted early. They may be described only as candidates until the responsible owner source carries their status.

Exact repositories, commits, branches, change IDs, contract paths and runtime bindings are verified internally but are not aggregated as a public evidence ledger.

```text
Public explainability != source completeness
Public provenance != exact internal topology
Projection freshness != authority
Candidate evidence != current canonical state
```

---

[← Previous: Architecture baseline](../status/bootstrap-materialization.md) · [Index](../README.md) · [Next: System overview →](../architecture/system-overview.md)
