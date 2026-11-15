---
name: orchestration
description: Bootstrap, adopt, update, and coordinate Orchestration-managed ChatGPT Projects. Use for requests such as "создай проект", "запускай проект", "init", "обнови проект", "создай ветку", branch handoffs, or Orchestration protocol maintenance. Read the project's locally adopted STABLE release and keep durable state in Library; do not treat GitHub as live project state.
---

# Orchestration

Use this skill as a **thin entry point** to the existing versioned Orchestration system, not as a replacement for its protocol. This skill must work after subsequent protocol releases without changing its own hard-coded protocol version.

## Resolve the correct protocol

1. Identify the user's **current target ChatGPT Project**. Do not import other projects' context or authorization. For an existing project, discover `<PROJECT_ROOT>/Protocol/adopted/`, then `<PROJECT_ROOT>/INIT.md` if no confirmed marker exists. Resolve the **locally adopted** version. Do not silently upgrade it.
2. Obtain protocol content from the target account's persistent **Library**, using the available Files access. For new project bootstrap and explicitly requested global-upgrade targets, read `/Orchestration/protocol/CURRENT.md`, then the **exact production STABLE release** it identifies. Historical releases may have different paths. Do not guess paths or fall back to a draft.
3. For maintenance of `/Orchestration` itself, read `/Orchestration/INIT.md`, `/Orchestration/INDEX.md`, `/Orchestration/STATUS.md`, `/Orchestration/protocol/CURRENT.md`, the exact STABLE release, and only the task-relevant branch/audit/handoff. Historical INDEX/STATUS snapshots do not supersede newer verified events.
4. If the Library's required source files are unavailable, use the authorized GitHub repository only for read-only provenance or as an explicit source of a verified portable import. Never claim that fetching GitHub data installed a local protocol, and never invent missing project state.

## Execute the user's task

- For new-project commands, run the exact `PROJECT_BOOTSTRAP` flow in the selected STABLE protocol. Keep the target project root, source and generated control-plane files distinguishable. Confirm saved files with a real Library readback.
- For an existing project, respect its local release and existing project-specific instructions. A global STABLE change is not consent to `PROJECT_UPGRADE`.
- For branch creation and lifecycle, follow the locally adopted protocol, reserve identities where required, persist branch state/evidence, and preserve existing approvals and history. Avoid duplicate branches for the same work.
- For `PROJECT_UPGRADE`, follow the exact target release and issue the complete universal Project Instructions when required. Never claim ChatGPT Project settings changed without observing the change through a supported action.
- Preserve authority boundaries, approval gates, and explicit deletion rules. Do not overwrite Library files if forbidden by the current release. Record real outcomes, remaining blockers, and the next action; never claim an audit or a scheduled task completed without verification.

## GitHub release and cross-account distribution

The public source of portable Orchestration distributions is `https://github.com/ilyasclick/orchestration`. The authoritative operational state remains in each account's Library. Read `references/DISTRIBUTION.md` before importing from GitHub, modifying this skill, or publishing. Never export credentials, sessions, unrelated project data, or local-only installation records.

A skill install and a protocol install are **different operations**: installing this skill makes the workflow available where the host supports skills; the account must also have an accessible, verified runtime protocol in `/Orchestration/protocol/`. Conversely, protocol files in Library do not prove this skill is registered or activated. Describe each result separately and verify actual activation where possible.