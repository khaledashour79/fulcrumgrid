# Content admin & build system

FulcrumGrid stays a fully pre-rendered static site (great for SEO), but content
now lives in structured files under `/content/` and a build step turns those into
the finished HTML. A browser-based admin at **`/admin/`** edits that content.

```
Edit at /admin/  →  commits a file in /content/  →  Deploy Action runs
scripts/build/build.py  →  regenerates pages + sitemap + llms.txt  →  Pages deploys
```

Nothing renders in the browser at runtime — every page still ships finished HTML
with its hreflang, JSON-LD, and OG tags intact.

## What the build owns
`scripts/build/build.py` (run automatically on every deploy) regenerates:

| From | Pages |
|---|---|
| `content/blog/*.json` | the blog posts it manages, the blog index cards + schema, sitemap and llms.txt entries |
| `content/pricing/*.json` | the three detailed pricing pages (tiers, prices, module matrix), EN + AR |

The build is **idempotent**: with content unchanged it reproduces the committed
HTML exactly, so a deploy never silently alters a page. A build error fails the
deploy (fail-safe) rather than publishing something broken.

## What's managed where
- **Blog** — fully editable in `/admin/`. Create or edit a post (all EN + AR
  fields, FAQs, CTA); saving rebuilds and deploys it, and slots it into the index,
  sitemap and llms.txt automatically.
- **Pricing** — externalised to `content/pricing/*.json` and build-managed. Edit
  the JSON (prices, tier names, taglines, module matrix) and the pages rebuild.
  A form UI for it in `/admin/` is a fast follow (the module matrix needs a
  custom widget).
- **Legacy blog posts** (the 14 pre-existing guides) are catalogued under
  `content/blog/catalog/` so they appear in the index/sitemap, but their HTML is
  left untouched. Migrate one into `content/blog/` (with its body) whenever you
  want it editable.
- **Product & marketing pages** (home, products, features, etc.) remain
  hand-authored HTML for now; they can be templatised into `/content/` the same
  way over time.

## Editing the blog
1. Go to `https://fulcrumgrid.com/admin/`, log in with GitHub.
2. **Blog posts → New Blog post.** Fill in the slug, category, date, and the
   EN/AR fields. `body_en` / `body_ar` take article HTML (`<h2>…</h2><p>…</p>`);
   the template adds the FAQ block, related links and CTA around it.
3. **Publish.** The Deploy Action rebuilds and the post is live in a minute or two.

## One-time setup (login)
The admin logs in with GitHub, which needs a small OAuth broker. Follow
`scripts/oauth-worker/README.md` once (register a GitHub OAuth App, deploy the
Cloudflare Worker, paste its URL into `admin/config.yml`). After that, editing is
entirely in the browser.

## Regenerating OG images (occasional)
The per-page Open Graph cards under `assets/og/` are rendered from HTML by a
headless browser, so they're not rebuilt on every deploy. When an app's name,
price or plans change, regenerate them:

```bash
cd scripts/build
python3 gen_og.py && python3 gen_og2.py     # writes card HTML
node render_og.mjs                           # renders PNGs (needs Playwright)
# then copy the PNGs into ../../assets/og/
```

## Running the build locally
```bash
python3 scripts/build/build.py     # regenerates blog + pricing from /content/
git diff                           # review, commit
```
