# Semantic commands — review candidate

These are natural-language intents, not a CLI/parser, guaranteed host routing, or OrchVoice dispatch. Read the target project's adopted release first. Report support as DOCUMENTED, SKILL_SOURCE_VERIFIED, HOST_ACTIVATION_VERIFIED, UNPRIMED_ROUTING_VERIFIED, EXECUTED_AND_READBACK_VERIFIED, CLI_PARSER_VERIFIED or VOICE_DISPATCH_VERIFIED, without conflating levels.

| Intent | Example phrase | Scope, side effects and proof |
|---|---|---|
| `PROJECT_BOOTSTRAP` | создай проект | New authorized project only; exact STABLE source, created files and readback |
| `BRANCH_LIST` | список веток | Read-only; actual direct active/archive folders, not stale INDEX |
| `BRANCH_CREATE` | создай ветку | Authorized project; unique folder, scope, collision check and readback |
| `BRANCH_RESUME` | продолжи ветку | Resolve exact branch and latest events; no automatic replay |
| `BRANCH_CLOSURE_CRITERIA` | критерии закрытия ветки | Strictly read-only; criteria and evidence, never close/archive/launch audit |
| `BRANCH_ARCHIVE` | архивируй ветку | Explicit exact-target approval; preserve handoff, move and readback both locations |
| `BRANCH_RESTORE` | восстанови ветку | Explicit exact-target approval; collision check, move and readback |
| `SELF_ARCHIVE_PREPARE` | подготовь чат к архиву | Save handoff; UI chat archival is a separate verified action |
| `PROJECT_UPGRADE` | обнови проект | Exact project/version approval; manifest, rollback, adopted marker last |
| `VERSION_CHECK` | какая версия | Read-only; distinguish GitHub source, installed Skill, global STABLE, local pin and voice runtime |
| `INDEPENDENT_AUDIT` | независимый аудит | Separate non-author agent/context; exact immutable digest, attribution and verdict |
| `HANDOFF` | передай задачу | Save and read back handoff; sending/launching requires separate receipt |
| `STATUS_READ` | статус ветки | Read-only; actual event and delivery receipts, not filenames |
| `HELP` | доступные команды | Read-only; describe documented versus tested capabilities |

## Phrase aliases, prerequisites and negative outcomes

These phrases are examples for semantic interpretation only. There is no dedicated CLI/parser or proven unprimed voice route. Every command requires an exact authorized target, applicable local pin and capability check.

| Intent | Accepted phrase family | Minimum prerequisite | Negative outcome |
|---|---|---|---|
| PROJECT_BOOTSTRAP | «создай проект», «запускай проект», `init` | New project root and exact GitHub STABLE | Existing root without explicit upgrade → STOP |
| BRANCH_LIST | «список веток», «покажи ветки» | Read active/archive direct children | Missing local pin → LOCAL_PROTOCOL_UNRESOLVED |
| BRANCH_CREATE | «создай ветку», «новая ветка» | Owner create intent, unique ID, collision check | Existing ID in either location → CONFLICT |
| BRANCH_RESUME | «продолжи ветку», «вернись к ветке» | Exact ID/path, events and scope | Ambiguous label → ASK_EXACT_TARGET |
| BRANCH_CLOSURE_CRITERIA | «критерии закрытия», «что осталось», «проверь готовность ветки» | Read-only evidence and original criteria | No audit/archive/close side effects |
| BRANCH_ARCHIVE | «закрой ветку», «архивируй ветку» | Explicit owner intent, exact ID, handoff, move tool | Collision, no move tool or unknown outcome → BLOCKED |
| BRANCH_RESTORE | «восстанови ветку», «верни из архива» | Exact archived ID, owner intent, free active path | Collision or no verified move → BLOCKED |
| SELF_ARCHIVE_PREPARE | «подготовь чат к архиву», «архивируй себя» | Exact current chat/branch, saved handoff | Never archive branch or UI chat by implication |
| PROJECT_UPGRADE | «обнови проект до версии», «обнови до STABLE» | Explicit project/version, exact pin, migration evidence | No approval or pin conflict → BLOCKED |
| VERSION_CHECK | «какая версия», «проверь обновления» | Distinct GitHub/installed/global/local/voice layers | One check does not authorize weekly monitor |
| INDEPENDENT_AUDIT | «проведи независимый аудит», «проверь релиз» | Immutable exact payload and non-author reviewer | No identity/non-overlap proof → INDEPENDENCE_UNVERIFIED |
| HANDOFF | «передай задачу», «подготовь поручение» | Exact task/branch/recipient and permission | Saved handoff ≠ submitted/delivered |
| STATUS_READ | «покажи статус», «статус ветки» | Verified status event and receipts | No status inference from newest filename |
| HELP | «покажи команды», `@Orchestration help` | Current catalog and capability evidence | Never imply installed CLI or voice dispatch |

External send, destructive action, scheduling, and migration require their own explicit scope; a broad intent is not a substitute. An unknown send/archive outcome must be reconciled by exact target, Task ID and post-action receipt before any retry. See [EVIDENCE.md](EVIDENCE.md).

For all writes: resolve authority, verify target and current state, use append-only history, require consent for irreversible actions, and read back. Distinguish PLANNED, QUEUED, LAUNCHED, EXECUTED, DELIVERED, ACCEPTED and REMEDIATED. Unknown delivery forbids blind retry. Explicit monitoring opt-in requires target, cadence, stop condition and permitted actions; "check now" is not consent for recurring automation. External sends require exact recipient verification.

No semantic intent implies a registered executable command. A GitHub commit does not update an installed Skill, Library, production protocol, or OrchVoice runtime.