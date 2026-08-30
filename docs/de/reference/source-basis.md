# Quellengrundlage

**Snapshot-Datum:** 30.08.2026  
**Repository-Rolle:** PUBLIC DOCUMENTATION PROJECTION  
**Autorität:** keine aus sich selbst heraus

## Verifizierte Refs der Owner-Repositories

| Owner-Repository | Verifizierte Ref des Default-Branches | Verwendet für |
|---|---|---|
| baum777/coreos | 3f23e2fa920f8b3bfe78d7fe898078ff924c1814 | Foundation, Company Brain, Promotion und Governance-Status |
| baum777/unitera-os | 18c50f837aa5442d29edf0bae7f0beb5fd9fa94b | Providerneutrale Capability-/Autonomie-/Execution-Verträge |
| baum777/Unitera_Systems | 786d03ca731acf5ab1af38731954891e84542d8c | Runtime, Persistenz, API, gehostete Authentifizierung, Produkt und Consumer-Erzwingung |
| baum777/unitera_control_plane | 10e2a3953a76a892cb4112dcf9c1f7998d970970 | Physisches Tenant-/Governance-Ownership, Zuordnungstopologie und Pilot-Policy |
| baum777/unitera-registry | a2f4ccac009305741e463eba99069e8052c172fd | Registry-Schema, Referenzvertrag, Validierung und Erreichbarkeitsstatus |

## Qualifizierte nichtkanonische Evidenz

Die Discovery-Dokumentation berücksichtigt außerdem den Remote-Branch:

~~~yaml
repository: baum777/Unitera_Systems
ref: codex/discovery-pilot-readiness-closure
head: 7f7a3b35e957dafaf0d3cb11eb46c5788ddecdfe
compared_to_main:
  ahead_by: 11
  behind_by: 0
classification: QUALIFIED_DEVELOPMENT_SLICE
~~~

Branch-Evidenz wird niemals als kanonisches main oder Produktionsaktivierung dargestellt.

Die Personal-Realm-Dokumentation berücksichtigt zusätzlich den Review-Branch des owner-designierten Repositories:

~~~yaml
repository: baum777/unitera_companion
ref: architecture/personal-realm-foundation
head: cb59971c8f171954e979a0f8a6fccbd5a0176116
pull_request: 1
classification: OWNER_DECISIONS_FINALIZED_OWNER_MATERIALIZATION_IN_REVIEW
owner_main_merged: false
cross_repo_adoption_complete: false
runtime_activated: false
~~~

Dieser Branch wird verwendet, weil die Owner-Grill-Me-Entscheidungen finalisiert und dort materialisiert sind, während der Default Branch des Owner-Repositories das Architekturfundament noch nicht adopted hat.

## Bereitgestelltes Quellen-Abgleichsmaterial

Das für diese Prüfung bereitgestellte Paket vom 15.08.2026 umfasst:

- Systemarchitektur und Autoritätsvorrang;
- Tenant, Discovery, epistemischen Zustand und Company-Brain-Lifecycle;
- KNOW / THINK / ACT und Autonomie-/Sicherheitsgrenzen;
- Lifecycle-Gates, Bindings und semantischen Kern;
- Quellenstatus, Konflikte, Adoptions- und Supersession-Kandidaten;
- Herleitung der Sicherheitslogik und Familien negativer Tests.

Diese Artefakte enthalten ausdrücklich eingefrorene Spezifikationen, Owner-Entscheidungen vor Adoption, Kandidaten und abgeleitete nichtautoritative Zusammenfassungen. Ihre Klassifikationen bleiben erhalten.

## Später bereitgestellte Source Candidates

Für die öffentliche Projektion des Local Runtime Node wird zusätzlich herangezogen:

- UNITERA Local Runtime Node & Device Capability Boundary, Spec-ID UNITERA-LOCAL-RUNTIME-NODE-DEVICE-CAPABILITY-BOUNDARY-001, Version 0.1.0, Status SOURCE_CANDIDATE_NON_AUTHORITATIVE;
- UNITERA Local Runtime Node — Device Identity & Enrollment Amendment v0.1.1, Status SOURCE_CANDIDATE_READY_NON_AUTHORITATIVE.

Diese Kandidaten werden ausschließlich als Kandidaten dokumentiert. Sie belegen weder Owner-Surface-Adoption noch Runtime-Aktivierung, Production Execution oder Source-Pointer-Aktivierung.

