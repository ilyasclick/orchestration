# Orchestration

Current public production protocol: **0.4.3 STABLE** (2026-11-08).

The exact active protocol is specified in [Orchestration/protocol/CURRENT.md](Orchestration/protocol/CURRENT.md). The full supported release chain is under [Orchestration/protocol/releases/](Orchestration/protocol/releases/), including the 0.4.3 [protocol](Orchestration/protocol/releases/v0.4.3/PROTOCOL.md) and [universal project instructions template](Orchestration/protocol/releases/v0.4.3/PROJECT_INSTRUCTIONS_TEMPLATE.md).

The consumer install file list, sizes and SHA-256 checksums are in [runtime-package.json](packaging/manifests/runtime-package.json). The repository snapshot allowlist and checksums are in [repository-files.json](packaging/manifests/repository-files.json). Preserve exact repository paths when importing into a ChatGPT account Library. An existing project's adopted protocol is never silently upgraded; PROJECT_UPGRADE requires explicit authorization.

GitHub distributes portable source. Library is authoritative for each installed account's live project state. The repository may retain historical maintainer state; it is not a synchronized live mirror of all Library branches. Never export secrets, accounts, sessions or unrelated projects.
