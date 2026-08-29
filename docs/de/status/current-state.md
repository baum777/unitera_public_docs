# Aktueller öffentlicher Stand — 29.08.2026

**Status:** PUBLIC SNAPSHOT — beschreibend, nicht autoritativ  
**Autorität:** keine aus sich selbst heraus  
**Quellengrundlage:** exakte Refs in `PUBLICATION_MANIFEST.yaml`, Remote-Branch-Vergleich und bereitgestelltes Quellen-Abgleichsmaterial vom 15.08.2026

## Gesamtergebnis

`PARTIAL` — UNITERA besitzt einen materiell implementierten kontrollierten Kern. Self-Service-Onboarding, kanonisches Discovery, vollständige Cognition Runtime und produktive End-to-End-Qualifikation sind noch unvollständig.

## Kanonischer Status der Owner-Repositories

| Oberfläche | Evidenz | Bewertung | Öffentliche Einordnung |
|---|---|---|---|
| Foundation und Company Brain | `coreos@3f23e2f` | **pass** | Aktive Founder-Baseline, deterministische Prime-Projektion, Review-/Promotion-Verträge, Governance-Validierung und CI liegen beim Owner-Repository. |
| Providerneutrale Execution Control | `unitera-os@18c50f8` | **pass** | Capability-, Grant-, Receipt-, Policy- und Execution-Control-Verträge sind hier kanonisch; Build, Tests, Typecheck und Konformität laufen in CI. |
| Tenant- und Governance-Autorität | `unitera_control_plane@10e2a39` | **pass / partial downstream** | Physischer Owner, Zuordnungstopologie, Contract v3 und Pilot-Policy sind materialisiert; Qualifikation der Consumer-Runtime bleibt separat. |
| Produkt-/Runtime-Consumer | `Unitera_Systems@786d03c` | **partial** | Gehostete Authentifizierung, Authority Runtime, Persistenz, APIs, Produktoberflächen und begrenzte Execution Controls existieren; nicht jeder umfassendere UNITERA-Lifecycle ist kanonisch oder produktiv qualifiziert. |
| Repository-übergreifende Registry | `unitera-registry@a2f4cca` | **pass as reference layer** | Schema `1.1.0`, Offline-Validierung und Erreichbarkeitserzwingung sind materialisiert; die Registry bleibt nichtautoritativ. |

## Status der Product Journey

```mermaid
flowchart LR
    A[Gehostetes Sign-in<br/>MATERIALIZED] --> B[Profil<br/>OPEN]
    B --> C[Tenant-Bootstrap<br/>OPEN]
    C --> D[Discovery<br/>QUALIFIED BRANCH]
    D --> E[Aktivierung und First Work<br/>PARTIAL]
    E --> F[/work<br/>PARTIAL]
```

| Journey-Schritt | Bewertung | Grundlage |
|---|---|---|
| Gehostetes OIDC-Sign-in und opake Session | **pass** | Kanonische Routen, Session Service, interne IdP-Bindings, Membership-abgeleitete Rolle, RLS-bewusste Auflösung und signierter BFF-Proxy. |
| Öffentliches Sign-up | **missing** | Kein kanonischer produktionsreifer Self-Service-Lifecycle belegt. |
| Persönliches Profil | **missing** | Kein verpflichtender Profilabschlussvertrag und keine Übergabe belegt. |
| Tenant-Bootstrap/-Auswahl | **partial / blocked for self-service** | Tenant-Autorität existiert; öffentliches Self-Service-Ownership und initialer Membership-Fluss sind jedoch nicht geschlossen. |
| Discovery Runtime | **partial** | Auf Branch `7f7a3b3` qualifiziert, 11 Commits vor kanonischem `main`; weder gemergt noch produktiv aktiv. |
| First Work und `/work` | **partial** | Work-first-Richtung und mehrere Read-Model-/Produktoberflächen existieren; die vollständige Journey von Aktivierung zu First Work hängt weiterhin von kanonischer Lifecycle-Integration ab. |

## Runtime-Status

| Runtime | Bewertung | Grenze |
|---|---|---|
| KNOW / Company-Brain-Consumption | **partial to materialized** | Owner Truth verbleibt in `coreos`; Runtime-Consumption muss integritätsgebunden bleiben. |
| THINK / Cognition | **partial** | Compute-Envelope-Vertrag ist auf `main`; vollständige Root-/Child-Run-Admission, Lifecycle, Ledger, Memory und Produktions-Backend bleiben offen. |
| ACT / kontrollierte Wirkung | **materialized bounded core** | `email.send.commit` bleibt die einzelne begrenzte v1-Wirkungsreferenz; umfassendere Integrationen erweitern diese Grenze nicht stillschweigend. |
| Local Runtime Node | **candidate** | Keine kanonische Runtime-Aktivierung. |

## Explizite Nichtaussagen

Dieser Snapshot behauptet nicht:

- einen produktionsreifen öffentlichen Sign-up- und Onboarding-Funnel;
- Discovery auf kanonischem `Unitera_Systems/main`;
- produktives Deployment oder Kundenerreichbarkeit des Branch-qualifizierten Discovery Slice;
- vollständige Aktivierung der Cognition Runtime;
- unbeschränkte Autonomie;
- automatische regulatorische Compliance oder Zertifizierung.

## Nächstes dokumentarisches Gate

Dieser Snapshot wird aktualisiert, sobald sich einer der folgenden Punkte kanonisch ändert: Self-Service-Identity-/Profil-/Tenant-Verträge, Discovery-Merge, deployter End-to-End-Onboarding-Nachweis, Admission/Lifecycle der Cognition Runtime oder Registry-Bindings für diese materiellen Änderungen.

