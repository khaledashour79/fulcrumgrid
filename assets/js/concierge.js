/* FulcrumGrid concierge — lower-left AI voice character (front-end).
 *
 * Config is provided by the page as window.FG_CONCIERGE = { endpoint, riveSrc, langs }.
 *
 * Worker API contract (workers/concierge/):
 *   POST  <endpoint>/chat   body { sessionId, lang, message, history:[{role,content}] }
 *         -> text/event-stream of `data: {"delta":"..."}` lines, ending `data: {"done":true}`
 *            (a plain JSON { reply } body is also accepted as a non-streaming fallback)
 *   POST  <endpoint>/tts    body { text, lang }
 *         -> audio/mpeg bytes (the Worker proxies the TTS vendor; keys stay server-side)
 *
 * The widget degrades gracefully: no endpoint -> character still greets and routes to
 * /contact; no Rive runtime/art -> built-in SVG placeholder; no SpeechRecognition ->
 * text input only; no Worker TTS -> browser speechSynthesis.
 */
(function () {
  'use strict';
  var CFG = window.FG_CONCIERGE || {};
  var mount = document.getElementById('fg-concierge');
  if (!mount || mount.dataset.fgcInit) return;
  mount.dataset.fgcInit = '1';

  var docLang = (document.documentElement.lang || 'en').slice(0, 2).toLowerCase();
  var RTL = document.documentElement.dir === 'rtl' || docLang === 'ar';
  var langs = CFG.langs && CFG.langs.length ? CFG.langs : ['en'];
  var active = langs.indexOf(docLang) !== -1;           // voice/chat enabled for this locale?
  var endpoint = (CFG.endpoint || '').replace(/\/$/, '');

  // ---- copy ----
  var T = {
    en: { title: 'FulcrumGrid assistant', invite: "Hi — I'm here to help. Ask me anything about FulcrumGrid.",
          talk: 'Talk to me', placeholder: 'Type a message…', send: 'Send', listening: 'Listening…',
          thinking: 'Thinking…', mic: 'Hold to talk', close: 'Close', dismiss: 'Dismiss',
          consent: 'Tap the mic to talk — your voice is sent to our assistant to answer you. ',
          contact: 'Contact us', err: "Sorry — I couldn't reach the assistant. Please try the contact page.",
          sr: "Voice isn't supported in this browser — you can type instead." },
    ar: { title: 'مساعد FulcrumGrid', invite: 'مرحبًا — أنا هنا للمساعدة. اسألني أي شيء عن FulcrumGrid.',
          talk: 'تحدّث إليّ', placeholder: 'اكتب رسالة…', send: 'إرسال', listening: 'أستمع…',
          thinking: 'أفكّر…', mic: 'اضغط للتحدّث', close: 'إغلاق', dismiss: 'إخفاء',
          consent: 'اضغط الميكروفون للتحدّث — يُرسَل صوتك إلى مساعدنا للإجابة عليك. ',
          contact: 'تواصل معنا', err: 'عذرًا — تعذّر الوصول إلى المساعد. جرّب صفحة التواصل من فضلك.',
          sr: 'الإدخال الصوتي غير مدعوم في هذا المتصفح — يمكنك الكتابة بدلًا من ذلك.' }
  };
  var t = T[docLang] || T.en;
  var contactHref = (docLang === 'en' ? '' : '/' + docLang) + '/contact/';

  // ---- small helpers ----
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) {} }
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) {} }
  var inviteDismissed = !!ss('fgc_invite_dismissed');   // greeting bubble dismissed this visit (character stays as launcher)

  var sessionId = ss('fgc_sid') || (Math.random().toString(36).slice(2) + Date.now().toString(36));
  ss('fgc_sid', sessionId);
  var history = [];
  var busy = false;

  // ---- DOM ----
  var stage = el('button', 'fgc-stage');
  stage.setAttribute('aria-label', t.talk);
  stage.appendChild(placeholderSVG());
  var ring = el('span', 'fgc-ring'); stage.appendChild(ring);

  var invite = el('div', 'fgc-invite');
  invite.innerHTML = '<button class="fgc-x" aria-label="' + t.dismiss + '">×</button>' +
    '<div>' + esc(t.invite) + '</div>' +
    '<button class="fgc-cta">🎙 ' + esc(t.talk) + '</button>';

  var panel = el('div', 'fgc-panel');
  panel.setAttribute('role', 'dialog'); panel.setAttribute('aria-label', t.title);
  panel.innerHTML =
    '<div class="fgc-head"><span class="fgc-dot"></span><span class="fgc-title">' + esc(t.title) + '</span>' +
      '<span class="fgc-status" aria-live="polite"><span class="fgc-wave"><i></i><i></i><i></i><i></i></span><span class="fgc-status-txt"></span></span>' +
      '<button class="fgc-min" aria-label="' + t.close + '">–</button></div>' +
    '<div class="fgc-log" aria-live="polite"></div>' +
    '<div class="fgc-foot">' +
      '<button class="fgc-mic" aria-label="' + t.mic + '" aria-pressed="false">' + micIcon() + '</button>' +
      '<input class="fgc-input" type="text" placeholder="' + esc(t.placeholder) + '" aria-label="' + esc(t.placeholder) + '">' +
      '<button class="fgc-send">' + esc(t.send) + '</button></div>' +
    '<div class="fgc-consent" hidden>' + esc(t.consent) + '<a href="' + contactHref + '">' + esc(t.contact) + '</a></div>';

  mount.appendChild(panel); mount.appendChild(invite); mount.appendChild(stage);
  var log = panel.querySelector('.fgc-log');
  var statusTxt = panel.querySelector('.fgc-status-txt');
  var micBtn = panel.querySelector('.fgc-mic');
  var input = panel.querySelector('.fgc-input');
  var consentBox = panel.querySelector('.fgc-consent');

  // ---- reveal (not intrusive): after a short delay, unless dismissed ----
  function reveal() { mount.hidden = false; }
  if (document.readyState === 'complete') setTimeout(reveal, 3500);
  else window.addEventListener('load', function () { setTimeout(reveal, 3500); });

  // ---- state machine (drives Rive if present, else CSS classes) ----
  var rive = null, riveInputs = {};
  var STATES = ['idle', 'listening', 'thinking', 'talking'];
  function setState(s) {
    STATES.forEach(function (x) { mount.classList.toggle('is-' + x, x === s); });
    statusTxt.textContent = s === 'listening' ? t.listening : (s === 'thinking' ? t.thinking : '');
    if (riveInputs.state) { try { riveInputs.state.value = STATES.indexOf(s); } catch (e) {} }
    if (s !== 'talking' && riveInputs.mouth) { try { riveInputs.mouth.value = 0; } catch (e) {} }
  }
  function setMouth(v) {
    v = Math.max(0, Math.min(1, v || 0));
    if (riveInputs.mouth) { try { riveInputs.mouth.value = v; } catch (e) {} }
    try { mount.style.setProperty('--fgc-mouth', v.toFixed(3)); } catch (e) {}   // drives the SVG placeholder mouth
  }
  setState('idle');

  // ---- open / close ----
  function open() {
    dismissInvite();                               // once engaged, drop the proactive greeting
    mount.classList.add('is-open'); mount.hidden = false;
    if (!ls('fgc_consent')) consentBox.hidden = false;
    setTimeout(function () { input.focus(); }, 60);
  }
  function close() { mount.classList.remove('is-open'); }      // collapse to the character launcher
  // The "×" dismisses only the greeting bubble; the character stays as a quiet,
  // always-clickable launcher so the chat can always be reopened.
  function dismissInvite() { inviteDismissed = true; ss('fgc_invite_dismissed', '1'); mount.classList.add('fgc-no-invite'); }

  stage.addEventListener('click', function () { mount.classList.contains('is-open') ? close() : open(); });
  invite.querySelector('.fgc-cta').addEventListener('click', open);
  invite.querySelector('.fgc-x').addEventListener('click', function (e) { e.stopPropagation(); dismissInvite(); });
  panel.querySelector('.fgc-min').addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && mount.classList.contains('is-open')) close(); });

  // ---- conversation ----
  function addMsg(role, text, isCaption) {
    var m = el('div', 'fgc-msg ' + (role === 'user' ? 'user' : 'bot') + (isCaption ? ' is-caption' : ''), esc(text));
    log.appendChild(m); log.scrollTop = log.scrollHeight; return m;
  }

  // Per-turn speech pipeline state (one turn at a time, since ask() gates on busy).
  var ttsQueue = [], ttsPlaying = false, streamDone = false;

  function ask(text) {
    text = (text || '').trim(); if (!text || busy) return;
    addMsg('user', text);
    history.push({ role: 'user', content: text });
    input.value = '';
    if (!endpoint) {                               // backend not wired yet → route to a human
      addMsg('bot', t.err);
      setTimeout(function () { location.href = contactHref; }, 1200);
      return;
    }
    busy = true; setState('thinking');
    var bubble = addMsg('bot', '…');
    ttsQueue = []; ttsPlaying = false; streamDone = false;
    var spokenChars = 0, firstDone = false;

    // Fire the first complete sentence at TTS as soon as it streams in, so the
    // voice starts within ~1s instead of after the whole answer. The remainder
    // goes as one more call on completion — at most 2 /tts calls per turn.
    function onText(full) {
      if (firstDone) return;
      var m = full.slice(spokenChars).match(/^[\s\S]*?[.!?؟\n]["')»”]?(\s|$)/);
      if (m && m[0].trim().length >= 12) {
        firstDone = true;
        var sentence = full.slice(spokenChars, spokenChars + m[0].length).trim();
        spokenChars += m[0].length;
        enqueueSpeak(sentence);
      }
    }

    streamChat(text, bubble, onText).then(function (reply) {
      history.push({ role: 'assistant', content: reply });
      busy = false; streamDone = true;
      var rest = (reply || '').slice(spokenChars).trim();
      if (rest) enqueueSpeak(rest);
      pumpQueue();                                 // handle the already-drained case
      if (!firstDone && !rest) setState('idle');   // empty reply
    }).catch(function () { bubble.textContent = t.err; busy = false; streamDone = true; setState('idle'); });
  }

  function streamChat(message, bubble, onText) {
    var body = JSON.stringify({ sessionId: sessionId, lang: docLang, message: message, history: history.slice(0, -1) });
    return fetch(endpoint + '/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: body })
      .then(function (r) {
        if (!r.ok) throw new Error('chat ' + r.status);
        var ct = r.headers.get('content-type') || '';
        if (ct.indexOf('text/event-stream') === -1 || !r.body) {
          return r.json().then(function (j) { var txt = j.reply || ''; bubble.textContent = txt; if (onText) onText(txt); return txt; });
        }
        var reader = r.body.getReader(), dec = new TextDecoder(), buf = '', out = '';
        bubble.textContent = '';
        return (function pump() {
          return reader.read().then(function (res) {
            if (res.done) return out;
            buf += dec.decode(res.value, { stream: true });
            var lines = buf.split('\n'); buf = lines.pop();
            lines.forEach(function (ln) {
              ln = ln.trim(); if (ln.indexOf('data:') !== 0) return;
              var payload = ln.slice(5).trim(); if (!payload) return;
              try { var d = JSON.parse(payload);
                if (d.delta) { out += d.delta; bubble.textContent = out; log.scrollTop = log.scrollHeight; if (onText) onText(out); }
              } catch (e) {}
            });
            return pump();
          });
        })();
      });
  }

  // ---- ordered speech queue: fetch each chunk's audio and play it in turn,
  //      with lip-flap; browser speechSynthesis is the per-chunk fallback. ----
  var audioEl = null, audioCtx = null, analyser = null, rafId = 0;
  function enqueueSpeak(text) {
    if (!text) return;
    ttsQueue.push(text);
    setState('talking');
    pumpQueue();
  }
  function pumpQueue() {
    if (ttsPlaying) return;
    if (!ttsQueue.length) { if (streamDone) finishSpeaking(); return; }
    ttsPlaying = true;
    var text = ttsQueue.shift();
    fetch(endpoint + '/tts', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text: text, lang: docLang }) })
      .then(function (r) { if (!r.ok) throw 0; return r.blob(); })
      .then(function (blob) { playBlob(blob); })
      .catch(function () { browserSpeakChunk(text); });   // keep the queue moving
  }
  function playBlob(blob) {
    try {
      if (!audioEl) { audioEl = new Audio(); audioEl.addEventListener('ended', onChunkEnd); audioEl.addEventListener('error', onChunkEnd); }
      audioEl.src = URL.createObjectURL(blob);
      startAnalyser(audioEl);
      audioEl.play().catch(function () { onChunkEnd(); });
    } catch (e) { onChunkEnd(); }
  }
  function onChunkEnd() { ttsPlaying = false; if (rafId) cancelAnimationFrame(rafId); setMouth(0); pumpQueue(); }
  function finishSpeaking() { if (rafId) cancelAnimationFrame(rafId); setMouth(0); setState('idle'); }
  function startAnalyser(a) {
    try {
      audioCtx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') { try { audioCtx.resume(); } catch (e) {} }
      if (!a._fgcSrc) { a._fgcSrc = audioCtx.createMediaElementSource(a); analyser = audioCtx.createAnalyser(); analyser.fftSize = 256; a._fgcSrc.connect(analyser); analyser.connect(audioCtx.destination); }
      var data = new Uint8Array(analyser.frequencyBinCount);
      (function tick() {
        if (!analyser) return; analyser.getByteFrequencyData(data);
        var s = 0; for (var i = 0; i < data.length; i++) s += data[i];
        setMouth((s / data.length) / 110);
        rafId = requestAnimationFrame(tick);
      })();
    } catch (e) {}
  }
  function browserSpeakChunk(text) {
    try {
      if (!('speechSynthesis' in window)) { onChunkEnd(); return; }
      var u = new SpeechSynthesisUtterance(text);
      u.lang = sttLang();
      var flap = setInterval(function () { setMouth(Math.random() * 0.8); }, 90);
      u.onend = function () { clearInterval(flap); onChunkEnd(); };
      u.onerror = function () { clearInterval(flap); onChunkEnd(); };
      speechSynthesis.speak(u);
    } catch (e) { onChunkEnd(); }
  }

  // ---- speech recognition (STT) ----
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  var recog = null, listening = false;
  function sttLang() {
    return { en: 'en-US', ar: 'ar-SA', fr: 'fr-FR', de: 'de-DE', es: 'es-ES', it: 'it-IT', nl: 'nl-NL' }[docLang] || 'en-US';
  }
  function toggleMic() {
    if (!active) { location.href = contactHref; return; }
    if (!SR) { addMsg('bot', t.sr, true); input.focus(); return; }
    ls('fgc_consent', '1'); consentBox.hidden = true;
    listening ? stopListening() : startListening();
  }
  function startListening() {
    try {
      recog = new SR(); recog.lang = sttLang(); recog.interimResults = true; recog.maxAlternatives = 1;
      var finalTxt = '';
      recog.onresult = function (ev) {
        var interim = '';
        for (var i = ev.resultIndex; i < ev.results.length; i++) {
          var r = ev.results[i]; if (r.isFinal) finalTxt += r[0].transcript; else interim += r[0].transcript;
        }
        statusTxt.textContent = (finalTxt + interim) || t.listening;
      };
      recog.onerror = function () { stopListening(); };
      recog.onend = function () { setMic(false); mount.classList.remove('is-listening'); if (finalTxt.trim()) ask(finalTxt); };
      recog.start(); listening = true; setMic(true); setState('listening');
    } catch (e) { setMic(false); }
  }
  function stopListening() { listening = false; setMic(false); try { recog && recog.stop(); } catch (e) {} }
  function setMic(on) { micBtn.setAttribute('aria-pressed', on ? 'true' : 'false'); }

  micBtn.addEventListener('click', toggleMic);
  panel.querySelector('.fgc-send').addEventListener('click', function () { ask(input.value); });
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter') ask(input.value); });

  // ---- optional Rive character ----
  loadRive();
  function loadRive() {
    if (!CFG.riveSrc) return;
    ensureRiveRuntime(function (ok) {
      if (!ok || !window.rive) return;                 // keep SVG placeholder
      try {
        var canvas = document.createElement('canvas');
        var old = stage.querySelector('svg'); if (old) old.replaceWith(canvas);
        rive = new window.rive.Rive({
          src: CFG.riveSrc, canvas: canvas, autoplay: true,
          stateMachines: 'Concierge', fit: 'contain',
          onLoad: function () {
            try {
              rive.resizeDrawingSurfaceToCanvas();
              var sm = rive.stateMachineInputs('Concierge') || [];
              sm.forEach(function (i) { if (i.name === 'state') riveInputs.state = i; if (i.name === 'mouth') riveInputs.mouth = i; });
              setState('idle');
            } catch (e) {}
          }
        });
      } catch (e) {}
    });
  }
  function ensureRiveRuntime(cb) {
    if (window.rive) return cb(true);
    var s = document.createElement('script');
    s.src = '/assets/js/rive.min.js'; s.async = true;
    s.onload = function () { cb(true); }; s.onerror = function () { cb(false); };
    document.head.appendChild(s);
  }

  // ---- built-in placeholder character (brand-styled standing figure) ----
  function placeholderSVG() {
    var wrap = el('span', 'fgc-float fgc-char');
    wrap.innerHTML =
      '<svg viewBox="0 0 120 184" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="FulcrumGrid assistant">' +
      '<defs>' +
        '<linearGradient id="fgcBody" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6d92b6"/><stop offset="1" stop-color="#4f749a"/></linearGradient>' +
        '<linearGradient id="fgcHead" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7498bb"/><stop offset="1" stop-color="#5980a6"/></linearGradient>' +
      '</defs>' +
      '<ellipse class="fgc-shadow" cx="60" cy="176" rx="32" ry="6" fill="rgba(29,31,32,.12)"/>' +
      // body + arms
      '<g class="fgc-body">' +
        '<rect x="51" y="86" width="18" height="34" rx="8" fill="url(#fgcBody)"/>' +   // neck
        '<path d="M30 180 v-40 a30 30 0 0 1 60 0 v40 z" fill="url(#fgcBody)"/>' +
        '<rect class="fgc-arm fgc-arm-l" x="24" y="120" width="12" height="40" rx="6" fill="url(#fgcBody)"/>' +
        '<rect class="fgc-arm fgc-arm-r" x="84" y="120" width="12" height="40" rx="6" fill="url(#fgcBody)"/>' +
        // lanyard + accent badge (reads as a helpful rep)
        '<path d="M52 112 L58 140 M68 112 L62 140" stroke="#2d4660" stroke-width="2.4" fill="none" opacity=".55"/>' +
        '<rect x="54" y="138" width="12" height="9" rx="2" fill="#f2f2f3"/>' +
        '<rect x="56" y="140.5" width="8" height="2" rx="1" fill="#5980a6"/>' +
      '</g>' +
      // head group (leans in when listening via CSS)
      '<g class="fgc-head">' +
        '<circle cx="60" cy="66" r="31" fill="url(#fgcHead)"/>' +
        // headset
        '<path d="M31 66 a29 23 0 0 1 58 0" fill="none" stroke="#3a597a" stroke-width="4" stroke-linecap="round" opacity=".9"/>' +
        '<rect x="27" y="62" width="7" height="13" rx="3" fill="#3a597a"/>' +
        '<rect x="86" y="62" width="7" height="13" rx="3" fill="#3a597a"/>' +
        '<path class="fgc-boom" d="M30 72 q-6 14 18 18" fill="none" stroke="#3a597a" stroke-width="2.6" stroke-linecap="round"/>' +
        '<circle cx="49" cy="91" r="2.6" fill="#3a597a"/>' +
        // eyes (with lids for blinking)
        '<g class="fgc-eyes">' +
          '<ellipse cx="50" cy="63" rx="5" ry="5.4" fill="#fff"/><ellipse cx="70" cy="63" rx="5" ry="5.4" fill="#fff"/>' +
          '<circle class="fgc-pupil" cx="50.5" cy="64" r="2.3" fill="#1d1f20"/><circle class="fgc-pupil" cx="70.5" cy="64" r="2.3" fill="#1d1f20"/>' +
          '<rect class="fgc-lid" x="44.6" y="57" width="10.8" height="11" rx="5" fill="url(#fgcHead)"/>' +
          '<rect class="fgc-lid" x="64.6" y="57" width="10.8" height="11" rx="5" fill="url(#fgcHead)"/>' +
        '</g>' +
        // mouth (scaleY driven by --fgc-mouth while talking)
        '<g class="fgc-mouth-g"><ellipse class="fgc-mouth" cx="60" cy="80" rx="7" ry="4.2" fill="#223247"/></g>' +
      '</g>' +
      '</svg>';
    return wrap;
  }
  function micIcon() { return '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 15a3 3 0 0 0 3-3V6a3 3 0 1 0-6 0v6a3 3 0 0 0 3 3Zm5-3a5 5 0 0 1-10 0H5a7 7 0 0 0 6 6.92V22h2v-3.08A7 7 0 0 0 19 12h-2Z"/></svg>'; }
  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
})();
