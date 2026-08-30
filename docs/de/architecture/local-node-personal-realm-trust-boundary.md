# Local Runtime Node × Personal Realm — gemeinsame Trust Boundary

**Status:** ÖFFENTLICHE CROSS-SOURCE-PROJEKTION — beschreibend, nicht autoritativ  
**Authority:** keine aus diesem Dokument heraus  
**Source basis:** Local-Runtime-Node-Candidate v0.1.0 + Device-Identity/Enrollment-Amendment sowie Personal-Realm-Owner-Surface baum777/unitera_companion main@8dd8112a74631516c134bc3fc528d6220cdd27a7

[English edition](../../en/architecture/local-node-personal-realm-trust-boundary.md)

## 1. Reifegrad und gemeinsame Boundary

Local Runtime Node und Personal Realm sind unterschiedliche Trust Boundaries, besitzen aber eine reale Bootstrap- und Runtime-Beziehung.

~~~text
Local Runtime Node
= SOURCE_CANDIDATE_NON_AUTHORITATIVE
= nicht source-adoptiert
= nicht runtime-aktiv
= nicht produktiv autorisiert

Personal Realm
= Owner Decisions 20/20 finalisiert
= Owner-Architekturfundament auf unitera_companion/main gemerged
= Cross-Repo Adoption ausstehend
= Runtime absent
= Production Effects nicht autorisiert
~~~

Beide Flächen dürfen gemeinsam auditiert werden, aber nicht als gleich reife Architektur-Candidates behandelt werden.

## 2. Bootstrap-Abhängigkeit ohne Identitätsverschmelzung

Die Owner-Entscheidung für das Personal Realm bindet den initialen Companion-Bootstrap an:

1. authentifizierten PlatformPrincipal;
2. erfolgreich gebundenen Local Runtime Node;
3. initialisierten lokalen UNITERA Workspace;
4. expliziten Companion Bootstrap.

~~~text
LocalNodeIdentity != PersonalRealm
LocalNodeIdentity != PersonIdentity
TenantNodeBinding != PersonalRealmBinding
Node replacement != new Personal Realm
~~~

Ein Personal Realm kann mehrere Local Runtime Nodes binden. Der Node ist Materialisierungs- und Resource-Bedingung, nicht semantischer Owner des Realm.

## 3. Keine Authority durch Lokalität

~~~text
Local Reachability != Authority
Device Ownership != Tenant Authority
Node Enrollment != Capability Grant
Filesystem Reachability != Resource Permission
Resource Permission != Business Authority
OS Permission != UNITERA Permission
~~~

Dass Datei, Credential oder Anwendung auf demselben Gerät liegen, berechtigt weder Companion noch Tenant automatisch zum Zugriff.

## 4. Person, Realm, Tenant und Membership

~~~text
Person != PlatformPrincipal
PersonalRealm != CompanyTenant
PersonalRealm != Membership
same person != same institutional authority
~~~

Dieselbe Person kann mehreren Company Tenants angehören und ihr Personal Realm fortführen. Institutionelle Kontexte bleiben isoliert.

## 5. Local-first Persistenz und Multi-Node

Die Owner-Richtung für das Personal Realm ist local-first:

~~~text
Primary Local Workspace
→ authoritative working materialization

Encrypted Remote Layer
→ sync / backup / transport / recovery substrate
~~~

Der Remote Layer ist weder Semantic Owner noch standardmäßig zentraler Plaintext-Personal-Store.

~~~text
mechanically safe metadata
→ deterministic merge may be allowed

semantic conflict
→ preserve both revisions
→ explicit reconciliation

last-write-wins
!= default semantic conflict policy
~~~

## 6. Backup und Restore

Personal-Realm-Backups müssen gemäß Owner-Richtung hardware-key-signiert sein.

~~~text
Hardware-Key-Proof
+ Principal/Person Binding
+ Backup Integrity Verification
+ Target Local Runtime Node Binding
→ Restore Eligibility
~~~

Account-Loss-Recovery nutzt einen separaten Break-Glass-Pfad mit unabhängiger Identity Re-Verification.

~~~text
HardwareKey != PersonIdentity
Backup Possession != RestoreAuthority
~~~

Konkrete Kryptographie- und Hardware-Standards bleiben ein separates Implementation Profile.

## 7. Company Context und Personal Memory

~~~text
Company Context Access
!= Personal Memory Residency Permission
~~~

Company-derived durable memory benötigt eine CrossBoundaryResidencyDecision:

~~~text
RETAIN
TRANSFORMED_RETAIN
TRANSIENT_ONLY
DENY
~~~

Bei Membership-Ende muss retained company-derived Personal Memory erneut geprüft werden.

Die Gegenrichtung ist default deny:

~~~text
Company Tenant
→ kein Raw Access auf Personal Memory
~~~

Nur eine explizite PersonalContextProjection darf zweck-, tenant-, scope- und zeitgebunden in Company Context übergehen. Sie bleibt widerrufbar und provenance-aware.

## 8. Kein Local-Node-Bypass für fehlende Company APIs

