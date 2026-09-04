# Funktionen, Capabilities und Use Cases

**Disclosure:** PUBLIC_CORE · PUBLIC_ABSTRACTED · PUBLIC_STATUS
**Stand:** 4. September 2026

Diese Seite übersetzt die öffentliche UNITERA-Architektur in konkrete
Produktfähigkeiten und Anwendungssituationen. **Capability** bezeichnet hier
eine öffentlich erklärte Produktfähigkeit — nicht einen formalen Capability
Grant oder eine Ausführungserlaubnis.

## Status lesen

| Status | Bedeutung |
|---|---|
| **Etabliert** | Die Semantik oder Architektur ist fest beschrieben. Das bedeutet nicht automatisch vollständige Produktverfügbarkeit. |
| **Begrenzte Umsetzung** | Nachweisbare Teile sind umgesetzt; daraus folgt keine allgemeine Ende-zu-Ende-Reife. |
| **Aktive Entwicklung** | Das Produkterlebnis wird materialisiert und kann noch unvollständig sein. |
| **Vertrags- und Produktrichtung** | Der fachliche Rahmen ist beschrieben; Runtime- und produktive Nutzung bleiben separat gegatet. |
| **Owner-bestätigter Kandidat** | Die Richtung ist bestätigt, aber noch nicht vollständig kanonisch adoptiert. |
| **Pilotvorbereitung** | Ein begrenzter Pilot wird vorbereitet, ist durch diese Dokumentation aber nicht aktiviert. |
| **Absichtlich begrenzt** | Wirkung ist auf nachgewiesene, kontrollierte Pfade beschränkt; breite Autonomie wird nicht behauptet. |

## Produktfunktionen

| Funktion | Öffentliche Capability | Typische Use Cases | Aktueller Status | Was man öffentlich erwarten kann |
|---|---|---|---|---|
| Sign-up und Discovery | Organisationsgrundlagen, Quellen, Grenzen und offene Fragen strukturiert erfassen und prüfen | Onboarding, Organisationsprofil, Vorbereitung des Company Brain | Aktive Entwicklung; institutionelles Wissen in begrenzter Form umgesetzt | Eine nachvollziehbare Discovery-Journey; keine Zusage universeller Integrationen oder vollständiger Live-Onboarding-Reife |
| Company Brain | Versionierten, geprüften institutionellen Kontext bereitstellen | Kundenantworten, Entscheidungsvorlagen, organisationsbezogene Arbeit | Begrenzte Umsetzung | Eine kontrollierte Kontextgrundlage; kein Modellgedächtnis, Agent oder Ausführungsrecht |
| `/work` | Vorgänge, Quellen, nächste Schritte und erforderliche Entscheidungen zusammenführen | Tagesarbeit, Fallbearbeitung, Arbeitskoordination | Aktive Entwicklung | Die primäre institutionelle Arbeitsoberfläche als Produktmodell; nicht jede Journey ist bereits Ende zu Ende qualifiziert |
| Needs You | Erforderliche menschliche Mitwirkung sichtbar machen | Freigaben, Rückfragen, blockierte Entscheidungen | Etablierte Kernsemantik; Produkterlebnis in aktiver Entwicklung | Eine Beteiligungswarteschlange; Einordnung allein ist kein Dringlichkeits- oder Autoritätssignal |
| Chat und Quickactions | Fragen klären, Arbeit verfeinern und begrenzte nächste Schritte anbieten | Recherchefragen, Entwurfsarbeit, Navigation, kontextbezogene Vorbereitung | Aktive Entwicklung; neuere Surface-Details sind Owner-bestätigte Kandidaten | Unterstützung innerhalb des aktuellen Kontexts; Sichtbarkeit einer Aktion bedeutet nicht Ausführbarkeit |
| Personal Realm und Companion | Persönliche Kontinuität, Erinnerung, Ideation und Beitragsvorbereitung getrennt vom Company Brain halten | Arbeit wiederaufnehmen, Gedanken entwickeln, persönlichen Beitrag vorbereiten | Vertrags- und Produktrichtung | Einen klar beschriebenen persönlichen Bereich; keine Behauptung aktivierter Personal-Realm-Runtime oder autonomer Übergabe |
| Today, Resume und geräteübergreifende Kontinuität | Einen bewussten Neustartpunkt, stabilen Fokus und fortbestehende Pausen abbilden | Mobiler Tagesstart, Session-Fortsetzung, Gerätewechsel | Owner-bestätigter Kandidat | Eine Produkt-Richtung mit expliziten Grenzen; die vollständige kanonische Adoption steht noch aus |
| Lokale Runtime-Grenze | Freigegebene lokale Ressourcen kontrolliert erreichbar machen | Lokaler Kontextzugriff, begrenzte systemnahe Arbeit | Begrenzte Architektur und Umsetzung | Kontrollierte Nähe zu Daten und Wirkung; Erreichbarkeit ist weder Lese- noch Ausführungserlaubnis |

