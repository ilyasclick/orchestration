# Universal project launch strategy

Status: DRAFT
Date: 2026-10-27
Owner role: Strategist / Protocol editor
Gate: `0_3_0_DRAFT_READY_FOR_INDEPENDENT_AUDIT`

## Objective

Create a universal operating method in which a `Conductor` can start any project in a new chat using ordinary language, while the first chat deterministically discovers the global bootstrap protocol, initializes persistent project state, asks only for missing intent, and routes work into replaceable agent roles.

The same system must support later protocol evolution without silently changing existing projects, and support multiple persistent parallel work branches inside one project without turning each branch into a separate project.

## Human interface

The Conductor should not need to remember a command grammar.

Semantic triggers include examples such as:

- `запускай проект`
- `создай проект`
- `init`
- `первый чат`
- `начинаем новый проект`

Canonical state name: `PROJECT_BOOTSTRAP`. `PROJECT_CREATE`, if encountered in older material, is an alias for the new-project subflow of `PROJECT_BOOTSTRAP`.

## Deterministic bootstrap discovery / bootloader

A brand-new target project cannot depend on target-project files that do not exist yet. Therefore bootstrap requires one environment-level discovery hook outside the target project.

The hook is installed once at the host/user/workspace orchestration layer and has exactly this semantic contract:

```text
On natural-language intent either (a) to create/initialize a project or (b) to upgrade/adopt Orchestration for an existing project, read /Orchestration/protocol/CURRENT.md plus only the exact Orchestration sources referenced by the applicable production pointer. This is read-only cross-project authorization for Orchestration discovery only; it does not authorize reading any other project.
```

The hook may be implemented later by product instructions, a wrapper, an agent runner or another guaranteed mechanism. Its implementation is outside this draft. The protocol only defines the required behavior.

Discovery sequence for `PROJECT_BOOTSTRAP`:

1. Detect semantic `PROJECT_BOOTSTRAP` intent.
2. Use the discovery hook to read `/Orchestration/protocol/CURRENT.md`.
3. Read the exact release file referenced by the production STABLE pointer.
4. In production mode, require an explicit STABLE production pointer and a release whose status is `STABLE`.
5. Before target-project writes, perform persistent-storage capability preflight: establish that the environment can create/update target-project persistent files and read them back. Capability introspection is preferred; if unavailable, a reversible project-local write/read/delete probe may be used. If persistence cannot be established, stop.
6. After seed creation, read back every seed file and required metadata before claiming bootstrap success.

Discovery sequence for semantic existing-project `PROJECT_UPGRADE` / adoption intent:

1. If trustworthy local Orchestration metadata already pins a protocol, continue through the managed-project upgrade flow.
2. If the project is unpinned or lacks trustworthy Orchestration metadata, use the same external discovery hook to read `/Orchestration/protocol/CURRENT.md` and only the exact production STABLE upgrade/adoption source(s) it references.
3. Production legacy adoption always uses the production STABLE pointer. A DRAFT candidate is development/test-only and is never a fallback.
4. Keep this cross-project authorization Orchestration-only and read-only until the loaded STABLE protocol explicitly permits bounded `LEGACY_ADOPTION_PREFLIGHT` target-project control-plane writes.
5. If this path cannot be used, stop with `UPGRADE_BLOCKED_DISCOVERY_UNAVAILABLE`; do not reconstruct the protocol from memory or another project.

The discovery authorization is narrow. It never grants blanket access to `/Orchestration`, other project roots, credentials, devices, accounts or remembered context.

### Bootstrap failure states

Use explicit blockers instead of improvising:

