# Orchestration — INDEX

## Entry points

- `/Orchestration/INIT.md` — project purpose and invariant rules.
- `/Orchestration/STATUS.md` — current operational state and next gate.
- `/Orchestration/AGENTS.md` — universal role/lifecycle rules used while developing this system.

## Audit

- `/Orchestration/audits/library-baseline-audit-2026-10-26.md` — audit of reusable practices already present in Library.
- `/Orchestration/audits/project-bootstrap-protocol-audit-2026-10-26.md` — independent audit of the initial strategy/protocol; verdict `AUDIT_PASS_WITH_FIXES`.
- `/Orchestration/audits/project-bootstrap-protocol-reaudit-2026-10-27.md` — fresh independent re-audit of the revised `0.1.0` draft; verdict `AUDIT_PASS`.
- `/Orchestration/audits/legacy-adoption-protocol-audit-2026-10-27.md` — ORCH-05 independent audit of `0.2.0-draft`; verdict `AUDIT_PASS_WITH_FIXES`; produced three MUST fixes.
- `/Orchestration/audits/legacy-adoption-protocol-reaudit-2026-10-27.md` — ORCH-07 fresh independent re-audit after ORCH-06 fixes; verdict `AUDIT_PASS`; the audited candidate was subsequently promoted by explicit Conductor approval.
- `/Orchestration/audits/branch-lifecycle-protocol-audit-2026-10-27.md` — ORCH-08 independent audit of `0.3.0-draft`; verdict `AUDIT_PASS_WITH_FIXES`; produced three MUST fixes.
- `/Orchestration/audits/branch-lifecycle-protocol-reaudit-2026-10-27.md` — ORCH-10 fresh independent re-audit after ORCH-09 corrections; verdict `AUDIT_PASS`; all prior MUST/SHOULD findings closed.

## Strategy

- `/Orchestration/strategy/universal-project-launch-strategy.md` — living universal strategy underlying the STABLE `0.3.0` branch-lifecycle contract.
- `/Orchestration/strategy/legacy-adoption-fix-2026-10-27.md` — defect analysis and design rationale for the `0.2.0` legacy-adoption correction.
- `/Orchestration/strategy/branch-lifecycle-2026-10-27.md` — design rationale for persistent parallel branch lifecycle promoted in STABLE `0.3.0`.

## Protocol

- `/Orchestration/protocol/CURRENT.md` — production pointer; STABLE `0.3.0`, no active development candidate.
- `/Orchestration/protocol/CHANGELOG.md` — protocol history and compatibility notes.
- `/Orchestration/protocol/releases/v0.3.0.md` — current production STABLE release; immutable after promotion.
- `/Orchestration/protocol/releases/v0.3.0-draft.md` — historical audited draft retained for provenance; ORCH-10 verdict `AUDIT_PASS`.
- `/Orchestration/protocol/releases/v0.2.0.md` — historical STABLE release; immutable; projects pinned to it remain there until explicit upgrade.
- `/Orchestration/protocol/releases/v0.2.0-draft.md` — historical audited draft retained for provenance.
- `/Orchestration/protocol/releases/v0.1.0.md` — historical STABLE release; immutable.
- `/Orchestration/protocol/releases/v0.1.0-draft.md` — historical draft retained for provenance.

## Branches

- `/Orchestration/branches/` — canonical persistent branch control plane.

## Branch registry / non-reuse ledger

| branch_id | current label | canonical path | mutation state | mutation_id |
| --- | --- | --- | --- | --- |
| `github-orchestration` | GitHub orchestration | `/Orchestration/branches/github-orchestration/` | `STABLE` | `-` |

## Handoffs

- `/Orchestration/handoffs/legacy-adoption-independent-auditor-prompt-2026-10-27.md` — completed `ORCH-05` independent-audit handoff for `0.2.0-draft`.
- `/Orchestration/handoffs/legacy-adoption-fresh-reauditor-prompt-2026-10-27.md` — completed `ORCH-07` fresh independent re-audit handoff after ORCH-06 MUST fixes.
- `/Orchestration/handoffs/branch-lifecycle-independent-auditor-prompt-2026-10-27.md` — completed `ORCH-08` independent-audit handoff for `0.3.0-draft`.
- `/Orchestration/handoffs/branch-lifecycle-fresh-reauditor-prompt-2026-10-27.md` — completed `ORCH-10` fresh independent re-audit after ORCH-09 corrections; verdict `AUDIT_PASS`.
- `/Orchestration/handoffs/strategy-independent-auditor-prompt-2026-10-26.md` — prompt used for initial independent review.
- `/Orchestration/handoffs/protocol-independent-reauditor-prompt-2026-10-26.md` — handoff used for the completed `0.1.0` fresh re-audit.

STABLE `0.3.0` was promoted on 2026-10-28 after ORCH-10 `AUDIT_PASS` and explicit Conductor approval. Persisted `next_chat_serial` is `12`; ORCH-11 is consumed by the initial `github-orchestration` branch chat.
