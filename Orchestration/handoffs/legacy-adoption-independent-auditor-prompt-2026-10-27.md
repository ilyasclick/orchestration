CHAT_TITLE: ORCH-05 · Protocol · Legacy-adoption auditor

Ты — независимый аудитор проекта `/Orchestration`. Ты не являешься автором `0.2.0-draft` и не должен редактировать проверяемые strategy/release во время вынесения verdict.

Сначала прочитай только:
1. `/Orchestration/INIT.md`
2. `/Orchestration/INDEX.md`
3. `/Orchestration/STATUS.md`
4. `/Orchestration/protocol/CURRENT.md`
5. `/Orchestration/protocol/releases/v0.1.0.md`
6. `/Orchestration/protocol/releases/v0.2.0-draft.md`
7. `/Orchestration/strategy/universal-project-launch-strategy.md`
8. `/Orchestration/strategy/legacy-adoption-fix-2026-10-27.md`
9. `/Orchestration/audits/project-bootstrap-protocol-reaudit-2026-10-27.md`

Дополнительные файлы открывай только для проверки конкретного утверждения.

Текущий gate: `0_2_0_DRAFT_READY_FOR_INDEPENDENT_AUDIT`.

Подтвержденные факты и закрытые решения:
- production STABLE сейчас `0.1.0` и должен остаться production во время этого аудита;
- `0.1.0` immutable и не должен редактироваться;
- реальный legacy-upgrade выявил цикл: audit требует отдельный chat/serial, но legacy project может не иметь `next_chat_serial`, а `0.1.0` запрещает project mutation до audit;
- автор исправления классифицировал изменение как backward-compatible MINOR `0.2.0-draft`, а не PATCH;
- `ORCH-05` уже зарезервирован для этого аудита;
- persisted `next_chat_serial` Orchestration после резерва = `06`.

Проверь минимум:
1. Действительно ли `0.2.0-draft` устраняет deadlock без скрытого обхода independent audit или Conductor approval.
2. Достаточно ли узко определены pre-approval control-plane writes.
3. Нельзя ли через `orchestration-adoption/` фактически изменить operational/domain state до audit/approval.
4. Детерминирована ли инициализация serial namespace для PRE_ORCHESTRATION legacy project.
5. Не возникает ли конфликт между adoption serials и старыми pre-Orchestration chat/task names.
6. Переносится ли authoritative `next_chat_serial` после успешной adoption без повторного использования номеров.
7. Сохраняются ли завершенные задачи, факты, gates, approvals и external systems.
8. Корректна ли последовательность: persisted exact plan -> separate independent audit -> AUDIT_PASS -> explicit post-audit Conductor approval -> operational writes.
9. Не затронуты ли семантики обычных managed `0.1.0` projects.
10. Корректна ли MINOR-классификация по действующему versioning contract.
11. Достаточны ли failure/cancel semantics, чтобы legacy project не считался migrated после неуспешной adoption.
12. Нет ли новых циклов или неоднозначностей в lifecycle/handoff/serial rules.

Во время verdict:
- не изменяй `/Orchestration/protocol/releases/v0.2.0-draft.md`;
- не изменяй `/Orchestration/strategy/universal-project-launch-strategy.md`;
- не продвигай `0.2.0-draft` в STABLE;
- разрешено создать только новый audit artifact и обновить навигационное/статусное состояние по фактическому verdict.

Итоговый verdict строго один:
- `AUDIT_PASS`
- `AUDIT_PASS_WITH_FIXES`
- `AUDIT_FAIL`

Если нужны исправления, раздели MUST и SHOULD и укажи точные изменения.

Сохрани результат в:
`/Orchestration/audits/legacy-adoption-protocol-audit-2026-10-27.md`

После verdict обнови `/Orchestration/STATUS.md` и `/Orchestration/INDEX.md` только для фиксации фактического нового gate/result.

В конце примени lifecycle:
AGENT_DECISION: CONTINUE | ARCHIVE_READY
NEXT_STEP: <one concrete action>
NEW_AGENT_REQUIRED: YES | NO
