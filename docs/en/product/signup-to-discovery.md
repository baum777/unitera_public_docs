# From sign-in to Discovery

Status: `PUBLIC_CORE`

The public journey describes product behavior, not authentication or service topology.

```mermaid
flowchart LR
    S["Sign in"] -->|"verified identity"| O["Organization context"]
    O -->|"approved foundations"| D["Discovery"]
    D -->|"reviewable organizational understanding"| R["Review"]
    R -->|"explicit activation"| W["/work"]
```

Discovery helps capture mission, operating model, boundaries, sources and open questions in a traceable way. Results remain reviewable before they become active institutional context.

> Conceptual public projection — not deployment, service, repository, protocol or security topology.
