# -*- coding: utf-8 -*-
"""Per-page translations for the Command Center and Collection product pages.

Keys are EXACT English substrings of the EN source HTML (including HTML
entities, straight apostrophes, em dashes and the ↗ glyph). Brand/product
names (FulcrumGrid, Command Center, Collection, HR Suite) and code labels
(SAR, USD, EUR, GCC, KPI, CRM, SMS, DSO, P&L, GDPR, SIF/WPS/GOSI, OPS/FIN/EX/
AR/SMB marks) are left as-is. Common chrome lives in loc_catalog.COMMON.

Note on the Collection "Privacy & data-subject rights" heading: COMMON runs
first and translates the leading word "Privacy", so this catalog translates
only the remaining "&amp; data-subject rights" fragment.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# ---- Segments shared verbatim by both pages ------------------------------
_SHARED = {
    'Available now': _t('Disponible maintenant', 'Jetzt verfügbar', 'Disponible ahora', 'Disponibile ora', 'Nu beschikbaar'),
    'Included': _t('Inclus', 'Enthalten', 'Incluido', 'Incluso', 'Inbegrepen'),
    'Start free trial': _t("Démarrer l'essai gratuit", 'Kostenlos testen', 'Iniciar prueba gratuita', 'Inizia la prova gratuita', 'Start gratis proefperiode'),
    'See full pricing ↗': _t('Voir tous les tarifs ↗', 'Alle Preise ansehen ↗', 'Ver todos los precios ↗', 'Vedi tutti i prezzi ↗', 'Bekijk alle prijzen ↗'),
    'Email support': _t('Assistance par e-mail', 'E-Mail-Support', 'Soporte por correo', 'Assistenza via e-mail', 'E-mailondersteuning'),
    'Capabilities': _t('Capacités', 'Fähigkeiten', 'Capacidades', 'Capacità', 'Mogelijkheden'),
    'Built for your region': _t('Conçu pour votre région', 'Für Ihre Region gebaut', 'Diseñado para su región', 'Costruito per la tua regione', 'Gebouwd voor uw regio'),
    'Built for': _t('Conçu pour', 'Entwickelt für', 'Diseñado para', 'Pensato per', 'Gemaakt voor'),
    'Your region': _t('Votre région', 'Ihre Region', 'Su región', 'La tua regione', 'Uw regio'),
    'The FulcrumGrid family': _t('La famille FulcrumGrid', 'Die FulcrumGrid-Familie', 'La familia FulcrumGrid', 'La famiglia FulcrumGrid', 'De FulcrumGrid-familie'),
    'Explore the rest of the grid': _t('Découvrez le reste de la grille', 'Entdecken Sie den Rest des Grids', 'Explore el resto de la cuadrícula', 'Esplora il resto della griglia', 'Ontdek de rest van het grid'),
    'Finance': _t('Finance', 'Finanzen', 'Finanzas', 'Finanza', 'Financiën'),
    'People operations': _t('Gestion des personnes', 'Personalmanagement', 'Gestión de personas', 'Gestione del personale', 'Personeelsbeheer'),
    'More apps': _t("Plus d'applications", 'Weitere Apps', 'Más apps', 'Altre app', 'Meer apps'),
    'Inventory, CRM &amp; more': _t('Inventaire, CRM &amp; plus', 'Lagerverwaltung, CRM &amp; mehr', 'Inventario, CRM &amp; más', 'Inventario, CRM &amp; altro', 'Voorraad, CRM &amp; meer'),
}


# ---- Command Center ------------------------------------------------------
_CC = {
    # Meta
    "Command Center is FulcrumGrid's real-time operations dashboard — live KPIs, alerts, automated workflows, and reporting from one control room.": _t(
        "Command Center est le tableau de bord des opérations en temps réel de FulcrumGrid — KPI en direct, alertes, flux de travail automatisés et reporting depuis une seule salle de contrôle.",
        'Command Center ist das Echtzeit-Betriebs-Dashboard von FulcrumGrid — Live-KPIs, Warnungen, automatisierte Workflows und Reporting aus einem Kontrollraum.',
        'Command Center es el panel de operaciones en tiempo real de FulcrumGrid — KPI en directo, alertas, flujos de trabajo automatizados e informes desde una sola sala de control.',
        "Command Center è la dashboard operativa in tempo reale di FulcrumGrid — KPI in tempo reale, avvisi, flussi di lavoro automatizzati e reporting da un'unica sala di controllo.",
        "Command Center is het realtime operationele dashboard van FulcrumGrid — live KPI's, meldingen, geautomatiseerde workflows en rapportage vanuit één controlekamer."),
    'Real-time operations dashboard: live KPIs, alerts, automation, and reporting.': _t(
        'Tableau de bord des opérations en temps réel : KPI en direct, alertes, automatisation et reporting.',
        'Echtzeit-Betriebs-Dashboard: Live-KPIs, Warnungen, Automatisierung und Reporting.',
        'Panel de operaciones en tiempo real: KPI en directo, alertas, automatización e informes.',
        'Dashboard operativa in tempo reale: KPI in tempo reale, avvisi, automazione e reporting.',
        "Realtime operationeel dashboard: live KPI's, meldingen, automatisering en rapportage."),
    # Hero
    '>Operations ·': _t('>Opérations ·', '>Betrieb ·', '>Operaciones ·', '>Operazioni ·', '>Operaties ·'),
    'See everything. Control anything.': _t(
        'Voir tout. Tout contrôler.',
        'Alles sehen. Alles steuern.',
        'Véalo todo. Contrólelo todo.',
        'Vedi tutto. Controlla tutto.',
        'Zie alles. Beheer alles.'),
    "Command Center is your business's control room — a real-time dashboard that brings your key metrics, workflows, and alerts into one view, so nothing slips and every decision is made on live data.": _t(
        "Command Center est la salle de contrôle de votre entreprise — un tableau de bord en temps réel qui réunit vos indicateurs clés, vos flux de travail et vos alertes en une seule vue, pour que rien ne vous échappe et que chaque décision repose sur des données en direct.",
        'Command Center ist der Kontrollraum Ihres Unternehmens — ein Echtzeit-Dashboard, das Ihre wichtigsten Kennzahlen, Workflows und Warnungen in einer Ansicht zusammenführt, damit nichts durchrutscht und jede Entscheidung auf Live-Daten beruht.',
        'Command Center es la sala de control de su empresa — un panel en tiempo real que reúne sus métricas clave, flujos de trabajo y alertas en una sola vista, para que nada se escape y cada decisión se tome con datos en directo.',
        "Command Center è la sala di controllo della tua azienda — una dashboard in tempo reale che riunisce le tue metriche chiave, i flussi di lavoro e gli avvisi in un'unica vista, così nulla sfugge e ogni decisione si basa su dati in tempo reale.",
        'Command Center is de controlekamer van uw bedrijf — een realtime dashboard dat uw belangrijkste metrieken, workflows en meldingen in één weergave samenbrengt, zodat niets ontglipt en elke beslissing op live data berust.'),
    'Open Command Center': _t('Ouvrir Command Center', 'Command Center öffnen', 'Abrir Command Center', 'Apri Command Center', 'Command Center openen'),
    # Pricing
    'Command Center pricing': _t('Tarifs Command Center', 'Command Center Preise', 'Precios de Command Center', 'Prezzi di Command Center', 'Command Center prijzen'),
    'Per organization / month': _t('Par organisation / mois', 'Pro Organisation / Monat', 'Por organización / mes', 'Per organizzazione / mese', 'Per organisatie / maand'),
    '<span>Pilot</span>': _t('<span>Pilot</span>', '<span>Pilot</span>', '<span>Pilot</span>', '<span>Pilot</span>', '<span>Pilot</span>'),
    'On the Pilot plan': _t('Sur le forfait Pilot', 'Im Pilot-Tarif', 'En el plan Pilot', 'Nel piano Pilot', 'Op het Pilot-abonnement'),
    'Flat monthly price per organization. 14-day free trial, no card required.': _t(
        'Prix mensuel forfaitaire par organisation. Essai gratuit de 14 jours, sans carte.',
        'Pauschaler Monatspreis pro Organisation. 14 Tage kostenlos testen, keine Karte erforderlich.',
        'Precio mensual fijo por organización. Prueba gratuita de 14 días, sin tarjeta.',
        'Prezzo mensile fisso per organizzazione. Prova gratuita di 14 giorni, senza carta.',
        'Vast maandbedrag per organisatie. Gratis proefperiode van 14 dagen, geen kaart nodig.'),
    'Flat monthly price per organization (Pilot plan). 14-day free trial, no card required.': _t(
        "Prix mensuel forfaitaire par organisation (offre Pilot). Essai gratuit de 14 jours, sans carte.",
        'Pauschaler Monatspreis pro Organisation (Pilot-Tarif). 14 Tage kostenlos testen, keine Karte erforderlich.',
        'Precio mensual fijo por organización (plan Pilot). Prueba gratuita de 14 días, sin tarjeta.',
        'Prezzo mensile fisso per organizzazione (piano Pilot). Prova gratuita di 14 giorni, senza carta.',
        'Vast maandbedrag per organisatie (Pilot-abonnement). Gratis proefperiode van 14 dagen, geen kaart nodig.'),
    'Live KPIs &amp; custom dashboards': _t('KPI en direct &amp; tableaux de bord personnalisés', 'Live-KPIs &amp; individuelle Dashboards', 'KPI en directo &amp; paneles personalizados', 'KPI in tempo reale &amp; dashboard personalizzate', "Live KPI's &amp; aangepaste dashboards"),
    'Alerts &amp; automated workflows': _t('Alertes &amp; flux de travail automatisés', 'Warnungen &amp; automatisierte Workflows', 'Alertas &amp; flujos de trabajo automatizados', 'Avvisi &amp; flussi di lavoro automatizzati', 'Meldingen &amp; geautomatiseerde workflows'),
    'Reporting &amp; exports': _t('Reporting &amp; exports', 'Reporting &amp; Exporte', 'Informes &amp; exportaciones', 'Reporting &amp; esportazioni', 'Rapportage &amp; exports'),
    # Capabilities
    'Everything you need to run operations live': _t(
        "Tout ce qu'il faut pour piloter vos opérations en direct",
        'Alles, was Sie brauchen, um den Betrieb live zu steuern',
        'Todo lo que necesita para gestionar las operaciones en directo',
        'Tutto ciò che serve per gestire le operazioni in tempo reale',
        'Alles wat u nodig hebt om operaties live te draaien'),
    'From high-level health to the single alert that needs attention right now.': _t(
        "De la santé globale à l'unique alerte qui exige votre attention maintenant.",
        'Vom Gesamtzustand bis zur einzelnen Warnung, die jetzt Aufmerksamkeit braucht.',
        'Desde el estado general hasta la única alerta que necesita atención ahora mismo.',
        'Dallo stato generale al singolo avviso che richiede attenzione proprio ora.',
        'Van het totaalbeeld tot de ene melding die nu aandacht nodig heeft.'),
    'Live dashboards': _t('Tableaux de bord en direct', 'Live-Dashboards', 'Paneles en directo', 'Dashboard in tempo reale', 'Live dashboards'),
    'Build dashboards from any data on the grid. Metrics refresh in real time — no exports, no stale reports.': _t(
        "Créez des tableaux de bord à partir de n'importe quelle donnée de la grille. Les indicateurs se rafraîchissent en temps réel — aucun export, aucun rapport périmé.",
        'Erstellen Sie Dashboards aus beliebigen Daten im Grid. Kennzahlen aktualisieren sich in Echtzeit — keine Exporte, keine veralteten Berichte.',
        'Cree paneles a partir de cualquier dato de la cuadrícula. Las métricas se actualizan en tiempo real — sin exportaciones, sin informes obsoletos.',
        'Crea dashboard da qualsiasi dato della griglia. Le metriche si aggiornano in tempo reale — nessuna esportazione, nessun report obsoleto.',
        "Bouw dashboards uit alle data op het grid. Metrieken vernieuwen in realtime — geen exports, geen verouderde rapporten."),
    'Alerts &amp; thresholds': _t('Alertes &amp; seuils', 'Warnungen &amp; Schwellenwerte', 'Alertas &amp; umbrales', 'Avvisi &amp; soglie', 'Meldingen &amp; drempels'),
    "Set thresholds on any metric and get notified the moment they're crossed — in-app, by email, or to your team channel.": _t(
        "Définissez des seuils sur n'importe quel indicateur et soyez notifié dès qu'ils sont franchis — dans l'application, par e-mail ou sur le canal de votre équipe.",
        'Legen Sie Schwellenwerte für jede Kennzahl fest und werden Sie benachrichtigt, sobald sie überschritten werden — in der App, per E-Mail oder in Ihrem Team-Kanal.',
        'Fije umbrales en cualquier métrica y reciba un aviso en cuanto se superen — en la app, por correo o en el canal de su equipo.',
        "Imposta soglie su qualsiasi metrica e ricevi una notifica nel momento in cui vengono superate — nell'app, via e-mail o sul canale del tuo team.",
        'Stel drempels in op elke metriek en word gewaarschuwd zodra ze worden overschreden — in de app, per e-mail of naar uw teamkanaal.'),
    'Automated workflows': _t('Flux de travail automatisés', 'Automatisierte Workflows', 'Flujos de trabajo automatizados', 'Flussi di lavoro automatizzati', 'Geautomatiseerde workflows'),
    'Turn a signal into an action: open a task, notify an owner, or trigger a job in another app — automatically.': _t(
        "Transformez un signal en action : ouvrir une tâche, prévenir un responsable ou déclencher un traitement dans une autre application — automatiquement.",
        'Machen Sie aus einem Signal eine Aktion: eine Aufgabe öffnen, einen Verantwortlichen benachrichtigen oder einen Vorgang in einer anderen App auslösen — automatisch.',
        'Convierta una señal en una acción: abrir una tarea, avisar a un responsable o activar un proceso en otra app — automáticamente.',
        "Trasforma un segnale in un'azione: aprire un'attività, avvisare un responsabile o avviare un processo in un'altra app — automaticamente.",
        'Maak van een signaal een actie: een taak openen, een eigenaar waarschuwen of een taak in een andere app starten — automatisch.'),
    'Build the reports your team needs and export them anytime — no more digging through a dozen spreadsheets.': _t(
        "Créez les rapports dont votre équipe a besoin et exportez-les à tout moment — fini de fouiller dans une douzaine de tableurs.",
        'Erstellen Sie die Berichte, die Ihr Team braucht, und exportieren Sie sie jederzeit — kein Wühlen mehr in einem Dutzend Tabellen.',
        'Cree los informes que su equipo necesita y expórtelos cuando quiera — se acabó rebuscar en una docena de hojas de cálculo.',
        'Crea i report di cui il tuo team ha bisogno ed esportali quando vuoi — niente più ricerche in una dozzina di fogli di calcolo.',
        'Bouw de rapporten die uw team nodig heeft en exporteer ze wanneer u wilt — geen gespit meer door een dozijn spreadsheets.'),
    'Custom views &amp; KPIs': _t('Vues personnalisées &amp; KPI', 'Individuelle Ansichten &amp; KPIs', 'Vistas personalizadas &amp; KPI', 'Viste personalizzate &amp; KPI', "Aangepaste weergaven &amp; KPI's"),
    'Define the KPIs that matter to your business and pin them into role-specific views for each team.': _t(
        "Définissez les KPI qui comptent pour votre entreprise et épinglez-les dans des vues adaptées au rôle de chaque équipe.",
        'Definieren Sie die KPIs, die für Ihr Unternehmen zählen, und heften Sie sie in rollenspezifische Ansichten für jedes Team.',
        'Defina los KPI que importan a su negocio y fíjelos en vistas específicas para el rol de cada equipo.',
        'Definisci i KPI che contano per la tua azienda e fissali in viste specifiche per il ruolo di ogni team.',
        "Bepaal de KPI's die er voor uw bedrijf toe doen en zet ze vast in rolspecifieke weergaven voor elk team."),
    'Audit trail': _t("Piste d'audit", 'Audit-Trail', 'Registro de auditoría', 'Traccia di audit', 'Audittrail'),
    'Every change, alert, and action is logged. Know what happened, when, and who acted on it.': _t(
        "Chaque modification, alerte et action est enregistrée. Sachez ce qui s'est passé, quand et qui est intervenu.",
        'Jede Änderung, Warnung und Aktion wird protokolliert. Wissen Sie, was passiert ist, wann und wer gehandelt hat.',
        'Cada cambio, alerta y acción queda registrado. Sepa qué pasó, cuándo y quién actuó.',
        'Ogni modifica, avviso e azione viene registrato. Sappi cosa è successo, quando e chi è intervenuto.',
        'Elke wijziging, melding en actie wordt vastgelegd. Weet wat er gebeurde, wanneer en wie handelde.'),
    # Use cases
    'Made for the people who keep things running': _t(
        'Conçu pour ceux qui font tourner la machine',
        'Gemacht für die Menschen, die den Laden am Laufen halten',
        'Hecho para quienes mantienen todo en marcha',
        'Fatto per chi tiene tutto in funzione',
        'Gemaakt voor de mensen die de boel draaiende houden'),
    'Operations leads': _t('Responsables des opérations', 'Betriebsleiter', 'Responsables de operaciones', 'Responsabili operativi', 'Operationeel leidinggevenden'),
    'Watch throughput, SLAs, and exceptions across the whole business without waiting on a weekly report.': _t(
        "Suivez le débit, les SLA et les exceptions dans toute l'entreprise sans attendre un rapport hebdomadaire.",
        'Behalten Sie Durchsatz, SLAs und Ausnahmen im gesamten Unternehmen im Blick, ohne auf einen Wochenbericht zu warten.',
        'Vigile el rendimiento, los SLA y las excepciones en todo el negocio sin esperar a un informe semanal.',
        "Monitora throughput, SLA ed eccezioni in tutta l'azienda senza aspettare un report settimanale.",
        "Volg doorvoer, SLA's en uitzonderingen in het hele bedrijf zonder op een weekrapport te wachten."),
    'Track cash, receivables, and spend live — and get alerted before a number becomes a problem.': _t(
        "Suivez la trésorerie, les créances et les dépenses en direct — et soyez alerté avant qu'un chiffre ne devienne un problème.",
        'Verfolgen Sie Liquidität, Forderungen und Ausgaben live — und werden Sie gewarnt, bevor eine Zahl zum Problem wird.',
        'Controle la caja, los cobros y el gasto en directo — y reciba un aviso antes de que una cifra sea un problema.',
        'Monitora liquidità, crediti e spese in tempo reale — e ricevi un avviso prima che un numero diventi un problema.',
        'Volg kas, vorderingen en uitgaven live — en word gewaarschuwd voordat een getal een probleem wordt.'),
    'Executives': _t('Dirigeants', 'Führungskräfte', 'Directivos', 'Dirigenti', 'Bestuurders'),
    'One screen for the health of the company, with the ability to drill into any metric down to the record.': _t(
        "Un seul écran pour la santé de l'entreprise, avec la possibilité d'explorer n'importe quel indicateur jusqu'à l'enregistrement.",
        'Ein Bildschirm für die Gesundheit des Unternehmens, mit der Möglichkeit, jede Kennzahl bis auf den einzelnen Datensatz aufzuschlüsseln.',
        'Una sola pantalla para la salud de la empresa, con la posibilidad de profundizar en cualquier métrica hasta el registro.',
        'Una sola schermata per lo stato dell\'azienda, con la possibilità di analizzare qualsiasi metrica fino al singolo record.',
        'Eén scherm voor de gezondheid van het bedrijf, met de mogelijkheid om elke metriek tot op het record uit te diepen.'),
    # Region
    'GCC-native finance, Arabic-first, and multi-currency — Command Center adapts to your market.': _t(
        "Finance native GCC, priorité à l'arabe et multidevise — Command Center s'adapte à votre marché.",
        'GCC-native Finanzen, Arabisch zuerst und mehrwährungsfähig — Command Center passt sich Ihrem Markt an.',
        'Finanzas nativas GCC, árabe primero y multidivisa — Command Center se adapta a su mercado.',
        'Finanza nativa GCC, arabo prima di tutto e multivaluta — Command Center si adatta al tuo mercato.',
        'GCC-native financiën, Arabisch eerst en multivaluta — Command Center past zich aan uw markt aan.'),
    'Tax &amp; Zakat': _t('Impôts &amp; Zakat', 'Steuern &amp; Zakat', 'Impuestos &amp; Zakat', 'Imposte &amp; Zakat', 'Belasting &amp; Zakat'),
    'Tax and Zakat as a first-class group in your P&amp;L and executive snapshot — GCC finance, out of the box.': _t(
        "Impôts et Zakat traités comme un groupe à part entière dans votre P&amp;L et votre synthèse pour la direction — finance GCC, prête à l'emploi.",
        'Steuern und Zakat als vollwertige Gruppe in Ihrer P&amp;L und Ihrer Management-Übersicht — GCC-Finanzen, sofort einsatzbereit.',
        'Impuestos y Zakat como un grupo de primer nivel en su P&amp;L y su resumen ejecutivo — finanzas GCC, listas para usar.',
        "Imposte e Zakat come gruppo di primo livello nel tuo P&amp;L e nella panoramica per la direzione — finanza GCC, pronta all'uso.",
        'Belasting en Zakat als een volwaardige groep in uw P&amp;L en uw directieoverzicht — GCC-financiën, direct klaar voor gebruik.'),
    'VAT-ready': _t('Prêt pour la TVA', 'MwSt.-bereit', 'Preparado para el IVA', "Pronto per l'IVA", 'Btw-klaar'),
    'VAT tracked alongside your other liabilities, with a compliance and governance module to keep filings on track.': _t(
        "La TVA suivie aux côtés de vos autres passifs, avec un module de conformité et de gouvernance pour tenir vos déclarations à jour.",
        'Die MwSt. wird neben Ihren anderen Verbindlichkeiten verfolgt, mit einem Compliance- und Governance-Modul, das Ihre Meldungen auf Kurs hält.',
        'El IVA se controla junto a sus demás pasivos, con un módulo de cumplimiento y gobernanza para mantener las declaraciones al día.',
        "L'IVA viene monitorata insieme alle altre passività, con un modulo di conformità e governance per tenere in ordine le dichiarazioni.",
        'De btw wordt naast uw andere verplichtingen gevolgd, met een compliance- en governancemodule om aangiften op koers te houden.'),
    'Arabic &amp; multi-currency': _t('Arabe &amp; multidevise', 'Arabisch &amp; Mehrwährung', 'Árabe &amp; multidivisa', 'Arabo &amp; multivaluta', 'Arabisch &amp; multivaluta'),
    'Arabic, right-to-left throughout, with reporting in SAR, USD, EUR or your own currency.': _t(
        "L'arabe, de droite à gauche partout, avec un reporting en SAR, USD, EUR ou votre propre devise.",
        'Arabisch, durchgängig von rechts nach links, mit Reporting in SAR, USD, EUR oder Ihrer eigenen Währung.',
        'Árabe, de derecha a izquierda en todo, con informes en SAR, USD, EUR o su propia moneda.',
        'Arabo, da destra a sinistra ovunque, con reporting in SAR, USD, EUR o nella tua valuta.',
        'Arabisch, overal van rechts naar links, met rapportage in SAR, USD, EUR of uw eigen valuta.'),
    'Country-aware console': _t('Console adaptée à chaque pays', 'Länderbewusste Konsole', 'Consola adaptada al país', 'Console consapevole del paese', 'Landbewuste console'),
    'The console offers the right languages and a sensible default timezone for each market automatically.': _t(
        "La console propose automatiquement les bonnes langues et un fuseau horaire par défaut pertinent pour chaque marché.",
        'Die Konsole bietet automatisch die passenden Sprachen und eine sinnvolle Standard-Zeitzone für jeden Markt.',
        'La consola ofrece automáticamente los idiomas adecuados y una zona horaria por defecto sensata para cada mercado.',
        'La console offre automaticamente le lingue giuste e un fuso orario predefinito sensato per ogni mercato.',
        'De console biedt automatisch de juiste talen en een verstandige standaardtijdzone voor elke markt.'),
    # FulcrumGrid family
    'Command Center is one of several FulcrumGrid apps, each built to the same standard. Explore the others built for your operations.': _t(
        "Command Center est l'une des nombreuses applications FulcrumGrid, toutes conçues selon le même standard. Découvrez les autres, pensées pour vos opérations.",
        'Command Center ist eine von mehreren FulcrumGrid-Apps, jede nach demselben Standard gebaut. Entdecken Sie die anderen, gebaut für Ihren Betrieb.',
        'Command Center es una de las varias apps de FulcrumGrid, todas creadas con el mismo estándar. Explore las demás, pensadas para sus operaciones.',
        'Command Center è una delle numerose app FulcrumGrid, tutte costruite secondo lo stesso standard. Esplora le altre, pensate per le tue operazioni.',
        'Command Center is een van de vele FulcrumGrid-apps, elk gebouwd volgens dezelfde standaard. Ontdek de andere, gebouwd voor uw operatie.'),
    'Receivables &amp; payments': _t('Créances &amp; paiements', 'Forderungen &amp; Zahlungen', 'Cobros &amp; pagos', 'Crediti &amp; pagamenti', 'Vorderingen &amp; betalingen'),
    # CTA
    'Put your operations<br />on one screen.': _t(
        'Réunissez vos opérations<br />sur un seul écran.',
        'Bringen Sie Ihren Betrieb<br />auf einen Bildschirm.',
        'Ponga sus operaciones<br />en una sola pantalla.',
        "Metti le tue operazioni<br />su un'unica schermata.",
        'Zet uw operatie<br />op één scherm.'),
    "See Command Center running on your data. We'll walk you through it.": _t(
        'Voyez Command Center fonctionner sur vos données. Nous vous accompagnons pas à pas.',
        'Sehen Sie Command Center mit Ihren Daten in Aktion. Wir führen Sie Schritt für Schritt durch.',
        'Vea Command Center funcionando con sus datos. Le guiamos paso a paso.',
        'Guarda Command Center in funzione sui tuoi dati. Ti guidiamo passo dopo passo.',
        'Zie Command Center draaien op uw data. We leiden u er stap voor stap doorheen.'),
}
_CC.update(_SHARED)


# ---- Collection ----------------------------------------------------------
_COL = {
    # Meta
    "Collection is FulcrumGrid's receivables app — invoice tracking, automated reminders, payment plans, and reconciliation to recover revenue predictably.": _t(
        "Collection est l'application de gestion des créances de FulcrumGrid — suivi des factures, relances automatisées, plans de paiement et rapprochement pour recouvrer vos revenus de façon prévisible.",
        'Collection ist die Forderungs-App von FulcrumGrid — Rechnungsverfolgung, automatisierte Erinnerungen, Zahlungspläne und Abgleich, um Umsätze planbar einzutreiben.',
        'Collection es la app de cobros de FulcrumGrid — seguimiento de facturas, recordatorios automatizados, planes de pago y conciliación para recuperar ingresos de forma previsible.',
        "Collection è l'app di gestione crediti di FulcrumGrid — monitoraggio delle fatture, solleciti automatizzati, piani di pagamento e riconciliazione per recuperare i ricavi in modo prevedibile.",
        'Collection is de debiteuren-app van FulcrumGrid — factuuropvolging, geautomatiseerde herinneringen, betalingsplannen en reconciliatie om omzet voorspelbaar te innen.'),
    'Receivables and payments: invoice tracking, automated reminders, payment plans, and reconciliation.': _t(
        'Créances et paiements : suivi des factures, relances automatisées, plans de paiement et rapprochement.',
        'Forderungen und Zahlungen: Rechnungsverfolgung, automatisierte Erinnerungen, Zahlungspläne und Abgleich.',
        'Cobros y pagos: seguimiento de facturas, recordatorios automatizados, planes de pago y conciliación.',
        'Crediti e pagamenti: monitoraggio delle fatture, solleciti automatizzati, piani di pagamento e riconciliazione.',
        'Vorderingen en betalingen: factuuropvolging, geautomatiseerde herinneringen, betalingsplannen en reconciliatie.'),
    # Hero
    'Get paid, predictably.': _t(
        'Soyez payé, de façon prévisible.',
        'Werden Sie bezahlt, planbar.',
        'Cobre, de forma previsible.',
        'Fatti pagare, in modo prevedibile.',
        'Word betaald, voorspelbaar.'),
    'Collection turns messy receivables into a clear, auditable process. Track every invoice, automate the follow-ups, offer payment plans, and reconcile the money coming in — so revenue lands on time and nothing falls through the cracks.': _t(
        "Collection transforme des créances désordonnées en un processus clair et auditable. Suivez chaque facture, automatisez les relances, proposez des plans de paiement et rapprochez l'argent qui rentre — pour que les revenus arrivent à temps et que rien ne passe entre les mailles du filet.",
        'Collection macht aus unübersichtlichen Forderungen einen klaren, prüfbaren Prozess. Verfolgen Sie jede Rechnung, automatisieren Sie die Nachfassaktionen, bieten Sie Zahlungspläne an und gleichen Sie eingehende Zahlungen ab — damit Umsätze pünktlich eingehen und nichts durchs Raster fällt.',
        'Collection convierte unos cobros caóticos en un proceso claro y auditable. Siga cada factura, automatice el seguimiento, ofrezca planes de pago y concilie el dinero que entra — para que los ingresos lleguen a tiempo y nada se escape.',
        'Collection trasforma crediti disordinati in un processo chiaro e verificabile. Monitora ogni fattura, automatizza i solleciti, offri piani di pagamento e riconcilia il denaro in entrata — così i ricavi arrivano in tempo e nulla sfugge.',
        'Collection maakt van rommelige vorderingen een helder, controleerbaar proces. Volg elke factuur, automatiseer de opvolging, bied betalingsplannen aan en verwerk het binnenkomende geld — zodat omzet op tijd binnenkomt en niets tussen wal en schip valt.'),
    'Open Collection': _t('Ouvrir Collection', 'Collection öffnen', 'Abrir Collection', 'Apri Collection', 'Collection openen'),
    # Pricing
    'Collection pricing': _t('Tarifs Collection', 'Collection Preise', 'Precios de Collection', 'Prezzi di Collection', 'Collection prijzen'),
    'Per workspace / month': _t('Par espace de travail / mois', 'Pro Workspace / Monat', 'Por espacio de trabajo / mes', 'Per spazio di lavoro / mese', 'Per werkruimte / maand'),
    '<span>Starter</span>': _t('<span>Starter</span>', '<span>Starter</span>', '<span>Starter</span>', '<span>Starter</span>', '<span>Starter</span>'),
    '<b>Free</b>': _t('<b>Gratuit</b>', '<b>Kostenlos</b>', '<b>Gratis</b>', '<b>Gratis</b>', '<b>Gratis</b>'),
    'On the Starter plan': _t('Sur le forfait Starter', 'Im Starter-Tarif', 'En el plan Starter', 'Nel piano Starter', 'Op het Starter-abonnement'),
    'Starter is free — paid plans from SAR 370 / month.': _t(
        'Starter est gratuit — offres payantes à partir de SAR 370 / mois.',
        'Starter ist kostenlos — kostenpflichtige Tarife ab SAR 370 / Monat.',
        'Starter es gratis — planes de pago desde SAR 370 / mes.',
        'Starter è gratis — piani a pagamento da SAR 370 / mese.',
        'Starter is gratis — betaalde abonnementen vanaf SAR 370 / maand.'),
    'Invoice &amp; ledger tracking': _t('Suivi des factures &amp; du grand livre', 'Rechnungs- &amp; Buchungsverfolgung', 'Seguimiento de facturas &amp; libro mayor', 'Monitoraggio fatture &amp; registro contabile', 'Factuur- &amp; grootboekopvolging'),
    'Automated reminders &amp; plans': _t('Relances &amp; plans automatisés', 'Automatisierte Erinnerungen &amp; Pläne', 'Recordatorios &amp; planes automatizados', 'Solleciti &amp; piani automatizzati', 'Geautomatiseerde herinneringen &amp; plannen'),
    'Payment reconciliation': _t('Rapprochement des paiements', 'Zahlungsabgleich', 'Conciliación de pagos', 'Riconciliazione dei pagamenti', 'Betalingsreconciliatie'),
    # Capabilities
    'From invoice to paid, in one place': _t(
        'De la facture au paiement, au même endroit',
        'Von der Rechnung bis zur Zahlung, an einem Ort',
        'De la factura al cobro, en un solo lugar',
        'Dalla fattura al pagamento, in un unico posto',
        'Van factuur tot betaald, op één plek'),
    'Every step of the receivables cycle, tracked and automated.': _t(
        'Chaque étape du cycle des créances, suivie et automatisée.',
        'Jeder Schritt des Forderungszyklus, verfolgt und automatisiert.',
        'Cada paso del ciclo de cobros, controlado y automatizado.',
        'Ogni fase del ciclo dei crediti, monitorata e automatizzata.',
        'Elke stap van de debiteurencyclus, gevolgd en geautomatiseerd.'),
    'A live view of every invoice — who owes what, since when, and where each one stands.': _t(
        "Une vue en direct de chaque facture — qui doit quoi, depuis quand et où en est chacune.",
        'Eine Live-Ansicht jeder Rechnung — wer was schuldet, seit wann und wo jede steht.',
        'Una vista en directo de cada factura — quién debe qué, desde cuándo y en qué situación está cada una.',
        'Una vista in tempo reale di ogni fattura — chi deve cosa, da quando e a che punto è ciascuna.',
        'Een live-weergave van elke factuur — wie wat verschuldigd is, sinds wanneer en waar elke staat.'),
    'Automated reminders': _t('Relances automatisées', 'Automatisierte Erinnerungen', 'Recordatorios automatizados', 'Solleciti automatizzati', 'Geautomatiseerde herinneringen'),
    'Schedule polite, escalating follow-ups by email or SMS — sent automatically so no one has to chase manually.': _t(
        "Programmez des relances polies et progressives par e-mail ou SMS — envoyées automatiquement, pour que personne n'ait à relancer à la main.",
        'Planen Sie höfliche, eskalierende Nachfassaktionen per E-Mail oder SMS — automatisch versendet, sodass niemand manuell nachfassen muss.',
        'Programe seguimientos corteses y progresivos por correo o SMS — enviados automáticamente para que nadie tenga que reclamar a mano.',
        'Pianifica solleciti cortesi e progressivi via e-mail o SMS — inviati automaticamente, così nessuno deve rincorrere manualmente.',
        'Plan beleefde, oplopende opvolgingen per e-mail of sms — automatisch verzonden, zodat niemand handmatig hoeft na te jagen.'),
    'Payment plans': _t('Plans de paiement', 'Zahlungspläne', 'Planes de pago', 'Piani di pagamento', 'Betalingsplannen'),
    'Split a balance into scheduled installments and let Collection track each one to completion.': _t(
        'Divisez un solde en échéances programmées et laissez Collection suivre chacune jusqu\'à son terme.',
        'Teilen Sie einen Saldo in geplante Raten auf und lassen Sie Collection jede bis zum Abschluss verfolgen.',
        'Divida un saldo en cuotas programadas y deje que Collection siga cada una hasta el final.',
        'Suddividi un saldo in rate programmate e lascia che Collection segua ciascuna fino al completamento.',
        'Splits een saldo in geplande termijnen en laat Collection elk tot voltooiing volgen.'),
    "Match incoming payments to invoices automatically and flag anything that doesn't line up.": _t(
        'Rapprochez automatiquement les paiements entrants des factures et signalez tout ce qui ne concorde pas.',
        'Ordnen Sie eingehende Zahlungen automatisch den Rechnungen zu und markieren Sie alles, was nicht passt.',
        'Concilie automáticamente los pagos entrantes con las facturas y señale todo lo que no cuadre.',
        'Abbina automaticamente i pagamenti in entrata alle fatture e segnala tutto ciò che non torna.',
        'Koppel binnenkomende betalingen automatisch aan facturen en markeer alles wat niet klopt.'),
    'Aging &amp; risk reports': _t("Rapports d'ancienneté &amp; de risque", 'Fälligkeits- &amp; Risikoberichte', 'Informes de antigüedad &amp; riesgo', 'Report di scadenza &amp; rischio', 'Ouderdoms- &amp; risicorapporten'),
    "See receivables by age bucket, spot at-risk accounts early, and forecast the cash that's actually coming.": _t(
        "Visualisez les créances par tranche d'ancienneté, repérez tôt les comptes à risque et prévoyez la trésorerie qui va réellement rentrer.",
        'Sehen Sie Forderungen nach Altersklasse, erkennen Sie gefährdete Konten frühzeitig und prognostizieren Sie die tatsächlich eingehende Liquidität.',
        'Vea los cobros por tramo de antigüedad, detecte pronto las cuentas en riesgo y prevea la caja que realmente va a entrar.',
        'Visualizza i crediti per fascia di anzianità, individua in anticipo i conti a rischio e prevedi la liquidità che arriverà davvero.',
        'Bekijk vorderingen per ouderdomscategorie, spot risicovolle accounts vroeg en voorspel het geld dat echt binnenkomt.'),
    'Disputes &amp; notes': _t('Litiges &amp; notes', 'Streitfälle &amp; Notizen', 'Disputas &amp; notas', 'Contestazioni &amp; note', 'Geschillen &amp; notities'),
    'Log disputes, promises to pay, and account notes against each record — a full history for every customer.': _t(
        "Consignez les litiges, les promesses de paiement et les notes de compte sur chaque enregistrement — un historique complet pour chaque client.",
        'Erfassen Sie Streitfälle, Zahlungszusagen und Kontonotizen zu jedem Datensatz — eine vollständige Historie für jeden Kunden.',
        'Registre disputas, promesas de pago y notas de cuenta en cada registro — un historial completo de cada cliente.',
        'Registra contestazioni, promesse di pagamento e note sul conto per ogni record — uno storico completo per ogni cliente.',
        'Leg geschillen, betalingstoezeggingen en accountnotities vast bij elk record — een volledige historie voor elke klant.'),
    # Use cases
    'For everyone chasing revenue': _t(
        'Pour tous ceux qui courent après les revenus',
        'Für alle, die Umsätzen hinterherlaufen',
        'Para todos los que persiguen ingresos',
        'Per tutti coloro che rincorrono i ricavi',
        'Voor iedereen die achter omzet aan zit'),
    'Accounts receivable': _t('Comptes clients', 'Debitorenbuchhaltung', 'Cuentas por cobrar', 'Contabilità clienti', 'Debiteurenadministratie'),
    'Work the whole book from one queue instead of a stack of spreadsheets and sticky notes.': _t(
        "Traitez tout le portefeuille depuis une seule file d'attente au lieu d'une pile de tableurs et de pense-bêtes.",
        'Bearbeiten Sie das gesamte Portfolio aus einer einzigen Warteschlange statt aus einem Stapel Tabellen und Klebezetteln.',
        'Gestione toda la cartera desde una sola cola en lugar de una pila de hojas de cálculo y notas adhesivas.',
        "Gestisci l'intero portafoglio da un'unica coda invece che da una pila di fogli di calcolo e foglietti adesivi.",
        'Werk de hele portefeuille vanuit één wachtrij in plaats van een stapel spreadsheets en plaknotities.'),
    'Finance teams': _t('Équipes financières', 'Finanzteams', 'Equipos de finanzas', 'Team finanziari', 'Financiële teams'),
    'Cut days-sales-outstanding and forecast cash with confidence backed by live data.': _t(
        'Réduisez le délai moyen de recouvrement et prévoyez la trésorerie en toute confiance, appuyé sur des données en direct.',
        'Senken Sie die Außenstandsdauer (DSO) und prognostizieren Sie die Liquidität mit Zuversicht, gestützt auf Live-Daten.',
        'Reduzca el periodo medio de cobro y prevea la caja con confianza, respaldado por datos en directo.',
        'Riduci i giorni di incasso (DSO) e prevedi la liquidità con sicurezza, sulla base di dati in tempo reale.',
        'Verkort de gemiddelde incassotermijn (DSO) en voorspel de kas met vertrouwen, onderbouwd met live data.'),
    'Growing businesses': _t('Entreprises en croissance', 'Wachsende Unternehmen', 'Empresas en crecimiento', 'Aziende in crescita', 'Groeiende bedrijven'),
    'Professional, consistent collections without hiring a whole department to run them.': _t(
        'Un recouvrement professionnel et cohérent sans embaucher tout un service pour le gérer.',
        'Professionelles, konsistentes Inkasso, ohne eine ganze Abteilung dafür einzustellen.',
        'Cobros profesionales y coherentes sin contratar todo un departamento para gestionarlos.',
        'Un recupero crediti professionale e coerente senza assumere un intero reparto per gestirlo.',
        'Professionele, consistente incasso zonder een hele afdeling aan te nemen om die te draaien.'),
    # Region
    'Multi-currency, Arabic-first, and privacy-ready — Collection works the way your market does.': _t(
        "Multidevise, priorité à l'arabe et prêt pour la confidentialité — Collection fonctionne comme votre marché.",
        'Mehrwährungsfähig, Arabisch zuerst und datenschutzbereit — Collection arbeitet so, wie Ihr Markt es tut.',
        'Multidivisa, árabe primero y preparado para la privacidad — Collection funciona como lo hace su mercado.',
        'Multivaluta, arabo prima di tutto e pronto per la privacy — Collection funziona come il tuo mercato.',
        'Multivaluta, Arabisch eerst en privacyklaar — Collection werkt zoals uw markt werkt.'),
    'Multi-currency': _t('Multidevise', 'Mehrwährung', 'Multidivisa', 'Multivaluta', 'Multivaluta'),
    'Receivables and payments carry their own ISO currency, so you collect in SAR, USD, EUR or any currency your customers pay in.': _t(
        "Les créances et les paiements portent leur propre devise ISO, pour que vous encaissiez en SAR, USD, EUR ou dans toute devise dans laquelle vos clients paient.",
        'Forderungen und Zahlungen führen ihre eigene ISO-Währung, sodass Sie in SAR, USD, EUR oder jeder Währung einziehen, in der Ihre Kunden zahlen.',
        'Los cobros y pagos llevan su propia moneda ISO, de modo que cobra en SAR, USD, EUR o cualquier moneda en la que paguen sus clientes.',
        'Crediti e pagamenti portano la propria valuta ISO, così incassi in SAR, USD, EUR o in qualsiasi valuta con cui pagano i tuoi clienti.',
        'Vorderingen en betalingen dragen hun eigen ISO-valuta, zodat u int in SAR, USD, EUR of elke valuta waarin uw klanten betalen.'),
    'Arabic &amp; debtor portal': _t('Arabe &amp; portail débiteur', 'Arabisch &amp; Schuldnerportal', 'Árabe &amp; portal del deudor', 'Arabo &amp; portale del debitore', 'Arabisch &amp; debiteurenportaal'),
    'Arabic, right-to-left throughout, including the self-service portal where debtors view balances and settle.': _t(
        "L'arabe, de droite à gauche partout, y compris le portail en libre-service où les débiteurs consultent leurs soldes et règlent.",
        'Arabisch, durchgängig von rechts nach links, einschließlich des Self-Service-Portals, in dem Schuldner Salden einsehen und begleichen.',
        'Árabe, de derecha a izquierda en todo, incluido el portal de autoservicio donde los deudores consultan saldos y pagan.',
        'Arabo, da destra a sinistra ovunque, incluso il portale self-service in cui i debitori consultano i saldi e pagano.',
        'Arabisch, overal van rechts naar links, inclusief het selfserviceportaal waar debiteuren saldi bekijken en betalen.'),
    '&amp; data-subject rights': _t(
        '&amp; droits des personnes concernées',
        '&amp; Rechte der betroffenen Personen',
        '&amp; derechos de los interesados',
        "&amp; diritti dell'interessato",
        '&amp; rechten van betrokkenen'),
    'Built-in data-subject request handling helps you meet GDPR-style privacy obligations wherever you operate.': _t(
        'La gestion intégrée des demandes des personnes concernées vous aide à respecter les obligations de confidentialité de type RGPD partout où vous opérez.',
        'Die integrierte Bearbeitung von Betroffenenanfragen hilft Ihnen, DSGVO-ähnliche Datenschutzpflichten überall dort zu erfüllen, wo Sie tätig sind.',
        'La gestión integrada de solicitudes de los interesados le ayuda a cumplir obligaciones de privacidad tipo RGPD dondequiera que opere.',
        'La gestione integrata delle richieste degli interessati ti aiuta a rispettare gli obblighi sulla privacy in stile GDPR ovunque operi.',
        'De ingebouwde afhandeling van verzoeken van betrokkenen helpt u te voldoen aan AVG-achtige privacyverplichtingen waar u ook actief bent.'),
    'Jurisdiction-tagged legal': _t('Juridique étiqueté par juridiction', 'Rechtsfälle mit Zuständigkeits-Tag', 'Legal etiquetado por jurisdicción', 'Legale con tag di giurisdizione', 'Juridisch met jurisdictielabel'),
    'Tag each legal case with its jurisdiction, so escalations follow the rules of the market they belong to.': _t(
        "Étiquetez chaque dossier juridique avec sa juridiction, pour que les escalades suivent les règles du marché auquel elles appartiennent.",
        'Versehen Sie jeden Rechtsfall mit seiner Zuständigkeit, damit Eskalationen den Regeln des jeweiligen Marktes folgen.',
        'Etiquete cada caso legal con su jurisdicción, para que las escalaciones sigan las reglas del mercado al que pertenecen.',
        'Etichetta ogni caso legale con la sua giurisdizione, così le escalation seguono le regole del mercato a cui appartengono.',
        'Label elke juridische zaak met de bijbehorende jurisdictie, zodat escalaties de regels volgen van de markt waartoe ze behoren.'),
    # FulcrumGrid family
    'Collection is one of several FulcrumGrid apps, each built to the same standard. Explore the others built for your operations.': _t(
        "Collection est l'une des nombreuses applications FulcrumGrid, toutes conçues selon le même standard. Découvrez les autres, pensées pour vos opérations.",
        'Collection ist eine von mehreren FulcrumGrid-Apps, jede nach demselben Standard gebaut. Entdecken Sie die anderen, gebaut für Ihren Betrieb.',
        'Collection es una de las varias apps de FulcrumGrid, todas creadas con el mismo estándar. Explore las demás, pensadas para sus operaciones.',
        'Collection è una delle numerose app FulcrumGrid, tutte costruite secondo lo stesso standard. Esplora le altre, pensate per le tue operazioni.',
        'Collection is een van de vele FulcrumGrid-apps, elk gebouwd volgens dezelfde standaard. Ontdek de andere, gebouwd voor uw operatie.'),
    'Operations dashboard': _t('Tableau de bord des opérations', 'Betriebs-Dashboard', 'Panel de operaciones', 'Dashboard operativa', 'Operationeel dashboard'),
    # CTA
    'Recover revenue,<br />on autopilot.': _t(
        'Recouvrez vos revenus,<br />en pilote automatique.',
        'Holen Sie Umsätze zurück,<br />im Autopilot.',
        'Recupere ingresos,<br />en piloto automático.',
        'Recupera i ricavi,<br />con il pilota automatico.',
        'Haal omzet terug,<br />op de automatische piloot.'),
    'See how Collection shortens the path from invoice to paid.': _t(
        'Découvrez comment Collection raccourcit le chemin de la facture au paiement.',
        'Sehen Sie, wie Collection den Weg von der Rechnung zur Zahlung verkürzt.',
        'Vea cómo Collection acorta el camino de la factura al cobro.',
        'Scopri come Collection accorcia il percorso dalla fattura al pagamento.',
        'Zie hoe Collection het pad van factuur tot betaald verkort.'),
}
_COL.update(_SHARED)


PAGE = {
    '/products/command-center/': {
        'src': 'products/command-center/index.html',
        't': _CC,
    },
    '/products/collection/': {
        'src': 'products/collection/index.html',
        't': _COL,
    },
}
