/* FulcrumGrid — editorial redesign interactions
   Header flourishes run on every page; hero 3D / parallax only where present. */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Header: scroll-progress meter + sliding nav indicator ---- */
  (function () {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var progress = document.createElement('span');
    progress.className = 'fg-progress';
    header.appendChild(progress);

    var nav = header.querySelector('.site-nav');
    var ind = null, links = [];
    if (nav) {
      ind = document.createElement('span');
      ind.className = 'fg-nav-ind';
      nav.appendChild(ind);
      links = Array.prototype.slice.call(nav.querySelectorAll('a'));
      var activeLink = nav.querySelector('a.active');
      var moveTo = function (link) {
        if (!link) { ind.style.opacity = '0'; return; }
        var nr = nav.getBoundingClientRect(), lr = link.getBoundingClientRect();
        ind.style.width = lr.width + 'px';
        ind.style.transform = 'translateX(' + (lr.left - nr.left) + 'px)';
        ind.style.opacity = '1';
      };
      links.forEach(function (a) { a.addEventListener('mouseenter', function () { moveTo(a); }); });
      nav.addEventListener('mouseleave', function () { moveTo(activeLink); });
      window.addEventListener('resize', function () { moveTo(activeLink); });
      requestAnimationFrame(function () { moveTo(activeLink); });
    }

    var onScroll = function () {
      var y = window.scrollY || 0;
      header.classList.toggle('scrolled', y > 8);
      var docH = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = (docH > 0 ? (y / docH) * 100 : 0) + '%';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  })();

  /* ---- Hero 3D camera: pointer tilt + scroll dolly ---- */
  (function () {
    if (reduce) return;
    var hero = document.getElementById('hero');
    var scene = document.getElementById('heroScene');
    var content = document.getElementById('heroContent');
    if (!hero || !scene) return;
    var tx = 0, ty = 0, cx = 0, cy = 0, active = false;
    function loop() {
      cx += (tx - cx) * 0.07; cy += (ty - cy) * 0.07;
      var r = hero.getBoundingClientRect();
      var p = Math.min(Math.max(-r.top / (r.height || 1), 0), 1);
      scene.style.transform = 'rotateY(' + (cx * 5) + 'deg) rotateX(' + (-cy * 3.4) + 'deg) translateY(' + (p * 70) + 'px) scale(' + (1 + p * 0.06) + ')';
      if (content) {
        content.style.transform = 'translate3d(' + (cx * 16) + 'px,' + (cy * 11 - p * 60) + 'px,0)';
        content.style.opacity = String(1 - p * 0.92);
      }
      if (Math.abs(tx - cx) > 0.0008 || Math.abs(ty - cy) > 0.0008 || p > 0.001) { requestAnimationFrame(loop); }
      else { active = false; }
    }
    function kick() { if (!active) { active = true; requestAnimationFrame(loop); } }
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
      ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
      kick();
    });
    hero.addEventListener('pointerleave', function () { tx = 0; ty = 0; kick(); });
    window.addEventListener('scroll', kick, { passive: true });
  })();

  /* ---- App-card 3D tilt + glare ---- */
  (function () {
    if (reduce) return;
    Array.prototype.forEach.call(document.querySelectorAll('.fg-app'), function (card) {
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
        card.classList.add('tilting');
        card.style.transform = 'rotateY(' + ((px - 0.5) * 12) + 'deg) rotateX(' + ((0.5 - py) * 12) + 'deg) translateZ(26px)';
        card.style.setProperty('--gx', (px * 100) + '%');
        card.style.setProperty('--gy', (py * 100) + '%');
      });
      card.addEventListener('pointerleave', function () {
        card.classList.remove('tilting');
        card.style.transform = '';
      });
    });
  })();

  /* ---- Feature-panel image parallax ---- */
  (function () {
    if (reduce) return;
    var imgs = Array.prototype.slice.call(document.querySelectorAll('.fg-parallax'));
    if (!imgs.length) return;
    var ticking = false;
    function update() {
      var vh = window.innerHeight;
      imgs.forEach(function (img) {
        var r = img.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var prog = (r.top + r.height / 2 - vh / 2) / vh;
        img.style.transform = 'translate3d(0,' + (Math.max(-1, Math.min(1, prog)) * -6) + '%,0)';
      });
      ticking = false;
    }
    function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  })();

  /* ---- Hero signal particles ---- */
  (function () {
    var canvas = document.getElementById('fgParticles');
    if (!canvas || !canvas.getContext) return;
    var ctx = canvas.getContext('2d');
    var host = canvas.parentElement;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, nodes = [], raf = null;
    function size() {
      W = host.clientWidth; H = host.clientHeight;
      canvas.width = W * dpr; canvas.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var count = Math.max(18, Math.min(40, Math.round(W / 42)));
      nodes = [];
      for (var i = 0; i < count; i++) {
        nodes.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - 0.5) * 0.22, vy: (Math.random() - 0.5) * 0.22, r: Math.random() * 1.6 + 0.8 });
      }
    }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        if (!reduce) { a.x += a.vx; a.y += a.vy; }
        if (a.x < 0 || a.x > W) a.vx *= -1;
        if (a.y < 0 || a.y > H) a.vy *= -1;
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d = Math.hypot(dx, dy);
          if (d < 118) { ctx.strokeStyle = 'rgba(90,140,255,' + (0.16 * (1 - d / 118)) + ')'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); }
        }
      }
      for (var k = 0; k < nodes.length; k++) { var n = nodes[k]; ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2); ctx.fillStyle = 'rgba(120,165,255,.7)'; ctx.fill(); }
      if (!reduce) raf = requestAnimationFrame(draw);
    }
    function start() { if (raf) cancelAnimationFrame(raf); size(); draw(); }
    var t; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(start, 180); });
    start();
  })();
})();

