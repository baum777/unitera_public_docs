# Funktionen, Capabilities und Use Cases

**Disclosure:** PUBLIC_CORE · PUBLIC_ABSTRACTED · PUBLIC_STATUS
**Stand:** 25. September 2026

Diese Seite übersetzt die öffentliche UNITERA-Architektur in konkrete
Produktfähigkeiten und Anwendungssituationen. **Capability** bezeichnet hier
eine öffentlich erklärte Produktfähigkeit — nicht einen formalen Capability
Grant oder eine Ausführungserlaubnis.

## Status lesen

| Status | Bedeutung |
|---|---|
| **Etabliert** | Die Semantik oder Architektur ist fest beschrieben. Das bedeutet nicht automatisch vollständige Produktverfügbarkeit. |
| **Begrenzte Umsetzung** | Nachweisbare Produkt-, Contract- oder Runtime-Teile sind materialisiert; daraus folgt keine allgemeine Live- oder Ende-zu-Ende-Reife. |
| **Aktive Entwicklung** | Eine bereits materialisierte Fläche wird weiter vervollständigt oder qualifiziert. |
| **Owner-bestätigter Kandidat** | Eine Richtung ist bestätigt, aber noch nicht als aktueller kanonischer Istzustand materialisiert. |
| **Pilotvorbereitung** | Ein begrenzter Pilot wird vorbereitet, ist durch diese Dokumentation aber nicht aktiviert. |
| **Live gegatet** | Die interne Capability-Kette ist begrenzt materialisiert, während reale externe Nutzung zusätzliche aktuelle Gates benötigt. |
| **Absichtlich begrenzt** | Wirkung bleibt auf explizit kontrollierte Pfade beschränkt; breite Autonomie wird nicht behauptet. |

## Produktfunktionen

| Funktion | Öffentliche Capability | Typische Use Cases | Aktueller Status | Was man öffentlich erwarten kann |
|---|---|---|---|---|
| Sign-up und Discovery | Organisationsgrundlagen, Quellen, Grenzen und offene Fragen strukturiert erfassen und prüfen | Onboarding, Organisationsprofil, Vorbereitung des Company Brain | Begrenzte Umsetzung; Pilotqualifikation läuft weiter | Eine nachvollziehbare Discovery- und Review-Journey; keine Zusage universeller Integrationen oder vollständiger Live-Onboarding-Reife |
| Company Brain | Versionierten, geprüften institutionellen Kontext bereitstellen | Kundenantworten, Entscheidungsvorlagen, organisationsbezogene Arbeit | Aktive versionierte Grundlage; begrenzte Produkt- und Runtime-Integration | Eine kontrollierte Kontextgrundlage; kein Modellgedächtnis, Agent oder Ausführungsrecht |
| `/work` | Vorgänge, Quellen, nächste Schritte und erforderliche Entscheidungen zusammenführen | Tagesarbeit, Fallbearbeitung, Arbeitskoordination | Begrenzte Umsetzung; aktive Weiterentwicklung | Eine materialisierte institutionelle Arbeitsfläche; nicht jede Journey ist bereits live Ende zu Ende qualifiziert |
| Needs You | Erforderliche menschliche Mitwirkung sichtbar machen | Freigaben, Rückfragen, blockierte Entscheidungen | Etablierte Kernsemantik; begrenzte Umsetzung | Eine materialisierte Beteiligungs- und Aufmerksamkeitsprojektion; Einordnung allein ist kein Dringlichkeits- oder Autoritätssignal |
| Chat und Quickactions | Fragen klären, Arbeit verfeinern und begrenzte nächste Schritte anbieten | Recherchefragen, Entwurfsarbeit, Navigation, kontextbezogene Vorbereitung | Begrenzte Umsetzung | Unterstützung innerhalb des aktuellen Kontexts; Sichtbarkeit oder Klick einer Aktion bedeutet nicht Ausführbarkeit |
| Personal Realm und Companion | Persönliche Kontinuität, Erinnerung, Ideation und Beitragsvorbereitung getrennt vom Company Brain halten | Arbeit wiederaufnehmen, Gedanken entwickeln, persönlichen Beitrag vorbereiten | Etablierte Contract-Semantik; produktseitig begrenzt umgesetzt | Persönliche Kontinuität und bestätigungsgebundene Beitragsvorbereitung; keine autonome Übergabe oder allgemeine Personal-Runtime-Aktivierung behauptet |
| Today, Resume und geräteübergreifende Kontinuität | Einen bewussten Neustartpunkt, stabilen Fokus, veraltete Snapshots und fortbestehende Pausen korrekt abbilden | Mobiler Tagesstart, Session-Fortsetzung, Gerätewechsel | Begrenzte Umsetzung | Wiederaufnahme mit klarer Aktualitätsgrenze; Continuity überträgt keine Authority und löst keine automatische Wiederholung aus |
| Native Arbeitsflächen | Institutionelle und persönliche Projektionen auf nativen Oberflächen konsistent darstellen | Desktop-Arbeit, mobile Fallbearbeitung, Personal Hub | Cross-Surface-Contract-Baseline materialisiert; repräsentative E2E-Qualifikation offen | Gemeinsame Produktgrammatik mit serverseitiger Authority; Clientzustand bleibt Projektion und erzeugt keine eigene Wahrheit |
| Lokale Runtime-Grenze | Freigegebene lokale Ressourcen kontrolliert erreichbar machen | Lokaler Kontextzugriff, begrenzte systemnahe Arbeit | Begrenzte Umsetzung | Kontrollierte Nähe zu Daten und Wirkung; Erreichbarkeit ist weder Lese- noch Ausführungserlaubnis |

