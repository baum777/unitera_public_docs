---
description: Öffentlicher Einstieg in UNITERA Contracts ohne eingeschränkte interne Contract-IDs oder Topologie offenzulegen.
icon: file-signature
---

# Öffentlicher Contract-Index

`UPD-CONTRACT-INDEX-001` · `CONTRACT` · `PUBLIC_ABSTRACTED`

Die öffentliche UNITERA-Dokumentation beschreibt **Contract-Semantik und Grenzen vor Contract-IDs**. Interne IDs, rekonstruierbare Topologie und unveröffentlichte Schemas bleiben außerhalb der öffentlichen Projektion, solange sie nicht explizit freigegeben sind.

{% include "../.gitbook/includes/public-projection.md" %}

## Verfügbare öffentliche Contract-Semantik

- [Authority- und Source-of-Truth-Modell](../architecture/authority-and-source-model.md)
- [Kontrollierte externe Wirkung](../runtime/governed-effect.md)
- [Funktionen, Capabilities und Use Cases](../status/capability-use-case-matrix.md)
- [Public-Disclosure-Policy](../reference/public-disclosure-policy.md)

## Publikationsregel

Sobald ein stabiler öffentlicher API-Contract existiert, soll dieser Bereich **OpenAPI-first** aufgebaut werden, statt Endpoints in Prosa zu duplizieren. Bis dahin darf das Fehlen einer Endpoint-Seite nicht als stilles Produktions-API-Versprechen interpretiert werden.
