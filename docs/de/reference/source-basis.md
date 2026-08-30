# Quellengrundlage

**Snapshot-Datum:** 30.08.2026  
**Repository-Rolle:** PUBLIC DOCUMENTATION PROJECTION  
**Autorität:** keine aus sich selbst heraus

## Verifizierte Default-Branch-Refs

| Repository | Verifizierte Default-Branch-Ref | Verwendet für |
|---|---|---|
| baum777/coreos | c34b61a9264348afaaae96c5b94e169011bf76ab | Foundation, Company Brain, Tenant-Foundation-Semantik und aktuellen Owner-Boundary-Stand |
| baum777/unitera-os | 18c50f837aa5442d29edf0bae7f0beb5fd9fa94b | Providerneutrale Capability-/Autonomie-/Execution-Verträge und CI-gegatete Conformance |
| baum777/Unitera_Systems | 786d03ca731acf5ab1af38731954891e84542d8c | Kanonischer Runtime-Consumer, Persistenz, APIs, gehostete Authentifizierung und begrenzte Authority-Enforcement |
| baum777/unitera_control_plane | fc9370eb146dd068027f9dd9b3a7bdd01626bb65 | Aktueller Tenant-/Governance-Owner-Repository-Head; frühere Contract-Revisionen bleiben dort zitiert, wo sie das exakte semantische Review-Subject sind |
| baum777/unitera-registry | 891f9b967328131d8d3348ffba3dc64e7c1163ac | Registry-Vertrag, Provenienz, Continuous Reachability und RCC-/Digest-Verification-Closure |
| baum777/unitera_companion | 8dd8112a74631516c134bc3fc528d6220cdd27a7 | Personal-Realm-Owner-Decisions und gemergtes Architekturfundament |

Diese Refs identifizieren die zum Review-Zeitpunkt verifizierten aktuellen Default Branches. Ein neuerer Repository-Head verändert nicht rückwirkend den Scope einer Decision oder eines Reviews, das an einen früheren exakten Commit gebunden war.

## Verifizierte Implementierungsprojektion

Das dedizierte Production Pilot Interface ist separat verifiziert:

~~~yaml
repository: baum777/unitera-production-interface
ref: main
head: d7cbf8ce78bb7c2e5737a126d972dfd638a378fd
role: PRODUCT_UI_PLUS_BFF
semantic_authority: NONE_BY_IMPLEMENTATION
production_execution_activated: false
live_effect_active: false
~~~

Sein gemergter PR #1 enthält den Migration-Closure-Stack und die kontrollierte Settings-/Profile-Produktoberfläche. Für den qualifizierten PR-Head `9e688b94b3335a625543a39aeb9873b1d88444e5` ist ein erfolgreicher Remote-`ci`-Run beobachtet.

Dieses Repository belegt Product-/UI-/BFF-Materialisierung, ist aber keine Ersatz-Authority-Quelle für Tenant-, Membership-, Company-Brain-, Capability-, Grant- oder Execution-Semantik.

## Qualifizierte nichtkanonische Evidenz

### Discovery Runtime — Unitera_Systems PR #94

~~~yaml
repository: baum777/Unitera_Systems
ref: codex/discovery-pilot-readiness-closure
head: 19e70f220a83c331b7fc7f4c9bbd9e3ff9d35893
pull_request: 94
compared_to_main:
  ahead_by: 15
  behind_by: 0
classification: QUALIFIED_DEVELOPMENT_SLICE
canonical_main: false
runtime_activation_claimed: false
~~~

Dieser Branch enthält Discovery-Persistenz, deterministische Cognition, strukturiertes Wissen/Provenienz, `/work/discovery`, First Work, RLS und Qualifikationsevidenz.

Branch-Evidenz wird niemals als kanonisches main oder Production Activation dargestellt.

### Pilot UI / Identity / Decision Integration — Unitera_Systems PR #98

~~~yaml
repository: baum777/Unitera_Systems
ref: pilot-ui-01/production-entry-readonly-pilot
head: 903f0250dd754ecc6ddaa87752a86e5c2c1a7f4d
pull_request: 98
classification: QUALIFIED_INTEGRATION_IN_REVIEW
canonical_main: false
remote_workflows:
  audit_gates: success
  visual_enforcement_level_2: success
  canonical_enforcement: success
  governance_guardrails: success
  ci: success
