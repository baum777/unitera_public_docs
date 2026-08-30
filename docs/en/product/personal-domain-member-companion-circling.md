# Personal Domain, Member Companion, Personal Memory & Circling

**Status:** PUBLIC PROJECTION — CANDIDATE  
**Authority:** none by itself  
**Source basis:** source-reconciled concept candidate UNITERA-PERSONAL-DOMAIN-MEMBER-COMPANION-CIRCLING-001@0.1.0 plus the current Tenant, Company Brain, Product, Context, Authority and source-governance direction  
**Canonicalization:** not owner-bound, not source-adopted, not runtime-materialized by this document

This concept extends UNITERA with a persistent personal relationship layer around a person without turning personal memory into company truth or turning companionship into authority.

The intended direction is simple:

> **The Company Brain remembers the company. The Personal Companion remembers the person. Circling preserves what may matter before either the person or the organization commits to it.**

## Why this concept exists

UNITERA already separates organizational knowledge, current operational state, cognition, work and real-world authority. A long-term personal companion introduces another kind of continuity: what UNITERA should remember for one person across sessions, plans, ideas and potentially changing organizational memberships.

That requires a new boundary rather than one undifferentiated AI memory.

The concept separates:

- personal continuity from institutional truth;
- attention from commitment;
- an idea from a Claim;
- a personal plan from a Work Order;
- advice from a Decision;
- remembered company context from current authoritative company state;
- a trusted relationship with a Companion from institutional permission.

## Naming boundary: Personal Tenant is a working term

The original architecture idea used **Personal Tenant**. The current UNITERA vocabulary already uses Tenant for an institutional security and authority boundary, so this public projection uses **Personal Domain** as the candidate term until terminology and owner binding are resolved.

Therefore:

~~~text
Personal Tenant
= working term

Personal Domain
= preferred candidate term in this document

neither
= project-canonical by this document
~~~

This prevents a personal continuity boundary from silently redefining the existing Tenant concept.

## Architecture at a glance

~~~mermaid
flowchart TB
    P[Person] --> PD[Personal Domain]
    PD --> C[Member Companion]

    C --> I[Communication and interaction]
    C --> PL[Planner]
    C --> ST[Strategist]
    C --> AD[Advisor]
    C --> PM[Personal Memory]
    C --> CI[Circling]

    PM --> PC[Personal continuity]
    CI --> IC[Ideas and concepts]
    IC --> CP[Contribution Proposal]

    P --> M[Verified Membership]

    subgraph Company["Company Tenant"]
        D[Discovery / Learning]
        W[/work]
        OP[Operational Pulse]
        CB[Company Brain]
    end

    M --> Company
    CP -->|explicit contribution boundary| D
    D --> CB
    CB -->|purpose-bound context| C
    OP -->|current operational context| C
    W -->|work-bound context| C
~~~

The diagram deliberately shows two directions:

1. company context can be projected into the Companion when membership, purpose and policy allow it;
2. personal thought can enter company knowledge only through an explicit contribution path.

Neither direction creates authority merely by crossing the boundary.

## Core concepts

| Concept | Candidate meaning | Explicitly not |
|---|---|---|
| **Personal Domain** | User-bound continuity and isolation domain for a person's persistent UNITERA relationship | Company Tenant, Membership, authority domain |
| **Member** | A person/principal participating in a Company Tenant through Membership | Automatically an employee, owner or authority holder |
| **Member Companion** | Persistent personal interaction and cognition projection | Company Agent Assignment, Company Brain, Capability Grant |
| **Personal Memory** | Deliberately retained user-bound continuity information | Transcript archive, Runtime State, institutional truth |
| **Circling** | Incubation state for potentially meaningful but not yet committed material | Priority, Work Order, Claim, Decision |
| **Contribution Proposal** | Explicit proposal to move personal material toward an institutional lifecycle | Claim inclusion, Brain activation, authority |
| **Company Brain** | Versioned institutional knowledge and active organizational truth | Personal Memory, conversation history |
| **Operational Pulse** | Current operational company reality such as active work, blockers and recent events | Personal Memory, Company Brain revision |
| **/work** | Primary committed operating surface | General personal ideation space |
| **Authority** | Independent control over binding institutional consequence | Relationship depth, memory, model capability |

## The responsibility model

The concept is easiest to understand as six different responsibilities:

~~~text
Personal Memory
→ continuity

Circling
→ incubation

