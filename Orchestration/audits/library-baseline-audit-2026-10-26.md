# Library baseline audit — reusable project orchestration practices

Date: 2026-10-26
Role: audit / architecture inventory
Mode: read-only
Verdict: `BASELINE_READY_FOR_STRATEGY`

## Scope

Audit only architecture-relevant project-management materials already present in Library. This is not a recursive audit of every user file.

## Sources reviewed

- `/Management/INIT.md`
- existing `PROJECT_INIT.md` copies found in Library
- `/Vertime/AGENTS.md`
- `/Vertime/shared/context-isolation.md`
- `/Vertime/shared/agent-completion-protocol.md`
- `/Vertime/INDEX.md`
- representative Vertime strategist/auditor/coordinator handoffs
- `/GoogleDrive-Cleanup/INIT.md`
- `/GoogleDrive-Cleanup/AGENTS.md`
- `/GoogleDrive-Cleanup/branches/03-chat-naming/chat-naming-standard.md`
- representative GoogleDrive-Cleanup branch STATUS/handoff files

## What already works well

### 1. Persistent state outside chats

Management already establishes INIT/INDEX/STATUS/AGENTS plus tasks, handoffs, audits, decisions and archive, and explicitly ranks persisted project evidence above chat memory.

### 2. Progressive disclosure

Vertime avoids recursive project scans: root rules and index first, then only the relevant section and files referenced for the current task.

### 3. Context isolation and provenance

Vertime has a strong rule that memory, browser history, visible devices, accounts and unrelated project paths are not authorization. Project mapping and fact provenance are explicit.

### 4. Deterministic agent lifecycle

Vertime requires CONTINUE/ARCHIVE_READY, one concrete NEXT_STEP and a complete next-agent prompt when a new role is needed.

### 5. Anti-stall behavior

A real coordination failure exposed a useful rule: transient `pending/waiting` states must not end a workflow when the agent/coordinator can continue or define a future trigger.

### 6. Role separation and audit gates

Vertime successfully used `strategist -> independent auditor -> coordinator/executor`, with audit verdicts before high-impact execution.

### 7. Branching and chat identity

GoogleDrive-Cleanup demonstrates project branches and a useful universal chat naming pattern: project code + monotonic chat serial + branch + role/task.

### 8. Older technical bootstrap guidance

Existing `PROJECT_INIT.md` contains good reusable rules for project maps, safe external-system work, verification, rollback and keeping the project easier for the next agent.

## Problems/gaps

### A. No single global bootstrap source of truth

Reusable practices are distributed across multiple projects. A new project still depends on knowing which prior project to imitate.

### B. Duplicate universal initialization guidance

At least two Library files named `PROJECT_INIT.md` contain the same universal bootstrap text. This is evidence that global guidance is already being copied rather than centrally versioned.

### C. No protocol release/version model

Current project rules can be edited, but there is no global `CURRENT` release pointer, changelog, compatibility policy or explicit record of which protocol version created a project.

### D. No universal `CREATE PROJECT` state machine

Existing files explain how agents should work once inside a project, but do not define one deterministic flow from a Conductor's natural-language trigger through initialization and intent capture.

### E. No universal `UPGRADE PROJECT` flow

There is no standard comparison/migration process for bringing an existing project onto newer global rules without silently changing behavior.

### F. Human/operator role is implicit

Existing systems assume the user is the operator. The future delegation target needs an explicit human role with a narrow interface. Working name: `Conductor`.

### G. Naming standard is project-local

GoogleDrive-Cleanup's naming convention is reusable, but is not yet part of a global protocol.

## Audit conclusion

Do not replace the existing good practices. Consolidate them into one versioned global protocol with two explicit entry flows:

1. `PROJECT_CREATE` — initialize a new project from natural-language intent.
2. `PROJECT_UPGRADE` — compare a pinned project release to the current global release and migrate explicitly.

The project should preserve local rules and project-specific safety constraints; the global protocol governs orchestration mechanics rather than domain content.
