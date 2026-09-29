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
    'desc_en': "HR Suite for the UK — PAYE and National Insurance deductions, P60 and P45 statements, NINO validation, workplace pensions, and full HR on one platform.",
    'desc_ar': "منظومة الموارد البشرية للمملكة المتحدة — استقطاعات PAYE والتأمين الوطني، وكشوف P60 و P45، والتحقق من رقم التأمين الوطني، ومعاشات العمل، وموارد بشرية كاملة على منصة واحدة.",
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
       "Employee records, onboarding, time off, documents and employee self-service — the whole lifecycle on one platform.",
       "سجلّات الموظفين والتأهيل والإجازات والمستندات والخدمة الذاتية — دورة الحياة كاملة على منصة واحدة."),
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
      ("Benefits &amp; deductions", "المزايا والاستقطاعات",
       "Model 401(k), benefits and other pre- and post-tax deductions on the same engine, with employer contributions tracked as company cost.",
       "أنشئ خطة 401(k) والمزايا وغيرها من الاستقطاعات قبل الضريبة وبعدها على النظام نفسه، مع تتبّع مساهمات صاحب العمل كتكلفة على الشركة."),
      ("Core HR &amp; self-service", "الموارد البشرية الأساسية والخدمة الذاتية",
       "Employee records, onboarding, time off, documents and employee self-service — the whole lifecycle on one platform.",
       "سجلّات الموظفين والتأهيل والإجازات والمستندات والخدمة الذاتية — دورة الحياة كاملة على منصة واحدة."),
    ],
    'cta_h_en': 'Run US HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في الولايات المتحدة كما ينبغي',
    'cta_p_en': "See HR Suite handle US payroll, W-2, and ACH for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير الرواتب و W-2 و ACH في الولايات المتحدة لفريقك.",
  },
  'europe': {
    'en_name': 'Europe', 'ar_name': 'أوروبا',
    'tag_en': 'Europe · EU', 'tag_ar': 'أوروبا · EU',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'Europe',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة لأوروبا',
    'lead_en': "HR Suite runs your European workforce with SEPA payments, GDPR-grade data privacy, configurable local deductions, and full employee records — one platform across your entities.",
    'lead_ar': "تدير منظومة الموارد البشرية قوتك العاملة في أوروبا مع مدفوعات SEPA، وخصوصية بيانات بمستوى GDPR، واستقطاعات محلية قابلة للتهيئة، وسجلّات موظفين كاملة — منصة واحدة عبر كياناتك.",
    'desc_en': "HR Suite for Europe — SEPA credit-transfer pay files, GDPR data-subject rights (export and erasure), configurable local deductions, and full HR on one platform.",
    'desc_ar': "منظومة الموارد البشرية لأوروبا — ملفات دفع SEPA، وحقوق أصحاب البيانات وفق GDPR (التصدير والمحو)، واستقطاعات محلية قابلة للتهيئة، وموارد بشرية كاملة على منصة واحدة.",
    'hub_sub_en': 'UK · SEPA · GDPR', 'hub_sub_ar': 'UK · SEPA · GDPR',
    'members': ['uk'],
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
       "Employee records, onboarding, time off and self-service — the whole lifecycle on one platform.",
       "سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية — دورة الحياة كاملة على منصة واحدة."),
    ],
    'cta_h_en': 'Run European HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في أوروبا كما ينبغي',
    'cta_p_en': "See HR Suite handle SEPA payments, GDPR, and payroll for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير مدفوعات SEPA و GDPR والرواتب لفريقك.",
  },
  'gcc': {
    'en_name': 'the GCC', 'ar_name': 'دول الخليج',
    'tag_en': 'Gulf Cooperation Council · GCC', 'tag_ar': 'مجلس التعاون الخليجي · GCC',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'the Gulf',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للخليج',
    'lead_en': "Six Gulf states, one platform — WPS payroll, statutory end-of-service by each country's labour law, social insurance, and nationalization tracking, with Arabic throughout. Pick a country for the detail.",
    'lead_ar': "ست دول خليجية على منصة واحدة — رواتب WPS، ونهاية خدمة نظامية وفق قانون العمل في كل دولة، وتأمينات اجتماعية، ومتابعة التوطين، مع دعم العربية بالكامل. اختر دولة لعرض التفاصيل.",
    'desc_en': "HR Suite across the GCC — Saudi Arabia, UAE, Qatar, Kuwait, Bahrain and Oman — with WPS payroll, statutory end-of-service, social insurance and nationalization tracking per country.",
    'desc_ar': "منظومة الموارد البشرية عبر دول الخليج — السعودية والإمارات وقطر والكويت والبحرين وعُمان — مع رواتب WPS، ونهاية خدمة نظامية، وتأمينات، ومتابعة توطين لكل دولة.",
    'hub_sub_en': 'Saudi · UAE · Qatar · Kuwait · Bahrain · Oman', 'hub_sub_ar': 'السعودية · الإمارات · قطر · الكويت · البحرين · عُمان',
    'members': ['saudi-arabia', 'uae', 'qatar', 'kuwait', 'bahrain', 'oman'],
    'cta_h_en': 'Run Gulf HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في الخليج كما ينبغي',
    'cta_p_en': "See HR Suite handle Gulf payroll, WPS, and end-of-service for your team.",
    'cta_p_ar': "شاهد منظومة الموارد البشرية تدير رواتب الخليج و WPS ونهاية الخدمة لفريقك.",
  },
  'middle-east': {
    'en_name': 'the Middle East', 'ar_name': 'الشرق الأوسط',
    'tag_en': 'Middle East · MENA', 'tag_ar': 'الشرق الأوسط · MENA',
    'h1_en': 'HR &amp; payroll, built for', 'h1_grad_en': 'the Middle East',
    'h1_ar': 'موارد بشرية ورواتب،', 'h1_grad_ar': 'مصمّمة للشرق الأوسط',
    'lead_en': "Arabic-first HR and payroll across the wider Middle East — configurable local deductions and end-of-service, multi-currency pay, and full employee records. Deepest in the Gulf, ready beyond it.",
    'lead_ar': "موارد بشرية ورواتب بالعربية أولًا عبر الشرق الأوسط الأوسع — استقطاعات محلية ونهاية خدمة قابلة للتهيئة، ودفع متعدّد العملات، وسجلّات موظفين كاملة. الأعمق في الخليج، وجاهزة لما بعده.",
    'desc_en': "HR Suite across the Middle East — Egypt, Jordan and the Levant — with configurable local payroll, rule-based end-of-service, multi-currency pay and Arabic-first HR.",
    'desc_ar': "منظومة الموارد البشرية عبر الشرق الأوسط — مصر والأردن وبلاد الشام — مع رواتب محلية قابلة للتهيئة، ونهاية خدمة قائمة على القواعد، ودفع متعدّد العملات، وموارد بشرية بالعربية أولًا.",
    'hub_sub_en': 'Egypt · Jordan · Levant', 'hub_sub_ar': 'مصر · الأردن · بلاد الشام',
    'members': ['egypt', 'jordan'],
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
       "Employee records, onboarding, time off and self-service — the whole lifecycle on one platform.",
       "سجلّات الموظفين والتأهيل والإجازات والخدمة الذاتية — دورة الحياة كاملة على منصة واحدة."),
    ],
    'cta_h_en': 'Run Middle East HR &amp; payroll the right way', 'cta_h_ar': 'أدِر الموارد البشرية والرواتب في الشرق الأوسط كما ينبغي',
    'cta_p_en': "Tell us where you operate and we'll show you how HR Suite fits.",
    'cta_p_ar': "أخبرنا أين تعمل وسنعرض لك كيف تناسبك منظومة الموارد البشرية.",
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
}

