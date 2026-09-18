# Public Source Assurance

Status: `PUBLIC_ABSTRACTED`

**Stand der Quellenprüfung:** 18. September 2026

Öffentliche Aussagen werden vor Publikation gegen zuständige, aktuelle Owner-Quellen geprüft. Aktuelle Owner-Quellen schlagen ältere Ableitungen; Kandidaten und externe Konzepte bleiben klar gekennzeichnet.

## Prüfmodell

| Quellenklasse | Öffentliche Assurance |
|---|---|
| Semantik- und Contract-Owner | aktueller kanonischer Stand verifiziert |
| Produkt- und Runtime-Materialisierung | aktueller kanonischer Stand verifiziert und abstrahiert |
| Governance- und Control-Quellen | aktueller kanonischer Stand verifiziert und abstrahiert |
| Registry- und Kartographieprojektionen | auf Kohärenz geprüft; möglicher zeitlicher Projection-Lag berücksichtigt |
| Nicht zusammengeführte Kandidaten | nicht als aktueller Istzustand gezählt |
| Ältere Source-Candidates und Ableitungen | nur Kontext; sie überschreiben keinen neueren Owner-Zustand |
| Externe Konzepte | separat attribuiert |

## Reconciliation-Regel

Eine abgeleitete Projektion kann hinter einem bereits kanonischen Owner-Zustand liegen. In diesem Fall gilt:

```text
Current owner source
> derived projection
> older source candidate
> historical summary
```

Der zeitliche Nachlauf einer Registry-, Kartographie- oder Dokumentationsprojektion ist deshalb selbst ein Audit-Signal, aber keine neue Authority und kein Grund, einen verifizierten Owner-Zustand zurückzustufen.

Offene oder nicht zusammengeführte Änderungen werden umgekehrt nicht vorzeitig hochgestuft. Sie dürfen nur als Kandidaten beschrieben werden, bis die zuständige Owner-Quelle ihren Status trägt.

Exakte Repositories, Commits, Branches, Change-IDs, Contract-Pfade und Runtime-Bindings werden intern geprüft, aber nicht als öffentliches Evidence-Ledger aggregiert.

```text
Public explainability != source completeness
Public provenance != exact internal topology
Projection freshness != authority
Candidate evidence != current canonical state
```

---

[← Vorherige: Architektur-Baseline](../status/bootstrap-materialization.md) · [Index](../README.md) · [Nächste: Systemüberblick →](../architecture/system-overview.md)
