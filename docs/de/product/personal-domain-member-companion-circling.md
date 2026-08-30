# Personal Domain, Member Companion, Personal Memory und Circling

**Status:** PUBLIC PROJECTION — CANDIDATE  
**Autorität:** keine aus sich selbst heraus  
**Quellengrundlage:** source-reconciled Concept Candidate UNITERA-PERSONAL-DOMAIN-MEMBER-COMPANION-CIRCLING-001@0.1.0 sowie die aktuelle Tenant-, Company-Brain-, Product-, Context-, Authority- und Source-Governance-Richtung  
**Canonicalization:** durch dieses Dokument weder Owner-gebunden noch source-adopted oder runtime-materialisiert

Dieses Konzept erweitert UNITERA um eine dauerhafte persönliche Beziehungsebene rund um eine Person, ohne persönliches Gedächtnis zu Unternehmenswahrheit oder Begleitung zu Autorität zu machen.

Die Kernrichtung lautet:

> **Das Company Brain erinnert das Unternehmen. Der Personal Companion erinnert die Person. Circling bewahrt, was relevant werden könnte, bevor Person oder Organisation sich darauf festlegen.**

## Warum dieses Konzept benötigt wird

UNITERA trennt bereits Organisationswissen, aktuelle operative Realität, Cognition, Work und reale Autorität. Ein langfristiger persönlicher Companion bringt eine weitere Form von Kontinuität hinzu: Was UNITERA für genau eine Person über Sessions, Pläne, Ideen und gegebenenfalls wechselnde Organisationszugehörigkeiten hinweg erinnern soll.

Dafür braucht es eine neue Grenze statt eines einzigen undifferenzierten KI-Gedächtnisses.

Das Konzept trennt:

- persönliche Kontinuität von institutioneller Wahrheit;
- Aufmerksamkeit von Commitment;
- eine Idee von einem Claim;
- einen persönlichen Plan von einem Work Order;
- Beratung von einer Decision;
- erinnerten Unternehmenskontext von aktuellem autoritativem Unternehmenszustand;
- eine vertrauensvolle Companion-Beziehung von institutioneller Berechtigung.

## Naming Boundary: Personal Tenant ist ein Working Term

Die ursprüngliche Architekturidee verwendete **Personal Tenant**. Die aktuelle UNITERA-Terminologie verwendet Tenant bereits für eine institutionelle Sicherheits- und Autoritätsgrenze. Deshalb nutzt diese öffentliche Projektion **Personal Domain** als Candidate-Term, bis Terminologie und Owner Binding entschieden sind.

Daher:

~~~text
Personal Tenant
= Working Term

Personal Domain
= bevorzugter Candidate-Term in diesem Dokument

beides
= durch dieses Dokument nicht project-canonical
~~~

Damit wird verhindert, dass eine persönliche Kontinuitätsgrenze den bestehenden Tenant-Begriff still umdefiniert.

## Architektur auf einen Blick

~~~mermaid
flowchart TB
    P[Person] --> PD[Personal Domain]
    PD --> C[Member Companion]

    C --> I[Kommunikation und Interaktion]
    C --> PL[Planner]
    C --> ST[Strategist]
    C --> AD[Advisor]
    C --> PM[Personal Memory]
    C --> CI[Circling]

    PM --> PC[Persönliche Kontinuität]
    CI --> IC[Ideen und Konzepte]
    IC --> CP[Contribution Proposal]

    P --> M[Verifizierte Membership]

    subgraph Company["Company Tenant"]
        D[Discovery / Learning]
        W[/work]
        OP[Operational Pulse]
        CB[Company Brain]
    end

    M --> Company
    CP -->|explizite Contribution Boundary| D
    D --> CB
    CB -->|zweckgebundener Kontext| C
    OP -->|aktueller operativer Kontext| C
    W -->|Work-gebundener Kontext| C
~~~

