# Independent audit — Project Bootstrap Protocol 0.3.0-draft branch lifecycle

Date: 2026-10-27
Role: Independent auditor (`ORCH-08`)
Scope: `/Orchestration/protocol/releases/v0.3.0-draft.md`, corresponding branch-lifecycle strategy/design, and the normative persistent branch capability added over STABLE `0.2.0`
Gate reviewed: `0_3_0_DRAFT_READY_FOR_INDEPENDENT_AUDIT`
Verdict: `AUDIT_PASS_WITH_FIXES`
Promotion to STABLE: NOT ALLOWED until all MUST fixes are persisted and a fresh independent re-audit returns `AUDIT_PASS`; promotion then still requires a separate explicit Conductor decision.

## Independence and observed state

This audit did not edit the audited candidate or strategy while issuing the verdict.

Observed candidate/provenance:
- production CURRENT remains STABLE `0.2.0`;
- `/Orchestration/protocol/releases/v0.2.0.md` remains the immutable production baseline;
- development candidate is `/Orchestration/protocol/releases/v0.3.0-draft.md`;
- requested capability is multiple persistent branches within one project with one project-wide chat serial namespace;
- ORCH-08 was already reserved for this audit and authoritative `next_chat_serial` was `09` before this verdict.

Evidence reviewed:
- `/Orchestration/INIT.md`
- `/Orchestration/INDEX.md`
- `/Orchestration/STATUS.md`
- `/Orchestration/protocol/CURRENT.md`
- `/Orchestration/protocol/releases/v0.2.0.md`
- `/Orchestration/protocol/releases/v0.3.0-draft.md`
- `/Orchestration/strategy/universal-project-launch-strategy.md`
- `/Orchestration/strategy/branch-lifecycle-2026-10-27.md`
- `/Orchestration/handoffs/branch-lifecycle-independent-auditor-prompt-2026-10-27.md`

## Executive result

The branch model is directionally sound and most of the requested contract is already deterministic: branch-vs-project classification is usable; `branch_id` derivation is stable; branch seed/state ownership is compact; sibling authority is isolated; one project-wide chat serial namespace is preserved; completion does not silently merge branch claims into root truth; existing `0.2.0` projects remain pinned; and MINOR `0.3.0` is the correct release class.

Three normative gaps still block promotion. First, branch creation/rename is not crash-safe across branch files and the root registry, so an interruption can leave an orphan or ambiguous identity and a retry can incorrectly suffix into a duplicate. Second, the authority rule for root/shared writes conflicts with the mandatory root INDEX/STATUS writes required by semantic branch creation and lifecycle maintenance. Third, reopen semantics preserve identity/history but do not deterministically define the resulting state and persisted transition record.

## Required check matrix

| # | Check | Result | Independent finding |
|---|---|---|---|
| 1 | Branch vs separate-project classification | PASS | The draft distinguishes branches by shared project authority/constraints/root/context and routes independently governed or materially separate long-term work to a separate project. |
| 2 | `branch_id` identity, collision, rename, non-reuse | PASS WITH FIX | Derivation/suffixing/immutable identity are sound, but non-reuse and rename consistency need a crash-safe authoritative registry/recovery rule so partial writes cannot create an orphan or ambiguous label/identity. |
| 3 | Minimum branch storage / replacement chats | PASS | `BRANCH.md` + `STATUS.md`, lazy additional structure, root-first read order and handoff identity are sufficient without copying project-wide protocol rules. |
| 4 | Root vs branch authority/conflict semantics | PASS WITH FIX | Branch STATUS vs root STATUS precedence is clear, but root registry vs BRANCH identity/label mismatch after partial create/rename has no deterministic repair authority. |
| 5 | Concurrent branch creation/readback | PASS WITH FIX | Project-level serialization is required, but failure between branch-seed creation and root registration is not normatively recovered; retry can encounter an unregistered existing id/path and create a suffixed duplicate. |
| 6 | ACTIVE/PAUSED/BLOCKED/COMPLETED/CANCELLED/ARCHIVED and reopen | PASS WITH FIX | Normal states and anti-stall triggers are good. Reopen preserves id/history and requires an explicit decision, but the resulting state and minimum persisted transition evidence are not defined. |
| 7 | Branch-scoped authority / sibling and root writes | PASS WITH FIX | Sibling protection is sound. However, semantic branch creation is declared sufficient while mandatory root registry/summary writes require explicit root/shared-write authority, creating a normative authorization contradiction. |
| 8 | Cross-branch dependencies/conflicts / root coordination | PASS | Stable branch-id dependencies, continuation triggers and shared-conflict routing are sufficient; incompatible shared changes cannot silently win. |
| 9 | One project-wide serial namespace | PASS | The candidate correctly keeps `next_chat_serial` project-wide and serializes allocation across parallel branches. Branch creation itself does not consume a serial. |
| 10 | Completion / integration safety | PASS | Substantive completion persists a result artifact and does not make branch claims project-wide truth without an authorized root/shared integration update. |
| 11 | Branch read order / handoff / progressive disclosure | PASS | Root INIT/INDEX/STATUS then branch BRANCH/STATUS then referenced artifacts is sufficient and sibling visibility does not grant authority. |
| 12 | Existing `0.2.0` protection / ad-hoc branch migration | PASS | Existing projects remain pinned until explicit PROJECT_UPGRADE and existing ad-hoc workstreams are mapped/preserved rather than silently recreated. |
| 13 | Branch blockers | PASS WITH FIX | The blocker set is useful, especially registry/shared conflict blockers, but registry inconsistency needs an explicit recovery path rather than only stop/report semantics. |
| 14 | MINOR classification | PASS | Persistent branch lifecycle is a backward-compatible capability/rule addition and correctly belongs in `0.3.0`. |
| 15 | New cycles, ambiguous authority, destructive archive/delete, orphan/stall risks | PASS WITH FIX | Archive/delete safety is good and no serial-cycle regression was found. A partial create/rename can orphan or split branch identity across root/branch artifacts; authority wording can also deadlock mandatory control-plane synchronization. |

