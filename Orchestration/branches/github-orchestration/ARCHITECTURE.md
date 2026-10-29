# GitHub Orchestration — architecture

Date: 2026-10-28
Branch: `github-orchestration`
Status: DESIGN_READY
Applies to: Orchestration STABLE `0.3.0`

## 1. Goal

Provide a reproducible GitHub representation of Orchestration that can be installed on another ChatGPT account and synchronized explicitly without weakening project-scoped authority, persistent Library state, protocol version pinning, branch identity, or audit/approval gates.

## 2. Source-of-truth model

Do not make GitHub and Library competing masters for the same live state.

Authority is split by class:

1. **Published portable source** — GitHub is the distribution source for immutable protocol releases, deployment package metadata, validation scripts and repository documentation.
2. **Live account runtime state** — the target account's Library remains authoritative after installation for project state, branch state, `next_chat_serial`, local approvals/gates, project-specific AGENTS rules and project results.
3. **Existing project protocol pins** — importing a newer global Orchestration package must never silently upgrade an existing managed project. Existing projects remain pinned until their own `PROJECT_UPGRADE`.
4. **Orchestration maintainer state** — one ChatGPT account is the active Library writer for the canonical Orchestration development project until a later protocol explicitly supports distributed conflict-safe coordination.

Consequences:

- GitHub is not a live-mounted replacement for Library under protocol 0.3.0.
- Target accounts receive an explicit copy/import of portable files and then operate from local persistent files.
- No automatic last-write-wins synchronization is allowed.
- Orchestration persistent branches are directories/state inside the repository tree; they are not mapped 1:1 to Git branches.

## 3. Deployment modes

### 3.1 Consumer mode

Use when an account only needs to create/run Orchestration-managed projects.

Install only the portable runtime package:

```text
/Orchestration/protocol/CURRENT.md
/Orchestration/protocol/CHANGELOG.md
/Orchestration/protocol/releases/<all supported STABLE releases>.md
/Orchestration/deployment/INSTALLATION.md        # target-local, generated at install
```

The account also receives the account/workspace bootstrap hook in its user-level instructions:

```text
On natural-language intent to create/initialize a project, or to adopt/upgrade Orchestration for an existing project, use the Orchestration bootstrap system. Read /Orchestration/protocol/CURRENT.md and the exact production STABLE release it references. Cross-project access is read-only and limited to Orchestration discovery. Do not use files, context or permissions from unrelated projects without explicit authorization.
```

`INSTALLATION.md` records only portable provenance such as repository, source commit/tag, install mode, installed package hash and installation/readback timestamp. It contains no token or account credential and is excluded from export back to GitHub.

### 3.2 Maintainer mode

Use only when another account must continue development of Orchestration itself.

It installs a full approved snapshot of `/Orchestration/`, including project root, protocol, strategy, audits and persistent Orchestration branches, plus deployment provenance.

Initial rule: **single-writer maintainer**. Only one account is authoritative for live Orchestration project coordination at a time. A second maintainer account may be a read-only replica or an explicitly transferred successor. Concurrent independent allocation of `next_chat_serial` or root branch-registry mutations is prohibited until a distributed allocation/locking contract exists.

## 4. Repository layout

Recommended repository root:

```text
README.md
INSTALL.md
SECURITY.md
LICENSE                         # if/when distribution terms are chosen
.gitignore
.github/
  workflows/
    validate.yml
Orchestration/
  INIT.md
  INDEX.md
  STATUS.md
  AGENTS.md
  protocol/
    CURRENT.md
    CHANGELOG.md
    releases/
  strategy/
  audits/
  handoffs/
  branches/
packaging/
  manifests/
    repository-files.json
    runtime-package.json
  bootstrap/
    USER_INSTRUCTIONS.txt
  schemas/
  scripts/
    validate_manifest.py
    build_runtime_package.py
    verify_package.py
  exclusions.md
```

Design rule: `Orchestration/` is a path-preserving mirror of the canonical maintainer snapshot. `packaging/` contains portability tooling and must not become a second copy of protocol files.

Generated release bundles belong in GitHub Release assets or CI artifacts, not as duplicated editable protocol trees in normal source.

