# Fresh independent re-audit handoff — Project Bootstrap Protocol 0.2.0-draft

Date: 2026-10-27
CHAT_TITLE: ORCH-07 · Protocol · Legacy-adoption fresh re-auditor
Role: Fresh independent Auditor
Current gate: `0_2_0_READY_FOR_FRESH_REAUDIT`

## Objective

Independently re-audit the corrected `0.2.0-draft` legacy-adoption contract after ORCH-06. Determine whether all three MUST findings from the prior audit are now fully and deterministically resolved. Do not edit the strategy or protocol candidate while issuing the verdict.

## Read in this order

1. `/Orchestration/INIT.md`
2. `/Orchestration/INDEX.md`
3. `/Orchestration/STATUS.md`
4. `/Orchestration/AGENTS.md`
5. `/Orchestration/audits/legacy-adoption-protocol-audit-2026-10-27.md`
6. `/Orchestration/protocol/CURRENT.md`
7. `/Orchestration/protocol/releases/v0.1.0.md`
8. `/Orchestration/protocol/releases/v0.2.0-draft.md`
9. `/Orchestration/strategy/universal-project-launch-strategy.md`
10. `/Orchestration/strategy/legacy-adoption-fix-2026-10-27.md`

## Confirmed facts — do not re-ask or re-prove absent contradictory evidence

- Production STABLE remains `0.1.0` and `/Orchestration/protocol/releases/v0.1.0.md` is immutable.
- The production CURRENT pointer remains `0.1.0`.
- `0.2.0-draft` is development-only and must not be promoted by the auditor.
- ORCH-05 returned `AUDIT_PASS_WITH_FIXES` with exactly three MUST findings.
- ORCH-06 performed the fixes and is not eligible to self-audit them.
- `ORCH-07` is already reserved for this fresh re-audit.
- Persisted Orchestration `next_chat_serial` after reserving ORCH-07 is `08`.
- The bounded `/<PROJECT>/orchestration-adoption/` control-plane direction and the MINOR classification were already accepted by the prior audit; re-open them only if the fixes introduce a concrete contradiction.

## Required checks

Re-test the previous MUST findings as normative protocol behavior, not merely presence of wording:

1. Discovery: semantic existing-project `PROJECT_UPGRADE` / PRE_ORCHESTRATION adoption must be discoverable without trustworthy local pinned metadata, using narrow read-only Orchestration access and production STABLE semantics; blockers must prevent memory/other-project improvisation.
2. Exact plan identity: persisted/read-back `PLAN.md`, audit verdict, and post-audit Conductor approval must bind to one deterministic plan revision/digest/target-version identity; PLAN changes must invalidate prior audit/approval for application.
3. STATE/serial continuity: failed/cancelled/restarted adoption must preserve authoritative STATE and monotonic serial history, expose explicit run states and recovery blockers, and persist deterministic adoption project-code handling before first serial allocation.

Also verify that the corrected candidate does not silently alter managed `0.1.0` projects, does not authorize pre-approval operational/domain writes, and does not change the production pointer.

## Allowed

- Read Orchestration project files required by this handoff.
- Write only the independent re-audit artifact and necessary Orchestration audit/navigation/status state after the verdict, consistent with the project protocol.
- Reserve the next chat serial only if the verdict/lifecycle requires another new agent, using authoritative current serial state and normal readback rules.

## Forbidden

- Do not modify `/Orchestration/protocol/releases/v0.1.0.md`.
- Do not edit `v0.2.0-draft` or the strategy while issuing the verdict.
- Do not promote `0.2.0-draft` to STABLE.
- Do not change the production CURRENT pointer.
- Do not treat `AUDIT_PASS_WITH_FIXES` as promotion-eligible.
- Do not rely on prior chat history or model memory instead of persisted project artifacts.

## Expected artifact

`/Orchestration/audits/legacy-adoption-protocol-reaudit-2026-10-27.md`

The artifact must identify the reviewed files, evaluate each former MUST finding separately, check for regressions/new blockers, and return exactly one verdict:

- `AUDIT_PASS`
- `AUDIT_PASS_WITH_FIXES`
- `AUDIT_FAIL`

Promotion is eligible for a later separate Conductor decision only if the fresh verdict is `AUDIT_PASS`.

## Completion criterion

The re-audit is complete when the verdict artifact is persisted and read back, STATUS/INDEX are updated consistently if required, and the lifecycle block is emitted without the auditor implementing its own fixes.

Required lifecycle block:

```text
AGENT_DECISION: CONTINUE | ARCHIVE_READY
NEXT_STEP: <one concrete next action>
NEW_AGENT_REQUIRED: YES | NO
NEXT_AGENT_ROLE: <only if YES>
NEXT_AGENT_PROMPT: <complete handoff prompt, only if YES>
```
