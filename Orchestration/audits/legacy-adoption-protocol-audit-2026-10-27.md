# Independent audit — Project Bootstrap Protocol 0.2.0-draft legacy adoption

Date: 2026-10-27
Role: Independent auditor (`ORCH-05`)
Scope: `/Orchestration/protocol/releases/v0.2.0-draft.md`, the corresponding strategy update, and the PRE_ORCHESTRATION legacy-adoption correction
Verdict: `AUDIT_PASS_WITH_FIXES`
Promotion to STABLE: NOT ALLOWED until all MUST fixes are persisted and a fresh independent re-audit returns `AUDIT_PASS`.

## Evidence reviewed

- `/Orchestration/INIT.md`
- `/Orchestration/INDEX.md`
- `/Orchestration/STATUS.md`
- `/Orchestration/protocol/CURRENT.md`
- `/Orchestration/protocol/releases/v0.1.0.md`
- `/Orchestration/protocol/releases/v0.2.0-draft.md`
- `/Orchestration/strategy/universal-project-launch-strategy.md`
- `/Orchestration/strategy/legacy-adoption-fix-2026-10-27.md`
- `/Orchestration/audits/project-bootstrap-protocol-reaudit-2026-10-27.md`
- `/Orchestration/handoffs/legacy-adoption-independent-auditor-prompt-2026-10-27.md`

The audited strategy/release were not modified while issuing this verdict. Production `0.1.0` and the production CURRENT pointer remain unchanged.

## Executive result

The core correction is sound: a PRE_ORCHESTRATION legacy project may persist a narrowly bounded adoption control plane without treating that as operational migration; independent audit and post-audit Conductor approval remain mandatory before operational writes. The new adoption serial state also breaks the original `audit -> separate chat -> serial -> forbidden write` cycle.

However, three deterministic gaps remain. The most important is an entry-point gap: the environment-level discovery hook is still defined only for create/init bootstrap intent. A legacy project with no pinned Orchestration protocol cannot deterministically discover the upgrade/adoption contract from ordinary `PROJECT_UPGRADE` intent. This shifts, rather than completely removes, the chicken-and-egg problem. The candidate also needs an explicit persisted identity for the exact audited plan and explicit continuity rules for failed/cancelled/restarted adoption state so serials and audit verdicts cannot be reused ambiguously.

## Required check matrix

| # | Check | Result | Rationale |
|---|---|---|---|
| 1 | Removes the legacy deadlock without bypassing audit/approval | PASS WITH FIX | The bounded control plane breaks the serial-write cycle, but discovery into that flow is not deterministic for an unpinned existing project. |
| 2 | Pre-approval control-plane writes are sufficiently narrow | PASS | Writes are restricted to `/orchestration-adoption/` and named artifact classes, with explicit operational prohibitions. |
| 3 | Control plane cannot silently mutate operational/domain state | PASS | The release explicitly forbids rewriting operational root state, domain facts, gates, permissions, external systems, credentials or production state. |
| 4 | Serial namespace initialization is deterministic | PASS WITH FIX | `01 -> 02` is clear for first adoption, but restart/cancel continuity and absent project-code selection need explicit treatment. |
| 5 | No semantic conflict with pre-Orchestration chat/task numbers | PASS WITH SHOULD | Old labels are explicitly non-authoritative and do not retroactively consume Orchestration serials. A display-name collision policy would still improve operator clarity. |
| 6 | Authoritative serial carries forward after adoption without reuse | PASS WITH FIX | Carry-forward is explicit, but a later adoption attempt after FAILED/CANCELLED must be required to retain a valid prior adoption serial state rather than reinitialize it. |
| 7 | Completed work/facts/gates/approvals/external systems preserved | PASS | The candidate explicitly preserves these and prohibits pre-approval changes. |
| 8 | Sequence is persisted exact plan -> independent audit -> AUDIT_PASS -> post-audit approval -> operational writes | PASS WITH FIX | The sequence is correct, but the audit/approval must be bound to a persisted immutable plan revision/identity. |
| 9 | Managed 0.1.0 projects keep existing semantics | PASS | The candidate explicitly leaves correctly managed 0.1.0 projects pinned until explicit PROJECT_UPGRADE. |
| 10 | MINOR classification is correct | PASS | The change is a backward-compatible capability/rule addition, matching the existing MINOR definition. |
| 11 | Failure/cancel semantics prevent false migration | PASS WITH FIX | The project remains legacy, but restart/resume authority and serial/plan continuity are not fully specified. |
| 12 | No new lifecycle/handoff/serial ambiguity | PASS WITH FIX | Core lifecycle is preserved; the three MUST fixes below close remaining ambiguities. |

