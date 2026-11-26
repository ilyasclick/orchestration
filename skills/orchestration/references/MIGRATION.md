# Per-project migration — review candidate

No project migration is authorized by publication of this reference.

Preflight:
1. Obtain explicit owner approval for the exact target project and target STABLE version. No adjacent project or automatic global-pin migration.
2. Save a durable exact path/object-ID manifest, legacy consumer crosswalk, mandatory safety guards, local pin, hashes where possible, case-collision assessment and exact rollback manifest. The earlier 2102-file/532-folder enumeration is NOT a saved 2634-row manifest.
3. Prove no concurrent writer. Test safe moves, history selection, link integrity and rollback on an authorized disposable fixture. Do not assume multi-operation atomicity.
4. Negative fixtures: real 0.3.0, 0.4.0, 0.4.1+, 0.4.3 pins; missing/contradictory pin; stale INDEX; duplicate active topic; archive collision; case-only alias; broken link; nested workstream; no-monitoring opt-in.
5. If any required evidence is absent, return MIGRATION_BLOCKED and leave adopted marker unchanged.

Cutover:
1. Freeze only the authorized project's writers; record exact prestate.
2. Create modules/events under unique paths. For approved replacements, verify one active top-level topic, move old document to history/, create new immutable active document, and read back each step.
3. Verify safety modules, resolver, 14 semantic intent outcomes, status provenance, legacy compatibility and negative fixtures without external sends or production changes.
4. Save the universal Project Instructions required by the applicable protocol. A Library file is not proof that ChatGPT Project UI settings changed.
5. Switch the local adopted marker LAST, only after all readbacks and guards pass. Never overwrite existing markers. Record and verify the transition event.

Failure/rollback: stop on races, broken links, partial moves or unknown outcomes. Reverse only exact verified moves with no later writer; never recursive-delete. If safe reversal cannot be proven, return ROLLBACK_REQUIRES_OWNER_DECISION with affected paths.

OrchVoice runtime, other-project technical fixes, recurring monitoring and global STABLE promotion are separate operations.