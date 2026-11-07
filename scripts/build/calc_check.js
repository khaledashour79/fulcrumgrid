const { computeResults, totalsAtRealization } = require('../../assets/js/calculator.js');
const cfg = {
  fallback:{},
  activities:{ cvScreen:{manual:5,platform:1}, interview:{manual:25,platform:12}, payroll:{manual:8,platform:3}, iqama:{manual:40,platform:20}, letters:{manual:10,platform:2},
    attendance:{manual:6,platform:2}, performance:{manual:30,platform:12}, loans:{manual:20,platform:6}, eosb:{manual:90,platform:30}, airtickets:{manual:20,platform:5}, erp:{manual:45,platform:10} },
  interviewsPerHire:12, reviewCyclesPerYear:1, erpPostingsPerYear:12,
  staffCostMonthly:12000, productiveHours:160, realization:0.80
};
const ALL = {recruitment:true,payroll:true,iqama:true,letters:true,attendance:true,performance:true,loans:true,eosb:true,airtickets:true,erp:true};
const input = { employees:500, annualHires:60, appsPerVacancy:50, iqamaRenewals:400, monthlyLetters:100,
  annualLeavers:60, loanRequests:75, airTickets:200,
  enabled:Object.assign({},ALL), cfg };
const r = computeResults(input);
function approx(a,b,t){ return Math.abs(a-b) <= (t||1e-4); }
const checks = [
  // Original four groups — formulas unchanged.
  ['Recruitment hrs', r.groups.recruitment.hoursYear, 284.8],
  ['Recruitment SAR', r.groups.recruitment.valueYear, 21360],
  ['Payroll hrs', r.groups.payroll.hoursYear, 400],
  ['Payroll SAR', r.groups.payroll.valueYear, 30000],
  ['Iqama hrs', r.groups.iqama.hoursYear, 106.66666666666667],
  ['Iqama SAR', r.groups.iqama.valueYear, 8000],
  ['Letters hrs', r.groups.letters.hoursYear, 128],
  ['Letters SAR', r.groups.letters.valueYear, 9600],
  // Added groups.
  ['Attendance hrs', r.groups.attendance.hoursYear, 320],
  ['Attendance SAR', r.groups.attendance.valueYear, 24000],
  ['Performance hrs', r.groups.performance.hoursYear, 120],
  ['Performance SAR', r.groups.performance.valueYear, 9000],
  ['Loans hrs', r.groups.loans.hoursYear, 14],
  ['Loans SAR', r.groups.loans.valueYear, 1050],
  ['EOSB hrs', r.groups.eosb.hoursYear, 48],
  ['EOSB SAR', r.groups.eosb.valueYear, 3600],
  ['Air tickets hrs', r.groups.airtickets.hoursYear, 40],
  ['Air tickets SAR', r.groups.airtickets.valueYear, 3000],
  ['ERP postings hrs', r.groups.erp.hoursYear, 5.6],
  ['ERP postings SAR', r.groups.erp.valueYear, 420],
  // Totals (all ten groups on).
  ['Total hrs/yr', r.totalHoursYear, 1467.0666666666666],
  ['Total hrs/mo', r.totalHoursMonth, 122.25555555555555],
  ['Total SAR/yr', r.totalValueYear, 110030],
  ['Total SAR/mo', r.totalValueMonth, 9169.166666666666],
  ['Hourly', r.hourly, 75],
];
let ok=true;
checks.forEach(([n,got,exp])=>{ const pass=approx(got,exp); if(!pass) ok=false; console.log((pass?'PASS':'FAIL')+'  '+n+' = '+got+'  (expected '+exp+')'); });
// Sensitivity
const lo = totalsAtRealization(input,0.5), hi = totalsAtRealization(input,1.0);
console.log('Sens 50%:  hrs='+lo.hoursYear.toFixed(2)+' SAR='+lo.valueYear.toFixed(0));
console.log('Sens 100%: hrs='+hi.hoursYear.toFixed(2)+' SAR='+hi.valueYear.toFixed(0));
// Toggle test: disable iqama -> total drops by the iqama group only.
const r2 = computeResults(Object.assign({},input,{enabled:Object.assign({},ALL,{iqama:false})}));
console.log('Iqama disabled -> total hrs='+r2.totalHoursYear.toFixed(4)+' (expect 1360.4)');
// Original four only (back-compat): enabling just the first four reproduces the original total.
const r4 = computeResults(Object.assign({},input,{enabled:{recruitment:true,payroll:true,iqama:true,letters:true}}));
console.log('First four only -> total hrs='+r4.totalHoursYear.toFixed(4)+' SAR='+r4.totalValueYear+' (expect 919.4667 / 68960)');
// Zero activity
const r3 = computeResults(Object.assign({},input,{annualHires:0}));
console.log('Zero hires -> recruitment hrs='+r3.groups.recruitment.hoursYear+' (expect 0)');
console.log(ok ? '\nALL REFERENCE CHECKS PASS' : '\nSOME CHECKS FAILED');
process.exit(ok?0:1);
