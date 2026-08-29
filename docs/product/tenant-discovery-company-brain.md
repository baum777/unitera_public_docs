# Tenant, Discovery & Company Brain

**Status:** PUBLIC PROJECTION  
**Mixed maturity:** stable principles plus source-adoption-dependent lifecycle details

The Tenant is the institutional security and authority boundary. Discovery is not free-form chat persistence; it is assisted organizational sensemaking that turns evidence and human input into reviewable organizational knowledge.

```mermaid
flowchart LR
    A[Account] --> T[Tenant]
    T --> FC[First Contact]
    FC --> D[Discovery]
    D --> E[Evidence / Sources]
    E --> C[Claims]
    C --> CA[Candidate]
    CA --> R[Review]
    R --> AP[Approval]
    AP --> RV[Revision]
    RV --> AC[Activation]
    AC --> FW[First Work]
    FW --> W[/work]
```

## Epistemic states

Typical source-oriented distinctions include:

- `founder_confirmed`
- `document_supported`
- `observed`
- `assumption`
- `unresolved`
- `conflicting`

A message is not automatically a Claim. A Claim is not automatically active truth. A Company Map is a read model, not the authority itself.

## Product direction

The source-reconciled direction is **work-first, chat-secondary**: `/work` is the primary operational surface, while chat is contextual support. Company Brain context should be inspectable without pretending the UI is the underlying truth store.