/* Currency switcher — SAR base, indicative conversion, IP pre-select (pricing pages only) */
(function () {
  var priced = document.querySelectorAll('.num[data-amt]');
  if (!priced.length) return;

  var RTL = document.documentElement.dir === 'rtl';
  var RATES = { SAR: 3.75, USD: 1, AED: 3.6725, EUR: 0.92, GBP: 0.79 }; // units per 1 USD
  var SYM = { SAR: 'SAR', USD: '$', AED: 'AED', EUR: '€', GBP: '£' };
  var ORDER = ['SAR', 'USD', 'AED', 'EUR', 'GBP'];
  var C2CUR = { SA: 'SAR', AE: 'AED', GB: 'GBP', US: 'USD', CA: 'USD', AU: 'USD',
    DE:'EUR',FR:'EUR',ES:'EUR',IT:'EUR',NL:'EUR',IE:'EUR',BE:'EUR',AT:'EUR',PT:'EUR',FI:'EUR',GR:'EUR',LU:'EUR',SK:'EUR',SI:'EUR',EE:'EUR',LV:'EUR',LT:'EUR',CY:'EUR',MT:'EUR',HR:'EUR' };
  var LSKEY = 'fg_currency';

  function fmt(cur, amt, base) {
    var usd = amt / RATES[base];
    var v = Math.round(usd * RATES[cur]);
    var num = v.toLocaleString('en-US');
    var sym = SYM[cur];
    var body = /^[A-Z]/.test(sym) ? sym + ' ' + num : sym + num; // letters get a thin space
    return (cur === base ? '' : '≈ ') + body;
  }
  function apply(cur) {
    Array.prototype.forEach.call(priced, function (el) {
      var amt = parseFloat(el.getAttribute('data-amt'));
      var base = el.getAttribute('data-base') || 'SAR';
      if (isNaN(amt)) return;
      el.textContent = fmt(cur, amt, base);
    });
    Array.prototype.forEach.call(document.querySelectorAll('.fg-cur button'), function (b) {
      b.classList.toggle('active', b.getAttribute('data-cur') === cur);
      b.setAttribute('aria-pressed', b.getAttribute('data-cur') === cur ? 'true' : 'false');
    });
    try { localStorage.setItem(LSKEY, cur); } catch (e) {}
  }

  // Build switcher
  var anchor = document.querySelector('.pricing-grid') || document.querySelector('.fg-priceblock');
  if (!anchor) return;
  var wrap = document.createElement('div');
  wrap.className = 'fg-cur';
  wrap.setAttribute('role', 'group');
  wrap.setAttribute('aria-label', RTL ? 'العملة' : 'Currency');
  var label = document.createElement('span');
  label.className = 'fg-cur-label';
  label.textContent = RTL ? 'العملة' : 'Currency';
  wrap.appendChild(label);
  ORDER.forEach(function (c) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.setAttribute('data-cur', c);
    btn.textContent = c;
    btn.addEventListener('click', function () { apply(c); });
    wrap.appendChild(btn);
  });
  var note = document.createElement('span');
  note.className = 'fg-cur-note';
  note.textContent = RTL ? 'تحويلات تقديرية — الفوترة بالريال السعودي' : 'Indicative — billed in SAR';
  wrap.appendChild(note);
  anchor.parentNode.insertBefore(wrap, anchor);

  // Initial currency: stored → geo-IP → SAR
  var stored = null;
  try { stored = localStorage.getItem(LSKEY); } catch (e) {}
  if (stored && RATES[stored]) { apply(stored); return; }
  apply('SAR');
  if (window.matchMedia && window.matchMedia('(prefers-reduced-data: reduce)').matches) return;
  try {
    var ctrl = ('AbortController' in window) ? new AbortController() : null;
    if (ctrl) setTimeout(function () { ctrl.abort(); }, 2500);
    fetch('https://ipapi.co/json/', ctrl ? { signal: ctrl.signal } : undefined)
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (!d) return;
        var cur = C2CUR[(d.country_code || '').toUpperCase()];
        var chosen = null; try { chosen = localStorage.getItem(LSKEY); } catch (e) {}
        // only auto-apply if the visitor hasn't clicked since load
        if (cur && RATES[cur] && (!chosen || chosen === 'SAR')) apply(cur);
      })
      .catch(function () {});
  } catch (e) {}
})();
