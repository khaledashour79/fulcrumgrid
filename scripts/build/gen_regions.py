# -*- coding: utf-8 -*-
"""Region pages generator.

Builds the /regions/ hub and one page per region (EN + AR), modelled on the
static product pages (body class `fg product-page`). Region-specific payroll
and compliance detail lives here so the pricing pages stay region-generic.

Idempotent: with content unchanged it reproduces the committed HTML, so it is
safe to run on every deploy (wired into scripts/build/build.py).
"""
import os

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

CSP = ('<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; '
       'script-src \'self\' \'unsafe-inline\' https://www.googletagmanager.com https://www.google-analytics.com https://www.googleadservices.com https://www.google.com; '
       'style-src \'self\' \'unsafe-inline\' https://fonts.googleapis.com; '
       'img-src \'self\' data: https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net; '
       'connect-src \'self\' https://ipapi.co https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://analytics.google.com https://region1.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net; '
       'font-src \'self\' https://fonts.gstatic.com; object-src \'none\'; base-uri \'self\'; form-action \'self\' mailto:; frame-src https://td.doubleclick.net" />')

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

MARK = ('<span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 32 32" width="26" height="26" fill="none" xmlns="http://www.w3.org/2000/svg">'
        '<rect x="1" y="1" width="30" height="30" rx="7" stroke="url(#bg)" stroke-width="1.5"/>'
        '<path d="M9 23V9h9M9 16h7" stroke="url(#bg)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="22.5" cy="22.5" r="2.6" fill="url(#bg)"/>'
        '<defs><linearGradient id="bg" x1="2" y1="2" x2="30" y2="30" gradientUnits="userSpaceOnUse"><stop stop-color="#2156df"/><stop offset="1" stop-color="#1d47ba"/></linearGradient></defs></svg></span>')

MARKF = ('<span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 32 32" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg">'
         '<rect x="1" y="1" width="30" height="30" rx="7" stroke="url(#bgf)" stroke-width="1.5"/>'
         '<path d="M9 23V9h9M9 16h7" stroke="url(#bgf)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
         '<circle cx="22.5" cy="22.5" r="2.6" fill="url(#bgf)"/>'
         '<defs><linearGradient id="bgf" x1="2" y1="2" x2="30" y2="30" gradientUnits="userSpaceOnUse"><stop stop-color="#5eead4"/><stop offset="1" stop-color="#6366f1"/></linearGradient></defs></svg></span>')

NAV = [('/products/', 'Products', 'المنتجات'), ('/features/', 'Platform', 'المنصّة'),
       ('/pricing/', 'Pricing', 'الأسعار'), ('/blog/', 'Blog', 'المدوّنة'),
       ('/about/', 'About', 'من نحن'), ('/contact/', 'Contact', 'اتصل بنا')]

# A neutral shield-check icon used for every compliance feature.
SHIELD = ('<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" '
          'stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>')
GLOBE = ('<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" '
         'stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18z"/></svg>')

FOOTER_COLS_EN = ('<div class="footer-col"><h3>Products</h3><a href="/products/">All products</a><a href="/products/command-center/">Command Center</a><a href="/products/collection/">Collection</a><a href="/products/hr-suite/">HR Suite</a><a href="/custom-apps/">Custom apps</a><a href="/products/coming-soon/">Coming soon</a></div>'
                  '<div class="footer-col"><h3>Platform</h3><a href="/features/">Features</a><a href="/how-it-works/">How it works</a><a href="/pricing/">Pricing</a><a href="/regions/">Regions</a><a href="/blog/">Blog</a></div>'
                  '<div class="footer-col"><h3>Company</h3><a href="/about/">About</a><a href="/faq/">FAQ</a><a href="/contact/">Contact</a><a href="mailto:contact@avenlorconsulting.com">Email us</a><a href="/privacy/">Privacy</a><a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting ↗</a></div>')

