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

    /* Localize messages by page language (English default, Arabic on /ar/) */
    var isAr = (document.documentElement.lang || '').toLowerCase().indexOf('ar') === 0;
    var t = isAr ? {
      invalid: 'يرجى إدخال اسمك وبريد مهني صحيح.',
      sending: 'جارٍ الإرسال…',
      thanks: function (n) { return 'شكرًا ' + n + '! تم استلام طلبك وسنتواصل معك قريبًا.'; },
      fallback: 'تعذّر الإرسال تلقائيًا — يتم فتح تطبيق البريد كخيار بديل…',
      subject: 'طلب عرض توضيحي — FulcrumGrid',
      body: function (name, email) { return 'الاسم: ' + name + '\nالبريد: ' + email + '\n\nأودّ مشاهدة عرض توضيحي لـ FulcrumGrid.'; }
    } : {
      invalid: 'Please enter your name and a valid work email.',
      sending: 'Sending…',
      thanks: function (n) { return 'Thanks, ' + n + '! We\'ve got your request and will be in touch shortly.'; },
      fallback: 'Couldn\'t send automatically — opening your email app as a fallback…',
      subject: 'Demo request — FulcrumGrid',
      body: function (name, email) { return 'Name: ' + name + '\nEmail: ' + email + '\n\nI\'d like to see a demo of FulcrumGrid.'; }
    };

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
        setNote(t.invalid, true);
        return;
      }

      /* Honeypot: if a bot filled the hidden field, silently drop. */
      var hp = document.getElementById('lead-hp');
      if (hp && hp.value) { return; }

      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; }
      setNote(t.sending, false);

      var mailtoFallback = function () {
        setNote(t.fallback, false);
        var subject = encodeURIComponent(t.subject);
        var body = encodeURIComponent(t.body(name, email));
        window.location.href = 'mailto:contact@avenlorconsulting.com?subject=' + subject + '&body=' + body;
      };

      /* Submit in the background via Web3Forms — no email client, delivered
         to contact@avenlorconsulting.com with the visitor set as reply-to. */
      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          access_key: '51242534-fc79-4ef7-a99b-f767f1765d90',
          subject: t.subject + ' — ' + name,
          from_name: 'FulcrumGrid website',
          name: name,
          email: email,
          replyto: email,
          botcheck: false,
          message: t.body(name, email)
        })
      })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data && data.success) {
            setNote(t.thanks(name.split(' ')[0]), false);
            form.reset();
          } else {
            mailtoFallback();
          }
        })
        .catch(mailtoFallback)
        .then(function () { if (btn) { btn.disabled = false; } });
    });
  }
})();
