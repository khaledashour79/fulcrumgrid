const { computeResults, totalsAtRealization } = require('../../assets/js/calculator.js');
const cfg = {
  fallback:{}, 
  activities:{ cvScreen:{manual:5,platform:1}, interview:{manual:25,platform:12}, payroll:{manual:8,platform:3}, iqama:{manual:40,platform:20}, letters:{manual:10,platform:2} },
  interviewsPerHire:12, staffCostMonthly:12000, productiveHours:160, realization:0.80
};
const input = { employees:500, annualHires:60, appsPerVacancy:50, iqamaRenewals:400, monthlyLetters:100,
  enabled:{recruitment:true,payroll:true,iqama:true,letters:true}, cfg };
const r = computeResults(input);
function approx(a,b,t){ return Math.abs(a-b) <= (t||1e-4); }
const checks = [
  ['Recruitment hrs', r.groups.recruitment.hoursYear, 284.8],
  ['Recruitment SAR', r.groups.recruitment.valueYear, 21360],
  ['Payroll hrs', r.groups.payroll.hoursYear, 400],
  ['Payroll SAR', r.groups.payroll.valueYear, 30000],
  ['Iqama hrs', r.groups.iqama.hoursYear, 106.66666666666667],
  ['Iqama SAR', r.groups.iqama.valueYear, 8000],
  ['Letters hrs', r.groups.letters.hoursYear, 128],
  ['Letters SAR', r.groups.letters.valueYear, 9600],
  ['Total hrs/yr', r.totalHoursYear, 919.4666666666667],
  ['Total hrs/mo', r.totalHoursMonth, 76.62222222222222],
  ['Total SAR/yr', r.totalValueYear, 68960],
  ['Total SAR/mo', r.totalValueMonth, 5746.666666666667],
  ['Hourly', r.hourly, 75],
];
let ok=true;
checks.forEach(([n,got,exp])=>{ const pass=approx(got,exp); if(!pass) ok=false; console.log((pass?'PASS':'FAIL')+'  '+n+' = '+got+'  (expected '+exp+')'); });
// Sensitivity
const lo = totalsAtRealization(input,0.5), hi = totalsAtRealization(input,1.0);
console.log('Sens 50%:  hrs='+lo.hoursYear.toFixed(2)+' SAR='+lo.valueYear.toFixed(0));
console.log('Sens 100%: hrs='+hi.hoursYear.toFixed(2)+' SAR='+hi.valueYear.toFixed(0));
// Toggle test: disable iqama
const r2 = computeResults(Object.assign({},input,{enabled:{recruitment:true,payroll:true,iqama:false,letters:true}}));
console.log('Iqama disabled -> total hrs='+r2.totalHoursYear.toFixed(4)+' (expect 812.8)');
// Zero activity
const r3 = computeResults(Object.assign({},input,{annualHires:0}));
console.log('Zero hires -> recruitment hrs='+r3.groups.recruitment.hoursYear+' (expect 0)');
console.log(ok ? '\nALL REFERENCE CHECKS PASS' : '\nSOME CHECKS FAILED');
process.exit(ok?0:1);
