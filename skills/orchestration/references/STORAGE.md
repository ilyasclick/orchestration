# Modular storage and history — review candidate

No automatic restructure of current Library projects. The candidate layout for a separately migrated project is:

```text
<PROJECT_ROOT>/
  Protocol/adopted/<confirmed-version>/
  instructions/core/<topic>/
  instructions/workflows/<topic>/
  instructions/local/<topic>/
  branches/<branch-id>/events/<event-id>/
  branches/<branch-id>/plans/<plan-id>/
  branches/<branch-id>/results/<run-id>/
  branches/<branch-id>/handoff/<handoff-id>/
  branches/archive/<branch-id>/
  Status/<event-id>/
```

A folder can encode a simple event. Content-bearing results require immutable unique files, source/task/run links, and real readback. Historical INIT, INDEX, AGENTS, STATUS, BRANCH, CURRENT and CHANGELOG files remain available until exact consumers and rollback are proven. Do not bulk-delete or assume move/create is atomic.

## D01–D25: complete role crosswalk (design, not migrated state)

The 25 roles below are drawn from the canonical 2026-11-21 Library design `CONTROL-PLANE-INVENTORY-v001.md`. They are logical roles, not 25 folders that already exist. A filename alone does not make an object mutable. Exact legacy consumers and the complete Library path/ID manifest are NOT_VERIFIED.

| ID | Logical role | Proposed authority / target | Legacy guard |
|---|---|---|---|
| D01 | Local adopted protocol | `<P>/protocol/adopted/` | Marker after approved migration; preserve confirmed legacy pin |
| D02 | Global production pointer | `/Orchestration/protocol/current/` | Keep legacy CURRENT readers until proven compatible; approval required |
| D03 | CHANGELOG and release history | `<P>/changes/<event-id>/` | Append immutable events; historical CHANGELOG preserved |
| D04 | Project status and stage | `<P>/status/<event-id>/` | No latest-by-date without verified supersession |
| D05 | Branch list and lifecycle | `<P>/branches/`, `branches/archive/` | Direct children only; legacy 0.3.0 registry stays for 0.3.0 |
| D06 | Branch identity and scope | `branches/<B>/identity/`, `decisions/` | Immutable ID; scope change requires decision |
| D07 | Branch stage and blocker | `branches/<B>/events/<event-id>/` | Old STATUS is evidence, not automatic authority |
| D08 | Handoff and next agent | `branches/<B>/handoff/<handoff-id>/` | Task/branch link; handoff is not delivery |
| D09 | Result/report/acceptance | `branches/<B>/results/<run-id>/` | Keep distinct runs; gate needs verified postcondition |
| D10 | Plans and priorities | `branches/<B>/plans/<plan-id>/` | Frozen plan and explicit decision on scope changes |
| D11 | Task queues, claims, HOLD | `<P>/tasks/<task-id>/`, `claims/` | Preserve lease/owner and domain HOLD; never conflate queues |
| D12 | AGENTS roles and safety | `instructions/local/{roles,safety}/<topic>/` | All mandatory local safety rules must survive |
| D13 | INIT mixed identity/current fields | `project/identity/`, `decisions/`, `status/` | Split by meaning, preserve immutable original |
| D14 | Project Instructions | `instructions/core/bootstrap/` plus host UI | Library write never proves UI settings changed |
| D15 | Workflow/local instructions | `instructions/{core,workflows,local}/<topic>/` | One active per topic, history and applies_when |
| D16 | Thematic INDEX navigation | Domain folders + workflow routing modules | List actual domain; do not force business data migration |
| D17 | Dispatchers FNS_NEXT, QUEUE, START | `instructions/workflows/<domain>/routing/`, `tasks/` | Preserve FNS approval and other domain gates |
| D18 | Connection/source maps | `instructions/local/sources/`, `connections/` | No secrets; visibility is not authority |
| D19 | REGISTER/STATE/inventory/manifest | `inventories/<run-id>/` for control-plane | Domain REGISTER and test fixtures are not automatically live |
| D20 | Incident families and postconditions | `incidents/<incident-id>/events/` | One primary family; no close without postcondition |
| D21 | Approvals and revocations | `decisions/<decision-id>/` | Scope and owner immutable; explicit permission boundary |
| D22 | Dynamic CURRENT/STATE/MAPPING pointers | One active in `<domain>/<logical-object>/` | Classify consumer first; immutable snapshots stay snapshots |
| D23 | Global protocol sections/distribution | `protocol/releases/vX.Y.Z/sections/`, Skill refs | Immutable release; source/install/local pin separate |
| D24 | OrchVoice current modules | Separate `voice/current/<module>/` only after approval | Existing runtime and live top-level docs untouched |
| D25 | Version checks/schedules | `version-check/<account-id>/events/` | Explicit per-account opt-in; checking is not upgrading |

Mandatory migration crosswalk: for each *actual* object record source path, object ID, version, logical role, owner, current reader/writer, required safety rules, destination, conflict/case-alias risk, approval, readback and exact rollback path. No role-only table can substitute for this per-object evidence.

Writer rules: resolve exact identity and exclusive writer or fail closed; use unique append-only events; before replacing an active topic verify one active document and old object ID; with approved safe backend moves create history/, move old there, create new top-level object, and read back both. Partial failure stops further writes and preserves evidence. Archive exact branch folder only after result/handoff and collision checks, then read back both paths. UI chat archival is separate.

Do not mutate OrchVoice runtime, other projects, production pointers, external recipients or Project settings. Existing Vertime FNS, FreshPlants import and FPsell NDA guards remain binding in their projects.