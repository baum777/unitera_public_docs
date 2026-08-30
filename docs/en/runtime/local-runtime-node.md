# Local Runtime Node

**Status:** CANDIDATE — public projection of a SOURCE_CANDIDATE_NON_AUTHORITATIVE; not repo-canonical, not source-adopted, not runtime-active, and not production-authorized by this document.  
**Authority:** none by itself.  
**Source basis:** UNITERA-LOCAL-RUNTIME-NODE-DEVICE-CAPABILITY-BOUNDARY-001@0.1.0 plus the Device Identity & Enrollment Amendment v0.1.1.

[Deutsche Ausgabe](../../de/runtime/local-runtime-node.md)

## 1. Purpose and mental model

The **UNITERA Local Runtime Node** is a proposed local runtime and enforcement service running on a physical computer. It extends UNITERA in a governed way to local files, software, local services, and potentially additional device surfaces over time.

It is **not a fourth semantic plane** beside KNOW / THINK / ACT.

Its job is to:

- make local resources safely addressable and bounded for **KNOW**;
- provide concrete local technical execution routes for **ACT**;
- keep credentials local;
- enforce local policy as an additional ceiling;
- bind execution, receipts, verification, and failure evidence.

The core idea is:

> The model describes or proposes an effect. Authority is evaluated independently. The Local Runtime Node executes only the exact bound operation that is also permitted locally.

~~~mermaid
flowchart TB
    E[Evidence / Resources] --> K[KNOW<br/>Context Runtime]
    K --> T[THINK<br/>Cognition Runtime]
    T --> P[Action Proposal]
    P --> G[Policy / Human Control / Capability Grant]
    G --> B[Exact Route + Node + Adapter Binding]

    subgraph DEVICE["Physical Device Trust Boundary"]
        N[Local Runtime Node]
        R[Local Resources]
        A[Local Adapters]
        C[Credential Boundary]
        L[Local Policy / Sandbox]
    end

    B --> N
    N --> L
    L --> A
    A --> C
    A --> R
    A --> X[Local or external effect]
    X --> RC[Receipt]
    RC --> V[Verification / Reconciliation]
~~~

## 2. Hard semantic boundaries

The candidate preserves existing UNITERA separations and adds local variants:

~~~text
Context != Permission
Approval != Capability Grant
Grant != Dispatch
Receipt != Verification
Verification != Business Outcome

Local Reachability != Authority
Node Registration != Capability Grant
Node Enrollment != Capability Grant
Node Identity != Tenant Binding
Node Assignment != Capability Grant
OS Permission != UNITERA Permission

Local Resource Addressability != Model Read Permission
Read Permission != Write Permission

Installed Software != Trusted Adapter
Executable Presence != Allowed Operation
Local Adapter Availability != Capability Authority

Credential Availability != Credential Disclosure

Remote Grant != Local Policy Override
Local Policy Allowance != Remote Grant

Runtime Containment != Persistent Revocation

Local Execution != Trusted Execution
Remote Execution != Untrusted Execution
~~~

Most importantly: **locality is not a source of trust.** It may reduce data movement and keep credentials on-device, but it creates neither tenant authority, capability authority, nor execution authority.

## 3. Position in KNOW / THINK / ACT

### KNOW — local resource plane

For local information, the Node acts as a governed resource host:

~~~text
Local File / DB / App State
        ↓
Local Resource Adapter
        ↓
LocalResourceDescriptor
        ↓
tenant + purpose + policy evaluation
        ↓
LocalResourceHandle
        ↓
bounded / transformed content
        ↓
Context Runtime
        ↓
THINK
~~~

The model should not normally operate with unrestricted file paths or direct filesystem permissions. Instead, it receives tenant-bound, purpose-bound, time-bounded resource handles.

### THINK — remains independent

The Local Runtime Node does not become cognition authority. A model may run locally or remotely; neither deployment choice creates additional permission.

~~~text
better model != more authority
local model != trusted authority
~~~

### ACT — local effect plane

For real effects, the existing authority chain remains intact:

~~~text
Action Proposal
→ Capability Request
→ Effective Autonomy
→ Policy
→ Human Control where required
→ Capability Grant
→ Trusted Route Resolution
→ exact Local Node + Adapter Binding
→ local policy re-evaluation
→ credential resolution
→ sandboxed execution
→ Receipt
→ Verification / Reconciliation
~~~

## 4. Deployment topology

The preferred direction is **outbound-first**: the Node initiates an authenticated connection to the UNITERA runtime.