- `BOOTSTRAP_BLOCKED_DISCOVERY_UNAVAILABLE` — the environment has no usable bootstrap hook or cannot resolve the Orchestration bootstrap source.
- `BOOTSTRAP_BLOCKED_PROTOCOL_POINTER` — CURRENT is missing, malformed or references an unavailable release.
- `BOOTSTRAP_BLOCKED_NO_STABLE_PROTOCOL` — production bootstrap has no STABLE production pointer or the pointed release is not STABLE.
- `BOOTSTRAP_BLOCKED_STORAGE_UNAVAILABLE` — persistent target-project create/update/readback capability cannot be established.
- `BOOTSTRAP_BLOCKED_PERSISTENCE_VERIFICATION` — seed writes occurred but mandatory readback does not match the intended seed/metadata.
- `BOOTSTRAP_EXISTING_PROJECT` — the target root already exists; do not overwrite and switch to resume/repair/upgrade routing.
- `UPGRADE_BLOCKED_DISCOVERY_UNAVAILABLE` — an unpinned existing project cannot load the production upgrade/adoption contract through the external discovery hook.
- `UPGRADE_BLOCKED_PROTOCOL_POINTER` — the production pointer needed for upgrade/adoption is missing, malformed or unavailable.
- `UPGRADE_BLOCKED_NO_STABLE_PROTOCOL` — production upgrade/adoption has no valid STABLE target; never fall back to a DRAFT candidate.

A blocked bootstrap must report the exact blocker and must not claim that the project was initialized.

## Bootstrap state machine

### B0 — Detect intent

Determine that the user wants to create or initialize a project. Extract the project name/code if supplied. Do not demand a magic keyword.

### B1 — Discover and load global protocol

Run the deterministic discovery sequence above. State the exact draft/STABLE release being used and whether the flow is development/test or production.

### B2 — Determine project state

Check whether a project root already exists.

- If no: new-project flow.
- If yes: do not overwrite; switch to resume/repair/upgrade decision.

### B3 — Give Project Instructions snippet

For a new project, output one short copy-paste instruction for the ChatGPT Project settings. It should establish that project Library files are persistent project context, define root INIT/INDEX entry points and forbid cross-project context unless explicitly authorized.

Showing the snippet is not itself a stop gate. Continue bootstrap when safe. Stop for user action only if the environment actually requires that setting to be installed before persistence or safe continuation is possible.

### B4 — Persistent-storage preflight and minimum seed

Verify persistent target-project write/readback capability, then create only what is needed initially:

```text
/<PROJECT>
  INIT.md
  INDEX.md
  STATUS.md
  AGENTS.md
```

Create task/branch/audit/handoff/result folders only when the first real task requires them. When persistent parallel workstreams are needed, use the normative branch lifecycle rather than ad-hoc chat-only labels.

Persist at least:

```text
project_name
project_code
created_at
protocol_created_with
protocol_current_local
update_policy
current_stage
current_gate
next_chat_serial
```

The bootstrap chat consumes project-wide serial `01`. Therefore a newly initialized project persists `next_chat_serial: 02` before bootstrap can be declared successful.

Default `update_policy`: `EXPLICIT_MIGRATION`; never silently adopt a newer global release.

Read back all four seed files and required metadata. A failed/mismatched readback yields `BOOTSTRAP_BLOCKED_PERSISTENCE_VERIFICATION`.

### B5 — Capture intent from the Conductor

Use one low-friction prompt:

`Опишите, что нужно сделать и какой результат ожидаете. Если есть сроки, ограничения, запреты или обязательные условия — добавьте их.`

Do not force the Conductor through a long form when ordinary prose is sufficient.

### B6 — Normalize intent

Convert the response into structured project state:

- goal;
- expected outcome;
- scope;
- constraints;
- known sources/resources;
- unknowns;
- safety/approval gates;
- first stage;
- completion criteria.

Ask a follow-up only for information that blocks a safe or correct next step.

### B7 — Select workflow

Choose the smallest role chain appropriate to risk and ambiguity.

Examples:

- simple bounded task: `Coordinator/Executor`;
- uncertain architecture: `Strategist -> Auditor -> Coordinator/Executor`;
- missing facts: insert `Researcher` before strategy/audit;
- state-changing/high-impact work: require independent audit/preflight and explicit user gates where applicable.

### B8 — Persist and route

Create the first task/branch artifacts, update INDEX/STATUS, and either continue in the bootstrap chat or allocate a new project-wide chat serial and produce a complete handoff.

