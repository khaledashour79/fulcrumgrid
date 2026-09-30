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
       ('/pricing/', 'Pricing', 'الأسعار'), ('/regions/', 'Regions', 'المناطق'), ('/blog/', 'Blog', 'المدوّنة'),
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
    'hub_sub_en': 'WPS · gratuity · GOSI · Nitaqat', 'hub_sub_ar': 'WPS · نهاية الخدمة · التأمينات · نطاقات',
    'features': [
      ("Payroll + WPS wage files", "الرواتب + ملفات حماية الأجور (WPS)",
       "Run compliant pay runs and export the Wage Protection System (WPS) bank file in the mandated format, so salaries clear through the right channels and on-time payment is on record.",
       "شغّل دورات رواتب متوافقة وصدّر ملف نظام حماية الأجور (WPS) بالصيغة المعتمدة، لتُصرف الرواتب عبر القنوات الصحيحة وتُسجَّل المدفوعات في وقتها."),
      ("GOSI contributions", "اشتراكات التأمينات (GOSI)",
       "GOSI (General Organization for Social Insurance) contributions are calculated automatically for Saudi and non-Saudi employees and wired straight into every pay run.",
       "تُحتسب اشتراكات التأمينات الاجتماعية (GOSI) تلقائيًا للموظفين السعوديين وغير السعوديين، وتُربط مباشرةً بكل دورة رواتب."),
      ("End-of-service (EOSB)", "نهاية الخدمة (EOSB)",
       "End-of-service benefits computed to the Saudi Labor Law (art. 84) — half a month's wage per year for the first five years, a full month per year thereafter — with resignation and termination handled distinctly.",
       "تُحتسب مكافأة نهاية الخدمة وفق نظام العمل السعودي (المادة ٨٤) — نصف شهر عن كل سنة للسنوات الخمس الأولى، وشهر كامل عن كل سنة بعدها — مع معالجة منفصلة لحالتَي الاستقالة وإنهاء الخدمة."),
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
  'uae': {
    'en_name': 'UAE', 'ar_name': 'الإمارات',
    'tag_en': 'United Arab Emirates · UAE', 'tag_ar': 'الإمارات العربية المتحدة · UAE',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'the UAE',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للإمارات',
    'lead_en': "HR Suite runs your UAE workforce end to end — MOHRE-compliant payroll and WPS salary files, gratuity to Federal Decree-Law 33/2021, pension and Emiratization tracking, and Arabic throughout.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في الإمارات بالكامل — رواتب متوافقة مع وزارة الموارد البشرية وملفات حماية الأجور (WPS)، ونهاية خدمة وفق المرسوم بقانون اتحادي 33/2021، ومتابعة المعاشات والتوطين، مع دعم العربية بالكامل.",
    'desc_en': "HR Suite for the UAE — MOHRE payroll and WPS salary files, gratuity under Federal Decree-Law 33/2021, GPSSA pensions, Emiratization (Nafis) tracking, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية للإمارات — رواتب وزارة الموارد البشرية وملفات WPS، ونهاية الخدمة وفق المرسوم بقانون 33/2021، ومعاشات GPSSA، ومتابعة التوطين (نافس)، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'WPS · gratuity · GPSSA · Emiratization', 'hub_sub_ar': 'WPS · نهاية الخدمة · المعاشات · التوطين',
    'features': [
      ("Payroll + WPS salary files", "الرواتب + ملفات WPS",
       "Run MOHRE-compliant pay runs and export the Wage Protection System (WPS) SIF file, so salaries clear through approved agents and on-time payment is on record.",
       "شغّل دورات رواتب متوافقة مع وزارة الموارد البشرية وصدّر ملف نظام حماية الأجور (WPS/SIF)، لتُصرف الرواتب عبر الوكلاء المعتمدين وتُسجَّل المدفوعات في وقتها."),
      ("End-of-service gratuity", "مكافأة نهاية الخدمة",
       "Gratuity computed to Federal Decree-Law 33/2021 — 21 days' basic wage per year for the first five years, 30 days per year thereafter, capped at two years' wage.",
       "تُحتسب المكافأة وفق المرسوم بقانون اتحادي 33/2021 — ٢١ يومًا من الأجر الأساسي عن كل سنة للسنوات الخمس الأولى، و٣٠ يومًا عن كل سنة بعدها، بحدٍّ أقصى أجر سنتين."),
      ("Pensions &amp; GPSSA", "المعاشات و GPSSA",
       "Set up pension and social-security deductions for GPSSA-registered UAE and GCC nationals, applied automatically in every pay run.",
       "أعدّ استقطاعات المعاشات والتأمينات لمواطني الإمارات ودول الخليج المسجَّلين في الهيئة العامة للمعاشات (GPSSA)، وتُطبَّق تلقائيًا في كل دورة رواتب."),
      ("Emiratization tracking", "متابعة التوطين",
       "Track your Emiratization ratio (Nafis) in the analytics dashboard, so you can see where you stand against MOHRE targets before they become a penalty.",
       "تابِع نسبة التوطين (نافس) في لوحة التحليلات، لتعرف موقفك من مستهدفات وزارة الموارد البشرية قبل أن تتحوّل إلى غرامة."),
      ("Arabic &amp; documents", "العربية والمستندات",
       "Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and visa, Emirates ID and work-permit expiry tracking so nothing lapses.",
       "واجهة بالعربية أولًا ومن اليمين إلى اليسار، وعقود وخطابات ثنائية اللغة، وتتبّع انتهاء التأشيرة والهوية الإماراتية وتصريح العمل حتى لا يفوت شيء."),
    ],
    'cta_h_en': 'Run UAE HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في الإمارات كما ينبغي',
    'cta_p_en': "See HR Suite handle UAE payroll, WPS, and gratuity for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب و WPS ونهاية الخدمة في الإمارات لفريقك.",
  },
  'qatar': {
    'en_name': 'Qatar', 'ar_name': 'قطر',
    'tag_en': 'Qatar · QA', 'tag_ar': 'قطر · QA',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Qatar',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لقطر',
    'lead_en': "HR Suite runs your Qatar workforce end to end — WPS-compliant payroll, end-of-service under Labour Law No. 14 of 2004, GRSIA pensions and Qatarization tracking, with Arabic throughout.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في قطر بالكامل — رواتب متوافقة مع نظام حماية الأجور، ونهاية خدمة وفق قانون العمل رقم 14 لسنة 2004، ومعاشات التقاعد والتقطير، مع دعم العربية بالكامل.",
    'desc_en': "HR Suite for Qatar — WPS payroll, end-of-service gratuity under Labour Law No. 14 of 2004, GRSIA pensions, Qatarization tracking, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية لقطر — رواتب WPS، ونهاية الخدمة وفق قانون العمل رقم 14 لسنة 2004، ومعاشات التقاعد، ومتابعة التقطير، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'WPS · gratuity · pensions · Qatarization', 'hub_sub_ar': 'WPS · نهاية الخدمة · المعاشات · التقطير',
    'features': [
      ("Payroll + WPS", "الرواتب + WPS",
       "Run compliant pay runs and export the Wage Protection System (WPS) file, so salaries clear through the mandated channel and payment is on record.",
       "شغّل دورات رواتب متوافقة وصدّر ملف نظام حماية الأجور (WPS)، لتُصرف الرواتب عبر القناة المعتمدة وتُسجَّل المدفوعات."),
      ("End-of-service gratuity", "مكافأة نهاية الخدمة",
       "End-of-service computed to Labour Law No. 14 of 2004 (art. 54) — a minimum of three weeks' (21 days') basic wage per year of service, across all years.",
       "تُحتسب نهاية الخدمة وفق قانون العمل رقم 14 لسنة 2004 (المادة ٥٤) — بحدٍّ أدنى ثلاثة أسابيع (٢١ يومًا) من الأجر الأساسي عن كل سنة خدمة، لكل السنوات."),
      ("Pensions &amp; GRSIA", "المعاشات و GRSIA",
       "Set up pension and social-insurance deductions for Qatari nationals registered with GRSIA, applied automatically in every pay run.",
       "أعدّ استقطاعات المعاشات والتأمينات للمواطنين القطريين المسجَّلين في هيئة التقاعد والتأمينات الاجتماعية (GRSIA)، وتُطبَّق تلقائيًا في كل دورة رواتب."),
      ("Qatarization tracking", "متابعة التقطير",
       "Track your Qatarization ratio in the analytics dashboard, so you can see your national-workforce share at a glance.",
       "تابِع نسبة التقطير في لوحة التحليلات، لترى حصّة القوى العاملة الوطنية في لمحة."),
      ("Arabic &amp; documents", "العربية والمستندات",
       "Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and residence-permit and document expiry tracking.",
       "واجهة بالعربية أولًا ومن اليمين إلى اليسار، وعقود وخطابات ثنائية اللغة، وتتبّع انتهاء الإقامة والمستندات."),
    ],
    'cta_h_en': 'Run Qatar HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في قطر كما ينبغي',
    'cta_p_en': "See HR Suite handle Qatar payroll, WPS, and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب و WPS ونهاية الخدمة في قطر لفريقك.",
  },
  'kuwait': {
    'en_name': 'Kuwait', 'ar_name': 'الكويت',
    'tag_en': 'Kuwait · KW', 'tag_ar': 'الكويت · KW',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Kuwait',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للكويت',
    'lead_en': "HR Suite runs your Kuwait workforce end to end — WPS-compliant payroll, indemnity under Labour Law No. 6 of 2010, PIFSS social security and national-workforce tracking, with Arabic throughout.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في الكويت بالكامل — رواتب متوافقة مع نظام حماية الأجور، ومكافأة نهاية الخدمة وفق قانون العمل رقم 6 لسنة 2010، وتأمينات المؤسسة العامة، ومتابعة القوى العاملة الوطنية، مع دعم العربية بالكامل.",
    'desc_en': "HR Suite for Kuwait — WPS payroll, end-of-service indemnity under Labour Law No. 6 of 2010, PIFSS deductions, national-workforce tracking, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية للكويت — رواتب WPS، ومكافأة نهاية الخدمة وفق قانون العمل رقم 6 لسنة 2010، واستقطاعات التأمينات، ومتابعة القوى العاملة الوطنية، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'WPS · indemnity · PIFSS · Kuwaitization', 'hub_sub_ar': 'WPS · المكافأة · التأمينات · القوى الوطنية',
    'features': [
      ("Payroll + WPS", "الرواتب + WPS",
       "Run compliant pay runs and export the Wage Protection System (WPS) file, so salaries clear through the mandated channel and payment is on record.",
       "شغّل دورات رواتب متوافقة وصدّر ملف نظام حماية الأجور (WPS)، لتُصرف الرواتب عبر القناة المعتمدة وتُسجَّل المدفوعات."),
      ("End-of-service indemnity", "مكافأة نهاية الخدمة",
       "Indemnity computed to the Private Sector Labour Law No. 6 of 2010 (art. 51) — 15 days' wage per year for the first five years, a full month per year thereafter, capped at 1.5 years' wage, with a resignation scale.",
       "تُحتسب المكافأة وفق قانون العمل في القطاع الأهلي رقم 6 لسنة 2010 (المادة ٥١) — ١٥ يومًا عن كل سنة للسنوات الخمس الأولى، وشهر كامل عن كل سنة بعدها، بحدٍّ أقصى أجر سنة ونصف، مع تدرّج عند الاستقالة."),
      ("Social security &amp; PIFSS", "التأمينات و PIFSS",
       "Set up social-security deductions for Kuwaiti nationals registered with PIFSS, applied automatically in every pay run.",
       "أعدّ استقطاعات التأمينات للمواطنين الكويتيين المسجَّلين في المؤسسة العامة للتأمينات الاجتماعية (PIFSS)، وتُطبَّق تلقائيًا في كل دورة رواتب."),
      ("National-workforce tracking", "متابعة القوى العاملة الوطنية",
       "Track your national-workforce ratio in the analytics dashboard, so your Kuwaitization share is always visible.",
       "تابِع نسبة القوى العاملة الوطنية في لوحة التحليلات، لتبقى حصّة التكويت ظاهرة دائمًا."),
      ("Arabic &amp; documents", "العربية والمستندات",
       "Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and residence and permit expiry tracking.",
       "واجهة بالعربية أولًا ومن اليمين إلى اليسار، وعقود وخطابات ثنائية اللغة، وتتبّع انتهاء الإقامة والتصاريح."),
    ],
    'cta_h_en': 'Run Kuwait HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في الكويت كما ينبغي',
    'cta_p_en': "See HR Suite handle Kuwait payroll, WPS, and indemnity for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب و WPS ونهاية الخدمة في الكويت لفريقك.",
  },
  'bahrain': {
    'en_name': 'Bahrain', 'ar_name': 'البحرين',
    'tag_en': 'Bahrain · BH', 'tag_ar': 'البحرين · BH',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Bahrain',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للبحرين',
    'lead_en': "HR Suite runs your Bahrain workforce end to end — WPS-compliant payroll, leaving indemnity under Law No. 36 of 2012, SIO social insurance and national-workforce tracking, with Arabic throughout.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في البحرين بالكامل — رواتب متوافقة مع نظام حماية الأجور، ومكافأة نهاية الخدمة وفق قانون رقم 36 لسنة 2012، وتأمينات الهيئة العامة، ومتابعة القوى العاملة الوطنية، مع دعم العربية بالكامل.",
    'desc_en': "HR Suite for Bahrain — WPS payroll, leaving indemnity under Labour Law No. 36 of 2012, SIO social insurance, national-workforce tracking, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية للبحرين — رواتب WPS، ومكافأة نهاية الخدمة وفق قانون العمل رقم 36 لسنة 2012، وتأمينات SIO، ومتابعة القوى العاملة الوطنية، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'WPS · indemnity · SIO · Bahrainization', 'hub_sub_ar': 'WPS · المكافأة · التأمينات · القوى الوطنية',
    'features': [
      ("Payroll + WPS", "الرواتب + WPS",
       "Run compliant pay runs and export the Wage Protection System (WPS) file, so salaries clear through the mandated channel and payment is on record.",
       "شغّل دورات رواتب متوافقة وصدّر ملف نظام حماية الأجور (WPS)، لتُصرف الرواتب عبر القناة المعتمدة وتُسجَّل المدفوعات."),
      ("Leaving indemnity", "مكافأة نهاية الخدمة",
       "Leaving indemnity computed to the Private Sector Labour Law No. 36 of 2012 (art. 116) — 15 days' wage per year for the first three years, a full month per year thereafter. Nationals covered by SIO are handled separately.",
       "تُحتسب المكافأة وفق قانون العمل في القطاع الأهلي رقم 36 لسنة 2012 (المادة ١١٦) — ١٥ يومًا عن كل سنة للسنوات الثلاث الأولى، وشهر كامل عن كل سنة بعدها. ويُعامَل المواطنون المشمولون بالتأمينات (SIO) على حدة."),
      ("Social insurance &amp; SIO", "التأمينات و SIO",
       "Set up social-insurance deductions for Bahraini nationals registered with the Social Insurance Organisation (SIO), applied automatically in every pay run.",
       "أعدّ استقطاعات التأمينات للمواطنين البحرينيين المسجَّلين في الهيئة العامة للتأمين الاجتماعي (SIO)، وتُطبَّق تلقائيًا في كل دورة رواتب."),
      ("National-workforce tracking", "متابعة القوى العاملة الوطنية",
       "Track your national-workforce ratio in the analytics dashboard, so your Bahrainization share is always visible.",
       "تابِع نسبة القوى العاملة الوطنية في لوحة التحليلات، لتبقى حصّة البحرنة ظاهرة دائمًا."),
      ("Arabic &amp; documents", "العربية والمستندات",
       "Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and CPR and permit expiry tracking.",
       "واجهة بالعربية أولًا ومن اليمين إلى اليسار، وعقود وخطابات ثنائية اللغة، وتتبّع انتهاء البطاقة الذكية والتصاريح."),
    ],
    'cta_h_en': 'Run Bahrain HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في البحرين كما ينبغي',
    'cta_p_en': "See HR Suite handle Bahrain payroll, WPS, and indemnity for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب و WPS ونهاية الخدمة في البحرين لفريقك.",
  },
  'oman': {
    'en_name': 'Oman', 'ar_name': 'عُمان',
    'tag_en': 'Oman · OM', 'tag_ar': 'عُمان · OM',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Oman',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لعُمان',
    'lead_en': "HR Suite runs your Oman workforce end to end — WPS-compliant payroll, end-of-service gratuity, social protection and Omanization tracking, with Arabic throughout — and it follows the Social Protection Law reform as it phases in.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في عُمان بالكامل — رواتب متوافقة مع نظام حماية الأجور، ومكافأة نهاية الخدمة، والحماية الاجتماعية ومتابعة التعمين، مع دعم العربية بالكامل — وتواكب إصلاح قانون الحماية الاجتماعية أثناء تطبيقه التدريجي.",
    'desc_en': "HR Suite for Oman — WPS payroll, end-of-service gratuity, PASI / Social Protection Fund, Omanization tracking, and Arabic-first HR, aligned with the Social Protection Law (Royal Decree 52/2023).",
    'desc_ar': "منظومة الموارد البشرية لعُمان — رواتب WPS، ومكافأة نهاية الخدمة، وصندوق الحماية الاجتماعية، ومتابعة التعمين، وموارد بشرية بالعربية أولًا، بما يتوافق مع قانون الحماية الاجتماعية (مرسوم سلطاني 52/2023).",
    'hub_sub_en': 'WPS · gratuity · social protection · Omanization', 'hub_sub_ar': 'WPS · نهاية الخدمة · الحماية الاجتماعية · التعمين',
    'features': [
      ("Payroll + WPS", "الرواتب + WPS",
       "Run compliant pay runs and export the Wage Protection System (WPS) file, so salaries clear through the mandated channel and payment is on record.",
       "شغّل دورات رواتب متوافقة وصدّر ملف نظام حماية الأجور (WPS)، لتُصرف الرواتب عبر القناة المعتمدة وتُسجَّل المدفوعات."),
      ("End-of-service gratuity", "مكافأة نهاية الخدمة",
       "End-of-service gratuity of 15 days' wage per year for the first three years and a full month per year thereafter — with the Social Protection Law (Royal Decree 52/2023) savings scheme supported as it phases in.",
       "مكافأة نهاية خدمة بواقع ١٥ يومًا عن كل سنة للسنوات الثلاث الأولى، وشهر كامل عن كل سنة بعدها — مع دعم نظام الادّخار وفق قانون الحماية الاجتماعية (مرسوم سلطاني 52/2023) أثناء تطبيقه التدريجي."),
      ("Social protection", "الحماية الاجتماعية",
       "Set up social-protection and pension deductions for Omani nationals, applied automatically in every pay run and ready for the new contributory savings scheme.",
       "أعدّ استقطاعات الحماية الاجتماعية والمعاشات للمواطنين العُمانيين، وتُطبَّق تلقائيًا في كل دورة رواتب، وجاهزة لنظام الادّخار التشاركي الجديد."),
      ("Omanization tracking", "متابعة التعمين",
       "Track your Omanization ratio in the analytics dashboard, so your national-workforce share is always visible.",
       "تابِع نسبة التعمين في لوحة التحليلات، لتبقى حصّة القوى العاملة الوطنية ظاهرة دائمًا."),
      ("Arabic &amp; documents", "العربية والمستندات",
       "Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and resident-card and permit expiry tracking.",
       "واجهة بالعربية أولًا ومن اليمين إلى اليسار، وعقود وخطابات ثنائية اللغة، وتتبّع انتهاء البطاقة والتصاريح."),
    ],
    'cta_h_en': 'Run Oman HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في عُمان كما ينبغي',
    'cta_p_en': "See HR Suite handle Oman payroll, WPS, and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب و WPS ونهاية الخدمة في عُمان لفريقك.",
  },
  'uk': {
    'en_name': 'United Kingdom', 'ar_name': 'المملكة المتحدة',
    'tag_en': 'United Kingdom · UK', 'tag_ar': 'المملكة المتحدة · UK',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'the UK',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للمملكة المتحدة',
    'lead_en': "HR Suite runs your UK workforce end to end — PAYE and National Insurance on a configurable payroll, P60 and P45 statements, NINO validation, pensions, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في المملكة المتحدة بالكامل — ضريبة PAYE والتأمين الوطني على نظام رواتب قابل للتهيئة، وكشوف P60 و P45، والتحقق من رقم التأمين الوطني، والمعاشات، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for the UK — PAYE and National Insurance deductions, P60 and P45 statements, NINO validation, workplace pensions, and full HR on one grid.",
    'desc_ar': "منظومة الموارد البشرية للمملكة المتحدة — استقطاعات PAYE والتأمين الوطني، وكشوف P60 و P45، والتحقق من رقم التأمين الوطني، ومعاشات العمل، وموارد بشرية كاملة على شبكة واحدة.",
    'hub_sub_en': 'PAYE · NI · P60/P45', 'hub_sub_ar': 'PAYE · التأمين الوطني · P60/P45',
    'features': [
      ("PAYE &amp; National Insurance", "PAYE والتأمين الوطني",
       "Pay runs with deductions classified as PAYE income tax (rest-of-UK and Scottish rates) and National Insurance, on a configurable engine that keeps payslips and reports aligned.",
       "دورات رواتب باستقطاعات مصنّفة كضريبة دخل PAYE (لبقية المملكة والمعدّلات الاسكتلندية) وتأمين وطني، على نظام قابل للتهيئة يبقي كشوف الرواتب والتقارير متطابقة."),
      ("P60 &amp; P45 statements", "كشوف P60 و P45",
       "Generate P60 (year-end) and P45 (leaver) statements from your finalized pay runs — statements from your own records, not the official HMRC form or an RTI submission.",
       "أنشئ كشوف P60 (نهاية السنة) و P45 (عند المغادرة) من دورات الرواتب المعتمدة — كشوف من سجلّاتك، وليست النموذج الرسمي لهيئة HMRC ولا تقديم RTI."),
      ("NINO validation", "التحقق من رقم التأمين الوطني",
       "National Insurance numbers are checksum-validated on entry, so employee records stay clean and payroll-ready.",
       "تُتحقَّق أرقام التأمين الوطني بخوارزمية تدقيق عند الإدخال، لتبقى سجلّات الموظفين نظيفة وجاهزة للرواتب."),
      ("Pensions &amp; deductions", "المعاشات والاستقطاعات",
       "Model workplace pension and other pre- and post-tax deductions on the same engine, with employer contributions tracked as company cost.",
       "أنشئ معاش العمل وغيره من الاستقطاعات قبل الضريبة وبعدها على النظام نفسه، مع تتبّع مساهمات صاحب العمل كتكلفة على الشركة."),
      ("Core HR &amp; self-service", "الموارد البشرية الأساسية والخدمة الذاتية",
       "Employee records, onboarding, time off, documents and employee self-service — the whole lifecycle on one grid.",
       "سجلّات الموظفين والتأهيل والإجازات والمستندات والخدمة الذاتية — دورة الحياة كاملة على شبكة واحدة."),
    ],
    'cta_h_en': 'Run UK HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في المملكة المتحدة كما ينبغي',
    'cta_p_en': "See HR Suite handle UK PAYE, National Insurance, and year-end for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير PAYE والتأمين الوطني ونهاية السنة في المملكة المتحدة لفريقك.",
  },
  'usa': {
    'en_name': 'United States', 'ar_name': 'الولايات المتحدة',
    'tag_en': 'United States · US', 'tag_ar': 'الولايات المتحدة · US',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'the US',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للولايات المتحدة',
    'lead_en': "HR Suite runs your US workforce end to end — configurable payroll with federal and state income tax, Social Security and Medicare, W-2 year-end statements, ACH pay files, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في الولايات المتحدة بالكامل — رواتب قابلة للتهيئة مع ضريبة الدخل الفيدرالية والولائية، والضمان الاجتماعي و Medicare، وكشوف W-2 لنهاية السنة، وملفات دفع ACH، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for the US — configurable payroll with federal/state income tax, Social Security and Medicare, W-2 year-end statements, ACH (NACHA) pay files, and full HR.",
    'desc_ar': "منظومة الموارد البشرية للولايات المتحدة — رواتب قابلة للتهيئة مع ضريبة الدخل الفيدرالية والولائية، والضمان الاجتماعي و Medicare، وكشوف W-2، وملفات دفع ACH، وموارد بشرية كاملة.",
    'hub_sub_en': 'Payroll · W-2 · ACH', 'hub_sub_ar': 'الرواتب · W-2 · ACH',
    'features': [
      ("Payroll + tax categories", "الرواتب + فئات الضريبة",
       "Configurable pay runs with deductions classified as federal income tax, state income tax, Social Security and Medicare, so every payslip and report lines up.",
       "دورات رواتب قابلة للتهيئة باستقطاعات مصنّفة كضريبة دخل فيدرالية وولائية، وضمان اجتماعي و Medicare، لتتطابق كل قسيمة راتب وتقرير."),
      ("W-2 year-end statements", "كشوف W-2 لنهاية السنة",
       "Generate W-2 statements for employees from your finalized pay runs at year-end — statements from your own records, not an IRS EFW2 e-file.",
       "أنشئ كشوف W-2 للموظفين من دورات الرواتب المعتمدة في نهاية السنة — كشوف من سجلّاتك، وليست تقديمًا إلكترونيًا EFW2 لمصلحة الضرائب."),
      ("ACH pay files", "ملفات دفع ACH",
       "Export an ACH (NACHA) file from a finalized pay run for upload to your bank, with account details validated on entry.",
       "صدّر ملف ACH (NACHA) من دورة رواتب معتمدة لرفعه إلى بنكك، مع التحقق من بيانات الحساب عند الإدخال."),
      ("Overtime — FLSA", "العمل الإضافي — FLSA",
       "Overtime to the Fair Labor Standards Act — 1.5× the regular rate for hours over 40 in a week — with state variants like California's daily 1.5× / 2× configurable.",
       "عمل إضافي وفق قانون معايير العمل العادلة (FLSA) — ١٫٥× من الأجر المعتاد للساعات التي تتجاوز ٤٠ أسبوعيًا — مع إمكانية تهيئة تنويعات الولايات مثل معدّل كاليفورنيا اليومي ١٫٥×/٢×."),
      ("Leave &amp; US holidays", "الإجازات والعطلات الأمريكية",
       "PTO and FMLA leave with the US federal holiday calendar — Juneteenth, Independence Day, Veterans Day and more — built in.",
       "إجازة مدفوعة (PTO) وإجازة FMLA مع تقويم العطلات الفيدرالية الأمريكية — Juneteenth ويوم الاستقلال ويوم المحاربين القدامى وغيرها — مدمجة."),
      ("Benefits &amp; deductions", "المزايا والاستقطاعات",
       "Model 401(k), benefits and other pre- and post-tax deductions on the same engine, with employer contributions tracked as company cost.",
       "أنشئ خطة 401(k) والمزايا وغيرها من الاستقطاعات قبل الضريبة وبعدها على النظام نفسه، مع تتبّع مساهمات صاحب العمل كتكلفة على الشركة."),
      ("Core HR &amp; self-service", "الموارد البشرية الأساسية والخدمة الذاتية",
       "Employee records, onboarding, time off, documents and employee self-service — the whole lifecycle on one grid.",
       "سجلّات الموظفين والتأهيل والإجازات والمستندات والخدمة الذاتية — دورة الحياة كاملة على شبكة واحدة."),
    ],
    'cta_h_en': 'Run US HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في الولايات المتحدة كما ينبغي',
    'cta_p_en': "See HR Suite handle US payroll, W-2, and ACH for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب و W-2 و ACH في الولايات المتحدة لفريقك.",
  },
  'europe': {
    'en_name': 'Europe', 'ar_name': 'أوروبا',
    'tag_en': 'Europe · EU', 'tag_ar': 'أوروبا · EU',
    'h1_en': 'FulcrumGrid, built for', 'h1_grad_en': 'Europe',
    'h1_ar': 'FulcrumGrid،', 'h1_grad_ar': 'مصمّمة لأوروبا',
    'lead_en': "The whole grid runs across Europe — HR Suite with SEPA payroll and GDPR-grade data privacy; Command Center with multi-currency, VAT-ready finance; and Collection with SEPA-friendly receivables. One grid across your entities.",
    'lead_ar': "الشبكة كاملة تعمل عبر أوروبا — HR Suite برواتب SEPA وخصوصية بيانات بمستوى GDPR؛ وCommand Center بمالية متعددة العملات وجاهزة لضريبة القيمة المضافة؛ وCollection بتحصيل متوافق مع SEPA. شبكة واحدة عبر كياناتك.",
    'desc_en': "FulcrumGrid across Europe — HR Suite, Command Center and Collection — with SEPA payroll, GDPR-grade data privacy and multi-currency, VAT-ready finance.",
    'desc_ar': "FulcrumGrid عبر أوروبا — HR Suite وCommand Center وCollection — برواتب SEPA وخصوصية بيانات بمستوى GDPR ومالية متعددة العملات جاهزة لضريبة القيمة المضافة.",
    'hub_sub_en': 'UK · Ireland · France · Germany · Spain · Italy · NL', 'hub_sub_ar': 'المملكة المتحدة · أيرلندا · فرنسا · ألمانيا · إسبانيا · إيطاليا · هولندا',
    'members': ['uk', 'ireland', 'france', 'germany', 'spain', 'italy', 'netherlands'],
    'served_en': 'Belgium · Portugal · Poland · Sweden · Denmark · Finland · Austria · Greece · and the rest of the EU / EEA',
    'served_ar': 'بلجيكا · البرتغال · بولندا · السويد · الدنمارك · فنلندا · النمسا · اليونان · وبقية الاتحاد الأوروبي والمنطقة الاقتصادية',
    'features': [
      ("SEPA payments", "مدفوعات SEPA",
       "Export a SEPA credit-transfer file from a finalized pay run for upload to your bank, with IBANs validated on entry.",
       "صدّر ملف تحويل SEPA من دورة رواتب معتمدة لرفعه إلى بنكك، مع التحقق من الآيبان عند الإدخال."),
      ("GDPR data-subject rights", "حقوق أصحاب البيانات (GDPR)",
       "Built-in subject-access export (everything held about a person, as JSON) and selective erasure-with-retention, so DSARs are a workflow — with DPO contact and retention policies included.",
       "تصدير حق الوصول للبيانات مدمج (كل ما يخصّ الشخص بصيغة JSON) ومحو انتقائي مع الاحتفاظ، لتصبح طلبات أصحاب البيانات إجراءً منظّمًا — مع بيانات مسؤول حماية البيانات وسياسات الاحتفاظ."),
      ("Configurable local deductions", "استقطاعات محلية قابلة للتهيئة",
       "Model each country's income tax and social contributions as configurable, classified deduction types, so payslips and reports stay consistent across entities.",
       "أنشئ ضريبة الدخل والمساهمات الاجتماعية لكل دولة كأنواع استقطاعات قابلة للتهيئة ومصنّفة، لتبقى كشوف الرواتب والتقارير متّسقة عبر الكيانات."),
      ("Documents &amp; e-sign", "المستندات والتوقيع الإلكتروني",
       "Contracts, letters and click-to-sign, with data-retention rules applied automatically.",
       "العقود والخطابات والتوقيع بنقرة، مع تطبيق قواعد الاحتفاظ بالبيانات تلقائيًا."),
      ("Core HR &amp; self-service", "الموارد البشرية الأساسية والخدمة الذاتية",
       "Employee records, onboarding, time off and self-service — the whole lifecycle on one grid.",
       "سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية — دورة الحياة كاملة على شبكة واحدة."),
    ],
    'cta_h_en': 'Run your European operation on one grid', 'cta_h_ar': 'أدِر عملياتك الأوروبية على شبكة واحدة',
    'cta_p_en': "Tell us where you operate and we'll show you the whole grid in action.",
    'cta_p_ar': "أخبرنا أين تعمل وسنعرض لك الشبكة كاملة وهي تعمل.",
  },
  'gcc': {
    'en_name': 'GCC', 'ar_name': 'دول الخليج',
    'tag_en': 'Gulf Cooperation Council · GCC', 'tag_ar': 'مجلس التعاون الخليجي · GCC',
    'h1_en': 'FulcrumGrid, built for', 'h1_grad_en': 'the Gulf',
    'h1_ar': 'FulcrumGrid،', 'h1_grad_ar': 'مصمّمة للخليج',
    'lead_en': "The whole grid runs in the Gulf — HR Suite with WPS payroll, end-of-service and Arabic throughout; Command Center with GCC-native finance, Tax and Zakat and multi-currency; and Collection for local receivables. Pick a country for the detail.",
    'lead_ar': "الشبكة كاملة تعمل في الخليج — HR Suite برواتب WPS ونهاية الخدمة ودعم العربية بالكامل؛ وCommand Center بمالية خليجية أصيلة والضريبة والزكاة وتعدّد العملات؛ وCollection للتحصيل المحلي. اختر دولة لعرض التفاصيل.",
    'desc_en': "FulcrumGrid across the GCC — HR Suite, Command Center and Collection — with WPS payroll, statutory end-of-service and Arabic, plus GCC-native finance and Tax and Zakat, per country.",
    'desc_ar': "FulcrumGrid عبر دول الخليج — HR Suite وCommand Center وCollection — برواتب WPS ونهاية خدمة نظامية ودعم العربية، ومالية خليجية أصيلة والضريبة والزكاة، لكل دولة.",
    'hub_sub_en': 'Saudi · UAE · Qatar · Kuwait · Bahrain · Oman', 'hub_sub_ar': 'السعودية · الإمارات · قطر · الكويت · البحرين · عُمان',
    'members': ['saudi-arabia', 'uae', 'qatar', 'kuwait', 'bahrain', 'oman'],
    'cta_h_en': 'Run your Gulf operation on one grid', 'cta_h_ar': 'أدِر عملياتك الخليجية على شبكة واحدة',
    'cta_p_en': "Tell us where you operate and we'll show you the whole grid in action.",
    'cta_p_ar': "أخبرنا أين تعمل وسنعرض لك الشبكة كاملة وهي تعمل.",
  },
  'middle-east': {
    'en_name': 'Middle East', 'ar_name': 'الشرق الأوسط',
    'tag_en': 'Middle East · MENA', 'tag_ar': 'الشرق الأوسط · MENA',
    'h1_en': 'FulcrumGrid, built for', 'h1_grad_en': 'the Middle East',
    'h1_ar': 'FulcrumGrid،', 'h1_grad_ar': 'مصمّمة للشرق الأوسط',
    'lead_en': "The whole grid runs across the Middle East — HR Suite with configurable local payroll and end-of-service; Command Center with Arabic-first finance and multi-currency reporting; and Collection for local receivables. Deepest in the Gulf, ready beyond it.",
    'lead_ar': "الشبكة كاملة تعمل عبر الشرق الأوسط — HR Suite برواتب محلية ونهاية خدمة قابلة للتهيئة؛ وCommand Center بمالية بالعربية أولًا وتقارير متعددة العملات؛ وCollection للتحصيل المحلي. الأعمق في الخليج، وجاهزة لما بعده.",
    'desc_en': "FulcrumGrid across the Middle East — HR Suite, Command Center and Collection — with configurable local payroll and end-of-service, Arabic-first finance and multi-currency.",
    'desc_ar': "FulcrumGrid عبر الشرق الأوسط — HR Suite وCommand Center وCollection — برواتب محلية ونهاية خدمة قابلة للتهيئة ومالية بالعربية أولًا وتعدّد العملات.",
    'hub_sub_en': 'Egypt · Jordan · Lebanon · Iraq · Palestine · Syria · Yemen', 'hub_sub_ar': 'مصر · الأردن · لبنان · العراق · فلسطين · سوريا · اليمن',
    'members': ['egypt', 'jordan', 'lebanon', 'iraq', 'palestine', 'syria', 'yemen'],
    'served_en': 'Morocco · Tunisia · Algeria · Libya · Sudan',
    'served_ar': 'المغرب · تونس · الجزائر · ليبيا · السودان',
    'features': [
      ("Configurable local payroll", "رواتب محلية قابلة للتهيئة",
       "Model each country's income tax and social contributions as configurable, classified deduction types — no country hard-coding required.",
       "أنشئ ضريبة الدخل والمساهمات الاجتماعية لكل دولة كأنواع استقطاعات قابلة للتهيئة ومصنّفة — دون ترميز خاص بكل دولة."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "The end-of-service engine is rule-based — days of wage per year, banded by service — so you configure local gratuity even without a built-in preset.",
       "محرّك نهاية الخدمة قائم على القواعد — أيام أجر عن كل سنة، مقسّمة حسب مدة الخدمة — فتُهيّئ المكافأة المحلية حتى دون إعداد جاهز."),
      ("Arabic-first &amp; multi-currency", "العربية أولًا وتعدّد العملات",
       "Arabic, right-to-left throughout, bilingual documents, and pay in local currency.",
       "العربية ومن اليمين إلى اليسار بالكامل، ومستندات ثنائية اللغة، والدفع بالعملة المحلية."),
      ("Core HR &amp; self-service", "الموارد البشرية الأساسية والخدمة الذاتية",
       "Employee records, onboarding, time off and self-service — the whole lifecycle on one grid.",
       "سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية — دورة الحياة كاملة على شبكة واحدة."),
    ],
    'cta_h_en': 'Run your Middle East operation on one grid', 'cta_h_ar': 'أدِر عملياتك في الشرق الأوسط على شبكة واحدة',
    'cta_p_en': "Tell us where you operate and we'll show you the whole grid in action.",
    'cta_p_ar': "أخبرنا أين تعمل وسنعرض لك الشبكة كاملة وهي تعمل.",
  },
  'egypt': {
    'en_name': 'Egypt', 'ar_name': 'مصر',
    'tag_en': 'Egypt · EG', 'tag_ar': 'مصر · EG',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Egypt',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لمصر',
    'lead_en': "HR Suite runs your Egypt workforce — configurable payroll with local income tax and social-insurance deductions, end-of-service on a rule-based engine, EGP pay, Arabic throughout, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في مصر — رواتب قابلة للتهيئة مع ضريبة الدخل المحلية واستقطاعات التأمينات، ونهاية خدمة على محرّك قائم على القواعد، ودفع بالجنيه المصري، ودعم العربية بالكامل، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Egypt — configurable payroll with local income tax and social insurance, rule-based end-of-service, EGP pay, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية لمصر — رواتب قابلة للتهيئة مع ضريبة الدخل المحلية والتأمينات، ونهاية خدمة قائمة على القواعد، ودفع بالجنيه المصري، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Payroll · EOSB · Arabic', 'hub_sub_ar': 'الرواتب · نهاية الخدمة · العربية',
    'features': [
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model Egyptian income tax and social-insurance contributions as configurable, classified deduction types, applied in every pay run.",
       "أنشئ ضريبة الدخل المصرية واستقطاعات التأمينات كأنواع استقطاعات قابلة للتهيئة ومصنّفة، تُطبَّق في كل دورة رواتب."),
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual, sick and maternity leave and the Egyptian public-holiday calendar, built in.",
       "الإجازة السنوية والمرضية وإجازة الأمومة النظامية وتقويم العطلات الرسمية المصرية، مدمجة."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "Configure end-of-service on the same rule-based engine — days of wage per year — so local gratuity fits without a hard-coded preset.",
       "هيّئ نهاية الخدمة على المحرّك نفسه القائم على القواعد — أيام أجر عن كل سنة — لتناسب المكافأة المحلية دون إعداد جاهز."),
      ("EGP pay &amp; documents", "الدفع بالجنيه والمستندات",
       "Pay in Egyptian pounds, with bilingual contracts and letters and document-expiry tracking.",
       "الدفع بالجنيه المصري، مع عقود وخطابات ثنائية اللغة وتتبّع انتهاء المستندات."),
      ("Arabic-first &amp; core HR", "العربية أولًا والموارد البشرية الأساسية",
       "Arabic, right-to-left throughout, plus employee records, onboarding, time off and self-service.",
       "العربية ومن اليمين إلى اليسار بالكامل، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Egypt HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في مصر كما ينبغي',
    'cta_p_en': "See HR Suite handle Egypt payroll and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب ونهاية الخدمة في مصر لفريقك.",
  },
  'jordan': {
    'en_name': 'Jordan', 'ar_name': 'الأردن',
    'tag_en': 'Jordan · JO', 'tag_ar': 'الأردن · JO',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Jordan',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للأردن',
    'lead_en': "HR Suite runs your Jordan workforce — configurable payroll with local income tax and Social Security Corporation deductions, end-of-service on a rule-based engine, JOD pay, Arabic throughout, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في الأردن — رواتب قابلة للتهيئة مع ضريبة الدخل المحلية واستقطاعات الضمان الاجتماعي، ونهاية خدمة على محرّك قائم على القواعد، ودفع بالدينار الأردني، ودعم العربية بالكامل، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Jordan — configurable payroll with local income tax and Social Security Corporation (SSC), rule-based end-of-service, JOD pay, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية للأردن — رواتب قابلة للتهيئة مع ضريبة الدخل المحلية والضمان الاجتماعي (SSC)، ونهاية خدمة قائمة على القواعد، ودفع بالدينار الأردني، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Payroll · SSC · Arabic', 'hub_sub_ar': 'الرواتب · الضمان · العربية',
    'features': [
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model Jordanian income tax and Social Security Corporation (SSC) contributions as configurable, classified deduction types, applied in every pay run.",
       "أنشئ ضريبة الدخل الأردنية واستقطاعات الضمان الاجتماعي (SSC) كأنواع استقطاعات قابلة للتهيئة ومصنّفة، تُطبَّق في كل دورة رواتب."),
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual, sick and maternity leave and the Jordanian public-holiday calendar, built in.",
       "الإجازة السنوية والمرضية وإجازة الأمومة النظامية وتقويم العطلات الرسمية الأردنية، مدمجة."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "Configure end-of-service on the same rule-based engine — days of wage per year — so local gratuity fits without a hard-coded preset.",
       "هيّئ نهاية الخدمة على المحرّك نفسه القائم على القواعد — أيام أجر عن كل سنة — لتناسب المكافأة المحلية دون إعداد جاهز."),
      ("JOD pay &amp; documents", "الدفع بالدينار والمستندات",
       "Pay in Jordanian dinars, with bilingual contracts and letters and document-expiry tracking.",
       "الدفع بالدينار الأردني، مع عقود وخطابات ثنائية اللغة وتتبّع انتهاء المستندات."),
      ("Arabic-first &amp; core HR", "العربية أولًا والموارد البشرية الأساسية",
       "Arabic, right-to-left throughout, plus employee records, onboarding, time off and self-service.",
       "العربية ومن اليمين إلى اليسار بالكامل، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Jordan HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في الأردن كما ينبغي',
    'cta_p_en': "See HR Suite handle Jordan payroll and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب ونهاية الخدمة في الأردن لفريقك.",
  },
  'france': {
    'en_name': 'France', 'ar_name': 'فرنسا',
    'tag_en': 'France · FR', 'tag_ar': 'فرنسا · FR',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'France',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لفرنسا',
    'lead_en': "HR Suite runs your France workforce — overtime priced to the statutory 35-hour week, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في فرنسا — عمل إضافي وفق أسبوع الـ٣٥ ساعة النظامي، وملفات دفع SEPA، وحقوق أصحاب البيانات وفق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for France — statutory 35-hour-week overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.",
    'desc_ar': "منظومة الموارد البشرية لفرنسا — عمل إضافي وفق أسبوع الـ٣٥ ساعة، وملفات SEPA، وحقوق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وموارد بشرية كاملة.",
    'hub_sub_en': '35h week · SEPA · GDPR', 'hub_sub_ar': 'أسبوع ٣٥ ساعة · SEPA · GDPR',
    'features': [
      ("Overtime — 35-hour week", "العمل الإضافي — أسبوع ٣٥ ساعة",
       "Overtime priced to the statutory 35-hour week — +25% for the first eight hours (36–43) and +50% beyond, with collective-agreement rates configurable.",
       "يُحتسب العمل الإضافي وفق أسبوع الـ٣٥ ساعة النظامي — +٢٥٪ لأول ثماني ساعات (٣٦–٤٣) و+٥٠٪ بعدها، مع إمكانية تهيئة معدّلات الاتفاقيات الجماعية."),
      ("SEPA payments", "مدفوعات SEPA",
       "Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.",
       "صدّر ملف تحويل SEPA من دورة رواتب معتمدة، مع التحقق من الآيبان عند الإدخال."),
      ("GDPR data-subject rights", "حقوق أصحاب البيانات (GDPR)",
       "Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.",
       "تصدير حق الوصول ومحو انتقائي مع الاحتفاظ، مع بيانات مسؤول حماية البيانات وسياسات الاحتفاظ مدمجة."),
      ("Local payroll &amp; core HR", "الرواتب المحلية والموارد البشرية الأساسية",
       "Model French income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.",
       "أنشئ ضريبة الدخل الفرنسية والمساهمات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة — مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية، باليورو."),
    ],
    'cta_h_en': 'Run France HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في فرنسا كما ينبغي',
    'cta_p_en': "See HR Suite handle French overtime, SEPA and GDPR for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير العمل الإضافي و SEPA و GDPR في فرنسا لفريقك.",
  },
  'germany': {
    'en_name': 'Germany', 'ar_name': 'ألمانيا',
    'tag_en': 'Germany · DE', 'tag_ar': 'ألمانيا · DE',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Germany',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لألمانيا',
    'lead_en': "HR Suite runs your Germany workforce — collective-agreement overtime with Working Time Act caps, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في ألمانيا — عمل إضافي وفق الاتفاقيات الجماعية مع سقوف قانون وقت العمل، وملفات دفع SEPA، وحقوق أصحاب البيانات وفق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Germany — CBA overtime with Working Time Act caps, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.",
    'desc_ar': "منظومة الموارد البشرية لألمانيا — عمل إضافي وفق الاتفاقيات مع سقوف قانون وقت العمل، وملفات SEPA، وحقوق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وموارد بشرية كاملة.",
    'hub_sub_en': 'Overtime · SEPA · GDPR', 'hub_sub_ar': 'العمل الإضافي · SEPA · GDPR',
    'features': [
      ("Overtime &amp; working-time caps", "العمل الإضافي وسقوف وقت العمل",
       "Overtime at the customary 1.25× collective-agreement rate, with the Working Time Act's hour caps (10h/day) respected — configurable per agreement.",
       "عمل إضافي بمعدّل ١٫٢٥× المعتاد في الاتفاقيات الجماعية، مع الالتزام بسقوف قانون وقت العمل (١٠ ساعات/يوم) — قابل للتهيئة حسب الاتفاقية."),
      ("SEPA payments", "مدفوعات SEPA",
       "Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.",
       "صدّر ملف تحويل SEPA من دورة رواتب معتمدة، مع التحقق من الآيبان عند الإدخال."),
      ("GDPR data-subject rights", "حقوق أصحاب البيانات (GDPR)",
       "Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.",
       "تصدير حق الوصول ومحو انتقائي مع الاحتفاظ، مع بيانات مسؤول حماية البيانات وسياسات الاحتفاظ مدمجة."),
      ("Local payroll &amp; core HR", "الرواتب المحلية والموارد البشرية الأساسية",
       "Model German income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.",
       "أنشئ ضريبة الدخل الألمانية والمساهمات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة — مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية، باليورو."),
    ],
    'cta_h_en': 'Run Germany HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في ألمانيا كما ينبغي',
    'cta_p_en': "See HR Suite handle German overtime, SEPA and GDPR for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير العمل الإضافي و SEPA و GDPR في ألمانيا لفريقك.",
  },
  'spain': {
    'en_name': 'Spain', 'ar_name': 'إسبانيا',
    'tag_en': 'Spain · ES', 'tag_ar': 'إسبانيا · ES',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Spain',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لإسبانيا',
    'lead_en': "HR Suite runs your Spain workforce — Workers' Statute overtime, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في إسبانيا — عمل إضافي وفق نظام العمال، وملفات دفع SEPA، وحقوق أصحاب البيانات وفق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Spain — Workers' Statute overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.",
    'desc_ar': "منظومة الموارد البشرية لإسبانيا — عمل إضافي وفق نظام العمال، وملفات SEPA، وحقوق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وموارد بشرية كاملة.",
    'hub_sub_en': 'Overtime · SEPA · GDPR', 'hub_sub_ar': 'العمل الإضافي · SEPA · GDPR',
    'features': [
      ("Overtime — Workers' Statute", "العمل الإضافي — نظام العمال",
       "Overtime at your collective-agreement premium (commonly around +75%), floored at the ordinary-hour value and capped at 80 hours a year.",
       "عمل إضافي بعلاوة الاتفاقية الجماعية (نحو +٧٥٪ عادةً)، بحدٍّ أدنى قيمة الساعة العادية وبسقف ٨٠ ساعة سنويًا."),
      ("SEPA payments", "مدفوعات SEPA",
       "Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.",
       "صدّر ملف تحويل SEPA من دورة رواتب معتمدة، مع التحقق من الآيبان عند الإدخال."),
      ("GDPR data-subject rights", "حقوق أصحاب البيانات (GDPR)",
       "Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.",
       "تصدير حق الوصول ومحو انتقائي مع الاحتفاظ، مع بيانات مسؤول حماية البيانات وسياسات الاحتفاظ مدمجة."),
      ("Local payroll &amp; core HR", "الرواتب المحلية والموارد البشرية الأساسية",
       "Model Spanish income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.",
       "أنشئ ضريبة الدخل الإسبانية والمساهمات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة — مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية، باليورو."),
    ],
    'cta_h_en': 'Run Spain HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في إسبانيا كما ينبغي',
    'cta_p_en': "See HR Suite handle Spanish overtime, SEPA and GDPR for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير العمل الإضافي و SEPA و GDPR في إسبانيا لفريقك.",
  },
  'italy': {
    'en_name': 'Italy', 'ar_name': 'إيطاليا',
    'tag_en': 'Italy · IT', 'tag_ar': 'إيطاليا · IT',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Italy',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لإيطاليا',
    'lead_en': "HR Suite runs your Italy workforce — CCNL overtime, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في إيطاليا — عمل إضافي وفق CCNL، وملفات دفع SEPA، وحقوق أصحاب البيانات وفق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Italy — CCNL overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.",
    'desc_ar': "منظومة الموارد البشرية لإيطاليا — عمل إضافي وفق CCNL، وملفات SEPA، وحقوق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وموارد بشرية كاملة.",
    'hub_sub_en': 'Overtime · SEPA · GDPR', 'hub_sub_ar': 'العمل الإضافي · SEPA · GDPR',
    'features': [
      ("Overtime — CCNL rates", "العمل الإضافي — معدّلات CCNL",
       "Overtime at your national collective-agreement (CCNL) supplement — typically +15% to +50% — configurable per agreement.",
       "عمل إضافي بعلاوة الاتفاقية الجماعية الوطنية (CCNL) — عادةً +١٥٪ إلى +٥٠٪ — قابل للتهيئة حسب الاتفاقية."),
      ("SEPA payments", "مدفوعات SEPA",
       "Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.",
       "صدّر ملف تحويل SEPA من دورة رواتب معتمدة، مع التحقق من الآيبان عند الإدخال."),
      ("GDPR data-subject rights", "حقوق أصحاب البيانات (GDPR)",
       "Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.",
       "تصدير حق الوصول ومحو انتقائي مع الاحتفاظ، مع بيانات مسؤول حماية البيانات وسياسات الاحتفاظ مدمجة."),
      ("Local payroll &amp; core HR", "الرواتب المحلية والموارد البشرية الأساسية",
       "Model Italian income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.",
       "أنشئ ضريبة الدخل الإيطالية والمساهمات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة — مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية، باليورو."),
    ],
    'cta_h_en': 'Run Italy HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في إيطاليا كما ينبغي',
    'cta_p_en': "See HR Suite handle Italian overtime, SEPA and GDPR for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير العمل الإضافي و SEPA و GDPR في إيطاليا لفريقك.",
  },
  'netherlands': {
    'en_name': 'Netherlands', 'ar_name': 'هولندا',
    'tag_en': 'Netherlands · NL', 'tag_ar': 'هولندا · NL',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'the Netherlands',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لهولندا',
    'lead_en': "HR Suite runs your Netherlands workforce — collective-agreement overtime, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في هولندا — عمل إضافي وفق الاتفاقيات الجماعية، وملفات دفع SEPA، وحقوق أصحاب البيانات وفق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for the Netherlands — CBA overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.",
    'desc_ar': "منظومة الموارد البشرية لهولندا — عمل إضافي وفق الاتفاقيات، وملفات SEPA، وحقوق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وموارد بشرية كاملة.",
    'hub_sub_en': 'Overtime · SEPA · GDPR', 'hub_sub_ar': 'العمل الإضافي · SEPA · GDPR',
    'features': [
      ("Overtime — CBA rates", "العمل الإضافي — الاتفاقيات الجماعية",
       "Overtime at the customary 1.25× collective-agreement rate, configurable per agreement.",
       "عمل إضافي بمعدّل ١٫٢٥× المعتاد في الاتفاقيات الجماعية، قابل للتهيئة حسب الاتفاقية."),
      ("SEPA payments", "مدفوعات SEPA",
       "Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.",
       "صدّر ملف تحويل SEPA من دورة رواتب معتمدة، مع التحقق من الآيبان عند الإدخال."),
      ("GDPR data-subject rights", "حقوق أصحاب البيانات (GDPR)",
       "Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.",
       "تصدير حق الوصول ومحو انتقائي مع الاحتفاظ، مع بيانات مسؤول حماية البيانات وسياسات الاحتفاظ مدمجة."),
      ("Local payroll &amp; core HR", "الرواتب المحلية والموارد البشرية الأساسية",
       "Model Dutch income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.",
       "أنشئ ضريبة الدخل الهولندية والمساهمات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة — مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية، باليورو."),
    ],
    'cta_h_en': 'Run Netherlands HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في هولندا كما ينبغي',
    'cta_p_en': "See HR Suite handle Dutch overtime, SEPA and GDPR for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير العمل الإضافي و SEPA و GDPR في هولندا لفريقك.",
  },
  'lebanon': {
    'en_name': 'Lebanon', 'ar_name': 'لبنان',
    'tag_en': 'Lebanon · LB', 'tag_ar': 'لبنان · LB',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Lebanon',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للبنان',
    'lead_en': "HR Suite runs your Lebanon workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and NSSF, rule-based end-of-service, Arabic throughout, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في لبنان — الإجازات النظامية وتقويم العطلات المحلي، ورواتب قابلة للتهيئة مع ضريبة الدخل والضمان الاجتماعي، ونهاية خدمة قائمة على القواعد، ودعم العربية بالكامل، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Lebanon — statutory leave and holidays, configurable payroll with income tax and NSSF, rule-based end-of-service, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية للبنان — الإجازات والعطلات النظامية، ورواتب قابلة للتهيئة مع ضريبة الدخل والضمان الاجتماعي، ونهاية خدمة قائمة على القواعد، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Leave · Payroll · NSSF', 'hub_sub_ar': 'الإجازات · الرواتب · الضمان',
    'features': [
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual, sick and maternity leave and the Lebanese public-holiday calendar, built in.",
       "الإجازة السنوية والمرضية وإجازة الأمومة النظامية وتقويم العطلات الرسمية اللبنانية، مدمجة."),
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model Lebanese income tax and National Social Security Fund (NSSF) contributions as configurable, classified deductions.",
       "أنشئ ضريبة الدخل اللبنانية واستقطاعات الصندوق الوطني للضمان الاجتماعي (NSSF) كاستقطاعات قابلة للتهيئة ومصنّفة."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.",
       "هيّئ نهاية الخدمة على المحرّك القائم على القواعد — أيام أجر عن كل سنة — لتناسب الاستحقاقات المحلية دون إعداد جاهز."),
      ("Arabic-first &amp; core HR", "العربية أولًا والموارد البشرية الأساسية",
       "Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.",
       "العربية ومن اليمين إلى اليسار بالكامل، والدفع بالعملة المحلية، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Lebanon HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في لبنان كما ينبغي',
    'cta_p_en': "See HR Suite handle Lebanon leave, payroll and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الإجازات والرواتب ونهاية الخدمة في لبنان لفريقك.",
  },
  'iraq': {
    'en_name': 'Iraq', 'ar_name': 'العراق',
    'tag_en': 'Iraq · IQ', 'tag_ar': 'العراق · IQ',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Iraq',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للعراق',
    'lead_en': "HR Suite runs your Iraq workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social security, rule-based end-of-service, Arabic throughout, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في العراق — الإجازات النظامية وتقويم العطلات المحلي، ورواتب قابلة للتهيئة مع ضريبة الدخل والضمان الاجتماعي، ونهاية خدمة قائمة على القواعد، ودعم العربية بالكامل، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Iraq — statutory leave and holidays, configurable payroll with income tax and social security, rule-based end-of-service, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية للعراق — الإجازات والعطلات النظامية، ورواتب قابلة للتهيئة مع ضريبة الدخل والضمان الاجتماعي، ونهاية خدمة قائمة على القواعد، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Leave · Payroll · Arabic', 'hub_sub_ar': 'الإجازات · الرواتب · العربية',
    'features': [
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual, sick and maternity leave and the Iraqi public-holiday calendar, built in.",
       "الإجازة السنوية والمرضية وإجازة الأمومة النظامية وتقويم العطلات الرسمية العراقية، مدمجة."),
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model Iraqi income tax and social-security contributions as configurable, classified deductions, applied in every pay run.",
       "أنشئ ضريبة الدخل العراقية واستقطاعات الضمان الاجتماعي كاستقطاعات قابلة للتهيئة ومصنّفة، تُطبَّق في كل دورة رواتب."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.",
       "هيّئ نهاية الخدمة على المحرّك القائم على القواعد — أيام أجر عن كل سنة — لتناسب الاستحقاقات المحلية دون إعداد جاهز."),
      ("Arabic-first &amp; core HR", "العربية أولًا والموارد البشرية الأساسية",
       "Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.",
       "العربية ومن اليمين إلى اليسار بالكامل، والدفع بالعملة المحلية، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Iraq HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في العراق كما ينبغي',
    'cta_p_en': "See HR Suite handle Iraq leave, payroll and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الإجازات والرواتب ونهاية الخدمة في العراق لفريقك.",
  },
  'palestine': {
    'en_name': 'Palestine', 'ar_name': 'فلسطين',
    'tag_en': 'Palestine · PS', 'tag_ar': 'فلسطين · PS',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Palestine',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لفلسطين',
    'lead_en': "HR Suite runs your Palestine workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social contributions, rule-based end-of-service, Arabic throughout, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في فلسطين — الإجازات النظامية وتقويم العطلات المحلي، ورواتب قابلة للتهيئة مع ضريبة الدخل والمساهمات الاجتماعية، ونهاية خدمة قائمة على القواعد، ودعم العربية بالكامل، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Palestine — statutory leave and holidays, configurable payroll with income tax and social contributions, rule-based end-of-service, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية لفلسطين — الإجازات والعطلات النظامية، ورواتب قابلة للتهيئة مع ضريبة الدخل والمساهمات الاجتماعية، ونهاية خدمة قائمة على القواعد، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Leave · Payroll · Arabic', 'hub_sub_ar': 'الإجازات · الرواتب · العربية',
    'features': [
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual, sick and maternity leave and the Palestinian public-holiday calendar, built in.",
       "الإجازة السنوية والمرضية وإجازة الأمومة النظامية وتقويم العطلات الرسمية الفلسطينية، مدمجة."),
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model Palestinian income tax and social contributions as configurable, classified deductions, applied in every pay run.",
       "أنشئ ضريبة الدخل الفلسطينية والمساهمات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة، تُطبَّق في كل دورة رواتب."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.",
       "هيّئ نهاية الخدمة على المحرّك القائم على القواعد — أيام أجر عن كل سنة — لتناسب الاستحقاقات المحلية دون إعداد جاهز."),
      ("Arabic-first &amp; core HR", "العربية أولًا والموارد البشرية الأساسية",
       "Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.",
       "العربية ومن اليمين إلى اليسار بالكامل، والدفع بالعملة المحلية، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Palestine HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في فلسطين كما ينبغي',
    'cta_p_en': "See HR Suite handle Palestine leave, payroll and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الإجازات والرواتب ونهاية الخدمة في فلسطين لفريقك.",
  },
  'ireland': {
    'en_name': 'Ireland', 'ar_name': 'أيرلندا',
    'tag_en': 'Ireland · IE', 'tag_ar': 'أيرلندا · IE',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Ireland',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لأيرلندا',
    'lead_en': "HR Suite runs your Ireland workforce — statutory leave and the local holiday calendar, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في أيرلندا — الإجازات النظامية وتقويم العطلات المحلي، وملفات دفع SEPA، وحقوق أصحاب البيانات وفق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Ireland — statutory leave and holidays, SEPA pay files, GDPR rights, configurable local payroll (PAYE/PRSI/USC) in EUR, and full HR.",
    'desc_ar': "منظومة الموارد البشرية لأيرلندا — الإجازات والعطلات النظامية، وملفات SEPA، وحقوق GDPR، ورواتب محلية قابلة للتهيئة باليورو، وموارد بشرية كاملة.",
    'hub_sub_en': 'Leave · SEPA · GDPR', 'hub_sub_ar': 'الإجازات · SEPA · GDPR',
    'features': [
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual leave and the Irish public-holiday calendar, built in.",
       "الإجازة السنوية النظامية وتقويم العطلات الرسمية الأيرلندية، مدمجة."),
      ("SEPA payments", "مدفوعات SEPA",
       "Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.",
       "صدّر ملف تحويل SEPA من دورة رواتب معتمدة، مع التحقق من الآيبان عند الإدخال."),
      ("GDPR data-subject rights", "حقوق أصحاب البيانات (GDPR)",
       "Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.",
       "تصدير حق الوصول ومحو انتقائي مع الاحتفاظ، مع بيانات مسؤول حماية البيانات وسياسات الاحتفاظ مدمجة."),
      ("Local payroll &amp; core HR", "الرواتب المحلية والموارد البشرية الأساسية",
       "Model Irish income tax (PAYE), PRSI and USC as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.",
       "أنشئ ضريبة الدخل الأيرلندية (PAYE) و PRSI و USC كاستقطاعات قابلة للتهيئة ومصنّفة — مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية، باليورو."),
    ],
    'cta_h_en': 'Run Ireland HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في أيرلندا كما ينبغي',
    'cta_p_en': "See HR Suite handle Irish leave, SEPA and GDPR for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الإجازات و SEPA و GDPR في أيرلندا لفريقك.",
  },
  'canada': {
    'en_name': 'Canada', 'ar_name': 'كندا',
    'tag_en': 'Canada · CA', 'tag_ar': 'كندا · CA',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Canada',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لكندا',
    'lead_en': "HR Suite runs your Canada workforce — statutory leave and the local holiday calendar, configurable payroll with federal and provincial tax, CPP and EI, and full employee records in CAD.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في كندا — الإجازات النظامية وتقويم العطلات المحلي، ورواتب قابلة للتهيئة مع الضريبة الفيدرالية والإقليمية و CPP و EI، وسجلّات موظفين كاملة بالدولار الكندي.",
    'desc_en': "HR Suite for Canada — statutory leave and holidays, configurable payroll with federal/provincial tax, CPP and EI, and full HR in CAD.",
    'desc_ar': "منظومة الموارد البشرية لكندا — الإجازات والعطلات النظامية، ورواتب قابلة للتهيئة مع الضريبة الفيدرالية والإقليمية و CPP و EI، وموارد بشرية كاملة بالدولار الكندي.",
    'hub_sub_en': 'Leave · Payroll · CPP/EI', 'hub_sub_ar': 'الإجازات · الرواتب · CPP/EI',
    'features': [
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Vacation, sick and parental leave with the Canadian statutory-holiday calendar, built in.",
       "إجازة سنوية ومرضية وإجازة والدية مع تقويم العطلات الرسمية الكندية، مدمجة."),
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model federal and provincial income tax, CPP and EI as configurable, classified deductions, applied in every pay run.",
       "أنشئ ضريبة الدخل الفيدرالية والإقليمية و CPP و EI كاستقطاعات قابلة للتهيئة ومصنّفة، تُطبَّق في كل دورة رواتب."),
      ("Overtime — configurable", "العمل الإضافي — قابل للتهيئة",
       "Provincial overtime (commonly 1.5× over 44 hours a week) on the rule-based engine — configure the rule that applies to you.",
       "العمل الإضافي الإقليمي (عادةً ١٫٥× بعد ٤٤ ساعة أسبوعيًا) على المحرّك القائم على القواعد — هيّئ القاعدة التي تنطبق عليك."),
      ("Core HR &amp; self-service", "الموارد البشرية الأساسية والخدمة الذاتية",
       "Pay in Canadian dollars, plus employee records, onboarding, time off and self-service.",
       "الدفع بالدولار الكندي، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Canada HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في كندا كما ينبغي',
    'cta_p_en': "See HR Suite handle Canadian leave, payroll and overtime for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الإجازات والرواتب والعمل الإضافي في كندا لفريقك.",
  },
  'north-america': {
    'en_name': 'North America', 'ar_name': 'أمريكا الشمالية',
    'tag_en': 'North America · US &amp; Canada', 'tag_ar': 'أمريكا الشمالية · US و Canada',
    'h1_en': 'FulcrumGrid, built for', 'h1_grad_en': 'North America',
    'h1_ar': 'FulcrumGrid،', 'h1_grad_ar': 'مصمّمة لأمريكا الشمالية',
    'lead_en': "The whole grid runs across North America — HR Suite with configurable payroll and federal, state and provincial rules; Command Center with real-time finance and reporting in USD and CAD; and Collection for receivables and reminders. Pick a country for the detail.",
    'lead_ar': "الشبكة كاملة تعمل عبر أمريكا الشمالية — HR Suite برواتب قابلة للتهيئة وقواعد فيدرالية وولائية وإقليمية؛ وCommand Center بمالية وتقارير فورية بالدولار الأمريكي والكندي؛ وCollection للتحصيل والتذكيرات. اختر دولة لعرض التفاصيل.",
    'desc_en': "FulcrumGrid across North America — HR Suite, Command Center and Collection — with configurable payroll by federal, state and provincial rule, real-time finance in USD and CAD, and receivables.",
    'desc_ar': "FulcrumGrid عبر أمريكا الشمالية — HR Suite وCommand Center وCollection — برواتب قابلة للتهيئة وفق القواعد الفيدرالية والولائية والإقليمية، ومالية فورية بالدولار الأمريكي والكندي، وتحصيل.",
    'hub_sub_en': 'United States · Canada', 'hub_sub_ar': 'الولايات المتحدة · كندا',
    'members': ['usa', 'canada'],
    'cta_h_en': 'Run your North American operation on one grid', 'cta_h_ar': 'أدِر عملياتك في أمريكا الشمالية على شبكة واحدة',
    'cta_p_en': "Tell us where you operate and we'll show you the whole grid in action.",
    'cta_p_ar': "أخبرنا أين تعمل وسنعرض لك الشبكة كاملة وهي تعمل.",
  },
  'syria': {
    'en_name': 'Syria', 'ar_name': 'سوريا',
    'tag_en': 'Syria · SY', 'tag_ar': 'سوريا · SY',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Syria',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لسوريا',
    'lead_en': "HR Suite runs your Syria workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social insurance, rule-based end-of-service, Arabic throughout, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في سوريا — الإجازات النظامية وتقويم العطلات المحلي، ورواتب قابلة للتهيئة مع ضريبة الدخل والتأمينات الاجتماعية، ونهاية خدمة قائمة على القواعد، ودعم العربية بالكامل، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Syria — statutory leave and holidays, configurable payroll with income tax and social insurance, rule-based end-of-service, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية لسوريا — الإجازات والعطلات النظامية، ورواتب قابلة للتهيئة مع ضريبة الدخل والتأمينات، ونهاية خدمة قائمة على القواعد، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Leave · Payroll · Arabic', 'hub_sub_ar': 'الإجازات · الرواتب · العربية',
    'features': [
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual, sick and maternity leave and the Syrian public-holiday calendar, built in.",
       "الإجازة السنوية والمرضية وإجازة الأمومة النظامية وتقويم العطلات الرسمية السورية، مدمجة."),
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model Syrian income tax and social-insurance contributions as configurable, classified deductions, applied in every pay run.",
       "أنشئ ضريبة الدخل السورية واستقطاعات التأمينات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة، تُطبَّق في كل دورة رواتب."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.",
       "هيّئ نهاية الخدمة على المحرّك القائم على القواعد — أيام أجر عن كل سنة — لتناسب الاستحقاقات المحلية دون إعداد جاهز."),
      ("Arabic-first &amp; core HR", "العربية أولًا والموارد البشرية الأساسية",
       "Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.",
       "العربية ومن اليمين إلى اليسار بالكامل، والدفع بالعملة المحلية، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Syria HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في سوريا كما ينبغي',
    'cta_p_en': "See HR Suite handle Syria leave, payroll and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الإجازات والرواتب ونهاية الخدمة في سوريا لفريقك.",
  },
  'yemen': {
    'en_name': 'Yemen', 'ar_name': 'اليمن',
    'tag_en': 'Yemen · YE', 'tag_ar': 'اليمن · YE',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Yemen',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لليمن',
    'lead_en': "HR Suite runs your Yemen workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social insurance, rule-based end-of-service, Arabic throughout, and full employee records.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في اليمن — الإجازات النظامية وتقويم العطلات المحلي، ورواتب قابلة للتهيئة مع ضريبة الدخل والتأمينات الاجتماعية، ونهاية خدمة قائمة على القواعد، ودعم العربية بالكامل، وسجلّات موظفين كاملة.",
    'desc_en': "HR Suite for Yemen — statutory leave and holidays, configurable payroll with income tax and social insurance, rule-based end-of-service, and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية لليمن — الإجازات والعطلات النظامية، ورواتب قابلة للتهيئة مع ضريبة الدخل والتأمينات، ونهاية خدمة قائمة على القواعد، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Leave · Payroll · Arabic', 'hub_sub_ar': 'الإجازات · الرواتب · العربية',
    'features': [
      ("Statutory leave &amp; holidays", "الإجازات والعطلات النظامية",
       "Statutory annual, sick and maternity leave and the Yemeni public-holiday calendar, built in.",
       "الإجازة السنوية والمرضية وإجازة الأمومة النظامية وتقويم العطلات الرسمية اليمنية، مدمجة."),
      ("Configurable payroll", "رواتب قابلة للتهيئة",
       "Model Yemeni income tax and social-insurance contributions as configurable, classified deductions, applied in every pay run.",
       "أنشئ ضريبة الدخل اليمنية واستقطاعات التأمينات الاجتماعية كاستقطاعات قابلة للتهيئة ومصنّفة، تُطبَّق في كل دورة رواتب."),
      ("End-of-service, your rules", "نهاية الخدمة بقواعدك",
       "Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.",
       "هيّئ نهاية الخدمة على المحرّك القائم على القواعد — أيام أجر عن كل سنة — لتناسب الاستحقاقات المحلية دون إعداد جاهز."),
      ("Arabic-first &amp; core HR", "العربية أولًا والموارد البشرية الأساسية",
       "Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.",
       "العربية ومن اليمين إلى اليسار بالكامل، والدفع بالعملة المحلية، مع سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية."),
    ],
    'cta_h_en': 'Run Yemen HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في اليمن كما ينبغي',
    'cta_p_en': "See HR Suite handle Yemen leave, payroll and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الإجازات والرواتب ونهاية الخدمة في اليمن لفريقك.",
  },
}

