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

Approval ist kein Grant und keine Ausführung, Receipt ist nicht Verifikation und ein unbekanntes Ergebnis ist keine Einladung zum blinden Retry. Reale Wirkung bleibt absichtlich eng begrenzt.

Wenn menschliche Kontrolle erforderlich ist, zählt die aktuell belegte und
für genau diese Entscheidung berechtigte Person. Unterschiedliche Accounts
beweisen keine unabhängigen Menschen. Eine positive Kontrollbewertung ist kein
Grant; eine materielle Änderung des Vorschlags oder der geltenden Regeln
erfordert eine neue Bewertung. Siehe [Identity, Human Control und
Authority](../architecture/identity-human-control-and-authority.md).

> Conceptual public projection — not deployment, service, repository, protocol or security topology.

---

[← Vorherige: Modell- und Provider-Unabhängigkeit](model-and-provider-independence.md) · [Index](../README.md) · [Nächste: Lokale Runtime-Grenze →](local-runtime-node.md)
