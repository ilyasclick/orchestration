# Install Orchestration as an AI Agent Skill

Canonical source: https://github.com/ilyasclick/orchestration
Skill directory: `skills/orchestration/`
Agent Plugins wrapper: `plugin.json` (optional for standalone Skill)
License: [LICENSE](LICENSE)

## 1. Install from public GitHub

Use a supported Agent Skills host with Node.js 22.20+:

```bash
npx skills add ilyasclick/orchestration --skill orchestration
```

This prompts for supported target agents and defaults to project scope. For a specific agent:

```bash
npx skills add ilyasclick/orchestration --skill orchestration --agent codex --yes
```

`--agent` selects the target; `--yes` skips prompts. Other targets include `claude-code`, `github-copilot`, and `cursor`, subject to the installed CLI version. Use `--global` only when you intend to install for all local projects.

With GitHub CLI 2.90.0+:

```bash
gh skill preview ilyasclick/orchestration orchestration
gh skill install ilyasclick/orchestration orchestration --agent codex --scope project
```

`preview` inspects content without installing. `--scope project` keeps the installation local to the current project; `--agent` selects the host. For a reproducible installation, pin a published release:

```bash
gh skill install ilyasclick/orchestration orchestration --agent codex --scope project --pin v0.2.0
```

Use this pinned command only **after** the v0.2.0 tag has actually been published and verified.

## 2. Verify

Check that the selected agent's Skill directory contains `orchestration/SKILL.md`, `references/DISTRIBUTION.md`, `references/HOST-CAPABILITIES.md`, and `LICENSE`. Verify the frontmatter name is `orchestration` and ask the agent to describe its Orchestration host capability requirements. This confirms discovery and instruction loading, not ChatGPT Project bootstrap.

A real bootstrap acceptance requires a compatible authorized host, GitHub source read, target project writes, and persistent readback. Do not perform production bootstrap merely to test package discovery.

## 3. ChatGPT Plugin users

The repository also includes `plugin.json` for compatible Agent Plugins installers. A ChatGPT Plugin installation is a separate host-specific distribution channel. A GitHub commit does not automatically update a previously installed Plugin. Follow the host's supported refresh/update controls and verify the installed Skill content.

A standalone Skill does not automatically add ChatGPT Library tools, modify ChatGPT Project settings, or install `packaging/bootstrap/USER_INSTRUCTIONS.txt`.

**No mandatory local runtime import for fresh bootstrap.** The `packaging/manifests/runtime-package.json` import is optional for managed/offline use. The source of current STABLE for fresh accounts is public GitHub `Orchestration/protocol/CURRENT.md`.

## 4. Update and rollback

For Skills CLI:

```bash
npx skills check
npx skills update
```

For GitHub CLI:

```bash
gh skill update
```

To roll back, reinstall a previously verified tag or commit with `gh skill install ... --pin <tag-or-sha> --force` after inspecting that version. Do not change an existing project's `Protocol/adopted/` marker or the global STABLE protocol pointer when rolling back the Skill.

## 5. Maintainer validation and release

Run before publication:

```bash
skills-ref validate ./skills/orchestration
gh skill publish --dry-run
```

Review the diff and package paths; validate `plugin.json` against the [Agent Plugins 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json); run disposable installs and readbacks for the intended agents.

With owner authorization and GitHub authentication, publish the reviewed commit:

```bash
gh skill publish --tag v0.2.0
```

This command creates a GitHub Skill release and can add the `agent-skills` repository topic. The release/tag must be verified after publication. The skills.sh directory is an independent discovery service; an installable GitHub repository is not a guaranteed listing.

Do not overwrite immutable `Orchestration/protocol/releases/*` files, update `CURRENT.md` merely to publish a Skill, or import GitHub over live Library state.
