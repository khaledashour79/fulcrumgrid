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
          thinking: 'Thinking…', speaking: 'Speaking…', voicehint: 'Tap the mic to stop',
          mic: 'Hold to talk', close: 'Close', dismiss: 'Dismiss',
          consent: 'Tap the mic to talk — your voice is sent to our assistant to answer you. ',
          contact: 'Contact us', err: "Sorry — I couldn't reach the assistant. Please try the contact page.",
          sr: "Voice isn't supported in this browser — you can type instead.",
          micdenied: "I couldn't use the mic — allow microphone access in your browser, or just type.",
          noheard: "I didn't catch that — tap the mic and try again, or type your question." },
    ar: { title: 'مساعد FulcrumGrid', invite: 'مرحبًا — أنا هنا للمساعدة. اسألني أي شيء عن FulcrumGrid.',
          talk: 'تحدّث إليّ', placeholder: 'اكتب رسالة…', send: 'إرسال', listening: 'أستمع…',
          thinking: 'أفكّر…', speaking: 'أتحدّث…', voicehint: 'اضغط الميكروفون للإيقاف',
          mic: 'اضغط للتحدّث', close: 'إغلاق', dismiss: 'إخفاء',
          consent: 'اضغط الميكروفون للتحدّث — يُرسَل صوتك إلى مساعدنا للإجابة عليك. ',
          contact: 'تواصل معنا', err: 'عذرًا — تعذّر الوصول إلى المساعد. جرّب صفحة التواصل من فضلك.',
          sr: 'الإدخال الصوتي غير مدعوم في هذا المتصفح — يمكنك الكتابة بدلًا من ذلك.',
          micdenied: 'تعذّر استخدام الميكروفون — اسمح بالوصول إلى الميكروفون في المتصفح، أو اكتب رسالتك.',
          noheard: 'لم ألتقط ذلك — اضغط الميكروفون وحاول مجددًا، أو اكتب سؤالك.' }
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
    '<div class="fgc-voice"><div class="fgc-orb"><i></i></div>' +
      '<div class="fgc-voice-status" aria-live="polite"></div>' +
      '<div class="fgc-voice-hint">' + esc(t.voicehint) + '</div></div>' +
    '<div class="fgc-foot">' +
      '<button class="fgc-mic" aria-label="' + t.mic + '" aria-pressed="false">' + micIcon() + '</button>' +
      '<input class="fgc-input" type="text" placeholder="' + esc(t.placeholder) + '" aria-label="' + esc(t.placeholder) + '">' +
      '<button class="fgc-send">' + esc(t.send) + '</button></div>' +
    '<div class="fgc-consent" hidden>' + esc(t.consent) + '<a href="' + contactHref + '">' + esc(t.contact) + '</a></div>';

  mount.appendChild(panel); mount.appendChild(invite); mount.appendChild(stage);
  var log = panel.querySelector('.fgc-log');
  var statusTxt = panel.querySelector('.fgc-status-txt');
  var voiceStatus = panel.querySelector('.fgc-voice-status');
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
    var word = s === 'listening' ? t.listening : (s === 'thinking' ? t.thinking : (s === 'talking' ? t.speaking : ''));
    statusTxt.textContent = (s === 'talking' && !voiceMode) ? '' : word;
    if (voiceStatus) voiceStatus.textContent = word;
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
    unlockAudio();                                 // bless audio while we're in the open gesture
    mount.classList.add('is-open'); mount.hidden = false;
    if (!ls('fgc_consent')) consentBox.hidden = false;
    setTimeout(function () { input.focus(); }, 60);
  }
  function close() { if (voiceMode) exitVoice(); mount.classList.remove('is-open'); }   // collapse to the character launcher
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
  // Voice-only mode: entered on a mic tap. No transcript/answer text is shown —
  // the visitor just speaks and hears the reply, and the mic auto-reopens after
  // each answer (hands-free loop). If audio can't play, we fall back to text.
  var voiceMode = false, canceling = false, turnSpoke = false,
      lastUserText = '', lastReply = '', vadHeard = false, noSpeechTimer = null;

  function ask(text) {
    text = (text || '').trim(); if (!text || busy) return;
    var vm = voiceMode;                            // this turn's mode (snapshot)
    lastUserText = text; lastReply = '';
    if (!vm) addMsg('user', text);                 // voice mode shows no transcript
    history.push({ role: 'user', content: text });
    if (!vm) input.value = '';
    if (!endpoint) {                               // backend not wired yet → route to a human
      if (vm) exitVoice();
      addMsg('bot', t.err);
      setTimeout(function () { location.href = contactHref; }, 1200);
      return;
    }
    busy = true; setState('thinking');
    var bubble = vm ? el('div') : addMsg('bot', '…');   // detached (invisible) in voice mode
    ttsQueue = []; ttsPlaying = false; streamDone = false; turnSpoke = false;
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
      lastReply = reply;
      busy = false; streamDone = true;
      var rest = (reply || '').slice(spokenChars).trim();
      if (rest) enqueueSpeak(rest);
      pumpQueue();                                 // handle the already-drained case
      if (!firstDone && !rest) { setState('idle'); if (vm) exitVoice(); }   // empty reply
    }).catch(function () {
      busy = false; streamDone = true; setState('idle');
      if (vm) exitVoice(); else bubble.textContent = t.err;
    });
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
  var audioEl = null, flapTimer = 0;
  // Mobile (esp. iOS) blocks audio that wasn't started by a user gesture, so a
  // spoken reply arriving seconds after the mic tap is silently refused. Prime
  // the <audio> element inside the gesture once — a tiny silent clip "blesses"
  // it — so later TTS can play. Playback uses this plain element (not Web Audio)
  // on purpose: after the mic has been used, Web Audio output gets stuck on the
  // phone earpiece, while a plain media element routes to the loudspeaker.
  var SILENT_MP3 = 'data:audio/mpeg;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA//tQxAADB8AhSmxhIIEVCSiJrDCQBTcu3UrAIwUdkRgQbFAZC1CQEwTJ9mjRvBA4UOLD8nKVOWfh+UlK3z/177OXrfOdKl7pyn3Xf//WreyTEFNRTMuMTAwVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV';
  function ensureAudioEl() {
    if (!audioEl) {
      audioEl = new Audio();
      try { audioEl.setAttribute('playsinline', ''); } catch (e) {}
      audioEl.addEventListener('ended', onChunkEnd);
      audioEl.addEventListener('error', onChunkEnd);
    }
    return audioEl;
  }
  function unlockAudio() {
    try {
      ensureAudioEl();
      if (!audioEl._fgcBlessed) {
        audioEl._fgcBlessed = true;
        audioEl.src = SILENT_MP3;
        var p = audioEl.play(); if (p && p.catch) p.catch(function () {});
      }
    } catch (e) {}
  }
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
      ensureAudioEl();
      audioEl.src = URL.createObjectURL(blob);
      startFlap();
      var p = audioEl.play();
      if (p && p.then) p.then(function () { turnSpoke = true; }).catch(function () { onChunkEnd(); });
    } catch (e) { onChunkEnd(); }
  }
  function onChunkEnd() { ttsPlaying = false; stopFlap(); setMouth(0); pumpQueue(); }
  function finishSpeaking() {
    stopFlap(); setMouth(0); setState('idle');
    if (!voiceMode) return;
    if (!turnSpoke) { revealTurn(); return; }                 // audio never played → reveal as text
    setTimeout(function () {                                    // hands-free: listen for the next question
      if (voiceMode && !busy && !recording && !listening && mount.classList.contains('is-open')) startMic();
    }, 550);
  }
  // Fallback: audio couldn't play, so drop out of voice mode and show the turn.
  function revealTurn() {
    voiceMode = false; mount.classList.remove('is-voice');
    if (lastUserText) addMsg('user', lastUserText);
    if (lastReply) addMsg('bot', lastReply);
    setState('idle');
  }
  // Plain-element playback gives us no amplitude to read, so the mouth is driven
  // by a gentle timed flap while a chunk is playing.
  function startFlap() { stopFlap(); flapTimer = setInterval(function () { setMouth(0.22 + Math.random() * 0.6); }, 95); }
  function stopFlap() { if (flapTimer) { clearInterval(flapTimer); flapTimer = 0; } }
  function browserSpeakChunk(text) {
    try {
      if (!('speechSynthesis' in window)) { onChunkEnd(); return; }
      var u = new SpeechSynthesisUtterance(text);
      u.lang = sttLang();
      var flap = setInterval(function () { setMouth(Math.random() * 0.8); }, 90);
      u.onend = function () { clearInterval(flap); turnSpoke = true; onChunkEnd(); };
      u.onerror = function () { clearInterval(flap); onChunkEnd(); };
      speechSynthesis.speak(u);
    } catch (e) { onChunkEnd(); }
  }

  // ---- speech-to-text: Web Speech API on desktop; on mobile/iOS (where it is
  //      unavailable or unreliable) record the mic and transcribe via /stt ----
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  var canRecord = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder);
  var isTouch = (navigator.maxTouchPoints > 0) || ('ontouchstart' in window) ||
                (window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  var useServerSTT = canRecord && (!SR || isTouch);
  var recog = null, listening = false;
  var mediaRec = null, recStream = null, recChunks = [], recording = false, recTimer = null;

  function sttLang() {
    return { en: 'en-US', ar: 'ar-SA', fr: 'fr-FR', de: 'de-DE', es: 'es-ES', it: 'it-IT', nl: 'nl-NL' }[docLang] || 'en-US';
  }
  function setMic(on) { micBtn.setAttribute('aria-pressed', on ? 'true' : 'false'); }

  function startMic() {
    if (useServerSTT) startRecording();
    else if (SR) startListening();
    else { exitVoice(); addMsg('bot', t.sr, true); input.focus(); }
  }
  function enterVoice() { voiceMode = true; mount.classList.add('is-voice'); }
  function exitVoice() {
    voiceMode = false; mount.classList.remove('is-voice');
    if (noSpeechTimer) { clearTimeout(noSpeechTimer); noSpeechTimer = null; }
    if (recording || listening) canceling = true;  // don't transcribe/answer a canceled turn
    ttsQueue = []; try { if (audioEl) audioEl.pause(); } catch (e) {}
    ttsPlaying = false; stopFlap(); setMouth(0);
    if (recording || listening) stopMic();
    setState('idle');
  }
  function toggleMic() {
    if (!active) { location.href = contactHref; return; }
    unlockAudio();                                 // the tap is our gesture — bless audio for the spoken reply
    ls('fgc_consent', '1'); consentBox.hidden = true;
    if (voiceMode) { exitVoice(); return; }        // a tap while in voice mode stops & exits
    if (recording || listening) { stopMic(); return; }
    enterVoice(); startMic();                       // mic tap → enter hands-free voice mode
  }
  function stopMic() {
    if (recording) { try { mediaRec && mediaRec.state !== 'inactive' && mediaRec.stop(); } catch (e) { recording = false; setMic(false); } }
    else stopListening();
  }

  // --- Web Speech (desktop) ---
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
      recog.onend = function () {
        setMic(false); mount.classList.remove('is-listening');
        if (canceling) { canceling = false; return; }
        if (finalTxt.trim()) ask(finalTxt);
        else if (voiceMode) exitVoice();                 // nothing said → end the hands-free loop
      };
      recog.start(); listening = true; setMic(true); setState('listening');
    } catch (e) { setMic(false); if (canRecord) startRecording(); }   // fall back to server STT
  }
  function stopListening() { listening = false; setMic(false); try { recog && recog.stop(); } catch (e) {} }

  // --- server STT (mobile/iOS): record, then transcribe through the Worker ---
  function pickMime() {
    var types = ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4', 'audio/aac', 'audio/ogg'];
    for (var i = 0; i < types.length; i++) { try { if (window.MediaRecorder.isTypeSupported(types[i])) return types[i]; } catch (e) {} }
    return '';
  }
  function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function (stream) {
      recStream = stream;
      var mime = pickMime();
      try { mediaRec = mime ? new MediaRecorder(stream, { mimeType: mime }) : new MediaRecorder(stream); }
      catch (e) { mediaRec = new MediaRecorder(stream); }
      recChunks = [];
      mediaRec.ondataavailable = function (e) { if (e.data && e.data.size) recChunks.push(e.data); };
      mediaRec.onstop = function () {
        if (recTimer) { clearTimeout(recTimer); recTimer = null; }
        if (noSpeechTimer) { clearTimeout(noSpeechTimer); noSpeechTimer = null; }
        stopStream();
        closeMicCtx();                        // release the record audio session → playback returns to the loudspeaker
        var blob = new Blob(recChunks, { type: (mediaRec && mediaRec.mimeType) || 'audio/webm' });
        recording = false; setMic(false); mount.classList.remove('is-listening');
        if (canceling) { canceling = false; setState('idle'); return; }          // exited/canceled → don't send
        if (blob.size > 1200) { setState('thinking'); statusTxt.textContent = t.thinking; sendSTT(blob); }
        else { setState('idle'); if (voiceMode) exitVoice(); }
      };
      mediaRec.start();
      recording = true; vadHeard = false; setMic(true); setState('listening'); statusTxt.textContent = t.listening;
      recTimer = setTimeout(function () { if (recording) stopMic(); }, 30000);   // 30s safety cap
      // Hands-free loop: if nothing is said, end quietly instead of hanging on the 30s cap.
      if (voiceMode) noSpeechTimer = setTimeout(function () { if (recording && voiceMode && !vadHeard) exitVoice(); }, 8000);
      startVAD(stream);                                                           // auto-stop on a pause
    }).catch(function () { setMic(false); setState('idle'); if (voiceMode) exitVoice(); addMsg('bot', t.micdenied, true); });
  }
  // Voice-activity auto-stop: once the visitor has spoken, end the recording
  // after ~1.4s of quiet so they don't have to tap the mic again. Falls back to
  // the 30s cap / manual tap if the audio context can't run (older browsers).
  // The VAD runs on its OWN short-lived AudioContext (micCtx), closed the moment
  // recording ends — never the playback path — so the mic's record audio session
  // doesn't trap the spoken reply on the earpiece.
  var micCtx = null;
  function closeMicCtx() { if (micCtx) { try { micCtx.close(); } catch (e) {} micCtx = null; } }
  function startVAD(stream) {
    try {
      micCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (micCtx.state === 'suspended') { try { micCtx.resume(); } catch (e) {} }
      var src = micCtx.createMediaStreamSource(stream);
      var vad = micCtx.createAnalyser(); vad.fftSize = 512;
      src.connect(vad);                                    // not to destination — no feedback
      var buf = new Uint8Array(vad.frequencyBinCount);
      var started = Date.now(), lastLoud = started, heard = false;
      var MIN_MS = 700, SILENCE_MS = 1400, LOUD = 12;
      (function monitor() {
        if (!recording || !micCtx) { try { src.disconnect(); } catch (e) {} return; }
        vad.getByteFrequencyData(buf);
        var s = 0; for (var i = 0; i < buf.length; i++) s += buf[i];
        var avg = s / buf.length, now = Date.now();
        if (avg > LOUD) { lastLoud = now; if (now - started > 200) { heard = true; vadHeard = true; } }
        if (heard && now - started > MIN_MS && now - lastLoud > SILENCE_MS) { try { src.disconnect(); } catch (e) {} stopMic(); return; }
        requestAnimationFrame(monitor);
      })();
    } catch (e) { /* no VAD — manual stop / 30s cap still apply */ }
  }
  function stopStream() { if (recStream) { try { recStream.getTracks().forEach(function (tr) { tr.stop(); }); } catch (e) {} recStream = null; } }
  function sendSTT(blob) {
    fetch(endpoint + '/stt?lang=' + encodeURIComponent(docLang), {
      method: 'POST', headers: { 'Content-Type': blob.type || 'audio/webm' }, body: blob
    }).then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (j) {
        var txt = (j && j.text || '').trim();
        if (txt) ask(txt); else { setState('idle'); addMsg('bot', t.noheard, true); }
      }).catch(function () { setState('idle'); addMsg('bot', t.err, true); });
  }

  micBtn.addEventListener('click', toggleMic);
  panel.querySelector('.fgc-send').addEventListener('click', function () { unlockAudio(); ask(input.value); });
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter') { unlockAudio(); ask(input.value); } });

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