## MUST fixes before promotion

### MUST 1 — Deterministic discovery for PROJECT_UPGRADE / legacy adoption

Problem: the environment-level discovery hook is normatively triggered only by natural-language create/init intent. `PROJECT_UPGRADE` is defined after the protocol is already loaded, but a PRE_ORCHESTRATION legacy project may have no pinned release or local Orchestration metadata that tells a new chat to load it.

Required change in both strategy and release:

1. Extend the discovery contract to recognize semantic existing-project upgrade/adoption intent, not only create/init intent.
2. For an unpinned existing project, authorize the same narrow read-only access to `/Orchestration/protocol/CURRENT.md` and only the exact production upgrade/adoption sources it references.
3. Keep the authorization Orchestration-only and read-only until the candidate's bounded `LEGACY_ADOPTION_PREFLIGHT` rules permit target-project control-plane writes.
4. Define a deterministic blocker such as `UPGRADE_BLOCKED_DISCOVERY_UNAVAILABLE` when that discovery path is unavailable; do not improvise from memory or another project.
5. Production legacy adoption must use the production STABLE pointer. A DRAFT candidate remains development/test-only.

### MUST 2 — Bind audit and Conductor approval to an exact persisted PLAN identity

Problem: the candidate repeatedly says "exact plan", but `PLAN.md` is writable during preflight and no normative plan revision/identity is carried from persistence -> audit -> verdict -> Conductor approval. A changed file could otherwise be ambiguously treated as the plan that passed audit.

Required change:

1. `STATE.md` must persist an immutable audit-target identity for the submitted plan, for example `plan_revision` plus a content digest, or another equivalently deterministic identifier.
2. The plan must be read back successfully before audit handoff publication.
3. Every `AUDIT-*.md` verdict must identify the exact audited plan revision/identity and target protocol version.
4. Post-audit Conductor approval must identify that same plan revision/identity and target version.
5. Any content change to `PLAN.md` after the audited identity was established creates a new plan revision and invalidates the prior `AUDIT_PASS` for application; a fresh independent audit is required before approval/application.

### MUST 3 — Define restart/resume continuity for adoption STATE and serials

Problem: the candidate says a failed/cancelled adoption remains legacy, but does not fully define what a later attempt does with an existing adoption `STATE.md`. Reinitializing `next_chat_serial: 01` after a failed/cancelled attempt would reuse reserved numbers and could attach new work to stale plan/audit state.

Required change:

1. A valid existing `/orchestration-adoption/STATE.md` remains authoritative control-plane history even when the adoption run is `FAILED` or `CANCELLED`; reserved serials are never reset or reused.
2. A later attempt must resume the authoritative `next_chat_serial` or explicitly start a new `adoption_run_id` while carrying the same monotonic serial namespace forward.
3. Persist explicit run states at least sufficient to distinguish `PREFLIGHT`, `AUDIT_PENDING`, `FIXES_REQUIRED`, `AUDIT_PASS`, `AWAITING_CONDUCTOR_APPROVAL`, `APPLYING`, `COMPLETED`, `FAILED`, and `CANCELLED` (names may differ if semantics are equivalent).
4. Define the blocker/recovery behavior for missing, corrupt or internally inconsistent adoption STATE instead of silently reinitializing it.
5. Persist the project code used for adoption titles before the first serial allocation. If no trustworthy project code exists, define a deterministic control-plane-only derivation/selection rule and include the final code in the migration plan that the Conductor approves.

## SHOULD fixes

1. Make the permitted readback/validation artifact shape explicit instead of leaving "readback/validation metadata" open-ended; a fixed filename or metadata section in `STATE.md` is sufficient.
2. Add an operator-facing display-collision rule for old legacy chat/task labels that happen to look like `<PROJECT_CODE>-01`. Semantically they are not Orchestration serials, but the protocol should state how to avoid or annotate ambiguous duplicate-looking titles when the host can detect them.

