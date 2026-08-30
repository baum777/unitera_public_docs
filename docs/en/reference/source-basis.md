# Source Basis

**Snapshot date:** 2026-08-30  
**Repository role:** PUBLIC DOCUMENTATION PROJECTION  
**Authority:** none by itself

## Verified default-branch refs

| Repository | Verified default-branch ref | Used for |
|---|---|---|
| baum777/coreos | c34b61a9264348afaaae96c5b94e169011bf76ab | Foundation, Company Brain, Tenant-Foundation semantics and current owner-boundary posture |
| baum777/unitera-os | 18c50f837aa5442d29edf0bae7f0beb5fd9fa94b | Provider-neutral capability/autonomy/execution contracts and CI-gated conformance |
| baum777/Unitera_Systems | 786d03ca731acf5ab1af38731954891e84542d8c | Canonical runtime consumer, persistence, APIs, hosted auth and bounded authority enforcement |
| baum777/unitera_control_plane | fc9370eb146dd068027f9dd9b3a7bdd01626bb65 | Current Tenant/Governance owner-repository head; earlier contract revisions remain cited where they are the exact semantic subject |
| baum777/unitera-registry | 891f9b967328131d8d3348ffba3dc64e7c1163ac | Registry contract, provenance, continuous reachability and RCC/digest-verification closure |
| baum777/unitera_companion | 8dd8112a74631516c134bc3fc528d6220cdd27a7 | Personal Realm owner decisions and merged architecture foundation |

These refs identify the current verified default branches at review time. A newer repository head does not retroactively change the scope of a decision or review that was bound to an earlier exact commit.

## Verified implementation projection

The dedicated Production Pilot Interface is separately verified:

~~~yaml
repository: baum777/unitera-production-interface
ref: main
head: d7cbf8ce78bb7c2e5737a126d972dfd638a378fd
role: PRODUCT_UI_PLUS_BFF
semantic_authority: NONE_BY_IMPLEMENTATION
production_execution_activated: false
live_effect_active: false
~~~

Its merged PR #1 contains the migration-closure stack and governed Settings/Profile product surface. The qualified PR head `9e688b94b3335a625543a39aeb9873b1d88444e5` has an observed successful remote `ci` run.

This repository is evidence for product/UI/BFF materialization, not a replacement authority source for Tenant, Membership, Company Brain, Capability, Grant or Execution semantics.

## Qualified noncanonical evidence

### Discovery runtime — Unitera_Systems PR #94

~~~yaml
repository: baum777/Unitera_Systems
ref: codex/discovery-pilot-readiness-closure
head: 19e70f220a83c331b7fc7f4c9bbd9e3ff9d35893
pull_request: 94
compared_to_main:
  ahead_by: 15
  behind_by: 0
classification: QUALIFIED_DEVELOPMENT_SLICE
canonical_main: false
runtime_activation_claimed: false
~~~

This branch contains Discovery persistence, deterministic cognition, structured knowledge/provenance, `/work/discovery`, First Work, RLS and qualification evidence.

Branch evidence is never presented as canonical main or production activation.

### Pilot UI / identity / decision integration — Unitera_Systems PR #98

~~~yaml
repository: baum777/Unitera_Systems
ref: pilot-ui-01/production-entry-readonly-pilot
head: 903f0250dd754ecc6ddaa87752a86e5c2c1a7f4d
pull_request: 98
classification: QUALIFIED_INTEGRATION_IN_REVIEW
canonical_main: false
remote_workflows:
  audit_gates: success
  visual_enforcement_level_2: success
  canonical_enforcement: success
  governance_guardrails: success
  ci: success
~~~

This branch is used only for claims explicitly labeled as noncanonical integration progress. It currently carries natural-person identity/attestation, HumanDecision/DualControlSet, broader Work read models and a read-only pilot product entry.

Passing workflows do not turn this branch into owner authority, source adoption, runtime activation or production permission.

## Personal Realm source-state update

The earlier public projection treated `unitera_companion/architecture/personal-realm-foundation@cb59971c` as an open owner-materialization PR.

