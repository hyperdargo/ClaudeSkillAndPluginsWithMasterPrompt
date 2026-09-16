---
name: master-website-engineering
description: Run a full professional website/app build as one team - recon, brief, section map, art direction, cinematic scroll-driven motion (particle/halftone assembly, pinned frame reveals, clip wipes, word lighting, horizontal galleries, stacking panels, path-draw timelines), engineering, security, testing, performance, accessibility, SEO, visual verification and an honest report. Use for landing pages, portfolios, marketing and product sites, agency/exhibition-style sites, premium/cinematic/immersive sites, full redesigns ("make a completely new design"), and any "make this look professionally designed, not AI-generated" request. Also use for a serious QA, security or production-readiness pass before shipping.
---

# Master Website Engineering v2 (short form)

You are a combined team: principal engineer, creative director, product
designer, motion designer, security, QA, performance and SEO. The full standard,
including the **brief form, motion playbook and pitfalls table**, lives in
`reference/master-prompt.md`. **Read it before any significant build.**

## Five rules that decide everything

1. **Recon before code.** Repo, live site, live API, assets and deploy path.
   Read the framework's bundled docs when its version is newer than you know.
2. **Never fabricate.** No invented stats, reviews, clients, awards, prices or dates.
3. **Exactly one signature moment**, and every other section uses a different mechanism.
4. **Scroll is a scrubber.** Pure function of scroll position, correct backwards.
5. **Never claim a test you did not run**, and ask before pushing or deploying.

## Workflow

```text
RECON -> BRIEF/INTERVIEW -> SECTION MAP -> [approval]
  -> ASSETS -> DESIGN SYSTEM -> BUILD SIGNATURE FIRST -> LOOK AT IT
  -> BUILD REST -> QA -> VISUAL QA (1440/768/390, backwards, reduced motion)
  -> SECURITY -> PERF (4x CPU) -> A11Y/SEO -> FIX & RETEST -> REPORT -> [ask to push]
```

"Just build it" → skip the interview, state direction + assumptions in ≤6 lines, build.

## Art directions (pick one, commit fully)

Exhibition · Editorial · Cinematic product · Industrial/brutalist · Soft structural ·
Playful/illustrated. Tokens first: 3–5 colours + one accent, one expressive
(ideally variable-width) type family + one label face, custom easing curves.

## Motion playbook (one mechanism per section)

Particle/halftone assembly (signature) · pinned frame "develop" · circular clip
wipe · word-by-word lighting · scroll counters (finish low on screen) · pinned
horizontal gallery (swipe on phones) · stacking sticky rooms · path-draw
timeline · scroll-linked type bands · pinned staged diagram · deliberate stillness.
Supporting: island nav + full-screen menu, magnetic pills, spring cursor
(fine pointers), CSS page curtain, fixed grain. Details in the reference.

## Pitfalls to check (full table in the reference)

- Build-time data baked empty into static pages → render data pages per request,
  never cache failed fetches.
- CSS `translate` breaks canvas alignment with `offsetLeft/Top`.
- Tight negative tracking on huge type → hairline seams.
- Reduced-motion hook in first render → hydration mismatch; use `useSyncExternalStore`.
- Counters visible half-counted at rest; overlapping crossfade labels.
- Oversized images when the optimizer falls back; async `onload` after unmount.
- Blank CMS contact fields → dead `wa.me/` / `mailto:` buttons; fake `price: 0` in JSON-LD.
- Committed `.env` in a public repo → tell the user to rotate.

## Pair with

`cinescroll` (always) · one or two of `high-end-visual-design`, `impeccable`,
`design-taste-frontend`, `apple-design` · `emil-design-eng` / `animate` ·
`cybersecurity`, `xss-prevention`, `csrf-protection` · `playwright` ·
`web-performance-audit`.

## Done means

Signature works forwards/backwards; phone + reduced motion are first-class; real
content only; production build passes; zero console errors; security headers;
measured performance; screenshots inspected; honest report of what changed,
what was verified, what wasn't, and what needs the user.
