# Orchestration

Orchestration is a portable **AI Agent Skill** for versioned project bootstrap, adoption, handoffs, and lifecycle operations. The canonical skill is [skills/orchestration/SKILL.md](skills/orchestration/SKILL.md). A separate [Agent Plugins 1.0.0](https://agent-plugins.org/specification) wrapper is provided by [plugin.json](plugin.json).

## Install as an Agent Skill

Requires Node.js 22.20+ and a supported agent environment. From a disposable or authorized project directory:

```bash
npx skills add ilyasclick/orchestration --skill orchestration
```

For GitHub CLI 2.90.0+:

```bash
gh skill preview ilyasclick/orchestration orchestration
gh skill install ilyasclick/orchestration orchestration --agent codex --scope project
```

Choose another supported agent with `--agent` (e.g. `claude-code`, `github-copilot`, `cursor`). See [SKILL_INSTALL.md](SKILL_INSTALL.md) for installation, update, version pinning, verification, and rollback.

**Host capabilities:** Installing the Skill supplies instructions, not ChatGPT Projects, Library, GitHub authentication, or write permissions. Actual project bootstrap requires authorized persistent project storage and readback. See [HOST-CAPABILITIES.md](skills/orchestration/references/HOST-CAPABILITIES.md).

## Protocol version authority

Current public production protocol: **0.4.3 STABLE** (2026-11-08).

The GitHub production pointer is [Orchestration/protocol/CURRENT.md](Orchestration/protocol/CURRENT.md). STABLE releases are under [Orchestration/protocol/releases/](Orchestration/protocol/releases/), including [v0.4.3](Orchestration/protocol/releases/v0.4.3/PROTOCOL.md).

**Fresh accounts:** the Skill reads the production pointer and exact STABLE release from public GitHub; it does not require a pre-existing `/Orchestration/` Library tree. Missing `/Orchestration/protocol/CURRENT.md` in a new account is normal. Do not fall back to embedded 0.3.0.

**Existing projects:** retain their own locally adopted protocol pin until explicitly upgraded. GitHub is a portable protocol source, not a synchronized copy of account-specific Library state.

An [optional runtime-package manifest](packaging/manifests/runtime-package.json) documents offline/managed import with SHA-256 verification; it is not a prerequisite for GitHub-first bootstrap.

## Distribution and licensing

The Skill is source-available under the [Orchestration Source-Available License 1.0](LICENSE). It permits personal and internal installation/use, but is **not** an OSI-approved open-source license and does not grant unrestricted redistribution. A future open-source license requires a separate copyright-owner decision.

The Skill package version, `plugin.json` version, and production protocol version are distinct. Updating GitHub does not prove that another account's installed Skill or Plugin refreshed. Never export credentials, sessions, or unrelated projects.