# Every page generated (country detail + region group), used by the sitemap too.
REGION_ORDER = ['saudi-arabia', 'uae', 'qatar', 'kuwait', 'bahrain', 'oman', 'uk', 'usa', 'canada',
                'north-america', 'europe', 'france', 'germany', 'spain', 'italy', 'netherlands', 'ireland',
                'egypt', 'jordan', 'lebanon', 'iraq', 'palestine', 'syria', 'yemen', 'gcc', 'middle-east']
# The top-level regions shown on the /regions/ hub, in order.
HUB_ORDER = ['north-america', 'europe', 'gcc', 'middle-east']

# Reverse map: country slug -> its region group (for cross-app regional copy).
COUNTRY_GROUP = {}
for _g in HUB_ORDER:
    for _m in REGIONS[_g].get('members', []):
        COUNTRY_GROUP[_m] = _g
DEFAULT_GROUP = 'europe'  # generic fallback for any country without a group

# Per region group: how Command Center and Collection fit that region, as
# (body_en, body_ar). Used on the region-group "grid in your region" section
# and each country's "rest of the grid" section, so the outside view shows
# every app working in every region while country pages stay HR-deep.
GRID_APPS = {
  'gcc': {
    'cc': ("GCC-native finance — Tax and Zakat, VAT, and multi-currency reporting in SAR, AED and more, Arabic and right-to-left throughout.",
           "مالية خليجية أصيلة — الضريبة والزكاة وضريبة القيمة المضافة وتقارير متعددة العملات بالريال والدرهم وغيرها، بالعربية ومن اليمين إلى اليسار بالكامل."),
    'col': ("Chase receivables in your local currency with Arabic reminders and local payment terms.",
            "تابِع التحصيل بعملتك المحلية مع تذكيرات بالعربية وشروط سداد محلية."),
  },
  'middle-east': {
    'cc': ("Arabic-first finance with multi-currency reporting and local tax handling, real-time across your operation.",
           "مالية بالعربية أولًا مع تقارير متعددة العملات ومعالجة الضرائب المحلية، فوريًا عبر عملياتك."),
    'col': ("Chase receivables in local currency with Arabic reminders and local payment terms.",
            "تابِع التحصيل بالعملة المحلية مع تذكيرات بالعربية وشروط سداد محلية."),
  },
  'europe': {
    'cc': ("Multi-currency, VAT-ready finance and real-time dashboards in EUR, GBP and local currencies.",
           "مالية متعددة العملات وجاهزة لضريبة القيمة المضافة ولوحات فورية باليورو والجنيه والعملات المحلية."),
    'col': ("SEPA-friendly receivables with local payment terms and automated reminders.",
            "تحصيل متوافق مع SEPA بشروط سداد محلية وتذكيرات آلية."),
  },
  'north-america': {
    'cc': ("Real-time finance and reporting in USD and CAD, with live dashboards across your operation.",
           "مالية وتقارير فورية بالدولار الأمريكي والكندي، بلوحات حيّة عبر عملياتك."),
    'col': ("Track invoices and automate reminders with local payment terms.",
            "تابِع الفواتير وأتمت التذكيرات بشروط سداد محلية."),
  },
}
# Generic HR one-liner for the region-group "grid in your region" section
# (country pages already lead with HR, so they don't repeat it).
HR_GRID = ("Local payroll, statutory compliance and full HR — the deepest local coverage on the grid.",
           "رواتب محلية وامتثال نظامي وموارد بشرية كاملة — أعمق تغطية محلية في الشبكة.")


