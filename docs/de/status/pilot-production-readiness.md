# Pilot und Produktionsreife

Status: `PUBLIC_STATUS`

**Stand:** 25. September 2026

UNITERA befindet sich weiterhin in **Pilotvorbereitung**. Gegenüber dem vorherigen öffentlichen Snapshot ist die technische und produktseitige Vorbereitung jedoch deutlich weiter materialisiert: der begrenzte Pilotumfang, Commissioning, Onboarding, kontrollierte Workflows, Evidence-/Recovery-Semantik sowie Web- und native Produktflächen besitzen inzwischen nachweisbare Umsetzungsanteile.

Das ist ausdrücklich **keine Pilotaktivierung** und keine Produktionsfreigabe.

## Bereits materialisiert

Öffentlich belastbar ist inzwischen folgende Reifestufe:

- ein versionierter, begrenzter Pilotumfang mit expliziter Änderungsgrenze;
- geführtes Onboarding und Commissioning mit qualitativer Readiness statt künstlicher Prozentwerte;
- Work-, Needs-You-, Chat- und Quickaction-Grammatik mit getrennten Authority-Grenzen;
- begrenzte Web-, Desktop- und Mobile-Projektionen einschließlich Wiederaufnahme, Pause und aktuellen/veralteten Zuständen;
- eine materialisierte Cross-Surface-Präsentationsbaseline für zentrale Zustände, ohne daraus vollständige Ende-zu-Ende-Parität abzuleiten;
- getrennte Entscheidung, Grant, Ausführung, Receipt, Verification und Reconciliation;
- fehlertolerante Recovery-Semantik ohne blinden Retry nach unklarem externem Effekt;
- Personal-Continuity- und Beitragsvorbereitung, ohne persönliche Kontinuität mit institutioneller Authority zu vermischen;
- materialisierte Security-Klassifikation und Evidenzqualifikation, ohne daraus Produktions-Enforcement abzuleiten.

## Vor einem realen Pilotstart weiterhin offen

Für einen Live-Pilot müssen die aktuellen, realen Voraussetzungen des konkreten Betriebs zusätzlich nachgewiesen werden. Dazu gehören insbesondere:

- tatsächlich erreichbare und aktuell zugelassene externe Systeme;
- repräsentative Ende-zu-Ende-Qualifikation der oberflächenübergreifend gebundenen Arbeits- und Kontinuitätszustände;
- gültige tenant- und ressourcengebundene Betriebsbindungen;
- reale Ende-zu-Ende-Evidenz für die im Pilot benötigten externen Pfade;
- aktuelle Grant-, Pause-, Revocation-, Expiry- und Re-Evaluation-Nachweise an den effectful Grenzen;
- ein geführter realer Fall mit ehrlichem Ergebnisnachweis und Recovery-Verhalten;
- die ausdrückliche Aktivierung des exakt angezeigten Pilotumfangs.

Fehlt eine dieser Voraussetzungen, bleibt die betroffene Funktion sichtbar als nicht bereit, blockiert oder nur vorbereitbar. Ein implementierter Pfad darf nicht als live ausgegeben werden, nur weil Contract-, Fixture- oder Simulationsprüfungen erfolgreich sind.

## Pilot-Erlebnis

Die Owner-bestätigte Pilot-Richtung bleibt mobile-first und setzt auf nachvollziehbare, begrenzte Arbeitsabläufe statt breite autonome Softwaresteuerung. Zur Vorbereitung gehören:

- geführtes Onboarding mit verständlicher Schritt-für-Schritt-Dokumentation;
- ein abschließender Test von Öffnen, Prüfen, Entscheiden, Ergebnisnachweis und Pause;
- ein Feedback- und Hilfekanal sowie regelmäßige gemeinsame Reviews;
- eine fortbestehende menschliche Pause als klare Betriebsgrenze;
- manueller Takeover, wenn ein abhängiger technischer Pfad nicht zuverlässig fortgesetzt werden kann;
- anschließende Reconciliation, damit manuell erledigte oder unklare Wirkungen nicht doppelt ausgeführt werden.

Ein technischer Erfolg ist nicht automatisch ein Geschäftserfolg. Unklare Ergebnisse bleiben unklar, bis ausreichende Evidenz vorliegt.

## Produktionsgrenze

Produktion ist eine eigene Reifestufe. Weder ein grüner technischer Check noch ein materialisierter Pilotpfad, eine erfolgreiche Simulation oder ein begrenzter Live-Pilot erzeugen automatisch Produktionsautonomie.

Diese Seite veröffentlicht keine Engineering-Tickets, internen Gates, Anbieter-, Credential-, Security- oder Runtime-Bindings.

---

[← Vorherige: Lokale Runtime-Grenze](../runtime/local-runtime-node.md) · [Index](../README.md) · [Nächste: Dokumentations- und Diagrammkonventionen →](../style/documentation-and-diagrams.md)
