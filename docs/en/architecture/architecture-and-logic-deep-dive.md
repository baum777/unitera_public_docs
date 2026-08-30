# UNITERA Architecture & Logic — Detailed Concept

**Status:** PUBLIC PROJECTION — SOURCE-RECONCILED  
**Authority:** none by itself  
**As of:** 2026-08-30  
**Purpose:** A coherent, readable explanation of the UNITERA architecture, including stable core semantics, owner-decided directions, source candidates, and long-term infrastructure directions.

> This page is a public projection. It creates no owner authority, source status, runtime activation, or production authorization. If it conflicts with a verified artifact in the owning repository, the owning artifact wins.

## 1. UNITERA in one sentence

UNITERA is a Company Operating System with a personal AI companion layer that turns organizational evidence into reviewable institutional knowledge, compiles purpose-bound context, uses capable cognition, and creates real business effects only through independently checked authority, capabilities, grants, bound execution routes, and evidence.

In compact form:

~~~text
REMEMBER THE PERSON.
UNDERSTAND THE ORGANIZATION.
KNOW WHAT MATTERS NOW.
THINK WITH THE RIGHT COMPUTE.
ACT ONLY WITH INDEPENDENT AUTHORITY.
PROVE WHAT HAPPENED.
LEARN BY PROPOSAL, NEVER SILENT MUTATION.
~~~

The defining architectural idea is not a specific model, provider, or UI. It is the separation of meaning, state, cognition, authority, and effect.

~~~text
Understanding != Belief
Thinking != Decision
Decision != Authorization
Authorization != Execution
Execution != Verification
Verification != Business Outcome
~~~

## 2. Maturity: stable core and extensions

UNITERA currently combines layers with different maturity levels. This page connects them without silently canonicalizing candidates.

| Area | Public classification |
|---|---|
| Tenant as institutional security/authority boundary | ESTABLISHED |
| Company Brain lifecycle, Evidence/Claim separation, immutable revisions | ESTABLISHED |
| KNOW / THINK / ACT and authority separation | ESTABLISHED |
| /work primary, Chat/Assistant secondary | Owner-decided / public projection |
| Personal Domain, Member Companion, Personal Memory, Circling | CANDIDATE |
| Semantic Compilation as an explicit intermediate stage | CANDIDATE / architecture extension |
| Backend-agnostic processing and route-resolution contracts | CANDIDATE |
| Local Runtime Node | CANDIDATE |
| Open-weights artifact, training, qualification, and deployment architecture | LONG-TERM DIRECTION |
| Canonical Naming, Terms & Definitions ruling | CANDIDATE, owner binding required |

Maturity labels are part of the meaning. A candidate may be documented publicly without becoming canonical or runtime-active.

## 3. Updated system model

~~~mermaid
flowchart TB
    P[Person] --> PD[Personal Domain — Candidate]
    PD --> PC[Personal / Member Companion]
    PC --> PM[Personal Memory]
    PC --> CI[Circling / Planning / Strategy]

    PC --> CP[Contribution Proposal]

    CP --> BOUNDARY[Personal / Institutional Boundary]

    BOUNDARY --> M[Verified Membership]
    M --> T[Company Tenant]

    T --> D[Discovery]
    D --> E[Evidence / Claims / Conflicts / Open Decisions]
    E --> CB[Company Brain]
    T --> OP[Operational Pulse]
    T --> W[/work]

    CB --> K[KNOW — Context Runtime]
    OP --> K
    W --> K
    PM -. eligible personal context .-> K

    K --> TH[THINK — Cognition Runtime]
    TH --> AP[Action Proposal]

    AP --> AU[Authority Boundary]
    AU --> EA[Effective Autonomy + Policy]
    EA --> H[Human Control when required]
    H --> G[Capability Grant]

    G --> RR[Trusted Route / Binding]
    RR --> CLOUD[Cloud Route]
    RR --> LOCAL[Local Runtime Node — Candidate]

    CLOUD --> ACT[ACT — Trusted Execution]
    LOCAL --> ACT

    ACT --> X[External / Local System]
    X --> R[Receipt]
    R --> V[Verification]
    V --> BO[Business Outcome / Reconciliation]
    BO --> LE[Evidence / Learning Candidate]