def app_cell(b, slug, name, body_en, body_ar, en):
    """A .cell linking to an app's product page, used in the cross-app grids."""
    body = body_en if en else body_ar
    arrow = '→' if en else '←'
    return (f'          <div class="cell"><h4><a href="{b}/products/{slug}/" '
            f'style="text-decoration:none;color:inherit">{name} {arrow}</a></h4><p>{body}</p></div>')


def grid_apps_section(d, slug, lang, n, is_group):
    """Cross-app section: on a region-group page it shows all three apps ('the
    grid, in your region'); on a country page it shows the two non-HR apps
    ('the rest of the grid'), since the page already leads with HR."""
    en = lang == 'en'
    b = '' if en else '/ar'
    grp = slug if is_group else COUNTRY_GROUP.get(slug, DEFAULT_GROUP)
    ga = GRID_APPS.get(grp, GRID_APPS[DEFAULT_GROUP])
    if is_group:
        eye = ('%02d · The grid, in your region' % n) if en else 'الشبكة في منطقتك'
        h2 = 'Every app, built for your region' if en else 'كل تطبيق، مصمّم لمنطقتك'
        lead = ('HR Suite, Command Center and Collection all run here — in your language and currency.'
                if en else 'يعمل هنا HR Suite وCommand Center وCollection جميعًا — بلغتك وعملتك.')
        cells = [
            app_cell(b, 'hr-suite', 'HR Suite', HR_GRID[0], HR_GRID[1], en),
            app_cell(b, 'command-center', 'Command Center', ga['cc'][0], ga['cc'][1], en),
            app_cell(b, 'collection', 'Collection', ga['col'][0], ga['col'][1], en),
        ]
    else:
        eye = ('%02d · The rest of the grid' % n) if en else 'بقية الشبكة'
        h2 = 'The rest of the grid, here too' if en else 'بقية الشبكة، هنا أيضًا'
        lead = ('HR Suite is only part of it — Command Center and Collection run in your market too, in your language and currency.'
                if en else 'HR Suite جزء منها فقط — يعمل Command Center وCollection في سوقك أيضًا، بلغتك وعملتك.')
        cells = [
            app_cell(b, 'command-center', 'Command Center', ga['cc'][0], ga['cc'][1], en),
            app_cell(b, 'collection', 'Collection', ga['col'][0], ga['col'][1], en),
        ]
    return f'''    <section class="section">
      <div class="wrap pad">
        <div class="section-head">
          <div>
            <p class="mono mono-accent">{eye}</p>
            <h2>{h2}</h2>
          </div>
          <p class="section-lead">{lead}</p>
        </div>
        <div class="grid-2">
{chr(10).join(cells)}
        </div>
      </div>
    </section>'''

