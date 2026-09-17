# -*- coding: utf-8 -*-
import os
FD = os.path.abspath(os.path.join(os.path.dirname(__file__),'ogfonts'))
OUT = os.path.join(os.path.dirname(__file__),'og_out')
os.makedirs(OUT, exist_ok=True)

def furl(name): return 'file://%s/%s' % (FD, name)

# per app: accent (eyebrow dot), and copy in EN + AR
APPS = {
 'command-center': dict(accent='#12a19a',
   en=dict(eyebrow='COMMAND CENTER', app='Command Center',
           price='From SAR 490', per='/ month',
           plans='Pilot · Growth · Enterprise'),
   ar=dict(eyebrow='مركز القيادة', app='مركز القيادة',
           price='من SAR 490', per='/ شهريًا',
           plans='التجريبية · النمو · المؤسسات')),
 'collection': dict(accent='#5b53d6',
   en=dict(eyebrow='COLLECTION', app='Collection',
           price='From $12', per='/ user / month',
           plans='Starter · Professional · Business · Enterprise / Agency'),
   ar=dict(eyebrow='التحصيل', app='التحصيل',
           price='من $12', per='/ لكل مستخدم شهريًا',
           plans='المبتدئة · الاحترافية · الأعمال · المؤسسات / الوكالات')),
 'hr-suite': dict(accent='#e5537f',
   en=dict(eyebrow='HR SUITE', app='HR Suite',
           price='From SAR 15', per='/ seat / month',
           plans='Essentials · Operations · Payroll & Compliance · Enterprise'),
   ar=dict(eyebrow='منظومة الموارد البشرية', app='الموارد البشرية',
           price='من SAR 15', per='/ لكل مقعد شهريًا',
           plans='الأساسية · العمليات · الرواتب والامتثال · المؤسسات')),
}

# EN: "{App} pricing" with pricing cobalt. AR: "أسعار {App}" with أسعار cobalt.
def head_html(lang, app):
    if lang=='en':
        return '%s <span class="ac">pricing</span>' % app
    return '<span class="ac">أسعار</span> %s' % app

CSS = '''
@font-face{font-family:'In';src:url('%s') format('woff2');font-weight:400;}
@font-face{font-family:'In';src:url('%s') format('woff2');font-weight:600;}
@font-face{font-family:'In';src:url('%s') format('woff2');font-weight:700;}
@font-face{font-family:'Ge';src:url('%s') format('woff2');font-weight:700;}
@font-face{font-family:'Ca';src:url('%s') format('woff2');font-weight:600;}
@font-face{font-family:'Ca';src:url('%s') format('woff2');font-weight:700;}
''' % (furl('inter-400.woff2'),furl('inter-600.woff2'),furl('inter-700.woff2'),
       furl('gelasio-700.woff2'),furl('cairo-600.woff2'),furl('cairo-700.woff2'))

TPL = '''<!doctype html><html lang="%(lang)s"%(dir)s><head><meta charset="utf-8"><style>
%(css)s
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1200px;height:630px;}
body{
  font-family:%(body)s,system-ui,sans-serif;
  background:#f0f2ed;
  color:#161d26;
  position:relative;overflow:hidden;
}
/* faint hairline grid */
.grid{position:absolute;inset:0;
  background-image:linear-gradient(#161d2609 1px,transparent 1px),linear-gradient(90deg,#161d2609 1px,transparent 1px);
  background-size:60px 60px;}
.frame{position:absolute;inset:22px;border:1px solid #161d2618;border-radius:14px;}
.accentbar{position:absolute;%(barside)s:0;top:0;bottom:0;width:10px;background:%(accent)s;}
.wrap{position:absolute;inset:0;padding:74px 84px;display:flex;flex-direction:column;justify-content:space-between;}
.brand{display:flex;align-items:center;gap:15px;}
.mark{width:52px;height:52px;border:2px solid #2156df;border-radius:13px;display:flex;align-items:center;justify-content:center;position:relative;}
.mark b{font-family:'Ge',serif;font-weight:700;color:#2156df;font-size:26px;line-height:1;}
.mark i{position:absolute;right:9px;bottom:11px;width:5px;height:5px;border-radius:50%%;background:#2156df;}
.word{font-family:'In',sans-serif;font-weight:700;font-size:33px;letter-spacing:-.01em;}
.word .g{color:#2156df;}
.mid{display:flex;flex-direction:column;gap:20px;%(align)s}
.eyebrow{display:flex;align-items:center;gap:11px;font-family:'In',sans-serif;font-weight:700;font-size:16px;letter-spacing:.16em;color:#5b6472;%(rev)s}
.dot{width:11px;height:11px;border-radius:50%%;background:%(accent)s;}
.head{font-family:%(disp)s,serif;font-weight:700;font-size:82px;line-height:1.04;letter-spacing:-.015em;}
.head .ac{color:#2156df;font-style:italic;}
.price{font-family:'In',sans-serif;font-weight:700;font-size:38px;color:#161d26;}
.price .per{font-weight:600;font-size:23px;color:#5b6472;margin-inline-start:8px;}
.plans{font-family:%(body)s,sans-serif;font-weight:600;font-size:24px;color:#3a424e;}
.foot{display:flex;align-items:center;justify-content:space-between;}
.dom{font-family:'In',sans-serif;font-weight:600;font-size:24px;color:#5b6472;}
.dots{display:flex;gap:11px;}
.dots span{width:14px;height:14px;border-radius:50%%;}
</style></head><body>
<div class="grid"></div><div class="frame"></div><div class="accentbar"></div>
<div class="wrap">
  <div class="brand">
    <span class="mark"><b>F</b><i></i></span>
    <span class="word">Fulcrum<span class="g">Grid</span></span>
  </div>
  <div class="mid">
    <div class="eyebrow"><span class="dot"></span>%(eyebrow)s</div>
    <div class="head">%(head)s</div>
    <div class="price">%(price)s<span class="per">%(per)s</span></div>
    <div class="plans">%(plans)s</div>
  </div>
  <div class="foot">
    <span class="dom" dir="ltr">fulcrumgrid.com</span>
    <span class="dots"><span style="background:#12a19a"></span><span style="background:#2156df"></span><span style="background:#e5537f"></span><span style="background:#c3c8cf"></span></span>
  </div>
</div>
</body></html>'''

manifest=[]
for slug,a in APPS.items():
    for lang in ('en','ar'):
        c=a[lang]; rtl = lang=='ar'
        body = "'Ca'" if rtl else "'In'"
        disp = "'Ca'" if rtl else "'Ge'"
        html = TPL % dict(
            lang=lang, dir=(' dir="rtl"' if rtl else ''), css=CSS,
            body=body, disp=disp, accent=a['accent'],
            barside=('right' if rtl else 'left'),
            align=('align-items:flex-end;text-align:right;' if rtl else ''),
            rev=('flex-direction:row-reverse;' if rtl else ''),
            eyebrow=c['eyebrow'], head=head_html(lang,c['app']),
            price=c['price'], per=c['per'], plans=c['plans'])
        fn = '%s-%s.html' % (slug, lang)
        open(os.path.join(OUT,fn),'w',encoding='utf-8').write(html)
        manifest.append((slug,lang,fn))
        print('wrote', fn)
import json
open(os.path.join(OUT,'manifest.json'),'w').write(json.dumps(manifest))
