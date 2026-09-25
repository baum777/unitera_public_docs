# UNITERA Licensing Policy

## Purpose

This document defines the public licensing policy for UNITERA.

It separates:

- proprietary UNITERA software;
- public documentation;
- third-party materials;
- trademarks and brand assets;
- explicitly licensed exceptions.

## 1. Proprietary software by default

UNITERA code and implementation material is intended to remain closed source unless a specific repository, package, file, or written agreement expressly grants broader rights.

A public description of UNITERA does not make the underlying implementation open source.

## 2. Repository-local license required

Every proprietary code repository should contain a root-level `LICENSE` file or equivalent legal notice that identifies the applicable proprietary terms.

The central documents in this repository are a policy and reference surface. They do **not** by themselves apply a license to another repository merely because that repository is part of UNITERA.

## 3. Public documentation is a separate surface

`unitera_public_docs` is a curated public documentation projection.

Publication of documentation does not grant rights to non-public source code, internal implementation details, runtime systems, private repositories, or other proprietary materials.

The license applicable to the documentation repository itself must be stated separately at repository level if broader reuse rights are intended.

## 4. Third-party software remains separately licensed

Third-party materials retain their original licensing terms. UNITERA's proprietary licensing must not be used to remove or reduce rights granted by an applicable third-party license.

See [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

## 5. Exceptions must be explicit

Any open-source, source-available, SDK, sample-code, partner, evaluation, or commercial exception must be explicit and scoped.

An exception should identify at minimum:

- the covered repository, package, files, or deliverable;
- the applicable license or agreement;
- the version or effective date where relevant;
- any redistribution, attribution, patent, copyleft, or notice obligations.

## 6. No implied cross-repository grant

A license in one UNITERA repository does not automatically license another UNITERA repository.

Each repository and distributable artifact must be independently unambiguous about its licensing status.

## 7. Legal review

Before external commercial licensing, source disclosure, SDK publication, enterprise distribution, or material changes to these terms, the applicable legal text should be reviewed by qualified counsel.

---

## Deutsche Kurzfassung

UNITERA-Code bleibt grundsätzlich proprietär, sofern nicht ausdrücklich eine andere Lizenz oder schriftliche Vereinbarung gilt.

Jedes proprietäre Code-Repository benötigt eine eigene eindeutige `LICENSE` im Root. Die zentralen Dateien in `unitera_public_docs` dokumentieren die gemeinsame Policy, lizenzieren aber andere Repositories nicht automatisch.

Drittanbieter-Lizenzen und zwingende gesetzliche Rechte bleiben unberührt.
