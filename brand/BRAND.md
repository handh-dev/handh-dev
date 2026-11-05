# handh.dev brand mood board and design spec

> **For agents:** read this whole file before you design, write or build anything for handh.dev.
> It is the source of truth. `tokens.json` / `tokens.css` hold the exact values, `moodboard.html` shows them,
> and `assets/` holds the only approved logo files. If something here conflicts with your defaults, this file wins.

---

## 0. The ten rules (if you only read one section)

1. The name is **`handh.dev`** or **`handh-dev`**. Nothing else, ever. Always lowercase.
2. **Never use the ampersand character** anywhere in brand copy, headlines, nav, alt text, metadata or file names. Write "and".
3. Two brand colors only: **ink `#1d252f`** and **blue `#0073fe`**, on white or near-black neutrals.
4. Color budget by area: about **75% neutral, 15% ink, 10% blue**. Blue is a signal, not a wallpaper.
5. Brand blue `#0073fe` is **not** for small text. Small blue text and button fills use **`#005fd6`**.
6. Logos come from `assets/` only. Never redraw, retype, recolor (beyond the provided variants), stretch or add effects.
7. Shape language: **outer corners round, inner edges square**, one **64° diagonal cut**, one thin **seam** gap. Nothing else decorative.
8. Type: **Lexend** for headlines, **Inter** for text, **JetBrains Mono** for code and labels.
9. Flat surfaces. No gradients, no glows, no glassmorphism, no stock-photo handshakes, no emoji in UI.
10. Run `python3 brand/check-brand-name.py <your output>` before you hand anything back. It must say PASS.

---

## 1. Name

| Use | Form | Where |
|---|---|---|
| Display name | `handh.dev` | Headlines, body copy, page titles, alt text, social bios, email signatures, legal footers |
| Slug | `handh-dev` | Repo names, package names, file names, CSS/JS identifiers, URL paths, social handles that disallow dots |

Rules:

- **Always lowercase**, including at the start of a sentence. If a sentence would start with the name, rephrase it or start it anyway in lowercase: "handh.dev builds…" is correct.
- The `.dev` is part of the name. Do not drop it in copy. A bare "handh" is not a name. <!-- brand-lint: ignore -->
- Never abbreviate, never use initials, never add "Inc", "Studio" or "Team" as part of the name.
- In the logo the `.dev` is blue and `handh` is ink. In running text the name is the same color as the text around it. Do not color it inline. <!-- brand-lint: ignore -->
- In code, prefer `handh-dev` (kebab). Where kebab is impossible, use a neutral identifier such as `brand` rather than inventing a new spelling.

<!-- brand-lint: ignore-start -->
**Never write any of these** (non-exhaustive):

| Wrong | Why |
|---|---|
| H&H, H & H, h&h, H&amp;H | Ampersand. Banned outright. |
| H and H, H+H, HnH, H'n'H | Not the name. |
| HandH, Handh, HANDH, Handh.dev, HANDH.DEV, Handh-Dev | Wrong case. |
| handh, handh dev, handhdev, handh_dev, handh.io | Incomplete or invented form. |
| HH, H.H., "the H's" | Initials or nicknames. |
<!-- brand-lint: ignore-end -->

The ampersand ban goes beyond the name: **no ampersand character in any visible brand text.** "Design and build", not the symbol. Code syntax (for example `&&` in a code sample) is the only exception.

---

## 2. Brand essence

**What the mark says:** two halves that meet. A solid ink stem on the left (steady, structural) and a blue form on the right that flows out of the crossbar and is cut on a sharp diagonal (motion, craft, the build). A thin seam separates them. Two parts, one letter.

**Mood words:** precise, engineered, calm, confident, direct, crafted, modern, trustworthy.
**Not:** playful, cute, loud, corporate-stiff, trendy-neon, hacker-cliché, luxury.

**Personality sliders** (1 = left word, 5 = right word):

| | 1 | 2 | 3 | 4 | 5 | |
|---|---|---|---|---|---|---|
| Serious | | ● | | | | Playful |
| Minimal | ● | | | | | Ornate |
| Technical | | ● | | | | Friendly |
| Quiet | | ● | | | | Loud |
| Classic | | | | ● | | Futuristic |
| Exclusive | | | | ● | | Approachable |

**Visual references (the feeling, not things to copy):** engineering drawings, precision-machined parts, well-set technical documentation, a clean terminal, architectural plans with one blue highlight, Swiss grid layouts.

> Positioning, audience and services are **not** defined here yet. Do not invent client names, stats, testimonials, prices or claims. Use clearly marked placeholders (for example `[client name]`) when copy needs facts.

---

## 3. Logo

Files in `brand/assets/` (SVG preferred, PNG fallback):