~~~

Dieser Branch wird ausschließlich für ausdrücklich als nichtkanonischer Integrationsfortschritt markierte Aussagen verwendet. Er enthält aktuell Natural-Person-Identity/Attestation, HumanDecision/DualControlSet, umfassendere Work-Read-Models und einen Read-only Pilot Product Entry.

Erfolgreiche Workflows machen diesen Branch weder zu Owner Authority noch zu Source Adoption, Runtime Activation oder Production Permission.

## Personal-Realm-Source-State-Update

Die frühere öffentliche Projektion behandelte `unitera_companion/architecture/personal-realm-foundation@cb59971c` als offenen Owner-Materialisierungs-PR.

Dieser Zustand ist superseded: PR #1 wurde am 30.08.2026 gemerged; `unitera_companion/main@8dd8112` enthält nun das owner-designierte Architekturfundament.

Aktueller Stand:

~~~yaml
owner_decisions_finalized: true
owner_main_merged: true
cross_repo_adoption_complete: false
runtime_activated: false
production_execution_authorized: false
~~~

## Registry-Integritätsstand

`unitera-registry@891f9b9` enthält den Abschluss des RCC-/Digest-Verification-Programms.

Beobachtetes Ergebnis des gemergten Review-Programms:

~~~text
Digest-Assertions klassifiziert: 188 / 188
exakte rekalkulierbare Matches: 130
non-recalculable-by-design: 58
unresolved: 0

Live Reachability:
verified: 163
mismatch: 0
unverifiable: 0
record gaps: 0
~~~

Dies belegt Integritäts-/Reachability-Eigenschaften von Registry-Assertions. Es erzeugt **keine** Source Adoption oder Authority.

Dieselbe Registry weist für den Pilot Authority Freeze weiterhin `FREEZE_NOT_AUTHORIZED` aus, weil Independent-Review- und Tenant-Control-Plane-Runtime-Conformance-Declaration-Gates offen bleiben.

## Bereitgestelltes Source-Reconciliation-Material

Das im Projekt bereitgestellte Paket vom 15.08.2026 umfasst:

- Systemarchitektur und Autoritätsvorrang;
- Tenant, Discovery, epistemischen Zustand und Company-Brain-Lifecycle;
- KNOW / THINK / ACT und Autonomie-/Sicherheitsgrenzen;
- Lifecycle-Gates, Bindings und semantischen Kern;
- Source State, Konflikte, Adoption und Supersession Candidates;
- Herleitung der Sicherheitslogik und Familien negativer Tests.

Diese Artefakte enthalten ausdrücklich eingefrorene Spezifikationen, Owner Decisions vor Adoption, Candidates und abgeleitete nichtautoritative Zusammenfassungen. Ihre Klassifikationen bleiben erhalten.

## Später bereitgestellte Source Candidates und Architektur-Richtungen

Die zusammenhängende öffentliche Architekturprojektion berücksichtigt zusätzlich diese bereitgestellten Materialien, ohne ihren Reifegrad durch die Publikation anzuheben:

- UNITERA Local Runtime Node & Device Capability Boundary, v0.1.0, `SOURCE_CANDIDATE_NON_AUTHORITATIVE`;
- Local Runtime Node Device Identity & Enrollment Amendment, Candidate/non-authoritative;
- UNITERA Backend-Agnostic Processing and Governed Route Resolution, v0.1.0, `SOURCE_CANDIDATE_NON_AUTHORITATIVE`;
- UNITERA Open-Weights Model Infrastructure — Long-Term Architecture Plan, v0.1.0, `LONG_TERM_ARCHITECTURE_DIRECTION_NON_AUTHORITATIVE`;
- UNITERA Canonical Naming, Terms & Definitions Ruling Specification, v0.1.0, `RULING_SOURCE_CANDIDATE_READY_FOR_OWNER_BINDING`;
- historisches Personal-Domain-/Member-Companion-/Personal-Memory-/Circling-Candidate-Material, öffentlich in Terminologie und Owner-Richtung inzwischen durch die gemergte Personal-Realm-Owner-Foundation superseded;
- source-reconciled Runtime-/Harness-Ergänzungen zu Runtime State, Memory, Handoff, Evaluation und Failure Attribution, soweit ausdrücklich als Candidate-Richtung markiert.

