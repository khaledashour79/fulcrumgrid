# -*- coding: utf-8 -*-
import os, re, json, glob, html
ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CONTENT = os.path.join(ROOT, 'content', 'blog')

CSP = "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com https://www.googleadservices.com https://www.google.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; img-src 'self' data: https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net; connect-src 'self' https://ipapi.co https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://analytics.google.com https://region1.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net https://api.web3forms.com; font-src 'self' https://fonts.gstatic.com; object-src 'none'; base-uri 'self'; form-action 'self' mailto:; frame-src https://td.doubleclick.net"

GA = '''<!-- Google tag (gtag.js) — FulcrumGrid GA4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-YJDJ643CY3"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('consent','default',{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied','analytics_storage':'denied','wait_for_update':500});
    try{if(localStorage.getItem('fg_consent')==='granted'){gtag('consent','update',{'ad_storage':'granted','ad_user_data':'granted','ad_personalization':'granted','analytics_storage':'granted'});}}catch(e){}
    gtag('config', 'G-YJDJ643CY3');
  </script>'''

# 7-language cluster used across the site (en lives at the root).
LANGS = [('en', '', 'English'), ('ar', 'ar/', 'العربية'), ('fr', 'fr/', 'Français'),
         ('de', 'de/', 'Deutsch'), ('es', 'es/', 'Español'), ('it', 'it/', 'Italiano'),
         ('nl', 'nl/', 'Nederlands')]

CAT = {
 'collection': dict(label_en='Collection', label_ar='التحصيل', og='og-collection.png',
    acc='var(--color-accent)',
    ogalt_en='FulcrumGrid Collection — receivables and payments',
    ogalt_ar='التحصيل من FulcrumGrid — الذمم والمدفوعات',
    prod_en='/products/collection/', prod_ar='/ar/products/collection/',
    k_en='FulcrumGrid Collection', k_ar='التحصيل من FulcrumGrid',
    explore_en='Explore Collection', explore_ar='استكشف التحصيل'),
 'hr': dict(label_en='HR', label_ar='الموارد البشرية', og='og-hr-suite.png',
    acc='var(--color-accent)',
    ogalt_en='FulcrumGrid HR Suite — people operations',
    ogalt_ar='الموارد البشرية من FulcrumGrid — عمليات الأفراد',
    prod_en='/products/hr-suite/', prod_ar='/ar/products/hr-suite/',
    k_en='FulcrumGrid HR Suite', k_ar='الموارد البشرية من FulcrumGrid',
    explore_en='Explore HR Suite', explore_ar='استكشف الموارد البشرية'),
 'operations': dict(label_en='Operations', label_ar='العمليات', og='og-command-center.png',
    acc='var(--color-accent)',
    ogalt_en='FulcrumGrid Command Center — operations at a glance',
    ogalt_ar='مركز القيادة من FulcrumGrid — العمليات في لمحة',
    prod_en='/products/command-center/', prod_ar='/ar/products/command-center/',
    k_en='FulcrumGrid Command Center', k_ar='مركز القيادة من FulcrumGrid',
    explore_en='Explore Command Center', explore_ar='استكشف مركز القيادة'),
}

def load_posts():
    """Load managed posts from content/blog/*.json and legacy catalogue
    entries from content/blog/catalog/*.json, newest first (by date). FAQs are
    stored as {q,a} objects (what the CMS list widget writes) and normalised to
    (q, a) tuples for rendering."""
    files = (glob.glob(os.path.join(CONTENT, '*.json'))
             + glob.glob(os.path.join(CONTENT, 'catalog', '*.json')))
    posts = []
    for fp in files:
        if os.path.basename(fp).startswith('_'):
            continue
        p = json.load(open(fp, encoding='utf-8'))
        for k in ('faqs_en', 'faqs_ar'):
            if k in p:
                p[k] = [((f['q'], f['a']) if isinstance(f, dict) else tuple(f)) for f in p[k]]
        posts.append(p)
    posts.sort(key=lambda p: (p['date'], p['slug']), reverse=True)
    return posts

POSTS = load_posts()

def esc(s):
    return s.replace('&','&amp;')

