---
name: orchestration
description: Bootstrap, adopt, update, and coordinate versioned Orchestration projects. Use for "создай проект", "запускай проект", "init", "обнови проект", "создай ветку", project handoffs, and protocol maintenance. ChatGPT Projects and Library operations require compatible host tools.
license: Proprietary. See LICENSE
compatibility: Requires read access to public GitHub for fresh bootstrap and authorized persistent project storage for state changes. ChatGPT Projects/Library operations require ChatGPT-compatible tools.
metadata:
  author: ilyasclick
  version: "0.2.0"
---

# Orchestration

A portable Agent Skill entry point for the versioned Orchestration protocol. The skill provides instructions, not extra permissions or a universal project-storage API. It must work in a fresh account without a pre-existing `/Orchestration/` Library tree. Read [references/HOST-CAPABILITIES.md](references/HOST-CAPABILITIES.md) when adapting to a host other than ChatGPT or when a required tool is missing.

## Check host capabilities

1. Determine whether the host can read public GitHub files, read and write the **authorized target project's** persistent state, and read back writes. Do not infer permissions from the skill's installation.
2. Treat ChatGPT Projects, Library, chat lifecycle, and project settings as **host-specific**. Do not simulate them with an unrelated filesystem or claim that an unsupported host changed them.
3. If a required capability is missing, report the exact blocker and any verified read-only result. Never claim bootstrap, installation, or migration succeeded without durable readback.

## Resolve the correct protocol

1. **New project / fresh account**: Read `https://github.com/ilyasclick/orchestration` and fetch `Orchestration/protocol/CURRENT.md` from public GitHub using an available GitHub connector or web reader. Resolve the **exact production STABLE release** identified by that pointer from the same repository snapshot/ref. If the release declares baseline dependencies, read those exact releases. Record the retrieved ref. The GitHub pointer is version authority for fresh bootstrap, **not** proof that the target account has an Orchestration Library tree. Missing `/Orchestration/protocol/CURRENT.md` in a new account must not block bootstrap.
2. **Existing project**: Inspect only the authorized target project's `<PROJECT_ROOT>/Protocol/adopted/` marker, or confirmed legacy `INIT.md` if no marker exists. Preserve the project's adopted STABLE version. Read the exact historical release from authorized local files when available; otherwise fetch it from GitHub without upgrading.
3. **Explicit global upgrade**: Resolve the GitHub production pointer for the offered version. Do not adopt it for an existing project without separate project-specific authorization.
4. **Orchestration maintenance**: Follow the locally adopted release and the authorized Library branch state. GitHub is a portable release source, not a mirror of account-specific projects or permissions.

Never compare the GitHub version with a hard-coded bundled version, including 0.3.0. Never use a cached version as the current release. If GitHub cannot be read for fresh bootstrap, report the source-access failure instead of guessing a version.

## Execute the user's task

- Execute `PROJECT_BOOTSTRAP` from the resolved STABLE protocol **only if** the host supports the required target-project operations. Bootstrap may create authorized target-project Library state; a separate global Orchestration Library import is not required for GitHub-first bootstrap. Verify actual writes by readback.
- For existing projects, follow their locally adopted protocol and project instructions; never silently run `PROJECT_UPGRADE`.
- Respect branch lifecycle, authority, approvals, isolation, and history requirements from the selected release. Never read or modify unrelated projects without authorization.
- When host project settings cannot be changed through supported actions, provide exact manual steps; never report a settings change that did not occur.
- Report source ref, protocol version, observed operations, readback evidence, and blockers. Publishing GitHub source does not prove an already installed plugin or skill refreshed in another account.

## Distribution

Public source: `https://github.com/ilyasclick/orchestration`. Read [references/DISTRIBUTION.md](references/DISTRIBUTION.md) before importing or publishing. The optional local runtime cache is not required for GitHub-based new-project bootstrap. The target account's persistent state remains authoritative for its projects. Never export secrets, sessions, or unrelated project data.


## Candidate modular contracts (nonproduction)

For development of the next protocol release, consult [semantic commands](references/COMMANDS.md), [resolver](references/RESOLVER.md), [storage/history](references/STORAGE.md), [per-project migration](references/MIGRATION.md), and [release/audit](references/RELEASE.md). These are **review candidates**, not replacements for a project's locally adopted STABLE protocol. Do not invoke them to bypass legacy pin rules, create monitoring, move Library objects, change CURRENT, or promote a release. The 14 intents are natural-language workflows, not proof of CLI/voice routing. Release promotion requires exact-payload independent acceptance and explicit owner approval.