## Kernfähigkeiten des Arbeitsflusses

| Schritt | Capability | Use Cases | Aktueller Status | Grenze |
|---|---|---|---|---|
| **KNOW** | Zweckgebundenen, aktuellen und nachvollziehbaren Kontext bereitstellen | Kundenanliegen verstehen, Entscheidung vorbereiten, Arbeit fortsetzen | Etablierte Architektur; begrenzte Umsetzung | Mehr Kontext erzeugt keine zusätzlichen Rechte |
| **THINK** | Optionen analysieren sowie Entwürfe und Vorschläge erstellen | Antwortentwurf, Zusammenfassung, Plan, Rückfragen | Etablierte Semantik; begrenzte Produktintegration | Ein Modelloutput bleibt ein Vorschlag und besitzt keine institutionelle Wahrheit |
| **Govern** | Richtlinien, Authority und erforderliche menschliche Entscheidung trennen und prüfen | Freigeben, ablehnen, zurückfragen, stoppen | Etablierte Architektur; begrenzte Umsetzung | Approval ist weder Grant noch Ausführung |
| **ACT** | Nur eine aktuell erlaubte, begrenzte Wirkung ausführen | Kontrollierter Versand oder begrenzte Änderung in einem zugelassenen Pfad | Begrenzte Runtime-Umsetzung; live gegatet | Keine breite autonome Softwaresteuerung oder allgemeine Produktionsreife behauptet |
| **PROVE** | Ausführungsevidenz, Verifikation und Reconciliation unterscheidbar halten | Zustellung prüfen, unklaren Ausgang klären, Doppelwirkung vermeiden | Etablierte Semantik; begrenzte Runtime- und Testqualifikation | Receipt ist nicht Geschäftsergebnis; ein unklarer Ausgang erlaubt keinen blinden Retry |
| Modellwahl und Kognition | Austauschbare Modelle und qualifizierte Verarbeitungsrouten innerhalb unveränderter Grenzen nutzen | Entwerfen, analysieren, geeignete Kognitionsintensität wählen | Routing- und Resolution-Evidence-Verträge begrenzt materialisiert; Runtime-Nutzung separat gegatet | Modellalias, gewählte Route oder stärkeres Modell erzeugen weder zusätzliche Authority noch Datenfreigabe |

## Begrenzte Pilotfähigkeitsfamilien

Die aktuelle Pilotvorbereitung materialisiert mehrere klar begrenzte Fähigkeitsfamilien. Die folgende Darstellung abstrahiert bewusst von internen Operationsnamen, Anbietern und Bindungsdetails.

