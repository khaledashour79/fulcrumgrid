# -*- coding: utf-8 -*-
"""Translations for the Middle East group of REGION pages.

Covers the regional hub (/regions/middle-east/) and its country landing pages
(Egypt, Jordan, Lebanon, Iraq, Palestine, Syria, Yemen). Structure, nav/footer
chrome and the shared tagline come from i18n.py + COMMON; this module carries
only each page's own visible copy.

Brand/product names (FulcrumGrid, HR Suite), technical acronyms and agency names
(WPS, GDPR, EOSB, SSC, NSSF, "Social Security Corporation", "National Social
Security Fund"), currency codes (EGP, JOD) and country codes stay as written.
Country/region names take their natural form per language. The "configurable /
rule-based / without a built-in preset" honesty hedges are preserved.
"""

def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# ---- Fragments shared across several pages ---------------------------------

T_HOME = _t('Accueil', 'Startseite', 'Inicio', 'Home', 'Home')
T_BUILT_IN = _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd')
T_EXPLORE = _t('Découvrir HR Suite', 'HR Suite entdecken', 'Explorar HR Suite',
               'Esplora HR Suite', 'Ontdek HR Suite')
T_SEE_PRICING = _t('Voir les tarifs HR Suite', 'HR Suite Preise ansehen',
                   'Ver los precios de HR Suite', 'Vedi i prezzi di HR Suite',
                   'Bekijk HR Suite-prijzen')

T_EOS_TITLE = _t('Fin de service, vos règles', 'Dienstende, Ihre Regeln',
                 'Fin de servicio, sus reglas', 'Fine servizio, le tue regole',
                 'Einde dienstverband, uw regels')
T_STAT_LEAVE_TITLE = _t('Congés légaux &amp; jours fériés',
                        'Gesetzlicher Urlaub &amp; Feiertage',
                        'Permisos legales &amp; festivos',
                        'Ferie legali &amp; festività',
                        'Wettelijk verlof &amp; feestdagen')
T_CONFIG_PAYROLL_TITLE = _t('Paie configurable', 'Konfigurierbare Gehaltsabrechnung',
                            'Nómina configurable', 'Buste paga configurabili',
                            'Configureerbare loonadministratie')
T_ARABIC_CORE_HR_TITLE = _t('Arabe en priorité &amp; RH essentielles',
                            'Arabisch zuerst &amp; Kern-HR',
                            'Árabe primero &amp; RR. HH. esenciales',
                            'Arabo prima di tutto &amp; HR di base',
                            'Arabisch eerst &amp; kern-HR')

# Feature body: core-HR line (Egypt / Jordan variant, no local-currency clause).
T_ARABIC_PLUS = _t(
    'Arabe, de droite à gauche partout, plus dossiers des employés, intégration, congés et libre-service.',
    'Arabisch, durchgehend von rechts nach links, plus Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service.',
    'Árabe, de derecha a izquierda en todo, además de expedientes de empleados, incorporación, ausencias y autoservicio.',
    'Arabo, da destra a sinistra ovunque, più anagrafiche dei dipendenti, onboarding, ferie e self-service.',
    'Arabisch, van rechts naar links overal, plus personeelsdossiers, onboarding, verlof en selfservice.')
# Feature body: core-HR line (Levant variant, with local-currency clause).
T_ARABIC_LOCALCUR = _t(
    'Arabe, de droite à gauche partout, paie en monnaie locale, plus dossiers des employés, intégration, congés et libre-service.',
    'Arabisch, durchgehend von rechts nach links, Bezahlung in lokaler Währung, plus Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service.',
    'Árabe, de derecha a izquierda en todo, pago en moneda local, además de expedientes de empleados, incorporación, ausencias y autoservicio.',
    'Arabo, da destra a sinistra ovunque, retribuzione in valuta locale, più anagrafiche dei dipendenti, onboarding, ferie e self-service.',
    'Arabisch, van rechts naar links overal, uitbetaling in lokale valuta, plus personeelsdossiers, onboarding, verlof en selfservice.')

# End-of-service body — "gratuity" variant (Egypt / Jordan).
T_EOS_GRATUITY = _t(
    "Configurez la fin de service sur le même moteur basé sur des règles — des jours de salaire par année — pour que la gratification locale s'ajuste sans préréglage codé en dur.",
    'Konfigurieren Sie das Dienstende auf derselben regelbasierten Engine — Lohntage pro Jahr — sodass die lokale Abfindung ohne fest codierte Voreinstellung passt.',
    'Configure el fin de servicio en el mismo motor basado en reglas — días de salario por año — para que la gratificación local encaje sin un preajuste codificado.',
    'Configura la fine servizio sullo stesso motore basato su regole — giorni di retribuzione per anno — così la gratifica locale si adatta senza un preset codificato.',
    'Configureer het einde dienstverband op dezelfde op regels gebaseerde engine — loondagen per jaar — zodat de lokale gratificatie past zonder hardgecodeerde voorinstelling.')
# End-of-service body — "entitlements" variant (Lebanon / Iraq / Palestine / Syria / Yemen).
T_EOS_ENTITLE = _t(
    "Configurez la fin de service sur le moteur basé sur des règles — des jours de salaire par année — pour que les droits locaux s'ajustent sans préréglage codé en dur.",
    'Konfigurieren Sie das Dienstende auf der regelbasierten Engine — Lohntage pro Jahr — sodass die lokalen Ansprüche ohne fest codierte Voreinstellung passen.',
    'Configure el fin de servicio en el motor basado en reglas — días de salario por año — para que los derechos locales encajen sin un preajuste codificado.',
    'Configura la fine servizio sul motore basato su regole — giorni di retribuzione per anno — così i diritti locali si adattano senza un preset codificato.',
    'Configureer het einde dienstverband op de op regels gebaseerde engine — loondagen per jaar — zodat de lokale aanspraken passen zonder hardgecodeerde voorinstelling.')

# Shared price note (identical on all eight pages).
T_PRICE_NOTE = _t(
    'Chaque module ici fait partie de HR Suite — paie avancée, clôture de fin d\'année et conformité sur le plan Enterprise, ou ajouté à n\'importe quel plan en complément par utilisateur. <a href="/pricing/hr-suite/">Voir les tarifs HR Suite →</a>',
    'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Add-on pro Platz zu jedem Plan hinzufügbar. <a href="/pricing/hr-suite/">HR Suite Preise ansehen →</a>',
    'Cada módulo aquí forma parte de HR Suite — nómina avanzada, cierre de fin de año y cumplimiento en el plan Enterprise, o añadido a cualquier plan como complemento por puesto. <a href="/pricing/hr-suite/">Ver los precios de HR Suite →</a>',
    'Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura di fine anno e conformità nel piano Enterprise, oppure aggiunto a qualsiasi piano come add-on per postazione. <a href="/pricing/hr-suite/">Vedi i prezzi di HR Suite →</a>',
    'Elke module hier maakt deel uit van HR Suite — geavanceerde loonadministratie, jaarafsluiting en compliance in het Enterprise-plan, of toegevoegd aan elk plan als add-on per gebruiker. <a href="/pricing/hr-suite/">Bekijk HR Suite-prijzen →</a>')

PRICE_NOTE_EN = ('Every module here is part of HR Suite — advanced payroll, year-end and '
                 'compliance on the Enterprise plan, or added to any plan as a per-seat '
                 'add-on. <a href="/pricing/hr-suite/">See HR Suite pricing →</a>')


def _common(t):
    """Segments that appear (identically) on every page in the group."""
    t['<a href="/">Home</a>'] = {k: '<a href="/">%s</a>' % v for k, v in T_HOME.items()}
    t['Built in'] = T_BUILT_IN
    t['Explore HR Suite'] = T_EXPLORE
    t['See HR Suite pricing'] = T_SEE_PRICING
    t[PRICE_NOTE_EN] = T_PRICE_NOTE
    return t


PAGE = {}


