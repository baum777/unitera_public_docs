# Current Public State — 2026-08-30

**Status:** PUBLIC SNAPSHOT — descriptive, not authoritative  
**Authority:** none by itself  
**Source basis:** exact refs in `PUBLICATION_MANIFEST.yaml`, verified owner/implementation repositories, open-PR qualification evidence, and supplied source-reconciliation material

## Overall result

`PARTIAL` — UNITERA has a materially implemented governed core and several newly qualified product/runtime slices, while canonical self-service onboarding, canonical Discovery integration, cognition-runtime admission, pilot owner freeze, and production execution remain gated.

## Verified default-branch state

| Surface | Evidence | Rating | Public interpretation |
|---|---|---|---|
| Foundation and Company Brain | `coreos@c34b61a` | **pass / active owner semantics with open follow-up gates** | Foundation/Company-Brain semantics and the Tenant-Foundation consumer surface are owner-repository concerns. The latest consumer-contract rematerialization is present on main but explicitly remains a proposed/not-frozen boundary. |
| Provider-neutral execution control | `unitera-os@18c50f8` | **pass** | Capability, policy, autonomy, grant, receipt and execution-control contracts are canonical here; build/tests/typecheck/conformance are CI-gated. |
| Tenant and Governance authority | `unitera_control_plane@fc9370e` | **pass / partial downstream declaration** | Tenant/Governance authority and assignment topology are materialized. Registry evidence still records an open owner declaration for current runtime-enforcement conformance. |
| Product/runtime consumer | `Unitera_Systems@786d03c` | **partial** | Hosted auth, bounded authority/runtime enforcement, persistence, APIs and product surfaces exist; newer Discovery and pilot-UI integration remain on qualified open PRs. |
| Personal Realm semantic owner | `unitera_companion@8dd8112` | **owner foundation merged** | The Personal Realm owner decisions and architecture foundation are now on owner `main`. Cross-repository adoption, runtime activation and production execution remain separate and incomplete. |
| Cross-repository Registry | `unitera-registry@891f9b9` | **pass as reference/integrity layer** | RCC/digest verification closure is merged: 188/188 digest assertions classified, 130 exact matches, 58 non-recalculable-by-design, 0 unresolved; live reachability reported 163 verified, 0 mismatch, 0 unverifiable and 0 record gaps. Registry remains non-authoritative. |
| Production Interface | `unitera-production-interface@d7cbf8c` | **merged product UI+BFF implementation** | The dedicated Production Pilot Interface now contains the migration-closure stack plus governed Profile/Settings surfaces. It owns product UI/BFF materialization only; live effects and production execution remain off. |

## Personal Realm

The previous public snapshot said Personal Realm PR #1 was still open. That is no longer correct.

`baum777/unitera_companion` PR #1 was merged on 2026-08-30, producing owner-main merge commit `8dd8112a74631516c134bc3fc528d6220cdd27a7`.

~~~text
Owner decisions = finalized
Owner-repo architecture foundation = merged to main
Cross-repo adoption = pending
Runtime activation = none
Production execution = not authorized
~~~

The owner surface continues to preserve the hard boundary between personal continuity/memory and institutional truth/authority.

## Product journey status

```mermaid
flowchart LR
    A[Hosted sign-in<br/>MATERIALIZED] --> B[Profile / preferences<br/>PRODUCT SLICE MATERIALIZED]
    B --> C[Tenant bootstrap<br/>SELF-SERVICE GAP]
    C --> D[Discovery<br/>QUALIFIED OPEN PR]
    D --> E[Activation and First Work<br/>PARTIAL]
    E --> F[/work<br/>PARTIAL / INTEGRATION IN REVIEW]
```

| Journey step | Rating | Basis |
|---|---|---|
| Hosted OIDC sign-in and opaque session | **pass on canonical runtime** | Canonical routes, session service, internal identity bindings, membership-derived role and tenant-scoped resolution exist on `Unitera_Systems/main`. |
| Public sign-up | **missing as canonical self-service lifecycle** | No complete owner-backed public account/bootstrap lifecycle is proven end to end. |
| Personal profile / preferences | **materialized product projection** | `unitera-production-interface@d7cbf8c` provides governed Profile/Preferences/Account settings. These are product-owned settings and do not mutate Membership, Tenant authority or Company Brain. |
| Tenant bootstrap / initial membership | **partial / blocked for self-service** | Tenant authority exists, but the complete public self-service ownership/initial-membership handoff is not closed. |
| Discovery runtime | **qualified noncanonical** | PR #94, branch `codex/discovery-pilot-readiness-closure@19e70f2`, is 15 ahead / 0 behind canonical `Unitera_Systems/main`; it remains open and is not production-active. |
| First Work and `/work` | **partial, stronger integration in review** | Canonical work-first semantics exist. PR #98 adds a qualified read-only pilot/product integration stack but remains open. |

