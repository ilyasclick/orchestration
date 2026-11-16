# Branch closure criteria workflow

Command ID: `BRANCH_CLOSURE_CRITERIA`
Canonical phrase: «Критерии закрытия ветки <branch>»
Aliases: «Критерии закрытия ветки» (only with unambiguous current branch context); «Покажи критерии закрытия <branch>»; «Что осталось для закрытия ветки <branch>»; «Проверь готовность ветки <branch> к закрытию».

This is a natural-language skill workflow, not a shell command, slash command, CLI parser, or promise of a dedicated host-side handler.

## Parameters

- `branch` — conditionally required. Accept an exact branch_id, canonical Library path, or unique branch label. If omitted, use the current branch only when unambiguous; otherwise ask one question.
- `as_of` — optional observation time. Default to the time of the actual source read, not a historical report date.
- `evidence_scope` — optional. Default to branch-local evidence and explicitly referenced project-level sources. Do not read another project, account, device, or external system without permission.
- `detail` — optional. Default to a complete criterion-by-criterion report. A concise response may compress explanations but must not hide criteria, blockers, or unverified claims.

Parameters are expressed in ordinary language. Do not invent `--branch`, `--json`, `--audit`, or other CLI flags.

## Resolve project, protocol, and branch

1. Establish the target project root and determine its locally adopted protocol. Prefer a confirmed `Protocol/adopted/v<version>/` marker; otherwise use the exact version recorded in the project's INIT.md or other authoritative local adoption evidence. Global CURRENT alone does not migrate an existing project. If the local pin cannot be resolved, state `LOCAL_PROTOCOL_UNRESOLVED`; do not silently assume the global version is locally adopted.
2. Read the exact release applicable to that project. Do not combine rules from different releases.
3. Resolve branch identity by the protocol version:
   - For 0.4.0 and later, inspect the actual Library folders `branches/<branch_id>/` and `branches/archive/<branch_id>/`. The active path means the branch is active; the archive path means archived. If both exist, report `BRANCH_LOCATION_CONFLICT`; if neither exists, report `BRANCH_NOT_FOUND`. Do not invent a replacement identity.
   - For 0.4.0, `BRANCH.md` is part of the branch identity contract.
   - For 0.4.1 and later, a branch folder name is sufficient for a simple branch; read `BRANCH.md` when present or when the branch's purpose/scope/criteria need more than the folder name can express.
   - For a project locally pinned to 0.3.0, apply that exact legacy release's branch registry and lifecycle requirements. Do not carry those requirements into 0.4.0+.
4. In 0.4.0+, root `INDEX.md`, root `STATUS.md`, branch-local `STATUS.md`, `RESULT.md`, `HANDOFF.md`, and `next_chat_serial` are not universal mandatory branch artifacts. Root INDEX may be useful navigation or a project-specific supplementary view, but absence of a row is not a branch-existence blocker when the actual folder is present. A missing branch-local STATUS.md is not a blocker.
5. In 0.4.0+, stages, completion, blockers, and decisions are represented by relevant new events under the project's `Status/` folder. Inspect relevant event folders with pagination and readback; do not treat a stale file or a date in a folder name as proof of current state. Under 0.4.3, legacy INDEX.md/STATUS.md may be read as historical context but must not override newer verified evidence.
6. If a current project navigation/index file explicitly points to a replacement status file, read that exact replacement. If a legacy STATUS.md is inaccessible, report that fact and use only a verified, explicitly referenced current source; do not invent content.

## Build the criterion list

Use, in priority order, explicit user completion criteria, the current branch identity/scope document, approved scope changes, applicable protocol requirements, and relevant project/branch events. Use handoffs, plans, task registers, test reports, result records, and audit reports as evidence and context.

Do not manufacture extra criteria from templates, prior-version conventions, or generic best practices. If no authoritative criterion source can be found, report `NOT_VERIFIABLE` rather than inventing a gate. Preserve superseded criteria as history but assess only the latest authorized scope; show any change and its decision provenance.

## Criterion statuses

Assign exactly one status to each criterion:

- `PASS` — current evidence directly proves the whole criterion.
- `PARTIAL` — some subconditions are proven, others remain open.
- `FAIL` — verified state contradicts the requirement.
- `BLOCKED` — a concrete technical, permission, or dependency blocker prevents progress or verification.
- `NOT_STARTED` — no evidence of substantive work.
- `NOT_VERIFIABLE` — available sources do not prove the state or the source is inaccessible/ambiguous.
- `NOT_APPLICABLE` — criterion is explicitly out of scope or inapplicable, with a cited reason.

Evidence classes:

- `LIVE_READBACK` — direct current observation of the target resource.
- `LIBRARY_READBACK` — exact saved Library object read again.
- `TEST_RESULT` — reproducible test with input, expected result, and actual result.
- `INDEPENDENT_AUDIT` — verdict from a separate agent/chat context that did not author or fix the target.
- `HISTORICAL_REPORT` — evidence of a past observation, not current state by itself.
- `SELF_REPORT` — executor statement without primary corroboration.
- `INFERENCE` — reasoned conclusion from identified sources; distinguish it from direct observation.

A plan, handoff, filename, status label, or self-report does not establish PASS without supporting evidence.

## Required report

1. Branch identity: project root, branch_id/path/label, physical location, lifecycle as defined by the locally applicable protocol, and protocol-version confidence.
2. Overall readiness: one of `NOT_READY`, `BLOCKED`, `READY_FOR_INDEPENDENT_ACCEPTANCE`, `READY_FOR_CONDUCTOR_DECISION`, or `COMPLETION_CRITERIA_MET`.
3. Every criterion: stable number, source, exact requirement, status, evidence with path and observation time, missing evidence, remaining steps, owner/role, prerequisite/permission, and measurable postcondition.
4. Independent acceptance: whether required by the source criteria/protocol/Conductor; exact scope and immutable digest where applicable; auditor context; actual verdict; remaining findings; and whether fresh re-audit is needed after fixes.
5. Blockers and limitations: missing/inaccessible sources, incomplete enumeration, unresolved dependencies, and explicit scope restrictions.
6. Side effects: state that the command did not change lifecycle, move/delete files, run external actions, launch an auditor, or write status records.

## Overall readiness and lifecycle separation

- `NOT_READY` — at least one required criterion is not PASS.
- `BLOCKED` — branch/protocol/source resolution or a required action is blocked by a concrete condition.
- `READY_FOR_INDEPENDENT_ACCEPTANCE` — executor criteria pass but a required independent review is pending.
- `READY_FOR_CONDUCTOR_DECISION` — all criteria and required audits pass; a separate Conductor decision remains.
- `COMPLETION_CRITERIA_MET` — all criteria and required acceptance gates pass. This is an assessment only.

For 0.4.0+, do not invent branch lifecycle states such as `COMPLETED` or `CANCELLED` from the 0.3.0 contract. Physical placement distinguishes active from archived; completion and blockers are recorded as events. `COMPLETION_CRITERIA_MET` does not archive or move the branch. For a 0.3.0-pinned project, use its exact lifecycle states and transition rules.

## Independent acceptance

Do not invent an independent audit requirement. It is required only when the original criterion, applicable protocol, or Conductor decision requires it. If required, the auditor must use a separate context and remain read-only; the exact target revision/digest must be identified. `AUDIT_PASS_WITH_FIXES` and `AUDIT_FAIL` do not pass the gate. After corrections, the auditor must inspect the exact new revision. A scheduled task or Automation is not an audit verdict. If no independent mechanism is available, report the exact state without simulating independence.

## Acceptance tests for the workflow

1. Exact branch_id/path in an active folder, with no root INDEX row: resolve as active; do not report registry inconsistency.
2. 0.4.1+ branch folder without BRANCH.md or branch STATUS.md: resolve the simple branch by folder name; do not invent missing mandatory files.
3. Branch under `branches/archive/`: report archived, not active.
4. Same branch_id present in active and archive folders: report `BRANCH_LOCATION_CONFLICT`; do not choose.
5. No matching folder: report `BRANCH_NOT_FOUND`; do not create a replacement.
6. Ambiguous branch label: ask one concise clarification.
7. 0.3.0-pinned target: apply its exact legacy registry/STATUS requirements; do not infer 0.4.x.
8. Historical STATUS conflicts with a newer verified Status event or physical location: report the conflict and apply the exact protocol's source priority.
9. External dependency outside approved evidence scope: do not read it; report dependency and missing proof.
10. Read-only invariant: no branch lifecycle, Library, external system, or automation writes during command execution.

## Implementation status vocabulary

- `SKILL_INTENT_IMPLEMENTED` — the Orchestration skill source contains the workflow and its trigger phrases.
- `SKILL_SOURCE_READBACK_VERIFIED` — the saved plugin source was read back after update.
- `HOST_ACTIVATION_VERIFIED` — a fresh host invocation demonstrably loaded the updated skill; do not infer this from a saved plugin release.
- `DEDICATED_CLI_OR_PARSER` — only when a real registered parser/tool is observed.
- `VOICE_DISPATCH` — only when the separate OrchVoice controller demonstrably dispatches this phrase.