def faq_details(faqs):
    return '\n'.join('        <details class="faq-item"><summary>%s</summary><p>%s</p></details>'%(q,a) for q,a in faqs)

def faq_schema(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

# ── New-design (fg2) shared chrome ─────────────────────────────────────────

def hreflang_cluster(suffix):
    """Full 7-language hreflang cluster + x-default for a path suffix such as
    'blog/' or 'blog/<slug>/'. English lives at the site root."""
    lines = ['  <link rel="alternate" hreflang="%s" href="https://fulcrumgrid.com/%s%s" />' % (code, pre, suffix)
             for code, pre, _ in LANGS]
    lines.append('  <link rel="alternate" hreflang="x-default" href="https://fulcrumgrid.com/%s" />' % suffix)
    return '\n'.join(lines)

def page_head(title_tag, desc, canon, suffix, meta_block, ld=''):
    """New-design <head>: CSP, GA, Barlow fonts, /assets/css/fg2.css, icons,
    manifest, canonical + full hreflang cluster, and the page-specific
    og/twitter meta_block (+ optional JSON-LD)."""
    ld_part = ('\n' + ld) if ld else ''
    return '''<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Content-Security-Policy" content="%(csp)s" />

  %(ga)s

  <title>%(title)s</title>
  <meta name="description" content="%(desc)s" />
  <meta name="theme-color" content="#f2f2f3" />

%(meta)s
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />

  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/icon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/icon-16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/icon-180.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="canonical" href="%(canon)s" />
%(hreflang)s

  <link rel="preload" href="/assets/fonts/barlowcond-600-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="/assets/fonts/barlow-400-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="/assets/css/fg2.css" />%(ld)s
</head>''' % dict(csp=CSP, ga=GA, title=esc(title_tag), desc=esc(desc), meta=meta_block,
                  canon=canon, hreflang=hreflang_cluster(suffix), ld=ld_part)

def site_header(suffix):
    """New-design sticky header (site-head) with the Blog nav item active.
    Language menu links point at the per-language equivalent of this page."""
    menu = []
    for code, pre, name in LANGS:
        active = ' class="active"' if code == 'en' else ''
        menu.append('            <a href="/%s%s"%s hreflang="%s" lang="%s">%s</a>' % (pre, suffix, active, code, code, name))
    return '''  <header class="site-head">
    <div class="wrap row">
      <a class="brand" href="/" aria-label="FulcrumGrid home">
        <span class="brand-mark">F</span>
        <span class="brand-name">Fulcrum<b>Grid</b></span>
      </a>
      <nav class="site-nav" aria-label="Primary">
        <a href="/products/">Products</a>
        <a href="/features/">Platform</a>
        <a href="/pricing/">Pricing</a>
        <a href="/regions/">Regions</a>
        <a href="/blog/" class="active" aria-current="page">Blog</a>
        <a href="/contact/">Contact</a>
      </nav>
      <div class="head-cta">
        <details class="lang-dd">
          <summary aria-label="Language">EN ▾</summary>
          <div class="lang-dd-menu">
%(menu)s
          </div>
        </details>
        <a class="btn btn-primary btn-sm" href="/contact/">Request a demo</a>
      </div>
      <button class="nav-toggle" aria-label="Menu"><span>≡</span></button>
    </div>
  </header>''' % dict(menu='\n'.join(menu))

# New-design footer (site-foot). HR Suite is listed first among the apps.
FOOTER_EN = '''  <footer class="site-foot">
    <div class="wrap">
      <div class="foot-grid">
        <div class="foot-brand">
          <span class="brand-name">Fulcrum<b>Grid</b></span>
          <p>The operational backbone for modern teams.</p>
        </div>
        <div class="foot-col">
          <h5>Products</h5>
          <a href="/products/">All products</a>
          <a href="/products/hr-suite/">HR Suite</a>
          <a href="/products/command-center/">Command Center</a>
          <a href="/products/collection/">Collection</a>
          <a href="/custom-apps/">Custom apps</a>
        </div>
        <div class="foot-col">
          <h5>Platform</h5>
          <a href="/features/">Features</a>
          <a href="/integrations/">Integrations</a>
          <a href="/how-it-works/">How it works</a>
          <a href="/pricing/">Pricing</a>
          <a href="/regions/">Regions</a>
          <a href="/blog/">Blog</a>
        </div>
        <div class="foot-col">
          <h5>Company</h5>
          <a href="/about/">About</a>
          <a href="/faq/">FAQ</a>
          <a href="/contact/">Contact</a>
          <a href="/privacy/">Privacy</a>
          <a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting ↗</a>
        </div>
      </div>
      <div class="foot-bottom">
        <span>© <span id="yr">2026</span> FulcrumGrid. All rights reserved.</span>
        <span class="mono">fulcrumgrid.com</span>
      </div>
    </div>
  </footer>'''

END_SCRIPT = '  <script src="/assets/js/consent.js" defer></script>'

# ── Article pages (English, new design) ────────────────────────────────────

def render(post, lang):
    # Arabic emission is guarded for now — handled in a later pass. Only the
    # English article pages are rendered in the new (fg2) design.
    assert lang == 'en', 'render() only emits English in the new design'
    c = CAT[post['cat']]
    slug = post['slug']
    canon = 'https://fulcrumgrid.com/blog/%s/' % slug
    title = post['title_en']; desc = post['desc_en']; ogdesc = post['ogdesc_en']
    # Optional shorter <title> tag (h1/og/schema still use the full title).
    title_tag = (post.get('title_short_en') or title) + ' — FulcrumGrid'
    faqs = post.get('faqs_en') or []

    # JSON-LD (preserved from the previous build).
    blogposting = {"@context":"https://schema.org","@type":"BlogPosting","headline":title,
      "description":ogdesc,"datePublished":post['date'],"dateModified":post['date'],
      "author":{"@type":"Organization","name":"FulcrumGrid","@id":"https://fulcrumgrid.com/#organization"},
      "publisher":{"@id":"https://fulcrumgrid.com/#organization"},
      "image":"https://fulcrumgrid.com/assets/og/"+c['og'],
      "mainEntityOfPage":{"@type":"WebPage","@id":canon},"inLanguage":"en"}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":"https://fulcrumgrid.com/"},
      {"@type":"ListItem","position":2,"name":"Blog","item":"https://fulcrumgrid.com/blog/"},
      {"@type":"ListItem","position":3,"name":post['bc_en'],"item":canon}]}
    ld_objs = [blogposting, bc] + ([faq_schema(faqs)] if faqs else [])
    ld = '\n'.join('  <script type="application/ld+json">\n  %s\n  </script>'
                   % json.dumps(o, ensure_ascii=False, indent=2).replace('\n', '\n  ') for o in ld_objs)

    meta_block = '''  <meta property="og:type" content="article" />
  <meta property="og:title" content="%(title)s" />
  <meta property="og:description" content="%(ogdesc)s" />
  <meta property="og:url" content="%(canon)s" />
  <meta property="og:site_name" content="FulcrumGrid" />
  <meta property="og:locale" content="en_US" />
  <meta property="article:published_time" content="%(date)s" />
  <meta property="og:image" content="https://fulcrumgrid.com/assets/og/%(og)s" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:type" content="image/png" />
  <meta property="og:image:alt" content="%(ogalt)s" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="%(title)s" />
  <meta name="twitter:description" content="%(ogdesc)s" />
  <meta name="twitter:image" content="https://fulcrumgrid.com/assets/og/%(og)s" />''' % dict(
        title=esc(title), ogdesc=esc(ogdesc), canon=canon, date=post['date'],
        og=c['og'], ogalt=esc(c['ogalt_en']))

    body_inner = post['body_en'].strip()
    faq_block = ('\n        <h2>Frequently asked questions</h2>\n%s\n' % faq_details(faqs)) if faqs else ''
    related = (post.get('related_en') or '').strip()
    rel_block = ('\n        <hr />\n        %s\n' % related) if related else ''

    return '''<!DOCTYPE html>
<html lang="en">
%(head)s
<body>
%(header)s

  <main>
    <section class="section">
      <div class="wrap pad">
        <p class="mono"><a href="/">Home</a> / <a href="/blog/">Blog</a> / %(bc)s</p>
        <span class="tag tag-accent">%(catlabel)s</span>
        <h1>%(title_html)s</h1>
        <p class="hero-intro">%(dek)s</p>
        <p class="mono"><time datetime="%(date)s">%(metadate)s</time> · %(read)s</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap pad" style="max-width:760px">
%(body)s
%(faq_block)s%(rel_block)s
        <p style="margin-top:32px"><a href="/blog/"><span aria-hidden="true">←</span> Back to the blog</a></p>
      </div>
    </section>

    <section class="section cta">
      <div class="wrap">
        <p class="mono mono-accent">%(k)s</p>
        <h2>%(cta_h)s</h2>
        <p class="section-lead" style="margin:0 auto 26px">%(cta_p)s</p>
        <div class="actions">
          <a class="btn btn-primary" href="%(prod)s">%(explore)s</a>
          <a class="btn btn-secondary" href="/blog/">Back to the blog</a>
        </div>
      </div>
    </section>
  </main>

%(footer)s

%(end_script)s
</body>
</html>
''' % dict(
        head=page_head(title_tag, desc, canon, 'blog/%s/' % slug, meta_block, ld),
        header=site_header('blog/%s/' % slug), footer=FOOTER_EN, end_script=END_SCRIPT,
        bc=esc(post['bc_en']), catlabel=esc(c['label_en']), title_html=esc(title),
        dek=esc(desc), date=post['date'], metadate=post['metadate_en'], read=post['read_en'],
        body=body_inner, faq_block=faq_block, rel_block=rel_block,
        k=esc(c['k_en']), cta_h=esc(post['cta_h_en']), cta_p=esc(post['cta_p_en']),
        prod=c['prod_en'], explore=esc(c['explore_en']))