The bootstrap chat may continue as coordinator if no role/context boundary requires replacement.

## Project Instructions snippet model

The bootstrap agent should generate a project-specific copy-paste snippet equivalent to:

```text
Используй файлы Library этого проекта как постоянный проектный контекст. Перед работой начинай с /<PROJECT>/INIT.md и /<PROJECT>/INDEX.md, затем читай только материалы, относящиеся к текущей задаче. Не используй файлы, доступы или контекст других проектов без явного разрешения текущего проекта или пользователя.
```

The exact root must be substituted by the bootstrap agent.

## Global protocol versioning

Use semantic releases:

- MAJOR — incompatible orchestration/metadata contract change;
- MINOR — backward-compatible capability or rule addition;
- PATCH — clarification/fix that does not alter project contract.

Draft metadata uses creation/update fields. `released_at` is reserved for actual release promotion.

A release records:

```text
version
status: DRAFT | STABLE | DEPRECATED
draft_created_at
draft_updated_at
released_at        # only after promotion to STABLE/DEPRECATED release event as applicable
supersedes
compatibility
migration_required
```

`CURRENT.md` must distinguish a development candidate from the production STABLE pointer. New production projects use only the production STABLE pointer.

Once a release is promoted, its historical file is immutable. Corrections are new releases, not in-place rewriting of historical releases. A DRAFT candidate may be revised until promotion.

## Existing project pinning

Every project stores:

```text
protocol_created_with: x.y.z
protocol_current_local: x.y.z
```

A global update does not automatically change `protocol_current_local`.

This prevents a project from changing behavior merely because the global instruction evolved.

## PROJECT_UPGRADE flow

Trigger examples:

- `обнови проект по новой инструкции`
- `upgrade project`
- `проверь новую версию протокола`

Default policy is `EXPLICIT_MIGRATION`.

### Managed Orchestration projects

If the project already has trustworthy `protocol_current_local` and authoritative `next_chat_serial`:

1. Read project INIT/STATUS, local overrides and pinned protocol version.
2. Read global CURRENT and the target release.
3. Compare releases and project-local overrides read-only.
4. Classify changes: compatible, migration-required, conflicting, irrelevant.
5. Produce a concrete migration plan identifying target version, affected files, intended edits, preserved facts/gates/approvals, validation steps and rollback/recovery approach. No migration write to operational project state is allowed yet.
6. If the migration is nontrivial, breaking, changes authority/approval semantics, or can reopen/alter completed work, send that exact plan to an independent auditor. The pre-approval audit gate is satisfied only by `AUDIT_PASS` on that exact plan; `AUDIT_PASS_WITH_FIXES` or `AUDIT_FAIL` returns the plan to its owner for correction and a fresh independent re-audit.
7. Obtain explicit Conductor approval for the exact audited migration plan and target version.
8. Only after all required audit and Conductor-approval gates are satisfied may migration writes to operational project state occur.
9. Update protocol metadata and changelog/handoff.
10. Read back changed state and verify that completed domain work, confirmed facts, permissions and current gates were not accidentally reset or reopened.

Early Conductor interest/approval before a required audit does not authorize migration writes. It remains non-operative until the exact audited plan is approved for application.

A protocol upgrade must not repeat completed domain work merely because orchestration rules changed.

### PRE_ORCHESTRATION legacy adoption

Semantic existing-project upgrade/adoption intent is itself a discovery trigger even when the project has no local Orchestration metadata. For an unpinned project, load the production STABLE adoption contract through the global discovery hook; if unavailable, stop with `UPGRADE_BLOCKED_DISCOVERY_UNAVAILABLE`. A DRAFT release is development/test-only.

An existing project without trustworthy pinned Orchestration metadata and/or authoritative `next_chat_serial` is classified `PRE_ORCHESTRATION_LEGACY`. It cannot safely enter the managed-project flow because independent audit handoff requires persistent serial state while the legacy project does not have it.