Diese Materialien dürfen die Erklärung erweitern. Sie dürfen keine verifizierte Owner-Repository-Authority überschreiben.

## Pilot-Modellwahl-Evidenz

Die öffentliche OpenRouter-/Model-Routing-Seite verwendet zusätzlich:

- den Backend-Agnostic-Processing-Candidate;
- den Open-Weights-Langfristplan;
- datierte Modellvergleichs- und Harness-Evaluations-Evidenz vom 29.–30.08.2026.

Diese Evidenz bleibt **Pilot Working Evidence**.

Spätere Chat-only Provider-/Modell-Entscheidungen werden hier nicht hochgestuft, solange sie nicht unabhängig in einer zuständigen Repository-Surface verifizierbar sind. Die aktuelle Public Page bleibt deshalb ein Pilot-Architecture-/Working-Plan-Dokument und kein permanenter Modell-/Provider-Standard.

## Pointer-Status

Die aktuelle Registry-Evidenz bewahrt:

~~~text
CURRENT_SOURCE_POINTER = NOT_CHANGED
Pilot Owner Freeze = FREEZE_NOT_AUTHORIZED
~~~

Diese Prüfung behauptet keine Aktivierung eines einheitlichen Source Pointers.

## Evidenzklassen

- **Observed:** aus exakten GitHub-Refs, Trees, Commits, Branch-Vergleichen, Dateien, PR-Metadaten, Reviews oder Workflow-Ergebnissen gelesen.
- **Source-derived:** aus bereitgestelltem Source-Material unter Beibehaltung des Reifegrads zusammengefasst.
- **Inferred:** ausdrücklich markierte Schlussfolgerung aus beobachteter Evidenz.
- **Unverified:** von kanonischen/materialisierten/Production-Claims ausgeschlossen.


## Cross-Source-Reconciliation: Local Node × Personal Realm

Für die gemeinsame Trust-Boundary-Projektion werden zwei unterschiedlich reife Quellen nebeneinander verwendet:

~~~text
Local Runtime Node
→ SOURCE_CANDIDATE_NON_AUTHORITATIVE

Personal Realm
→ owner decisions finalized
→ unitera_companion/main@8dd8112
→ cross-repo adoption pending
~~~

Die Personal-Realm-Owner-Surface entscheidet die Bootstrap-Abhängigkeit von gebundenem Local Runtime Node und lokalem Workspace. Sie adoptiert dadurch den Local-Node-Candidate nicht automatisch und erzeugt keine Local-Node-Runtime-Aktivierung.

## Reviewer-Assurance-Source-Gap

Im verifizierten GitHub-Stand dieser Aktualisierung wurde kein exakter Owner-Repository-Ref für eine neuere REVIEWER-MODEL-001-/R2-/R3-Materialisierung gefunden.

Der aktuell verifizierbare Registry-Eintrag bleibt:

~~~text
REVIEWER-MODEL-001
state: open_source_available
source_ref: GOV-DC-001@0.1.0
governance_activation: decision_recorded_implementation_pending
~~~

Daher werden neuere, nur lokal oder in Session-Evidence berichtete Reviewer-Assurance-Entscheidungen nicht als source-backed Public State publiziert. Public Documentation != Authority.

## OpenRouter-Reconciliation-Hinweis

Die Public OpenRouter-/Model-Routing-Seite bleibt ein Pilot Working Plan. Diese Publikationsrunde hat keine neue Live-Serving-/Provider-Qualification durchgeführt. Ein eventueller neuerer Runtime-Closure-Stand muss gegen exakte Owner-/Implementation-Refs separat verifiziert werden, bevor die öffentliche Statusklassifikation geändert wird.

## Konfliktregel

Weicht diese öffentliche Projektion von einem verifizierten Owner-Artefakt ab, gewinnt das Owner-Artefakt. Widersprechen sich Owner-Quellen oder können sie nicht verifiziert werden, muss das öffentliche Dokument die Lücke ausweisen statt sie still zu schließen.