## 5. File classes and synchronization policy

### A. Immutable protocol releases

Examples: `protocol/releases/v0.1.0.md`, `v0.2.0.md`, `v0.3.0.md`.

Policy:
- byte-preserving export after promotion;
- never edited in place after promotion;
- change requires a new protocol version;
- package manifest stores SHA-256 for each file.

### B. Mutable global distribution pointers

Examples: `protocol/CURRENT.md`, `protocol/CHANGELOG.md`.

Policy:
- may change only through the normal Orchestration release/change process;
- `CURRENT.md` must resolve to an existing `STABLE` release;
- deployment verifies this invariant before import.

### C. Canonical maintainer project state

Examples: Orchestration root `STATUS.md`, root `INDEX.md`, active `branches/*/STATUS.md`, current handoffs/audits.

Policy:
- included in full maintainer snapshots;
- excluded from consumer runtime bundle unless required by the runtime contract;
- never merged with target-local state by last-write-wins;
- maintainer import requires explicit diff/recovery handling.

### D. Target-account runtime/project state

Examples: another project's `INIT.md`, `STATUS.md`, `AGENTS.md`, branch registry, results, approvals and serials.

Policy:
- never exported by the Orchestration repository sync;
- never overwritten by Orchestration package update;
- belongs only to its target project/account unless explicitly exported as its own project.

### E. Local-only installation metadata

Example: `/Orchestration/deployment/INSTALLATION.md`.

Policy:
- generated per account;
- not included in GitHub canonical source;
- contains no credentials.

### F. Forbidden repository content

Never export:
- passwords, API tokens, OAuth secrets, cookies, private keys, `.env` contents;
- connected-app credentials or account session data;
- Library internal IDs as portable identity;
- model memory or chat history as authoritative state;
- files/state from unrelated projects;
- target-project operational data merely because it is visible from the maintainer account.

## 6. Git model

Git branches and Orchestration branches have different purposes.

- `main` — protected, last accepted repository state.
- short-lived Git branches — repository change/review mechanism, e.g. `feature/runtime-packaging` or `release/protocol-0.4.0`.
- pull request — review and CI boundary.
- Git tag `protocol-vX.Y.Z` — immutable marker for a promoted STABLE protocol release.
- GitHub Release `orchestration-runtime-vX.Y.Z` — generated consumer installation bundle plus manifest/checksums.

Do not create one Git branch for every `/Orchestration/branches/<branch_id>/`. Persistent Orchestration branch identity remains in `INDEX.md`, `BRANCH.md` and `STATUS.md` regardless of Git branch names.

## 7. Export flow: Library -> GitHub

No implicit push.

```text
1. Read canonical Orchestration root and active branch state.
2. Export only files allowed by repository-files.json whitelist.
3. Refuse forbidden paths/content classes.
4. Compute SHA-256 manifest.
5. Validate repository invariants locally.
6. Compare against current GitHub base commit.
7. If divergent, create a bounded Git change set; never overwrite blindly.
8. Push to a short-lived Git branch only after external GitHub write is authorized.
9. Run CI validation.
10. Review/audit as required by the Orchestration change being published.
11. Merge after required approval.
12. For a promoted protocol release, create immutable tag and generated runtime Release bundle.
```

Repository sync is evidence of publication, not authority to reopen completed protocol gates or mutate unrelated project state.

## 8. Import/update flow: GitHub -> Library

### Consumer update

```text
1. Fetch exact manifest and tagged runtime bundle.
2. Verify checksums and pointer -> STABLE consistency.
3. Read local /Orchestration/deployment/INSTALLATION.md if present.
4. Diff only portable Orchestration runtime paths.
5. Stop on unexpected local divergence in a file that would be replaced.
6. Import files into local /Orchestration/protocol/.
7. Read back every imported file.
8. Re-run manifest/checksum verification on persisted bytes when possible.
9. Update INSTALLATION.md with source tag/commit/hash and readback result.
10. Do not modify any existing project's protocol_current_local.
```

Defined sync blockers for the implementation layer:

