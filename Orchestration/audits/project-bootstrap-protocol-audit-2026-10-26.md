# Independent audit — Project Bootstrap Protocol 0.1.0-draft

Date: 2026-10-26
Role: Independent auditor
Scope: `/Orchestration` initial universal project-launch strategy and `Project Bootstrap Protocol 0.1.0-draft`
Verdict: `AUDIT_PASS_WITH_FIXES`
Promotion to STABLE: NOT ALLOWED until MUST fixes are applied and independently re-audited.

## Evidence reviewed

- `/Orchestration/INIT.md`
- `/Orchestration/INDEX.md`
- `/Orchestration/STATUS.md`
- `/Orchestration/audits/library-baseline-audit-2026-10-26.md`
- `/Orchestration/strategy/universal-project-launch-strategy.md`
- `/Orchestration/protocol/CURRENT.md`
- `/Orchestration/protocol/releases/v0.1.0-draft.md`
- `/Management/INIT.md`
- `/Vertime/shared/context-isolation.md`
- `/Vertime/shared/agent-completion-protocol.md`
- `/GoogleDrive-Cleanup/branches/03-chat-naming/chat-naming-standard.md`

## Findings

### 1. Natural-language bootstrap and Conductor interface

PASS.

The strategy correctly accepts semantic project-start intent instead of a magic command and reduces the Conductor intake to one compact free-form question. This matches the target interaction model and avoids an unnecessary form.

### 2. Persistent project state and replaceable chats

PASS WITH FIX.

The seed `INIT.md / INDEX.md / STATUS.md / AGENTS.md`, pinned protocol metadata, lifecycle block and full handoff requirement are sufficient for chat replacement in principle. However, the release does not yet require a replacement handoff to preserve already confirmed facts/approvals that must not be asked again. That omission can cause a new agent to repeat questions or reopen settled gates.

### 3. Global vs local rules

PASS WITH FIX.

The strategy correctly states that the global protocol owns orchestration mechanics and the project owns domain-specific rules. However, because every project is required to create `AGENTS.md`, the protocol must explicitly define that local `AGENTS.md` contains only project-specific roles, constraints and overrides plus a pointer to the pinned global release. It must not copy universal lifecycle/bootstrap rules into every project, otherwise the system recreates the duplication the Orchestration project is meant to eliminate.

### 4. Bootstrap determinism and protocol discovery

FIX REQUIRED.

The strategy assumes that a brand-new first chat can read `/Orchestration/protocol/CURRENT.md`, but it does not define the bootloader/discovery contract that tells an otherwise empty project chat to do so, nor what to do if the global Orchestration source is unavailable in that project context.

A deterministic system needs an explicit bootstrap hook outside the project-local files, or an equivalent guaranteed mechanism, that maps natural-language project-start intent to the Orchestration entry point. The trigger may authorize read-only access only to the global Orchestration bootstrap source; it must not become blanket permission to read other projects.

The bootstrap flow must also verify that project-file persistence/writes are available and read back the created seed before claiming initialization succeeded. If the global protocol or persistent project storage is unavailable, stop with a defined bootstrap blocker instead of improvising or claiming success.

### 5. Version pinning and silent upgrades

PASS.

`protocol_created_with`, `protocol_current_local`, explicit migration policy, immutable historical releases and the rule that global updates do not silently alter existing projects correctly implement version pinning.

### 6. `PROJECT_UPGRADE`

PASS WITH FIX.

The upgrade sequence is structurally sound but `apply only approved migration` is not deterministic enough. With default `EXPLICIT_MIGRATION`, the protocol must state exactly who approves mutation and when.

Required rule: comparison/planning is read-only; no project-file mutation occurs until the Conductor explicitly approves the concrete migration plan. Nontrivial/breaking migrations additionally require an independent audit before that approval/apply gate. Completed domain work and current gates remain preserved.

### 7. Chat serial allocation

FIX REQUIRED.

`next_chat_serial` is required metadata but its semantics are undefined. The protocol must define it as the next unused project-wide serial. The first bootstrap chat consumes `01`; after that allocation the persisted value is `02`. Allocating a new chat reserves the current value and advances it before emitting the handoff. Reserved/abandoned numbers are not reused.

This is required to make naming deterministic under replacement, retries and parallel branches.

### 8. Source priority

FIX REQUIRED.

`/Orchestration/INIT.md` defines a useful source-priority model, but the global draft release does not carry an equivalent universal conflict-resolution contract. A generated project therefore cannot deterministically resolve conflicts between verified current state, project safety/local rules, current audit/result/handoff, STATUS, INDEX, pinned protocol and chat memory.

The global release must define the canonical priority order, while allowing project-specific mandatory safety/legal/business rules and explicit local protocol overrides to remain authoritative within their scope.

### 9. Independent audit semantics

FIX REQUIRED.

