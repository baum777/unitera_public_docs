# Current Public State — 2026-08-30

**Status:** PUBLIC SNAPSHOT — descriptive, not authoritative  
**Authority:** none by itself  
**Source basis:** exact refs in `PUBLICATION_MANIFEST.yaml`, remote branch comparison, and supplied 2026-08-15 source-reconciliation material

## Overall result

`PARTIAL` — UNITERA has a materially implemented governed core, while self-service onboarding, canonical Discovery, full cognition runtime, and end-to-end production qualification remain incomplete.

## Canonical owner-repository state

| Surface | Evidence | Rating | Public interpretation |
|---|---|---|---|
| Foundation and Company Brain | `coreos@3f23e2f` | **pass** | Active founder baseline, deterministic Prime projection, review/promotion contracts, governance validation and CI are owner-repository concerns. |
| Provider-neutral execution control | `unitera-os@18c50f8` | **pass** | Capability, grant, receipt, policy and execution-control contracts are canonical here; build/test/typecheck/conformance run in CI. |
| Tenant and Governance authority | `unitera_control_plane@10e2a39` | **pass / partial downstream** | Physical owner, assignment topology, contract v3 and pilot policy are materialized; consumer runtime qualification remains separate. |
| Product/runtime consumer | `Unitera_Systems@786d03c` | **partial** | Hosted auth, authority runtime, persistence, APIs, product surfaces and bounded execution controls exist; not every broader UNITERA lifecycle is canonical or production-qualified. |
| Cross-repository Registry | `unitera-registry@a2f4cca` | **pass as reference layer** | Schema `1.1.0`, offline validation and reachability enforcement are materialized; Registry remains non-authoritative. |


## Personal Realm owner decision

The Personal Realm architecture has moved beyond the earlier open candidate stage: the 20-step Owner Grill-Me is finalized and `baum777/unitera_companion` is the designated semantic owner surface. The current architecture foundation is materialized on branch `architecture/personal-realm-foundation@cb59971c` in PR #1 and is **not yet merged to owner `main`**.

Public interpretation:

~~~text
Owner decision = finalized
Owner-repo materialization = qualified PR branch
Cross-repo adoption = pending
Runtime activation = none
~~~

The owner-decided direction includes Personal Realm naming, local-first/multi-node continuity, hardware-key-signed backup/recovery, Personal Memory residency controls, first-class Circling semantics, PersonalIdea/PersonalConcept/PersonalPlan, explicit personal→institutional contribution, capability-specific Companion autonomy, and the tiered Companion Shadow Guard.

## Product journey status

```mermaid
flowchart LR
    A[Hosted sign-in<br/>MATERIALIZED] --> B[Profile<br/>OPEN]
    B --> C[Tenant bootstrap<br/>OPEN]
    C --> D[Discovery<br/>QUALIFIED BRANCH]
    D --> E[Activation and First Work<br/>PARTIAL]
    E --> F[/work<br/>PARTIAL]
```

| Journey step | Rating | Basis |
|---|---|---|
| Hosted OIDC sign-in and opaque session | **pass** | Canonical routes, session service, internal IdP bindings, membership-derived role, RLS-aware resolution, signed BFF proxy. |
| Public sign-up | **missing** | No canonical production-ready self-service lifecycle evidenced. |
| Personal profile | **missing** | No required profile-completion contract and handoff evidenced. |
| Tenant bootstrap/selection | **partial / blocked for self-service** | Tenant authority exists, but public self-service ownership and initial membership flow are not closed. |
| Discovery runtime | **partial** | Qualified at branch `7f7a3b3`, 11 commits ahead of canonical main; not merged or production-active. |
| First Work and `/work` | **partial** | Work-first direction and several read-model/product surfaces exist; full activation-to-first-work journey remains dependent on canonical lifecycle integration. |

## Runtime status

| Runtime | Rating | Boundary |
|---|---|---|
| KNOW / Company Brain consumption | **partial to materialized** | Owner truth stays in `coreos`; runtime consumption must remain integrity-bound. |
| THINK / cognition | **partial** | Compute-envelope contract is on main; full root/child run admission, lifecycle, ledger, memory and production backend remain open. |
| ACT / governed effect | **materialized bounded core** | `email.send.commit` remains the single bounded v1 effect reference; broader integrations do not silently expand this boundary. |
| Local Runtime Node | **candidate** | No canonical runtime activation. |
| Personal Realm / Companion | **owner-decided architecture / qualified owner branch** | Dedicated owner surface and detailed architecture are materialized in `unitera_companion` PR #1; contracts, cross-repo adoption and runtime remain pending. |

## Explicit non-claims

This snapshot does not claim:

- a production-ready public sign-up and onboarding funnel;
- Discovery on canonical `Unitera_Systems/main`;
- production deployment or customer reachability of the branch-qualified Discovery slice;
- complete cognition runtime activation;
- unrestricted autonomy;
- a merged/canonical `unitera_companion/main` architecture state or activated Personal Realm runtime;
- automatic regulatory compliance or certification.

## Next documentary gate

Update this snapshot when any of the following changes canonically: self-service identity/profile/tenant contracts, Discovery merge, deployed end-to-end onboarding proof, cognition runtime admission/lifecycle, Personal Realm owner-branch merge/cross-repo adoption/runtime proof, or Registry bindings for those material changes.
