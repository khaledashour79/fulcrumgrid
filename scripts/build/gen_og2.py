# -*- coding: utf-8 -*-
import os, json
FD = os.path.abspath(os.path.join(os.path.dirname(__file__),'ogfonts'))
OUT = os.path.join(os.path.dirname(__file__),'og_out2')
os.makedirs(OUT, exist_ok=True)
def furl(n): return 'file://%s/%s' % (FD, n)

CSS = '''
@font-face{font-family:'In';src:url('%s') format('woff2');font-weight:400;}
@font-face{font-family:'In';src:url('%s') format('woff2');font-weight:600;}
@font-face{font-family:'In';src:url('%s') format('woff2');font-weight:700;}
@font-face{font-family:'Ge';src:url('%s') format('woff2');font-weight:700;}
''' % (furl('inter-400.woff2'),furl('inter-600.woff2'),furl('inter-700.woff2'),furl('gelasio-700.woff2'))

TPL = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
%(css)s
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1200px;height:630px;}
body{font-family:'In',system-ui,sans-serif;background:#f0f2ed;color:#161d26;position:relative;overflow:hidden;}
.grid{position:absolute;inset:0;background-image:linear-gradient(#161d2609 1px,transparent 1px),linear-gradient(90deg,#161d2609 1px,transparent 1px);background-size:60px 60px;}
.frame{position:absolute;inset:22px;border:1px solid #161d2618;border-radius:14px;}
.accentbar{position:absolute;left:0;top:0;bottom:0;width:10px;background:%(accent)s;}
.wrap{position:absolute;inset:0;padding:74px 84px;display:flex;flex-direction:column;justify-content:space-between;}
.brand{display:flex;align-items:center;gap:15px;}
.mark{width:52px;height:52px;border:2px solid #2156df;border-radius:13px;display:flex;align-items:center;justify-content:center;position:relative;}
.mark b{font-family:'Ge',serif;font-weight:700;color:#2156df;font-size:26px;line-height:1;}
.mark i{position:absolute;right:9px;bottom:11px;width:5px;height:5px;border-radius:50%%;background:#2156df;}
.word{font-family:'In',sans-serif;font-weight:700;font-size:33px;letter-spacing:-.01em;}
.word .g{color:#2156df;}
.mid{display:flex;flex-direction:column;gap:22px;}
.eyebrow{display:flex;align-items:center;gap:11px;font-family:'In',sans-serif;font-weight:700;font-size:16px;letter-spacing:.16em;color:#5b6472;}
.dot{width:11px;height:11px;border-radius:50%%;background:%(accent)s;}
.head{font-family:'Ge',serif;font-weight:700;font-size:%(hsize)spx;line-height:1.05;letter-spacing:-.015em;max-width:1010px;}
.head .ac{color:#2156df;font-style:italic;}
.tag{font-family:'In',sans-serif;font-weight:600;font-size:27px;line-height:1.4;color:#3a424e;max-width:930px;}
.foot{display:flex;align-items:center;justify-content:space-between;}
.dom{font-family:'In',sans-serif;font-weight:600;font-size:24px;color:#5b6472;}
.dots{display:flex;gap:11px;}
.dots span{width:14px;height:14px;border-radius:50%%;}
</style></head><body>
<div class="grid"></div><div class="frame"></div><div class="accentbar"></div>
<div class="wrap">
  <div class="brand"><span class="mark"><b>F</b><i></i></span><span class="word">Fulcrum<span class="g">Grid</span></span></div>
  <div class="mid">
    <div class="eyebrow"><span class="dot"></span>%(eyebrow)s</div>
    <div class="head">%(head)s</div>
    <div class="tag">%(tag)s</div>
  </div>
  <div class="foot">
    <span class="dom" dir="ltr">fulcrumgrid.com</span>
    <span class="dots"><span style="background:#12a19a"></span><span style="background:#2156df"></span><span style="background:#e5537f"></span><span style="background:#c3c8cf"></span></span>
  </div>
</div></body></html>'''

CARDS = {
 'og-command-center': dict(accent='#12a19a', hsize=84, eyebrow='OPERATIONS',
   head='Command Center',
   tag='Real-time operations dashboard — live KPIs, alerts, automation, and reporting.'),
 'og-collection': dict(accent='#5b53d6', hsize=84, eyebrow='FINANCE',
   head='Collection',
   tag='Receivables and payments — invoice tracking, automated reminders, payment plans, and reconciliation.'),
 'og-hr-suite': dict(accent='#e5537f', hsize=84, eyebrow='PEOPLE',
   head='HR Suite',
   tag='People operations from hire to retire — records, onboarding, payroll, time, leave, and performance.'),
 'og-default': dict(accent='#2156df', hsize=76, eyebrow='BUSINESS APPS',
   head='One platform,<br><span class="ac">every operation.</span>',
   tag='Purpose-built business apps from one team — Command Center, Collection, HR Suite, and more.'),
}

for fn,c in CARDS.items():
    html = TPL % dict(css=CSS, accent=c['accent'], hsize=c['hsize'],
                      eyebrow=c['eyebrow'], head=c['head'], tag=c['tag'])
    open(os.path.join(OUT,fn+'.html'),'w',encoding='utf-8').write(html)
    print('wrote', fn)
open(os.path.join(OUT,'manifest.json'),'w').write(json.dumps(list(CARDS.keys())))
