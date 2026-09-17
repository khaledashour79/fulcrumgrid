# -*- coding: utf-8 -*-
import os, re, json, html

ROOT = os.environ.get('FG_ROOT') or os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PCONTENT = os.path.join(ROOT, 'content', 'pricing')

def load_app(slug, fallback):
    """Overlay editable pricing content from content/pricing/<slug>.json.
    The JSON is the source of truth; the inline dict is the default."""
    fp = os.path.join(PCONTENT, slug + '.json')
    if not os.path.exists(fp):
        return fallback
    d = json.load(open(fp, encoding='utf-8'))
    if isinstance(d.get('badge_labels'), dict):
        d['badge_labels'] = {int(k): v for k, v in d['badge_labels'].items()}
    return d

TIER_NAMES = {'en':['Starter','Pro','Business','Enterprise'],
              'ar':['المبتدئة','المتقدّمة','الأعمال','المؤسسات']}
PRICES = ['$12','$24','$39',('Custom','مخصّص')]
PER = {'en':'/ user / month','ar':'/ لكل مستخدم شهريًا'}

APPS = {
 'command-center': {
   'en_name':'Command Center','ar_name':'مركز القيادة',
   'en_lead':"Real-time operations dashboards, priced by plan. Start with the essentials and step up as your operation grows — every plan runs on the same platform.",
   'ar_lead':"لوحات عمليات فورية، مُسعّرة حسب الخطة. ابدأ بالأساسيات وارتقِ مع نموّ عملياتك — وكل الخطط تعمل على المنصة نفسها.",
   'en_desc':"Command Center pricing plans — Starter, Pro, Business, and Enterprise — with a module-by-module breakdown of what's included at each tier.",
   'ar_desc':"خطط أسعار مركز القيادة — المبتدئة والمتقدّمة والأعمال والمؤسسات — مع تفصيل للوحدات المشمولة في كل خطة.",
   'taglines_en':["Small teams getting started.","Growing operations.","Whole-company visibility.","Large or regulated orgs."],
   'taglines_ar':["للفرق الصغيرة في بدايتها.","لعمليات متنامية.","رؤية على مستوى الشركة.","مؤسسات كبيرة أو خاضعة للتنظيم."],
   'tiers_en':[["Up to 10 users","3 live dashboards","Custom KPIs &amp; alerts","Email support"],
               ["Up to 50 users","15 dashboards","Automated workflows","Integrations &amp; API"],
               ["Unlimited users &amp; dashboards","Role-based access control","Audit log","Priority support"],
               ["Everything in Business","SSO / SAML","SLA &amp; dedicated support","Custom integrations"]],
   'tiers_ar':[["حتى ١٠ مستخدمين","٣ لوحات حيّة","مؤشرات وتنبيهات مخصّصة","دعم عبر البريد"],
               ["حتى ٥٠ مستخدمًا","١٥ لوحة","سير عمل آلي","تكاملات وواجهة برمجية"],
               ["مستخدمون ولوحات بلا حدود","صلاحيات حسب الدور","سجل تدقيق","دعم ذو أولوية"],
               ["كل ما في خطة الأعمال","تسجيل دخول موحّد SSO/SAML","اتفاقية مستوى خدمة ودعم مخصّص","تكاملات مخصّصة"]],
   'matrix':[
     (("Users","المستخدمون"),("10","10"),("50","50"),("Unlimited","بلا حدود"),("Unlimited","بلا حدود")),
     (("Live dashboards","اللوحات الحيّة"),("3","٣"),("15","١٥"),("Unlimited","بلا حدود"),("Unlimited","بلا حدود")),
     (("Custom KPIs &amp; metrics","مؤشرات ومقاييس مخصّصة"),'y','y','y','y'),
     (("Alerts &amp; notifications","تنبيهات وإشعارات"),'y','y','y','y'),
     (("Automated workflows","سير عمل آلي"),'n','y','y','y'),
     (("Scheduled reports &amp; exports","تقارير وتصدير مجدولة"),'n','y','y','y'),
     (("Integrations &amp; API","تكاملات وواجهة برمجية"),'n','y','y','y'),
     (("Role-based access control","صلاحيات حسب الدور"),'n','n','y','y'),
     (("Audit log","سجل تدقيق"),'n','n','y','y'),
     (("Data retention","مدة حفظ البيانات"),("6 months","٦ أشهر"),("2 years","سنتان"),("5 years","٥ سنوات"),("Custom","مخصّص")),
     (("SSO / SAML","تسجيل دخول موحّد SSO/SAML"),'n','n','n','y'),
     (("SLA &amp; dedicated support","اتفاقية مستوى خدمة ودعم مخصّص"),'n','n','n','y'),
     (("Support","الدعم"),("Email","بريد"),("Email","بريد"),("Priority","أولوية"),("Dedicated","مخصّص")),
   ],
 },
 'collection': {
   'en_name':'Collection','ar_name':'التحصيل',
   'en_lead':"Receivables and payments, priced by plan. Start collecting faster and scale up as your ledger grows — all on one platform.",
   'ar_lead':"الذمم المدينة والمدفوعات، مُسعّرة حسب الخطة. ابدأ التحصيل أسرع وتوسّع مع نموّ دفترك — وكلّها على منصة واحدة.",
   'en_desc':"Collection pricing plans — Starter, Pro, Business, and Enterprise — with a module-by-module breakdown of what's included at each tier.",
   'ar_desc':"خطط أسعار التحصيل — المبتدئة والمتقدّمة والأعمال والمؤسسات — مع تفصيل للوحدات المشمولة في كل خطة.",
   'taglines_en':["First invoices &amp; reminders.","Scaling receivables.","Company-wide collections.","Large or regulated orgs."],
   'taglines_ar':["أول الفواتير والتذكيرات.","ذمم مدينة تتوسّع.","تحصيل على مستوى الشركة.","مؤسسات كبيرة أو خاضعة للتنظيم."],
   'tiers_en':[["Up to 10 users","500 invoices / month","Payment reminders","Email support"],
               ["Up to 50 users","5,000 invoices / month","Reminder automation","Payment plans"],
               ["Unlimited users &amp; invoices","Role-based access control","Audit log","Priority support"],
               ["Everything in Business","SSO / SAML","SLA &amp; dedicated support","Custom integrations"]],
   'tiers_ar':[["حتى ١٠ مستخدمين","٥٠٠ فاتورة شهريًا","تذكيرات بالدفع","دعم عبر البريد"],
               ["حتى ٥٠ مستخدمًا","٥٬٠٠٠ فاتورة شهريًا","أتمتة التذكيرات","خطط سداد"],
               ["مستخدمون وفواتير بلا حدود","صلاحيات حسب الدور","سجل تدقيق","دعم ذو أولوية"],
               ["كل ما في خطة الأعمال","تسجيل دخول موحّد SSO/SAML","اتفاقية مستوى خدمة ودعم مخصّص","تكاملات مخصّصة"]],
   'matrix':[
     (("Users","المستخدمون"),("10","10"),("50","50"),("Unlimited","بلا حدود"),("Unlimited","بلا حدود")),
     (("Invoices / month","الفواتير شهريًا"),("500","٥٠٠"),("5,000","٥٬٠٠٠"),("Unlimited","بلا حدود"),("Unlimited","بلا حدود")),
     (("Invoice &amp; ledger tracking","تتبّع الفواتير ودفتر الأستاذ"),'y','y','y','y'),
     (("Payment reminders","تذكيرات بالدفع"),'y','y','y','y'),
     (("Reminder automation &amp; schedules","أتمتة التذكيرات وجدولتها"),'n','y','y','y'),
     (("Payment plans","خطط السداد"),'n','y','y','y'),
     (("Payment reconciliation","تسوية المدفوعات"),'y','y','y','y'),
     (("Statements &amp; exports","كشوف وتصدير"),'n','y','y','y'),
     (("Integrations &amp; API","تكاملات وواجهة برمجية"),'n','y','y','y'),
     (("Role-based access control","صلاحيات حسب الدور"),'n','n','y','y'),
     (("Audit log","سجل تدقيق"),'n','n','y','y'),
     (("SSO / SAML","تسجيل دخول موحّد SSO/SAML"),'n','n','n','y'),
     (("SLA &amp; dedicated support","اتفاقية مستوى خدمة ودعم مخصّص"),'n','n','n','y'),
     (("Support","الدعم"),("Email","بريد"),("Email","بريد"),("Priority","أولوية"),("Dedicated","مخصّص")),
   ],
 },
 'hr-suite': {
   'en_name':'HR Suite','ar_name':'منظومة الموارد البشرية',
   'en_lead':"People operations from hire to retire, priced by plan. Start with core records and add payroll, time, and performance as you grow.",
   'ar_lead':"عمليات الأفراد من التعيين إلى التقاعد، مُسعّرة حسب الخطة. ابدأ بالسجلّات الأساسية وأضِف الرواتب والوقت والأداء مع نموّك.",
   'en_desc':"HR Suite pricing plans — Starter, Pro, Business, and Enterprise — with a module-by-module breakdown of what's included at each tier.",
   'ar_desc':"خطط أسعار منظومة الموارد البشرية — المبتدئة والمتقدّمة والأعمال والمؤسسات — مع تفصيل للوحدات المشمولة في كل خطة.",
   'taglines_en':["Core people records.","Growing teams.","Whole-company HR.","Large or regulated orgs."],
   'taglines_ar':["سجلّات الأفراد الأساسية.","فرق متنامية.","موارد بشرية على مستوى الشركة.","مؤسسات كبيرة أو خاضعة للتنظيم."],
   'tiers_en':[["Up to 10 employees","Employee records","Time off &amp; leave","Email support"],
               ["Up to 50 employees","Onboarding &amp; documents","Time tracking","Payroll"],
               ["Unlimited employees","Performance &amp; reviews","Role-based access control","Priority support"],
               ["Everything in Business","SSO / SAML","SLA &amp; dedicated support","Custom integrations"]],
   'tiers_ar':[["حتى ١٠ موظفين","سجلّات الموظفين","الإجازات والغياب","دعم عبر البريد"],
               ["حتى ٥٠ موظفًا","التأهيل والمستندات","تتبّع الوقت","الرواتب"],
               ["موظفون بلا حدود","الأداء والتقييمات","صلاحيات حسب الدور","دعم ذو أولوية"],
               ["كل ما في خطة الأعمال","تسجيل دخول موحّد SSO/SAML","اتفاقية مستوى خدمة ودعم مخصّص","تكاملات مخصّصة"]],
   'matrix':[
     (("Employees","الموظفون"),("10","10"),("50","50"),("Unlimited","بلا حدود"),("Unlimited","بلا حدود")),
     (("Employee records","سجلّات الموظفين"),'y','y','y','y'),
     (("Time off &amp; leave","الإجازات والغياب"),'y','y','y','y'),
     (("Onboarding workflows","سير عمل التأهيل"),'n','y','y','y'),
     (("Time tracking","تتبّع الوقت"),'n','y','y','y'),
     (("Payroll","الرواتب"),'n','y','y','y'),
     (("Documents &amp; e-sign","المستندات والتوقيع الإلكتروني"),'n','y','y','y'),
     (("Performance &amp; reviews","الأداء والتقييمات"),'n','n','y','y'),
     (("Role-based access control","صلاحيات حسب الدور"),'n','n','y','y'),
     (("Audit log","سجل تدقيق"),'n','n','y','y'),
     (("SSO / SAML","تسجيل دخول موحّد SSO/SAML"),'n','n','n','y'),
     (("SLA &amp; dedicated support","اتفاقية مستوى خدمة ودعم مخصّص"),'n','n','n','y'),
     (("Support","الدعم"),("Email","بريد"),("Email","بريد"),("Priority","أولوية"),("Dedicated","مخصّص")),
   ],
 },
}

