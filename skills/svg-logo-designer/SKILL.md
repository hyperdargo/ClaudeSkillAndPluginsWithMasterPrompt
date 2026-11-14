---
name: svg-logo-designer
description: Create professional SVG logos from descriptions and design specifications. Generates multiple logo variations with different layouts, styles, and concepts. Produces scalable vector graphics that can be used directly or exported to PNG. Use this skill when users ask to create logos, brand identities, icons, or visual marks for their designs.
---

# SVG Logo Designer

This skill creates professional, scalable vector graphic (SVG) logos from design specifications, offering multiple variations and layout options.

## When to Use This Skill

Activate this skill when the user requests:
- Create a logo from a description or specification
- Design a brand identity or visual mark
- Generate logo variations and concepts
- Create icons or symbols
- Design wordmarks or lettermarks
- Produce scalable graphics for branding
- Export logos in different layouts and styles

## Core Workflow

### Phase 1: Requirements Gathering

When a user requests a logo, gather comprehensive design requirements:

1. **Brand Information**
   - Company/product name
   - Industry and market
   - Target audience
   - Brand personality (modern, classic, playful, serious, etc.)
   - Brand values and messaging
   - Competitors (for differentiation)

2. **Design Preferences**
   - Logo type:
     - **Wordmark**: Text-based logo (Google, Coca-Cola style)
     - **Lettermark**: Initials/abbreviation (IBM, HBO style)
     - **Pictorial Mark**: Icon/symbol (Apple, Twitter style)
     - **Abstract Mark**: Abstract geometric form (Pepsi, Adidas style)
     - **Mascot**: Character-based (KFC Colonel, Michelin Man style)
     - **Combination Mark**: Icon + text (Burger King, Lacoste style)
     - **Emblem**: Text inside symbol (Starbucks, Harley-Davidson style)

3. **Style Guidelines**
   - Color palette (specific colors or let AI choose)
   - Color psychology considerations
   - Font preferences (if text-based)
   - Visual style: Minimalist, Geometric, Organic/flowing, Bold/strong, Elegant/refined, Playful/friendly, Tech/modern, Vintage/retro

4. **Technical Requirements**
   - Size constraints (will it be used small? large?)
   - Application contexts (website, print, merchandise, etc.)
   - Color vs monochrome versions needed
   - Background usage (light, dark, transparent)
   - Scalability requirements

5. **Number of Variations**
   - Concepts: recommend 3-5
   - Layouts: Horizontal, vertical, square, icon-only, text-only
   - Color variations: Full color, monochrome-dark, monochrome-light

### Phase 2: Design Concept Development

Develop 3-5 distinct concepts:
- **Concept 1**: Primary Direction (central metaphor, balanced simplicity and uniqueness)
- **Concepts 2-5**: Alternative Directions (varied metaphors, geometric forms, stylings)

### Phase 3: Layout Variations
For each concept:
- **Horizontal Lockup**: Icon left, text right (headers, cards)
- **Vertical Lockup**: Icon top, text below (social profiles, mobile)
- **Square / Centered**: Centered 1:1 (favicons, app icons)
- **Icon Only**: Symbol without text
- **Text Only**: Wordmark without icon

### Phase 4: SVG Generation Best Practices
- Clean semantic code with `<defs>`, `<style>`, `<g id="...">`
- Always use `viewBox` (e.g. `viewBox="0 0 200 60"` or `0 0 100 100"`)
- Relative units or scalable vector coordinates, no hardcoded fixed-pixel dependencies
- Optimize paths and polygons; combine where appropriate
- Accessibility: `<title>` and `<desc>` with `role="img"`

### Phase 5: Presentation & Deliverables
- Present each concept with design rationale
- Provide full SVG markup
- Deliver SVG files to workspace when requested
- Provide clear space, minimum size, color codes (hex, RGB), and usage guidelines
