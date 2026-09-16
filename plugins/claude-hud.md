# claude-hud

Real-time statusline HUD for Claude Code — model, context usage, session cost,
git branch and more, rendered into your statusline.

- **Marketplace:** `claude-hud`
- **Source:** https://github.com/jarrodwatts/claude-hud
- **Version in this bundle:** 0.8.0
- **License:** MIT © Jarrod Watts

## Install

```
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud@claude-hud
```

## Set it up

```
/claude-hud:setup
```

Writes the statusline entry into your `settings.json`. Then:

```
/claude-hud:configure
```

for layout, language, presets and which elements are shown. It preserves manual
overrides you have already made.

## Notes

Ships compiled JS (`dist/`) and runs as a statusline command, so it needs Node
available on your `PATH`. It is the one plugin here that changes Claude Code's
chrome rather than its behaviour — safe to skip if you like your statusline bare.