MARK = '<span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 32 32" width="26" height="26" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="1" y="1" width="30" height="30" rx="7" stroke="url(#bg)" stroke-width="1.5"/><path d="M9 23V9h9M9 16h7" stroke="url(#bg)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="22.5" cy="22.5" r="2.6" fill="url(#bg)"/><defs><linearGradient id="bg" x1="2" y1="2" x2="30" y2="30" gradientUnits="userSpaceOnUse"><stop stop-color="#2156df"/><stop offset="1" stop-color="#1d47ba"/></linearGradient></defs></svg></span>'
MARKF = MARK.replace('id="bg"','id="bgf"').replace('url(#bg)','url(#bgf)').replace('width="26" height="26"','width="24" height="24"')

CSP = '''<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com https://www.googleadservices.com https://www.google.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; img-src 'self' data: https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net; connect-src 'self' https://ipapi.co https://www.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://analytics.google.com https://region1.google-analytics.com https://www.google.com https://www.googleadservices.com https://googleads.g.doubleclick.net https://api.web3forms.com; font-src 'self' https://fonts.gstatic.com; object-src 'none'; base-uri 'self'; form-action 'self' mailto:; frame-src https://td.doubleclick.net" />'''
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

def cell(v, lang):
    if v == 'y': return '<td class="cell"><span class="yes">✓</span></td>'
    if v == 'n': return '<td class="cell"><span class="no">—</span></td>'
    if v == '+': return '<td class="cell"><span class="addon" title="Available as add-on">＋</span></td>'
    return '<td class="cell">%s</td>' % (v[0] if lang=='en' else v[1])