| Fähigkeitsfamilie | Öffentliche Erwartung | Reifegrenze |
|---|---|---|
| Betriebs- und Verfügbarkeitsinformationen lesen | Aktuelle, zugelassene Betriebsinformationen für einen Vorgang heranziehen | reale Quelle, Tenant-/Ressourcenzugriff und Aktualität bleiben Voraussetzungen |
| Buchungsbezogene Vorgänge | Buchungen innerhalb eines zugelassenen Pfads vorbereiten, anlegen, ändern oder stornieren | schreibende Wirkung bleibt policy-, authority-, evidence- und live-gategesteuert |
| Kalenderarbeit | Verfügbarkeit lesen sowie freigegebene Terminänderungen kontrolliert ausführen | externe Zulassung und aktuelle Berechtigung bleiben separat erforderlich |
| Externe Kommunikation | Nachrichten vorbereiten und nur über einen gültigen Wirkungspfad versenden | Versandnachweis ist nicht automatisch Zustellung oder Geschäftserfolg |
| Erinnerungen und Fristen | Interne Folgearbeit aus hinreichend eindeutigem Kontext vorbereiten oder erzeugen | keine allgemeine Aufgaben- oder Softwaresteuerung |
| Wissenszugriff | Zugelassene Wissensquellen durchsuchen und lesen | read-only bedeutet nicht globale Datenfreigabe; Herkunft und Aktualität bleiben relevant |
| Ergebnisnachweis und Recovery | Wirkung, Receipt, Verifikation und Reconciliation getrennt halten | unklarer Ausgang bleibt unklar und erlaubt keinen blinden Retry |

Diese Fähigkeitsfamilien sind kein Servicekatalog und keine Aussage, dass jede Familie im konkreten Betrieb bereits live zugelassen ist.

## Use-Case-Matrix

| Use Case | Unterstützte Funktionen | Erwartbares Ergebnis | Öffentliche Reife |
|---|---|---|---|
| Kundenantwort vorbereiten | Company Brain, KNOW, THINK, `/work`, Chat | Nachvollziehbarer Entwurf mit Quellen, Annahmen und offenen Punkten | Begrenzte Umsetzung; ein realer Live-Versand wird nicht allgemein zugesagt |
| Entscheidungsvorlage erstellen | KNOW, THINK, Govern, Needs You | Strukturierte Optionen und eine sichtbare menschliche Entscheidung | Etablierte Semantik; begrenzte Produktumsetzung |
| Organisationskontext aufbauen | Sign-up, Discovery, Company Brain | Prüfbare Grundlagen, bevor Kontext institutionell aktiv genutzt wird | Aktive versionierte Grundlage und begrenzte Journey-Umsetzung |
| Arbeit wiederaufnehmen | Personal Realm, Companion, Today, Resume | Letzter nachvollziehbarer Stand, offene Fragen und nächster sinnvoller Schritt | Begrenzte produktseitige Umsetzung; keine allgemeine Live-Verfügbarkeit über alle Geräte behauptet |
| Begrenzte externe Wirkung | Govern, ACT, PROVE | Erlaubte Wirkung oder nachvollziehbarer Stopp mit Evidenz | Begrenzte Runtime-Umsetzung; Pilotvorbereitung und externe Live-Gates offen |
| Unklaren Ausgang klären | PROVE, Reconciliation, menschlicher Takeover | Status bleibt sichtbar, bis ausreichende Evidenz vorliegt | Kernsemantik und begrenzte Recovery-Pfade materialisiert; reale externe Qualifikation bleibt separat |
| Lokale oder Remote-Kognition nutzen | KNOW, THINK, Modellwahl, lokale Kontrollgrenze | Zweckgebundene Verarbeitung geeigneten Kontexts | Begrenzte Architektur und Integration; Datenfreigabe und Authority bleiben separat gegatet |

## Aussagegrenze

Die Matrix ist eine öffentliche Erwartungslandkarte, kein Servicekatalog, SLA,
Capability Grant oder Nachweis von Produktionsreife. Statusangaben sind bewusst
grob. Materialisierung, externe Live-Bereitschaft, Pilotaktivierung und
Produktion werden getrennt bewertet.

Siehe auch [aktueller öffentlicher Stand](current-state.md),
[Pilot und Produktionsreife](pilot-production-readiness.md) und
[Public Source Assurance](../reference/source-basis.md).

---

[← Vorherige: Aktueller öffentlicher Stand](current-state.md) · [Index](../README.md) · [Nächste: Architektur-Baseline →](bootstrap-materialization.md)
