# playwright

Browser automation and end-to-end testing. Auto-detects dev servers and writes clean test scripts — page tests, form fills, screenshots, responsive checks, login flows, link checking.

- **Marketplace:** `claude-skills`
- **Source:** https://github.com/secondsky/claude-skills
- **Version in this bundle:** 3.9.0
- **License:** MIT

## Install

```
/plugin marketplace add https://github.com/secondsky/claude-skills.git
/plugin install playwright@claude-skills
```

The marketplace only needs adding once — after that, install the rest with a
single `/plugin install <name>@claude-skills` each.

## When it fires

This is the browser QA phase. Cross-browser runs, visual regression, API tests and component tests in TypeScript/JavaScript and Python projects.

## Notes

The master prompt's visual verification phase depends on this: screenshots at 0/10/25/50/75/90/100 percent scroll depth, then fix what you see.
