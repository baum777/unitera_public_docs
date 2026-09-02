# Documentation & Diagram Conventions

**Status:** repository-local publication convention  
**Authority:** applies only to this public projection repository

## Document header

Every architecture/status page should begin with a compact status declaration:

```text
Status: PUBLIC PROJECTION | ESTABLISHED | MATERIALIZED | CANDIDATE | OPEN
Authority: none by itself
Source basis: owning repo / frozen source / candidate source
```

`PUBLIC PROJECTION` describes the document's role. It does not upgrade the maturity of the architecture described inside it.

## Technical vocabulary

Preserve canonical technical identifiers and casing:

- `UNITERA`
- `Unitera_Systems`
- `coreos`
- `unitera-os`
- `KNOW`
- `THINK`
- `ACT`
- `Company Brain`
- `Action Proposal`
- `Capability Request`
- `Capability Grant`
- `Receipt`
- `Verification`
- `email.send.commit`

Do not invent aliases for authority-bearing identifiers.

## Mermaid conventions

Use GitHub-native Mermaid in Markdown. The repository-root syntax card is [`MERMAID.md`](../../../MERMAID.md), taken from [GitHub: Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).

Required fence: a fenced code block whose language identifier is `mermaid`. Quote labels that contain `/`, `&`, HTML breaks, or a leading path. Use `<br>`, never `<br/>`. Write `/work` as `W["/work"]`, not `W[/work]`.

### Flow diagrams

Use `flowchart LR` for lifecycle or cross-boundary movement and `flowchart TB` for layered architecture.

```mermaid
flowchart LR
    A[Source] --> B[Evaluation]
    B --> C[Decision]
```

### Sequence diagrams

Use `sequenceDiagram` when actor order and request/response semantics matter.

```mermaid
sequenceDiagram
    participant A as Agent
    participant G as Governance
    participant X as Executor
    A->>G: Proposal
    G->>X: Authorized request
    X-->>G: Receipt
```

### Boundary notation

- Solid arrow `-->`: normal data/control progression.
- Dotted arrow `-.->`: explanatory/reference relationship or prohibited authority backflow when labeled explicitly.
- Subgraphs: use for KNOW/THINK/ACT or clear trust/ownership domains.
- Do not rely on color alone to encode authority, risk, or maturity.

## Public wording rules

Prefer:

- “source-reconciled direction” over “finished architecture” when adoption is incomplete;
- “candidate” over “planned feature” when the source explicitly classifies it as candidate;
- “materialized in the owning runtime” only when verified;
- “receipt” and “verification” as separate concepts;
- “Registry reference” rather than “Registry authority”.

Avoid unverified claims of production readiness, compliance, certification, customer proof, or autonomous permission.