```text
SYNC_BLOCKED_SOURCE_UNAVAILABLE
SYNC_BLOCKED_MANIFEST_INVALID
SYNC_BLOCKED_CHECKSUM_MISMATCH
SYNC_BLOCKED_PROTOCOL_POINTER
SYNC_BLOCKED_LOCAL_DIVERGENCE
SYNC_BLOCKED_STORAGE_UNAVAILABLE
SYNC_BLOCKED_PERSISTENCE_VERIFICATION
SYNC_BLOCKED_MAINTAINER_CONFLICT
```

### Maintainer update/transfer

A full maintainer import additionally verifies:
- exact root `next_chat_serial` continuity;
- branch registry/non-reuse ledger consistency;
- no `PENDING_CREATE` / `PENDING_RENAME` mutation is being silently abandoned;
- active branch statuses/history are preserved;
- source snapshot commit is recorded.

A maintainer transfer is an explicit handover. The previous maintainer must stop allocating new Orchestration serials/root registry mutations before the successor becomes authoritative.

## 9. Cross-account bootstrap procedure

For a fresh target account:

```text
1. Obtain a tagged runtime bundle from GitHub.
2. Verify manifest/checksums.
3. Import the portable files to the target account Library under /Orchestration/.
4. Install the user/workspace bootstrap-hook instruction.
5. Start a disposable test project with natural-language intent such as "создай проект Test".
6. Verify the bootstrap reads /Orchestration/protocol/CURRENT.md, resolves the STABLE release and creates persistent seed state.
7. Verify seed readback and that the test project records protocol_created_with / protocol_current_local.
8. Verify an existing managed project remains pinned and is not silently upgraded.
9. Record deployment verification in target-local INSTALLATION.md.
```

The GitHub connection/authentication itself is account-specific and is not transferred by the bundle.

## 10. Validation / CI

`validate.yml` should run without production secrets and check at least:

1. every manifest path exists and has the expected hash;
2. `CURRENT.md` production pointer resolves to an included release whose metadata says `STABLE`;
3. promoted `protocol/releases/v*.md` files are immutable relative to their release tags;
4. no duplicate current/historical Orchestration `branch_id` occurs in the root registry model;
5. every exported branch directory has identity/status files expected by the current protocol;
6. no target-local `deployment/INSTALLATION.md` is in canonical source;
7. forbidden secret filenames/patterns are absent;
8. runtime bundle contains only the runtime allowlist;
9. runtime bundle can be unpacked path-preservingly under `/Orchestration/`;
10. generated package manifest and checksums are reproducible from the same commit.

CI validates structure; it does not replace independent Orchestration audit when protocol semantics require one.

## 11. Current ChatGPT/GitHub product constraints

As of 2026-10-28, ChatGPT's GitHub connection retrieves authorized repository content on demand. It does not provide a live synchronized GitHub index, and the standard GitHub connection is read-only for repository analysis/search; direct push requires another supported execution path such as Codex or a Git client. Therefore this design deliberately uses explicit import/export instead of pretending the connector is a bidirectional filesystem.

Library is account/workspace-scoped persistent storage. Files can be uploaded and reused there, so a release bundle/import step is compatible with the protocol's requirement that target project state be persisted and read back locally.

## 12. Decisions

Accepted by design:

- GitHub = portable distribution/version-control layer, not live runtime master.
- Library = authoritative live state inside each installed account/project.
- Consumer installs may exist on many accounts independently.
- Maintainer mode is single-writer initially.
- Existing projects never auto-upgrade from a GitHub/global update.
- Git branches do not represent Orchestration branches.
- Sync is explicit, manifest-driven, checksum-verified and conflict-blocking.
- Consumer and maintainer packages are separate.
- Account credentials, plugin connections and secrets are never part of deployment artifacts.

## 13. Next implementation slice

Without performing any GitHub write:

1. create the exact `repository-files.json` allowlist;
2. create the exact `runtime-package.json` manifest schema;
3. build a local dry-run export of the current Orchestration Library state;
4. verify exclusion rules and SHA-256 reproducibility;
5. produce the proposed initial repository tree and diff before requesting authorization for repository creation/push.
