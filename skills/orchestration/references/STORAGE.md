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

The Library architecture records D01–D25 object classes, but a complete authoritative D01–D25 map and per-object manifest are NOT_VERIFIED. Only this earlier inventory crosswalk is supported:

| Class references | Observed source | Candidate role |
|---|---|---|
| D01/D13 | adopted marker, INIT | local identity |
| D02/D23 | CURRENT, releases | global version identity |
| D03 | CHANGELOG | release provenance |
| D04/D22 | Status, STATUS-CURRENT | event/status evidence |
| D05/D16/D22 | INDEX, branches | derived navigation |
| D06/D07 | BRANCH, branch events | branch identity/lifecycle |
| D08 | handoffs | transfer, not delivery |
| D09/D10 | plans/results | work and run evidence |
| D12/D15 | AGENTS, local instructions | roles and safety |
| D19 | tests | fixtures, not live state |
| D20/D21 | incidents, approvals | source/decision evidence |
| D24 | voice/current | separate OrchVoice scope |

Writer rules: resolve exact identity and exclusive writer or fail closed; use unique append-only events; before replacing an active topic verify one active document and old object ID; with approved safe backend moves create history/, move old there, create new top-level object, and read back both. Partial failure stops further writes and preserves evidence. Archive exact branch folder only after result/handoff and collision checks, then read back both paths. UI chat archival is separate.

Do not mutate OrchVoice runtime, other projects, production pointers, external recipients or Project settings. Existing Vertime FNS, FreshPlants import and FPsell NDA guards remain binding in their projects.