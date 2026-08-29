# Sign-up → Tenant → Discovery Journey

**Status:** PUBLIC PROJECTION with explicit implementation gaps  
**Authority:** none by itself  
**Source basis:** `Unitera_Systems/main@786d03c`, Discovery branch `7f7a3b3`, and supplied Tenant/Product/Company Brain sources

## Intended production journey

```mermaid
flowchart TD
    V[Visitor] --> I[Hosted Sign-up or Sign-in]
    I --> S[Opaque hosted session]
    S --> P[Personal profile]
    P --> T[Tenant bootstrap or selection]
    T --> M[Verified membership and role]
    M --> F[First Contact]
    F --> D[Discovery workspace]
    D --> C[Claims, sources, conflicts, open decisions]
    C --> R[Server-side readiness]
    R --> B[Candidate and exact-revision review]
    B --> A[Materialization and activation]
    A --> W[First advisory Work Order]
    W --> X[/work]
```

This is the semantically correct end-to-end journey. It is **not** yet one fully canonical production flow.

## What is canonical on `Unitera_Systems/main`

Hosted authentication is materially implemented:

```mermaid
sequenceDiagram
    participant U as User
    participant W as Web BFF
    participant I as OIDC Provider
    participant A as UNITERA API
    participant D as PostgreSQL

    U->>W: Start hosted sign-in
    W->>I: OIDC Authorization Code + PKCE
    I-->>W: Callback
    W->>A: Signed method-bound proxy request
    A->>D: Resolve subject + organization bindings
    D-->>A: Internal user + tenant + membership role
    A-->>W: Opaque hosted session cookie
    W-->>U: Authenticated product handoff
```

The important boundary is:

```text
external OIDC identity
!= internal user
!= tenant
!= membership authority
```

External subject and organization identifiers are resolved through provisioned internal bindings. Roles remain membership-derived, and tenant-scoped resolution runs under PostgreSQL isolation.

## What is not yet canonical

The repository tree and route surface do not currently evidence a complete self-service chain for:

- public account creation under UNITERA-owned lifecycle rules;
- required personal-profile completion;
- safe tenant creation/selection and ownership establishment;
- controlled initial membership provisioning;
- a canonical handoff from those states into Discovery.

Hosted sign-in readiness must therefore not be described as production-ready sign-up/onboarding readiness.

## Discovery implementation posture

The remote branch `codex/discovery-pilot-readiness-closure` is currently 11 commits ahead of and 0 behind `Unitera_Systems/main`, at `7f7a3b35e957dafaf0d3cb11eb46c5788ddecdfe`.

It contains a qualified development slice with:

- tenant-isolated Discovery persistence and migration `0050`;
- API controller, service, repository, and deterministic cognition backend;
- `/work/discovery` and session UI routes;
- structured knowledge, provenance, review, and first-work projections;
- integration, smoke, negative-boundary, and qualification evidence.

The branch reports build, migrations, governance, premerge, and 1,845-test qualification with a database. Because it is not canonical `main`, this repository labels it **QUALIFIED DEVELOPMENT SLICE**, not production-active.

## Product closure gates

```mermaid
flowchart LR
    A[Hosted sign-in] --> B[Self-service identity lifecycle]
    B --> C[Profile contract]
    C --> D[Tenant bootstrap and membership]
    D --> E[Discovery admission]
    E --> F[Canonical merge and deployment qualification]
```

The production-ready onboarding slice closes only when each transition has an owning contract, fail-closed error state, tenant-isolation proof, migration path, canonical-main materialization, and deployed end-to-end evidence.
