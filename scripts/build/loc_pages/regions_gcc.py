# -*- coding: utf-8 -*-
"""Translations for the REGION pages: the /regions/ hub and the GCC group.

Brand/product names (FulcrumGrid, HR Suite, Command Center, Collection),
statutory/technical proper nouns and acronyms (WPS, SIF, GOSI, EOSB, GPSSA,
GRSIA, MOHRE, Nitaqat, Saudization, Emiratization, Nafis, PIFSS, SIO, PASI,
Qatarization, Kuwaitization, Bahrainization, Omanization, Iqama, Emirates ID,
CPR), law citations and currency stay in English per the localization rules.
Country/region names are rendered in each language's natural form.

Keys are EXACT substrings of the committed English source (entities, dashes and
glyphs preserved). Common chrome (nav/footer/buttons, "Request a demo",
"Email us", "Regions" label) is handled by loc_catalog.COMMON and is not
repeated here. Because COMMON runs first and translates the bare word
"Regions" everywhere, the /regions/ <title> is keyed on its tail (the part
after "Regions"), which COMMON leaves untouched.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# ---------------------------------------------------------------------------
# Segments shared across several pages (defined once, reused below).
# ---------------------------------------------------------------------------

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

_HOME = {}

_BUILT_IN = {'Built in': _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd')}

_PRICE_NOTE = {
    'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on.': _t(
        "Chaque module présenté ici fait partie de HR Suite — paie avancée, clôture annuelle et conformité sur le plan Enterprise, ou en option par poste sur n'importe quel plan.",
        'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Zusatz pro Platz zu jedem Plan.',
        'Cada módulo aquí forma parte de HR Suite — nóminas avanzadas, cierre de año y cumplimiento en el plan Enterprise, o añadido a cualquier plan como complemento por usuario.',
        'Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura annuale e conformità nel piano Enterprise, oppure aggiunto a qualsiasi piano come componente aggiuntivo per postazione.',
        'Elke module hier maakt deel uit van HR Suite — geavanceerde salarisadministratie, jaarafsluiting en compliance in het Enterprise-plan, of toe te voegen aan elk plan als add-on per gebruiker.'),
}

# Feature title reused by UAE, Qatar and Oman.
_EOS_GRATUITY = {'End-of-service gratuity': _t(
    'Indemnité de fin de service', 'Abfindung zum Dienstende',
    'Gratificación por fin de servicio', 'Indennità di fine servizio',
    'Ontslagvergoeding')}

# Feature title reused by Kuwait and Bahrain.
_NAT_WORKFORCE = {'National-workforce tracking': _t(
    'Suivi des effectifs nationaux', 'Nachverfolgung der nationalen Belegschaft',
    'Seguimiento de la plantilla nacional', "Monitoraggio dell'organico nazionale",
    'Tracking van het nationale personeelsbestand')}

_ARABIC_DOCS = {'Arabic &amp; documents': _t(
    'Arabe &amp; documents', 'Arabisch &amp; Dokumente', 'Árabe &amp; documentos',
    'Arabo &amp; documenti', 'Arabisch &amp; documenten')}

# "Payroll + WPS" feature title reused by Qatar, Kuwait, Bahrain, Oman.
_PAYROLL_WPS = {'Payroll + WPS': _t(
    'Paie + WPS', 'Gehaltsabrechnung + WPS', 'Nóminas + WPS',
    'Buste paga + WPS', 'Salarisadministratie + WPS')}

# First feature paragraph, identical on Qatar, Kuwait, Bahrain, Oman.
_PAYRUN_WPS_FILE = {
    'Run compliant pay runs and export the Wage Protection System (WPS) file, so salaries clear through the mandated channel and payment is on record.': _t(
        'Exécutez des cycles de paie conformes et exportez le fichier du Wage Protection System (WPS), afin que les salaires transitent par le canal imposé et que le paiement soit consigné.',
        'Führen Sie konforme Gehaltsläufe durch und exportieren Sie die Datei des Wage Protection System (WPS), damit Gehälter über den vorgeschriebenen Kanal laufen und die Zahlung dokumentiert ist.',
        'Ejecute procesos de nómina conformes y exporte el archivo del Wage Protection System (WPS), para que los salarios se abonen por el canal exigido y el pago quede registrado.',
        'Esegui cicli di paga conformi ed esporta il file del Wage Protection System (WPS), così gli stipendi passano attraverso il canale previsto e il pagamento è documentato.',
        'Voer conforme salarisruns uit en exporteer het bestand van het Wage Protection System (WPS), zodat salarissen via het voorgeschreven kanaal worden verwerkt en betaling is vastgelegd.'),
}


def _merge(*dicts):
    out = {}
    for d in dicts:
        out.update(d)
    return out


PAGE = {}


PAGE['/regions/'] = {
    'src': 'regions/index.html',
    't': _merge(_HOME, {
        # ---- Meta (title tail; COMMON translates the leading "Regions") ----
        ' — every app, built for your region | FulcrumGrid': _t(
            ' — chaque application, conçue pour votre région | FulcrumGrid',
            ' — jede App, gebaut für Ihre Region | FulcrumGrid',
            ' — cada app, diseñada para su región | FulcrumGrid',
            ' — ogni app, costruita per la tua regione | FulcrumGrid',
            ' — elke app, gebouwd voor uw regio | FulcrumGrid'),
        'FulcrumGrid runs in your region — HR Suite, Command Center and Collection, adapted to local payroll, compliance, finance, currency and language.': _t(
            'FulcrumGrid fonctionne dans votre région — HR Suite, Command Center et Collection, adaptés à la paie, la conformité, la finance, la devise et la langue locales.',
            'FulcrumGrid läuft in Ihrer Region — HR Suite, Command Center und Collection, angepasst an lokale Gehaltsabrechnung, Compliance, Finanzen, Währung und Sprache.',
            'FulcrumGrid funciona en su región — HR Suite, Command Center y Collection, adaptados a la nómina, el cumplimiento, las finanzas, la moneda y el idioma locales.',
            'FulcrumGrid funziona nella tua regione — HR Suite, Command Center e Collection, adattati a buste paga, conformità, finanza, valuta e lingua locali.',
            'FulcrumGrid draait in uw regio — HR Suite, Command Center en Collection, aangepast aan lokale salarisadministratie, compliance, financiën, valuta en taal.'),
        # ---- Hero ----
        'Built for how your <em style="font-style:normal;color:var(--color-accent)">region runs</em>': _t(
            'Conçu pour le fonctionnement de <em style="font-style:normal;color:var(--color-accent)">votre région</em>',
            'Gebaut für die Arbeitsweise <em style="font-style:normal;color:var(--color-accent)">Ihrer Region</em>',
            'Diseñado para cómo opera <em style="font-style:normal;color:var(--color-accent)">su región</em>',
            'Pensato per come lavora <em style="font-style:normal;color:var(--color-accent)">la tua regione</em>',
            'Gebouwd voor hoe <em style="font-style:normal;color:var(--color-accent)">uw regio</em> werkt'),
        'The whole grid runs in your region — HR Suite for local payroll and compliance, Command Center for regional finance and tax, and Collection for local receivables — in your language and currency. Wherever you operate, your data runs on servers hosted in your region. Choose your region.': _t(
            "Toute la grille fonctionne dans votre région — HR Suite pour la paie et la conformité locales, Command Center pour la finance et la fiscalité régionales, et Collection pour le recouvrement local — dans votre langue et votre devise. Où que vous opériez, vos données s'exécutent sur des serveurs hébergés dans votre région. Choisissez votre région.",
            'Das gesamte Grid läuft in Ihrer Region — HR Suite für lokale Gehaltsabrechnung und Compliance, Command Center für regionale Finanzen und Steuern und Collection für lokalen Forderungseinzug — in Ihrer Sprache und Währung. Wo immer Sie tätig sind, laufen Ihre Daten auf Servern, die in Ihrer Region gehostet werden. Wählen Sie Ihre Region.',
            'Toda la cuadrícula funciona en su región — HR Suite para la nómina y el cumplimiento locales, Command Center para las finanzas y los impuestos regionales, y Collection para el cobro local — en su idioma y moneda. Opere donde opere, sus datos se ejecutan en servidores alojados en su región. Elija su región.',
            'Tutta la griglia funziona nella tua regione — HR Suite per buste paga e conformità locali, Command Center per finanza e fiscalità regionali e Collection per il recupero crediti locale — nella tua lingua e valuta. Ovunque operi, i tuoi dati vengono eseguiti su server ospitati nella tua regione. Scegli la tua regione.',
            'Het hele grid draait in uw regio — HR Suite voor lokale salarisadministratie en compliance, Command Center voor regionale financiën en belasting, en Collection voor lokale debiteuren — in uw taal en valuta. Waar u ook actief bent, uw gegevens draaien op servers die in uw regio worden gehost. Kies uw regio.'),
        'Choose your region.': _t(
            'Choisissez votre région.',
            'Wählen Sie Ihre Region.',
            'Elija su región.',
            'Scegli la tua regione.',
            'Kies uw regio.'),
        # ---- Cross-grid: region names ----
        '<h4>North America</h4>': _t('<h4>Amérique du Nord</h4>', '<h4>Nordamerika</h4>', '<h4>América del Norte</h4>', '<h4>Nord America</h4>', '<h4>Noord-Amerika</h4>'),
        '<h4>Europe</h4>': _t('<h4>Europe</h4>', '<h4>Europa</h4>', '<h4>Europa</h4>', '<h4>Europa</h4>', '<h4>Europa</h4>'),
        '<h4>Middle East</h4>': _t('<h4>Moyen-Orient</h4>', '<h4>Naher Osten</h4>', '<h4>Oriente Medio</h4>', '<h4>Medio Oriente</h4>', '<h4>Midden-Oosten</h4>'),
        '<h4>More markets</h4>': _t('<h4>Autres marchés</h4>', '<h4>Weitere Märkte</h4>', '<h4>Más mercados</h4>', '<h4>Altri mercati</h4>', '<h4>Meer markten</h4>'),
        # ---- Cross-grid: served lists ----
        'United States · Canada': _t('États-Unis · Canada', 'Vereinigte Staaten · Kanada', 'Estados Unidos · Canadá', 'Stati Uniti · Canada', 'Verenigde Staten · Canada'),
        'UK · Ireland · France · Germany · Spain · Italy · NL': _t(
            'UK · Irlande · France · Allemagne · Espagne · Italie · NL',
            'UK · Irland · Frankreich · Deutschland · Spanien · Italien · NL',
            'UK · Irlanda · Francia · Alemania · España · Italia · NL',
            'UK · Irlanda · Francia · Germania · Spagna · Italia · NL',
            'VK · Ierland · Frankrijk · Duitsland · Spanje · Italië · NL'),
        'Saudi · UAE · Qatar · Kuwait · Bahrain · Oman': _t(
            'Arabie saoudite · EAU · Qatar · Koweït · Bahreïn · Oman',
            'Saudi-Arabien · VAE · Katar · Kuwait · Bahrain · Oman',
            'Arabia Saudí · EAU · Catar · Kuwait · Baréin · Omán',
            'Arabia Saudita · EAU · Qatar · Kuwait · Bahrein · Oman',
            'Saoedi-Arabië · VAE · Qatar · Koeweit · Bahrein · Oman'),
        'Egypt · Jordan · Lebanon · Iraq · Palestine · Syria · Yemen': _t(
            'Égypte · Jordanie · Liban · Irak · Palestine · Syrie · Yémen',
            'Ägypten · Jordanien · Libanon · Irak · Palästina · Syrien · Jemen',
            'Egipto · Jordania · Líbano · Irak · Palestina · Siria · Yemen',
            'Egitto · Giordania · Libano · Iraq · Palestina · Siria · Yemen',
            'Egypte · Jordanië · Libanon · Irak · Palestina · Syrië · Jemen'),
        'Elsewhere — on request': _t('Ailleurs — sur demande', 'Anderswo — auf Anfrage', 'En otros lugares — a petición', 'Altrove — su richiesta', 'Elders — op aanvraag'),
        # ---- CTA ----
        'Not sure your region is covered?': _t(
            'Vous ne savez pas si votre région est couverte ?',
            'Nicht sicher, ob Ihre Region abgedeckt ist?',
            '¿No sabe si su región está cubierta?',
            'Non sai se la tua regione è coperta?',
            'Weet u niet zeker of uw regio wordt gedekt?'),
    }),
}


PAGE['/regions/gcc/'] = {
    'src': 'regions/gcc/index.html',
    't': _merge(_HOME, {
        # ---- Meta ----
        'FulcrumGrid in GCC — every app, built for your region | FulcrumGrid': _t(
            'FulcrumGrid dans le GCC — chaque application, conçue pour votre région | FulcrumGrid',
            'FulcrumGrid im GCC — jede App, gebaut für Ihre Region | FulcrumGrid',
            'FulcrumGrid en el GCC — cada app, diseñada para su región | FulcrumGrid',
            'FulcrumGrid nel GCC — ogni app, costruita per la tua regione | FulcrumGrid',
            'FulcrumGrid in de GCC — elke app, gebouwd voor uw regio | FulcrumGrid'),
        'FulcrumGrid across the GCC — HR Suite, Command Center and Collection — with WPS payroll, statutory end-of-service and Arabic, plus GCC-native finance and Tax and Zakat, per country.': _t(
            'FulcrumGrid dans tout le GCC — HR Suite, Command Center et Collection — avec paie WPS, fin de service légale et arabe, plus une finance native du GCC et taxe et Zakat, par pays.',
            'FulcrumGrid im gesamten GCC — HR Suite, Command Center und Collection — mit WPS-Gehaltsabrechnung, gesetzlichem Dienstende und Arabisch, dazu GCC-native Finanzverwaltung sowie Steuer und Zakat, pro Land.',
            'FulcrumGrid en todo el GCC — HR Suite, Command Center y Collection — con nóminas WPS, fin de servicio obligatorio y árabe, además de finanzas nativas del GCC e impuesto y Zakat, por país.',
            'FulcrumGrid in tutto il GCC — HR Suite, Command Center e Collection — con buste paga WPS, fine servizio di legge e arabo, oltre a finanza nativa del GCC e imposta e Zakat, per Paese.',
            'FulcrumGrid in de hele GCC — HR Suite, Command Center en Collection — met WPS-salarisadministratie, wettelijk einde dienstverband en Arabisch, plus GCC-native financiën en belasting en Zakat, per land.'),
        # ---- Hero ----
        'Gulf Cooperation Council · GCC': _t(
            'Conseil de coopération du Golfe · GCC', 'Golf-Kooperationsrat · GCC',
            'Consejo de Cooperación del Golfo · GCC', 'Consiglio di cooperazione del Golfo · GCC',
            'Samenwerkingsraad van de Golf · GCC'),
        'KSA': _t('KSA', 'KSA', 'KSA', 'KSA', 'KSA'),
        'FulcrumGrid, built for <em style="font-style:normal;color:var(--color-accent)">the Gulf</em>': _t(
            'FulcrumGrid, conçu pour <em style="font-style:normal;color:var(--color-accent)">le Golfe</em>',
            'FulcrumGrid, entwickelt für <em style="font-style:normal;color:var(--color-accent)">die Golfregion</em>',
            'FulcrumGrid, diseñado para <em style="font-style:normal;color:var(--color-accent)">el Golfo</em>',
            'FulcrumGrid, pensato per <em style="font-style:normal;color:var(--color-accent)">il Golfo</em>',
            'FulcrumGrid, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">de Golfregio</em>'),
        'The whole grid runs in the Gulf — HR Suite with WPS payroll, end-of-service and Arabic throughout; Command Center with GCC-native finance, Tax and Zakat and multi-currency; and Collection for local receivables. Pick a country for the detail.': _t(
            "Toute la grille fonctionne dans le Golfe — HR Suite avec paie WPS, fin de service et arabe partout ; Command Center avec une finance native du GCC, taxe et Zakat et multidevise ; et Collection pour le recouvrement local. Choisissez un pays pour le détail.",
            'Das gesamte Grid läuft am Golf — HR Suite mit WPS-Gehaltsabrechnung, Dienstende und durchgehend Arabisch; Command Center mit GCC-nativer Finanzverwaltung, Steuer und Zakat und Mehrwährung; und Collection für lokalen Forderungseinzug. Wählen Sie ein Land für die Details.',
            'Toda la cuadrícula funciona en el Golfo — HR Suite con nóminas WPS, fin de servicio y árabe en todo momento; Command Center con finanzas nativas del GCC, impuesto y Zakat y multidivisa; y Collection para el cobro local. Elija un país para ver el detalle.',
            "Tutta la griglia funziona nel Golfo — HR Suite con buste paga WPS, fine servizio e arabo ovunque; Command Center con finanza nativa del GCC, imposta e Zakat e multivaluta; e Collection per il recupero crediti locale. Scegli un Paese per il dettaglio.",
            'Het hele grid draait in de Golf — HR Suite met WPS-salarisadministratie, einde dienstverband en Arabisch overal; Command Center met GCC-native financiën, belasting en Zakat en meerdere valuta; en Collection voor lokale debiteuren. Kies een land voor de details.'),
        # ---- Sub-head ----
        'Countries': _t('Pays', 'Länder', 'Países', 'Paesi', 'Landen'),
        'Countries in this region': _t('Pays de cette région', 'Länder in dieser Region', 'Países de esta región', 'Paesi di questa regione', 'Landen in deze regio'),
        'Pick a country for its statutory payroll and compliance detail — and it runs across the wider region too.': _t(
            "Choisissez un pays pour le détail de sa paie légale et de sa conformité — et cela fonctionne aussi dans l'ensemble de la région.",
            'Wählen Sie ein Land für die Details seiner gesetzlichen Gehaltsabrechnung und Compliance — und es funktioniert auch in der gesamten Region.',
            'Elija un país para ver el detalle de su nómina obligatoria y su cumplimiento — y también funciona en toda la región.',
            "Scegli un Paese per il dettaglio delle sue buste paga di legge e della conformità — e funziona anche nell'intera regione.",
            'Kies een land voor de details van de wettelijke salarisadministratie en compliance — en het werkt ook in de bredere regio.'),
        # ---- Country cross-grid: names ----
        '<h4>Saudi Arabia</h4>': _t('<h4>Arabie saoudite</h4>', '<h4>Saudi-Arabien</h4>', '<h4>Arabia Saudí</h4>', '<h4>Arabia Saudita</h4>', '<h4>Saoedi-Arabië</h4>'),
        '<h4>UAE</h4>': _t('<h4>EAU</h4>', '<h4>VAE</h4>', '<h4>EAU</h4>', '<h4>EAU</h4>', '<h4>VAE</h4>'),
        '<h4>Qatar</h4>': _t('<h4>Qatar</h4>', '<h4>Katar</h4>', '<h4>Catar</h4>', '<h4>Qatar</h4>', '<h4>Qatar</h4>'),
        '<h4>Kuwait</h4>': _t('<h4>Koweït</h4>', '<h4>Kuwait</h4>', '<h4>Kuwait</h4>', '<h4>Kuwait</h4>', '<h4>Koeweit</h4>'),
        '<h4>Bahrain</h4>': _t('<h4>Bahreïn</h4>', '<h4>Bahrain</h4>', '<h4>Baréin</h4>', '<h4>Bahrein</h4>', '<h4>Bahrein</h4>'),
        '<h4>Oman</h4>': _t('<h4>Oman</h4>', '<h4>Oman</h4>', '<h4>Omán</h4>', '<h4>Oman</h4>', '<h4>Oman</h4>'),
        # ---- Country cross-grid: served lists (proper nouns kept) ----
        'WPS · gratuity · GOSI · Nitaqat': _t('WPS · indemnité · GOSI · Nitaqat', 'WPS · Abfindung · GOSI · Nitaqat', 'WPS · gratificación · GOSI · Nitaqat', 'WPS · indennità · GOSI · Nitaqat', 'WPS · ontslagvergoeding · GOSI · Nitaqat'),
        'WPS · gratuity · GPSSA · Emiratization': _t('WPS · indemnité · GPSSA · Emiratization', 'WPS · Abfindung · GPSSA · Emiratization', 'WPS · gratificación · GPSSA · Emiratization', 'WPS · indennità · GPSSA · Emiratization', 'WPS · ontslagvergoeding · GPSSA · Emiratization'),
        'WPS · gratuity · pensions · Qatarization': _t('WPS · indemnité · retraites · Qatarization', 'WPS · Abfindung · Renten · Qatarization', 'WPS · gratificación · pensiones · Qatarization', 'WPS · indennità · pensioni · Qatarization', 'WPS · ontslagvergoeding · pensioenen · Qatarization'),
        'WPS · indemnity · PIFSS · Kuwaitization': _t('WPS · indemnité · PIFSS · Kuwaitization', 'WPS · Abfindung · PIFSS · Kuwaitization', 'WPS · indemnización · PIFSS · Kuwaitization', 'WPS · indennità · PIFSS · Kuwaitization', 'WPS · ontslagvergoeding · PIFSS · Kuwaitization'),
        'WPS · indemnity · SIO · Bahrainization': _t('WPS · indemnité · SIO · Bahrainization', 'WPS · Abfindung · SIO · Bahrainization', 'WPS · indemnización · SIO · Bahrainization', 'WPS · indennità · SIO · Bahrainization', 'WPS · ontslagvergoeding · SIO · Bahrainization'),
        'WPS · gratuity · social protection · Omanization': _t('WPS · indemnité · protection sociale · Omanization', 'WPS · Abfindung · Sozialschutz · Omanization', 'WPS · gratificación · protección social · Omanization', 'WPS · indennità · protezione sociale · Omanization', 'WPS · ontslagvergoeding · sociale bescherming · Omanization'),
        # ---- CTA ----
        'Run your Gulf operation on one grid': _t(
            'Gérez votre activité dans le Golfe sur une seule grille',
            'Führen Sie Ihren Betrieb am Golf auf einem Grid',
            'Gestione su operación del Golfo en una sola cuadrícula',
            "Gestisci la tua attività nel Golfo su un'unica griglia",
            'Run uw activiteiten in de Golf op één grid'),
    }),
}


PAGE['/regions/saudi-arabia/'] = {
    'src': 'regions/saudi-arabia/index.html',
    't': _merge(_HOME, _EXPLORE, _SEE_PRICING, _BUILT_IN, _ARABIC_DOCS, _PRICE_NOTE, {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for Saudi Arabia | FulcrumGrid': _t(
            "HR Suite — RH &amp; paie pour l'Arabie saoudite | FulcrumGrid",
            'HR Suite — HR &amp; Gehaltsabrechnung für Saudi-Arabien | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Arabia Saudí | FulcrumGrid',
            "HR Suite — HR &amp; buste paga per l'Arabia Saudita | FulcrumGrid",
            'HR Suite — HR &amp; salarisadministratie voor Saoedi-Arabië | FulcrumGrid'),
        'HR Suite for Saudi Arabia — WPS wage-protection files, GOSI, end-of-service (EOSB), Nitaqat and Saudization, housing advance, and Arabic-first payroll and HR.': _t(
            "HR Suite pour l'Arabie saoudite — fichiers de protection des salaires WPS, GOSI, fin de service (EOSB), Nitaqat et Saudization, avance logement, et paie et RH en priorité arabe.",
            'HR Suite für Saudi-Arabien — WPS-Lohnschutzdateien, GOSI, Dienstende (EOSB), Nitaqat und Saudization, Wohnungsvorschuss sowie Arabisch-First-Gehaltsabrechnung und HR.',
            'HR Suite para Arabia Saudí — archivos de protección salarial WPS, GOSI, fin de servicio (EOSB), Nitaqat y Saudization, anticipo de vivienda, y nóminas y RR. HH. con árabe primero.',
            "HR Suite per l'Arabia Saudita — file di protezione salariale WPS, GOSI, fine servizio (EOSB), Nitaqat e Saudization, anticipo alloggio, e buste paga e HR in arabo prima di tutto.",
            'HR Suite voor Saoedi-Arabië — WPS-loonbeschermingsbestanden, GOSI, einde dienstverband (EOSB), Nitaqat en Saudization, huisvestingsvoorschot, en salarisadministratie en HR met Arabisch voorop.'),
        # ---- Hero ----
        'Saudi Arabia · KSA': _t('Arabie saoudite · KSA', 'Saudi-Arabien · KSA', 'Arabia Saudí · KSA', 'Arabia Saudita · KSA', 'Saoedi-Arabië · KSA'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Saudi Arabia</em>': _t(
            "RH &amp; paie, conçu pour <em style=\"font-style:normal;color:var(--color-accent)\">l'Arabie saoudite</em>",
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Saudi-Arabien</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">Arabia Saudí</em>',
            "HR &amp; buste paga, pensato per <em style=\"font-style:normal;color:var(--color-accent)\">l'Arabia Saudita</em>",
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Saoedi-Arabië</em>'),
        'HR Suite ships with Saudi payroll and compliance built in — WPS wage files, GOSI, end-of-service, Nitaqat and Saudization, with Arabic throughout. Run your Saudi workforce by the book, without bolt-ons.': _t(
            "HR Suite intègre nativement la paie et la conformité saoudiennes — fichiers de salaires WPS, GOSI, fin de service, Nitaqat et Saudization, avec l'arabe partout. Gérez vos effectifs saoudiens dans les règles, sans modules externes.",
            'HR Suite bringt saudische Gehaltsabrechnung und Compliance von Haus aus mit — WPS-Lohndateien, GOSI, Dienstende, Nitaqat und Saudization, durchgehend auf Arabisch. Führen Sie Ihre saudische Belegschaft vorschriftsgemäß, ohne Zusatzmodule.',
            'HR Suite incorpora de serie la nómina y el cumplimiento saudíes — archivos de salarios WPS, GOSI, fin de servicio, Nitaqat y Saudization, con árabe en todo momento. Gestione su plantilla saudí conforme a la norma, sin complementos.',
            "HR Suite integra nativamente buste paga e conformità saudite — file salariali WPS, GOSI, fine servizio, Nitaqat e Saudization, con l'arabo ovunque. Gestisci il tuo organico saudita a norma, senza componenti aggiuntivi.",
            'HR Suite heeft Saoedische salarisadministratie en compliance standaard ingebouwd — WPS-loonbestanden, GOSI, einde dienstverband, Nitaqat en Saudization, met Arabisch overal. Beheer uw Saoedische personeelsbestand volgens de regels, zonder extra modules.'),
        # ---- Sub-head ----
        'Saudi Arabia compliance, out of the box': _t(
            "La conformité pour l'Arabie saoudite, prête à l'emploi",
            'Compliance für Saudi-Arabien, sofort einsatzbereit',
            'Cumplimiento para Arabia Saudí, listo para usar',
            "Conformità per l'Arabia Saudita, pronta all'uso",
            'Compliance voor Saoedi-Arabië, kant-en-klaar'),
        'The modules that make HR Suite work the way Saudi Arabia does — each part of the same grid, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière de l'Arabie saoudite — chacun fait partie de la même grille, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie es Saudi-Arabien tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Arabia Saudí — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            "I moduli che fanno funzionare HR Suite come fa l'Arabia Saudita — ognuno parte della stessa griglia, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Saoedi-Arabië dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards ----
        'Payroll + WPS wage files': _t('Paie + fichiers de salaires WPS', 'Gehaltsabrechnung + WPS-Lohndateien', 'Nóminas + archivos de salarios WPS', 'Buste paga + file salariali WPS', 'Salarisadministratie + WPS-loonbestanden'),
        'Run compliant pay runs and export the Wage Protection System (WPS) bank file in the mandated format, so salaries clear through the right channels and on-time payment is on record.': _t(
            'Exécutez des cycles de paie conformes et exportez le fichier bancaire du Wage Protection System (WPS) au format imposé, afin que les salaires transitent par les bons canaux et que le paiement à temps soit consigné.',
            'Führen Sie konforme Gehaltsläufe durch und exportieren Sie die Bankdatei des Wage Protection System (WPS) im vorgeschriebenen Format, damit Gehälter über die richtigen Kanäle laufen und die pünktliche Zahlung dokumentiert ist.',
            'Ejecute procesos de nómina conformes y exporte el archivo bancario del Wage Protection System (WPS) en el formato exigido, para que los salarios se abonen por los canales correctos y el pago puntual quede registrado.',
            'Esegui cicli di paga conformi ed esporta il file bancario del Wage Protection System (WPS) nel formato previsto, così gli stipendi passano attraverso i canali giusti e il pagamento puntuale è documentato.',
            'Voer conforme salarisruns uit en exporteer het bankbestand van het Wage Protection System (WPS) in het voorgeschreven formaat, zodat salarissen via de juiste kanalen worden verwerkt en tijdige betaling is vastgelegd.'),
        'GOSI contributions': _t('Cotisations GOSI', 'GOSI-Beiträge', 'Cotizaciones GOSI', 'Contributi GOSI', 'GOSI-bijdragen'),
        'GOSI (General Organization for Social Insurance) contributions are calculated automatically for Saudi and non-Saudi employees and wired straight into every pay run.': _t(
            'Les cotisations GOSI (General Organization for Social Insurance) sont calculées automatiquement pour les employés saoudiens et non saoudiens et intégrées directement à chaque cycle de paie.',
            'GOSI-Beiträge (General Organization for Social Insurance) werden für saudische und nicht-saudische Mitarbeiter automatisch berechnet und direkt in jeden Gehaltslauf eingebunden.',
            'Las cotizaciones a GOSI (General Organization for Social Insurance) se calculan automáticamente para empleados saudíes y no saudíes y se integran directamente en cada proceso de nómina.',
            'I contributi GOSI (General Organization for Social Insurance) sono calcolati automaticamente per i dipendenti sauditi e non sauditi e integrati direttamente in ogni ciclo di paga.',
            'GOSI-bijdragen (General Organization for Social Insurance) worden automatisch berekend voor Saoedische en niet-Saoedische werknemers en rechtstreeks in elke salarisrun verwerkt.'),
        'End-of-service (EOSB)': _t('Fin de service (EOSB)', 'Dienstende (EOSB)', 'Fin de servicio (EOSB)', 'Fine servizio (EOSB)', 'Einde dienstverband (EOSB)'),
        "End-of-service benefits computed to the Saudi Labor Law (art. 84) — half a month's wage per year for the first five years, a full month per year thereafter — with resignation and termination handled distinctly.": _t(
            'Indemnités de fin de service calculées selon la Saudi Labor Law (art. 84) — un demi-mois de salaire par an pour les cinq premières années, puis un mois entier par an — la démission et le licenciement étant traités distinctement.',
            'Leistungen zum Dienstende berechnet nach der Saudi Labor Law (art. 84) — ein halbes Monatsgehalt pro Jahr für die ersten fünf Jahre, danach ein volles Monatsgehalt pro Jahr — wobei Kündigung und Entlassung getrennt behandelt werden.',
            'Prestaciones de fin de servicio calculadas conforme a la Saudi Labor Law (art. 84) — medio mes de salario por año durante los primeros cinco años y un mes completo por año a partir de entonces — con la dimisión y el despido tratados por separado.',
            'Prestazioni di fine servizio calcolate secondo la Saudi Labor Law (art. 84) — mezzo mese di stipendio all\'anno per i primi cinque anni, poi un mese intero all\'anno — con dimissioni e licenziamento gestiti distintamente.',
            'Eindedienstuitkeringen berekend volgens de Saudi Labor Law (art. 84) — een half maandsalaris per jaar voor de eerste vijf jaar, daarna een volledige maand per jaar — waarbij ontslagname en ontslag apart worden behandeld.'),
        'Nitaqat &amp; Saudization': _t('Nitaqat &amp; Saudization', 'Nitaqat &amp; Saudization', 'Nitaqat &amp; Saudization', 'Nitaqat &amp; Saudization', 'Nitaqat &amp; Saudization'),
        'Track your Saudization ratio and Nitaqat band in the analytics dashboard, so you know where you stand before it becomes a compliance issue.': _t(
            'Suivez votre ratio de Saudization et votre bande Nitaqat dans le tableau de bord analytique, afin de savoir où vous en êtes avant que cela ne devienne un problème de conformité.',
            'Verfolgen Sie Ihre Saudization-Quote und Ihr Nitaqat-Band im Analyse-Dashboard, damit Sie wissen, wo Sie stehen, bevor es zu einem Compliance-Problem wird.',
            'Haga seguimiento de su ratio de Saudization y de su banda Nitaqat en el panel de analítica, para saber dónde se encuentra antes de que se convierta en un problema de cumplimiento.',
            'Monitora il tuo rapporto di Saudization e la tua fascia Nitaqat nella dashboard di analisi, così sai a che punto sei prima che diventi un problema di conformità.',
            'Volg uw Saudization-ratio en uw Nitaqat-band in het analysedashboard, zodat u weet waar u staat voordat het een compliance-probleem wordt.'),
        'Housing advance': _t('Avance logement', 'Wohnungsvorschuss', 'Anticipo de vivienda', 'Anticipo alloggio', 'Huisvestingsvoorschot'),
        'Interest-free housing advances with structured repayment, matching the way Saudi employment packages are commonly built.': _t(
            "Avances logement sans intérêt avec remboursement structuré, à l'image de la composition habituelle des packages d'emploi saoudiens.",
            'Zinslose Wohnungsvorschüsse mit strukturierter Rückzahlung, passend zur üblichen Gestaltung saudischer Vergütungspakete.',
            'Anticipos de vivienda sin intereses con reembolso estructurado, acordes con la forma habitual en que se componen los paquetes de empleo saudíes.',
            'Anticipi alloggio senza interessi con rimborso strutturato, in linea con il modo in cui sono comunemente strutturati i pacchetti retributivi sauditi.',
            'Renteloze huisvestingsvoorschotten met gestructureerde terugbetaling, passend bij de manier waarop Saoedische arbeidsvoorwaardenpakketten doorgaans zijn opgebouwd.'),
        "Arabic-first, right-to-left interface throughout, bilingual HR letters and contracts, and Iqama and permit expiry tracking so nothing lapses.": _t(
            "Interface en priorité arabe, de droite à gauche partout, lettres RH et contrats bilingues, et suivi de l'expiration de l'Iqama et des permis pour que rien n'expire.",
            'Durchgehend Arabisch-First-Oberfläche von rechts nach links, zweisprachige HR-Schreiben und Verträge sowie Nachverfolgung des Ablaufs von Iqama und Genehmigungen, damit nichts verfällt.',
            'Interfaz con árabe primero, de derecha a izquierda en todo momento, cartas de RR. HH. y contratos bilingües, y seguimiento del vencimiento de la Iqama y los permisos para que nada caduque.',
            'Interfaccia in arabo prima di tutto, da destra a sinistra ovunque, lettere HR e contratti bilingui e monitoraggio della scadenza di Iqama e permessi, così nulla scade.',
            'Interface met Arabisch voorop, overal van rechts naar links, tweetalige HR-brieven en contracten, en tracking van het verlopen van Iqama en vergunningen zodat niets verloopt.'),
        # ---- CTA ----
        'Run Saudi HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie saoudiennes comme il se doit',
            'Führen Sie saudische HR &amp; Gehaltsabrechnung richtig durch',
            'Gestione RR. HH. &amp; nóminas saudíes como es debido',
            'Gestisci HR &amp; buste paga saudite nel modo giusto',
            'Voer Saoedische HR &amp; salarisadministratie op de juiste manier uit'),
        'See HR Suite handle Saudi payroll, GOSI, and end-of-service for your team.': _t(
            'Voyez HR Suite gérer la paie saoudienne, le GOSI et la fin de service pour votre équipe.',
            'Sehen Sie, wie HR Suite saudische Gehaltsabrechnung, GOSI und Dienstende für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona la nómina saudí, el GOSI y el fin de servicio para su equipo.',
            'Guarda HR Suite gestire buste paga saudite, GOSI e fine servizio per il tuo team.',
            'Zie hoe HR Suite Saoedische salarisadministratie, GOSI en einde dienstverband voor uw team afhandelt.'),
    }),
}


PAGE['/regions/uae/'] = {
    'src': 'regions/uae/index.html',
    't': _merge(_HOME, _EXPLORE, _SEE_PRICING, _BUILT_IN, _ARABIC_DOCS, _PRICE_NOTE, _EOS_GRATUITY, {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for UAE | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour les EAU | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für die VAE | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para los EAU | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per gli EAU | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor de VAE | FulcrumGrid'),
        'HR Suite for the UAE — MOHRE payroll and WPS salary files, gratuity under Federal Decree-Law 33/2021, GPSSA pensions, Emiratization (Nafis) tracking, and Arabic-first HR.': _t(
            "HR Suite pour les EAU — paie MOHRE et fichiers de salaires WPS, indemnité au titre du Federal Decree-Law 33/2021, retraites GPSSA, suivi de l'Emiratization (Nafis), et RH en priorité arabe.",
            'HR Suite für die VAE — MOHRE-Gehaltsabrechnung und WPS-Gehaltsdateien, Abfindung gemäß Federal Decree-Law 33/2021, GPSSA-Renten, Emiratization-(Nafis-)Nachverfolgung und Arabisch-First-HR.',
            'HR Suite para los EAU — nóminas MOHRE y archivos salariales WPS, gratificación conforme al Federal Decree-Law 33/2021, pensiones GPSSA, seguimiento de Emiratization (Nafis) y RR. HH. con árabe primero.',
            "HR Suite per gli EAU — buste paga MOHRE e file salariali WPS, indennità ai sensi del Federal Decree-Law 33/2021, pensioni GPSSA, monitoraggio dell'Emiratization (Nafis) e HR in arabo prima di tutto.",
            'HR Suite voor de VAE — MOHRE-salarisadministratie en WPS-salarisbestanden, ontslagvergoeding onder Federal Decree-Law 33/2021, GPSSA-pensioenen, tracking van Emiratization (Nafis) en HR met Arabisch voorop.'),
        # ---- Hero ----
        'United Arab Emirates · UAE': _t('Émirats arabes unis · EAU', 'Vereinigte Arabische Emirate · VAE', 'Emiratos Árabes Unidos · EAU', 'Emirati Arabi Uniti · EAU', 'Verenigde Arabische Emiraten · VAE'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">the UAE</em>': _t(
            'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">les EAU</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">die VAE</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">los EAU</em>',
            'HR &amp; buste paga, pensato per <em style="font-style:normal;color:var(--color-accent)">gli EAU</em>',
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">de VAE</em>'),
        'HR Suite runs your UAE workforce end to end — MOHRE-compliant payroll and WPS salary files, gratuity to Federal Decree-Law 33/2021, pension and Emiratization tracking, and Arabic throughout.': _t(
            "HR Suite gère vos effectifs aux EAU de bout en bout — paie conforme MOHRE et fichiers de salaires WPS, indemnité selon le Federal Decree-Law 33/2021, suivi des retraites et de l'Emiratization, avec l'arabe partout.",
            'HR Suite steuert Ihre Belegschaft in den VAE durchgängig — MOHRE-konforme Gehaltsabrechnung und WPS-Gehaltsdateien, Abfindung gemäß Federal Decree-Law 33/2021, Renten- und Emiratization-Nachverfolgung, durchgehend auf Arabisch.',
            'HR Suite gestiona su plantilla en los EAU de principio a fin — nóminas conformes con MOHRE y archivos salariales WPS, gratificación según el Federal Decree-Law 33/2021, seguimiento de pensiones y Emiratization, con árabe en todo momento.',
            "HR Suite gestisce il tuo organico negli EAU end to end — buste paga conformi a MOHRE e file salariali WPS, indennità secondo il Federal Decree-Law 33/2021, monitoraggio di pensioni ed Emiratization, con l'arabo ovunque.",
            'HR Suite beheert uw personeelsbestand in de VAE van begin tot eind — MOHRE-conforme salarisadministratie en WPS-salarisbestanden, ontslagvergoeding volgens Federal Decree-Law 33/2021, tracking van pensioen en Emiratization, met Arabisch overal.'),
        # ---- Sub-head ----
        'UAE compliance, out of the box': _t(
            "La conformité pour les EAU, prête à l'emploi",
            'Compliance für die VAE, sofort einsatzbereit',
            'Cumplimiento para los EAU, listo para usar',
            "Conformità per gli EAU, pronta all'uso",
            'Compliance voor de VAE, kant-en-klaar'),
        'The modules that make HR Suite work the way UAE does — each part of the same grid, no separate tools.': _t(
            'Les modules qui font fonctionner HR Suite à la manière des EAU — chacun fait partie de la même grille, sans outils séparés.',
            'Die Module, die HR Suite so arbeiten lassen, wie es die VAE tun — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hacen los EAU — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            'I moduli che fanno funzionare HR Suite come fanno gli EAU — ognuno parte della stessa griglia, senza strumenti separati.',
            'De modules die HR Suite laten werken zoals de VAE dat doen — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards ----
        'Payroll + WPS salary files': _t('Paie + fichiers de salaires WPS', 'Gehaltsabrechnung + WPS-Gehaltsdateien', 'Nóminas + archivos salariales WPS', 'Buste paga + file salariali WPS', 'Salarisadministratie + WPS-salarisbestanden'),
        'Run MOHRE-compliant pay runs and export the Wage Protection System (WPS) SIF file, so salaries clear through approved agents and on-time payment is on record.': _t(
            'Exécutez des cycles de paie conformes MOHRE et exportez le fichier SIF du Wage Protection System (WPS), afin que les salaires transitent par des agents agréés et que le paiement à temps soit consigné.',
            'Führen Sie MOHRE-konforme Gehaltsläufe durch und exportieren Sie die SIF-Datei des Wage Protection System (WPS), damit Gehälter über zugelassene Agenten laufen und die pünktliche Zahlung dokumentiert ist.',
            'Ejecute procesos de nómina conformes con MOHRE y exporte el archivo SIF del Wage Protection System (WPS), para que los salarios se abonen a través de agentes autorizados y el pago puntual quede registrado.',
            'Esegui cicli di paga conformi a MOHRE ed esporta il file SIF del Wage Protection System (WPS), così gli stipendi passano attraverso agenti autorizzati e il pagamento puntuale è documentato.',
            'Voer MOHRE-conforme salarisruns uit en exporteer het SIF-bestand van het Wage Protection System (WPS), zodat salarissen via goedgekeurde agenten worden verwerkt en tijdige betaling is vastgelegd.'),
        "Gratuity computed to Federal Decree-Law 33/2021 — 21 days' basic wage per year for the first five years, 30 days per year thereafter, capped at two years' wage.": _t(
            'Indemnité calculée selon le Federal Decree-Law 33/2021 — 21 jours de salaire de base par an pour les cinq premières années, 30 jours par an ensuite, plafonnée à deux ans de salaire.',
            'Abfindung berechnet gemäß Federal Decree-Law 33/2021 — 21 Tage Grundgehalt pro Jahr für die ersten fünf Jahre, danach 30 Tage pro Jahr, begrenzt auf zwei Jahresgehälter.',
            'Gratificación calculada conforme al Federal Decree-Law 33/2021 — 21 días de salario base por año durante los primeros cinco años, 30 días por año a partir de entonces, con un tope de dos años de salario.',
            "Indennità calcolata secondo il Federal Decree-Law 33/2021 — 21 giorni di retribuzione base all'anno per i primi cinque anni, 30 giorni all'anno in seguito, con un tetto di due anni di retribuzione.",
            'Ontslagvergoeding berekend volgens Federal Decree-Law 33/2021 — 21 dagen basisloon per jaar voor de eerste vijf jaar, daarna 30 dagen per jaar, met een maximum van twee jaarlonen.'),
        'Pensions &amp; GPSSA': _t('Retraites &amp; GPSSA', 'Renten &amp; GPSSA', 'Pensiones &amp; GPSSA', 'Pensioni &amp; GPSSA', 'Pensioenen &amp; GPSSA'),
        'Set up pension and social-security deductions for GPSSA-registered UAE and GCC nationals, applied automatically in every pay run.': _t(
            'Configurez les retenues de retraite et de sécurité sociale pour les ressortissants des EAU et du GCC enregistrés auprès de la GPSSA, appliquées automatiquement à chaque cycle de paie.',
            'Richten Sie Renten- und Sozialversicherungsabzüge für bei der GPSSA registrierte Staatsangehörige der VAE und des GCC ein, die automatisch in jedem Gehaltslauf angewendet werden.',
            'Configure las deducciones de pensión y seguridad social para nacionales de los EAU y del GCC registrados en la GPSSA, aplicadas automáticamente en cada proceso de nómina.',
            'Configura le trattenute per pensione e previdenza sociale per i cittadini degli EAU e del GCC registrati presso la GPSSA, applicate automaticamente in ogni ciclo di paga.',
            'Stel pensioen- en socialezekerheidsinhoudingen in voor bij de GPSSA geregistreerde onderdanen van de VAE en de GCC, automatisch toegepast in elke salarisrun.'),
        'Emiratization tracking': _t("Suivi de l'Emiratization", 'Emiratization-Nachverfolgung', 'Seguimiento de Emiratization', "Monitoraggio dell'Emiratization", 'Emiratization-tracking'),
        'Track your Emiratization ratio (Nafis) in the analytics dashboard, so you can see where you stand against MOHRE targets before they become a penalty.': _t(
            "Suivez votre ratio d'Emiratization (Nafis) dans le tableau de bord analytique, afin de voir où vous en êtes par rapport aux objectifs MOHRE avant qu'ils ne deviennent une pénalité.",
            'Verfolgen Sie Ihre Emiratization-Quote (Nafis) im Analyse-Dashboard, damit Sie sehen, wo Sie im Verhältnis zu den MOHRE-Zielen stehen, bevor daraus eine Strafe wird.',
            'Haga seguimiento de su ratio de Emiratization (Nafis) en el panel de analítica, para ver dónde se encuentra respecto a los objetivos de MOHRE antes de que se conviertan en una sanción.',
            'Monitora il tuo rapporto di Emiratization (Nafis) nella dashboard di analisi, così vedi a che punto sei rispetto agli obiettivi MOHRE prima che diventino una sanzione.',
            'Volg uw Emiratization-ratio (Nafis) in het analysedashboard, zodat u ziet waar u staat ten opzichte van de MOHRE-doelen voordat ze een boete worden.'),
        'Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and visa, Emirates ID and work-permit expiry tracking so nothing lapses.': _t(
            "Interface en priorité arabe, de droite à gauche partout, contrats et lettres bilingues, et suivi de l'expiration des visas, de l'Emirates ID et des permis de travail pour que rien n'expire.",
            'Durchgehend Arabisch-First-Oberfläche von rechts nach links, zweisprachige Verträge und Schreiben sowie Nachverfolgung des Ablaufs von Visum, Emirates ID und Arbeitsgenehmigung, damit nichts verfällt.',
            'Interfaz con árabe primero, de derecha a izquierda en todo momento, contratos y cartas bilingües, y seguimiento del vencimiento de visados, Emirates ID y permisos de trabajo para que nada caduque.',
            'Interfaccia in arabo prima di tutto, da destra a sinistra ovunque, contratti e lettere bilingui e monitoraggio della scadenza di visto, Emirates ID e permesso di lavoro, così nulla scade.',
            'Interface met Arabisch voorop, overal van rechts naar links, tweetalige contracten en brieven, en tracking van het verlopen van visum, Emirates ID en werkvergunning zodat niets verloopt.'),
        # ---- CTA ----
        'Run UAE HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie des EAU comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung der VAE richtig durch',
            'Gestione RR. HH. &amp; nóminas de los EAU como es debido',
            'Gestisci HR &amp; buste paga degli EAU nel modo giusto',
            'Voer HR &amp; salarisadministratie voor de VAE op de juiste manier uit'),
        'See HR Suite handle UAE payroll, WPS, and gratuity for your team.': _t(
            "Voyez HR Suite gérer la paie des EAU, le WPS et l'indemnité pour votre équipe.",
            'Sehen Sie, wie HR Suite Gehaltsabrechnung der VAE, WPS und Abfindung für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona la nómina de los EAU, el WPS y la gratificación para su equipo.',
            'Guarda HR Suite gestire buste paga degli EAU, WPS e indennità per il tuo team.',
            'Zie hoe HR Suite salarisadministratie van de VAE, WPS en ontslagvergoeding voor uw team afhandelt.'),
    }),
}


PAGE['/regions/qatar/'] = {
    'src': 'regions/qatar/index.html',
    't': _merge(_HOME, _EXPLORE, _SEE_PRICING, _BUILT_IN, _ARABIC_DOCS, _PRICE_NOTE, _EOS_GRATUITY, _PAYROLL_WPS, _PAYRUN_WPS_FILE, {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for Qatar | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour le Qatar | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für Katar | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Catar | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per il Qatar | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor Qatar | FulcrumGrid'),
        'HR Suite for Qatar — WPS payroll, end-of-service gratuity under Labour Law No. 14 of 2004, GRSIA pensions, Qatarization tracking, and Arabic-first HR.': _t(
            'HR Suite pour le Qatar — paie WPS, indemnité de fin de service au titre du Labour Law No. 14 of 2004, retraites GRSIA, suivi de la Qatarization, et RH en priorité arabe.',
            'HR Suite für Katar — WPS-Gehaltsabrechnung, Abfindung zum Dienstende gemäß Labour Law No. 14 of 2004, GRSIA-Renten, Qatarization-Nachverfolgung und Arabisch-First-HR.',
            'HR Suite para Catar — nóminas WPS, gratificación por fin de servicio conforme al Labour Law No. 14 of 2004, pensiones GRSIA, seguimiento de Qatarization y RR. HH. con árabe primero.',
            'HR Suite per il Qatar — buste paga WPS, indennità di fine servizio ai sensi del Labour Law No. 14 of 2004, pensioni GRSIA, monitoraggio della Qatarization e HR in arabo prima di tutto.',
            'HR Suite voor Qatar — WPS-salarisadministratie, ontslagvergoeding onder Labour Law No. 14 of 2004, GRSIA-pensioenen, tracking van Qatarization en HR met Arabisch voorop.'),
        # ---- Hero ----
        'Qatar · QA': _t('Qatar · QA', 'Katar · QA', 'Catar · QA', 'Qatar · QA', 'Qatar · QA'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Qatar</em>': _t(
            'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">le Qatar</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Katar</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">Catar</em>',
            'HR &amp; buste paga, pensato per <em style="font-style:normal;color:var(--color-accent)">il Qatar</em>',
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Qatar</em>'),
        'HR Suite runs your Qatar workforce end to end — WPS-compliant payroll, end-of-service under Labour Law No. 14 of 2004, GRSIA pensions and Qatarization tracking, with Arabic throughout.': _t(
            "HR Suite gère vos effectifs au Qatar de bout en bout — paie conforme WPS, fin de service selon le Labour Law No. 14 of 2004, retraites GRSIA et suivi de la Qatarization, avec l'arabe partout.",
            'HR Suite steuert Ihre Belegschaft in Katar durchgängig — WPS-konforme Gehaltsabrechnung, Dienstende gemäß Labour Law No. 14 of 2004, GRSIA-Renten und Qatarization-Nachverfolgung, durchgehend auf Arabisch.',
            'HR Suite gestiona su plantilla en Catar de principio a fin — nóminas conformes con WPS, fin de servicio según el Labour Law No. 14 of 2004, pensiones GRSIA y seguimiento de Qatarization, con árabe en todo momento.',
            "HR Suite gestisce il tuo organico in Qatar end to end — buste paga conformi a WPS, fine servizio secondo il Labour Law No. 14 of 2004, pensioni GRSIA e monitoraggio della Qatarization, con l'arabo ovunque.",
            'HR Suite beheert uw personeelsbestand in Qatar van begin tot eind — WPS-conforme salarisadministratie, einde dienstverband volgens Labour Law No. 14 of 2004, GRSIA-pensioenen en tracking van Qatarization, met Arabisch overal.'),
        # ---- Sub-head ----
        'Qatar compliance, out of the box': _t(
            "La conformité pour le Qatar, prête à l'emploi",
            'Compliance für Katar, sofort einsatzbereit',
            'Cumplimiento para Catar, listo para usar',
            "Conformità per il Qatar, pronta all'uso",
            'Compliance voor Qatar, kant-en-klaar'),
        'The modules that make HR Suite work the way Qatar does — each part of the same grid, no separate tools.': _t(
            'Les modules qui font fonctionner HR Suite à la manière du Qatar — chacun fait partie de la même grille, sans outils séparés.',
            'Die Module, die HR Suite so arbeiten lassen, wie es Katar tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Catar — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            'I moduli che fanno funzionare HR Suite come fa il Qatar — ognuno parte della stessa griglia, senza strumenti separati.',
            'De modules die HR Suite laten werken zoals Qatar dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards ----
        "End-of-service computed to Labour Law No. 14 of 2004 (art. 54) — a minimum of three weeks' (21 days') basic wage per year of service, across all years.": _t(
            'Fin de service calculée selon le Labour Law No. 14 of 2004 (art. 54) — un minimum de trois semaines (21 jours) de salaire de base par année de service, pour toutes les années.',
            'Dienstende berechnet nach dem Labour Law No. 14 of 2004 (art. 54) — mindestens drei Wochen (21 Tage) Grundgehalt pro Dienstjahr, über alle Jahre hinweg.',
            'Fin de servicio calculado conforme al Labour Law No. 14 of 2004 (art. 54) — un mínimo de tres semanas (21 días) de salario base por año de servicio, en todos los años.',
            'Fine servizio calcolata secondo il Labour Law No. 14 of 2004 (art. 54) — un minimo di tre settimane (21 giorni) di retribuzione base per anno di servizio, per tutti gli anni.',
            'Einde dienstverband berekend volgens Labour Law No. 14 of 2004 (art. 54) — minimaal drie weken (21 dagen) basisloon per dienstjaar, over alle jaren.'),
        'Pensions &amp; GRSIA': _t('Retraites &amp; GRSIA', 'Renten &amp; GRSIA', 'Pensiones &amp; GRSIA', 'Pensioni &amp; GRSIA', 'Pensioenen &amp; GRSIA'),
        'Set up pension and social-insurance deductions for Qatari nationals registered with GRSIA, applied automatically in every pay run.': _t(
            "Configurez les retenues de retraite et d'assurance sociale pour les ressortissants qatariens enregistrés auprès de la GRSIA, appliquées automatiquement à chaque cycle de paie.",
            'Richten Sie Renten- und Sozialversicherungsabzüge für bei der GRSIA registrierte katarische Staatsangehörige ein, die automatisch in jedem Gehaltslauf angewendet werden.',
            'Configure las deducciones de pensión y seguro social para nacionales cataríes registrados en la GRSIA, aplicadas automáticamente en cada proceso de nómina.',
            'Configura le trattenute per pensione e assicurazione sociale per i cittadini qatarioti registrati presso la GRSIA, applicate automaticamente in ogni ciclo di paga.',
            'Stel pensioen- en socialeverzekeringsinhoudingen in voor bij de GRSIA geregistreerde Qatarese onderdanen, automatisch toegepast in elke salarisrun.'),
        'Qatarization tracking': _t('Suivi de la Qatarization', 'Qatarization-Nachverfolgung', 'Seguimiento de Qatarization', 'Monitoraggio della Qatarization', 'Qatarization-tracking'),
        'Track your Qatarization ratio in the analytics dashboard, so you can see your national-workforce share at a glance.': _t(
            "Suivez votre ratio de Qatarization dans le tableau de bord analytique, afin de voir en un coup d'œil la part de vos effectifs nationaux.",
            'Verfolgen Sie Ihre Qatarization-Quote im Analyse-Dashboard, damit Sie den Anteil Ihrer nationalen Belegschaft auf einen Blick sehen.',
            'Haga seguimiento de su ratio de Qatarization en el panel de analítica, para ver de un vistazo la proporción de su plantilla nacional.',
            "Monitora il tuo rapporto di Qatarization nella dashboard di analisi, così vedi a colpo d'occhio la quota del tuo organico nazionale.",
            'Volg uw Qatarization-ratio in het analysedashboard, zodat u in één oogopslag het aandeel van uw nationale personeelsbestand ziet.'),
        'Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and residence-permit and document expiry tracking.': _t(
            "Interface en priorité arabe, de droite à gauche partout, contrats et lettres bilingues, et suivi de l'expiration des permis de séjour et des documents.",
            'Durchgehend Arabisch-First-Oberfläche von rechts nach links, zweisprachige Verträge und Schreiben sowie Nachverfolgung des Ablaufs von Aufenthaltsgenehmigungen und Dokumenten.',
            'Interfaz con árabe primero, de derecha a izquierda en todo momento, contratos y cartas bilingües, y seguimiento del vencimiento de permisos de residencia y documentos.',
            'Interfaccia in arabo prima di tutto, da destra a sinistra ovunque, contratti e lettere bilingui e monitoraggio della scadenza di permessi di soggiorno e documenti.',
            'Interface met Arabisch voorop, overal van rechts naar links, tweetalige contracten en brieven, en tracking van het verlopen van verblijfsvergunningen en documenten.'),
        # ---- CTA ----
        'Run Qatar HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie du Qatar comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung Katars richtig durch',
            'Gestione RR. HH. &amp; nóminas de Catar como es debido',
            'Gestisci HR &amp; buste paga del Qatar nel modo giusto',
            'Voer HR &amp; salarisadministratie voor Qatar op de juiste manier uit'),
        'See HR Suite handle Qatar payroll, WPS, and end-of-service for your team.': _t(
            'Voyez HR Suite gérer la paie du Qatar, le WPS et la fin de service pour votre équipe.',
            'Sehen Sie, wie HR Suite Gehaltsabrechnung Katars, WPS und Dienstende für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona la nómina de Catar, el WPS y el fin de servicio para su equipo.',
            'Guarda HR Suite gestire buste paga del Qatar, WPS e fine servizio per il tuo team.',
            'Zie hoe HR Suite salarisadministratie van Qatar, WPS en einde dienstverband voor uw team afhandelt.'),
    }),
}


PAGE['/regions/kuwait/'] = {
    'src': 'regions/kuwait/index.html',
    't': _merge(_HOME, _EXPLORE, _SEE_PRICING, _BUILT_IN, _ARABIC_DOCS, _PRICE_NOTE, _NAT_WORKFORCE, _PAYROLL_WPS, _PAYRUN_WPS_FILE, {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for Kuwait | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour le Koweït | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für Kuwait | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Kuwait | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per il Kuwait | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor Koeweit | FulcrumGrid'),
        'HR Suite for Kuwait — WPS payroll, end-of-service indemnity under Labour Law No. 6 of 2010, PIFSS deductions, national-workforce tracking, and Arabic-first HR.': _t(
            'HR Suite pour le Koweït — paie WPS, indemnité de fin de service au titre du Labour Law No. 6 of 2010, retenues PIFSS, suivi des effectifs nationaux, et RH en priorité arabe.',
            'HR Suite für Kuwait — WPS-Gehaltsabrechnung, Abfindung zum Dienstende gemäß Labour Law No. 6 of 2010, PIFSS-Abzüge, Nachverfolgung der nationalen Belegschaft und Arabisch-First-HR.',
            'HR Suite para Kuwait — nóminas WPS, indemnización por fin de servicio conforme al Labour Law No. 6 of 2010, deducciones PIFSS, seguimiento de la plantilla nacional y RR. HH. con árabe primero.',
            "HR Suite per il Kuwait — buste paga WPS, indennità di fine servizio ai sensi del Labour Law No. 6 of 2010, trattenute PIFSS, monitoraggio dell'organico nazionale e HR in arabo prima di tutto.",
            'HR Suite voor Koeweit — WPS-salarisadministratie, ontslagvergoeding onder Labour Law No. 6 of 2010, PIFSS-inhoudingen, tracking van het nationale personeelsbestand en HR met Arabisch voorop.'),
        # ---- Hero ----
        'Kuwait · KW': _t('Koweït · KW', 'Kuwait · KW', 'Kuwait · KW', 'Kuwait · KW', 'Koeweit · KW'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Kuwait</em>': _t(
            'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">le Koweït</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Kuwait</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">Kuwait</em>',
            'HR &amp; buste paga, pensato per <em style="font-style:normal;color:var(--color-accent)">il Kuwait</em>',
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Koeweit</em>'),
        'HR Suite runs your Kuwait workforce end to end — WPS-compliant payroll, indemnity under Labour Law No. 6 of 2010, PIFSS social security and national-workforce tracking, with Arabic throughout.': _t(
            "HR Suite gère vos effectifs au Koweït de bout en bout — paie conforme WPS, indemnité selon le Labour Law No. 6 of 2010, sécurité sociale PIFSS et suivi des effectifs nationaux, avec l'arabe partout.",
            'HR Suite steuert Ihre Belegschaft in Kuwait durchgängig — WPS-konforme Gehaltsabrechnung, Abfindung gemäß Labour Law No. 6 of 2010, PIFSS-Sozialversicherung und Nachverfolgung der nationalen Belegschaft, durchgehend auf Arabisch.',
            'HR Suite gestiona su plantilla en Kuwait de principio a fin — nóminas conformes con WPS, indemnización según el Labour Law No. 6 of 2010, seguridad social PIFSS y seguimiento de la plantilla nacional, con árabe en todo momento.',
            "HR Suite gestisce il tuo organico in Kuwait end to end — buste paga conformi a WPS, indennità secondo il Labour Law No. 6 of 2010, previdenza sociale PIFSS e monitoraggio dell'organico nazionale, con l'arabo ovunque.",
            'HR Suite beheert uw personeelsbestand in Koeweit van begin tot eind — WPS-conforme salarisadministratie, ontslagvergoeding volgens Labour Law No. 6 of 2010, PIFSS sociale zekerheid en tracking van het nationale personeelsbestand, met Arabisch overal.'),
        # ---- Sub-head ----
        'Kuwait compliance, out of the box': _t(
            "La conformité pour le Koweït, prête à l'emploi",
            'Compliance für Kuwait, sofort einsatzbereit',
            'Cumplimiento para Kuwait, listo para usar',
            "Conformità per il Kuwait, pronta all'uso",
            'Compliance voor Koeweit, kant-en-klaar'),
        'The modules that make HR Suite work the way Kuwait does — each part of the same grid, no separate tools.': _t(
            'Les modules qui font fonctionner HR Suite à la manière du Koweït — chacun fait partie de la même grille, sans outils séparés.',
            'Die Module, die HR Suite so arbeiten lassen, wie es Kuwait tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Kuwait — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            'I moduli che fanno funzionare HR Suite come fa il Kuwait — ognuno parte della stessa griglia, senza strumenti separati.',
            'De modules die HR Suite laten werken zoals Koeweit dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards ----
        'End-of-service indemnity': _t('Indemnité de fin de service', 'Abfindung zum Dienstende', 'Indemnización por fin de servicio', 'Indennità di fine servizio', 'Ontslagvergoeding'),
        "Indemnity computed to the Private Sector Labour Law No. 6 of 2010 (art. 51) — 15 days' wage per year for the first five years, a full month per year thereafter, capped at 1.5 years' wage, with a resignation scale.": _t(
            'Indemnité calculée selon la Private Sector Labour Law No. 6 of 2010 (art. 51) — 15 jours de salaire par an pour les cinq premières années, puis un mois entier par an, plafonnée à 1,5 an de salaire, avec un barème de démission.',
            'Abfindung berechnet nach der Private Sector Labour Law No. 6 of 2010 (art. 51) — 15 Tage Gehalt pro Jahr für die ersten fünf Jahre, danach ein volles Monatsgehalt pro Jahr, begrenzt auf 1,5 Jahresgehälter, mit einer Kündigungsstaffel.',
            'Indemnización calculada conforme a la Private Sector Labour Law No. 6 of 2010 (art. 51) — 15 días de salario por año durante los primeros cinco años, un mes completo por año a partir de entonces, con un tope de 1,5 años de salario y una escala por dimisión.',
            "Indennità calcolata secondo la Private Sector Labour Law No. 6 of 2010 (art. 51) — 15 giorni di retribuzione all'anno per i primi cinque anni, poi un mese intero all'anno, con un tetto di 1,5 anni di retribuzione e una scala per le dimissioni.",
            'Ontslagvergoeding berekend volgens de Private Sector Labour Law No. 6 of 2010 (art. 51) — 15 dagen loon per jaar voor de eerste vijf jaar, daarna een volledige maand per jaar, met een maximum van 1,5 jaarloon en een schaal bij ontslagname.'),
        'Social security &amp; PIFSS': _t('Sécurité sociale &amp; PIFSS', 'Sozialversicherung &amp; PIFSS', 'Seguridad social &amp; PIFSS', 'Previdenza sociale &amp; PIFSS', 'Sociale zekerheid &amp; PIFSS'),
        'Set up social-security deductions for Kuwaiti nationals registered with PIFSS, applied automatically in every pay run.': _t(
            'Configurez les retenues de sécurité sociale pour les ressortissants koweïtiens enregistrés auprès de la PIFSS, appliquées automatiquement à chaque cycle de paie.',
            'Richten Sie Sozialversicherungsabzüge für bei der PIFSS registrierte kuwaitische Staatsangehörige ein, die automatisch in jedem Gehaltslauf angewendet werden.',
            'Configure las deducciones de seguridad social para nacionales kuwaitíes registrados en la PIFSS, aplicadas automáticamente en cada proceso de nómina.',
            'Configura le trattenute previdenziali per i cittadini kuwaitiani registrati presso la PIFSS, applicate automaticamente in ogni ciclo di paga.',
            'Stel socialezekerheidsinhoudingen in voor bij de PIFSS geregistreerde Koeweitse onderdanen, automatisch toegepast in elke salarisrun.'),
        'Track your national-workforce ratio in the analytics dashboard, so your Kuwaitization share is always visible.': _t(
            "Suivez votre ratio d'effectifs nationaux dans le tableau de bord analytique, afin que votre part de Kuwaitization soit toujours visible.",
            'Verfolgen Sie Ihre Quote der nationalen Belegschaft im Analyse-Dashboard, damit Ihr Kuwaitization-Anteil stets sichtbar ist.',
            'Haga seguimiento de su ratio de plantilla nacional en el panel de analítica, para que su proporción de Kuwaitization sea siempre visible.',
            'Monitora il tuo rapporto di organico nazionale nella dashboard di analisi, così la tua quota di Kuwaitization è sempre visibile.',
            'Volg uw ratio nationaal personeelsbestand in het analysedashboard, zodat uw Kuwaitization-aandeel altijd zichtbaar is.'),
        'Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and residence and permit expiry tracking.': _t(
            "Interface en priorité arabe, de droite à gauche partout, contrats et lettres bilingues, et suivi de l'expiration des titres de séjour et des permis.",
            'Durchgehend Arabisch-First-Oberfläche von rechts nach links, zweisprachige Verträge und Schreiben sowie Nachverfolgung des Ablaufs von Aufenthalt und Genehmigungen.',
            'Interfaz con árabe primero, de derecha a izquierda en todo momento, contratos y cartas bilingües, y seguimiento del vencimiento de la residencia y los permisos.',
            'Interfaccia in arabo prima di tutto, da destra a sinistra ovunque, contratti e lettere bilingui e monitoraggio della scadenza di soggiorno e permessi.',
            'Interface met Arabisch voorop, overal van rechts naar links, tweetalige contracten en brieven, en tracking van het verlopen van verblijf en vergunningen.'),
        # ---- CTA ----
        'Run Kuwait HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie du Koweït comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung Kuwaits richtig durch',
            'Gestione RR. HH. &amp; nóminas de Kuwait como es debido',
            'Gestisci HR &amp; buste paga del Kuwait nel modo giusto',
            'Voer HR &amp; salarisadministratie voor Koeweit op de juiste manier uit'),
        'See HR Suite handle Kuwait payroll, WPS, and indemnity for your team.': _t(
            "Voyez HR Suite gérer la paie du Koweït, le WPS et l'indemnité pour votre équipe.",
            'Sehen Sie, wie HR Suite Gehaltsabrechnung Kuwaits, WPS und Abfindung für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona la nómina de Kuwait, el WPS y la indemnización para su equipo.',
            'Guarda HR Suite gestire buste paga del Kuwait, WPS e indennità per il tuo team.',
            'Zie hoe HR Suite salarisadministratie van Koeweit, WPS en ontslagvergoeding voor uw team afhandelt.'),
    }),
}


PAGE['/regions/bahrain/'] = {
    'src': 'regions/bahrain/index.html',
    't': _merge(_HOME, _EXPLORE, _SEE_PRICING, _BUILT_IN, _ARABIC_DOCS, _PRICE_NOTE, _NAT_WORKFORCE, _PAYROLL_WPS, _PAYRUN_WPS_FILE, {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for Bahrain | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour Bahreïn | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für Bahrain | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Baréin | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per il Bahrein | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor Bahrein | FulcrumGrid'),
        'HR Suite for Bahrain — WPS payroll, leaving indemnity under Labour Law No. 36 of 2012, SIO social insurance, national-workforce tracking, and Arabic-first HR.': _t(
            'HR Suite pour Bahreïn — paie WPS, indemnité de départ au titre du Labour Law No. 36 of 2012, assurance sociale SIO, suivi des effectifs nationaux, et RH en priorité arabe.',
            'HR Suite für Bahrain — WPS-Gehaltsabrechnung, Abfindung beim Ausscheiden gemäß Labour Law No. 36 of 2012, SIO-Sozialversicherung, Nachverfolgung der nationalen Belegschaft und Arabisch-First-HR.',
            'HR Suite para Baréin — nóminas WPS, indemnización por cese conforme al Labour Law No. 36 of 2012, seguro social SIO, seguimiento de la plantilla nacional y RR. HH. con árabe primero.',
            "HR Suite per il Bahrein — buste paga WPS, indennità di cessazione ai sensi del Labour Law No. 36 of 2012, assicurazione sociale SIO, monitoraggio dell'organico nazionale e HR in arabo prima di tutto.",
            'HR Suite voor Bahrein — WPS-salarisadministratie, vertrekvergoeding onder Labour Law No. 36 of 2012, SIO sociale verzekering, tracking van het nationale personeelsbestand en HR met Arabisch voorop.'),
        # ---- Hero ----
        'Bahrain · BH': _t('Bahreïn · BH', 'Bahrain · BH', 'Baréin · BH', 'Bahrein · BH', 'Bahrein · BH'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Bahrain</em>': _t(
            'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">Bahreïn</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Bahrain</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">Baréin</em>',
            'HR &amp; buste paga, pensato per <em style="font-style:normal;color:var(--color-accent)">il Bahrein</em>',
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Bahrein</em>'),
        'HR Suite runs your Bahrain workforce end to end — WPS-compliant payroll, leaving indemnity under Law No. 36 of 2012, SIO social insurance and national-workforce tracking, with Arabic throughout.': _t(
            "HR Suite gère vos effectifs à Bahreïn de bout en bout — paie conforme WPS, indemnité de départ selon la Law No. 36 of 2012, assurance sociale SIO et suivi des effectifs nationaux, avec l'arabe partout.",
            'HR Suite steuert Ihre Belegschaft in Bahrain durchgängig — WPS-konforme Gehaltsabrechnung, Abfindung beim Ausscheiden gemäß Law No. 36 of 2012, SIO-Sozialversicherung und Nachverfolgung der nationalen Belegschaft, durchgehend auf Arabisch.',
            'HR Suite gestiona su plantilla en Baréin de principio a fin — nóminas conformes con WPS, indemnización por cese según la Law No. 36 of 2012, seguro social SIO y seguimiento de la plantilla nacional, con árabe en todo momento.',
            "HR Suite gestisce il tuo organico in Bahrein end to end — buste paga conformi a WPS, indennità di cessazione secondo la Law No. 36 of 2012, assicurazione sociale SIO e monitoraggio dell'organico nazionale, con l'arabo ovunque.",
            'HR Suite beheert uw personeelsbestand in Bahrein van begin tot eind — WPS-conforme salarisadministratie, vertrekvergoeding volgens Law No. 36 of 2012, SIO sociale verzekering en tracking van het nationale personeelsbestand, met Arabisch overal.'),
        # ---- Sub-head ----
        'Bahrain compliance, out of the box': _t(
            "La conformité pour Bahreïn, prête à l'emploi",
            'Compliance für Bahrain, sofort einsatzbereit',
            'Cumplimiento para Baréin, listo para usar',
            "Conformità per il Bahrein, pronta all'uso",
            'Compliance voor Bahrein, kant-en-klaar'),
        'The modules that make HR Suite work the way Bahrain does — each part of the same grid, no separate tools.': _t(
            'Les modules qui font fonctionner HR Suite à la manière de Bahreïn — chacun fait partie de la même grille, sans outils séparés.',
            'Die Module, die HR Suite so arbeiten lassen, wie es Bahrain tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Baréin — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            'I moduli che fanno funzionare HR Suite come fa il Bahrein — ognuno parte della stessa griglia, senza strumenti separati.',
            'De modules die HR Suite laten werken zoals Bahrein dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards ----
        'Leaving indemnity': _t('Indemnité de départ', 'Abfindung beim Ausscheiden', 'Indemnización por cese', 'Indennità di cessazione', 'Vertrekvergoeding'),
        "Leaving indemnity computed to the Private Sector Labour Law No. 36 of 2012 (art. 116) — 15 days' wage per year for the first three years, a full month per year thereafter. Nationals covered by SIO are handled separately.": _t(
            'Indemnité de départ calculée selon la Private Sector Labour Law No. 36 of 2012 (art. 116) — 15 jours de salaire par an pour les trois premières années, puis un mois entier par an. Les ressortissants couverts par la SIO sont traités séparément.',
            'Abfindung beim Ausscheiden berechnet nach der Private Sector Labour Law No. 36 of 2012 (art. 116) — 15 Tage Gehalt pro Jahr für die ersten drei Jahre, danach ein volles Monatsgehalt pro Jahr. Staatsangehörige, die von der SIO abgedeckt sind, werden gesondert behandelt.',
            'Indemnización por cese calculada conforme a la Private Sector Labour Law No. 36 of 2012 (art. 116) — 15 días de salario por año durante los primeros tres años, un mes completo por año a partir de entonces. Los nacionales cubiertos por la SIO se tratan por separado.',
            'Indennità di cessazione calcolata secondo la Private Sector Labour Law No. 36 of 2012 (art. 116) — 15 giorni di retribuzione all\'anno per i primi tre anni, poi un mese intero all\'anno. I cittadini coperti dalla SIO sono gestiti separatamente.',
            'Vertrekvergoeding berekend volgens de Private Sector Labour Law No. 36 of 2012 (art. 116) — 15 dagen loon per jaar voor de eerste drie jaar, daarna een volledige maand per jaar. Onderdanen die onder de SIO vallen, worden apart behandeld.'),
        'Social insurance &amp; SIO': _t('Assurance sociale &amp; SIO', 'Sozialversicherung &amp; SIO', 'Seguro social &amp; SIO', 'Assicurazione sociale &amp; SIO', 'Sociale verzekering &amp; SIO'),
        'Set up social-insurance deductions for Bahraini nationals registered with the Social Insurance Organisation (SIO), applied automatically in every pay run.': _t(
            "Configurez les retenues d'assurance sociale pour les ressortissants bahreïniens enregistrés auprès de la Social Insurance Organisation (SIO), appliquées automatiquement à chaque cycle de paie.",
            'Richten Sie Sozialversicherungsabzüge für bei der Social Insurance Organisation (SIO) registrierte bahrainische Staatsangehörige ein, die automatisch in jedem Gehaltslauf angewendet werden.',
            'Configure las deducciones de seguro social para nacionales bahreiníes registrados en la Social Insurance Organisation (SIO), aplicadas automáticamente en cada proceso de nómina.',
            "Configura le trattenute per l'assicurazione sociale per i cittadini bahreiniti registrati presso la Social Insurance Organisation (SIO), applicate automaticamente in ogni ciclo di paga.",
            'Stel socialeverzekeringsinhoudingen in voor bij de Social Insurance Organisation (SIO) geregistreerde Bahreinse onderdanen, automatisch toegepast in elke salarisrun.'),
        'Track your national-workforce ratio in the analytics dashboard, so your Bahrainization share is always visible.': _t(
            "Suivez votre ratio d'effectifs nationaux dans le tableau de bord analytique, afin que votre part de Bahrainization soit toujours visible.",
            'Verfolgen Sie Ihre Quote der nationalen Belegschaft im Analyse-Dashboard, damit Ihr Bahrainization-Anteil stets sichtbar ist.',
            'Haga seguimiento de su ratio de plantilla nacional en el panel de analítica, para que su proporción de Bahrainization sea siempre visible.',
            'Monitora il tuo rapporto di organico nazionale nella dashboard di analisi, così la tua quota di Bahrainization è sempre visibile.',
            'Volg uw ratio nationaal personeelsbestand in het analysedashboard, zodat uw Bahrainization-aandeel altijd zichtbaar is.'),
        'Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and CPR and permit expiry tracking.': _t(
            "Interface en priorité arabe, de droite à gauche partout, contrats et lettres bilingues, et suivi de l'expiration du CPR et des permis.",
            'Durchgehend Arabisch-First-Oberfläche von rechts nach links, zweisprachige Verträge und Schreiben sowie Nachverfolgung des Ablaufs von CPR und Genehmigungen.',
            'Interfaz con árabe primero, de derecha a izquierda en todo momento, contratos y cartas bilingües, y seguimiento del vencimiento del CPR y los permisos.',
            'Interfaccia in arabo prima di tutto, da destra a sinistra ovunque, contratti e lettere bilingui e monitoraggio della scadenza del CPR e dei permessi.',
            'Interface met Arabisch voorop, overal van rechts naar links, tweetalige contracten en brieven, en tracking van het verlopen van CPR en vergunningen.'),
        # ---- CTA ----
        'Run Bahrain HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie de Bahreïn comme il se doit',
            'Führen Sie HR &amp; Gehaltsabrechnung Bahrains richtig durch',
            'Gestione RR. HH. &amp; nóminas de Baréin como es debido',
            'Gestisci HR &amp; buste paga del Bahrein nel modo giusto',
            'Voer HR &amp; salarisadministratie voor Bahrein op de juiste manier uit'),
        'See HR Suite handle Bahrain payroll, WPS, and indemnity for your team.': _t(
            "Voyez HR Suite gérer la paie de Bahreïn, le WPS et l'indemnité pour votre équipe.",
            'Sehen Sie, wie HR Suite Gehaltsabrechnung Bahrains, WPS und Abfindung für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona la nómina de Baréin, el WPS y la indemnización para su equipo.',
            'Guarda HR Suite gestire buste paga del Bahrein, WPS e indennità per il tuo team.',
            'Zie hoe HR Suite salarisadministratie van Bahrein, WPS en ontslagvergoeding voor uw team afhandelt.'),
    }),
}


PAGE['/regions/oman/'] = {
    'src': 'regions/oman/index.html',
    't': _merge(_HOME, _EXPLORE, _SEE_PRICING, _BUILT_IN, _ARABIC_DOCS, _PRICE_NOTE, _EOS_GRATUITY, _PAYROLL_WPS, _PAYRUN_WPS_FILE, {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for Oman | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour Oman | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für Oman | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Omán | FulcrumGrid',
            "HR Suite — HR &amp; buste paga per l'Oman | FulcrumGrid",
            'HR Suite — HR &amp; salarisadministratie voor Oman | FulcrumGrid'),
        'HR Suite for Oman — WPS payroll, end-of-service gratuity, PASI / Social Protection Fund, Omanization tracking, and Arabic-first HR, aligned with the Social Protection Law (Royal Decree 52/2023).': _t(
            "HR Suite pour Oman — paie WPS, indemnité de fin de service, PASI / Social Protection Fund, suivi de l'Omanization, et RH en priorité arabe, aligné sur la Social Protection Law (Royal Decree 52/2023).",
            'HR Suite für Oman — WPS-Gehaltsabrechnung, Abfindung zum Dienstende, PASI / Social Protection Fund, Omanization-Nachverfolgung und Arabisch-First-HR, im Einklang mit der Social Protection Law (Royal Decree 52/2023).',
            'HR Suite para Omán — nóminas WPS, gratificación por fin de servicio, PASI / Social Protection Fund, seguimiento de Omanization y RR. HH. con árabe primero, en consonancia con la Social Protection Law (Royal Decree 52/2023).',
            "HR Suite per l'Oman — buste paga WPS, indennità di fine servizio, PASI / Social Protection Fund, monitoraggio dell'Omanization e HR in arabo prima di tutto, in linea con la Social Protection Law (Royal Decree 52/2023).",
            'HR Suite voor Oman — WPS-salarisadministratie, ontslagvergoeding, PASI / Social Protection Fund, tracking van Omanization en HR met Arabisch voorop, afgestemd op de Social Protection Law (Royal Decree 52/2023).'),
        # ---- Hero ----
        'Oman · OM': _t('Oman · OM', 'Oman · OM', 'Omán · OM', 'Oman · OM', 'Oman · OM'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Oman</em>': _t(
            'RH &amp; paie, conçu pour <em style="font-style:normal;color:var(--color-accent)">Oman</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Oman</em>',
            'RR. HH. &amp; nóminas, diseñado para <em style="font-style:normal;color:var(--color-accent)">Omán</em>',
            "HR &amp; buste paga, pensato per <em style=\"font-style:normal;color:var(--color-accent)\">l'Oman</em>",
            'HR &amp; salarisadministratie, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Oman</em>'),
        'HR Suite runs your Oman workforce end to end — WPS-compliant payroll, end-of-service gratuity, social protection and Omanization tracking, with Arabic throughout — and it follows the Social Protection Law reform as it phases in.': _t(
            "HR Suite gère vos effectifs à Oman de bout en bout — paie conforme WPS, indemnité de fin de service, protection sociale et suivi de l'Omanization, avec l'arabe partout — et elle suit la réforme de la Social Protection Law à mesure de son entrée en vigueur.",
            'HR Suite steuert Ihre Belegschaft in Oman durchgängig — WPS-konforme Gehaltsabrechnung, Abfindung zum Dienstende, Sozialschutz und Omanization-Nachverfolgung, durchgehend auf Arabisch — und folgt der Reform der Social Protection Law, während sie schrittweise in Kraft tritt.',
            'HR Suite gestiona su plantilla en Omán de principio a fin — nóminas conformes con WPS, gratificación por fin de servicio, protección social y seguimiento de Omanization, con árabe en todo momento — y sigue la reforma de la Social Protection Law a medida que entra en vigor.',
            "HR Suite gestisce il tuo organico in Oman end to end — buste paga conformi a WPS, indennità di fine servizio, protezione sociale e monitoraggio dell'Omanization, con l'arabo ovunque — e segue la riforma della Social Protection Law man mano che entra in vigore.",
            'HR Suite beheert uw personeelsbestand in Oman van begin tot eind — WPS-conforme salarisadministratie, ontslagvergoeding, sociale bescherming en tracking van Omanization, met Arabisch overal — en volgt de hervorming van de Social Protection Law naarmate die gefaseerd ingaat.'),
        # ---- Sub-head ----
        'Oman compliance, out of the box': _t(
            "La conformité pour Oman, prête à l'emploi",
            'Compliance für Oman, sofort einsatzbereit',
            'Cumplimiento para Omán, listo para usar',
            "Conformità per l'Oman, pronta all'uso",
            'Compliance voor Oman, kant-en-klaar'),
        'The modules that make HR Suite work the way Oman does — each part of the same grid, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière d'Oman — chacun fait partie de la même grille, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie es Oman tut — jedes Teil demselben Grid, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Omán — cada uno forma parte de la misma cuadrícula, sin herramientas separadas.',
            "I moduli che fanno funzionare HR Suite come fa l'Oman — ognuno parte della stessa griglia, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Oman dat doet — elk onderdeel van hetzelfde grid, geen aparte tools.'),
        # ---- Feature cards ----
        "End-of-service gratuity of 15 days' wage per year for the first three years and a full month per year thereafter — with the Social Protection Law (Royal Decree 52/2023) savings scheme supported as it phases in.": _t(
            "Indemnité de fin de service de 15 jours de salaire par an pour les trois premières années et d'un mois entier par an ensuite — avec la prise en charge du régime d'épargne de la Social Protection Law (Royal Decree 52/2023) à mesure de son entrée en vigueur.",
            'Abfindung zum Dienstende von 15 Tagen Gehalt pro Jahr für die ersten drei Jahre und einem vollen Monatsgehalt pro Jahr danach — wobei das Sparmodell der Social Protection Law (Royal Decree 52/2023) unterstützt wird, während es schrittweise in Kraft tritt.',
            'Gratificación por fin de servicio de 15 días de salario por año durante los primeros tres años y un mes completo por año a partir de entonces — con el régimen de ahorro de la Social Protection Law (Royal Decree 52/2023) admitido a medida que entra en vigor.',
            "Indennità di fine servizio di 15 giorni di retribuzione all'anno per i primi tre anni e di un mese intero all'anno in seguito — con il supporto del piano di risparmio della Social Protection Law (Royal Decree 52/2023) man mano che entra in vigore.",
            'Ontslagvergoeding van 15 dagen loon per jaar voor de eerste drie jaar en een volledige maand per jaar daarna — waarbij de spaarregeling van de Social Protection Law (Royal Decree 52/2023) wordt ondersteund naarmate die gefaseerd ingaat.'),
        'Social protection': _t('Protection sociale', 'Sozialschutz', 'Protección social', 'Protezione sociale', 'Sociale bescherming'),
        'Set up social-protection and pension deductions for Omani nationals, applied automatically in every pay run and ready for the new contributory savings scheme.': _t(
            "Configurez les retenues de protection sociale et de retraite pour les ressortissants omanais, appliquées automatiquement à chaque cycle de paie et prêtes pour le nouveau régime d'épargne contributif.",
            'Richten Sie Sozialschutz- und Rentenabzüge für omanische Staatsangehörige ein, die automatisch in jedem Gehaltslauf angewendet werden und für das neue beitragsbasierte Sparmodell bereit sind.',
            'Configure las deducciones de protección social y pensión para nacionales omaníes, aplicadas automáticamente en cada proceso de nómina y listas para el nuevo régimen de ahorro contributivo.',
            'Configura le trattenute per protezione sociale e pensione per i cittadini omaniti, applicate automaticamente in ogni ciclo di paga e pronte per il nuovo piano di risparmio contributivo.',
            'Stel inhoudingen voor sociale bescherming en pensioen in voor Omaanse onderdanen, automatisch toegepast in elke salarisrun en klaar voor de nieuwe op bijdragen gebaseerde spaarregeling.'),
        'Omanization tracking': _t("Suivi de l'Omanization", 'Omanization-Nachverfolgung', 'Seguimiento de Omanization', "Monitoraggio dell'Omanization", 'Omanization-tracking'),
        'Track your Omanization ratio in the analytics dashboard, so your national-workforce share is always visible.': _t(
            "Suivez votre ratio d'Omanization dans le tableau de bord analytique, afin que la part de vos effectifs nationaux soit toujours visible.",
            'Verfolgen Sie Ihre Omanization-Quote im Analyse-Dashboard, damit der Anteil Ihrer nationalen Belegschaft stets sichtbar ist.',
            'Haga seguimiento de su ratio de Omanization en el panel de analítica, para que la proporción de su plantilla nacional sea siempre visible.',
            'Monitora il tuo rapporto di Omanization nella dashboard di analisi, così la quota del tuo organico nazionale è sempre visibile.',
            'Volg uw Omanization-ratio in het analysedashboard, zodat het aandeel van uw nationale personeelsbestand altijd zichtbaar is.'),
        'Arabic-first, right-to-left interface throughout, bilingual contracts and letters, and resident-card and permit expiry tracking.': _t(
            "Interface en priorité arabe, de droite à gauche partout, contrats et lettres bilingues, et suivi de l'expiration de la carte de résident et des permis.",
            'Durchgehend Arabisch-First-Oberfläche von rechts nach links, zweisprachige Verträge und Schreiben sowie Nachverfolgung des Ablaufs von Aufenthaltskarte und Genehmigungen.',
            'Interfaz con árabe primero, de derecha a izquierda en todo momento, contratos y cartas bilingües, y seguimiento del vencimiento de la tarjeta de residente y los permisos.',
            'Interfaccia in arabo prima di tutto, da destra a sinistra ovunque, contratti e lettere bilingui e monitoraggio della scadenza della carta di residente e dei permessi.',
            'Interface met Arabisch voorop, overal van rechts naar links, tweetalige contracten en brieven, en tracking van het verlopen van de verblijfskaart en vergunningen.'),
        # ---- CTA ----
        'Run Oman HR &amp; payroll the right way': _t(
            "Gérez la RH &amp; la paie d'Oman comme il se doit",
            'Führen Sie HR &amp; Gehaltsabrechnung Omans richtig durch',
            'Gestione RR. HH. &amp; nóminas de Omán como es debido',
            "Gestisci HR &amp; buste paga dell'Oman nel modo giusto",
            'Voer HR &amp; salarisadministratie voor Oman op de juiste manier uit'),
        'See HR Suite handle Oman payroll, WPS, and end-of-service for your team.': _t(
            "Voyez HR Suite gérer la paie d'Oman, le WPS et la fin de service pour votre équipe.",
            'Sehen Sie, wie HR Suite Gehaltsabrechnung Omans, WPS und Dienstende für Ihr Team abwickelt.',
            'Vea cómo HR Suite gestiona la nómina de Omán, el WPS y el fin de servicio para su equipo.',
            "Guarda HR Suite gestire buste paga dell'Oman, WPS e fine servizio per il tuo team.",
            'Zie hoe HR Suite salarisadministratie van Oman, WPS en einde dienstverband voor uw team afhandelt.'),
    }),
}