Nicht zulässig als Architekturabkürzung:

~~~text
missing Company Brain API
→ raw local DB/file access through node
→ treat result as Company Brain truth
~~~

Local Resource Access bleibt Resource Access. Institutionelle Wahrheit bleibt an Company-Brain-, Tenant- und Lifecycle-Surfaces gebunden.

## 9. Credential Boundary

~~~text
Companion / Cognition
→ governed tool request
→ Local Node / Credential Broker
→ local credential resolution
→ bounded adapter execution
→ result / evidence

raw credential
!→ model context
~~~

Raw Credentials gehören weder in Conversation History, Personal Memory, Company Brain, Action Proposal, Capability Grant noch allgemeine Evidence Payloads.

## 10. Companion Shadow Guard und ACT

Der Companion Shadow Guard prüft autonome effectful Personal Actions zusätzlich. Deterministische Checks bleiben immer aktiv; der semantische Layer prüft Reasonableness gegen Intent, Routine, Magnitude, External Visibility, Sensitivity und Novelty.

~~~text
ShadowGuardPass != Authority
Companion Suggestion != Decision
Personal Autonomy != Company Authority
Approval != Capability Grant
Grant != Dispatch
Receipt != Verification
~~~

Der Local Node darf keinen zweiten effectful ACT-Pfad außerhalb der kanonischen Execution-Control-Kette erzeugen.

## 11. Familiarity, Qualification und Autonomie

~~~text
Relationship Familiarity
!= Qualification
!= Global Autonomy Tier
!= Capability-specific Delegation
!= Effective Capability Tier

effective capability tier
<= capability delegated tier
<= global Companion ceiling
~~~

Within-tier Growth darf nur innerhalb bereits autorisierter Bounds erfolgen. Cross-tier Promotion verlangt explizite User Approval und eine neue Delegation Revision.

## 12. Personal → Company Contribution

~~~text
Personal cognition
→ Companion prepares ContributionProposal
→ explicit user confirmation
→ lifecycle-aware institutional command
~~~

Je nach Company-Brain-Lifecycle kann das Ziel DiscoveryInput, CandidateChangeRequest oder BrainChangeProposal/LearningCandidate sein.

~~~text
ContributionProposal != Claim
ContributionProposal != ClaimEligibility
ContributionProposal != Brain Activation
~~~

## 13. Reviewer Assurance bleibt separat

Der aktuell GitHub-verifizierbare Public-Source-Stand enthält noch keine neuere owner-repository-verifizierbare R2/R3-ReviewerClass-Materialisierung. Die Registry projiziert REVIEWER-MODEL-001 weiterhin über GOV-DC-001@0.1.0.

Daher erhebt diese Seite keine neueren R2/R3-Semantiken zu einem source-backed öffentlichen Zustand.

~~~text
Companion Shadow Guard
!= R2/R3 Reviewer Assurance
!= Human Control
!= Capability Grant
~~~

Sobald eine aktuelle Reviewer-Model-Owner-Surface mit exaktem Ref publiziert und verifiziert ist, muss diese Boundary erneut reconciled werden.

## 14. PR #98 bleibt paralleler Product-Track

Unitera_Systems PR #98 bei 903f0250dd754ecc6ddaa87752a86e5c2c1a7f4d ist eine qualifizierte offene Product-/Identity-/Dual-Control-Integration in Review, aber kein semantischer Owner dieser Boundary.

~~~text
PR #98 green
!= Local Node adopted
!= Personal Realm runtime active
!= production authorization
~~~

## 15. Nächste Gates

### Local Runtime Node

Offen bleiben insbesondere:

- v1 Deployment Target oder post-v1;
- Decision Class für TenantNodeBinding;
- Hardware-backed Identity Schwelle;
- user-registrierbare Resource Classes;
- Long-lived Provider Credentials;
- lokale Adapter Qualification;
- Offline-ACT dauerhaft forbidden oder zunächst deferred.

### Personal Realm

Owner Gate 0 ist PASS. Danach folgen:

1. Canonical Contract Materialization;
2. External Authority Bindings;
3. Persistence/Crypto Design;
4. Personal Memory Runtime;
5. Circling/Ideation;
6. Contribution Boundary;
7. Autonomy Contracts;
8. Shadow Guard;
9. Local Effect Pilots;
10. Qualification/Sampling;
11. Cross-Repo Source Adoption;
12. separate Production Activation.

## 16. Explizite Nichtaussagen

Diese Seite behauptet nicht, dass Local Runtime Node adopted/active ist, Personal Realm Runtime existiert, Companion Effects produktiv laufen, company-derived Context automatisch retainable ist, Reviewer Assurance bereits source-verifiziert ist oder PR #98 diese Architektur aktiviert.

## 17. Kurzform

~~~text
Local Node
= physical resource / credential / enforcement boundary

Personal Realm
= personal continuity / memory / context boundary

Company Tenant
= institutional authority boundary

Company Brain
= institutional truth / meaning boundary

Companion
= personal cognition and continuity assistant

None of these boundaries may silently inherit authority from another.
~~~
