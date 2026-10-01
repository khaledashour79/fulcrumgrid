/* FulcrumGrid redesign — "Apps in orbit" hero (option 1d from the Claude Design
   handoff). Available apps ride the outer ring, coming-soon apps the inner
   dashed ring, both around a small solid "FG · Platform" cube. Hovering a tile
   holds the orbit; selecting one jumps to it further down the page.
   Vanilla, CSP safe, respects prefers-reduced-motion. Localised strings come
   from data-l-* attributes on the stage so each language page owns its copy. */
(function () {
  'use strict';
  var stage = document.querySelector('[data-stage="orbit"]');
  if (!stage) return;

  // [name, status, explorer key] — status must match the homepage's
  // "Coming soon" list; available apps open their tab in the explorer.
  var APPS = [
    ['HR Suite', 'live', 'hr'], ['Command Center', 'live', 'cc'], ['Collection', 'live', 'col'],
    ['Close', 'soon', ''], ['TMS', 'soon', ''], ['Voice', 'soon', ''], ['Assure', 'soon', '']
  ];
  // Tiles per ring — drives the angular spacing so each ring stays evenly spread
  // however many apps it carries.
  var COUNT = { live: 0, soon: 0 };
  APPS.forEach(function (a) { COUNT[a[1]]++; });
  var FACE = ['rotateY(0deg)', 'rotateY(90deg)', 'rotateY(180deg)', 'rotateY(-90deg)', 'rotateX(90deg)', 'rotateX(-90deg)'];
  var CORE = ['FG · Platform', 'FG · Platform', 'FG · Platform', 'FG · Platform', 'FG', 'FG'];

  var clamp = function (v, a, b) { a = a == null ? 0 : a; b = b == null ? 1 : b; return Math.max(a, Math.min(b, v)); };
  var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
  var pad = function (n) { return String(n).padStart(2, '0'); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var L = function (k, d) { return stage.getAttribute('data-l-' + k) || d; };
  var txtLive = L('live', 'Available'), txtSoon = L('soon', 'Coming soon');
  var txtOrbit = L('orbit', 'Orbit'), txtHeld = L('held', 'Orbit held');
  // Localized app names by explorer key, e.g. data-l-apps="hr=…|cc=…|col=…".
  // Falls back to the English name in the APPS array when unset (EN/European).
  var NAMES = {};
  (stage.getAttribute('data-l-apps') || '').split('|').forEach(function (p) {
    var i = p.indexOf('='); if (i > 0) NAMES[p.slice(0, i)] = p.slice(i + 1);
  });
  var appName = function (a) { return NAMES[a[2]] || a[0]; };

  var NS = 'http://www.w3.org/2000/svg';
  function svgLayer(cls, paths) {
    var s = document.createElementNS(NS, 'svg'); s.setAttribute('class', 'ostage-svg ' + cls);
    var out = {};
    paths.forEach(function (p) {
      var el = document.createElementNS(NS, 'path');
      el.setAttribute('class', p); el.setAttribute('fill', 'none');
      s.appendChild(el); out[p] = el;
    });
    stage.appendChild(s);
    return out;
  }
  // back layer (behind the core) and front layer (in front of it)
  var back = svgLayer('back', ['o-ring-live b', 'o-ring-soon b', 'o-spoke b']);
  var core = document.createElement('div'); core.className = 'ocore';
  CORE.forEach(function (t, i) {
    var f = document.createElement('div'); f.className = 'ocore-face'; f.textContent = t;
    f.style.transform = FACE[i] + ' translateZ(50px)';
    core.appendChild(f);
  });
  stage.appendChild(core);
  var front = svgLayer('front', ['o-ring-live f', 'o-ring-soon f', 'o-spoke f']);

  var tiles = APPS.map(function (a, i) {
    var t = document.createElement('div');
    t.className = 'otile ' + a[1];
    t.innerHTML =
      '<i class="corner tl"></i><i class="corner tr"></i><i class="corner bl"></i><i class="corner br"></i>' +
      '<span class="ot-head"><span class="ot-num">' + pad(i + 1) + '</span>' +
      '<span class="ot-st"><i class="ot-dot"></i>' + (a[1] === 'live' ? txtLive : txtSoon) + '</span></span>' +
      '<span class="ot-name">' + appName(a) + '</span>';
    t.addEventListener('click', function () { pick(a); });
    stage.appendChild(t);
    return t;
  });

  function pick(a) {
    var target;
    if (a[2]) {
      var tab = document.querySelector('.exp-tab[data-exp="' + a[2] + '"]');
      if (tab) tab.click();
      target = document.getElementById('explorer');
    } else {
      target = document.getElementById('products');
    }
    if (target) window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 70, behavior: reduce ? 'auto' : 'smooth' });
  }

  var readout = stage.parentElement.querySelector('[data-readout]');
  var mx = 0, my = 0, tx = 0, ty = 0, oa = 0, t0 = performance.now(), visible = true;
  stage.addEventListener('pointermove', function (ev) {
    if (ev.pointerType !== 'mouse') return;
    var r = stage.getBoundingClientRect();
    mx = (ev.clientX - r.left) / r.width - 0.5; my = (ev.clientY - r.top) / r.height - 0.5;
  });
  stage.addEventListener('pointerleave', function () { mx = 0; my = 0; });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(stage);
  }

  // Outer ring = available apps, inner ring = coming soon (counter-rotating).
  var RINGS = { live: { f: 1, inc: 0.12, spd: 1 }, soon: { f: 0.58, inc: -0.3, spd: -1.5 } };

  function tick() {
    requestAnimationFrame(tick);
    if (!visible) return;
    var now = (performance.now() - t0) / 1000;
    tx += (mx - tx) * 0.05; ty += (my - ty) * 0.05;
    var W = stage.clientWidth, H = stage.clientHeight;
    var R = Math.min(W * 0.4, H * 0.38), cx = W / 2, cy = H / 2 + 8, ts = clamp(W / 760, 0.6, 1);
    var intro = reduce ? 1 : ease(clamp((now - 0.2) / 1.6));
    var held = !!stage.querySelector('.otile:hover');
    if (!held && !reduce) oa += 0.003;
    var tilt = 0.82 - ty * 0.2, yaw = tx * 0.35;
    var cw = Math.cos(yaw), sw = Math.sin(yaw), ct = Math.cos(tilt), st = Math.sin(tilt);
    var P = function (x, y, z) { var X = x * cw + z * sw, Z = -x * sw + z * cw; return [cx + X, cy - (y * ct - Z * st), y * st + Z * ct]; };
    var k = 0.35 + 0.65 * intro;
    var ringPt = function (rg, th) { var r = R * rg.f * k, x = Math.cos(th) * r, z = Math.sin(th) * r; return P(x * Math.cos(rg.inc), x * Math.sin(rg.inc), z); };

    ['live', 'soon'].forEach(function (key) {
      var rg = RINGS[key], b = '', f = '', pf = null;
      for (var s = 0; s <= 96; s++) {
        var q = ringPt(rg, s / 96 * Math.PI * 2), fr = q[2] >= 0;
        var cmd = (pf === fr ? 'L' : 'M') + q[0].toFixed(1) + ' ' + q[1].toFixed(1);
        if (fr) f += cmd; else b += cmd;
        pf = fr;
      }
      back['o-ring-' + key + ' b'].setAttribute('d', b);
      front['o-ring-' + key + ' f'].setAttribute('d', f);
    });

    var sb = '', sf = '', idx = { live: 0, soon: 0 };
    tiles.forEach(function (el, i) {
      var key = APPS[i][1], rg = RINGS[key], j = idx[key]++;
      var th = oa * rg.spd + j * Math.PI * 2 / COUNT[key] + (key === 'soon' ? Math.PI / COUNT[key] : 0);
      var q = ringPt(rg, th);
      var dn = clamp((q[2] / (R * rg.f * k) + 1) / 2);
      el.style.transform = 'translate(' + q[0].toFixed(1) + 'px,' + q[1].toFixed(1) + 'px) translate(-50%,-50%) scale(' + (ts * (0.8 + 0.2 * dn)).toFixed(3) + ')';
      // front half sits above the core (z 10) and front rings (z 15); nearer tiles win overlaps
      el.style.zIndex = q[2] >= 0 ? 20 + Math.round(dn * 20) : 2 + Math.round(dn * 6);
      el.style.opacity = (intro * (0.6 + 0.4 * dn)).toFixed(3);
      var seg = 'M' + cx.toFixed(1) + ' ' + cy.toFixed(1) + 'L' + q[0].toFixed(1) + ' ' + q[1].toFixed(1);
      if (q[2] >= 0) sf += seg; else sb += seg;
    });
    back['o-spoke b'].setAttribute('d', sb);
    front['o-spoke f'].setAttribute('d', sf);

    core.style.transform = 'translate(' + cx.toFixed(1) + 'px,' + cy.toFixed(1) + 'px) rotateX(-24deg) rotateY(' + (reduce ? -32 : now * 12).toFixed(2) + 'deg) scale(' + (ts * 0.8 * (0.6 + 0.4 * intro)).toFixed(3) + ')';

    if (readout) readout.textContent = held ? txtHeld : txtOrbit + ' ' + String(Math.round(((oa * 57.3) % 360 + 360) % 360)).padStart(3, '0') + '°';
  }
  requestAnimationFrame(tick);
})();
