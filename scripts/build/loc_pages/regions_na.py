# -*- coding: utf-8 -*-
"""Translations for the North America group of REGION pages.

Covers the regional hub (/regions/north-america/) and its country landing
pages (United States, Canada). Structure, nav/footer chrome and the shared
tagline come from i18n.py + COMMON; this module carries only each page's own
visible copy.

Brand/product names (FulcrumGrid, HR Suite), technical acronyms and agency
names (FLSA, W-2, IRS, EFW2, ACH, NACHA, FMLA, CPP, EI, CRA), plan names
(Enterprise), currency codes (CAD) and country codes (US, CA) stay as written.
Country/region names take their natural form per language. The "configurable /
statements not filings / W-2 statements not IRS EFW2" honesty hedges are
preserved exactly, not strengthened.
"""

def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# ---- Fragments shared across several pages in this group -------------------

T_EXPLORE =_t('Découvrir HR Suite', 'HR Suite entdecken', 'Explorar HR Suite',
               'Esplora HR Suite', 'Ontdek HR Suite')
T_SEE_PRICING = _t('Voir les tarifs HR Suite', 'HR Suite Preise ansehen',
                   'Ver los precios de HR Suite', 'Vedi i prezzi di HR Suite',
                   'Bekijk HR Suite-prijzen')
T_BUILT_IN = _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd')
T_CORE_HR_TITLE = _t('RH essentielles &amp; libre-service', 'Kern-HR &amp; Self-Service',
                     'RR. HH. esenciales &amp; autoservicio', 'HR di base &amp; self-service',
                     'Kern-HR &amp; selfservice')

PRICE_NOTE_EN = ('Every module here is part of HR Suite — advanced payroll, year-end and '
                 'compliance on the Enterprise plan, or added to any plan as a per-seat '
                 'add-on. <a href="/pricing/hr-suite/">See HR Suite pricing →</a>')
T_PRICE_NOTE = _t(
    'Chaque module ici fait partie de HR Suite — paie avancée, clôture de fin d\'année et conformité sur le plan Enterprise, ou ajouté à n\'importe quel plan en complément par utilisateur. <a href="/pricing/hr-suite/">Voir les tarifs HR Suite →</a>',
    'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Add-on pro Platz zu jedem Plan hinzufügbar. <a href="/pricing/hr-suite/">HR Suite Preise ansehen →</a>',
    'Cada módulo aquí forma parte de HR Suite — nómina avanzada, cierre de fin de año y cumplimiento en el plan Enterprise, o añadido a cualquier plan como complemento por puesto. <a href="/pricing/hr-suite/">Ver los precios de HR Suite →</a>',
    'Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura di fine anno e conformità nel piano Enterprise, oppure aggiunto a qualsiasi piano come add-on per postazione. <a href="/pricing/hr-suite/">Vedi i prezzi di HR Suite →</a>',
    'Elke module hier maakt deel uit van HR Suite — geavanceerde loonadministratie, jaarafsluiting en compliance in het Enterprise-plan, of toegevoegd aan elk plan als add-on per gebruiker. <a href="/pricing/hr-suite/">Bekijk HR Suite-prijzen →</a>')


def _hero(t):
    """Hero buttons — identical on every page in the group."""
    t['Explore HR Suite'] = T_EXPLORE
    t['See HR Suite pricing'] = T_SEE_PRICING
    return t


PAGE = {}


