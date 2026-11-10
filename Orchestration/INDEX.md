# Orchestration — INDEX


Current reconciliation: 2026-11-08; 0.4.3 STABLE; three registered branches have lifecycle ARCHIVED, no open lifecycle branches. Historical full root INDEX snapshot: /Orchestration/Status/20261108T2202Z--vnext-archive-reconciliation/previous/INDEX.md.


## Entry points


- `/Orchestration/INIT.md` — project purpose and invariant rules.
- `/Orchestration/STATUS.md` — current operational state and next gate.
- `/Orchestration/AGENTS.md` — universal role/lifecycle rules used while developing this system.


## Audit


- `/Orchestration/audits/library-baseline-audit-2026-10-26.md` — audit of reusable practices already present in Library.
- `/Orchestration/audits/project-bootstrap-protocol-audit-2026-10-26.md` — independent audit of the initial strategy/protocol; verdict `AUDIT_PASS_WITH_FIXES`.
- `/Orchestration/audits/project-bootstrap-protocol-reaudit-2026-10-27.md` — fresh independent re-audit of the revised `0.1.0` draft; verdict `AUDIT_PASS`.
- `/Orchestration/audits/legacy-adoption-protocol-audit-2026-10-27.md` — ORCH-05 independent audit of `0.2.0-draft`; verdict `AUDIT_PASS_WITH_FIXES`; produced three MUST fixes.
- `/Orchestration/audits/legacy-adoption-protocol-reaudit-2026-10-27.md` — ORCH-07 fresh independent re-audit after ORCH-06 fixes; verdict `AUDIT_PASS`; the audited candidate was subsequently promoted by explicit Conductor approval.
- `/Orchestration/audits/branch-lifecycle-protocol-audit-2026-10-27.md` — ORCH-08 independent audit of `0.3.0-draft`; verdict `AUDIT_PASS_WITH_FIXES`; produced three MUST fixes.
- `/Orchestration/audits/branch-lifecycle-protocol-reaudit-2026-10-27.md` — ORCH-10 fresh independent re-audit after ORCH-09 corrections; verdict `AUDIT_PASS`; all prior MUST/SHOULD findings closed.


## Strategy


- `/Orchestration/strategy/universal-project-launch-strategy.md` — living universal strategy underlying the STABLE `0.3.0` branch-lifecycle contract.
- `/Orchestration/strategy/legacy-adoption-fix-2026-10-27.md` — defect analysis and design rationale for the `0.2.0` legacy-adoption correction.
- `/Orchestration/strategy/branch-lifecycle-2026-10-27.md` — design rationale for persistent parallel branch lifecycle promoted in STABLE `0.3.0`.
- `/Orchestration/strategy/autonomous-execution-field-guide-2026-11-07.md` — проверенная методика самостоятельного технического исполнения, least privilege, rollback, live readback и независимого аудита (NON-NORMATIVE; источник — RDCX/MikroTik).


## Protocol


- `/Orchestration/protocol/CURRENT.md` — production pointer; STABLE `0.4.3`, no active development candidate.
- `/Orchestration/protocol/CHANGELOG.md` — protocol history and compatibility notes.
- `/Orchestration/protocol/releases/v0.4.3/PROTOCOL.md` — current production STABLE release, dated 2026-11-08.
- `/Orchestration/protocol/releases/v0.4.2/PROTOCOL.md` — historical STABLE.
- `/Orchestration/protocol/releases/v0.4.1/PROTOCOL.md` — historical STABLE.
- `/Orchestration/protocol/releases/v0.4.0.md` — historical STABLE, approved 2026-11-08.
- `/Orchestration/protocol/releases/v0.4.0-draft.md` — historical development candidate retained for provenance.
- `/Orchestration/protocol/releases/v0.3.0.md` — historical STABLE release; immutable.
- `/Orchestration/protocol/releases/v0.3.0-draft.md` — historical audited draft retained for provenance; ORCH-10 verdict `AUDIT_PASS`.
- `/Orchestration/protocol/releases/v0.2.0.md` — historical STABLE release; immutable; projects pinned to it remain there until explicit upgrade.
- `/Orchestration/protocol/releases/v0.2.0-draft.md` — historical audited draft retained for provenance.
- `/Orchestration/protocol/releases/v0.1.0.md` — historical STABLE release; immutable.
- `/Orchestration/protocol/releases/v0.1.0-draft.md` — historical draft retained for provenance.


## Branches


- `/Orchestration/branches/` — canonical branch control plane; `/Orchestration/branches/archive/` holds physically archived vNext.
- `/Orchestration/branches/archive/orchestration-vnext/RESULT.md` — terminal branch archive act and preserved audit/result evidence.
- `/Orchestration/Status/20261108T1333Z--orchestration-vnext-archived--superseded-by-0-4-3/DETAILS.md` — clarification of prior archive event.
- `/Orchestration/Status/20261108T2202Z--vnext-archive-reconciliation/DETAILS.md` — verified root reconciliation and preserved historical snapshots.


