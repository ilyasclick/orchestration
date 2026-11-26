# Next release: closure criteria and execution plan

Date: 2026-11-25
Canonical Library branch: /Orchestration/branches/next-release-incidents-commands-20261115/
Development GitHub branch: next-release-architecture-20261125 (not Library state)
Production baseline: 0.4.3 STABLE. Owner approval required before promotion.

| Gate | Exact acceptance | Current state |
|---|---|---|
| C1 — Incidents | All relevant source incidents canonicalized without duplicate counting; source, owner, severity, status and independently verified postcondition or explicit UNKNOWN | PARTIAL: 87 direct + 1 nested incident inventory; normalization and live postconditions incomplete |
| C2 — Commands | All 14 semantic intents documented with aliases, scope, approval, support level and negative receipts; Skill, CLI and voice separated | PARTIAL: contracts drafted, host routing and runtime execution unverified |
| C3 — Architecture | Modular reader/storage/migration/release contracts; full authoritative D01–D25 map; refreshed durable 2634-object path/ID manifest; consumer crosswalk and rollback | PARTIAL: contracts drafted; per-object Library manifest missing |
| C4 — Acceptance/audit | Immutable exact-digest candidate; reproducible metrics; authorized behavioral tests; attributable non-author audit; re-audit after fixes | NOT_READY: historical draft-02 had 1 PASS/28 NOT_VERIFIED |
| C5 — Owner approval | Present exact candidate, diff, evidence, risks and rollback; obtain explicit approval before STABLE | NOT_STARTED |

Ordered work:
1. Read local adopted STABLE, branch, latest incident/command evidence and historical audits; keep GitHub, Skill, local pin and runtime distinct.
2. Implement nonproduction reference contracts and minimal Skill routing on a feature branch; do not change CURRENT, main or immutable releases.
3. Validate all 14 intents and static guards; distinguish static from real behavioral acceptance.
4. Persist refreshed full Library path/object-ID manifest and authoritative D01–D25 mapping; classify every live legacy reader before migration. This is a hard gate.
5. Test authorized read-only/disposable fixtures: pins, active/archive, status, history move/rollback, case aliases, fresh-host routing, monitoring opt-in and project-specific safety.
6. Freeze new immutable draft, exact SHA-256 digest, independent auditor identity and test receipts. Fix in a new revision and re-audit.
7. Present owner approval packet; do not release STABLE or migrate other projects before separate approvals.

Limitations: earlier 2634 count was a non-atomic enumeration, not a saved per-file manifest. The canonical Library branch is not writable via the currently exposed tools in this execution. GitHub work is NOT Library readback or migration evidence. No independent PASS is claimed.

AGENT_DECISION: CONTINUE
NEXT_STEP: Complete source verification and independent review, then obtain current Library manifest and behavioral receipts.
NEW_AGENT_REQUIRED: YES (independent auditor)