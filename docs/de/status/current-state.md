# Aktueller öffentlicher Stand — 30.08.2026

**Status:** PUBLIC SNAPSHOT — beschreibend, nicht autoritativ  
**Autorität:** keine aus sich selbst heraus  
**Quellengrundlage:** exakte Refs in `PUBLICATION_MANIFEST.yaml`, verifizierte Owner-/Implementierungs-Repositories, Qualifikationsevidenz offener PRs und bereitgestelltes Source-Reconciliation-Material

## Gesamtergebnis

`PARTIAL` — UNITERA besitzt einen materiell implementierten kontrollierten Kern und mehrere neu qualifizierte Produkt-/Runtime-Slices. Kanonisches Self-Service-Onboarding, kanonische Discovery-Integration, Cognition-Runtime-Admission, Pilot-Owner-Freeze und Production Execution bleiben jedoch gegatet.

## Verifizierter Default-Branch-Stand

| Surface | Evidenz | Bewertung | Öffentliche Einordnung |
|---|---|---|---|
| Foundation und Company Brain | `coreos@c34b61a` | **pass / aktive Owner-Semantik mit offenen Folge-Gates** | Foundation-/Company-Brain-Semantik und die Tenant-Foundation-Consumer-Surface liegen beim Owner-Repository. Die neueste Consumer-Contract-Rematerialisierung ist auf main vorhanden, bleibt aber ausdrücklich proposed/not-frozen. |
| Providerneutrale Execution Control | `unitera-os@18c50f8` | **pass** | Capability-, Policy-, Autonomie-, Grant-, Receipt- und Execution-Control-Verträge sind hier kanonisch; Build, Tests, Typecheck und Conformance sind CI-gegatet. |
| Tenant- und Governance-Autorität | `unitera_control_plane@fc9370e` | **pass / partielle Downstream-Deklaration** | Tenant-/Governance-Autorität und Assignment-Topologie sind materialisiert. Die Registry weist weiterhin eine offene Owner-Deklaration zur aktuellen Runtime-Enforcement-Conformance aus. |
| Produkt-/Runtime-Consumer | `Unitera_Systems@786d03c` | **partial** | Gehostete Authentifizierung, begrenzte Authority-/Runtime-Erzwingung, Persistenz, APIs und Produktoberflächen existieren; neuere Discovery- und Pilot-UI-Integration liegen auf qualifizierten offenen PRs. |
| Semantischer Owner des Personal Realm | `unitera_companion@8dd8112` | **Owner-Foundation gemerged** | Owner Decisions und Architekturfundament des Personal Realm liegen nun auf Owner-`main`. Cross-Repo-Adoption, Runtime-Aktivierung und Production Execution bleiben getrennt und unvollständig. |
| Repository-übergreifende Registry | `unitera-registry@891f9b9` | **pass als Referenz-/Integritätslayer** | RCC-/Digest-Verification-Closure ist gemerged: 188/188 Digest-Assertions klassifiziert, 130 Exact Matches, 58 non-recalculable-by-design, 0 unresolved; Live-Reachability meldete 163 verified, 0 mismatch, 0 unverifiable und 0 record gaps. Die Registry bleibt nichtautoritativ. |
| Production Interface | `unitera-production-interface@d7cbf8c` | **gemergte Product-UI+BFF-Implementierung** | Das dedizierte Production Pilot Interface enthält jetzt den Migration-Closure-Stack plus kontrollierte Profile-/Settings-Surfaces. Es besitzt nur Product-UI-/BFF-Materialisierung; Live Effects und Production Execution bleiben aus. |

## Personal Realm

Der vorherige öffentliche Snapshot sagte noch, Personal-Realm-PR #1 sei offen. Das ist nicht mehr korrekt.

`baum777/unitera_companion` PR #1 wurde am 30.08.2026 gemerged; der Owner-`main`-Merge-Commit lautet `8dd8112a74631516c134bc3fc528d6220cdd27a7`.

~~~text
Owner Decisions = finalisiert
Owner-Repo-Architekturfundament = auf main gemerged
Cross-Repo Adoption = ausstehend
Runtime Activation = keine
Production Execution = nicht autorisiert
~~~

Die Owner-Surface bewahrt weiterhin die harte Grenze zwischen persönlicher Kontinuität/Memory und institutioneller Wahrheit/Autorität.

## Status der Product Journey

```mermaid
flowchart LR
    A[Gehostetes Sign-in<br/>MATERIALIZED] --> B[Profil / Preferences<br/>PRODUCT SLICE MATERIALIZED]
    B --> C[Tenant-Bootstrap<br/>SELF-SERVICE GAP]
    C --> D[Discovery<br/>QUALIFIED OPEN PR]
    D --> E[Aktivierung und First Work<br/>PARTIAL]
    E --> F[/work<br/>PARTIAL / INTEGRATION IN REVIEW]
```

