# Mitwirken

Dieses Repository ist eine öffentliche Projektion der UNITERA-Architektur. Beiträge müssen Quellenautorität und Statusunterscheidungen bewahren.

## Vor der Bearbeitung

1. Zuständige Domäne und Quellartefakt bestimmen.
2. Aussage als `ESTABLISHED`, `MATERIALIZED`, `CANDIDATE` oder `OPEN` klassifizieren.
3. Diagramme und Zusammenfassungen dem Kopieren interner Quelltexte vorziehen.
4. Exakte technische Bezeichner wie `email.send.commit`, `KNOW`, `THINK`, `ACT` und Namen der Autoritätsdomänen unverändert lassen.
5. Niemals einen Kandidaten allein durch Dokumentation zu einer kanonischen Aussage machen.
6. Inhaltliche Änderungen synchron in `docs/de` und `docs/en` ausführen.

## Diagrammstil

GitHub-natives Mermaid in Markdown verwenden. [`MERMAID.md`](../../../MERMAID.md) beachten. Explizite Lifecycle-Pfeile bevorzugen und Vertrauens- sowie Autoritätsgrenzen beschriften, statt sich auf Farbcodierung zu verlassen.

## Änderungen mit besonderem Prüfbedarf

- Autoritätszuständigkeit
- Capability-/Grant-Semantik
- Produktionsaktivierung
- Tenant-Isolation
- externe Wirkungen
- Source-Pointer- und Adoptionsstatus
- Sicherheitsgrenzen
- Compliance- oder Zertifizierungsaussagen
