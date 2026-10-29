# Legacy adoption deadlock — protocol correction design

Date: 2026-10-27
Owner role: Strategist / Protocol editor
Source production release: `0.1.0`
Target candidate: `0.2.0-draft`
Classification: backward-compatible MINOR capability addition

## Defect

`0.1.0` requires a nontrivial `PROJECT_UPGRADE` plan to receive independent `AUDIT_PASS` before project mutation. The same release requires a next-agent handoff to contain a previously reserved project-wide chat serial, and serial reservation requires persistent `next_chat_serial`.

A pre-Orchestration legacy project may have neither pinned protocol metadata nor `next_chat_serial`.

This creates a cycle:

`independent audit required -> separate chat required -> reserved serial required -> persistent serial write required -> all project writes forbidden before audit`

Persisting the exact migration plan before audit is also ambiguous under the blanket `no project-file mutation` wording.

## Resolution

Introduce `PRE_ORCHESTRATION_LEGACY` classification and `LEGACY_ADOPTION_PREFLIGHT`.

Before independent audit and post-audit Conductor approval, permit only bounded control-plane writes under:

`/<PROJECT>/orchestration-adoption/`

Allowed artifacts:

- `STATE.md`
- `PLAN.md`
- `HANDOFF-*.md`
- `AUDIT-*.md`
- readback/validation metadata for those artifacts

These artifacts may initialize and advance an Orchestration serial namespace solely to coordinate audit/re-audit. They must not alter operational project state, domain facts, completed work, existing gates, permissions or external systems, and they must not claim successful migration.

If no authoritative serial exists, the adoption namespace starts with `next_chat_serial: 01`; the first independent adoption auditor consumes `01`, then `02` is persisted/read back before handoff publication.

After `AUDIT_PASS`, the Conductor must explicitly approve the exact audited migration plan and target STABLE version. Only then may operational migration writes occur.

## Compatibility

Projects already managed under `0.1.0` keep the existing `EXPLICIT_MIGRATION` semantics and are not forced to upgrade.

The correction adds a new supported input state and new bounded pre-approval control-plane behavior. Under the existing versioning contract this changes the protocol contract in a backward-compatible way, so the candidate is `0.2.0-draft`, not `0.1.1`.

## Production safety

- `/Orchestration/protocol/releases/v0.1.0.md` remains immutable.
- Production CURRENT remains `0.1.0` during audit.
- `0.2.0-draft` is development-only until independent `AUDIT_PASS` and separate Conductor promotion.