| File | Use on |
|---|---|
| `handh-dev-full.svg` / `.png` | Primary lockup (mark above wordmark). White or `ink-50` backgrounds. |
| `handh-dev-full-reversed.svg` | Ink or near-black backgrounds (ink parts turn white, blue stays). |
| `handh-dev-full-mono-ink.svg` | One-color print, embossing, fax-grade, single-color light contexts. |
| `handh-dev-full-mono-white.svg` | One-color on photos or on brand blue. |
| `handh-dev-brandmark.svg` / `.png` | Mark only: favicon, app icon, avatar, small spaces, watermark. |
| `handh-dev-brandmark-reversed.svg` | Mark on dark backgrounds. |
| `handh-dev-brandmark-mono-ink.svg` / `-mono-white.svg` | One-color mark. |
| `handh-dev-full-tight.svg`, `-full-reversed-tight.svg`, `-full-mono-ink-tight.svg`, `-full-mono-white-tight.svg` | Same lockups cropped to the artwork. Use in headers, footers, and anywhere you size the logo by height. |

Note: the untrimmed full-lockup files have generous built-in padding (artboard 1254×1254). Prefer the `-tight` files in layouts.

**Headers and navs:** the full lockup is stacked (mark above wordmark), so it is too small to read at header height. Use the **brandmark alone** at 24 to 40px in headers, navs, tabs and avatars. Use the full lockup where it can be 96px wide or more (hero, footer, cover, card). There is **no horizontal lockup** yet; do not build one by setting "handh.dev" in a font next to the mark.

**Clear space:** at least the width of the mark's ink stem on all sides (about 25% of the mark's width).
**Minimum size:** brandmark 16px (favicon) / 24px in UI; full lockup 96px wide on screen, 25mm in print.
**Backgrounds:** white, `ink-50`, `ink-950`, `ink-800`. On brand blue, use mono-white only.

**Never:** stretch or skew; rotate; recolor outside the provided variants; swap the two colors; add shadows, outlines, gradients, glows or 3D; place full-color logo on busy photos or mid-tone backgrounds; retype "handh.dev" in a font and call it the logo; separate the `.dev` from `handh`; animate the mark apart in a way that breaks the seam permanently; put the mark inside another shape (circle, shield, speech bubble). Exception: an app icon may sit the mark on an ink or white rounded square with the clear space above. <!-- brand-lint: ignore -->

---

## 4. Color

| Token | Hex | Role |
|---|---|---|
| `ink` (ink-800) | `#1d252f` | Logo charcoal. Primary text. Dark surfaces. |
| `blue` (blue-500) | `#0073fe` | Logo blue. The signal: logo, large display words, key graphic shape, focus rings, one highlight per view. |
| `blue-600` | `#005fd6` | **Action**: filled buttons, links, small blue text on light. |
| `blue-700` | `#004cad` | Hover / pressed. |
| `blue-400` | `#4a93ff` | Links and blue text on dark backgrounds. |
| `blue-50`/`100` | `#eef5ff` / `#d9e8ff` | Selected rows, info callouts, code highlights. |
| `white` | `#ffffff` | Default light background. |
| `ink-50` | `#f6f7f9` | Alternate light section. |
| `ink-100` | `#eceef2` | Subtle fill, code blocks on light. |
| `ink-200` | `#d8dce3` | Borders and dividers on light. |
| `ink-500` | `#5f6a7a` | Muted text on light. |
| `ink-700` | `#313a46` | Borders on dark. |
| `ink-900` | `#141a22` | Cards / panels on dark. |
| `ink-950` | `#0b0f14` | Dark page background. |
| status | `#0f8a5f` / `#b25e00` / `#d1293d` | Success / warning / danger. Functional UI only. |

Full 50 to 950 scales are in `tokens.json`.

**Contrast facts (WCAG):**

| Pair | Ratio | Verdict |
|---|---|---|
| ink on white | 15.46 | Body text ✔ |
| ink-500 on white | 5.48 | Muted text ✔ |
| blue-500 on white | 4.30 | **Large text (24px+, or 19px+ bold) and graphics only** |
| blue-600 on white | 5.82 | Links, small blue text ✔ |
| white on blue-600 | 5.82 | Button labels ✔ |
| white on blue-500 | 4.30 | Only for labels 19px+ bold |
| ink-50 on ink-950 | 17.93 | Dark-mode text ✔ |
| blue-400 on ink-950 | 6.32 | Dark-mode links ✔ |
| ink-400 on ink-900 | 5.70 | Dark-mode muted text ✔ |

**Approved pairings:** ink on white · white on ink · blue on white (large only) · white on blue-600 · blue-400 on ink-950 · mono-white logo on blue-500.
**Never:** blue text on ink (3.60, muddy); blue on blue; status colors as decoration; a third brand hue (no purple, teal, orange accents); gradients between ink and blue.

