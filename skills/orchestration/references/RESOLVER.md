# Source and identity resolver — review candidate

This contract does not retroactively modify any adopted release.

1. Existing project: verify PROJECT_ROOT and authority; read confirmed `Protocol/adopted/` marker. If absent, use a legacy INIT only when its release permits. Contradictory/missing mandatory evidence means `LOCAL_PROTOCOL_UNRESOLVED`; stop writes. Never substitute global CURRENT for local adoption.
2. Fresh project: fetch one pinned GitHub commit/tag snapshot, `Orchestration/protocol/CURRENT.md`, exact immutable STABLE and its baseline dependencies. Local Orchestration Library cache is optional. If GitHub is unavailable, stop rather than guess.
3. Maintenance: read account-local adopted marker, exact STABLE, current branch evidence and pointer. GitHub is distribution, not live account state.
4. Keep five layers distinct: GitHub source, installed Skill/Plugin, global STABLE, project-local adopted and OrchVoice runtime. One never upgrades another automatically.
5. Under 0.4.0+, a direct `branches/<id>/` child is active and `branches/archive/<id>/` is archived. Nested workstreams are not branches. 0.4.0 requires BRANCH.md; 0.4.1+ permits simple folder identity. A 0.3.0 project keeps its own registry/STATUS rules.
6. Both active and archive paths, ambiguous labels, conflicting IDs or case-only collisions yield `AMBIGUOUS_BRANCH`. Do not pick the newest date, lexical maximum or a stale INDEX.
7. In 0.4.x root INDEX/STATUS snapshots are historical/supplementary. Use actual folders and later verified events.
8. Only after separately approved migration: load applicable `instructions/core/`, `instructions/workflows/`, `instructions/local/` modules by topic and applies_when. Exactly one active top-level document per topic; history/candidate/reports/tests are never auto-active. Missing safety module, broken link or competing active documents means `AMBIGUOUS_OR_INCOMPLETE`; stop.
9. `Status/status` and `Protocol/protocol` may be read aliases only after object verification. Never create case-only sibling without backend proof. Preserve legacy reader/writer behavior until explicit per-project cutover; no mixed legacy INDEX writer and new folder-only authority.

Output PROJECT_ROOT, ADOPTED_RELEASE, SOURCE_REF, BRANCH_ID, BRANCH_LOCATION, EVIDENCE_LEVEL and BLOCKERS; unresolved fields are NOT_VERIFIED.
## Deterministic multi-marker resolution (audit F08)

1. Enumerate direct children of both documented and observed adopted-marker roots, and retain **physical object IDs**. Treat case-only paths as the same object only when the backend returns the same ID. Never merge by lowercased path alone.
2. For every marker, read its complete adoption record, version, scope, approval and associated migration event. Classify as `CONFIRMED_ACTIVE`, `HISTORICAL_SUPERSEDED`, `PENDING`, `INVALID` or `UNREADABLE`. A directory name alone is not an approval receipt.
3. Exactly one `CONFIRMED_ACTIVE` marker with consistent migration readback is authoritative. Older markers count as superseded only when an explicit verified transition references them. A legacy INIT or stale INDEX never overrides a confirmed active marker.
4. Two unlinked valid-looking active markers, contradictory migration receipts, an unreadable mandatory record, or an unknown writer => `LOCAL_PROTOCOL_UNRESOLVED`; **no** lexical maximum, date maximum or global CURRENT fallback.
5. With no markers, read legacy INIT and project-specific evidence only as permitted by the project's **known historical** contract. If identity and release still cannot be proven, stop before interpreting lifecycle or changing state.
6. Return `resolution_source_id`, `adopted_version`, `supersession_event_id`, `legacy_conflicts` and `readback_status`. A proposed marker or a GitHub branch is never adoption.
7. Before an authorized project upgrade, re-read the same IDs and versions and compare with the preflight manifest. A changed source or case-alias mismatch is a concurrency conflict; stop. Switch adopted marker last after all modules and rollback paths pass.

No in-place overwrite of any historical adoption marker. This resolver is a design contract pending real host fixtures and per-project approval.
