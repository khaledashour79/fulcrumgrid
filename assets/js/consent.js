/* FulcrumGrid — IP-based language defaulting + Arabic toggle geo-gate.
   On a first visit that lands on the English (root) tree, redirect the visitor
   to the language version matching their country, preserving the page path;
   English is the fallback for any unmapped country. Guardrails:
     • only from the root tree — never within /fr/, /de/, …, /ar/ (no loops);
     • only for real browsers — bots are skipped so every tree stays crawlable;
     • never once the visitor has used the switcher — that choice is remembered
       (localStorage 'fg_lang') and honored on later visits;
     • fails open to English if the lookup is unavailable.
   Arabic auto-defaults only in the GCC, but the Arabic switcher entry is shown
   across the wider Arabic-speaking (MENA) region and hidden elsewhere. One geo
   lookup per session, cached; the hreflang <link> tags are never touched. */
(function(){
  try{
    var path=location.pathname;
    var seg=(path.split('/')[1]||'').toLowerCase();
    var TREES={fr:1,de:1,es:1,it:1,nl:1,ar:1};   // language subdirectories
    var inLangTree=TREES[seg]===1;
    var onArabic=(seg==='ar')||(((document.documentElement.lang||'').toLowerCase().indexOf('ar'))===0);

    // Remember the visitor's explicit language choice when they use the switcher.
    document.addEventListener('click', function(ev){
      var t=ev.target, a=(t&&t.closest)?t.closest('.lang-dd-menu a[hreflang]'):null;
      if(a){ try{ localStorage.setItem('fg_lang',(a.getAttribute('hreflang')||'').toLowerCase()); }catch(e){} }
    }, true);

    // Country → language. Arabic only in the GCC; everything unmapped → English.
    var LANG_BY_CC={FR:'fr',BE:'fr',LU:'fr',MC:'fr',DE:'de',AT:'de',CH:'de',LI:'de',
      ES:'es',IT:'it',SM:'it',VA:'it',NL:'nl',SA:'ar',AE:'ar',QA:'ar',KW:'ar',BH:'ar',OM:'ar'};
    // Countries where the Arabic switcher entry stays visible (Arab League / MENA).
    var MENA=/^(SA|AE|QA|KW|BH|OM|YE|IQ|SY|JO|LB|PS|EG|SD|LY|TN|DZ|MA|MR|SO|DJ|KM|EH)$/;
    var BOT=/bot|crawl|spider|slurp|mediapartners|bingpreview|facebookexternalhit|embedly|quora|pinterest|slackbot|vkshare|w3c_validator|whatsapp|telegram|discord|applebot|yandex|baidu|duckduck|semrush|ahrefs|petal|lighthouse|headless/i;

    function hideArabicToggle(){
      var a=document.querySelectorAll('.lang-dd-menu a[hreflang="ar"]');
      for(var i=0;i<a.length;i++){ a[i].style.display='none'; }
    }
    function gate(cc){ if(!onArabic && cc && !MENA.test(cc)) hideArabicToggle(); }
    function go(lang){
      if(!lang || TREES[lang]!==1) return false;
      var here=path+location.search+location.hash;
      location.replace('/'+lang+here); return true;
    }

    var canRedirect=!inLangTree && !BOT.test(navigator.userAgent||'');
    var choice; try{ choice=(localStorage.getItem('fg_lang')||'').toLowerCase(); }catch(e){}

    // Returning visitor with a remembered non-English choice → send them there.
    if(canRedirect && choice && choice!=='en'){ if(go(choice)) return; }

    function handle(cc){
      if(canRedirect && !choice && go(LANG_BY_CC[cc])) return;  // first-visit default
      gate(cc);                                                 // stayed → gate toggle
    }

    var cc; try{ cc=sessionStorage.getItem('fg_geo_cc'); }catch(e){}
    if(cc){ handle(cc); return; }
    fetch('https://ipapi.co/json/').then(function(r){ return r.json(); }).then(function(d){
      var c=((d&&d.country_code)||'').toUpperCase();
      if(/^[A-Z]{2}$/.test(c)){ try{ sessionStorage.setItem('fg_geo_cc',c); }catch(e){} handle(c); }
    }).catch(function(){});
  }catch(e){}
})();

