# Install

## What a skill is

A skill is a folder containing a `SKILL.md` with YAML frontmatter:

```markdown
---
name: cinescroll
description: When to use this skill, in the model's own decision language.
---

The instructions Claude follows once the skill loads.
```

Claude Code reads every skill's `name` + `description` at startup and pulls the
body into context only when the task matches. That is why descriptions here are
long and trigger-heavy — they are matching text, not marketing.

Some skills carry extra files (`reference/`, `scripts/`, `assets/`). Keep the
folder intact; don't copy `SKILL.md` alone.

---

## Where skills go

| Scope | Path | Use when |
| --- | --- | --- |
| User | `~/.claude/skills/<name>/` | You want it in every project |
| Project | `<repo>/.claude/skills/<name>/` | Team-shared, committed with the repo |

On Windows, `~` is `C:\Users\<you>`, so user skills live in
`C:\Users\<you>\.claude\skills\`.

---

## Install everything

### macOS / Linux

```bash
git clone https://github.com/hyperdargo/ClaudeSkillAndPluginsWithMasterPrompt.git
cd ClaudeSkillAndPluginsWithMasterPrompt
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

### Windows (PowerShell)

```powershell
git clone https://github.com/hyperdargo/ClaudeSkillAndPluginsWithMasterPrompt.git
cd ClaudeSkillAndPluginsWithMasterPrompt
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.claude\skills\"
```

### Windows (Git Bash)

```bash
mkdir -p ~/.claude/skills && cp -r skills/* ~/.claude/skills/
```

**Copying overwrites same-named skills.** If you already have customised
versions, back them up first:

```bash
cp -r ~/.claude/skills ~/.claude/skills.backup
```

---

## Install a subset

Copy only the folders you want:

```bash
cp -r skills/master-website-engineering ~/.claude/skills/
cp -r skills/cinescroll               ~/.claude/skills/
cp -r skills/impeccable               ~/.claude/skills/
```

Fewer skills means cleaner routing. Installing five overlapping design skills
makes Claude's choice worse, not better.

---

## Symlink instead of copy (stay in sync with `git pull`)

```bash
# macOS / Linux
for d in skills/*/; do
  ln -sfn "$(pwd)/$d" ~/.claude/skills/"$(basename "$d")"
done
```

```powershell
# Windows PowerShell — needs an elevated shell or Developer Mode
Get-ChildItem .\skills -Directory | ForEach-Object {
  New-Item -ItemType SymbolicLink `
    -Path "$env:USERPROFILE\.claude\skills\$($_.Name)" `
    -Target $_.FullName -Force
}
```

---

## Verify

1. Restart Claude Code (skills are read at startup).
2. Ask: *"which skills do you have available?"*
3. Or trigger one directly — type `/` and look for user-invocable ones such as
   `/impeccable`, `/ponytail-help`, `/caveman`.

---

## Troubleshooting

**A skill never activates.**
Check the folder is `~/.claude/skills/<name>/SKILL.md` — a nested extra
directory (`skills/cinescroll/cinescroll/SKILL.md`) breaks discovery.

**Frontmatter errors.**
`name` and `description` are both required. `name` must match the folder name
and be lowercase-kebab-case.

**It loads but ignores the instructions.**
Say the skill name explicitly: *"use the cinescroll skill for this"*.

**Two skills fight over the same task.**
Remove one. `design-taste-frontend` and `design-taste-frontend-v1` are the same
skill at two versions — keep one. Same for overlapping visual-design skills.

**`graphify` loads but every command fails.**
The skill drives a Python CLI that isn't in this repo. Install it with
`uv tool install graphifyy` (or `pipx install graphifyy`). If `graphify` isn't
found afterwards, run `uv tool update-shell` and open a new terminal.
`graphify install` can also write the skill for you. It adds a short `/graphify`
note to `~/.claude/CLAUDE.md`.

**Scripts won't run.**
A few skills (`impeccable`, `caveman-stats`) ship helper scripts that need
`Bash(...)` permissions and, in some cases, Node. Check that skill's own
`SKILL.md` frontmatter for its `allowed-tools`.

---

## Uninstall

```bash
rm -rf ~/.claude/skills/<name>
```

Then restart Claude Code.