PAGE['/regions/egypt/'] = {'src': 'regions/egypt/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Egypt | FulcrumGrid': _t(
        "HR Suite — RH &amp; paie pour l'Égypte | FulcrumGrid",
        'HR Suite — HR &amp; Gehaltsabrechnung für Ägypten | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Egipto | FulcrumGrid',
        "HR Suite — HR &amp; buste paga per l'Egitto | FulcrumGrid",
        'HR Suite — HR &amp; loonadministratie voor Egypte | FulcrumGrid'),
    'HR Suite for Egypt — configurable payroll with local income tax and social insurance, rule-based end-of-service, EGP pay, and Arabic-first HR.': _t(
        "HR Suite pour l'Égypte — paie configurable avec impôt sur le revenu local et assurance sociale, fin de service basée sur des règles, paie en EGP et RH en arabe d'abord.",
        'HR Suite für Ägypten — konfigurierbare Gehaltsabrechnung mit lokaler Einkommensteuer und Sozialversicherung, regelbasiertes Dienstende, Bezahlung in EGP und Arabisch-zuerst-HR.',
        'HR Suite para Egipto — nómina configurable con impuesto sobre la renta local y seguridad social, fin de servicio basado en reglas, pago en EGP y RR. HH. en árabe primero.',
        "HR Suite per l'Egitto — buste paga configurabili con imposta sul reddito locale e assicurazione sociale, fine servizio basata su regole, retribuzione in EGP e HR in arabo prima di tutto.",
        'HR Suite voor Egypte — configureerbare loonadministratie met lokale inkomstenbelasting en sociale verzekering, op regels gebaseerd einde dienstverband, uitbetaling in EGP en Arabisch-eerst-HR.'),
    'Egypt · EG': _t('Égypte · EG', 'Ägypten · EG', 'Egipto · EG', 'Egitto · EG', 'Egypte · EG'),
    '<span class="current">Egypt</span>': _t(
        '<span class="current">Égypte</span>', '<span class="current">Ägypten</span>',
        '<span class="current">Egipto</span>', '<span class="current">Egitto</span>',
        '<span class="current">Egypte</span>'),
    'HR &amp; payroll, built for <span class="p-grad">Egypt</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">l\'Égypte</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">Ägypten</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">Egipto</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">l\'Egitto</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">Egypte</span>'),
    'HR Suite runs your Egypt workforce — configurable payroll with local income tax and social-insurance deductions, end-of-service on a rule-based engine, EGP pay, Arabic throughout, and full employee records.': _t(
        "HR Suite gère vos effectifs en Égypte — paie configurable avec impôt sur le revenu local et retenues d'assurance sociale, fin de service sur un moteur basé sur des règles, paie en EGP, arabe partout et dossiers complets des employés.",
        'HR Suite steuert Ihre Belegschaft in Ägypten — konfigurierbare Gehaltsabrechnung mit lokaler Einkommensteuer und Sozialversicherungsabzügen, Dienstende auf einer regelbasierten Engine, Bezahlung in EGP, durchgehend Arabisch und vollständige Mitarbeiterakten.',
        'HR Suite gestiona su plantilla en Egipto — nómina configurable con impuesto sobre la renta local y deducciones de seguridad social, fin de servicio en un motor basado en reglas, pago en EGP, árabe en todo y expedientes completos de empleados.',
        "HR Suite gestisce il tuo organico in Egitto — buste paga configurabili con imposta sul reddito locale e trattenute per l'assicurazione sociale, fine servizio su un motore basato su regole, retribuzione in EGP, arabo ovunque e anagrafiche complete dei dipendenti.",
        'HR Suite runt uw personeelsbestand in Egypte — configureerbare loonadministratie met lokale inkomstenbelasting en inhoudingen voor sociale verzekering, einde dienstverband op een op regels gebaseerde engine, uitbetaling in EGP, overal Arabisch en volledige personeelsdossiers.'),
    'Egypt compliance, out of the box': _t(
        "Conformité Égypte, prête à l'emploi", 'Ägypten-Compliance, sofort einsatzbereit',
        'Cumplimiento en Egipto, listo para usar', "Conformità Egitto, pronta all'uso",
        'Egypte-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Egypt does — each part of the same platform, no separate tools.': _t(
        "Les modules qui font fonctionner HR Suite comme l'Égypte le fait — chacun faisant partie de la même plateforme, sans outils séparés.",
        'Die Module, die HR Suite so arbeiten lassen, wie Ägypten es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Egipto — cada uno parte de la misma plataforma, sin herramientas separadas.',
        "I moduli che fanno funzionare HR Suite come fa l'Egitto — ciascuno parte della stessa piattaforma, senza strumenti separati.",
        'De modules die HR Suite laten werken zoals Egypte dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Configurable payroll': T_CONFIG_PAYROLL_TITLE,
    'Model Egyptian income tax and social-insurance contributions as configurable, classified deduction types, applied in every pay run.': _t(
        "Modélisez l'impôt sur le revenu égyptien et les cotisations d'assurance sociale sous forme de types de retenues configurables et classifiés, appliqués à chaque cycle de paie.",
        'Modellieren Sie die ägyptische Einkommensteuer und Sozialversicherungsbeiträge als konfigurierbare, klassifizierte Abzugsarten, die bei jedem Abrechnungslauf angewendet werden.',
        'Modele el impuesto sobre la renta egipcio y las cotizaciones a la seguridad social como tipos de deducción configurables y clasificados, aplicados en cada ejecución de nómina.',
        "Modella l'imposta sul reddito egiziana e i contributi per l'assicurazione sociale come tipi di trattenuta configurabili e classificati, applicati a ogni elaborazione delle buste paga.",
        'Modelleer de Egyptische inkomstenbelasting en socialeverzekeringsbijdragen als configureerbare, geclassificeerde inhoudingstypen die bij elke loonrun worden toegepast.'),
    'Statutory leave &amp; holidays': T_STAT_LEAVE_TITLE,
    'Statutory annual, sick and maternity leave and the Egyptian public-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et de maternité légaux et le calendrier des jours fériés égyptiens, intégrés.',
        'Gesetzlicher Jahres-, Kranken- und Mutterschaftsurlaub sowie der ägyptische Feiertagskalender, integriert.',
        'Permisos legales anual, por enfermedad y por maternidad y el calendario de festivos egipcio, integrados.',
        'Ferie annuali, per malattia e per maternità di legge e il calendario delle festività egiziane, integrati.',
        'Wettelijk jaarlijks, ziekte- en zwangerschapsverlof en de Egyptische feestdagenkalender, ingebouwd.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'Configure end-of-service on the same rule-based engine — days of wage per year — so local gratuity fits without a hard-coded preset.': T_EOS_GRATUITY,
    'EGP pay &amp; documents': _t('Paie en EGP &amp; documents', 'EGP-Bezahlung &amp; Dokumente',
        'Pago en EGP &amp; documentos', 'Retribuzione in EGP &amp; documenti', 'EGP-uitbetaling &amp; documenten'),
    'Pay in Egyptian pounds, with bilingual contracts and letters and document-expiry tracking.': _t(
        "Payez en livres égyptiennes, avec contrats et lettres bilingues et suivi de l'expiration des documents.",
        'Bezahlen Sie in ägyptischen Pfund, mit zweisprachigen Verträgen und Schreiben sowie Nachverfolgung des Dokumentenablaufs.',
        'Pague en libras egipcias, con contratos y cartas bilingües y seguimiento de la caducidad de documentos.',
        'Paga in sterline egiziane, con contratti e lettere bilingui e tracciamento della scadenza dei documenti.',
        'Betaal in Egyptische pond, met tweetalige contracten en brieven en het bijhouden van documentvervaldata.'),
    'Arabic-first &amp; core HR': T_ARABIC_CORE_HR_TITLE,
    'Arabic, right-to-left throughout, plus employee records, onboarding, time off and self-service.': T_ARABIC_PLUS,
    'Run Egypt HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie en Égypte comme il se doit',
        'HR &amp; Gehaltsabrechnung in Ägypten richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Egipto como es debido',
        'Gestisci HR &amp; buste paga in Egitto nel modo giusto',
        'Regel HR &amp; loonadministratie in Egypte zoals het hoort'),
    'See HR Suite handle Egypt payroll and end-of-service for your team.': _t(
        'Voyez HR Suite gérer la paie et la fin de service en Égypte pour votre équipe.',
        'Sehen Sie, wie HR Suite Gehaltsabrechnung und Dienstende in Ägypten für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona la nómina y el fin de servicio en Egipto para su equipo.',
        'Guarda HR Suite gestire buste paga e fine servizio in Egitto per il tuo team.',
        'Zie HR Suite de loonadministratie en het einde dienstverband in Egypte voor uw team afhandelen.'),
})}