FOOTER_COLS_AR = ('<div class="footer-col"><h3>المنتجات</h3><a href="/ar/products/">كل المنتجات</a><a href="/ar/products/command-center/">مركز القيادة</a><a href="/ar/products/collection/">التحصيل</a><a href="/ar/products/hr-suite/">الموارد البشرية</a><a href="/ar/custom-apps/">تطبيقات مخصّصة</a><a href="/ar/products/coming-soon/">قريبًا</a></div>'
                  '<div class="footer-col"><h3>المنصّة</h3><a href="/ar/features/">الميزات</a><a href="/ar/how-it-works/">كيف تعمل</a><a href="/ar/pricing/">الأسعار</a><a href="/ar/regions/">المناطق</a><a href="/ar/blog/">المدوّنة</a></div>'
                  '<div class="footer-col"><h3>الشركة</h3><a href="/ar/about/">من نحن</a><a href="/ar/faq/">الأسئلة الشائعة</a><a href="/ar/contact/">اتصل بنا</a><a href="mailto:contact@avenlorconsulting.com">راسلنا</a><a href="/ar/privacy/">الخصوصية</a><a href="https://avenlorconsulting.com/ar/" target="_blank" rel="noopener">أفنلور للاستشارات ↗</a></div>')

# ── Region content ───────────────────────────────────────────────────────────
REGIONS = {
  'saudi-arabia': {
    'en_name': 'Saudi Arabia', 'ar_name': 'المملكة العربية السعودية',
    'tag_en': 'Saudi Arabia · KSA', 'tag_ar': 'المملكة العربية السعودية · السعودية',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Saudi Arabia',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للسعودية',
    'lead_en': "HR Suite ships with Saudi payroll and compliance built in — WPS wage files, GOSI, end-of-service, Nitaqat and Saudization, with Arabic throughout. Run your Saudi workforce by the book, without bolt-ons.",
    'lead_ar': "تأتي منظومة الموارد البشرية بالرواتب والامتثال السعودي جاهزَين — ملفات حماية الأجور (WPS)، والتأمينات الاجتماعية (GOSI)، ونهاية الخدمة، ونطاقات والسعودة، مع دعم العربية بالكامل. أدِر قوتك العاملة في السعودية وفق النظام، دون إضافات.",
    'desc_en': "HR Suite for Saudi Arabia — WPS wage-protection files, GOSI, end-of-service (EOSB), Nitaqat and Saudization, housing advance, and Arabic-first payroll and HR.",
    'desc_ar': "منظومة الموارد البشرية للسعودية — ملفات حماية الأجور (WPS)، والتأمينات (GOSI)، ونهاية الخدمة، ونطاقات والسعودة، وسلفة السكن، ورواتب وموارد بشرية بالعربية أولًا.",
    'features': [
      ("Payroll + WPS wage files", "الرواتب + ملفات حماية الأجور (WPS)",
       "Run compliant pay runs and export the Wage Protection System (WPS) bank file in the mandated format, so salaries clear through the right channels and on-time payment is on record.",
       "شغّل دورات رواتب متوافقة وصدّر ملف نظام حماية الأجور (WPS) بالصيغة المعتمدة، لتُصرف الرواتب عبر القنوات الصحيحة وتُسجَّل المدفوعات في وقتها."),
      ("GOSI contributions", "اشتراكات التأمينات (GOSI)",
       "GOSI (General Organization for Social Insurance) contributions are calculated automatically for Saudi and non-Saudi employees and wired straight into every pay run.",
       "تُحتسب اشتراكات التأمينات الاجتماعية (GOSI) تلقائيًا للموظفين السعوديين وغير السعوديين، وتُربط مباشرةً بكل دورة رواتب."),
      ("End-of-service (EOSB)", "نهاية الخدمة (EOSB)",
       "End-of-service benefits accrue and settle in line with the Saudi Labor Law, with resignation and termination cases handled distinctly.",
       "تُستحق مكافأة نهاية الخدمة وتُسوّى بما يتوافق مع نظام العمل السعودي، مع معالجة منفصلة لحالتَي الاستقالة وإنهاء الخدمة."),
      ("Nitaqat &amp; Saudization", "نطاقات والسعودة",
       "Track your Saudization ratio and Nitaqat band in the analytics dashboard, so you know where you stand before it becomes a compliance issue.",
       "تابِع نسبة السعودة ونطاقك في نطاقات ضمن لوحة التحليلات، لتعرف موقفك قبل أن يتحوّل إلى مسألة امتثال."),
      ("Housing advance", "سلفة السكن",
       "Interest-free housing advances with structured repayment, matching the way Saudi employment packages are commonly built.",
       "سلف سكن بدون فائدة مع سداد منظّم، بما يوافق طريقة بناء حزم التوظيف الشائعة في السعودية."),
      ("Arabic &amp; documents", "العربية والمستندات",
       "Arabic-first, right-to-left interface throughout, bilingual HR letters and contracts, and Iqama and permit expiry tracking so nothing lapses.",
       "واجهة بالعربية أولًا ومن اليمين إلى اليسار بالكامل، وخطابات وعقود ثنائية اللغة، وتتبّع انتهاء الإقامة والتصاريح حتى لا يفوت شيء."),
    ],
    'cta_h_en': 'Run Saudi HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في السعودية كما ينبغي',
    'cta_p_en': "See HR Suite handle Saudi payroll, GOSI, and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب والتأمينات ونهاية الخدمة في السعودية لفريقك.",
  },
}

