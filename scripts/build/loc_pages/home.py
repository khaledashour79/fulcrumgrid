# -*- coding: utf-8 -*-
"""Translations for the homepage (/), new design system.

Keys are EXACT substrings of the committed English index.html (inline markup,
entities and glyphs preserved). Common chrome (nav, footer, buttons, tagline)
is handled by loc_catalog.COMMON and not repeated here. Brand/product names
(FulcrumGrid, Command Center, Collection, HR Suite, TMS, Voice, CRM) stay
English, as do technology proper nouns (SAP Business One, REST API v1,
Webhooks, Sandbox) and acronyms (MFA, SoD, TLS, ERP, GCC, UAE). The
interactive orbit hero is rendered by JavaScript (hero-orbit.js); its tile
names are product names, and its status/readout labels are read from the
data-l-* attributes localized below.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/': {
        'src': 'index.html',
        't': {
            # ---- Meta (title / description / og / twitter) ----
            "FulcrumGrid — One platform. Every operation.": _t(
                "FulcrumGrid — Une plateforme. Chaque opération.",
                "FulcrumGrid — Eine Plattform. Jeder Betrieb.",
                "FulcrumGrid — Una plataforma. Cada operación.",
                "FulcrumGrid — Una piattaforma. Ogni operazione.",
                "FulcrumGrid — Eén platform. Elke operatie."),
            "FulcrumGrid is the operational backbone for modern teams — HR Suite, Command Center, Collection and more: purpose-built business apps on one platform.": _t(
                "FulcrumGrid est l'épine dorsale opérationnelle des équipes modernes — HR Suite, Command Center, Collection et plus : des applications métier sur mesure sur une seule plateforme.",
                "FulcrumGrid ist das operative Rückgrat für moderne Teams — HR Suite, Command Center, Collection und mehr: zweckgebaute Business-Apps auf einer Plattform.",
                "FulcrumGrid es la columna vertebral operativa de los equipos modernos — HR Suite, Command Center, Collection y más: aplicaciones de negocio a medida en una sola plataforma.",
                "FulcrumGrid è la spina dorsale operativa dei team moderni — HR Suite, Command Center, Collection e altro: applicazioni aziendali su misura su un'unica piattaforma.",
                "FulcrumGrid is de operationele ruggengraat voor moderne teams — HR Suite, Command Center, Collection en meer: doelgerichte bedrijfsapps op één platform."),
            "HR Suite, Command Center, Collection, and more — purpose-built business apps from one team.": _t(
                "HR Suite, Command Center, Collection et plus — des applications métier sur mesure, d'une seule équipe.",
                "HR Suite, Command Center, Collection und mehr — zweckgebaute Business-Apps aus einer Hand.",
                "HR Suite, Command Center, Collection y más — aplicaciones de negocio a medida, de un solo equipo.",
                "HR Suite, Command Center, Collection e altro — applicazioni aziendali su misura, da un unico team.",
                "HR Suite, Command Center, Collection en meer — doelgerichte bedrijfsapps van één team."),

            # ---- Hero ----
            # Orbit hero (hero-orbit.js). "Coming soon" is covered by
            # loc_catalog.COMMON; attribute/markup context keeps the short
            # words ("Available", "Orbit") from rewriting other copy.
            "FIG. 01 — Apps in orbit": _t(
                "FIG. 01 — Les applications en orbite",
                "FIG. 01 — Apps im Orbit",
                "FIG. 01 — Apps en órbita",
                "FIG. 01 — App in orbita",
                "FIG. 01 — Apps in een baan"),
            "Hover to hold · select an app": _t(
                "Survolez pour figer · choisissez une application",
                "Zum Anhalten darüberfahren · App auswählen",
                "Pase el cursor para detener · elija una app",
                "Passa sopra per fermare · scegli un'app",
                "Beweeg erover om te pauzeren · kies een app"),
            '<i class="lg-live"></i>Available': _t(
                '<i class="lg-live"></i>Disponible',
                '<i class="lg-live"></i>Verfügbar',
                '<i class="lg-live"></i>Disponible',
                '<i class="lg-live"></i>Disponibile',
                '<i class="lg-live"></i>Beschikbaar'),
            'data-l-orbit="Orbit" data-l-held="Orbit held" data-l-live="Available"': _t(
                'data-l-orbit="Orbite" data-l-held="Orbite figée" data-l-live="Disponible"',
                'data-l-orbit="Orbit" data-l-held="Orbit angehalten" data-l-live="Verfügbar"',
                'data-l-orbit="Órbita" data-l-held="Órbita detenida" data-l-live="Disponible"',
                'data-l-orbit="Orbita" data-l-held="Orbita ferma" data-l-live="Disponibile"',
                'data-l-orbit="Baan" data-l-held="Baan gepauzeerd" data-l-live="Beschikbaar"'),
            "One platform.<br />Every <em>operation.</em>": _t(
                "Une plateforme.<br />Chaque <em>opération.</em>",
                "Eine Plattform.<br />Jeder <em>Betrieb.</em>",
                "Una plataforma.<br />Cada <em>operación.</em>",
                "Una piattaforma.<br />Ogni <em>operazione.</em>",
                "Eén platform.<br />Elke <em>operatie.</em>"),
            "A growing family of purpose-built business apps from one team — HR Suite, Command Center, Collection and more. Start with one today, and add more as you grow.": _t(
                "Une famille grandissante d'applications métier sur mesure, d'une seule équipe — HR Suite, Command Center, Collection et plus. Commencez par une aujourd'hui, et ajoutez-en d'autres à mesure que vous grandissez.",
                "Eine wachsende Familie zweckgebauter Business-Apps aus einer Hand — HR Suite, Command Center, Collection und mehr. Starten Sie heute mit einer und fügen Sie weitere hinzu, wenn Sie wachsen.",
                "Una familia creciente de aplicaciones de negocio a medida, de un solo equipo — HR Suite, Command Center, Collection y más. Empiece hoy con una y añada más a medida que crece.",
                "Una famiglia in crescita di applicazioni aziendali su misura, da un unico team — HR Suite, Command Center, Collection e altro. Inizia oggi con una e aggiungine altre man mano che cresci.",
                "Een groeiende familie doelgerichte bedrijfsapps van één team — HR Suite, Command Center, Collection en meer. Begin vandaag met één en voeg er meer toe naarmate u groeit."),
            "Explore the apps": _t(
                "Découvrir les applications", "Apps entdecken", "Explorar las apps",
                "Esplora le app", "Ontdek de apps"),

            # ---- 01 · Products ----
            "01 · The grid of apps": _t(
                "01 · La grille d'applications", "01 · Das Grid der Apps",
                "01 · La cuadrícula de apps", "01 · La griglia di app",
                "01 · Het grid van apps"),
            "Purpose-built apps for every operation.": _t(
                "Des applications sur mesure pour chaque opération.",
                "Zweckgebaute Apps für jeden Betrieb.",
                "Aplicaciones a medida para cada operación.",
                "App su misura per ogni operazione.",
                "Doelgerichte apps voor elke operatie."),
            "Each app solves a real problem on its own. Start with one today, and add more as you grow.": _t(
                "Chaque application résout à elle seule un vrai problème. Commencez par une aujourd'hui, et ajoutez-en d'autres à mesure que vous grandissez.",
                "Jede App löst für sich ein echtes Problem. Starten Sie heute mit einer und fügen Sie weitere hinzu, wenn Sie wachsen.",
                "Cada app resuelve por sí sola un problema real. Empiece hoy con una y añada más a medida que crece.",
                "Ogni app risolve da sola un problema reale. Inizia oggi con una e aggiungine altre man mano che cresci.",
                "Elke app lost op zichzelf een echt probleem op. Begin vandaag met één en voeg er meer toe naarmate u groeit."),
            '<span class="tag tag-outline">People</span>': _t(
                '<span class="tag tag-outline">Personnel</span>',
                '<span class="tag tag-outline">Personal</span>',
                '<span class="tag tag-outline">Personas</span>',
                '<span class="tag tag-outline">Persone</span>',
                '<span class="tag tag-outline">Personeel</span>'),
            '<span class="tag tag-outline">Operations</span>': _t(
                '<span class="tag tag-outline">Opérations</span>',
                '<span class="tag tag-outline">Betrieb</span>',
                '<span class="tag tag-outline">Operaciones</span>',
                '<span class="tag tag-outline">Operazioni</span>',
                '<span class="tag tag-outline">Operaties</span>'),
            '<span class="tag tag-outline">Receivables</span>': _t(
                '<span class="tag tag-outline">Créances</span>',
                '<span class="tag tag-outline">Forderungen</span>',
                '<span class="tag tag-outline">Cobros</span>',
                '<span class="tag tag-outline">Crediti</span>',
                '<span class="tag tag-outline">Vorderingen</span>'),
            "People operations from hire to retire. Manage employees, payroll, time off, and everything in between.": _t(
                "La gestion des personnes, de l'embauche au départ. Gérez les employés, la paie, les congés et tout le reste.",
                "Personalmanagement von der Einstellung bis zum Ruhestand. Verwalten Sie Mitarbeiter, Gehaltsabrechnung, Abwesenheiten und alles dazwischen.",
                "Gestión de personas, de la contratación a la jubilación. Gestione empleados, nóminas, ausencias y todo lo demás.",
                "Gestione del personale, dall'assunzione alla pensione. Gestisci dipendenti, buste paga, ferie e tutto il resto.",
                "Personeelsbeheer van aanwerving tot pensioen. Beheer medewerkers, loonadministratie, verlof en alles daartussenin."),
            "Real-time operations dashboard. Monitor every metric, workflow, and alert across your business from one screen.": _t(
                "Tableau de bord des opérations en temps réel. Surveillez chaque indicateur, flux de travail et alerte de votre entreprise depuis un seul écran.",
                "Echtzeit-Dashboard für den Betrieb. Überwachen Sie jede Kennzahl, jeden Workflow und jede Warnung Ihres Unternehmens von einem Bildschirm aus.",
                "Panel de operaciones en tiempo real. Supervise cada métrica, flujo de trabajo y alerta de su negocio desde una sola pantalla.",
                "Dashboard operativa in tempo reale. Monitora ogni metrica, flusso di lavoro e avviso della tua azienda da un'unica schermata.",
                "Realtime operationeel dashboard. Volg elke metriek, workflow en melding in uw bedrijf vanaf één scherm."),
            "Receivables and payments, handled. Track invoices, automate reminders, and get paid faster without the chase.": _t(
                "Créances et paiements, maîtrisés. Suivez les factures, automatisez les relances et soyez payé plus vite sans courir après.",
                "Forderungen und Zahlungen, im Griff. Verfolgen Sie Rechnungen, automatisieren Sie Erinnerungen und werden Sie schneller bezahlt — ohne Hinterherlaufen.",
                "Cobros y pagos, resueltos. Controle facturas, automatice recordatorios y cobre más rápido sin perseguir a nadie.",
                "Crediti e pagamenti, gestiti. Monitora le fatture, automatizza i solleciti e fatti pagare più in fretta senza rincorrere nessuno.",
                "Vorderingen en betalingen, geregeld. Volg facturen, automatiseer herinneringen en word sneller betaald zonder achtervolging."),
            "Explore HR Suite →": _t(
                "Découvrir HR Suite →", "HR Suite entdecken →", "Explorar HR Suite →",
                "Esplora HR Suite →", "Ontdek HR Suite →"),
            "Explore Command Center →": _t(
                "Découvrir Command Center →", "Command Center entdecken →",
                "Explorar Command Center →", "Esplora Command Center →",
                "Ontdek Command Center →"),
            "Explore Collection →": _t(
                "Découvrir Collection →", "Collection entdecken →", "Explorar Collection →",
                "Esplora Collection →", "Ontdek Collection →"),
            "On the roadmap": _t(
                "Sur la feuille de route", "Auf der Roadmap", "En la hoja de ruta",
                "Nella roadmap", "Op de roadmap"),
            '<span class="tag tag-outline">Inventory</span>': _t(
                '<span class="tag tag-outline">Inventaire</span>',
                '<span class="tag tag-outline">Lagerverwaltung</span>',
                '<span class="tag tag-outline">Inventario</span>',
                '<span class="tag tag-outline">Inventario</span>',
                '<span class="tag tag-outline">Voorraad</span>'),
            '<span class="tag tag-outline">Analytics</span>': _t(
                '<span class="tag tag-outline">Analytique</span>',
                '<span class="tag tag-outline">Analysen</span>',
                '<span class="tag tag-outline">Analítica</span>',
                '<span class="tag tag-outline">Analisi</span>',
                '<span class="tag tag-outline">Analyse</span>'),
            '<span class="tag tag-outline">Procurement</span>': _t(
                '<span class="tag tag-outline">Achats</span>',
                '<span class="tag tag-outline">Beschaffung</span>',
                '<span class="tag tag-outline">Compras</span>',
                '<span class="tag tag-outline">Approvvigionamento</span>',
                '<span class="tag tag-outline">Inkoop</span>'),

            # ---- 02 · Explorer ----
            "02 · Inside each app": _t(
                "02 · Au cœur de chaque application", "02 · In jeder App",
                "02 · Dentro de cada app", "02 · Dentro ogni app", "02 · In elke app"),
            "Depth where you need it.": _t(
                "De la profondeur là où il en faut.", "Tiefe, wo Sie sie brauchen.",
                "Profundidad donde la necesita.", "Profondità dove serve.",
                "Diepgang waar u die nodig hebt."),
            "Every app ships a deep module set — turn on what you need, add the rest as you grow.": _t(
                "Chaque application est livrée avec un ensemble de modules approfondi — activez ce dont vous avez besoin, ajoutez le reste à mesure que vous grandissez.",
                "Jede App bringt einen umfangreichen Modulsatz mit — aktivieren Sie, was Sie brauchen, und ergänzen Sie den Rest, wenn Sie wachsen.",
                "Cada app incluye un amplio conjunto de módulos — active lo que necesita y añada el resto a medida que crece.",
                "Ogni app include un ricco set di moduli — attiva ciò che ti serve e aggiungi il resto man mano che cresci.",
                "Elke app wordt geleverd met een uitgebreide set modules — schakel in wat u nodig hebt en voeg de rest toe naarmate u groeit."),

            # ---- 03 · Metrics ----
            "03 · FulcrumGrid — at a glance": _t(
                "03 · FulcrumGrid — en un coup d'œil",
                "03 · FulcrumGrid — auf einen Blick",
                "03 · FulcrumGrid — de un vistazo",
                "03 · FulcrumGrid — in sintesi",
                "03 · FulcrumGrid — in het kort"),
            "At a glance.": _t(
                "En un coup d'œil.", "Auf einen Blick.", "De un vistazo.",
                "In sintesi.", "In het kort."),
            "FG-100 · Sheet 01": _t(
                "FG-100 · Feuille 01", "FG-100 · Blatt 01", "FG-100 · Hoja 01",
                "FG-100 · Foglio 01", "FG-100 · Blad 01"),
            "HR Suite modules": _t(
                "Modules HR Suite", "HR-Suite-Module", "Módulos de HR Suite",
                "Moduli HR Suite", "HR Suite-modules"),
            "Core HR always on; the rest by plan or add-on.": _t(
                "Le HR de base toujours actif ; le reste selon l'offre ou en option.",
                "Kern-HR immer aktiv; der Rest je nach Tarif oder als Add-on.",
                "El HR básico siempre activo; el resto según el plan o como complemento.",
                "HR di base sempre attivo; il resto in base al piano o come componente aggiuntivo.",
                "Kern-HR altijd actief; de rest per abonnement of als add-on."),
            "Languages": _t("Langues", "Sprachen", "Idiomas", "Lingue", "Talen"),
            "English, Arabic (RTL), French, German, Spanish, Italian, Dutch.": _t(
                "Anglais, arabe (RTL), français, allemand, espagnol, italien, néerlandais.",
                "Englisch, Arabisch (RTL), Französisch, Deutsch, Spanisch, Italienisch, Niederländisch.",
                "Inglés, árabe (RTL), francés, alemán, español, italiano, neerlandés.",
                "Inglese, arabo (RTL), francese, tedesco, spagnolo, italiano, olandese.",
                "Engels, Arabisch (RTL), Frans, Duits, Spaans, Italiaans, Nederlands."),
            "Countries with local HR detail": _t(
                "Pays avec des spécificités HR locales", "Länder mit lokalem HR-Detail",
                "Países con detalle de HR local", "Paesi con dettaglio HR locale",
                "Landen met lokaal HR-detail"),
            "Across North America, Europe, the GCC and the Middle East.": _t(
                "En Amérique du Nord, en Europe, dans le GCC et au Moyen-Orient.",
                "In Nordamerika, Europa, der GCC-Region und dem Nahen Osten.",
                "En Norteamérica, Europa, el GCC y Oriente Medio.",
                "In Nord America, Europa, GCC e Medio Oriente.",
                "In Noord-Amerika, Europa, de GCC en het Midden-Oosten."),
            "Region hubs": _t(
                "Hubs régionaux", "Regionale Hubs", "Centros regionales",
                "Hub regionali", "Regionale hubs"),
            "North America · Europe · GCC · Middle East.": _t(
                "Amérique du Nord · Europe · GCC · Moyen-Orient.",
                "Nordamerika · Europa · GCC · Naher Osten.",
                "Norteamérica · Europa · GCC · Oriente Medio.",
                "Nord America · Europa · GCC · Medio Oriente.",
                "Noord-Amerika · Europa · GCC · Midden-Oosten."),
            "Free trial": _t(
                "Essai gratuit", "Kostenlose Testphase", "Prueba gratuita",
                "Prova gratuita", "Gratis proefperiode"),
            "On every HR Suite and Command Center plan.": _t(
                "Sur chaque offre HR Suite et Command Center.",
                "Bei jedem HR-Suite- und Command-Center-Tarif.",
                "En todos los planes de HR Suite y Command Center.",
                "Su ogni piano HR Suite e Command Center.",
                "Bij elk HR Suite- en Command Center-abonnement."),
            '<span style="font-size:24px"> days</span>': _t(
                '<span style="font-size:24px"> jours</span>',
                '<span style="font-size:24px"> Tage</span>',
                '<span style="font-size:24px"> días</span>',
                '<span style="font-size:24px"> giorni</span>',
                '<span style="font-size:24px"> dagen</span>'),

            # ---- 04 · Integrations ----
            "04 · Integrations": _t(
                "04 · Intégrations", "04 · Integrationen", "04 · Integraciones",
                "04 · Integrazioni", "04 · Integraties"),
            "Connects to the systems you already run.": _t(
                "Se connecte aux systèmes que vous utilisez déjà.",
                "Verbindet sich mit den Systemen, die Sie bereits nutzen.",
                "Se conecta con los sistemas que ya utiliza.",
                "Si collega ai sistemi che già utilizzi.",
                "Verbindt met de systemen die u al gebruikt."),
            "ERP &amp; accounting": _t(
                "ERP &amp; comptabilité", "ERP &amp; Buchhaltung", "ERP &amp; contabilidad",
                "ERP &amp; contabilità", "ERP &amp; boekhouding"),
            "See all integrations →": _t(
                "Voir toutes les intégrations →", "Alle Integrationen ansehen →",
                "Ver todas las integraciones →", "Vedi tutte le integrazioni →",
                "Alle integraties bekijken →"),
            "Collection · Business and up": _t(
                "Collection · Société et plus", "Collection · Unternehmen und höher",
                "Collection · Negocio y superior", "Collection · Azienda e oltre",
                "Collection · Bedrijf en hoger"),
            "HR Suite · Enterprise": _t(
                "HR Suite · Entreprise", "HR Suite · Großunternehmen",
                "HR Suite · Empresa", "HR Suite · Impresa", "HR Suite · Onderneming"),
            # Technology proper nouns — kept English on every locale (declared so
            # the acceptance oracle treats them as handled rather than untranslated).
            "SAP Business One": _t("SAP Business One", "SAP Business One", "SAP Business One", "SAP Business One", "SAP Business One"),
            "REST API v1": _t("REST API v1", "REST API v1", "REST API v1", "REST API v1", "REST API v1"),
            "Webhooks": _t("Webhooks", "Webhooks", "Webhooks", "Webhooks", "Webhooks"),
            "Sandbox": _t("Sandbox", "Sandbox", "Sandbox", "Sandbox", "Sandbox"),

            # ---- 05 · Security ----
            "05 · Security &amp; compliance": _t(
                "05 · Sécurité &amp; conformité", "05 · Sicherheit &amp; Compliance",
                "05 · Seguridad &amp; cumplimiento", "05 · Sicurezza &amp; conformità",
                "05 · Beveiliging &amp; compliance"),
            "Secure by design. Auditable by default.": _t(
                "Sécurisé par conception. Auditable par défaut.",
                "Sicher durch Design. Prüfbar von Haus aus.",
                "Seguro por diseño. Auditable por defecto.",
                "Sicuro per progettazione. Verificabile per impostazione predefinita.",
                "Veilig door ontwerp. Standaard controleerbaar."),
            "Role-based access": _t(
                "Accès basé sur les rôles", "Rollenbasierter Zugriff",
                "Acceso basado en roles", "Accesso basato sui ruoli",
                "Rolgebaseerde toegang"),
            "Custom roles and permissions per team.": _t(
                "Rôles et permissions personnalisés par équipe.",
                "Individuelle Rollen und Berechtigungen pro Team.",
                "Roles y permisos personalizados por equipo.",
                "Ruoli e autorizzazioni personalizzati per team.",
                "Aangepaste rollen en rechten per team."),
            "Full audit trail": _t(
                "Piste d'audit complète", "Vollständiger Audit-Trail",
                "Registro de auditoría completo", "Audit trail completo",
                "Volledig audittrail"),
            "Every change recorded, with who and when.": _t(
                "Chaque modification enregistrée, avec qui et quand.",
                "Jede Änderung wird protokolliert — mit wer und wann.",
                "Cada cambio queda registrado, con quién y cuándo.",
                "Ogni modifica registrata, con chi e quando.",
                "Elke wijziging vastgelegd, met wie en wanneer."),
            "Multi-factor auth": _t(
                "Authentification multifacteur", "Multi-Faktor-Authentifizierung",
                "Autenticación multifactor", "Autenticazione a più fattori",
                "Multifactorauthenticatie"),
            "MFA on sign-in.": _t(
                "MFA à la connexion.", "MFA bei der Anmeldung.", "MFA al iniciar sesión.",
                "MFA all'accesso.", "MFA bij het inloggen."),
            "Approvals &amp; SoD": _t(
                "Validations &amp; SoD", "Freigaben &amp; SoD", "Aprobaciones &amp; SoD",
                "Approvazioni &amp; SoD", "Goedkeuringen &amp; SoD"),
            "Approval chains and segregation of duties.": _t(
                "Chaînes d'approbation et séparation des tâches.",
                "Genehmigungsketten und Funktionstrennung.",
                "Cadenas de aprobación y segregación de funciones.",
                "Catene di approvazione e separazione dei compiti.",
                "Goedkeuringsketens en functiescheiding."),
            "Exportable data": _t(
                "Données exportables", "Exportierbare Daten", "Datos exportables",
                "Dati esportabili", "Exporteerbare gegevens"),
            "Your records, exportable whenever you need them.": _t(
                "Vos données, exportables dès que vous en avez besoin.",
                "Ihre Datensätze, exportierbar, wann immer Sie sie brauchen.",
                "Sus registros, exportables siempre que los necesite.",
                "I tuoi dati, esportabili ogni volta che ti servono.",
                "Uw gegevens, exporteerbaar wanneer u ze nodig hebt."),
            "Your domain, your TLS": _t(
                "Votre domaine, votre TLS", "Ihre Domain, Ihr TLS", "Su dominio, su TLS",
                "Il tuo dominio, il tuo TLS", "Uw domein, uw TLS"),
            "Custom domain and certificate on Enterprise.": _t(
                "Domaine et certificat personnalisés sur l'offre Entreprise.",
                "Individuelle Domain und Zertifikat im Großunternehmen-Tarif.",
                "Dominio y certificado personalizados en el plan Empresa.",
                "Dominio e certificato personalizzati con il piano Impresa.",
                "Aangepast domein en certificaat bij Onderneming."),
            "Dedicated environment": _t(
                "Environnement dédié", "Dedizierte Umgebung", "Entorno dedicado",
                "Ambiente dedicato", "Toegewijde omgeving"),
            "A single-tenant instance isolated to your organization, on Enterprise.": _t(
                "Une instance à locataire unique isolée pour votre organisation, sur Enterprise.",
                "Eine Single-Tenant-Instanz, isoliert für Ihre Organisation, bei Enterprise.",
                "Una instancia de un solo inquilino aislada para su organización, en Enterprise.",
                "Un’istanza single-tenant isolata per la tua organizzazione, su Enterprise.",
                "Een single-tenant-instantie geïsoleerd voor uw organisatie, op Enterprise."),
            "On-premise option": _t(
                "Option sur site", "On-Premise-Option", "Opción on-premise",
                "Opzione on-premise", "On-premise-optie"),
            "Run in your own datacenter or private cloud on Enterprise, by arrangement.": _t(
                "Exécution dans votre propre datacenter ou cloud privé sur Enterprise, sur accord.",
                "Betrieb in Ihrem eigenen Rechenzentrum oder Ihrer Private Cloud bei Enterprise, nach Vereinbarung.",
                "Ejecución en su propio centro de datos o nube privada en Enterprise, previo acuerdo.",
                "Esecuzione nel tuo datacenter o cloud privato su Enterprise, su accordo.",
                "Draaien in uw eigen datacenter of private cloud op Enterprise, in overleg."),

            # ---- 06 · Regions ----
            "Built for how your region runs.": _t(
                "Conçu pour le fonctionnement de votre région.",
                "Gebaut für die Arbeitsweise Ihrer Region.",
                "Creado para cómo funciona su región.",
                "Costruito per il modo in cui opera la tua regione.",
                "Gebouwd voor hoe uw regio werkt."),
            "See all regions →": _t(
                "Voir toutes les régions →", "Alle Regionen ansehen →",
                "Ver todas las regiones →", "Vedi tutte le regioni →",
                "Bekijk alle regio's →"),
            "Hosted in every region we serve — your data stays close to your users.": _t(
                "Hébergé dans chaque région que nous desservons — vos données restent proches de vos utilisateurs.",
                "Gehostet in jeder Region, die wir bedienen — Ihre Daten bleiben nah bei Ihren Nutzern.",
                "Alojado en cada región que servimos — sus datos permanecen cerca de sus usuarios.",
                "Ospitato in ogni regione che serviamo — i tuoi dati restano vicini ai tuoi utenti.",
                "Gehost in elke regio die we bedienen — uw gegevens blijven dicht bij uw gebruikers."),
            "<h4>North America</h4>": _t(
                "<h4>Amérique du Nord</h4>", "<h4>Nordamerika</h4>", "<h4>Norteamérica</h4>",
                "<h4>Nord America</h4>", "<h4>Noord-Amerika</h4>"),
            "<h4>Europe</h4>": _t(
                "<h4>Europe</h4>", "<h4>Europa</h4>", "<h4>Europa</h4>",
                "<h4>Europa</h4>", "<h4>Europa</h4>"),
            "<h4>Middle East</h4>": _t(
                "<h4>Moyen-Orient</h4>", "<h4>Naher Osten</h4>", "<h4>Oriente Medio</h4>",
                "<h4>Medio Oriente</h4>", "<h4>Midden-Oosten</h4>"),
            "<h4>More markets</h4>": _t(
                "<h4>Autres marchés</h4>", "<h4>Weitere Märkte</h4>", "<h4>Más mercados</h4>",
                "<h4>Altri mercati</h4>", "<h4>Meer markten</h4>"),
            "United States · Canada": _t(
                "États-Unis · Canada", "USA · Kanada", "Estados Unidos · Canadá",
                "Stati Uniti · Canada", "Verenigde Staten · Canada"),
            "UK · Ireland · France · Germany · Spain · Italy · Netherlands": _t(
                "UK · Irlande · France · Allemagne · Espagne · Italie · Pays-Bas",
                "UK · Irland · Frankreich · Deutschland · Spanien · Italien · Niederlande",
                "UK · Irlanda · Francia · Alemania · España · Italia · Países Bajos",
                "UK · Irlanda · Francia · Germania · Spagna · Italia · Paesi Bassi",
                "VK · Ierland · Frankrijk · Duitsland · Spanje · Italië · Nederland"),
            "Saudi Arabia · UAE · Qatar · Kuwait · Bahrain · Oman": _t(
                "Arabie saoudite · UAE · Qatar · Koweït · Bahreïn · Oman",
                "Saudi-Arabien · UAE · Katar · Kuwait · Bahrain · Oman",
                "Arabia Saudí · UAE · Catar · Kuwait · Baréin · Omán",
                "Arabia Saudita · UAE · Qatar · Kuwait · Bahrein · Oman",
                "Saoedi-Arabië · UAE · Qatar · Koeweit · Bahrein · Oman"),
            "Egypt · Jordan · Lebanon · Iraq · Palestine · Syria · Yemen": _t(
                "Égypte · Jordanie · Liban · Irak · Palestine · Syrie · Yémen",
                "Ägypten · Jordanien · Libanon · Irak · Palästina · Syrien · Jemen",
                "Egipto · Jordania · Líbano · Irak · Palestina · Siria · Yemen",
                "Egitto · Giordania · Libano · Iraq · Palestina · Siria · Yemen",
                "Egypte · Jordanië · Libanon · Irak · Palestina · Syrië · Jemen"),
            "Elsewhere — on request": _t(
                "Ailleurs — sur demande", "Anderswo — auf Anfrage",
                "En otros lugares — a petición", "Altrove — su richiesta",
                "Elders — op aanvraag"),

            # ---- 07 · Pricing ----
            "Priced per app.": _t(
                "Tarifé par application.", "Preise pro App.", "Precio por app.",
                "Prezzo per app.", "Prijs per app."),
            "Full pricing →": _t(
                "Tarifs complets →", "Alle Preise →", "Precios completos →",
                "Prezzi completi →", "Volledige prijzen →"),
            "Per seat / month": _t(
                "Par utilisateur / mois", "Pro Platz / Monat", "Por usuario / mes",
                "Per utente / mese", "Per gebruiker / maand"),
            "Per organization / month": _t(
                "Par organisation / mois", "Pro Organisation / Monat", "Por organización / mes",
                "Per organizzazione / mese", "Per organisatie / maand"),
            "Per workspace / month": _t(
                "Par espace de travail / mois", "Pro Workspace / Monat", "Por espacio de trabajo / mes",
                "Per workspace / mese", "Per werkruimte / maand"),
            "Tailored": _t(
                "Sur mesure", "Maßgeschneidert", "A medida", "Su misura", "Op maat"),
            "<span>Starter</span>": _t(
                "<span>Essentiel</span>", "<span>Einsteiger</span>", "<span>Inicial</span>",
                "<span>Base</span>", "<span>Instap</span>"),
            "<span>Growth</span>": _t(
                "<span>Croissance</span>", "<span>Wachstum</span>", "<span>Crecimiento</span>",
                "<span>Crescita</span>", "<span>Groei</span>"),
            "<span>Enterprise</span>": _t(
                "<span>Entreprise</span>", "<span>Großunternehmen</span>", "<span>Empresa</span>",
                "<span>Impresa</span>", "<span>Onderneming</span>"),
            "<span>Pilot</span>": _t(
                "<span>Pilote</span>", "<span>Testphase</span>", "<span>Piloto</span>",
                "<span>Pilota</span>", "<span>Proef</span>"),
            "<span>Professional</span>": _t(
                "<span>Professionnel</span>", "<span>Professionell</span>", "<span>Profesional</span>",
                "<span>Professionale</span>", "<span>Professioneel</span>"),
            "<span>Business</span>": _t(
                "<span>Société</span>", "<span>Unternehmen</span>", "<span>Negocio</span>",
                "<span>Azienda</span>", "<span>Bedrijf</span>"),
            "<span>Enterprise · Agency</span>": _t(
                "<span>Entreprise · Agence</span>", "<span>Großunternehmen · Agentur</span>",
                "<span>Empresa · Agencia</span>", "<span>Impresa · Agenzia</span>",
                "<span>Onderneming · Bureau</span>"),
            "<span>Built to order</span>": _t(
                "<span>Sur commande</span>", "<span>Auf Bestellung</span>", "<span>Hecho a medida</span>",
                "<span>Su ordinazione</span>", "<span>Op bestelling</span>"),
            "<b>Free</b>": _t(
                "<b>Gratuit</b>", "<b>Kostenlos</b>", "<b>Gratis</b>", "<b>Gratis</b>", "<b>Gratis</b>"),
            "<b>Custom</b>": _t(
                "<b>Sur mesure</b>", "<b>Individuell</b>", "<b>A medida</b>",
                "<b>Su misura</b>", "<b>Op maat</b>"),
            "<b>On request</b>": _t(
                "<b>Sur demande</b>", "<b>Auf Anfrage</b>", "<b>A petición</b>",
                "<b>Su richiesta</b>", "<b>Op aanvraag</b>"),
            "Core HR on every plan. 14-day free trial.": _t(
                "Le HR de base sur chaque offre. Essai gratuit de 14 jours.",
                "Kern-HR bei jedem Tarif. 14 Tage kostenlos testen.",
                "HR básico en todos los planes. Prueba gratuita de 14 días.",
                "HR di base su ogni piano. Prova gratuita di 14 giorni.",
                "Kern-HR bij elk abonnement. Gratis proefperiode van 14 dagen."),
            "Annual billing saves 20%. 14-day free trial.": _t(
                "La facturation annuelle fait économiser 20 %. Essai gratuit de 14 jours.",
                "Jährliche Abrechnung spart 20 %. 14 Tage kostenlos testen.",
                "La facturación anual ahorra un 20 %. Prueba gratuita de 14 días.",
                "La fatturazione annuale fa risparmiare il 20%. Prova gratuita di 14 giorni.",
                "Jaarlijkse facturering bespaart 20%. Gratis proefperiode van 14 dagen."),
            "Seats included by plan.": _t(
                "Places incluses selon l'offre.", "Plätze je nach Tarif inbegriffen.",
                "Puestos incluidos según el plan.", "Postazioni incluse in base al piano.",
                "Plaatsen inbegrepen per abonnement."),
            "A business app built for your specific workflow, on the same platform.": _t(
                "Une application métier conçue pour votre flux de travail spécifique, sur la même plateforme.",
                "Eine Business-App, gebaut für Ihren spezifischen Workflow — auf derselben Plattform.",
                "Una aplicación de negocio creada para su flujo de trabajo específico, en la misma plataforma.",
                "Un'applicazione aziendale creata per il tuo flusso di lavoro specifico, sulla stessa piattaforma.",
                "Een bedrijfsapp gebouwd voor uw specifieke workflow, op hetzelfde platform."),
            "Talk to us →": _t(
                "Parlons-en →", "Sprechen Sie mit uns →", "Hablemos →",
                "Parliamone →", "Neem contact op →"),

            # ---- 08 · CTA ----
            "Ready to run<br />on one grid?": _t(
                "Prêt à tout piloter<br />sur une seule grille ?",
                "Bereit, alles<br />auf einem Grid zu betreiben?",
                "¿Listo para operar<br />en una sola cuadrícula?",
                "Pronto a lavorare<br />su un'unica griglia?",
                "Klaar om te draaien<br />op één grid?"),
            "Tell us what your team needs and we'll show you FulcrumGrid in action.": _t(
                "Dites-nous ce dont votre équipe a besoin et nous vous montrerons FulcrumGrid en action.",
                "Sagen Sie uns, was Ihr Team braucht, und wir zeigen Ihnen FulcrumGrid in Aktion.",
                "Cuéntenos qué necesita su equipo y le mostraremos FulcrumGrid en acción.",
                "Dicci di cosa ha bisogno il tuo team e ti mostreremo FulcrumGrid in azione.",
                "Vertel ons wat uw team nodig heeft en we tonen u FulcrumGrid in actie."),
        },
    },
}