def head(lang, path, title, desc):
    # New fg2 ("industry" redesign) <head>, modelled on the homepage index.html:
    # CSP + GA, Barlow / Barlow Condensed fonts, /assets/css/fg2.css, icons and
    # manifest, per-page title/description/OG/Twitter, canonical + og:url on
    # https://fulcrumgrid.com<path>, and the full 7-language hreflang cluster
    # plus x-default. English only for now — Arabic emission is guarded off in
    # the write loop below, so `lang` currently only ever arrives as 'en'.
    en = lang == 'en'
    pre = '' if en else '/ar'
    canon = 'https://fulcrumgrid.com%s%s' % (pre, path)
    en_url = 'https://fulcrumgrid.com%s' % path
    og = 'https://fulcrumgrid.com/assets/og/og-hr-suite.png'
    htmltag = '<html lang="en">' if en else '<html lang="ar" dir="rtl">'
    oglocale = 'en_US' if en else 'ar_AR'
    fontpreload = ('  <link rel="preload" href="/assets/fonts/barlowcond-600-latin.woff2" as="font" type="font/woff2" crossorigin />\n'
                   '  <link rel="preload" href="/assets/fonts/barlow-400-latin.woff2" as="font" type="font/woff2" crossorigin />') if en else (
                   '  <link rel="preload" href="/assets/fonts/cairo-600-arabic.woff2" as="font" type="font/woff2" crossorigin />\n'
                   '  <link rel="preload" href="/assets/fonts/cairo-400-arabic.woff2" as="font" type="font/woff2" crossorigin />')
    hreflang = '\n'.join(
        '  <link rel="alternate" hreflang="%s" href="https://fulcrumgrid.com%s%s" />' % (code, p, path)
        for code, p in (('en', ''), ('ar', '/ar'), ('fr', '/fr'), ('de', '/de'),
                        ('es', '/es'), ('it', '/it'), ('nl', '/nl')))
    return f'''<!DOCTYPE html>
{htmltag}
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  {CSP}

  {GA}

  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#f2f2f3" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:site_name" content="FulcrumGrid" />
  <meta property="og:locale" content="{oglocale}" />
  <meta property="og:image" content="{og}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{og}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />

  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/icon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/icon-16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/icon-180.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="canonical" href="{canon}" />
{hreflang}
  <link rel="alternate" hreflang="x-default" href="{en_url}" />

{fontpreload}
  <link rel="stylesheet" href="/assets/css/fg2.css" />
</head>'''

