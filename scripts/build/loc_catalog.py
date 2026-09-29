# -*- coding: utf-8 -*-
"""Hand-written translations for the static (non-generator) pages.

COMMON  — chrome that repeats on every page (nav, footer, buttons). Applied
          best-effort: a page that lacks a segment simply skips it.
PAGES   — per-page copy, keyed by canonical path. Applied strictly: every
          declared English segment must exist in that page's EN source.

Conventions:
  * Brand and product names stay English: FulcrumGrid, Command Center,
    Collection, HR Suite. "Blog" and "FAQ" are left untranslated.
  * Keys are the EXACT English text as it appears in the source HTML
    (including curly apostrophes and the ↗ glyph).
  * Every key carries fr/de/es/it/nl. English + Arabic are authored elsewhere.
"""

def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


COMMON = {
    # Nav / footer labels
    'Products':      _t('Produits', 'Produkte', 'Productos', 'Prodotti', 'Producten'),
    'Platform':      _t('Plateforme', 'Plattform', 'Plataforma', 'Piattaforma', 'Platform'),
    'Pricing':       _t('Tarifs', 'Preise', 'Precios', 'Prezzi', 'Prijzen'),
    'Regions':       _t('Régions', 'Regionen', 'Regiones', 'Regioni', "Regio's"),
    'About':         _t('À propos', 'Über uns', 'Acerca de', 'Chi siamo', 'Over ons'),
    'Contact':       _t('Contact', 'Kontakt', 'Contacto', 'Contatti', 'Contact'),
    'Company':       _t('Entreprise', 'Unternehmen', 'Empresa', 'Azienda', 'Bedrijf'),
    'All products':  _t('Tous les produits', 'Alle Produkte', 'Todos los productos', 'Tutti i prodotti', 'Alle producten'),
    'Custom apps':   _t('Applications sur mesure', 'Individuelle Apps', 'Apps a medida', 'App su misura', 'Apps op maat'),
    'Coming soon':   _t('Bientôt disponible', 'Demnächst', 'Próximamente', 'In arrivo', 'Binnenkort'),
    'Features':      _t('Fonctionnalités', 'Funktionen', 'Funciones', 'Funzionalità', 'Functies'),
    'How it works':  _t('Comment ça marche', "So funktioniert's", 'Cómo funciona', 'Come funziona', 'Hoe het werkt'),
    'Email us':      _t('Écrivez-nous', 'Schreiben Sie uns', 'Escríbenos', 'Scrivici', 'Mail ons'),
    'Privacy':       _t('Confidentialité', 'Datenschutz', 'Privacidad', 'Privacy', 'Privacy'),
    # Buttons / a11y
    'Request a demo': _t('Demander une démo', 'Demo anfragen', 'Solicitar una demo', 'Richiedi una demo', 'Vraag een demo aan'),
    'Skip to content': _t('Aller au contenu', 'Zum Inhalt springen', 'Ir al contenido', 'Vai al contenuto', 'Naar de inhoud'),
    'Toggle menu':   _t('Basculer le menu', 'Menü umschalten', 'Alternar menú', 'Attiva/disattiva menu', 'Menu wisselen'),
    'FulcrumGrid home': _t('Accueil FulcrumGrid', 'FulcrumGrid Startseite', 'Inicio de FulcrumGrid', 'Home di FulcrumGrid', 'FulcrumGrid home'),
    # Shared tagline (period version listed first so longest-match wins)
    'The operational backbone for modern teams.': _t(
        "L'épine dorsale opérationnelle des équipes modernes.",
        'Das operative Rückgrat für moderne Teams.',
        'La columna vertebral operativa de los equipos modernos.',
        'La spina dorsale operativa dei team moderni.',
        'De operationele ruggengraat voor moderne teams.'),
    'The operational backbone for modern teams': _t(
        "L'épine dorsale opérationnelle des équipes modernes",
        'Das operative Rückgrat für moderne Teams',
        'La columna vertebral operativa de los equipos modernos',
        'La spina dorsale operativa dei team moderni',
        'De operationele ruggengraat voor moderne teams'),
    'All rights reserved.': _t('Tous droits réservés.', 'Alle Rechte vorbehalten.', 'Todos los derechos reservados.', 'Tutti i diritti riservati.', 'Alle rechten voorbehouden.'),
    # JSON-LD available languages
    '["English", "Arabic"]': {k: '["English", "Arabic", "French", "German", "Spanish", "Italian", "Dutch"]' for k in ('fr', 'de', 'es', 'it', 'nl')},
}


