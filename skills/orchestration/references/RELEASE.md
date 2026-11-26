# Immutable candidate and independent audit — review contract

1. Freeze scope and an acceptance matrix before creating a versioned candidate. Preserve all historical drafts; never overwrite v0.4.4-draft-01 or v0.4.4-draft-02.
2. Identify the exact payload by immutable commit/ref, per-file SHA-256 and a deterministic manifest digest. Publish reproducible metrics: bytes, sections, normative rules and changed modules. An unpinned main link is not a candidate identity.
3. Run static and behavioral tests separately. Static checks cannot prove host routing, Library writes/moves, source-project postconditions or migrations. Each scenario needs exact input, expected/observed result, run ID, authority and PASS/FAIL/NOT_VERIFIED.
4. Require a separate non-author agent/context, identity and non-overlap receipt, read-only inspection of the exact digest, and an independent verdict. A scheduled audit, separate window, self-review or matching hash alone is not a PASS.
5. Correct findings in a NEW immutable candidate revision; re-audit that exact revision. AUDIT_PASS_WITH_FIXES, AUDIT_FAIL, NOT_READY and INDEPENDENCE_UNVERIFIED block release.
6. Present diff, test evidence, auditor verdict, risks, compatibility, rollback and exact proposed release to the owner. No global CURRENT, main merge, STABLE, installed Plugin or local pin change before **explicit owner approval**.
7. After approval, publish approved payload/tag, verify pointer and distribution separately, and read back. Existing projects migrate only by explicit per-project PROJECT_UPGRADE.

Historical draft-02 audit: 1 of 29 behavioral scenarios PASS, 28 NOT_VERIFIED; independence unverified. This is not acceptance of this candidate.
## Frozen S1–S6 scope preservation (audit F03)

| Gate | Contract source | Acceptance condition |
|---|---|---|
| S1 incident identity/evidence | [EVIDENCE.md](EVIDENCE.md) | One family per incident, source versus independent status, measurable postcondition |
| S2 truthful commands/capability | [COMMANDS.md](COMMANDS.md) | 14 intents with aliases, prereqs, negative outcomes and distinct proof levels |
| S3 local pin and legacy | [RESOLVER.md](RESOLVER.md) | Fail closed on conflicting markers, 0.3.0/0.4.0/0.4.1+ isolation |
| S4 monitoring opt-in | [EVIDENCE.md](EVIDENCE.md) | No recurring monitor without explicit target/cadence/stop/actions; preserve authorized jobs |
| S5 execution/delivery/irreversible proof | [EVIDENCE.md](EVIDENCE.md) | SCHEDULED, SUBMITTED, CONVERSATION_NOT_LOADED, DELIVERY_UNKNOWN, Task ID and recipient validation |
| S6 immutable candidate/owner gate | This file and [MIGRATION.md](MIGRATION.md) | Exact SHA-256, T01–T24/M01–M05, non-author audit, owner approval before STABLE |

The historical `v0.4.4-draft-01/02` Library candidates remain immutable and separate. PR #8 is a GitHub source-review artifact, **not** a released protocol candidate. Freeze a new versioned payload only after the full manifest, acceptance evidence and source mapping are complete.

## Audit finding disposition

F01 full D01–D25 roles: addressed in candidate STORAGE; real consumer crosswalk pending.
F02 current complete Library object-ID manifest: OPEN.
F03 S1–S6 mapping: addressed in candidate references; host behavior pending.
F04 behavioral T/M tests: OPEN.
F05 non-atomic move, rollback, concurrent writers: OPEN.
F06 independently attributable non-author audit: OPEN.
F07 command alias and negative table: addressed in candidate COMMANDS; unprimed routing pending.
F08 multiple adopted markers: addressed in candidate RESOLVER; real fixtures pending.
F09 immutable exact SHA-256 release payload: OPEN.

No finding is declared closed for production merely because text was updated. New head commits invalidate the previous PR #8 audit's exact-SHA target and require a fresh audit after freeze.
