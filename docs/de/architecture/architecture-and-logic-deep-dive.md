# UNITERA Architektur & Logik — Detailed Concept

**Status:** PUBLIC PROJECTION — SOURCE-RECONCILED  
**Autorität:** keine aus sich selbst heraus  
**Stand:** 30.08.2026  
**Zweck:** Verständliche, zusammenhängende Erklärung der UNITERA-Gesamtarchitektur einschließlich stabiler Kernsemantik, Owner-decided Richtungen, Source Candidates und langfristiger Infrastruktur-Richtungen.

> Diese Seite ist eine öffentliche Projektion. Sie erzeugt keine Owner-Authority, keinen Source-Status, keine Runtime-Aktivierung und keine Produktionsfreigabe. Bei Abweichungen gewinnt das verifizierte Artefakt im zuständigen Owner-Repository.

## 1. UNITERA in einem Satz

UNITERA ist ein Company Operating System mit einer persönlichen KI-Begleitschicht, das organisatorische Evidenz in überprüfbares institutionelles Wissen überführt, zweckgebundenen Kontext kompiliert, leistungsfähige Cognition nutzt und reale Geschäftswirkung nur über unabhängig geprüfte Authority, Capabilities, Grants, gebundene Ausführungsrouten und Evidence erzeugt.

Kurz:

~~~text
REMEMBER THE PERSON.
UNDERSTAND THE ORGANIZATION.
KNOW WHAT MATTERS NOW.
THINK WITH THE RIGHT COMPUTE.
ACT ONLY WITH INDEPENDENT AUTHORITY.
PROVE WHAT HAPPENED.
LEARN BY PROPOSAL, NEVER SILENT MUTATION.
~~~

Die wichtigste UNITERA-Regel ist nicht ein bestimmtes Modell, ein bestimmter Provider oder ein bestimmtes UI-Muster. Es ist die Trennung von Bedeutung, Zustand, Cognition, Authority und Wirkung.

~~~text
Verstehen != Glauben
Denken != Entscheiden
Entscheiden != Berechtigen
Berechtigen != Ausführen
Ausführen != Verifikation
Verifikation != Business Outcome
~~~

## 2. Reifegrad: stabiler Kern und Erweiterungen

UNITERA besteht aktuell aus Schichten mit unterschiedlichem Reifegrad. Diese Seite führt sie zusammen, ohne Kandidaten still zu kanonisieren.

| Bereich | Öffentliche Einordnung |
|---|---|
| Tenant als institutionelle Security-/Authority-Boundary | ESTABLISHED |
| Company-Brain-Lifecycle, Evidenz-/Claim-Trennung, immutable Revisions | ESTABLISHED |
| KNOW / THINK / ACT und Authority Separation | ESTABLISHED |
| /work primär, Chat/Assistant sekundär | Owner-decided / public projection |
| Personal Domain, Member Companion, Personal Memory, Circling | CANDIDATE |
| Semantic Compilation als explizite Zwischenstufe | CANDIDATE / architecture extension |
| Backend-agnostische Processing- und Route-Resolution-Contracts | CANDIDATE |
| Local Runtime Node | CANDIDATE |
| Open-Weights Artifact-, Training-, Qualification- und Deployment-Architektur | LONG-TERM DIRECTION |
| Canonical Naming, Terms & Definitions Ruling | CANDIDATE, owner binding required |

Die Reifegrade sind Teil der Semantik. Ein Candidate darf in der Public Documentation erklärt werden, aber dadurch nicht als bereits canonical oder runtime-active erscheinen.

## 3. Das aktualisierte Gesamtmodell

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

Dieses Bild enthält zwei verschiedene Arten von Erweiterung:

1. **nach oben zum Menschen:** persönliche Kontinuität, Erinnerung, Ideen und Begleitung;
2. **nach unten zur Infrastruktur:** austauschbare Compute-, Provider-, Cloud- und Local-Runtime-Implementierungen.

Beides darf die institutionelle Authority-Grenze nicht verwischen.

## 4. Zwei verbundene Welten: Person und Unternehmen

### 4.1 Persönliche Welt

