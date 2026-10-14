# Concierge character — Rive artwork spec

This is what the `.riv` file must expose so it drops straight into the website
widget (`assets/js/concierge.js`) with no code changes. Until the file is
supplied the widget shows a built-in SVG placeholder, so the site keeps working.

Deliver the exported runtime file to **`assets/brand/concierge.riv`**
(the path `RIVE_SRC` in `scripts/build/concierge_config.py` — change the path
there if you prefer another location).

## The figure

- A **full standing character** (head-to-toe or head-to-knees), not a bust or an
  icon. It renders at roughly **120–220 px wide / 150–280 px tall** on desktop
  and about 60% of that on phones, so keep it readable at small sizes.
- On-brand for a clean B2B SaaS: restrained, friendly, professional — not a
  cartoon mascot. Brand accent is **#5980a6** (slate blue); ink **#1d1f20**;
  surfaces are light (#f2f2f3 / #fff). Match that palette.
- Design the artboard so the figure is **bottom-anchored and centered**; leave a
  little headroom. Transparent background. The widget adds the drop shadow.
- Keep the file lightweight (vector; target well under ~400 KB).

## Required state machine

Name the state machine exactly **`Concierge`**. It must expose these **inputs**
(exact names, case-sensitive):

| Input    | Type              | Driven by the site to mean…                                   |
|----------|-------------------|---------------------------------------------------------------|
| `state`  | **Number** (0–3)  | `0` idle · `1` listening · `2` thinking · `3` talking         |
| `mouth`  | **Number** (0–1)  | Live mouth-open amount while talking (0 = closed, 1 = open)    |

The code sets `state` on every transition and continuously writes `mouth`
(0→1) from the real audio amplitude while the character speaks, so **lip-sync is
automatic** — just wire the `mouth` number to the mouth shape (e.g. a blend/þ
interpolation or a 1D blend state on the jaw). You do not need visemes; a single
open/close blend reads well at this size.

### What each `state` should look like

- **0 · idle** — calm breathing / subtle sway, occasional blink. Approachable.
- **1 · listening** — leans in slightly, attentive; eyes up. (The site also
  draws a pulsing ring, so you don't have to.)
- **2 · thinking** — a brief "considering" beat (look away / small gesture).
- **3 · talking** — speaking posture / light gestures; the `mouth` input drives
  the lip movement on top of this.

Transitions between states should be quick (150–300 ms) and loop cleanly.

## Optional (nice to have, not required)

- A `wave` trigger for a one-time greeting wave when the character first appears.
- Separate idle variants so repeated idling doesn't look robotic.
- A boolean `rtl` input if you want the figure to face the other way in Arabic
  (the widget can set it; tell us the input name and we'll wire it).

## How it's wired (for reference)

```js
rive = new rive.Rive({ src: '/assets/brand/concierge.riv', canvas,
  stateMachines: 'Concierge', autoplay: true, fit: 'contain' });
// inputs 'state' (0–3) and 'mouth' (0–1) are set by the site each frame.
```

If any input name or the state-machine name differs in your file, either match
this spec or send us the names and we'll adjust the two lines that read them.
