# How to use the master prompt

The rule is simple:

> **Write what you want. Paste the master prompt underneath it. Send.**

Your brief comes first so Claude knows *what* to build. The prompt comes second
and tells it *how* — which skills to load, which plugins to run, what counts as
finished.

---

## Copy-paste template

```
[Describe your project in your own words. Include anything real:
 the existing site URL, the business, who visits it, what you
 want them to do, brand colors, any assets you already have.]

---

[Paste the entire contents of MASTER-PROMPT.md here]
```

---

## Real examples

### New site, you have a brand

```
Build a landing page for Harbor Coffee, a small-batch roastery in Bristol.
Real site: harborcoffee.example. Logo and product photos are in assets/raw/.
The one thing visitors should do is book a tasting session.

---
[MASTER-PROMPT.md]
```

### Redesign

```
Redesign hyperdargo.example. Keep all the existing copy and services —
the content is accurate, the presentation is dated. Don't invent anything
new about the business.

---
[MASTER-PROMPT.md]
```

### You want it decided for you

```
Portfolio site for a freelance motion designer. Just build it — you decide
the direction, tell me your assumptions and show me the first pass.

---
[MASTER-PROMPT.md]
```

The prompt handles "just build it" specifically: no interview, two lines of
stated assumptions, then a real result you can react to.

### You're generating your own images

```
Marketing site for an indie audio plugin. I'm generating every asset myself.

---
[MASTER-PROMPT.md]
```

The prompt will stop after writing `ASSETS.md` and wait — it won't fill the gap
with stock photos or placeholder boxes. When your files are in `assets/raw/`,
say so and it validates them before building.

---

## Skip the pasting

Install the skill version once:

```bash
cp -r skills/master-website-engineering ~/.claude/skills/
```

Restart Claude Code, then just describe your website task normally. The skill
loads itself when the task matches — same standard, no paste, fewer tokens
burned. The full prompt sits in the skill's `reference/` folder and is only read
when the build actually needs it.

For a project you'll return to, paste the prompt into the repo's `CLAUDE.md`
instead so it applies to every session in that codebase.

---

## What you should expect to see

If the prompt is working, Claude will:

1. **Look before it types** — read your repo, fetch your existing site, list your assets.
2. **Show you a section map** before building, one mechanism per section, and wait.
3. **Build the signature moment first**, then check whether it actually deserves to be the signature.
4. **Screenshot the result** at several scroll depths and fix what it sees.
5. **Tell you what it did not verify**, instead of claiming a clean pass.

If it jumps straight to code, or hands you a page of fade-up cards with invented
testimonials, the prompt didn't load. Say *"use the
master-website-engineering skill"* explicitly.

---

## Giving feedback mid-build

Say what to change and what to keep:

```
Good first pass. The hero timing is too fast and the CTA needs more room.
Everything else stays.
```

The prompt binds Claude to exactly that — no silent redesign, no new sections,
no swapped visual system. If it had to fix one adjacent thing to make your
change work, it has to say so explicitly.
