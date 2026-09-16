# web-performance-audit

Web performance auditing against Core Web Vitals — LCP, INP, CLS, TTFB — with bottleneck identification and prioritised optimization recommendations.

- **Marketplace:** `claude-skills`
- **Source:** https://github.com/secondsky/claude-skills
- **Version in this bundle:** 3.9.0
- **License:** MIT

## Install

```
/plugin marketplace add https://github.com/secondsky/claude-skills.git
/plugin install web-performance-audit@claude-skills
```

The marketplace only needs adding once — after that, install the rest with a
single `/plugin install <name>@claude-skills` each.

## When it fires

Use for slow page loads, pre-launch performance reviews, render-blocking resources and animation jank.

## Notes

The master prompt says do not optimize blindly. This is how you measure first.