Die neue Personal-Domain-Richtung beschreibt eine dauerhafte persönliche Beziehung zwischen einer Person und UNITERA.

Sie kann umfassen:

- Personal Memory;
- persönliche Präferenzen und Working Patterns;
- persönliche Ziele und Pläne;
- Reflexion;
- Strategie;
- Advice;
- Ideen;
- Circling;
- langfristige Companion-Kontinuität.

Die zentrale Grenze lautet:

~~~text
Personal Domain != Company Tenant
Personal Memory != Company Brain
Personal Goal != Company Objective
Personal Plan != Work Order
Personal Advice != Decision
Companion Relationship != Institutional Authority
~~~

Der bevorzugte Candidate-Term ist derzeit **Personal Domain**. Personal Tenant bleibt Working Term, weil Tenant in UNITERA bereits stark als institutionelle Security- und Authority-Boundary belegt ist.

Mehr dazu: [Personal Domain, Member Companion, Personal Memory und Circling](../product/personal-domain-member-companion-circling.md).

### 4.2 Institutionelle Welt

Der Company Tenant bleibt die institutionelle Boundary für Identität, Membership, Organisation und Authority-Kontext.

Innerhalb dieses Rahmens liegen unter anderem:

- Discovery;
- Company Brain;
- Operational Pulse;
- /work;
- Governance;
- Capability-/Grant-/Execution-Pfade.

Die persönliche Beziehung darf institutionelle Semantik unterstützen, aber nicht ersetzen.

## 5. Sechs verschiedene Arten von Information und Zustand

Ein zentrales Architekturprinzip ist, nicht alles als Memory zu behandeln.

| Bereich | Aufgabe | Beispiel |
|---|---|---|
| Conversation History | Interaktions-Evidence | „Ich glaube, Sophie macht das normalerweise.“ |
| Personal Memory | persönliche Kontinuität | „Ich arbeite morgens lieber strategisch.“ |
| Circling | Inkubation ohne Commitment | „Vielleicht sollten wir Einkauf zentralisieren.“ |
| Company Brain | institutionelle, versionierte Wahrheit | „Einkaufsfreigaben liegen bei Rolle X.“ |
| Operational Pulse | volatile operative Realität | „Drei Lieferantenanfragen sind offen.“ |
| Runtime State | autoritativer Workflow-/Systemzustand | „Approval B fehlt; kein Grant vorhanden.“ |

Harte Trennungen:

~~~text
Conversation History != Personal Memory
Personal Memory != Runtime State
Personal Memory != Company Brain
Company Brain != Operational Pulse
Operational Pulse != Runtime State
Context != Runtime State
~~~

Ein Modell darf sich beispielsweise erinnern, dass eine Approval „noch offen war“. Das ist keine Autorität für den aktuellen Approval State. Die Runtime muss den echten State aus der zuständigen Source of Truth auflösen.

## 6. Von Sprache zu Bedeutung: Evidence und Semantic Compilation

UNITERA behandelt rohe Sprache oder Systemdaten nicht direkt als institutionelle Wahrheit.

Die architecture-candidate Richtung macht einen mehrstufigen Pfad explizit:

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

Mögliche semantische Dimensionen sind:

- Entity und Reference Resolution;
- Semantic Frames und Rollen;
- Zeitbezug;
- Modalität;
- Pragmatic Act;
- Factuality;
- Ambiguität;
- Well-posedness.

Damit können Aussagen wie diese auseinandergehalten werden:

~~~text
„Wir haben 20 Mitarbeiter.“
!=
„Wir planen 20 Mitarbeiter.“
!=
„Wir könnten 20 Mitarbeiter haben.“
!=
„Jemand sagte, wir hätten 20 Mitarbeiter.“
~~~

Zusätzliche Kandidaten-Invarianten:

~~~text
Sentence Meaning != Speaker Intent
Semantic Proposition != Institutional Claim
Pragmatic Intent != Domain Command
Reported Content != Current Fact
Planned Content != Current Fact
Forecast != Current Fact
Ambiguity != Permission to Guess
~~~

Semantic Compilation erweitert KNOW und THINK; sie ersetzt Company-Brain-Review oder Authority nicht.

