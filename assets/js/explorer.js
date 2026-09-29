/* FulcrumGrid redesign — "Inside each app" module explorer.
   Tab-switches between apps and renders each app's module grid. Content is the
   real product module set. No framework; CSP safe. */
(function () {
  'use strict';
  var APPS = {
    cc: {
      name: 'Command Center', tag: 'Operations',
      line: 'Real-time operations dashboard. Monitor every metric, workflow, and alert across your business from one screen.',
      price: 'From SAR 490 / mo', href: '/products/command-center/',
      modules: ['OKRs', 'KPIs', 'Projects', 'P&L', 'Balance sheet', 'Cash flow', 'Budget', 'Compliance', 'Risk', 'Innovation pipeline', 'AI assistant', 'Anomaly alerts', 'ERP integrations', 'Contracts, loans & rents', 'Announcements']
    },
    col: {
      name: 'Collection', tag: 'Receivables',
      line: 'Receivables and payments, handled. Track invoices, automate reminders, and get paid faster without the chase.',
      price: 'Starter free · from SAR 370 / mo', href: '/products/collection/',
      modules: ['Debtors & accounts', 'Invoices & payments', 'Tasks & promises', 'Disputes', 'Debtor portal', 'Strategies & templates', 'Custom roles (RBAC)', 'Approvals / SoD', 'Advanced analytics', 'SAP Business One', 'Legal & settlements', 'REST API & webhooks', 'Agency mode', 'Trust accounting', 'Creditor portal']
    },
    hr: {
      name: 'HR Suite', tag: 'People',
      line: 'People operations from hire to retire. Manage employees, payroll, time off, and everything in between.',
      price: 'From SAR 5 / seat / mo', href: '/products/hr-suite/',
      modules: ['Core HR', 'Time off', 'Expenses', 'HR letters', 'Onboarding', 'Documents & e-sign', 'Time & attendance', 'Overtime', 'Employment contracts', 'Assets', 'HR helpdesk', 'Benefits', 'Performance', 'Payroll', 'GOSI', 'End-of-service', 'Recruitment (ATS)', 'Learning (LMS)', 'Engagement surveys', 'AI helper', 'SSO & SCIM', 'SAP Business One', '+ 13 more modules']
    }
  };

  var panel = document.querySelector('[data-exp-panel]');
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.exp-tab'));
  if (!panel || !tabs.length) return;

  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function pad(n) { return String(n).padStart(2, '0'); }

  function render(key) {
    var a = APPS[key]; if (!a) return;
    var mods = a.modules.map(function (m, i) {
      var n = m.charAt(0) === '+' ? '' : pad(i + 1);
      return '<div class="mod"><span class="mn">' + n + '</span><span>' + esc(m) + '</span></div>';
    }).join('');
    panel.innerHTML =
      '<div class="top">' +
        '<div><span class="tag tag-outline">' + esc(a.tag) + '</span>' +
        '<h3>' + esc(a.name) + '</h3></div>' +
        '<div style="text-align:right"><div class="price">' + esc(a.price) + '</div>' +
        '<a class="go" href="' + a.href + '" style="color:var(--color-accent);text-decoration:none;font-weight:600">See ' + esc(a.name) + ' →</a></div>' +
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