PAGE['/regions/jordan/'] = {'src': 'regions/jordan/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Jordan | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour la Jordanie | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für Jordanien | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Jordania | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per la Giordania | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor Jordanië | FulcrumGrid'),
    'HR Suite for Jordan — configurable payroll with local income tax and Social Security Corporation (SSC), rule-based end-of-service, JOD pay, and Arabic-first HR.': _t(
        "HR Suite pour la Jordanie — paie configurable avec impôt sur le revenu local et Social Security Corporation (SSC), fin de service basée sur des règles, paie en JOD et RH en arabe d'abord.",
        'HR Suite für Jordanien — konfigurierbare Gehaltsabrechnung mit lokaler Einkommensteuer und Social Security Corporation (SSC), regelbasiertes Dienstende, Bezahlung in JOD und Arabisch-zuerst-HR.',
        'HR Suite para Jordania — nómina configurable con impuesto sobre la renta local y Social Security Corporation (SSC), fin de servicio basado en reglas, pago en JOD y RR. HH. en árabe primero.',
        'HR Suite per la Giordania — buste paga configurabili con imposta sul reddito locale e Social Security Corporation (SSC), fine servizio basata su regole, retribuzione in JOD e HR in arabo prima di tutto.',
        'HR Suite voor Jordanië — configureerbare loonadministratie met lokale inkomstenbelasting en Social Security Corporation (SSC), op regels gebaseerd einde dienstverband, uitbetaling in JOD en Arabisch-eerst-HR.'),
    'Jordan · JO': _t('Jordanie · JO', 'Jordanien · JO', 'Jordania · JO', 'Giordania · JO', 'Jordanië · JO'),
    '<span class="current">Jordan</span>': _t(
        '<span class="current">Jordanie</span>', '<span class="current">Jordanien</span>',
        '<span class="current">Jordania</span>', '<span class="current">Giordania</span>',
        '<span class="current">Jordanië</span>'),
    'HR &amp; payroll, built for <span class="p-grad">Jordan</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">la Jordanie</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">Jordanien</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">Jordania</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">la Giordania</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">Jordanië</span>'),
    'HR Suite runs your Jordan workforce — configurable payroll with local income tax and Social Security Corporation deductions, end-of-service on a rule-based engine, JOD pay, Arabic throughout, and full employee records.': _t(
        'HR Suite gère vos effectifs en Jordanie — paie configurable avec impôt sur le revenu local et retenues de la Social Security Corporation, fin de service sur un moteur basé sur des règles, paie en JOD, arabe partout et dossiers complets des employés.',
        'HR Suite steuert Ihre Belegschaft in Jordanien — konfigurierbare Gehaltsabrechnung mit lokaler Einkommensteuer und Abzügen der Social Security Corporation, Dienstende auf einer regelbasierten Engine, Bezahlung in JOD, durchgehend Arabisch und vollständige Mitarbeiterakten.',
        'HR Suite gestiona su plantilla en Jordania — nómina configurable con impuesto sobre la renta local y deducciones de la Social Security Corporation, fin de servicio en un motor basado en reglas, pago en JOD, árabe en todo y expedientes completos de empleados.',
        'HR Suite gestisce il tuo organico in Giordania — buste paga configurabili con imposta sul reddito locale e trattenute della Social Security Corporation, fine servizio su un motore basato su regole, retribuzione in JOD, arabo ovunque e anagrafiche complete dei dipendenti.',
        'HR Suite runt uw personeelsbestand in Jordanië — configureerbare loonadministratie met lokale inkomstenbelasting en inhoudingen van de Social Security Corporation, einde dienstverband op een op regels gebaseerde engine, uitbetaling in JOD, overal Arabisch en volledige personeelsdossiers.'),
    'Jordan compliance, out of the box': _t(
        "Conformité Jordanie, prête à l'emploi", 'Jordanien-Compliance, sofort einsatzbereit',
        'Cumplimiento en Jordania, listo para usar', "Conformità Giordania, pronta all'uso",
        'Jordanië-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Jordan does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme la Jordanie le fait — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie Jordanien es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Jordania — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fa la Giordania — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals Jordanië dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Configurable payroll': T_CONFIG_PAYROLL_TITLE,
    'Model Jordanian income tax and Social Security Corporation (SSC) contributions as configurable, classified deduction types, applied in every pay run.': _t(
        "Modélisez l'impôt sur le revenu jordanien et les cotisations à la Social Security Corporation (SSC) sous forme de types de retenues configurables et classifiés, appliqués à chaque cycle de paie.",
        'Modellieren Sie die jordanische Einkommensteuer und Beiträge zur Social Security Corporation (SSC) als konfigurierbare, klassifizierte Abzugsarten, die bei jedem Abrechnungslauf angewendet werden.',
        'Modele el impuesto sobre la renta jordano y las cotizaciones a la Social Security Corporation (SSC) como tipos de deducción configurables y clasificados, aplicados en cada ejecución de nómina.',
        "Modella l'imposta sul reddito giordana e i contributi alla Social Security Corporation (SSC) come tipi di trattenuta configurabili e classificati, applicati a ogni elaborazione delle buste paga.",
        'Modelleer de Jordaanse inkomstenbelasting en bijdragen aan de Social Security Corporation (SSC) als configureerbare, geclassificeerde inhoudingstypen die bij elke loonrun worden toegepast.'),
    'Statutory leave &amp; holidays': T_STAT_LEAVE_TITLE,
    'Statutory annual, sick and maternity leave and the Jordanian public-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et de maternité légaux et le calendrier des jours fériés jordaniens, intégrés.',
        'Gesetzlicher Jahres-, Kranken- und Mutterschaftsurlaub sowie der jordanische Feiertagskalender, integriert.',
        'Permisos legales anual, por enfermedad y por maternidad y el calendario de festivos jordano, integrados.',
        'Ferie annuali, per malattia e per maternità di legge e il calendario delle festività giordane, integrati.',
        'Wettelijk jaarlijks, ziekte- en zwangerschapsverlof en de Jordaanse feestdagenkalender, ingebouwd.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'Configure end-of-service on the same rule-based engine — days of wage per year — so local gratuity fits without a hard-coded preset.': T_EOS_GRATUITY,
    'JOD pay &amp; documents': _t('Paie en JOD &amp; documents', 'JOD-Bezahlung &amp; Dokumente',
        'Pago en JOD &amp; documentos', 'Retribuzione in JOD &amp; documenti', 'JOD-uitbetaling &amp; documenten'),
    'Pay in Jordanian dinars, with bilingual contracts and letters and document-expiry tracking.': _t(
        "Payez en dinars jordaniens, avec contrats et lettres bilingues et suivi de l'expiration des documents.",
        'Bezahlen Sie in jordanischen Dinar, mit zweisprachigen Verträgen und Schreiben sowie Nachverfolgung des Dokumentenablaufs.',
        'Pague en dinares jordanos, con contratos y cartas bilingües y seguimiento de la caducidad de documentos.',
        'Paga in dinari giordani, con contratti e lettere bilingui e tracciamento della scadenza dei documenti.',
        'Betaal in Jordaanse dinar, met tweetalige contracten en brieven en het bijhouden van documentvervaldata.'),
    'Arabic-first &amp; core HR': T_ARABIC_CORE_HR_TITLE,
    'Arabic, right-to-left throughout, plus employee records, onboarding, time off and self-service.': T_ARABIC_PLUS,
    'Run Jordan HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie en Jordanie comme il se doit',
        'HR &amp; Gehaltsabrechnung in Jordanien richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Jordania como es debido',
        'Gestisci HR &amp; buste paga in Giordania nel modo giusto',
        'Regel HR &amp; loonadministratie in Jordanië zoals het hoort'),
    'See HR Suite handle Jordan payroll and end-of-service for your team.': _t(
        'Voyez HR Suite gérer la paie et la fin de service en Jordanie pour votre équipe.',
        'Sehen Sie, wie HR Suite Gehaltsabrechnung und Dienstende in Jordanien für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona la nómina y el fin de servicio en Jordania para su equipo.',
        'Guarda HR Suite gestire buste paga e fine servizio in Giordania per il tuo team.',
        'Zie HR Suite de loonadministratie en het einde dienstverband in Jordanië voor uw team afhandelen.'),
})}


PAGE['/regions/lebanon/'] = {'src': 'regions/lebanon/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Lebanon | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour le Liban | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für den Libanon | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para el Líbano | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per il Libano | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor Libanon | FulcrumGrid'),
    'HR Suite for Lebanon — statutory leave and holidays, configurable payroll with income tax and NSSF, rule-based end-of-service, and Arabic-first HR.': _t(
        "HR Suite pour le Liban — congés et jours fériés légaux, paie configurable avec impôt sur le revenu et NSSF, fin de service basée sur des règles, et RH en arabe d'abord.",
        'HR Suite für den Libanon — gesetzlicher Urlaub und Feiertage, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und NSSF, regelbasiertes Dienstende und Arabisch-zuerst-HR.',
        'HR Suite para el Líbano — permisos y festivos legales, nómina configurable con impuesto sobre la renta y NSSF, fin de servicio basado en reglas, y RR. HH. en árabe primero.',
        'HR Suite per il Libano — ferie e festività di legge, buste paga configurabili con imposta sul reddito e NSSF, fine servizio basata su regole, e HR in arabo prima di tutto.',
        'HR Suite voor Libanon — wettelijk verlof en feestdagen, configureerbare loonadministratie met inkomstenbelasting en NSSF, op regels gebaseerd einde dienstverband, en Arabisch-eerst-HR.'),
    'Lebanon · LB': _t('Liban · LB', 'Libanon · LB', 'Líbano · LB', 'Libano · LB', 'Libanon · LB'),
    '<span class="current">Lebanon</span>': _t(
        '<span class="current">Liban</span>', '<span class="current">Libanon</span>',
        '<span class="current">Líbano</span>', '<span class="current">Libano</span>',
        '<span class="current">Libanon</span>'),
    'HR &amp; payroll, built for <span class="p-grad">Lebanon</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">le Liban</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">den Libanon</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">el Líbano</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">il Libano</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">Libanon</span>'),
    'HR Suite runs your Lebanon workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and NSSF, rule-based end-of-service, Arabic throughout, and full employee records.': _t(
        'HR Suite gère vos effectifs au Liban — congés légaux et le calendrier des jours fériés locaux, paie configurable avec impôt sur le revenu et NSSF, fin de service basée sur des règles, arabe partout et dossiers complets des employés.',
        'HR Suite steuert Ihre Belegschaft im Libanon — gesetzlicher Urlaub und der lokale Feiertagskalender, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und NSSF, regelbasiertes Dienstende, durchgehend Arabisch und vollständige Mitarbeiterakten.',
        'HR Suite gestiona su plantilla en el Líbano — permisos legales y el calendario de festivos local, nómina configurable con impuesto sobre la renta y NSSF, fin de servicio basado en reglas, árabe en todo y expedientes completos de empleados.',
        'HR Suite gestisce il tuo organico in Libano — ferie di legge e il calendario delle festività locali, buste paga configurabili con imposta sul reddito e NSSF, fine servizio basata su regole, arabo ovunque e anagrafiche complete dei dipendenti.',
        'HR Suite runt uw personeelsbestand in Libanon — wettelijk verlof en de lokale feestdagenkalender, configureerbare loonadministratie met inkomstenbelasting en NSSF, op regels gebaseerd einde dienstverband, overal Arabisch en volledige personeelsdossiers.'),
    'Lebanon compliance, out of the box': _t(
        "Conformité Liban, prête à l'emploi", 'Libanon-Compliance, sofort einsatzbereit',
        'Cumplimiento en el Líbano, listo para usar', "Conformità Libano, pronta all'uso",
        'Libanon-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Lebanon does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme le Liban le fait — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie der Libanon es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace el Líbano — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fa il Libano — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals Libanon dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Statutory leave &amp; holidays': T_STAT_LEAVE_TITLE,
    'Statutory annual, sick and maternity leave and the Lebanese public-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et de maternité légaux et le calendrier des jours fériés libanais, intégrés.',
        'Gesetzlicher Jahres-, Kranken- und Mutterschaftsurlaub sowie der libanesische Feiertagskalender, integriert.',
        'Permisos legales anual, por enfermedad y por maternidad y el calendario de festivos libanés, integrados.',
        'Ferie annuali, per malattia e per maternità di legge e il calendario delle festività libanesi, integrati.',
        'Wettelijk jaarlijks, ziekte- en zwangerschapsverlof en de Libanese feestdagenkalender, ingebouwd.'),
    'Configurable payroll': T_CONFIG_PAYROLL_TITLE,
    'Model Lebanese income tax and National Social Security Fund (NSSF) contributions as configurable, classified deductions.': _t(
        "Modélisez l'impôt sur le revenu libanais et les cotisations au National Social Security Fund (NSSF) sous forme de retenues configurables et classifiées.",
        'Modellieren Sie die libanesische Einkommensteuer und Beiträge zum National Social Security Fund (NSSF) als konfigurierbare, klassifizierte Abzüge.',
        'Modele el impuesto sobre la renta libanés y las cotizaciones al National Social Security Fund (NSSF) como deducciones configurables y clasificadas.',
        "Modella l'imposta sul reddito libanese e i contributi al National Social Security Fund (NSSF) come trattenute configurabili e classificate.",
        'Modelleer de Libanese inkomstenbelasting en bijdragen aan het National Social Security Fund (NSSF) als configureerbare, geclassificeerde inhoudingen.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.': T_EOS_ENTITLE,
    'Arabic-first &amp; core HR': T_ARABIC_CORE_HR_TITLE,
    'Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.': T_ARABIC_LOCALCUR,
    'Run Lebanon HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie au Liban comme il se doit',
        'HR &amp; Gehaltsabrechnung im Libanon richtig machen',
        'Gestione las RR. HH. &amp; la nómina en el Líbano como es debido',
        'Gestisci HR &amp; buste paga in Libano nel modo giusto',
        'Regel HR &amp; loonadministratie in Libanon zoals het hoort'),
    'See HR Suite handle Lebanon leave, payroll and end-of-service for your team.': _t(
        'Voyez HR Suite gérer les congés, la paie et la fin de service au Liban pour votre équipe.',
        'Sehen Sie, wie HR Suite Urlaub, Gehaltsabrechnung und Dienstende im Libanon für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona los permisos, la nómina y el fin de servicio en el Líbano para su equipo.',
        'Guarda HR Suite gestire ferie, buste paga e fine servizio in Libano per il tuo team.',
        'Zie HR Suite verlof, loonadministratie en einde dienstverband in Libanon voor uw team afhandelen.'),
})}