~~~mermaid
flowchart LR
    CP[Tenant Control Plane] -->|Enrollment authorization / TenantNodeBinding| S[UNITERA Runtime]
    N[Local Runtime Node] -->|authenticated outbound channel| S

    subgraph DEVICE["Physical computer"]
        N --> RB[Resource Broker]
        N --> AR[Adapter Registry]
        N --> LP[Local Policy Evaluator]
        N --> CB[Credential Broker]
        N --> SB[Sandbox / Process Broker]
        N --> ER[Evidence Recorder]
        N --> HM[Health Monitor]

        RB --> FS[Filesystem]
        AR --> SW[Software / Local Services]
    end
~~~

This means the architecture does **not require an internet-reachable inbound control port** on the user's computer as a baseline assumption.

A local browser or desktop UI may interact with the Node, but:

~~~text
localhost != authentication
loopback != authority
same device != permission
~~~

Principal, tenant, node, session, and allowed operation still need explicit resolution.

## 5. Node identity, enrollment, and tenant binding

### 5.1 Local operational identity

The candidate specifies that the Node generates its operational asymmetric key pair locally.

~~~text
Operational private key:
- on-device generated
- never returned by Control Plane
- never exposed to model
- non-exportable where supported
~~~

Preferred protection order:

~~~text
hardware-backed keystore
→ OS-protected keystore
→ encrypted local store
~~~

Candidate assurance classes:

~~~text
SOFTWARE_PROTECTED
OS_PROTECTED
HARDWARE_BACKED
~~~

The v0.1 amendment explicitly treats hardware attestation as **an assurance enhancement, not an initial prerequisite**. Stronger profiles may require it later.

### 5.2 Enrollment authority

A device may **initiate** enrollment but may never **authorize** its own enrollment:

~~~text
self-initiation = allowed
self-authorization = forbidden
~~~

A tenant-bound NodeEnrollmentAuthorization must already exist.

~~~text
Enrollment Token != Enrollment Decision
~~~

### 5.3 Enrollment protocol

~~~mermaid
sequenceDiagram
    participant H as Authorized Human / Governance
    participant CP as Tenant Control Plane
    participant N as Local Node
    participant R as UNITERA Runtime

    H->>CP: Authorize node enrollment
    CP-->>N: Short-lived enrollment credential
    N->>N: Generate operational key
    N->>CP: NodeEnrollmentInitiate
    CP-->>N: Challenge
    N->>CP: Proof of possession
    CP->>CP: Integrity + tenant checks
    CP-->>N: Enrollment commit + short-lived channel credential
    N->>R: Authenticated outbound connection
    R-->>N: Node session established
~~~

### 5.4 Durable object separation

The source deliberately separates:

~~~text
LocalNodeIdentity
!= TenantNodeBinding
!= NodeRuntimeStatus
!= NodeIdentityAssuranceRecord
!= NodeRuntimeIntegrityRecord
!= NodePolicyBinding
~~~

A successfully installed or enrolled device is therefore not automatically permitted to expose resources or execute effects.

## 6. Initial zero-authority policy

Every newly enrolled Node begins under:

~~~text
ENROLLMENT_ONLY
~~~

Allowed:

- authenticated channel;
- heartbeat;
- health reporting;
- credential rotation;
- re-attestation.

Denied:

- resource access;
- resource registration;
- adapter execution;
- business credential resolution;
- effectful execution;
- non-Control-Plane network access.

Therefore:

~~~text
Successful Enrollment
!= Resource Permission
!= Adapter Permission
!= Capability Grant
~~~

## 7. Node lifecycle

Candidate lifecycle:

~~~text
untrusted
→ enrollment_authorized
→ enrollment_pending
→ provisional
→ channel_proven
→ active
~~~

Additional operating states:

~~~text
degraded
quarantined
suspended
revoked
retired
~~~

Meaning:

- **active** only means the Node is available to participate in protocols allowed by its current policy.
- **degraded** may retain read/prepare surfaces if policy permits.
- **quarantined** receives no new effectful dispatches.
- **revoked** persistently invalidates dependent eligibility according to Tenant Control Plane authority.
- re-registration must not silently restore revoked authority.

Runtime containment and persistent revocation remain separate responsibilities.

## 8. Core contract family

The source proposes the following logical objects:

| Object | Purpose | Explicitly is not |
|---|---|---|
| LocalNodeRef | stable reference to node + tenant context | Node Authority / Grant |
| LocalNodeIdentity | operational device identity | Tenant Binding / User Identity |
| TenantNodeBinding | tenant-authorized binding of the node | Agent Assignment / Grant |
| NodeSurfaceManifest | technically available resource/adapter surface | Business Permission |
| LocalResourceDescriptor | registered local resource with classification/provenance | Model Permission |
| LocalResourceHandle | purpose-bound bounded access for KNOW | Credential / Write Permission |
| LocalAdapterDescriptor | versioned technical adapter descriptor | Capability |
| LocalAdapterBinding | exact semantic ↔ implementation binding | Grant |
| LocalPolicyProfile | local ceiling for resource/process/network/credential rules | central authority |
| NodeExecutionBinding | exact bound execution parameters | Credential |
| LocalExecutionReceipt | evidence about execution attempt/state | Verification |
| LocalVerificationEvidence | subsequent state verification | Business Outcome |

## 9. Resource plane — KNOW

### 9.1 Registration

~~~text
local file/app/db exists
→ explicit user selection or governed local discovery
→ LocalResourceDescriptor candidate
→ tenant/node policy evaluation
→ registered resource
~~~

**Discovery alone does not create model visibility.**

### 9.2 Resolution

~~~text
Context Runtime requests resource
→ verify tenant/node binding
→ verify purpose
→ verify access class
→ resolve revision/freshness
→ minimize / transform
→ issue LocalResourceHandle
→ return bounded content or derived observation
~~~

Candidate access modes:

~~~text
metadata
search
bounded_read
transformed_read
privileged_read
~~~

### 9.3 Path minimization

Prefer a resource ID plus an opaque local locator rather than propagating full local paths into model context by default.

### 9.4 Read-before-write / stale-state protection

Future mutations should bind to the state that was actually inspected:

~~~text
read / inspect
→ observation digest/version
→ proposed mutation
→ pre-write version check
→ write only if still valid
~~~

If the underlying state changed:

~~~text
stale
→ reject or re-resolve
~~~

Never:

~~~text
stale
→ blind overwrite
~~~

## 10. Effect plane — ACT

Immediately before local execution, the Node must re-check:

- tenant match;
- active TenantNodeBinding;
- valid Tenant Agent Assignment;
- valid, unexpired, non-revoked grant;
- exact target binding;
- exact payload digest;
- exact context binding digest;
- exact adapter binding digest;
- current local policy revision;
- adapter health;
- required sandbox availability;
- credential profile availability;
- allowed network route;
- idempotency state.

Material drift after review or grant:

~~~text
→ no dispatch
→ re-evaluation required
~~~

Unknown effect:

~~~text
unknown_effect
→ reconciliation
~~~

and explicitly not:

~~~text
unknown_effect
→ automatic retry
~~~

## 11. Local effective permission

The local runtime may only **attenuate** permission further:

~~~text
local_effective_permission
=
capability_grant
∩ tenant_node_binding
∩ tenant_agent_assignment
∩ node_surface_manifest
∩ local_adapter_binding
∩ local_policy_profile
∩ sandbox_state
∩ credential_profile_state
∩ runtime_health
∩ network_policy
∩ revocation_state
∩ expiry
~~~

Required invariants:

~~~text
local_effective_permission <= capability_grant
local_effective_permission <= local_policy_ceiling
~~~

Therefore:

~~~text
central grant + local deny = DENY
local allow + no central grant = DENY
~~~

Neither side can independently widen the other's authority.

## 12. Credential boundary

Raw credentials remain outside model context, conversation history, action proposals, capability-grant payloads, general logs, and adapter metadata.

Use:

~~~text
CredentialProfileRef
→ local Credential Broker
→ ephemeral execution material
→ exact adapter invocation
~~~

Candidate secret stores are **not canonicalized**. The source only lists possible implementations such as OS keychains, secret services, hardware-backed keys, or a local encrypted vault.

Core rule:

~~~text
adapter may use secret
!=
model may read secret
~~~

## 13. Sandbox and local enforcement

A production-grade Node would need to constrain at least:

~~~text
filesystem
process
network
IPC
credential access
device access
resource quotas
temporary storage
child process tree
environment variables
local socket access
~~~

Candidate profiles:

~~~text
READ_ONLY_RESOURCE
PREPARE_SANDBOXED
EFFECT_CONFINED
PRIVILEGED_ADMIN   # deferred / non-v1
~~~

If the required enforcement level is unavailable:

~~~text
operation denied
~~~

There is no silent unconfined fallback.

## 14. Software integration hierarchy

Preferred technical integration order:

1. native structured API / SDK / database protocol;
2. application plugin / IPC;
3. structured CLI with fixed argv/schema contract;
4. GUI/computer-use automation.

This order is a **reliability preference**, not authority.