Das Diagramm zeigt bewusst zwei Richtungen:

1. Unternehmenskontext kann in den Companion projiziert werden, wenn Membership, Zweck und Policy dies erlauben;
2. persönliches Denken kann Unternehmenswissen nur über einen expliziten Contribution-Pfad erreichen.

Keine der beiden Richtungen erzeugt allein durch das Überschreiten der Grenze Autorität.

## Kernkonzepte

| Konzept | Candidate-Bedeutung | Explizit nicht |
|---|---|---|
| **Personal Domain** | Nutzergebundene Kontinuitäts- und Isolationsdomäne für die dauerhafte UNITERA-Beziehung einer Person | Company Tenant, Membership, Authority Domain |
| **Member** | Person/Principal, die über Membership an einem Company Tenant teilnimmt | automatisch Employee, Owner oder Authority Holder |
| **Member Companion** | Dauerhafte persönliche Interaktions- und Cognition-Projektion | Company Agent Assignment, Company Brain, Capability Grant |
| **Personal Memory** | Bewusst gespeicherte nutzergebundene Kontinuitätsinformation | Transcript-Archiv, Runtime State, institutionelle Wahrheit |
| **Circling** | Inkubationszustand für potenziell Relevantes, das noch nicht committed ist | Priority, Work Order, Claim, Decision |
| **Contribution Proposal** | Expliziter Vorschlag, persönliches Material in einen institutionellen Lifecycle zu überführen | Claim Inclusion, Brain Activation, Autorität |
| **Company Brain** | Versioniertes institutionelles Wissen und aktive Organisationswahrheit | Personal Memory, Conversation History |
| **Operational Pulse** | Aktuelle operative Realität des Unternehmens wie Work, Blocker und jüngste Ereignisse | Personal Memory, Company-Brain-Revision |
| **/work** | Primäre Oberfläche für committed operative Aufmerksamkeit | allgemeiner persönlicher Ideenraum |
| **Authority** | Unabhängige Kontrolle über verbindliche institutionelle Wirkung | Beziehungstiefe, Memory, Modellfähigkeit |

## Das Responsibility Model

Das Konzept lässt sich am besten über sechs verschiedene Verantwortungen verstehen:

~~~text
Personal Memory
→ Kontinuität

Circling
→ Inkubation

Company Brain
→ institutionelle Wahrheit

Operational Pulse
→ aktuelle organisationale Realität

/work
→ committed operative Aufmerksamkeit

Authority
→ kontrollierte institutionelle Wirkung
~~~

Die Grenzen sind wichtiger als die Bezeichnungen.

## Member bedeutet nicht Employee

Die generische Beziehung ist **Membership**. Ein Employee kann Member sein, Member soll aber breiter bleiben als ein Beschäftigungsverhältnis.

Mögliche Membership-Kontexte können Employees, Founder, Owner, Contractors, Advisors, Operators, Reviewers oder andere Collaborators umfassen. Die genaue Rollentaxonomie wird hier nicht canonicalized.

~~~text
Person
!= Platform Principal
!= Membership
!= Role
!= Authority Assignment
!= Permission
~~~

Eine Person kann außerdem Memberships in mehreren Company Tenants besitzen. Diese Unternehmenskontexte bleiben getrennt gebunden.

## Der Member Companion

Der Member Companion ist die langfristige Interaktionsbeziehung, über die UNITERA eine Person unterstützt.

Candidate-Rollen sind:

- **Communication und Interaction** — Gespräch, Quick Entry und reflektierender Dialog;
- **Planner** — Ziele, Optionen, Abhängigkeiten, Deadlines, nächste Schritte und persönliche Commitments;
- **Strategist** — Szenarien, Trade-offs, langfristiges Denken, Hypothesen und alternative Wege;
- **Advisor** — Annahmen herausfordern, Widersprüche sichtbar machen, frühere Überlegungen erinnern und blinde Flecken aufzeigen;
- **Continuity Layer** — aktuelles Work und Denken mit früherem persönlichen Kontext verbinden;
- **Idea Incubator** — Ideen erfassen, verbinden und entwickeln, ohne sie vorschnell zu Work oder Company Brain zu machen.

