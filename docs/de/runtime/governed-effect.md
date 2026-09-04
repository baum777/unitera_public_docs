# Kontrollierte Wirkung

Status: `PUBLIC_CORE`

```mermaid
flowchart LR
    P["Vorschlag"] -->|"angefragte Wirkung"| A["Authority- und Richtlinienprüfung"]
    A -->|"menschliche Kontrolle, falls erforderlich"| E["Autorisierte Ausführung"]
    E -->|"begrenzte externe Wirkung"| X["Externes System"]
    X -->|"Receipt"| V["Verifikation oder Reconciliation"]
    V -->|"prüfbare Evidenz"| R["Nachvollziehbares Ergebnis"]
```

Approval ist nicht Ausführung, Receipt ist nicht Verifikation und ein unbekanntes Ergebnis ist keine Einladung zum blinden Retry. Reale Wirkung bleibt absichtlich eng begrenzt.

> Conceptual public projection — not deployment, service, repository, protocol or security topology.

---

[← Vorherige: Modell- und Provider-Unabhängigkeit](model-and-provider-independence.md) · [Index](../README.md) · [Nächste: Lokale Runtime-Grenze →](local-runtime-node.md)
