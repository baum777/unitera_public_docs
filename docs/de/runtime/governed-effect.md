# Kontrollierte externe Wirkung

**Status:** ESTABLISHED architecture; exakte Runtime-Verfügbarkeit hängt von der zuständigen Implementierungsoberfläche ab.

UNITERA trennt Approval, Grant, externe Ausführung, Receipt und Verifikation. Externe Wirkungen dürfen nicht direkt aus der Cognition heraus ausgeführt werden.

```mermaid
sequenceDiagram
    participant AI as Cognition / Agent
    participant EC as Execution Control
    participant H as Menschliche Kontrolle
    participant X as Trusted Executor
    participant P as Externer Provider
    participant A as Audit / Evidenz

    AI->>EC: Action Proposal / Capability Request
    EC->>EC: Tenant-, Policy- und Autonomiebewertung
    alt menschliche Kontrolle erforderlich
        EC->>H: Review- / Approval-Anfrage
        H-->>EC: Approval-Entscheidung
    end
    EC->>EC: Capability Grant + erneute Prüfung vor Dispatch
    EC->>X: Autorisierte Ausführungsanfrage
    X->>P: Externe Wirkung
    P-->>X: Provider-Antwort
    X-->>EC: Receipt
    EC->>A: Evidenz anhängen
    EC->>EC: Ergebnis verifizieren / abgleichen
```

## v1-Wirkungsgrenze

Die etablierte technische Referenz für die einzelne begrenzte externe v1-Capability ist `email.send.commit`. Um sie herum können umfassendere Geschäftsabläufe komponiert werden; Namen von Workflows dürfen jedoch nicht stillschweigend zu neuen atomaren Capabilities werden.

## Fehlerregel

Ein unbekanntes externes Ergebnis ist keine Erlaubnis für einen blinden Retry. Das System muss unsichere Wirkungen abgleichen, bevor es entscheidet, ob ein weiterer Versuch sicher ist.

