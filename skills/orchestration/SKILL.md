---
name: orchestration
description: Bootstrap, adopt, update, and coordinate Orchestration-managed ChatGPT Projects. Use for "создай проект", "запускай проект", "init", "обнови проект", "создай ветку", branch handoffs, and protocol maintenance.
---

# Orchestration

This skill is a thin entry point to the versioned Orchestration protocol. It must work in a fresh ChatGPT account that installed only the GitHub plugin. Do not require a pre-existing `/Orchestration/` Library tree.

## Resolve the correct protocol

1. **New project / fresh account**: Read the public GitHub source at `https://github.com/ilyasclick/orchestration`. Fetch `Orchestration/protocol/CURRENT.md` from GitHub (via an available GitHub connector or web reader), then read the **exact production STABLE release** identified by that pointer from the same repository. If the release has baseline dependencies, read the exact referenced releases as needed. Record the retrieved source/ref. The repository pointer is version authority for new-project bootstrap; it is **not** evidence that a Library protocol has already been installed. Absence of `/Orchestration/protocol/CURRENT.md` in the target account is normal and must not block bootstrap.
2. **Existing project**: Identify the target project's own `<PROJECT_ROOT>/Protocol/adopted/` marker, or its confirmed legacy `INIT.md` if no marker exists. Preserve that project's locally adopted STABLE version. Read the exact historical release from authorized local files when available; otherwise retrieve it from GitHub without upgrading the project.
3. **Explicit global-upgrade request**: Resolve GitHub `CURRENT.md` for the offered production version; do not adopt it for any existing project without the user's separate permission.
4. **Maintainer work on Orchestration itself**: Use the locally adopted version and current authorized Library state for project operations. GitHub is the portable release source, not a synchronized mirror of account-specific branch, project, or permission state.

Do **not** compare the GitHub version with a hard-coded bundled version, including 0.3.0. Do not treat a cached/bundled version as latest. If GitHub is unavailable for a fresh bootstrap, report the source-access failure; never guess a production version or claim successful initialization.

## Execute the user's task

- Run `PROJECT_BOOTSTRAP` from the resolved STABLE protocol to create the **target project's** durable files. Bootstrap may create Library state under the new project's authorized root; it must not require a separate Orchestration Library installation first. Confirm actual writes by Library readback.
- For an existing project, follow the locally adopted protocol and existing project-specific instructions. Never silently perform `PROJECT_UPGRADE`.
- Follow branch, lifecycle, authority, approval, and history rules in the selected STABLE release. Do not read or modify unrelated projects without authorization.
- When project settings cannot be updated through a supported action, provide the actual instructions for the user to apply; do not claim those settings changed.
- Report source version and actual completion. Do not claim a GitHub update automatically refreshed an already installed plugin instance.

## GitHub release and distribution

Public portable source: `https://github.com/ilyasclick/orchestration`. Read `references/DISTRIBUTION.md` before importing or publishing. Optional installation of a local `/Orchestration/protocol/` runtime cache is **not a prerequisite** for GitHub-based new-project bootstrap. The account's Library remains authoritative for the actual project state and locally adopted versions. Never publish credentials, sessions, or unrelated project content.
