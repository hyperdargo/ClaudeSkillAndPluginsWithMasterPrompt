# xss-prevention

Cross-site scripting prevention: input sanitization, output encoding and Content Security Policy.

- **Marketplace:** `claude-skills`
- **Source:** https://github.com/secondsky/claude-skills
- **Version in this bundle:** 3.9.0
- **License:** MIT

## Install

```
/plugin marketplace add https://github.com/secondsky/claude-skills.git
/plugin install xss-prevention@claude-skills
```

The marketplace only needs adding once — after that, install the rest with a
single `/plugin install <name>@claude-skills` each.

## When it fires

Reach for it around user-generated content, rich text editors, anything rendering HTML you did not author, and when chasing stored XSS, reflected XSS, DOM-based injection or script-injection bugs.

## Notes

Pairs with csrf-protection for a full form-security pass.