Such a project enters `LEGACY_ADOPTION_PREFLIGHT`.

Before independent `AUDIT_PASS` and post-audit Conductor approval, only bounded control-plane artifacts may be created under:

`/<PROJECT>/orchestration-adoption/`

The control plane may contain only:

- `STATE.md` — authoritative adoption history containing `adoption_run_id`, explicit run state, target protocol, adoption project code, exact plan identity, audit/approval gate, authoritative serial state, and fixed readback/validation records;
- `PLAN.md` — exact migration plan submitted for audit;
- `HANDOFF-*.md` — adoption audit/re-audit handoffs;
- `AUDIT-*.md` — independent audit verdicts bound to one exact plan identity and target version.

These writes are orchestration metadata required to make the migration itself auditable. They do not authorize operational migration and must not alter the legacy project's domain state, completed work, existing gates, business facts, permissions, external systems or production infrastructure.

Before the first serial allocation, persist `adoption_project_code`. Use a trustworthy existing project code when one exists; otherwise derive the control-plane-only code deterministically as `ADP-<H8>`, where `<H8>` is the first eight uppercase hexadecimal characters of SHA-256 over the canonical target project root path string. This adoption code is immutable for control-plane titles/provenance. The final operational `project_code` is stated in the exact migration plan and may differ only as an audited/approved plan change.

If no authoritative Orchestration serial state has ever existed:

1. Initialize a new serial namespace in adoption `STATE.md` with `next_chat_serial: 01` and the persisted `adoption_project_code`.
2. Pre-Orchestration chats are not renumbered and do not retroactively consume the new namespace.
3. Reserve the auditor by normal serial rules: consume `01`, persist/read back `02`, then emit `<ADOPTION_PROJECT_CODE>-01 · Adoption · Auditor`.
4. Retries/replacements/re-audits consume subsequent serials.
5. On successful adoption, carry the authoritative serial state into normal project metadata.

Once a valid adoption `STATE.md` exists, it remains authoritative control-plane history after `FAILED`, `CANCELLED`, retry or replacement. Reserved serials are never reset or reused. Every run persists `adoption_run_id` and one explicit state from at least: `PREFLIGHT`, `AUDIT_PENDING`, `FIXES_REQUIRED`, `AUDIT_PASS`, `AWAITING_CONDUCTOR_APPROVAL`, `APPLYING`, `COMPLETED`, `FAILED`, `CANCELLED`.

A later attempt either resumes a recoverable `adoption_run_id` or creates a new one while carrying forward the same monotonic `next_chat_serial` and prior plan/audit history. If previously valid STATE is missing, corrupt, unreadable or internally inconsistent, stop with `ADOPTION_BLOCKED_STATE_UNAVAILABLE` or `ADOPTION_BLOCKED_STATE_INCONSISTENT`; repair/reconstruct from verifiable persisted artifacts before allocating another serial. Do not silently reinitialize. Old legacy labels that resemble Orchestration serials remain non-authoritative; keep the reserved serial and explicit `Adoption` branch label rather than renumbering.

Before audit handoff, bind the persisted plan to an immutable audit target in `STATE.md`:

```text
plan_revision: <monotonic integer within adoption history>
plan_digest_sha256: <SHA-256 of the exact persisted PLAN.md bytes>
plan_target_protocol: <exact target version>
```

`PLAN.md` must be read back successfully before handoff. The fixed STATE validation record stores artifact path, observed digest, validation timestamp/result and matching revision. Every audit verdict and the post-audit Conductor approval must identify the same `plan_revision`, digest and target version. Any PLAN content change increments the revision, produces a new digest, invalidates the prior `AUDIT_PASS` and approval for application, and requires a fresh independent audit followed by new post-audit approval.

Legacy adoption sequence:

1. Inspect legacy project read-only and classify it.
2. Build the exact migration plan in memory.
3. Persist only the bounded adoption control plane and exact `PLAN.md`; read it back, establish the exact plan identity and set `AUDIT_PENDING`.
4. Reserve a serial and route that exact plan identity to a separate independent auditor.
5. The auditor may write its verdict/control-plane run-state only; it does not implement the migration it audits.
6. `AUDIT_PASS_WITH_FIXES` / `AUDIT_FAIL` leaves the run in `FIXES_REQUIRED`; corrections create a new plan revision/digest and require a fresh independent re-audit.
7. `AUDIT_PASS` is valid only for the named plan identity and advances to `AWAITING_CONDUCTOR_APPROVAL`.
8. Obtain explicit Conductor approval naming that same plan identity and target STABLE version.
9. Only then set `APPLYING` and perform operational migration writes.
10. Read back migrated state; verify preserved facts, completed work, gates and permissions; persist normal Orchestration metadata including carried-forward `next_chat_serial`; mark `COMPLETED`; retain/archive adoption artifacts as provenance.

If adoption fails or is cancelled, record `FAILED` or `CANCELLED`. The project remains legacy, while existing STATE, plan identities, audit artifacts and serial history remain authoritative provenance and must not be represented as migrated.

This is a backward-compatible capability addition for legacy projects, so it belongs in a MINOR release rather than a PATCH under the versioning contract above.

## Local AGENTS.md contract

The global protocol owns universal bootstrap, lifecycle, chat-serial, source-priority, handoff and upgrade mechanics.

A project's local `AGENTS.md` contains only:

- project-specific roles and authority boundaries;
- project-specific constraints/prohibitions;
- project-specific resource/access rules;
- project-specific approval ownership;
- explicit local protocol overrides/deltas with scope and rationale;
- a pointer to `protocol_current_local` / the pinned global release.

Do not copy universal protocol text into every local `AGENTS.md`. If a project changes a global rule, record only the local delta and its scope.

## Universal source-priority / conflict-resolution contract

Within project scope, resolve conflicts in this order:

1. Current explicit Conductor/user instruction for intent, scope and authorization.
2. Project-specific mandatory safety/legal/business constraints and explicit local protocol overrides.
3. Verified current state of the target system/resource.
4. Current task/audit/result/handoff for the active branch.
5. Active branch `BRANCH.md` and branch `STATUS.md`.
6. Project `STATUS.md` for project-wide state/cross-branch coordination.
7. Project `INIT.md`, `INDEX.md` and local `AGENTS.md`.
8. The project's pinned global protocol release.
9. Chat history, model memory or inferred recollection.

A lower-priority source cannot silently override a higher-priority one. Current user instruction governs desired action/permission, but does not convert a contradicted factual observation into a fact; when intent and verified state differ, preserve both explicitly. If current instruction conflicts with a project-specific mandatory safety/legal constraint, that hard constraint blocks execution. A mutable business rule/local override changes only when the current instruction explicitly changes it and the new rule is persisted. Mandatory platform/system safety constraints remain outside and above this project contract.

## Independent audit contract

When a gate requires an independent audit:

- the auditor runs in a separate chat/agent context from the author/executor whose work is being audited;
- the auditor must not mutate the audited implementation while issuing the verdict;
- findings are returned to the owning author/editor/executor for correction;
- any required re-audit occurs only after corrections are persisted;
- a `fresh independent re-audit` means a new audit chat/agent context that did not perform the fixes being judged.

Roles may be combined only when the gate is not explicitly independent.

## Chat serial allocation and lifecycle

Universal title format:

`<PROJECT_CODE>-<NN> · <Branch> · <Role/Task>`

`next_chat_serial` means the next unused project-wide serial, not the current chat number, branch number, stage or gate.

Rules:

1. The first bootstrap chat consumes `01`; after its allocation the persisted `next_chat_serial` is `02`.
2. To allocate a new chat, read the authoritative current `next_chat_serial = N` immediately before allocation.
3. Reserve `N` for that chat and persist `next_chat_serial = N + 1` before emitting the handoff/title.
4. Verify the increment by readback before publishing `CHAT_TITLE`.
5. A reserved serial is never reused even if the chat is abandoned, replaced, archived, deleted or never started.
6. Replacements/retries/re-audits use the next unused project-wide serial.
7. Allocation is a project-level critical section. Parallel branches must serialize allocation through the authoritative coordinator/state writer; if conflict-safe write semantics are unavailable, branch agents must not allocate independently.
8. Display at least two digits for `01`-`99`; continue naturally at `100+`.

