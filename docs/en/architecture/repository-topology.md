# Responsibility and trust domains

Status: `PUBLIC_ABSTRACTED`

The public architecture shows responsibility roles, not repository, service or deployment topology.

```mermaid
flowchart TB
    IK["Institutional knowledge"] -->|"reviewed context"| CR["Context and cognition"]
    GOV["Governance and authority"] -->|"governed permission"| EX["Governed execution"]
    CR -->|"proposal"| EX
    EX -->|"receipt and verification"| EV["Evidence and provenance"]
    PC["Personal continuity"] -.->|"explicit bounded contribution"| IK
    UI["Human interaction"] -->|"objectives and decisions"| GOV
```

Physical allocation, internal contracts and enforcement chains remain in the responsible internal sources.

> Conceptual public projection — not deployment, service, repository, protocol or security topology.