Company Brain
→ institutional truth

Operational Pulse
→ current organizational reality

/work
→ committed operating attention

Authority
→ governed institutional consequence
~~~

The boundaries are more important than the names.

## Member does not mean employee

The generic relationship is **Membership**. An employee may be a Member, but Member should remain broader than employment.

Potential membership contexts can include employees, founders, owners, contractors, advisors, operators, reviewers or other collaborators. The exact role taxonomy is not canonicalized here.

~~~text
Person
!= Platform Principal
!= Membership
!= Role
!= Authority Assignment
!= Permission
~~~

A single person may also hold Memberships in several Company Tenants. Those company contexts remain separately bounded.

## The Member Companion

The Member Companion is the long-term interaction relationship through which UNITERA can support a person.

Candidate interaction roles include:

- **Communication and interaction** — conversation, quick entry and reflective dialogue;
- **Planner** — goals, options, dependencies, deadlines, next steps and personal commitments;
- **Strategist** — scenarios, trade-offs, long-horizon thinking, hypotheses and alternative paths;
- **Advisor** — challenge assumptions, expose contradictions, recall prior reasoning and surface blind spots;
- **Continuity layer** — reconnect current work and thought to earlier personal context;
- **Idea incubator** — capture, connect and develop ideas without prematurely forcing them into Work or Company Brain.

These are cognition and product roles. They do not create authority roles.

A Companion may say:

> This pattern has appeared several times and may be worth revisiting.

It may not turn that statement into:

> This is now company policy.

without the independent institutional lifecycle that would actually create such a state.

## One interaction surface, different semantics

The Companion should not be modeled as one undifferentiated chat stream.

Candidate semantic modes include:

| Mode | Intended meaning |
|---|---|
| Quick interaction | lightweight personal conversation |
| Reflection | inspect thought, assumptions and previous reasoning |
| Planning | develop a personal plan or next-step structure |
| Strategy | compare options and longer-horizon paths |
| Advice | request challenge, critique or recommendation |
| Circling review | revisit incubating ideas and open patterns |
| Work context | reason inside a bounded Work Object |
| Contribution | intentionally move personal material toward company processes |

The same composer surface may remain visible while the underlying domain command changes.

~~~text
same surface
!= same domain command
~~~

That follows the broader UNITERA pattern already used for lifecycle-aware Composer semantics.

## Personal Memory

Personal Memory is persistent information retained specifically to improve future personal continuity.

It may eventually include candidate classes such as:

- interaction preferences;
- working patterns;
- personal goals;
- planning context;
- previous personal decisions and rationale;
- personal projects;
- reflections;
- ideas and developed concepts.

The exact retention classes and policy owner remain open.

### Memory formation

A message should not automatically become long-term memory.

~~~mermaid
flowchart LR
    I[Interaction or observation] --> MC[Memory Candidate]
    MC --> E[Memory eligibility]
    E -->|retain| M[Personal Memory Item]
    E -->|ask| U[User confirmation]
    E -->|transient| T[Session-only context]
    E -->|reject| X[Do not retain]
    U --> M
~~~

Potential eligibility dimensions include future usefulness, user intent, stability, sensitivity, provenance, contradiction, scope and explicit retention preference.

### Personal Memory is not Runtime State

Remembering that an approval was pending is not the same as the current Approval state.

~~~text
Personal Memory:
"I remember that approval was pending."

Authoritative Runtime State:
resolve the current canonical Approval state
~~~

Work state, Membership state, grants, receipts, verification, Tenant bindings and other authoritative runtime objects remain external to model memory.

### Personal Memory is not Company Brain

A person may remember:

> I think supplier ownership is unclear.

The Company Brain may currently state:

> Supplier ownership is assigned to Role X under Revision Y.

Both can coexist. One must not silently overwrite the other.

## Company-derived personal memory

A Companion may temporarily see Company Brain, Operational Pulse or Work context because the person has an eligible Membership and purpose.

That does **not** imply durable personal-memory residency.

~~~mermaid
flowchart LR
    C[Company context] --> P[Purpose-bound Companion projection]
    P --> R[Personal memory candidate]
    R --> G[Cross-boundary residency decision]
    G -->|allowed| M[Retained or transformed memory]
    G -->|transient only| T[Do not retain durably]
    G -->|deny| D[Discard memory candidate]
~~~

Candidate rule:

~~~text
Company Context Access
!= Personal Memory Residency Permission
~~~