PAGE['/regions/iraq/'] = {'src': 'regions/iraq/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Iraq | FulcrumGrid': _t(
        "HR Suite — RH &amp; paie pour l'Irak | FulcrumGrid",
        'HR Suite — HR &amp; Gehaltsabrechnung für den Irak | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Irak | FulcrumGrid',
        "HR Suite — HR &amp; buste paga per l'Iraq | FulcrumGrid",
        'HR Suite — HR &amp; loonadministratie voor Irak | FulcrumGrid'),
    'HR Suite for Iraq — statutory leave and holidays, configurable payroll with income tax and social security, rule-based end-of-service, and Arabic-first HR.': _t(
        "HR Suite pour l'Irak — congés et jours fériés légaux, paie configurable avec impôt sur le revenu et sécurité sociale, fin de service basée sur des règles, et RH en arabe d'abord.",
        'HR Suite für den Irak — gesetzlicher Urlaub und Feiertage, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialversicherung, regelbasiertes Dienstende und Arabisch-zuerst-HR.',
        'HR Suite para Irak — permisos y festivos legales, nómina configurable con impuesto sobre la renta y seguridad social, fin de servicio basado en reglas, y RR. HH. en árabe primero.',
        'HR Suite per l\'Iraq — ferie e festività di legge, buste paga configurabili con imposta sul reddito e previdenza sociale, fine servizio basata su regole, e HR in arabo prima di tutto.',
        'HR Suite voor Irak — wettelijk verlof en feestdagen, configureerbare loonadministratie met inkomstenbelasting en sociale zekerheid, op regels gebaseerd einde dienstverband, en Arabisch-eerst-HR.'),
    'Iraq · IQ': _t('Irak · IQ', 'Irak · IQ', 'Irak · IQ', 'Iraq · IQ', 'Irak · IQ'),
    '<span class="current">Iraq</span>': _t(
        '<span class="current">Irak</span>', '<span class="current">Irak</span>',
        '<span class="current">Irak</span>', '<span class="current">Iraq</span>',
        '<span class="current">Irak</span>'),
    'HR &amp; payroll, built for <span class="p-grad">Iraq</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">l\'Irak</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">den Irak</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">Irak</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">l\'Iraq</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">Irak</span>'),
    'HR Suite runs your Iraq workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social security, rule-based end-of-service, Arabic throughout, and full employee records.': _t(
        "HR Suite gère vos effectifs en Irak — congés légaux et le calendrier des jours fériés locaux, paie configurable avec impôt sur le revenu et sécurité sociale, fin de service basée sur des règles, arabe partout et dossiers complets des employés.",
        'HR Suite steuert Ihre Belegschaft im Irak — gesetzlicher Urlaub und der lokale Feiertagskalender, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialversicherung, regelbasiertes Dienstende, durchgehend Arabisch und vollständige Mitarbeiterakten.',
        'HR Suite gestiona su plantilla en Irak — permisos legales y el calendario de festivos local, nómina configurable con impuesto sobre la renta y seguridad social, fin de servicio basado en reglas, árabe en todo y expedientes completos de empleados.',
        "HR Suite gestisce il tuo organico in Iraq — ferie di legge e il calendario delle festività locali, buste paga configurabili con imposta sul reddito e previdenza sociale, fine servizio basata su regole, arabo ovunque e anagrafiche complete dei dipendenti.",
        'HR Suite runt uw personeelsbestand in Irak — wettelijk verlof en de lokale feestdagenkalender, configureerbare loonadministratie met inkomstenbelasting en sociale zekerheid, op regels gebaseerd einde dienstverband, overal Arabisch en volledige personeelsdossiers.'),
    'Iraq compliance, out of the box': _t(
        "Conformité Irak, prête à l'emploi", 'Irak-Compliance, sofort einsatzbereit',
        'Cumplimiento en Irak, listo para usar', "Conformità Iraq, pronta all'uso",
        'Irak-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Iraq does — each part of the same platform, no separate tools.': _t(
        "Les modules qui font fonctionner HR Suite comme l'Irak le fait — chacun faisant partie de la même plateforme, sans outils séparés.",
        'Die Module, die HR Suite so arbeiten lassen, wie der Irak es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Irak — cada uno parte de la misma plataforma, sin herramientas separadas.',
        "I moduli che fanno funzionare HR Suite come fa l'Iraq — ciascuno parte della stessa piattaforma, senza strumenti separati.",
        'De modules die HR Suite laten werken zoals Irak dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Statutory leave &amp; holidays': T_STAT_LEAVE_TITLE,
    'Statutory annual, sick and maternity leave and the Iraqi public-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et de maternité légaux et le calendrier des jours fériés irakiens, intégrés.',
        'Gesetzlicher Jahres-, Kranken- und Mutterschaftsurlaub sowie der irakische Feiertagskalender, integriert.',
        'Permisos legales anual, por enfermedad y por maternidad y el calendario de festivos iraquí, integrados.',
        'Ferie annuali, per malattia e per maternità di legge e il calendario delle festività irachene, integrati.',
        'Wettelijk jaarlijks, ziekte- en zwangerschapsverlof en de Iraakse feestdagenkalender, ingebouwd.'),
    'Configurable payroll': T_CONFIG_PAYROLL_TITLE,
    'Model Iraqi income tax and social-security contributions as configurable, classified deductions, applied in every pay run.': _t(
        "Modélisez l'impôt sur le revenu irakien et les cotisations de sécurité sociale sous forme de retenues configurables et classifiées, appliquées à chaque cycle de paie.",
        'Modellieren Sie die irakische Einkommensteuer und Sozialversicherungsbeiträge als konfigurierbare, klassifizierte Abzüge, die bei jedem Abrechnungslauf angewendet werden.',
        'Modele el impuesto sobre la renta iraquí y las cotizaciones a la seguridad social como deducciones configurables y clasificadas, aplicadas en cada ejecución de nómina.',
        "Modella l'imposta sul reddito irachena e i contributi previdenziali come trattenute configurabili e classificate, applicate a ogni elaborazione delle buste paga.",
        'Modelleer de Iraakse inkomstenbelasting en socialezekerheidsbijdragen als configureerbare, geclassificeerde inhoudingen die bij elke loonrun worden toegepast.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.': T_EOS_ENTITLE,
    'Arabic-first &amp; core HR': T_ARABIC_CORE_HR_TITLE,
    'Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.': T_ARABIC_LOCALCUR,
    'Run Iraq HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie en Irak comme il se doit',
        'HR &amp; Gehaltsabrechnung im Irak richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Irak como es debido',
        'Gestisci HR &amp; buste paga in Iraq nel modo giusto',
        'Regel HR &amp; loonadministratie in Irak zoals het hoort'),
    'See HR Suite handle Iraq leave, payroll and end-of-service for your team.': _t(
        'Voyez HR Suite gérer les congés, la paie et la fin de service en Irak pour votre équipe.',
        'Sehen Sie, wie HR Suite Urlaub, Gehaltsabrechnung und Dienstende im Irak für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona los permisos, la nómina y el fin de servicio en Irak para su equipo.',
        'Guarda HR Suite gestire ferie, buste paga e fine servizio in Iraq per il tuo team.',
        'Zie HR Suite verlof, loonadministratie en einde dienstverband in Irak voor uw team afhandelen.'),
})}


