# agent-skills

Addy Osmani's production engineering workflow, spec to ship: 25 skills, 9 slash
commands, 4 reviewer agents and a SessionStart hook.

- **Marketplace:** `addy-agent-skills`
- **Source:** https://github.com/addyosmani/agent-skills
- **Version in this bundle:** 0.6.9
- **License:** MIT

## Install

```
/plugin marketplace add https://github.com/addyosmani/agent-skills.git
/plugin install agent-skills@addy-agent-skills
```

> **`fatal: Could not read from remote repository`?** The plugin entry clones
> over SSH even when the marketplace was added over HTTPS. Without a GitHub SSH
> key, the install fails. Either add an SSH key to GitHub, or tell git to use
> HTTPS for GitHub and run the install again:
>
> ```bash
> git config --global url."https://github.com/".insteadOf git@github.com:
> ```
>
> Without the plugin system: `npx skills add addyosmani/agent-skills` installs
> the 25 skills only (no commands, agents or hook).

## What you get

| Kind | Items |
| --- | --- |
| Define & plan | `idea-refine`, `interview-me`, `spec-driven-development`, `planning-and-task-breakdown`, `constraint-driven-development` |
| Build | `incremental-implementation`, `test-driven-development`, `frontend-ui-engineering`, `api-and-interface-design`, `source-driven-development`, `context-engineering` |
| Verify | `debugging-and-error-recovery`, `browser-testing-with-devtools`, `doubt-driven-development` |
| Review | `code-review-and-quality`, `code-simplification`, `security-and-hardening`, `performance-optimization` |
| Ship | `git-workflow-and-versioning`, `ci-cd-and-automation`, `shipping-and-launch`, `observability-and-instrumentation`, `deprecation-and-migration`, `documentation-and-adrs` |
| Meta | `using-agent-skills` (chooses the workflow for the task) |
| Commands | `/spec`, `/plan`, `/build`, `/test`, `/review`, `/code-simplify`, `/constraints`, `/ship`, `/webperf` |
| Agents | `code-reviewer`, `security-auditor`, `test-engineer`, `web-performance-auditor` |

## When it fires

Engineering around the design work: specs and plans before a big build,
changes in thin tested slices, root-cause debugging, multi-axis review, then a
launch checklist with git hygiene, CI and monitoring.

## Notes

`browser-testing-with-devtools` needs the `chrome-devtools` MCP server. The
master prompt uses `playwright` for repeatable screenshots and E2E, and
DevTools for live console, network and performance debugging.