def nav(lang, slug):
    base = '/ar' if lang=='ar' else ''
    N = [('/products/','Products','المنتجات'),('/features/','Platform','المنصّة'),
         ('/pricing/','Pricing','الأسعار'),('/blog/','Blog','المدوّنة'),
         ('/about/','About','من نحن'),('/contact/','Contact','اتصل بنا')]
    out=[]
    for href,en,ar in N:
        act = ' class="active" aria-current="page"' if href=='/pricing/' else ''
        out.append('        <a href="%s%s"%s>%s</a>'%(base,href,act,en if lang=='en' else ar))
    return '\n'.join(out)

def page(slug, d, lang):
    en = lang=='en'
    name = d['en_name'] if en else d['ar_name']
    base = '' if en else '/ar'
    other_base = '/ar' if en else ''
    home = '/' if en else '/ar/'
    contact = '/contact/' if en else '/ar/contact/'
    pricing = '/pricing/' if en else '/ar/pricing/'
    product = '%s/products/%s/'%(base,slug)
    canon = 'https://fulcrumgrid.com%s/pricing/%s/'%(base,slug)
    en_url = 'https://fulcrumgrid.com/pricing/%s/'%slug
    ar_url = 'https://fulcrumgrid.com/ar/pricing/%s/'%slug
    ogimg = 'https://fulcrumgrid.com/assets/og/og-pricing-%s%s.png' % (slug, '' if en else '-ar')
    ogalt = ('%s pricing — plans and modules | FulcrumGrid'%name) if en else ('أسعار %s — الخطط والوحدات | FulcrumGrid'%name)
    title = ('%s pricing — plans &amp; modules | FulcrumGrid'%name) if en else ('أسعار %s — الخطط والوحدات | FulcrumGrid'%name)
    desc = d['en_desc'] if en else d['ar_desc']
    lead = d['en_lead'] if en else d['ar_lead']
    tnames = d.get('tier_names_'+lang, TIER_NAMES[lang])
    tags = d['taglines_en'] if en else d['taglines_ar']
    tiers = d['tiers_en'] if en else d['tiers_ar']
    N = len(tnames)
    popi = d.get('popular_index', 2 if N==4 else (1 if N==3 else 0))
    per = d.get('per_'+lang, PER[lang])
    raw = d.get('prices', PRICES)
    prices = [(tuple(p) if isinstance(p,(list,tuple)) else (p,p)) for p in raw]
    avail = 'Available now' if en else 'متوفّر الآن'
    brandname = '<span class="brand-name">Fulcrum<span class="brand-accent">Grid</span></span>' if en else '<span class="brand-name" dir="ltr">Fulcrum<span class="brand-accent">Grid</span></span>'
    aria_home = 'FulcrumGrid home' if en else 'FulcrumGrid الصفحة الرئيسية'
    demo = 'Request a demo' if en else 'اطلب عرضًا توضيحيًا'
    # tier cards
    cards=[]
    for i in range(N):
        popular = (i==popi)
        pen,par = prices[i]
        pnum = pen if en else par
        is_custom = pen.strip().lower()=='custom'
        numdir = '' if is_custom else ' dir="ltr"'
        peruser = '' if is_custom else '<span class="per">%s</span>'%per
        dataattr = ''
        pm = re.match(r'^(SAR|\$)\s?([\d,]+)$', pen.strip())
        if pm and not is_custom:
            dataattr = ' data-amt="%s" data-base="%s"'%(pm.group(2).replace(',',''), 'SAR' if pm.group(1)=='SAR' else 'USD')
        blab = d.get('badge_labels', {}).get(i)
        btext = (blab[0] if en else blab[1]) if blab else (('Most popular' if en else 'الأكثر شيوعًا') if popular else None)
        badge = ('<span class="price-badge">%s</span>'%btext) if btext else ''
        feats='\n'.join('              <li>%s</li>'%f for f in tiers[i])
        if is_custom:
            btn = '<a class="btn btn-outline btn-lg" href="mailto:contact@avenlorconsulting.com">%s</a>'%('Contact sales' if en else 'تواصل مع المبيعات')
        else:
            cls = 'btn-primary' if popular else 'btn-outline'
            btn = '<a class="btn %s btn-lg" href="%s">%s</a>'%(cls,contact,'Start free trial' if en else 'ابدأ تجربة مجانية')
        cards.append('''          <div class="price-card%s">
            %s<div>
              <div class="price-name">%s</div>
              <p class="price-tagline">%s</p>
            </div>
            <div class="price-amount"><span class="num"%s%s>%s</span>%s</div>
            <ul class="price-features">
%s
            </ul>
            %s
          </div>'''%(' popular' if popular else '', badge, tnames[i], tags[i],
                     numdir, dataattr, pnum, peruser, feats, btn))
    cards='\n\n'.join(cards)
    # matrix
    modhdr = 'Module' if en else 'الوحدة'
    rows=[]
    for r in d['matrix']:
        if r[0]=='__grp__':
            rows.append('              <tr class="grp"><th colspan="%d">%s</th></tr>'%(N+1, r[1][0] if en else r[1][1]))
            continue
        label = r[0][0] if en else r[0][1]
        cells=''.join(cell(r[1+j],lang) for j in range(N))
        rows.append('              <tr><th scope="row">%s</th>%s</tr>'%(label,cells))
    rows='\n'.join(rows)
    colnames=''.join('<th scope="col" class="cell%s">%s</th>'%(' col-hi' if k==popi else '', tnames[k]) for k in range(N))
    # strings
    S = {
     'whatsin': "What's included" if en else 'ما المشمول',
     'modbyplan': 'Modules by plan' if en else 'الوحدات حسب الخطة',
     'modsub': d.get('modsub_'+lang, ('Every %s module, and where it unlocks across the four plans.'%name) if en else ('كل وحدة في %s، وأين تتوفّر عبر الخطط الأربع.'%name)),
     'pricenote': d.get('pricenote_'+lang, ('Per user, per month. Annual billing saves 20%. Every plan includes a 14-day free trial.' if en else 'لكل مستخدم شهريًا. الدفع السنوي يوفّر ٢٠٪. كل خطة تشمل تجربة مجانية ١٤ يومًا.')),
     'faq': 'FAQ' if en else 'الأسئلة الشائعة',
     'faqh': ('%s pricing, answered'%name) if en else ('أسئلة أسعار %s، مُجابة'%name),
     'cta_h': ('See %s on your data'%name) if en else ('شاهد %s على بياناتك'%name),
     'cta_p': "Tell us how your team runs today and we'll show you the right plan in action." if en else 'أخبرنا كيف يعمل فريقك اليوم وسنعرض لك الخطة المناسبة أثناء العمل.',
     'about': ('About %s'%name) if en else ('عن %s'%name),
     'back': '← Back to all pricing' if en else 'العودة إلى كل الأسعار →',
     'bc_home':'Home' if en else 'الرئيسية','bc_pricing':'Pricing' if en else 'الأسعار',
    }
    faqs_en = [
      ("Can I change plans later?","Yes — move up or down between Starter, Pro, Business, and Enterprise at any time. Changes take effect on your next billing cycle."),
      ("How are users counted?","A user is anyone with a login to %s. You're billed per active user, per month."%name),
      ("Do I need other FulcrumGrid apps?","No. %s works on its own. If you run several apps, the <a href=\"%s\">whole-grid bundle</a> is cheaper than subscribing to each."%(name,pricing)),
      ("Is there a free trial?","Every plan includes a 14-day free trial with full features. No credit card required to start."),
    ]
    faqs_ar = [
      ("هل يمكنني تغيير الخطة لاحقًا؟","نعم — انتقل صعودًا أو نزولًا بين المبتدئة والمتقدّمة والأعمال والمؤسسات في أي وقت، ويسري التغيير في دورة الفوترة التالية."),
      ("كيف يُحتسب المستخدمون؟","المستخدم هو كل من له تسجيل دخول إلى %s. تُحتسب الفوترة لكل مستخدم نشط شهريًا."%name),
      ("هل أحتاج تطبيقات FulcrumGrid الأخرى؟","لا. %s يعمل بمفرده. وإن كنت تشغّل عدّة تطبيقات، فإن <a href=\"%s\">باقة الشبكة كاملة</a> أوفر من الاشتراك في كلٍّ على حدة."%(name,pricing)),
      ("هل توجد تجربة مجانية؟","كل خطة تشمل تجربة مجانية ١٤ يومًا بكامل الميزات، دون بطاقة ائتمان للبدء."),
    ]
    faqs = faqs_en if en else faqs_ar
    faq_html='\n'.join('          <details class="faq-item"><summary>%s</summary><p>%s</p></details>'%(q,a) for q,a in faqs)
    htmlopen = '<html lang="en">' if en else '<html lang="ar" dir="rtl">'
    fonts = ('Inter:wght@400;500;600;700' if en else 'Cairo:wght@400;500;600;700;800')
    skip = 'Skip to content' if en else 'تخطَّ إلى المحتوى'

    # ---- structured data: SoftwareApplication + AggregateOffer + BreadcrumbList ----
    nums=[]; sd_cur=None
    for pen,par in prices:
        m = re.match(r'^(SAR|\$)\s?([\d,]+)$', pen.strip())
        if m:
            nums.append(int(m.group(2).replace(',','')))
            sd_cur = 'SAR' if m.group(1)=='SAR' else 'USD'
    app_ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "FulcrumGrid %s" % name,
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        "url": canon,
        "description": html.unescape(desc),
        "inLanguage": "en" if en else "ar",
        "provider": {"@type": "Organization", "name": "FulcrumGrid", "url": "https://fulcrumgrid.com/"},
    }
    if nums:
        app_ld["offers"] = {
            "@type": "AggregateOffer",
            "priceCurrency": sd_cur,
            "lowPrice": str(min(nums)),
            "highPrice": str(max(nums)),
            "offerCount": str(len(prices)),
            "url": canon,
            "availability": "https://schema.org/InStock",
        }
    bc_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": S['bc_home'], "item": "https://fulcrumgrid.com%s" % home},
            {"@type": "ListItem", "position": 2, "name": S['bc_pricing'], "item": "https://fulcrumgrid.com%s" % pricing},
            {"@type": "ListItem", "position": 3, "name": name, "item": canon},
        ],
    }
    ld_json = '<script type="application/ld+json">%s</script>\n  <script type="application/ld+json">%s</script>' % (
        json.dumps(app_ld, ensure_ascii=False), json.dumps(bc_ld, ensure_ascii=False))

    return '''<!DOCTYPE html>
%s
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  %s

  %s

  <title>%s</title>
  <meta name="description" content="%s" />
  <meta name="theme-color" content="#f0f2ed" />
  <meta name="robots" content="index, follow, max-image-preview:large" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="%s" />
  <meta property="og:description" content="%s" />
  <meta property="og:url" content="%s" />
  <meta property="og:site_name" content="FulcrumGrid" />
  <meta property="og:locale" content="%s" />
  <meta property="og:image" content="%s" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:type" content="image/png" />
  <meta property="og:image:alt" content="%s" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="%s" />

  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/icon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/icon-16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/icon-180.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="canonical" href="%s" />
  <link rel="alternate" hreflang="en" href="%s" />
  <link rel="alternate" hreflang="ar" href="%s" />
  <link rel="alternate" hreflang="x-default" href="%s" />

  %s

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=%s&display=swap" />
  <link href="https://fonts.googleapis.com/css2?family=%s&display=swap" rel="stylesheet" media="print" onload="this.media='all'" />
  <noscript><link href="https://fonts.googleapis.com/css2?family=%s&display=swap" rel="stylesheet" /></noscript>

  <link rel="stylesheet" href="/assets/css/fg.css" />
</head>
<body class="fg">
  <a class="skip-link" href="#main">%s</a>

  <header class="site-header" id="top">
    <div class="header-inner">
      <a class="brand" href="%s" aria-label="%s">
        %s
        %s
      </a>
      <nav class="site-nav" aria-label="Primary">
%s
      </nav>
      <div class="header-cta">
        <div class="lang-switch" role="group" aria-label="Language">
          <a href="/pricing/%s/"%s hreflang="en" lang="en">EN</a>
          <a href="/ar/pricing/%s/"%s hreflang="ar" lang="ar">ع</a>
        </div>
        <a class="btn btn-primary" href="%s">%s</a>
      </div>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="mobile-menu">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="mobile-menu" id="mobile-menu" hidden>
%s
      <a class="btn btn-primary" href="%s">%s</a>
    </div>
  </header>

  <main id="main">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="%s">%s</a><span>/</span><a href="%s">%s</a><span>/</span><span class="current">%s</span>
      </nav>
    </div>

    <section class="product-hero" style="padding-bottom:24px">
      <div class="container">
        <div class="product-hero-inner" style="max-width:760px">
          <p class="product-eyebrow"><span class="tag tag-live" style="padding:3px 10px">%s</span> %s</p>
          <h1>%s <span class="p-grad">%s</span></h1>
          <p class="lead">%s</p>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:8px">
      <div class="container">
        <div class="pricing-grid tiers">
%s
        </div>
        <p class="price-note">%s</p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="sub-head" style="max-width:680px">
          <p class="eyebrow">%s</p>
          <h2>%s</h2>
          <p>%s</p>
        </div>
        <div class="compare-wrap">
          <table class="compare-table">
            <thead>
              <tr><th scope="col">%s</th>%s</tr>
            </thead>
            <tbody>
%s
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">%s</p>
          <h2>%s</h2>
        </div>
        <div class="faq">
%s
        </div>
      </div>
    </section>

    <section class="section section-alt" id="contact">
      <div class="container">
        <div class="cta-panel">
          <div class="cta-content">
            <h2>%s</h2>
            <p>%s</p>
            <div class="hero-actions" style="justify-content:center">
              <a class="btn btn-primary btn-lg" href="%s">%s</a>
              <a class="btn btn-outline btn-lg" href="%s">%s</a>
            </div>
            <p class="cta-alt"><a href="%s">%s</a></p>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <a class="brand" href="%s" aria-label="%s">
          %s
          %s
        </a>
        <p class="footer-tag">%s</p>
      </div>
      <div class="footer-cols">%s</div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year">2026</span> FulcrumGrid. %s</p>
      <p class="footer-domain" dir="ltr">fulcrumgrid.com</p>
    </div>
  </footer>

  <script src="/assets/js/main.js" defer></script>
  <script src="/assets/js/fg.js" defer></script>
  <script src="/assets/js/consent.js" defer></script>
</body>
</html>
''' % (
      htmlopen, CSP, GA, title, desc, title, desc, canon,
      ('en_US' if en else 'ar_AR'), ogimg, ogalt, ogimg, canon, en_url, ar_url, en_url,
      ld_json,
      fonts, fonts, fonts, skip,
      home, aria_home, MARK, brandname, nav(lang,slug),
      slug, (' class="active" aria-current="page"' if en else ''), slug, ('' if en else ' class="active" aria-current="page"'),
      contact, demo,
      nav(lang,slug), contact, demo,
      home, S['bc_home'], pricing, S['bc_pricing'], name,
      avail, name, name, ('pricing' if en else 'الأسعار'), lead,
      cards, S['pricenote'],
      S['whatsin'], S['modbyplan'], S['modsub'], modhdr, colnames, rows,
      S['faq'], S['faqh'], faq_html,
      S['cta_h'], S['cta_p'], contact, demo, product, S['about'], pricing, S['back'],
      home, aria_home, MARKF, brandname, ('The operational backbone for modern teams.' if en else 'العمود الفقري التشغيلي للفرق الحديثة.'),
      footer_cols(lang), ('All rights reserved.' if en else 'جميع الحقوق محفوظة.')
    )