~~~

The model contains two kinds of extension:

1. **upward toward the person:** continuity, memory, ideas, and companionship;
2. **downward toward infrastructure:** replaceable compute, provider, cloud, and local-runtime implementations.

Neither extension is allowed to blur institutional authority.

## 4. Two connected worlds: person and company

### 4.1 Personal world

The Personal Domain direction describes a persistent relationship between one person and UNITERA.

It may eventually contain:

- Personal Memory;
- personal preferences and working patterns;
- personal goals and plans;
- reflection;
- strategy;
- advice;
- ideas;
- Circling;
- long-term Companion continuity.

The core boundary is:

~~~text
Personal Domain != Company Tenant
Personal Memory != Company Brain
Personal Goal != Company Objective
Personal Plan != Work Order
Personal Advice != Decision
Companion Relationship != Institutional Authority
~~~

The preferred candidate term is currently **Personal Domain**. Personal Tenant remains a working term because Tenant is already strongly defined as an institutional security and authority boundary.

See [Personal Domain, Member Companion, Personal Memory & Circling](../product/personal-domain-member-companion-circling.md).

### 4.2 Institutional world

The Company Tenant remains the institutional boundary for identity, membership, organizational context, and authority.

Its surrounding system includes:

- Discovery;
- Company Brain;
- Operational Pulse;
- /work;
- Governance;
- capability, grant, and execution paths.

The personal relationship may support institutional work. It may not replace institutional semantics.

## 5. Six different kinds of information and state

A core architectural principle is to avoid calling everything memory.

| Area | Responsibility | Example |
|---|---|---|
| Conversation History | interaction evidence | “I think Sophie usually handles this.” |
| Personal Memory | personal continuity | “I prefer strategic work in the morning.” |
| Circling | incubation without commitment | “Maybe purchasing should be centralized.” |
| Company Brain | institutional, versioned truth | “Purchasing approvals belong to Role X.” |
| Operational Pulse | volatile operational reality | “Three supplier follow-ups are open.” |
| Runtime State | authoritative workflow/system state | “Approval B is missing; no grant exists.” |

Hard separations:

~~~text
Conversation History != Personal Memory
Personal Memory != Runtime State
Personal Memory != Company Brain
Company Brain != Operational Pulse
Operational Pulse != Runtime State
Context != Runtime State
~~~

A model may remember that an approval “was pending.” That does not establish the current Approval state. Runtime must resolve current canonical state from the appropriate source of truth.

## 6. From language to meaning: Evidence and Semantic Compilation

UNITERA does not treat raw language or system data as institutional truth.

The architecture-candidate direction makes a layered path explicit:

~~~text
Evidence / Language / System Data
        ↓
Deterministic Extraction
        ↓
Semantic Compilation
        ↓
Semantic Observation
        ↓
Domain Interpretation
        ↓
Claim Candidate / Clarification / Proposal / Work
~~~

Potential semantic dimensions include:

- entity and reference resolution;
- semantic frames and roles;
- temporal meaning;
- modality;
- pragmatic act;
- factuality;
- ambiguity;
- well-posedness.

This allows UNITERA to distinguish:

~~~text
“We have 20 employees.”
!=
“We plan to have 20 employees.”
!=
“We could have 20 employees.”
!=
“Someone said we have 20 employees.”
~~~

Additional candidate invariants:

~~~text
Sentence Meaning != Speaker Intent
Semantic Proposition != Institutional Claim
Pragmatic Intent != Domain Command
Reported Content != Current Fact
Planned Content != Current Fact
Forecast != Current Fact
Ambiguity != Permission to Guess
~~~

Semantic Compilation extends KNOW and THINK. It does not replace Company Brain review or authority.

## 7. Company Brain: from evidence space to active institutional truth

The Company Brain is not chat history and not a super-prompt.

The stable lifecycle is conceptually:

~~~mermaid
flowchart LR
    T[Verified Tenant Boundary] --> D[Discovery]
    D --> C[Claims + Sources + Conflicts + Open Decisions]
    C --> CA[Company Brain Candidate]
    CA --> CR[Candidate Revision]
    CR --> KB[Knowledge Binding Manifest]
    KB --> A[Exact Revision Review / Approval]
    A --> BR[Immutable Company Brain Revision]
    BR --> AM[Activation Manifest]
    AM --> TB[Tenant Brain Binding]
~~~

Important separations:

~~~text
Message != Claim
Claim != Active Institutional Truth
Candidate != Active Brain
Materialized Revision != Active Revision
Approval != Activation
Activation != Execution Authority
~~~

Runtime should not load “latest.” It should load the exact bound revision and digest.

See [Tenant, Discovery & Company Brain](../product/tenant-discovery-company-brain.md).

## 8. Company Brain and Operational Pulse

UNITERA separates relatively stable institutional truth from volatile operational reality.

~~~text
Company Brain
= institutional structure, policies, roles, knowledge, meaning

Operational Pulse
= current priorities, work, blockers, incidents, KPI snapshots, open loops
~~~

The Context Compiler may combine both without collapsing them.

A short-lived operational fact must not silently become Company Brain truth. A Company Brain revision must not replace current runtime or operational-state resolution.

## 9. KNOW: Context Runtime instead of “put everything in the prompt”

KNOW answers:

> Which information may this principal receive for this exact purpose and run, in which minimally sufficient projection?

The Context Runtime may bind:

- Tenant;
- membership and principal context;
- active Company Brain revision;
- Operational Pulse;
- Work Object;
- Resource Handles;
- freshness;
- provenance;
- epistemic state;
- privacy/minimization rules;
- context budget;
- eligible personal context.

The rule is:

~~~text
least privilege
+
least sufficient context
~~~

Not maximum context.

Resource Handles are opaque, tenant-bound references. They are not credentials and do not carry Execution Grant semantics.

~~~text
Context != Permission
Readable != Effect-authorized
Resource Handle != Credential
Resource Handle != Grant
~~~

See [KNOW / THINK / ACT](know-think-act.md).

## 10. THINK: cognition is not synonymous with an LLM

The Cognition Runtime covers analysis, planning, replanning, hypotheses, simulation, structured findings, child work, and Action Proposals.

The core formula remains:

> **Open-ended cognition, hard-bounded compute, strictly-bounded authority.**

Three axes remain separate:

~~~text
Cognitive Capability
×
Compute Envelope
×
Delegated / Effective Autonomy
~~~

Execution Authority is separate again.

Therefore:

~~~text
better model != more authority
more tokens != more authority
more child runs != more authority
fine-tuned behavior != enforcement
~~~

### Deterministic-first

Where a requirement can be solved completely and reliably through deterministic processing, UNITERA should not add a probabilistic model as an unnecessary authority or reliability dependency.

Examples:

- schema validation;
- hashing;
- parsing;
- fixed calculations;
- policy checks;
- exact state comparisons.

But:

~~~text
deterministic output != institutional truth
~~~

### Backend-agnostic cognition

THINK should not be permanently tied to a provider or model family.

Potential processing classes include:

- deterministic parser;
- deterministic computation;
- OCR / vision;
- language model;
- forecasting model;
- simulator;
- optimizer;
- other qualified domain models.

Candidate flow:

~~~text
Work Requirement
→ Backend Requirement
→ hard policy filters
→ eligible qualified backends
→ trusted host-side resolver
→ exact Backend Binding
→ Cognition Invocation
~~~

A model may propose a route. It does not create routing authority.

See [Cognition Runtime](../runtime/cognition-runtime.md).

## 11. ACT: real effect begins only behind an independent authority boundary

THINK ends in an Action Proposal, not a direct API call.

~~~mermaid
flowchart LR
    AP[Action Proposal] --> CR[Capability Request]
    CR --> EA[Effective Autonomy]
    EA --> P[Policy]
    P --> H[Human Control when required]
    H --> G[Capability Grant]
    G --> RE[Pre-dispatch re-evaluation]
    RE --> RB[Exact route + adapter binding]
    RB --> EX[Trusted Executor]
    EX --> AD[Execution Adapter]
    AD --> S[External / Local System]
    S --> R[Receipt]
    R --> V[Verification]
    V --> O[Business Outcome / Reconciliation]
