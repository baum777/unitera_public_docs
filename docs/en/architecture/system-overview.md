# System Overview

**Status:** PUBLIC PROJECTION  
**Authority:** none by itself

UNITERA separates organizational knowledge, cognition, and external action so that richer AI reasoning cannot silently expand business authority.

```mermaid
flowchart TB
    subgraph KNOW[KNOW — Context Runtime]
      E[Evidence]
      CB[Company Brain]
      C[Compiled Context]
      E --> CB --> C
    end

    subgraph THINK[THINK — Cognition Runtime]
      AN[Analysis]
      PL["Planning / Replanning"]
      AP[Action Proposal]
      AN --> PL --> AP
    end

    subgraph ACT[ACT — Execution Control]
      CR[Capability Request]
      PE[Policy & Effective Autonomy]
      HC[Human Control if required]
      GR[Capability Grant]
      EX[Trusted Executor]
      CR --> PE --> HC --> GR --> EX
    end

    C --> AN
    AP --> CR
    EX --> XS[External System]
    XS --> RC[Receipt]
    RC --> VR["Verification / Reconciliation"]
```

## System thesis

UNITERA can be summarized as **evidence-grounded, context-compiled, authority-separated execution**.

The architecture intentionally avoids treating a model, prompt, harness, external tool, or adapter as an authority boundary. Authority remains explicit in owning domains and runtime enforcement.