def footer_cols(lang):
    en = lang=='en'
    b = '' if en else '/ar'
    if en:
        return ('<div class="footer-col"><h3>Products</h3><a href="/products/">All products</a><a href="/products/command-center/">Command Center</a><a href="/products/collection/">Collection</a><a href="/products/hr-suite/">HR Suite</a><a href="/custom-apps/">Custom apps</a><a href="/products/coming-soon/">Coming soon</a></div>'
                '<div class="footer-col"><h3>Platform</h3><a href="/features/">Features</a><a href="/how-it-works/">How it works</a><a href="/pricing/">Pricing</a><a href="/blog/">Blog</a></div>'
                '<div class="footer-col"><h3>Company</h3><a href="/about/">About</a><a href="/faq/">FAQ</a><a href="/contact/">Contact</a><a href="mailto:contact@avenlorconsulting.com">Email us</a><a href="/privacy/">Privacy</a><a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting ↗</a></div>')
    return ('<div class="footer-col"><h3>المنتجات</h3><a href="/ar/products/">كل المنتجات</a><a href="/ar/products/command-center/">مركز القيادة</a><a href="/ar/products/collection/">التحصيل</a><a href="/ar/products/hr-suite/">الموارد البشرية</a><a href="/ar/custom-apps/">تطبيقات مخصّصة</a><a href="/ar/products/coming-soon/">قريبًا</a></div>'
            '<div class="footer-col"><h3>المنصّة</h3><a href="/ar/features/">الميزات</a><a href="/ar/how-it-works/">كيف تعمل</a><a href="/ar/pricing/">الأسعار</a><a href="/ar/blog/">المدوّنة</a></div>'
            '<div class="footer-col"><h3>الشركة</h3><a href="/ar/about/">من نحن</a><a href="/ar/faq/">الأسئلة الشائعة</a><a href="/ar/contact/">اتصل بنا</a><a href="mailto:contact@avenlorconsulting.com">راسلنا</a><a href="/ar/privacy/">الخصوصية</a><a href="https://avenlorconsulting.com/ar/" target="_blank" rel="noopener">أفنلور للاستشارات ↗</a></div>')

