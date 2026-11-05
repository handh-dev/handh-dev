# handh.dev brand

every line is a constraint. follow all of them.
what: technology and infrastructure for howeth and harp, bubbas fireworks, and related companies.
base: https://raw.githubusercontent.com/handh-dev/handh-dev/main/brand/

## name
- only `handh.dev` (display) or `handh-dev` (slugs, repos, files, code). always lowercase.
- no ampersand in any visible text, write "and". no initials, no other spelling.
- lowercase repo slugs like `handh-infra` are identifiers, not the name.

## color
- ink `#1d252f`: text, dark surfaces
- blue `#0073fe`: logo, text 24px+, graphics, focus. never small text
- action `#005fd6`: buttons, links, small blue text. hover `#004cad`
- light: bg `#ffffff`, subtle `#f6f7f9`, border `#d8dce3`, muted `#5f6a7a`
- dark: bg `#0b0f14`, surface `#141a22`, border `#313a46`, muted `#8a94a3`, link `#4a93ff`
- status `#0f8a5f` `#b25e00` `#d1293d`: ui feedback only
- area 75% neutral, 15% ink, 10% blue. one blue focal point per view. no other hues, no gradients, no blue on ink
- css variables, light and dark: base + `tokens.css`

## type
- Lexend 600/700 headlines, tracking -0.025em, sentence case, at most one blue word
- Inter 400/500/600 body, 16px, line height 1.6, max 68ch
- JetBrains Mono code and eyebrows: 12-14px, uppercase, +0.08em, e.g. `// process`
- scale px: 12 14 16 20 25 31 39 49 61 76

## shape
- decoration comes only from the mark: outer corners round, inner corners square (pairs `24px 0 0 24px` + `0 24px 24px 0`), seam gap 2-8px between joined blocks, one 64° diagonal cut per view, vertical stem bar for quotes and active states
- radius: 6 input, 10 button, 16 card, 24 hero, pill tags only
- 4px grid, 1200px max, left aligned, generous space, borders over shadows
- never: blobs, waves, glass, glows, 3d, stock photos, emoji in ui

## ui
- button: bg `#005fd6`, white Inter 600 15px, radius 10, padding 12×20, focus `0 0 0 3px rgba(0,115,254,.35)`
- card: 1px border, radius 16, padding 24, no shadow
- icons: outline, 1.5px stroke, currentColor

## logo
base + `assets/` + file. use as-is: never redraw, retype, recolor, stretch, rotate or add effects.
- `handh-dev-full-tight.svg`: light backgrounds
- `handh-dev-full-reversed-tight.svg`: dark backgrounds
- `handh-dev-full-mono-white-tight.svg`: on blue or photos
- `handh-dev-brandmark.svg`, `handh-dev-brandmark-reversed.svg`: headers and navs. the full logo is stacked and has no horizontal version
- min size: mark 24px, full logo 96px wide. clear space 25% of mark width

## voice
- clear, direct, calm. short sentences, active verbs, specifics
- no buzzwords, no hype, no invented clients, numbers or quotes: use `[placeholder]`

## verify
`curl -fsSL https://raw.githubusercontent.com/handh-dev/handh-dev/main/brand/check-brand-name.py | python3 - <path>` must print PASS.

## more
fetch base + `BRAND.md` only for: imagery and ai image prompts (§9), motion (§10), layout recipes for og cards, decks, business cards (§12).