Das sind Cognition- und Product-Rollen. Sie erzeugen keine Authority-Rollen.

Ein Companion darf sagen:

> Dieses Muster ist mehrfach aufgetaucht und könnte eine erneute Betrachtung wert sein.

Er darf daraus nicht machen:

> Das ist jetzt Unternehmenspolicy.

ohne den unabhängigen institutionellen Lifecycle, der einen solchen Zustand tatsächlich erzeugen würde.

## Eine Interaktionsoberfläche, unterschiedliche Semantik

Der Companion sollte nicht als ein einziger undifferenzierter Chat-Stream modelliert werden.

Candidate Semantic Modes:

| Mode | Beabsichtigte Bedeutung |
|---|---|
| Quick Interaction | leichte persönliche Konversation |
| Reflection | Denken, Annahmen und frühere Begründungen prüfen |
| Planning | persönlichen Plan oder Next-Step-Struktur entwickeln |
| Strategy | Optionen und langfristigere Wege vergleichen |
| Advice | Challenge, Kritik oder Empfehlung anfordern |
| Circling Review | inkubierende Ideen und offene Muster erneut betrachten |
| Work Context | innerhalb eines gebundenen Work Objects denken |
| Contribution | persönliches Material absichtlich in Unternehmensprozesse überführen |

Dieselbe Composer-Oberfläche kann sichtbar bleiben, während sich der zugrunde liegende Domain Command ändert.

~~~text
same surface
!= same domain command
~~~

Das folgt dem breiteren UNITERA-Muster für lifecycle-aware Composer-Semantik.

## Personal Memory

Personal Memory ist persistente Information, die gezielt gespeichert wird, um zukünftige persönliche Kontinuität zu verbessern.

Mögliche Candidate-Klassen sind:

- Interaktionspräferenzen;
- Working Patterns;
- persönliche Ziele;
- Planning Context;
- frühere persönliche Entscheidungen und Begründungen;
- persönliche Projekte;
- Reflexionen;
- Ideen und entwickelte Konzepte.

Die exakten Retention Classes und der Policy Owner bleiben offen.

### Memory Formation

Eine Nachricht sollte nicht automatisch Long-Term Memory werden.

~~~mermaid
flowchart LR
    I[Interaktion oder Beobachtung] --> MC[Memory Candidate]
    MC --> E[Memory Eligibility]
    E -->|retain| M[Personal Memory Item]
    E -->|ask| U[User Confirmation]
    E -->|transient| T[Nur Session-Kontext]
    E -->|reject| X[Nicht speichern]
    U --> M
~~~

Mögliche Eligibility-Dimensionen sind künftiger Nutzen, User Intent, Stabilität, Sensitivität, Provenienz, Widerspruch, Scope und explizite Retention-Präferenz.

### Personal Memory ist nicht Runtime State

Sich zu erinnern, dass eine Approval ausstand, ist nicht dasselbe wie der aktuelle Approval-State.

~~~text
Personal Memory:
"Ich erinnere, dass die Approval noch ausstand."

Authoritative Runtime State:
aktuellen kanonischen Approval-State auflösen
~~~

Work State, Membership State, Grants, Receipts, Verification, Tenant Bindings und andere autoritative Runtime-Objekte bleiben außerhalb des Model Memory.

### Personal Memory ist nicht Company Brain

Eine Person kann erinnern:

> Ich glaube, dass Supplier Ownership unklar ist.

Das Company Brain kann aktuell festhalten:

> Supplier Ownership ist Role X unter Revision Y zugeordnet.

Beides kann gleichzeitig existieren. Keines darf das andere still überschreiben.

## Company-derived Personal Memory