## Weitere Source Candidates und Architektur-Richtungen

Für die zusammenhängende Architektur-&-Logik-Projektion werden zusätzlich die folgenden bereitgestellten, nicht automatisch kanonischen Materialien berücksichtigt:

- UNITERA Backend-Agnostic Processing and Governed Route Resolution Source Candidate, Version 0.1.0, Status SOURCE_CANDIDATE_NON_AUTHORITATIVE;
- UNITERA Open-Weights Model Infrastructure — Long-Term Architecture Plan, Version 0.1.0, Status LONG_TERM_ARCHITECTURE_DIRECTION_NON_AUTHORITATIVE;
- UNITERA Canonical Naming, Terms & Definitions Ruling Specification, Version 0.1.0, Status RULING_SOURCE_CANDIDATE_READY_FOR_OWNER_BINDING;
- der frühere Candidate UNITERA Personal Domain, Member Companion, Personal Memory & Circling v0.1.0 als historische/source-reconciled Grundlage, öffentlich in Terminologie und Owner-Richtung inzwischen durch die qualifizierte Personal-Realm-Owner-Materialisierung in `unitera_companion` superseded;
- source-reconciled Runtime-/Harness-Ergänzungen zu Runtime State, Memory, Handoff, Evaluation und Failure Attribution, soweit sie in der öffentlichen Gesamterklärung ausdrücklich als Candidate-Richtung markiert sind.

Diese Materialien erweitern die Erklärung des Systembilds. Sie dürfen keine verifizierte Owner-Repo-Authority überschreiben und erzeugen insbesondere keine Routing-, Model-, Tenant-, Memory-, Naming- oder Execution-Authority.

Für die öffentliche Projektion der Pilot-Modellwahl und des OpenRouter-Routings werden zusätzlich herangezogen:

- `UNITERA Backend-Agnostic Processing and Governed Route Resolution Source Candidate`, Version 0.1.0, Status `SOURCE_CANDIDATE_NON_AUTHORITATIVE`;
- `UNITERA Open-Weights Model Infrastructure — Long-Term Architecture Plan`, Version 0.1.0, Status `LONG_TERM_ARCHITECTURE_DIRECTION_NON_AUTHORITATIVE`;
- datierte Modellvergleichs- und Harness-Evaluations-Evidenz aus den Discovery-/Grill-Me-Pilotläufen vom 29.–30.08.2026.

Die Modellvergleichsevidenz wird als **Pilot Working Evidence** behandelt. Sie begründet weder allgemeine Modellüberlegenheit noch eine dauerhafte Provider- oder Modellbindung. Die konkrete Runtime-Bindung bleibt vor Aktivierung separat zu verifizieren.

## Pointer-Status

Der bereitgestellte Source-State-Snapshot meldet candidate_pointer_not_activated. Diese Prüfung hat spätere Zustände der Owner-Repositories einzeln verifiziert, aber keine separate Aktivierung eines einheitlichen Pointers. Eine solche Aktivierung wird daher nicht behauptet.

## Evidenzklassen

- **Observed:** aus exakten GitHub-Refs, Trees, Commits, Branch-Vergleichen, Dateien oder Review-Metadaten gelesen.
- **Source-derived:** aus dem bereitgestellten Paket oder ausdrücklich bezeichneten Source Candidates unter Beibehaltung des ursprünglichen Reifegrads zusammengefasst.
- **Inferred:** ausdrücklich gekennzeichnete Schlussfolgerung aus beobachteter Evidenz.
- **Unverified:** von Aussagen über Materialisierung oder Produktion ausgeschlossen.

## Konfliktregel

Weicht diese öffentliche Projektion von einem verifizierten Owner-Artefakt ab, gewinnt das Owner-Artefakt. Widersprechen sich Owner-Quellen oder können sie nicht verifiziert werden, muss das öffentliche Dokument OPEN ausweisen.

## Source-State-Hinweis zum Personal Realm

Für das Personal Realm darf die öffentliche Dokumentation festhalten, dass die **Owner Decisions finalisiert** sind und `unitera_companion` die **owner-designierte semantische Surface** ist. Gleichzeitig muss sie ausweisen, dass die aktuellen Architekturartefakte noch in PR #1 / Branch `architecture/personal-realm-foundation` liegen, Cross-Repo Adoption aussteht und durch diese Dokumente weder Runtime noch Production Execution aktiviert wurden.
