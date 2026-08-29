# Systemübersicht

**Status:** PUBLIC PROJECTION  
**Autorität:** keine aus sich selbst heraus

UNITERA trennt Organisationswissen, Kognition und externe Handlung, damit leistungsfähigeres KI-Reasoning nicht unbemerkt geschäftliche Autorität erweitert.

```mermaid
flowchart TB
    subgraph KNOW[KNOW — Context Runtime]
      E[Evidenz]
      CB[Company Brain]
      C[Kompilierter Kontext]
      E --> CB --> C
    end

    subgraph THINK[THINK — Cognition Runtime]
      AN[Analyse]
      PL[Planung / Neuplanung]
      AP[Action Proposal]
      AN --> PL --> AP
    end

    subgraph ACT[ACT — Execution Control]
      CR[Capability Request]
      PE[Policy und effektive Autonomie]
      HC[Menschliche Kontrolle, falls erforderlich]
      GR[Capability Grant]
      EX[Trusted Executor]
      CR --> PE --> HC --> GR --> EX
    end

    C --> AN
    AP --> CR
    EX --> XS[Externes System]
    XS --> RC[Receipt]
    RC --> VR[Verifikation / Abgleich]
```

## Systemthese

UNITERA lässt sich als **evidenzbasierte, kontextkompilierte und autoritätsgetrennte Ausführung** zusammenfassen.

Die Architektur behandelt weder Modell, Prompt, Harness, externes Werkzeug noch Adapter als Autoritätsgrenze. Autorität bleibt in den zuständigen Domänen und in der Runtime-Erzwingung explizit.