Dark mode is first-class. Swap semantic tokens (see `tokens.css`), never invert the logo by filter: use the reversed file.

---

## 5. Typography

| Role | Family | Weights | Notes |
|---|---|---|---|
| Display / headlines | **Lexend** | 600, 700 | Geometric, open, close cousin to the wordmark. Tracking -0.025em. Sentence case. |
| Body / UI | **Inter** | 400, 500, 600 | 16px base, 1.6 line height for prose, 1.4 for UI. |
| Code / eyebrow / data | **JetBrains Mono** | 400, 500 | Eyebrows: 12 to 14px, uppercase, +0.08em tracking, often blue-600 or ink-500. |

Google Fonts: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Lexend:wght@500;600;700&display=swap`

Scale (px, ratio 1.25): 12 · 14 · 16 · 20 · 25 · 31 · 39 · 49 · 61 · 76. Use `clamp()` for hero sizes.

Rules:
- **Sentence case** for headlines, buttons and nav. No ALL CAPS except mono eyebrows.
- Headlines are short (2 to 8 words). One idea each.
- You may set **one word** of a headline in brand blue `#0073fe` (large text only). Echoes the blue `.dev`. Never more than one.
- A mono eyebrow above a headline is a signature pattern: `// services`, `01 / process`, `v1.0`.
- No italics for emphasis in headlines. No underline except links. No text shadows.
- Prose max width 68ch.

---

## 6. Shape language and graphic motifs

Everything decorative comes from the mark. Nothing else.

1. **Outer round, inner square.** The mark's outside corners are heavily rounded; the inside edges where the halves meet are square. Apply this to cards, hero panels, images and buttons in pairs: a left panel gets `border-radius: 24px 0 0 24px`, its right partner `0 24px 24px 0`. A single standalone card can use a uniform `16px` radius.
2. **The seam.** A thin gap (not a line) between two adjacent blocks: 2 to 8px depending on scale, background showing through. Use it to split hero image and text, two-column feature rows, before/after, pricing pairs.
3. **The cut.** A single diagonal at **64°** from horizontal. Use it sparingly: a clipped corner on a hero image, a section divider, an animated wipe, a background slash in blue at low area. Never more than one cut per view.
4. **The stem.** A solid vertical ink or blue bar used as a left rule on quotes, callouts, active nav items and timelines.
5. **Two halves.** Compositions that pair ink and blue, left and right: dark left panel, blue right accent; "problem / solution"; "design / build". Duality is the brand idea.

Radius tokens: 6 (inputs, small chips), 10 (buttons), 16 (cards), 24 (hero panels), pill (tags only).

**Never:** blobs, waves, random circles, sparkles, 3D renders, isometric illustrations, glassmorphism, neon glows, noise gradients, drop-shadow-heavy cards, more than one diagonal angle.

---

## 7. Layout

- 12-column grid, max width 1200px, gutters 16px mobile / 32px desktop.
- 4px spacing grid; use only tokens 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
- Generous whitespace: section padding 96 to 128px desktop, 64px mobile.
- Strong left alignment. Centered text only for short hero lines and single CTAs.
- Asymmetric splits (5/7, 4/8) feel more on-brand than 6/6.
- Borders before shadows. 1px `ink-200` (light) or `ink-700` (dark).
- One blue focal point per screen.

---

## 8. Components (reference behavior)

| Component | Spec |
|---|---|
| Primary button | bg `blue-600`, text white 15 to 16px Inter 600, radius 10px, padding 12×20, hover `blue-700`, focus ring `0 0 0 3px rgba(0,115,254,.35)`. |
| Secondary button | transparent, 1px border `ink-200`, text ink; dark mode border `ink-700`, text `ink-50`. |
| Link | `blue-600` light / `blue-400` dark, underline offset 3px, underline on hover. |
| Card | surface bg, 1px border, radius 16px, padding 24 to 32px, no shadow by default. |
| Paired panels | outer-round / inner-square radii with a seam gap (section 6). |
| Code block | `ink-100` light / `ink-800` dark, JetBrains Mono 14px, radius 10px, blue for keywords only. |
| Tag / badge | mono 12px, pill radius, `blue-50` bg with `blue-700` text, or outline. |
| Input | 1px `ink-200`, radius 6px, focus border `blue-500` plus focus ring. |
| Nav | logo left, links Inter 500 15px, active item marked with a 2px blue stem or underline. |
| Callout | left stem 3px blue, `blue-50` bg (light) or `ink-900` (dark). |

---

## 9. Imagery and iconography

