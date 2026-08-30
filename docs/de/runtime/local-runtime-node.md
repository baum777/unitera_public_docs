# Local Runtime Node

**Status:** CANDIDATE — öffentliche Projektion eines SOURCE_CANDIDATE_NON_AUTHORITATIVE; weder Repository-kanonisch noch source-adoptiert, Runtime-aktiv oder produktiv autorisiert.  
**Authority:** keine aus diesem Dokument heraus.  
**Source basis:** UNITERA-LOCAL-RUNTIME-NODE-DEVICE-CAPABILITY-BOUNDARY-001@0.1.0 plus Device-Identity-&-Enrollment-Amendment v0.1.1.

[English edition](../../en/runtime/local-runtime-node.md)

## 1. Zweck und Mental Model

Der **UNITERA Local Runtime Node** ist ein vorgeschlagener, lokal laufender Runtime- und Enforcement-Dienst auf einem physischen Rechner. Er erweitert UNITERA kontrolliert auf lokale Dateien, Programme, lokale Dienste und perspektivisch weitere Geräteoberflächen.

Er ist **keine vierte semantische Ebene** neben KNOW / THINK / ACT.

Seine Aufgabe ist vielmehr:

- lokale Ressourcen für **KNOW** sicher adressierbar und begrenzt lesbar zu machen;
- lokale technische Ausführungswege für **ACT** bereitzustellen;
- Credentials lokal zu halten;
- lokale Policy als zusätzliche Begrenzung durchzusetzen;
- Ausführung, Receipt, Verification und Failure Evidence nachvollziehbar zu binden.

Die Kernidee lautet:

> Das Modell beschreibt oder schlägt eine Wirkung vor. Authority wird unabhängig geprüft. Der Local Runtime Node führt nur die exakt gebundene, lokal ebenfalls zulässige Operation aus.

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

## 2. Harte semantische Grenzen

Der Candidate übernimmt die bestehenden UNITERA-Trennungen und ergänzt lokale Varianten:

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

Damit gilt insbesondere: **Lokalität ist keine Vertrauensquelle.** Sie kann Datenbewegung reduzieren und Credentials auf dem Gerät halten, erzeugt aber weder Tenant-, Capability- noch Execution-Authority.

## 3. Position in KNOW / THINK / ACT

### KNOW — lokale Resource Plane

Für lokale Informationen ist der Node ein kontrollierter Resource Host:

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

Das Modell soll möglichst nicht mit freien Dateipfaden oder direkten Filesystem-Rechten arbeiten. Stattdessen nutzt es tenantgebundene, zweckgebundene und zeitlich begrenzte Resource Handles.

### THINK — bleibt unabhängig

Der Local Runtime Node wird nicht zur Cognition Authority. Ein Modell kann lokal oder remote laufen; daraus folgt keine neue Berechtigung.

~~~text
better model != more authority
local model != trusted authority
~~~

### ACT — lokale Effect Plane

Für reale Wirkung bleibt die zentrale Authority-Kette bestehen:

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

## 4. Deployment-Topologie

Die bevorzugte Richtung ist **outbound-first**: Der Node baut selbst eine authentifizierte Verbindung zur UNITERA-Runtime auf.

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

Die Architektur setzt damit **keinen öffentlich erreichbaren eingehenden Control-Port** als Grundannahme voraus.

Eine lokale Browser- oder Desktop-UI darf den Node verwenden, aber:

~~~text
localhost != authentication
loopback != authority
same device != permission
~~~

Auch lokal müssen Principal, Tenant, Node, Session und erlaubte Operation aufgelöst werden.

## 5. Node Identity, Enrollment und Tenant Binding

### 5.1 Lokale operative Identität

Der Candidate sieht vor, dass der Node sein asymmetrisches operatives Schlüsselpaar lokal erzeugt.

~~~text
Operational private key:
- on-device generated
- never returned by Control Plane
- never exposed to model
- non-exportable where supported
~~~

Bevorzugte Schutzreihenfolge:

~~~text
hardware-backed keystore
→ OS-protected keystore
→ encrypted local store
~~~

Candidate-Assurance-Klassen:

~~~text
SOFTWARE_PROTECTED
OS_PROTECTED
HARDWARE_BACKED
~~~

