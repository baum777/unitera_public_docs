# Local Runtime Node × Personal Realm — Joint Trust Boundary

**Status:** PUBLIC CROSS-SOURCE PROJECTION — descriptive, not authoritative  
**Authority:** none by itself  
**Source basis:** Local Runtime Node candidate v0.1.0 + Device Identity/Enrollment amendment, plus Personal Realm owner surface baum777/unitera_companion main@8dd8112a74631516c134bc3fc528d6220cdd27a7

[Deutsche Ausgabe](../../de/architecture/local-node-personal-realm-trust-boundary.md)

## 1. Maturity and shared boundary

Local Runtime Node and Personal Realm are distinct trust boundaries with a real bootstrap/runtime relationship.

~~~text
Local Runtime Node
= SOURCE_CANDIDATE_NON_AUTHORITATIVE
= not source-adopted
= not runtime-active
= not production-authorized

Personal Realm
= 20/20 owner decisions finalized
= owner architecture foundation merged to unitera_companion/main
= cross-repo adoption pending
= runtime absent
= production effects not authorized
~~~

They should be audited together without treating them as equally mature architecture candidates.

## 2. Bootstrap dependency without identity collapse

Initial Companion bootstrap is owner-bound to:

1. authenticated PlatformPrincipal;
2. successfully bound Local Runtime Node;
3. initialized local UNITERA workspace;
4. explicit Companion bootstrap.

~~~text
LocalNodeIdentity != PersonalRealm
LocalNodeIdentity != PersonIdentity
TenantNodeBinding != PersonalRealmBinding
Node replacement != new Personal Realm
~~~

One Personal Realm may bind multiple Local Runtime Nodes. The node is a materialization/resource prerequisite, not the realm's semantic owner.

## 3. Locality creates no authority

~~~text
Local Reachability != Authority
Device Ownership != Tenant Authority
Node Enrollment != Capability Grant
Filesystem Reachability != Resource Permission
Resource Permission != Business Authority
OS Permission != UNITERA Permission
~~~

Co-location of a file, credential or application on a device does not automatically authorize Companion or Tenant access.

## 4. Person, Realm, Tenant and Membership

~~~text
Person != PlatformPrincipal
PersonalRealm != CompanyTenant
PersonalRealm != Membership
same person != same institutional authority
~~~

The same person may belong to several Company Tenants while retaining one Personal Realm. Institutional contexts remain isolated.

## 5. Local-first persistence and multi-node

~~~text
Primary Local Workspace
→ authoritative working materialization

Encrypted Remote Layer
→ sync / backup / transport / recovery substrate
~~~

The remote layer is neither semantic owner nor default central plaintext personal store.

~~~text
mechanically safe metadata
→ deterministic merge may be allowed

semantic conflict
→ preserve both revisions
→ explicit reconciliation

last-write-wins
!= default semantic conflict policy
~~~

## 6. Backup and restore

Personal Realm backups are owner-directed to be hardware-key signed.

~~~text
Hardware-Key-Proof
+ Principal/Person Binding
+ Backup Integrity Verification
+ Target Local Runtime Node Binding
→ Restore Eligibility
~~~

Account-loss recovery uses a separate break-glass path with independent identity re-verification.

~~~text
HardwareKey != PersonIdentity
Backup Possession != RestoreAuthority
~~~

Concrete cryptographic algorithms and hardware standards remain a separate implementation profile.

## 7. Company Context and Personal Memory

~~~text
Company Context Access
!= Personal Memory Residency Permission
~~~

Durable company-derived memory requires a CrossBoundaryResidencyDecision:

~~~text
RETAIN
TRANSFORMED_RETAIN
TRANSIENT_ONLY
DENY
~~~

Retained company-derived Personal Memory must be reviewed when the relevant Membership ends.

Reverse direction is default deny:

~~~text
Company Tenant
→ no raw Personal Memory access
~~~

Only an explicit PersonalContextProjection may cross into company context, remaining tenant-, purpose-, scope- and time-bound, revocable and provenance-preserving.

## 8. No Local-Node bypass for missing company APIs

Not an acceptable shortcut:

~~~text
missing Company Brain API
→ raw local DB/file access through node
→ treat result as Company Brain truth
~~~

