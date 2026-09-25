---
description: Gepflegte öffentliche Reifeprojektion für UNITERA; Architekturintention, materialisierte Umsetzung und Live-Reife bleiben getrennt.
icon: gauge-high
---

# Aktueller öffentlicher Stand

`UPD-STATE-001` · `STATUS` · `PUBLIC_STATUS` · `PILOT`

> **Warum existiert das?**
> Architekturintention, materialisierte Capability und Live-/Produktionsreife sind unterschiedliche Aussagen. Diese Seite hält sie getrennt.

{% include "../.gitbook/includes/public-projection.md" %}

| Kontext | Öffentliche Projektion |
|---|---|
| **You are here** | Start / Governance → Aktueller öffentlicher Stand |
| **Authority** | Statuspublikation erzeugt keine Runtime- oder Produktions-Authority |
| **Source State** | gegen aktuelle Owner-Quellen geprüft; abgeleitete Projektionen dürfen zeitlich nachlaufen |
| **Stand** | 25. September 2026 |

## Aktuelle Reifekarte

| Bereich | Semantik / Contract | Materialisierte Umsetzung | Live-Status |
|---|---|---|---|
| Kernarchitektur | etabliert | zentrale Grenzen und Bindungen in begrenzter Form umgesetzt | keine Produktionsautonomie behauptet |
| Institutionelles Wissen | versionierte, aktive Grundlage etabliert | Discovery, Review und Kontextnutzung begrenzt integriert | laufende Organisationsänderungen bleiben review- und aktivierungsgebunden |
| Institutionelles Produkterlebnis | Work-first, Needs You, Chat und Quickactions etabliert | Web- und native Arbeitsflächen sowie eine gemeinsame Cross-Surface-Präsentationsbaseline in begrenzter Form materialisiert | repräsentative Ende-zu-Ende-Qualifikation bleibt für einzelne Journeys offen |
| Persönliche Kontinuität | Personal Realm, Erinnerung, Wiederaufnehmen und Beitragsgrenze etabliert | Personal Hub, Kontinuität und bestätigungsgebundene Beitragsvorbereitung begrenzt umgesetzt | die reale persönliche-zu-institutionelle Runtime-Übertragung wird nicht allgemein als aktiv behauptet |
| Native Kontinuität | Clientzustand bleibt Präsentation, Authority bleibt serverseitig | zentrale Read-, Resume-, Pause-, Trust- und Intent-Zustände sind oberflächenübergreifend vertraglich gebunden | Geräte- oder Clientzustand überträgt keine Authority; repräsentative Live-Parität bleibt separat nachzuweisen |
| Kognition und Routing | Modellfähigkeit, Route, Authority und Datenfreigabe bleiben getrennt | begrenzte Routing- und Resolution-Evidence-Verträge sind materialisiert | Routing-Vertrag oder Modellwahl bedeuten weder Runtime-Aktivierung noch zusätzliche Datenfreigabe oder Authority |
| Kontrollierte Wirkung | Approval, Grant, Execution, Receipt und Verification bleiben getrennt | begrenzte Routing-, Ausführungs- und Evidence-Pfade materialisiert | reale externe Live-Bereitschaft und Pilotaktivierung bleiben separat gegatet |
| Security Evaluation | Finding, Evidenzqualifikation und Authority bleiben getrennt | Klassifikations- und Qualifikationsfähigkeit materialisiert | breite produktive Enforcement-Aktivierung wird nicht behauptet |
| Pilot | versionierter, begrenzter Scope und Commissioning-Grammatik etabliert | Scope-, Onboarding-, Commissioning- und Runtime-Bindungen sind substanziell materialisiert | **Vorbereitung**; reale Betriebsbindungen, externe Zulassung, Ende-zu-Ende-Nachweis und ausdrückliche Aktivierung bleiben offen |
| Produktionsautonomie | nicht Zielbehauptung dieser Reifestufe | — | **nicht behauptet** |

## Was sich seit dem vorherigen Snapshot geändert hat

Seit dem Snapshot vom 18. September wurden weitere begrenzte Implementierungs- und Contract-Slices materialisiert. Dazu gehören insbesondere eine festere Cross-Surface-Präsentationsbaseline für native Arbeitsflächen, zusätzliche deterministische Runtime-Projektionen sowie eine weiter ausdifferenzierte Kognitions-Routing- und Resolution-Evidence-Grenze.

Diese Fortschritte erhöhen die nachweisbare Implementierungsreife, aber nicht automatisch die Live-Reife. Persönliche Beitragsübergabe, reale externe Betriebsbindungen, repräsentative Ende-zu-Ende-Pfade und die ausdrückliche Pilotaktivierung bleiben eigenständige Gates.

Gleichzeitig bleibt die Aussagegrenze unverändert streng:

- materialisierte UI, Contract- oder Runtime-Bausteine bedeuten nicht Live-Aktivierung;
- materialisierte Cross-Surface-Verträge bedeuten nicht repräsentative Ende-zu-Ende-Qualifikation;
- ein eingefrorener Pilotumfang erzeugt weder Grant noch Ausführungsrecht;
- ein Client kann Authority anzeigen oder anfragen, aber nicht selbst erzeugen;
- technische Receipt- oder Provider-Evidenz ist nicht automatisch verifiziertes Geschäftsergebnis;
- reale externe Anbindung, aktuelle Admission, Ende-zu-Ende-Nachweis und ausdrückliche Pilotaktivierung bleiben eigene Gates;
- nicht zusammengeführte Kandidaten werden nicht als aktueller Istzustand gezählt.

## Cross-Repo-Reconciliation-Regel

Der aktuelle Istzustand wird aus den jeweils zuständigen Owner-Quellen abgeleitet. Registry-, Kartographie-, Dokumentations- oder andere abgeleitete Projektionen können zeitlich hinter einem bereits kanonischen Owner-Zustand liegen. Ein solcher Projection-Lag darf den Owner-Zustand weder überschreiben noch künstlich zurückstufen.

Die [Capability- und Use-Case-Matrix](capability-use-case-matrix.md) schlüsselt diese Einordnung nach Produktfunktion, erwartetem Ergebnis und Grenze auf.

## Bedeutet nicht

- `PILOT` bedeutet nicht `CONFORMANT`.
- begrenzte Implementierung bedeutet nicht Live-Verfügbarkeit.
- materialisierte Capability bedeutet keine Ausführungsberechtigung.
- öffentliche Evidenz etabliert aus sich selbst heraus keine operative Wahrheit außerhalb ihres angegebenen Scopes.
