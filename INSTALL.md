# Install skills

## Safe installation

Requires Python 3.9+. Run from this repository. Existing files and custom skill folders are never overwritten.

```sh
python scripts/install_skills.py --target ~/.claude/skills --dry-run
python scripts/install_skills.py --target ~/.claude/skills
```

The same commands work in PowerShell, macOS and Linux when `python` is available. Use `python3` if that is your Python executable.

For a subset:

```sh
python scripts/install_skills.py --target ~/.claude/skills --skill animate --skill cinescroll
```

For project-local skills, use `--target .claude/skills`. For another assistant, including Hermes, supply the actual directory configured by that host or profile. This installer does not discover profiles, install plugins, or adapt tool names.

## Updating an existing skill

Existing directories are skipped deliberately. Compare your installed copy against this repository, back it up, and merge the changes you want. The installer has no overwrite switch.

## Platform packages

`platform-skills/` contains Codex system and plugin packages for reference and source identification. They are excluded from the installer because their tools and runtime services must be supplied by the corresponding host. See [platform compatibility](platform-skills/README.md).

## Dependencies and verification

Keep each skill's whole folder together. Read its `SKILL.md` for required CLIs, packages, environment variables and permissions. Dependencies such as `node_modules`, virtual environments and caches are not distributed. Install dependencies only for skills you intend to use.

Restart or reload your assistant as required by its host, then confirm the selected skill is discovered. A successful copy does not prove its commands work in that host.

Validate this snapshot with:

```sh
python scripts/verify_catalog.py
```

The validator checks inventory, unique IDs, paths and normalized SKILL.md hashes; it does not execute third-party skill scripts.
