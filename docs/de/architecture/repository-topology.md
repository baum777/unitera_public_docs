# Verantwortungs- und Vertrauensdomänen

Status: `PUBLIC_ABSTRACTED`

Die öffentliche Architektur zeigt Verantwortungsrollen, keine Repository-, Service- oder Deployment-Topologie.

```mermaid
flowchart TB
    IK["Institutionelles Wissen"] -->|"geprüfter Kontext"| CR["Kontext und Kognition"]
    GOV["Governance und Authority"] -->|"kontrollierte Erlaubnis"| EX["Kontrollierte Ausführung"]
    CR -->|"Vorschlag"| EX
    EX -->|"Receipt und Verifikation"| EV["Evidenz und Provenance"]
    PC["Persönliche Kontinuität"] -.->|"ausdrücklich begrenzter Beitrag"| IK
    UI["Menschliche Interaktion"] -->|"Ziele und Entscheidungen"| GOV
```

Die physische Zuordnung, interne Verträge und Enforcement-Ketten bleiben in den zuständigen internen Quellen.

> Conceptual public projection — not deployment, service, repository, protocol or security topology.

---

[← Vorherige: Human Agency und Model Sovereignty](human-agency-and-model-sovereignty.md) · [Index](../README.md) · [Nächste: Authority- und Quellenmodell →](authority-and-source-model.md)
