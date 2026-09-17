import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'fs';
const dir='og_out';
const man=JSON.parse(fs.readFileSync(dir+'/manifest.json'));
const b=await chromium.launch({ executablePath:'/opt/pw-browsers/chromium' });
const p=await b.newPage({ viewport:{width:1200,height:630}, deviceScaleFactor:1 });
for(const [slug,lang,fn] of man){
  await p.goto('file://'+process.cwd()+'/'+dir+'/'+fn,{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(200);
  const out=dir+'/og-pricing-'+slug+(lang==='ar'?'-ar':'')+'.png';
  await p.screenshot({path:out});
  console.log('rendered',out);
}
await b.close();