The first chat is not a permanent special object. After state is persisted, it can be archived/replaced like any other agent.

## Required next-agent handoff

When `NEW_AGENT_REQUIRED: YES`, the handoff must include:

- exact `CHAT_TITLE` with an already reserved serial;
- next role and concrete objective;
- mandatory project paths to read;
- current run-state/gate/result;
- confirmed facts that must not be re-asked or re-proved without new contradictory evidence;
- permissions/approvals already granted, including their scope and any limits;
- completed/closed gates and work that must not be repeated;
- active blockers/open gates;
- prohibitions and stop-gates;
- expected artifacts/result paths;
- completion criterion;
- the lifecycle/completion contract the next agent must apply;
- for branch-scoped work: immutable `branch_id`, canonical branch paths, branch state and material cross-branch dependency/shared-state authority.

A handoff must be sufficient for a replacement chat to continue without relying on prior chat history.

## Persistent branch lifecycle

A branch is a persistent sub-workstream under one project root. Prefer a branch when the work has a distinct goal/lifecycle but shares the project's authority, constraints, root context and substantial resources. Prefer a separate project when it needs independent authority/context isolation, separate project-wide rules or a materially separate long-term outcome.

### Branch identity and seed

Semantic user intent is sufficient: e.g. "создай ветку Cron", "дизайн отдельно", "ведём документы отдельной веткой". No magic command is required.

Every branch receives an immutable project-unique `branch_id` and human-facing `branch_label`. Use an explicit valid lowercase ASCII `[a-z0-9][a-z0-9-]*` id when supplied; otherwise derive it deterministically from the label via Unicode NFKD -> ASCII alphanumeric runs -> lowercase kebab-case. If normalization is empty, use `branch-<h8>` from the first eight lowercase hex characters of SHA-256 over the exact UTF-8 label bytes. Collision suffixing considers current, pending, historical and tombstoned identities. Once reserved/allocated, an id is permanently consumed and is never reused for unrelated work. Label changes do not change identity.

Minimum persistent branch structure:

```text
/<PROJECT>/branches/<branch_id>/
  BRANCH.md
  STATUS.md
```

`BRANCH.md` contains at least branch id/label, created_at, purpose, goal, scope and completion criteria. `STATUS.md` contains dynamic state, current stage/gate, next step, owner role, updated_at, blocker/resume trigger where applicable, and append-only transition history. Each successful state transition records a stable transition id, from/to state, reason, provenance and timestamp. Additional branch INDEX/tasks/results/audits are lazy-created only when useful.

Root `INDEX.md` owns both the branch registry and identity non-reuse ledger (id/current label/path plus mutation state). Entries remain discoverable after completion/cancellation/archive; even explicitly deleted branch content leaves an identity tombstone. Root `STATUS.md` owns the compact live project-wide branch overview and material cross-branch dependencies/conflicts. Detailed branch state is authoritative in branch `STATUS.md`; root summary mismatch is repaired from verified branch state. Root project stage/gate is not used to flatten all branch gates into one.

### Crash-safe creation / rename / recovery

Branch identity/registry mutation is a project-level serialized critical section. Creation first persists/read-backs a root registry reservation `PENDING_CREATE` with `mutation_id`, branch id, label and path; only then writes/read-backs branch seed and root summary; finally it marks the registry entry `STABLE` and reads back all affected artifacts. A pending reservation immediately consumes the id.

Rename preserves id and journals `PENDING_RENAME` with a mutation id and old/target labels before changing `BRANCH.md` and root summary; only after readback is it finalized `STABLE`. The canonical branch directory does not move merely because its human label changes.

