/* FulcrumGrid — cookie consent banner (Google Consent Mode) */
(function(){
  var KEY='fg_consent';
  function upd(g){ try{ if(window.gtag){ gtag('consent','update',{'analytics_storage':g?'granted':'denied','ad_storage':g?'granted':'denied'}); } }catch(e){} }
  var stored; try{ stored=localStorage.getItem(KEY); }catch(e){}
  if(stored==='granted'){ upd(true); return; }
  if(stored==='denied'){ upd(false); return; }

  function build(){
    var s=document.createElement('style');
    s.textContent='#fg-cc{position:fixed;z-index:9999;left:16px;right:16px;bottom:16px;max-width:560px;margin:0 auto;'
      +'background:#131a33;border:1px solid rgba(148,163,214,.28);border-radius:16px;padding:18px 20px;'
      +'box-shadow:0 24px 60px -24px rgba(0,0,0,.7);color:#e7ecf6;'
      +'font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:13.5px;line-height:1.55;'
      +'opacity:0;transform:translateY(12px);transition:opacity .4s ease,transform .4s ease;}'
      +'#fg-cc.show{opacity:1;transform:none;}'
      +'#fg-cc p{margin:0 0 14px;color:#9aa6c6;}#fg-cc a{color:#5eead4;text-decoration:none;}'
      +'#fg-cc .row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;}'
      +'#fg-cc button{font:inherit;cursor:pointer;border:none;padding:9px 18px;border-radius:8px;font-weight:600;font-size:12.5px;}'
      +'#fg-cc .ok{background:linear-gradient(135deg,#6366f1,#4f46e5);color:#fff;}'
      +'#fg-cc .no{background:transparent;color:#9aa6c6;border:1px solid rgba(148,163,214,.28);}'
      +'#fg-cc .more{margin-inline-start:auto;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:#6b779c;}';
    document.head.appendChild(s);
    var d=document.createElement('div');
    d.id='fg-cc';
    d.setAttribute('role','dialog'); d.setAttribute('aria-label','Cookie consent');
    d.innerHTML='<p>We use cookies for analytics to understand how this site is used. Analytics stay off until you accept.</p><div class="row">'
      +'<button class="ok">Accept</button>'
      +'<button class="no">Decline</button>'
      +'<a class="more" href="/privacy/">Privacy</a></div>';
    document.body.appendChild(d);
    requestAnimationFrame(function(){ d.classList.add('show'); });
    d.querySelector('.ok').onclick=function(){ try{localStorage.setItem(KEY,'granted');}catch(e){} upd(true); d.remove(); };
    d.querySelector('.no').onclick=function(){ try{localStorage.setItem(KEY,'denied');}catch(e){} upd(false); d.remove(); };
  }
  if(document.body){ build(); } else { document.addEventListener('DOMContentLoaded', build); }
})();