The exact legal, privacy, retention and employer-access rules remain outside this candidate and require their proper authority/source closure.

## Circling

**Circling** is the holding and incubation state between noticing something and committing to it.

It is for material that appears potentially meaningful but is not yet ready to become a priority, project, Work Order, Claim or institutional decision.

Typical material includes:

- ideas;
- questions;
- weak signals;
- patterns;
- tensions;
- hypotheses;
- opportunities;
- concept fragments;
- possible projects;
- concerns;
- potential improvements.

The defining separation is:

~~~text
attention
!=
commitment
~~~

### Circling lifecycle

~~~mermaid
flowchart LR
    A[Captured] --> C[Circling]
    C --> D[Developing]
    D --> C
    D --> M[Mature]
    M --> L[Land]
    M --> C
    M --> X[Discard or archive]
~~~

Candidate maturity labels and lifecycle state names are not canonicalized by this page.

### Circling review

A review should answer four questions:

1. What is circling?
2. Why is it still open?
3. What changed since the last review?
4. What would make it land?

Candidate actions include keeping it circling, developing it, connecting it to another item, challenging it, landing it, discarding it or archiving it.

The Companion may recommend a disposition. Recommendation does not itself create the transition if policy or user control requires otherwise.

## Idea, concept and landing

An **Idea** is a relatively unconstrained possibility or thought.

A more developed concept is a structured explanation, design or solution candidate. The exact canonical term for this second object remains open because UNITERA terminology governance also uses Concept in a formal vocabulary sense.

The intended maturity grammar is:

~~~text
Impulse
→ Idea
→ Circling
→ Developed Idea
→ Structured Concept
→ Personal Evaluation
→ Landing Decision
~~~

Possible landing destinations include:

~~~mermaid
flowchart TB
    C[Circling Item] --> M[Personal Memory]
    C --> P[Personal Plan]
    C --> PP[Personal Project]
    C --> WP[Work Proposal]
    C --> DI[Discovery Contribution]
    C --> CR[Candidate Change Request]
    C --> BP[Brain Change Proposal / Learning Candidate]
~~~

Landing preserves provenance and does not imply destination acceptance.

~~~text
Circling Item
→ Work Proposal

does not mean

Work Order created
~~~

## The contribution boundary

Personal cognition may contribute to institutional knowledge. It may not silently promote itself into institutional truth.

~~~mermaid
flowchart LR
    P[Personal observation / idea / concept / Circling Item] --> I[Explicit contribution intent]
    I --> CP[Contribution Proposal]
    CP --> R[Lifecycle-aware domain command]
    R --> D[Discovery Input]
    R --> C[Candidate Change Request]
    R --> B[Brain Change Proposal / Learning Candidate]
    D --> L[Existing Company Brain lifecycle]
    C --> L
    B --> L
~~~

Therefore:

~~~text
Personal Memory Item
!= Company Evidence

Contribution Proposal
!= Claim

Contribution Proposal
!= Claim Eligibility

Contribution Proposal
!= Candidate Inclusion

Contribution Proposal
!= Active Brain mutation
~~~

Institutional adoption continues through the existing attributed Evidence, Claim, Candidate, revision, review and activation semantics.

## Company context flowing back to the Companion

The reverse direction is equally important.

~~~mermaid
flowchart LR
    B[Verified Tenant and Membership binding] --> K[Context compiler]
    CB[Active Company Brain revision] --> K
    OP[Operational Pulse] --> K
    W[Current Work context] --> K
    PM[Eligible Personal context] --> K
    K --> CP[Least-sufficient Companion context]
    CP --> C[Member Companion]
~~~

The Companion does not need to copy the whole Company Brain into Personal Memory. It should receive only the purpose-bound context needed for the interaction.

## Multiple memberships and tenant isolation

A Personal Domain may remain continuous while a person moves between or simultaneously participates in multiple organizations.

~~~mermaid
flowchart TB
    PD[Personal Domain] --> MA[Membership A]
    PD --> MB[Membership B]
    PD --> MC[Membership C]
    MA --> TA[Company Tenant A]
    MB --> TB[Company Tenant B]
    MC --> TC[Company Tenant C]
~~~

Hard default:

~~~text
Tenant A context
→ Tenant B context

DENY
~~~

The fact that the same person belongs to both organizations does not merge their data or authority boundaries.

## Membership exit

A revoked or ended Membership should remove the corresponding company access. It does not automatically imply deletion of all person-owned memory, preferences or Circling Items.

