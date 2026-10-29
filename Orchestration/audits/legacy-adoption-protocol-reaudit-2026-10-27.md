# Fresh independent re-audit — Project Bootstrap Protocol 0.2.0-draft legacy adoption

Date: 2026-10-27
Role: Fresh independent Auditor (`ORCH-07`)
Scope: corrected `/Orchestration/protocol/releases/v0.2.0-draft.md`, corresponding strategy, and the three MUST findings from ORCH-05
Gate reviewed: `0_2_0_READY_FOR_FRESH_REAUDIT`
Verdict: `AUDIT_PASS`
Promotion to STABLE: ELIGIBLE FOR SEPARATE CONDUCTOR DECISION; this audit does not itself promote the draft or change the production CURRENT pointer.

## Independence and immutability

This re-audit was performed in a fresh auditor context that did not perform ORCH-06 fixes. The audited strategy and candidate were not edited while issuing this verdict.

Observed audited artifacts:
- `/Orchestration/protocol/releases/v0.2.0-draft.md` — DRAFT, file version observed by the audit: 1.
- `/Orchestration/strategy/universal-project-launch-strategy.md` — file version observed by the audit: 4.
- source audit: `/Orchestration/audits/legacy-adoption-protocol-audit-2026-10-27.md` — ORCH-05 verdict `AUDIT_PASS_WITH_FIXES`.
- correction rationale: `/Orchestration/strategy/legacy-adoption-fix-2026-10-27.md`.

Production was separately verified to remain:
- STABLE version `0.1.0`;
- production release `/Orchestration/protocol/releases/v0.1.0.md`;
- CURRENT production pointer `0.1.0`.

## MUST re-audit matrix

| MUST | Result | Independent finding |
|---|---|---|
| 1. Deterministic discovery for unpinned `PROJECT_UPGRADE` / PRE_ORCHESTRATION adoption | PASS | The discovery hook now recognizes semantic existing-project upgrade/adoption intent. An unpinned project loads only CURRENT and exact production-STABLE upgrade/adoption source(s); discovery remains Orchestration-only/read-only until bounded preflight is authorized. Explicit discovery/pointer/STABLE blockers are defined, memory/other-project fallback is forbidden, and DRAFT remains development/test-only. |
| 2. Exact PLAN revision/digest/target binding | PASS | `PLAN.md` must be persisted and read back before handoff; `STATE.md` records monotonic `plan_revision`, SHA-256 of exact persisted PLAN bytes, and exact target version. Every audit verdict and post-audit Conductor approval must name the same identity. Any PLAN content change creates a new revision/digest and invalidates prior audit pass/approval for application. |
| 3. STATE continuity, monotonic serials, recovery, deterministic adoption code | PASS | A valid adoption STATE remains authoritative after `FAILED`, `CANCELLED`, retry and replacement; serials are never reset/reused. Explicit run states and missing/corrupt/inconsistent-state blockers are defined. A later run resumes or creates a new `adoption_run_id` while carrying forward serial/history. `adoption_project_code` is persisted before first allocation and has an explicit deterministic fallback derivation; final operational project code is part of the audited/approved plan. |

## Regression checks

| Check | Result | Finding |
|---|---|---|
| Managed `0.1.0` projects are not changed automatically | PASS | Correctly managed projects remain pinned until explicit `PROJECT_UPGRADE`; legacy-adoption capability does not force migration. |
| No operational/domain writes before audit + post-audit approval | PASS | Pre-approval writes remain confined to `/orchestration-adoption/` control-plane artifacts. Operational root files, business/domain facts, completed work, gates, permissions, external systems, credentials and production state remain protected. |
| Audit remains independent from implementation | PASS | Auditor is forbidden from implementing the migration it judges; fixes require a fresh independent re-audit. |
| `AUDIT_PASS_WITH_FIXES` is insufficient for apply/promotion gate | PASS | The corrected contract explicitly requires `AUDIT_PASS`; fixes/re-audits do not collapse into self-certification. |
| Production CURRENT pointer remains unchanged during candidate audit | PASS | CURRENT still exposes production STABLE `0.1.0`; `0.2.0-draft` remains a development candidate. |
| Production `0.1.0` remains immutable | PASS | No change to the STABLE release is required or authorized by the corrected draft. |

## Determinism review

### Discovery

The prior chicken-and-egg gap is closed at the environment discovery layer. Existing-project upgrade/adoption intent is now itself a discovery trigger, so an unpinned legacy project does not need pre-existing target-project Orchestration metadata to find the production contract. Failure has explicit blockers rather than memory-based reconstruction.

### PLAN identity

The audit target is now a persisted tuple:

`(plan_revision, plan_digest_sha256, plan_target_protocol)`.

Readback precedes identity establishment; verdict and approval are both identity-bound. This removes the ambiguity identified by ORCH-05 between a plan that was audited and a later-mutated `PLAN.md`.

### STATE and serial continuity

The corrected contract distinguishes first-ever adoption initialization from recovery of existing adoption history. Valid STATE survives terminal run outcomes; later attempts cannot reset the namespace. Missing/corrupt/inconsistent prior STATE blocks allocation until verifiable recovery. Run states are explicit and sufficient to distinguish preflight, audit, fixes, approval, apply, completion, failure and cancellation.

## Non-blocking hardening observations

These do not prevent `AUDIT_PASS` because the ORCH-05 MUST requirements are satisfied:

1. A future clarification may define the exact canonicalization algorithm for the target-project root string used by the `ADP-<H8>` fallback, so equivalent path spellings cannot vary across hosts.
2. A future clarification may state explicitly that the independent auditor recomputes the current `PLAN.md` digest immediately before issuing a verdict, although the present requirement that the verdict applies only to the exact persisted identity already makes a mismatched plan ineligible for the gate.

## Verdict rationale

`AUDIT_PASS`.

All three ORCH-05 MUST findings are normatively closed in both the strategy and `0.2.0-draft`. The corrected flow is deterministic enough for discovery, exact-plan audit binding, post-audit approval, failed/cancelled recovery and monotonic serial continuation. No audited regression was found in managed-project pinning, pre-approval write boundaries, production-pointer isolation or independent-audit semantics.

This verdict makes the corrected candidate eligible for a separate Conductor promotion decision. It does not itself promote `0.2.0-draft`, rename/rewrite the release as STABLE, or change `/Orchestration/protocol/CURRENT.md`.

## Lifecycle

AGENT_DECISION: ARCHIVE_READY
NEXT_STEP: Conductor explicitly approves or rejects promotion of the audited corrected `0.2.0-draft`; until that decision, production remains `0.1.0` and no promotion writes are authorized.
NEW_AGENT_REQUIRED: NO