## 7. Company Brain: vom Evidence-Raum zur aktiven institutionellen Wahrheit

Der Company Brain ist kein Chat-Verlauf und kein Super-Prompt.

Der stabile Lifecycle ist konzeptionell:

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

Wichtig:

~~~text
Message != Claim
Claim != Active Institutional Truth
Candidate != Active Brain
Materialized Revision != Active Revision
Approval != Activation
Activation != Execution Authority
~~~

Die Runtime soll nicht „latest“ laden, sondern die exakt gebundene Revision und ihren Digest.

Mehr dazu: [Tenant, Discovery und Company Brain](../product/tenant-discovery-company-brain.md).

## 8. Company Brain und Operational Pulse

UNITERA trennt relativ stabile institutionelle Wahrheit von volatiler operativer Realität.

~~~text
Company Brain
= institutionelle Struktur, Policies, Rollen, Wissen, Bedeutung

Operational Pulse
= aktuelle Prioritäten, Work, Blocker, Incidents, KPI-Snapshots, offene Loops
~~~

Der Context Compiler kann beide kombinieren, ohne sie gleichzusetzen.

Ein kurzfristiger operativer Zustand darf nicht still Company-Brain-Wahrheit werden. Umgekehrt darf die Company-Brain-Revision nicht als Ersatz für aktuelle Runtime- oder Operational-State-Auflösung dienen.

## 9. KNOW: Context Runtime statt „alles in den Prompt“

KNOW beantwortet die Frage:

> Welche Information darf dieser Principal für genau diesen Zweck und diesen Run in welcher minimal ausreichenden Projektion erhalten?

Die Context Runtime kann unter anderem binden:

- Tenant;
- Membership und Principal-Kontext;
- aktive Company-Brain-Revision;
- Operational Pulse;
- Work Object;
- Resource Handles;
- Freshness;
- Provenance;
- Epistemic State;
- Privacy-/Minimization-Regeln;
- Context Budget;
- eligible Personal Context.

Die Leitregel ist:

~~~text
least privilege
+
least sufficient context
~~~

Nicht: möglichst viel Kontext.

Resource Handles sind opake, Tenant-gebundene Referenzen. Sie sind keine Credentials und keine Execution Grants.

~~~text
Context != Permission
Readable != Effect-authorized
Resource Handle != Credential
Resource Handle != Grant
~~~

Mehr dazu: [KNOW / THINK / ACT](know-think-act.md).

## 10. THINK: Cognition ist nicht gleich LLM

Die Cognition Runtime umfasst Analyse, Planung, Neuplanung, Hypothesen, Simulation, strukturierte Findings, Child Work und Action Proposals.

Die zentrale Formel bleibt:

> **Open-ended cognition, hard-bounded compute, strictly-bounded authority.**

Drei Achsen bleiben getrennt:

~~~text
Cognitive Capability
×
Compute Envelope
×
Delegated / Effective Autonomy
~~~

Und Execution Authority bleibt zusätzlich separat.

Daher:

~~~text
better model != more authority
more tokens != more authority
more child runs != more authority
fine-tuned behavior != enforcement
~~~

### Deterministic-first

Wenn eine Aufgabe vollständig und zuverlässig deterministisch gelöst werden kann, soll kein probabilistisches Modell als unnötige Authority- oder Reliability-Abhängigkeit eingeführt werden.

Beispiele:

- Schema Validation;
- Hashing;
- Parsing;
- feste Berechnungen;
- Policy Checks;
- exakte State-Vergleiche.

Aber auch:

~~~text
deterministic output != institutional truth
~~~

### Backend-agnostische Cognition

THINK soll langfristig nicht an einen Provider oder eine Modellfamilie gekoppelt sein.

Mögliche Processing-Klassen:

- deterministic parser;
- deterministic computation;
- OCR / Vision;
- language model;
- forecasting model;
- simulator;
- optimizer;
- andere qualifizierte Domain Models.

Candidate-Flow:

~~~text
Work Requirement
→ Backend Requirement
→ hard policy filters
→ eligible qualified backends
→ trusted host-side resolver
→ exact Backend Binding
→ Cognition Invocation
~~~