## MUST fixes

### MUST 1 — Crash-safe branch identity/registry commit and deterministic recovery

The candidate must define one authoritative commit/recovery contract for branch creation and identity/label registry mutations.

Required normative behavior:
1. A `branch_id` that has ever been successfully allocated must remain discoverable as historical identity and must never become reusable through normal completion/cancellation/archive cleanup. Root registry semantics must explicitly retain historical identities or an equivalent authoritative non-reuse ledger.
2. Branch creation must not treat an unregistered pre-existing `branches/<branch_id>/` seed left by an interrupted prior attempt as an ordinary collision and allocate `-2`. It must stop/recover as registry inconsistency, determine whether the persisted seed belongs to the same attempted logical branch, and either complete registration or route an explicit repair/rollback decision.
3. Creation/rename mutations spanning `BRANCH.md`, root `INDEX.md` and root `STATUS.md` must define deterministic readback and partial-write recovery. A mismatch must name the authoritative fields and repair direction; no last-writer-wins improvisation.
4. `BRANCH_BLOCKED_REGISTRY_INCONSISTENT` must have a normative recovery rule that preserves allocated identity/history before another branch id is allocated.

### MUST 2 — Narrow authority for mandatory root branch-control-plane synchronization

Resolve the contradiction between semantic branch lifecycle intent and section 15.5 root/shared-write authority.

Required normative behavior:
1. An explicitly authorized branch lifecycle action such as create, resume/reopen, rename, pause/block/complete/cancel/archive may authorize only the root branch-control-plane synchronization that the protocol requires for that same branch: branch registry/label/path and compact root STATUS summary/dependency/conflict state.
2. This narrow control-plane authority must not authorize unrelated root project metadata, project-wide business/domain facts, sibling branch content, shared resources, permissions, constraints or integration decisions.
3. Any broader shared/root change must continue to require explicit task/user authority and normal root coordination.

This keeps semantic requests such as `создай ветку Cron` executable without turning branch scope into blanket root authority.

### MUST 3 — Deterministic reopen transition and persisted lifecycle continuity

Define exact reopen behavior for `COMPLETED`, `CANCELLED` and `ARCHIVED` branches.

Required normative behavior:
1. Reopen requires an explicit authorized reopen decision and preserves the same immutable `branch_id`, prior result/evidence, prior gates and historical state.
2. Define the resulting current state deterministically: normally `ACTIVE`, or `BLOCKED`/`PAUSED` only when the reopen decision/current verified condition explicitly establishes that state and its required trigger/owner.
3. Persist at least the prior state, reopen reason/decision provenance and transition timestamp (or an equivalent append-only transition record) before claiming reopen succeeded.
4. Read back branch state and required root registry/summary synchronization before resuming execution.

## SHOULD fixes

1. Add a minimal append-only branch transition log (or fixed history section in branch STATUS) for all lifecycle transitions, not only reopen, to make replacement-agent recovery and audit easier.
2. State explicitly that root INDEX keeps archived/completed/cancelled branch registry entries visible for identity discovery while root STATUS may summarize only live branches.
3. When a cross-branch dependency becomes material, specify whether the branch agent may perform the narrow root summary synchronization under MUST 2 or must route it to the coordinator; avoid leaving root STATUS stale.

