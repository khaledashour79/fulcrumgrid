# -*- coding: utf-8 -*-
import os, re, json, glob, html
ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CONTENT = os.path.join(ROOT, 'content', 'blog')

CSP = "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com https://www.googleadservices.com https://www.google.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; img-src 'self' data: https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net; connect-src 'self' https://ipapi.co https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://analytics.google.com https://region1.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net; font-src 'self' https://fonts.gstatic.com; object-src 'none'; base-uri 'self'; form-action 'self' mailto:; frame-src https://td.doubleclick.net"

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

MARK = '<span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 32 32" width="26" height="26" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="1" y="1" width="30" height="30" rx="7" stroke="url(#bg)" stroke-width="1.5"/><path d="M9 23V9h9M9 16h7" stroke="url(#bg)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="22.5" cy="22.5" r="2.6" fill="url(#bg)"/><defs><linearGradient id="bg" x1="2" y1="2" x2="30" y2="30" gradientUnits="userSpaceOnUse"><stop stop-color="#2156df"/><stop offset="1" stop-color="#1d47ba"/></linearGradient></defs></svg></span>'

FOOTER_EN = '''  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-brand">
        <a class="brand" href="/" aria-label="FulcrumGrid home">
          <span class="brand-mark" aria-hidden="true">
            <svg viewBox="0 0 32 32" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="1" y="1" width="30" height="30" rx="7" stroke="url(#bgf)" stroke-width="1.5"/>
              <path d="M9 23V9h9M9 16h7" stroke="url(#bgf)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="22.5" cy="22.5" r="2.6" fill="url(#bgf)"/>
              <defs><linearGradient id="bgf" x1="2" y1="2" x2="30" y2="30" gradientUnits="userSpaceOnUse"><stop stop-color="#5eead4"/><stop offset="1" stop-color="#6366f1"/></linearGradient></defs>
            </svg>
          </span>
          <span class="brand-name">Fulcrum<span class="brand-accent">Grid</span></span>
        </a>
        <p class="footer-tag">The operational backbone for modern teams.</p>
      </div>
      <div class="footer-cols">
        <div class="footer-col"><h3>Products</h3><a href="/products/">All products</a><a href="/products/command-center/">Command Center</a><a href="/products/collection/">Collection</a><a href="/products/hr-suite/">HR Suite</a><a href="/custom-apps/">Custom apps</a><a href="/products/coming-soon/">Coming soon</a></div>
        <div class="footer-col"><h3>Platform</h3><a href="/features/">Features</a><a href="/how-it-works/">How it works</a><a href="/pricing/">Pricing</a><a href="/blog/">Blog</a></div>
        <div class="footer-col"><h3>Company</h3><a href="/about/">About</a><a href="/faq/">FAQ</a><a href="/contact/">Contact</a><a href="mailto:contact@avenlorconsulting.com">Email us</a><a href="/privacy/">Privacy</a><a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting ↗</a></div>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; <span id="year">2026</span> FulcrumGrid. All rights reserved.</p>
      <p class="footer-domain">fulcrumgrid.com</p>
    </div>
  </footer>'''