def is_legacy(p):
    return bool(p.get('legacy'))

def write_posts():
    # Only render pages the build owns (non-legacy). Legacy posts are
    # catalogued for the index but their HTML is left untouched.
    # Arabic (/ar/blog/...) is intentionally NOT written for now — the AR
    # migration is a later pass; AR data in the JSON is preserved untouched.
    for p in POSTS:
        if is_legacy(p):
            continue
        for lang in ('en',):  # AR guarded — do not write /ar/blog/<slug>/
            d = os.path.join(ROOT, 'blog/%s' % p['slug'])
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(render(p, lang))
            print('wrote', d + '/index.html')

# ── Blog index (English, new design) ───────────────────────────────────────

def card(p):
    c = CAT[p['cat']]
    return '''          <article class="app-card">
            <div class="head"><span class="tag tag-outline">%s</span></div>
            <h3><a href="/blog/%s/" style="text-decoration:none;color:inherit">%s</a></h3>
            <p class="line">%s</p>
            <p class="mono"><time datetime="%s">%s</time> · %s</p>
          </article>''' % (esc(c['label_en']), p['slug'], esc(p['title_en']),
                           esc(p['card_en']), p['date'], p['cardtime_en'], p['read_en'])

def index_html():
    cards = '\n'.join(card(p) for p in POSTS)
    blog_ld = {"@context":"https://schema.org","@type":"Blog","@id":"https://fulcrumgrid.com/blog/#blog",
      "name":"The FulcrumGrid blog",
      "description":"Practical guides on operations, receivables, and people operations.",
      "url":"https://fulcrumgrid.com/blog/","inLanguage":"en",
      "publisher":{"@id":"https://fulcrumgrid.com/#organization"},
      "blogPost":[{"@type":"BlogPosting","headline":p['title_en'],
                   "url":"https://fulcrumgrid.com/blog/%s/"%p['slug'],"datePublished":p['date']}
                  for p in POSTS]}
    ld = '  <script type="application/ld+json">\n  %s\n  </script>' % json.dumps(
        blog_ld, ensure_ascii=False, indent=2).replace('\n', '\n  ')

    meta_block = '''  <meta property="og:type" content="website" />
  <meta property="og:title" content="The FulcrumGrid blog" />
  <meta property="og:description" content="Practical guides on operations, receivables, and people operations." />
  <meta property="og:url" content="https://fulcrumgrid.com/blog/" />
  <meta property="og:site_name" content="FulcrumGrid" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:image" content="https://fulcrumgrid.com/assets/og/og-blog.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:type" content="image/png" />
  <meta property="og:image:alt" content="The FulcrumGrid blog — practical guides for operators" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="The FulcrumGrid blog" />
  <meta name="twitter:description" content="Practical guides on operations, receivables, and people operations." />
  <meta name="twitter:image" content="https://fulcrumgrid.com/assets/og/og-blog.png" />'''

    return '''<!DOCTYPE html>
<html lang="en">
%(head)s
<body>
%(header)s

  <main>
    <section class="section">
      <div class="wrap pad">
        <p class="hero-eyebrow">Blog</p>
        <h1>The FulcrumGrid blog</h1>
        <p class="hero-intro">Practical guides on operations, receivables, and people operations — from the team building FulcrumGrid.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap pad">
        <div class="apps-grid">
%(cards)s
        </div>
      </div>
    </section>
  </main>

%(footer)s

%(end_script)s
</body>
</html>
''' % dict(
        head=page_head('Blog — FulcrumGrid',
                       "Practical guides on operations, receivables, and people operations — from the team building FulcrumGrid's business apps.",
                       'https://fulcrumgrid.com/blog/', 'blog/', meta_block, ld),
        header=site_header('blog/'), footer=FOOTER_EN, end_script=END_SCRIPT, cards=cards)