def head(lang, path, title, desc):
    en = lang == 'en'
    base = '' if en else '/ar'
    canon = 'https://fulcrumgrid.com%s%s' % (base, path)
    en_url = 'https://fulcrumgrid.com%s' % path
    ar_url = 'https://fulcrumgrid.com/ar%s' % path
    fonts = ('Inter:wght@400;500;600;700;800' if en else 'Cairo:wght@400;500;600;700;800') + '&family=Space+Grotesk:wght@500;600;700'
    og = 'https://fulcrumgrid.com/assets/og/og-hr-suite%s.png' % ('' if en else '-ar')
    htmlopen = '<html lang="en">' if en else '<html lang="ar" dir="rtl">'
    return f'''<!DOCTYPE html>
{htmlopen}
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  {CSP}

  {GA}

  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#f0f2ed" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:site_name" content="FulcrumGrid" />
  <meta property="og:locale" content="{'en_US' if en else 'ar_AR'}" />
  <meta property="og:image" content="{og}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="{og}" />
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/icon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/icon-16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/icon-180.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="canonical" href="{canon}" />
  <link rel="alternate" hreflang="en" href="{en_url}" />
  <link rel="alternate" hreflang="ar" href="{ar_url}" />
  <link rel="alternate" hreflang="x-default" href="{en_url}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family={fonts}&display=swap" />
  <link href="https://fonts.googleapis.com/css2?family={fonts}&display=swap" rel="stylesheet" media="print" onload="this.media='all'" />
  <noscript><link href="https://fonts.googleapis.com/css2?family={fonts}&display=swap" rel="stylesheet" /></noscript>
  <link rel="stylesheet" href="/assets/css/fg.css" />
  <style>:root {{ --p-accent: var(--teal); }}</style>
</head>'''

def header(lang, path):
    en = lang == 'en'
    home = '/' if en else '/ar/'
    aria = 'FulcrumGrid home' if en else 'FulcrumGrid الصفحة الرئيسية'
    brand = '<span class="brand-name">Fulcrum<span class="brand-accent">Grid</span></span>' if en else '<span class="brand-name" dir="ltr">Fulcrum<span class="brand-accent">Grid</span></span>'
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    b = '' if en else '/ar'
    items = '\n'.join('        <a href="%s%s">%s</a>' % (b, href, (e if en else a)) for href, e, a in NAV)
    en_href = path
    ar_href = '/ar' + path
    return f'''<body class="fg product-page">
  <a class="skip-link" href="#main">{'Skip to content' if en else 'تخطَّ إلى المحتوى'}</a>

  <header class="site-header" id="top">
    <div class="header-inner">
      <a class="brand" href="{home}" aria-label="{aria}">
        {MARK}
        {brand}
      </a>
      <nav class="site-nav" aria-label="Primary">
{items}
      </nav>
      <div class="header-cta">
        <div class="lang-switch" role="group" aria-label="Language">
          <a href="{en_href}"{' class="active" aria-current="page"' if en else ''} hreflang="en" lang="en">EN</a>
          <a href="{ar_href}"{'' if en else ' class="active" aria-current="page"'} hreflang="ar" lang="ar">ع</a>
        </div>
        <a class="btn btn-primary" href="{b}/contact/">{demo}</a>
      </div>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="mobile-menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="mobile-menu" id="mobile-menu" hidden>
{items}
      <a class="btn btn-primary" href="{b}/contact/">{demo}</a>
    </div>
  </header>'''

