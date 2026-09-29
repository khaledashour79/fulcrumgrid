/* FulcrumGrid redesign — interactive isometric APP-GRID hero (grid variant).
   An isometric floor of extruded app tiles that assemble in on load, spread as
   you scroll into the hero, and respond to drag + pointer tilt. Vanilla, CSP
   safe, respects prefers-reduced-motion. */
(function () {
  'use strict';
  var stage = document.querySelector('[data-stage="grid"]');
  if (!stage) return;

  // [name, status] — real apps live; the rest roadmap / built-to-order.
  var GRID = [
    ['Command Center', 'Live'], ['Collection', 'Live'], ['HR Suite', 'Live'], ['Inventory', 'Roadmap'],
    ['CRM', 'Roadmap'], ['Analytics', 'Roadmap'], ['Procurement', 'Roadmap'], ['TMS', 'Roadmap'],
    ['Custom apps', 'Built to order'], ['Your next app', '']
  ];
  var COLS = 4, W = 148, GAP = 174;
  var Hs = { 'Live': 50, 'Built to order': 36, 'Roadmap': 22, '': 36 };

  var clamp = function (v, a, b) { a = a == null ? 0 : a; b = b == null ? 1 : b; return Math.max(a, Math.min(b, v)); };
  var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var floor = document.createElement('div'); floor.className = 'gfloor';
  var rows = Math.ceil(GRID.length / COLS);
  var floorW = (COLS - 1) * GAP + W, floorH = (rows - 1) * GAP + W;
  floor.style.width = floorW + 'px';
  floor.style.height = floorH + 'px';
  floor.style.marginLeft = (-floorW / 2) + 'px';
  floor.style.marginTop = (-floorH / 2) + 'px';

  var tiles = [];
  GRID.forEach(function (g, i) {
    var name = g[0], status = g[1];
    var h = Hs[status] != null ? Hs[status] : 20;
    var cls = status === 'Live' ? 'live' : (status === 'Roadmap' ? 'road' : (status === '' ? 'empty' : 'built'));
    var col = i % COLS, row = Math.floor(i / COLS);
    var t = document.createElement('div');
    t.className = 'gtile ' + cls;
    t.style.left = (col * GAP) + 'px'; t.style.top = (row * GAP) + 'px';
    t.style.width = W + 'px'; t.style.height = W + 'px';
    // Extruded tile — exact recipe: top face raised to z=H, plus a front wall
    // (at the front edge, folded up) and a left wall (folded in).
    var bc = 'color-mix(in srgb, var(--color-text) 40%, transparent)';
    var bs = cls === 'live' ? 'solid' : 'dashed';
    var nameCol = cls === 'live' ? 'var(--color-text)' : 'color-mix(in srgb, var(--color-text) 62%, transparent)';
    var stCol = cls === 'live' ? 'var(--color-accent-700)' : 'color-mix(in srgb, var(--color-text) 45%, transparent)';
    t.innerHTML =
      '<div style="position:absolute;left:0;top:' + W + 'px;width:' + W + 'px;height:' + h + 'px;transform-origin:center top;transform:rotateX(90deg);background:var(--color-neutral-200);border:1px solid ' + bc + ';box-sizing:border-box"></div>' +
      '<div style="position:absolute;left:-' + h + 'px;top:0;width:' + h + 'px;height:' + W + 'px;transform-origin:right center;transform:rotateY(90deg);background:var(--color-neutral-300);border:1px solid ' + bc + ';box-sizing:border-box"></div>' +
      '<div style="position:absolute;inset:0;transform:translateZ(' + h + 'px);background:var(--color-bg);border:1px ' + bs + ' ' + bc + ';box-sizing:border-box">' +
        '<span style="position:absolute;left:12px;top:11px;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:' + stCol + '">' + (status || 'Planned') + '</span>' +
        '<span style="position:absolute;left:12px;right:12px;bottom:12px;font-family:var(--font-heading);font-weight:600;font-size:20px;line-height:1.02;letter-spacing:.02em;text-transform:uppercase;color:' + nameCol + '">' + name + '</span>' +
      '</div>';
    floor.appendChild(t); tiles.push(t);
  });
  stage.appendChild(floor);

  var readout = document.querySelector('[data-readout]');
  var hero = stage.closest('.hero') || stage.parentElement;
  var mx = 0, my = 0, tx = 0, ty = 0, drag = 0, down = null, t0 = performance.now();

  function rel(ev) { var r = stage.getBoundingClientRect(); return [(ev.clientX - r.left) / r.width - 0.5, (ev.clientY - r.top) / r.height - 0.5, ev.clientY]; }
  stage.addEventListener('pointerdown', function (ev) { down = { y: ev.clientY, d: drag }; try { stage.setPointerCapture(ev.pointerId); } catch (_) {} });
  stage.addEventListener('pointermove', function (ev) { var a = rel(ev); mx = a[0]; my = a[1]; if (down) drag = clamp(down.d - (a[2] - down.y) / 260, -1, 1); });
  stage.addEventListener('pointerup', function () { down = null; });
  stage.addEventListener('pointerleave', function () { mx = 0; my = 0; down = null; });

  function tick() {
    var now = (performance.now() - t0) / 1000;
    tx += (mx - tx) * 0.05; ty += (my - ty) * 0.05;
    var r = stage.getBoundingClientRect();
    var sc = clamp(Math.min(r.width / 840, r.height / 500), 0.5, 1.25);
    floor.style.transform = 'scale3d(' + sc + ',' + sc + ',' + sc + ') rotateX(' + (56 - ty * 4) + 'deg) rotateZ(' + (-36 + tx * 6) + 'deg)';
    var p = reduce ? 0 : clamp(window.scrollY / (hero.offsetHeight * 0.7));

    tiles.forEach(function (el, i) {
      var col = i % COLS, row = Math.floor(i / COLS);
      var a = reduce ? 1 : ease(clamp((now - 0.2 - (col + row) * 0.12) / 0.9));
      var hov = el.matches(':hover');
      var z = (1 - a) * 340 + p * (col + row) * 26 + (hov ? 18 : 0) - drag * (col + row) * 20;
      el.style.transform = 'translateZ(' + z.toFixed(1) + 'px)';
      el.style.opacity = a.toFixed(3);
    });
    if (readout) {
      var prog = reduce ? 1 : ease(clamp((now - 0.2) / 1.7)) * (1 - p);
      readout.textContent = 'Assembly ' + String(Math.round(prog * 100)).padStart(3, '0') + '%';
    }
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();