PAGE['/regions/palestine/'] = {'src': 'regions/palestine/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Palestine | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour la Palestine | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für Palästina | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Palestina | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per la Palestina | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor Palestina | FulcrumGrid'),
    'HR Suite for Palestine — statutory leave and holidays, configurable payroll with income tax and social contributions, rule-based end-of-service, and Arabic-first HR.': _t(
        "HR Suite pour la Palestine — congés et jours fériés légaux, paie configurable avec impôt sur le revenu et cotisations sociales, fin de service basée sur des règles, et RH en arabe d'abord.",
        'HR Suite für Palästina — gesetzlicher Urlaub und Feiertage, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialbeiträgen, regelbasiertes Dienstende und Arabisch-zuerst-HR.',
        'HR Suite para Palestina — permisos y festivos legales, nómina configurable con impuesto sobre la renta y contribuciones sociales, fin de servicio basado en reglas, y RR. HH. en árabe primero.',
        'HR Suite per la Palestina — ferie e festività di legge, buste paga configurabili con imposta sul reddito e contributi sociali, fine servizio basata su regole, e HR in arabo prima di tutto.',
        'HR Suite voor Palestina — wettelijk verlof en feestdagen, configureerbare loonadministratie met inkomstenbelasting en sociale bijdragen, op regels gebaseerd einde dienstverband, en Arabisch-eerst-HR.'),
    'Palestine · PS': _t('Palestine · PS', 'Palästina · PS', 'Palestina · PS', 'Palestina · PS', 'Palestina · PS'),
    '<span class="current">Palestine</span>': _t(
        '<span class="current">Palestine</span>', '<span class="current">Palästina</span>',
        '<span class="current">Palestina</span>', '<span class="current">Palestina</span>',
        '<span class="current">Palestina</span>'),
    'HR &amp; payroll, built for <span class="p-grad">Palestine</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">la Palestine</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">Palästina</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">Palestina</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">la Palestina</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">Palestina</span>'),
    'HR Suite runs your Palestine workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social contributions, rule-based end-of-service, Arabic throughout, and full employee records.': _t(
        'HR Suite gère vos effectifs en Palestine — congés légaux et le calendrier des jours fériés locaux, paie configurable avec impôt sur le revenu et cotisations sociales, fin de service basée sur des règles, arabe partout et dossiers complets des employés.',
        'HR Suite steuert Ihre Belegschaft in Palästina — gesetzlicher Urlaub und der lokale Feiertagskalender, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialbeiträgen, regelbasiertes Dienstende, durchgehend Arabisch und vollständige Mitarbeiterakten.',
        'HR Suite gestiona su plantilla en Palestina — permisos legales y el calendario de festivos local, nómina configurable con impuesto sobre la renta y contribuciones sociales, fin de servicio basado en reglas, árabe en todo y expedientes completos de empleados.',
        'HR Suite gestisce il tuo organico in Palestina — ferie di legge e il calendario delle festività locali, buste paga configurabili con imposta sul reddito e contributi sociali, fine servizio basata su regole, arabo ovunque e anagrafiche complete dei dipendenti.',
        'HR Suite runt uw personeelsbestand in Palestina — wettelijk verlof en de lokale feestdagenkalender, configureerbare loonadministratie met inkomstenbelasting en sociale bijdragen, op regels gebaseerd einde dienstverband, overal Arabisch en volledige personeelsdossiers.'),
    'Palestine compliance, out of the box': _t(
        "Conformité Palestine, prête à l'emploi", 'Palästina-Compliance, sofort einsatzbereit',
        'Cumplimiento en Palestina, listo para usar', "Conformità Palestina, pronta all'uso",
        'Palestina-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Palestine does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme la Palestine le fait — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie Palästina es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Palestina — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fa la Palestina — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals Palestina dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Statutory leave &amp; holidays': T_STAT_LEAVE_TITLE,
    'Statutory annual, sick and maternity leave and the Palestinian public-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et de maternité légaux et le calendrier des jours fériés palestiniens, intégrés.',
        'Gesetzlicher Jahres-, Kranken- und Mutterschaftsurlaub sowie der palästinensische Feiertagskalender, integriert.',
        'Permisos legales anual, por enfermedad y por maternidad y el calendario de festivos palestino, integrados.',
        'Ferie annuali, per malattia e per maternità di legge e il calendario delle festività palestinesi, integrati.',
        'Wettelijk jaarlijks, ziekte- en zwangerschapsverlof en de Palestijnse feestdagenkalender, ingebouwd.'),
    'Configurable payroll': T_CONFIG_PAYROLL_TITLE,
    'Model Palestinian income tax and social contributions as configurable, classified deductions, applied in every pay run.': _t(
        "Modélisez l'impôt sur le revenu palestinien et les cotisations sociales sous forme de retenues configurables et classifiées, appliquées à chaque cycle de paie.",
        'Modellieren Sie die palästinensische Einkommensteuer und Sozialbeiträge als konfigurierbare, klassifizierte Abzüge, die bei jedem Abrechnungslauf angewendet werden.',
        'Modele el impuesto sobre la renta palestino y las contribuciones sociales como deducciones configurables y clasificadas, aplicadas en cada ejecución de nómina.',
        "Modella l'imposta sul reddito palestinese e i contributi sociali come trattenute configurabili e classificate, applicate a ogni elaborazione delle buste paga.",
        'Modelleer de Palestijnse inkomstenbelasting en sociale bijdragen als configureerbare, geclassificeerde inhoudingen die bij elke loonrun worden toegepast.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.': T_EOS_ENTITLE,
    'Arabic-first &amp; core HR': T_ARABIC_CORE_HR_TITLE,
    'Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.': T_ARABIC_LOCALCUR,
    'Run Palestine HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie en Palestine comme il se doit',
        'HR &amp; Gehaltsabrechnung in Palästina richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Palestina como es debido',
        'Gestisci HR &amp; buste paga in Palestina nel modo giusto',
        'Regel HR &amp; loonadministratie in Palestina zoals het hoort'),
    'See HR Suite handle Palestine leave, payroll and end-of-service for your team.': _t(
        'Voyez HR Suite gérer les congés, la paie et la fin de service en Palestine pour votre équipe.',
        'Sehen Sie, wie HR Suite Urlaub, Gehaltsabrechnung und Dienstende in Palästina für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona los permisos, la nómina y el fin de servicio en Palestina para su equipo.',
        'Guarda HR Suite gestire ferie, buste paga e fine servizio in Palestina per il tuo team.',
        'Zie HR Suite verlof, loonadministratie en einde dienstverband in Palestina voor uw team afhandelen.'),
})}