def header(lang, path):
    # New fg2 header (site-head), modelled on index.html, with Regions active.
    en = lang == 'en'
    b = '' if en else '/ar'
    brand_aria = 'FulcrumGrid home' if en else 'FulcrumGrid الصفحة الرئيسية'
    nav_aria = 'Primary' if en else 'التنقّل الرئيسي'
    nav_items = ([('/products/', 'Products'), ('/features/', 'Platform'), ('/pricing/', 'Pricing'),
                  ('/regions/', 'Regions'), ('/blog/', 'Blog'), ('/contact/', 'Contact')] if en else
                 [('/products/', 'المنتجات'), ('/features/', 'المنصّة'), ('/pricing/', 'الأسعار'),
                  ('/regions/', 'المناطق'), ('/blog/', 'المدوّنة'), ('/contact/', 'اتصل بنا')])
    nav = []
    for href, label in nav_items:
        act = ' class="active" aria-current="page"' if href == '/regions/' else ''
        nav.append('        <a href="%s%s"%s>%s</a>' % (b, href, act, label))
    nav = '\n'.join(nav)
    langs = [('en', '/', 'English'), ('ar', '/ar/', 'العربية'), ('fr', '/fr/', 'Français'),
             ('de', '/de/', 'Deutsch'), ('es', '/es/', 'Español'), ('it', '/it/', 'Italiano'),
             ('nl', '/nl/', 'Nederlands')]
    lang_links = []
    for code, href, native in langs:
        active = ' class="active"' if code == lang else ''
        lang_links.append('            <a href="%s"%s hreflang="%s" lang="%s">%s</a>' % (href, active, code, code, native))
    lang_links = '\n'.join(lang_links)
    summary = ('Language', 'EN ▾') if en else ('اللغة', 'ع ▾')
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    menu_aria = 'Menu' if en else 'القائمة'
    return f'''<body>
  <!-- ===== Header ===== -->
  <header class="site-head">
    <div class="wrap row">
      <a class="brand" href="{b}/" aria-label="{brand_aria}">
        <span class="brand-mark">F</span>
        <span class="brand-name">Fulcrum<b>Grid</b></span>
      </a>
      <nav class="site-nav" aria-label="{nav_aria}">
{nav}
      </nav>
      <div class="head-cta">
        <details class="lang-dd">
          <summary aria-label="{summary[0]}">{summary[1]}</summary>
          <div class="lang-dd-menu">
{lang_links}
          </div>
        </details>
        <a class="btn btn-primary btn-sm" href="{b}/contact/">{demo}</a>
      </div>
      <button class="nav-toggle" aria-label="{menu_aria}"><span>≡</span></button>
    </div>
  </header>'''

