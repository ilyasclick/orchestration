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

For all writes: resolve authority, verify target and current state, use append-only history, require consent for irreversible actions, and read back. Distinguish PLANNED, QUEUED, LAUNCHED, EXECUTED, DELIVERED, ACCEPTED and REMEDIATED. Unknown delivery forbids blind retry. Explicit monitoring opt-in requires target, cadence, stop condition and permitted actions; "check now" is not consent for recurring automation. External sends require exact recipient verification.

No semantic intent implies a registered executable command. A GitHub commit does not update an installed Skill, Library, production protocol, or OrchVoice runtime.