The draft says audit independence must be preserved where required, but does not define independence. For any gate explicitly marked independent, the auditor must be a separate chat/agent context from the author/executor whose work is being audited and must not mutate the audited implementation while issuing the verdict. Findings go back to the owning role for correction, followed by re-audit when required.

### 10. Lifecycle and anti-stall

PASS WITH FIX.

The required `AGENT_DECISION`, one `NEXT_STEP`, `NEW_AGENT_REQUIRED`, complete next-agent prompt and anti-stall rule preserve the strongest Vertime practices. Add to every required next-agent prompt the already accepted facts, approvals and completed gates that must not be re-requested or repeated.

### 11. Structure and complexity

PASS.

The four-file seed is small enough and deferred folders avoid premature structure. The strategy correctly postpones ChatGPT Project UI automation and external implementation of the Conductor role.

## MUST fixes before STABLE

1. Add a deterministic bootstrap-discovery/bootloader contract for a brand-new project chat, including narrowly scoped authorization to read the Orchestration bootstrap source, explicit failure state when it is unavailable, storage capability preflight and post-create readback.
2. Define `next_chat_serial` precisely as the next unused project-wide serial and specify reserve/increment/no-reuse behavior.
3. Make `PROJECT_UPGRADE` mutation authorization explicit: read-only compare/plan first; Conductor approval of the concrete migration plan before writes; independent audit additionally required for nontrivial/breaking migrations.
4. Add a universal source-priority/conflict-resolution contract to the released protocol, not only to the Orchestration project's own INIT.
5. Define local `AGENTS.md` as project-specific roles/constraints/overrides plus pinned-protocol reference; do not copy universal orchestration rules into each project.
6. Define mandatory independent-audit separation: separate chat/agent context from the audited author/executor; auditor does not implement its own required fixes while issuing the verdict.
7. Extend the next-agent handoff contract to carry already confirmed facts, approvals and completed gates that must not be re-asked or repeated.

## SHOULD fixes

1. Normalize terminology between `PROJECT_BOOTSTRAP` and the baseline audit's `PROJECT_CREATE` by making one canonical state name and treating the other, if retained, as an alias/subflow.
2. Clarify DRAFT metadata: use a draft creation/update field while DRAFT and reserve `released_at` for an actual release/promotion event.
3. State that showing the Project Instructions snippet is not by itself a reason to stop bootstrap and wait for confirmation; ask the Conductor only when that UI action is genuinely required before safe continuation.
4. Clarify `CURRENT.md` fields so development candidate and production STABLE pointer cannot be confused when both exist.

## Verdict rationale

The core architecture is sound and preserves the strongest reusable patterns from Management, Vertime and GoogleDrive-Cleanup without importing their domain specifics. The defects are contract gaps rather than a failed design. They are material enough that `0.1.0-draft` must not be promoted to STABLE yet.

## Lifecycle

AGENT_DECISION: ARCHIVE_READY
NEXT_STEP: A separate Strategist/Protocol editor applies all MUST fixes to the strategy and draft protocol, keeps production STABLE unset, then routes the revised draft to a fresh independent re-audit.
NEW_AGENT_REQUIRED: YES
NEXT_AGENT_ROLE: Strategist / Protocol editor
NEXT_AGENT_PROMPT:
CHAT_TITLE: ORCH-03 · Protocol · Strategy revision

Ты — стратег/редактор протокола проекта `/Orchestration` после независимого аудита первоначального draft.

Сначала прочитай только:
1. `/Orchestration/INIT.md`
2. `/Orchestration/INDEX.md`
3. `/Orchestration/STATUS.md`
4. `/Orchestration/audits/project-bootstrap-protocol-audit-2026-10-26.md`
5. `/Orchestration/strategy/universal-project-launch-strategy.md`
6. `/Orchestration/protocol/CURRENT.md`
7. `/Orchestration/protocol/releases/v0.1.0-draft.md`
8. `/Vertime/shared/agent-completion-protocol.md`
9. `/GoogleDrive-Cleanup/branches/03-chat-naming/chat-naming-standard.md`

Текущий gate: `AUDIT_PASS_WITH_FIXES`.

Цель: применить все MUST fixes из независимого аудита к стратегии и draft протокола, сохранив короткий интерфейс Дирижёра, pinning версий, изоляцию проектов и заменяемость чатов.

Обязательно:
- определить deterministic bootstrap discovery/bootloader и failure states;
- определить точную семантику `next_chat_serial`;
- определить точный approval gate для `PROJECT_UPGRADE`;
- перенести универсальный source-priority contract в release;
- определить назначение локального `AGENTS.md` без копирования глобальных правил;
- определить независимость audit как отдельный chat/agent context;
- дополнить handoff подтвержденными фактами/разрешениями/закрытыми gates;
- не переводить release в STABLE и не назначать production pointer;
- не внедрять автоматическое создание ChatGPT Projects или внешнего исполнителя Дирижёра.

После исправлений обнови STATUS фактическим новым gate и подготовь handoff свежему независимому re-auditor. Сам не выдавай финальный независимый PASS своей же редакции.