That state is superseded: PR #1 was merged on 2026-08-30, and `unitera_companion/main@8dd8112` now contains the owner-designated architecture foundation.

Current posture:

~~~yaml
owner_decisions_finalized: true
owner_main_merged: true
cross_repo_adoption_complete: false
runtime_activated: false
production_execution_authorized: false
~~~

## Registry integrity state

`unitera-registry@891f9b9` includes the RCC/digest-verification closure.

Observed result from the merged review program:

~~~text
digest assertions classified: 188 / 188
exact recalculable matches: 130
non-recalculable-by-design: 58
unresolved: 0

live reachability:
verified: 163
mismatch: 0
unverifiable: 0
record gaps: 0
~~~

This proves integrity/reachability properties of Registry assertions. It does **not** create Source adoption or Authority.

The same Registry still reports `FREEZE_NOT_AUTHORIZED` for the pilot authority freeze because independent-review and Tenant-Control-Plane runtime-conformance declaration gates remain open.

## Supplied source-reconciliation material

The 2026-08-15 bundle supplied with this project review covers:

- system architecture and authority precedence;
- Tenant, Discovery, epistemic state and Company Brain lifecycle;
- KNOW / THINK / ACT and autonomy/security boundaries;
- lifecycle gates, bindings and semantic core;
- source state, conflicts, adoption and supersession candidates;
- security-logic derivation and negative-test families.

Those artifacts explicitly include frozen specs, owner decisions pending adoption, candidates, and derived non-authoritative summaries. Their classifications are preserved.

## Later supplied source candidates and architecture directions

The coherent public architecture projection additionally considers these supplied materials without upgrading their maturity merely through publication:

- UNITERA Local Runtime Node & Device Capability Boundary, v0.1.0, `SOURCE_CANDIDATE_NON_AUTHORITATIVE`;
- Local Runtime Node Device Identity & Enrollment amendment, candidate/non-authoritative;
- UNITERA Backend-Agnostic Processing and Governed Route Resolution, v0.1.0, `SOURCE_CANDIDATE_NON_AUTHORITATIVE`;
- UNITERA Open-Weights Model Infrastructure — Long-Term Architecture Plan, v0.1.0, `LONG_TERM_ARCHITECTURE_DIRECTION_NON_AUTHORITATIVE`;
- UNITERA Canonical Naming, Terms & Definitions Ruling Specification, v0.1.0, `RULING_SOURCE_CANDIDATE_READY_FOR_OWNER_BINDING`;
- historical Personal Domain / Member Companion / Personal Memory / Circling candidate material, now superseded in public terminology and owner direction by the merged Personal Realm owner foundation;
- source-reconciled runtime/harness complements covering Runtime State, memory, handoff, evaluation and failure attribution where explicitly labeled as candidate direction.

These materials may extend explanation. They may not override verified owner-repository authority.

## Pilot model-selection evidence

The public OpenRouter/model-routing page additionally uses:

- the backend-agnostic processing candidate;
- the Open-Weights long-term plan;
- dated model-comparison and harness-evaluation evidence from 2026-08-29–30.

That evidence remains **Pilot Working Evidence**.

No later chat-only provider/model decision is promoted here unless it is independently verifiable in an applicable repository surface. The current public page therefore remains a pilot architecture/working-plan document, not a permanent model/provider standard.

## Pointer posture

The current Registry evidence preserves:

~~~text
CURRENT_SOURCE_POINTER = NOT_CHANGED
pilot owner freeze = FREEZE_NOT_AUTHORIZED
~~~

This review does not claim a unified source-pointer activation.

## Evidence classes

- **Observed:** read from exact GitHub refs, trees, commits, branch comparisons, files, PR metadata, reviews or workflow results.
- **Source-derived:** summarized from supplied source material while preserving the source maturity label.
- **Inferred:** explicitly labeled reasoning from observed evidence.
- **Unverified:** excluded from canonical/materialized/production claims.

## Conflict rule

If this public projection differs from a verified owner artifact, the owner artifact wins. If owner sources conflict or cannot be verified, the public document must state the gap rather than silently resolve it.