**Photography** (if used): real work, real hands on real keyboards and whiteboards, desk-level detail, architecture and structure. Cool neutral grade, slightly desaturated, high clarity, lots of negative space. A single blue element in frame is ideal. Crop with the outer-round / inner-square corners or the 64° cut.
**Avoid:** handshake stock photos, people pointing at screens, fake code with random neon, glowing brains, robots, globes, generic "teamwork" shots.

**Illustration:** prefer none. If required: flat geometric, built only from the mark's shapes (rounded bars, square inner edges, 64° cuts), ink and blue only.

**UI and diagrams:** wireframe-style line diagrams, 1.5px strokes in ink, one blue path for "the flow". Code screenshots on `ink-950` with blue highlights.

**Icons:** outline, 1.5px stroke (24px grid), rounded caps and joins, square inner corners where possible. Lucide is an acceptable base set. Ink or currentColor; blue only for the active state. No filled multicolor icons, no emoji.

**AI image prompt suffix** (append to any generation prompt):
`minimal, precise, engineered, cool neutral palette of charcoal #1d252f and white with a single electric blue #0073fe accent, flat lighting, generous negative space, no text, no logos, no gradients, no neon, no people pointing at screens`

---

## 10. Motion

- Short and decisive: 120ms (hover), 200ms (UI), 360ms (section reveals). Ease `cubic-bezier(0.2, 0.8, 0.2, 1)`.
- Signature moves: **the join** (two halves slide together and close the seam), **the cut wipe** (a 64° diagonal reveal), **the stem draw** (a vertical bar grows from top).
- No bounce, no elastic, no spin, no parallax overload. Respect `prefers-reduced-motion`.

---

## 11. Voice and copy

**Voice:** clear, direct, quietly confident. An expert colleague, not a salesperson.

| Do | Don't |
|---|---|
| Short sentences. Active verbs. | Long, padded paragraphs. |
| Concrete outcomes and specifics. | Buzzwords: synergy, cutting-edge, world-class, revolutionary, seamless, leverage. |
| "We" and "you". | Third-person corporate voice. |
| Plain technical terms where they help. | Jargon to sound clever. |
| One exclamation mark per page, max. Preferably none. | Hype, ALL CAPS, emoji in headlines. |
| "and" | The ampersand character. |

Mechanics: sentence case; Oxford comma; numerals for 10 and above; no ampersand; "handh.dev" always lowercase; em dashes sparingly.

**Sample tone (placeholder copy, not approved claims):**
- Headline: "Built right. Built to last."
- Headline: "Two halves of one job: design and build."
- Eyebrow + headline: `// process` then "From first sketch to shipped."
- CTA: "Start a project" · "See the work" · "Talk to us"
- Microcopy: "Saved." · "Something broke on our side. Try again in a minute."

---

## 12. Application recipes

- **Website hero:** white bg, mono eyebrow in blue-600, Lexend 61 to 76px headline in ink with one blue word, Inter 20px subline in ink-500, primary plus secondary button, right side a paired panel (ink left, image or blue right) with seam gap.
- **Social / OG card (1200×630):** ink-950 bg, reversed brandmark top left (64px), Lexend 700 headline in white, one word in blue-400, `handh.dev` in mono bottom left, a single blue 64° slash on the right third.
- **Favicon / app icon:** brandmark on white, or reversed brandmark on ink-800 rounded square.
- **Business card:** front ink-800 with reversed full logo centered; back white, name in Lexend, details in Inter, `handh.dev` URL in blue-600.
- **Slide deck:** white content slides, ink-950 section dividers with a big blue 64° cut, mono slide numbers `01 / 12`.
- **Email signature:** name (Inter 600), role (Inter 400, ink-500), `handh.dev` link in blue-600, no logo image or a 24px brandmark only.
- **README / docs:** brandmark 48px, H1 in Lexend, code blocks per section 8.

---

## 13. Agent checklist (run before you hand back)

- [ ] Name appears only as `handh.dev` or `handh-dev`, lowercase.
- [ ] Zero ampersands in visible text.
- [ ] `python3 brand/check-brand-name.py <files>` prints PASS.
- [ ] Only ink, blue, neutral scales and functional status colors used.
- [ ] Blue covers about 10% of area or less; one focal blue element per view.
- [ ] No `#0073fe` text under 24px (19px bold); small blue text uses `#005fd6` / `#4a93ff` on dark.
- [ ] Fonts are Lexend / Inter / JetBrains Mono.
- [ ] Logo is an unmodified file from `brand/assets/` with clear space.
- [ ] Decoration only from the motifs: outer-round corners, seam, 64° cut, stem.
- [ ] No gradients, glows, glass, blobs, stock handshakes or emoji.
- [ ] No invented facts (clients, numbers, testimonials).
- [ ] Works in light and dark, passes WCAG AA.
