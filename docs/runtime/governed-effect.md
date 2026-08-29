# Governed External Effect

**Status:** ESTABLISHED architecture; exact runtime availability depends on the owning implementation surface.

UNITERA separates approval, grant, external execution, receipt, and verification. External effects must not be dispatched directly from cognition.

```mermaid
sequenceDiagram
    participant AI as Cognition / Agent
    participant EC as Execution Control
    participant H as Human Control
    participant X as Trusted Executor
    participant P as External Provider
    participant A as Audit / Evidence

    AI->>EC: Action Proposal / Capability Request
    EC->>EC: Tenant + policy + autonomy evaluation
    alt human control required
        EC->>H: Review / approval request
        H-->>EC: Approval decision
    end
    EC->>EC: Capability Grant + pre-dispatch re-evaluation
    EC->>X: Authorized execution request
    X->>P: External effect
    P-->>X: Provider response
    X-->>EC: Receipt
    EC->>A: Append evidence
    EC->>EC: Verify / reconcile outcome
```

## v1 effect boundary

The established technical reference for the single bounded v1 external capability is `email.send.commit`. Broader business workflows may compose around it, but workflow names must not silently become new atomic capabilities.

## Failure rule

Unknown external outcome is not permission to retry blindly. The system must reconcile uncertain effects before deciding whether another attempt is safe.