## Qualified integration slices that are not canonical main

### Discovery — PR #94

Current branch head:

```text
19e70f220a83c331b7fc7f4c9bbd9e3ff9d35893
ahead of Unitera_Systems/main: 15
behind: 0
```

The slice includes tenant-isolated Discovery persistence, deterministic cognition, structured knowledge/provenance, `/work/discovery`, First Work projections, RLS/integration evidence and governance admission. It still uses no live LLM provider and does not add a second effectful v1 capability.

### Pilot UI / identity / decision integration — PR #98

Current head:

```text
903f0250dd754ecc6ddaa87752a86e5c2c1a7f4d
```

The open PR materializes, **in-stack only**:

- natural-person identity / attestation / fail-closed independence evaluation;
- HumanDecision + DualControlSet persistence and server-side enforcement;
- broader Work Order state-vector/read-model projections;
- a read-only production-entry pilot and product navigation.

All five observed remote workflow families at this exact head are successful: Audit Gates, Visual Enforcement Level 2, Canonical Enforcement, Governance Guardrails and CI.

This means **qualified integration in review**, not canonical owner/runtime state and not production activation.

## Production Interface

`baum777/unitera-production-interface` is now a verified implementation repository with the explicit role:

```text
B — PRODUCT_UI_PLUS_BFF
```

PR #1 was merged as `d7cbf8c`. Its qualified head `9e688b9` had a successful remote `ci` run.

The merged product slice includes:

- migration-closure work;
- canonical identity-boundary and fail-closed effect guards;
- governed Profile and Preferences;
- Settings IA for Personal, Workspace and Expert/Admin projections;
- explicit disabled/unavailable role and invitation commands where no canonical command exists.

Hard boundary:

```text
Product UI / BFF
!= Tenant authority
!= Membership authority
!= Company Brain authority
!= Capability Grant
!= Dispatch
!= Verification
```

Production execution is **not activated** and the live effect adapter is **not active**.

## Pilot authority freeze

The current Registry freeze-readiness report remains:

```text
FREEZE_NOT_AUTHORIZED
```

The technical pilot path is substantially materialized, but two owner/governance conditions remain blocking in the verified Registry projection:

1. commit-bound independent review of originally self-merged owner surfaces;
2. an explicit Tenant Control Plane declaration reconciling the runtime-enforcement conformance state.

The unified/current source pointer remains unchanged. Pilot authorization is a separate later act.

## Runtime status

| Runtime | Rating | Boundary |
|---|---|---|
| KNOW / Company Brain consumption | **partial to materialized** | Owner truth stays in `coreos`; consumption remains exact-binding/integrity constrained. |
| THINK / cognition | **partial** | Compute-envelope contracts exist; complete root/child admission, lifecycle, ledger/memory and production backend activation remain gated. |
| ACT / governed effect | **materialized bounded core** | `email.send.commit` remains the single bounded v1 effect reference; no update here silently broadens effect scope. |
| Local Runtime Node | **candidate** | No canonical runtime activation. |
| Personal Realm / Companion | **owner foundation merged; runtime absent** | Owner semantics are on `unitera_companion/main`; cross-repo adoption and runtime remain pending. |
| Production Interface | **product implementation merged; effects off** | UI/BFF and Settings are materialized without gaining semantic authority or activating live execution. |

## Explicit non-claims

This snapshot does not claim:

- a production-ready public sign-up/onboarding funnel;
- Discovery merged to `Unitera_Systems/main`;
- PR #98 identity/dual-control/product integration as canonical while that PR remains open;
- a completed cognition-runtime activation;
- an authorized pilot owner freeze;
- a changed unified source pointer;
- live production execution in `unitera-production-interface`;
- unrestricted autonomy;
- automatic regulatory compliance or certification.

## Next documentary gate

Update this snapshot when one of these materially changes: Discovery PR #94 merge/status, Product Integration PR #98 merge/review, self-service identity/tenant bootstrap, cognition-runtime admission, pilot freeze blockers, Production Interface canonical wiring/staging/live-effect gate, Personal Realm cross-repo adoption/runtime, or a verified source-pointer decision.