FOOTER_AR = '''  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-brand">
        <a class="brand" href="/ar/" aria-label="FulcrumGrid الصفحة الرئيسية">
          <span class="brand-mark" aria-hidden="true">
            <svg viewBox="0 0 32 32" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="1" y="1" width="30" height="30" rx="7" stroke="url(#bgf)" stroke-width="1.5"/>
              <path d="M9 23V9h9M9 16h7" stroke="url(#bgf)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="22.5" cy="22.5" r="2.6" fill="url(#bgf)"/>
              <defs><linearGradient id="bgf" x1="2" y1="2" x2="30" y2="30" gradientUnits="userSpaceOnUse"><stop stop-color="#5eead4"/><stop offset="1" stop-color="#6366f1"/></linearGradient></defs>
            </svg>
          </span>
          <span class="brand-name" dir="ltr">Fulcrum<span class="brand-accent">Grid</span></span>
        </a>
        <p class="footer-tag">العمود الفقري التشغيلي للفرق الحديثة.</p>
      </div>
      <div class="footer-cols">
        <div class="footer-col"><h3>المنتجات</h3><a href="/ar/products/">كل المنتجات</a><a href="/ar/products/command-center/">مركز القيادة</a><a href="/ar/products/collection/">التحصيل</a><a href="/ar/products/hr-suite/">الموارد البشرية</a><a href="/ar/custom-apps/">تطبيقات مخصّصة</a><a href="/ar/products/coming-soon/">قريبًا</a></div>
        <div class="footer-col"><h3>المنصّة</h3><a href="/ar/features/">الميزات</a><a href="/ar/how-it-works/">كيف تعمل</a><a href="/ar/pricing/">الأسعار</a><a href="/ar/blog/">المدوّنة</a></div>
        <div class="footer-col"><h3>الشركة</h3><a href="/ar/about/">من نحن</a><a href="/ar/faq/">الأسئلة الشائعة</a><a href="/ar/contact/">اتصل بنا</a><a href="mailto:contact@avenlorconsulting.com">راسلنا</a><a href="/ar/privacy/">الخصوصية</a><a href="https://avenlorconsulting.com/ar/" target="_blank" rel="noopener">أفنلور للاستشارات ↗</a></div>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; <span id="year">2026</span> FulcrumGrid. جميع الحقوق محفوظة.</p>
      <p class="footer-domain" dir="ltr">fulcrumgrid.com</p>
    </div>
  </footer>'''