For structured CLI usage, executable identity, argv structure, working directory, minimized environment, network policy, and a versioned output parser are bounded.

A generic shell(command) must not become the normal UNITERA business-ACT interface.

GUI automation remains a last resort and initially defaults to:

~~~text
observe
prepare
assist
~~~

until dedicated effect and verification semantics exist.

## 15. Secure Node Channel

The exact transport protocol is intentionally deferred. The semantic requirements are fixed:

- mutual endpoint authentication;
- node identity binding;
- tenant binding;
- session binding;
- message integrity;
- replay protection;
- expiry;
- unique command identity;
- acknowledgement;
- revocation;
- reconnect semantics;
- bounded offline queue.

Candidate message classes:

~~~text
NodeHello
NodeChallenge
NodeSessionEstablished
NodeHeartbeat
ResourceResolveRequest
ResourceResolveResult
ExecutionDispatchRequest
ExecutionDispatchResult
NodeHealthUpdate
NodeRevocationNotice
~~~

A message does not create business authority merely because it arrived over an authenticated channel.

### Offline behavior v0.1

~~~text
offline read of already-authorized resources
→ candidate by policy

offline prepare-only work
→ candidate by policy

offline real-world effect
→ forbidden / deferred
~~~

## 16. Runtime state, evidence, and audit

Authoritative Node state remains outside model memory:

~~~text
node lifecycle
channel session
resource bindings
adapter bindings
local policy revision
pending execution bindings
idempotency state
receipts
verification state
revocation state
~~~

Conversation history may only project this state.

Minimum event families:

~~~text
node.registered
node.binding.changed
node.health.changed
node.quarantined
node.revoked

resource.registered
resource.resolved
resource.read
resource.stale

adapter.registered
adapter.binding.changed
adapter.quarantined

execution.received
execution.denied
execution.attempted
receipt.issued
verification.completed
reconciliation.required
~~~

Evidence binds at minimum tenant, node, principal/run, work order where applicable, resource/adapter identity, contract revision, policy revision, grant digest, payload/target digest, timestamps, and result digest.

Raw secrets must not be stored in evidence.

## 17. Failure model

Candidate failure classes:

~~~text
NODE_UNREACHABLE
NODE_NOT_BOUND
NODE_REVOKED
NODE_QUARANTINED
NODE_RUNTIME_DRIFT
NODE_POLICY_DRIFT

RESOURCE_NOT_REGISTERED
RESOURCE_NOT_ALLOWED
RESOURCE_STALE
RESOURCE_INTEGRITY_MISMATCH

ADAPTER_NOT_REGISTERED
ADAPTER_NOT_ELIGIBLE
ADAPTER_QUARANTINED
ADAPTER_BINDING_MISMATCH

GRANT_INVALID
GRANT_EXPIRED
GRANT_REVOKED
TARGET_MISMATCH
PAYLOAD_DIGEST_MISMATCH
CONTEXT_BINDING_MISMATCH

SANDBOX_UNAVAILABLE
CREDENTIAL_UNAVAILABLE
NETWORK_POLICY_DENIED

PRE_EFFECT_FAILURE
KNOWN_NO_EFFECT
UNKNOWN_EFFECT
VERIFICATION_INCONCLUSIVE
~~~

Failure attribution remains diagnostic evidence:

~~~text
authority
policy
node
adapter
sandbox
credential
network
external_system
verification
unknown
~~~

It does not itself create permission.

## 18. Threat model

| Threat | Mitigation direction |
|---|---|
| malicious local browser / UI | authenticated local session; localhost never treated as authority |
| prompt injection / compromised model | model cannot mint grants or receive raw credentials |
| compromised adapter | registration, digest, qualification, sandbox, network policy, quarantine |
| stolen node identity | key protection, revocation, short-lived sessions, optional hardware attestation |
| local privilege escalation | least-privileged daemon, OS-native isolation, no generic admin runtime |
| replay | expiry, nonce/message ID, idempotency, binding revision, replay cache |
| TOCTOU / stale state | exact digests, resource versions, pre-dispatch re-evaluation |

## 19. v1 boundary

The Local Runtime Node must **not expand the existing bounded v1 effect scope**.

### Allowed resource scope

~~~text
explicit selected workspace registration
read-only metadata
bounded file reads
file search
repository inspection
explicit LocalResourceHandles
~~~

### Allowed prepare scope

~~~text
deterministic transformation
draft generation
sandbox/temp artifact creation
non-authoritative analysis
local indexing
~~~

Writes are limited to Node-owned temporary storage or an explicitly registered staging area.

### No new atomic effect

For the filesystem pilot, the amendment names:

~~~text
local.fs.metadata
local.fs.read
local.fs.search
local.fs.prepare_draft
~~~

local.fs.write is **not introduced as a new v0.1 real-world-effect capability**.

Forbidden in the first scope:

~~~text
unrestricted home-directory access
generic arbitrary shell as business capability
dynamic effect-adapter discovery
automatic local-vs-cloud route selection
GUI automation for business commitments
offline effectful execution
self-installing runtime plugins
node self-registration authority
node self-assignment
credential export to model
second atomic effectful v1 capability
~~~

## 20. Planned first product flow

The internal security architecture should project to a simple experience:

~~~text
"Connect computer"
→ authenticate / confirm tenant
→ node enrollment
→ "Computer connected"
→ "Share folder"
→ read-only workspace registered
~~~

Users should not need to understand certificates, nonces, key digests, or node manifests.

## 21. Recommended first implementation slice

The source recommends starting with:

~~~text
LRN-01 + LRN-03 + LRN-04 + LRN-05
~~~

meaning:

~~~text
provider-neutral contracts
+
Local Node daemon
+
secure outbound channel
+
read-only selected workspace
~~~

Target proof:

> A tenant-bound, authenticated Local Runtime Node can expose one explicitly registered workspace to UNITERA KNOW through bounded, provenance-aware, read-only Resource Handles, while the model receives neither implicit filesystem authority nor execution authority.

This validates the core architecture **without opening ACT**.

## 22. Working plan LRN-00 through LRN-12

| Phase | Goal | Hard boundary |
|---|---|---|
| LRN-00 | source / owner-surface reconciliation | no runtime mutation |
| LRN-01 | provider-neutral Local Node contracts | no runtime authority |
| LRN-02 | TenantNodeBinding authority design | no runtime substitute for missing TCP authority |
| LRN-03 | Node daemon skeleton | no business resources |
| LRN-04 | secure outbound channel | no remote effect execution |
| LRN-05 | read-only local resource plane | no write / no process execution |
| LRN-06 | prepare-only local processing | no business effect |
| LRN-07 | adapter registry + local policy ceiling | no generic business shell |
| LRN-08 | credential broker | no raw secret exposure to model |
| LRN-09 | governed effect bridge in shadow | no real dispatch |
| LRN-10 | one exact bounded real effect route | separate production authorization |
| LRN-11 | hardening and qualification | Critical Authority Breach = 0 |
| LRN-12 | source adoption / provenance / freeze | pointer review only afterwards |

## 23. Owner-surface allocation

The candidate does not move semantic authority into the runtime repository.

~~~text
unitera-os
→ provider-neutral Local Node / Resource / Adapter / Receipt contracts

Tenant Control Plane
→ TenantNodeBinding, persistent suspension / revocation / lifecycle authority

Unitera_Systems
→ concrete Node runtime, channel, Resource Broker, Adapter Registry,
  Local Policy, Sandbox, Credential Broker, Evidence and Health

coreos
→ no Node execution authority; consumes only institutionally relevant semantics

Registry
→ reference / provenance after adoption; never creates authority
~~~

## 24. Open owner questions

Not decided by the candidate:

1. Is the Local Runtime Node a supported v1 deployment target or a post-v1 track?
2. Which Tenant Control Plane decision class authorizes TenantNodeBinding?
3. At what sensitivity level does hardware-backed node identity become mandatory?
4. Which local resource classes may a normal tenant user register without owner/admin approval?
5. May nodes retain long-lived provider credentials, or should effectful credentials be short-lived where possible?
6. What qualification level is required before a local adapter may carry the existing v1 effect?
7. Is offline ACT permanently prohibited or only deferred?

Runtime implementation must not silently answer these questions.

## 25. Explicit non-claims

This public projection does **not** claim:

- that a Local Runtime Node is already production-deployed;
- that localhost is trusted;
- that local execution is inherently safer than remote execution;
- that any transport, keystore, or sandbox technology is canonical;
- that a Node may self-register, self-assign to a tenant, or mint grants;
- that a generic shell is a UNITERA business capability;
- that a second effectful v1 capability exists;
- that source adoption, owner freeze, or source-pointer activation has occurred.

## 26. Summary

The Local Runtime Node is most precisely:

> **a local, tenant-bound enforcement, resource, adapter, credential, and evidence boundary that gives UNITERA governed access to a physical computer without confusing locality, software availability, or model capability with authority.**

In short:

~~~text
THINK proposes.
Authority decides.
The Local Node attenuates and enforces.
ACT executes exactly.
Evidence records.
Verification proves.
~~~
