# Functions, capabilities and use cases

**Disclosure:** PUBLIC_CORE · PUBLIC_ABSTRACTED · PUBLIC_STATUS
**As of:** 25 September 2026

This page translates the public UNITERA architecture into concrete product
capabilities and situations of use. **Capability** means a publicly explained
product ability here — not a formal Capability Grant or permission to execute.

## Reading the status

| Status | Meaning |
|---|---|
| **Established** | The semantics or architecture is clearly defined. This does not automatically mean complete product availability. |
| **Bounded implementation** | Verifiable product, contract or runtime parts are materialized; this does not imply general live or end-to-end readiness. |
| **Active development** | An already-materialized surface is still being completed or qualified. |
| **Owner-confirmed candidate** | A direction is confirmed but has not yet been materialized as the current canonical state. |
| **Pilot preparation** | A bounded pilot is being prepared but is not activated by this documentation. |
| **Live-gated** | A bounded internal capability chain is materialized while real external use still requires current gates. |
| **Deliberately limited** | Effects remain restricted to explicitly governed paths; broad autonomy is not claimed. |

## Product functions

| Function | Public capability | Typical use cases | Current status | What the public can expect |
|---|---|---|---|---|
| Sign-up and Discovery | Capture and review organizational foundations, sources, boundaries and open questions | Onboarding, organization profile, Company Brain preparation | Bounded implementation; pilot qualification continues | A traceable Discovery and review journey; no commitment to universal integrations or complete live-onboarding readiness |
| Company Brain | Supply versioned, reviewed institutional context | Customer responses, decision briefs, organization-specific work | Active versioned foundation; bounded product and runtime integration | A governed context foundation; not model memory, an agent or execution permission |
| `/work` | Bring work, sources, next steps and required decisions together | Daily work, case handling, work coordination | Bounded implementation; active development | A materialized institutional work surface; not every journey is live-qualified end to end |
| Needs You | Surface required human participation | Approvals, clarification, blocked decisions | Established core semantics; bounded implementation | A materialized participation and attention projection; inclusion alone is not an urgency or authority signal |
| Chat and Quick Actions | Clarify questions, refine work and offer bounded next steps | Research questions, drafting, navigation, contextual preparation | Bounded implementation | Assistance within current context; visibility or a click does not mean executability |
| Personal Realm and Companion | Keep personal continuity, memory, ideation and contribution preparation separate from the Company Brain | Resume work, develop ideas, prepare a personal contribution | Established contract semantics; bounded product-side implementation | Personal continuity and confirmation-bound contribution preparation; no autonomous handoff or general Personal Realm runtime activation claimed |
| Today, Resume and cross-device continuity | Represent a deliberate restart point, stable focus, stale snapshots and persistent pauses correctly | Mobile daily start, session continuation, device change | Bounded implementation | Resume with an explicit freshness boundary; continuity carries no authority and triggers no automatic retry |
| Native work surfaces | Project institutional and personal state consistently on native surfaces | Desktop work, mobile case handling, Personal Hub | Cross-surface contract baseline materialized; representative E2E qualification open | Shared product grammar with server-side authority; client state remains a projection and creates no independent truth |
| Local runtime boundary | Make approved local resources reachable under control | Local context access, bounded system-adjacent work | Bounded implementation | Controlled proximity to data and effects; reachability is neither read nor execution permission |

## Core work-flow capabilities

| Step | Capability | Use cases | Current status | Boundary |
|---|---|---|---|---|
| **KNOW** | Supply purpose-bound, current and traceable context | Understand a customer request, prepare a decision, resume work | Established architecture; bounded implementation | More context creates no additional rights |
| **THINK** | Analyze options and produce drafts or proposals | Response draft, summary, plan, follow-up questions | Established semantics; bounded product integration | Model output remains a proposal and owns no institutional truth |
| **Govern** | Separate and evaluate policy, authority and required human decisions | Approve, reject, clarify, stop | Established architecture; bounded implementation | Approval is neither a grant nor execution |
| **ACT** | Perform only a currently authorized, bounded effect | Governed delivery or a bounded change through an admitted path | Bounded runtime implementation; live-gated | No claim of broad autonomous software control or general production readiness |
| **PROVE** | Keep execution evidence, verification and reconciliation distinct | Check delivery, resolve an uncertain outcome, prevent duplicate effect | Established semantics; bounded runtime and test qualification | A receipt is not a business outcome; an uncertain result does not permit blind retry |
| Model choice and cognition | Use replaceable models and qualified processing routes within unchanged boundaries | Draft, analyze and choose an appropriate level of cognition | Routing and resolution-evidence contracts materialized in bounded form; runtime use separately gated | A model alias, selected route or stronger model creates neither additional authority nor data-release permission |

## Bounded pilot capability families

Current pilot preparation materializes several clearly bounded capability families. This view deliberately abstracts internal operation names, providers and binding details.

| Capability family | Public expectation | Maturity boundary |
|---|---|---|
| Operational and availability reads | Use current, admitted operational information for a work item | real source access, tenant/resource access and freshness remain prerequisites |
| Booking-related work | Prepare, create, change or cancel bookings only through an admitted path | write effects remain policy-, authority-, evidence- and live-gated |
| Calendar work | Read availability and perform approved schedule changes through a governed path | external admission and current permission remain separately required |
| External communication | Prepare messages and send them only through a valid effect path | send evidence is not automatically delivery or business success |
| Reminders and deadlines | Prepare or create internal follow-up work from sufficiently unambiguous context | no claim of general task or software control |
| Knowledge access | Search and read admitted knowledge sources | read-only does not mean global data release; provenance and freshness remain relevant |
| Outcome evidence and recovery | Keep effect, receipt, verification and reconciliation separate | an uncertain outcome stays uncertain and never authorizes blind retry |

These capability families are not a service catalog and do not claim that every family is already live-admitted in a concrete operating environment.

## Use-case matrix

| Use case | Supporting functions | Expected result | Public maturity |
|---|---|---|---|
| Prepare a customer response | Company Brain, KNOW, THINK, `/work`, Chat | A traceable draft with sources, assumptions and open questions | Bounded implementation; real live delivery is not generally committed |
| Prepare a decision brief | KNOW, THINK, Govern, Needs You | Structured options and a visible human decision | Established semantics; bounded product implementation |
| Build organizational context | Sign-up, Discovery, Company Brain | Reviewable foundations before context becomes active institutionally | Active versioned foundation and bounded journey implementation |
| Resume work | Personal Realm, Companion, Today, Resume | Last traceable state, open questions and next useful step | Bounded product-side implementation; no claim of general live availability across all devices |
| Create bounded external effect | Govern, ACT, PROVE | Authorized effect or a traceable stop with evidence | Bounded runtime implementation; pilot preparation and external live gates remain open |
| Resolve an uncertain outcome | PROVE, reconciliation, human takeover | Status remains visible until sufficient evidence exists | Core semantics and bounded recovery paths materialized; real external qualification remains separate |
| Use local or remote cognition | KNOW, THINK, model choice, local control boundary | Purpose-bound processing of eligible context | Bounded architecture and integration; data release and authority remain separately gated |

## Claim boundary

This matrix is a public expectation map, not a service catalog, SLA, Capability
Grant or evidence of production readiness. Status classifications are
deliberately coarse. Materialization, external live readiness, pilot activation
and production are evaluated separately.

See also the [current public state](current-state.md),
[pilot and production readiness](pilot-production-readiness.md) and
[public source assurance](../reference/source-basis.md).

---

[← Previous: Current public state](current-state.md) · [Index](../README.md) · [Next: Architecture baseline →](bootstrap-materialization.md)