PAGES = {
    '/': {
        'src': 'index.html',
        't': {
            # ---- Meta ----
            'FulcrumGrid — One platform for every operation': _t(
                'FulcrumGrid — Une plateforme pour chaque opération',
                'FulcrumGrid — Eine Plattform für jeden Betrieb',
                'FulcrumGrid — Una plataforma para cada operación',
                'FulcrumGrid — Una piattaforma per ogni operazione',
                'FulcrumGrid — Eén platform voor elke operatie'),
            'FulcrumGrid is the operational backbone for modern businesses — Command Center, Collection, HR Suite, and more: purpose-built business apps from one team.': _t(
                "FulcrumGrid est l'épine dorsale opérationnelle des entreprises modernes — Command Center, Collection, HR Suite et plus : des applications métier sur mesure, d'une seule équipe.",
                'FulcrumGrid ist das operative Rückgrat für moderne Unternehmen — Command Center, Collection, HR Suite und mehr: zweckgebaute Business-Apps aus einer Hand.',
                'FulcrumGrid es la columna vertebral operativa de las empresas modernas — Command Center, Collection, HR Suite y más: aplicaciones de negocio a medida, de un solo equipo.',
                'FulcrumGrid è la spina dorsale operativa delle aziende moderne — Command Center, Collection, HR Suite e altro: applicazioni aziendali su misura, da un unico team.',
                'FulcrumGrid is de operationele ruggengraat voor moderne bedrijven — Command Center, Collection, HR Suite en meer: doelgerichte bedrijfsapps van één team.'),
            'Command Center, Collection, HR Suite, and more — purpose-built business apps from one team.': _t(
                "Command Center, Collection, HR Suite et plus — des applications métier sur mesure, d'une seule équipe.",
                'Command Center, Collection, HR Suite und mehr — zweckgebaute Business-Apps aus einer Hand.',
                'Command Center, Collection, HR Suite y más — aplicaciones de negocio a medida, de un solo equipo.',
                'Command Center, Collection, HR Suite e altro — applicazioni aziendali su misura, da un unico team.',
                'Command Center, Collection, HR Suite en meer — doelgerichte bedrijfsapps van één team.'),
            'FulcrumGrid — purpose-built business apps for every operation': _t(
                'FulcrumGrid — des applications métier sur mesure pour chaque opération',
                'FulcrumGrid — zweckgebaute Business-Apps für jeden Betrieb',
                'FulcrumGrid — aplicaciones de negocio a medida para cada operación',
                'FulcrumGrid — applicazioni aziendali su misura per ogni operazione',
                'FulcrumGrid — doelgerichte bedrijfsapps voor elke operatie'),
            # ---- Hero ----
            'One platform.<br />Every <em>operation.</em>': _t(
                'Une plateforme.<br />Chaque <em>opération.</em>',
                'Eine Plattform.<br />Jeder <em>Betrieb.</em>',
                'Una plataforma.<br />Cada <em>operación.</em>',
                'Una piattaforma.<br />Ogni <em>operazione.</em>',
                'Eén platform.<br />Elke <em>operatie.</em>'),
            'FulcrumGrid is a growing family of business apps — Command Center, Collection, HR Suite, and more. Each one is purpose-built for the job, with the same clean, consistent experience across the grid.': _t(
                "FulcrumGrid est une famille grandissante d'applications métier — Command Center, Collection, HR Suite et plus. Chacune est conçue sur mesure pour sa tâche, avec la même expérience claire et cohérente sur toute la grille.",
                'FulcrumGrid ist eine wachsende Familie von Business-Apps — Command Center, Collection, HR Suite und mehr. Jede ist zweckgebaut für ihre Aufgabe, mit demselben klaren, konsistenten Erlebnis über das gesamte Grid.',
                'FulcrumGrid es una familia creciente de aplicaciones de negocio — Command Center, Collection, HR Suite y más. Cada una está diseñada a medida para su función, con la misma experiencia clara y coherente en toda la cuadrícula.',
                "FulcrumGrid è una famiglia in crescita di applicazioni aziendali — Command Center, Collection, HR Suite e altro. Ognuna è costruita su misura per il proprio compito, con la stessa esperienza pulita e coerente su tutta la griglia.",
                'FulcrumGrid is een groeiende familie bedrijfsapps — Command Center, Collection, HR Suite en meer. Elk is doelgericht gebouwd voor de taak, met dezelfde heldere, consistente ervaring over het hele grid.'),
            'Explore the apps': _t('Découvrir les applications', 'Apps entdecken', 'Explorar las apps', 'Esplora le app', 'Ontdek de apps'),
            'Scroll': _t('Défiler', 'Scrollen', 'Desplazar', 'Scorri', 'Scroll'),
            # ---- Proof row ----
            'At a glance': _t("En un coup d'œil", 'Auf einen Blick', 'De un vistazo', 'In sintesi', 'In het kort'),
            'FulcrumGrid / in brief': _t('FulcrumGrid / en bref', 'FulcrumGrid / in Kürze', 'FulcrumGrid / en breve', 'FulcrumGrid / in breve', 'FulcrumGrid / in het kort'),
            'A growing family of purpose-built business apps, unified on one grid.': _t(
                "Une famille grandissante d'applications métier sur mesure, réunies sur une seule grille.",
                'Eine wachsende Familie zweckgebauter Business-Apps, vereint auf einem Grid.',
                'Una familia creciente de aplicaciones de negocio a medida, unificadas en una sola cuadrícula.',
                "Una famiglia in crescita di applicazioni aziendali su misura, unificate su un'unica griglia.",
                'Een groeiende familie doelgerichte bedrijfsapps, verenigd op één grid.'),
            'Apps live today': _t('Applications disponibles', 'Apps heute verfügbar', 'Apps disponibles hoy', 'App disponibili oggi', 'Apps nu beschikbaar'),
            'Three': _t('Trois', 'Drei', 'Tres', 'Tre', 'Drie'),
            'Experience': _t('Expérience', 'Erlebnis', 'Experiencia', 'Esperienza', 'Ervaring'),
            'One grid': _t('Une grille', 'Ein Grid', 'Una cuadrícula', 'Una griglia', 'Eén grid'),
            'Deploy': _t('Déploiement', 'Einführung', 'Despliegue', 'Implementazione', 'Uitrol'),
            'What you need': _t("Ce qu'il vous faut", 'Was Sie brauchen', 'Lo que necesita', 'Ciò che serve', 'Wat u nodig hebt'),
            # ---- Products ----
            'The grid of apps': _t("La grille d'applications", 'Das Grid der Apps', 'La cuadrícula de apps', 'La griglia di app', 'Het grid van apps'),
            'Purpose-built apps for every operation.': _t(
                'Des applications sur mesure pour chaque opération.',
                'Zweckgebaute Apps für jeden Betrieb.',
                'Aplicaciones a medida para cada operación.',
                'App su misura per ogni operazione.',
                'Doelgerichte apps voor elke operatie.'),
            'Each app solves a real problem on its own. Start with one today, and add more as you grow.': _t(
                "Chaque application résout à elle seule un vrai problème. Commencez par une aujourd'hui, et ajoutez-en d'autres à mesure que vous grandissez.",
                'Jede App löst für sich ein echtes Problem. Starten Sie heute mit einer und fügen Sie weitere hinzu, wenn Sie wachsen.',
                'Cada app resuelve por sí sola un problema real. Empiece hoy con una y añada más a medida que crece.',
                'Ogni app risolve da sola un problema reale. Inizia oggi con una e aggiungine altre man mano che cresci.',
                'Elke app lost op zichzelf een echt probleem op. Begin vandaag met één en voeg er meer toe naarmate u groeit.'),
            'Real-time operations dashboard. Monitor every metric, workflow, and alert across your business from one screen.': _t(
                'Tableau de bord des opérations en temps réel. Surveillez chaque indicateur, flux de travail et alerte de votre entreprise depuis un seul écran.',
                'Echtzeit-Dashboard für den Betrieb. Überwachen Sie jede Kennzahl, jeden Workflow und jede Warnung Ihres Unternehmens von einem Bildschirm aus.',
                'Panel de operaciones en tiempo real. Supervise cada métrica, flujo de trabajo y alerta de su negocio desde una sola pantalla.',
                "Dashboard operativa in tempo reale. Monitora ogni metrica, flusso di lavoro e avviso della tua azienda da un'unica schermata.",
                'Realtime operationeel dashboard. Volg elke metriek, workflow en melding in uw bedrijf vanaf één scherm.'),
            'Explore Command Center ↗': _t('Découvrir Command Center ↗', 'Command Center entdecken ↗', 'Explorar Command Center ↗', 'Esplora Command Center ↗', 'Ontdek Command Center ↗'),
            'Receivables and payments, handled. Track invoices, automate reminders, and get paid faster without the chase.': _t(
                'Créances et paiements, maîtrisés. Suivez les factures, automatisez les relances et soyez payé plus vite sans courir après.',
                'Forderungen und Zahlungen, im Griff. Verfolgen Sie Rechnungen, automatisieren Sie Erinnerungen und werden Sie schneller bezahlt — ohne Hinterherlaufen.',
                'Cobros y pagos, resueltos. Controle facturas, automatice recordatorios y cobre más rápido sin perseguir a nadie.',
                'Crediti e pagamenti, gestiti. Monitora le fatture, automatizza i solleciti e fatti pagare più in fretta senza rincorrere nessuno.',
                'Vorderingen en betalingen, geregeld. Volg facturen, automatiseer herinneringen en word sneller betaald zonder achtervolging.'),
            'Explore Collection ↗': _t('Découvrir Collection ↗', 'Collection entdecken ↗', 'Explorar Collection ↗', 'Esplora Collection ↗', 'Ontdek Collection ↗'),
            'People operations from hire to retire. Manage employees, payroll, time off, and everything in between.': _t(
                "La gestion des personnes, de l'embauche au départ. Gérez les employés, la paie, les congés et tout le reste.",
                'Personalmanagement von der Einstellung bis zum Ruhestand. Verwalten Sie Mitarbeiter, Gehaltsabrechnung, Abwesenheiten und alles dazwischen.',
                'Gestión de personas, de la contratación a la jubilación. Gestione empleados, nóminas, ausencias y todo lo demás.',
                "Gestione del personale, dall'assunzione alla pensione. Gestisci dipendenti, buste paga, ferie e tutto il resto.",
                'Personeelsbeheer van aanwerving tot pensioen. Beheer medewerkers, loonadministratie, verlof en alles daartussenin.'),
            'Explore HR Suite ↗': _t('Découvrir HR Suite ↗', 'HR Suite entdecken ↗', 'Explorar HR Suite ↗', 'Esplora HR Suite ↗', 'Ontdek HR Suite ↗'),
            'View all products ↗': _t('Voir tous les produits ↗', 'Alle Produkte ansehen ↗', 'Ver todos los productos ↗', 'Vedi tutti i prodotti ↗', 'Bekijk alle producten ↗'),
            # ---- One standard panel ----
            'One standard': _t('Un seul standard', 'Ein Standard', 'Un solo estándar', 'Un unico standard', 'Eén standaard'),
            'Built to the same high standard.': _t(
                'Conçues selon le même haut standard.', 'Nach demselben hohen Standard gebaut.',
                'Creadas con el mismo alto estándar.', 'Costruite secondo lo stesso alto standard.',
                'Gebouwd volgens dezelfde hoge standaard.'),
            'Every app on the grid shares one interface, one login, and one way of working — so moving between them feels like using a single product, not a bundle of tools.': _t(
                "Chaque application de la grille partage une même interface, un même identifiant et une même façon de travailler — passer de l'une à l'autre revient à utiliser un seul produit, pas un assemblage d'outils.",
                'Jede App im Grid teilt eine Oberfläche, eine Anmeldung und eine Arbeitsweise — der Wechsel zwischen ihnen fühlt sich an wie ein einziges Produkt, nicht wie ein Bündel von Tools.',
                'Cada app de la cuadrícula comparte una interfaz, un inicio de sesión y una forma de trabajar — pasar de una a otra se siente como usar un solo producto, no un conjunto de herramientas.',
                "Ogni app della griglia condivide un'unica interfaccia, un unico accesso e un unico modo di lavorare — passare dall'una all'altra è come usare un solo prodotto, non un insieme di strumenti.",
                'Elke app op het grid deelt één interface, één login en één manier van werken — schakelen ertussen voelt als één product, niet als een bundel tools.'),
            'Shared sign-in across every app': _t('Connexion partagée sur toutes les applications', 'Gemeinsame Anmeldung für alle Apps', 'Inicio de sesión compartido en todas las apps', 'Accesso condiviso su tutte le app', 'Gedeelde login voor elke app'),
            'Consistent layout, shortcuts, and controls': _t('Mise en page, raccourcis et commandes cohérents', 'Einheitliches Layout, Shortcuts und Bedienelemente', 'Diseño, atajos y controles coherentes', 'Layout, scorciatoie e controlli coerenti', 'Consistente lay-out, sneltoetsen en besturing'),
            'Data that connects instead of scattering': _t('Des données qui se connectent au lieu de se disperser', 'Daten, die sich verbinden statt zu zerstreuen', 'Datos que se conectan en lugar de dispersarse', 'Dati che si collegano invece di disperdersi', 'Data die verbindt in plaats van versnippert'),
            # ---- Platform panel ----
            'The platform': _t('La plateforme', 'Die Plattform', 'La plataforma', 'La piattaforma', 'Het platform'),
            'One platform beneath every app.': _t(
                'Une seule plateforme sous chaque application.', 'Eine Plattform unter jeder App.',
                'Una sola plataforma bajo cada app.', "Un'unica piattaforma sotto ogni app.",
                'Eén platform onder elke app.'),
            'Command Center, Collection, and HR Suite all run on the same foundation — the same security, the same reliability, the same team. Add an app and it simply belongs.': _t(
                "Command Center, Collection et HR Suite reposent tous sur les mêmes fondations — la même sécurité, la même fiabilité, la même équipe. Ajoutez une application et elle s'intègre naturellement.",
                'Command Center, Collection und HR Suite laufen alle auf demselben Fundament — dieselbe Sicherheit, dieselbe Zuverlässigkeit, dasselbe Team. Fügen Sie eine App hinzu, und sie gehört einfach dazu.',
                'Command Center, Collection y HR Suite funcionan sobre la misma base — la misma seguridad, la misma fiabilidad, el mismo equipo. Añada una app y sencillamente encaja.',
                "Command Center, Collection e HR Suite girano tutte sulle stesse fondamenta — la stessa sicurezza, la stessa affidabilità, lo stesso team. Aggiungi un'app e si integra naturalmente.",
                'Command Center, Collection en HR Suite draaien allemaal op hetzelfde fundament — dezelfde beveiliging, dezelfde betrouwbaarheid, hetzelfde team. Voeg een app toe en ze hoort er gewoon bij.'),
            'Composable — run one app or the whole grid': _t('Modulaire — une seule application ou toute la grille', 'Komponierbar — eine App oder das ganze Grid', 'Componible — una app o toda la cuadrícula', "Componibile — una sola app o l'intera griglia", 'Samenstelbaar — één app of het hele grid'),
            'Secure by default, maintained by one team': _t('Sécurisé par défaut, maintenu par une seule équipe', 'Standardmäßig sicher, gepflegt von einem Team', 'Seguro por defecto, mantenido por un solo equipo', 'Sicuro per impostazione predefinita, mantenuto da un unico team', 'Standaard veilig, onderhouden door één team'),
            'Human-readable, built for real operating pressure': _t("Lisible par l'humain, conçu pour la pression opérationnelle réelle", 'Menschenlesbar, gebaut für echten Betriebsdruck', 'Legible para las personas, creado para la presión operativa real', 'Leggibile dalle persone, costruito per la reale pressione operativa', 'Leesbaar voor mensen, gebouwd voor echte operationele druk'),
            'On the roadmap': _t('Sur la feuille de route', 'Auf der Roadmap', 'En la hoja de ruta', 'Nella roadmap', 'Op de roadmap'),
            'More apps are joining the grid, each built to the same standard.': _t(
                "D'autres applications rejoignent la grille, chacune conçue selon le même standard.",
                'Weitere Apps kommen ins Grid, jede nach demselben Standard gebaut.',
                'Más apps se unen a la cuadrícula, cada una creada con el mismo estándar.',
                'Altre app si uniscono alla griglia, ognuna costruita secondo lo stesso standard.',
                'Meer apps komen bij het grid, elk gebouwd volgens dezelfde standaard.'),
            '<span class="fg-tag">Inventory</span>': _t('<span class="fg-tag">Inventaire</span>', '<span class="fg-tag">Lagerverwaltung</span>', '<span class="fg-tag">Inventario</span>', '<span class="fg-tag">Inventario</span>', '<span class="fg-tag">Voorraad</span>'),
            '<span class="fg-tag">Procurement</span>': _t('<span class="fg-tag">Achats</span>', '<span class="fg-tag">Beschaffung</span>', '<span class="fg-tag">Compras</span>', '<span class="fg-tag">Approvvigionamento</span>', '<span class="fg-tag">Inkoop</span>'),
            # ---- How it works ----
            'Get running': _t('Se lancer', 'Loslegen', 'Poner en marcha', 'Inizia subito', 'Aan de slag'),
            'Live in three steps.': _t('Opérationnel en trois étapes.', 'In drei Schritten startklar.', 'En marcha en tres pasos.', 'Operativo in tre passi.', 'Live in drie stappen.'),
            'Choose your apps, set them up in minutes, and run your operations — adding more apps at your own pace.': _t(
                'Choisissez vos applications, configurez-les en quelques minutes et pilotez vos opérations — en ajoutant d\'autres applications à votre rythme.',
                'Wählen Sie Ihre Apps, richten Sie sie in Minuten ein und steuern Sie Ihren Betrieb — weitere Apps in Ihrem eigenen Tempo.',
                'Elija sus apps, configúrelas en minutos y gestione sus operaciones — añadiendo más apps a su propio ritmo.',
                'Scegli le tue app, configurale in pochi minuti e gestisci le tue operazioni — aggiungendo altre app al tuo ritmo.',
                'Kies uw apps, stel ze in minuten in en run uw operatie — voeg meer apps toe in uw eigen tempo.'),
            'Choose your apps': _t('Choisissez vos applications', 'Wählen Sie Ihre Apps', 'Elija sus apps', 'Scegli le tue app', 'Kies uw apps'),
            'Pick the app that solves your most pressing problem first. No all-or-nothing rollout.': _t(
                "Choisissez d'abord l'application qui résout votre problème le plus urgent. Pas de déploiement tout-ou-rien.",
                'Wählen Sie zuerst die App, die Ihr dringendstes Problem löst. Kein Alles-oder-nichts-Rollout.',
                'Elija primero la app que resuelve su problema más urgente. Sin despliegue de todo o nada.',
                'Scegli prima l\'app che risolve il tuo problema più urgente. Nessun rollout tutto-o-niente.',
                'Kies eerst de app die uw meest dringende probleem oplost. Geen alles-of-niets-uitrol.'),
            'Set up in minutes': _t('Configurez en quelques minutes', 'In Minuten einrichten', 'Configure en minutos', 'Configura in pochi minuti', 'Stel in binnen minuten'),
            'Sensible defaults and a consistent interface mean your team is productive the same day.': _t(
                'Des réglages par défaut pertinents et une interface cohérente rendent votre équipe productive dès le premier jour.',
                'Sinnvolle Voreinstellungen und eine einheitliche Oberfläche machen Ihr Team noch am selben Tag produktiv.',
                'Unos ajustes por defecto sensatos y una interfaz coherente hacen que su equipo sea productivo el mismo día.',
                'Impostazioni predefinite sensate e un\'interfaccia coerente rendono il tuo team produttivo già dal primo giorno.',
                'Verstandige standaardinstellingen en een consistente interface maken uw team dezelfde dag productief.'),
            'Run your operations': _t('Pilotez vos opérations', 'Steuern Sie Ihren Betrieb', 'Gestione sus operaciones', 'Gestisci le tue operazioni', 'Run uw operatie'),
            'Work in one clean experience, and add more apps from the grid whenever you’re ready.': _t(
                "Travaillez dans une expérience unique et épurée, et ajoutez d'autres applications de la grille quand vous êtes prêt.",
                'Arbeiten Sie in einem einzigen, klaren Erlebnis und fügen Sie weitere Apps aus dem Grid hinzu, wann immer Sie bereit sind.',
                'Trabaje en una experiencia única y limpia, y añada más apps de la cuadrícula cuando esté listo.',
                "Lavora in un'unica esperienza pulita e aggiungi altre app dalla griglia quando sei pronto.",
                'Werk in één heldere ervaring en voeg meer apps van het grid toe wanneer u er klaar voor bent.'),
            'See how it works ↗': _t('Voir comment ça marche ↗', "So funktioniert's ↗", 'Ver cómo funciona ↗', 'Scopri come funziona ↗', 'Bekijk hoe het werkt ↗'),
            # ---- Quote ----
            'Why one grid': _t('Pourquoi une seule grille', 'Warum ein Grid', 'Por qué una sola cuadrícula', "Perché un'unica griglia", 'Waarom één grid'),
            'When every team runs on a different tool, alignment is just a polite word for overhead.': _t(
                'Quand chaque équipe utilise un outil différent, « alignement » n\'est qu\'un mot poli pour dire surcharge.',
                'Wenn jedes Team ein anderes Tool nutzt, ist „Abstimmung“ nur ein höfliches Wort für Mehraufwand.',
                'Cuando cada equipo usa una herramienta distinta, «alineación» no es más que una palabra amable para decir sobrecarga.',
                'Quando ogni team usa uno strumento diverso, «allineamento» è solo un modo gentile per dire sovraccarico.',
                "Als elk team met een ander tool werkt, is 'afstemming' maar een net woord voor overhead."),
            'One grid changes that.': _t('Une seule grille change la donne.', 'Ein Grid ändert das.', 'Una sola cuadrícula lo cambia.', "Un'unica griglia cambia tutto.", 'Eén grid verandert dat.'),
            # ---- CTA ----
            'Ready to run on one grid?': _t('Prêt à tout piloter sur une seule grille ?', 'Bereit, auf einem Grid zu arbeiten?', '¿Listo para operar en una sola cuadrícula?', "Pronto a lavorare su un'unica griglia?", 'Klaar om op één grid te werken?'),
            'Tell us what your team needs and we’ll show you FulcrumGrid in action.': _t(
                'Dites-nous ce dont votre équipe a besoin et nous vous montrerons FulcrumGrid en action.',
                'Sagen Sie uns, was Ihr Team braucht, und wir zeigen Ihnen FulcrumGrid in Aktion.',
                'Cuéntenos qué necesita su equipo y le mostraremos FulcrumGrid en acción.',
                'Dicci di cosa ha bisogno il tuo team e ti mostreremo FulcrumGrid in azione.',
                'Vertel ons wat uw team nodig heeft en we tonen u FulcrumGrid in actie.'),
            # ("Request a demo ↗" is covered by the COMMON "Request a demo" segment.)
            # ---- Image alts ----
            'A luminous cobalt grid held within pale architectural planes': _t(
                'Une grille cobalt lumineuse tenue dans de pâles plans architecturaux',
                'Ein leuchtendes kobaltblaues Grid in blassen architektonischen Ebenen',
                'Una luminosa cuadrícula cobalto contenida en pálidos planos arquitectónicos',
                'Una luminosa griglia cobalto racchiusa in pallidi piani architettonici',
                'Een lichtgevend kobaltblauw grid in bleke architecturale vlakken'),
            'Translucent cobalt filaments converging at a single fulcrum point': _t(
                "Des filaments cobalt translucides convergeant vers un unique point d'appui",
                'Durchscheinende kobaltblaue Fäden, die in einem einzigen Angelpunkt zusammenlaufen',
                'Filamentos cobalto translúcidos que convergen en un único punto de apoyo',
                'Filamenti cobalto traslucidi che convergono in un unico fulcro',
                'Doorschijnende kobaltblauwe filamenten die samenkomen in één draaipunt'),
            'A modular field of pale platforms linked by graphite paths': _t(
                'Un champ modulaire de plateformes pâles reliées par des chemins graphite',
                'Ein modulares Feld blasser Plattformen, verbunden durch graphitfarbene Pfade',
                'Un campo modular de plataformas pálidas unidas por senderos de grafito',
                'Un campo modulare di piattaforme pallide collegate da percorsi grafite',
                'Een modulair veld van bleke platforms verbonden door grafietpaden'),
        },
    },
}
