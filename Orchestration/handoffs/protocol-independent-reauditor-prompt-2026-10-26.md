CHAT_TITLE: ORCH-04 · Protocol · Re-auditor

Ты — свежий независимый re-auditor проекта `/Orchestration`. Ты не являешься автором исправлений и не должен редактировать проверяемую стратегию или draft во время вынесения verdict.

Сначала прочитай только:
1. `/Orchestration/INIT.md`
2. `/Orchestration/INDEX.md`
3. `/Orchestration/STATUS.md`
4. `/Orchestration/audits/project-bootstrap-protocol-audit-2026-10-26.md`
5. `/Orchestration/strategy/universal-project-launch-strategy.md`
6. `/Orchestration/protocol/CURRENT.md`
7. `/Orchestration/protocol/releases/v0.1.0-draft.md`
8. `/Vertime/shared/agent-completion-protocol.md`
9. `/GoogleDrive-Cleanup/branches/03-chat-naming/chat-naming-standard.md`

Текущий gate: `REVISION_READY_FOR_INDEPENDENT_REAUDIT`.

Разрешения уже даны:
- читать перечисленные ниже материалы в пределах этой проверки;
- создать новый независимый audit artifact только в `/Orchestration/audits/`;
- после verdict обновить только навигационное/статусное состояние `/Orchestration/STATUS.md` и `/Orchestration/INDEX.md`, если это требуется для фиксации результата;
- не изменять проверяемые strategy/release/CURRENT для исправления найденных дефектов.

Закрытые gates/работа, которые не повторять:
- исходный независимый audit уже завершен с `AUDIT_PASS_WITH_FIXES`; не проводить его заново как первичный audit;
- редакторский проход ORCH-03 завершен и его задача только проверить, а не воспроизводить;
- serial `ORCH-04` уже зарезервирован для этого re-audit, `next_chat_serial` после резерва = `05`; номер `04` не переиспользовать.

Цель: независимо проверить, что все MUST fixes предыдущего аудита действительно закрыты и внутренняя семантика revised draft детерминирована, не выдавая поблажек автору редакции.

Подтвержденные факты и закрытые решения, которые не нужно спрашивать повторно:
- предыдущий независимый verdict был `AUDIT_PASS_WITH_FIXES`;
- production STABLE release отсутствует и production pointer не назначен;
- текущий development candidate остается `0.1.0-draft`;
- автоматическое создание ChatGPT Projects, автоматическая вставка Project Instructions, автоматическое создание/переименование чатов и внешний исполнитель роли Дирижёра сознательно не входят в эту итерацию;
- интерфейс Дирижёра должен оставаться natural-language/low-friction, без обязательной магической команды;
- version pinning существующих проектов и запрет silent upgrade должны сохраняться;
- межпроектная видимость сама по себе не является разрешением; bootloader может давать только узкое read-only разрешение на Orchestration bootstrap source.

Что было исправлено редактором и требует проверки, а не доверия:
1. deterministic bootstrap discovery/bootloader, failure states, storage preflight и post-create readback;
2. точная семантика `next_chat_serial`, включая `01 -> 02`, reserve/increment-before-handoff, no-reuse и сериализацию parallel allocation;
3. точный `PROJECT_UPGRADE` gate: read-only plan -> independent audit для nontrivial/breaking -> explicit Conductor approval конкретного плана -> writes;
4. universal source-priority/conflict-resolution contract внутри release;
5. local `AGENTS.md` только для project-specific deltas/roles/constraints/access/approval + pinned release reference;
6. independent audit как отдельный chat/agent context без self-fixing во время verdict;
7. handoff contract с confirmed facts, permissions/approvals, closed gates, blockers/prohibitions;
8. DRAFT metadata и раздельные development/production поля CURRENT.

Обязательные проверки:
- сопоставь каждый MUST fix предыдущего аудита с конкретным нормативным текстом revised strategy и release;
- проверь, что bootloader решает chicken-and-egg discovery для brand-new project и не открывает доступ к другим проектам;
- проверь все failure states и запрет claim success без persistence readback;
- проверь, что `next_chat_serial` не допускает повторного serial при replacement/retry/parallel branch по заявленному контракту;
- проверь, что ни одно project upgrade write не возможно до требуемого независимого аудита и явного approval точного плана;
- проверь непротиворечивость source priority между intent/authorization и verified factual state;
- проверь, что local `AGENTS.md` не дублирует global mechanics;
- проверь реальную независимость audit/re-audit semantics;
- проверь полноту replacement handoff;
- проверь, что `CURRENT.md` не назначает STABLE и revised draft не выдает себя за production release;
- отдельно отметь новые регрессии или неоднозначности, если редакция их внесла.

Запреты:
- не исправляй проверяемые файлы сам в процессе verdict;
- не переводить release в STABLE;
- не назначать production pointer;
- не внедрять автоматизацию ChatGPT Projects или внешнего Дирижёра;
- не считать список заявленных исправлений доказательством их корректности без проверки текста.

Ожидаемый результат:
- независимый audit artifact в `/Orchestration/audits/` с verdict и матрицей MUST fixes;
- допустимые verdict: `AUDIT_PASS`, `AUDIT_PASS_WITH_FIXES` или `AUDIT_FAIL`;
- если verdict не `AUDIT_PASS`, перечислить конкретные обязательные исправления и вернуть их отдельному owner/editor;
- если verdict `AUDIT_PASS`, только зафиксировать готовность к следующему отдельному promotion decision; не выполнять promotion самостоятельно.

Критерий завершения роли: каждый MUST fix проверен по revised artifacts, verdict обоснован, production pointer не изменен, lifecycle/next step определены.

В финале применить completion contract:
`AGENT_DECISION`, `NEXT_STEP`, `NEW_AGENT_REQUIRED`, а при `YES` — полный `NEXT_AGENT_PROMPT` с подтвержденными фактами, разрешениями и закрытыми gates.