| Journey-Schritt | Bewertung | Grundlage |
|---|---|---|
| Gehostetes OIDC-Sign-in und opake Session | **pass auf kanonischer Runtime** | Kanonische Routen, Session Service, interne Identity-Bindings, Membership-abgeleitete Rolle und Tenant-bezogene Auflösung existieren auf `Unitera_Systems/main`. |
| Öffentliches Sign-up | **missing als kanonischer Self-Service-Lifecycle** | Kein vollständiger Owner-gebundener öffentlicher Account-/Bootstrap-Lifecycle ist End-to-End belegt. |
| Persönliches Profil / Preferences | **materialisierte Produktprojektion** | `unitera-production-interface@d7cbf8c` stellt kontrollierte Profile-/Preferences-/Account-Settings bereit. Diese sind produkt-owned und mutieren weder Membership, Tenant Authority noch Company Brain. |
| Tenant-Bootstrap / initiale Membership | **partial / blocked for self-service** | Tenant-Autorität existiert; der vollständige öffentliche Self-Service-Ownership-/Initial-Membership-Handoff ist jedoch nicht geschlossen. |
| Discovery Runtime | **qualifiziert, nichtkanonisch** | PR #94, Branch `codex/discovery-pilot-readiness-closure@19e70f2`, liegt 15 vor / 0 hinter kanonischem `Unitera_Systems/main`; PR bleibt offen und ist nicht produktiv aktiv. |
| First Work und `/work` | **partial, stärkere Integration in Review** | Kanonische Work-first-Semantik existiert. PR #98 ergänzt einen qualifizierten Read-only-Pilot-/Product-Integration-Stack, bleibt aber offen. |

## Qualifizierte Integrations-Slices außerhalb von kanonischem main

### Discovery — PR #94

Aktueller Branch-Head:

```text
19e70f220a83c331b7fc7f4c9bbd9e3ff9d35893
vor Unitera_Systems/main: 15
hinter: 0
```

Der Slice umfasst Tenant-isolierte Discovery-Persistenz, deterministische Cognition, strukturiertes Wissen/Provenienz, `/work/discovery`, First-Work-Projektionen, RLS-/Integrationsevidenz und Governance Admission. Er verwendet weiterhin keinen Live-LLM-Provider und fügt keine zweite effectful v1 Capability hinzu.

### Pilot UI / Identity / Decision Integration — PR #98

Aktueller Head:

```text
903f0250dd754ecc6ddaa87752a86e5c2c1a7f4d
```

Der offene PR materialisiert **nur innerhalb dieses Stacks**:

- Natural-Person-Identity / Attestation / fail-closed Independence Evaluation;
- HumanDecision + DualControlSet Persistenz und serverseitige Erzwingung;
- umfassendere Work-Order-State-Vector-/Read-Model-Projektionen;
- einen Read-only Production-Entry-Pilot und Produktnavigation.

Alle fünf beobachteten Remote-Workflow-Familien auf genau diesem Head sind erfolgreich: Audit Gates, Visual Enforcement Level 2, Canonical Enforcement, Governance Guardrails und CI.

Das bedeutet **qualifizierte Integration in Review**, nicht kanonischen Owner-/Runtime-Stand und keine Production Activation.

## Production Interface

`baum777/unitera-production-interface` ist jetzt als Implementierungs-Repository mit der expliziten Rolle verifiziert:

```text
B — PRODUCT_UI_PLUS_BFF
```

PR #1 wurde als `d7cbf8c` gemerged. Der qualifizierte Head `9e688b9` hatte einen erfolgreichen Remote-`ci`-Run.

Der gemergte Product Slice umfasst:

- Migration-Closure-Arbeit;
- kanonische Identity-Boundary und fail-closed Effect Guards;
- kontrollierte Profile und Preferences;
- Settings IA für Personal, Workspace und Expert/Admin Projections;
- ausdrücklich deaktivierte/nicht verfügbare Rollen- und Einladungsbefehle, wo kein kanonischer Command existiert.

Harte Grenze:

```text
Product UI / BFF
!= Tenant Authority
!= Membership Authority
!= Company Brain Authority
!= Capability Grant
!= Dispatch
!= Verification
```

Production Execution ist **nicht aktiviert**, der Live-Effect-Adapter ist **nicht aktiv**.

## Pilot Authority Freeze

Der aktuelle Registry-Freeze-Readiness-Report bleibt:

```text
FREEZE_NOT_AUTHORIZED
```

Der technische Pilotpfad ist weitgehend materialisiert. In der verifizierten Registry-Projektion bleiben aber zwei Owner-/Governance-Bedingungen blockierend:

1. commit-gebundener Independent Review ursprünglich selbst gemergter Owner-Surfaces;
2. eine explizite Tenant-Control-Plane-Deklaration, welche den Runtime-Enforcement-Conformance-Stand reconciled.

