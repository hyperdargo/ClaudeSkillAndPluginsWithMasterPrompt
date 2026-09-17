# Plugins

Eight plugins, each with its own install page in this folder. Plugins are
**not vendored here** — they ship their own code, dependencies and update
cycle, so copying them in would freeze them at one version and strip their
upstream licenses. Install them from their marketplaces instead.

---

## Install all eight (copy-paste)

Run these inside Claude Code, one line at a time:

```
/plugin marketplace add jarrodwatts/claude-hud
/plugin marketplace add https://github.com/secondsky/claude-skills.git
/plugin marketplace add https://github.com/addyosmani/agent-skills.git

/plugin install claude-hud@claude-hud
/plugin install cybersecurity@claude-skills
/plugin install xss-prevention@claude-skills
/plugin install csrf-protection@claude-skills
/plugin install api-design-principles@claude-skills
/plugin install playwright@claude-skills
/plugin install web-performance-audit@claude-skills
/plugin install agent-skills@addy-agent-skills
```

If `agent-skills` fails with `Could not read from remote repository`, it's
cloning over SSH. See [agent-skills.md](agent-skills.md#install) for the one-line fix.

Then restart Claude Code. Or browse and install interactively with `/plugin`.

A marketplace only needs adding once. After that, installing anything else from
it is a single `/plugin install <name>@claude-skills`.

---

## The set

| Plugin | Install page | Version | License | What it does |
| --- | --- | --- | --- | --- |
| `claude-hud` | [claude-hud.md](claude-hud.md) | 0.8.0 | MIT | Statusline HUD — model, context, cost, git state |
| `cybersecurity` | [cybersecurity.md](cybersecurity.md) | 3.9.0 | MIT | OWASP Top 10, pentest, STRIDE/ATT&CK, SAST — OSS tooling only |
| `xss-prevention` | [xss-prevention.md](xss-prevention.md) | 3.9.0 | MIT | Sanitization, output encoding, Content Security Policy |
| `csrf-protection` | [csrf-protection.md](csrf-protection.md) | 3.9.0 | MIT | Synchronizer tokens, double-submit cookies, SameSite |
| `api-design-principles` | [api-design-principles.md](api-design-principles.md) | 3.9.0 | MIT | REST and GraphQL design standards |
| `playwright` | [playwright.md](playwright.md) | 3.9.0 | MIT | Browser automation, E2E, responsive and visual checks |
| `web-performance-audit` | [web-performance-audit.md](web-performance-audit.md) | 3.9.0 | MIT | Core Web Vitals, bottlenecks, optimization plans |
| `agent-skills` | [agent-skills.md](agent-skills.md) | 0.6.9 | MIT | 25 engineering-workflow skills, 9 commands, 4 reviewer agents |

Versions are what was installed when this bundle was captured (2026-09-16;
`agent-skills` on 2026-09-17).
Run `/plugin` to pull current releases.

Sources: [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) ·
[secondsky/claude-skills](https://github.com/secondsky/claude-skills) ·
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

---

## Skills vs plugins — what's the difference

| | Skill | Plugin |
| --- | --- | --- |
| Install | Copy a folder into `~/.claude/skills/` | `/plugin install` |
| Contains | `SKILL.md` + optional reference files | Skills, commands, hooks, agents, MCP servers, code |
| Updates | You re-copy | `/plugin` |
| Ships in this repo | Yes, all 51 | No — install from upstream |

A plugin can contain skills. The six `claude-skills` plugins above are mostly
skill wrappers; `claude-hud` is real code with a statusline command.

---

## Where they land

```
~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/
~/.claude/plugins/installed_plugins.json
~/.claude/plugins/known_marketplaces.json
```

To check what you have installed:

```bash
cat ~/.claude/plugins/installed_plugins.json
```

---

## Why these eight

They are the QA half of [`MASTER-PROMPT.md`](../MASTER-PROMPT.md). The prompt
refuses to call anything done without a security pass, browser QA and a
*measured* performance audit — and `cybersecurity`, `xss-prevention`,
`csrf-protection`, `playwright` and `web-performance-audit` are what actually
perform those phases. Without them, Phases 10–13 of the prompt have no tooling
behind them and Claude can only guess.

`agent-skills` covers the rest of the engineering: specs, plans, thin tested
slices, debugging, review and the launch checklist. The prompt's skills router
(§2) says which of its 25 skills applies at each phase.