## Checks that passed without required changes

- Bounded pre-approval writes are contained under `/<PROJECT>/orchestration-adoption/`.
- Operational `INIT.md`, `INDEX.md`, `STATUS.md`, `AGENTS.md`, `CHANGELOG.md`, task/branch state and external systems remain protected before audit/approval.
- Managed 0.1.0 projects are not silently upgraded.
- Production `0.1.0` remains immutable and production CURRENT is unchanged during this audit.
- MINOR versioning is correct under the current semantic-release contract.
- The intended post-audit order remains correct: `AUDIT_PASS` first, explicit Conductor approval second, operational migration writes third.

## Verdict rationale

`AUDIT_PASS_WITH_FIXES`.

The design direction is valid and the original serial-write cycle is substantially resolved. Promotion is blocked because legacy adoption is not yet fully deterministic from the first unpinned upgrade intent through exact-plan audit binding and failed/cancelled restart semantics. These are protocol-contract issues, not implementation preferences.

## Lifecycle

AGENT_DECISION: ARCHIVE_READY
NEXT_STEP: `ORCH-06 · Protocol · Legacy-adoption fixes` applies all three MUST fixes to the strategy and `0.2.0-draft`, keeps production `0.1.0` unchanged, updates STATUS, then reserves a new serial for a fresh independent re-audit.
NEW_AGENT_REQUIRED: YES
NEXT_AGENT_ROLE: Strategist / Protocol editor
NEXT_AGENT_PROMPT:

```text
CHAT_TITLE: ORCH-06 · Protocol · Legacy-adoption fixes

Ты — стратег/редактор протокола проекта /Orchestration после независимого аудита 0.2.0-draft.

Сначала прочитай:
1. /Orchestration/INIT.md
2. /Orchestration/INDEX.md
3. /Orchestration/STATUS.md
4. /Orchestration/audits/legacy-adoption-protocol-audit-2026-10-27.md
5. /Orchestration/protocol/CURRENT.md
6. /Orchestration/protocol/releases/v0.1.0.md
7. /Orchestration/protocol/releases/v0.2.0-draft.md
8. /Orchestration/strategy/universal-project-launch-strategy.md
9. /Orchestration/strategy/legacy-adoption-fix-2026-10-27.md

Текущий gate: 0_2_0_AUDIT_PASS_WITH_FIXES.

Подтверждено и не требует повторного доказательства:
- production STABLE = 0.1.0 и во время исправлений остаётся production;
- 0.1.0 immutable;
- bounded /orchestration-adoption/ control plane как направление принят аудитом;
- MINOR-классификация 0.2.0 корректна;
- ORCH-05 завершил независимый аудит с AUDIT_PASS_WITH_FIXES;
- ORCH-06 уже зарезервирован;
- persisted Orchestration next_chat_serial после резерва ORCH-06 = 07.

Обязательно исправь три MUST из audit artifact:
1. deterministic discovery entry point for existing-project PROJECT_UPGRADE / PRE_ORCHESTRATION legacy adoption;
2. persisted exact PLAN identity/revision binding across readback, audit verdict and post-audit Conductor approval;
3. failed/cancelled/restarted adoption STATE continuity, monotonic serial preservation, explicit run states/recovery and deterministic project-code handling.

Разрешено:
- редактировать только development strategy/candidate and necessary Orchestration navigation/status artifacts;
- уточнить SHOULD fixes, если это не расширяет scope.

Запрещено:
- менять /Orchestration/protocol/releases/v0.1.0.md;
- продвигать 0.2.0-draft в STABLE;
- менять production pointer;
- объявлять собственные исправления независимо прошедшими audit.

Критерий завершения:
- все MUST нормативно присутствуют в strategy и release;
- CURRENT по-прежнему production 0.1.0;
- STATUS фиксирует новый gate READY_FOR_FRESH_REAUDIT;
- зарезервирован следующий новый serial для свежего независимого re-auditor;
- создан полный handoff свежему auditor, который не выполнял эти fixes.

В конце примени lifecycle contract.
```
