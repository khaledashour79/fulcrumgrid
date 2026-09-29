/* FulcrumGrid redesign — interactive isometric hero.
   Vanilla port of the design's stack animation: an exploded stack of app
   "slabs" that assembles on intro, collapses as you scroll into the hero, and
   responds to drag (assemble/disassemble) and pointer tilt. No framework; CSP
   safe (self-hosted, no eval). Respects prefers-reduced-motion. */
(function () {
  'use strict';
  var stage = document.querySelector('[data-stage]');
  if (!stage) return;

  var LAYERS = [
    { n: '00', name: 'FulcrumGrid platform', tag: 'Foundation' },
    { n: '01', name: 'Command Center', tag: 'Operations' },
    { n: '02', name: 'Collection', tag: 'Receivables' },
    { n: '03', name: 'HR Suite', tag: 'People' }
  ];

  var clamp = function (v, a, b) { a = a == null ? 0 : a; b = b == null ? 1 : b; return Math.max(a, Math.min(b, v)); };
  var ease = function (t) { return 1 - Math.pow(1 - t, 3); };

  var iso = document.createElement('div'); iso.className = 'iso';
  var labelWrap = document.createElement('div');
  labelWrap.style.cssText = 'position:absolute;inset:0;pointer-events:none;z-index:4';
  var slabs = [], labels = [];

  LAYERS.forEach(function (L, i) {
    var slab = document.createElement('div'); slab.className = 'slab';
    var top = document.createElement('div'); top.className = 'top';
    ['tl', 'tr', 'bl', 'br'].forEach(function (p) {
      var c = document.createElement('span'); c.className = 'c ' + p; c.setAttribute('data-c', ''); top.appendChild(c);
    });
    var n = document.createElement('span'); n.className = 'n'; n.textContent = L.n; top.appendChild(n);
    slab.appendChild(top); iso.appendChild(slab); slabs.push(slab);

    var lb = document.createElement('span'); lb.className = 'iso-label';
    lb.innerHTML = '<b>' + L.name + '</b><span class="lt">' + L.tag + '</span>';
    labelWrap.appendChild(lb); labels.push(lb);
  });
  stage.appendChild(iso); stage.appendChild(labelWrap);

  var readout = document.querySelector('[data-readout]');
  var hero = stage.closest('.hero') || stage.parentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var mx = 0, my = 0, tx = 0, ty = 0, e = 0, drag = 0, down = null, t0 = performance.now();

  function rel(ev) {
    var r = stage.getBoundingClientRect();
    return [(ev.clientX - r.left) / r.width - 0.5, (ev.clientY - r.top) / r.height - 0.5, ev.clientY];
  }
  stage.addEventListener('pointerdown', function (ev) { down = { y: ev.clientY, d: drag }; try { stage.setPointerCapture(ev.pointerId); } catch (_) {} });
  stage.addEventListener('pointermove', function (ev) { var a = rel(ev); mx = a[0]; my = a[1]; if (down) drag = clamp(down.d - (a[2] - down.y) / 260, -1, 1); });
  stage.addEventListener('pointerup', function () { down = null; });
  stage.addEventListener('pointerleave', function () { mx = 0; my = 0; down = null; });

  function tick() {
    var now = (performance.now() - t0) / 1000;
    tx += (mx - tx) * 0.05; ty += (my - ty) * 0.05;
    var r = stage.getBoundingClientRect();
    var sc = clamp(Math.min(r.width / 720, r.height / 700), 0.5, 1.15);
    iso.style.transform = 'scale3d(' + sc + ',' + sc + ',' + sc + ') rotateX(' + (58 - ty * 5) + 'deg) rotateZ(' + (-42 + tx * 7) + 'deg)';

    var p = reduce ? 0 : clamp(window.scrollY / (hero.offsetHeight * 0.6));
    var intro = reduce ? 1 : ease(clamp((now - 0.2) / 1.6));
    var target = clamp(intro * (1 - p) + drag);
    e += (target - e) * (reduce ? 1 : 0.08);

    var sr = stage.getBoundingClientRect();
    slabs.forEach(function (el, i) {
      var hov = el.matches(':hover');
      var z = i * (16 + e * 48) + (hov ? 22 * e : 0);
      el.style.transform = 'translateZ(' + z.toFixed(1) + 'px)';
      var top = el.firstChild;
      var bg = hov ? 'var(--color-accent-100)' : (i === 0 ? 'var(--color-accent-100)' : 'var(--color-bg)');
      if (top.dataset.bg !== bg) { top.dataset.bg = bg; top.style.background = bg; top.style.borderColor = hov ? 'var(--color-accent-700)' : ''; }

      var lb = labels[i]; if (!lb) return;
      var best = null, cs = el.querySelectorAll('[data-c]');
      for (var k = 0; k < cs.length; k++) { var cr = cs[k].getBoundingClientRect(); if (!best || cr.left > best.left) best = cr; }
      if (!best) return;
      var narrow = r.width < 620;
      var lt = lb.lastElementChild; if (lt && lt.style.display !== (narrow ? 'none' : '')) lt.style.display = narrow ? 'none' : '';
      var x = Math.min(best.left - sr.left + 6, r.width - lb.offsetWidth - 12), y = best.top - sr.top - 10;
      lb.style.transform = 'translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px)';
      var show = e > 0.35 || i === labels.length - 1;
      lb.style.opacity = show ? (hov ? '1' : '0.9') : '0';
    });

    if (readout) readout.textContent = 'Assembly ' + String(Math.round((1 - e) * 100)).padStart(3, '0') + '%';
    raf = requestAnimationFrame(tick);
  }
  var raf = requestAnimationFrame(tick);
})();