PAGE['/regions/north-america/'] = {'src': 'regions/north-america/index.html', 't': {
    'FulcrumGrid in North America — every app, built for your region | FulcrumGrid': _t(
        "FulcrumGrid en Amérique du Nord — chaque application, conçue pour votre région | FulcrumGrid",
        'FulcrumGrid in Nordamerika — jede App, gebaut für Ihre Region | FulcrumGrid',
        'FulcrumGrid en Norteamérica — cada app, diseñada para su región | FulcrumGrid',
        'FulcrumGrid in Nord America — ogni app, costruita per la tua regione | FulcrumGrid',
        'FulcrumGrid in Noord-Amerika — elke app, gebouwd voor uw regio | FulcrumGrid'),
    'FulcrumGrid across North America — HR Suite, Command Center and Collection — with configurable payroll by federal, state and provincial rule, real-time finance in USD and CAD, and receivables.': _t(
        "FulcrumGrid dans toute l'Amérique du Nord — HR Suite, Command Center et Collection — avec une paie configurable selon les règles fédérales, des États et provinciales, une finance en temps réel en USD et CAD, et le recouvrement.",
        'FulcrumGrid in ganz Nordamerika — HR Suite, Command Center und Collection — mit konfigurierbarer Gehaltsabrechnung nach Bundes-, Bundesstaats- und Provinzregelung, Echtzeit-Finanzverwaltung in USD und CAD und Forderungseinzug.',
        'FulcrumGrid en toda América del Norte — HR Suite, Command Center y Collection — con nómina configurable según normas federales, estatales y provinciales, finanzas en tiempo real en USD y CAD y cobros.',
        'FulcrumGrid in tutto il Nord America — HR Suite, Command Center e Collection — con buste paga configurabili secondo le norme federali, statali e provinciali, finanza in tempo reale in USD e CAD e recupero crediti.',
        'FulcrumGrid in heel Noord-Amerika — HR Suite, Command Center en Collection — met configureerbare loonadministratie volgens federale, staats- en provinciale regels, realtime financiën in USD en CAD en debiteuren.'),
    'North America · US &amp; Canada': _t(
        'Amérique du Nord · États-Unis &amp; Canada', 'Nordamerika · USA &amp; Kanada',
        'América del Norte · EE. UU. &amp; Canadá', 'Nord America · USA &amp; Canada',
        'Noord-Amerika · VS &amp; Canada'),
    'FulcrumGrid, built for <em style="font-style:normal;color:var(--color-accent)">North America</em>': _t(
        'FulcrumGrid, conçu pour <em style="font-style:normal;color:var(--color-accent)">l\'Amérique du Nord</em>',
        'FulcrumGrid, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Nordamerika</em>',
        'FulcrumGrid, diseñado para <em style="font-style:normal;color:var(--color-accent)">Norteamérica</em>',
        'FulcrumGrid, pensato per <em style="font-style:normal;color:var(--color-accent)">il Nord America</em>',
        'FulcrumGrid, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Noord-Amerika</em>'),
    'The whole grid runs across North America — HR Suite with configurable payroll and federal, state and provincial rules; Command Center with real-time finance and reporting in USD and CAD; and Collection for receivables and reminders. Pick a country for the detail.': _t(
        'Toute la grille fonctionne dans toute l\'Amérique du Nord — HR Suite avec une paie configurable et des règles fédérales, des États et provinciales ; Command Center avec une finance et un reporting en temps réel en USD et CAD ; et Collection pour le recouvrement et les relances. Choisissez un pays pour le détail.',
        'Das gesamte Grid läuft in ganz Nordamerika — HR Suite mit konfigurierbarer Gehaltsabrechnung sowie Bundes-, Bundesstaats- und Provinzregeln; Command Center mit Echtzeit-Finanzverwaltung und -Reporting in USD und CAD; und Collection für Forderungseinzug und Mahnungen. Wählen Sie ein Land für die Details.',
        'Toda la cuadrícula funciona en toda América del Norte — HR Suite con nómina configurable y normas federales, estatales y provinciales; Command Center con finanzas e informes en tiempo real en USD y CAD; y Collection para cobros y recordatorios. Elija un país para ver el detalle.',
        'Tutta la griglia funziona in tutto il Nord America — HR Suite con buste paga configurabili e norme federali, statali e provinciali; Command Center con finanza e reporting in tempo reale in USD e CAD; e Collection per il recupero crediti e i solleciti. Scegli un paese per il dettaglio.',
        'Het hele grid draait in heel Noord-Amerika — HR Suite met configureerbare loonadministratie en federale, staats- en provinciale regels; Command Center met realtime financiën en rapportage in USD en CAD; en Collection voor debiteuren en herinneringen. Kies een land voor de details.'),
    'Countries': _t('Pays', 'Länder', 'Países', 'Paesi', 'Landen'),
    'Countries in this region': _t('Pays de cette région', 'Länder in dieser Region',
        'Países de esta región', 'Paesi di questa regione', 'Landen in deze regio'),
    'Pick a country for its statutory payroll and compliance detail — and it runs across the wider region too.': _t(
        'Choisissez un pays pour le détail de sa paie légale et de sa conformité — et cela fonctionne aussi dans toute la région élargie.',
        'Wählen Sie ein Land für die Details zu gesetzlicher Gehaltsabrechnung und Compliance — und es funktioniert auch in der gesamten erweiterten Region.',
        'Elija un país para ver el detalle de su nómina legal y su cumplimiento — y también funciona en toda la región ampliada.',
        'Scegli un paese per il dettaglio della sua busta paga di legge e della conformità — e funziona anche in tutta la regione allargata.',
        'Kies een land voor de details van de wettelijke loonadministratie en compliance — en het werkt ook in de hele bredere regio.'),
    '<h4>United States</h4>': _t('<h4>États-Unis</h4>', '<h4>USA</h4>', '<h4>Estados Unidos</h4>',
        '<h4>Stati Uniti</h4>', '<h4>Verenigde Staten</h4>'),
    'Payroll · W-2 · ACH': _t('Paie · W-2 · ACH', 'Gehaltsabrechnung · W-2 · ACH',
        'Nómina · W-2 · ACH', 'Buste paga · W-2 · ACH', 'Loon · W-2 · ACH'),
    '<h4>Canada</h4>': _t('<h4>Canada</h4>', '<h4>Kanada</h4>', '<h4>Canadá</h4>',
        '<h4>Canada</h4>', '<h4>Canada</h4>'),
    'Leave · Payroll · CPP/EI': _t('Congés · Paie · CPP/EI', 'Urlaub · Gehaltsabrechnung · CPP/EI',
        'Permisos · Nómina · CPP/EI', 'Ferie · Buste paga · CPP/EI', 'Verlof · Loon · CPP/EI'),
    'Run your North American operation on one platform': _t(
        'Gérez votre activité nord-américaine sur une seule plateforme',
        'Führen Sie Ihren nordamerikanischen Betrieb auf einer Plattform',
        'Gestione su operación norteamericana en una sola plataforma',
        "Gestisci la tua attività nordamericana su un'unica piattaforma",
        'Run uw Noord-Amerikaanse activiteiten op één platform'),
}}


