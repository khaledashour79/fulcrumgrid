# -*- coding: utf-8 -*-
"""Translations for the Integrations page (/integrations/), new design system.

Keys are EXACT substrings of the committed English integrations/index.html
(inline markup, entities and glyphs preserved). Common chrome (nav, footer,
buttons, tagline) is handled by loc_catalog.COMMON and not repeated here.
Brand/product names (FulcrumGrid, Command Center, Collection, HR Suite) and
integration/technology proper nouns (SAP Business One, Odoo, Oracle,
QuickBooks Online, QBO, REST API v1, Webhooks, Sandbox, SSO, SCIM) stay
English on every locale — the acceptance oracle allowlists them.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/integrations/': {
        'src': 'integrations/index.html',
        't': {
            # ---- Meta ----
            'Integrations — SAP, Odoo, Oracle &amp; QuickBooks | FulcrumGrid': _t(
                'Intégrations — SAP, Odoo, Oracle &amp; QuickBooks | FulcrumGrid',
                'Integrationen — SAP, Odoo, Oracle &amp; QuickBooks | FulcrumGrid',
                'Integraciones — SAP, Odoo, Oracle &amp; QuickBooks | FulcrumGrid',
                'Integrazioni — SAP, Odoo, Oracle &amp; QuickBooks | FulcrumGrid',
                'Integraties — SAP, Odoo, Oracle &amp; QuickBooks | FulcrumGrid'),
            'FulcrumGrid connects to the systems you already run — SAP Business One, Odoo, Oracle and QuickBooks Online — plus a REST API, webhooks and SSO/SCIM to fit your stack.': _t(
                "FulcrumGrid se connecte aux systèmes que vous utilisez déjà — SAP Business One, Odoo, Oracle et QuickBooks Online — avec une API REST, des webhooks et SSO/SCIM pour s'adapter à votre pile.",
                'FulcrumGrid verbindet sich mit den Systemen, die Sie bereits nutzen — SAP Business One, Odoo, Oracle und QuickBooks Online — plus REST-API, Webhooks und SSO/SCIM, passend zu Ihrem Stack.',
                'FulcrumGrid se conecta con los sistemas que ya utiliza — SAP Business One, Odoo, Oracle y QuickBooks Online — además de una API REST, webhooks y SSO/SCIM para encajar en su stack.',
                'FulcrumGrid si collega ai sistemi che già utilizzi — SAP Business One, Odoo, Oracle e QuickBooks Online — più API REST, webhook e SSO/SCIM per adattarsi al tuo stack.',
                'FulcrumGrid verbindt met de systemen die u al gebruikt — SAP Business One, Odoo, Oracle en QuickBooks Online — plus een REST-API, webhooks en SSO/SCIM voor uw stack.'),
            'Connect FulcrumGrid to SAP Business One, Odoo, Oracle and QuickBooks Online, with a REST API, webhooks and SSO/SCIM to fit your stack.': _t(
                "Connectez FulcrumGrid à SAP Business One, Odoo, Oracle et QuickBooks Online, avec une API REST, des webhooks et SSO/SCIM pour s'adapter à votre pile.",
                'Verbinden Sie FulcrumGrid mit SAP Business One, Odoo, Oracle und QuickBooks Online — mit REST-API, Webhooks und SSO/SCIM, passend zu Ihrem Stack.',
                'Conecte FulcrumGrid con SAP Business One, Odoo, Oracle y QuickBooks Online, con una API REST, webhooks y SSO/SCIM para encajar en su stack.',
                'Collega FulcrumGrid a SAP Business One, Odoo, Oracle e QuickBooks Online, con API REST, webhook e SSO/SCIM per adattarsi al tuo stack.',
                'Verbind FulcrumGrid met SAP Business One, Odoo, Oracle en QuickBooks Online, met een REST-API, webhooks en SSO/SCIM voor uw stack.'),

            # ---- Hero ----
            'Integrations': _t('Intégrations', 'Integrationen', 'Integraciones', 'Integrazioni', 'Integraties'),
            'Connects to the systems you already run.': _t(
                'Se connecte aux systèmes que vous utilisez déjà.',
                'Verbindet sich mit den Systemen, die Sie bereits nutzen.',
                'Se conecta con los sistemas que ya utiliza.',
                'Si collega ai sistemi che già utilizzi.',
                'Verbindt met de systemen die u al gebruikt.'),
            'FulcrumGrid works alongside your ERP and accounting stack — SAP Business One, Odoo, Oracle and QuickBooks Online — and gives your developers a REST API, webhooks and SSO/SCIM to wire it into everything else. Keep your books where they are; put your operations on one grid.': _t(
                "FulcrumGrid fonctionne aux côtés de votre pile ERP et comptable — SAP Business One, Odoo, Oracle et QuickBooks Online — et offre à vos développeurs une API REST, des webhooks et SSO/SCIM pour le relier à tout le reste. Gardez votre comptabilité où elle est ; mettez vos opérations sur une seule grille.",
                'FulcrumGrid arbeitet neben Ihrem ERP- und Buchhaltungs-Stack — SAP Business One, Odoo, Oracle und QuickBooks Online — und gibt Ihren Entwicklern eine REST-API, Webhooks und SSO/SCIM, um es mit allem anderen zu verbinden. Lassen Sie Ihre Buchhaltung, wo sie ist; bringen Sie Ihren Betrieb auf ein Grid.',
                'FulcrumGrid funciona junto a su stack de ERP y contabilidad — SAP Business One, Odoo, Oracle y QuickBooks Online — y ofrece a sus desarrolladores una API REST, webhooks y SSO/SCIM para conectarlo con todo lo demás. Mantenga su contabilidad donde está; ponga sus operaciones en una sola cuadrícula.',
                "FulcrumGrid lavora accanto al tuo stack ERP e contabile — SAP Business One, Odoo, Oracle e QuickBooks Online — e offre ai tuoi sviluppatori un'API REST, webhook e SSO/SCIM per collegarlo a tutto il resto. Tieni la contabilità dov'è; porta le tue operazioni su un'unica griglia.",
                'FulcrumGrid werkt naast uw ERP- en boekhoudstack — SAP Business One, Odoo, Oracle en QuickBooks Online — en geeft uw ontwikkelaars een REST-API, webhooks en SSO/SCIM om het aan alles te koppelen. Houd uw boekhouding waar die is; zet uw operatie op één grid.'),
            'Talk to us about your stack': _t(
                'Parlez-nous de votre pile', 'Sprechen Sie mit uns über Ihren Stack',
                'Cuéntenos sobre su stack', 'Parlaci del tuo stack', 'Vertel ons over uw stack'),
            'Explore the apps': _t('Découvrir les applications', 'Apps entdecken', 'Explorar las apps', 'Esplora le app', 'Ontdek de apps'),

            # ---- 01 · ERP & accounting ----
            'ERP &amp; accounting': _t(
                'ERP &amp; comptabilité', 'ERP &amp; Buchhaltung', 'ERP &amp; contabilidad',
                'ERP &amp; contabilità', 'ERP &amp; boekhouding'),
            'Connect your ERP and accounting.': _t(
                'Connectez votre ERP et votre comptabilité.',
                'Verbinden Sie Ihr ERP und Ihre Buchhaltung.',
                'Conecte su ERP y su contabilidad.',
                'Collega il tuo ERP e la tua contabilità.',
                'Verbind uw ERP en boekhouding.'),
            'Sync master data, post transactions, and pull balances on a schedule — without double entry.': _t(
                'Synchronisez les données de référence, enregistrez les transactions et récupérez les soldes selon un calendrier — sans double saisie.',
                'Synchronisieren Sie Stammdaten, buchen Sie Transaktionen und rufen Sie Salden nach Zeitplan ab — ohne Doppelerfassung.',
                'Sincronice datos maestros, registre transacciones y extraiga saldos según un calendario — sin doble entrada.',
                'Sincronizza i dati anagrafici, registra le transazioni ed estrai i saldi secondo una pianificazione — senza doppia immissione.',
                'Synchroniseer stamgegevens, boek transacties en haal saldi op volgens een schema — zonder dubbele invoer.'),
            'Sync customers, vendors, items and journals with SAP Business One. Available across HR Suite, Collection and Command Center.': _t(
                'Synchronisez clients, fournisseurs, articles et écritures avec SAP Business One. Disponible dans HR Suite, Collection et Command Center.',
                'Synchronisieren Sie Kunden, Lieferanten, Artikel und Buchungen mit SAP Business One. Verfügbar in HR Suite, Collection und Command Center.',
                'Sincronice clientes, proveedores, artículos y asientos con SAP Business One. Disponible en HR Suite, Collection y Command Center.',
                'Sincronizza clienti, fornitori, articoli e registrazioni con SAP Business One. Disponibile in HR Suite, Collection e Command Center.',
                'Synchroniseer klanten, leveranciers, artikelen en boekingen met SAP Business One. Beschikbaar in HR Suite, Collection en Command Center.'),
            'Two-way connector for Odoo — keep contacts, invoices and payments aligned between Odoo and the grid.': _t(
                'Connecteur bidirectionnel pour Odoo — gardez contacts, factures et paiements alignés entre Odoo et la grille.',
                'Bidirektionaler Konnektor für Odoo — halten Sie Kontakte, Rechnungen und Zahlungen zwischen Odoo und dem Grid im Einklang.',
                'Conector bidireccional para Odoo — mantenga contactos, facturas y pagos alineados entre Odoo y la cuadrícula.',
                'Connettore bidirezionale per Odoo — mantieni contatti, fatture e pagamenti allineati tra Odoo e la griglia.',
                'Tweerichtingsconnector voor Odoo — houd contacten, facturen en betalingen op één lijn tussen Odoo en het grid.'),
            'Connect Oracle financials to feed live balances and receivables into Command Center dashboards and alerts.': _t(
                'Connectez Oracle Financials pour alimenter les tableaux de bord et alertes de Command Center en soldes et créances en direct.',
                'Verbinden Sie Oracle Financials, um Live-Salden und Forderungen in Command-Center-Dashboards und -Warnungen einzuspeisen.',
                'Conecte Oracle Financials para alimentar los paneles y alertas de Command Center con saldos y cobros en directo.',
                'Collega Oracle Financials per alimentare dashboard e avvisi di Command Center con saldi e crediti in tempo reale.',
                'Verbind Oracle Financials om live saldi en vorderingen in Command Center-dashboards en -meldingen te voeden.'),
            'Link QuickBooks Online (QBO) to reconcile invoices and payments automatically — no more exporting spreadsheets.': _t(
                'Reliez QuickBooks Online (QBO) pour rapprocher automatiquement factures et paiements — fini les exports de tableurs.',
                'Verknüpfen Sie QuickBooks Online (QBO), um Rechnungen und Zahlungen automatisch abzustimmen — kein Export von Tabellen mehr.',
                'Enlace QuickBooks Online (QBO) para conciliar facturas y pagos automáticamente — se acabó exportar hojas de cálculo.',
                'Collega QuickBooks Online (QBO) per riconciliare fatture e pagamenti automaticamente — niente più esportazioni di fogli di calcolo.',
                'Koppel QuickBooks Online (QBO) om facturen en betalingen automatisch af te letteren — geen spreadsheets meer exporteren.'),
            'Command Center includes one ERP connection on Growth, and unlimited connections with a scheduled pull on Enterprise.': _t(
                'Command Center inclut une connexion ERP sur Growth, et des connexions illimitées avec récupération planifiée sur Enterprise.',
                'Command Center enthält eine ERP-Verbindung bei Growth und unbegrenzte Verbindungen mit geplantem Abruf bei Enterprise.',
                'Command Center incluye una conexión ERP en Growth y conexiones ilimitadas con extracción programada en Enterprise.',
                'Command Center include una connessione ERP su Growth e connessioni illimitate con estrazione pianificata su Enterprise.',
                'Command Center bevat één ERP-verbinding op Growth en onbeperkte verbindingen met geplande ophaling op Enterprise.'),
            'See Command Center integrations →': _t(
                'Voir les intégrations de Command Center →', 'Command-Center-Integrationen ansehen →',
                'Ver las integraciones de Command Center →', 'Vedi le integrazioni di Command Center →',
                'Command Center-integraties bekijken →'),

            # ---- 02 · Build on the API ----
            'Build on the API': _t("Construire sur l'API", 'Auf der API aufbauen', 'Construir sobre la API', "Sviluppare sull'API", 'Bouwen op de API'),
            'Wire it into everything else.': _t(
                'Reliez-le à tout le reste.', 'Verbinden Sie es mit allem anderen.',
                'Conéctelo con todo lo demás.', 'Collegalo a tutto il resto.', 'Koppel het aan al het andere.'),
            'Everything you can do in the apps, you can do through the API — with a sandbox to build against safely.': _t(
                "Tout ce que vous faites dans les applications, vous pouvez le faire via l'API — avec un bac à sable pour développer en toute sécurité.",
                'Alles, was Sie in den Apps tun können, können Sie über die API tun — mit einer Sandbox für sicheres Entwickeln.',
                'Todo lo que puede hacer en las apps, lo puede hacer a través de la API — con un sandbox para desarrollar con seguridad.',
                "Tutto ciò che puoi fare nelle app puoi farlo tramite l'API — con una sandbox per sviluppare in sicurezza.",
                'Alles wat u in de apps kunt doen, kunt u via de API doen — met een sandbox om veilig tegen te bouwen.'),
            'A clean, documented REST API to read and write your data. Available on Collection Business and up.': _t(
                'Une API REST claire et documentée pour lire et écrire vos données. Disponible sur Collection Société et plus.',
                'Eine saubere, dokumentierte REST-API zum Lesen und Schreiben Ihrer Daten. Verfügbar ab Collection Unternehmen.',
                'Una API REST clara y documentada para leer y escribir sus datos. Disponible en Collection Negocio y superior.',
                'Un’API REST chiara e documentata per leggere e scrivere i tuoi dati. Disponibile su Collection Azienda e oltre.',
                'Een heldere, gedocumenteerde REST-API om uw data te lezen en te schrijven. Beschikbaar op Collection Bedrijf en hoger.'),
            'Subscribe to events and push updates into your own systems in real time — no polling required.': _t(
                'Abonnez-vous aux événements et poussez les mises à jour dans vos propres systèmes en temps réel — sans interrogation.',
                'Abonnieren Sie Ereignisse und übertragen Sie Updates in Echtzeit in Ihre eigenen Systeme — ohne Polling.',
                'Suscríbase a eventos y envíe actualizaciones a sus propios sistemas en tiempo real — sin sondeo.',
                'Iscriviti agli eventi e invia gli aggiornamenti ai tuoi sistemi in tempo reale — senza polling.',
                'Abonneer u op events en push updates in realtime naar uw eigen systemen — geen polling nodig.'),
            'A full sandbox environment to build and test integrations before you touch production data.': _t(
                'Un environnement bac à sable complet pour créer et tester des intégrations avant de toucher aux données de production.',
                'Eine vollständige Sandbox-Umgebung, um Integrationen zu erstellen und zu testen, bevor Sie Produktionsdaten anfassen.',
                'Un entorno sandbox completo para crear y probar integraciones antes de tocar los datos de producción.',
                'Un ambiente sandbox completo per creare e testare integrazioni prima di toccare i dati di produzione.',
                'Een volledige sandbox-omgeving om integraties te bouwen en te testen voordat u productiedata aanraakt.'),
            'Scheduled pull': _t('Récupération planifiée', 'Geplanter Abruf', 'Extracción programada', 'Estrazione pianificata', 'Geplande ophaling'),
            'Let Command Center pull balances and records from your ERP on a schedule, so dashboards stay current on their own.': _t(
                'Laissez Command Center récupérer soldes et données de votre ERP selon un calendrier, pour que les tableaux de bord restent à jour tout seuls.',
                'Lassen Sie Command Center Salden und Daten aus Ihrem ERP nach Zeitplan abrufen, damit Dashboards von selbst aktuell bleiben.',
                'Deje que Command Center extraiga saldos y registros de su ERP según un calendario, para que los paneles se mantengan al día solos.',
                'Lascia che Command Center estragga saldi e dati dal tuo ERP secondo una pianificazione, così le dashboard restano aggiornate da sole.',
                'Laat Command Center volgens een schema saldi en gegevens uit uw ERP ophalen, zodat dashboards vanzelf actueel blijven.'),

            # ---- 03 · Identity & access ----
            'Identity &amp; access': _t(
                'Identité &amp; accès', 'Identität &amp; Zugriff', 'Identidad &amp; acceso',
                'Identità &amp; accesso', 'Identiteit &amp; toegang'),
            'Single sign-on and provisioning.': _t(
                'Authentification unique et provisionnement.',
                'Single Sign-On und Provisionierung.',
                'Inicio de sesión único y aprovisionamiento.',
                'Single sign-on e provisioning.',
                'Eenmalige aanmelding en provisioning.'),
            'Bring your own identity provider and manage people the way you already do.': _t(
                "Apportez votre propre fournisseur d'identité et gérez les personnes comme vous le faites déjà.",
                'Bringen Sie Ihren eigenen Identitätsanbieter mit und verwalten Sie Personen so, wie Sie es bereits tun.',
                'Traiga su propio proveedor de identidad y gestione a las personas como ya lo hace.',
                'Porta il tuo provider di identità e gestisci le persone come già fai.',
                'Neem uw eigen identiteitsprovider mee en beheer mensen zoals u dat al doet.'),
            'Single sign-on so your team signs in with the identity provider you already use. Available on HR Suite Enterprise.': _t(
                "Authentification unique pour que votre équipe se connecte avec le fournisseur d'identité que vous utilisez déjà. Disponible sur HR Suite Enterprise.",
                'Single Sign-On, damit sich Ihr Team mit dem bereits genutzten Identitätsanbieter anmeldet. Verfügbar bei HR Suite Enterprise.',
                'Inicio de sesión único para que su equipo entre con el proveedor de identidad que ya usa. Disponible en HR Suite Enterprise.',
                "Single sign-on così il tuo team accede con il provider di identità che già usi. Disponibile su HR Suite Enterprise.",
                'Eenmalige aanmelding zodat uw team inlogt met de identiteitsprovider die u al gebruikt. Beschikbaar op HR Suite Enterprise.'),
            'Automated user provisioning and de-provisioning through SCIM — joiners and leavers stay in sync.': _t(
                'Provisionnement et déprovisionnement automatisés des utilisateurs via SCIM — arrivées et départs restent synchronisés.',
                'Automatisiertes Bereitstellen und Entziehen von Benutzern über SCIM — Zu- und Abgänge bleiben synchron.',
                'Aprovisionamiento y desaprovisionamiento automatizado de usuarios mediante SCIM — altas y bajas se mantienen sincronizadas.',
                'Provisioning e de-provisioning automatizzati degli utenti tramite SCIM — ingressi e uscite restano sincronizzati.',
                'Geautomatiseerd gebruikers in- en uitfaseren via SCIM — instromers en vertrekkers blijven synchroon.'),

            # ---- CTA ----
            "Don't see your system?": _t(
                'Vous ne voyez pas votre système ?', 'Ihr System nicht dabei?',
                '¿No ve su sistema?', 'Non trovi il tuo sistema?', 'Ziet u uw systeem niet?'),
            "Tell us what you run and we'll show you how FulcrumGrid fits your stack.": _t(
                "Dites-nous ce que vous utilisez et nous vous montrerons comment FulcrumGrid s'intègre à votre pile.",
                'Sagen Sie uns, was Sie einsetzen, und wir zeigen Ihnen, wie FulcrumGrid in Ihren Stack passt.',
                'Díganos qué utiliza y le mostraremos cómo FulcrumGrid encaja en su stack.',
                'Dicci cosa usi e ti mostreremo come FulcrumGrid si adatta al tuo stack.',
                'Vertel ons wat u gebruikt en we laten zien hoe FulcrumGrid in uw stack past.'),
            'Talk to us': _t('Contactez-nous', 'Sprechen Sie mit uns', 'Hable con nosotros', 'Parla con noi', 'Praat met ons'),
            'See pricing': _t('Voir les tarifs', 'Preise ansehen', 'Ver precios', 'Vedi i prezzi', 'Bekijk prijzen'),
        },
    },
}