for slug,d in APPS.items():
    for lang in ('en','ar'):
        p = os.path.join(ROOT, ('' if lang=='en' else 'ar/')+('pricing/%s/index.html'%slug))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p,'w',encoding='utf-8').write(page(slug,d,lang))
        print("wrote", p)

# ---- Real Collection data (from product owner) ----
APPS['collection'] = {
  'en_name':'Collection','ar_name':'التحصيل',
  'tier_names_en':['Starter','Professional','Business','Enterprise / Agency'],
  'tier_names_ar':['المبتدئة','الاحترافية','الأعمال','المؤسسات / الوكالات'],
  'en_lead':"Receivables and collections, priced by plan — from a small in-house AR team to a multi-client agency. Every plan runs on the same secure platform.",
  'ar_lead':"الذمم المدينة والتحصيل، مُسعّرة حسب الخطة — من فريق تحصيل داخلي صغير إلى وكالة متعددة العملاء. وكل الخطط تعمل على المنصة الآمنة نفسها.",
  'en_desc':"Collection pricing plans — Starter, Professional, Business, and Enterprise / Agency — with a module-by-module breakdown of what's included at each tier.",
  'ar_desc':"خطط أسعار التحصيل — المبتدئة والاحترافية والأعمال والمؤسسات / الوكالات — مع تفصيل للوحدات المشمولة في كل خطة.",
  'taglines_en':["Small in-house AR teams","Growing collection teams","Large ops / compliance-heavy","Collection agencies &amp; multi-client"],
  'taglines_ar':["فرق تحصيل داخلية صغيرة","فرق تحصيل متنامية","عمليات كبيرة / كثيفة الامتثال","وكالات تحصيل ومتعددة العملاء"],
  'tiers_en':[
    ["Debtors, accounts, invoices &amp; payments","Workspace · tasks · promises · disputes","Dashboard · audit trail · MFA","3 seats · email support"],
    ["Everything in Starter","Strategies &amp; templates automation","Custom roles (RBAC), approvals / SoD, import","Advanced analytics · 15 seats · priority"],
    ["Everything in Professional","Legal &amp; tiered settlements","Integrations: API, REST v1, webhooks, sandbox","Custom domain · unlimited seats · SLA"],
    ["Everything in Business","Agency mode: creditors + trust accounting","Creditor portal · per-tenant subdomains","Unlimited seats · dedicated support"]],
  'tiers_ar':[
    ["المدينون والحسابات والفواتير والمدفوعات","مساحة العمل · المهام · الوعود · المنازعات","لوحة المعلومات · سجل التدقيق · المصادقة الثنائية","٣ مقاعد · دعم بالبريد"],
    ["كل ما في المبتدئة","الاستراتيجيات والقوالب (أتمتة)","أدوار مخصّصة (RBAC)، موافقات / فصل المهام، استيراد","تحليلات متقدّمة · ١٥ مقعدًا · أولوية"],
    ["كل ما في الاحترافية","القضايا القانونية والتسويات المتدرّجة","تكاملات: مفاتيح API، REST v1، Webhooks، بيئة اختبار","نطاق مخصّص · مقاعد بلا حدود · SLA"],
    ["كل ما في الأعمال","وضع الوكالة: الدائنون + محاسبة الأمانات","بوابة الدائن · نطاقات فرعية لكل مستأجر","مقاعد بلا حدود · دعم مخصّص"]],
  'matrix':[
    (("Debtors · Accounts · Invoices · Payments","المدينون · الحسابات · الفواتير · المدفوعات"),'y','y','y','y'),
    (("Workspace · Tasks · Promises · Disputes","مساحة العمل · المهام · الوعود · المنازعات"),'y','y','y','y'),
    (("Dashboard · audit trail · MFA","لوحة المعلومات · سجل التدقيق · المصادقة الثنائية"),'y','y','y','y'),
    (("Email + debtor portal","البريد + بوابة المدين"),'y','y','y','y'),
    (("Custom branding","علامة تجارية مخصّصة"),'n','y','y','y'),
    (("Strategies + Templates (automation)","الاستراتيجيات + القوالب (أتمتة)"),'n','y','y','y'),
    (("Custom Roles (RBAC) · Approvals/SoD · Import","أدوار مخصّصة (RBAC) · موافقات/فصل المهام · استيراد"),'n','y','y','y'),
    (("Advanced analytics (A/B, forecast)","تحليلات متقدّمة (A/B، تنبّؤ)"),'n','y','y','y'),
    (("Legal · Settlements (tiered)","القضايا القانونية · التسويات (متدرّجة)"),'n','n','y','y'),
    (("Integrations: API keys · REST v1 · webhooks · sandbox","تكاملات: مفاتيح API · REST v1 · Webhooks · بيئة اختبار"),'n','n','y','y'),
    (("Custom domain","نطاق مخصّص"),'n','n','y','y'),
    (("Agency mode: Creditors + Trust accounting","وضع الوكالة: الدائنون + محاسبة الأمانات"),'n','n','n','y'),
    (("Creditor portal · per-tenant subdomains","بوابة الدائن · نطاقات فرعية لكل مستأجر"),'n','n','n','y'),
    (("Seats / support","المقاعد / الدعم"),("3 seats · email","٣ مقاعد · بريد"),("15 seats · priority","١٥ مقعدًا · أولوية"),("Unlimited · SLA","بلا حدود · SLA"),("Unlimited · dedicated","بلا حدود · مخصّص")),
  ],
}
APPS['collection'] = load_app('collection', APPS['collection'])
for lang in ('en','ar'):
    p = os.path.join(ROOT, ('' if lang=='en' else 'ar/')+'pricing/collection/index.html')
    open(p,'w',encoding='utf-8').write(page('collection', APPS['collection'], lang))
    print('regenerated', p)

