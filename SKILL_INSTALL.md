# Orchestration skill installation

This repository includes a skill-only Agent Plugin at `plugin.json` and `skills/orchestration/SKILL.md`.

For a ChatGPT interface that supports uploading a personal skill, upload the `orchestration-skill.zip` bundle containing the `orchestration/` directory and its SKILL.md. For a plugin/local marketplace interface, use `orchestration-plugin.zip` (root `plugin.json`, `skills/orchestration/` folder) or point a compatible plugin installer at this repository.

In a ChatGPT account with a supported Skills interface: Plugins > Skills > Create > Upload from your computer. Availability and install controls vary by account and surface. If this UI is absent, installing a ZIP in Library does not activate a skill. The Plugin Creator app may be used to create a personal plugin source and install it from the Plugins Directory.

The skill is a portable activation layer. The consumer runtime is a distinct package under `packaging/manifests/runtime-package.json`. It must be installed and verified in Library separately. Installing this skill does not migrate existing projects or change ChatGPT Project settings.

To publish updates: edit the Git source, validate, open and review a PR, merge when authorized, then reinstall/update the skill on each account (no automatic sync from GitHub is assumed). Never change a promoted protocol release in place.