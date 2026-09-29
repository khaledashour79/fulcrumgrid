# -*- coding: utf-8 -*-
"""Daily multilingual Q&A blog posts.

Each post is authored ONCE as a self-contained 7-language JSON in
content/blog/daily/<slug>.json and this generator emits all seven new-design
pages (en at /blog/<slug>/, and ar/fr/de/es/it/nl at /<lang>/blog/<slug>/),
wires a card into every language's blog index, and appends the post URLs to
sitemap.xml.

It runs LAST in build.py — after gen_blog (English index), loc_static (European
indexes) and gen_sitemap — so the daily posts sit on top of a freshly built
site without going through loc_static's per-string catalogs (which would make a
new post's translations impossible to keep up at 3/day). Idempotent: the index
cards live in a marked region that is replaced every run, and the sitemap block
likewise.

Chrome (header, footer, language switcher) is lifted verbatim from each
language's already-built blog index, so nav labels, the switcher and the footer
always match the rest of that language's site.
"""
import os, re, sys, json, glob, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_blog as gb  # CSP, GA, hreflang_cluster, CAT, esc

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(HERE, '..', '..'))
DAILY = os.path.join(ROOT, 'content', 'blog', 'daily')

LANGS = [c for c, _, _ in gb.LANGS]                 # en, ar, fr, de, es, it, nl
PREFIX = {c: (pre) for c, pre, _ in gb.LANGS}       # '' , 'ar/', 'fr/', …
OG_LOCALE = {'en': 'en_US', 'ar': 'ar_AR', 'fr': 'fr_FR', 'de': 'de_DE',
             'es': 'es_ES', 'it': 'it_IT', 'nl': 'nl_NL'}

# Fixed per-language micro-copy for the article shell.
L = {
 'en': dict(home='Home', blog='Blog', faq='Frequently asked questions', back='Back to the blog', explore='Explore'),
 'ar': dict(home='الرئيسية', blog='المدوّنة', faq='الأسئلة الشائعة', back='العودة إلى المدوّنة', explore='استكشف'),
 'fr': dict(home='Accueil', blog='Blog', faq='Questions fréquentes', back='Retour au blog', explore='Découvrir'),
 'de': dict(home='Startseite', blog='Blog', faq='Häufige Fragen', back='Zurück zum Blog', explore='Entdecken'),
 'es': dict(home='Inicio', blog='Blog', faq='Preguntas frecuentes', back='Volver al blog', explore='Explorar'),
 'it': dict(home='Home', blog='Blog', faq='Domande frequenti', back='Torna al blog', explore='Esplora'),
 'nl': dict(home='Home', blog='Blog', faq='Veelgestelde vragen', back='Terug naar de blog', explore='Ontdek'),
}
# Category tag label per language.
CATLABEL = {
 'collection': dict(en='Collection', ar='التحصيل', fr='Collection', de='Collection', es='Collection', it='Collection', nl='Collection'),
 'hr':         dict(en='HR', ar='الموارد البشرية', fr='RH', de='HR', es='RRHH', it='HR', nl='HR'),
 'operations': dict(en='Operations', ar='العمليات', fr='Opérations', de='Betrieb', es='Operaciones', it='Operazioni', nl='Operaties'),
}
# Product proper names stay English except Arabic.
PRODNAME = {
 'collection': dict(ar='التحصيل', other='Collection'),
 'hr':         dict(ar='الموارد البشرية', other='HR Suite'),
 'operations': dict(ar='مركز القيادة', other='Command Center'),
}
PRODSLUG = {'collection': 'collection', 'hr': 'hr-suite', 'operations': 'command-center'}

MARK_A, MARK_B = '<!-- daily:start -->', '<!-- daily:end -->'
SITE = 'https://fulcrumgrid.com'
INDEX_CARDS = 18  # how many recent daily posts to surface on the blog index
                  # (every post still gets its pages and a sitemap entry)


