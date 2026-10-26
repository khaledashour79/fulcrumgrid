/* FulcrumGrid redesign — "Inside each app" module explorer.
   Tab-switches between apps and renders each app's module grid. Content is the
   real product module set. No framework; CSP safe.
   Arabic pages (lang="ar") get the localized data set below; English and the
   European locales keep the English names. */
(function () {
  'use strict';
  var APPS = {
    cc: {
      name: 'Command Center', tag: 'Operations',
      line: 'Real-time operations dashboard. Monitor every metric, workflow, and alert across your business from one screen.',
      price: 'From SAR 490 / mo', href: '/products/command-center/',
      modules: ['OKRs', 'KPIs', 'Projects', 'Tasks', 'Approvals', 'P&L', 'Balance sheet', 'Cash flow', 'Budget', 'Compliance', 'Risk', 'Innovation pipeline', 'AI assistant', 'Anomaly alerts', 'ERP integrations', 'Slack & Teams alerts', 'REST API & webhooks', 'SSO (OIDC)', 'Contracts, loans & rents', 'Announcements', 'Business cards']
    },
    col: {
      name: 'Collection', tag: 'Receivables',
      line: 'Receivables and payments, handled. Track invoices, automate reminders, and get paid faster without the chase.',
      price: 'Starter free · from SAR 370 / mo', href: '/products/collection/',
      modules: ['Debtors & accounts', 'Invoices & payments', 'Tasks & promises', 'Disputes', 'Debtor portal', 'Field visits', 'Strategies & templates', 'Custom roles (RBAC)', 'Approvals / SoD', 'Advanced analytics', 'AI add-on', 'ERP connectors', 'Cheque register', 'Legal & settlements', 'SSO (OIDC)', 'REST API & webhooks', 'Agency mode', 'Trust accounting', 'Creditor portal']
    },
    hr: {
      name: 'HR Suite', tag: 'People',
      line: 'People operations from hire to retire. Manage employees, payroll, time off, and everything in between.',
      price: 'From SAR 5 / seat / mo', href: '/products/hr-suite/',
      modules: ['Core HR', 'Time off', 'Expenses', 'HR letters', 'Onboarding', 'Documents & e-sign', 'Time & attendance', 'Overtime', 'Employment contracts', 'Assets', 'HR helpdesk', 'Benefits', 'Performance', 'Payroll', 'Statutory & local compliance', 'Recruitment (ATS)', 'Candidate portal', 'Learning (LMS)', 'Learning providers', 'Engagement surveys', 'Approval workflows', 'Policy Library', 'Business travel', 'Report builder', 'Mobile app', 'Document requests', 'Company news', 'Video interviews', 'Sales commissions', 'AI Copilot & Agents', 'SSO & SCIM', 'SAP Business One', 'End-of-service (EOSB)', 'GOSI', 'Saudization (Nitaqat)', 'Loans & advances', 'Credentials & expiry', 'Probation', 'Disciplinary', 'Recognition', 'Compensation review', 'Succession', 'Positions', 'HR analytics', 'Offboarding & clearance', 'Grievances', 'Performance plans (PIP)', 'Air tickets', 'Iqama renewal', 'Exit & re-entry visas', 'Overseas hiring', 'Total rewards', 'Medical insurance', 'Data rights (DSAR)', 'Interview scheduling', 'Daftara', 'Partner API', 'Custom domain', '+ more modules']
    },
    tms: {
      name: 'TMS', tag: 'Logistics',
      line: 'Logistics operations and finance on one grid. Forwarding, transport, yard, parcel and warehousing, with the books built in.',
      price: 'Talk to sales', href: '/products/tms/',
      modules: ['Finance (GL · AR · AP)', 'VAT engine', 'Freight forwarding', 'Customs clearance', 'Transport & fleet', 'Container yard', 'Parcel & express', 'Warehousing / 3PL', 'Purchasing & inventory', 'Maintenance & workshop', 'ERP connectors', 'SSO & REST API']
    },
    assure: {
      name: 'Assure', tag: 'Compliance',
      line: 'Governance, risk and compliance, built for Saudi regulation. Obligations mapped to controls, with the evidence trail to match.',
      price: 'Talk to sales', href: '/products/assure/',
      modules: ['Obligations register', 'Entities & scope gate', 'Controls & crosswalk', 'Self-assessment', 'Risk register', 'Authorized scanning', 'Cloud posture (CSPM)', 'PDPL (DSAR & RoPA)', 'Vendor risk (TPRM)', 'Incidents', 'Attestations', 'My Work', 'KRIs & dashboard', 'Posture trends', 'Reports & exports', 'Policies', 'Evidence vault', 'SSO & API tokens', 'Roles & permissions', 'Audit log']
    },
    close: {
      name: 'Close', tag: 'Finance',
      line: 'IFRS period-end estimates. IAS 19, IFRS 9 and IFRS 16, with versioned assumptions and a full audit trail.',
      price: 'Talk to sales', href: '/products/close/',
      modules: ['IAS 19 (end-of-service)', 'IFRS 9 (ECL)', 'IFRS 16 (leases)', 'Reporting periods', 'Input snapshots', 'Versioned assumptions', 'Reproducible runs', 'Segregation of duties', 'Actuary sign-off', 'Journal vouchers', 'Audit pack', 'Access log']
    },
    consolidate: {
      name: 'Consolidate', tag: 'Finance',
      line: 'Consolidated commercial and financial KPIs across every company you run, read from your books into one operator dashboard.',
      price: 'Talk to sales', href: '/products/consolidate/',
      modules: ['Daftra source', 'Consolidated KPIs', 'AR ageing', 'P&L snapshot', 'VAT & ZATCA status', 'MRR & pipeline', 'Client cohorts', 'Top clients', 'Base-currency FX', 'Per-company drill-in', 'Nightly snapshots', 'Encrypted keys', 'SSRF-hardened egress', 'Operator token', 'PWA & push']
    }
  };

  var APPS_AR = {
    cc: {
      name: 'لوحة التحكم للتنفيذيين', tag: 'العمليات',
      line: 'لوحة عمليات فورية. راقب كل مقياس وسير عمل وتنبيه عبر أعمالك من شاشة واحدة.',
      price: 'من 490 ريال / شهريًا', href: '/ar/products/command-center/',
      modules: ['الأهداف والنتائج (OKRs)', 'مؤشرات الأداء (KPIs)', 'المشاريع', 'المهام', 'الموافقات', 'الأرباح والخسائر', 'الميزانية العمومية', 'التدفّق النقدي', 'الموازنة', 'الامتثال', 'المخاطر', 'مسار الابتكار', 'المساعد الذكي', 'تنبيهات الشذوذ', 'تكاملات ERP', 'تنبيهات Slack و Teams', 'REST API و webhooks', 'الدخول الموحّد (OIDC)', 'العقود والقروض والإيجارات', 'الإعلانات', 'بطاقات العمل']
    },
    col: {
      name: 'منصة تحصيل الديون', tag: 'الذمم',
      line: 'الذمم والمدفوعات، مُدارة. تتبّع الفواتير وأتمت التذكيرات واحصل على مستحقّاتك أسرع دون مطاردة.',
      price: 'الباقة الأساسية مجانية · من 370 ريال / شهريًا', href: '/ar/products/collection/',
      modules: ['المدينون والحسابات', 'الفواتير والمدفوعات', 'المهام والوعود', 'النزاعات', 'بوابة المدين', 'الزيارات الميدانية', 'الاستراتيجيات والقوالب', 'أدوار مخصّصة (RBAC)', 'الموافقات / فصل المهام (SoD)', 'تحليلات متقدّمة', 'إضافة الذكاء الاصطناعي', 'موصلات ERP', 'سجل الشيكات', 'الشؤون القانونية والتسويات', 'الدخول الموحّد (OIDC)', 'REST API و webhooks', 'وضع الوكالة', 'محاسبة الأمانات', 'بوابة الدائن']
    },
    hr: {
      name: 'منصة الموارد البشرية', tag: 'الأفراد',
      line: 'عمليات الأفراد من التعيين إلى التقاعد. أدِر الموظفين والرواتب والإجازات وكل ما بينهما.',
      price: 'من 5 ريال / مقعد / شهريًا', href: '/ar/products/hr-suite/',
      modules: ['الموارد البشرية الأساسية', 'الإجازات', 'المصروفات', 'خطابات الموارد البشرية', 'التأهيل', 'المستندات والتوقيع الإلكتروني', 'الوقت والحضور', 'العمل الإضافي', 'عقود العمل', 'العُهد والأصول', 'مكتب خدمة الموارد البشرية', 'المزايا', 'الأداء', 'الرواتب', 'الامتثال النظامي والمحلي', 'التوظيف (ATS)', 'بوابة المتقدّمين', 'التعلّم (LMS)', 'مزوّدو التعلّم', 'استبيانات التفاعل', 'مسارات الموافقات', 'مكتبة السياسات', 'سفر الأعمال', 'منشئ التقارير', 'تطبيق الجوال', 'طلبات المستندات', 'أخبار الشركة', 'المقابلات المرئية', 'عمولات المبيعات', 'المساعد الذكي والوكلاء', 'SSO و SCIM', 'SAP Business One', 'نهاية الخدمة', 'التأمينات الاجتماعية (GOSI)', 'السعودة (نطاقات)', 'القروض والسلف', 'الوثائق وانتهاؤها', 'فترة التجربة', 'الإجراءات التأديبية', 'التقدير', 'مراجعة التعويضات', 'التعاقب الوظيفي', 'الوظائف والمِلاك', 'تحليلات الموارد البشرية', 'إنهاء الخدمة والإخلاء', 'التظلّمات', 'خطط تحسين الأداء', 'تذاكر الطيران', 'تجديد الإقامة', 'تأشيرات الخروج والعودة', 'الاستقدام من الخارج', 'إجمالي المكافآت', 'التأمين الطبي', 'حقوق البيانات (DSAR)', 'جدولة المقابلات', 'دفترة', 'واجهة الشركاء (API)', 'نطاق مخصّص', '+ المزيد من الوحدات']
    },
    tms: {
      name: 'منصة العمليات اللوجستية', tag: 'اللوجستيات',
      line: 'عمليات لوجستية ومالية على شبكة واحدة. الشحن والنقل والساحة والطرود والتخزين، مع الحسابات مدمجة.',
      price: 'تواصل مع المبيعات', href: '/ar/products/tms/',
      modules: ['المالية (دفتر الأستاذ · المدينون · الدائنون)', 'محرك ضريبة القيمة المضافة', 'الشحن والتخليص', 'التخليص الجمركي', 'النقل والأسطول', 'ساحة الحاويات', 'الطرود والتوصيل السريع', 'التخزين / الطرف الثالث', 'المشتريات والمخزون', 'الصيانة والورشة', 'موصلات ERP', 'الدخول الموحّد و REST API']
    },
    assure: {
      name: 'منصة الحوكمة والامتثال', tag: 'الامتثال',
      line: 'الحوكمة والمخاطر والامتثال، مبنية للتنظيم السعودي. الالتزامات مرتبطة بالضوابط، مع سجلّ أدلّة مطابق.',
      price: 'تواصل مع المبيعات', href: '/ar/products/assure/',
      modules: ['سجل الالتزامات', 'الكيانات وبوابة النطاق', 'الضوابط والربط المرجعي', 'التقييم الذاتي', 'سجل المخاطر', 'الفحص المُصرَّح', 'الوضع السحابي (CSPM)', 'حماية البيانات (DSAR و RoPA)', 'مخاطر الموردين (TPRM)', 'الحوادث', 'الإقرارات', 'مهامّي', 'المؤشرات واللوحة', 'اتجاهات الوضع', 'التقارير والتصدير', 'السياسات', 'خزنة الأدلّة', 'الدخول الموحّد ومفاتيح الواجهة', 'الأدوار والصلاحيات', 'سجل التدقيق']
    },
    close: {
      name: 'منصة المعايير المحاسبية والإغلاق', tag: 'المالية',
      line: 'تقديرات إقفال الفترة وفق IFRS. المعايير IAS 19 و IFRS 9 و IFRS 16، مع افتراضات مُؤرشَفة وسجل تدقيق كامل.',
      price: 'تواصل مع المبيعات', href: '/ar/products/close/',
      modules: ['IAS 19 (نهاية الخدمة)', 'IFRS 9 (خسائر ائتمانية)', 'IFRS 16 (الإيجارات)', 'فترات التقرير', 'لقطات المدخلات', 'افتراضات مُؤرشَفة', 'عمليات قابلة للتكرار', 'فصل المهام', 'اعتماد الخبير الاكتواري', 'قيود اليومية', 'حزمة التدقيق', 'سجل الوصول']
    },
    consolidate: {
      name: 'منصة التوحيد المالي', tag: 'المالية',
      line: 'مؤشرات تجارية ومالية موحَّدة عبر كل شركة تُديرها، مقروءة من دفاترك إلى لوحة مُشغِّل واحدة.',
      price: 'تواصل مع المبيعات', href: '/ar/products/consolidate/',
      modules: ['مصدر دفترة', 'مؤشرات موحَّدة', 'أعمار الذمم', 'لمحة الأرباح والخسائر', 'ضريبة القيمة المضافة وحالة ZATCA', 'الإيراد المتكرّر وخط الأنابيب', 'شرائح العملاء', 'أفضل العملاء', 'صرف بعملة الأساس', 'التعمّق في كل شركة', 'لقطات ليلية', 'مفاتيح مشفّرة', 'حماية SSRF', 'رمز المُشغِّل', 'تطبيق ويب وإشعارات']
    }
  };

  var isAR = (document.documentElement.lang || '').toLowerCase().indexOf('ar') === 0;
  var DATA = isAR ? APPS_AR : APPS;
  var SEE = isAR ? 'استكشف ' : 'See ';
  var ARROW = isAR ? ' ←' : ' →';

  var panel = document.querySelector('[data-exp-panel]');
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.exp-tab'));
  if (!panel || !tabs.length) return;

  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function pad(n) { return String(n).padStart(2, '0'); }

  function render(key) {
    var a = DATA[key]; if (!a) return;
    var mods = a.modules.map(function (m, i) {
      var n = m.charAt(0) === '+' ? '' : pad(i + 1);
      return '<div class="mod"><span class="mn">' + n + '</span><span>' + esc(m) + '</span></div>';
    }).join('');
    panel.innerHTML =
      '<div class="top">' +
        '<div><span class="tag tag-outline">' + esc(a.tag) + '</span>' +
        '<h3>' + esc(a.name) + '</h3></div>' +
        '<div style="text-align:right"><div class="price">' + esc(a.price) + '</div>' +
        '<a class="go" href="' + a.href + '" style="color:var(--color-accent);text-decoration:none;font-weight:600">' + SEE + esc(a.name) + ARROW + '</a></div>' +
      '</div>' +
      '<p class="text-muted" style="max-width:56ch">' + esc(a.line) + '</p>' +
      '<div class="mods">' + mods + '</div>';
  }

  tabs.forEach(function (t) {
    t.addEventListener('click', function () {
      tabs.forEach(function (x) { x.setAttribute('aria-selected', 'false'); });
      t.setAttribute('aria-selected', 'true');
      render(t.getAttribute('data-exp'));
    });
  });
  render('hr');
})();
