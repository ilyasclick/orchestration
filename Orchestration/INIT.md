# Orchestration — INIT

Status: ACTIVE
Initialized: 2026-10-26
Project code: ORCH

## Purpose

`Orchestration` develops and maintains a universal, versioned method for launching and operating agent-based projects in separate chats.

The method must allow a human `Conductor` to start a project with a natural-language trigger, hand the first chat a goal in ordinary language, and then let the project persist its state outside chats so agents can be replaced without losing context.

## Current source protocol

Current protocol pointer: `/Orchestration/protocol/CURRENT.md`.

A project created from this system must record which protocol release it was created with. A newer global release must not silently rewrite an existing project's rules.

## Core principles

1. Project state lives in Library/project files, not in chat history.
2. The first chat is replaceable; it is a bootstrap/coordinator role, not the project itself.
3. The Conductor provides intent, expected outcome, business constraints and explicit approvals when required; agents resolve technical details where safely possible.
4. Every agent has an explicit role, scope and authority.
5. Context and external resources are project-scoped; visibility is not authorization.
6. Every substantial result has a next step and lifecycle decision.
7. Temporary `pending/waiting` states do not terminate a workflow without an owner/trigger.
8. Existing project structure is reused when sound; unnecessary restructuring is avoided.
9. Global protocol releases are versioned and upgradeable through an explicit comparison/migration step.

## Start order for any new Orchestration chat

1. `/Orchestration/INIT.md`
2. `/Orchestration/INDEX.md`
3. `/Orchestration/STATUS.md`
4. Relevant task/audit/strategy/handoff referenced by INDEX or STATUS.

Do not recursively read the entire Library.

## Source priority

1. Current explicit user instruction.
2. Verified current state of the target system, when applicable.
3. Current project audit/result/task/handoff.
4. Project STATUS.
5. Project INDEX and local project rules.
6. Global protocol release recorded by the project.
7. Chat memory or model memory.
