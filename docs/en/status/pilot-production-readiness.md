# Pilot Production Readiness — 2026-08-31

**Status:** PUBLIC SNAPSHOT — descriptive, not authoritative  
**Authority:** none by itself  
**Source basis:** exact refs in `PUBLICATION_MANIFEST.yaml`  
**Related:** [Current public state](current-state.md), [Source basis](../reference/source-basis.md)

## Public verdict

```text
IMPLEMENTATION          = PARTIAL (bounded core materialized)
DISCOVERY ON MAIN       = YES (deterministic; LIVE_LLM_PROVIDER=NONE)
PP-00 REQUALIFICATION   = PARTIAL
PP-07 DualControl       = BLOCKED (open PR #98)
PP-09 Effect preview    = BLOCKED
PP-12 Recovery path     = PARTIAL
OWNER FREEZE            = FREEZE_NOT_AUTHORIZED
PILOT ACTIVATION        = NOT_AUTHORIZED
PRODUCTION EXECUTION    = NO
LIVE LLM PROVIDER       = NONE
V1 EFFECTFUL SET        = email.send.commit only
SOURCE POINTER          = NOT_CHANGED
```

This page does not authorize a pilot, change a source pointer, or declare production readiness.

## What is on current owner main

| Surface | Current verified main | Readiness meaning |
|---|---|---|
| `Unitera_Systems` | `f4debe6` | Hosted auth, authority runtime, Discovery PR #94, WP-030, WP-035. No live LLM. No production execution. |
| `unitera-registry` | `1de27e8` | WP-002 freeze projection merged. Result remains `FREEZE_NOT_AUTHORIZED`. |
| `unitera-os` | `36718e9` | Execution-control contracts plus LRN-C1 local-node contracts. Runtime unactivated. |
| `unitera_control_plane` | `021ead9` | Tenant/Governance authority and Decision-Class taxonomy. Contract v3 still records runtime enforcement `NOT_MATERIALIZED`. |
| `coreos` | `c34b61a` | Company Brain / Foundation semantics. |
| `unitera_companion` | `526177e` | Personal Realm owner foundation and Gate-1 contract freeze. No runtime. |
| `unitera-production-interface` | `afa92cf` | Product UI+BFF. Live effects off. |

## What remains off current main

| Item | State | May close a current-main gate? |
|---|---|---|
| Unitera_Systems PR #98 (`05b47e3`) | open, qualified in review, base lags `main` | No |
| Unitera_Systems PR #95 / #92 | open cognition-authority rematerialization | No |
| Draft PRs #83 / #72 / #59 | draft / noncanonical | No |

## Freeze vs later merges

The Registry freeze report is merged and remains unauthorized. Two blockers stand:

1. commit-bound independent review of originally self-merged owner surfaces;
2. explicit TCP owner declaration that runtime enforcement is current.

The report's internally recorded freeze-review heads lag current owner mains. Later merges (Discovery, LRN-C1, Decision-Class taxonomy, WP-030/035) do not authorize the freeze.

## Activation is a later act

Even after an owner freeze, pilot activation remains a separate owner act. Still externally blocked:

- owner enforcement / freeze declaration;
- concrete provider activation;
- live credential for `email.send.commit`;
- real tenant binding (OD-06);
- independent review of unreviewed surfaces.

## Non-claims

This page does not claim production-ready onboarding, a live LLM, an authorized freeze, a changed source pointer, live production execution, unrestricted autonomy, or regulatory certification.