PAGE['/regions/usa/'] = {'src': 'regions/usa/index.html', 't': _hero({
    'HR Suite — HR &amp; payroll for United States | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour les États-Unis | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für die USA | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Estados Unidos | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per gli Stati Uniti | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor de Verenigde Staten | FulcrumGrid'),
    "HR Suite for the US — configurable payroll with federal/state income tax, Social Security and Medicare, W-2 year-end statements, ACH (NACHA) pay files, and full HR.": _t(
        "HR Suite pour les États-Unis — paie configurable avec impôt fédéral/des États sur le revenu, Social Security et Medicare, relevés de fin d'année W-2, fichiers de paie ACH (NACHA) et RH complètes.",
        'HR Suite für die USA — konfigurierbare Gehaltsabrechnung mit föderaler/einzelstaatlicher Einkommensteuer, Social Security und Medicare, W-2-Jahresendbescheinigungen, ACH-(NACHA-)Zahldateien und vollständigem HR.',
        'HR Suite para Estados Unidos — nómina configurable con impuesto sobre la renta federal/estatal, Social Security y Medicare, comprobantes de fin de año W-2, archivos de pago ACH (NACHA) y RR. HH. completos.',
        'HR Suite per gli Stati Uniti — buste paga configurabili con imposta sul reddito federale/statale, Social Security e Medicare, prospetti di fine anno W-2, file di pagamento ACH (NACHA) e HR completa.',
        'HR Suite voor de Verenigde Staten — configureerbare loonadministratie met federale/staatsinkomstenbelasting, Social Security en Medicare, W-2-jaaropgaven, ACH-(NACHA-)betaalbestanden en volledige HR.'),
    'United States · US': _t('États-Unis · US', 'USA · US', 'Estados Unidos · US',
        'Stati Uniti · US', 'Verenigde Staten · US'),
    'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">the US</em>': _t(
        'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">les États-Unis</em>',
        'HR &amp; Gehaltsabrechnung, gebaut für <em style="font-style:normal;color:var(--color-accent)">die USA</em>',
        'RR. HH. &amp; nómina, creado para <em style="font-style:normal;color:var(--color-accent)">Estados Unidos</em>',
        'HR &amp; buste paga, costruito per <em style="font-style:normal;color:var(--color-accent)">gli Stati Uniti</em>',
        'HR &amp; loonadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">de VS</em>'),
    'HR Suite runs your US workforce end to end — configurable payroll with federal and state income tax, Social Security and Medicare, W-2 year-end statements, ACH pay files, and full employee records.': _t(
        "HR Suite gère vos effectifs américains de bout en bout — paie configurable avec impôt fédéral et des États sur le revenu, Social Security et Medicare, relevés de fin d'année W-2, fichiers de paie ACH et dossiers complets des employés.",
        'HR Suite steuert Ihre US-Belegschaft durchgängig — konfigurierbare Gehaltsabrechnung mit föderaler und einzelstaatlicher Einkommensteuer, Social Security und Medicare, W-2-Jahresendbescheinigungen, ACH-Zahldateien und vollständigen Mitarbeiterakten.',
        'HR Suite gestiona su plantilla estadounidense de principio a fin — nómina configurable con impuesto sobre la renta federal y estatal, Social Security y Medicare, comprobantes de fin de año W-2, archivos de pago ACH y expedientes completos de empleados.',
        'HR Suite gestisce il tuo organico statunitense end-to-end — buste paga configurabili con imposta sul reddito federale e statale, Social Security e Medicare, prospetti di fine anno W-2, file di pagamento ACH e anagrafiche complete dei dipendenti.',
        'HR Suite runt uw Amerikaanse personeelsbestand end-to-end — configureerbare loonadministratie met federale en staatsinkomstenbelasting, Social Security en Medicare, W-2-jaaropgaven, ACH-betaalbestanden en volledige personeelsdossiers.'),
    'United States compliance, out of the box': _t(
        "Conformité États-Unis, prête à l'emploi", 'USA-Compliance, sofort einsatzbereit',
        'Cumplimiento en Estados Unidos, listo para usar', "Conformità Stati Uniti, pronta all'uso",
        'Verenigde Staten-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way United States does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme les États-Unis le font — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie die USA es tun — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hacen los Estados Unidos — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fanno gli Stati Uniti — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals de Verenigde Staten dat doen — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Payroll + tax categories': _t('Paie + catégories fiscales', 'Gehaltsabrechnung + Steuerkategorien',
        'Nómina + categorías fiscales', 'Buste paga + categorie fiscali',
        'Loonadministratie + belastingcategorieën'),
    'Configurable pay runs with deductions classified as federal income tax, state income tax, Social Security and Medicare, so every payslip and report lines up.': _t(
        "Cycles de paie configurables avec des retenues classées en impôt fédéral sur le revenu, impôt des États sur le revenu, Social Security et Medicare, pour que chaque bulletin de paie et chaque rapport concordent.",
        'Konfigurierbare Abrechnungsläufe mit Abzügen, klassifiziert als Bundeseinkommensteuer, einzelstaatliche Einkommensteuer, Social Security und Medicare, sodass jede Gehaltsabrechnung und jeder Bericht übereinstimmen.',
        'Ejecuciones de nómina configurables con deducciones clasificadas como impuesto federal sobre la renta, impuesto estatal sobre la renta, Social Security y Medicare, para que cada nómina y cada informe cuadren.',
        'Elaborazioni delle buste paga configurabili con trattenute classificate come imposta federale sul reddito, imposta statale sul reddito, Social Security e Medicare, così ogni cedolino e ogni report combaciano.',
        'Configureerbare loonruns met inhoudingen geclassificeerd als federale inkomstenbelasting, staatsinkomstenbelasting, Social Security en Medicare, zodat elke loonstrook en elk rapport kloppen.'),
    'W-2 year-end statements': _t("Relevés de fin d'année W-2", 'W-2-Jahresendbescheinigungen',
        'Comprobantes de fin de año W-2', 'Prospetti di fine anno W-2', 'W-2-jaaropgaven'),
    'Generate W-2 statements for employees from your finalized pay runs at year-end — statements from your own records, not an IRS EFW2 e-file.': _t(
        "Générez les relevés W-2 des employés à partir de vos cycles de paie finalisés en fin d'année — des relevés issus de vos propres données, et non une télédéclaration EFW2 auprès de l'IRS.",
        'Erstellen Sie W-2-Bescheinigungen für Mitarbeiter aus Ihren finalisierten Abrechnungsläufen zum Jahresende — Bescheinigungen aus Ihren eigenen Daten, keine elektronische EFW2-Einreichung beim IRS.',
        'Genere comprobantes W-2 para los empleados a partir de sus ejecuciones de nómina finalizadas a fin de año — comprobantes a partir de sus propios registros, no una presentación electrónica EFW2 ante el IRS.',
        "Genera i prospetti W-2 per i dipendenti dalle tue elaborazioni delle buste paga finalizzate a fine anno — prospetti dai tuoi stessi dati, non una trasmissione elettronica EFW2 all'IRS.",
        'Genereer W-2-opgaven voor werknemers uit uw afgeronde loonruns aan het einde van het jaar — opgaven uit uw eigen gegevens, geen elektronische EFW2-indiening bij de IRS.'),
    'ACH pay files': _t('Fichiers de paie ACH', 'ACH-Zahldateien', 'Archivos de pago ACH',
        'File di pagamento ACH', 'ACH-betaalbestanden'),
    'Export an ACH (NACHA) file from a finalized pay run for upload to your bank, with account details validated on entry.': _t(
        "Exportez un fichier ACH (NACHA) à partir d'un cycle de paie finalisé pour le téléverser à votre banque, avec validation des coordonnées bancaires à la saisie.",
        'Exportieren Sie eine ACH-(NACHA-)Datei aus einem finalisierten Abrechnungslauf zum Hochladen bei Ihrer Bank, wobei die Kontodaten bei der Eingabe validiert werden.',
        'Exporte un archivo ACH (NACHA) desde una ejecución de nómina finalizada para subirlo a su banco, con los datos de la cuenta validados al introducirlos.',
        "Esporta un file ACH (NACHA) da un'elaborazione delle buste paga finalizzata per caricarlo nella tua banca, con i dati del conto convalidati all'inserimento.",
        'Exporteer een ACH-(NACHA-)bestand uit een afgeronde loonrun om te uploaden naar uw bank, met bankgegevens die bij invoer worden gevalideerd.'),
    'Overtime — FLSA': _t('Heures supplémentaires — FLSA', 'Überstunden — FLSA', 'Horas extra — FLSA',
        'Straordinari — FLSA', 'Overuren — FLSA'),
    "Overtime to the Fair Labor Standards Act — 1.5× the regular rate for hours over 40 in a week — with state variants like California's daily 1.5× / 2× configurable.": _t(
        "Heures supplémentaires selon le Fair Labor Standards Act — 1,5× le taux normal pour les heures au-delà de 40 par semaine — avec des variantes d'État comme le 1,5× / 2× journalier de la Californie, configurables.",
        'Überstunden nach dem Fair Labor Standards Act — 1,5× des regulären Satzes für Stunden über 40 pro Woche — mit einzelstaatlichen Varianten wie Kaliforniens täglichem 1,5× / 2×, konfigurierbar.',
        'Horas extra según la Fair Labor Standards Act — 1,5× la tarifa normal para las horas por encima de 40 a la semana — con variantes estatales como el 1,5× / 2× diario de California, configurables.',
        "Straordinari secondo il Fair Labor Standards Act — 1,5× la tariffa normale per le ore oltre le 40 a settimana — con varianti statali come l'1,5× / 2× giornaliero della California, configurabili.",
        "Overuren volgens de Fair Labor Standards Act — 1,5× het normale tarief voor uren boven de 40 per week — met staatsvarianten zoals Californië's dagelijkse 1,5× / 2×, configureerbaar."),
    'Leave &amp; US holidays': _t('Congés &amp; jours fériés américains', 'Urlaub &amp; US-Feiertage',
        'Permisos &amp; festivos de EE. UU.', 'Ferie &amp; festività USA', 'Verlof &amp; Amerikaanse feestdagen'),
    'PTO and FMLA leave with the US federal holiday calendar — Juneteenth, Independence Day, Veterans Day and more — built in.': _t(
        "Congés PTO et FMLA avec le calendrier des jours fériés fédéraux américains — Juneteenth, jour de l'Indépendance, Veterans Day et plus — intégrés.",
        'PTO- und FMLA-Abwesenheiten mit dem US-Bundesfeiertagskalender — Juneteenth, Independence Day, Veterans Day und mehr — integriert.',
        'Permisos PTO y FMLA con el calendario de festivos federales de EE. UU. — Juneteenth, Día de la Independencia, Día de los Veteranos y más — integrados.',
        'Permessi PTO e FMLA con il calendario delle festività federali statunitensi — Juneteenth, Independence Day, Veterans Day e altro — integrati.',
        'PTO- en FMLA-verlof met de Amerikaanse federale feestdagenkalender — Juneteenth, Independence Day, Veterans Day en meer — ingebouwd.'),
    'Benefits &amp; deductions': _t('Avantages &amp; retenues', 'Leistungen &amp; Abzüge',
        'Beneficios &amp; deducciones', 'Benefit &amp; trattenute', 'Voordelen &amp; inhoudingen'),
    'Model 401(k), benefits and other pre- and post-tax deductions on the same engine, with employer contributions tracked as company cost.': _t(
        "Modélisez le 401(k), les avantages et d'autres retenues avant et après impôt sur le même moteur, avec les cotisations patronales suivies comme coût de l'entreprise.",
        'Modellieren Sie 401(k), Leistungen und weitere Abzüge vor und nach Steuern auf derselben Engine, wobei Arbeitgeberbeiträge als Unternehmenskosten erfasst werden.',
        'Modele el 401(k), los beneficios y otras deducciones antes y después de impuestos en el mismo motor, con las aportaciones del empleador registradas como coste de la empresa.',
        'Modella il 401(k), i benefit e altre trattenute al lordo e al netto delle imposte sullo stesso motore, con i contributi del datore di lavoro tracciati come costo aziendale.',
        'Modelleer 401(k), voordelen en andere inhoudingen vóór en na belasting op dezelfde engine, met werkgeversbijdragen bijgehouden als bedrijfskosten.'),
    'Core HR &amp; self-service': T_CORE_HR_TITLE,
    'Employee records, onboarding, time off, documents and employee self-service — the whole lifecycle on one platform.': _t(
        'Dossiers des employés, intégration, congés, documents et libre-service des employés — tout le cycle de vie sur une seule plateforme.',
        'Mitarbeiterakten, Onboarding, Abwesenheiten, Dokumente und Mitarbeiter-Self-Service — der gesamte Lebenszyklus auf einer Plattform.',
        'Expedientes de empleados, incorporación, ausencias, documentos y autoservicio del empleado — todo el ciclo de vida en una sola plataforma.',
        "Anagrafiche dei dipendenti, onboarding, ferie, documenti e self-service dei dipendenti — l'intero ciclo di vita su un'unica piattaforma.",
        'Personeelsdossiers, onboarding, verlof, documenten en selfservice voor medewerkers — de hele levenscyclus op één platform.'),
    PRICE_NOTE_EN: T_PRICE_NOTE,
    'Built in': T_BUILT_IN,
    'Run US HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie aux États-Unis comme il se doit',
        'HR &amp; Gehaltsabrechnung in den USA richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Estados Unidos como es debido',
        'Gestisci HR &amp; buste paga negli Stati Uniti nel modo giusto',
        'Regel HR &amp; loonadministratie in de VS zoals het hoort'),
    'See HR Suite handle US payroll, W-2, and ACH for your team.': _t(
        "Voyez HR Suite gérer la paie, les W-2 et l'ACH américains pour votre équipe.",
        'Sehen Sie, wie HR Suite US-Gehaltsabrechnung, W-2 und ACH für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona la nómina, los W-2 y el ACH de EE. UU. para su equipo.',
        'Guarda HR Suite gestire buste paga, W-2 e ACH statunitensi per il tuo team.',
        'Zie HR Suite de Amerikaanse loonadministratie, W-2 en ACH voor uw team afhandelen.'),
})}