# Every page generated (country detail + region group), used by the sitemap too.
REGION_ORDER = ['saudi-arabia', 'uae', 'qatar', 'kuwait', 'bahrain', 'oman', 'uk', 'usa',
                'europe', 'egypt', 'jordan', 'gcc', 'middle-east']
# The top-level regions shown on the /regions/ hub, in order.
HUB_ORDER = ['gcc', 'europe', 'usa', 'middle-east']

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
    whatsin_h = ('%s compliance, out of the box' % name) if en else ('امتثال %s جاهز' % name)
    whatsin_p = ("The modules that make HR Suite work the way %s does — each part of the same platform, no separate tools." % name if en
                 else "الوحدات التي تجعل منظومة الموارد البشرية تعمل بالطريقة المحلية في %s — كلّها جزء من المنصة نفسها، دون أدوات منفصلة." % name)
    note = (f'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on. <a href="{b}/pricing/hr-suite/">See HR Suite pricing →</a>'
            if en else
            f'كل وحدة هنا جزء من منظومة الموارد البشرية — الرواتب المتقدّمة ونهاية السنة والامتثال في خطة المؤسسات، أو تُضاف إلى أي خطة كإضافة لكل مقعد. <a href="{b}/pricing/hr-suite/">أسعار الموارد البشرية ←</a>')
    cta_h = d['cta_h_en'] if en else d['cta_h_ar']
    cta_p = d['cta_p_en'] if en else d['cta_p_ar']
    bc = breadcrumb(lang, [('Home' if en else 'الرئيسية', b + '/'),
                           ('Regions' if en else 'المناطق', b + '/regions/'),
                           (name, None)])
    arrow = '→' if en else '←'
    # Build the middle sections: a feature grid (country detail) and/or a
    # member-country grid (region group). Backgrounds alternate automatically.
    inners = []
    if d.get('features'):
        feats = []
        for te, ta, be, ba in d['features']:
            feats.append(f'''          <div class="feature">
            <div class="feature-icon" aria-hidden="true">{SHIELD}</div>
            <h3>{te if en else ta}</h3>
            <p>{be if en else ba}</p>
          </div>''')
        inners.append(f'''        <div class="sub-head">
          <p class="eyebrow">{whatsin_eye}</p>
          <h2>{whatsin_h}</h2>
          <p>{whatsin_p}</p>
        </div>
        <div class="feature-grid">
{chr(10).join(feats)}
        </div>
        <p class="price-note" style="margin-top:28px">{note}</p>''')
    if d.get('members'):
        mc = []
        for m in d['members']:
            md = REGIONS[m]
            mname = md['en_name'] if en else md['ar_name']
            msub = md['hub_sub_en'] if en else md['hub_sub_ar']
            mc.append(f'''          <a class="cross-card" href="{b}/regions/{m}/" style="--cc: var(--teal)"><span class="ci" aria-hidden="true">{GLOBE}</span><div><h3>{mname}</h3><p>{msub}</p></div><span class="arrow" aria-hidden="true">{arrow}</span></a>''')
        c_eye = 'Countries' if en else 'الدول'
        c_h = 'Countries in this region' if en else 'الدول في هذه المنطقة'
        c_p = ('Pick a country for its statutory payroll and compliance detail.' if en
               else 'اختر دولة لعرض تفاصيل الرواتب والامتثال النظامي فيها.')
        inners.append(f'''        <div class="sub-head">
          <p class="eyebrow">{c_eye}</p>
          <h2>{c_h}</h2>
          <p>{c_p}</p>
        </div>
        <div class="cross-grid">
{chr(10).join(mc)}
        </div>''')
    sec_html = ''
    for i, inner in enumerate(inners):
        cls = 'section section-alt' if i % 2 == 0 else 'section'
        sec_html += f'''    <section class="{cls}">
      <div class="container">
{inner}
      </div>
    </section>

'''
    cta_cls = 'section section-alt' if len(inners) % 2 == 0 else 'section'
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

