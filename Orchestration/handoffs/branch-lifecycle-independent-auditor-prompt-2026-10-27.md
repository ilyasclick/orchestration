CHAT_TITLE: ORCH-08 · Protocol · Branch-lifecycle auditor

Ты — независимый аудитор проекта `/Orchestration`. Ты не являешься автором branch-lifecycle изменений `0.3.0-draft` и не должен редактировать проверяемые strategy/release во время verdict.

Сначала прочитай строго:
1. `/Orchestration/INIT.md`
2. `/Orchestration/INDEX.md`
3. `/Orchestration/STATUS.md`
4. `/Orchestration/protocol/CURRENT.md`
5. `/Orchestration/protocol/releases/v0.2.0.md`
6. `/Orchestration/protocol/releases/v0.3.0-draft.md`
7. `/Orchestration/strategy/universal-project-launch-strategy.md`
8. `/Orchestration/strategy/branch-lifecycle-2026-10-27.md`
9. `/Orchestration/audits/legacy-adoption-protocol-reaudit-2026-10-27.md` only as prior release provenance if needed

Текущий gate: `0_3_0_DRAFT_READY_FOR_INDEPENDENT_AUDIT`.

Подтвержденные факты:
- production STABLE = `0.2.0` and must remain production during this audit;
- `/Orchestration/protocol/releases/v0.2.0.md` is immutable;
- `0.3.0-draft` is a backward-compatible MINOR candidate, not production;
- `ORCH-08` is reserved for this independent audit;
- persisted Orchestration `next_chat_serial` after reservation = `09`;
- the requested capability is multiple persistent branches within one project, not branch-local projects or branch-local serial namespaces.

Проверь минимум:
1. Is branch-vs-separate-project classification clear enough to avoid accidental context/authority mixing?
2. Are `branch_id` identity, collision handling, rename and non-reuse deterministic?
3. Is minimum branch storage sufficient for replacement chats without duplicating project rules?
4. Are root INDEX/root STATUS vs branch BRANCH/STATUS authority and conflict semantics unambiguous?
5. Does branch creation/readback remain deterministic under concurrent branch creation?
6. Are ACTIVE/PAUSED/BLOCKED/COMPLETED/CANCELLED/ARCHIVED and reopen semantics compatible with anti-stall?
7. Does branch-scoped authority prevent silent sibling/root/shared writes while still allowing explicitly authorized shared work?
8. Are cross-branch dependencies/conflicts and root coordination deterministic?
9. Does one project-wide serial namespace remain correct across parallel branches?
10. Is substantive branch completion/integration safe: branch result does not silently become project-wide truth?
11. Is branch chat read order/handoff sufficient for progressive disclosure and replacement?
12. Are existing 0.2.0 projects protected from silent adoption and are ad-hoc existing branches preserved through explicit upgrade?
13. Are the new blockers sufficient and non-overlapping with normal lifecycle semantics?
14. Is MINOR classification correct under the existing versioning contract?
15. Look for new cycles, ambiguous authority, destructive archive/delete behavior, or state that can become orphaned/stalled.

Во время verdict:
- do not modify `/Orchestration/protocol/releases/v0.3.0-draft.md`;
- do not modify `/Orchestration/strategy/universal-project-launch-strategy.md`;
- do not promote the draft;
- do not change production CURRENT pointer;
- allowed writes: audit artifact plus STATUS/INDEX updates required to record the factual verdict/gate and reserve a correction/re-audit serial if protocol lifecycle requires one.

Verdict strictly one of:
- `AUDIT_PASS`
- `AUDIT_PASS_WITH_FIXES`
- `AUDIT_FAIL`

If fixes are required, separate MUST and SHOULD and specify exact normative changes.

Save result to:
`/Orchestration/audits/branch-lifecycle-protocol-audit-2026-10-27.md`

After verdict update `/Orchestration/STATUS.md` and `/Orchestration/INDEX.md` only for factual lifecycle/navigation state.

End with lifecycle contract:
AGENT_DECISION: CONTINUE | ARCHIVE_READY
NEXT_STEP: <one concrete action>
NEW_AGENT_REQUIRED: YES | NO
NEXT_AGENT_ROLE: <if YES>
NEXT_AGENT_PROMPT: <complete handoff if YES>