Ein Modell kann eine Route vorschlagen. Es erzeugt keine Routing Authority.

Mehr dazu: [Cognition Runtime](../runtime/cognition-runtime.md).

## 11. ACT: reale Wirkung beginnt erst hinter einer unabhängigen Authority-Grenze

THINK endet in einem Action Proposal. Es endet nicht in einem direkten API Call.

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

Harte Grenzen:

~~~text
Action Proposal != Grant
Approval != Capability Grant
Grant != Dispatch
Dispatch != Receipt
Receipt != Verification
Verification != Business Outcome
Unknown Effect != Safe Retry
~~~

Ein Receipt belegt Ausführungs-Evidence. Verification prüft danach, was tatsächlich beobachtbar passiert ist. Ein Business Outcome kann wiederum weiter entfernt liegen.

Mehr dazu: [Kontrollierte externe Wirkung](../runtime/governed-effect.md).

## 12. Effective Autonomy ist eine Laufzeit-Schnittmenge

Delegated Autonomy ist das Governance Ceiling. Effective Autonomy ist der aktuell tatsächlich nutzbare Raum.

Konzeptionell:

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

Invariante:

~~~text
effective autonomy <= delegated autonomy
~~~

Runtime darf fail-closed reduzieren. Runtime oder Modell dürfen Delegation niemals selbst erhöhen.

## 13. Local Runtime Node: lokale Reichweite ohne lokale Selbstermächtigung

Der Local Runtime Node ist ein Candidate, der UNITERA kontrolliert auf den physischen Rechner eines Nutzers oder Tenants erweitert.

Er kann perspektivisch hosten:

- lokale Dateien;
- Repositories;
- Office- oder Browser-Adapter;
- lokale Datenbanken;
- interne Services;
- lokale Credentials über einen Credential Broker;
- lokale Execution Adapter.

Er ist keine vierte semantische Ebene.

~~~text
Local Resource Plane → KNOW
Local Effect Plane → ACT
~~~

Wichtige Grenzen:

~~~text
localhost != authentication
Local Reachability != Authority
Device Ownership != Tenant Authority
OS Permission != UNITERA Permission
Installed Software != Trusted Adapter
Local Adapter Availability != Capability Authority
Local Credential Availability != Credential Disclosure
~~~

Ein Remote Grant darf lokale Policy nicht ausweiten. Lokale Policy darf umgekehrt keinen Remote Grant erfinden. Beide Seiten können nur einschränken.

Mehr dazu: [Local Runtime Node — Kandidat](../runtime/local-runtime-node.md).

## 14. Open Weights: langfristige Cognition-Infrastruktur, kein neues semantisches Zentrum

Die Open-Weights-Richtung erweitert den Backend-Ansatz um eigene Modellartefakte, Evaluation, Qualification, Training und Deployment.

Langfristiger Flow:

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

Harte Grenzen:

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

Tenant-Wissen soll standardmäßig nicht als volatile Unternehmenswahrheit in gemeinsame Modellgewichte eingebrannt werden.

Bevorzugte Richtung:

~~~text
Shared Base Model
+
UNITERA Behavioral Adapter
+
Tenant-scoped Retrieval
+
Purpose-bound Context
~~~

Fine-Tuning eignet sich eher für stabile Verhaltensmuster wie Evidence Discipline, Source Attribution, Conflict Handling, Structured Outputs oder Authority Awareness.

Diese Schicht ist eine **Long-Term Architecture Direction**, keine Behauptung über den aktuellen v1 Runtime Scope.

## 15. /work, Companion und Company Brain haben unterschiedliche Produktrollen

Die aktuelle Product-Richtung bleibt:

~~~text
/work
= primäre Company Operating Surface

Chat / Assistant / Companion
= sekundäre Interaction- und Cognition-Surfaces

Company Brain
= context-first inspectable infrastructure
~~~

Daraus ergibt sich:

### Companion
hilft erinnern, reflektieren, planen, challengen, erklären und strategisch denken.

### /work
zeigt committed operative Aufmerksamkeit: was bearbeitet wird, was blockiert ist, was Human Input braucht und was abgeschlossen wurde.

