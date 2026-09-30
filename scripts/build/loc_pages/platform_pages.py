# -*- coding: utf-8 -*-
"""Per-page translations for the Platform pages:

  /features/      -> features/index.html
  /how-it-works/  -> how-it-works/index.html
  /custom-apps/   -> custom-apps/index.html

Conventions (see loc_catalog.py):
  * Brand/product names stay English: FulcrumGrid, Command Center, Collection,
    HR Suite, Blog, FAQ. Numeric/code labels and currency codes untranslated.
  * Keys are the EXACT English text as it appears in the EN source, including
    inline tags, &amp;, straight apostrophes and em dashes (—).
  * Chrome/global strings live in the shared COMMON catalog and are NOT
    repeated here (nav, footer, buttons, "Request a demo", the tagline, etc.).
  * The <title>/og:title/twitter:title on /features/ embeds two COMMON words
    ("Platform" and "Features"), which COMMON translates first; only the
    remaining descriptor fragment is keyed here so the match still lands.
  * A few JSON-LD content strings (HowTo / Service) are translated too, so the
    structured data localizes with the page rather than staying English.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# ---- Reused across all three pages -----------------------------------------

_OG_IMAGE_ALT = _t(
    'FulcrumGrid — des applications métier sur mesure pour chaque opération',
    'FulcrumGrid — zweckgebaute Business-Apps für jeden Betrieb',
    'FulcrumGrid — aplicaciones de negocio a medida para cada operación',
    'FulcrumGrid — applicazioni aziendali su misura per ogni operazione',
    'FulcrumGrid — doelgerichte bedrijfsapps voor elke operatie')

_HOME = _t('Accueil', 'Startseite', 'Inicio', 'Home', 'Home')

_EXPLORE_THE_APPS = _t('Découvrir les applications', 'Apps entdecken',
                       'Explorar las apps', 'Esplora le app', 'Ontdek de apps')


PAGE = {
    # =========================================================================
    '/features/': {
        'src': 'features/index.html',
        't': {
            # ---- Meta (title tail; COMMON handles "Platform"/"Features") ----
            'Secure, Consistent, Built for Operations': _t(
                'Sécurisée, cohérente, conçue pour les opérations',
                'Sicher, konsistent, für den Betrieb gebaut',
                'Segura, coherente, creada para las operaciones',
                'Sicura, coerente, costruita per le operazioni',
                'Veilig, consistent, gebouwd voor de operatie'),
            'Every FulcrumGrid app is secure by design, keeps your data exportable, and shares one consistent experience — built for real operations and made to grow with you.': _t(
                "Chaque application FulcrumGrid est sécurisée par conception, garde vos données exportables et partage une expérience cohérente — conçue pour les opérations réelles et faite pour grandir avec vous.",
                'Jede FulcrumGrid-App ist von Grund auf sicher, hält Ihre Daten exportierbar und teilt ein einheitliches Erlebnis — gebaut für den realen Betrieb und gemacht, um mit Ihnen zu wachsen.',
                'Cada app de FulcrumGrid es segura por diseño, mantiene sus datos exportables y comparte una experiencia coherente — creada para operaciones reales y hecha para crecer con usted.',
                "Ogni app FulcrumGrid è sicura per progettazione, mantiene i tuoi dati esportabili e condivide un'esperienza coerente — costruita per operazioni reali e pensata per crescere con te.",
                'Elke FulcrumGrid-app is veilig van opzet, houdt uw gegevens exporteerbaar en deelt één consistente ervaring — gebouwd voor echte operaties en gemaakt om met u mee te groeien.'),
            # ---- Hero ----
            'Why FulcrumGrid': _t('Pourquoi FulcrumGrid', 'Warum FulcrumGrid', 'Por qué FulcrumGrid', 'Perché FulcrumGrid', 'Waarom FulcrumGrid'),
            'Built to the same high standard': _t(
                'Conçue selon le même haut standard',
                'Nach dem gleichen hohen Standard gebaut',
                'Creada con el mismo alto estándar',
                'Costruita secondo lo stesso alto standard',
                'Gebouwd volgens dezelfde hoge standaard'),
            # ---- Section head ----
            '01 · What every app shares': _t('01 · Ce que partage chaque app', '01 · Was jede App teilt', '01 · Lo que comparte cada app', '01 · Cosa condivide ogni app', '01 · Wat elke app deelt'),
            'The same foundation, every app.': _t('Le même socle, pour chaque app.', 'Dasselbe Fundament, jede App.', 'La misma base, cada app.', 'Le stesse fondamenta, ogni app.', 'Hetzelfde fundament, elke app.'),
            'Built for the teams who keep businesses running — clarity and reliability over hype.': _t(
                'Conçu pour les équipes qui font tourner les entreprises — clarté et fiabilité plutôt que battage.',
                'Gebaut für die Teams, die Unternehmen am Laufen halten — Klarheit und Zuverlässigkeit statt Hype.',
                'Creado para los equipos que mantienen los negocios en marcha — claridad y fiabilidad antes que el bombo.',
                'Costruito per i team che mandano avanti le aziende — chiarezza e affidabilità invece del clamore.',
                'Gebouwd voor de teams die bedrijven draaiende houden — helderheid en betrouwbaarheid boven hype.'),
            "One team builds every FulcrumGrid app to the same standard — so each one is focused, familiar, and ready for real work from day one. Here's what every app on the grid shares.": _t(
                "Une seule équipe conçoit chaque application FulcrumGrid selon le même standard — chacune est ainsi ciblée, familière et prête pour le travail réel dès le premier jour. Voici ce que partage chaque application de la grille.",
                'Ein Team baut jede FulcrumGrid-App nach demselben Standard — so ist jede fokussiert, vertraut und vom ersten Tag an bereit für echte Arbeit. Das teilt jede App im Grid.',
                'Un solo equipo crea cada app de FulcrumGrid con el mismo estándar — así cada una es enfocada, familiar y está lista para el trabajo real desde el primer día. Esto es lo que comparte cada app de la cuadrícula.',
                'Un unico team costruisce ogni app FulcrumGrid secondo lo stesso standard — così ognuna è mirata, familiare e pronta per il lavoro reale dal primo giorno. Ecco cosa condivide ogni app della griglia.',
                'Eén team bouwt elke FulcrumGrid-app volgens dezelfde standaard — zo is elke app gericht, vertrouwd en vanaf dag één klaar voor echt werk. Dit is wat elke app op het grid deelt.'),
            # ---- Feature cards ----
            'Secure by design': _t('Sécurisé par conception', 'Von Grund auf sicher', 'Seguro por diseño', 'Sicuro per progettazione', 'Veilig van opzet'),
            'Role-based access and a full audit trail within each app. Grant the right people the right access.': _t(
                "Accès basé sur les rôles et une piste d'audit complète dans chaque application. Accordez le bon accès aux bonnes personnes.",
                'Rollenbasierter Zugriff und ein vollständiger Audit-Trail in jeder App. Geben Sie den richtigen Personen den richtigen Zugriff.',
                'Acceso basado en roles y un registro de auditoría completo dentro de cada app. Otorgue el acceso adecuado a las personas adecuadas.',
                "Accesso basato sui ruoli e un registro di audit completo all'interno di ogni app. Concedi il giusto accesso alle persone giuste.",
                'Rolgebaseerde toegang en een volledig auditspoor binnen elke app. Geef de juiste mensen de juiste toegang.'),
            'Your data, exportable': _t('Vos données, exportables', 'Ihre Daten, exportierbar', 'Sus datos, exportables', 'I tuoi dati, esportabili', 'Uw gegevens, exporteerbaar'),
            'Every app keeps clean, structured records you can export anytime. Your data stays yours.': _t(
                'Chaque application conserve des enregistrements propres et structurés que vous pouvez exporter à tout moment. Vos données restent les vôtres.',
                'Jede App führt saubere, strukturierte Datensätze, die Sie jederzeit exportieren können. Ihre Daten bleiben Ihre.',
                'Cada app mantiene registros limpios y estructurados que puede exportar en cualquier momento. Sus datos siguen siendo suyos.',
                'Ogni app conserva dati puliti e strutturati che puoi esportare in qualsiasi momento. I tuoi dati restano tuoi.',
                'Elke app bewaart schone, gestructureerde gegevens die u altijd kunt exporteren. Uw gegevens blijven van u.'),
            'Consistent experience': _t('Expérience cohérente', 'Einheitliches Erlebnis', 'Experiencia coherente', 'Esperienza coerente', 'Consistente ervaring'),
            'One design language and navigation across every app. Learn it once and move fast in all of them.': _t(
                'Un même langage de conception et une même navigation sur toutes les applications. Apprenez-les une fois et avancez vite dans toutes.',
                'Eine Designsprache und Navigation über alle Apps hinweg. Einmal lernen und in allen schnell vorankommen.',
                'Un mismo lenguaje de diseño y navegación en todas las apps. Apréndalo una vez y avance rápido en todas.',
                'Un unico linguaggio di design e una sola navigazione in tutte le app. Imparalo una volta e muoviti veloce in tutte.',
                'Eén ontwerptaal en navigatie in elke app. Leer het één keer en werk snel in allemaal.'),
            'Built for real operations': _t('Conçu pour les opérations réelles', 'Für den realen Betrieb gebaut', 'Creado para operaciones reales', 'Costruito per operazioni reali', 'Gebouwd voor echte operaties'),
            'Made for the teams who keep businesses running every day — clarity and reliability over hype.': _t(
                'Fait pour les équipes qui font tourner les entreprises chaque jour — clarté et fiabilité plutôt que battage.',
                'Gemacht für die Teams, die Unternehmen jeden Tag am Laufen halten — Klarheit und Zuverlässigkeit statt Hype.',
                'Hecho para los equipos que mantienen los negocios en marcha cada día — claridad y fiabilidad antes que el bombo.',
                'Fatto per i team che mandano avanti le aziende ogni giorno — chiarezza e affidabilità invece del clamore.',
                'Gemaakt voor de teams die bedrijven elke dag draaiende houden — helderheid en betrouwbaarheid boven hype.'),
            'Insight where it counts': _t('Des informations là où elles comptent', 'Einblick, wo er zählt', 'Información donde importa', 'Informazioni dove contano', 'Inzicht waar het telt'),
            'Each app reports on its own domain in real time, so you always know where things stand.': _t(
                'Chaque application rend compte de son propre domaine en temps réel, pour que vous sachiez toujours où en sont les choses.',
                'Jede App berichtet in Echtzeit über ihren eigenen Bereich, sodass Sie immer wissen, wo die Dinge stehen.',
                'Cada app informa sobre su propio dominio en tiempo real, para que siempre sepa cómo están las cosas.',
                'Ogni app riporta il proprio ambito in tempo reale, così sai sempre a che punto sono le cose.',
                'Elke app rapporteert in realtime over haar eigen domein, zodat u altijd weet hoe de zaken ervoor staan.'),
            'Grows with you': _t('Grandit avec vous', 'Wächst mit Ihnen', 'Crece con usted', 'Cresce con te', 'Groeit met u mee'),
            'Start with one app. Add the rest as you scale — no migration, no re-platforming, no rip and replace.': _t(
                'Commencez par une application. Ajoutez les autres à mesure que vous grandissez — pas de migration, pas de changement de plateforme, pas de tout casser pour tout remplacer.',
                'Beginnen Sie mit einer App. Fügen Sie den Rest hinzu, wenn Sie skalieren — keine Migration, kein Plattformwechsel, kein Rausreißen und Ersetzen.',
                'Empiece con una app. Añada el resto a medida que escala — sin migración, sin cambio de plataforma, sin arrancar y reemplazar.',
                'Inizia con una app. Aggiungi le altre man mano che cresci — nessuna migrazione, nessun cambio di piattaforma, niente da buttare e sostituire.',
                'Begin met één app. Voeg de rest toe naarmate u opschaalt — geen migratie, geen overstap van platform, geen slopen en vervangen.'),
            # ---- Deployment ----
            'Deployment': _t('Déploiement', 'Bereitstellung', 'Despliegue', 'Distribuzione', 'Implementatie'),
            'Run it where it suits you.': _t(
                'Exécutez-le là où cela vous convient.',
                'Betreiben Sie es dort, wo es Ihnen passt.',
                'Ejecútelo donde le convenga.',
                'Eseguilo dove ti conviene.',
                'Draai het waar het u uitkomt.'),
            'Most teams run on our managed cloud. Regulated and enterprise organizations can run dedicated or on-premise. ': _t(
                'La plupart des équipes utilisent notre cloud géré. Les organisations réglementées et les grandes entreprises peuvent opter pour un déploiement dédié ou sur site. ',
                'Die meisten Teams nutzen unsere verwaltete Cloud. Regulierte und große Unternehmen können dediziert oder on-premise betreiben. ',
                'La mayoría de los equipos usan nuestro cloud gestionado. Las organizaciones reguladas y las grandes empresas pueden optar por un despliegue dedicado o on-premise. ',
                'La maggior parte dei team usa il nostro cloud gestito. Le organizzazioni regolamentate e le grandi imprese possono scegliere un deployment dedicato o on-premise. ',
                'De meeste teams draaien op onze beheerde cloud. Gereguleerde en grote organisaties kunnen dedicated of on-premise draaien. '),
            'Talk to sales →': _t('Parler aux ventes →', 'Vertrieb kontaktieren →', 'Hablar con ventas →', 'Parla con le vendite →', 'Praat met sales →'),
            'Our managed, multi-tenant cloud — included on every plan, with nothing for you to run or maintain.': _t(
                'Notre cloud géré et multi-locataire — inclus dans chaque offre, sans rien à exécuter ni à maintenir.',
                'Unsere verwaltete, mandantenfähige Cloud — in jedem Tarif enthalten, ohne dass Sie etwas betreiben oder warten müssen.',
                'Nuestro cloud gestionado y multiinquilino — incluido en cada plan, sin nada que ejecutar ni mantener.',
                'Il nostro cloud gestito e multi-tenant — incluso in ogni piano, senza nulla da eseguire o mantenere.',
                'Onze beheerde, multi-tenant cloud — inbegrepen in elk plan, zonder dat u iets hoeft te draaien of onderhouden.'),
            'Dedicated environment': _t('Environnement dédié', 'Dedizierte Umgebung', 'Entorno dedicado', 'Ambiente dedicato', 'Toegewijde omgeving'),
            'A single-tenant instance isolated to your organization, with its own database. Available on Enterprise.': _t(
                'Une instance à locataire unique isolée pour votre organisation, avec sa propre base de données. Disponible sur Enterprise.',
                'Eine Single-Tenant-Instanz, isoliert für Ihre Organisation, mit eigener Datenbank. Verfügbar bei Enterprise.',
                'Una instancia de un solo inquilino aislada para su organización, con su propia base de datos. Disponible en Enterprise.',
                'Un’istanza single-tenant isolata per la tua organizzazione, con un database dedicato. Disponibile su Enterprise.',
                'Een single-tenant-instantie geïsoleerd voor uw organisatie, met een eigen database. Beschikbaar op Enterprise.'),
            'On-premise / self-hosted': _t('Sur site / auto-hébergé', 'On-Premise / selbstgehostet', 'On-premise / autoalojado', 'On-premise / self-hosted', 'On-premise / zelf-gehost'),
            'Run FulcrumGrid in your own datacenter or private cloud, behind your firewall. Available on Enterprise, by arrangement.': _t(
                'Exécutez FulcrumGrid dans votre propre datacenter ou cloud privé, derrière votre pare-feu. Disponible sur Enterprise, sur accord.',
                'Betreiben Sie FulcrumGrid in Ihrem eigenen Rechenzentrum oder Ihrer Private Cloud, hinter Ihrer Firewall. Verfügbar bei Enterprise, nach Vereinbarung.',
                'Ejecute FulcrumGrid en su propio centro de datos o nube privada, tras su firewall. Disponible en Enterprise, previo acuerdo.',
                'Esegui FulcrumGrid nel tuo datacenter o cloud privato, dietro il tuo firewall. Disponibile su Enterprise, su accordo.',
                'Draai FulcrumGrid in uw eigen datacenter of private cloud, achter uw firewall. Beschikbaar op Enterprise, in overleg.'),
            'Data residency': _t('Résidence des données', 'Datenspeicherort', 'Residencia de datos', 'Residenza dei dati', 'Dataresidentie'),
            'Choose the region your data is stored and processed in, to meet local requirements.': _t(
                'Choisissez la région où vos données sont stockées et traitées, pour répondre aux exigences locales.',
                'Wählen Sie die Region, in der Ihre Daten gespeichert und verarbeitet werden, um lokale Anforderungen zu erfüllen.',
                'Elija la región donde se almacenan y procesan sus datos, para cumplir los requisitos locales.',
                'Scegli la regione in cui i tuoi dati vengono archiviati ed elaborati, per soddisfare i requisiti locali.',
                'Kies de regio waarin uw gegevens worden opgeslagen en verwerkt, om aan lokale eisen te voldoen.'),
            'Servers in your region': _t(
                'Des serveurs dans votre région', 'Server in Ihrer Region', 'Servidores en su región',
                'Server nella tua regione', 'Servers in uw regio'),
            'We run infrastructure in every region we serve, so your data sits on servers close to your users — low latency, and kept in-region.': _t(
                'Nous exploitons une infrastructure dans chaque région que nous desservons : vos données résident sur des serveurs proches de vos utilisateurs — faible latence, et conservées dans votre région.',
                'Wir betreiben Infrastruktur in jeder Region, die wir bedienen, sodass Ihre Daten auf Servern nahe bei Ihren Nutzern liegen — geringe Latenz und in der Region gehalten.',
                'Operamos infraestructura en cada región que servimos, de modo que sus datos residen en servidores cercanos a sus usuarios — baja latencia y mantenidos en la región.',
                'Gestiamo infrastruttura in ogni regione che serviamo, così i tuoi dati risiedono su server vicini ai tuoi utenti — bassa latenza e mantenuti nella regione.',
                'We draaien infrastructuur in elke regio die we bedienen, zodat uw gegevens op servers dicht bij uw gebruikers staan — lage latentie en in de regio gehouden.'),
            # ---- CTA ----
            'See the platform in action': _t('Voyez la plateforme en action', 'Sehen Sie die Plattform in Aktion', 'Vea la plataforma en acción', 'Guarda la piattaforma in azione', 'Zie het platform in actie'),
            'Explore the apps built on it, or tell us what your team needs.': _t(
                'Découvrez les applications qui reposent dessus, ou dites-nous ce dont votre équipe a besoin.',
                'Entdecken Sie die darauf gebauten Apps oder sagen Sie uns, was Ihr Team braucht.',
                'Explore las apps creadas sobre ella, o cuéntenos qué necesita su equipo.',
                'Esplora le app costruite su di essa, o dicci di cosa ha bisogno il tuo team.',
                'Ontdek de apps die erop gebouwd zijn, of vertel ons wat uw team nodig heeft.'),
            'Explore the apps': _EXPLORE_THE_APPS,
        },
    },

    # =========================================================================
    '/how-it-works/': {
        'src': 'how-it-works/index.html',
        't': {
            # ---- Meta ----
            'How It Works — Get Started in Three Steps | FulcrumGrid': _t(
                'Comment ça marche — Démarrez en trois étapes | FulcrumGrid',
                "So funktioniert's — In drei Schritten starten | FulcrumGrid",
                'Cómo funciona — Empiece en tres pasos | FulcrumGrid',
                'Come funziona — Inizia in tre passi | FulcrumGrid',
                'Hoe het werkt — Begin in drie stappen | FulcrumGrid'),
            'Get started with FulcrumGrid in three steps: choose your apps, set them up in minutes, and run your operations — adding more apps at your own pace.': _t(
                "Démarrez avec FulcrumGrid en trois étapes : choisissez vos applications, configurez-les en quelques minutes et pilotez vos opérations — en ajoutant d'autres applications à votre rythme.",
                'Starten Sie mit FulcrumGrid in drei Schritten: Wählen Sie Ihre Apps, richten Sie sie in Minuten ein und steuern Sie Ihren Betrieb — weitere Apps in Ihrem eigenen Tempo.',
                'Empiece con FulcrumGrid en tres pasos: elija sus apps, configúrelas en minutos y gestione sus operaciones — añadiendo más apps a su propio ritmo.',
                'Inizia con FulcrumGrid in tre passi: scegli le tue app, configurale in pochi minuti e gestisci le tue operazioni — aggiungendo altre app al tuo ritmo.',
                'Begin met FulcrumGrid in drie stappen: kies uw apps, stel ze in binnen minuten en run uw operatie — voeg meer apps toe in uw eigen tempo.'),
            # ---- Hero ----
            'Live in three steps': _t(
                'Opérationnel en trois étapes',
                'In drei Schritten startklar',
                'En marcha en tres pasos',
                'Operativo in tre passi',
                'Live in drie stappen'),
            # ---- Section head ----
            '01 · Getting started': _t('01 · Pour commencer', '01 · Erste Schritte', '01 · Para empezar', '01 · Per iniziare', '01 · Aan de slag'),
            'From sign-up to live.': _t("De l'inscription à la mise en service.", 'Von der Anmeldung bis zum Start.', 'Del registro a la puesta en marcha.', "Dall'iscrizione all'operatività.", 'Van aanmelding tot live.'),
            'Three steps, at your pace — no migration project, no re-platforming.': _t(
                'Trois étapes, à votre rythme — pas de projet de migration, pas de changement de plateforme.',
                'Drei Schritte, in Ihrem Tempo — kein Migrationsprojekt, kein Plattformwechsel.',
                'Tres pasos, a su ritmo — sin proyecto de migración, sin cambio de plataforma.',
                'Tre passi, al tuo ritmo — nessun progetto di migrazione, nessun cambio di piattaforma.',
                'Drie stappen, in uw eigen tempo — geen migratieproject, geen overstap van platform.'),
            # ---- Step eyebrows ----
            'STEP 01': _t('ÉTAPE 01', 'SCHRITT 01', 'PASO 01', 'PASSO 01', 'STAP 01'),
            'STEP 02': _t('ÉTAPE 02', 'SCHRITT 02', 'PASO 02', 'PASSO 02', 'STAP 02'),
            'STEP 03': _t('ÉTAPE 03', 'SCHRITT 03', 'PASO 03', 'PASSO 03', 'STAP 03'),
            'Getting started with FulcrumGrid is straightforward. Choose what you need, set it up in minutes, and add more apps at your own pace.': _t(
                "Démarrer avec FulcrumGrid est simple. Choisissez ce dont vous avez besoin, configurez-le en quelques minutes et ajoutez d'autres applications à votre rythme.",
                'Der Einstieg in FulcrumGrid ist unkompliziert. Wählen Sie, was Sie brauchen, richten Sie es in Minuten ein und fügen Sie weitere Apps in Ihrem eigenen Tempo hinzu.',
                'Empezar con FulcrumGrid es sencillo. Elija lo que necesita, configúrelo en minutos y añada más apps a su propio ritmo.',
                'Iniziare con FulcrumGrid è semplice. Scegli ciò di cui hai bisogno, configuralo in pochi minuti e aggiungi altre app al tuo ritmo.',
                'Beginnen met FulcrumGrid is eenvoudig. Kies wat u nodig hebt, stel het in binnen minuten en voeg meer apps toe in uw eigen tempo.'),
            # ---- Steps ----
            'Choose your apps': _t('Choisissez vos applications', 'Wählen Sie Ihre Apps', 'Elija sus apps', 'Scegli le tue app', 'Kies uw apps'),
            'Pick the apps your team needs today. HR Suite, Command Center, Collection — or all three.': _t(
                "Choisissez les applications dont votre équipe a besoin aujourd'hui. HR Suite, Command Center, Collection — ou les trois.",
                'Wählen Sie die Apps, die Ihr Team heute braucht. HR Suite, Command Center, Collection — oder alle drei.',
                'Elija las apps que su equipo necesita hoy. HR Suite, Command Center, Collection — o las tres.',
                'Scegli le app di cui il tuo team ha bisogno oggi. HR Suite, Command Center, Collection — o tutte e tre.',
                'Kies de apps die uw team vandaag nodig heeft. HR Suite, Command Center, Collection — of alle drie.'),
            'Set up your app': _t('Configurez votre application', 'Richten Sie Ihre App ein', 'Configure su app', 'Configura la tua app', 'Stel uw app in'),
            'Import your records and invite your team. Configure roles and permissions in minutes.': _t(
                'Importez vos données et invitez votre équipe. Configurez les rôles et les autorisations en quelques minutes.',
                'Importieren Sie Ihre Datensätze und laden Sie Ihr Team ein. Konfigurieren Sie Rollen und Berechtigungen in Minuten.',
                'Importe sus registros e invite a su equipo. Configure roles y permisos en minutos.',
                'Importa i tuoi dati e invita il tuo team. Configura ruoli e permessi in pochi minuti.',
                'Importeer uw gegevens en nodig uw team uit. Configureer rollen en rechten binnen minuten.'),
            'Run your operations': _t('Pilotez vos opérations', 'Steuern Sie Ihren Betrieb', 'Gestione sus operaciones', 'Gestisci le tue operazioni', 'Run uw operatie'),
            "Get to work. Add more FulcrumGrid apps whenever you're ready — at your pace.": _t(
                "Mettez-vous au travail. Ajoutez d'autres applications FulcrumGrid quand vous êtes prêt — à votre rythme.",
                'Legen Sie los. Fügen Sie weitere FulcrumGrid-Apps hinzu, wann immer Sie bereit sind — in Ihrem Tempo.',
                'Manos a la obra. Añada más apps de FulcrumGrid cuando esté listo — a su ritmo.',
                'Mettiti al lavoro. Aggiungi altre app FulcrumGrid quando sei pronto — al tuo ritmo.',
                'Ga aan de slag. Voeg meer FulcrumGrid-apps toe wanneer u er klaar voor bent — in uw eigen tempo.'),
            # ---- CTA ----
            'Ready to get started?': _t('Prêt à vous lancer ?', 'Bereit loszulegen?', '¿Listo para empezar?', 'Pronto a iniziare?', 'Klaar om te beginnen?'),
            "Tell us what your team needs and we'll show you FulcrumGrid in action.": _t(
                'Dites-nous ce dont votre équipe a besoin et nous vous montrerons FulcrumGrid en action.',
                'Sagen Sie uns, was Ihr Team braucht, und wir zeigen Ihnen FulcrumGrid in Aktion.',
                'Cuéntenos qué necesita su equipo y le mostraremos FulcrumGrid en acción.',
                'Dicci di cosa ha bisogno il tuo team e ti mostreremo FulcrumGrid in azione.',
                'Vertel ons wat uw team nodig heeft en we tonen u FulcrumGrid in actie.'),
            'Explore the apps': _EXPLORE_THE_APPS,
        },
    },

    # =========================================================================
    '/custom-apps/': {
        'src': 'custom-apps/index.html',
        't': {
            # ---- Meta ----
            'Custom Business Apps Tailored to Your Workflow | FulcrumGrid': _t(
                'Applications métier sur mesure adaptées à votre flux de travail | FulcrumGrid',
                'Individuelle Business-Apps, zugeschnitten auf Ihren Workflow | FulcrumGrid',
                'Apps de negocio a medida adaptadas a su flujo de trabajo | FulcrumGrid',
                'App aziendali su misura adattate al tuo flusso di lavoro | FulcrumGrid',
                'Zakelijke apps op maat, afgestemd op uw workflow | FulcrumGrid'),
            'FulcrumGrid builds customized business apps tailored to your specific use case — on the same secure, auditable grid as our ready-made apps.': _t(
                "FulcrumGrid conçoit des applications métier personnalisées, adaptées à votre cas d'usage précis — sur la même grille sécurisée et auditable que nos applications prêtes à l'emploi.",
                'FulcrumGrid entwickelt maßgeschneiderte Business-Apps, zugeschnitten auf Ihren konkreten Anwendungsfall — auf demselben sicheren, prüfbaren Grid wie unsere fertigen Apps.',
                'FulcrumGrid crea apps de negocio personalizadas, adaptadas a su caso de uso concreto — en la misma cuadrícula segura y auditable que nuestras apps listas para usar.',
                "FulcrumGrid crea app aziendali personalizzate, adattate al tuo caso d'uso specifico — sulla stessa griglia sicura e verificabile delle nostre app pronte all'uso.",
                'FulcrumGrid bouwt aangepaste bedrijfsapps, afgestemd op uw specifieke gebruikssituatie — op hetzelfde veilige, controleerbare grid als onze kant-en-klare apps.'),
            # ---- Hero ----
            'Built for you': _t('Conçu pour vous', 'Für Sie gebaut', 'Creado para usted', 'Costruito per te', 'Voor u gebouwd'),
            'Custom business apps for your exact workflow': _t(
                'Des applications métier sur mesure pour votre flux de travail exact',
                'Individuelle Business-Apps für genau Ihren Workflow',
                'Apps de negocio a medida para su flujo de trabajo exacto',
                'App aziendali su misura per il tuo flusso di lavoro preciso',
                'Zakelijke apps op maat voor precies uw workflow'),
            'Beyond our ready-made apps, we build customized business apps tailored to your specific use case — designed around how your team actually works, on the same secure, auditable foundation as the rest of the grid.': _t(
                "Au-delà de nos applications prêtes à l'emploi, nous concevons des applications métier personnalisées, adaptées à votre cas d'usage précis — pensées autour de la façon dont votre équipe travaille réellement, sur le même socle sécurisé et auditable que le reste de la grille.",
                'Über unsere fertigen Apps hinaus entwickeln wir maßgeschneiderte Business-Apps, zugeschnitten auf Ihren konkreten Anwendungsfall — gestaltet rund um die tatsächliche Arbeitsweise Ihres Teams, auf demselben sicheren, prüfbaren Fundament wie der Rest des Grids.',
                'Más allá de nuestras apps listas para usar, creamos apps de negocio personalizadas, adaptadas a su caso de uso concreto — diseñadas en torno a cómo trabaja realmente su equipo, sobre la misma base segura y auditable que el resto de la cuadrícula.',
                "Oltre alle nostre app pronte all'uso, creiamo app aziendali personalizzate, adattate al tuo caso d'uso specifico — progettate attorno al modo in cui il tuo team lavora davvero, sulle stesse fondamenta sicure e verificabili del resto della griglia.",
                'Naast onze kant-en-klare apps bouwen we aangepaste bedrijfsapps, afgestemd op uw specifieke gebruikssituatie — ontworpen rond hoe uw team echt werkt, op hetzelfde veilige, controleerbare fundament als de rest van het grid.'),
            'Discuss a custom app': _t("Discuter d'une application sur mesure", 'Eine individuelle App besprechen', 'Hablar de una app a medida', "Parla di un'app su misura", 'Bespreek een app op maat'),
            'See ready-made apps': _t("Voir les applications prêtes à l'emploi", 'Fertige Apps ansehen', 'Ver apps listas para usar', "Vedi le app pronte all'uso", 'Bekijk kant-en-klare apps'),
            # ---- Where custom fits ----
            'Example use cases': _t("Exemples de cas d'usage", 'Beispielhafte Anwendungsfälle', 'Casos de uso de ejemplo', "Esempi di casi d'uso", 'Voorbeelden van gebruikssituaties'),
            'Where custom fits': _t('Où le sur-mesure trouve sa place', 'Wo Individuelles passt', 'Dónde encaja lo personalizado', 'Dove si inserisce il su misura', 'Waar maatwerk past'),
            "When an off-the-shelf app isn't quite it": _t(
                'Quand une application clé en main ne suffit pas tout à fait',
                'Wenn eine Standard-App nicht ganz passt',
                'Cuando una app estándar no encaja del todo',
                "Quando un'app pronta all'uso non basta del tutto",
                'Wanneer een kant-en-klare app net niet past'),
            'If your operation has a workflow no standard tool covers, we build the app around it — so your team works the way it should, not the way a generic tool forces.': _t(
                "Si votre activité comporte un flux de travail qu'aucun outil standard ne couvre, nous construisons l'application autour de lui — pour que votre équipe travaille comme elle le doit, et non comme un outil générique l'y contraint.",
                'Wenn Ihr Betrieb einen Ablauf hat, den kein Standardwerkzeug abdeckt, bauen wir die App darum herum — damit Ihr Team so arbeitet, wie es soll, und nicht so, wie ein generisches Tool es erzwingt.',
                'Si su operación tiene un flujo de trabajo que ninguna herramienta estándar cubre, construimos la app a su alrededor — para que su equipo trabaje como debe, y no como le obliga una herramienta genérica.',
                "Se la tua operatività ha un flusso di lavoro che nessuno strumento standard copre, costruiamo l'app attorno a esso — così il tuo team lavora come dovrebbe, non come lo costringe uno strumento generico.",
                'Als uw operatie een werkstroom heeft die geen standaardtool dekt, bouwen we de app eromheen — zodat uw team werkt zoals het hoort, niet zoals een generiek tool het afdwingt.'),
            # ---- Use-case tags ----
            'Field service': _t('Service sur le terrain', 'Außendienst', 'Servicio de campo', 'Assistenza sul campo', 'Buitendienst'),
            'Clinics &amp; care': _t('Cliniques &amp; soins', 'Kliniken &amp; Pflege', 'Clínicas &amp; atención', 'Cliniche &amp; assistenza', 'Klinieken &amp; zorg'),
            'Logistics': _t('Logistique', 'Logistik', 'Logística', 'Logistica', 'Logistiek'),
            'Manufacturing': _t('Fabrication', 'Fertigung', 'Fabricación', 'Produzione', 'Productie'),
            'Nonprofits': _t('Associations', 'Non-Profits', 'Organizaciones sin fines de lucro', 'No profit', 'Non-profits'),
            'Agencies': _t('Agences', 'Agenturen', 'Agencias', 'Agenzie', 'Bureaus'),
            # ---- How we build ----
            'How we build': _t('Comment nous construisons', 'Wie wir bauen', 'Cómo construimos', 'Come costruiamo', 'Hoe we bouwen'),
            'On the same secure, auditable grid as every ready-made app.': _t(
                "Sur la même grille sécurisée et auditable que chaque application prête à l'emploi.",
                'Auf demselben sicheren, prüfbaren Grid wie jede fertige App.',
                'En la misma cuadrícula segura y auditable que cada app lista para usar.',
                "Sulla stessa griglia sicura e verificabile di ogni app pronta all'uso.",
                'Op hetzelfde veilige, controleerbare grid als elke kant-en-klare app.'),
            'STEP 01': _t('ÉTAPE 01', 'SCHRITT 01', 'PASO 01', 'PASSO 01', 'STAP 01'),
            'STEP 02': _t('ÉTAPE 02', 'SCHRITT 02', 'PASO 02', 'PASSO 02', 'STAP 02'),
            'STEP 03': _t('ÉTAPE 03', 'SCHRITT 03', 'PASO 03', 'PASSO 03', 'STAP 03'),
            'From your workflow to a working app': _t(
                'De votre flux de travail à une application opérationnelle',
                'Von Ihrem Workflow zur funktionierenden App',
                'De su flujo de trabajo a una app en funcionamiento',
                "Dal tuo flusso di lavoro a un'app funzionante",
                'Van uw workflow naar een werkende app'),
            'Map your workflow': _t('Cartographiez votre flux de travail', 'Ihren Workflow erfassen', 'Mapee su flujo de trabajo', 'Mappa il tuo flusso di lavoro', 'Breng uw workflow in kaart'),
            'We start with how your team actually works today — the steps, the records, the people, and the rules.': _t(
                "Nous partons de la façon dont votre équipe travaille réellement aujourd'hui — les étapes, les données, les personnes et les règles.",
                'Wir beginnen damit, wie Ihr Team heute tatsächlich arbeitet — die Schritte, die Datensätze, die Menschen und die Regeln.',
                'Partimos de cómo trabaja realmente su equipo hoy — los pasos, los registros, las personas y las reglas.',
                'Partiamo da come il tuo team lavora davvero oggi — i passaggi, i dati, le persone e le regole.',
                'We beginnen bij hoe uw team vandaag echt werkt — de stappen, de gegevens, de mensen en de regels.'),
            'Build on the grid': _t('Construire sur la grille', 'Auf dem Grid bauen', 'Construir sobre la cuadrícula', 'Costruire sulla griglia', 'Bouwen op het grid'),
            'Your app is built on the same secure, auditable grid — with role-based access and exportable data from day one.': _t(
                "Votre application est construite sur la même grille sécurisée et auditable — avec un accès basé sur les rôles et des données exportables dès le premier jour.",
                'Ihre App wird auf demselben sicheren, prüfbaren Grid gebaut — mit rollenbasiertem Zugriff und exportierbaren Daten vom ersten Tag an.',
                'Su app se crea en la misma cuadrícula segura y auditable — con acceso basado en roles y datos exportables desde el primer día.',
                'La tua app è costruita sulla stessa griglia sicura e verificabile — con accesso basato sui ruoli e dati esportabili fin dal primo giorno.',
                'Uw app wordt gebouwd op hetzelfde veilige, controleerbare grid — met rolgebaseerde toegang en exporteerbare gegevens vanaf dag één.'),
            'Run &amp; evolve': _t('Exploiter &amp; faire évoluer', 'Betreiben &amp; weiterentwickeln', 'Operar &amp; evolucionar', 'Gestire &amp; evolvere', 'Draaien &amp; doorontwikkelen'),
            'Launch with your team, then refine as you learn. It plugs straight into the rest of your grid.': _t(
                'Lancez avec votre équipe, puis affinez à mesure que vous apprenez. Elle se connecte directement au reste de votre grille.',
                'Starten Sie mit Ihrem Team und verfeinern Sie dann, während Sie dazulernen. Sie fügt sich direkt in den Rest Ihres Grids ein.',
                'Lance con su equipo y luego refine a medida que aprende. Se conecta directamente con el resto de su cuadrícula.',
                'Lancia con il tuo team, poi perfeziona man mano che impari. Si integra direttamente nel resto della tua griglia.',
                'Lanceer met uw team en verfijn dan naarmate u leert. Ze sluit direct aan op de rest van uw grid.'),
            # ---- CTA ----
            'Have a workflow in mind?': _t('Un flux de travail en tête ?', 'Einen Workflow im Kopf?', '¿Tiene un flujo de trabajo en mente?', 'Hai un flusso di lavoro in mente?', 'Hebt u een workflow in gedachten?'),
            "Tell us what your team needs and we'll scope a custom app with you.": _t(
                "Dites-nous ce dont votre équipe a besoin et nous définirons une application sur mesure avec vous.",
                'Sagen Sie uns, was Ihr Team braucht, und wir umreißen gemeinsam mit Ihnen eine individuelle App.',
                'Cuéntenos qué necesita su equipo y definiremos una app a medida con usted.',
                "Dicci di cosa ha bisogno il tuo team e definiremo insieme un'app su misura.",
                'Vertel ons wat uw team nodig heeft en we bepalen samen met u een app op maat.'),
        },
    },
}