# ---- Real Command Center data (from product owner) ----
APPS['command-center'] = {
  'en_name':'Command Center','ar_name':'مركز القيادة',
  'tier_names_en':['Pilot','Growth','Enterprise'],
  'tier_names_ar':['التجريبية','النمو','المؤسسات'],
  'prices':[('SAR 490','SAR 490'),('SAR 1,900','SAR 1,900'),('Custom','مخصّص')],
  'per_en':'/ month','per_ar':'/ شهريًا','popular_index':1,
  'pricenote_en':"Flat monthly price per organization (suggested). Annual billing saves 20%. Every plan includes a 14-day free trial.",
  'pricenote_ar':"سعر شهري ثابت لكل مؤسسة (مقترح). الدفع السنوي يوفّر ٢٠٪. كل خطة تشمل تجربة مجانية ١٤ يومًا.",
  'en_lead':"Run strategy, finance, and governance from one command center — priced by plan, from a piloting team to a multi-department, regulated organization.",
  'ar_lead':"أدِر الاستراتيجية والمالية والحوكمة من مركز قيادة واحد — مُسعّر حسب الخطة، من فريق تجريبي إلى مؤسسة متعددة الأقسام وخاضعة للتنظيم.",
  'en_desc':"Command Center pricing — Pilot, Growth, and Enterprise plans — with a module-by-module breakdown of what's included at each tier.",
  'ar_desc':"أسعار مركز القيادة — خطط التجريبية والنمو والمؤسسات — مع تفصيل للوحدات المشمولة في كل خطة.",
  'taglines_en':["Small team piloting","Scaling company","Multi-dept / regulated"],
  'taglines_ar':["فريق صغير في مرحلة تجريبية","شركة في مرحلة توسّع","متعددة الأقسام / خاضعة للتنظيم"],
  'tiers_en':[
    ["Up to 10 users · 3 departments","Strategy: OKRs, KPIs, projects","Finance: P&amp;L, BS, cash flow, budget","Compliance · email support"],
    ["Up to 50 users · unlimited departments","Everything in Pilot + risk","AI assistant, auto-summary &amp; anomalies","1 ERP connection · innovation pipeline"],
    ["Unlimited users &amp; departments","Unlimited + scheduled ERP pull","Custom domain + your TLS","SLA + onboarding · log export"]],
  'tiers_ar':[
    ["حتى ١٠ مستخدمين · ٣ أقسام","الاستراتيجية: OKRs، KPIs، المشاريع","المالية: الأرباح والخسائر، الميزانية، التدفق النقدي، الموازنة","الامتثال · دعم بالبريد"],
    ["حتى ٥٠ مستخدمًا · أقسام بلا حدود","كل ما في التجريبية + المخاطر","مساعد ذكي، ملخّص تلقائي ورصد الشذوذ","اتصال ERP واحد · خط ابتكار"],
    ["مستخدمون وأقسام بلا حدود","سحب ERP بلا حدود ومجدول","نطاق مخصّص مع TLS الخاص بك","SLA وتأهيل · تصدير السجل"]],
  'matrix':[
    (("Users","المستخدمون"),("up to 10","حتى ١٠"),("up to 50","حتى ٥٠"),("Unlimited","بلا حدود")),
    (("Departments","الأقسام"),("3","٣"),("Unlimited","بلا حدود"),("Unlimited","بلا حدود")),
    (("Strategy (OKRs, KPIs, Projects)","الاستراتيجية (OKRs، KPIs، المشاريع)"),'y','y','y'),
    (("Finance (P&amp;L, BS, CF, Budget)","المالية (الأرباح، الميزانية، التدفق، الموازنة)"),'y','y','y'),
    (("Governance (Compliance + Risk)","الحوكمة (الامتثال + المخاطر)"),("Compliance only","الامتثال فقط"),("Both","كلاهما"),("Both","كلاهما")),
    (("Innovation pipeline","خط الابتكار"),'n','y','y'),
    (("AI assistant + auto-summary + anomalies","مساعد ذكي + ملخّص تلقائي + رصد الشذوذ"),'n','y','y'),
    (("ERP integrations (SAP · QBO · Odoo · Oracle)","تكاملات ERP (SAP · QBO · Odoo · Oracle)"),'n',("1 connection","اتصال واحد"),("Unlimited + scheduled pull","بلا حدود + سحب مجدول")),
    (("Contracts, Loans &amp; Rents","العقود والقروض والإيجارات"),'n','y','y'),
    (("Announcements / broadcast","الإعلانات / البثّ"),("Notify only","إشعار فقط"),("+ Require-ack","+ إلزام بالإقرار"),("+ Require-ack","+ إلزام بالإقرار")),
    (("Branded domain","نطاق بعلامتك"),("Shared apex","نطاق مشترك"),("Subdomain","نطاق فرعي"),("Custom + TLS","مخصّص + TLS")),
    (("Activity log retention","مدة حفظ سجل النشاط"),("30 days","٣٠ يومًا"),("1 year","سنة واحدة"),("Unlimited + export","بلا حدود + تصدير")),
    (("Support","الدعم"),("Email","بريد"),("Priority","أولوية"),("SLA + onboarding","SLA + تأهيل")),
  ],
}
APPS['command-center'] = load_app('command-center', APPS['command-center'])
for lang in ('en','ar'):
    p = os.path.join(ROOT, ('' if lang=='en' else 'ar/')+'pricing/command-center/index.html')
    open(p,'w',encoding='utf-8').write(page('command-center', APPS['command-center'], lang))
    print('regenerated', p)