Ein Companion kann Company Brain, Operational Pulse oder Work Context temporär sehen, weil die Person eine geeignete Membership und einen passenden Zweck besitzt.

Das bedeutet **nicht** automatisch dauerhaftes Residency-Recht im Personal Memory.

~~~mermaid
flowchart LR
    C[Company Context] --> P[Zweckgebundene Companion Projection]
    P --> R[Personal Memory Candidate]
    R --> G[Cross-boundary Residency Decision]
    G -->|allowed| M[Gespeichertes oder transformiertes Memory]
    G -->|transient only| T[Nicht dauerhaft speichern]
    G -->|deny| D[Memory Candidate verwerfen]
~~~

Candidate-Regel:

~~~text
Company Context Access
!= Personal Memory Residency Permission
~~~

Die exakten Rechts-, Privacy-, Retention- und Employer-Access-Regeln liegen außerhalb dieses Candidates und benötigen die dafür zuständige Authority-/Source-Closure.

## Circling

**Circling** ist der Halte- und Inkubationszustand zwischen dem Wahrnehmen eines möglichen Themas und dem Commitment dazu.

Es ist für Material gedacht, das potenziell bedeutsam wirkt, aber noch nicht bereit ist, Priority, Project, Work Order, Claim oder institutionelle Decision zu werden.

Typische Inhalte:

- Ideen;
- Fragen;
- Weak Signals;
- Muster;
- Spannungen;
- Hypothesen;
- Opportunities;
- Konzeptfragmente;
- mögliche Projekte;
- Bedenken;
- potenzielle Verbesserungen.

Die entscheidende Trennung lautet:

~~~text
Aufmerksamkeit
!=
Commitment
~~~

### Circling Lifecycle

~~~mermaid
flowchart LR
    A[Captured] --> C[Circling]
    C --> D[Developing]
    D --> C
    D --> M[Mature]
    M --> L[Land]
    M --> C
    M --> X[Discard oder Archive]
~~~

Candidate-Maturity-Labels und Lifecycle-State-Namen werden durch diese Seite nicht canonicalized.

### Circling Review

Ein Review sollte vier Fragen beantworten:

1. Was circuliert?
2. Warum ist es noch offen?
3. Was hat sich seit dem letzten Review verändert?
4. Was würde es landen lassen?

Candidate-Aktionen sind weiter circlen, entwickeln, mit einem anderen Item verbinden, challengen, landen, verwerfen oder archivieren.

Der Companion darf eine Disposition empfehlen. Eine Empfehlung erzeugt nicht selbst die Transition, wenn User Control oder Policy etwas anderes verlangen.

## Idea, Concept und Landing

Eine **Idea** ist eine relativ offene Möglichkeit oder ein Gedanke.

Ein weiter entwickeltes Konzept ist eine strukturierte Erklärung, ein Design oder ein Lösungskandidat. Der exakte canonical Term für dieses zweite Objekt bleibt offen, weil UNITERA Terminology Governance Concept auch im formalen Vocabulary-Sinn verwendet.

Die beabsichtigte Maturity Grammar:

~~~text
Impulse
→ Idea
→ Circling
→ Developed Idea
→ Structured Concept
→ Personal Evaluation
→ Landing Decision
~~~

Mögliche Landing-Ziele:

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

Landing bewahrt Provenienz und bedeutet keine automatische Annahme durch das Zielsystem.

~~~text
Circling Item
→ Work Proposal

bedeutet nicht

Work Order created
~~~

## Die Contribution Boundary

Persönliche Cognition darf zu institutionellem Wissen beitragen. Sie darf sich nicht still zu institutioneller Wahrheit hochstufen.