Local resource access remains resource access. Institutional truth remains bound to Company Brain, Tenant and lifecycle surfaces.

## 9. Credential boundary

~~~text
Companion / Cognition
→ governed tool request
→ Local Node / Credential Broker
→ local credential resolution
→ bounded adapter execution
→ result / evidence

raw credential
!→ model context
~~~

Raw credentials do not belong in Conversation History, Personal Memory, Company Brain, Action Proposals, Capability Grants or general evidence payloads.

## 10. Companion Shadow Guard and ACT

The Companion Shadow Guard adds review for autonomous effectful personal actions. Deterministic checks remain always on; the semantic layer checks reasonableness against intent, routine, magnitude, external visibility, sensitivity and novelty.

~~~text
ShadowGuardPass != Authority
Companion Suggestion != Decision
Personal Autonomy != Company Authority
Approval != Capability Grant
Grant != Dispatch
Receipt != Verification
~~~

Local Node must not create a second effectful ACT path outside canonical Execution Control.

## 11. Familiarity, Qualification and autonomy

~~~text
Relationship Familiarity
!= Qualification
!= Global Autonomy Tier
!= Capability-specific Delegation
!= Effective Capability Tier

effective capability tier
<= capability delegated tier
<= global Companion ceiling
~~~

Within-tier growth may occur only inside already authorized bounds. Cross-tier promotion requires explicit user approval and a new delegation revision.

## 12. Personal → company contribution

~~~text
Personal cognition
→ Companion prepares ContributionProposal
→ explicit user confirmation
→ lifecycle-aware institutional command
~~~

Depending on Company Brain lifecycle, the target may be DiscoveryInput, CandidateChangeRequest or BrainChangeProposal/LearningCandidate.

~~~text
ContributionProposal != Claim
ContributionProposal != ClaimEligibility
ContributionProposal != Brain Activation
~~~

## 13. Reviewer Assurance remains separate

The currently verifiable GitHub public-source state does not yet expose a newer owner-repository-verifiable R2/R3 ReviewerClass materialization. The Registry still projects REVIEWER-MODEL-001 through GOV-DC-001@0.1.0.

This page therefore does not promote newer R2/R3 semantics into source-backed public state.

~~~text
Companion Shadow Guard
!= R2/R3 Reviewer Assurance
!= Human Control
!= Capability Grant
~~~

Once a current Reviewer Model owner surface is published at an exact verifiable ref, this boundary should be reconciled again.

## 14. PR #98 remains a parallel Product track

Unitera_Systems PR #98 at 903f0250dd754ecc6ddaa87752a86e5c2c1a7f4d is a qualified open Product/Identity/Dual-Control integration under review, but not semantic owner of this boundary.

~~~text
PR #98 green
!= Local Node adopted
!= Personal Realm runtime active
!= production authorization
~~~

## 15. Next gates

### Local Runtime Node

Open questions include:

- v1 deployment target vs post-v1;
- Decision Class for TenantNodeBinding;
- hardware-backed identity threshold;
- user-registerable resource classes;
- long-lived provider credentials;
- local adapter qualification;
- offline ACT permanently forbidden vs initially deferred.

### Personal Realm

Owner Gate 0 is PASS, followed by:

1. Canonical Contract Materialization;
2. External Authority Bindings;
3. Persistence/Crypto Design;
4. Personal Memory Runtime;
5. Circling/Ideation;
6. Contribution Boundary;
7. Autonomy Contracts;
8. Shadow Guard;
9. Local Effect Pilots;
10. Qualification/Sampling;
11. Cross-Repo Source Adoption;
12. separate Production Activation.

## 16. Explicit non-claims

This page does not claim that Local Runtime Node is adopted/active, Personal Realm runtime exists, Companion effects are production-enabled, company-derived context is automatically retainable, Reviewer Assurance is already source-verified, or PR #98 activates this architecture.

## 17. Short form

~~~text
Local Node
= physical resource / credential / enforcement boundary

Personal Realm
= personal continuity / memory / context boundary

Company Tenant
= institutional authority boundary

Company Brain
= institutional truth / meaning boundary

Companion
= personal cognition and continuity assistant

None of these boundaries may silently inherit authority from another.
~~~