## Branch registry / non-reuse ledger


| branch_id | current label | canonical path | mutation state | lifecycle | mutation_id |
| --- | --- | --- | --- | --- | --- |
| `github-orchestration` | GitHub orchestration | `/Orchestration/branches/github-orchestration/` | `STABLE` | `ARCHIVED` (legacy logical archive, physical folder unmoved) | `-` |
| `branch-b0ae2385` | Идеи для реализации в следующей версии | `/Orchestration/branches/branch-b0ae2385/` | `STABLE` | `ARCHIVED` (legacy logical archive, physical folder unmoved) | `-` |
| `orchestration-vnext` | Orchestration vNext — разработка и релиз | `/Orchestration/branches/archive/orchestration-vnext/` | `STABLE` | `ARCHIVED` (physical path verified) | `-` |


## Handoffs


- `/Orchestration/branches/archive/orchestration-vnext/AUDITOR-HANDOFF-ORCH-18-2026-11-04.md` — fresh read-only gate after the ORCH-17 metadata correction.
- `/Orchestration/branches/archive/orchestration-vnext/ORCH-17-INDEPENDENT-RELEASE-AUDIT-2026-11-04.md` — RC3 verdict `AUDIT_PASS_WITH_FIXES`; one MUST in `candidate_identity` fields.
- `/Orchestration/branches/archive/orchestration-vnext/ORCH-18-INDEPENDENT-RELEASE-AUDIT-2026-11-04.md` — same RC3 digest `AUDIT_PASS` after the identity metadata fix.


- `/Orchestration/branches/archive/orchestration-vnext/AUDITOR-HANDOFF-ORCH-17-2026-11-04.md` — fresh independent audit handoff for frozen 1.0.0-rc3.
- `/Orchestration/branches/archive/orchestration-vnext/ORCH-15-INDEPENDENT-RELEASE-AUDIT-2026-11-04.md` — RC1 verdict `RELEASE_AUDIT_NOT_READY`.
- `/Orchestration/branches/archive/orchestration-vnext/ORCH-16-INDEPENDENT-RELEASE-AUDIT-2026-11-04.md` — RC2 verdict `AUDIT_FAIL`; standalone artifact hashes did not match the package manifest.


- `/Orchestration/handoffs/legacy-adoption-independent-auditor-prompt-2026-10-27.md` — completed `ORCH-05` independent-audit handoff for `0.2.0-draft`.
- `/Orchestration/handoffs/legacy-adoption-fresh-reauditor-prompt-2026-10-27.md` — completed `ORCH-07` fresh independent re-audit handoff after ORCH-06 MUST fixes.
- `/Orchestration/handoffs/branch-lifecycle-independent-auditor-prompt-2026-10-27.md` — completed `ORCH-08` independent-audit handoff for `0.3.0-draft`.
- `/Orchestration/handoffs/branch-lifecycle-fresh-reauditor-prompt-2026-10-27.md` — completed `ORCH-10` fresh independent re-audit after ORCH-09 corrections; verdict `AUDIT_PASS`.
- `/Orchestration/handoffs/strategy-independent-auditor-prompt-2026-10-26.md` — prompt used for initial independent review.
- `/Orchestration/handoffs/protocol-independent-reauditor-prompt-2026-10-26.md` — handoff used for the completed `0.1.0` fresh re-audit.


Historical: STABLE `0.3.0` was promoted on 2026-10-28 after ORCH-10 `AUDIT_PASS` and explicit Conductor approval. Persisted `next_chat_serial` is `23`. ORCH-19 and ORCH-20 were used as chat/task titles without required advance serial reservation; both are permanently consumed by explicit Conductor-approved reconciliation on 2026-11-05 and must never be reused. ORCH-21 was reserved and consumed for the scoped Library-only follow-up Executor. ORCH-22 is reserved for a fresh independent read-only audit of the exact ORCH-21 Library artifacts; this reservation advances the project-wide serial before the scheduled auditor chat is published. ORCH-13 is the vNext Executor; ORCH-14 and ORCH-15 are completed; ORCH-16 returned `AUDIT_FAIL` for RC2; ORCH-17 returned `AUDIT_PASS_WITH_FIXES` for RC3; ORCH-18 returned `AUDIT_PASS` for the same digest after the metadata correction. ORCH-11 and ORCH-12 are consumed.


Current facts take precedence over the historical narrative above: CURRENT points to 0.4.3 STABLE. The archived 1.0.0-rc3 candidate never became that release and has no 1.0.0 deployment/publication authorization. The two other branches' legacy directories still reside immediately under /branches/ despite their own archived lifecycle status; physical placement was not changed in this vNext reconciliation. No branch ID or existing serial number is reused or advanced.