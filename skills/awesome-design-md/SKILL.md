---
name: awesome-design-md
description: Curated collection of 84+ production DESIGN.md design systems extracted from real developer tools, SaaS, AI platforms, fintech, and consumer websites (Vercel, Linear, Stripe, Supabase, Cursor, Apple, Airbnb, Shopify, Raycast, etc.). Use when asked to build UI following a specific brand's aesthetic, apply a DESIGN.md file, or inspect design tokens, palettes, typography, and component styling.
---

# Awesome DESIGN.md

A curated collection of 84+ production `DESIGN.md` design system documents extracted from top websites and brands.

## When to Use

Activate this skill when:
- The user asks to design or build UI that looks like a specific brand (e.g. "make it look like Linear", "use Vercel's style", "design like Stripe or Supabase").
- The user requests a `DESIGN.md` for their project or wants design tokens, color palettes, spacing scales, or component styles from a real brand.
- The user mentions `awesome-design-md` or asks for design guidance from known industry leaders.

## Location of Design Systems

All design systems are installed locally at:
`C:\Users\light\.config\opencode\external\awesome-design-md\design-md\<brand>\`

Each brand directory contains:
- `DESIGN.md`: The complete design specification (colors, typography, components, elevation, responsive behavior, do's & don'ts, agent prompt guide).
- `preview.html`: Visual catalog showing color swatches, type scale, buttons, cards.
- `preview-dark.html`: Dark surface variant catalog.

## Available Brands (84 Total)

### AI & LLM Platforms
- `claude` (Anthropic Claude - Warm terracotta, clean editorial layout)
- `cohere` (Enterprise AI platform - Vibrant gradients, data-rich)
- `elevenlabs` (AI voice platform - Dark cinematic UI, audio-waveform aesthetics)
- `jobright` (AI job hunting - Spring-mint green, black pill buttons)
- `minimax` (AI model provider - Bold dark interface with neon accents)
- `mistral.ai` (Open-weight LLM provider - French-engineered minimalism, purple)
- `ollama` (Local LLMs - Terminal-first, monochrome simplicity)
- `opencode.ai` (AI coding platform - Developer-centric dark theme)
- `replicate` (Run ML models - Clean white canvas, code-forward)
- `runwayml` (AI creative tools - Editorial film-festival aesthetic)
- `together.ai` (Open-source AI infrastructure - Technical blueprint style)
- `voltagent` (AI agent framework - Void-black canvas, emerald accent)
- `x.ai` (Stark monochrome, futuristic minimalism)

### Developer Tools & IDEs
- `cursor` (AI-first code editor - Sleek dark interface, gradient accents)
- `expo` (React Native platform - Dark theme, tight letter-spacing)
- `lovable` (AI full-stack builder - Playful gradients, friendly dev aesthetic)
- `raycast` (Productivity launcher - Sleek dark chrome, vibrant gradient accents)
- `superhuman` (Fast email client - Premium dark UI, keyboard-first, purple glow)
- `vercel` (Frontend deployment platform - Black and white precision, Geist font)
- `warp` (Modern terminal - Dark IDE-like interface, block-based UI)

### Backend, Database & DevOps
- `clickhouse` (Fast analytics - Yellow-accented, technical documentation style)
- `composio` (Tool integration - Modern dark with colorful icons)
- `hashicorp` (Infrastructure automation - Enterprise-clean, black & white)
- `mongodb` (Document database - Green leaf branding, dev focus)
- `oracle` (Enterprise cloud - Warm neutral ladder, charcoal actions)
- `posthog` (Product analytics - Playful hedgehog branding, dev-friendly dark UI)
- `sanity` (Headless content platform - Dark-first editorial, coral-red accent)
- `sentry` (Error monitoring - Dark dashboard, data-dense, pink-purple accent)
- `supabase` (Open-source Firebase alternative - Dark emerald theme, code-first)

### Productivity & SaaS
- `cal` (Cal.com - Clean neutral UI, developer-oriented simplicity)
- `intercom` (Customer messaging - Friendly blue palette, conversational UI)
- `linear.app` (Project management - Ultra-minimal, precise, purple accent)
- `mintlify` (Documentation platform - Clean, green-accented, reading-optimized)
- `notion` (All-in-one workspace - Warm minimalism, serif headings, soft surfaces)
- `resend` (Email API - Minimal dark theme, monospace accents)
- `sap` (Enterprise software - White canvas, flat blue bands)
- `slack` (Team communication - Playful multi-color, clean channels)
- `zapier` (Automation platform - Warm orange, illustration-driven)

### Design & Creative Tools
- `airtable` (Spreadsheet-database - Colorful, friendly, structured data)
- `clay` (Creative agency - Organic shapes, soft gradients, art-directed)
- `figma` (Design tool - Vibrant multi-color, playful yet professional)
- `framer` (Website builder - Bold black and blue, motion-first)
- `miro` (Visual collaboration - Bright yellow accent, infinite canvas)
- `webflow` (Visual web builder - Blue-accented, polished marketing site)

### Fintech & Crypto
- `binance` (Crypto exchange - Binance Yellow on monochrome)
- `coinbase` (Crypto exchange - Clean blue identity, trust-focused)
- `kraken` (Crypto trading - Purple-accented dark UI, data-dense)
- `mastercard` (Global payments - Warm cream canvas, orbital pill shapes)
- `mercury` (Startup banking - Ink-violet night world, indigo action pill)
- `nerdwallet` (Personal finance - Deep spruce green, mint washes)
- `revolut` (Digital banking - Sleek dark interface, gradient cards)
- `stripe` (Payment infrastructure - Signature purple gradients, weight-300 elegance)
- `wise` (Money transfer - Bright green accent, friendly and clear)

### E-commerce & Retail
- `airbnb` (Travel marketplace - Warm coral accent, photography-driven)
- `meta` (Tech retail - Photography-first, binary light/dark surfaces)
- `mydealz` (Deals community - Dense white-card feed, hot/cold voting pill)
- `nike` (Athletic retail - Monochrome UI, massive uppercase Futura)
- `shopify` (E-commerce - Dark-first cinematic, neon green accent)
- `starbucks` (Coffee retail - Four-tier earth-green, warm cream canvas)

### Media & Consumer Tech
- `1win`, `aljazeera`, `apple`, `dji`, `hp`, `ibm`, `nvidia`, `oura`, `pinterest`, `playstation`, `spacex`, `spotify`, `theverge`, `uber`, `vodafone`, `wired`

### Automotive & Retro Web
- `bmw`, `bmw-m`, `bugatti`, `ferrari`, `lamborghini`, `renault`, `tesla`
- `dell-1996`, `nintendo-2001`

## Workflow: How to Apply a Brand's Design

1. **Read the Brand's Specification**:
   Read `C:\Users\light\.config\opencode\external\awesome-design-md\design-md\<brand>\DESIGN.md`.
2. **Copy to Project (if requested)**:
   Copy or write the `DESIGN.md` into the user's project root as `./DESIGN.md`.
3. **Extract and Apply Guidelines**:
   Extract exact hex colors, font pairings, border radii, shadow tokens, and spacing scale to configure CSS / Tailwind / UI components accordingly.
