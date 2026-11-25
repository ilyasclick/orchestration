# Orchestration Skill distribution and version authority

Public source: https://github.com/ilyasclick/orchestration. The canonical Agent Skill is `skills/orchestration/SKILL.md`. The root `plugin.json` is an optional Agent Plugins 1.0.0 wrapper; it is not required for standalone Agent Skills installation.

## Fresh account / GitHub-first bootstrap

1. Install the Skill from GitHub using a compatible Agent Skills installer. See the repository's `SKILL_INSTALL.md`.
2. No pre-existing `/Orchestration/` Library tree or manual protocol import is required for **new-project bootstrap**. Fetch `Orchestration/protocol/CURRENT.md` and the exact STABLE release from public GitHub using an available GitHub connector or web reader.
3. The host must separately provide authorized target-project persistent writes and readback. Skill installation does not grant ChatGPT Projects/Library permissions. See `references/HOST-CAPABILITIES.md`.
4. Create only the authorized target project's durable state, following the selected release. Confirm actual writes by readback. If the host lacks tools, report a capability blocker rather than success.
5. The optional `packaging/bootstrap/USER_INSTRUCTIONS.txt` host hook is not automatically installed.
6. If GitHub cannot be read, report source-access failure; never fall back to hard-coded 0.3.0.

## Existing projects and optional offline cache

- Preserve existing projects' `Protocol/adopted/` or confirmed legacy pins. A new global CURRENT pointer never authorizes automatic migration.
- Fetch historical releases from authorized local files or GitHub without upgrading.
- `packaging/manifests/runtime-package.json` documents an **optional** local cache/import for managed or offline deployments. If imported, validate checksums, avoid overwrites, and read back.
- GitHub source is not account-specific Library state. Publishing to GitHub does not refresh every installed plugin/skill automatically.

## Release workflow

1. Update the canonical Skill, its references, README, installation instructions, and plugin metadata consistently.
2. Validate `SKILL.md` with `skills-ref validate`, validate `plugin.json` against Agent Plugins 1.0.0 schema, check paths and secrets, and run `gh skill publish --dry-run`.
3. Run disposable installations for target agent directories. Directory installation is not a full host functional test.
4. Review PR and publish a new Git tag/release only with owner authorization; record commit, tag, source and test evidence.
5. Preserve immutable `Orchestration/protocol/releases/*` and `Orchestration/protocol/CURRENT.md` unless a separately authorized protocol release changes them.
6. Roll back a broken Skill by reinstalling a previous verified tag; do not revert live Library state or existing adopted protocol pins automatically.

License: `LICENSE` in the repository and bundled Skill directory. The current source-available license permits internal use but does not grant unrestricted redistribution; selecting an OSI-approved license remains a separate legal decision for the owner.
