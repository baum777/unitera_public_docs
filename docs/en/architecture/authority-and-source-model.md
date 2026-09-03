# Authority and source model

Status: `PUBLIC_ABSTRACTED`

Verified owner sources define domain truth. Public documentation explains that truth in reduced form and creates no authority of its own.

```mermaid
flowchart LR
    S["Verified domain sources"] -->|"reviewed semantics"| P["Public projection"]
    E["External concepts"] -->|"clearly attributed rationale"| P
    P -->|"explainable principles"| H["People and organizations"]
    P -.->|"no authority backflow"| S
```

Candidates remain candidates. Publication is not adoption; adoption is not runtime activation. Exact source states are verified internally but are not published as an operational map.

> Conceptual public projection — not deployment, service, repository, protocol or security topology.