def footer(lang):
    # New fg2 footer (site-foot), modelled on index.html. HR Suite listed first
    # among the apps.
    en = lang == 'en'
    if en:
        return '''  <!-- ===== Footer ===== -->
  <footer class="site-foot">
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
  </footer>

  <script src="/assets/js/consent.js" defer></script>
</body>
</html>'''
    return '''  <!-- ===== Footer ===== -->
  <footer class="site-foot">
    <div class="wrap">
      <div class="foot-grid">
        <div class="foot-brand">
          <span class="brand-name">Fulcrum<b>Grid</b></span>
          <p>العمود الفقري التشغيلي للفرق الحديثة.</p>
        </div>
        <div class="foot-col">
          <h5>المنتجات</h5>
          <a href="/ar/products/">كل المنتجات</a>
          <a href="/ar/products/hr-suite/">HR Suite</a>
          <a href="/ar/products/command-center/">Command Center</a>
          <a href="/ar/products/collection/">Collection</a>
          <a href="/ar/custom-apps/">تطبيقات مخصّصة</a>
        </div>
        <div class="foot-col">
          <h5>المنصّة</h5>
          <a href="/ar/features/">الميزات</a>
          <a href="/ar/integrations/">التكاملات</a>
          <a href="/ar/how-it-works/">كيف تعمل</a>
          <a href="/ar/pricing/">الأسعار</a>
          <a href="/ar/regions/">المناطق</a>
          <a href="/ar/blog/">المدوّنة</a>
        </div>
        <div class="foot-col">
          <h5>الشركة</h5>
          <a href="/ar/about/">من نحن</a>
          <a href="/ar/faq/">الأسئلة الشائعة</a>
          <a href="/ar/contact/">اتصل بنا</a>
          <a href="/ar/privacy/">الخصوصية</a>
          <a href="https://avenlorconsulting.com/ar/" target="_blank" rel="noopener">أفنلور للاستشارات ↗</a>
        </div>
      </div>
      <div class="foot-bottom">
        <span>© <span id="yr">2026</span> FulcrumGrid. جميع الحقوق محفوظة.</span>
        <span class="mono">fulcrumgrid.com</span>
      </div>
    </div>
  </footer>

  <script src="/assets/js/consent.js" defer></script>
</body>
</html>'''

