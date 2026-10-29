# GitHub orchestration — STATUS

state: ACTIVE
current_stage: DESIGN_READY
current_gate: NONE
next_step: Build an exact repository allowlist/runtime manifest and a local dry-run export package; do not perform any external GitHub write.
owner_role: Coordinator / Strategist
updated_at: 2026-10-28T23:49:00+03:00
initial_chat: ORCH-11 · GitHub orchestration · Discovery

## Current design

- Architecture artifact: `/Orchestration/branches/github-orchestration/ARCHITECTURE.md`.
- GitHub is the portable version-control/distribution layer; Library remains authoritative live runtime state after installation.
- Deployment modes: `consumer` and `maintainer`.
- Consumer mode supports independent installation on multiple accounts.
- Maintainer mode is single-writer until a distributed conflict-safe serial/registry contract exists.
- Synchronization is explicit import/export with manifests, SHA-256 verification and divergence blockers; no automatic last-write-wins sync.
- Git branches are repository-change mechanisms and are not mapped 1:1 to persistent Orchestration branches.
- Existing managed projects remain pinned to their local protocol until explicit `PROJECT_UPGRADE`.
- No external GitHub write has been authorized or performed.

## History

- transition_id: ORCH-GITHUB-0001
  prior_state: NONE
  resulting_state: ACTIVE
  reason: Conductor explicitly requested a new branch named "GitHub orchestration".
  provenance: user instruction in the current Orchestration chat on 2026-10-28
  timestamp: 2026-10-28T23:41:00+03:00

- transition_id: ORCH-GITHUB-0002
  prior_state: ACTIVE/DISCOVERY
  resulting_state: ACTIVE/DESIGN_READY
  reason: GitHub architecture, synchronization direction and cross-account deployment model were designed against Orchestration STABLE 0.3.0 and current ChatGPT/GitHub connector constraints.
  provenance: ORCH-11 current branch work on 2026-10-28
  timestamp: 2026-10-28T23:49:00+03:00
