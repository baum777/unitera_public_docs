# Source Basis

**Snapshot date:** 2026-08-30  
**Repository role:** PUBLIC DOCUMENTATION PROJECTION  
**Authority:** none by itself

## Verified owner-repository refs

| Owning repository | Verified default-branch ref | Used for |
|---|---|---|
| baum777/coreos | 3f23e2fa920f8b3bfe78d7fe898078ff924c1814 | Foundation, Company Brain, promotion and governance posture |
| baum777/unitera-os | 18c50f837aa5442d29edf0bae7f0beb5fd9fa94b | Provider-neutral capability/autonomy/execution contracts |
| baum777/Unitera_Systems | 786d03ca731acf5ab1af38731954891e84542d8c | Runtime, persistence, API, hosted auth, product and consumer enforcement |
| baum777/unitera_control_plane | 10e2a3953a76a892cb4112dcf9c1f7998d970970 | Tenant/Governance physical ownership, assignment topology and pilot policy |
| baum777/unitera-registry | a2f4ccac009305741e463eba99069e8052c172fd | Registry schema, reference contract, validation and reachability posture |

## Qualified noncanonical evidence

Discovery documentation also reads the remote branch:

~~~yaml
repository: baum777/Unitera_Systems
ref: codex/discovery-pilot-readiness-closure
head: 7f7a3b35e957dafaf0d3cb11eb46c5788ddecdfe
compared_to_main:
  ahead_by: 11
  behind_by: 0
classification: QUALIFIED_DEVELOPMENT_SLICE
~~~

Branch evidence is never presented as canonical main or production activation.

Personal Realm documentation additionally reads the owner-designated repository review branch:

~~~yaml
repository: baum777/unitera_companion
ref: architecture/personal-realm-foundation
head: cb59971c8f171954e979a0f8a6fccbd5a0176116
pull_request: 1
classification: OWNER_DECISIONS_FINALIZED_OWNER_MATERIALIZATION_IN_REVIEW
owner_main_merged: false
cross_repo_adoption_complete: false
runtime_activated: false
~~~

This branch is used because the Owner Grill-Me decisions are finalized and materialized there, while the owner repository's default branch has not yet adopted the architecture foundation.

## Supplied source-reconciliation material

The 2026-08-15 bundle supplied with this review covers:

- system architecture and authority precedence;
- Tenant, Discovery, epistemic state and Company Brain lifecycle;
- KNOW / THINK / ACT and autonomy/security boundaries;
- lifecycle gates, bindings and semantic core;
- source state, conflicts, adoption and supersession candidates;
- security-logic derivation and negative-test families.

Those artifacts explicitly include frozen specs, owner decisions pending adoption, candidates, and derived non-authoritative summaries. Their classifications are preserved.

## Later supplied source candidates

The public projection of the Local Runtime Node additionally uses:

- UNITERA Local Runtime Node & Device Capability Boundary, Spec-ID UNITERA-LOCAL-RUNTIME-NODE-DEVICE-CAPABILITY-BOUNDARY-001, version 0.1.0, status SOURCE_CANDIDATE_NON_AUTHORITATIVE;
- UNITERA Local Runtime Node — Device Identity & Enrollment Amendment v0.1.1, status SOURCE_CANDIDATE_READY_NON_AUTHORITATIVE.

These materials are documented strictly as candidates. They do not prove owner-surface adoption, runtime activation, production execution, or source-pointer activation.

## Additional source candidates and architecture directions

The coherent Architecture & Logic projection additionally considers the following supplied materials, none of which becomes canonical merely through publication:

- UNITERA Backend-Agnostic Processing and Governed Route Resolution Source Candidate, version 0.1.0, status SOURCE_CANDIDATE_NON_AUTHORITATIVE;
- UNITERA Open-Weights Model Infrastructure — Long-Term Architecture Plan, version 0.1.0, status LONG_TERM_ARCHITECTURE_DIRECTION_NON_AUTHORITATIVE;
- UNITERA Canonical Naming, Terms & Definitions Ruling Specification, version 0.1.0, status RULING_SOURCE_CANDIDATE_READY_FOR_OWNER_BINDING;
- the earlier UNITERA Personal Domain, Member Companion, Personal Memory & Circling v0.1.0 candidate as historical/source-reconciliation basis, now superseded in public terminology and owner direction by the qualified `unitera_companion` Personal Realm owner materialization;
- source-reconciled runtime/harness complements covering Runtime State, memory, handoff, evaluation, and failure attribution where the public system explanation explicitly labels them as candidate direction.

These materials extend the explanation of the system model. They may not override verified owner-repository authority and create no routing, model, tenant, memory, naming, or execution authority.

The public projection of pilot model selection and OpenRouter routing additionally uses:

- `UNITERA Backend-Agnostic Processing and Governed Route Resolution Source Candidate`, version 0.1.0, status `SOURCE_CANDIDATE_NON_AUTHORITATIVE`;
- `UNITERA Open-Weights Model Infrastructure — Long-Term Architecture Plan`, version 0.1.0, status `LONG_TERM_ARCHITECTURE_DIRECTION_NON_AUTHORITATIVE`;
- dated model-comparison and harness-evaluation evidence from Discovery / Grill-Me pilot runs performed on 2026-08-29–30.

The model-comparison evidence is treated as **Pilot Working Evidence**. It establishes neither general model superiority nor a permanent provider/model binding. Concrete runtime bindings still require separate verification before activation.

## Pointer posture

The supplied source-state snapshot reports candidate_pointer_not_activated. This review verified later owner-repository states individually; it did not verify a separate unified pointer activation. Therefore no such activation is claimed.

## Evidence classes

- **Observed:** read from exact GitHub refs, trees, commits, branch comparisons, files, or review metadata.
- **Source-derived:** summarized from the supplied bundle or explicitly named source candidates while preserving the original maturity label.
- **Inferred:** explicitly labeled reasoning from observed evidence.
- **Unverified:** excluded from materialized or production claims.

## Conflict rule

If this public projection differs from a verified owner artifact, the owner artifact wins. If owner sources conflict or cannot be verified, the public document must say OPEN.

## Personal Realm source-state note

For Personal Realm, the public documentation may state that the **Owner decisions are finalized** and that `unitera_companion` is the **owner-designated semantic surface**. It must simultaneously state that the current architecture artifacts are still on PR #1 / branch `architecture/personal-realm-foundation`, that cross-repository adoption is pending, and that no runtime or production execution has been activated by those documents.