def _t(s):
    """Escape a plain-text node (visible copy: headings, dek, card, FAQ text)."""
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _a(s):
    """Escape an HTML attribute value (title tag, og/twitter content=...)."""
    return _t(s).replace('"', '&quot;')


def load():
    posts = []
    for fp in sorted(glob.glob(os.path.join(DAILY, '*.json'))):
        if os.path.basename(fp).startswith('_'):
            continue
        posts.append(json.load(open(fp, encoding='utf-8')))
    posts.sort(key=lambda p: (p['date'], p['slug']), reverse=True)
    return posts


def chrome(lang):
    """(header, footer) lifted from the language's built blog index."""
    idx = os.path.join(ROOT, PREFIX[lang] + 'blog/index.html')
    txt = open(idx, encoding='utf-8').read()
    hdr = re.search(r'  <header class="site-head">.*?</header>', txt, re.S).group(0)
    ftr = re.search(r'  <footer class="site-foot">.*?</footer>', txt, re.S).group(0)
    return hdr, ftr


def head(lang, p, tr):
    slug = p['slug']; c = gb.CAT[p['cat']]
    pre = PREFIX[lang]
    canon = '%s/%sblog/%s/' % (SITE, pre, slug)
    suffix = 'blog/%s/' % slug
    title_tag = tr['title'] + ' — FulcrumGrid'
    og = c['og']; ogalt = c['ogalt_ar'] if lang == 'ar' else c['ogalt_en']
    alt = '\n'.join('  <meta property="og:locale:alternate" content="%s" />' % OG_LOCALE[o]
                    for o in LANGS if o != lang)
    meta_block = (
      '  <meta property="og:type" content="article" />\n'
      '  <meta property="og:title" content="%s" />\n'
      '  <meta property="og:description" content="%s" />\n'
      '  <meta property="og:url" content="%s" />\n'
      '  <meta property="og:site_name" content="FulcrumGrid" />\n'
      '  <meta property="og:locale" content="%s" />\n%s\n'
      '  <meta property="article:published_time" content="%s" />\n'
      '  <meta property="og:image" content="%s/assets/og/%s" />\n'
      '  <meta property="og:image:width" content="1200" />\n'
      '  <meta property="og:image:height" content="630" />\n'
      '  <meta property="og:image:type" content="image/png" />\n'
      '  <meta property="og:image:alt" content="%s" />\n'
      '  <meta name="twitter:card" content="summary_large_image" />\n'
      '  <meta name="twitter:title" content="%s" />\n'
      '  <meta name="twitter:description" content="%s" />\n'
      '  <meta name="twitter:image" content="%s/assets/og/%s" />'
    ) % (_a(tr['title']), _a(tr['desc']), canon, OG_LOCALE[lang], alt, p['date'],
         SITE, og, _a(ogalt), _a(tr['title']), _a(tr['desc']), SITE, og)

    faqs = [(f['q'], f['a']) for f in tr.get('faqs', [])]
    blogposting = {"@context":"https://schema.org","@type":"BlogPosting","headline":tr['title'],
      "description":tr['desc'],"datePublished":p['date'],"dateModified":p['date'],
      "author":{"@type":"Organization","name":"FulcrumGrid","@id":SITE+"/#organization"},
      "publisher":{"@id":SITE+"/#organization"},"image":SITE+"/assets/og/"+og,
      "mainEntityOfPage":{"@type":"WebPage","@id":canon},"inLanguage":lang}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":tr['home_name'] if 'home_name' in tr else L[lang]['home'],"item":"%s/%s"%(SITE, pre)},
      {"@type":"ListItem","position":2,"name":L[lang]['blog'],"item":"%s/%sblog/"%(SITE, pre)},
      {"@type":"ListItem","position":3,"name":tr['bc'],"item":canon}]}
    objs = [blogposting, bc] + ([{"@context":"https://schema.org","@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}] if faqs else [])
    ld = '\n'.join('  <script type="application/ld+json">\n  %s\n  </script>'
                   % json.dumps(o, ensure_ascii=False, indent=2).replace('\n', '\n  ') for o in objs)

    fonts = ('  <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
             '&family=Barlow+Condensed:wght@400;500;600;700&display=swap" rel="stylesheet" />')
    if lang == 'ar':
        fonts += ('\n  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800'
                  '&display=swap" rel="stylesheet" />')
    return ('<head>\n'
      '  <meta charset="UTF-8" />\n'
      '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
      '  <meta http-equiv="Content-Security-Policy" content="%s" />\n\n  %s\n\n'
      '  <title>%s</title>\n  <meta name="description" content="%s" />\n'
      '  <meta name="theme-color" content="#f2f2f3" />\n\n%s\n'
      '  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />\n\n'
      '  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />\n'
      '  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/icon-32.png" />\n'
      '  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/icon-16.png" />\n'
      '  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/icon-180.png" />\n'
      '  <link rel="manifest" href="/site.webmanifest" />\n'
      '  <link rel="canonical" href="%s" />\n%s\n\n'
      '  <link rel="preconnect" href="https://fonts.googleapis.com" />\n'
      '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n%s\n'
      '  <link rel="stylesheet" href="/assets/css/fg2.css" />\n%s\n</head>'
    ) % (gb.CSP, gb.GA, _a(title_tag), _a(tr['desc']), meta_block, canon,
         gb.hreflang_cluster(suffix), fonts, ld)


def page(lang, p, tr, hdr, ftr):
    pre = PREFIX[lang]; cat = p['cat']
    prodname = PRODNAME[cat]['ar'] if lang == 'ar' else PRODNAME[cat]['other']
    prod = '/%sproducts/%s/' % (pre, PRODSLUG[cat])
    bloghref = '/%sblog/' % pre
    homehref = '/%s' % pre if pre else '/'
    faqs = [(f['q'], f['a']) for f in tr.get('faqs', [])]
    faq_html = ''
    if faqs:
        items = '\n'.join('        <details class="faq-item"><summary>%s</summary><p>%s</p></details>' % (_t(q), _t(a)) for q, a in faqs)
        faq_html = '\n        <h2>%s</h2>\n%s\n' % (_t(L[lang]['faq']), items)
    htmltag = '<html lang="ar" dir="rtl">' if lang == 'ar' else '<html lang="%s">' % lang
    return '''<!DOCTYPE html>
%(htmltag)s
%(head)s
<body>
%(header)s

  <main>
    <section class="section">
      <div class="wrap pad">
        <p class="mono"><a href="%(homehref)s">%(home)s</a> / <a href="%(bloghref)s">%(blog)s</a> / %(bc)s</p>
        <span class="tag tag-accent">%(catlabel)s</span>
        <h1>%(title)s</h1>
        <p class="hero-intro">%(dek)s</p>
        <p class="mono"><time datetime="%(date)s">%(metadate)s</time> · %(read)s</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap pad" style="max-width:760px">
%(body)s
%(faq)s
        <p style="margin-top:32px"><a href="%(bloghref)s"><span aria-hidden="true">←</span> %(back)s</a></p>
      </div>
    </section>

    <section class="section cta">
      <div class="wrap">
        <p class="mono mono-accent">%(kicker)s</p>
        <h2>%(cta_h)s</h2>
        <p class="section-lead" style="margin:0 auto 26px">%(cta_p)s</p>
        <div class="actions">
          <a class="btn btn-primary" href="%(prod)s">%(explore)s %(prodname)s</a>
          <a class="btn btn-secondary" href="%(bloghref)s">%(back)s</a>
        </div>
      </div>
    </section>
  </main>

%(footer)s

  <script src="/assets/js/consent.js" defer></script>
</body>
</html>
''' % dict(htmltag=htmltag, head=head(lang, p, tr), header=hdr, footer=ftr,
           homehref=homehref, home=L[lang]['home'], bloghref=bloghref, blog=L[lang]['blog'],
           bc=_t(tr['bc']), catlabel=_t(CATLABEL[cat][lang]), title=_t(tr['title']),
           dek=_t(tr['desc']), date=p['date'], metadate=_t(tr['metadate']), read=_t(tr['read']),
           body=tr['body'].strip(), faq=faq_html, back=_t(L[lang]['back']),
           kicker=_t('FulcrumGrid ' + prodname), cta_h=_t(tr['cta_h']), cta_p=_t(tr['cta_p']),
           prod=prod, explore=_t(L[lang]['explore']), prodname=_t(prodname))


def card(lang, p, tr):
    pre = PREFIX[lang]
    return ('          <article class="app-card">\n'
            '            <div class="head"><span class="tag tag-outline">%s</span></div>\n'
            '            <h3><a href="/%sblog/%s/" style="text-decoration:none;color:inherit">%s</a></h3>\n'
            '            <p class="line">%s</p>\n'
            '            <p class="mono"><time datetime="%s">%s</time> · %s</p>\n'
            '          </article>') % (
        _t(CATLABEL[p['cat']][lang]), pre, p['slug'], _t(tr['title']),
        _t(tr['card']), p['date'], _t(tr['metadate']), _t(tr['read']))


def splice_index(lang, cards_html):
    """Insert (or replace) the daily-cards region at the top of the language's
    blog index apps-grid."""
    idx = os.path.join(ROOT, PREFIX[lang] + 'blog/index.html')
    txt = open(idx, encoding='utf-8').read()
    txt = re.sub(re.escape(MARK_A) + r'.*?' + re.escape(MARK_B) + r'\n?', '', txt, flags=re.S)
    region = '%s\n%s\n%s\n' % (MARK_A, cards_html, MARK_B)
    txt = re.sub(r'(<div class="apps-grid">\n)', r'\1' + region.replace('\\', '\\\\'), txt, count=1)
    open(idx, 'w', encoding='utf-8').write(txt)


def splice_sitemap(url_blocks):
    sm = os.path.join(ROOT, 'sitemap.xml')
    txt = open(sm, encoding='utf-8').read()
    txt = re.sub(r'  <!-- daily -->.*?  <!-- /daily -->\n', '', txt, flags=re.S)
    block = '  <!-- daily -->\n' + ''.join(url_blocks) + '  <!-- /daily -->\n'
    txt = txt.replace('</urlset>', block + '</urlset>')
    open(sm, 'w', encoding='utf-8').write(txt)


def sitemap_url(p):
    suffix = 'blog/%s/' % p['slug']
    alts = ''.join('    <xhtml:link rel="alternate" hreflang="%s" href="%s/%s%s" />\n'
                   % (c, SITE, PREFIX[c], suffix) for c in LANGS)
    alts += '    <xhtml:link rel="alternate" hreflang="x-default" href="%s/%s" />\n' % (SITE, suffix)
    out = []
    for c in LANGS:
        out.append('  <url>\n    <loc>%s/%s%s</loc>\n    <lastmod>%s</lastmod>\n'
                   '    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n%s  </url>\n'
                   % (SITE, PREFIX[c], suffix, p['date'], alts))
    return ''.join(out)


def main():
    posts = load()
    n = 0
    for lang in LANGS:
        hdr, ftr = chrome(lang)
        for p in posts:                       # every post gets its page in every language
            tr = p['lang'][lang]
            out = os.path.join(ROOT, PREFIX[lang] + 'blog/%s/index.html' % p['slug'])
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'w', encoding='utf-8').write(page(lang, p, tr, hdr, ftr))
            n += 1
        # Surface only the most recent INDEX_CARDS on the index (posts are
        # newest-first); always reconcile the region so removals disappear too.
        cards = [card(lang, p, p['lang'][lang]) for p in posts[:INDEX_CARDS]]
        splice_index(lang, '\n'.join(cards))
    splice_sitemap([sitemap_url(p) for p in posts])
    print('gen_daily: wrote %d pages for %d daily post(s)' % (n, len(posts)))


if __name__ == '__main__':
    main()