### Company Brain
liefert das institutionelle Bedeutungs- und Wissensfundament.

~~~text
Companion Thread != Work Object
Personal Plan != Work Order
Company Brain != Daily Task List
Chat Suggestion != Decision Authority
~~~

## 16. Die Contribution Boundary: persönliches Denken wird nicht automatisch Company Truth

Persönliche Ideen, Memory oder Circling dürfen institutionelle Prozesse unterstützen, aber nicht direkt Company Brain mutieren.

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

Harte Regeln:

~~~text
Personal Memory Item != Company Evidence
Contribution Proposal != Claim
Contribution Proposal != Claim Inclusion
Contribution Proposal != Brain Activation
Personal Context Access != Company Authority
~~~

Auch die Gegenrichtung ist kontrolliert:

~~~text
Company Context Access
!=
Personal Memory Residency Permission
~~~

Eine Person darf Company Context für einen aktuellen Zweck sehen, ohne dass dieser Context automatisch dauerhaft in Personal Memory kopiert wird.

## 17. Naming Governance: Wörter dürfen Bedeutung nicht erzeugen

Die Canonical Naming, Terms & Definitions Direction macht Terminologie selbst zu einer Governance-Frage.

Kernregel:

> **Ein Name darf Bedeutung repräsentieren. Er darf Bedeutung niemals selbst erzeugen.**

Daher:

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

Das verhindert gefährliche semantische Kurzschlüsse.

Beispiele:

~~~text
Approval != Grant
Workflow ID != Capability ID
Adapter ID != Capability ID
Technical Reference != Product Identity
Repository Name != Semantic Domain
Working ID != Canonical ID
~~~

Genau deshalb wird Personal Tenant derzeit nicht einfach zum neuen canonical Begriff, und supplier_opening_followup wird nicht automatisch zu einer atomaren Capability nur weil es im Produkt so genannt wird.

## 18. Repository- und Authority-Topologie

Die aktuelle Verantwortungsrichtung lässt sich öffentlich so zusammenfassen:

| Surface | Verantwortung |
|---|---|
| **coreos** | Foundation, Company Brain, Discovery-, Claim-, Candidate-, Revision- und institutionelle Semantik |
| **unitera-os** | provider-neutrale Capability-, Policy-, Grant-, Execution-, Context-/Backend-Primitives |
| **Unitera_Systems** | Runtime, DB, API, Product UI, Context Compiler, Cognition, Provider Integration, Enforcement |
| **unitera_control_plane** | Tenant-, Membership-, Governance- und Assignment-Authority-Surfaces |
| **unitera-registry** | Referenz, Provenance, Supersession und Reachability — keine Authority |
| **unitera_public_docs** | öffentliche Erklärung — keine Authority |

Harte Regeln:

~~~text
Runtime Materialization != Semantic Authority
Registry != Authority
Public Documentation != Authority
Repository Name != Concept Identity
~~~

Mehr dazu: [Repository- und Autoritätstopologie](repository-topology.md) und [Autoritäts- und Source-of-Truth-Modell](authority-and-source-model.md).

## 19. Evidence, Verification und Lernen

UNITERA soll nicht mit „Agent sagt fertig“ enden.

Der beobachtbare Pfad ist:

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

Lernen folgt einer eigenen Grenze:

~~~text
Runtime Evidence
→ Observation / Failure / New Information
→ Learning Candidate
→ Review / Domain Lifecycle
→ Versioned Change
~~~

Nicht:

~~~text
Runtime Event
→ silent Company Brain mutation
~~~

Und für persönliche Kontinuität:

~~~text
Interaction
→ Memory Candidate
→ Eligibility / User Control / Policy
→ Personal Memory
~~~

Nicht jede Nachricht wird automatisch Langzeitgedächtnis.

## 20. Durchgängiges Beispiel: Supplier Follow-up

Ein Beispiel zeigt, wie die Schichten zusammenarbeiten können.

### Schritt 1 — persönliche Beobachtung

Eine Person bespricht mit dem Companion:

> „Wir verlieren bei der Eröffnung gerade den Überblick über drei Lieferanten.“

Das ist zunächst Conversation / Personal Cognition, keine Company Truth.

