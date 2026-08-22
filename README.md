# FulcrumGrid — Landing Page

The marketing landing page for **FulcrumGrid**, the operational platform hosting
a growing grid of apps: **Command Center**, **Collection**, **HR Suite**, and more.

Live domain: **[fulcrumgrid.com](https://fulcrumgrid.com)**

## What's here

A fast, dependency-free static site — no build step, no framework, no server required.

```
.
├── index.html          # Landing page
├── 404.html            # Not-found page
├── assets/
│   ├── css/styles.css  # All styles (dark theme, grid motif, responsive)
│   ├── js/main.js      # Nav, scroll reveal, form validation
│   └── favicon.svg     # Brand mark
├── CNAME               # Custom domain for GitHub Pages
├── robots.txt          # Crawler rules
└── sitemap.xml         # Sitemap
```

## Local preview

It's plain static files — open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy

The site is fully static and can be hosted anywhere. Point `fulcrumgrid.com` DNS
at whichever host you choose.

### GitHub Pages
1. Push this branch and merge to your default branch.
2. In the repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
3. Select the default branch and the `/ (root)` folder.
4. The included `CNAME` file sets the custom domain to `fulcrumgrid.com`.
5. Add DNS records at your registrar:
   - `A` records for the apex → GitHub Pages IPs (`185.199.108.153`, `.109`, `.110`, `.111`)
   - `CNAME` for `www` → `<username>.github.io`

### Netlify / Vercel / Cloudflare Pages
- **Build command:** _(none)_
- **Publish/output directory:** `/` (repository root)
- Add `fulcrumgrid.com` as a custom domain and follow the host's DNS instructions.

## Customizing

- **Products** — edit the `.product-card` blocks in `index.html`. Each has an accent
  set via `data-accent="teal|indigo|rose|slate"` and a status via `.tag-live` / `.tag-soon`.
- **Colors & theme** — the palette lives in the `:root` block at the top of `assets/css/styles.css`.
- **Copy** — all text is in `index.html`; there is no CMS or templating to learn.

## Demo form

The "Request a demo" form validates input client-side and falls back to a `mailto:`
to `hello@fulcrumgrid.com`, so no backend is required to start collecting leads.
Wire it to a real endpoint (Formspree, a serverless function, your CRM, etc.) by
replacing the submit handler in `assets/js/main.js`.