def footer(lang):
    en = lang == 'en'
    home = '/' if en else '/ar/'
    aria = 'FulcrumGrid home' if en else 'FulcrumGrid الصفحة الرئيسية'
    brand = '<span class="brand-name">Fulcrum<span class="brand-accent">Grid</span></span>' if en else '<span class="brand-name" dir="ltr">Fulcrum<span class="brand-accent">Grid</span></span>'
    tag = 'The operational backbone for modern teams.' if en else 'العمود الفقري التشغيلي للفرق الحديثة.'
    rights = 'All rights reserved.' if en else 'جميع الحقوق محفوظة.'
    cols = FOOTER_COLS_EN if en else FOOTER_COLS_AR
    return f'''  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-brand">
        <a class="brand" href="{home}" aria-label="{aria}">
          {MARKF}
          {brand}
        </a>
        <p class="footer-tag">{tag}</p>
      </div>
      <div class="footer-cols">{cols}</div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; <span id="year">2026</span> FulcrumGrid. {rights}</p>
      <p class="footer-domain" dir="ltr">fulcrumgrid.com</p>
    </div>
  </footer>

  <script src="/assets/js/main.js" defer></script>
  <script src="/assets/js/fg.js" defer></script>
  <script src="/assets/js/consent.js" defer></script>
</body>
</html>'''

def breadcrumb(lang, trail):
    # trail: list of (label, href|None); last item is current
    en = lang == 'en'
    sep = '<span>/</span>'
    parts = []
    for i, (label, href) in enumerate(trail):
        if href:
            parts.append('<a href="%s">%s</a>' % (href, label))
        else:
            parts.append('<span class="current">%s</span>' % label)
    return ('    <div class="container">\n      <nav class="breadcrumb" aria-label="Breadcrumb">\n        '
            + sep.join(parts) + '\n      </nav>\n    </div>')