## Kernfähigkeiten des Arbeitsflusses

| Schritt | Capability | Use Cases | Aktueller Status | Grenze |
|---|---|---|---|---|
| **KNOW** | Zweckgebundenen, aktuellen und nachvollziehbaren Kontext bereitstellen | Kundenanliegen verstehen, Entscheidung vorbereiten, Arbeit fortsetzen | Etablierte Architektur; begrenzte Umsetzung | Mehr Kontext erzeugt keine zusätzlichen Rechte |
| **THINK** | Optionen analysieren sowie Entwürfe und Vorschläge erstellen | Antwortentwurf, Zusammenfassung, Plan, Rückfragen | Etablierte Semantik; Produkterlebnis in aktiver Entwicklung | Ein Modelloutput bleibt ein Vorschlag und besitzt keine institutionelle Wahrheit |
| **Govern** | Richtlinien, Authority und erforderliche menschliche Entscheidung trennen und prüfen | Freigeben, ablehnen, zurückfragen, stoppen | Etablierte Architektur; begrenzte Umsetzung | Approval ist weder Grant noch Ausführung |
| **ACT** | Nur eine aktuell erlaubte, begrenzte Wirkung ausführen | Kontrollierter Versand oder begrenzte Änderung in einem zugelassenen Pfad | Absichtlich begrenzt | Keine breite autonome Softwaresteuerung oder allgemeine Produktionsreife behauptet |
| **PROVE** | Ausführungsevidenz, Verifikation und Reconciliation unterscheidbar halten | Zustellung prüfen, unklaren Ausgang klären, Doppelwirkung vermeiden | Etablierte Semantik; Ende-zu-Ende-Qualifikation begrenzt | Receipt ist nicht Geschäftsergebnis; ein unklarer Ausgang erlaubt keinen blinden Retry |
| Modellwahl und Kognition | Austauschbare Modelle innerhalb unveränderter Grenzen nutzen | Entwerfen, analysieren, geeignete Kognitionsintensität wählen | Begrenzte Architektur; erweiterte Remote-Richtung als Owner-bestätigter Kandidat | Stärkeres oder anderes Modell erzeugt keine zusätzliche Authority oder Datenfreigabe |

## Use-Case-Matrix

| Use Case | Unterstützte Funktionen | Erwartbares Ergebnis | Öffentliche Reife |
|---|---|---|---|
| Kundenantwort vorbereiten | Company Brain, KNOW, THINK, `/work`, Chat | Nachvollziehbarer Entwurf mit Quellen, Annahmen und offenen Punkten | Begrenzte Umsetzung und aktive Entwicklung; ein Live-Versand wird nicht allgemein zugesagt |
| Entscheidungsvorlage erstellen | KNOW, THINK, Govern, Needs You | Strukturierte Optionen und eine sichtbare menschliche Entscheidung | Etablierte Semantik, Produkterlebnis in aktiver Entwicklung |
| Organisationskontext aufbauen | Sign-up, Discovery, Company Brain | Prüfbare Grundlagen, bevor Kontext institutionell aktiv genutzt wird | Institutionelles Wissen begrenzt umgesetzt; Journey in aktiver Entwicklung |
| Arbeit wiederaufnehmen | Personal Realm, Companion, Today, Resume | Letzter nachvollziehbarer Stand, offene Fragen und nächster sinnvoller Schritt | Vertrags- und Produktrichtung; erweiterte Surface-Kontinuität ist Kandidat |
| Begrenzte externe Wirkung | Govern, ACT, PROVE | Erlaubte Wirkung oder nachvollziehbarer Stopp mit Evidenz | Absichtlich begrenzt; Pilotvorbereitung |
| Unklaren Ausgang klären | PROVE, Reconciliation, menschlicher Takeover | Status bleibt sichtbar, bis ausreichende Evidenz vorliegt | Kernsemantik etabliert; produktübergreifende Qualifikation begrenzt |
| Lokale oder Remote-Kognition nutzen | KNOW, THINK, Modellwahl, lokale Kontrollgrenze | Zweckgebundene Verarbeitung geeigneten Kontexts | Begrenzte Architektur; erweiterte Betriebsrichtung ist Kandidat |

## Aussagegrenze

Die Matrix ist eine öffentliche Erwartungslandkarte, kein Servicekatalog, SLA,
Capability Grant oder Nachweis von Produktionsreife. Statusangaben sind bewusst
grob. Details können je Produktpfad variieren und werden erst nach aktueller
Verifikation höher eingestuft.

Siehe auch [aktueller öffentlicher Stand](current-state.md),
[Pilot und Produktionsreife](pilot-production-readiness.md) und
[Public Source Assurance](../reference/source-basis.md).

---

[← Vorherige: Aktueller öffentlicher Stand](current-state.md) · [Index](../README.md) · [Nächste: Architektur-Baseline →](bootstrap-materialization.md)
