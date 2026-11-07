/* FulcrumGrid — HR Time & Cost Savings Calculator
 *
 * Client-side only. No data collection, no network calls, no third-party
 * tracking. Inputs persist to localStorage as a per-viewer convenience.
 *
 * All assumptions live in CONFIG (one maintainable place, calibrate after
 * pilots). The core computeResults() is a pure function, unit-tested in Node
 * (see scripts/build/calc_check.js); the DOM wiring only runs in a browser.
 */
(function () {
  'use strict';

  // ---- One maintainable configuration -------------------------------------
  var CONFIG = {
    // Illustrative fallback assumptions for "Not sure — use an estimate".
    // These are calculator assumptions, NOT industry benchmarks or results.
    fallback: {
      hiresPctOfHeadcount: 0.12,   // annual hires = 12% of headcount
      appsPerVacancy: 50,          // applications per vacancy
      iqamaPctOfHeadcount: 0.80,   // annual Iqama renewals = 80% of headcount
      lettersPctOfHeadcount: 0.20  // monthly letters = 20% of headcount
    },
    // Minutes per activity: manual vs with the platform (remaining human review).
    activities: {
      cvScreen:  { manual: 5,  platform: 1  },  // initial CV screening
      interview: { manual: 25, platform: 12 },  // initial interview vs recorded-interview review
      payroll:   { manual: 8,  platform: 3  },  // payroll prep per employee per monthly cycle
      iqama:     { manual: 40, platform: 20 },  // Iqama renewal administration
      letters:   { manual: 10, platform: 2  }   // employee letter prep & delivery
    },
    interviewsPerHire: 12,
    staffCostMonthly: 12000,  // SAR, fully loaded
    productiveHours: 160,     // productive staff hours per month
    realization: 0.80         // expected realization / adoption factor (0..1)
  };

  // ---- Pure calculation engine --------------------------------------------
  // input: { employees, annualHires, appsPerVacancy, iqamaRenewals,
  //          monthlyLetters, enabled:{recruitment,payroll,iqama,letters},
  //          cfg:<CONFIG-shaped> }
  function hoursReleased(volume, manual, platform, realization) {
    return volume * (manual - platform) / 60 * realization;
  }

  function computeResults(input) {
    var cfg = input.cfg;
    var en = input.enabled || { recruitment: true, payroll: true, iqama: true, letters: true };
    var r = cfg.realization;
    var hourly = cfg.productiveHours > 0 ? cfg.staffCostMonthly / cfg.productiveHours : 0;

    // Annual activity volumes.
    var vol = {
      cvScreen: input.annualHires * input.appsPerVacancy,
      interview: input.annualHires * cfg.interviewsPerHire,
      payroll: input.employees * 12,
      iqama: input.iqamaRenewals,
      letters: input.monthlyLetters * 12
    };

    var a = cfg.activities;
    // Separate CV screening and interview review, combined under Recruitment.
    var cvHrs = en.recruitment ? hoursReleased(vol.cvScreen, a.cvScreen.manual, a.cvScreen.platform, r) : 0;
    var ivHrs = en.recruitment ? hoursReleased(vol.interview, a.interview.manual, a.interview.platform, r) : 0;
    var payHrs = en.payroll ? hoursReleased(vol.payroll, a.payroll.manual, a.payroll.platform, r) : 0;
    var iqHrs = en.iqama ? hoursReleased(vol.iqama, a.iqama.manual, a.iqama.platform, r) : 0;
    var ltHrs = en.letters ? hoursReleased(vol.letters, a.letters.manual, a.letters.platform, r) : 0;

    var groups = {
      recruitment: { hoursYear: cvHrs + ivHrs, enabled: !!en.recruitment },
      payroll: { hoursYear: payHrs, enabled: !!en.payroll },
      iqama: { hoursYear: iqHrs, enabled: !!en.iqama },
      letters: { hoursYear: ltHrs, enabled: !!en.letters }
    };
    var totalHoursYear = 0;
    Object.keys(groups).forEach(function (k) {
      var g = groups[k];
      g.valueYear = g.hoursYear * hourly;
      g.hoursMonth = g.hoursYear / 12;
      g.valueMonth = g.valueYear / 12;
      if (g.enabled) totalHoursYear += g.hoursYear;
    });
    var totalValueYear = totalHoursYear * hourly;

    // Per-activity flags where platform time exceeds current manual time.
    var warnings = [];
    [['cvScreen', 'recruitment'], ['interview', 'recruitment'], ['payroll', 'payroll'],
     ['iqama', 'iqama'], ['letters', 'letters']].forEach(function (pair) {
      var act = a[pair[0]];
      if (en[pair[1]] && act.platform > act.manual) warnings.push(pair[0]);
    });

    return {
      hourly: hourly,
      volumes: vol,
      groups: groups,
      totalHoursYear: totalHoursYear,
      totalHoursMonth: totalHoursYear / 12,
      totalValueYear: totalValueYear,
      totalValueMonth: totalValueYear / 12,
      warnings: warnings
    };
  }

  // Adoption sensitivity: totals at a given realization, other inputs fixed.
  function totalsAtRealization(input, r) {
    var cfg2 = Object.assign({}, input.cfg, { realization: r });
    var res = computeResults(Object.assign({}, input, { cfg: cfg2 }));
    return { hoursYear: res.totalHoursYear, valueYear: res.totalValueYear };
  }

  // Export for the Node unit test; ignored in the browser.
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { CONFIG: CONFIG, computeResults: computeResults, totalsAtRealization: totalsAtRealization };
  }

  // ---- Browser wiring ------------------------------------------------------
  if (typeof document === 'undefined') return;

  var _docLang = document.documentElement.lang;
  var LANG = ['ar', 'fr', 'de', 'es', 'it', 'nl'].indexOf(_docLang) >= 0 ? _docLang : 'en';
  var T = {
    en: {
      recruitment: 'Recruitment', payroll: 'Payroll', iqama: 'Iqama renewals', letters: 'Employee letters',
      hrsYear: 'hours / year', hrsMonth: 'hours / month', perYear: '/ year', perMonth: '/ month',
      estimated: 'Estimated', sar: 'SAR',
      base: 'Base case', low: 'Adoption 50%', high: 'Adoption 100%',
      warnPlatformHigher: 'Platform time is higher than your current manual time for this activity — this shows as a negative (added time), not a saving. Check the minutes or disable the feature.',
      warnProdHours: 'Productive hours per month must be greater than zero.',
      warnRealization: 'Realization must be between 0% and 100%.',
      disabled: 'disabled', net: 'Net annual modeled benefit', firstYear: 'First-year modeled benefit (incl. one-time implementation)'
    },
    ar: {
      recruitment: 'التوظيف', payroll: 'الرواتب', iqama: 'تجديد الإقامات', letters: 'خطابات الموظفين',
      hrsYear: 'ساعة / سنة', hrsMonth: 'ساعة / شهر', perYear: '/ سنة', perMonth: '/ شهر',
      estimated: 'تقديري', sar: 'ريال',
      base: 'الحالة الأساسية', low: 'التبنّي 50%', high: 'التبنّي 100%',
      warnPlatformHigher: 'وقت المنصة أعلى من وقتك اليدوي الحالي لهذا النشاط — يظهر ذلك كقيمة سالبة (وقت مضاف) لا كتوفير. راجِع الدقائق أو عطّل الميزة.',
      warnProdHours: 'يجب أن تكون ساعات العمل المنتجة شهريًا أكبر من صفر.',
      warnRealization: 'يجب أن تكون نسبة التحقّق بين 0% و100%.',
      disabled: 'معطّلة', net: 'صافي الأثر السنوي المُقدَّر', firstYear: 'الأثر المُقدَّر للسنة الأولى (شاملًا التنفيذ لمرّة واحدة)'
    },
    fr: {
      recruitment: 'Recrutement', payroll: 'Paie', iqama: "Renouvellements d'iqama", letters: "Lettres d'employés",
      hrsYear: 'heures / an', hrsMonth: 'heures / mois', perYear: '/ an', perMonth: '/ mois',
      estimated: 'Estimé', sar: 'SAR',
      base: 'Scénario de base', low: 'Adoption 50 %', high: 'Adoption 100 %',
      warnPlatformHigher: "Le temps avec la plateforme est supérieur à votre temps manuel actuel pour cette activité — cela apparaît comme une valeur négative (temps ajouté), pas une économie. Vérifiez les minutes ou désactivez la fonctionnalité.",
      warnProdHours: 'Les heures productives par mois doivent être supérieures à zéro.',
      warnRealization: 'La réalisation doit être comprise entre 0 % et 100 %.',
      disabled: 'désactivé', net: 'Bénéfice annuel net modélisé', firstYear: 'Bénéfice modélisé de la première année (mise en œuvre unique incluse)'
    },
    de: {
      recruitment: 'Einstellung', payroll: 'Gehaltsabrechnung', iqama: 'Iqama-Erneuerungen', letters: 'Mitarbeiterschreiben',
      hrsYear: 'Stunden / Jahr', hrsMonth: 'Stunden / Monat', perYear: '/ Jahr', perMonth: '/ Monat',
      estimated: 'Geschätzt', sar: 'SAR',
      base: 'Basisfall', low: 'Adoption 50 %', high: 'Adoption 100 %',
      warnPlatformHigher: 'Die Plattform-Zeit ist für diese Aktivität höher als Ihre aktuelle manuelle Zeit — dies erscheint als negativer Wert (zusätzliche Zeit), nicht als Einsparung. Prüfen Sie die Minuten oder deaktivieren Sie die Funktion.',
      warnProdHours: 'Die produktiven Stunden pro Monat müssen größer als null sein.',
      warnRealization: 'Die Realisierung muss zwischen 0 % und 100 % liegen.',
      disabled: 'deaktiviert', net: 'Modellierter jährlicher Nettonutzen', firstYear: 'Modellierter Nutzen im ersten Jahr (inkl. einmaliger Einrichtung)'
    },
    es: {
      recruitment: 'Contratación', payroll: 'Nóminas', iqama: 'Renovaciones de iqama', letters: 'Cartas de empleados',
      hrsYear: 'horas / año', hrsMonth: 'horas / mes', perYear: '/ año', perMonth: '/ mes',
      estimated: 'Estimado', sar: 'SAR',
      base: 'Caso base', low: 'Adopción 50 %', high: 'Adopción 100 %',
      warnPlatformHigher: 'El tiempo con la plataforma es mayor que su tiempo manual actual para esta actividad — se muestra como un valor negativo (tiempo añadido), no como un ahorro. Revise los minutos o desactive la función.',
      warnProdHours: 'Las horas productivas al mes deben ser mayores que cero.',
      warnRealization: 'La realización debe estar entre 0 % y 100 %.',
      disabled: 'desactivado', net: 'Beneficio neto anual modelado', firstYear: 'Beneficio modelado del primer año (incl. implementación única)'
    },
    it: {
      recruitment: 'Reclutamento', payroll: 'Buste paga', iqama: "Rinnovi dell'iqama", letters: 'Lettere per dipendenti',
      hrsYear: 'ore / anno', hrsMonth: 'ore / mese', perYear: '/ anno', perMonth: '/ mese',
      estimated: 'Stimato', sar: 'SAR',
      base: 'Caso base', low: 'Adozione 50%', high: 'Adozione 100%',
      warnPlatformHigher: "Il tempo con la piattaforma è superiore al tuo attuale tempo manuale per questa attività — appare come un valore negativo (tempo aggiunto), non come un risparmio. Controlla i minuti o disattiva la funzione.",
      warnProdHours: 'Le ore produttive al mese devono essere maggiori di zero.',
      warnRealization: 'La realizzazione deve essere compresa tra 0% e 100%.',
      disabled: 'disattivato', net: 'Beneficio netto annuo modellato', firstYear: 'Beneficio modellato del primo anno (incl. implementazione una tantum)'
    },
    nl: {
      recruitment: 'Werving', payroll: 'Loonadministratie', iqama: 'Iqama-verlengingen', letters: 'Werknemersbrieven',
      hrsYear: 'uren / jaar', hrsMonth: 'uren / maand', perYear: '/ jaar', perMonth: '/ maand',
      estimated: 'Geschat', sar: 'SAR',
      base: 'Basisscenario', low: 'Adoptie 50%', high: 'Adoptie 100%',
      warnPlatformHigher: 'De platformtijd is voor deze activiteit hoger dan uw huidige handmatige tijd — dit verschijnt als een negatieve waarde (extra tijd), niet als een besparing. Controleer de minuten of schakel de functie uit.',
      warnProdHours: 'De productieve uren per maand moeten groter zijn dan nul.',
      warnRealization: 'De realisatie moet tussen 0% en 100% liggen.',
      disabled: 'uitgeschakeld', net: 'Netto jaarlijks gemodelleerd voordeel', firstYear: 'Gemodelleerd voordeel eerste jaar (incl. eenmalige implementatie)'
    }
  }[LANG];

  var nf0 = new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 });
  var nf1 = new Intl.NumberFormat('en-US', { maximumFractionDigits: 1 });

  // Currency — approximate units per 1 SAR (SAR is USD-pegged at 3.75).
  // Illustrative fixed rates; the model is SAR-denominated internally.
  var RATES = { SAR: 1, AED: 0.979, USD: 0.2667, EUR: 0.245, GBP: 0.211, QAR: 0.971, KWD: 0.0819, BHD: 0.1003, OMR: 0.1025, EGP: 12.8, JOD: 0.189 };
  var CUR = 'SAR';
  function money(v) {
    var n = nf0.format(Math.round(v));
    return LANG === 'ar' ? (n + ' ' + CUR) : (CUR + ' ' + n);
  }
  // Currency-aware unit labels for the monetary inputs (filled by JS so the
  // code can switch without fragmenting the per-language catalog).
  var UNIT = {
    en: { perMonth: '· {c} / month', perYear: '· {c} / year', flat: '· {c}' },
    ar: { perMonth: '· {c} / شهر', perYear: '· {c} / سنة', flat: '· {c}' },
    fr: { perMonth: '· {c} / mois', perYear: '· {c} / an', flat: '· {c}' },
    de: { perMonth: '· {c} / Monat', perYear: '· {c} / Jahr', flat: '· {c}' },
    es: { perMonth: '· {c} / mes', perYear: '· {c} / año', flat: '· {c}' },
    it: { perMonth: '· {c} / mese', perYear: '· {c} / anno', flat: '· {c}' },
    nl: { perMonth: '· {c} / maand', perYear: '· {c} / jaar', flat: '· {c}' }
  }[LANG];
  function updateUnitLabels() {
    Array.prototype.forEach.call(document.querySelectorAll('.money-unit'), function (el) {
      var t = el.getAttribute('data-unit') || 'flat';
      el.textContent = (UNIT[t] || UNIT.flat).replace('{c}', CUR);
    });
    var sel = document.getElementById('currency'); if (sel) sel.value = CUR;
  }
  function roundMoney(n) { return n >= 200 ? Math.round(n / 10) * 10 : Math.round(n); }
  // Switch currency: convert the monetary input fields and re-render. Hours are
  // currency-agnostic; only the fully-loaded cost and the optional cost inputs
  // carry a currency, so converting them re-denominates every output.
  function setCurrency(code) {
    if (!RATES[code] || code === CUR) return;
    var factor = RATES[code] / RATES[CUR];
    ['staffCost', 'subscription', 'addlCosts', 'implementation'].forEach(function (id) {
      var el = document.getElementById(id); if (!el) return;
      var v = el.value.trim(); if (v === '') return;
      var n = parseFloat(v); if (!isFinite(n)) return;
      el.value = roundMoney(n * factor);
    });
    CUR = code;
    updateUnitLabels();
    render();
  }
  function detectCurrencyByIP() {
    try {
      fetch('https://ipapi.co/json/', { mode: 'cors' })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (d) { if (d && d.currency && RATES[d.currency]) setCurrency(d.currency); })
        .catch(function () { /* geolocation unavailable — stay on SAR */ });
    } catch (e) { /* ignore */ }
  }
  function $(id) { return document.getElementById(id); }
  function num(id, dflt) {
    var el = $(id); if (!el) return dflt;
    var v = el.value.trim();
    if (v === '') return dflt;
    var n = parseFloat(v);
    return isFinite(n) ? n : dflt;
  }

  var STORE = 'fg_hr_calc_v1';
  var estimated = { hires: false, apps: false, iqama: false, letters: false };

  function readInputs() {
    var employees = Math.max(0, num('employees', 0));
    var cfg = {
      fallback: CONFIG.fallback,
      activities: {
        cvScreen: { manual: Math.max(0, num('m-cvScreen-manual', 5)), platform: Math.max(0, num('m-cvScreen-platform', 1)) },
        interview: { manual: Math.max(0, num('m-interview-manual', 25)), platform: Math.max(0, num('m-interview-platform', 12)) },
        payroll: { manual: Math.max(0, num('m-payroll-manual', 8)), platform: Math.max(0, num('m-payroll-platform', 3)) },
        iqama: { manual: Math.max(0, num('m-iqama-manual', 40)), platform: Math.max(0, num('m-iqama-platform', 20)) },
        letters: { manual: Math.max(0, num('m-letters-manual', 10)), platform: Math.max(0, num('m-letters-platform', 2)) }
      },
      interviewsPerHire: Math.max(0, num('interviewsPerHire', 12)),
      staffCostMonthly: Math.max(0, num('staffCost', 12000)),
      productiveHours: num('productiveHours', 160),
      realization: num('realization', 80) / 100
    };
    var enabled = {
      recruitment: $('feat-recruitment').checked,
      payroll: $('feat-payroll').checked,
      iqama: $('feat-iqama').checked,
      letters: $('feat-letters').checked
    };
    return {
      employees: employees,
      annualHires: Math.max(0, num('hires', 0)),
      appsPerVacancy: Math.max(0, num('apps', 0)),
      iqamaRenewals: Math.max(0, num('iqama', 0)),
      monthlyLetters: Math.max(0, num('letters', 0)),
      enabled: enabled,
      cfg: cfg
    };
  }

  function validate(input) {
    var errs = [];
    if (!(input.cfg.productiveHours > 0)) errs.push(T.warnProdHours);
    if (input.cfg.realization < 0 || input.cfg.realization > 1) errs.push(T.warnRealization);
    return errs;
  }

  function barColor(i) {
    var c = ['#5980a6', '#6e9f88', '#b08968', '#8c7aa6'];
    return c[i % c.length];
  }

  function render() {
    var input = readInputs();
    var errs = validate(input);
    var res = computeResults(input);

    $('r-hours-month').textContent = nf1.format(res.totalHoursMonth);
    $('r-hours-year').textContent = nf1.format(res.totalHoursYear);
    $('r-value-year').textContent = money(res.totalValueYear);
    $('r-value-month').textContent = money(res.totalValueMonth);

    // Feature breakdown + chart.
    var order = ['recruitment', 'payroll', 'iqama', 'letters'];
    var maxVal = 0;
    order.forEach(function (k) { if (res.groups[k].enabled) maxVal = Math.max(maxVal, res.groups[k].valueYear); });
    var rows = '', bars = '', i = 0;
    order.forEach(function (k) {
      var g = res.groups[k];
      var label = T[k];
      if (!g.enabled) {
        rows += '<div class="bd-row bd-off"><span class="bd-name">' + label + '</span><span class="bd-val">' + T.disabled + '</span></div>';
        i++;
        return;
      }
      rows += '<div class="bd-row"><span class="bd-name">' + label + '</span>' +
        '<span class="bd-val"><b>' + money(g.valueYear) + '</b><small>' + nf1.format(g.hoursYear) + ' ' + T.hrsYear + '</small></span></div>';
      var w = maxVal > 0 ? Math.max(0, (g.valueYear / maxVal) * 100) : 0;
      bars += '<div class="chart-row"><span class="chart-label">' + label + '</span>' +
        '<span class="chart-track"><span class="chart-fill" style="width:' + w.toFixed(1) + '%;background:' + barColor(i) + '"></span></span>' +
        '<span class="chart-num">' + money(g.valueYear) + '</span></div>';
      i++;
    });
    $('breakdown').innerHTML = rows;
    $('chart').innerHTML = bars;

    // Adoption sensitivity (50% / base / 100%).
    var baseR = input.cfg.realization;
    var lo = totalsAtRealization(input, 0.5);
    var hi = totalsAtRealization(input, 1.0);
    var basePct = Math.round(baseR * 100);
    $('sensitivity').innerHTML =
      sensCell(T.low, lo) +
      sensCell(T.base + ' (' + basePct + '%)', { hoursYear: res.totalHoursYear, valueYear: res.totalValueYear }, true) +
      sensCell(T.high, hi);

    // Warnings.
    var wHtml = '';
    errs.forEach(function (e) { wHtml += '<p class="calc-warn">⚠ ' + e + '</p>'; });
    if (res.warnings.length) wHtml += '<p class="calc-warn">⚠ ' + T.warnPlatformHigher + '</p>';
    $('warnings').innerHTML = wHtml;
    $('warnings').hidden = !wHtml;

    renderNet(res);
    saveState();
  }

  function sensCell(label, t, isBase) {
    return '<div class="sens-cell' + (isBase ? ' sens-base' : '') + '">' +
      '<span class="sens-label">' + label + '</span>' +
      '<span class="sens-val">' + money(t.valueYear) + '</span>' +
      '<span class="sens-hrs">' + nf1.format(t.hoursYear) + ' ' + T.hrsYear + '</span></div>';
  }

  // Optional cost comparison — only renders net figures when costs are entered.
  function renderNet(res) {
    var sub = $('subscription') ? $('subscription').value.trim() : '';
    var addl = $('addlCosts') ? $('addlCosts').value.trim() : '';
    var impl = $('implementation') ? $('implementation').value.trim() : '';
    var any = sub !== '' || addl !== '' || impl !== '';
    var box = $('net');
    if (!box) return;
    if (!any) { box.hidden = true; box.innerHTML = ''; return; }
    var subN = Math.max(0, num('subscription', 0));
    var addlN = Math.max(0, num('addlCosts', 0));
    var implN = Math.max(0, num('implementation', 0));
    var net = res.totalValueYear - subN - addlN;          // recurring, negatives preserved
    var firstYear = net - implN;                           // implementation shown in year one only
    box.hidden = false;
    box.innerHTML =
      '<div class="net-row"><span>' + T.net + '</span><b class="' + (net < 0 ? 'neg' : '') + '">' + money(net) + '</b></div>' +
      '<div class="net-row"><span>' + T.firstYear + '</span><b class="' + (firstYear < 0 ? 'neg' : '') + '">' + money(firstYear) + '</b></div>';
  }

  // ---- Estimates, toggles, persistence ------------------------------------
  function applyEstimate(which) {
    var emp = Math.max(0, num('employees', 0));
    var map = {
      hires: Math.round(emp * CONFIG.fallback.hiresPctOfHeadcount),
      apps: CONFIG.fallback.appsPerVacancy,
      iqama: Math.round(emp * CONFIG.fallback.iqamaPctOfHeadcount),
      letters: Math.round(emp * CONFIG.fallback.lettersPctOfHeadcount)
    };
    var idmap = { hires: 'hires', apps: 'apps', iqama: 'iqama', letters: 'letters' };
    $(idmap[which]).value = map[which];
    estimated[which] = true;
    markEstimated();
    render();
  }

  function markEstimated() {
    ['hires', 'apps', 'iqama', 'letters'].forEach(function (k) {
      var badge = document.querySelector('[data-badge="' + k + '"]');
      if (badge) badge.hidden = !estimated[k];
    });
  }

  function saveState() {
    try {
      var data = {};
      document.querySelectorAll('[data-persist]').forEach(function (el) {
        data[el.id] = el.type === 'checkbox' ? el.checked : el.value;
      });
      data.__est = estimated;
      localStorage.setItem(STORE, JSON.stringify(data));
    } catch (e) { /* private mode / blocked — ignore */ }
  }

  function restoreState() {
    try {
      var raw = localStorage.getItem(STORE);
      if (!raw) return;
      var data = JSON.parse(raw);
      Object.keys(data).forEach(function (id) {
        if (id === '__est') return;
        var el = $(id);
        if (!el) return;
        if (el.type === 'checkbox') el.checked = !!data[id];
        else el.value = data[id];
      });
      if (data.__est) estimated = data.__est;
    } catch (e) { /* ignore */ }
  }

  function init() {
    restoreState();
    markEstimated();
    // Currency: adopt the saved currency if any (the stored field values were
    // already written in that currency, so no conversion on restore). On a
    // first visit, keep SAR and try IP geolocation once (below).
    var savedCur = null;
    try {
      var raw = localStorage.getItem(STORE);
      if (raw) { var d = JSON.parse(raw); if (d && d.currency && RATES[d.currency]) savedCur = d.currency; }
    } catch (e) { /* ignore */ }
    if (savedCur) CUR = savedCur;
    updateUnitLabels();

    document.querySelectorAll('[data-estimate]').forEach(function (btn) {
      btn.addEventListener('click', function () { applyEstimate(btn.getAttribute('data-estimate')); });
    });
    // Clear the "estimated" badge once a visitor edits that field by hand.
    ['hires', 'apps', 'iqama', 'letters'].forEach(function (k) {
      var el = $(k);
      if (el) el.addEventListener('input', function () { if (estimated[k]) { estimated[k] = false; markEstimated(); } });
    });
    document.querySelectorAll('[data-persist]').forEach(function (el) {
      if (el.id === 'currency') return;   // the currency selector converts, below
      el.addEventListener('input', render);
      el.addEventListener('change', render);
    });
    var curSel = $('currency');
    if (curSel) curSel.addEventListener('change', function () { setCurrency(curSel.value); });
    render();
    if (!savedCur) detectCurrencyByIP();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