### Schritt 2 — Beitrag zum Unternehmenskontext

Die Person entscheidet, das Thema in den Company-Kontext zu tragen.

~~~text
Personal Observation
→ explicit Contribution
→ Discovery / Work Domain
~~~

### Schritt 3 — institutioneller Kontext

UNITERA löst:

- Tenant;
- Membership;
- aktive Brain Revision;
- relevante Supplier-Claims;
- offene Decisions/Conflicts;
- aktuelles Work;
- Operational Pulse.

### Schritt 4 — KNOW

Der Context Compiler erzeugt einen least-sufficient Context für genau den Supplier-Follow-up.

### Schritt 5 — THINK

Ein qualifiziertes Cognition Backend analysiert:

- welche Informationen fehlen;
- welche Supplier tatsächlich offen sind;
- was ein sinnvoller nächster Schritt wäre;
- ob ein Action Proposal gerechtfertigt ist.

Das Modell darf einen Entwurf und Proposal erzeugen.

### Schritt 6 — Authority

Vor einer verbindlichen externen Kommunikation werden unabhängig geprüft:

- Tenant Binding;
- Workflow;
- Capability;
- Target;
- Payload;
- Materiality/Risk;
- Human Control;
- Grant;
- Route Binding.

### Schritt 7 — ACT

Der Trusted Executor dispatcht exakt den gebundenen Effect über einen qualifizierten Adapter — Cloud oder zukünftig Local Node.

### Schritt 8 — Nachweis

~~~text
Dispatch
→ Receipt
→ Delivery / State Verification
→ Supplier Response
→ Business Outcome
~~~

Eine ausbleibende Antwort ist weder automatisch Erfolg noch sicherer Retry.

### Schritt 9 — Lernen

Neue Information kann zu:

- Operational Pulse Update;
- Work Update;
- Learning Candidate;
- Brain Change Proposal;
- Personal Memory Candidate;

führen — je nach Bedeutung und Boundary.

Damit zeigt ein einziger Use Case die zentrale UNITERA-Idee:

> Cognition darf flexibel sein; institutionelle Bedeutung und Wirkung bleiben explizit gebunden.

## 21. Globale Nicht-Gleichheiten

Die folgende Grammatik beschreibt das System besser als ein einzelnes Produktdiagramm:

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

## 22. Was diese Seite ausdrücklich nicht behauptet

Diese Public Projection behauptet nicht:

- dass Personal Domain oder Circling bereits runtime-canonical sind;
- dass Semantic Compilation bereits als vollständiger Owner Contract adoptiert ist;
- dass dynamisches Backend Routing im v1 aktiv ist;
- dass Local Runtime Node produktiv aktiviert ist;
- dass Open-Weights Training/Deployment bereits im Production Path läuft;
- dass Naming Governance bereits project-canonical owner-bound ist;
- dass ein Public-Docs-Dokument Source Authority erzeugen kann;
- dass UNITERA regulatorische Compliance automatisch garantiert;
- dass ein besseres Modell, mehr Memory oder stärkere Personalisierung institutionelle Authority erhöht.

## 23. Die aktualisierte UNITERA-Doktrin

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

In einem Satz:

> **UNITERA verbindet persönliche Kontinuität, institutionelles Wissen, leistungsfähige Cognition und reale Ausführung, ohne diese vier Dinge in ein einziges unkontrolliertes KI-Gedächtnis oder einen allmächtigen Agenten zu kollabieren.**

## Verwandte Seiten

- [Systemübersicht](system-overview.md)
- [KNOW / THINK / ACT](know-think-act.md)
- [Autoritäts- und Source-of-Truth-Modell](authority-and-source-model.md)
- [Tenant, Discovery und Company Brain](../product/tenant-discovery-company-brain.md)
- [Personal Domain, Member Companion, Personal Memory und Circling](../product/personal-domain-member-companion-circling.md)
- [Cognition Runtime](../runtime/cognition-runtime.md)
- [Kontrollierte externe Wirkung](../runtime/governed-effect.md)
- [Local Runtime Node — Kandidat](../runtime/local-runtime-node.md)
- [Quellengrundlage](../reference/source-basis.md)