def region_page(slug, lang):
    d = REGIONS[slug]
    en = lang == 'en'
    b = '' if en else '/ar'
    path = '/regions/%s/' % slug
    name = d['en_name'] if en else d['ar_name']
    title = ('%s — HR &amp; payroll for %s | FulcrumGrid' % ('HR Suite', name)) if en else ('الموارد البشرية والرواتب في %s | FulcrumGrid' % name)
    desc = d['desc_en'] if en else d['desc_ar']
    tag = d['tag_en'] if en else d['tag_ar']
    h1 = d['h1_en'] if en else d['h1_ar']
    h1g = d['h1_grad_en'] if en else d['h1_grad_ar']
    lead = d['lead_en'] if en else d['lead_ar']
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    see_hr = 'Explore HR Suite' if en else 'استكشف الموارد البشرية'
    see_price = 'See HR Suite pricing' if en else 'أسعار الموارد البشرية'
    whatsin_eye = 'Built in' if en else 'مضمّن'
    whatsin_h = ('Saudi compliance, out of the box' if en else 'امتثال سعودي جاهز') if slug == 'saudi-arabia' else (name)
    whatsin_p = ("The modules that make HR Suite work the way Saudi Arabia does — each part of the same platform, no separate tools." if en
                 else "الوحدات التي تجعل منظومة الموارد البشرية تعمل بالطريقة السعودية — كلّها جزء من المنصة نفسها، دون أدوات منفصلة.")
    feats = []
    for te, ta, be, ba in d['features']:
        feats.append(f'''          <div class="feature">
            <div class="feature-icon" aria-hidden="true">{SHIELD}</div>
            <h3>{te if en else ta}</h3>
            <p>{be if en else ba}</p>
          </div>''')
    feats_html = '\n'.join(feats)
    note = (f'Every module here is part of HR Suite — payroll, GOSI and end-of-service on the Enterprise plan, or added to any plan as a per-seat add-on. <a href="{b}/pricing/hr-suite/">See HR Suite pricing →</a>'
            if en else
            f'كل وحدة هنا جزء من منظومة الموارد البشرية — الرواتب والتأمينات ونهاية الخدمة في خطة المؤسسات، أو تُضاف إلى أي خطة كإضافة لكل مقعد. <a href="{b}/pricing/hr-suite/">أسعار الموارد البشرية ←</a>')
    cta_h = d['cta_h_en'] if en else d['cta_h_ar']
    cta_p = d['cta_p_en'] if en else d['cta_p_ar']
    bc = breadcrumb(lang, [('Home' if en else 'الرئيسية', b + '/'),
                           ('Regions' if en else 'المناطق', b + '/regions/'),
                           (name, None)])
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
          '{"@type":"ListItem","position":1,"name":"%s","item":"https://fulcrumgrid.com%s/"},'
          '{"@type":"ListItem","position":2,"name":"%s","item":"https://fulcrumgrid.com%s/regions/"},'
          '{"@type":"ListItem","position":3,"name":"%s","item":"https://fulcrumgrid.com%s%s"}]}</script>'
          % (('Home' if en else 'الرئيسية'), b, ('Regions' if en else 'المناطق'), b, name, b, path))
    body = f'''{header(lang, path)}

  <main id="main">
{bc}

    <section class="product-hero">
      <div class="container">
        <div class="product-hero-inner">
          <span class="product-hero-icon" aria-hidden="true">{SHIELD}</span>
          <p class="product-eyebrow"><span class="tag tag-live" style="padding:3px 10px">{tag}</span></p>
          <h1>{h1} <span class="p-grad">{h1g}</span></h1>
          <p class="lead">{lead}</p>
          <div class="product-hero-actions">
            <a class="btn btn-primary btn-lg" href="{b}/contact/">{demo}</a>
            <a class="btn btn-outline btn-lg" href="{b}/products/hr-suite/">{see_hr}</a>
            <a class="btn btn-outline btn-lg" href="{b}/pricing/hr-suite/">{see_price}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="sub-head">
          <p class="eyebrow">{whatsin_eye}</p>
          <h2>{whatsin_h}</h2>
          <p>{whatsin_p}</p>
        </div>
        <div class="feature-grid">
{feats_html}
        </div>
        <p class="price-note" style="margin-top:28px">{note}</p>
      </div>
    </section>

    <section class="section" id="contact">
      <div class="container">
        <div class="cta-panel">
          <div class="grid-bg grid-bg-soft" aria-hidden="true"></div>
          <div class="cta-content">
            <h2>{cta_h}</h2>
            <p>{cta_p}</p>
            <div class="hero-actions" style="justify-content:center">
              <a class="btn btn-primary btn-lg" href="{b}/contact/">{demo}</a>
              <a class="btn btn-outline btn-lg" href="mailto:contact@avenlorconsulting.com">{'Email us' if en else 'راسلنا'}</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{footer(lang)}'''
    return head(lang, path, title, desc) + '\n' + body + '\n'

