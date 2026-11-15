# Orchestration skill distribution and version authority

The source repository is https://github.com/ilyasclick/orchestration (maintained by its repository owner). Published protocol releases are immutable. `Orchestration/protocol/CURRENT.md` names the global production STABLE; its content is not an automatic instruction to migrate existing projects. Existing projects record their locally adopted protocol and only upgrade explicitly.

## Consumer account installation

1. Acquire the approved skill bundle or install the skill-only plugin through a supported ChatGPT/Codex interface.
2. Separately import the **exact manifest-listed** runtime files from `packaging/manifests/runtime-package.json` into the target account's `/Orchestration/protocol/`. Verify SHA-256 and read back the imported files. Refuse ambiguous overwrite or divergent local state.
3. If the host requires it, add `packaging/bootstrap/USER_INSTRUCTIONS.txt` to user/workspace instructions. This is **not automatically installed** by the GitHub package.
4. Verify both the skill's installed/active state in the host and a real disposable project bootstrap with durable Library readback.
5. Record source commit, protocol version, actual verification, and any blockers in account-local `/Orchestration/deployment/INSTALLATION.md`. Do not export this file back to GitHub.

## Maintainer workflow

1. Read the Orchestration canonical Library snapshot and current release pointer, then plan a scoped change.
2. Change skill/packaging source in a Git feature branch; use a PR/review and test bundled paths, manifest consistency, and isolation. Do not change immutable `protocol/releases/*` files in place.
3. Publish a reviewed commit or tag to `ilyasclick/orchestration` only with the necessary authorization. Do not represent a PR as a merged release.
4. Do not import a GitHub commit over the account's live Library state or other projects. If necessary, perform an explicit, verified runtime import and record the source commit.
5. A future protocol release may update the runtime package and pointer while this skill's entry point stays stable and resolves `CURRENT.md` dynamically.

A ChatGPT Plus subscription alone does not prove custom skill creation/upload is available in a particular ChatGPT surface. Use whatever skill/plugin install controls are actually offered. Installing files into GitHub, a remote computer, Codex, or Library does not by itself register a skill in this ChatGPT account.