Hardware Attestation ist im v0.1-Amendment ausdrücklich **kein Muss** für den ersten begrenzten Node; sie bleibt eine mögliche zusätzliche Assurance für sensitivere Profile.

### 5.2 Enrollment Authority

Ein Gerät darf Enrollment **initiieren**, aber nicht selbst **autorisieren**:

~~~text
self-initiation = allowed
self-authorization = forbidden
~~~

Vorher muss eine tenantgebundene NodeEnrollmentAuthorization existieren.

~~~text
Enrollment Token != Enrollment Decision
~~~

### 5.3 Enrollment-Protokoll

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

### 5.4 Durable Object Separation

Die Source trennt bewusst:

~~~text
LocalNodeIdentity
!= TenantNodeBinding
!= NodeRuntimeStatus
!= NodeIdentityAssuranceRecord
!= NodeRuntimeIntegrityRecord
!= NodePolicyBinding
~~~

Ein erfolgreich installiertes oder enrolltes Gerät ist daher noch nicht automatisch für Ressourcen oder Effekte freigeschaltet.

## 6. Initiale Zero-Authority-Policy

Jeder frisch enrollte Node beginnt unter:

~~~text
ENROLLMENT_ONLY
~~~

Erlaubt:

- authentifizierter Channel;
- Heartbeat;
- Health Reporting;
- Credential Rotation;
- Re-Attestation.

Verboten:

- Resource Access;
- Resource Registration;
- Adapter Execution;
- Business-Credential Resolution;
- effectful execution;
- sonstige nicht-Control-Plane-Netzwerkzugriffe.

Daraus folgt:

~~~text
Successful Enrollment
!= Resource Permission
!= Adapter Permission
!= Capability Grant
~~~

## 7. Node Lifecycle

Candidate Lifecycle:

~~~text
untrusted
→ enrollment_authorized
→ enrollment_pending
→ provisional
→ channel_proven
→ active
~~~

Zusätzliche Betriebszustände:

~~~text
degraded
quarantined
suspended
revoked
retired
~~~

Wichtige Bedeutung:

- **active** heißt nur: Der Node ist erreichbar und darf an den für ihn zulässigen Protokollen teilnehmen.
- **degraded** kann unter Policy noch Read-/Prepare-Flächen behalten.
- **quarantined** erhält keine neuen effectful Dispatches.
- **revoked** invalidiert abhängige Eligibility dauerhaft gemäß Tenant-Control-Plane-Authority.
- Re-Registration darf widerrufene Authority nicht still wiederherstellen.

Runtime Containment und persistente Revocation bleiben getrennte Verantwortungen.

## 8. Zentrale Contract-Familie

Die Source schlägt folgende logische Objekte vor:

| Objekt | Zweck | Ist ausdrücklich nicht |
|---|---|---|
| LocalNodeRef | stabile Referenz auf Node + Tenant-Kontext | Node Authority / Grant |
| LocalNodeIdentity | operative Geräteidentität | Tenant Binding / User Identity |
| TenantNodeBinding | tenantautorisierte Bindung des Nodes | Agent Assignment / Grant |
| NodeSurfaceManifest | technisch verfügbare Resource-/Adapter-Fläche | Business Permission |
| LocalResourceDescriptor | registrierte lokale Ressource mit Klassifikation/Provenienz | Model Permission |
| LocalResourceHandle | zweckgebundener, begrenzter Zugriff für KNOW | Credential / Write Permission |
| LocalAdapterDescriptor | versionierte technische Adapterbeschreibung | Capability |
| LocalAdapterBinding | exakte Bindung Semantik ↔ lokale Implementierung | Grant |
| LocalPolicyProfile | lokale Obergrenze für Resource/Process/Network/Credential-Regeln | zentrale Authority |
| NodeExecutionBinding | exakte bindende Ausführungsparameter | Credential |
| LocalExecutionReceipt | Evidence über Ausführungsversuch/-zustand | Verification |
| LocalVerificationEvidence | nachgelagerte Zustandsprüfung | Business Outcome |

## 9. Resource Plane — KNOW

### 9.1 Registrierung

~~~text
local file/app/db exists
→ explicit user selection or governed local discovery
→ LocalResourceDescriptor candidate
→ tenant/node policy evaluation
→ registered resource
~~~