~~~

Hard boundaries:

~~~text
Action Proposal != Grant
Approval != Capability Grant
Grant != Dispatch
Dispatch != Receipt
Receipt != Verification
Verification != Business Outcome
Unknown Effect != Safe Retry
~~~

A Receipt records execution evidence. Verification separately checks what actually happened. Business Outcome may be further removed again.

See [Governed external effect](../runtime/governed-effect.md).

## 12. Effective Autonomy is a runtime intersection

Delegated Autonomy is the governance ceiling. Effective Autonomy is the currently usable space.

Conceptually:

~~~text
effective autonomy
=
delegated autonomy
∩ tenant binding
∩ assignment
∩ workflow scope
∩ capability surface
∩ context validity
∩ evidence state
∩ impact / risk policy
∩ compute / budget
∩ runtime health
∩ revocation state
~~~

Invariant:

~~~text
effective autonomy <= delegated autonomy
~~~

Runtime may fail closed and reduce. Runtime or model may never increase delegation by itself.

## 13. Local Runtime Node: local reach without local self-authorization

The Local Runtime Node is a candidate extension that brings governed UNITERA access to a user's or tenant's physical machine.

It may eventually host:

- local files;
- repositories;
- Office or browser adapters;
- local databases;
- internal services;
- local credentials through a credential broker;
- local execution adapters.

It is not a fourth semantic plane.

~~~text
Local Resource Plane → KNOW
Local Effect Plane → ACT
~~~

Important boundaries:

~~~text
localhost != authentication
Local Reachability != Authority
Device Ownership != Tenant Authority
OS Permission != UNITERA Permission
Installed Software != Trusted Adapter
Local Adapter Availability != Capability Authority
Local Credential Availability != Credential Disclosure
~~~

A remote Grant may not widen local policy. Local policy may not invent a remote Grant. Either side can only attenuate.

See [Local Runtime Node — candidate](../runtime/local-runtime-node.md).

## 14. Open weights: long-term cognition infrastructure, not a new semantic center

The open-weights direction extends the backend model with explicit model artifacts, evaluation, qualification, training, and deployment.

Long-term flow:

~~~text
Base Model Artifact
→ Runtime Variant
→ optional Adapter Artifact
→ Evaluation Record
→ Qualification Decision
→ Model Eligibility Binding
→ Deployment Binding
→ Inference Evidence
~~~

Hard boundaries:

~~~text
Model != Authority
Provider != Authority
Model Qualification != Capability Grant
Model Eligibility != Permission
Training Run Success != Model Qualified
Artifact Presence != Runtime Eligibility
Local Execution != Trusted Execution
Remote Execution != Untrusted Execution
~~~

Volatile tenant knowledge should not by default be embedded into shared model weights.

Preferred direction:

~~~text
Shared Base Model
+
UNITERA Behavioral Adapter
+
Tenant-scoped Retrieval
+
Purpose-bound Context
~~~

Fine-tuning is better suited to stable behaviors such as evidence discipline, source attribution, conflict handling, structured outputs, and authority awareness.

This is a **Long-Term Architecture Direction**, not a claim about the current v1 runtime scope.

## 15. /work, Companion, and Company Brain have different product roles

The current product direction remains:

~~~text
/work
= primary company operating surface

Chat / Assistant / Companion
= secondary interaction and cognition surfaces

Company Brain
= context-first inspectable infrastructure
~~~

Therefore:

### Companion
helps remember, reflect, plan, challenge, explain, and think strategically.

### /work
shows committed operating attention: what is being worked, what is blocked, what needs human input, and what completed.

### Company Brain
provides the institutional meaning and knowledge foundation.

~~~text
Companion Thread != Work Object
Personal Plan != Work Order
Company Brain != Daily Task List
Chat Suggestion != Decision Authority
~~~

## 16. The Contribution Boundary: personal thought does not become Company Truth automatically

Personal ideas, memory, or Circling may support institutional processes, but they do not directly mutate Company Brain.