{sec_html}    <section class="{cta_cls}" id="contact">
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
    # region cards — one per top-level region, in display order
    arrow = '→' if en else '←'
    cards_list = []
    for rslug in HUB_ORDER:
        rd = REGIONS[rslug]
        rname = rd['en_name'] if en else rd['ar_name']
        rsub = rd['hub_sub_en'] if en else rd['hub_sub_ar']
        cards_list.append(f'''          <a class="cross-card" href="{b}/regions/{rslug}/" style="--cc: var(--teal)">
            <span class="ci" aria-hidden="true">{GLOBE}</span>
            <div><h3>{rname}</h3><p>{rsub}</p></div><span class="arrow" aria-hidden="true">{arrow}</span>
          </a>''')
    more_t = 'More markets' if en else 'أسواق أخرى'
    more_s = 'Elsewhere — on request' if en else 'أماكن أخرى — عند الطلب'
    cards_list.append(f'''          <div class="cross-card" style="--cc: var(--text-dim); opacity:.72; cursor:default">
            <span class="ci" aria-hidden="true">{GLOBE}</span>
            <div><h3>{more_t}</h3><p>{more_s}</p></div>
          </div>''')
    cards = '\n'.join(cards_list)
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
    for slug in REGION_ORDER:
        write(pref + 'regions/%s/index.html' % slug, region_page(slug, lang))