**Discovery allein erzeugt keine Model-Sichtbarkeit.**

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

Candidate Access Modes:

~~~text
metadata
search
bounded_read
transformed_read
privileged_read
~~~

### 9.3 Pfadminimierung

Bevorzugt werden Resource-ID plus opaker lokaler Locator statt automatisch vollständige lokale Pfade in Model Context zu propagieren.

### 9.4 Read-before-write / stale-state protection

Künftige Mutationen sollen an den tatsächlich inspizierten Zustand gebunden sein:

~~~text
read / inspect
→ observation digest/version
→ proposed mutation
→ pre-write version check
→ write only if still valid
~~~

Wenn sich der Zustand geändert hat:

~~~text
stale
→ reject or re-resolve
~~~

Nie:

~~~text
stale
→ blind overwrite
~~~

## 10. Effect Plane — ACT

Vor lokaler Ausführung muss der Node unmittelbar erneut prüfen:

- Tenant Match;
- aktives TenantNodeBinding;
- gültiges Tenant-Agent Assignment;
- gültiger, nicht abgelaufener und nicht widerrufener Grant;
- exakter Target Binding;
- exakter Payload Digest;
- exakter Context Binding Digest;
- exakter Adapter Binding Digest;
- aktuelle lokale Policy Revision;
- Adapter Health;
- erforderliche Sandbox-Verfügbarkeit;
- Credential Profile Availability;
- erlaubte Netzwerkroute;
- Idempotency State.

Materielle Drift nach Review oder Grant:

~~~text
→ no dispatch
→ re-evaluation required
~~~

Unbekannte Wirkung:

~~~text
unknown_effect
→ reconciliation
~~~

und ausdrücklich nicht:

~~~text
unknown_effect
→ automatic retry
~~~

## 11. Lokale effektive Erlaubnis

Die lokale Runtime darf nur weiter **einschränken**:

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

Invarianten:

~~~text
local_effective_permission <= capability_grant
local_effective_permission <= local_policy_ceiling
~~~

Daraus folgt:

~~~text
central grant + local deny = DENY
local allow + no central grant = DENY
~~~

Keine Seite kann allein die Rechte der anderen erweitern.

## 12. Credential Boundary

Raw Credentials bleiben außerhalb von Model Context, Conversation History, Action Proposal, Capability-Grant-Payload, allgemeinen Logs und Adapter-Metadaten.

Verwendung:

~~~text
CredentialProfileRef
→ local Credential Broker
→ ephemeral execution material
→ exact adapter invocation
~~~

Candidate Secret Stores werden **nicht kanonisiert**. Die Source nennt nur mögliche Implementierungen wie OS Keychain, Secret Service, hardware-backed key oder lokalen verschlüsselten Vault.

Kernregel:

~~~text
adapter may use secret
!=
model may read secret
~~~

## 13. Sandbox und lokales Enforcement

Eine produktionsreife Node-Implementierung müsste mindestens folgende Flächen begrenzen:

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

Candidate Profiles:

~~~text
READ_ONLY_RESOURCE
PREPARE_SANDBOXED
EFFECT_CONFINED
PRIVILEGED_ADMIN   # deferred / non-v1
~~~

Wenn die geforderte Enforcement-Stärke nicht verfügbar ist:

~~~text
operation denied
~~~

Es gibt keinen stillen unconfined fallback.

## 14. Software-Integrationshierarchie

Bevorzugte technische Reihenfolge:

1. native strukturierte API / SDK / Datenbankprotokoll;
2. Application Plugin / IPC;
3. strukturierte CLI mit fixem argv-/Schema-Contract;
4. GUI-/Computer-Use-Automation.

Diese Reihenfolge ist eine **Reliability Preference**, keine Authority.

Bei strukturierter CLI werden mindestens Executable Identity, argv Structure, Working Directory, minimales Environment, Network Policy und versionierter Output Parser gebunden.

Ein generisches shell(command) soll nicht zur normalen UNITERA Business-ACT-Schnittstelle werden.

GUI-Automation bleibt Last Resort und im ersten Scope primär:

~~~text
observe
prepare
assist
~~~

bis eigene Effect- und Verification-Semantik existiert.

## 15. Secure Node Channel

Das konkrete Transportprotokoll ist im Candidate bewusst offen. Festgelegt sind nur semantische Anforderungen:

- mutual endpoint authentication;
- Node Identity Binding;
- Tenant Binding;
- Session Binding;
- Message Integrity;
- Replay Protection;
- Expiry;
- Unique Command Identity;
- Acknowledgement;
- Revocation;
- Reconnect Semantics;
- bounded offline queue.

Candidate Message Classes:

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

Eine Message erzeugt keine Business Authority allein dadurch, dass sie über einen authentifizierten Channel eingetroffen ist.

### Offline-Verhalten v0.1

~~~text
offline read of already-authorized resources
→ candidate by policy

offline prepare-only work
→ candidate by policy

offline real-world effect
→ forbidden / deferred
~~~

## 16. Runtime State, Evidence und Audit

Authoritativer Node-State bleibt außerhalb des Model Memory:

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

Conversation History darf diesen Zustand nur projizieren.

Minimum Event Families:

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

Evidence bindet mindestens Tenant, Node, Principal/Run, Work Order wo relevant, Resource-/Adapter-Identität, Contract Revision, Policy Revision, Grant Digest, Payload-/Target-Digest, Timestamps und Result Digest.

Raw Secrets gehören nicht in Evidence.

## 17. Failure Model

Candidate Failure Classes:

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

Failure Attribution bleibt diagnostische Evidence:

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

Sie erzeugt selbst keine Permission.

## 18. Threat Model

| Bedrohung | Gegenrichtung |
|---|---|
| bösartige lokale Browser-/UI-Nutzung | authentifizierte lokale Session; localhost nie als Authority |
| Prompt Injection / kompromittiertes Modell | Modell kann weder Grants minten noch rohe Credentials erhalten |
| kompromittierter Adapter | Registrierung, Digest, Qualification, Sandbox, Netzwerkregeln, Quarantine |
| gestohlene Node Identity | Key Protection, Revocation, kurzlebige Sessions, optional Hardware Attestation |
| lokale Privilege Escalation | least-privileged daemon, OS-native isolation, kein generischer Admin-Runtime |
| Replay | expiry, nonce/message id, idempotency, binding revision, replay cache |
| TOCTOU / stale state | exakte Digests, Resource Versions, Pre-Dispatch Re-Evaluation |

## 19. v1-Grenze

Der Local Runtime Node darf den bestehenden begrenzten v1-Effect-Scope **nicht erweitern**.

### Erlaubter Resource Scope

~~~text
explicit selected workspace registration
read-only metadata
bounded file reads
file search
repository inspection
explicit LocalResourceHandles
~~~

### Erlaubter Prepare Scope

~~~text
deterministic transformation
draft generation
sandbox/temp artifact creation
non-authoritative analysis
local indexing
~~~

Writes nur in Node-owned temp oder eine ausdrücklich registrierte Staging Area.

### Kein neuer atomarer Effect

Das Amendment nennt für den Filesystem-Pilot:

~~~text
local.fs.metadata
local.fs.read
local.fs.search
local.fs.prepare_draft
~~~

local.fs.write wird **nicht** als neue v0.1 Real-World-Effect-Capability eingeführt.

Verboten im ersten Scope:

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

## 20. Geplanter erster Product Flow

Die innere Sicherheitsarchitektur soll sich einfach anfühlen:

~~~text
"Computer verbinden"
→ authenticate / confirm tenant
→ node enrollment
→ "Computer verbunden"
→ "Ordner freigeben"
→ read-only workspace registered
~~~

Der Nutzer muss dafür keine Zertifikate, Nonces, Key Digests oder Node Manifests verstehen.

## 21. Empfohlener erster Implementierungsslice

Die Source empfiehlt zunächst:

~~~text
LRN-01 + LRN-03 + LRN-04 + LRN-05
~~~

also:

~~~text
provider-neutral contracts
+
Local Node daemon
+
secure outbound channel
+
read-only selected workspace
~~~

Zielnachweis:

> Ein tenantgebundener, authentifizierter Local Runtime Node kann einen ausdrücklich registrierten Workspace über begrenzte, provenance-aware, read-only Resource Handles für UNITERA KNOW bereitstellen, ohne dem Modell implizite Filesystem- oder Execution-Authority zu geben.

Damit wird zunächst die Kernarchitektur validiert, **ohne ACT zu öffnen**.

