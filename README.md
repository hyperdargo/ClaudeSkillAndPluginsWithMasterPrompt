<div align="center">

# Claude Skills, Plugins & the Master Prompt

**A complete working setup for [Claude Code](https://claude.com/claude-code):
50 skills, 7 plugins, and one master prompt that makes them work together.**

`50 skills` · `7 plugins` · `1 master prompt`

</div>

---

Most AI-built websites look AI-built. Same fade-up sections, same rounded cards,
same gradient hero, same invented testimonials. This bundle is the opposite
setup: skills that carry real design taste, plugins that actually run the
security and performance passes, and a master prompt that forces recon before
code and verification before "done".

**Contents**

1. [Install the skills](#1-install-the-skills)
2. [Install the plugins](#2-install-the-plugins)
3. [Use the master prompt](#3-use-the-master-prompt) ← the part that ties it together
   · [usage guide & templates](MASTER-PROMPT-USAGE.md)
4. [Skill catalog](#skill-catalog)
5. [Suggested stacks](#suggested-stacks)
6. [Credits](#credits--licensing)

```bash
git clone https://github.com/hyperdargo/ClaudeSkillAndPluginsWithMasterPrompt.git
cd ClaudeSkillAndPluginsWithMasterPrompt
```

---

## 1. Install the skills

A skill is a folder with a `SKILL.md` inside. Claude reads every skill's
description at startup and loads the body only when your task matches — so
installing all 50 costs you almost nothing until one is actually needed.

**Everything, user-wide** (available in every project):

<details open>
<summary><b>Windows (PowerShell)</b></summary>

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.claude\skills\"
```
</details>

<details>
<summary><b>macOS / Linux / Git Bash</b></summary>

```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```
</details>

**Just one skill** — copy that folder only:

```bash
cp -r skills/cinescroll ~/.claude/skills/
```

**Per-project instead** — use `.claude/skills/` inside the repo, and commit it
so your team gets the same setup.

Then **restart Claude Code** and ask *"which skills do you have?"* to confirm.

> Copying overwrites same-named skills. Back up first if you have customised any:
> `cp -r ~/.claude/skills ~/.claude/skills.backup`

Symlinking, subsets, verification and troubleshooting: **[INSTALL.md](INSTALL.md)**

---

## 2. Install the plugins

Plugins aren't copied into this repo — they carry their own code and update
cycle, so you install them from their marketplaces. Paste these into Claude Code:

```
/plugin marketplace add jarrodwatts/claude-hud
/plugin marketplace add https://github.com/secondsky/claude-skills.git

/plugin install claude-hud@claude-hud
/plugin install cybersecurity@claude-skills
/plugin install xss-prevention@claude-skills
/plugin install csrf-protection@claude-skills
/plugin install api-design-principles@claude-skills
/plugin install playwright@claude-skills
/plugin install web-performance-audit@claude-skills
```

| Plugin | What it does | Page |
| --- | --- | --- |
| `claude-hud` | Statusline HUD — model, context, cost, git state | [→](plugins/claude-hud.md) |
| `cybersecurity` | OWASP Top 10, pentest, threat modeling, SAST | [→](plugins/cybersecurity.md) |
| `xss-prevention` | Sanitization, output encoding, CSP | [→](plugins/xss-prevention.md) |
| `csrf-protection` | Synchronizer tokens, SameSite, double-submit | [→](plugins/csrf-protection.md) |
| `api-design-principles` | REST and GraphQL design standards | [→](plugins/api-design-principles.md) |
| `playwright` | Browser automation and E2E testing | [→](plugins/playwright.md) |
| `web-performance-audit` | Core Web Vitals and bottleneck analysis | [→](plugins/web-performance-audit.md) |

Each has its own install page in **[plugins/](plugins/README.md)** with version,
license and when it fires. Restart Claude Code after installing.

These five — `cybersecurity`, `xss-prevention`, `csrf-protection`, `playwright`,
`web-performance-audit` — are what actually *run* the security, QA and
performance phases the master prompt demands. Without them Claude can only guess.

---

## 3. Use the master prompt

**[`MASTER-PROMPT.md`](MASTER-PROMPT.md)** (v2) is a standard for building
websites that feel made, not generated. It has two parts:

- **Part A — a fill-in brief** anyone can complete in plain language, including an
  **art direction menu** (Exhibition, Editorial, Cinematic product,
  Industrial/brutalist, Soft structural, Playful/illustrated).
- **Part B — the standard:** recon, one signature moment, a **motion playbook**
  of proven scroll recipes (particle/halftone portrait assembly, pinned frame
  reveal, clip wipes, word lighting, horizontal galleries, stacking rooms,
  path-draw timelines), a **pitfalls table** taken from real bugs, security,
  a strict verification protocol and an honest report format.

### The pattern: fill in the brief, then paste the standard underneath

```
PROJECT:    Portfolio for me, a cybersecurity student who builds games and tools
ONE ACTION: People message me on LinkedIn: https://linkedin.com/in/your-name
DIRECTION:  Exhibition
just build it

---

[paste Part B of MASTER-PROMPT.md here]
```

Three lines are enough to start. The more of the brief you fill in, the better
the result.

Claude then reads your brief through the standard: it inspects your real site
first, pulls in `cinescroll` for the scroll work, picks *one* design skill,
builds the signature moment first, runs `playwright` and
`web-performance-audit` on it, and reports honestly what it verified.

### Three ways to load it

| Method | How | Best for |
| --- | --- | --- |
| **Paste after your brief** | Fill in Part A, paste Part B under it | Any one-off build — most direct control |
| **Install as a skill** | Copy `skills/master-website-engineering/` into `~/.claude/skills/` | Everyday use — loads itself when you describe a website task, no pasting |
| **Project-wide** | Paste it into your repo's `CLAUDE.md` | A site you'll keep working on, or a team |

The skill version is a short router; the full prompt sits in its `reference/`
folder and loads only when the task genuinely calls for it. Same standard,
fewer tokens.

More templates, real examples and what a correct run looks like:
**[MASTER-PROMPT-USAGE.md](MASTER-PROMPT-USAGE.md)**

### What the prompt enforces

| Rule | Meaning |
| --- | --- |
| **Recon before code** | Inspect the repo, the live site and the assets before changing anything |
| **Never fabricate** | No invented testimonials, stats, clients, prices, awards or addresses — ask instead |
| **One signature moment** | One interaction people remember, not five competing for attention |
| **Scroll is a scrubber** | Every scroll-driven animation must be correct forward *and* backward |
| **Mechanism follows content** | Never fade-up every section — pick the motion from the playbook |
| **Learn from real bugs** | A pitfalls table: build-time data baked empty, misaligned canvases, hydration mismatches, dead contact buttons, exposed `.env` |
| **Verify, then report** | Screenshots at 3 sizes, backwards scrub, reduced motion, E2E, measured performance. "Not verified" beats a false pass |

Its workflow, in short:

```
RECON → BRIEF/INTERVIEW → SECTION MAP → [your approval]
      → ASSETS → DESIGN SYSTEM → BUILD (signature first, then look at it)
      → QA → VISUAL QA → SECURITY → PERF → A11Y/SEO → FIX & RETEST
      → HONEST REPORT → [asks before pushing]
```

Say **"just build it"** and it skips the interview — states its assumptions in
two lines and ships a real first result instead of a questionnaire.

---

## Skill catalog

All 50 live in [`skills/`](skills/). Install all, or cherry-pick.

| Skill | What it does |
| --- | --- |
| `animate` | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, which properties, which curve and duration, how it interrupts, how... |
| `animate-expo` | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it runs on, which properties, spring or timing, how the gesture hands off,... |
| `animation-vocabulary` | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the iOS rubber-band scroll" → Rubber-banding). Use when the... |
| `apple-design` | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, drag/swipe/sheet interactions, momentum and interruptible... |
| `ask-sonner` | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and persisting toasts, styling, theming and icons, positioning and... |
| `brandkit` | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic, editorial, dark-tech, luxury, cultural,... |
| `cavecrew` | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline or using `Explore`. Their output is compressed, so main context lasts... |
| `caveman` | Ultra-compressed communication mode that cuts output tokens while keeping technical accuracy. Levels: lite, full, ultra and the wenyan variants. Use for /caveman, "caveman mode", "talk like caveman", "be brief" or "less tokens". |
| `caveman-compress` | Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup. Trigger: /caveman-compress. |
| `caveman-stats` | Show real token usage and estimated savings for the current session. Reads directly from the Claude Code session log — no AI estimation. Triggers on /caveman-stats. Output is injected by the mode-tracker hook; the model itself... |
| `cinescroll` | Build premium scroll-driven landing pages where scroll position controls what happens on screen — frame-scrubbed hero sequences, pinned narrative beats, data that counts up as you read it. Use this skill whenever the user... |
| `design-taste-frontend` | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable,... |
| `design-taste-frontend-v1` | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is a substantial rewrite. Use this v1 install name only if you need... |
| `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. |
| `find-animation-opportunities` | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does not implement it. Use when the user asks "what could be animated... |
| `full-output-enforcement` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output. |
| `gpt-taste` | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP... |
| `high-end-visual-design` | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or... |
| `image-to-code` | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. In Codex,... |
| `imagegen-frontend-mobile` | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hierarchy, comfortably readable text, strong... |
| `imagegen-frontend-web` | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces... |
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend interface. Covers websites, landing pages,... |
| `improve-animations` | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other agents (or cheaper models) to execute. Read-only on source code — it... |
| `industrial-brutalist-ui` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or... |
| `master-website-engineering` | Run a full professional website/app build as one team - recon, interview, section map, asset strategy, cinematic scroll design, engineering, security, testing, performance, accessibility, SEO, visual verification and a final... |
| `minimalist-ui` | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. |
| `pick-ui-library` | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, toasts, state, styling, and more. Only runs when explicitly... |
| `ponytail` | Forces the laziest solution that actually works, simplest, shortest, most minimal. Channels a senior dev who has seen everything: question whether the task needs to exist at all (YAGNI), reach for the standard library before... |
| `ponytail-audit` | Whole-repo audit for over-engineering. Like ponytail-review, but scans the entire codebase instead of a diff: a ranked list of what to delete, simplify, or replace with stdlib/native equivalents. Use when the user says "audit... |
| `ponytail-debt` | Harvest every `ponytail:` comment in the codebase into a debt ledger, so the deliberate shortcuts and deferrals ponytail leaves behind get tracked instead of rotting into "later means never". Use when the user says "ponytail... |
| `ponytail-gain` | Show ponytail's measured impact as a compact scoreboard: less code, less cost, more speed, from the benchmark medians. One-shot display, not a persistent mode, and not a per-repo number. Trigger: /ponytail-gain, "ponytail... |
| `ponytail-help` | Quick-reference card for all ponytail modes, skills, and commands. One-shot display, not a persistent mode. Trigger: /ponytail-help, "ponytail help", "what ponytail commands", "how do I use ponytail". |
| `ponytail-review` | Code review focused exclusively on over-engineering. Finds what to delete: reinvented standard library, unneeded dependencies, speculative abstractions, dead flexibility. One line per finding: location, what to cut, what... |
| `prototype` | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one that feels right. Only runs when explicitly invoked; it does not... |
| `redesign-existing-projects` | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS. |
| `remotion-best-practices` | Router for all Remotion skills |
| `remotion-captions` | Transcribing, displaying and animating captions |
| `remotion-create` | Create a new Remotion video |
| `remotion-docs` | Search Remotion documentation |
| `remotion-interactivity` | Structure Remotion markup for interactivity |
| `remotion-maps` | Remotion Map animation knowledge |
| `remotion-markup` | Content, animation and effects best practices |
| `remotion-multimedia` | Interacting with Mediabunny |
| `remotion-render` | Export a Remotion video |
| `remotion-saas` | Build an app with Remotion |
| `remotion-studio` | Preview a Remotion video |
| `remotion-upgrade` | Upgrade Remotion, and related packages |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. |
| `stitch-design-taste` | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and... |
| `write-swift` | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors, task groups), protocols and generics (some vs any), API design,... |

---

## Suggested stacks

Don't load every design skill at once — five overlapping ones makes Claude's
routing worse, not better. Pick the smallest combination.

**Cinematic landing page**
`master-website-engineering` + `cinescroll` + **one** design skill + `animate`
→ then `playwright` and `web-performance-audit` for the QA pass.

**Redesigning an existing site**
`master-website-engineering` + `redesign-existing-projects` + `impeccable`
→ audit first, preserve what works, don't invent a new business.

**Shipping safely**
`cybersecurity` + `xss-prevention` + `csrf-protection` + `web-performance-audit`.

**Cutting bloat**
`ponytail` while writing, `ponytail-review` on the diff, `ponytail-audit` on the repo.

**Design reference images before coding**
`imagegen-frontend-web` or `imagegen-frontend-mobile`, then `image-to-code`.

**Video**
The `remotion-*` family — start with `remotion-best-practices`, which routes to the rest.

**Fewer output tokens**
`caveman` (`/caveman`), `caveman-compress` for memory files, `caveman-stats` for real numbers.

---

## Repo layout

```
.
├── MASTER-PROMPT.md          v2: brief form + standard + motion playbook + pitfalls
├── MASTER-PROMPT-USAGE.md    how to apply it, with templates
├── archive/
│   └── MASTER-PROMPT-v1.md   the original 60-section prompt
├── INSTALL.md                detailed skill install + troubleshooting
├── CREDITS.md                authorship and licensing
├── skills/                   50 skills, install by copying folders
│   └── master-website-engineering/
│       ├── SKILL.md          short router version of the master prompt
│       └── reference/
│           └── master-prompt.md
└── plugins/                  install pages, one per plugin
    ├── README.md
    └── <plugin>.md × 7
```

---

## Credits & licensing

**These skills were written by many different authors.** This repo is a
convenience bundle of one working setup — it is not original work, and no
blanket license is claimed over it. Where a skill declares its own license or
author, that governs. See **[CREDITS.md](CREDITS.md)** for what is known about
each source.

If you authored something here and want it removed or re-attributed, open an
issue and it will be handled promptly.

`MASTER-PROMPT.md` and `skills/master-website-engineering/` are the only
original contributions in this repo.