/* FulcrumGrid — cookie consent banner (Google Consent Mode) */
(function(){
  var KEY='fg_consent';
  var lang=((document.documentElement.lang||'en').toLowerCase().indexOf('ar')===0)?'ar':'en';
  var rtl=(document.documentElement.dir==='rtl')||lang==='ar';
  var T={
    en:{msg:'We use cookies for analytics to understand how this site is used. Analytics stay off until you accept.',accept:'Accept',decline:'Decline',more:'Privacy',href:'/privacy/'},
    ar:{msg:'نستخدم ملفات تعريف الارتباط لأغراض التحليلات لفهم كيفية استخدام هذا الموقع. تبقى التحليلات معطّلة حتى توافق.',accept:'قبول',decline:'رفض',more:'الخصوصية',href:'/ar/privacy/'}
  }[lang];
  function upd(g){ try{ if(window.gtag){ gtag('consent','update',{'analytics_storage':g?'granted':'denied','ad_storage':g?'granted':'denied','ad_user_data':g?'granted':'denied','ad_personalization':g?'granted':'denied'}); } }catch(e){} }
  var stored; try{ stored=localStorage.getItem(KEY); }catch(e){}
  if(stored==='granted'){ upd(true); return; }
  if(stored==='denied'){ upd(false); return; }

  function build(){
    var s=document.createElement('style');
    s.textContent='#fg-cc{position:fixed;z-index:9999;left:16px;right:16px;bottom:16px;max-width:560px;margin:0 auto;'
      +'background:#f8f9f5;border:1px solid #cbd0ca;border-radius:12px;padding:18px 20px;'
      +'box-shadow:0 24px 60px -24px rgba(22,29,38,.28);color:#161d26;'
      +'font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:13.5px;line-height:1.55;'
      +'opacity:0;transform:translateY(12px);transition:opacity .4s ease,transform .4s ease;}'
      +'#fg-cc.show{opacity:1;transform:none;}'
      +'#fg-cc.rtl{direction:rtl;font-family:Cairo,Tahoma,"Segoe UI",sans-serif;}'
      +'#fg-cc p{margin:0 0 14px;color:#59636f;}#fg-cc a{color:#1d47ba;text-decoration:none;}'
      +'#fg-cc .row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;}'
      +'#fg-cc button{font:inherit;cursor:pointer;border:none;padding:9px 18px;border-radius:8px;font-weight:600;font-size:12.5px;}'
      +'#fg-cc .ok{background:#2156df;color:#fff;}'
      +'#fg-cc .no{background:transparent;color:#59636f;border:1px solid #cbd0ca;}'
      +'#fg-cc .more{margin-inline-start:auto;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:#788291;}';
    document.head.appendChild(s);
    var d=document.createElement('div');
    d.id='fg-cc'; if(rtl) d.className='rtl';
    d.setAttribute('role','dialog'); d.setAttribute('aria-label','Cookie consent');
    d.innerHTML='<p>'+T.msg+'</p><div class="row">'
      +'<button class="ok">'+T.accept+'</button>'
      +'<button class="no">'+T.decline+'</button>'
      +'<a class="more" href="'+T.href+'">'+T.more+'</a></div>';
    document.body.appendChild(d);
    requestAnimationFrame(function(){ d.classList.add('show'); });
    d.querySelector('.ok').onclick=function(){ try{localStorage.setItem(KEY,'granted');}catch(e){} upd(true); d.remove(); };
    d.querySelector('.no').onclick=function(){ try{localStorage.setItem(KEY,'denied');}catch(e){} upd(false); d.remove(); };
  }
  if(document.body){ build(); } else { document.addEventListener('DOMContentLoaded', build); }
})();