PAGE['/regions/syria/'] = {'src': 'regions/syria/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Syria | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour la Syrie | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für Syrien | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Siria | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per la Siria | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor Syrië | FulcrumGrid'),
    'HR Suite for Syria — statutory leave and holidays, configurable payroll with income tax and social insurance, rule-based end-of-service, and Arabic-first HR.': _t(
        "HR Suite pour la Syrie — congés et jours fériés légaux, paie configurable avec impôt sur le revenu et assurance sociale, fin de service basée sur des règles, et RH en arabe d'abord.",
        'HR Suite für Syrien — gesetzlicher Urlaub und Feiertage, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialversicherung, regelbasiertes Dienstende und Arabisch-zuerst-HR.',
        'HR Suite para Siria — permisos y festivos legales, nómina configurable con impuesto sobre la renta y seguro social, fin de servicio basado en reglas, y RR. HH. en árabe primero.',
        'HR Suite per la Siria — ferie e festività di legge, buste paga configurabili con imposta sul reddito e assicurazione sociale, fine servizio basata su regole, e HR in arabo prima di tutto.',
        'HR Suite voor Syrië — wettelijk verlof en feestdagen, configureerbare loonadministratie met inkomstenbelasting en sociale verzekering, op regels gebaseerd einde dienstverband, en Arabisch-eerst-HR.'),
    'Syria · SY': _t('Syrie · SY', 'Syrien · SY', 'Siria · SY', 'Siria · SY', 'Syrië · SY'),
    '<span class="current">Syria</span>': _t(
        '<span class="current">Syrie</span>', '<span class="current">Syrien</span>',
        '<span class="current">Siria</span>', '<span class="current">Siria</span>',
        '<span class="current">Syrië</span>'),
    'HR &amp; payroll, built for <span class="p-grad">Syria</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">la Syrie</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">Syrien</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">Siria</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">la Siria</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">Syrië</span>'),
    'HR Suite runs your Syria workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social insurance, rule-based end-of-service, Arabic throughout, and full employee records.': _t(
        'HR Suite gère vos effectifs en Syrie — congés légaux et le calendrier des jours fériés locaux, paie configurable avec impôt sur le revenu et assurance sociale, fin de service basée sur des règles, arabe partout et dossiers complets des employés.',
        'HR Suite steuert Ihre Belegschaft in Syrien — gesetzlicher Urlaub und der lokale Feiertagskalender, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialversicherung, regelbasiertes Dienstende, durchgehend Arabisch und vollständige Mitarbeiterakten.',
        'HR Suite gestiona su plantilla en Siria — permisos legales y el calendario de festivos local, nómina configurable con impuesto sobre la renta y seguro social, fin de servicio basado en reglas, árabe en todo y expedientes completos de empleados.',
        'HR Suite gestisce il tuo organico in Siria — ferie di legge e il calendario delle festività locali, buste paga configurabili con imposta sul reddito e assicurazione sociale, fine servizio basata su regole, arabo ovunque e anagrafiche complete dei dipendenti.',
        'HR Suite runt uw personeelsbestand in Syrië — wettelijk verlof en de lokale feestdagenkalender, configureerbare loonadministratie met inkomstenbelasting en sociale verzekering, op regels gebaseerd einde dienstverband, overal Arabisch en volledige personeelsdossiers.'),
    'Syria compliance, out of the box': _t(
        "Conformité Syrie, prête à l'emploi", 'Syrien-Compliance, sofort einsatzbereit',
        'Cumplimiento en Siria, listo para usar', "Conformità Siria, pronta all'uso",
        'Syrië-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Syria does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme la Syrie le fait — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie Syrien es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Siria — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fa la Siria — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals Syrië dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Statutory leave &amp; holidays': T_STAT_LEAVE_TITLE,
    'Statutory annual, sick and maternity leave and the Syrian public-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et de maternité légaux et le calendrier des jours fériés syriens, intégrés.',
        'Gesetzlicher Jahres-, Kranken- und Mutterschaftsurlaub sowie der syrische Feiertagskalender, integriert.',
        'Permisos legales anual, por enfermedad y por maternidad y el calendario de festivos sirio, integrados.',
        'Ferie annuali, per malattia e per maternità di legge e il calendario delle festività siriane, integrati.',
        'Wettelijk jaarlijks, ziekte- en zwangerschapsverlof en de Syrische feestdagenkalender, ingebouwd.'),
    'Configurable payroll': T_CONFIG_PAYROLL_TITLE,
    'Model Syrian income tax and social-insurance contributions as configurable, classified deductions, applied in every pay run.': _t(
        "Modélisez l'impôt sur le revenu syrien et les cotisations d'assurance sociale sous forme de retenues configurables et classifiées, appliquées à chaque cycle de paie.",
        'Modellieren Sie die syrische Einkommensteuer und Sozialversicherungsbeiträge als konfigurierbare, klassifizierte Abzüge, die bei jedem Abrechnungslauf angewendet werden.',
        'Modele el impuesto sobre la renta sirio y las cotizaciones al seguro social como deducciones configurables y clasificadas, aplicadas en cada ejecución de nómina.',
        "Modella l'imposta sul reddito siriana e i contributi per l'assicurazione sociale come trattenute configurabili e classificate, applicate a ogni elaborazione delle buste paga.",
        'Modelleer de Syrische inkomstenbelasting en socialeverzekeringsbijdragen als configureerbare, geclassificeerde inhoudingen die bij elke loonrun worden toegepast.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.': T_EOS_ENTITLE,
    'Arabic-first &amp; core HR': T_ARABIC_CORE_HR_TITLE,
    'Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.': T_ARABIC_LOCALCUR,
    'Run Syria HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie en Syrie comme il se doit',
        'HR &amp; Gehaltsabrechnung in Syrien richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Siria como es debido',
        'Gestisci HR &amp; buste paga in Siria nel modo giusto',
        'Regel HR &amp; loonadministratie in Syrië zoals het hoort'),
    'See HR Suite handle Syria leave, payroll and end-of-service for your team.': _t(
        'Voyez HR Suite gérer les congés, la paie et la fin de service en Syrie pour votre équipe.',
        'Sehen Sie, wie HR Suite Urlaub, Gehaltsabrechnung und Dienstende in Syrien für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona los permisos, la nómina y el fin de servicio en Siria para su equipo.',
        'Guarda HR Suite gestire ferie, buste paga e fine servizio in Siria per il tuo team.',
        'Zie HR Suite verlof, loonadministratie en einde dienstverband in Syrië voor uw team afhandelen.'),
})}


PAGE['/regions/yemen/'] = {'src': 'regions/yemen/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Yemen | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour le Yémen | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für den Jemen | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Yemen | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per lo Yemen | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor Jemen | FulcrumGrid'),
    'HR Suite for Yemen — statutory leave and holidays, configurable payroll with income tax and social insurance, rule-based end-of-service, and Arabic-first HR.': _t(
        "HR Suite pour le Yémen — congés et jours fériés légaux, paie configurable avec impôt sur le revenu et assurance sociale, fin de service basée sur des règles, et RH en arabe d'abord.",
        'HR Suite für den Jemen — gesetzlicher Urlaub und Feiertage, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialversicherung, regelbasiertes Dienstende und Arabisch-zuerst-HR.',
        'HR Suite para Yemen — permisos y festivos legales, nómina configurable con impuesto sobre la renta y seguro social, fin de servicio basado en reglas, y RR. HH. en árabe primero.',
        'HR Suite per lo Yemen — ferie e festività di legge, buste paga configurabili con imposta sul reddito e assicurazione sociale, fine servizio basata su regole, e HR in arabo prima di tutto.',
        'HR Suite voor Jemen — wettelijk verlof en feestdagen, configureerbare loonadministratie met inkomstenbelasting en sociale verzekering, op regels gebaseerd einde dienstverband, en Arabisch-eerst-HR.'),
    'Yemen · YE': _t('Yémen · YE', 'Jemen · YE', 'Yemen · YE', 'Yemen · YE', 'Jemen · YE'),
    '<span class="current">Yemen</span>': _t(
        '<span class="current">Yémen</span>', '<span class="current">Jemen</span>',
        '<span class="current">Yemen</span>', '<span class="current">Yemen</span>',
        '<span class="current">Jemen</span>'),
    'HR &amp; payroll, built for <span class="p-grad">Yemen</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">le Yémen</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">den Jemen</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">Yemen</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">lo Yemen</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">Jemen</span>'),
    'HR Suite runs your Yemen workforce — statutory leave and the local holiday calendar, configurable payroll with income tax and social insurance, rule-based end-of-service, Arabic throughout, and full employee records.': _t(
        'HR Suite gère vos effectifs au Yémen — congés légaux et le calendrier des jours fériés locaux, paie configurable avec impôt sur le revenu et assurance sociale, fin de service basée sur des règles, arabe partout et dossiers complets des employés.',
        'HR Suite steuert Ihre Belegschaft im Jemen — gesetzlicher Urlaub und der lokale Feiertagskalender, konfigurierbare Gehaltsabrechnung mit Einkommensteuer und Sozialversicherung, regelbasiertes Dienstende, durchgehend Arabisch und vollständige Mitarbeiterakten.',
        'HR Suite gestiona su plantilla en Yemen — permisos legales y el calendario de festivos local, nómina configurable con impuesto sobre la renta y seguro social, fin de servicio basado en reglas, árabe en todo y expedientes completos de empleados.',
        'HR Suite gestisce il tuo organico nello Yemen — ferie di legge e il calendario delle festività locali, buste paga configurabili con imposta sul reddito e assicurazione sociale, fine servizio basata su regole, arabo ovunque e anagrafiche complete dei dipendenti.',
        'HR Suite runt uw personeelsbestand in Jemen — wettelijk verlof en de lokale feestdagenkalender, configureerbare loonadministratie met inkomstenbelasting en sociale verzekering, op regels gebaseerd einde dienstverband, overal Arabisch en volledige personeelsdossiers.'),
    'Yemen compliance, out of the box': _t(
        "Conformité Yémen, prête à l'emploi", 'Jemen-Compliance, sofort einsatzbereit',
        'Cumplimiento en Yemen, listo para usar', "Conformità Yemen, pronta all'uso",
        'Jemen-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Yemen does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme le Yémen le fait — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie der Jemen es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Yemen — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fa lo Yemen — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals Jemen dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Statutory leave &amp; holidays': T_STAT_LEAVE_TITLE,
    'Statutory annual, sick and maternity leave and the Yemeni public-holiday calendar, built in.': _t(
        'Congés annuels, de maladie et de maternité légaux et le calendrier des jours fériés yéménites, intégrés.',
        'Gesetzlicher Jahres-, Kranken- und Mutterschaftsurlaub sowie der jemenitische Feiertagskalender, integriert.',
        'Permisos legales anual, por enfermedad y por maternidad y el calendario de festivos yemení, integrados.',
        'Ferie annuali, per malattia e per maternità di legge e il calendario delle festività yemenite, integrati.',
        'Wettelijk jaarlijks, ziekte- en zwangerschapsverlof en de Jemenitische feestdagenkalender, ingebouwd.'),
    'Configurable payroll': T_CONFIG_PAYROLL_TITLE,
    'Model Yemeni income tax and social-insurance contributions as configurable, classified deductions, applied in every pay run.': _t(
        "Modélisez l'impôt sur le revenu yéménite et les cotisations d'assurance sociale sous forme de retenues configurables et classifiées, appliquées à chaque cycle de paie.",
        'Modellieren Sie die jemenitische Einkommensteuer und Sozialversicherungsbeiträge als konfigurierbare, klassifizierte Abzüge, die bei jedem Abrechnungslauf angewendet werden.',
        'Modele el impuesto sobre la renta yemení y las cotizaciones al seguro social como deducciones configurables y clasificadas, aplicadas en cada ejecución de nómina.',
        "Modella l'imposta sul reddito yemenita e i contributi per l'assicurazione sociale come trattenute configurabili e classificate, applicate a ogni elaborazione delle buste paga.",
        'Modelleer de Jemenitische inkomstenbelasting en socialeverzekeringsbijdragen als configureerbare, geclassificeerde inhoudingen die bij elke loonrun worden toegepast.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'Configure end-of-service on the rule-based engine — days of wage per year — so local entitlements fit without a hard-coded preset.': T_EOS_ENTITLE,
    'Arabic-first &amp; core HR': T_ARABIC_CORE_HR_TITLE,
    'Arabic, right-to-left throughout, pay in local currency, plus employee records, onboarding, time off and self-service.': T_ARABIC_LOCALCUR,
    'Run Yemen HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie au Yémen comme il se doit',
        'HR &amp; Gehaltsabrechnung im Jemen richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Yemen como es debido',
        'Gestisci HR &amp; buste paga nello Yemen nel modo giusto',
        'Regel HR &amp; loonadministratie in Jemen zoals het hoort'),
    'See HR Suite handle Yemen leave, payroll and end-of-service for your team.': _t(
        'Voyez HR Suite gérer les congés, la paie et la fin de service au Yémen pour votre équipe.',
        'Sehen Sie, wie HR Suite Urlaub, Gehaltsabrechnung und Dienstende im Jemen für Ihr Team abwickelt.',
        'Vea cómo HR Suite gestiona los permisos, la nómina y el fin de servicio en Yemen para su equipo.',
        'Guarda HR Suite gestire ferie, buste paga e fine servizio nello Yemen per il tuo team.',
        'Zie HR Suite verlof, loonadministratie en einde dienstverband in Jemen voor uw team afhandelen.'),
})}


