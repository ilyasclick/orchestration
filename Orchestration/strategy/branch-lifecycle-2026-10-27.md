# Branch lifecycle capability design — 2026-10-27

Status: DEVELOPMENT CANDIDATE DESIGN — ORCH-09 CORRECTED
Target: `0.3.0-draft`
Production baseline: `0.2.0`
Audit input: `/Orchestration/audits/branch-lifecycle-protocol-audit-2026-10-27.md`

## Trigger

The Conductor requires several parallel long-lived workstreams inside one project, e.g. banners/design, cron jobs, admin-panel configuration and document production.

`0.2.0` already exposes `<Branch>` in chat titles and protects project-wide serial allocation under parallel branches, but it does not normatively define persistent branch identity, storage, state transitions, root/branch authority, pause/resume/close/archive semantics, or cross-branch integration.

## Design goals

1. Keep one project when authority/context/resources remain shared.
2. Make branches persistent and replaceable independently of chat history.
3. Keep one project-wide `next_chat_serial`; never create branch-local chat serial namespaces.
4. Prevent a branch agent from silently modifying sibling branch state.
5. Keep root INDEX/STATUS as the project control plane without duplicating full branch context.
6. Preserve progressive disclosure: branch chats load root entry points, then only their branch/task artifacts.
7. Define deterministic pause/block/complete/cancel/archive/reopen behavior.
8. Make branch results explicitly integratable into root/shared state rather than treating branch completion as an automatic merge.
9. Make branch identity/registry mutation crash-safe under non-transactional persistent storage.

## Compatibility choice

This is a backward-compatible capability/rule addition, therefore MINOR `0.3.0`, not PATCH. Existing `0.2.0` projects remain pinned and unchanged until explicit PROJECT_UPGRADE. Production `0.2.0` remains immutable while the draft is audited.

## Corrected identity/registry design

Root `INDEX.md` is both branch registry and non-reuse ledger. Every reserved/allocated `branch_id` remains represented permanently; normal complete/cancel/archive never removes it, and destructive content deletion retains an identity tombstone.

Registry mutation uses a serialized journal state:

- `PENDING_CREATE` with `mutation_id`, id, label and path is persisted/read back before branch seed creation;
- branch seed and root summary are then written/read back;
- registry finalizes to `STABLE` only after the required writes verify;
- rename similarly uses `PENDING_RENAME` with mutation id and old/target labels, never changes identity and finalizes only after readback.

A pending entry is a durable recovery point and consumes the id immediately. An unregistered pre-existing branch seed is not suffixable collision input: it blocks as `BRANCH_BLOCKED_REGISTRY_INCONSISTENT` until its immutable identity/history is reconciled. Recovery either completes registration of the same logical branch or performs an explicit repair/rollback while preserving the encountered identity as consumed; it never silently allocates a second branch identity.

## Corrected authority design

An authorized branch lifecycle action carries narrow root control-plane synchronization authority for the same branch only. It may update only protocol-required root branch registry/navigation mutation fields and the branch's compact root STATUS summary/dependency/conflict entry.

This narrow authority does not grant general root/shared authority: it excludes unrelated project metadata, project-wide business facts, sibling files, shared resources, permissions/constraints and result/integration decisions. Broader root/shared changes keep the existing explicit-authority/root-coordination requirement.

A material dependency/conflict directly involving the active branch may be reflected in the root summary under this narrow authority, without modifying sibling branch state.

## Corrected lifecycle/reopen design

Branch `STATUS.md` keeps append-only lifecycle transition evidence with stable transition id, prior/resulting state, reason, provenance and timestamp.

Reopen from `COMPLETED`, `CANCELLED` or `ARCHIVED`:

1. requires explicit authorized reopen decision;
2. preserves immutable id, prior results/evidence, gates and history;
3. results in `ACTIVE` by default;
4. may result in `PAUSED` or `BLOCKED` only when explicitly established with required trigger/owner metadata;
5. persists the transition record before claiming success;
6. performs mandatory same-branch root control-plane synchronization and readback before work resumes.

## Minimum contract after ORCH-09

- immutable stable `branch_id` + mutable human label;
- root registry/non-reuse ledger with `STABLE|PENDING_CREATE|PENDING_RENAME` mutation state;
- branch seed `branches/<id>/BRANCH.md` + `STATUS.md`;
- append-only branch transition history;
- root INDEX registry and root STATUS compact summary;
- states `ACTIVE|PAUSED|BLOCKED|COMPLETED|CANCELLED|ARCHIVED`;
- crash-safe create/rename recovery without duplicate suffixing after partial writes;
- narrow lifecycle-derived root branch-control-plane authority;
- root/shared/sibling authority boundaries preserved for all broader writes;
- project-wide serial namespace across branches;
- `RESULT.md` integration handoff on substantive completion;
- deterministic blockers/recovery for storage/id/registry/shared conflicts;
- branch-scoped handoff/read order.
