# Authority & Source-of-Truth Model

**Status:** PUBLIC PROJECTION

## Authority domains

| Domain | Owning surface | Public interpretation |
|---|---|---|
| Foundation, identity, Company Brain | `coreos` | Established authority domain |
| Agent autonomy, capability, policy, grant, execution contracts | `unitera-os` | Established provider-neutral authority domain |
| Runtime, persistence, API, integrations, product enforcement | `Unitera_Systems` | Established implementation/runtime boundary |
| Tenant control-plane authority | dedicated Tenant Control Plane authority surface | Owner-decided direction; adoption/materialization status must be checked before stronger claims |
| Cross-repo Registry | Registry surface | Reference/provenance layer only; never authority by itself |
| This repository | `unitera_public_docs` | Public documentation projection only |

```mermaid
flowchart TD
    CORE[coreos] -->|Foundation / Company Brain| SYS[Unitera_Systems]
    OS[unitera-os] -->|Provider-neutral contracts| SYS
    TCP[Tenant Control Plane] -->|Tenant authority / bindings| SYS

    CORE --> REG[Registry]
    OS --> REG
    SYS --> REG
    TCP --> REG

    REG --> DOCS[Public Docs]

    DOCS -. no authority backflow .-> REG
    REG -. no authority backflow .-> CORE
    REG -. no authority backflow .-> OS
    REG -. no authority backflow .-> SYS
```

## Principle

The Registry may record references, adoption state, digests, provenance, supersessions, dependency bindings, and qualified implementation bindings. It cannot create semantic, contract, tenant, execution, or runtime authority.

The public documentation layer adds **zero** authority. It exists to make the verified system state understandable.