~~~mermaid
flowchart LR
    P[Persönliche Beobachtung / Idee / Konzept / Circling Item] --> I[Expliziter Contribution Intent]
    I --> CP[Contribution Proposal]
    CP --> R[Lifecycle-aware Domain Command]
    R --> D[Discovery Input]
    R --> C[Candidate Change Request]
    R --> B[Brain Change Proposal / Learning Candidate]
    D --> L[Bestehender Company-Brain-Lifecycle]
    C --> L
    B --> L
~~~

Daher:

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

Institutionelle Adoption läuft weiterhin über die bestehende attribuierte Evidence-, Claim-, Candidate-, Revision-, Review- und Activation-Semantik.

## Unternehmenskontext zurück in den Companion

Die Gegenrichtung ist ebenso wichtig.

~~~mermaid
flowchart LR
    B[Verified Tenant und Membership Binding] --> K[Context Compiler]
    CB[Active Company Brain Revision] --> K
    OP[Operational Pulse] --> K
    W[Current Work Context] --> K
    PM[Eligible Personal Context] --> K
    K --> CP[Least-sufficient Companion Context]
    CP --> C[Member Companion]
~~~

Der Companion muss nicht das gesamte Company Brain in Personal Memory kopieren. Er soll nur den zweckgebundenen Kontext erhalten, der für die jeweilige Interaktion erforderlich ist.

## Mehrere Memberships und Tenant Isolation

Eine Personal Domain kann kontinuierlich bestehen, während eine Person zwischen mehreren Organisationen wechselt oder gleichzeitig an mehreren teilnimmt.

~~~mermaid
flowchart TB
    PD[Personal Domain] --> MA[Membership A]
    PD --> MB[Membership B]
    PD --> MC[Membership C]
    MA --> TA[Company Tenant A]
    MB --> TB[Company Tenant B]
    MC --> TC[Company Tenant C]
~~~

Harter Default:

~~~text
Tenant A Context
→ Tenant B Context

DENY
~~~

Dass dieselbe Person beiden Organisationen angehört, verschmilzt weder deren Daten- noch deren Autoritätsgrenzen.

## Membership Exit

Eine aufgehobene oder beendete Membership soll den jeweiligen Unternehmenszugriff entfernen. Das bedeutet nicht automatisch die Löschung aller person-owned Memories, Präferenzen oder Circling Items.

Company-derived Information im persönlichen Raum kann jedoch einen eigenen Residency-/Retention-Review erfordern.

Candidate-Richtung:

~~~text
Membership termination
→ Company Access widerrufen
→ Company-derived Personal Memory prüfen
→ retain / transform / expire / remove nach Policy
~~~

Die genaue Retention-Regel bleibt eine offene Policy- und Rechtsentscheidung.

## Beziehung zu /work

Die source-reconciled Product Direction bleibt **work-first, chat-secondary**.

Der Personal Companion ersetzt /work nicht.

Stattdessen:

- /work bleibt die primäre Oberfläche für committed operative Aufmerksamkeit im Unternehmen;
- der Companion kann rund um ein Work Object interpretieren, vorbereiten, erklären, planen und beraten;
- ein Work-bound Companion Context kann Current Work Object, eligible Company Context und eligible Personal Context kombinieren;
- ein persönlicher Plan wird nicht automatisch Work State;
- ein Companion Thread wird nicht automatisch Work Object.

~~~text
Personal Plan != Work Order
Companion Thread != Work Object
Companion Plan != Work State
~~~

## Authority- und Safety-Invarianten

Eine langfristige Beziehung darf niemals zu einem impliziten Authority Shortcut werden.

~~~text
mehr Memory
!= mehr Authority

bessere Personalisierung
!= mehr Authority

langfristige Beziehung
!= mehr Authority

User Trust
!= institutionelle Authority

besseres Modell
!= mehr Authority
~~~

Wenn eine Companion-Interaktion einen realen Effect Proposal erzeugt, gilt weiterhin die normale UNITERA-Kette:

~~~mermaid
flowchart LR
    C[Companion Cognition] --> P[Action Proposal]
    P --> E[Effective Autonomy und Policy]
    E --> H[Human Control wenn erforderlich]
    H --> G[Capability Grant]
    G --> D[Dispatch]
    D --> R[Receipt]
    R --> V[Verification]
~~~

Der Companion kann keinen Grant erzeugen, Approval aus conversational trust ableiten oder Personal Memory als Business Permission wiederverwenden.

## Candidate Product Topology

Eine künftige Product Projection könnte die persönliche Beziehung so darstellen:

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
├── Company Brain Inspection
└── Discovery / Learning
~~~

Das ist eine Product Direction und keine Behauptung aktueller Implementierung.

## Candidate Object Set

Der Source-ready Candidate schlägt aktuell folgende logische Objekte zur Owner-Prüfung vor:

- PersonalDomainRef;
- PersonalDomainBinding;
- PersonalMemoryItem;
- CirclingItem;
- PersonalPlan;
- ContributionProposal;
- CompanionContextBinding;
- CrossBoundaryResidencyDecision.

Owner Review sollte das kleinste ausreichende canonical Contract Set auswählen, statt automatisch jeden Candidate als separates Domain Object zu materialisieren.

## Offene Owner Decisions

Vor canonical Adoption sind mindestens diese Fragen offen:

1. Wie lautet der canonical Name: Personal Domain, Personal Tenant, Personal Space oder ein anderer Term?
2. Welche Authority Domain besitzt das Person ↔ Personal Domain Binding?
3. Wird für jeden Platform Principal eine Personal Domain provisioniert oder nur für explizit gebundene Personen?
4. Welche Klassen von Personal Memory dürfen standardmäßig persistieren?
5. Wer besitzt die Cross-Boundary-Memory-Residency-Policy?
6. Was geschieht mit Company-derived Personal Memory nach Suspension oder Revocation einer Membership?
7. Welche Memory-Klassen sind für die Person einsehbar, editierbar oder vergessbar?
8. Wird Circling ein canonical Domain Concept oder bleibt es ein Product Label über einem generischeren Objekt?
9. Welcher minimale Contract trennt Idea, entwickeltes Concept, Personal Plan und Work Proposal?
10. Darf ein Company Tenant jemals über explizit contributed Content hinaus auf Personal Memory zugreifen?

Eine konservative Architecture Direction ist **default deny** für beliebigen Unternehmenszugriff auf Personal Memory. Auch dies bleibt Candidate Policy, bis der Owner gebunden ist.

## Öffentlicher Status

Diese Seite dokumentiert einen **source-reconciled Architecture and Contract Candidate**. Sie behauptet nicht:

- dass Personal Domain bereits in der Runtime existiert;
- dass Personal Tenant canonical Terminology ist;
- dass jeder User bereits eine Personal Domain erhält;
- dass Circling bereits ein canonical Domain Object ist;
- dass Company Administrators Personal Memory einsehen dürfen;
- dass Company Information dauerhaft in Personal Memory kopiert werden darf;
- dass Personal Memory für Model Training verwendet werden darf;
- dass der Companion institutionelle Authority besitzt;
- dass der Companion /work oder Company-Brain-Governance umgehen darf.

## Candidate Doctrine

~~~text
ERINNERE die Person, ohne die Person zu institutionalisieren.

VERSTEHE das Unternehmen, ohne Company Truth zu personalisieren.

CIRCLE, was relevant werden könnte, bevor Commitment erzwungen wird.

LANDE bewusst.

CONTRIBUTE explizit.

PROMOTE über kontrollierte institutionelle Lifecycles.

ARBEITE über kontrollierte Work Surfaces.

ACT nur über unabhängige Authority.
~~~

In einem Satz:

> **UNITERA gibt einer Person eine dauerhafte Denkbeziehung, ohne persönliches Gedächtnis, Organisationswahrheit, committed Work und institutionelle Authority zu einem undifferenzierten KI-Gedächtnis zu verschmelzen.**