## Checks that passed without required changes

- Production CURRENT remains `0.2.0`; no silent promotion/adoption occurred.
- `0.2.0` production semantics were not modified by this audit.
- One project-wide serial namespace remains correct across parallel branches.
- Branch completion does not auto-integrate into root/shared truth.
- Destructive branch deletion remains outside normal lifecycle and requires explicit Conductor intent.
- Existing `0.2.0` projects remain pinned until explicit upgrade.
- The MINOR classification is correct.

## Verdict rationale

`AUDIT_PASS_WITH_FIXES`.

The design is viable and does not require architectural replacement. Promotion is blocked because the remaining defects sit on identity persistence, mutation authorization and lifecycle recovery boundaries. Those are protocol-contract issues: they can cause duplicate/orphan branches, an authorization deadlock for mandatory root synchronization, or ambiguous reopen state after replacement/retry.

## Lifecycle

AGENT_DECISION: ARCHIVE_READY
NEXT_STEP: `ORCH-09 · Protocol · Branch-lifecycle fixes` applies all three MUST fixes to the development strategy and `0.3.0-draft`, keeps production `0.2.0` unchanged, updates STATUS/INDEX, then reserves the next project-wide serial for a fresh independent re-audit.
NEW_AGENT_REQUIRED: YES
NEXT_AGENT_ROLE: Strategist / Protocol editor
NEXT_AGENT_PROMPT:

```text
CHAT_TITLE: ORCH-09 · Protocol · Branch-lifecycle fixes

Ты — стратег/редактор протокола проекта /Orchestration после независимого ORCH-08 аудита branch-lifecycle кандидата 0.3.0-draft.

Сначала прочитай строго:
1. /Orchestration/INIT.md
2. /Orchestration/INDEX.md
3. /Orchestration/STATUS.md
4. /Orchestration/audits/branch-lifecycle-protocol-audit-2026-10-27.md
5. /Orchestration/protocol/CURRENT.md
6. /Orchestration/protocol/releases/v0.2.0.md
7. /Orchestration/protocol/releases/v0.3.0-draft.md
8. /Orchestration/strategy/universal-project-launch-strategy.md
9. /Orchestration/strategy/branch-lifecycle-2026-10-27.md

Текущий gate: 0_3_0_AUDIT_PASS_WITH_FIXES.

Подтверждено и не требует повторного доказательства без новых противоречащих данных:
- production STABLE = 0.2.0 и должен оставаться production во время исправлений;
- /Orchestration/protocol/releases/v0.2.0.md immutable;
- 0.3.0-draft — backward-compatible MINOR candidate, не production;
- ORCH-08 завершил независимый audit с AUDIT_PASS_WITH_FIXES;
- ORCH-09 уже зарезервирован для этих исправлений;
- persisted Orchestration next_chat_serial после резерва ORCH-09 = 10;
- принятые части дизайна не нужно перепроектировать: branch-vs-project classification, one project-wide serial namespace, branch-scoped sibling isolation, RESULT/integration non-auto-merge, explicit upgrade for 0.2.0 projects и MINOR classification.

Обязательно исправь три MUST из audit artifact:
1. crash-safe branch identity/registry commit + deterministic recovery/non-reuse for partial create/rename;
2. narrow authority rule that lets an authorized branch lifecycle action perform only mandatory root branch-control-plane synchronization without granting broader root/shared authority;
3. deterministic reopen transition with preserved identity/history, explicit resulting state, persisted transition evidence and readback.

SHOULD можно применить, если это не расширяет scope.

Разрешено:
- редактировать только development strategy/design/candidate и необходимые Orchestration navigation/status artifacts;
- уточнить blockers/recovery/history consistently across strategy and draft.

Запрещено:
- менять /Orchestration/protocol/releases/v0.2.0.md;
- продвигать 0.3.0-draft в STABLE;
- менять production CURRENT pointer с 0.2.0;
- объявлять собственные исправления независимо прошедшими audit.

После исправлений:
- обнови STATUS фактическим gate 0_3_0_READY_FOR_FRESH_REAUDIT;
- зарезервируй следующий project-wide serial из authoritative next_chat_serial=10 для fresh independent re-auditor, persist/read back increment to 11 before publishing CHAT_TITLE;
- подготовь complete handoff свежему аудитору, который не выполнял эти fixes;
- сам не выдавай AUDIT_PASS своей редакции.

В конце применяй lifecycle contract проекта.
```
