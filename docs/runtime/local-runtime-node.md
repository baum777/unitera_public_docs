# Local Runtime Node

**Status:** CANDIDATE — not repo-canonical, not source-adopted, not runtime-active by this document.

The Local Runtime Node is a proposed deployment and trust-boundary extension for governed access to a tenant's physical computer. It is **not a fourth KNOW/THINK/ACT plane**.

```mermaid
flowchart LR
    CP[Tenant Control Plane] -->|Enrollment authorization / TenantNodeBinding| N[Local Runtime Node]
    N -->|Scoped local resources| K[KNOW]
    A[ACT] -->|Governed effect request| N
    N -->|Outbound authenticated channel| S[Unitera_Systems]

    D[Local device key] --> N
    P[Local policy ceiling] --> N
    R[Resource descriptors] --> N
```

Candidate security posture:

- explicit enrollment authorization
- locally generated asymmetric operational key
- proof of possession
- separate TenantNodeBinding
- short-lived outbound channel
- local policy ceiling
- zero implicit resources, adapters, or grants at enrollment
- optional hardware attestation as an assurance enhancement

**Locality may reduce data movement; locality never creates trust or permission by itself.**
