# Orchestration skill distribution and version authority

The public source repository is https://github.com/ilyasclick/orchestration. Published STABLE release contents are immutable. The GitHub file `Orchestration/protocol/CURRENT.md` identifies the production STABLE for a **new** project. It is not consent to migrate an existing project, whose locally adopted version remains authoritative.

## Fresh consumer account / GitHub-plugin installation

1. Install or connect the Orchestration plugin/skill from the supported GitHub source.
2. No preexisting `/Orchestration/` Library tree or manual import is required for **new-project bootstrap**. The skill reads `Orchestration/protocol/CURRENT.md` directly from public GitHub and follows the exact STABLE path in the same repository. A supported GitHub connector or web reader suffices for public read access.
3. Create only the authorized target project's Library control-plane state, following the selected release. Confirm actual saved project files with readback. Do not claim Library writes occurred if no compatible file tool was available.
4. The optional `packaging/bootstrap/USER_INSTRUCTIONS.txt` host hook is **not automatically installed**. A linked skill is not proof that host/user/project instructions were updated.
5. If GitHub cannot be fetched, report the source-access blocker; no hard-coded 0.3.0 fallback and no fabricated version or successful initialization.

## Existing-project compatibility and optional local installation

- Existing projects keep `Protocol/adopted/` or confirmed legacy protocol pins until an authorized PROJECT_UPGRADE.
- Fetch the exact historical STABLE release from authorized local files or GitHub; missing global `/Orchestration/protocol/CURRENT.md` alone is never a reason to replace an existing pin.
- `packaging/manifests/runtime-package.json` still documents an **optional** local protocol cache/import for offline or managed deployments. If imported, preserve paths, validate checksums, avoid overwrite, and read back. It is not an installer prerequisite for GitHub-plugin bootstrap.
- GitHub is portable protocol source, not live account project state. Do not export credentials or account-specific runtime.
- Publishing to the GitHub repository does not prove an already installed plugin in another account automatically refreshed. Verify its activation or reconnect/update through supported host controls.

## Maintainer publication

Update the skill, bootstrap hook, and relevant distribution documentation together. Preserve immutable `protocol/releases/*`; update the GitHub production pointer only as part of a separately authorized protocol release. Use explicit owner authorization for direct publication and record the exact commit. Maintain a consistent manifest if any listed artifact changes. The owner can waive the separate test phase; a readback only establishes the published source, not runtime behavior in a different account.
