# Orchestration

Current public production protocol: **0.4.3 STABLE** (2026-11-08).

The exact GitHub production version is specified in [Orchestration/protocol/CURRENT.md](Orchestration/protocol/CURRENT.md). The supported STABLE releases are under [Orchestration/protocol/releases/](Orchestration/protocol/releases/), including the [0.4.3 protocol](Orchestration/protocol/releases/v0.4.3/PROTOCOL.md).

**Fresh ChatGPT accounts:** installing the GitHub skill/plugin does not require a pre-existing `/Orchestration/` Library tree. For new-project bootstrap, the [skill](skills/orchestration/SKILL.md) reads the production pointer and exact STABLE release from GitHub, then initializes the **target** project and verifies its durable files. Missing `/Orchestration/protocol/CURRENT.md` in the new account is not a bootstrap blocker. Do not substitute a hard-coded 0.3.0.

Existing projects preserve their own locally adopted protocol version until explicitly upgraded. Their live Library state is authoritative; GitHub is the source of portable protocol files, not a synchronized copy of account-specific project data.

An optional local offline/managed protocol import remains documented in [runtime-package.json](packaging/manifests/runtime-package.json), with files and SHA-256 checksums. The repository snapshot allowlist is in [repository-files.json](packaging/manifests/repository-files.json). Local protocol import is **not required** for GitHub-based first-run bootstrap. GitHub source publication does not by itself establish that a previously linked plugin has refreshed in another account.

Never export secrets, accounts, sessions, or unrelated projects.
