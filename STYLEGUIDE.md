# FulcrumGrid — Style Guide

The visual system behind [fulcrumgrid.com](https://fulcrumgrid.com). Every value
below is the source of truth used across the site; the CSS tokens live in
[`assets/css/styles.css`](assets/css/styles.css) under `:root`.

A live, interactive version of this reference (click-to-copy swatches, type
specimens) is available as a shared artifact — ask the maintainer for the link.

---

## Brand at a glance

- **Theme:** deep-navy **dark theme**.
- **Accent pair:** **teal + indigo** (with violet as the bridge tone).
- **Type:** Space Grotesk (display) + Inter (body) + Cairo (Arabic).
- **Voice:** FulcrumGrid is a **family of purpose-built business apps from one
  team** — adopted independently. It is *not* a single integrated system, so
  avoid claims of single sign-on, shared data layers, or cross-app automation.

---

## Color

All colors are defined as CSS custom properties in `:root`. Prefer the token
(`var(--teal)`) over a raw hex in new code.

### Backgrounds

| Token | Hex | Use |
|-------|-----|-----|
| `--bg` | `#0b1020` | Page ground (near-black navy) |
| `--bg-2` | `#0e1428` | Alternate / banded sections |
| `--bg-elev` | `#131a33` | Elevated cards |
| `--surface` | `#161e3d` | Panels (e.g. the CTA panel) |

### Text

| Token | Hex | Use |
|-------|-----|-----|
| `--text` | `#e7ecf6` | Primary text |
| `--text-muted` | `#9aa6c6` | Secondary / supporting text |
| `--text-dim` | `#6b779c` | Captions, labels, disabled |

### Brand accents

| Token | Hex | Use |
|-------|-----|-----|
| `--teal` (`--accent-2`) | `#5eead4` | Primary accent — logo, links, highlights |
| `--indigo` (`--accent`) | `#6366f1` | Primary buttons, focus |
| `--violet` | `#a78bfa` | Gradient mid-tone |
| `--rose` | `#fb7185` | Third product accent |
| _(button gradient end)_ | `#4f46e5` | Deep indigo, primary-button gradient only |

### Borders

| Token | Value |
|-------|-------|
| `--border` | `rgba(148, 163, 214, 0.14)` |
| `--border-strong` | `rgba(148, 163, 214, 0.28)` |

### Semantic

| Purpose | Value |
|---------|-------|
| Success text (e.g. "Available now") | `#6ee7b7` |
| Success dot | `#34d399` |

> Semantic status color is intentionally separate from the brand accents.

### Signature gradient

Used on the logo, headline highlights (`.gradient-text`), and section accents:

```css
linear-gradient(100deg, #5eead4 0%, #a78bfa 50%, #6366f1 100%);
```

### Product color coding

Each app owns a single accent (set per page via the `--p-accent` variable, or
`data-accent` on homepage product cards):

| App | Accent | Hex |
|-----|--------|-----|
| Command Center | teal | `#5eead4` |
| Collection | indigo | `#6366f1` |
| HR Suite | rose | `#fb7185` |
| Coming soon | slate | `#6b779c` |

---

## Typography

Loaded from Google Fonts. Always declare the fallback stack.

| Face | Role | Weights | Token |
|------|------|---------|-------|
| **Space Grotesk** | Display — headings, logo, eyebrow labels | 500, 600, 700 | `--font-display` |
| **Inter** | Body & UI — paragraphs, buttons, captions | 400–800 | `--font-sans` |
| **Cairo** | Arabic (`/ar/`, RTL) — replaces both faces on Arabic pages | 400–800 | set per-page |

```css
--font-sans:    'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
--font-display: 'Space Grotesk', var(--font-sans);
/* Arabic pages override both to: 'Cairo', system-ui, sans-serif; */
```

**Guidelines**

- Headings use `--font-display`, `font-weight: 700`, `letter-spacing: -0.02em to -0.03em`, and `text-wrap: balance`.
- Eyebrow labels: `--font-display`, uppercase, `letter-spacing: 0.12em–0.16em`, teal.
- Body copy: Inter, `line-height: 1.6` (Arabic `1.75`), keep measure ~65ch.
- Fluid heading sizing via `clamp()` (e.g. hero `clamp(2.6rem, 6vw, 4.4rem)`).

---

## Design tokens

| Token | Value | Use |
|-------|-------|-----|
| `--radius` | `14px` | Cards, inputs, buttons |
| `--radius-lg` | `22px` | Large panels, product cards |
| _(pill)_ | `999px` | Tags, badges, the language switcher |
| `--shadow` | `0 20px 50px -20px rgba(0,0,0,0.6)` | Card hover / elevation |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | All transitions |
| `--maxw` | `1160px` | Content container width |
| Base font | `16px / 1.6` | Root |

All motion is gated behind `@media (prefers-reduced-motion: reduce)`.

---

## Components

### Buttons

```css
/* Primary */
background: linear-gradient(135deg, var(--indigo), #4f46e5);
color: #fff;
box-shadow: 0 10px 30px -12px rgba(99, 102, 241, 0.75);

/* Outline */
border: 1px solid var(--border-strong);
color: var(--text);
background: rgba(255, 255, 255, 0.02);   /* hover: teal border */

/* Ghost */
color: var(--text-muted);                /* hover: --text */
```

Shared: `padding: 11px 20px` (`btn-lg`: `14px 26px`), `border-radius: 11px`,
`font-weight: 600`. Hover lifts `translateY(-2px)`.

### Status tags (pills)

- **Available now** — `--tag-live`: `#6ee7b7` text on `rgba(52,211,153,0.1)`, glowing `#34d399` dot.
- **Coming soon** — `--tag-soon`: muted text on `rgba(148,163,214,0.08)`, dim dot.

### Cards

Elevated gradient `linear-gradient(180deg, var(--bg-elev), var(--bg-2))`, 1px
`--border`, `--radius-lg`, top accent bar tinted by the card's accent. Hover:
`translateY(-6px)` + `--border-strong` + `--shadow`.

---

## Layout & motion

- Grid/flex with `gap` for spacing — never per-element margins that collapse.
- Wide content (tables, code) scrolls inside its own `overflow-x: auto` container.
- Signature **grid motif** background: two 1px lavender line-gradients at `48px`
  spacing, masked with a radial fade.
- Scroll-reveal on cards/sections via `IntersectionObserver` (falls back to
  visible when unsupported or reduced-motion).

---

## Accessibility

- Skip-link on every page; visible keyboard focus states.
- Color contrast meets WCAG AA on the dark ground.
- Arabic pages are fully RTL (`dir="rtl"`) with a matching bilingual cookie banner.

---

## Where things live

```
assets/css/styles.css   → all tokens (:root) + components
assets/js/main.js       → nav, scroll reveal, form (lang-aware)
assets/js/consent.js    → bilingual cookie-consent banner
assets/favicon.svg      → brand mark (gradient F)
index.html /ar/         → English / Arabic homepages
products/ · pricing/ · about/  (mirrored under /ar/)
```

To retheme, edit the `:root` block in `assets/css/styles.css` — every surface,
button, and accent derives from those tokens.
