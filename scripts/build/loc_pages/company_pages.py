# -*- coding: utf-8 -*-
"""Per-page translation catalogs for the company / support pages:
the About page, the Contact & demo-request page, and the FAQ.

Conventions (see loc_catalog.py):
  * Brand / product names stay English: FulcrumGrid, Command Center, Collection,
    HR Suite; "Blog" and "FAQ" and plan tiers (Starter, Business, Enterprise)
    are left untranslated. Company name "Avenlor Consulting" and email addresses
    are kept verbatim. Roadmap app names Inventory/Procurement are translated to
    match the homepage catalog; CRM stays CRM.
  * Keys are the EXACT English text as it appears in the EN source HTML,
    including entities (&amp;), curly apostrophes (’), em dashes (—) and inline
    tags (<span>, <a>). Note the FAQ JSON-LD answers use STRAIGHT apostrophes
    while the visible answers use CURLY ones, so they are separate keys.
  * COMMON strings (nav/footer/buttons and the standalone words "About",
    "Contact", "Pricing", "Request a demo", "Email us", …) are handled by
    loc_catalog.COMMON, applied BEFORE this catalog, and are deliberately NOT
    repeated here. Where such a word sits inside a title/eyebrow/heading, only
    the surrounding "tail" is keyed here (adding a key with the COMMON word would
    never match after COMMON has run). This is why:
      - About title/og:title ("About — FulcrumGrid") and the eyebrow
        ("About FulcrumGrid") localize via COMMON's "About" alone.
      - Contact title tail is keyed as "&amp; Request a Demo | FulcrumGrid"
        (capital "Demo" is NOT the COMMON "Request a demo"); "Contact" is COMMON.
      - Contact <h1> "Request a demo &amp; talk to us": COMMON translates
        "Request a demo"; only the "talk to us" tail is keyed here.
      - FAQ title tail keyed as "Arabic Support &amp; Setup"; "Pricing" is COMMON.
  * Form field `name` attributes, hidden values and <option value="…"> values are
    NEVER translated (they are submitted to the form service). Where an option's
    visible text equals its value ("A custom app"), only the visible text is
    keyed, via the ">…</option>" wrapper, so the value attribute is untouched.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# Reused: breadcrumb "Home" and the shared og:image:alt (identical everywhere).
_HOME = _t('Accueil', 'Startseite', 'Inicio', 'Home', 'Home')
_OG_ALT = _t(
    'FulcrumGrid — des applications métier sur mesure pour chaque opération',
    'FulcrumGrid — zweckgebaute Business-Apps für jeden Betrieb',
    'FulcrumGrid — aplicaciones de negocio a medida para cada operación',
    'FulcrumGrid — applicazioni aziendali su misura per ogni operazione',
    'FulcrumGrid — doelgerichte bedrijfsapps voor elke operatie')


PAGE = {
    # =========================================================================
    '/about/': {
        'src': 'about/index.html',
        't': {
            # ---- Meta (title/og:title carry "About" -> handled by COMMON) ----
            'FulcrumGrid builds the operational backbone for modern teams — one connected grid of apps instead of a dozen disconnected tools.': _t(
                "FulcrumGrid construit l'épine dorsale opérationnelle des équipes modernes — une seule grille connectée d'applications au lieu d'une dizaine d'outils déconnectés.",
                'FulcrumGrid baut das operative Rückgrat für moderne Teams — ein vernetztes Grid aus Apps statt eines Dutzends getrennter Tools.',
                'FulcrumGrid construye la columna vertebral operativa de los equipos modernos — una sola cuadrícula conectada de apps en lugar de una docena de herramientas desconectadas.',
                "FulcrumGrid costruisce la spina dorsale operativa dei team moderni — un'unica griglia connessa di app invece di una dozzina di strumenti scollegati.",
                'FulcrumGrid bouwt de operationele ruggengraat voor moderne teams — één verbonden grid van apps in plaats van een dozijn losse tools.'),
            'One connected grid of apps instead of a dozen disconnected tools.': _t(
                "Une seule grille connectée d'applications au lieu d'une dizaine d'outils déconnectés.",
                'Ein vernetztes Grid aus Apps statt eines Dutzends getrennter Tools.',
                'Una sola cuadrícula conectada de apps en lugar de una docena de herramientas desconectadas.',
                "Un'unica griglia connessa di app invece di una dozzina di strumenti scollegati.",
                'Eén verbonden grid van apps in plaats van een dozijn losse tools.'),
            # ---- Breadcrumb ----
            'Home': _HOME,
            # ---- Hero ----
            'Building the operational backbone': _t(
                "Construire l'épine dorsale opérationnelle",
                'Wir bauen das operative Rückgrat',
                'Construimos la columna vertebral operativa',
                'Costruiamo la spina dorsale operativa',
                'De operationele ruggengraat bouwen'),
            'FulcrumGrid exists to give businesses genuinely good operational apps — each one focused and dependable — instead of bloated all-in-ones or scattered, half-built tools.': _t(
                'FulcrumGrid existe pour offrir aux entreprises des applications opérationnelles vraiment bonnes — chacune ciblée et fiable — plutôt que des solutions tout-en-un pléthoriques ou des outils dispersés et à moitié aboutis.',
                'FulcrumGrid gibt es, um Unternehmen wirklich gute operative Apps zu bieten — jede fokussiert und zuverlässig — statt überladener All-in-one-Lösungen oder verstreuter, halbfertiger Tools.',
                'FulcrumGrid existe para dar a las empresas apps operativas realmente buenas — cada una enfocada y fiable — en lugar de soluciones todo en uno recargadas o herramientas dispersas y a medio hacer.',
                'FulcrumGrid esiste per offrire alle aziende app operative davvero valide — ognuna mirata e affidabile — invece di soluzioni all-in-one sovraccariche o strumenti sparsi e incompleti.',
                'FulcrumGrid bestaat om bedrijven echt goede operationele apps te geven — elk gericht en betrouwbaar — in plaats van opgeblazen alles-in-één-oplossingen of versnipperde, half af gebouwde tools.'),
            # ---- At a glance (eyebrow + heading) ----
            '01 · FulcrumGrid today': _t("01 · FulcrumGrid aujourd'hui", '01 · FulcrumGrid heute', '01 · FulcrumGrid hoy', '01 · FulcrumGrid oggi', '01 · FulcrumGrid vandaag'),
            'At a glance.': _t("En un coup d'œil.", 'Auf einen Blick.', 'De un vistazo.', "A colpo d'occhio.", 'In één oogopslag.'),
            # ---- Stat row (numbers are not translated) ----
            'Apps live today': _t("Apps disponibles aujourd'hui", 'Apps heute verfügbar', 'Apps disponibles hoy', 'App disponibili oggi', 'Apps nu beschikbaar'),
            'Design language': _t('Langage de conception', 'Designsprache', 'Lenguaje de diseño', 'Linguaggio di design', 'Ontwerptaal'),
            'More on the roadmap': _t('Autres sur la feuille de route', 'Weitere auf der Roadmap', 'Más en la hoja de ruta', 'Altre nella roadmap', 'Meer op de roadmap'),
            'Team behind them all': _t('Équipe derrière toutes', 'Team hinter allen', 'Equipo detrás de todas', 'Team dietro tutte', 'Team achter ze allemaal'),
            # ---- Principles ----
            'What we believe': _t('Ce en quoi nous croyons', 'Woran wir glauben', 'En qué creemos', 'In cosa crediamo', 'Waar wij in geloven'),
            'Principles behind the grid': _t('Les principes derrière la grille', 'Prinzipien hinter dem Grid', 'Principios detrás de la cuadrícula', 'I principi dietro la griglia', 'Principes achter het grid'),
            'One team, one standard': _t('Une équipe, un standard', 'Ein Team, ein Standard', 'Un equipo, un estándar', 'Un team, uno standard', 'Eén team, één standaard'),
            'Every FulcrumGrid app is built by the same team to the same bar — focused, familiar, and dependable.': _t(
                'Chaque app FulcrumGrid est conçue par la même équipe selon la même exigence — ciblée, familière et fiable.',
                'Jede FulcrumGrid-App wird vom selben Team nach demselben Maßstab gebaut — fokussiert, vertraut und zuverlässig.',
                'Cada app de FulcrumGrid la crea el mismo equipo con el mismo nivel de exigencia — enfocada, familiar y fiable.',
                'Ogni app FulcrumGrid è costruita dallo stesso team secondo lo stesso standard — mirata, familiare e affidabile.',
                'Elke FulcrumGrid-app wordt door hetzelfde team gebouwd volgens dezelfde lat — gericht, vertrouwd en betrouwbaar.'),
            'Own your data': _t('Vos données vous appartiennent', 'Ihre Daten gehören Ihnen', 'Sus datos son suyos', 'I tuoi dati sono tuoi', 'Uw data is van u'),
            'Your records stay clean, structured, exportable, and yours — always, in every app.': _t(
                'Vos enregistrements restent propres, structurés, exportables et vôtres — toujours, dans chaque app.',
                'Ihre Datensätze bleiben sauber, strukturiert, exportierbar und Ihr Eigentum — immer, in jeder App.',
                'Sus registros se mantienen limpios, estructurados, exportables y suyos — siempre, en cada app.',
                'I tuoi record restano puliti, strutturati, esportabili e tuoi — sempre, in ogni app.',
                'Uw gegevens blijven schoon, gestructureerd, exporteerbaar en van u — altijd, in elke app.'),
            'Grow without re-platforming': _t('Grandir sans changer de plateforme', 'Wachsen ohne Re-Platforming', 'Crecer sin cambiar de plataforma', 'Crescere senza cambiare piattaforma', 'Groeien zonder van platform te wisselen'),
            'Start with one app and add more over time. No rip-and-replace, no migration tax as you grow.': _t(
                "Commencez par une app et ajoutez-en d'autres au fil du temps. Pas de tout-remplacer, pas de coût de migration à mesure que vous grandissez.",
                'Beginnen Sie mit einer App und fügen Sie mit der Zeit weitere hinzu. Kein Rundum-Austausch, keine Migrationskosten beim Wachsen.',
                'Empiece con una app y añada más con el tiempo. Sin arrancar y reemplazar, sin coste de migración a medida que crece.',
                "Inizia con un'app e aggiungine altre nel tempo. Nessuna sostituzione totale, nessun costo di migrazione mentre cresci.",
                'Begin met één app en voeg er na verloop van tijd meer toe. Geen volledige vervanging, geen migratiekosten terwijl u groeit.'),
            'Built for real operations': _t('Conçu pour les opérations réelles', 'Für den echten Betrieb gebaut', 'Creado para operaciones reales', 'Costruito per operazioni reali', 'Gebouwd voor echte operaties'),
            'We design for the teams who keep businesses running every day — clarity, reliability, and speed over hype.': _t(
                'Nous concevons pour les équipes qui font tourner les entreprises chaque jour — la clarté, la fiabilité et la rapidité plutôt que le battage.',
                'Wir gestalten für die Teams, die Unternehmen jeden Tag am Laufen halten — Klarheit, Zuverlässigkeit und Tempo statt Hype.',
                'Diseñamos para los equipos que mantienen las empresas en marcha cada día — claridad, fiabilidad y velocidad antes que el ruido.',
                "Progettiamo per i team che ogni giorno mandano avanti le aziende — chiarezza, affidabilità e velocità prima dell'hype.",
                'We ontwerpen voor de teams die bedrijven elke dag draaiende houden — duidelijkheid, betrouwbaarheid en snelheid boven hype.'),
            'Simple by default': _t('Simple par défaut', 'Standardmäßig einfach', 'Simple por defecto', 'Semplice per impostazione predefinita', 'Standaard eenvoudig'),
            "Powerful doesn't have to mean complicated. Teams should learn the grid once and move fast everywhere.": _t(
                "Puissant ne veut pas dire compliqué. Les équipes devraient apprendre la grille une seule fois et aller vite partout.",
                'Leistungsstark muss nicht kompliziert heißen. Teams sollten das Grid einmal lernen und überall schnell vorankommen.',
                'Potente no tiene por qué significar complicado. Los equipos deberían aprender la cuadrícula una vez y avanzar rápido en todas partes.',
                'Potente non deve voler dire complicato. I team dovrebbero imparare la griglia una volta e muoversi rapidamente ovunque.',
                'Krachtig hoeft niet ingewikkeld te betekenen. Teams zouden het grid één keer moeten leren en overal snel vooruit moeten kunnen.'),
            'Secure at the core': _t('Sécurisé au cœur', 'Sicher im Kern', 'Seguro en el núcleo', 'Sicuro al centro', 'Veilig in de kern'),
            'Role-based access and a full audit trail in every app — security is part of the foundation, not an add-on.': _t(
                "Un accès basé sur les rôles et une piste d'audit complète dans chaque app — la sécurité fait partie des fondations, pas un module en plus.",
                'Rollenbasierter Zugriff und ein vollständiges Audit-Protokoll in jeder App — Sicherheit ist Teil des Fundaments, kein Zusatz.',
                'Acceso basado en roles y un registro de auditoría completo en cada app — la seguridad es parte de los cimientos, no un añadido.',
                'Accesso basato sui ruoli e un registro di controllo completo in ogni app — la sicurezza fa parte delle fondamenta, non è un componente aggiuntivo.',
                'Rolgebaseerde toegang en een volledig auditspoor in elke app — beveiliging is onderdeel van het fundament, geen toevoeging.'),
            # ---- CTA ----
            'Run your business<br />on one grid': _t('Gérez votre entreprise<br />sur une seule grille', 'Führen Sie Ihr Unternehmen<br />auf einem Grid', 'Gestione su negocio<br />en una sola cuadrícula', "Gestisci la tua azienda<br />su un'unica griglia", 'Run uw bedrijf<br />op één grid'),
            'See what a single, connected grid can do for your team.': _t(
                "Découvrez ce qu'une grille unique et connectée peut faire pour votre équipe.",
                'Sehen Sie, was ein einziges, vernetztes Grid für Ihr Team leisten kann.',
                'Vea lo que una única cuadrícula conectada puede hacer por su equipo.',
                "Scopri cosa può fare per il tuo team un'unica griglia connessa.",
                'Ontdek wat één verbonden grid voor uw team kan doen.'),
            'Get in touch': _t('Prendre contact', 'Kontakt aufnehmen', 'Ponerse en contacto', 'Mettiti in contatto', 'Neem contact op'),
        },
    },
    # =========================================================================
    '/contact/': {
        'src': 'contact/index.html',
        't': {
            # ---- Meta (title/og/twitter carry "Contact" -> COMMON; tail keyed) ----
            '&amp; Request a Demo | FulcrumGrid': _t(
                '&amp; Demander une démo | FulcrumGrid',
                '&amp; Demo anfragen | FulcrumGrid',
                '&amp; Solicitar una demo | FulcrumGrid',
                '&amp; Richiedi una demo | FulcrumGrid',
                '&amp; Vraag een demo aan | FulcrumGrid'),
            "Request a FulcrumGrid demo or talk to our team. Tell us what your business needs and we'll show you the right apps — or email contact@avenlorconsulting.com.": _t(
                "Demandez une démo de FulcrumGrid ou parlez à notre équipe. Dites-nous ce dont votre entreprise a besoin et nous vous montrerons les bonnes apps — ou écrivez à contact@avenlorconsulting.com.",
                'Fordern Sie eine FulcrumGrid-Demo an oder sprechen Sie mit unserem Team. Sagen Sie uns, was Ihr Unternehmen braucht, und wir zeigen Ihnen die passenden Apps — oder schreiben Sie an contact@avenlorconsulting.com.',
                'Solicite una demo de FulcrumGrid o hable con nuestro equipo. Cuéntenos qué necesita su empresa y le mostraremos las apps adecuadas — o escriba a contact@avenlorconsulting.com.',
                'Richiedi una demo di FulcrumGrid o parla con il nostro team. Dicci di cosa ha bisogno la tua azienda e ti mostreremo le app giuste — oppure scrivi a contact@avenlorconsulting.com.',
                'Vraag een FulcrumGrid-demo aan of praat met ons team. Vertel ons wat uw bedrijf nodig heeft en we tonen u de juiste apps — of mail naar contact@avenlorconsulting.com.'),
            # ---- Breadcrumb ----
            'Home': _HOME,
            # ---- Hero (h1: "Request a demo" -> COMMON; tail keyed) ----
            '&amp; talk to us': _t(
                '&amp; discutons',
                '&amp; sprechen wir',
                '&amp; hablemos',
                '&amp; parliamone',
                '&amp; praat met ons'),
            "Tell us what your team needs and we'll show you FulcrumGrid in action. Prefer email? Reach us directly and we'll get right back to you.": _t(
                "Dites-nous ce dont votre équipe a besoin et nous vous montrerons FulcrumGrid en action. Vous préférez l'e-mail ? Écrivez-nous directement et nous vous répondrons très vite.",
                'Sagen Sie uns, was Ihr Team braucht, und wir zeigen Ihnen FulcrumGrid in Aktion. Lieber per E-Mail? Schreiben Sie uns direkt und wir melden uns umgehend.',
                'Cuéntenos qué necesita su equipo y le mostraremos FulcrumGrid en acción. ¿Prefiere el correo? Escríbanos directamente y le responderemos enseguida.',
                "Dicci di cosa ha bisogno il tuo team e ti mostreremo FulcrumGrid in azione. Preferisci l'e-mail? Scrivici direttamente e ti risponderemo subito.",
                'Vertel ons wat uw team nodig heeft en we tonen u FulcrumGrid in actie. Liever mailen? Schrijf ons rechtstreeks en we reageren snel.'),
            # ---- CTA panel ----
            'Ready to run on one grid?': _t('Prêt à tout piloter sur une seule grille ?', 'Bereit, auf einem Grid zu arbeiten?', '¿Listo para operar en una sola cuadrícula?', "Pronto a lavorare su un'unica griglia?", 'Klaar om op één grid te werken?'),
            "Tell us what your team needs and we'll show you FulcrumGrid in action.": _t(
                'Dites-nous ce dont votre équipe a besoin et nous vous montrerons FulcrumGrid en action.',
                'Sagen Sie uns, was Ihr Team braucht, und wir zeigen Ihnen FulcrumGrid in Aktion.',
                'Cuéntenos qué necesita su equipo y le mostraremos FulcrumGrid en acción.',
                'Dicci di cosa ha bisogno il tuo team e ti mostreremo FulcrumGrid in azione.',
                'Vertel ons wat uw team nodig heeft en we tonen u FulcrumGrid in actie.'),
            # ---- Lead form (visible labels/placeholders/option text only) ----
            'Which app are you interested in? (optional)': _t(
                'Quelle app vous intéresse ? (facultatif)',
                'Welche App interessiert Sie? (optional)',
                '¿Qué app le interesa? (opcional)',
                'Quale app ti interessa? (facoltativo)',
                'In welke app bent u geïnteresseerd? (optioneel)'),
            'Which app are you interested in?': _t(
                'Quelle app vous intéresse ?',
                'Welche App interessiert Sie?',
                '¿Qué app le interesa?',
                'Quale app ti interessa?',
                'In welke app bent u geïnteresseerd?'),
            '>A custom app</option>': _t(
                '>Une application sur mesure</option>',
                '>Eine individuelle App</option>',
                '>Una app a medida</option>',
                ">Un'app su misura</option>",
                '>Een app op maat</option>'),
            '>Not sure — please recommend one for me</option>': _t(
                ">Je ne sais pas — recommandez-m'en une</option>",
                '>Nicht sicher — bitte empfehlen Sie mir eine</option>',
                '>No estoy seguro — recomiéndeme una</option>',
                '>Non sono sicuro — consigliatemene una</option>',
                '>Niet zeker — beveel er een aan</option>'),
            'Your name': _t('Votre nom', 'Ihr Name', 'Su nombre', 'Il tuo nome', 'Uw naam'),
            'Work email': _t('E-mail professionnel', 'Geschäftliche E-Mail', 'Correo de trabajo', 'E-mail di lavoro', 'Zakelijk e-mailadres'),
            'Or email us at': _t('Ou écrivez-nous à', 'Oder schreiben Sie uns an', 'O escríbanos a', 'Oppure scrivici a', 'Of mail ons op'),
        },
    },
    # =========================================================================
    '/faq/': {
        'src': 'faq/index.html',
        't': {
            # ---- Meta (title tail; COMMON handles "Pricing") ----
            'Arabic Support &amp; Setup': _t(
                "Prise en charge de l'arabe et configuration",
                'Arabisch-Support &amp; Einrichtung',
                'Soporte en árabe y configuración',
                "Supporto per l'arabo e configurazione",
                'Arabisch-ondersteuning en installatie'),
            'Answers to common questions about FulcrumGrid: what it is, which apps it includes, pricing and free trial, Arabic support, data export, security, custom apps, and how to get started.': _t(
                "Réponses aux questions courantes sur FulcrumGrid : ce que c'est, quelles apps il comprend, les tarifs et l'essai gratuit, la prise en charge de l'arabe, l'export des données, la sécurité, les apps sur mesure et comment démarrer.",
                'Antworten auf häufige Fragen zu FulcrumGrid: was es ist, welche Apps es umfasst, Preise und kostenlose Testversion, Arabisch-Unterstützung, Datenexport, Sicherheit, individuelle Apps und wie man loslegt.',
                'Respuestas a preguntas comunes sobre FulcrumGrid: qué es, qué apps incluye, precios y prueba gratuita, soporte de árabe, exportación de datos, seguridad, apps a medida y cómo empezar.',
                "Risposte alle domande comuni su FulcrumGrid: cos'è, quali app include, prezzi e prova gratuita, supporto per l'arabo, esportazione dei dati, sicurezza, app su misura e come iniziare.",
                'Antwoorden op veelgestelde vragen over FulcrumGrid: wat het is, welke apps het omvat, prijzen en gratis proefperiode, Arabisch-ondersteuning, gegevensexport, beveiliging, apps op maat en hoe u begint.'),
            # ---- Breadcrumb ----
            'Home': _HOME,
            # ---- Hero ----
            'Frequently asked questions': _t(
                'Foire aux questions',
                'Häufig gestellte Fragen',
                'Preguntas frecuentes',
                'Domande frequenti',
                'Veelgestelde vragen'),
            # ---- Section head ----
            'Questions &amp; answers.': _t('Questions &amp; réponses.', 'Fragen &amp; Antworten.', 'Preguntas y respuestas.', 'Domande e risposte.', 'Vragen &amp; antwoorden.'),
            'Everything teams ask before they start — the apps, pricing, Arabic support, data and security.': _t(
                "Tout ce que les équipes demandent avant de se lancer — les apps, les tarifs, la prise en charge de l'arabe, les données et la sécurité.",
                'Alles, was Teams vor dem Start fragen — die Apps, Preise, Arabisch-Unterstützung, Daten und Sicherheit.',
                'Todo lo que los equipos preguntan antes de empezar — las apps, los precios, el soporte de árabe, los datos y la seguridad.',
                "Tutto ciò che i team chiedono prima di iniziare — le app, i prezzi, il supporto per l'arabo, i dati e la sicurezza.",
                'Alles wat teams vragen voordat ze beginnen — de apps, prijzen, Arabisch-ondersteuning, gegevens en beveiliging.'),
            'Straight answers about what FulcrumGrid is, what it includes, and how it works. Still have a question? Just ask.': _t(
                "Des réponses claires sur ce qu'est FulcrumGrid, ce qu'il comprend et comment il fonctionne. Vous avez encore une question ? Il suffit de nous la poser.",
                'Klare Antworten darauf, was FulcrumGrid ist, was es umfasst und wie es funktioniert. Noch eine Frage? Fragen Sie einfach.',
                'Respuestas claras sobre qué es FulcrumGrid, qué incluye y cómo funciona. ¿Aún tiene una pregunta? Solo pregunte.',
                "Risposte chiare su cos'è FulcrumGrid, cosa include e come funziona. Hai ancora una domanda? Basta chiedere.",
                'Heldere antwoorden over wat FulcrumGrid is, wat het omvat en hoe het werkt. Nog een vraag? Vraag het gerust.'),
            # ---- FAQ questions (also localize the JSON-LD "name" fields) ----
            'What is FulcrumGrid?': _t("Qu'est-ce que FulcrumGrid ?", 'Was ist FulcrumGrid?', '¿Qué es FulcrumGrid?', "Che cos'è FulcrumGrid?", 'Wat is FulcrumGrid?'),
            'Which apps does FulcrumGrid include?': _t('Quelles apps FulcrumGrid comprend-il ?', 'Welche Apps umfasst FulcrumGrid?', '¿Qué apps incluye FulcrumGrid?', 'Quali app include FulcrumGrid?', 'Welke apps omvat FulcrumGrid?'),
            'Who is FulcrumGrid for?': _t("À qui s'adresse FulcrumGrid ?", 'Für wen ist FulcrumGrid?', '¿Para quién es FulcrumGrid?', 'A chi si rivolge FulcrumGrid?', 'Voor wie is FulcrumGrid?'),
            'Can I start with just one app?': _t('Puis-je commencer avec une seule app ?', 'Kann ich mit nur einer App beginnen?', '¿Puedo empezar con una sola app?', 'Posso iniziare con una sola app?', 'Kan ik met één app beginnen?'),
            'Does FulcrumGrid support Arabic?': _t("FulcrumGrid prend-il en charge l'arabe ?", 'Unterstützt FulcrumGrid Arabisch?', '¿FulcrumGrid es compatible con el árabe?', "FulcrumGrid supporta l'arabo?", 'Ondersteunt FulcrumGrid Arabisch?'),
            'How much does FulcrumGrid cost?': _t('Combien coûte FulcrumGrid ?', 'Wie viel kostet FulcrumGrid?', '¿Cuánto cuesta FulcrumGrid?', 'Quanto costa FulcrumGrid?', 'Wat kost FulcrumGrid?'),
            'Is there a free trial?': _t('Existe-t-il un essai gratuit ?', 'Gibt es eine kostenlose Testversion?', '¿Hay una prueba gratuita?', 'È disponibile una prova gratuita?', 'Is er een gratis proefperiode?'),
            'Can I export my data?': _t('Puis-je exporter mes données ?', 'Kann ich meine Daten exportieren?', '¿Puedo exportar mis datos?', 'Posso esportare i miei dati?', 'Kan ik mijn gegevens exporteren?'),
            'How does FulcrumGrid handle access and security?': _t('Comment FulcrumGrid gère-t-il les accès et la sécurité ?', 'Wie handhabt FulcrumGrid Zugriff und Sicherheit?', '¿Cómo gestiona FulcrumGrid el acceso y la seguridad?', 'Come gestisce FulcrumGrid accessi e sicurezza?', 'Hoe gaat FulcrumGrid om met toegang en beveiliging?'),
            'Can we run FulcrumGrid on-premise or in a dedicated environment?': _t(
                'Pouvons-nous exécuter FulcrumGrid sur site ou dans un environnement dédié ?',
                'Können wir FulcrumGrid on-premise oder in einer dedizierten Umgebung betreiben?',
                '¿Podemos ejecutar FulcrumGrid on-premise o en un entorno dedicado?',
                'Possiamo eseguire FulcrumGrid on-premise o in un ambiente dedicato?',
                'Kunnen we FulcrumGrid on-premise of in een toegewijde omgeving draaien?'),
            'Yes. Beyond our managed cloud, Enterprise customers can run FulcrumGrid in a dedicated single-tenant environment, or self-hosted on-premise in their own datacenter or private cloud — with data residency in the region of their choice. Talk to sales about the right setup.': _t(
                'Oui. Au-delà de notre cloud géré, les clients Enterprise peuvent exécuter FulcrumGrid dans un environnement dédié à locataire unique, ou en auto-hébergement sur site dans leur propre datacenter ou cloud privé — avec résidence des données dans la région de leur choix. Parlez-en aux ventes pour trouver la bonne configuration.',
                'Ja. Über unsere verwaltete Cloud hinaus können Enterprise-Kunden FulcrumGrid in einer dedizierten Single-Tenant-Umgebung oder selbstgehostet on-premise im eigenen Rechenzentrum oder in der Private Cloud betreiben — mit Datenspeicherung in der Region ihrer Wahl. Sprechen Sie mit dem Vertrieb über die richtige Einrichtung.',
                'Sí. Más allá de nuestro cloud gestionado, los clientes Enterprise pueden ejecutar FulcrumGrid en un entorno dedicado de un solo inquilino, o autoalojado on-premise en su propio centro de datos o nube privada — con residencia de datos en la región que elijan. Hable con ventas sobre la configuración adecuada.',
                'Sì. Oltre al nostro cloud gestito, i clienti Enterprise possono eseguire FulcrumGrid in un ambiente dedicato single-tenant, o self-hosted on-premise nel proprio datacenter o cloud privato — con residenza dei dati nella regione che preferiscono. Parla con le vendite per la configurazione giusta.',
                'Ja. Naast onze beheerde cloud kunnen Enterprise-klanten FulcrumGrid draaien in een toegewijde single-tenant-omgeving, of zelf-gehost on-premise in hun eigen datacenter of private cloud — met dataresidentie in de regio van hun keuze. Overleg met sales over de juiste opzet.'),
            'Can FulcrumGrid build a custom app for my workflow?': _t('FulcrumGrid peut-il créer une app sur mesure pour mon flux de travail ?', 'Kann FulcrumGrid eine individuelle App für meinen Workflow entwickeln?', '¿Puede FulcrumGrid crear una app a medida para mi flujo de trabajo?', "FulcrumGrid può creare un'app su misura per il mio flusso di lavoro?", 'Kan FulcrumGrid een app op maat bouwen voor mijn workflow?'),
            'How do I get started or request a demo?': _t('Comment démarrer ou demander une démo ?', 'Wie lege ich los oder fordere eine Demo an?', '¿Cómo empiezo o solicito una demo?', 'Come inizio o richiedo una demo?', 'Hoe begin ik of vraag ik een demo aan?'),
            'Who builds FulcrumGrid?': _t('Qui développe FulcrumGrid ?', 'Wer entwickelt FulcrumGrid?', '¿Quién desarrolla FulcrumGrid?', 'Chi sviluppa FulcrumGrid?', 'Wie bouwt FulcrumGrid?'),
            # ---- FAQ visible answers (with inline links; curly apostrophes) ----
            'FulcrumGrid is a family of purpose-built business apps that run on one grid — <a href="/products/command-center/">Command Center</a> (a real-time operations dashboard), <a href="/products/collection/">Collection</a> (accounts receivable and payments), and <a href="/products/hr-suite/">HR Suite</a> (people operations) — plus <a href="/custom-apps/">custom apps</a> built for a specific workflow. It is built by Avenlor Consulting.': _t(
                'FulcrumGrid est une famille d\'applications métier sur mesure qui fonctionnent sur une seule grille — <a href="/products/command-center/">Command Center</a> (un tableau de bord des opérations en temps réel), <a href="/products/collection/">Collection</a> (comptes clients et paiements) et <a href="/products/hr-suite/">HR Suite</a> (gestion des personnes) — ainsi que des <a href="/custom-apps/">applications sur mesure</a> conçues pour un flux de travail spécifique. Il est développé par Avenlor Consulting.',
                'FulcrumGrid ist eine Familie zweckgebauter Business-Apps, die auf einem Grid laufen — <a href="/products/command-center/">Command Center</a> (ein Echtzeit-Betriebsdashboard), <a href="/products/collection/">Collection</a> (Forderungen und Zahlungen) und <a href="/products/hr-suite/">HR Suite</a> (Personalmanagement) — sowie <a href="/custom-apps/">individuelle Apps</a> für einen bestimmten Workflow. Sie wird von Avenlor Consulting entwickelt.',
                'FulcrumGrid es una familia de aplicaciones de negocio a medida que funcionan en una sola cuadrícula — <a href="/products/command-center/">Command Center</a> (un panel de operaciones en tiempo real), <a href="/products/collection/">Collection</a> (cuentas por cobrar y pagos) y <a href="/products/hr-suite/">HR Suite</a> (gestión de personas) — además de <a href="/custom-apps/">apps a medida</a> creadas para un flujo de trabajo específico. Está desarrollado por Avenlor Consulting.',
                'FulcrumGrid è una famiglia di applicazioni aziendali su misura che girano su un\'unica griglia — <a href="/products/command-center/">Command Center</a> (una dashboard operativa in tempo reale), <a href="/products/collection/">Collection</a> (crediti e pagamenti) e <a href="/products/hr-suite/">HR Suite</a> (gestione del personale) — oltre ad <a href="/custom-apps/">app su misura</a> create per un flusso di lavoro specifico. È sviluppato da Avenlor Consulting.',
                'FulcrumGrid is een familie doelgerichte bedrijfsapps die op één grid draaien — <a href="/products/command-center/">Command Center</a> (een realtime operationeel dashboard), <a href="/products/collection/">Collection</a> (debiteuren en betalingen) en <a href="/products/hr-suite/">HR Suite</a> (personeelsbeheer) — plus <a href="/custom-apps/">apps op maat</a> gebouwd voor een specifieke workflow. Het wordt gebouwd door Avenlor Consulting.'),
            'Available now: Command Center (operations dashboard), Collection (receivables and payments), and HR Suite (people operations). Close, TMS, Voice, and Assure are coming soon, with CRM, Agents, Real Estate, and Workshop on the <a href="/products/coming-soon/">roadmap</a>, and we also build custom apps on the same grid.': _t(
                'Disponibles dès maintenant : Command Center (tableau de bord des opérations), Collection (créances et paiements) et HR Suite (gestion des personnes). Close, TMS, Voice et Assure arrivent bientôt, avec CRM, Agents, Immobilier et Atelier sur la <a href="/products/coming-soon/">feuille de route</a>, et nous créons aussi des applications sur mesure sur la même grille.',
                'Ab sofort verfügbar: Command Center (Betriebsdashboard), Collection (Forderungen und Zahlungen) und HR Suite (Personalmanagement). Close, TMS, Voice und Assure kommen bald, mit CRM, Agenten, Immobilien und Werkstatt auf der <a href="/products/coming-soon/">Roadmap</a>, und wir entwickeln auch individuelle Apps auf demselben Grid.',
                'Disponibles ahora: Command Center (panel de operaciones), Collection (cobros y pagos) y HR Suite (gestión de personas). Close, TMS, Voice y Assure llegan pronto, con CRM, Agentes, Inmobiliaria y Taller en la <a href="/products/coming-soon/">hoja de ruta</a>, y también creamos apps a medida en la misma cuadrícula.',
                'Disponibili ora: Command Center (dashboard operativa), Collection (crediti e pagamenti) e HR Suite (gestione del personale). Close, TMS, Voice e Assure sono in arrivo, con CRM, Agenti, Immobiliare e Officina nella <a href="/products/coming-soon/">tabella di marcia</a>, e sviluppiamo anche app su misura sulla stessa griglia.',
                'Nu beschikbaar: Command Center (operationeel dashboard), Collection (debiteuren en betalingen) en HR Suite (personeelsbeheer). Close, TMS, Voice en Assure komen binnenkort, met CRM, Agents, Vastgoed en Werkplaats op de <a href="/products/coming-soon/">planning</a>, en we bouwen ook apps op maat op hetzelfde grid.'),
            'FulcrumGrid is built for small and mid-sized businesses and the operations, finance, and people teams that keep them running day to day.': _t(
                'FulcrumGrid est conçu pour les petites et moyennes entreprises et pour les équipes opérations, finance et ressources humaines qui les font tourner au quotidien.',
                'FulcrumGrid ist für kleine und mittlere Unternehmen und für die Betriebs-, Finanz- und Personalteams gemacht, die sie Tag für Tag am Laufen halten.',
                'FulcrumGrid está pensado para pequeñas y medianas empresas y para los equipos de operaciones, finanzas y personas que las mantienen en marcha cada día.',
                'FulcrumGrid è pensato per le piccole e medie imprese e per i team operazioni, finanza e risorse umane che le mandano avanti ogni giorno.',
                'FulcrumGrid is gebouwd voor kleine en middelgrote bedrijven en voor de operationele, financiële en personeelsteams die ze dag in dag uit draaiende houden.'),
            'Yes. You can start with a single app and add the rest whenever you’re ready — everything runs on the same grid, so there’s no migration or re-platforming. See <a href="/pricing/">pricing</a>.': _t(
                'Oui. Vous pouvez commencer avec une seule app et ajouter le reste quand vous êtes prêt — tout fonctionne sur la même grille, il n\'y a donc ni migration ni changement de plateforme. Voir les <a href="/pricing/">tarifs</a>.',
                'Ja. Sie können mit einer einzigen App beginnen und den Rest hinzufügen, wann immer Sie bereit sind — alles läuft auf demselben Grid, es gibt also keine Migration und kein Re-Platforming. Siehe <a href="/pricing/">Preise</a>.',
                'Sí. Puede empezar con una sola app y añadir el resto cuando esté listo — todo funciona en la misma cuadrícula, así que no hay migración ni cambio de plataforma. Consulte los <a href="/pricing/">precios</a>.',
                'Sì. Puoi iniziare con una sola app e aggiungere il resto quando sei pronto — tutto gira sulla stessa griglia, quindi niente migrazione né cambio di piattaforma. Vedi i <a href="/pricing/">prezzi</a>.',
                'Ja. U kunt met één app beginnen en de rest toevoegen wanneer u er klaar voor bent — alles draait op hetzelfde grid, dus geen migratie of overstap naar een ander platform. Bekijk de <a href="/pricing/">prijzen</a>.'),
            'Yes. FulcrumGrid is fully bilingual, with complete English and Arabic (right-to-left) versions of the product and site. See the <a href="/ar/">Arabic site</a>.': _t(
                'Oui. FulcrumGrid est entièrement bilingue, avec des versions complètes en anglais et en arabe (de droite à gauche) du produit et du site. Voir le <a href="/ar/">site en arabe</a>.',
                'Ja. FulcrumGrid ist vollständig zweisprachig, mit kompletten englischen und arabischen (rechts-nach-links) Versionen von Produkt und Website. Siehe die <a href="/ar/">arabische Website</a>.',
                'Sí. FulcrumGrid es totalmente bilingüe, con versiones completas en inglés y árabe (de derecha a izquierda) del producto y del sitio. Consulte el <a href="/ar/">sitio en árabe</a>.',
                'Sì. FulcrumGrid è completamente bilingue, con versioni complete in inglese e arabo (da destra a sinistra) del prodotto e del sito. Vedi il <a href="/ar/">sito in arabo</a>.',
                'Ja. FulcrumGrid is volledig tweetalig, met complete Engelse en Arabische (rechts-naar-links) versies van het product en de site. Bekijk de <a href="/ar/">Arabische site</a>.'),
            'FulcrumGrid uses simple per-user, per-month plans — Starter, Business, and Enterprise — and every plan includes a free trial. See the <a href="/pricing/">pricing page</a> for current details.': _t(
                'FulcrumGrid propose des formules simples par utilisateur et par mois — Starter, Business et Enterprise — et chaque formule inclut un essai gratuit. Consultez la <a href="/pricing/">page des tarifs</a> pour les détails actuels.',
                'FulcrumGrid nutzt einfache Tarife pro Nutzer und Monat — Starter, Business und Enterprise — und jeder Tarif enthält eine kostenlose Testversion. Details finden Sie auf der <a href="/pricing/">Preisseite</a>.',
                'FulcrumGrid usa planes sencillos por usuario y por mes — Starter, Business y Enterprise — y cada plan incluye una prueba gratuita. Consulte la <a href="/pricing/">página de precios</a> para ver los detalles actuales.',
                'FulcrumGrid usa piani semplici per utente e al mese — Starter, Business ed Enterprise — e ogni piano include una prova gratuita. Consulta la <a href="/pricing/">pagina dei prezzi</a> per i dettagli aggiornati.',
                'FulcrumGrid gebruikt eenvoudige abonnementen per gebruiker per maand — Starter, Business en Enterprise — en elk abonnement bevat een gratis proefperiode. Bekijk de <a href="/pricing/">prijspagina</a> voor de actuele details.'),
            'Yes. Every plan includes a 14-day free trial with full features, and no credit card is required to start.': _t(
                "Oui. Chaque formule inclut un essai gratuit de 14 jours avec toutes les fonctionnalités, et aucune carte bancaire n'est requise pour commencer.",
                'Ja. Jeder Tarif enthält eine 14-tägige kostenlose Testversion mit vollem Funktionsumfang, und für den Start ist keine Kreditkarte erforderlich.',
                'Sí. Cada plan incluye una prueba gratuita de 14 días con todas las funciones, y no se requiere tarjeta de crédito para empezar.',
                'Sì. Ogni piano include una prova gratuita di 14 giorni con tutte le funzionalità, e non è richiesta alcuna carta di credito per iniziare.',
                'Ja. Elk abonnement bevat een gratis proefperiode van 14 dagen met alle functies, en er is geen creditcard nodig om te beginnen.'),
            'Yes. Every app keeps clean, structured records you can export at any time. Your data stays yours.': _t(
                'Oui. Chaque app conserve des enregistrements propres et structurés que vous pouvez exporter à tout moment. Vos données restent les vôtres.',
                'Ja. Jede App führt saubere, strukturierte Datensätze, die Sie jederzeit exportieren können. Ihre Daten bleiben Ihre.',
                'Sí. Cada app mantiene registros limpios y estructurados que puede exportar en cualquier momento. Sus datos siguen siendo suyos.',
                'Sì. Ogni app conserva record puliti e strutturati che puoi esportare in qualsiasi momento. I tuoi dati restano tuoi.',
                'Ja. Elke app houdt schone, gestructureerde gegevens bij die u op elk moment kunt exporteren. Uw data blijft van u.'),
            'Each app has role-based access and a full audit trail, so you can grant the right people the right access and see the history of changes.': _t(
                "Chaque app dispose d'un accès basé sur les rôles et d'une piste d'audit complète : vous pouvez ainsi accorder les bons accès aux bonnes personnes et consulter l'historique des modifications.",
                'Jede App verfügt über rollenbasierten Zugriff und ein vollständiges Audit-Protokoll, sodass Sie den richtigen Personen den richtigen Zugriff gewähren und den Änderungsverlauf einsehen können.',
                'Cada app tiene acceso basado en roles y un registro de auditoría completo, de modo que puede dar el acceso adecuado a las personas adecuadas y ver el historial de cambios.',
                "Ogni app dispone di accesso basato sui ruoli e di un registro di controllo completo, così puoi concedere l'accesso giusto alle persone giuste e vedere lo storico delle modifiche.",
                'Elke app heeft rolgebaseerde toegang en een volledig auditspoor, zodat u de juiste mensen de juiste toegang kunt geven en de wijzigingsgeschiedenis kunt bekijken.'),
            'Yes. Beyond the ready-made apps, we build <a href="/custom-apps/">customized business apps</a> tailored to your specific use case, on the same secure, auditable foundation as the rest of the grid.': _t(
                'Oui. Au-delà des apps prêtes à l\'emploi, nous créons des <a href="/custom-apps/">applications métier personnalisées</a> adaptées à votre cas d\'usage précis, sur le même socle sécurisé et auditable que le reste de la grille.',
                'Ja. Über die fertigen Apps hinaus entwickeln wir <a href="/custom-apps/">maßgeschneiderte Business-Apps</a>, die auf Ihren konkreten Anwendungsfall zugeschnitten sind — auf demselben sicheren, prüfbaren Fundament wie der Rest des Grids.',
                'Sí. Más allá de las apps listas para usar, creamos <a href="/custom-apps/">apps de negocio personalizadas</a> adaptadas a su caso de uso concreto, sobre la misma base segura y auditable que el resto de la cuadrícula.',
                'Sì. Oltre alle app pronte all\'uso, creiamo <a href="/custom-apps/">app aziendali personalizzate</a> su misura per il tuo caso d\'uso specifico, sulle stesse fondamenta sicure e verificabili del resto della griglia.',
                'Ja. Naast de kant-en-klare apps bouwen we <a href="/custom-apps/">aangepaste bedrijfsapps</a> op maat van uw specifieke use case, op hetzelfde veilige, controleerbare fundament als de rest van het grid.'),
            'Tell us what your team needs on the <a href="/contact/">contact page</a>, or email <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a> and we’ll show you FulcrumGrid in action.': _t(
                'Dites-nous ce dont votre équipe a besoin sur la <a href="/contact/">page contact</a>, ou écrivez à <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a> et nous vous montrerons FulcrumGrid en action.',
                'Sagen Sie uns auf der <a href="/contact/">Kontaktseite</a>, was Ihr Team braucht, oder schreiben Sie an <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a>, und wir zeigen Ihnen FulcrumGrid in Aktion.',
                'Cuéntenos qué necesita su equipo en la <a href="/contact/">página de contacto</a>, o escriba a <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a> y le mostraremos FulcrumGrid en acción.',
                'Dicci di cosa ha bisogno il tuo team nella <a href="/contact/">pagina dei contatti</a>, oppure scrivi a <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a> e ti mostreremo FulcrumGrid in azione.',
                'Vertel ons wat uw team nodig heeft op de <a href="/contact/">contactpagina</a>, of mail naar <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a> en we tonen u FulcrumGrid in actie.'),
            'FulcrumGrid is built and supported by <a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting</a>.': _t(
                'FulcrumGrid est développé et pris en charge par <a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting</a>.',
                'FulcrumGrid wird von <a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting</a> entwickelt und betreut.',
                'FulcrumGrid está desarrollado y con soporte de <a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting</a>.',
                'FulcrumGrid è sviluppato e supportato da <a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting</a>.',
                'FulcrumGrid wordt ontwikkeld en ondersteund door <a href="https://avenlorconsulting.com" target="_blank" rel="noopener">Avenlor Consulting</a>.'),
            # ---- FAQ JSON-LD answer text (plain, straight apostrophes) ----
            'FulcrumGrid is a family of purpose-built business apps that run on one grid — Command Center (a real-time operations dashboard), Collection (accounts receivable and payments), and HR Suite (people operations) — plus custom apps built for a specific workflow. It is built by Avenlor Consulting.': _t(
                'FulcrumGrid est une famille d\'applications métier sur mesure qui fonctionnent sur une seule grille — Command Center (un tableau de bord des opérations en temps réel), Collection (comptes clients et paiements) et HR Suite (gestion des personnes) — ainsi que des applications sur mesure conçues pour un flux de travail spécifique. Il est développé par Avenlor Consulting.',
                'FulcrumGrid ist eine Familie zweckgebauter Business-Apps, die auf einem Grid laufen — Command Center (ein Echtzeit-Betriebsdashboard), Collection (Forderungen und Zahlungen) und HR Suite (Personalmanagement) — sowie individuelle Apps für einen bestimmten Workflow. Sie wird von Avenlor Consulting entwickelt.',
                'FulcrumGrid es una familia de aplicaciones de negocio a medida que funcionan en una sola cuadrícula — Command Center (un panel de operaciones en tiempo real), Collection (cuentas por cobrar y pagos) y HR Suite (gestión de personas) — además de apps a medida creadas para un flujo de trabajo específico. Está desarrollado por Avenlor Consulting.',
                'FulcrumGrid è una famiglia di applicazioni aziendali su misura che girano su un\'unica griglia — Command Center (una dashboard operativa in tempo reale), Collection (crediti e pagamenti) e HR Suite (gestione del personale) — oltre ad app su misura create per un flusso di lavoro specifico. È sviluppato da Avenlor Consulting.',
                'FulcrumGrid is een familie doelgerichte bedrijfsapps die op één grid draaien — Command Center (een realtime operationeel dashboard), Collection (debiteuren en betalingen) en HR Suite (personeelsbeheer) — plus apps op maat gebouwd voor een specifieke workflow. Het wordt gebouwd door Avenlor Consulting.'),
            'Available now: Command Center (operations dashboard), Collection (receivables and payments), and HR Suite (people operations). Close, TMS, Voice, and Assure are coming soon, with CRM, Agents, Real Estate, and Workshop on the roadmap, and we also build custom apps on the same grid.': _t(
                'Disponibles dès maintenant : Command Center (tableau de bord des opérations), Collection (créances et paiements) et HR Suite (gestion des personnes). Close, TMS, Voice et Assure arrivent bientôt, avec CRM, Agents, Immobilier et Atelier sur la feuille de route, et nous créons aussi des applications sur mesure sur la même grille.',
                'Ab sofort verfügbar: Command Center (Betriebsdashboard), Collection (Forderungen und Zahlungen) und HR Suite (Personalmanagement). Close, TMS, Voice und Assure kommen bald, mit CRM, Agenten, Immobilien und Werkstatt auf der Roadmap, und wir entwickeln auch individuelle Apps auf demselben Grid.',
                'Disponibles ahora: Command Center (panel de operaciones), Collection (cobros y pagos) y HR Suite (gestión de personas). Close, TMS, Voice y Assure llegan pronto, con CRM, Agentes, Inmobiliaria y Taller en la hoja de ruta, y también creamos apps a medida en la misma cuadrícula.',
                'Disponibili ora: Command Center (dashboard operativa), Collection (crediti e pagamenti) e HR Suite (gestione del personale). Close, TMS, Voice e Assure sono in arrivo, con CRM, Agenti, Immobiliare e Officina nella roadmap, e sviluppiamo anche app su misura sulla stessa griglia.',
                'Nu beschikbaar: Command Center (operationeel dashboard), Collection (debiteuren en betalingen) en HR Suite (personeelsbeheer). Close, TMS, Voice en Assure komen binnenkort, met CRM, Agents, Vastgoed en Werkplaats op de roadmap, en we bouwen ook apps op maat op hetzelfde grid.'),
            "Yes. You can start with a single app and add the rest whenever you're ready — everything runs on the same grid, so there's no migration or re-platforming.": _t(
                "Oui. Vous pouvez commencer avec une seule app et ajouter le reste quand vous êtes prêt — tout fonctionne sur la même grille, il n'y a donc ni migration ni changement de plateforme.",
                'Ja. Sie können mit einer einzigen App beginnen und den Rest hinzufügen, wann immer Sie bereit sind — alles läuft auf demselben Grid, es gibt also keine Migration und kein Re-Platforming.',
                'Sí. Puede empezar con una sola app y añadir el resto cuando esté listo — todo funciona en la misma cuadrícula, así que no hay migración ni cambio de plataforma.',
                'Sì. Puoi iniziare con una sola app e aggiungere il resto quando sei pronto — tutto gira sulla stessa griglia, quindi niente migrazione né cambio di piattaforma.',
                'Ja. U kunt met één app beginnen en de rest toevoegen wanneer u er klaar voor bent — alles draait op hetzelfde grid, dus geen migratie of overstap naar een ander platform.'),
            'Yes. FulcrumGrid is fully bilingual, with complete English and Arabic (right-to-left) versions of the product and site.': _t(
                'Oui. FulcrumGrid est entièrement bilingue, avec des versions complètes en anglais et en arabe (de droite à gauche) du produit et du site.',
                'Ja. FulcrumGrid ist vollständig zweisprachig, mit kompletten englischen und arabischen (rechts-nach-links) Versionen von Produkt und Website.',
                'Sí. FulcrumGrid es totalmente bilingüe, con versiones completas en inglés y árabe (de derecha a izquierda) del producto y del sitio.',
                'Sì. FulcrumGrid è completamente bilingue, con versioni complete in inglese e arabo (da destra a sinistra) del prodotto e del sito.',
                'Ja. FulcrumGrid is volledig tweetalig, met complete Engelse en Arabische (rechts-naar-links) versies van het product en de site.'),
            'FulcrumGrid uses simple per-user, per-month plans — Starter, Business, and Enterprise — and every plan includes a free trial. See the pricing page for current details.': _t(
                'FulcrumGrid propose des formules simples par utilisateur et par mois — Starter, Business et Enterprise — et chaque formule inclut un essai gratuit. Consultez la page des tarifs pour les détails actuels.',
                'FulcrumGrid nutzt einfache Tarife pro Nutzer und Monat — Starter, Business und Enterprise — und jeder Tarif enthält eine kostenlose Testversion. Details finden Sie auf der Preisseite.',
                'FulcrumGrid usa planes sencillos por usuario y por mes — Starter, Business y Enterprise — y cada plan incluye una prueba gratuita. Consulte la página de precios para ver los detalles actuales.',
                'FulcrumGrid usa piani semplici per utente e al mese — Starter, Business ed Enterprise — e ogni piano include una prova gratuita. Consulta la pagina dei prezzi per i dettagli aggiornati.',
                'FulcrumGrid gebruikt eenvoudige abonnementen per gebruiker per maand — Starter, Business en Enterprise — en elk abonnement bevat een gratis proefperiode. Bekijk de prijspagina voor de actuele details.'),
            'Yes. Beyond the ready-made apps, we build customized business apps tailored to your specific use case, on the same secure, auditable foundation as the rest of the grid.': _t(
                'Oui. Au-delà des apps prêtes à l\'emploi, nous créons des applications métier personnalisées adaptées à votre cas d\'usage précis, sur le même socle sécurisé et auditable que le reste de la grille.',
                'Ja. Über die fertigen Apps hinaus entwickeln wir maßgeschneiderte Business-Apps, die auf Ihren konkreten Anwendungsfall zugeschnitten sind — auf demselben sicheren, prüfbaren Fundament wie der Rest des Grids.',
                'Sí. Más allá de las apps listas para usar, creamos apps de negocio personalizadas adaptadas a su caso de uso concreto, sobre la misma base segura y auditable que el resto de la cuadrícula.',
                'Sì. Oltre alle app pronte all\'uso, creiamo app aziendali personalizzate su misura per il tuo caso d\'uso specifico, sulle stesse fondamenta sicure e verificabili del resto della griglia.',
                'Ja. Naast de kant-en-klare apps bouwen we aangepaste bedrijfsapps op maat van uw specifieke use case, op hetzelfde veilige, controleerbare fundament als de rest van het grid.'),
            "Tell us what your team needs on the contact page, or email contact@avenlorconsulting.com and we'll show you FulcrumGrid in action.": _t(
                'Dites-nous ce dont votre équipe a besoin sur la page contact, ou écrivez à contact@avenlorconsulting.com et nous vous montrerons FulcrumGrid en action.',
                'Sagen Sie uns auf der Kontaktseite, was Ihr Team braucht, oder schreiben Sie an contact@avenlorconsulting.com, und wir zeigen Ihnen FulcrumGrid in Aktion.',
                'Cuéntenos qué necesita su equipo en la página de contacto, o escriba a contact@avenlorconsulting.com y le mostraremos FulcrumGrid en acción.',
                'Dicci di cosa ha bisogno il tuo team nella pagina dei contatti, oppure scrivi a contact@avenlorconsulting.com e ti mostreremo FulcrumGrid in azione.',
                'Vertel ons wat uw team nodig heeft op de contactpagina, of mail naar contact@avenlorconsulting.com en we tonen u FulcrumGrid in actie.'),
            'FulcrumGrid is built and supported by Avenlor Consulting.': _t(
                'FulcrumGrid est développé et pris en charge par Avenlor Consulting.',
                'FulcrumGrid wird von Avenlor Consulting entwickelt und betreut.',
                'FulcrumGrid está desarrollado y con soporte de Avenlor Consulting.',
                'FulcrumGrid è sviluppato e supportato da Avenlor Consulting.',
                'FulcrumGrid wordt ontwikkeld en ondersteund door Avenlor Consulting.'),
            # ---- CTA panel ----
            'Still have<br />a question?': _t('Vous avez encore<br />une question ?', 'Noch<br />eine Frage?', '¿Aún tiene<br />una pregunta?', 'Hai ancora<br />una domanda?', 'Nog<br />een vraag?'),
            "Tell us what your team needs and we'll walk you through FulcrumGrid.": _t(
                'Dites-nous ce dont votre équipe a besoin et nous vous guiderons dans FulcrumGrid.',
                'Sagen Sie uns, was Ihr Team braucht, und wir führen Sie durch FulcrumGrid.',
                'Cuéntenos qué necesita su equipo y le guiaremos por FulcrumGrid.',
                'Dicci di cosa ha bisogno il tuo team e ti guideremo attraverso FulcrumGrid.',
                'Vertel ons wat uw team nodig heeft en we leiden u door FulcrumGrid.'),
            'See pricing': _t('Voir les tarifs', 'Preise ansehen', 'Ver precios', 'Vedi i prezzi', 'Bekijk prijzen'),
        },
    },
}