~~~mermaid
flowchart LR
    P[Personal Idea / Memory / Circling] --> I[Explicit Contribution Intent]
    I --> CP[Contribution Proposal]
    CP --> R[Lifecycle-aware Domain Command]
    R --> D[Discovery Input]
    R --> C[Candidate Change Request]
    R --> B[Brain Change Proposal / Learning Candidate]
    D --> L[Company Brain Lifecycle]
    C --> L
    B --> L
~~~

Hard rules:

~~~text
Personal Memory Item != Company Evidence
Contribution Proposal != Claim
Contribution Proposal != Claim Inclusion
Contribution Proposal != Brain Activation
Personal Context Access != Company Authority
~~~

The reverse direction is controlled as well:

~~~text
Company Context Access
!=
Personal Memory Residency Permission
~~~

A person may be allowed to see company context for a current purpose without that context automatically becoming durable Personal Memory.

## 17. Naming governance: words must not create meaning

The Canonical Naming, Terms & Definitions direction turns terminology into a governance concern.

Core rule:

> **A name may represent meaning. It may never create meaning by itself.**

Therefore:

~~~text
Concept Identity
!= Canonical Term
!= Machine Identifier
!= Serialized Name
!= Code Symbol
!= UI Label
!= Working ID
!= Technical Reference
~~~

This prevents dangerous semantic shortcuts.

Examples:

~~~text
Approval != Grant
Workflow ID != Capability ID
Adapter ID != Capability ID
Technical Reference != Product Identity
Repository Name != Semantic Domain
Working ID != Canonical ID
~~~

That is why Personal Tenant does not automatically become canonical terminology, and supplier_opening_followup does not become an atomic capability merely because a product surface uses that name.

## 18. Repository and authority topology

The current public responsibility direction is:

| Surface | Responsibility |
|---|---|
| **coreos** | Foundation, Company Brain, Discovery, Claim, Candidate, Revision, and institutional semantics |
| **unitera-os** | provider-neutral Capability, Policy, Grant, Execution, Context/backend primitives |
| **Unitera_Systems** | runtime, DB, API, product UI, Context Compiler, cognition, provider integration, enforcement |
| **unitera_control_plane** | Tenant, Membership, Governance, and assignment authority surfaces |
| **unitera-registry** | reference, provenance, supersession, and reachability — no authority |
| **unitera_public_docs** | public explanation — no authority |

Hard rules:

~~~text
Runtime Materialization != Semantic Authority
Registry != Authority
Public Documentation != Authority
Repository Name != Concept Identity
~~~

See [Repository & authority topology](repository-topology.md) and [Authority & Source-of-Truth model](authority-and-source-model.md).

## 19. Evidence, verification, and learning

UNITERA should not end at “the agent says it is done.”

The observable chain is:

~~~text
Proposal
→ Authority Evaluation
→ Grant
→ Dispatch
→ Receipt
→ Verification
→ Business Outcome / Reconciliation
→ Evidence
~~~

Learning follows its own boundary:

~~~text
Runtime Evidence
→ Observation / Failure / New Information
→ Learning Candidate
→ Review / Domain Lifecycle
→ Versioned Change
~~~

Not:

~~~text
Runtime Event
→ silent Company Brain mutation
~~~

For personal continuity:

~~~text
Interaction
→ Memory Candidate
→ Eligibility / User Control / Policy
→ Personal Memory
~~~

Not every message becomes long-term memory.

## 20. End-to-end example: supplier follow-up

A single example shows how the layers work together.

### Step 1 — personal observation

A person tells the Companion:

> “We are losing track of three suppliers during the opening.”

This is initially conversation/personal cognition, not Company Truth.

### Step 2 — contribution into company context

The person explicitly chooses to bring the topic into company context.

~~~text
Personal Observation
→ explicit Contribution
→ Discovery / Work Domain
~~~

### Step 3 — institutional context

UNITERA resolves:

- Tenant;
- Membership;
- active Brain revision;
- relevant supplier Claims;
- open Decisions/Conflicts;
- current Work;
- Operational Pulse.

### Step 4 — KNOW

