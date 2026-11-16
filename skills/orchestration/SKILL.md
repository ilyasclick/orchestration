---
name: orchestration
description: Bootstrap, adopt, update, and coordinate Orchestration-managed ChatGPT Projects. Use for requests such as "создай проект", "запускай проект", "init", "обнови проект", "создай ветку", "критерии закрытия ветки", branch handoffs, or Orchestration protocol maintenance. Read the project's locally adopted STABLE release and keep durable state in Library; do not treat GitHub as live project state.
---

# Orchestration

Use this skill as a thin entry point to the existing versioned Orchestration system, not as a replacement for its protocol. This skill must work after subsequent protocol releases without changing its own hard-coded protocol version.

## Resolve the correct protocol

1. Identify the user's current target ChatGPT Project. Do not import other projects' context or authorization. For an existing project, discover `<PROJECT_ROOT>/Protocol/adopted/`, then `<PROJECT_ROOT>/INIT.md` if no confirmed marker exists. Resolve the locally adopted version. Do not silently upgrade it.
2. Obtain protocol content from the target account's persistent Library, using the available Files access. For new project bootstrap and explicitly requested global-upgrade targets, read `/Orchestration/protocol/CURRENT.md`, then the exact production STABLE release it identifies. Historical releases may have different paths. Do not guess paths or fall back to a draft.
3. For maintenance of `/Orchestration` itself, read `/Orchestration/INIT.md`, the current root navigation/index source or its explicitly named replacement, the current status source identified by that navigation source, `/Orchestration/protocol/CURRENT.md`, the exact STABLE release, and only the task-relevant branch/audit/handoff. The legacy `/Orchestration/STATUS.md` may be inaccessible; do not invent its contents or block when a verified current replacement is explicitly identified. Under 0.4.x, root INDEX/STATUS files are not mandatory live branch registries; treat old snapshots as historical context and reconcile branch existence against the version-appropriate branch folders and events.
4. If the Library's required source files are unavailable, use the authorized GitHub repository only for read-only provenance or as an explicit source of a verified portable import. Never claim that fetching GitHub data installed a local protocol, and never invent missing project state.

## Execute the user's task

- For new-project commands, run the exact `PROJECT_BOOTSTRAP` flow in the selected STABLE protocol. Keep the target project root, source and generated control-plane files distinguishable. Confirm saved files with a real Library readback.
- For an existing project, respect its local release and existing project-specific instructions. A global STABLE change is not consent to `PROJECT_UPGRADE`.
- For branch creation and lifecycle, follow the locally adopted protocol. Do not impose a legacy 0.3.0 branch registry, pending-reservation, or branch STATUS.md requirement on a 0.4.0+ project. Under 0.4.0+, inspect the actual active/archive branch folders and Status events; under 0.4.1+, a folder name is sufficient for a simple branch and BRANCH.md is optional when the name adequately identifies it. A 0.4.0 project has its own BRANCH.md requirement. Use the exact pinned release rather than mixing rules across versions.
- For `PROJECT_UPGRADE`, follow the exact target release and issue the complete universal Project Instructions when required. Never claim ChatGPT Project settings changed without observing the change through a supported action.
- Preserve authority boundaries, approval gates, and explicit deletion rules. Do not overwrite Library files if forbidden by the current release. Record real outcomes, remaining blockers, and the next action; never claim an audit or a scheduled task completed without verification.

## Branch closure criteria

Use this workflow when the user asks «Критерии закрытия ветки», «Покажи критерии закрытия <branch>», «Что осталось для закрытия ветки <branch>», or «Проверь готовность ветки <branch> к закрытию». The semantic operation is `BRANCH_CLOSURE_CRITERIA`.

Read and follow `references/BRANCH-CLOSURE-CRITERIA.md`. The command is read-only: it reports criteria, statuses, evidence, remaining work, blockers, and independent-acceptance requirements. It does not close, complete, cancel, archive, delete, or otherwise mutate a branch. It does not create or launch an auditor.

Resolve the target branch from an explicit branch_id, canonical path, or unique label. If omitted, use the current branch only when the current project and branch identity are unambiguous; otherwise ask one concise clarification. Never select a similar branch by guess.

The output must distinguish:
- physical branch lifecycle/location from completion assessment;
- current Library readback from historical report and self-report;
- a documented skill workflow from a dedicated CLI/parser/tool action;
- an independent audit that actually ran from a planned or scheduled audit;
- `COMPLETION_CRITERIA_MET` from any lifecycle transition.

Do not invent criteria or mandatory audits. Trace each criterion to the user's task, branch scope, approved change, or applicable protocol. If a criterion has no authoritative source, mark it `NOT_VERIFIABLE` and explain the gap.

## GitHub release and cross-account distribution

The public source of portable Orchestration distributions is `https://github.com/ilyasclick/orchestration`. The authoritative operational state remains in each account's Library. Read `references/DISTRIBUTION.md` before importing from GitHub, modifying this skill, or publishing. Never export credentials, sessions, unrelated project data, or local-only installation records.

A skill install and a protocol install are different operations: installing this skill makes the workflow available where the host supports skills; the account must also have an accessible, verified runtime protocol in `/Orchestration/protocol/`. Conversely, protocol files in Library do not prove this skill is registered or activated. Describe each result separately and verify actual activation where possible.
