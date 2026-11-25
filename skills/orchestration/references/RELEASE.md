# Immutable candidate and independent audit — review contract

1. Freeze scope and an acceptance matrix before creating a versioned candidate. Preserve all historical drafts; never overwrite v0.4.4-draft-01 or v0.4.4-draft-02.
2. Identify the exact payload by immutable commit/ref, per-file SHA-256 and a deterministic manifest digest. Publish reproducible metrics: bytes, sections, normative rules and changed modules. An unpinned main link is not a candidate identity.
3. Run static and behavioral tests separately. Static checks cannot prove host routing, Library writes/moves, source-project postconditions or migrations. Each scenario needs exact input, expected/observed result, run ID, authority and PASS/FAIL/NOT_VERIFIED.
4. Require a separate non-author agent/context, identity and non-overlap receipt, read-only inspection of the exact digest, and an independent verdict. A scheduled audit, separate window, self-review or matching hash alone is not a PASS.
5. Correct findings in a NEW immutable candidate revision; re-audit that exact revision. AUDIT_PASS_WITH_FIXES, AUDIT_FAIL, NOT_READY and INDEPENDENCE_UNVERIFIED block release.
6. Present diff, test evidence, auditor verdict, risks, compatibility, rollback and exact proposed release to the owner. No global CURRENT, main merge, STABLE, installed Plugin or local pin change before **explicit owner approval**.
7. After approval, publish approved payload/tag, verify pointer and distribution separately, and read back. Existing projects migrate only by explicit per-project PROJECT_UPGRADE.

Historical draft-02 audit: 1 of 29 behavioral scenarios PASS, 28 NOT_VERIFIED; independence unverified. This is not acceptance of this candidate.