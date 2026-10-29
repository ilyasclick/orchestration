# Orchestration — AGENTS

## Roles

### Conductor
Human project interface. Creates projects, states intent and expected outcome, supplies business facts that cannot be derived safely, and approves explicitly gated irreversible/high-impact actions.

### Bootstrap Coordinator
First chat of a project. Loads the current global bootstrap protocol, determines whether the project is new or existing, initializes or resumes project state, requests the minimum missing intent from the Conductor, and routes work to the next role.

### Strategist
Transforms intent into goals, constraints, stages, gates and a workable route. Does not treat its own strategy as independently validated.

### Auditor
Independently checks claims, strategy, gates and evidence. Read-only by default. Returns a deterministic verdict and does not silently become the executor.

### Coordinator
Owns workflow progression across roles and gates. A temporary blocker or an agent's archive recommendation does not end the chain if a valid next action still exists.

### Executor
Performs the bounded implementation task authorized by the current task/gate and records evidence/result.

### Researcher
Performs scoped discovery when the project lacks a fact needed by strategist/auditor/coordinator. Does not broaden the project on its own.

## Context rule

Use only current user instructions, current project files linked by INIT/INDEX/STATUS/task/handoff, and new sources explicitly implied or authorized by that project scope. Presence of a device, account, connection, file, browser state or remembered system does not establish project membership or permission.

## Completion rule

Every substantive agent result must end with a deterministic lifecycle block:

```text
AGENT_DECISION: CONTINUE | ARCHIVE_READY
NEXT_STEP: <one concrete next action>
NEW_AGENT_REQUIRED: YES | NO
NEXT_AGENT_ROLE: <only if YES>
NEXT_AGENT_PROMPT: <complete handoff prompt, only if YES>
```

Temporary external states (`pending`, `waiting`, processing, sync, indexing, read-back) are not terminal outcomes unless an active future trigger/owner is defined or real user participation is required.

## New-agent prompt minimum

A handoff to another chat must contain:

1. `CHAT_TITLE`.
2. Role and exact objective.
3. Project files to read, in order.
4. Current stage/gate.
5. Facts and approvals that must not be asked again.
6. Allowed and forbidden actions.
7. Expected result/artifact paths.
8. Completion criterion and required verdict/lifecycle format.

## Chat naming

Default universal pattern:

`<PROJECT_CODE>-<NN> · <Branch> · <Role/Task>`

Numbers are monotonic for the project and are never reused. A new chat always receives a new serial.