PAGE['/regions/middle-east/'] = {'src': 'regions/middle-east/index.html', 't': _common({
    'HR Suite — HR &amp; payroll for Middle East | FulcrumGrid': _t(
        'HR Suite — RH &amp; paie pour le Moyen-Orient | FulcrumGrid',
        'HR Suite — HR &amp; Gehaltsabrechnung für den Nahen Osten | FulcrumGrid',
        'HR Suite — RR. HH. &amp; nómina para Oriente Medio | FulcrumGrid',
        'HR Suite — HR &amp; buste paga per il Medio Oriente | FulcrumGrid',
        'HR Suite — HR &amp; loonadministratie voor het Midden-Oosten | FulcrumGrid'),
    'HR Suite across the Middle East — Egypt, Jordan and the Levant — with configurable local payroll, rule-based end-of-service, multi-currency pay and Arabic-first HR.': _t(
        "HR Suite dans tout le Moyen-Orient — Égypte, Jordanie et le Levant — avec paie locale configurable, fin de service basée sur des règles, paie multidevise et RH en arabe d'abord.",
        'HR Suite im gesamten Nahen Osten — Ägypten, Jordanien und die Levante — mit konfigurierbarer lokaler Gehaltsabrechnung, regelbasiertem Dienstende, Mehrwährungs-Bezahlung und Arabisch-zuerst-HR.',
        'HR Suite en todo Oriente Medio — Egipto, Jordania y el Levante — con nómina local configurable, fin de servicio basado en reglas, pago multidivisa y RR. HH. en árabe primero.',
        'HR Suite in tutto il Medio Oriente — Egitto, Giordania e il Levante — con buste paga locali configurabili, fine servizio basata su regole, retribuzione multivaluta e HR in arabo prima di tutto.',
        "HR Suite in het hele Midden-Oosten — Egypte, Jordanië en de Levant — met configureerbare lokale loonadministratie, op regels gebaseerd einde dienstverband, uitbetaling in meerdere valuta's en Arabisch-eerst-HR."),
    'Middle East · MENA': _t('Moyen-Orient · MENA', 'Naher Osten · MENA', 'Oriente Medio · MENA',
        'Medio Oriente · MENA', 'Midden-Oosten · MENA'),
    '<span class="current">Middle East</span>': _t(
        '<span class="current">Moyen-Orient</span>', '<span class="current">Naher Osten</span>',
        '<span class="current">Oriente Medio</span>', '<span class="current">Medio Oriente</span>',
        '<span class="current">Midden-Oosten</span>'),
    'HR &amp; payroll, built for <span class="p-grad">the Middle East</span>': _t(
        'RH &amp; paie, conçu pour <span class="p-grad">le Moyen-Orient</span>',
        'HR &amp; Gehaltsabrechnung, gebaut für <span class="p-grad">den Nahen Osten</span>',
        'RR. HH. &amp; nómina, creado para <span class="p-grad">Oriente Medio</span>',
        'HR &amp; buste paga, costruito per <span class="p-grad">il Medio Oriente</span>',
        'HR &amp; loonadministratie, gebouwd voor <span class="p-grad">het Midden-Oosten</span>'),
    'Arabic-first HR and payroll across the wider Middle East — configurable local deductions and end-of-service, multi-currency pay, and full employee records. Deepest in the Gulf, ready beyond it.': _t(
        "RH et paie en arabe d'abord dans tout le Moyen-Orient élargi — retenues locales et fin de service configurables, paie multidevise et dossiers complets des employés. Le plus abouti dans le Golfe, prêt au-delà.",
        'Arabisch-zuerst-HR und -Gehaltsabrechnung im gesamten erweiterten Nahen Osten — konfigurierbare lokale Abzüge und Dienstende, Mehrwährungs-Bezahlung und vollständige Mitarbeiterakten. Am umfassendsten am Golf, bereit auch darüber hinaus.',
        'RR. HH. y nómina en árabe primero en todo el Oriente Medio ampliado — deducciones locales y fin de servicio configurables, pago multidivisa y expedientes completos de empleados. Más completo en el Golfo, listo más allá.',
        'HR e buste paga in arabo prima di tutto in tutto il Medio Oriente allargato — trattenute locali e fine servizio configurabili, retribuzione multivaluta e anagrafiche complete dei dipendenti. Più completo nel Golfo, pronto anche oltre.',
        "Arabisch-eerst HR en loonadministratie in het hele bredere Midden-Oosten — configureerbare lokale inhoudingen en einde dienstverband, uitbetaling in meerdere valuta's en volledige personeelsdossiers. Het meest uitgebreid in de Golf, klaar voor daarbuiten."),
    'Middle East compliance, out of the box': _t(
        "Conformité Moyen-Orient, prête à l'emploi", 'Compliance im Nahen Osten, sofort einsatzbereit',
        'Cumplimiento en Oriente Medio, listo para usar', "Conformità Medio Oriente, pronta all'uso",
        'Midden-Oosten-compliance, direct klaar voor gebruik'),
    'The modules that make HR Suite work the way Middle East does — each part of the same platform, no separate tools.': _t(
        'Les modules qui font fonctionner HR Suite comme le Moyen-Orient le fait — chacun faisant partie de la même plateforme, sans outils séparés.',
        'Die Module, die HR Suite so arbeiten lassen, wie der Nahe Osten es tut — jedes Teil derselben Plattform, keine separaten Tools.',
        'Los módulos que hacen que HR Suite funcione como lo hace Oriente Medio — cada uno parte de la misma plataforma, sin herramientas separadas.',
        'I moduli che fanno funzionare HR Suite come fa il Medio Oriente — ciascuno parte della stessa piattaforma, senza strumenti separati.',
        'De modules die HR Suite laten werken zoals het Midden-Oosten dat doet — elk onderdeel van hetzelfde platform, geen aparte tools.'),
    'Configurable local payroll': _t('Paie locale configurable', 'Konfigurierbare lokale Gehaltsabrechnung',
        'Nómina local configurable', 'Buste paga locali configurabili', 'Configureerbare lokale loonadministratie'),
    "Model each country's income tax and social contributions as configurable, classified deduction types — no country hard-coding required.": _t(
        "Modélisez l'impôt sur le revenu et les cotisations sociales de chaque pays sous forme de types de retenues configurables et classifiés — aucun codage en dur par pays requis.",
        'Modellieren Sie die Einkommensteuer und Sozialbeiträge jedes Landes als konfigurierbare, klassifizierte Abzugsarten — keine länderspezifische Festcodierung erforderlich.',
        'Modele el impuesto sobre la renta y las contribuciones sociales de cada país como tipos de deducción configurables y clasificados — sin necesidad de codificación fija por país.',
        "Modella l'imposta sul reddito e i contributi sociali di ciascun paese come tipi di trattenuta configurabili e classificati — senza alcuna codifica fissa per paese.",
        'Modelleer de inkomstenbelasting en sociale bijdragen van elk land als configureerbare, geclassificeerde inhoudingstypen — geen hardcoding per land nodig.'),
    'End-of-service, your rules': T_EOS_TITLE,
    'The end-of-service engine is rule-based — days of wage per year, banded by service — so you configure local gratuity even without a built-in preset.': _t(
        "Le moteur de fin de service est basé sur des règles — des jours de salaire par année, échelonnés selon l'ancienneté — pour que vous configuriez la gratification locale même sans préréglage intégré.",
        'Die Dienstende-Engine ist regelbasiert — Lohntage pro Jahr, gestaffelt nach Betriebszugehörigkeit — sodass Sie die lokale Abfindung auch ohne integrierte Voreinstellung konfigurieren.',
        'El motor de fin de servicio se basa en reglas — días de salario por año, escalonados según la antigüedad — para que configure la gratificación local incluso sin un preajuste integrado.',
        "Il motore di fine servizio è basato su regole — giorni di retribuzione per anno, suddivisi per anzianità — così configuri la gratifica locale anche senza un preset integrato.",
        'De einde-dienstverband-engine is op regels gebaseerd — loondagen per jaar, gestaffeld naar diensttijd — zodat u de lokale gratificatie configureert, zelfs zonder ingebouwde voorinstelling.'),
    'Arabic-first &amp; multi-currency': _t('Arabe en priorité &amp; multidevise', 'Arabisch zuerst &amp; Mehrwährung',
        'Árabe primero &amp; multidivisa', 'Arabo prima di tutto &amp; multivaluta', "Arabisch eerst &amp; meerdere valuta's"),
    'Arabic, right-to-left throughout, bilingual documents, and pay in local currency.': _t(
        'Arabe, de droite à gauche partout, documents bilingues et paie en monnaie locale.',
        'Arabisch, durchgehend von rechts nach links, zweisprachige Dokumente und Bezahlung in lokaler Währung.',
        'Árabe, de derecha a izquierda en todo, documentos bilingües y pago en moneda local.',
        'Arabo, da destra a sinistra ovunque, documenti bilingui e retribuzione in valuta locale.',
        'Arabisch, van rechts naar links overal, tweetalige documenten en uitbetaling in lokale valuta.'),
    'Core HR &amp; self-service': _t('RH essentielles &amp; libre-service', 'Kern-HR &amp; Self-Service',
        'RR. HH. esenciales &amp; autoservicio', 'HR di base &amp; self-service', 'Kern-HR &amp; selfservice'),
    'Employee records, onboarding, time off and self-service — the whole lifecycle on one platform.': _t(
        'Dossiers des employés, intégration, congés et libre-service — tout le cycle de vie sur une seule plateforme.',
        'Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service — der gesamte Lebenszyklus auf einer Plattform.',
        'Expedientes de empleados, incorporación, ausencias y autoservicio — todo el ciclo de vida en una sola plataforma.',
        "Anagrafiche dei dipendenti, onboarding, ferie e self-service — l'intero ciclo di vita su un'unica piattaforma.",
        'Personeelsdossiers, onboarding, verlof en selfservice — de hele levenscyclus op één platform.'),
    'Countries': _t('Pays', 'Länder', 'Países', 'Paesi', 'Landen'),
    'Countries in this region': _t('Pays de cette région', 'Länder in dieser Region',
        'Países de esta región', 'Paesi di questa regione', 'Landen in deze regio'),
    'Pick a country for its statutory payroll and compliance detail — and it runs across the wider region too.': _t(
        'Choisissez un pays pour le détail de sa paie légale et de sa conformité — et cela fonctionne aussi dans toute la région élargie.',
        'Wählen Sie ein Land für die Details zu gesetzlicher Gehaltsabrechnung und Compliance — und es funktioniert auch in der gesamten erweiterten Region.',
        'Elija un país para ver el detalle de su nómina legal y su cumplimiento — y también funciona en toda la región ampliada.',
        'Scegli un paese per il dettaglio della sua busta paga di legge e della conformità — e funziona anche in tutta la regione allargata.',
        'Kies een land voor de details van de wettelijke loonadministratie en compliance — en het werkt ook in de hele bredere regio.'),
    '<h3>Egypt</h3>': _t('<h3>Égypte</h3>', '<h3>Ägypten</h3>', '<h3>Egipto</h3>', '<h3>Egitto</h3>', '<h3>Egypte</h3>'),
    '<h3>Jordan</h3>': _t('<h3>Jordanie</h3>', '<h3>Jordanien</h3>', '<h3>Jordania</h3>', '<h3>Giordania</h3>', '<h3>Jordanië</h3>'),
    '<h3>Lebanon</h3>': _t('<h3>Liban</h3>', '<h3>Libanon</h3>', '<h3>Líbano</h3>', '<h3>Libano</h3>', '<h3>Libanon</h3>'),
    '<h3>Iraq</h3>': _t('<h3>Irak</h3>', '<h3>Irak</h3>', '<h3>Irak</h3>', '<h3>Iraq</h3>', '<h3>Irak</h3>'),
    '<h3>Palestine</h3>': _t('<h3>Palestine</h3>', '<h3>Palästina</h3>', '<h3>Palestina</h3>', '<h3>Palestina</h3>', '<h3>Palestina</h3>'),
    '<h3>Syria</h3>': _t('<h3>Syrie</h3>', '<h3>Syrien</h3>', '<h3>Siria</h3>', '<h3>Siria</h3>', '<h3>Syrië</h3>'),
    '<h3>Yemen</h3>': _t('<h3>Yémen</h3>', '<h3>Jemen</h3>', '<h3>Yemen</h3>', '<h3>Yemen</h3>', '<h3>Jemen</h3>'),
    'Payroll · EOSB · Arabic': _t('Paie · EOSB · Arabe', 'Gehaltsabrechnung · EOSB · Arabisch',
        'Nómina · EOSB · Árabe', 'Buste paga · EOSB · Arabo', 'Loon · EOSB · Arabisch'),
    'Payroll · SSC · Arabic': _t('Paie · SSC · Arabe', 'Gehaltsabrechnung · SSC · Arabisch',
        'Nómina · SSC · Árabe', 'Buste paga · SSC · Arabo', 'Loon · SSC · Arabisch'),
    'Leave · Payroll · NSSF': _t('Congés · Paie · NSSF', 'Urlaub · Gehaltsabrechnung · NSSF',
        'Permisos · Nómina · NSSF', 'Ferie · Buste paga · NSSF', 'Verlof · Loon · NSSF'),
    'Leave · Payroll · Arabic': _t('Congés · Paie · Arabe', 'Urlaub · Gehaltsabrechnung · Arabisch',
        'Permisos · Nómina · Árabe', 'Ferie · Buste paga · Arabo', 'Verlof · Loon · Arabisch'),
    '<strong>Also runs across the region:</strong> Morocco · Tunisia · Algeria · Libya · Sudan — with configurable local payroll, end-of-service and multi-currency pay. <a href="/contact/">Ask about your market →</a>': _t(
        '<strong>Fonctionne aussi dans toute la région :</strong> Maroc · Tunisie · Algérie · Libye · Soudan — avec paie locale configurable, fin de service et paie multidevise. <a href="/contact/">Renseignez-vous sur votre marché →</a>',
        '<strong>Läuft auch in der gesamten Region:</strong> Marokko · Tunesien · Algerien · Libyen · Sudan — mit konfigurierbarer lokaler Gehaltsabrechnung, Dienstende und Mehrwährungs-Bezahlung. <a href="/contact/">Fragen Sie nach Ihrem Markt →</a>',
        '<strong>También funciona en toda la región:</strong> Marruecos · Túnez · Argelia · Libia · Sudán — con nómina local configurable, fin de servicio y pago multidivisa. <a href="/contact/">Pregunte por su mercado →</a>',
        '<strong>Funziona anche in tutta la regione:</strong> Marocco · Tunisia · Algeria · Libia · Sudan — con buste paga locali configurabili, fine servizio e retribuzione multivaluta. <a href="/contact/">Chiedi informazioni sul tuo mercato →</a>',
        "<strong>Werkt ook in de hele regio:</strong> Marokko · Tunesië · Algerije · Libië · Soedan — met configureerbare lokale loonadministratie, einde dienstverband en uitbetaling in meerdere valuta's. <a href=\"/contact/\">Vraag naar uw markt →</a>"),
    'Run Middle East HR &amp; payroll the right way': _t(
        'Gérez les RH &amp; la paie au Moyen-Orient comme il se doit',
        'HR &amp; Gehaltsabrechnung im Nahen Osten richtig machen',
        'Gestione las RR. HH. &amp; la nómina en Oriente Medio como es debido',
        'Gestisci HR &amp; buste paga in Medio Oriente nel modo giusto',
        'Regel HR &amp; loonadministratie in het Midden-Oosten zoals het hoort'),
    "Tell us where you operate and we'll show you how HR Suite fits.": _t(
        "Dites-nous où vous opérez et nous vous montrerons comment HR Suite s'intègre.",
        'Sagen Sie uns, wo Sie tätig sind, und wir zeigen Ihnen, wie HR Suite passt.',
        'Cuéntenos dónde opera y le mostraremos cómo encaja HR Suite.',
        'Dicci dove operi e ti mostreremo come si integra HR Suite.',
        'Vertel ons waar u actief bent en we laten zien hoe HR Suite past.'),
})}
