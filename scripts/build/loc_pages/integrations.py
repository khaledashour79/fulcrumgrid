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
            'Two-way sync for business partners, items and journal entries — a change on either side lands on the other, with no re-keying. Available across HR Suite, Collection and Command Center.': _t(
                "Synchronisation bidirectionnelle des partenaires, articles et écritures comptables — toute modification d'un côté se répercute de l'autre, sans ressaisie. Disponible dans HR Suite, Collection et Command Center.",
                'Bidirektionale Synchronisation von Geschäftspartnern, Artikeln und Buchungen — eine Änderung auf einer Seite erscheint auf der anderen, ohne erneute Erfassung. Verfügbar in HR Suite, Collection und Command Center.',
                'Sincronización bidireccional de socios de negocio, artículos y asientos — un cambio en un lado aparece en el otro, sin volver a teclear. Disponible en HR Suite, Collection y Command Center.',
                "Sincronizzazione bidirezionale di partner commerciali, articoli e registrazioni contabili — una modifica da un lato compare dall'altro, senza reinserimento. Disponibile in HR Suite, Collection e Command Center.",
                'Tweerichtingssynchronisatie van zakenpartners, artikelen en boekingen — een wijziging aan de ene kant verschijnt aan de andere, zonder opnieuw invoeren. Beschikbaar in HR Suite, Collection en Command Center.'),
            'Post HR Suite payroll as draft journal entries into Odoo, and keep Command Center dashboards reading from the same numbers — a two-way connection, with no re-keying.': _t(
                "Postez la paie de HR Suite sous forme d'écritures comptables provisoires dans Odoo, et gardez les tableaux de bord de Command Center sur les mêmes chiffres — une connexion bidirectionnelle, sans ressaisie.",
                'Buchen Sie die HR-Suite-Gehaltsabrechnung als Buchungsentwürfe in Odoo und halten Sie die Command-Center-Dashboards auf denselben Zahlen — eine bidirektionale Verbindung, ohne erneute Eingabe.',
                'Contabilice la nómina de HR Suite como asientos en borrador en Odoo y mantenga los paneles de Command Center sobre las mismas cifras — una conexión bidireccional, sin volver a teclear.',
                'Registra le buste paga di HR Suite come scritture in bozza in Odoo e mantieni le dashboard di Command Center sugli stessi numeri — una connessione bidirezionale, senza reinserimenti.',
                'Boek de loonadministratie van HR Suite als concept-journaalposten in Odoo en houd de Command Center-dashboards op dezelfde cijfers — een tweerichtingsverbinding, zonder opnieuw typen.'),
            "Command Center streams live Oracle balances into your dashboards, and HR Suite posts payroll journals through Oracle Integration (OIC) and Oracle Fusion (ERP Cloud).": _t(
                "Command Center diffuse les soldes Oracle en direct dans vos tableaux de bord, et HR Suite poste les écritures de paie via Oracle Integration (OIC) et Oracle Fusion (ERP Cloud).",
                'Command Center streamt Live-Oracle-Salden in Ihre Dashboards, und HR Suite bucht Gehaltsabrechnungs-Journale über Oracle Integration (OIC) und Oracle Fusion (ERP Cloud).',
                'Command Center transmite saldos de Oracle en directo a sus paneles, y HR Suite contabiliza los asientos de nómina a través de Oracle Integration (OIC) y Oracle Fusion (ERP Cloud).',
                "Command Center trasmette in tempo reale i saldi Oracle nelle tue dashboard e HR Suite registra le scritture delle buste paga tramite Oracle Integration (OIC) e Oracle Fusion (ERP Cloud).",
                'Command Center streamt live Oracle-saldi naar uw dashboards, en HR Suite boekt loonjournalen via Oracle Integration (OIC) en Oracle Fusion (ERP Cloud).'),
            'Link QuickBooks Online (QBO) to match invoices to payments and reconcile automatically. Your books stay in QuickBooks; the export-and-reimport busywork disappears.': _t(
                "Reliez QuickBooks Online (QBO) pour rapprocher factures et paiements et faire la réconciliation automatiquement. Votre comptabilité reste dans QuickBooks ; la corvée d'export et de réimport disparaît.",
                'Verknüpfen Sie QuickBooks Online (QBO), um Rechnungen und Zahlungen zuzuordnen und automatisch abzustimmen. Ihre Buchhaltung bleibt in QuickBooks; die Mühe von Export und Reimport entfällt.',
                'Enlace QuickBooks Online (QBO) para casar facturas con pagos y conciliar automáticamente. Su contabilidad permanece en QuickBooks; el trabajo de exportar y reimportar desaparece.',
                'Collega QuickBooks Online (QBO) per abbinare fatture e pagamenti e riconciliare automaticamente. La tua contabilità resta in QuickBooks; il lavoro di esportazione e reimportazione sparisce.',
                'Koppel QuickBooks Online (QBO) om facturen aan betalingen te matchen en automatisch af te letteren. Uw boekhouding blijft in QuickBooks; het export-en-herimport-werk verdwijnt.'),
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
            "A clean, versioned REST API with predictable JSON and token auth — read and write any record your team can reach in the app. Fully documented: Collection's REST API on Business and up, and HR Suite's Partner API on Enterprise.": _t(
                "Une API REST claire et versionnée, avec un JSON prévisible et une authentification par jeton — lisez et écrivez tout enregistrement accessible à votre équipe dans l'application. Entièrement documentée : l'API REST de Collection à partir de Business, et l'API Partenaire de HR Suite sur Enterprise.",
                "Eine saubere, versionierte REST-API mit vorhersehbarem JSON und Token-Authentifizierung — lesen und schreiben Sie jeden Datensatz, den Ihr Team in der App erreichen kann. Vollständig dokumentiert: die REST-API von Collection ab Business und die Partner-API von HR Suite auf Enterprise.",
                "Una API REST limpia y versionada, con JSON predecible y autenticación por token — lea y escriba cualquier registro que su equipo pueda alcanzar en la app. Totalmente documentada: la API REST de Collection desde Business, y la API para socios de HR Suite en Enterprise.",
                "Un'API REST pulita e versionata, con JSON prevedibile e autenticazione tramite token — leggi e scrivi qualsiasi record raggiungibile dal tuo team nell'app. Completamente documentata: l'API REST di Collection da Business in su e l'API per partner di HR Suite su Enterprise.",
                "Een nette, geversioneerde REST-API met voorspelbare JSON en tokenauthenticatie — lees en schrijf elk record dat uw team in de app kan bereiken. Volledig gedocumenteerd: de REST-API van Collection vanaf Business en de Partner-API van HR Suite op Enterprise."),
            'Subscribe to the events that matter and FulcrumGrid pushes them to your endpoints the moment they happen — so your own systems react in real time, with no polling and no delay.': _t(
                'Abonnez-vous aux événements qui comptent et FulcrumGrid les envoie à vos points de terminaison dès qu’ils surviennent — pour que vos propres systèmes réagissent en temps réel, sans interrogation ni délai.',
                'Abonnieren Sie die relevanten Ereignisse, und FulcrumGrid sendet sie im selben Moment an Ihre Endpunkte — damit Ihre eigenen Systeme in Echtzeit reagieren, ohne Polling und ohne Verzögerung.',
                'Suscríbase a los eventos que importan y FulcrumGrid los envía a sus endpoints en cuanto ocurren — para que sus sistemas reaccionen en tiempo real, sin sondeo ni retraso.',
                'Iscriviti agli eventi che contano e FulcrumGrid li invia ai tuoi endpoint nel momento in cui accadono — così i tuoi sistemi reagiscono in tempo reale, senza polling e senza ritardi.',
                'Abonneer u op de events die ertoe doen en FulcrumGrid pusht ze naar uw endpoints zodra ze gebeuren — zodat uw eigen systemen in realtime reageren, zonder polling en zonder vertraging.'),
            'A full sandbox that mirrors production, with its own keys and test data — build and validate every integration safely before a single live record is touched.': _t(
                'Un bac à sable complet qui reflète la production, avec ses propres clés et données de test — créez et validez chaque intégration en toute sécurité avant de toucher le moindre enregistrement réel.',
                'Eine vollständige Sandbox als Abbild der Produktion, mit eigenen Schlüsseln und Testdaten — erstellen und prüfen Sie jede Integration sicher, bevor ein einziger Live-Datensatz berührt wird.',
                'Un sandbox completo que refleja producción, con sus propias claves y datos de prueba — cree y valide cada integración con seguridad antes de tocar un solo registro real.',
                'Una sandbox completa che rispecchia la produzione, con chiavi e dati di test propri — crea e valida ogni integrazione in sicurezza prima di toccare un solo record reale.',
                'Een volledige sandbox die productie weerspiegelt, met eigen sleutels en testdata — bouw en valideer elke integratie veilig voordat één live record wordt aangeraakt.'),
            'Scheduled pull': _t('Récupération planifiée', 'Geplanter Abruf', 'Extracción programada', 'Estrazione pianificata', 'Geplande ophaling'),
            'Set a cadence and Command Center pulls balances and records from your ERP on its own — hourly, nightly, however you need — so dashboards stay current without anyone lifting a finger.': _t(
                'Définissez une fréquence et Command Center récupère seul soldes et données de votre ERP — toutes les heures, chaque nuit, comme vous le souhaitez — pour que les tableaux de bord restent à jour sans lever le petit doigt.',
                'Legen Sie einen Takt fest, und Command Center ruft Salden und Daten aus Ihrem ERP von selbst ab — stündlich, nächtlich, wie Sie es brauchen — damit Dashboards aktuell bleiben, ohne dass jemand eingreift.',
                'Defina una cadencia y Command Center extrae por su cuenta saldos y registros de su ERP — cada hora, cada noche, como necesite — para que los paneles sigan al día sin que nadie mueva un dedo.',
                'Imposta una cadenza e Command Center estrae da solo saldi e dati dal tuo ERP — ogni ora, ogni notte, come ti serve — così le dashboard restano aggiornate senza muovere un dito.',
                'Stel een cadans in en Command Center haalt zelf saldi en gegevens uit uw ERP — elk uur, elke nacht, zoals u wilt — zodat dashboards actueel blijven zonder dat iemand iets hoeft te doen.'),

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
            'Single sign-on through the identity provider you already run, so your team signs in once with credentials IT already controls — no extra passwords to manage. Available on HR Suite and Collection (Enterprise).': _t(
                "Authentification unique via le fournisseur d'identité que vous utilisez déjà : votre équipe se connecte une fois avec des identifiants que l'informatique gère déjà — aucun mot de passe supplémentaire à gérer. Disponible sur HR Suite et Collection (Enterprise).",
                'Single Sign-On über den bereits genutzten Identitätsanbieter: Ihr Team meldet sich einmal mit Zugangsdaten an, die die IT bereits verwaltet — keine zusätzlichen Passwörter. Verfügbar für HR Suite und Collection (Enterprise).',
                'Inicio de sesión único mediante el proveedor de identidad que ya usa: su equipo entra una vez con credenciales que TI ya controla — sin contraseñas adicionales que gestionar. Disponible en HR Suite y Collection (Enterprise).',
                "Single sign-on tramite il provider di identità che già usi: il tuo team accede una volta con credenziali che l'IT già gestisce — nessuna password aggiuntiva. Disponibile su HR Suite e Collection (Enterprise).",
                'Eenmalige aanmelding via de identiteitsprovider die u al gebruikt: uw team logt één keer in met inloggegevens die IT al beheert — geen extra wachtwoorden. Beschikbaar op HR Suite en Collection (Enterprise).'),
            "Automated provisioning through SCIM — new hires get the right access the day they start, and leavers lose it the moment they're offboarded, straight from your directory.": _t(
                'Provisionnement automatisé via SCIM — les nouvelles recrues obtiennent le bon accès dès leur premier jour, et les départs le perdent au moment de leur sortie, directement depuis votre annuaire.',
                'Automatisierte Bereitstellung über SCIM — neue Mitarbeitende erhalten am ersten Tag die richtigen Zugriffe, Abgänge verlieren sie im Moment des Offboardings, direkt aus Ihrem Verzeichnis.',
                'Aprovisionamiento automatizado mediante SCIM — las nuevas incorporaciones obtienen el acceso correcto el día que empiezan, y las bajas lo pierden en el momento de su salida, directamente desde su directorio.',
                "Provisioning automatizzato tramite SCIM — i nuovi assunti ottengono l'accesso giusto il giorno in cui iniziano e chi esce lo perde nel momento dell'offboarding, direttamente dalla tua directory.",
                'Geautomatiseerde provisioning via SCIM — nieuwe medewerkers krijgen de juiste toegang op hun eerste dag, en vertrekkers verliezen die op het moment van offboarding, rechtstreeks vanuit uw directory.'),

            # ---- CTA ----
            "04 · Alerts &amp; messaging": _t(
                "04 · Alertes &amp; messagerie", "04 · Benachrichtigungen &amp; Messaging",
                "04 · Alertas &amp; mensajería", "04 · Avvisi &amp; messaggistica", "04 · Meldingen &amp; berichten"),
            "Push the signal where your team already is.": _t(
                "Envoyez le signal là où se trouve déjà votre équipe.",
                "Senden Sie das Signal dorthin, wo Ihr Team schon ist.",
                "Lleve la señal a donde ya está su equipo.",
                "Invia il segnale dove il tuo team è già.",
                "Stuur het signaal naar waar uw team al is."),
            "Send what matters to the channels people already watch — no extra dashboard to check.": _t(
                "Envoyez l'essentiel sur les canaux que vos équipes surveillent déjà — aucun tableau de bord supplémentaire à consulter.",
                "Senden Sie das Wesentliche an die Kanäle, die Ihre Leute ohnehin beobachten — kein zusätzliches Dashboard.",
                "Envíe lo importante a los canales que su gente ya vigila — sin otro panel que consultar.",
                "Invia ciò che conta ai canali che le persone già seguono — nessuna dashboard in più da controllare.",
                "Stuur wat telt naar de kanalen die mensen toch al volgen — geen extra dashboard om te checken."),
            "Slack &amp; Microsoft Teams": _t(
                "Slack &amp; Microsoft Teams", "Slack &amp; Microsoft Teams", "Slack &amp; Microsoft Teams",
                "Slack &amp; Microsoft Teams", "Slack &amp; Microsoft Teams"),
            "Command Center posts a summary of overdue items and key events to a Slack or Teams channel through an incoming webhook — so your team sees what needs attention without opening the app.": _t(
                "Command Center publie un résumé des éléments en retard et des événements clés dans un canal Slack ou Teams via un webhook entrant — pour que votre équipe voie ce qui requiert son attention sans ouvrir l'application.",
                "Command Center postet eine Zusammenfassung überfälliger Posten und wichtiger Ereignisse über einen eingehenden Webhook in einen Slack- oder Teams-Kanal — damit Ihr Team sieht, was Aufmerksamkeit braucht, ohne die App zu öffnen.",
                "Command Center publica un resumen de los elementos vencidos y los eventos clave en un canal de Slack o Teams mediante un webhook entrante — para que su equipo vea lo que requiere atención sin abrir la app.",
                "Command Center pubblica un riepilogo degli elementi scaduti e degli eventi chiave in un canale Slack o Teams tramite un webhook in entrata — così il tuo team vede cosa richiede attenzione senza aprire l'app.",
                "Command Center plaatst een samenvatting van achterstallige items en belangrijke gebeurtenissen in een Slack- of Teams-kanaal via een inkomende webhook — zodat uw team ziet wat aandacht nodig heeft zonder de app te openen."),
            "Multi-channel reminders": _t(
                "Rappels multicanaux", "Mehrkanal-Erinnerungen", "Recordatorios multicanal",
                "Promemoria multicanale", "Multichannel-herinneringen"),
            "Collection reaches each debtor on the channel they actually answer, sent automatically on the reminder schedule you set — so follow-ups go out without anyone chasing by hand.": _t(
                "Collection atteint chaque débiteur sur le canal auquel il répond vraiment, envoyé automatiquement selon le calendrier de relance que vous définissez — pour que les relances partent sans que personne ne relance à la main.",
                "Collection erreicht jeden Schuldner auf dem Kanal, auf dem er tatsächlich antwortet, automatisch gemäß dem von Ihnen festgelegten Erinnerungsplan versendet — damit Nachfassaktionen ausgehen, ohne dass jemand von Hand nachhakt.",
                "Collection llega a cada deudor por el canal al que realmente responde, enviado automáticamente según el calendario de recordatorios que usted define — para que los seguimientos salgan sin que nadie persiga a mano.",
                "Collection raggiunge ogni debitore sul canale a cui risponde davvero, inviato automaticamente secondo il calendario di solleciti che imposti — così i solleciti partono senza che nessuno insegua a mano.",
                "Collection bereikt elke debiteur op het kanaal waarop die echt reageert, automatisch verzonden volgens het herinneringsschema dat u instelt — zodat opvolging uitgaat zonder dat iemand handmatig achter betalingen aan zit."),
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
