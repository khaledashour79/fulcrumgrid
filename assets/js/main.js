/* FulcrumGrid — interactions */
(function () {
  'use strict';

  /* Current year in footer */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* Sticky header shadow on scroll */
  var header = document.querySelector('.site-header');
  var onScroll = function () {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 8);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Mobile menu toggle */
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('mobile-menu');
  if (toggle && menu) {
    var setMenu = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      menu.classList.toggle('open', open);
      menu.hidden = !open;
    };
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });
    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { setMenu(false); });
    });
  }

  /* Reveal-on-scroll */
  var revealEls = document.querySelectorAll(
    '.product-card, .feature, .step, .cta-panel, .section-head'
  );
  revealEls.forEach(function (el) { el.classList.add('reveal'); });

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* Lead form — client-side validation (no backend wired yet) */
  var form = document.getElementById('lead-form');
  if (form) {
    var note = document.getElementById('form-note');
    var nameInput = document.getElementById('name');
    var emailInput = document.getElementById('email');
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    var setNote = function (msg, isError) {
      if (!note) return;
      note.textContent = msg;
      note.classList.toggle('error', !!isError);
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = nameInput.value.trim();
      var email = emailInput.value.trim();
      var ok = true;

      nameInput.classList.remove('invalid');
      emailInput.classList.remove('invalid');

      if (!name) { nameInput.classList.add('invalid'); ok = false; }
      if (!emailRe.test(email)) { emailInput.classList.add('invalid'); ok = false; }

      if (!ok) {
        setNote('Please enter your name and a valid work email.', true);
        return;
      }

      /* No backend connected yet — surface a friendly confirmation and
         fall back to a mailto so the lead is never lost. */
      setNote('Thanks, ' + name.split(' ')[0] + '! Opening your email client…', false);
      var subject = encodeURIComponent('Demo request — FulcrumGrid');
      var body = encodeURIComponent('Name: ' + name + '\nEmail: ' + email + '\n\nI\'d like to see a demo of FulcrumGrid.');
      window.location.href = 'mailto:hello@fulcrumgrid.com?subject=' + subject + '&body=' + body;
      form.reset();
    });
  }
})();