def region_code(slug):
    """Short code shown on a region/country card (KSA, UAE, NA, ...).
    Hub-level regions get an explicit two/three-letter code (matching the
    homepage); country cards derive it from the tag suffix (e.g. 'Qatar · QA')."""
    override = {'north-america': 'NA', 'europe': 'EU', 'gcc': 'GCC', 'middle-east': 'ME'}
    if slug in override:
        return override[slug]
    return REGIONS[slug]['tag_en'].split('·')[-1].strip()

def region_page(slug, lang):
    d = REGIONS[slug]
    en = lang == 'en'
    b = '' if en else '/ar'
    path = '/regions/%s/' % slug
    name = d['en_name'] if en else d['ar_name']
    is_group = bool(d.get('members'))
    if is_group:
        title = ('FulcrumGrid in %s — every app, built for your region | FulcrumGrid' % name) if en else ('FulcrumGrid في %s — كل تطبيق، مصمّم لمنطقتك | FulcrumGrid' % name)
    else:
        title = ('%s — HR &amp; payroll for %s | FulcrumGrid' % ('HR Suite', name)) if en else ('الموارد البشرية والرواتب في %s | FulcrumGrid' % name)
    desc = d['desc_en'] if en else d['desc_ar']
    tag = d['tag_en'] if en else d['tag_ar']
    h1 = d['h1_en'] if en else d['h1_ar']
    h1g = d['h1_grad_en'] if en else d['h1_grad_ar']
    lead = d['lead_en'] if en else d['lead_ar']
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    if is_group:
        act2 = 'Explore the apps' if en else 'استكشف التطبيقات'
        act2_href = f'{b}/products/'
        act3 = 'See pricing' if en else 'شاهد الأسعار'
        act3_href = f'{b}/pricing/'
    else:
        act2 = 'Explore HR Suite' if en else 'استكشف الموارد البشرية'
        act2_href = f'{b}/products/hr-suite/'
        act3 = 'See HR Suite pricing' if en else 'أسعار الموارد البشرية'
        act3_href = f'{b}/pricing/hr-suite/'
    whatsin_h = ('%s compliance, out of the box' % name) if en else ('امتثال %s جاهز' % name)
    whatsin_p = ("The modules that make HR Suite work the way %s does — each part of the same grid, no separate tools." % name if en
                 else "الوحدات التي تجعل منظومة الموارد البشرية تعمل بالطريقة المحلية في %s — كلّها جزء من الشبكة نفسها، دون أدوات منفصلة." % name)
    note = (f'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on. <a href="{b}/pricing/hr-suite/">See HR Suite pricing →</a>'
            if en else
            f'كل وحدة هنا جزء من منظومة الموارد البشرية — الرواتب المتقدّمة ونهاية السنة والامتثال في خطة المؤسسات، أو تُضاف إلى أي خطة كإضافة لكل مقعد. <a href="{b}/pricing/hr-suite/">أسعار الموارد البشرية ←</a>')
    cta_h = d['cta_h_en'] if en else d['cta_h_ar']
    cta_p = d['cta_p_en'] if en else d['cta_p_ar']
    email = 'Email us' if en else 'راسلنا'
    # Build the middle fg2 sections: a feature grid (.grid-2/.cell, country
    # detail) and/or a member-country cross-grid (.regions/.region, region
    # group). Technical eyebrows are numbered monospace labels.
    sections = []
    n = 1
    if is_group:
        sections.append(grid_apps_section(d, slug, lang, n, True))
        n += 1
    if d.get('features'):
        cells = []
        for te, ta, be, ba in d['features']:
            cells.append(f'          <div class="cell"><h4>{te if en else ta}</h4><p>{be if en else ba}</p></div>')
        eye = ('%02d · Built in' % n) if en else 'مضمّن'
        n += 1
        sections.append(f'''    <section class="section">
      <div class="wrap pad">
        <div class="section-head">
          <div>
            <p class="mono mono-accent">{eye}</p>
            <h2>{whatsin_h}</h2>
          </div>
          <p class="section-lead">{whatsin_p}</p>
        </div>
        <div class="grid-2">
{chr(10).join(cells)}
        </div>
        <p class="text-muted" style="margin-top:26px;max-width:74ch">{note}</p>
      </div>
    </section>''')
    if not is_group:
        sections.append(grid_apps_section(d, slug, lang, n, False))
        n += 1
    if d.get('members'):
        mc = []
        for m in d['members']:
            md = REGIONS[m]
            mname = md['en_name'] if en else md['ar_name']
            msub = md['hub_sub_en'] if en else md['hub_sub_ar']
            mc.append(f'          <a class="region" href="{b}/regions/{m}/" style="text-decoration:none;color:inherit"><div class="code">{region_code(m)}</div><h4>{mname}</h4><p class="cs">{msub}</p></a>')
        c_eye = ('%02d · Countries' % n) if en else 'الدول'
        n += 1
        c_h = 'Countries in this region' if en else 'الدول في هذه المنطقة'
        c_p = ('Pick a country for its statutory payroll and compliance detail — and it runs across the wider region too.' if en
               else 'اختر دولة لعرض تفاصيل الرواتب والامتثال النظامي فيها — وتعمل كذلك عبر المنطقة الأوسع.')
        served_html = ''
        if d.get('served_en'):
            served = d['served_en'] if en else d['served_ar']
            if en:
                served_html = (f'\n        <p class="text-muted" style="margin-top:20px;max-width:74ch">'
                               f'<strong>Also runs across the region:</strong> {served} — with configurable local payroll, '
                               f'end-of-service and multi-currency pay. <a href="{b}/contact/">Ask about your market →</a></p>')
            else:
                served_html = (f'\n        <p class="text-muted" style="margin-top:20px;max-width:74ch">'
                               f'<strong>وتعمل أيضًا عبر المنطقة:</strong> {served} — مع رواتب محلية ونهاية خدمة قابلة للتهيئة '
                               f'ودفع متعدّد العملات. <a href="{b}/contact/">اسأل عن سوقك ←</a></p>')
        sections.append(f'''    <section class="section">
      <div class="wrap pad">
        <div class="section-head">
          <div>
            <p class="mono mono-accent">{c_eye}</p>
            <h2>{c_h}</h2>
          </div>
          <p class="section-lead">{c_p}</p>
        </div>
        <div class="regions">
{chr(10).join(mc)}
        </div>{served_html}
      </div>
    </section>''')
    cta_eye = ('%02d · Get started' % n) if en else 'ابدأ الآن'
    sec_html = ('\n' + '\n\n'.join(sections) + '\n') if sections else ''
    body = f'''{header(lang, path)}

  <main>
    <section class="section">
      <div class="wrap pad">
        <p class="hero-eyebrow">{tag}</p>
        <h1>{h1} <em style="font-style:normal;color:var(--color-accent)">{h1g}</em></h1>
        <p class="hero-intro">{lead}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{b}/contact/">{demo}</a>
          <a class="btn btn-secondary" href="{act2_href}">{act2}</a>
          <a class="btn btn-secondary" href="{act3_href}">{act3}</a>
        </div>
      </div>
    </section>
{sec_html}
    <section class="section cta" id="contact">
      <div class="wrap">
        <p class="mono mono-accent">{cta_eye}</p>
        <h2>{cta_h}</h2>
        <p class="section-lead" style="margin:0 auto 26px">{cta_p}</p>
        <div class="actions">
          <a class="btn btn-primary" href="{b}/contact/">{demo}</a>
          <a class="btn btn-secondary" href="mailto:contact@avenlorconsulting.com">{email}</a>
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
    title = ('Regions — every app, built for your region | FulcrumGrid' if en else 'المناطق — كل تطبيق، مصمّم لمنطقتك | FulcrumGrid')
    desc = ("FulcrumGrid runs in your region — HR Suite, Command Center and Collection, adapted to local payroll, compliance, finance, currency and language."
            if en else "يعمل FulcrumGrid في منطقتك — HR Suite وCommand Center وCollection، متكيّفة مع الرواتب والامتثال والمالية والعملة واللغة المحلية.")
    eye = 'Regions' if en else 'المناطق'
    h1 = 'Built for how your' if en else 'مصمّمة لطريقة'
    h1g = 'region runs' if en else 'عمل منطقتك'
    lead = ("The whole grid runs in your region — HR Suite for local payroll and compliance, Command Center for regional finance and tax, and Collection for local receivables — in your language and currency. Wherever you operate, your data runs on servers hosted in your region. Choose your region."
            if en else "الشبكة كاملة تعمل في منطقتك — HR Suite للرواتب والامتثال المحلي، وCommand Center للمالية والضرائب الإقليمية، وCollection للتحصيل المحلي — بلغتك وعملتك. وأينما تعمل، تعمل بياناتك على خوادم مستضافة في منطقتك. اختر منطقتك.")
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    see_hr = 'Explore the apps' if en else 'استكشف التطبيقات'
    # Region cards — one .region card per top-level region (code + name + served
    # list), like the homepage "06 · Regions" grid, plus a "More markets" tile.
    cards_list = []
    for rslug in HUB_ORDER:
        rd = REGIONS[rslug]
        rname = rd['en_name'] if en else rd['ar_name']
        rsub = rd['hub_sub_en'] if en else rd['hub_sub_ar']
        cards_list.append(f'          <a class="region" href="{b}/regions/{rslug}/" style="text-decoration:none;color:inherit"><div class="code">{region_code(rslug)}</div><h4>{rname}</h4><p class="cs">{rsub}</p></a>')
    more_t = 'More markets' if en else 'أسواق أخرى'
    more_s = 'Elsewhere — on request' if en else 'أماكن أخرى — عند الطلب'
    cards_list.append(f'          <div class="region" style="opacity:.72"><div class="code">+</div><h4>{more_t}</h4><p class="cs">{more_s}</p></div>')
    cards = '\n'.join(cards_list)
    reg_eye = '01 · Regions' if en else 'المناطق'
    reg_h = 'Built for how your region runs.' if en else 'مصمّمة لطريقة عمل منطقتك.'
    reg_lead = 'Choose your region.' if en else 'اختر منطقتك.'
    cta_eye = '02 · Get started' if en else 'ابدأ الآن'
    cta_h = 'Not sure your region is covered?' if en else 'لست متأكدًا من تغطية منطقتك؟'
    cta_p = "Tell us where you operate and we'll show you the whole grid in action." if en else 'أخبرنا أين تعمل وسنعرض لك الشبكة كاملة وهي تعمل.'
    body = f'''{header(lang, path)}

  <main>
    <section class="section">
      <div class="wrap pad">
        <p class="hero-eyebrow">{eye}</p>
        <h1>{h1} <em style="font-style:normal;color:var(--color-accent)">{h1g}</em></h1>
        <p class="hero-intro">{lead}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{b}/contact/">{demo}</a>
          <a class="btn btn-secondary" href="{b}/products/">{see_hr}</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap pad">
        <div class="section-head">
          <div>
            <p class="mono mono-accent">{reg_eye}</p>
            <h2>{reg_h}</h2>
          </div>
          <p class="section-lead">{reg_lead}</p>
        </div>
        <div class="regions">
{cards}
        </div>
      </div>
    </section>

    <section class="section cta" id="contact">
      <div class="wrap">
        <p class="mono mono-accent">{cta_eye}</p>
        <h2>{cta_h}</h2>
        <p class="section-lead" style="margin:0 auto 26px">{cta_p}</p>
        <div class="actions">
          <a class="btn btn-primary" href="{b}/contact/">{demo}</a>
          <a class="btn btn-secondary" href="{b}/products/">{see_hr}</a>
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

# ── Page emission ──────────────────────────────────────────────────────────
# Both English and Arabic pages use the new fg2 ("industry") design. The
# chrome (head/header/footer) and the region_page/hub_page bodies are fully
# language-aware, so the /ar/regions/… tree is generated from the same
# template and data as English (RTL, Cairo, Arabic nav/footer/switcher).
LANGS = ('en', 'ar')

for lang in LANGS:
    pref = '' if lang == 'en' else 'ar/'
    write(pref + 'regions/index.html', hub_page(lang))
    for slug in REGION_ORDER:
        write(pref + 'regions/%s/index.html' % slug, region_page(slug, lang))
