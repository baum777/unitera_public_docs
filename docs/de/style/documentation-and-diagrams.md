# Dokumentations- und Diagrammkonventionen

**Status:** lokale Publikationskonvention dieses Repositories  
**Autorität:** gilt ausschließlich für dieses öffentliche Projektions-Repository

## Dokumentkopf

Jede Architektur- oder Statusseite soll mit einer kompakten Statusdeklaration beginnen:

```text
Status: PUBLIC PROJECTION | ESTABLISHED | MATERIALIZED | CANDIDATE | OPEN
Authority: none by itself
Source basis: owning repo / frozen source / candidate source
```

`PUBLIC PROJECTION` beschreibt die Rolle des Dokuments. Es erhöht nicht den Reifegrad der darin beschriebenen Architektur.

## Technisches Vokabular

Kanonische technische Bezeichner und ihre Schreibweise bleiben erhalten:

- `UNITERA`
- `Unitera_Systems`
- `coreos`
- `unitera-os`
- `KNOW`
- `THINK`
- `ACT`
- `Company Brain`
- `Action Proposal`
- `Capability Request`
- `Capability Grant`
- `Receipt`
- `Verification`
- `email.send.commit`

Keine Aliasse für autoritätstragende Bezeichner erfinden.

## Mermaid-Konventionen

Diese Regeln sind für dieses Repository verbindlich. Der sprachneutrale Vertrag steht in [`MERMAID.md`](../../../MERMAID.md). Renderer der Aufzeichnung ist GitHub-natives Mermaid gemäß [Creating Mermaid diagrams on GitHub](https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams).

GitHub-natives Mermaid in Markdown verwenden. Nicht auf lokale oder Drittanbieter-Mermaid-Plugins verlassen; GitHub weist ausdrücklich darauf hin, dass solche Plugins gegenüber der GitHub-Syntax Fehler erzeugen können.

### Fence

Backtick-Fence mit Sprachkennung `mermaid` verwenden. Nicht `~~~mermaid` verwenden.

````markdown
```mermaid
flowchart LR
    A[Quelle] --> B[Bewertung]
```
````

### Flussdiagramme

Für Lifecycle- oder grenzüberschreitende Bewegungen `flowchart LR`, für geschichtete Architektur `flowchart TB` verwenden.

```mermaid
flowchart LR
    A[Quelle] --> B[Bewertung]
    B --> C[Entscheidung]
```

### Sequenzdiagramme

`sequenceDiagram` verwenden, wenn Reihenfolge der Akteure und Request-/Response-Semantik wesentlich sind.

```mermaid
sequenceDiagram
    participant A as Agent
    participant G as Governance
    participant X as Executor
    A->>G: Vorschlag
    G->>X: Autorisierte Anfrage
    X-->>G: Receipt
```

### Labels und GitHub-Parserfallen

Jede Knoten- oder Subgraph-Beschriftung in doppelte Anführungszeichen setzen, die `/`, `\\`, `<`, `>`, `#`, `;`, Anführungszeichen, Klammern oder einen Zeilenumbruch enthält. Innerhalb des Labels `<br>` verwenden, niemals `<br/>`.

```mermaid
flowchart LR
    A["Gehostetes Sign-in<br>MATERIALIZED"] --> B["/work"]
```

Unzitiertes `X[/work]` ist ungültig: `[/ ...]` startet die Parallelogramm-Formsyntax und zerlegt das Diagramm auf GitHub.

Niemals `end`, `subgraph`, `graph` oder `flowchart` als Knoten-ID verwenden. Keine `click`-Handler, kein `%%{init: ...}%%` und Farbe nicht als einzigen Träger von Autorität, Risiko oder Reifegrad nutzen.

### Grenznotation

- Durchgezogener Pfeil `-->`: normaler Daten- oder Kontrollfluss.
- Gepunkteter Pfeil `-.->`: erklärende Referenzbeziehung oder ausdrücklich beschriftetes Verbot des Autoritätsrückflusses.
- Subgraphs für KNOW/THINK/ACT oder klare Vertrauens-/Ownership-Domänen verwenden.
- Autorität, Risiko oder Reifegrad nicht allein durch Farbe codieren.

## Regeln für öffentliche Formulierungen

Bevorzugen:

- „abgeglichene Quellenrichtung“ statt „fertige Architektur“, solange die Adoption unvollständig ist;
- „Kandidat“, wenn die Quelle ausdrücklich `CANDIDATE` klassifiziert;
- „in der zuständigen Runtime materialisiert“ nur bei Verifikation;
- „Receipt“ und „Verification“ als getrennte Konzepte;
- „Registry-Referenz“ statt „Registry-Autorität“.

Unverifizierte Aussagen über Production Readiness, Compliance, Zertifizierung, Kundennachweis oder autonome Erlaubnis vermeiden.