def ensure_index(lang):
    """Rewrite the blog index in the new (fg2) design with a card for every
    catalogued post (legacy + owned), newest-first. Regenerated wholesale each
    run, so output is deterministic and idempotent. Arabic is guarded for now."""
    if lang != 'en':
        return False  # AR index guarded — handled in a later pass.
    f = os.path.join(ROOT, 'blog/index.html')
    new = index_html()
    old = open(f, encoding='utf-8').read() if os.path.exists(f) else None
    if old == new:
        return False
    open(f, 'w', encoding='utf-8').write(new)
    print('wrote index', f)
    return True

def ensure_sitemap():
    f = os.path.join(ROOT, 'sitemap.xml')
    s = open(f,encoding='utf-8').read()
    changed = False
    m = re.search(r'  <url>\n    <loc>https://fulcrumgrid\.com/blog/[a-z-]+/</loc>', s)
    if not m:
        return False
    anchor = m.start()
    for p in reversed(POSTS):
        slug = p['slug']
        if 'https://fulcrumgrid.com/blog/%s/</loc>' % slug in s:
            continue
        block = ('''  <url>
    <loc>https://fulcrumgrid.com/blog/%s/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://fulcrumgrid.com/blog/%s/" />
    <xhtml:link rel="alternate" hreflang="ar" href="https://fulcrumgrid.com/ar/blog/%s/" />
    <lastmod>%s</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://fulcrumgrid.com/ar/blog/%s/</loc>
    <lastmod>%s</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
''' % (slug, slug, slug, p['date'], slug, p['date']))
        s = s[:anchor] + block + s[anchor:]
        changed = True
    if changed:
        open(f,'w',encoding='utf-8').write(s)
        print('updated sitemap.xml')
    return changed

def ensure_llms():
    f = os.path.join(ROOT, 'llms.txt')
    s = open(f,encoding='utf-8').read()
    anchor = '## Guides (blog)\n'
    if anchor not in s:
        return False
    changed = False
    lines = ''
    for p in reversed(POSTS):
        url = 'https://fulcrumgrid.com/blog/%s/' % p['slug']
        if url in s:
            continue
        lines = '- [%s](%s)\n' % (html.unescape(p['title_en']), url) + lines
        changed = True
    if changed:
        s = s.replace(anchor, anchor + lines, 1)
        open(f,'w',encoding='utf-8').write(s)
        print('updated llms.txt')
    return changed

def build_blog():
    write_posts()
    ensure_index('en')
    # ensure_index('ar')  # AR blog index guarded for now — later migration pass.
    # sitemap.xml is regenerated wholesale (all languages) by gen_sitemap.py,
    # which build.py runs after localization; the old incremental EN/AR-only
    # appender is intentionally no longer called here.
    ensure_llms()

if __name__ == '__main__':
    build_blog()
