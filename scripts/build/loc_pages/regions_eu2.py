# -*- coding: utf-8 -*-
"""Translations for the EU REGION pages: Germany, Spain, Italy, Netherlands.

Brand/product names (FulcrumGrid, HR Suite, Command Center, Collection),
statutory/technical proper nouns and acronyms (GDPR, SEPA, DPO, CBA, CCNL,
Working Time Act, Workers' Statute), currency codes (EUR) and "Blog"/"FAQ"
stay in English per the localization rules. Country names are rendered in each
language's natural form. Prose around the kept terms is translated; honesty
hedges ("configurable", "classified deductions") are preserved faithfully.

Keys are EXACT substrings of the committed English source (entities such as
&amp;, straight apostrophes, em-dashes and the × glyph preserved). Common
chrome (nav/footer/buttons, "Request a demo", "Email us", "Regions", "Skip to
content") is handled by loc_catalog.COMMON and is not repeated here.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


def _merge(*dicts):
    out = {}
    for d in dicts:
        out.update(d)
    return out


# ---------------------------------------------------------------------------
# Segments shared across all four pages (defined once, reused below).
# ---------------------------------------------------------------------------

_BUILT_IN ={'Built in': _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd')}

_EXPLORE = {'Explore HR Suite': _t(
    'Découvrir HR Suite', 'HR Suite entdecken', 'Explorar HR Suite',
    'Esplora HR Suite', 'Ontdek HR Suite')}

_SEE_PRICING = {
    'See HR Suite pricing': _t(
        'Voir les tarifs de HR Suite', 'HR Suite Preise ansehen',
        'Ver precios de HR Suite', 'Vedi i prezzi di HR Suite',
        'Bekijk de prijzen van HR Suite'),
    'See HR Suite pricing →': _t(
        'Voir les tarifs de HR Suite →', 'HR Suite Preise ansehen →',
        'Ver precios de HR Suite →', 'Vedi i prezzi di HR Suite →',
        'Bekijk de prijzen van HR Suite →'),
}

_PRICE_NOTE = {
    'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on.': _t(
        "Chaque module présenté ici fait partie de HR Suite — paie avancée, clôture annuelle et conformité sur le plan Enterprise, ou en option par poste sur n'importe quel plan.",
        'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Zusatz pro Platz zu jedem Plan.',
        'Cada módulo aquí forma parte de HR Suite — nóminas avanzadas, cierre de año y cumplimiento en el plan Enterprise, o añadido a cualquier plan como complemento por usuario.',
        'Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura annuale e conformità nel piano Enterprise, oppure aggiunto a qualsiasi piano come componente aggiuntivo per postazione.',
        'Elke module hier maakt deel uit van HR Suite — geavanceerde salarisadministratie, jaarafsluiting en compliance in het Enterprise-plan, of toe te voegen aan elk plan als add-on per gebruiker.'),
}

# The three feature cards that are word-for-word identical on all four pages.
_SEPA = {
    'SEPA payments': _t('Paiements SEPA', 'SEPA-Zahlungen', 'Pagos SEPA', 'Pagamenti SEPA', 'SEPA-betalingen'),
    'Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.': _t(
        "Exportez un fichier de virement SEPA à partir d'un cycle de paie finalisé, avec des IBAN validés à la saisie.",
        'Exportieren Sie eine SEPA-Überweisungsdatei aus einem abgeschlossenen Gehaltslauf, mit bei der Eingabe validierten IBANs.',
        'Exporte un archivo de transferencia SEPA a partir de un proceso de nómina finalizado, con los IBAN validados al introducirlos.',
        "Esporta un file di bonifico SEPA da un ciclo di paga finalizzato, con gli IBAN convalidati all'inserimento.",
        "Exporteer een SEPA-overschrijvingsbestand uit een afgeronde salarisrun, met IBAN's die bij invoer worden gevalideerd."),
}

_GDPR = {
    'GDPR data-subject rights': _t(
        'Droits des personnes concernées (GDPR)', 'GDPR-Betroffenenrechte',
        'Derechos del interesado (GDPR)', "Diritti dell'interessato (GDPR)",
        'GDPR-rechten van betrokkenen'),
    'Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.': _t(
        "Export au titre du droit d'accès et effacement sélectif avec conservation, avec contact DPO et politiques de conservation intégrés.",
        'Auskunftsexport und selektive Löschung mit Aufbewahrung, mit integriertem DPO-Kontakt und Aufbewahrungsrichtlinien.',
        'Exportación por derecho de acceso y borrado selectivo con conservación, con contacto del DPO y políticas de conservación integrados.',
        "Esportazione per diritto di accesso ed erasure selettivo con conservazione, con contatto DPO e criteri di conservazione integrati.",
        'Export voor inzagerecht en selectieve wissing met bewaring, met DPO-contact en bewaarbeleid ingebouwd.'),
}

_LOCAL_HR_TITLE = {'Local payroll &amp; core HR': _t(
    'Paie locale &amp; RH de base', 'Lokale Gehaltsabrechnung &amp; Kern-HR',
    'Nóminas locales &amp; RR. HH. básicos', 'Buste paga locali &amp; HR di base',
    'Lokale salarisadministratie &amp; kern-HR')}


PAGE = {}


PAGE['/regions/germany/'] = {
    'src': 'regions/germany/index.html',
    't': _merge(_BUILT_IN, _EXPLORE, _SEE_PRICING, _PRICE_NOTE, _SEPA, _GDPR, _LOCAL_HR_TITLE, {
        # ---- Meta (title == og:title; description == og:description) ----
        'HR Suite — HR &amp; payroll for Germany | FulcrumGrid': _t(
            "HR Suite — RH &amp; paie pour l'Allemagne | FulcrumGrid",
            'HR Suite — HR &amp; Gehaltsabrechnung für Deutschland | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Alemania | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per la Germania | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor Duitsland | FulcrumGrid'),
        'HR Suite for Germany — CBA overtime with Working Time Act caps, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.': _t(
            "HR Suite pour l'Allemagne — heures supplémentaires CBA avec les plafonds du Working Time Act, fichiers de paie SEPA, droits GDPR, paie locale configurable en EUR, et RH complète.",
            'HR Suite für Deutschland — CBA-Überstunden mit den Grenzen des Working Time Act, SEPA-Zahlungsdateien, GDPR-Rechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige HR.',
            'HR Suite para Alemania — horas extra según CBA con los límites del Working Time Act, archivos de pago SEPA, derechos GDPR, nóminas locales configurables en EUR y RR. HH. completos.',
            'HR Suite per la Germania — straordinari CBA con i limiti del Working Time Act, file di pagamento SEPA, diritti GDPR, buste paga locali configurabili in EUR e HR completa.',
            'HR Suite voor Duitsland — CBA-overwerk met de limieten van de Working Time Act, SEPA-betaalbestanden, GDPR-rechten, configureerbare lokale salarisadministratie in EUR, en volledige HR.'),
        # ---- Hero ----
        'Germany · DE': _t('Allemagne · DE', 'Deutschland · DE', 'Alemania · DE', 'Germania · DE', 'Duitsland · DE'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Germany</em>': _t(
            "RH &amp; paie, conçu pour <em style=\"font-style:normal;color:var(--color-accent)\">l'Allemagne</em>",
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Deutschland</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">Alemania</em>',
            'HR &amp; buste paga, pensato per <em style="font-style:normal;color:var(--color-accent)">la Germania</em>',
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Duitsland</em>'),
        "HR Suite runs your Germany workforce — collective-agreement overtime with Working Time Act caps, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.": _t(
            "HR Suite pilote vos effectifs en Allemagne — heures supplémentaires prévues par la convention collective avec les plafonds du Working Time Act, fichiers de paie SEPA, droits des personnes concernées au titre du GDPR, paie locale configurable en EUR, et dossiers employés complets.",
            'HR Suite steuert Ihre Belegschaft in Deutschland — tarifvertragliche Überstunden mit den Grenzen des Working Time Act, SEPA-Zahlungsdateien, GDPR-Betroffenenrechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige Mitarbeiterakten.',
            'HR Suite gestiona su plantilla en Alemania — horas extra según convenio colectivo con los límites del Working Time Act, archivos de pago SEPA, derechos del interesado del GDPR, nóminas locales configurables en EUR y expedientes de empleados completos.',
            "HR Suite gestisce il tuo organico in Germania — straordinari da contratto collettivo con i limiti del Working Time Act, file di pagamento SEPA, diritti dell'interessato GDPR, buste paga locali configurabili in EUR e schede dipendente complete.",
            'HR Suite runt uw personeelsbestand in Duitsland — cao-overwerk met de limieten van de Working Time Act, SEPA-betaalbestanden, GDPR-rechten van betrokkenen, configureerbare lokale salarisadministratie in EUR, en volledige personeelsdossiers.'),
        # ---- Sub-head ----
        'Germany compliance, out of the box': _t(
            "La conformité pour l'Allemagne, prête à l'emploi",
            'Compliance für Deutschland, sofort einsatzbereit',
            'Cumplimiento para Alemania, listo para usar',
            "Conformità per la Germania, pronta all'uso",
            'Compliance voor Duitsland, kant-en-klaar'),
        'The modules that make HR Suite work the way Germany does — each part of the same grid, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière de l'Allemagne — chacun fait partie de la même grille, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie es Deutschland tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Alemania — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            "I moduli che fanno funzionare HR Suite come fa la Germania — ognuno parte della stessa griglia, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Duitsland dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards (Germany-specific) ----
        'Overtime &amp; working-time caps': _t(
            'Heures supplémentaires &amp; plafonds de temps de travail',
            'Überstunden &amp; Arbeitszeitgrenzen',
            'Horas extra &amp; límites de jornada',
            'Straordinari &amp; limiti di orario',
            'Overwerk &amp; arbeidstijdlimieten'),
        "Overtime at the customary 1.25× collective-agreement rate, with the Working Time Act's hour caps (10h/day) respected — configurable per agreement.": _t(
            "Heures supplémentaires au taux habituel de 1.25× prévu par la convention collective, dans le respect des plafonds horaires du Working Time Act (10 h/jour) — configurable par convention.",
            'Überstunden zum üblichen Satz von 1.25× laut Tarifvertrag, unter Einhaltung der Stundengrenzen des Working Time Act (10 Std./Tag) — konfigurierbar je Vertrag.',
            'Horas extra al tipo habitual de 1.25× del convenio colectivo, respetando los límites horarios del Working Time Act (10 h/día) — configurable por convenio.',
            'Straordinari alla tariffa abituale di 1.25× da contratto collettivo, nel rispetto dei limiti orari del Working Time Act (10 h/giorno) — configurabile per contratto.',
            'Overwerk tegen het gebruikelijke tarief van 1.25× volgens de cao, met inachtneming van de urenlimieten van de Working Time Act (10 u/dag) — configureerbaar per cao.'),
        "Model German income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.": _t(
            "Modélisez l'impôt sur le revenu et les cotisations sociales allemands sous forme de retenues configurables et classifiées — avec dossiers employés, intégration, congés et libre-service, en EUR.",
            'Bilden Sie deutsche Einkommensteuer und Sozialabgaben als konfigurierbare, klassifizierte Abzüge ab — mit Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service, in EUR.',
            'Modele el impuesto sobre la renta y las cotizaciones sociales alemanes como deducciones configurables y clasificadas — con expedientes de empleados, incorporación, ausencias y autoservicio, en EUR.',
            "Modella l'imposta sul reddito e i contributi previdenziali tedeschi come trattenute configurabili e classificate — con schede dipendente, onboarding, ferie e self-service, in EUR.",
            'Modelleer de Duitse inkomstenbelasting en sociale premies als configureerbare, geclassificeerde inhoudingen — met personeelsdossiers, onboarding, verlof en selfservice, in EUR.'),
        # ---- CTA ----
        'Run Germany HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie en Allemagne comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung in Deutschland richtig durch',
            'Gestione RR. HH. &amp; nóminas en Alemania como es debido',
            'Gestisci HR &amp; buste paga in Germania nel modo giusto',
            'Voer HR &amp; salarisadministratie in Duitsland op de juiste manier uit'),
        'See HR Suite handle German overtime, SEPA and GDPR for your team.': _t(
            "Voyez HR Suite gérer les heures supplémentaires allemandes, SEPA et GDPR pour votre équipe.",
            'Sehen Sie, wie HR Suite deutsche Überstunden, SEPA und GDPR für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona las horas extra alemanas, SEPA y GDPR para su equipo.',
            'Guarda HR Suite gestire gli straordinari tedeschi, SEPA e GDPR per il tuo team.',
            'Zie hoe HR Suite Duits overwerk, SEPA en GDPR voor uw team afhandelt.'),
    }),
}


PAGE['/regions/spain/'] = {
    'src': 'regions/spain/index.html',
    't': _merge(_BUILT_IN, _EXPLORE, _SEE_PRICING, _PRICE_NOTE, _SEPA, _GDPR, _LOCAL_HR_TITLE, {
        # ---- Meta (title == og:title; description == og:description) ----
        'HR Suite — HR &amp; payroll for Spain | FulcrumGrid': _t(
            "HR Suite — RH &amp; paie pour l'Espagne | FulcrumGrid",
            'HR Suite — HR &amp; Gehaltsabrechnung für Spanien | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para España | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per la Spagna | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor Spanje | FulcrumGrid'),
        "HR Suite for Spain — Workers' Statute overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.": _t(
            "HR Suite pour l'Espagne — heures supplémentaires du Statut des travailleurs, fichiers de paie SEPA, droits GDPR, paie locale configurable en EUR, et RH complète.",
            'HR Suite für Spanien — Überstunden nach dem Arbeitnehmerstatut, SEPA-Zahlungsdateien, GDPR-Rechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige HR.',
            'HR Suite para España — horas extra del Estatuto de los Trabajadores, archivos de pago SEPA, derechos GDPR, nóminas locales configurables en EUR y RR. HH. completos.',
            'HR Suite per la Spagna — straordinari da Statuto dei lavoratori, file di pagamento SEPA, diritti GDPR, buste paga locali configurabili in EUR e HR completa.',
            'HR Suite voor Spanje — overwerk volgens het Werknemersstatuut, SEPA-betaalbestanden, GDPR-rechten, configureerbare lokale salarisadministratie in EUR, en volledige HR.'),
        # ---- Hero ----
        'Spain · ES': _t('Espagne · ES', 'Spanien · ES', 'España · ES', 'Spagna · ES', 'Spanje · ES'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Spain</em>': _t(
            "RH &amp; paie, conçu pour <em style=\"font-style:normal;color:var(--color-accent)\">l'Espagne</em>",
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Spanien</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">España</em>',
            'HR &amp; buste paga, pensato per <em style="font-style:normal;color:var(--color-accent)">la Spagna</em>',
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Spanje</em>'),
        "HR Suite runs your Spain workforce — Workers' Statute overtime, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.": _t(
            "HR Suite pilote vos effectifs en Espagne — heures supplémentaires du Statut des travailleurs, fichiers de paie SEPA, droits des personnes concernées au titre du GDPR, paie locale configurable en EUR, et dossiers employés complets.",
            'HR Suite steuert Ihre Belegschaft in Spanien — Überstunden nach dem Arbeitnehmerstatut, SEPA-Zahlungsdateien, GDPR-Betroffenenrechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige Mitarbeiterakten.',
            'HR Suite gestiona su plantilla en España — horas extra del Estatuto de los Trabajadores, archivos de pago SEPA, derechos del interesado del GDPR, nóminas locales configurables en EUR y expedientes de empleados completos.',
            "HR Suite gestisce il tuo organico in Spagna — straordinari da Statuto dei lavoratori, file di pagamento SEPA, diritti dell'interessato GDPR, buste paga locali configurabili in EUR e schede dipendente complete.",
            'HR Suite runt uw personeelsbestand in Spanje — overwerk volgens het Werknemersstatuut, SEPA-betaalbestanden, GDPR-rechten van betrokkenen, configureerbare lokale salarisadministratie in EUR, en volledige personeelsdossiers.'),
        # ---- Sub-head ----
        'Spain compliance, out of the box': _t(
            "La conformité pour l'Espagne, prête à l'emploi",
            'Compliance für Spanien, sofort einsatzbereit',
            'Cumplimiento para España, listo para usar',
            "Conformità per la Spagna, pronta all'uso",
            'Compliance voor Spanje, kant-en-klaar'),
        'The modules that make HR Suite work the way Spain does — each part of the same grid, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière de l'Espagne — chacun fait partie de la même grille, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie es Spanien tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace España — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            "I moduli che fanno funzionare HR Suite come fa la Spagna — ognuno parte della stessa griglia, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Spanje dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards (Spain-specific) ----
        "Overtime — Workers' Statute": _t(
            'Heures supplémentaires — Statut des travailleurs',
            'Überstunden — Arbeitnehmerstatut',
            'Horas extra — Estatuto de los Trabajadores',
            'Straordinari — Statuto dei lavoratori',
            'Overwerk — Werknemersstatuut'),
        'Overtime at your collective-agreement premium (commonly around +75%), floored at the ordinary-hour value and capped at 80 hours a year.': _t(
            "Heures supplémentaires à la majoration prévue par votre convention collective (souvent autour de +75%), avec un plancher à la valeur de l'heure normale et un plafond de 80 heures par an.",
            'Überstunden zum Zuschlag Ihres Tarifvertrags (häufig um +75%), mindestens zum Wert der Normalstunde und auf 80 Stunden pro Jahr begrenzt.',
            'Horas extra con el recargo de su convenio colectivo (habitualmente en torno al +75%), con un mínimo del valor de la hora ordinaria y un tope de 80 horas al año.',
            "Straordinari alla maggiorazione del tuo contratto collettivo (spesso intorno al +75%), con un minimo pari al valore dell'ora ordinaria e un tetto di 80 ore all'anno.",
            'Overwerk tegen de toeslag van uw cao (vaak rond +75%), met als minimum de waarde van het normale uur en een maximum van 80 uur per jaar.'),
        "Model Spanish income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.": _t(
            "Modélisez l'impôt sur le revenu et les cotisations sociales espagnols sous forme de retenues configurables et classifiées — avec dossiers employés, intégration, congés et libre-service, en EUR.",
            'Bilden Sie spanische Einkommensteuer und Sozialabgaben als konfigurierbare, klassifizierte Abzüge ab — mit Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service, in EUR.',
            'Modele el impuesto sobre la renta y las cotizaciones sociales españoles como deducciones configurables y clasificadas — con expedientes de empleados, incorporación, ausencias y autoservicio, en EUR.',
            "Modella l'imposta sul reddito e i contributi previdenziali spagnoli come trattenute configurabili e classificate — con schede dipendente, onboarding, ferie e self-service, in EUR.",
            'Modelleer de Spaanse inkomstenbelasting en sociale premies als configureerbare, geclassificeerde inhoudingen — met personeelsdossiers, onboarding, verlof en selfservice, in EUR.'),
        # ---- CTA ----
        'Run Spain HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie en Espagne comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung in Spanien richtig durch',
            'Gestione RR. HH. &amp; nóminas en España como es debido',
            'Gestisci HR &amp; buste paga in Spagna nel modo giusto',
            'Voer HR &amp; salarisadministratie in Spanje op de juiste manier uit'),
        'See HR Suite handle Spanish overtime, SEPA and GDPR for your team.': _t(
            "Voyez HR Suite gérer les heures supplémentaires espagnoles, SEPA et GDPR pour votre équipe.",
            'Sehen Sie, wie HR Suite spanische Überstunden, SEPA und GDPR für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona las horas extra españolas, SEPA y GDPR para su equipo.',
            'Guarda HR Suite gestire gli straordinari spagnoli, SEPA e GDPR per il tuo team.',
            'Zie hoe HR Suite Spaans overwerk, SEPA en GDPR voor uw team afhandelt.'),
    }),
}


PAGE['/regions/italy/'] = {
    'src': 'regions/italy/index.html',
    't': _merge(_BUILT_IN, _EXPLORE, _SEE_PRICING, _PRICE_NOTE, _SEPA, _GDPR, _LOCAL_HR_TITLE, {
        # ---- Meta (title == og:title; description == og:description) ----
        'HR Suite — HR &amp; payroll for Italy | FulcrumGrid': _t(
            "HR Suite — RH &amp; paie pour l'Italie | FulcrumGrid",
            'HR Suite — HR &amp; Gehaltsabrechnung für Italien | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Italia | FulcrumGrid',
            "HR Suite — HR &amp; buste paga per l'Italia | FulcrumGrid",
            'HR Suite — HR &amp; salarisadministratie voor Italië | FulcrumGrid'),
        'HR Suite for Italy — CCNL overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.': _t(
            "HR Suite pour l'Italie — heures supplémentaires CCNL, fichiers de paie SEPA, droits GDPR, paie locale configurable en EUR, et RH complète.",
            'HR Suite für Italien — CCNL-Überstunden, SEPA-Zahlungsdateien, GDPR-Rechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige HR.',
            'HR Suite para Italia — horas extra según CCNL, archivos de pago SEPA, derechos GDPR, nóminas locales configurables en EUR y RR. HH. completos.',
            "HR Suite per l'Italia — straordinari CCNL, file di pagamento SEPA, diritti GDPR, buste paga locali configurabili in EUR e HR completa.",
            'HR Suite voor Italië — CCNL-overwerk, SEPA-betaalbestanden, GDPR-rechten, configureerbare lokale salarisadministratie in EUR, en volledige HR.'),
        # ---- Hero ----
        'Italy · IT': _t('Italie · IT', 'Italien · IT', 'Italia · IT', 'Italia · IT', 'Italië · IT'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Italy</em>': _t(
            "RH &amp; paie, conçu pour <em style=\"font-style:normal;color:var(--color-accent)\">l'Italie</em>",
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Italien</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">Italia</em>',
            "HR &amp; buste paga, pensato per <em style=\"font-style:normal;color:var(--color-accent)\">l'Italia</em>",
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Italië</em>'),
        "HR Suite runs your Italy workforce — CCNL overtime, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.": _t(
            "HR Suite pilote vos effectifs en Italie — heures supplémentaires CCNL, fichiers de paie SEPA, droits des personnes concernées au titre du GDPR, paie locale configurable en EUR, et dossiers employés complets.",
            'HR Suite steuert Ihre Belegschaft in Italien — CCNL-Überstunden, SEPA-Zahlungsdateien, GDPR-Betroffenenrechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige Mitarbeiterakten.',
            'HR Suite gestiona su plantilla en Italia — horas extra según CCNL, archivos de pago SEPA, derechos del interesado del GDPR, nóminas locales configurables en EUR y expedientes de empleados completos.',
            "HR Suite gestisce il tuo organico in Italia — straordinari CCNL, file di pagamento SEPA, diritti dell'interessato GDPR, buste paga locali configurabili in EUR e schede dipendente complete.",
            'HR Suite runt uw personeelsbestand in Italië — CCNL-overwerk, SEPA-betaalbestanden, GDPR-rechten van betrokkenen, configureerbare lokale salarisadministratie in EUR, en volledige personeelsdossiers.'),
        # ---- Sub-head ----
        'Italy compliance, out of the box': _t(
            "La conformité pour l'Italie, prête à l'emploi",
            'Compliance für Italien, sofort einsatzbereit',
            'Cumplimiento para Italia, listo para usar',
            "Conformità per l'Italia, pronta all'uso",
            'Compliance voor Italië, kant-en-klaar'),
        'The modules that make HR Suite work the way Italy does — each part of the same grid, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière de l'Italie — chacun fait partie de la même grille, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie es Italien tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Italia — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            "I moduli che fanno funzionare HR Suite come fa l'Italia — ognuno parte della stessa griglia, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Italië dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards (Italy-specific) ----
        'Overtime — CCNL rates': _t(
            'Heures supplémentaires — taux CCNL', 'Überstunden — CCNL-Sätze',
            'Horas extra — tarifas CCNL', 'Straordinari — tariffe CCNL',
            'Overwerk — CCNL-tarieven'),
        'Overtime at your national collective-agreement (CCNL) supplement — typically +15% to +50% — configurable per agreement.': _t(
            "Heures supplémentaires selon le supplément de votre convention collective nationale (CCNL) — généralement de +15% à +50% — configurable par convention.",
            'Überstunden nach dem Zuschlag Ihres nationalen Tarifvertrags (CCNL) — typischerweise +15% bis +50% — konfigurierbar je Vertrag.',
            'Horas extra según el complemento de su convenio colectivo nacional (CCNL) — normalmente del +15% al +50% — configurable por convenio.',
            'Straordinari secondo la maggiorazione del tuo contratto collettivo nazionale (CCNL) — tipicamente dal +15% al +50% — configurabile per contratto.',
            'Overwerk volgens de toeslag van uw nationale cao (CCNL) — doorgaans +15% tot +50% — configureerbaar per cao.'),
        "Model Italian income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.": _t(
            "Modélisez l'impôt sur le revenu et les cotisations sociales italiens sous forme de retenues configurables et classifiées — avec dossiers employés, intégration, congés et libre-service, en EUR.",
            'Bilden Sie italienische Einkommensteuer und Sozialabgaben als konfigurierbare, klassifizierte Abzüge ab — mit Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service, in EUR.',
            'Modele el impuesto sobre la renta y las cotizaciones sociales italianos como deducciones configurables y clasificadas — con expedientes de empleados, incorporación, ausencias y autoservicio, en EUR.',
            "Modella l'imposta sul reddito e i contributi previdenziali italiani come trattenute configurabili e classificate — con schede dipendente, onboarding, ferie e self-service, in EUR.",
            'Modelleer de Italiaanse inkomstenbelasting en sociale premies als configureerbare, geclassificeerde inhoudingen — met personeelsdossiers, onboarding, verlof en selfservice, in EUR.'),
        # ---- CTA ----
        'Run Italy HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie en Italie comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung in Italien richtig durch',
            'Gestione RR. HH. &amp; nóminas en Italia como es debido',
            'Gestisci HR &amp; buste paga in Italia nel modo giusto',
            'Voer HR &amp; salarisadministratie in Italië op de juiste manier uit'),
        'See HR Suite handle Italian overtime, SEPA and GDPR for your team.': _t(
            "Voyez HR Suite gérer les heures supplémentaires italiennes, SEPA et GDPR pour votre équipe.",
            'Sehen Sie, wie HR Suite italienische Überstunden, SEPA und GDPR für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona las horas extra italianas, SEPA y GDPR para su equipo.',
            'Guarda HR Suite gestire gli straordinari italiani, SEPA e GDPR per il tuo team.',
            'Zie hoe HR Suite Italiaans overwerk, SEPA en GDPR voor uw team afhandelt.'),
    }),
}


PAGE['/regions/netherlands/'] = {
    'src': 'regions/netherlands/index.html',
    't': _merge(_BUILT_IN, _EXPLORE, _SEE_PRICING, _PRICE_NOTE, _SEPA, _GDPR, _LOCAL_HR_TITLE, {
        # ---- Meta (title == og:title; description == og:description) ----
        'HR Suite — HR &amp; payroll for Netherlands | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour les Pays-Bas | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für die Niederlande | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para los Países Bajos | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per i Paesi Bassi | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor Nederland | FulcrumGrid'),
        'HR Suite for the Netherlands — CBA overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.': _t(
            'HR Suite pour les Pays-Bas — heures supplémentaires CBA, fichiers de paie SEPA, droits GDPR, paie locale configurable en EUR, et RH complète.',
            'HR Suite für die Niederlande — CBA-Überstunden, SEPA-Zahlungsdateien, GDPR-Rechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige HR.',
            'HR Suite para los Países Bajos — horas extra según CBA, archivos de pago SEPA, derechos GDPR, nóminas locales configurables en EUR y RR. HH. completos.',
            'HR Suite per i Paesi Bassi — straordinari CBA, file di pagamento SEPA, diritti GDPR, buste paga locali configurabili in EUR e HR completa.',
            'HR Suite voor Nederland — CBA-overwerk, SEPA-betaalbestanden, GDPR-rechten, configureerbare lokale salarisadministratie in EUR, en volledige HR.'),
        # ---- Hero ----
        'Netherlands · NL': _t('Pays-Bas · NL', 'Niederlande · NL', 'Países Bajos · NL', 'Paesi Bassi · NL', 'Nederland · NL'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">the Netherlands</em>': _t(
            'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">les Pays-Bas</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">die Niederlande</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">los Países Bajos</em>',
            'HR &amp; buste paga, pensato per <em style="font-style:normal;color:var(--color-accent)">i Paesi Bassi</em>',
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Nederland</em>'),
        "HR Suite runs your Netherlands workforce — collective-agreement overtime, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.": _t(
            "HR Suite pilote vos effectifs aux Pays-Bas — heures supplémentaires prévues par la convention collective, fichiers de paie SEPA, droits des personnes concernées au titre du GDPR, paie locale configurable en EUR, et dossiers employés complets.",
            'HR Suite steuert Ihre Belegschaft in den Niederlanden — tarifvertragliche Überstunden, SEPA-Zahlungsdateien, GDPR-Betroffenenrechte, konfigurierbare lokale Gehaltsabrechnung in EUR und vollständige Mitarbeiterakten.',
            'HR Suite gestiona su plantilla en los Países Bajos — horas extra según convenio colectivo, archivos de pago SEPA, derechos del interesado del GDPR, nóminas locales configurables en EUR y expedientes de empleados completos.',
            "HR Suite gestisce il tuo organico nei Paesi Bassi — straordinari da contratto collettivo, file di pagamento SEPA, diritti dell'interessato GDPR, buste paga locali configurabili in EUR e schede dipendente complete.",
            'HR Suite runt uw personeelsbestand in Nederland — cao-overwerk, SEPA-betaalbestanden, GDPR-rechten van betrokkenen, configureerbare lokale salarisadministratie in EUR, en volledige personeelsdossiers.'),
        # ---- Sub-head ----
        'Netherlands compliance, out of the box': _t(
            "La conformité pour les Pays-Bas, prête à l'emploi",
            'Compliance für die Niederlande, sofort einsatzbereit',
            'Cumplimiento para los Países Bajos, listo para usar',
            "Conformità per i Paesi Bassi, pronta all'uso",
            'Compliance voor Nederland, kant-en-klaar'),
        'The modules that make HR Suite work the way Netherlands does — each part of the same grid, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière des Pays-Bas — chacun fait partie de la même grille, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie es die Niederlande tun — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hacen los Países Bajos — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            "I moduli che fanno funzionare HR Suite come fanno i Paesi Bassi — ognuno parte della stessa griglia, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Nederland dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards (Netherlands-specific) ----
        'Overtime — CBA rates': _t(
            'Heures supplémentaires — taux de la convention collective',
            'Überstunden — Tarifsätze',
            'Horas extra — tarifas del convenio colectivo',
            'Straordinari — tariffe del contratto collettivo',
            'Overwerk — cao-tarieven'),
        'Overtime at the customary 1.25× collective-agreement rate, configurable per agreement.': _t(
            'Heures supplémentaires au taux habituel de 1.25× prévu par la convention collective, configurable par convention.',
            'Überstunden zum üblichen Satz von 1.25× laut Tarifvertrag, konfigurierbar je Vertrag.',
            'Horas extra al tipo habitual de 1.25× del convenio colectivo, configurable por convenio.',
            'Straordinari alla tariffa abituale di 1.25× da contratto collettivo, configurabile per contratto.',
            'Overwerk tegen het gebruikelijke tarief van 1.25× volgens de cao, configureerbaar per cao.'),
        "Model Dutch income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.": _t(
            "Modélisez l'impôt sur le revenu et les cotisations sociales néerlandais sous forme de retenues configurables et classifiées — avec dossiers employés, intégration, congés et libre-service, en EUR.",
            'Bilden Sie niederländische Einkommensteuer und Sozialabgaben als konfigurierbare, klassifizierte Abzüge ab — mit Mitarbeiterakten, Onboarding, Abwesenheiten und Self-Service, in EUR.',
            'Modele el impuesto sobre la renta y las cotizaciones sociales neerlandeses como deducciones configurables y clasificadas — con expedientes de empleados, incorporación, ausencias y autoservicio, en EUR.',
            "Modella l'imposta sul reddito e i contributi previdenziali olandesi come trattenute configurabili e classificate — con schede dipendente, onboarding, ferie e self-service, in EUR.",
            'Modelleer de Nederlandse inkomstenbelasting en sociale premies als configureerbare, geclassificeerde inhoudingen — met personeelsdossiers, onboarding, verlof en selfservice, in EUR.'),
        # ---- CTA ----
        'Run Netherlands HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie aux Pays-Bas comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung in den Niederlanden richtig durch',
            'Gestione RR. HH. &amp; nóminas en los Países Bajos como es debido',
            'Gestisci HR &amp; buste paga nei Paesi Bassi nel modo giusto',
            'Voer HR &amp; salarisadministratie in Nederland op de juiste manier uit'),
        'See HR Suite handle Dutch overtime, SEPA and GDPR for your team.': _t(
            "Voyez HR Suite gérer les heures supplémentaires néerlandaises, SEPA et GDPR pour votre équipe.",
            'Sehen Sie, wie HR Suite niederländische Überstunden, SEPA und GDPR für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona las horas extra neerlandesas, SEPA y GDPR para su equipo.',
            'Guarda HR Suite gestire gli straordinari olandesi, SEPA e GDPR per il tuo team.',
            'Zie hoe HR Suite Nederlands overwerk, SEPA en GDPR voor uw team afhandelt.'),
    }),
}
