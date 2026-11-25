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