An interrupted pending mutation is recovered under the same id/mutation id. A pre-existing unregistered `branches/<id>/` seed is `BRANCH_BLOCKED_REGISTRY_INCONSISTENT`, not an ordinary collision that may be skipped with `-2`: inspect immutable identity/history, then either register/recover that same logical identity or perform an explicit repair/rollback that preserves the encountered id as consumed before allocating anything else. Root registry, branch seed and root summary must be read back after repair before the blocker clears.

Creating a branch does not consume a chat serial.

### Lifecycle and reopen

Branch states: `ACTIVE`, `PAUSED`, `BLOCKED`, `COMPLETED`, `CANCELLED`, `ARCHIVED`. `PAUSED` stores a resume trigger; `BLOCKED` stores blocker + owner/trigger under anti-stall. Every successful transition appends transition evidence before success is claimed.

Reopening completed/cancelled/archived work requires an explicit authorized decision, preserves branch id/history/results/prior gates and normally results in `ACTIVE`. It may result in `PAUSED` or `BLOCKED` only when the decision/current verified condition explicitly establishes that state and its required trigger/owner. Persist prior state, resulting state, reopen reason, provenance and timestamp; synchronize/read back required same-branch root registry/summary before execution resumes. Normal lifecycle archives history rather than deleting it.

### Narrow root control-plane authority and parallel scope

Branch-scoped authority does not imply sibling/root authority. A branch may write its own artifacts and explicitly scoped resources. Sibling writes are never implicit.

However, an authorized lifecycle action on one branch necessarily authorizes the protocol-required **narrow root branch-control-plane synchronization** for that same branch: root registry/label/path/mutation fields and root STATUS branch summary plus material dependency/conflict entries directly involving it. This does not authorize unrelated root project metadata, business/domain facts, sibling content, shared resources, permissions/constraints or integration decisions. Any broader root/shared change still requires explicit authority and normal root coordination. Incompatible concurrent shared-state changes stop as `BRANCH_BLOCKED_SHARED_CONFLICT` rather than last-writer-wins.

Project-wide chat serials remain globally monotonic across branches. Cross-branch dependencies reference `branch_id`, not chat titles.

### Completion and integration

Substantive completion persists branch `RESULT.md` (or equivalent referenced artifact) with outcome vs criteria, outputs, confirmed facts/decisions, unresolved risks and any proposed project/sibling integration. Branch completion does not automatically promote branch claims into root/shared authority. Narrow lifecycle synchronization may mark integration pending, but actual root/shared integration requires separately authorized project-level change. Root coordinator records pending/completed integration in root STATUS.

Branch chats read project INIT -> INDEX -> root STATUS -> branch BRANCH -> branch STATUS -> referenced task/audit/handoff. Handoffs carry immutable branch id/path. Visibility of sibling branch files is not authorization.

### Compatibility

The branch lifecycle is a backward-compatible MINOR capability. Existing projects pinned to `0.2.0` are unchanged until explicit PROJECT_UPGRADE. Existing ad-hoc workstreams should be mapped/preserved during upgrade rather than recreated or renumbered, and discovered branch identities are added to the non-reuse registry/ledger.

## Success criteria for the universal method

A project bootstrap is successful only when:

1. deterministic bootstrap discovery succeeded;
2. the exact protocol release used is explicit and valid for the current mode;
3. persistent storage capability was established;
4. the Conductor received the Project Instructions snippet;
5. a minimal project root exists and passes readback;
6. goal/outcome/constraints are persisted or explicitly marked unknown;
7. current stage/gate and next action are unambiguous;
8. `next_chat_serial` has deterministic project-wide semantics;
9. another chat can take over without reading prior chat history;
10. future global protocol updates cannot silently change the project's behavior.

## Deliberately postponed

Not part of this initial strategy:

- automatic creation of ChatGPT Projects through UI automation;
- automatic insertion of Project Instructions into product settings;
- automatic spawning/renaming/archiving of chats where the product surface does not expose those capabilities;
- an external employee/agent implementation of the Conductor role.

The protocol defines the interface now so those capabilities can be added later without redesigning project files.
