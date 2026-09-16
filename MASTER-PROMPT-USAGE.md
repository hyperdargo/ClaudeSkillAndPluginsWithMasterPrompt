# How to use the master prompt (v2)

> **Fill in the brief. Paste the standard under it. Send.**

[`MASTER-PROMPT.md`](MASTER-PROMPT.md) has two parts:

- **Part A — Your brief.** A short fill-in form: who the site is for, the one
  action, the feeling, your real assets, and an art direction picked from a menu.
- **Part B — The standard.** How Claude must work: recon, one signature moment,
  a motion playbook with proven recipes, a pitfalls table, verification and an
  honest report.

You don't need to know any animation or engineering terms. The brief asks in
plain language; the standard turns it into the technical work.

---

## The 60-second version

```text
PROJECT:    Portfolio for me, a cybersecurity student who builds games and tools
ONE ACTION: People message me on LinkedIn: https://linkedin.com/in/your-name
DIRECTION:  Exhibition
just build it

---

[paste Part B of MASTER-PROMPT.md here]
```

That's enough. Claude picks the signature moment, states its assumptions in a
few lines, builds, screenshots its own work, fixes what it sees and tells you
what it couldn't verify.

---

## The full version (better results)

Copy Part A, fill in every line you know, delete the rest:

```text
PROJECT:        Redesign of https://example-shop.com
WHO IT IS FOR:  Harbor Coffee, small-batch roastery in Bristol
VISITORS:       Local coffee drinkers and cafés looking for a supplier
ONE ACTION:     Book a tasting: https://example-shop.com/book
ONE FEELING:    "These people are obsessive about coffee, in a good way"
REAL ASSETS:    Logo + 12 product photos in assets/raw/, roasting video (40 s)
NUMBERS:        none
DIRECTION:      Editorial
SIGNATURE IDEA: you decide
MUST KEEP:      Shopify checkout, blog
MUST NOT:       No stock photos, no invented awards
DEPLOY:         Vercel
PUSH/PUBLISH:   Ask me first

---

[paste Part B of MASTER-PROMPT.md here]
```

---

## Picking a direction

| If you want people to think… | Pick |
| --- | --- |
| "This is art. I want to walk through it." | **Exhibition** |
| "This is thoughtful and well written." | **Editorial** |
| "This product is precise and premium." | **Cinematic product** |
| "This is technical, raw and honest." | **Industrial / brutalist** |
| "This is calm, modern and friendly." | **Soft structural** |
| "This is fun and made by a human." | **Playful / illustrated** |

Not sure? Write `DIRECTION: you decide` and Claude will propose one grounded in
your content.

---

## What a correct run looks like

1. **It looks before it types.** Reads your repo and live site, checks your assets,
   flags security problems (like a committed `.env`) and broken buttons.
2. **It asks once, or not at all.** One message of questions with recommended
   answers, or none if you said "just build it".
3. **It builds the signature moment first** and looks at it in a real browser
   before building anything else.
4. **Every section moves differently**, or deliberately doesn't move.
5. **It screenshots desktop, tablet and phone** at many scroll depths, scrolls
   backwards, tests reduced motion, and fixes what it finds.
6. **It measures performance** and reports numbers, not adjectives.
7. **It tells you what it didn't verify** and asks before pushing or deploying.

If it jumps straight to code, or gives you fade-up cards with invented reviews,
the standard didn't load. Say *"follow MASTER-PROMPT.md strictly"* or *"use the
master-website-engineering skill"*.

---

## Giving feedback

**Small change:** say what to change and what to keep.

```text
Good first pass. The hero moves too fast and the button needs more space.
Everything else stays.
```

**Completely new look:** say so directly. Claude should start a new direction,
not patch the old one.

```text
I don't like this style. Make a completely new design, more like an art gallery.
Keep the content and the admin.
```

Feel-words map to real fixes:

| You say | What gets checked |
| --- | --- |
| "It feels bland" | Is the section actually bound to scroll, or just fading in? |
| "It scrolls too fast" | The section gets taller (more scroll distance), not slower easing |
| "It's too much" | More than one signature moment is competing, so one gets calmer |
| "It looks generic" | Repeated cards, repeated reveals, default fonts, meaningless gradients |

---

## Skip the pasting

Install the skill version once:

```bash
cp -r skills/master-website-engineering ~/.claude/skills/
```

Restart Claude Code, then describe your website normally, ideally with the
Part A brief. The skill loads itself when the task matches, and reads the full
standard from its `reference/` folder only when the build needs it.

For a site you'll keep working on, paste Part B into the repo's `CLAUDE.md` so it
applies to every session.

---

## Previous version

The original 60-section prompt is kept at
[`archive/MASTER-PROMPT-v1.md`](archive/MASTER-PROMPT-v1.md).