PAGE['/regions/canada/'] = {'src': 'regions/canada/index.html', 't': _hero({
    'HR Suite — HR &amp; payroll for Canada | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour le Canada | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für Kanada | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Canadá | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per il Canada | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor Canada | FulcrumGrid'),
    'HR Suite for Canada — statutory leave and holidays, configurable payroll with federal/provincial tax, CPP and EI, and full HR in CAD.': _t(
        'HR Suite pour le Canada — congés et jours fériés légaux, paie configurable avec impôt fédéral/provincial, CPP et EI, et RH complètes en CAD.',
        'HR Suite für Kanada — gesetzlicher Urlaub und Feiertage, konfigurierbare Gehaltsabrechnung mit Bundes-/Provinzsteuer, CPP und EI, und vollständigem HR in CAD.',
        'HR Suite para Canadá — permisos y festivos legales, nómina configurable con impuesto federal/provincial, CPP y EI, y RR. HH. completos en CAD.',
        'HR Suite per il Canada — ferie e festività di legge, buste paga configurabili con imposta federale/provinciale, CPP ed EI, e HR completa in CAD.',
        'HR Suite voor Canada — wettelijk verlof en feestdagen, configureerbare loonadministratie met federale/provinciale belasting, CPP en EI, en volledige HR in CAD.'),
    'Canada · CA': _t('Canada · CA', 'Kanada · CA', 'Canadá · CA', 'Canada · CA', 'Canada · CA'),
    'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Canada</em>': _t(
        'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">le Canada</em>',
        'HR &amp; Gehaltsabrechnung, gebaut für <em style="font-style:normal;color:var(--color-accent)">Kanada</em>',
        'RR. HH. &amp; nómina, creado para <em style="font-style:normal;color:var(--color-accent)">Canadá</em>',
        'HR &amp; buste paga, costruito per <em style="font-style:normal;color:var(--color-accent)">il Canada</em>',
        'HR &amp; loonadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Canada</em>'),
    'HR Suite runs your Canada workforce — statutory leave and the local holiday calendar, configurable payroll with federal and provincial tax, CPP and EI, and full employee records in CAD.': _t(
        'HR Suite gère vos effectifs au Canada — congés légaux et calendrier des jours fériés locaux, paie configurable avec impôt fédéral et provincial, CPP et EI, et dossiers complets des employés en CAD.',
        'HR Suite steuert Ihre Belegschaft in Kanada — gesetzlicher Urlaub und der lokale Feiertagskalender, konfigurierbare Gehaltsabrechnung mit Bundes- und Provinzsteuer, CPP und EI, und vollständige Mitarbeiterakten in CAD.',
        'HR Suite gestiona su plantilla en Canadá — permisos legales y el calendario de festivos local, nómina configurable con impuesto federal y provincial, CPP y EI, y expedientes completos de empleados en CAD.',
        'HR Suite gestisce il tuo organico in Canada — ferie di legge e il calendario delle festività locali, buste paga configurabili con imposta federale e provinciale, CPP ed EI, e anagrafiche complete dei dipendenti in CAD.',
        'HR Suite runt uw personeelsbestand in Canada — wettelijk verlof en de lokale feestdagenkalender, configureerbare loonadministratie met federale en provinciale belasting, CPP en EI, en volledige personeelsdossiers in CAD.'),
    'Built in': T_BUILT_IN,
    'Canada compliance, out of the box': _t(
        "Conformité Canada, prête à l'emploi", 'Kanada-Compliance, sofort einsatzbereit',
        'Cumplimiento en Canadá, listo para usar', "Conformità Canada, pronta all'uso",
        'Canada-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Canada does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme le Canada le fait — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie Kanada es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Canadá — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fa il Canada — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals Canada dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Statutory leave &amp; holidays': _t('Congés légaux &amp; jours fériés',
        'Gesetzlicher Urlaub &amp; Feiertage', 'Permisos legales &amp; festivos',
        'Ferie legali &amp; festività', 'Wettelijk verlof &amp; feestdagen'),
    'Vacation, sick and parental leave with the Canadian statutory-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et parentaux avec le calendrier canadien des jours fériés légaux, intégrés.',
        'Jahres-, Kranken- und Elternzeit mit dem kanadischen Kalender der gesetzlichen Feiertage, integriert.',
        'Vacaciones, permiso por enfermedad y permiso parental con el calendario canadiense de festivos legales, integrados.',
        'Ferie, malattia e congedo parentale con il calendario canadese delle festività di legge, integrati.',
        'Vakantie-, ziekte- en ouderschapsverlof met de Canadese kalender van wettelijke feestdagen, ingebouwd.'),
    'Configurable payroll': _t('Paie configurable', 'Konfigurierbare Gehaltsabrechnung',
        'Nómina configurable', 'Buste paga configurabili', 'Configureerbare loonadministratie'),
    'Model federal and provincial income tax, CPP and EI as configurable, classified deductions, applied in every pay run.': _t(
        "Modélisez l'impôt sur le revenu fédéral et provincial, le CPP et l'EI sous forme de retenues configurables et classifiées, appliquées à chaque cycle de paie.",
        'Modellieren Sie die föderale und provinzielle Einkommensteuer, CPP und EI als konfigurierbare, klassifizierte Abzüge, die bei jedem Abrechnungslauf angewendet werden.',
        'Modele el impuesto sobre la renta federal y provincial, el CPP y el EI como deducciones configurables y clasificadas, aplicadas en cada ejecución de nómina.',
        "Modella l'imposta sul reddito federale e provinciale, il CPP e l'EI come trattenute configurabili e classificate, applicate a ogni elaborazione delle buste paga.",
        'Modelleer de federale en provinciale inkomstenbelasting, CPP en EI als configureerbare, geclassificeerde inhoudingen die bij elke loonrun worden toegepast.'),
    'Overtime — configurable': _t('Heures supplémentaires — configurable', 'Überstunden — konfigurierbar',
        'Horas extra — configurable', 'Straordinari — configurabile', 'Overuren — configureerbaar'),
    'Provincial overtime (commonly 1.5× over 44 hours a week) on the rule-based engine — configure the rule that applies to you.': _t(
        "Heures supplémentaires provinciales (généralement 1,5× au-delà de 44 heures par semaine) sur le moteur basé sur des règles — configurez la règle qui s'applique à vous.",
        'Provinzielle Überstunden (üblicherweise 1,5× über 44 Stunden pro Woche) auf der regelbasierten Engine — konfigurieren Sie die für Sie geltende Regel.',
        'Horas extra provinciales (habitualmente 1,5× por encima de 44 horas a la semana) en el motor basado en reglas — configure la regla que le corresponde.',
        'Straordinari provinciali (di norma 1,5× oltre le 44 ore a settimana) sul motore basato su regole — configura la regola che si applica a te.',
        'Provinciale overuren (doorgaans 1,5× boven de 44 uur per week) op de op regels gebaseerde engine — configureer de regel die op u van toepassing is.'),
    'Core HR &amp; self-service': T_CORE_HR_TITLE,
    'Pay in Canadian dollars, plus employee records, onboarding, time off and self-service.': _t(
        'Payez en dollars canadiens, plus dossiers des employés, intégration, congés et libre-service.',
        'Bezahlen Sie in kanadischen Dollar, plus Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service.',
        'Pague en dólares canadienses, además de expedientes de empleados, incorporación, ausencias y autoservicio.',
        'Paga in dollari canadesi, più anagrafiche dei dipendenti, onboarding, ferie e self-service.',
        'Betaal in Canadese dollars, plus personeelsdossiers, onboarding, verlof en selfservice.'),
    PRICE_NOTE_EN: T_PRICE_NOTE,
    'Run Canada HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie au Canada comme il se doit',
        'HR &amp; Gehaltsabrechnung in Kanada richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Canadá como es debido',
        'Gestisci HR &amp; buste paga in Canada nel modo giusto',
        'Regel HR &amp; loonadministratie in Canada zoals het hoort'),
    'See HR Suite handle Canadian leave, payroll and overtime for your team.': _t(
        'Voyez HR Suite gérer les congés, la paie et les heures supplémentaires canadiens pour votre équipe.',
        'Sehen Sie, wie HR Suite kanadischen Urlaub, Gehaltsabrechnung und Überstunden für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona los permisos, la nómina y las horas extra canadienses para su equipo.',
        'Guarda HR Suite gestire ferie, buste paga e straordinari canadesi per il tuo team.',
        'Zie HR Suite het Canadese verlof, de loonadministratie en overuren voor uw team afhandelen.'),
})}