Der einheitliche/current Source Pointer bleibt unverändert. Pilot Authorization ist ein separater späterer Akt.

## Runtime-Status

| Runtime | Bewertung | Grenze |
|---|---|---|
| KNOW / Company-Brain-Consumption | **partial to materialized** | Owner Truth verbleibt in `coreos`; Consumption bleibt Exact-Binding-/Integritäts-beschränkt. |
| THINK / Cognition | **partial** | Compute-Envelope-Verträge existieren; vollständige Root-/Child-Admission, Lifecycle, Ledger/Memory und Production-Backend-Aktivierung bleiben gegatet. |
| ACT / kontrollierte Wirkung | **materialized bounded core** | `email.send.commit` bleibt die einzelne begrenzte v1-Wirkungsreferenz; dieses Update erweitert den Effect Scope nicht stillschweigend. |
| Local Runtime Node | **candidate** | Keine kanonische Runtime-Aktivierung. |
| Personal Realm / Companion | **Owner-Foundation gemerged; Runtime absent** | Owner-Semantik liegt auf `unitera_companion/main`; Cross-Repo Adoption und Runtime bleiben ausstehend. |
| Production Interface | **Produktimplementierung gemerged; Effects off** | UI/BFF und Settings sind materialisiert, ohne semantische Autorität zu erlangen oder Live Execution zu aktivieren. |


## Local Runtime Node × Personal Realm — gemeinsamer Boundary-Stand

Die beiden Flächen haben unterschiedliche Reifegrade, aber eine reale Bootstrap-Abhängigkeit.

~~~text
Local Runtime Node
= Candidate

Personal Realm
= Owner Foundation merged
= Runtime absent
~~~

Die Personal-Realm-Owner-Surface bindet den initialen Companion-Bootstrap an authentifizierten PlatformPrincipal, gebundenen Local Runtime Node, initialisierten lokalen UNITERA Workspace und expliziten Companion Bootstrap.

~~~text
LocalNodeIdentity != PersonalRealm
TenantNodeBinding != PersonalRealmBinding
Local Reachability != Authority
Company Context Access != Personal Memory Residency Permission
~~~

Die zusammenhängende Boundary ist auf [Local Runtime Node × Personal Realm](../architecture/local-node-personal-realm-trust-boundary.md) beschrieben.

## Reviewer-Assurance-Publikationslücke

Der aktuell verifizierbare Registry-Stand führt REVIEWER-MODEL-001 weiterhin über GOV-DC-001@0.1.0 als offenen Source-/Governance-Gap. In dieser Publikationsrunde wurde kein exakter Owner-Repository-Ref für eine neuere R2/R3-Materialisierung verifiziert.

Darum behauptet die Public Projection derzeit keine neueren R2/R3-ReviewerClass-Regeln als source-backed Zustand. Das ist eine Publikations-/Source-Verifikationslücke, keine Aussage, dass keine lokale Materialisierung existiert.

Siehe [Reviewer Assurance — Publikationsstatus](../reference/reviewer-assurance-publication-status.md).

## OpenRouter-/Cognition-Publikationsstatus

Die öffentliche OpenRouter-Seite bleibt ausdrücklich CANDIDATE / PILOT WORKING PLAN. Diese Dokumentationsaktualisierung hat keine neue Live-Provider-Qualification ausgeführt und erhebt deshalb keinen neuen CLOSED-Claim. Eine spätere Source-/Runtime-Reconciliation kann zeigen, dass die öffentliche Projektion hinter einem verifizierten Implementierungsstand zurückliegt.

## Explizite Nichtaussagen

Dieser Snapshot behauptet nicht:

- einen produktionsreifen öffentlichen Sign-up-/Onboarding-Funnel;
- Discovery gemerged auf `Unitera_Systems/main`;
- PR-#98-Identity-/Dual-Control-/Product-Integration als kanonisch, solange der PR offen ist;
- vollständige Cognition-Runtime-Aktivierung;
- einen autorisierten Pilot Owner Freeze;
- einen geänderten einheitlichen Source Pointer;
- Live Production Execution in `unitera-production-interface`;
- unbeschränkte Autonomie;
- automatische regulatorische Compliance oder Zertifizierung.

## Nächstes dokumentarisches Gate

Dieser Snapshot wird aktualisiert, wenn sich einer dieser Punkte materiell ändert: Merge/Status von Discovery PR #94, Merge/Review von Product Integration PR #98, Self-Service Identity/Tenant Bootstrap, Cognition-Runtime-Admission, Pilot-Freeze-Blocker, kanonisches Wiring/Staging/Live-Effect-Gate des Production Interface, Personal-Realm-Cross-Repo-Adoption/-Runtime oder eine verifizierte Source-Pointer-Entscheidung.
