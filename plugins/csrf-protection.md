# csrf-protection

Cross-site request forgery protection: synchronizer tokens, double-submit cookies and SameSite cookie attributes.

- **Marketplace:** `claude-skills`
- **Source:** https://github.com/secondsky/claude-skills
- **Version in this bundle:** 3.9.0
- **License:** MIT

## Install

```
/plugin marketplace add https://github.com/secondsky/claude-skills.git
/plugin install csrf-protection@claude-skills
```

The marketplace only needs adding once — after that, install the rest with a
single `/plugin install <name>@claude-skills` each.

## When it fires

Use when securing web forms, protecting any state-changing endpoint, or layering defence-in-depth onto an existing auth system.

## Notes

Covers the 'never trust client-side validation alone' rule from the master prompt.