CAT = {
 'collection': dict(label_en='Collection', label_ar='التحصيل',
    color='var(--indigo-text)', acc='var(--indigo)', og='og-collection.png',
    ogalt_en='FulcrumGrid Collection — receivables and payments',
    ogalt_ar='التحصيل من FulcrumGrid — الذمم والمدفوعات',
    prod_en='/products/collection/', prod_ar='/ar/products/collection/',
    k_en='FulcrumGrid Collection', k_ar='التحصيل من FulcrumGrid',
    explore_en='Explore Collection', explore_ar='استكشف التحصيل'),
 'hr': dict(label_en='HR', label_ar='الموارد البشرية',
    color='var(--rose)', acc='var(--rose)', og='og-hr-suite.png',
    ogalt_en='FulcrumGrid HR Suite — people operations',
    ogalt_ar='الموارد البشرية من FulcrumGrid — عمليات الأفراد',
    prod_en='/products/hr-suite/', prod_ar='/ar/products/hr-suite/',
    k_en='FulcrumGrid HR Suite', k_ar='الموارد البشرية من FulcrumGrid',
    explore_en='Explore HR Suite', explore_ar='استكشف الموارد البشرية'),
 'operations': dict(label_en='Operations', label_ar='العمليات',
    color='var(--teal)', acc='var(--teal)', og='og-command-center.png',
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
    return '\n'.join('          <details class="faq-item"><summary>%s</summary><p>%s</p></details>'%(q,a) for q,a in faqs)

def faq_schema(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

def render(post, lang):
    en = lang=='en'
    c = CAT[post['cat']]
    slug = post['slug']
    base = '' if en else '/ar'
    home = '/' if en else '/ar/'
    blog = '/blog/' if en else '/ar/blog/'
    canon = 'https://fulcrumgrid.com%s/blog/%s/'%(base,slug)
    en_url = 'https://fulcrumgrid.com/blog/%s/'%slug
    ar_url = 'https://fulcrumgrid.com/ar/blog/%s/'%slug
    title = post['title_'+lang]; desc = post['desc_'+lang]; ogdesc = post['ogdesc_'+lang]
    faqs = post['faqs_'+lang]
    # schema blocks
    blogposting = {"@context":"https://schema.org","@type":"BlogPosting","headline":title,
      "description":ogdesc,"datePublished":post['date'],"dateModified":post['date'],
      "author":{"@type":"Organization","name":"FulcrumGrid","@id":"https://fulcrumgrid.com/#organization"},
      "publisher":{"@id":"https://fulcrumgrid.com/#organization"},
      "image":"https://fulcrumgrid.com/assets/og/"+c['og'],
      "mainEntityOfPage":{"@type":"WebPage","@id":canon},"inLanguage":lang}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":("Home" if en else "الرئيسية"),"item":"https://fulcrumgrid.com"+home},
      {"@type":"ListItem","position":2,"name":("Blog" if en else "المدوّنة"),"item":"https://fulcrumgrid.com"+blog},
      {"@type":"ListItem","position":3,"name":post['bc_'+lang],"item":canon}]}
    ld = '\n'.join('  <script type="application/ld+json">\n  %s\n  </script>'%json.dumps(o,ensure_ascii=False,indent=2).replace('\n','\n  ') for o in [blogposting,bc,faq_schema(faqs)])

    htmlopen = '<html lang="en">' if en else '<html lang="ar" dir="rtl">'
    fonts = 'Inter:wght@400;500;600;700;800' if en else 'Cairo:wght@400;500;600;700;800'
    fonts += '&family=Space+Grotesk:wght@500;600;700'
    arstyle = '' if en else '\n  <style>:root { --font-sans: \'Cairo\', system-ui, sans-serif; --font-display: \'Cairo\', system-ui, sans-serif; }</style>'
    oglocale = '' if en else '\n  <meta property="og:locale" content="ar_AR" />'
    skip = 'Skip to content' if en else 'تخطَّ إلى المحتوى'
    brandname = 'Fulcrum<span class="brand-accent">Grid</span>' if en else '<span dir="ltr">Fulcrum<span class="brand-accent">Grid</span></span>'
    aria_home = 'FulcrumGrid home' if en else 'FulcrumGrid الصفحة الرئيسية'
    navlabels = [('Products','/products/'),('Platform','/features/'),('Pricing','/pricing/'),('Blog','/blog/'),('About','/about/'),('Contact','/contact/')] if en else \
                [('المنتجات','/ar/products/'),('المنصّة','/ar/features/'),('الأسعار','/ar/pricing/'),('المدوّنة','/ar/blog/'),('من نحن','/ar/about/'),('اتصل بنا','/ar/contact/')]
    def nav(mobile=False):
        out=[]
        for lbl,href in navlabels:
            active=' class="active" aria-current="page"' if lbl in ('Blog','المدوّنة') else ''
            out.append('        <a href="%s"%s>%s</a>'%(href,active,lbl))
        return '\n'.join(out)
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    primary_label = 'Primary' if en else 'التنقّل الرئيسي'
    lang_label = 'Language' if en else 'اللغة'
    menu_label = 'Toggle menu' if en else 'فتح القائمة'
    bc_label = 'Breadcrumb' if en else 'مسار التنقّل'
    faq_h = 'Frequently asked questions' if en else 'الأسئلة الشائعة'
    back = ('<span aria-hidden="true">←</span> Back to the blog' if en else '<span aria-hidden="true">→</span> العودة إلى المدوّنة')
    langswitch = ('        <a href="%s/blog/%s/"%s hreflang="en" lang="en">EN</a>\n        <a href="%s/ar/blog/%s/"%s hreflang="ar" lang="ar">ع</a>'
        % ('', slug, (' class="active" aria-current="page"' if en else ''), '', slug, ('' if en else ' class="active" aria-current="page"')))

    body_inner = post['body_'+lang].strip()
    related = post['related_'+lang].strip()
    cta = '''          <div class="article-cta" style="--cta-acc:%s">
            <span class="k">%s</span>
            <h3>%s</h3>
            <p>%s</p>
            <a class="btn btn-primary" href="%s">%s</a>
          </div>''' % (c['acc'], (c['k_'+lang]), post['cta_h_'+lang], post['cta_p_'+lang],
                       (c['prod_'+lang]), (c['explore_'+lang]))

    html = '''<!DOCTYPE html>
%(htmlopen)s
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Content-Security-Policy" content="%(csp)s" />

  %(ga)s

  <title>%(title)s — FulcrumGrid</title>
  <meta name="description" content="%(desc)s" />
  <meta name="theme-color" content="#0b1020" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="%(title)s" />
  <meta property="og:description" content="%(ogdesc)s" />
  <meta property="og:url" content="%(canon)s" />
  <meta property="og:site_name" content="FulcrumGrid" />%(oglocale)s
  <meta property="article:published_time" content="%(date)s" />
  <meta property="og:image" content="https://fulcrumgrid.com/assets/og/%(og)s" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:type" content="image/png" />
  <meta property="og:image:alt" content="%(ogalt)s" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="https://fulcrumgrid.com/assets/og/%(og)s" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/icon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/icon-16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/icon-180.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="canonical" href="%(canon)s" />
  <link rel="alternate" hreflang="en" href="%(en_url)s" />
  <link rel="alternate" hreflang="ar" href="%(ar_url)s" />
  <link rel="alternate" hreflang="x-default" href="%(en_url)s" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=%(fonts)s&display=swap" />
  <link href="https://fonts.googleapis.com/css2?family=%(fonts)s&display=swap" rel="stylesheet" media="print" onload="this.media='all'" />
  <noscript><link href="https://fonts.googleapis.com/css2?family=%(fonts)s&display=swap" rel="stylesheet" /></noscript>
  <link rel="stylesheet" href="/assets/css/fg.css" />%(arstyle)s
%(ld)s
</head>
<body class="fg product-page">
  <a class="skip-link" href="#main">%(skip)s</a>

    <header class="site-header" id="top">
    <div class="header-inner">
      <a class="brand" href="%(home)s" aria-label="%(aria_home)s">
        %(mark)s
        <span class="brand-name">%(brandname)s</span>
      </a>
      <nav class="site-nav" aria-label="%(primary_label)s">
%(nav)s
      </nav>
      <div class="header-cta">
        <div class="lang-switch" role="group" aria-label="%(lang_label)s">
%(langswitch)s
        </div>
        <a class="btn btn-primary" href="%(contact)s">%(demo)s</a>
      </div>
      <button class="nav-toggle" aria-label="%(menu_label)s" aria-expanded="false" aria-controls="mobile-menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="mobile-menu" id="mobile-menu" hidden>
%(nav)s
      <a class="btn btn-primary" href="%(contact)s">%(demo)s</a>
      <div class="lang-switch" role="group" aria-label="%(lang_label)s">
%(langswitch)s
      </div>
    </div>
  </header>

  <main id="main">
    <div class="container">
      <nav class="breadcrumb" aria-label="%(bc_label)s">
        <a href="%(home)s">%(home_label)s</a><span>/</span><a href="%(blog)s">%(blog_label)s</a><span>/</span><span class="current">%(bc_current)s</span>
      </nav>
    </div>

    <article class="section" style="padding-top:22px">
      <div class="container">
        <div class="article article-header">
          <span class="post-cat" style="color:%(catcolor)s">%(catlabel)s</span>
          <h1>%(title_html)s</h1>
          <div class="post-meta"><time datetime="%(date)s">%(metadate)s</time><span class="read">%(read)s</span></div>
        </div>

        <div class="article article-body">
%(body)s

          <h2>%(faq_h)s</h2>
%(faq_details)s

          <hr />
          %(related)s

%(cta)s
        </div>

        <div class="article-foot">
          <a class="back-link" href="%(blog)s">%(back)s</a>
        </div>
      </div>
    </article>
  </main>

%(footer)s

  <script src="/assets/js/main.js" defer></script>
  <script src="/assets/js/fg.js" defer></script>
  <script src="/assets/js/consent.js" defer></script>
</body>
</html>
''' % dict(
      htmlopen=htmlopen, csp=CSP, ga=GA, title=esc(title), desc=esc(desc), ogdesc=esc(ogdesc),
      canon=canon, en_url=en_url, ar_url=ar_url, oglocale=oglocale, date=post['date'],
      og=c['og'], ogalt=(c['ogalt_'+lang]), fonts=fonts, arstyle=arstyle, ld=ld,
      skip=skip, home=home, aria_home=aria_home, mark=MARK, brandname=brandname,
      primary_label=primary_label, nav=nav(), langswitch=langswitch,
      contact=('/contact/' if en else '/ar/contact/'), demo=demo, lang_label=lang_label,
      menu_label=menu_label, bc_label=bc_label, blog=blog,
      home_label=('Home' if en else 'الرئيسية'),
      blog_label=('Blog' if en else 'المدوّنة'),
      bc_current=post['bc_'+lang], catcolor=c['color'], catlabel=(c['label_'+lang]),
      title_html=esc(title), metadate=post['metadate_'+lang], read=post['read_'+lang],
      body=body_inner, faq_h=faq_h, faq_details=faq_details(faqs), related=related, cta=cta,
      back=back, footer=(FOOTER_EN if en else FOOTER_AR))
    return html

def is_legacy(p):
    return bool(p.get('legacy'))

def write_posts():
    # Only render pages the build owns (non-legacy). Legacy posts are
    # catalogued for the index/sitemap but their HTML is left untouched.
    for p in POSTS:
        if is_legacy(p):
            continue
        for lang in ('en','ar'):
            d = os.path.join(ROOT, ('' if lang=='en' else 'ar/')+'blog/%s'%p['slug'])
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(render(p,lang))
            print('wrote', d+'/index.html')

def card(p, lang):
    c = CAT[p['cat']]
    base = '/blog/' if lang=='en' else '/ar/blog/'
    return '''          <article class="post-card" data-cat="%s">
            <span class="post-cat">%s</span>
            <h2><a href="%s%s/">%s</a></h2>
            <p>%s</p>
            <div class="post-meta"><time datetime="%s">%s</time><span class="read">%s</span></div>
          </article>''' % (p['cat'], c['label_'+lang], base, p['slug'], esc(p['title_'+lang]),
                           esc(p['card_'+lang]), p['date'], p['cardtime_'+lang], p['read_'+lang])

def schema_entry(p, lang):
    url = 'https://fulcrumgrid.com/%sblog/%s/' % ('' if lang=='en' else 'ar/', p['slug'])
    return '      {"@type": "BlogPosting", "headline": %s, "url": "%s", "datePublished": "%s"}' % (
        json.dumps(p['title_'+lang], ensure_ascii=False), url, p['date'])

def ensure_index(lang):
    """Idempotently make sure every catalogued post has a card + schema entry
    in the blog index. Posts already present are left exactly as-is, so a
    fully-catalogued index produces no diff; a new post is inserted newest-first."""
    f = os.path.join(ROOT, ('' if lang=='en' else 'ar/')+'blog/index.html')
    s = open(f,encoding='utf-8').read()
    changed = False
    base = '/blog/' if lang=='en' else '/ar/blog/'
    # iterate oldest-first so successive top-inserts leave newest on top
    for p in reversed(POSTS):
        marker = '<a href="%s%s/">' % (base, p['slug'])
        if marker in s:
            continue
        s = s.replace('        <div class="post-grid">\n',
                      '        <div class="post-grid">\n'+card(p,lang)+'\n', 1)
        s = s.replace('    "blogPost": [\n',
                      '    "blogPost": [\n'+schema_entry(p,lang)+',\n', 1)
        changed = True
    if changed:
        open(f,'w',encoding='utf-8').write(s)
        print('updated index', f)
    return changed

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
    ensure_index('en'); ensure_index('ar')
    ensure_sitemap(); ensure_llms()

if __name__ == '__main__':
    build_blog()