The Context Compiler produces least-sufficient context for exactly this supplier follow-up.

### Step 5 — THINK

A qualified cognition backend analyzes:

- which information is missing;
- which suppliers are actually open;
- what a sensible next step is;
- whether an Action Proposal is justified.

The model may produce a draft and proposal.

### Step 6 — Authority

Before binding external communication, UNITERA independently checks:

- Tenant Binding;
- workflow;
- Capability;
- target;
- payload;
- materiality/risk;
- human control;
- Grant;
- route binding.

### Step 7 — ACT

The Trusted Executor dispatches exactly the bound effect through a qualified adapter — cloud or, in the future, a Local Node.

### Step 8 — proof

~~~text
Dispatch
→ Receipt
→ Delivery / State Verification
→ Supplier Response
→ Business Outcome
~~~

No response is not automatically success and not automatically a safe retry.

### Step 9 — learning

New information may become:

- Operational Pulse update;
- Work update;
- Learning Candidate;
- Brain Change Proposal;
- Personal Memory Candidate;

depending on its meaning and boundary.

One use case therefore expresses the central UNITERA idea:

> Cognition may remain flexible; institutional meaning and effect remain explicitly bound.

## 21. Global non-equivalences

The following grammar describes UNITERA better than any single product diagram:

~~~text
Evidence != Truth
Interpretation != Authority
Message != Claim
Claim != Active Institutional Truth

Conversation History != Personal Memory
Personal Memory != Company Brain
Personal Memory != Runtime State
Company Brain != Operational Pulse

Discovery != Activation
Candidate != Active Brain
Materialized Revision != Active Revision

Context != Permission
Readable != Effect-authorized

Cognition Backend != Capability
Model Output != Authority
Better Model != More Authority
Compute Envelope != Autonomy

Workflow != Capability
External Tool != UNITERA Capability
Adapter != Capability
Capability Availability != Permission

Approval != Capability Grant
Grant != Dispatch
Dispatch != Receipt
Receipt != Verification
Verification != Business Outcome

Local != Trusted
Remote != Untrusted
Runtime Implementation != Semantic Authority
Registry != Authority
Public Docs != Authority
~~~

## 22. What this page explicitly does not claim

This public projection does not claim:

- that Personal Domain or Circling are already runtime-canonical;
- that Semantic Compilation has already been adopted as a complete owner contract;
- that dynamic backend routing is active in v1;
- that the Local Runtime Node is production-active;
- that open-weights training/deployment already runs in the production path;
- that Naming Governance is already project-canonical and owner-bound;
- that a public-docs page can create source authority;
- that UNITERA automatically guarantees regulatory compliance;
- that a better model, more memory, or stronger personalization increases institutional authority.

## 23. Updated UNITERA doctrine

~~~text
REMEMBER the person
without institutionalizing personal memory.

UNDERSTAND the company
without turning every statement into truth.

KNOW precisely
through purpose-bound, provenance-aware context.

THINK freely
within hard compute and scope bounds.

PROPOSE
without self-authorizing.

ACT
only through independent policy, human control and grants.

BIND
the exact target, payload, context and route.

PROVE
what happened through receipts and verification.

RECONCILE
when effects are ambiguous.

LEARN
through proposals and versioned lifecycles,
never through silent mutation.
~~~

In one sentence:

> **UNITERA combines personal continuity, institutional knowledge, capable cognition, and real-world execution without collapsing those four things into one uncontrolled AI memory or all-powerful agent.**

## Related pages

- [System overview](system-overview.md)
- [KNOW / THINK / ACT](know-think-act.md)
- [Authority & Source-of-Truth model](authority-and-source-model.md)
- [Tenant, Discovery & Company Brain](../product/tenant-discovery-company-brain.md)
- [Personal Domain, Member Companion, Personal Memory & Circling](../product/personal-domain-member-companion-circling.md)
- [Cognition Runtime](../runtime/cognition-runtime.md)
- [Governed external effect](../runtime/governed-effect.md)
- [Local Runtime Node — candidate](../runtime/local-runtime-node.md)
- [Source basis](../reference/source-basis.md)