def hub_page(lang):
    en = lang == 'en'
    b = '' if en else '/ar'
    path = '/regions/'
    title = ('Regions — HR &amp; payroll by country | FulcrumGrid' if en else 'المناطق — الموارد البشرية والرواتب حسب الدولة | FulcrumGrid')
    desc = ("FulcrumGrid HR Suite adapts to local payroll and compliance — statutory contributions, wage-protection files, end-of-service, and language, by region."
            if en else "تتكيّف منظومة الموارد البشرية من FulcrumGrid مع الرواتب والامتثال المحلي — الاشتراكات النظامية وملفات حماية الأجور ونهاية الخدمة واللغة، حسب المنطقة.")
    eye = 'Regions' if en else 'المناطق'
    h1 = 'Built for how your' if en else 'مصمّمة لطريقة'
    h1g = 'region runs' if en else 'عمل منطقتك'
    lead = ("HR Suite adapts to local payroll and compliance — statutory contributions, wage-protection files, end-of-service rules, and language. Choose your region."
            if en else "تتكيّف منظومة الموارد البشرية مع الرواتب والامتثال المحلي — الاشتراكات النظامية وملفات حماية الأجور وقواعد نهاية الخدمة واللغة. اختر منطقتك.")
    # region cards
    sa = REGIONS['saudi-arabia']
    sa_name = sa['en_name'] if en else sa['ar_name']
    sa_sub = ('WPS · GOSI · EOSB · Nitaqat' if en else 'WPS · التأمينات · نهاية الخدمة · نطاقات')
    arrow = '→' if en else '←'
    soon_title = 'More regions' if en else 'مناطق أخرى'
    soon_sub = 'UAE &amp; GCC — coming soon' if en else 'الإمارات والخليج — قريبًا'
    cards = f'''          <a class="cross-card" href="{b}/regions/saudi-arabia/" style="--cc: var(--teal)">
            <span class="ci" aria-hidden="true">{GLOBE}</span>
            <div><h3>{sa_name}</h3><p>{sa_sub}</p></div><span class="arrow" aria-hidden="true">{arrow}</span>
          </a>
          <div class="cross-card" style="--cc: var(--text-dim); opacity:.72; cursor:default">
            <span class="ci" aria-hidden="true">{GLOBE}</span>
            <div><h3>{soon_title}</h3><p>{soon_sub}</p></div>
          </div>'''
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    bc = breadcrumb(lang, [('Home' if en else 'الرئيسية', b + '/'), (eye, None)])
    cta_h = 'Not sure your region is covered?' if en else 'لست متأكدًا من تغطية منطقتك؟'
    cta_p = "Tell us where you operate and we'll show you how HR Suite fits." if en else 'أخبرنا أين تعمل وسنعرض لك كيف تناسبك منظومة الموارد البشرية.'
    body = f'''{header(lang, path)}

  <main id="main">
{bc}

    <section class="product-hero">
      <div class="container">
        <div class="product-hero-inner">
          <span class="product-hero-icon" aria-hidden="true">{GLOBE}</span>
          <p class="product-eyebrow"><span class="tag tag-live" style="padding:3px 10px">{eye}</span></p>
          <h1>{h1} <span class="p-grad">{h1g}</span></h1>
          <p class="lead">{lead}</p>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="cross-grid">
{cards}
        </div>
      </div>
    </section>

    <section class="section" id="contact">
      <div class="container">
        <div class="cta-panel">
          <div class="grid-bg grid-bg-soft" aria-hidden="true"></div>
          <div class="cta-content">
            <h2>{cta_h}</h2>
            <p>{cta_p}</p>
            <div class="hero-actions" style="justify-content:center">
              <a class="btn btn-primary btn-lg" href="{b}/contact/">{demo}</a>
              <a class="btn btn-outline btn-lg" href="{b}/products/hr-suite/">{'Explore HR Suite' if en else 'استكشف الموارد البشرية'}</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{footer(lang)}'''
    return head(lang, path, title, desc) + '\n' + body + '\n'

def write(relpath, content):
    p = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(content)
    print('wrote', relpath)

for lang in ('en', 'ar'):
    pref = '' if lang == 'en' else 'ar/'
    write(pref + 'regions/index.html', hub_page(lang))
    for slug in REGIONS:
        write(pref + 'regions/%s/index.html' % slug, region_page(slug, lang))