However, company-derived information retained in the personal domain may require a dedicated residency and retention review.

Candidate direction:

~~~text
Membership termination
→ revoke company access
→ review company-derived personal memory
→ retain / transform / expire / remove according to policy
~~~

The exact retention rule is an open policy and legal decision.

## Relationship to /work

The source-reconciled product direction remains **work-first, chat-secondary**.

The Personal Companion does not replace /work.

Instead:

- /work remains the primary surface for committed company operating attention;
- the Companion can interpret, prepare, explain, plan and advise around a Work Object;
- a work-bound Companion context can combine the current Work Object, eligible company context and eligible personal context;
- a personal plan does not automatically become Work state;
- a Companion thread does not automatically become a Work Object.

~~~text
Personal Plan != Work Order
Companion Thread != Work Object
Companion Plan != Work State
~~~

## Authority and safety invariants

A long-term relationship must never become an implicit authority shortcut.

~~~text
more memory
!= more authority

better personalization
!= more authority

long-term relationship
!= more authority

user trust
!= institutional authority

better model
!= more authority
~~~

If a Companion interaction produces a real-world effect proposal, the normal UNITERA chain still applies:

~~~mermaid
flowchart LR
    C[Companion cognition] --> P[Action Proposal]
    P --> E[Effective Autonomy and Policy]
    E --> H[Human Control when required]
    H --> G[Capability Grant]
    G --> D[Dispatch]
    D --> R[Receipt]
    R --> V[Verification]
~~~

The Companion cannot mint a grant, infer an Approval from conversational trust or reuse personal memory as business permission.

## Candidate product topology

A future product projection could expose the personal relationship as:

~~~text
Global Personal Companion
├── Quick Entry
├── Conversation
├── Planner
├── Strategy
├── Memory
└── Circling
        │
        └── explicit contribution
                ↓
Company Context
├── /work
├── Needs You
├── Work-bound Companion
├── Company Brain inspection
└── Discovery / Learning
~~~

This is a product direction, not a claim of current implementation.

## Candidate object set

The source-ready concept currently proposes the following logical objects for owner review:

- PersonalDomainRef;
- PersonalDomainBinding;
- PersonalMemoryItem;
- CirclingItem;
- PersonalPlan;
- ContributionProposal;
- CompanionContextBinding;
- CrossBoundaryResidencyDecision.

Owner review should select the smallest sufficient canonical contract set rather than automatically materializing every candidate as a separate domain object.

## Open owner decisions

Before canonical adoption, at least these questions remain open:

1. What is the canonical name: Personal Domain, Personal Tenant, Personal Space, or another term?
2. Which authority domain owns Person ↔ Personal Domain binding?
3. Is a Personal Domain provisioned for every Platform Principal or only explicit persons?
4. What classes of Personal Memory may persist by default?
5. Who owns cross-boundary memory residency policy?
6. What happens to company-derived personal memory after Membership suspension or revocation?
7. Which memory classes are inspectable, editable or forgettable by the person?
8. Is Circling a canonical domain concept or a product label over a more generic object?
9. What minimum contract distinguishes Idea, developed concept, Personal Plan and Work Proposal?
10. Can a Company Tenant ever access personal memory beyond explicitly contributed content?

A conservative architecture direction is **default deny** for arbitrary company access to personal memory, but that remains a candidate policy until its owner is bound.

## Public status

This page documents a **source-reconciled architecture and contract candidate**. It does not claim:

- that Personal Domain already exists in runtime;
- that Personal Tenant is canonical terminology;
- that every user already receives a Personal Domain;
- that Circling is already a canonical domain object;
- that company administrators may inspect Personal Memory;
- that company information may be durably copied into Personal Memory;
- that personal memory may be used for model training;
- that the Companion possesses institutional authority;
- that the Companion may bypass /work or Company Brain governance.

## Candidate doctrine

~~~text
REMEMBER the person without institutionalizing the person.

UNDERSTAND the company without personalizing company truth.

CIRCLE what may matter before forcing commitment.

LAND intentionally.

CONTRIBUTE explicitly.

PROMOTE through governed institutional lifecycles.

WORK through governed work surfaces.

ACT only through independent Authority.
~~~

In one sentence:

> **UNITERA gives a person a persistent thinking relationship without collapsing personal memory, organizational truth, committed work and institutional authority into one undifferentiated AI memory.**
