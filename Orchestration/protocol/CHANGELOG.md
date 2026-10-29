# Orchestration protocol changelog

## 0.3.0 — 2026-10-28

Status: STABLE.

Promoted from the ORCH-09-corrected `0.3.0-draft` by explicit Conductor decision after fresh independent `AUDIT_PASS` in `/Orchestration/audits/branch-lifecycle-protocol-reaudit-2026-10-27.md`.

Production pointer: `/Orchestration/protocol/releases/v0.3.0.md`.

The normative contract is unchanged from the independently re-audited draft; promotion changes release metadata and production eligibility only. Historical STABLE release files remain immutable.

## 0.3.0-draft — 2026-10-27

Historical status: DRAFT candidate. ORCH-10 returned fresh independent `AUDIT_PASS` after ORCH-09 corrections, and explicit Conductor approval promoted the unchanged normative contract as STABLE `0.3.0` on 2026-10-28.

Backward-compatible branch-lifecycle capability added on top of STABLE `0.2.0`.

Introduces:
- persistent immutable `branch_id` and human branch labels;
- minimal branch seed under `/<PROJECT>/branches/<branch_id>/`;
- crash-safe root branch registry/non-reuse ledger with deterministic create/rename recovery;
- deterministic ACTIVE/PAUSED/BLOCKED/COMPLETED/CANCELLED/ARCHIVED lifecycle and reopen continuity;
- branch-vs-project decision rule;
- narrow same-branch root control-plane synchronization authority with sibling/root/shared-state boundaries;
- project-wide serial continuity across parallel branches;
- branch completion/result integration contract;
- branch-scoped read order and handoff requirements.

This draft is retained for provenance; production is now `0.3.0`.

## 0.2.0 — 2026-10-27

Status: STABLE.

Promoted from the corrected `0.2.0-draft` by explicit Conductor decision after fresh independent `AUDIT_PASS` in `/Orchestration/audits/legacy-adoption-protocol-reaudit-2026-10-27.md`.

Production pointer at release time: `/Orchestration/protocol/releases/v0.2.0.md`.

The normative contract is unchanged from the independently re-audited draft; promotion changes release metadata and production eligibility only. Historical STABLE release files remain immutable.

## 0.2.0-draft — 2026-10-27

Historical status: DRAFT candidate. ORCH-07 later returned `AUDIT_PASS`, and explicit Conductor approval promoted the unchanged normative contract as STABLE `0.2.0`.

Backward-compatible capability addition prompted by a real legacy-project adoption deadlock in `0.1.0`.

Introduces:

- `PRE_ORCHESTRATION_LEGACY` classification;
- `LEGACY_ADOPTION_PREFLIGHT`;
- bounded pre-approval control-plane writes under `/<PROJECT>/orchestration-adoption/`;
- deterministic serial initialization for legacy projects that lack `next_chat_serial`;
- explicit separation between control-plane audit coordination and operational migration writes;
- preservation of the existing `AUDIT_PASS -> post-audit Conductor approval -> operational migration` gate.

This draft is retained for provenance; `0.2.0` remains an immutable historical STABLE release superseded by `0.3.0`.

## 0.1.0 — 2026-10-27

Status: STABLE.

Promoted from independently re-audited `0.1.0-draft` by explicit Conductor decision after `AUDIT_PASS` in `/Orchestration/audits/project-bootstrap-protocol-reaudit-2026-10-27.md`.

Production pointer at release time: `/Orchestration/protocol/releases/v0.1.0.md`.

The normative contract is unchanged from the re-audited draft; promotion changes release metadata and production eligibility only. Historical STABLE release files are immutable.

## 0.1.0-draft — 2026-10-26

Initial consolidation based on reusable practices already present in Library.

Introduces:
- `Conductor` human interface role;
- semantic project-start trigger;
- `PROJECT_BOOTSTRAP` state machine;
- minimal project seed;
- persistent protocol pinning;
- explicit `PROJECT_UPGRADE` flow;
- Strategist/Auditor/Coordinator/Executor/Researcher role model;
- context isolation and provenance;
- deterministic lifecycle/handoff;
- anti-stall rule for transient pending states;
- universal chat naming pattern.

Historical status: DRAFT candidate, revised after independent audit and promoted as STABLE `0.1.0` on 2026-10-27 after fresh independent `AUDIT_PASS`.