# ---- Real HR Suite data (from product owner) ----
K = '<span class="ksa">KSA</span>'
APPS['hr-suite'] = {
  'en_name':'HR Suite','ar_name':'منظومة الموارد البشرية',
  'tier_names_en':['Essentials','Operations','Payroll & Compliance','Enterprise'],
  'tier_names_ar':['الأساسية','العمليات','الرواتب والامتثال','المؤسسات'],
  'prices':[('SAR 15','SAR 15'),('SAR 28','SAR 28'),('SAR 45','SAR 45'),('Custom','مخصّص')],
  'per_en':'/ seat / mo','per_ar':'/ لكل مقعد شهريًا','popular_index':1,
  'badge_labels':{1:('Most popular','الأكثر شيوعًا'),2:('Best for KSA','الأنسب للسعودية')},
  'pricenote_en':"Per seat, per month (suggested). Core HR is included free on every plan. Every plan includes a 14-day free trial.",
  'pricenote_ar':"لكل مقعد شهريًا (مقترح). الموارد البشرية الأساسية مشمولة مجانًا في كل خطة. كل خطة تشمل تجربة مجانية ١٤ يومًا.",
  'modsub_en':"Every HR Suite module, and where it unlocks across the four plans.  ✓ included · ＋ available as an add-on · KSA = Saudi compliance. Tiers are cumulative.",
  'modsub_ar':"كل وحدة في منظومة الموارد البشرية، وأين تتوفّر عبر الخطط الأربع.  ✓ مشمول · ＋ متاح كإضافة · KSA = امتثال سعودي. الخطط تراكمية.",
  'en_lead':"HR from hire to retire — 35 modules on one platform, with Core HR always on. Priced per seat, packaged into four plans plus à-la-carte add-ons.",
  'ar_lead':"الموارد البشرية من التعيين إلى التقاعد — ٣٥ وحدة على منصة واحدة، مع تفعيل الموارد البشرية الأساسية دائمًا. تُسعّر لكل مقعد، ومُجمّعة في أربع خطط مع إضافات اختيارية.",
  'en_desc':"HR Suite pricing — Essentials, Operations, Payroll & Compliance, and Enterprise — with a module-by-module breakdown, including Saudi payroll and compliance.",
  'ar_desc':"أسعار منظومة الموارد البشرية — الأساسية والعمليات والرواتب والامتثال والمؤسسات — مع تفصيل للوحدات، بما في ذلك الرواتب والامتثال السعودي.",
  'taglines_en':["Small teams getting HR in order","A real HR function, day to day","Saudi payroll done right","Everything, at any scale"],
  'taglines_ar':["فرق صغيرة تنظّم مواردها البشرية","وظيفة موارد بشرية حقيقية يوميًا","رواتب سعودية بإتقان","كل شيء، بأي حجم"],
  'tiers_en':[
    ["Up to 25 people","Time off &amp; HR requests","Expenses &amp; documents","Announcements &amp; recognition"],
    ["Up to 100 people","Attendance &amp; timesheets","Performance reviews","Assets, helpdesk &amp; contracts"],
    ["Up to 250 people","Payroll + WPS bank file","GOSI &amp; end-of-service","Nitaqat &amp; analytics"],
    ["Unlimited people","Recruitment &amp; careers page","Learning (LMS) &amp; surveys","SSO / SCIM &amp; SAP"]],
  'tiers_ar':[
    ["حتى ٢٥ فردًا","الإجازات وطلبات الموارد البشرية","النفقات والمستندات","الإعلانات والتقدير"],
    ["حتى ١٠٠ فرد","الحضور وسجلّات الدوام","تقييمات الأداء","الأصول والدعم والعقود"],
    ["حتى ٢٥٠ فردًا","الرواتب + ملف WPS","التأمينات ونهاية الخدمة","نطاقات والتحليلات"],
    ["أفراد بلا حدود","التوظيف وصفحة الوظائف","التعلّم (LMS) والاستبيانات","SSO / SCIM و SAP"]],
  'matrix':[
    ('__grp__',("Always included","مشمولة دائمًا")),
    (("Core HR "+K,"الموارد البشرية الأساسية "+K),'y','y','y','y'),
    ('__grp__',("People &amp; everyday self-service","الأفراد والخدمة الذاتية اليومية")),
    (("Time off","الإجازات"),'y','y','y','y'),
    (("HR requests","طلبات الموارد البشرية"),'y','y','y','y'),
    (("Expenses","النفقات"),'y','y','y','y'),
    (("Documents &amp; e-sign","المستندات والتوقيع الإلكتروني"),'y','y','y','y'),
    (("HR letters","خطابات الموارد البشرية"),'y','y','y','y'),
    (("Announcements","الإعلانات"),'y','y','y','y'),
    (("Recognition","التقدير"),'y','y','y','y'),
    (("Probation","فترة التجربة"),'y','y','y','y'),
    (("Onboarding","التأهيل"),'y','y','y','y'),
    ('__grp__',("Time, attendance &amp; operations","الوقت والحضور والعمليات")),
    (("Time &amp; attendance","الوقت والحضور"),'+','y','y','y'),
    (("Overtime","العمل الإضافي"),'+','y','y','y'),
    (("Credential tracking","تتبّع الوثائق"),'+','y','y','y'),
    (("Bulk renewals","التجديدات المجمّعة"),'+','y','y','y'),
    (("Employment contracts","عقود العمل"),'+','y','y','y'),
    (("Assets","الأصول"),'+','y','y','y'),
    (("HR helpdesk","مكتب دعم الموارد البشرية"),'+','y','y','y'),
    (("Disciplinary","الإجراءات التأديبية"),'+','y','y','y'),
    (("Benefits","المزايا"),'+','y','y','y'),
    (("Performance","الأداء"),'+','y','y','y'),
    (("Positions / establishment","الوظائف / الملاك"),'+','y','y','y'),
    ('__grp__',("Payroll &amp; Saudi compliance","الرواتب والامتثال السعودي")),
    (("Payroll (+ WPS) "+K,"الرواتب (+ WPS) "+K),'+','+','y','y'),
    (("GOSI "+K,"التأمينات الاجتماعية "+K),'+','+','y','y'),
    (("End-of-service (EOSB) "+K,"نهاية الخدمة (EOSB) "+K),'+','+','y','y'),
    (("Housing advance "+K,"سلفة السكن "+K),'+','+','y','y'),
    (("Compensation review","مراجعة التعويضات"),'+','+','y','y'),
    (("Analytics &amp; Nitaqat "+K,"التحليلات ونطاقات "+K),'+','+','y','y'),
    ('__grp__',("Talent, engagement &amp; integrations","المواهب والتفاعل والتكاملات")),
    (("Recruitment (ATS)","التوظيف (ATS)"),'+','+','+','y'),
    (("Careers page","صفحة الوظائف"),'+','+','+','y'),
    (("Succession &amp; development","التعاقب والتطوير"),'+','+','+','y'),
    (("Engagement surveys","استبيانات التفاعل"),'+','+','+','y'),
    (("Learning (LMS)","التعلّم (LMS)"),'+','+','+','y'),
    (("AI helper","المساعد الذكي"),'+','+','+','y'),
    (("SSO &amp; SCIM","SSO و SCIM"),'+','+','+','y'),
    (("SAP Business One","SAP Business One"),'+','+','+','y'),
  ],
}
APPS['hr-suite'] = load_app('hr-suite', APPS['hr-suite'])
for lang in ('en','ar'):
    p = os.path.join(ROOT, ('' if lang=='en' else 'ar/')+'pricing/hr-suite/index.html')
    open(p,'w',encoding='utf-8').write(page('hr-suite', APPS['hr-suite'], lang))
    print('regenerated', p)
