/* HR savings-calculator modal (HR product page).
 *
 * Lazy-loads the already-localized /<lang>/calculator/ page in an iframe
 * (embed mode hides the site chrome). Auto-opens once per visitor; the
 * on-page teaser button [data-calc-open] re-opens it any time. Client-side
 * only, no data collection. Degrades gracefully: without JS the teaser is a
 * normal link to the full calculator page.
 */
(function () {
  'use strict';
  if (typeof document === 'undefined') return;

  var modal = document.querySelector('[data-calc-modal]');
  if (!modal) return;
  var frame = modal.querySelector('iframe');
  var closeBtn = modal.querySelector('.calc-modal__close');

  var docLang = document.documentElement.lang || 'en';
  var lang = ['ar', 'fr', 'de', 'es', 'it', 'nl'].indexOf(docLang) >= 0 ? docLang : 'en';
  var STR = {
    en: { title: 'HR savings calculator', close: 'Close calculator' },
    ar: { title: 'حاسبة توفير الموارد البشرية', close: 'إغلاق الحاسبة' },
    fr: { title: "Calculateur d'économies RH", close: 'Fermer le calculateur' },
    de: { title: 'HR-Einsparungsrechner', close: 'Rechner schließen' },
    es: { title: 'Calculadora de ahorro de RR. HH.', close: 'Cerrar la calculadora' },
    it: { title: 'Calcolatore di risparmio HR', close: 'Chiudi il calcolatore' },
    nl: { title: 'HR-besparingscalculator', close: 'Calculator sluiten' }
  }[lang];

  var dialog = modal.querySelector('[role="dialog"]');
  if (dialog) dialog.setAttribute('aria-label', STR.title);
  if (frame) frame.setAttribute('title', STR.title);
  if (closeBtn) closeBtn.setAttribute('aria-label', STR.close);

  var calcUrl = (lang !== 'en' ? '/' + lang + '/calculator/' : '/calculator/') + '?embed=1';
  var loaded = false, lastFocus = null;

  function open() {
    if (!loaded && frame) { frame.src = calcUrl; loaded = true; }
    lastFocus = document.activeElement;
    modal.hidden = false;
    try { document.documentElement.style.overflow = 'hidden'; } catch (e) {}
    requestAnimationFrame(function () { modal.classList.add('is-open'); });
    if (closeBtn) closeBtn.focus();
    document.addEventListener('keydown', onKey);
  }
  function close() {
    modal.classList.remove('is-open');
    document.removeEventListener('keydown', onKey);
    try { document.documentElement.style.overflow = ''; } catch (e) {}
    setTimeout(function () { modal.hidden = true; }, 250);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  function onKey(e) { if (e.key === 'Escape' || e.key === 'Esc') close(); }

  Array.prototype.forEach.call(modal.querySelectorAll('[data-calc-close]'), function (el) {
    el.addEventListener('click', close);
  });
  Array.prototype.forEach.call(document.querySelectorAll('[data-calc-open]'), function (el) {
    el.addEventListener('click', function (e) { e.preventDefault(); open(); });
  });

  // Auto-open once per visitor, shortly after arrival.
  try {
    if (!localStorage.getItem('fg_hr_calc_modal_seen')) {
      localStorage.setItem('fg_hr_calc_modal_seen', '1');
      setTimeout(open, 1000);
    }
  } catch (e) { /* storage blocked — no auto-open, button still works */ }
})();
