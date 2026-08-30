# Reviewer Assurance — Publikationsstatus und Boundary

**Status:** PUBLIC GAP / RECONCILIATION NOTE — nicht autoritativ  
**Authority:** keine aus diesem Dokument heraus  
**Verifizierbarer GitHub-Stand:** unitera-registry@891f9b967328131d8d3348ffba3dc64e7c1163ac

[English edition](../../en/reference/reviewer-assurance-publication-status.md)

## Verifizierter öffentlicher Stand

Die aktuelle Registry führt REVIEWER-MODEL-001 weiterhin als offenen Source-/Governance-Konflikt:

~~~text
state = open_source_available
source_ref = GOV-DC-001@0.1.0
current_direction = no_permanent_pool_currently; dual_control_per_decision
governance_activation = decision_recorded_implementation_pending
~~~

Die Registry erzeugt keine Authority. Sie belegt nur den aktuell verifizierbaren veröffentlichten Source-/Gap-Stand.

## Warum hier keine neueren R2/R3-Regeln behauptet werden

Im aktuellen GitHub-Stand dieser Publikationsrunde wurde kein exakter Owner-Repository-Ref für eine neuere REVIEWER-MODEL-001-/R2-/R3-Materialisierung verifiziert.

~~~text
reported local/project materialization
!= verified owner-repo ref
!= source-backed public claim
~~~

Public Documentation darf eine lokale oder Chat-only Entscheidung nicht dadurch zu Authority machen, dass sie sie publiziert.

## Boundary für künftige Adoption

~~~text
Reviewer Assurance != Human Control
Reviewer Model != Authority
Reviewer PASS != Owner Approval
Reviewer PASS != Capability Grant
Reviewer PASS != Dispatch
Model Output != Institutional Truth
Companion Shadow Guard != Reviewer Assurance
~~~

Der Companion Shadow Guard prüft effectful Companion Actions innerhalb vorhandener Delegation/Policy. Ein allgemeiner R2/R3-Mechanismus wäre eine separate Assurance-Surface und darf weder Shadow Guard noch Human Control still ersetzen.

## Publication Gate

Bevor neuere Reviewer-Assurance-Semantik öffentlich als source-backed beschrieben wird, müssen mindestens verifizierbar sein:

1. exakter Owner-Repository-Ref;
2. Status der Owner Decision;
3. Adoption-/Activation-Status;
4. exakter ReviewerClass-/Output-Contract-Stand;
5. Qualification-Status gebundener Modelle/Harnesses;
6. klare Trennung zu Human Control und Capability Grant;
7. Registry-Reconciliation, falls der ältere REVIEWER-MODEL-001-Stand superseded wird.

Bis dahin bleibt diese Seite bewusst eine Gap-/Boundary-Notiz.
