# Claude Skills, Plugins & Master Prompt

A browsable collection of **321 skill folders**, **18 Codex platform skill packages**, **8 Claude plugin installation guides**, and a **v3.0 master engineering prompt**.

Snapshot: **14 November 2026**. Counts reflect files in this repository, not the skills activated by any particular assistant session.

## Start here

- [Browse every skill and its source](CATALOG.md)
- [Install without overwriting custom skills](INSTALL.md)
- [Use the master prompt](MASTER-PROMPT-USAGE.md)
- [Install Claude plugins](plugins/README.md)
- [Understand Codex packages and compatibility](platform-skills/README.md)
- [Read attribution and licensing](CREDITS.md)

```sh
git clone https://github.com/hyperdargo/ClaudeSkillAndPluginsWithMasterPrompt.git
cd ClaudeSkillAndPluginsWithMasterPrompt
python scripts/install_skills.py --target ~/.claude/skills --dry-run
python scripts/install_skills.py --target ~/.claude/skills
```

The installer requires Python 3.9+ and skips existing folders. Use `--skill NAME` to select a skill; repeat it for a subset. Review each skill's tool and dependency requirements before use.

## What's included

| Location | Contents |
| --- | --- |
| [skills/](skills/) | 321 skill folders, including scripts, references and assets where supplied |
| [platform-skills/](platform-skills/) | 18 platform-dependent Codex packages, kept out of the default installer |
| [plugins/](plugins/) | Eight existing Claude plugin installation guides |
| [MASTER-PROMPT.md](MASTER-PROMPT.md) | The preserved v3.0 website and software engineering standard |
| [CATALOG.md](CATALOG.md) | Clickable skill and package inventory |
| [catalog.json](catalog.json) | Package IDs, paths, local provenance, recorded upstream URLs and hashes |
| [archive/](archive/) | Earlier master prompt |
| [scripts/](scripts/) | Non-overwriting installer and catalog verification |

## Pick a small starting set

- **Website:** `master-website-engineering`, one design skill, and `responsive-web-design`.
- **Animation:** `animate`, `animation-vocabulary`, and `review-animations`.
- **Engineering:** `planning-and-task-breakdown`, `incremental-implementation`, and `code-review-and-quality`.
- **Codebase exploration:** `graphify` or the `understand` family.

These are task groupings, not guarantees of host compatibility. Some skills require CLIs, API keys, MCP tools, specific models, or host features supplied separately.

## Sources and portability

This is a snapshot assembled from local installed skill folders. Recorded upstream URLs come from installer metadata when available. Links merely mentioned inside a skill are listed separately in the JSON catalog and are **not verified package origins**.

Claude, Codex and Hermes expose different tools. No Hermes runtime compatibility or automatic profile detection is claimed. For Hermes, pass the skill directory configured by your profile to the installer after reviewing the relevant packages. Codex plugin instructions alone do not install their services.

Third-party license and attribution files are preserved where present. This collection has no blanket license; see [CREDITS.md](CREDITS.md).