## 22. Arbeitsplan LRN-00 bis LRN-12

| Phase | Ziel | Harte Grenze |
|---|---|---|
| LRN-00 | Source-/Owner-Surface-Reconciliation | keine Runtime-Mutation |
| LRN-01 | providerneutrale Local-Node-Contracts | keine Runtime Authority |
| LRN-02 | TenantNodeBinding Authority Design | kein Runtime-Ersatz für fehlende TCP-Authority |
| LRN-03 | Node-Daemon-Skeleton | keine Business Resources |
| LRN-04 | sicherer outbound Channel | keine Remote Effect Execution |
| LRN-05 | read-only Local Resource Plane | kein Write / kein Process Execution |
| LRN-06 | prepare-only lokale Verarbeitung | kein Business Effect |
| LRN-07 | Adapter Registry + Local Policy Ceiling | kein Generic Business Shell |
| LRN-08 | Credential Broker | keine Raw-Secret-Model-Exposure |
| LRN-09 | governed effect bridge im Shadow | kein realer Dispatch |
| LRN-10 | ein exakt begrenzter realer Effect-Route | separate Production-Autorisierung |
| LRN-11 | Hardening und Qualification | Critical Authority Breach = 0 |
| LRN-12 | Source Adoption / Provenance / Freeze | Pointer Review erst danach |

## 23. Owner-Surface-Aufteilung

Der Candidate verschiebt keine Authority in das Runtime-Repo.

~~~text
unitera-os
→ provider-neutrale Local-Node-/Resource-/Adapter-/Receipt-Verträge

Tenant Control Plane
→ TenantNodeBinding, persistente Suspension / Revocation / Lifecycle Authority

Unitera_Systems
→ konkrete Node Runtime, Channel, Resource Broker, Adapter Registry,
  Local Policy, Sandbox, Credential Broker, Evidence und Health

coreos
→ keine Node Execution Authority; konsumiert nur dort relevante institutionelle Semantik

Registry
→ Referenz / Provenance nach Adoption; erzeugt keine Authority
~~~

## 24. Open Owner Questions

Noch nicht durch den Candidate entschieden:

1. Ist der Local Runtime Node ein unterstütztes v1-Deployment-Target oder post-v1?
2. Welche Tenant-Control-Plane-Decision-Class autorisiert TenantNodeBinding?
3. Ab welchem Sensitivitätsprofil wird hardwaregestützte Node Identity Pflicht?
4. Welche lokalen Resource Classes darf ein normaler Tenant-Nutzer selbst registrieren?
5. Dürfen Nodes langfristige Provider Credentials halten oder sollen effectful Credentials möglichst kurzlebig sein?
6. Welche Qualification benötigt ein lokaler Adapter, bevor er den bestehenden v1-Effect transportieren darf?
7. Bleibt Offline-ACT dauerhaft verboten oder nur zunächst deferred?

Runtime-Implementierung darf diese Fragen nicht still beantworten.

## 25. Explizite Nichtaussagen

Diese öffentliche Projektion behauptet **nicht**:

- dass ein Local Runtime Node bereits produktiv existiert;
- dass localhost vertrauenswürdig ist;
- dass lokale Ausführung grundsätzlich sicherer als Remote-Ausführung ist;
- dass ein konkreter Transport, Keystore oder Sandbox-Mechanismus kanonisch festgelegt ist;
- dass ein Node sich selbst registrieren, einem Tenant zuordnen oder Grants erzeugen darf;
- dass eine generische Shell eine UNITERA Business Capability ist;
- dass eine zweite effectful v1-Capability entstanden ist;
- dass Source Adoption, Owner Freeze oder Pointer Switch erfolgt sind.

## 26. Zusammenfassung

Der Local Runtime Node ist am präzisesten:

> **eine lokale, tenantgebundene Enforcement-, Resource-, Adapter-, Credential- und Evidence-Grenze, die UNITERA kontrollierten Zugriff auf einen physischen Computer ermöglicht, ohne Locality, Software-Verfügbarkeit oder Modellfähigkeit mit Authority zu verwechseln.**

Kurz:

~~~text
THINK proposes.
Authority decides.
The Local Node attenuates and enforces.
ACT executes exactly.
Evidence records.
Verification proves.
~~~
