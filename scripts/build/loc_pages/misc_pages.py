# -*- coding: utf-8 -*-
"""Per-page translation catalogs for the miscellaneous hand-authored pages:
the Privacy & Cookies notice, the FulcrumGrid vs. spreadsheets comparison, and
the 404 page.

Conventions (see loc_catalog.py):
  * Brand / product names stay English: FulcrumGrid, Command Center, Collection,
    HR Suite; "Blog", "FAQ" and proper nouns (GDPR, Google, Excel, Google
    Sheets) are left untranslated. Company name "Avenlor Consulting" and email
    addresses are kept verbatim.
  * Keys are the EXACT English text as it appears in the EN source HTML,
    including entities (&amp;), curly quotes (“ ”), curly apostrophes (’),
    em/en dashes (— –) and inline tags (<strong>, <span>, <a>).
  * COMMON strings (nav/footer/buttons and the standalone word "Privacy") are
    handled by loc_catalog.COMMON and are deliberately NOT repeated here. In
    particular the Privacy page <title>/<h1>/og:title read "Privacy & Cookies";
    COMMON translates the word "Privacy" (applied before this catalog), so those
    headings localize correctly without a per-page key — adding one would never
    match after COMMON has run.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# Reused across pages: the shared og:image:alt (identical to the homepage's).
_OG_ALT = _t(
    'FulcrumGrid — des applications métier sur mesure pour chaque opération',
    'FulcrumGrid — zweckgebaute Business-Apps für jeden Betrieb',
    'FulcrumGrid — aplicaciones de negocio a medida para cada operación',
    'FulcrumGrid — applicazioni aziendali su misura per ogni operazione',
    'FulcrumGrid — doelgerichte bedrijfsapps voor elke operatie')


PAGE = {
    # ==================================================================
    '/privacy/': {
        'src': 'privacy/index.html',
        't': {
            # ---- Meta (title/h1/og:title now read "Privacy & Cookies") ----
            'Privacy &amp; Cookies — FulcrumGrid': _t(
                'Confidentialité et cookies — FulcrumGrid',
                'Datenschutz und Cookies — FulcrumGrid',
                'Privacidad y cookies — FulcrumGrid',
                'Privacy e cookie — FulcrumGrid',
                'Privacy en cookies — FulcrumGrid'),
            'Privacy &amp; Cookies': _t(
                'Confidentialité et cookies',
                'Datenschutz und Cookies',
                'Privacidad y cookies',
                'Privacy e cookie',
                'Privacy en cookies'),
            'How FulcrumGrid uses cookies and analytics, what we collect, and the choices available to you.': _t(
                "Comment FulcrumGrid utilise les cookies et l'analyse, ce que nous collectons et les choix qui s'offrent à vous.",
                'Wie FulcrumGrid Cookies und Analyse verwendet, was wir erfassen und welche Wahlmöglichkeiten Sie haben.',
                'Cómo utiliza FulcrumGrid las cookies y la analítica, qué recopilamos y las opciones a su disposición.',
                "Come FulcrumGrid utilizza i cookie e l'analisi, cosa raccogliamo e le scelte a tua disposizione.",
                'Hoe FulcrumGrid cookies en analyse gebruikt, wat we verzamelen en welke keuzes u hebt.'),
            'How FulcrumGrid uses cookies and analytics, and the choices available to you.': _t(
                "Comment FulcrumGrid utilise les cookies et l'analyse, et les choix qui s'offrent à vous.",
                'Wie FulcrumGrid Cookies und Analyse verwendet und welche Wahlmöglichkeiten Sie haben.',
                'Cómo utiliza FulcrumGrid las cookies y la analítica, y las opciones a su disposición.',
                "Come FulcrumGrid utilizza i cookie e l'analisi e le scelte a tua disposizione.",
                'Hoe FulcrumGrid cookies en analyse gebruikt en welke keuzes u hebt.'),
            # ---- Header of the article ----
            'Legal': _t('Juridique', 'Rechtliches', 'Legal', 'Legale', 'Juridisch'),
            # Product name — stays English; keeps the checker from flagging the bare link node.
            'Google Analytics': _t('Google Analytics', 'Google Analytics', 'Google Analytics', 'Google Analytics', 'Google Analytics'),
            'Last updated: August 2026': _t(
                'Dernière mise à jour : août 2026',
                'Zuletzt aktualisiert: August 2026',
                'Última actualización: agosto de 2026',
                'Ultimo aggiornamento: agosto 2026',
                'Laatst bijgewerkt: augustus 2026'),
            # ---- Body ----
            'This notice explains how FulcrumGrid ("FulcrumGrid", "we", "us") handles information on this website, the cookies we use, and the choices available to you. It applies to <a href="https://fulcrumgrid.com">fulcrumgrid.com</a> and its subpages.': _t(
                'Cet avis explique comment FulcrumGrid (« FulcrumGrid », « nous ») traite les informations sur ce site web, les cookies que nous utilisons et les choix qui s\'offrent à vous. Il s\'applique à <a href="https://fulcrumgrid.com">fulcrumgrid.com</a> et à ses sous-pages.',
                'Dieser Hinweis erklärt, wie FulcrumGrid ("FulcrumGrid", "wir", "uns") mit Informationen auf dieser Website umgeht, welche Cookies wir verwenden und welche Wahlmöglichkeiten Sie haben. Er gilt für <a href="https://fulcrumgrid.com">fulcrumgrid.com</a> und dessen Unterseiten.',
                'Este aviso explica cómo FulcrumGrid ("FulcrumGrid", "nosotros") gestiona la información en este sitio web, las cookies que utilizamos y las opciones a su disposición. Se aplica a <a href="https://fulcrumgrid.com">fulcrumgrid.com</a> y sus subpáginas.',
                'Questa informativa spiega come FulcrumGrid ("FulcrumGrid", "noi") gestisce le informazioni su questo sito web, i cookie che utilizziamo e le scelte a tua disposizione. Si applica a <a href="https://fulcrumgrid.com">fulcrumgrid.com</a> e alle sue sottopagine.',
                'Deze kennisgeving legt uit hoe FulcrumGrid ("FulcrumGrid", "wij", "ons") omgaat met informatie op deze website, welke cookies we gebruiken en welke keuzes u hebt. Ze geldt voor <a href="https://fulcrumgrid.com">fulcrumgrid.com</a> en de subpagina\'s.'),
            'Information we collect': _t(
                'Les informations que nous collectons', 'Informationen, die wir erfassen',
                'Información que recopilamos', 'Informazioni che raccogliamo',
                'Informatie die we verzamelen'),
            'This is a marketing website, not an app login. We do not require you to create an account here, and we do not knowingly collect sensitive personal data. Two things are worth explaining:': _t(
                "Il s'agit d'un site web marketing, non d'un espace de connexion applicatif. Nous ne vous demandons pas de créer un compte ici et nous ne collectons pas sciemment de données personnelles sensibles. Deux points méritent d'être expliqués :",
                'Dies ist eine Marketing-Website, kein App-Login. Wir verlangen hier nicht, dass Sie ein Konto erstellen, und wir erheben wissentlich keine sensiblen personenbezogenen Daten. Zwei Dinge sind erklärenswert:',
                'Este es un sitio web de marketing, no un acceso a una aplicación. No le exigimos crear una cuenta aquí y no recopilamos deliberadamente datos personales sensibles. Merece la pena explicar dos cosas:',
                "Questo è un sito web di marketing, non l'accesso a un'app. Non ti chiediamo di creare un account qui e non raccogliamo consapevolmente dati personali sensibili. Due aspetti meritano una spiegazione:",
                'Dit is een marketingwebsite, geen app-login. We vragen u hier geen account aan te maken en we verzamelen niet bewust gevoelige persoonsgegevens. Twee zaken zijn het uitleggen waard:'),
            '<strong>Analytics data</strong> — if you consent, we use Google Analytics to understand how the site is used (pages viewed, approximate location, device and browser type, and how visitors arrive). This helps us improve the site. It is collected in aggregate and is not used to identify you personally.': _t(
                "<strong>Données d'analyse</strong> — si vous y consentez, nous utilisons Google Analytics pour comprendre comment le site est utilisé (pages consultées, localisation approximative, type d'appareil et de navigateur, et comment les visiteurs arrivent). Cela nous aide à améliorer le site. Ces données sont collectées de manière agrégée et ne servent pas à vous identifier personnellement.",
                '<strong>Analysedaten</strong> — wenn Sie einwilligen, nutzen wir Google Analytics, um zu verstehen, wie die Website genutzt wird (aufgerufene Seiten, ungefährer Standort, Geräte- und Browsertyp sowie wie Besucher ankommen). Das hilft uns, die Website zu verbessern. Diese Daten werden aggregiert erfasst und nicht dazu verwendet, Sie persönlich zu identifizieren.',
                '<strong>Datos de analítica</strong> — si da su consentimiento, utilizamos Google Analytics para entender cómo se usa el sitio (páginas vistas, ubicación aproximada, tipo de dispositivo y navegador, y cómo llegan los visitantes). Esto nos ayuda a mejorar el sitio. Se recopilan de forma agregada y no se utilizan para identificarle personalmente.',
                "<strong>Dati analitici</strong> — se dai il consenso, utilizziamo Google Analytics per capire come viene usato il sito (pagine visualizzate, posizione approssimativa, tipo di dispositivo e browser e come arrivano i visitatori). Questo ci aiuta a migliorare il sito. Sono raccolti in forma aggregata e non vengono usati per identificarti personalmente.",
                '<strong>Analysegegevens</strong> — als u toestemming geeft, gebruiken we Google Analytics om te begrijpen hoe de site wordt gebruikt (bekeken pagina\'s, locatie bij benadering, apparaat- en browsertype, en hoe bezoekers binnenkomen). Dit helpt ons de site te verbeteren. Ze worden geaggregeerd verzameld en niet gebruikt om u persoonlijk te identificeren.'),
            '<strong>The demo request form</strong> — if you submit the form or email us, the name and email you provide reach us so we can respond to your request. We use them only for that purpose.': _t(
                "<strong>Le formulaire de demande de démo</strong> — si vous soumettez le formulaire ou nous écrivez, le nom et l'e-mail que vous fournissez nous parviennent afin que nous puissions répondre à votre demande. Nous ne les utilisons qu'à cette fin.",
                '<strong>Das Demo-Anfrageformular</strong> — wenn Sie das Formular absenden oder uns schreiben, erreichen uns der von Ihnen angegebene Name und die E-Mail-Adresse, damit wir auf Ihre Anfrage antworten können. Wir verwenden sie ausschließlich zu diesem Zweck.',
                '<strong>El formulario de solicitud de demo</strong> — si envía el formulario o nos escribe, el nombre y el correo que facilita nos llegan para que podamos responder a su solicitud. Los usamos únicamente con ese fin.',
                "<strong>Il modulo di richiesta demo</strong> — se invii il modulo o ci scrivi, il nome e l'e-mail che fornisci ci raggiungono così da poter rispondere alla tua richiesta. Li utilizziamo solo a tale scopo.",
                '<strong>Het aanvraagformulier voor een demo</strong> — als u het formulier verstuurt of ons mailt, bereiken de naam en het e-mailadres die u opgeeft ons zodat we op uw verzoek kunnen reageren. We gebruiken ze uitsluitend daarvoor.'),
            'Cookies and analytics': _t(
                'Cookies et analyse', 'Cookies und Analyse', 'Cookies y analítica',
                'Cookie e analisi', 'Cookies en analyse'),
            'Cookies are small files a website stores in your browser. We use them for one purpose only: <strong>analytics</strong>. We do not use advertising cookies, and we do not sell data.': _t(
                "Les cookies sont de petits fichiers qu'un site web enregistre dans votre navigateur. Nous ne les utilisons que dans un seul but : <strong>l'analyse</strong>. Nous n'utilisons pas de cookies publicitaires et nous ne vendons pas de données.",
                'Cookies sind kleine Dateien, die eine Website in Ihrem Browser speichert. Wir verwenden sie zu einem einzigen Zweck: <strong>Analyse</strong>. Wir setzen keine Werbe-Cookies ein und verkaufen keine Daten.',
                'Las cookies son pequeños archivos que un sitio web guarda en su navegador. Las usamos con un único fin: <strong>la analítica</strong>. No usamos cookies publicitarias y no vendemos datos.',
                "I cookie sono piccoli file che un sito web memorizza nel tuo browser. Li utilizziamo per un unico scopo: <strong>l'analisi</strong>. Non usiamo cookie pubblicitari e non vendiamo dati.",
                'Cookies zijn kleine bestanden die een website in uw browser opslaat. We gebruiken ze voor één doel: <strong>analyse</strong>. We gebruiken geen advertentiecookies en we verkopen geen gegevens.'),
            'Analytics stays switched <strong>off until you accept</strong>. When you first visit, a banner asks for your choice, and we apply Google Consent Mode so that no analytics cookies are set unless you agree. If you accept, Google Analytics (provided by Google) sets cookies to measure site usage. If you decline, those cookies are not set.': _t(
                "L'analyse reste <strong>désactivée jusqu'à ce que vous acceptiez</strong>. Lors de votre première visite, une bannière vous demande votre choix, et nous appliquons le mode Consentement de Google afin qu'aucun cookie d'analyse ne soit déposé sans votre accord. Si vous acceptez, Google Analytics (fourni par Google) dépose des cookies pour mesurer l'utilisation du site. Si vous refusez, ces cookies ne sont pas déposés.",
                'Die Analyse bleibt <strong>ausgeschaltet, bis Sie zustimmen</strong>. Bei Ihrem ersten Besuch fragt ein Banner nach Ihrer Wahl, und wir wenden den Google-Consent-Mode an, sodass ohne Ihre Zustimmung keine Analyse-Cookies gesetzt werden. Wenn Sie zustimmen, setzt Google Analytics (bereitgestellt von Google) Cookies, um die Websitenutzung zu messen. Wenn Sie ablehnen, werden diese Cookies nicht gesetzt.',
                'La analítica permanece <strong>desactivada hasta que la acepte</strong>. En su primera visita, un aviso le pide su elección y aplicamos el Modo de Consentimiento de Google para que no se instalen cookies de analítica sin su acuerdo. Si acepta, Google Analytics (proporcionado por Google) instala cookies para medir el uso del sitio. Si rechaza, esas cookies no se instalan.',
                "L'analisi resta <strong>disattivata finché non dai il consenso</strong>. Alla prima visita, un banner ti chiede la tua scelta e applichiamo la modalità di consenso di Google in modo che nessun cookie analitico venga impostato senza il tuo accordo. Se accetti, Google Analytics (fornito da Google) imposta cookie per misurare l'uso del sito. Se rifiuti, quei cookie non vengono impostati.",
                'Analyse blijft <strong>uitgeschakeld totdat u accepteert</strong>. Bij uw eerste bezoek vraagt een banner om uw keuze en passen we de Google Consent Mode toe, zodat er geen analysecookies worden geplaatst zonder uw akkoord. Als u accepteert, plaatst Google Analytics (geleverd door Google) cookies om het sitegebruik te meten. Als u weigert, worden die cookies niet geplaatst.'),
            'Third parties': _t('Tiers', 'Dritte', 'Terceros', 'Terze parti', 'Derden'),
            "The only third-party service that may process data through this site is <strong>Google Analytics</strong>, and only after you consent. Google acts as our analytics provider; its handling of data is governed by Google's own privacy terms. We do not share your information with any other third party for their own marketing.": _t(
                "Le seul service tiers susceptible de traiter des données via ce site est <strong>Google Analytics</strong>, et uniquement après votre consentement. Google agit comme notre prestataire d'analyse ; son traitement des données est régi par les propres conditions de confidentialité de Google. Nous ne partageons vos informations avec aucun autre tiers à des fins de marketing propres.",
                'Der einzige Drittanbieterdienst, der über diese Website Daten verarbeiten kann, ist <strong>Google Analytics</strong>, und nur nach Ihrer Einwilligung. Google fungiert als unser Analyseanbieter; der Umgang mit den Daten unterliegt den eigenen Datenschutzbestimmungen von Google. Wir geben Ihre Informationen an keinen anderen Dritten für dessen eigenes Marketing weiter.',
                'El único servicio de terceros que puede tratar datos a través de este sitio es <strong>Google Analytics</strong>, y solo después de su consentimiento. Google actúa como nuestro proveedor de analítica; su tratamiento de los datos se rige por las propias condiciones de privacidad de Google. No compartimos su información con ningún otro tercero para su propio marketing.',
                "L'unico servizio di terze parti che può trattare dati attraverso questo sito è <strong>Google Analytics</strong>, e solo dopo il tuo consenso. Google agisce come nostro fornitore di analisi; il suo trattamento dei dati è disciplinato dalle condizioni di privacy proprie di Google. Non condividiamo le tue informazioni con nessun altro terzo per il proprio marketing.",
                'De enige externe dienst die via deze site gegevens kan verwerken is <strong>Google Analytics</strong>, en alleen nadat u toestemming hebt gegeven. Google treedt op als onze analyseleverancier; de verwerking van de gegevens valt onder de eigen privacyvoorwaarden van Google. We delen uw informatie met geen enkele andere derde voor diens eigen marketing.'),
            'Your choices': _t('Vos choix', 'Ihre Wahlmöglichkeiten', 'Sus opciones', 'Le tue scelte', 'Uw keuzes'),
            '<strong>Accept or decline</strong> analytics using the buttons below — your choice is remembered on this device and can be changed here at any time.': _t(
                "<strong>Acceptez ou refusez</strong> l'analyse à l'aide des boutons ci-dessous — votre choix est mémorisé sur cet appareil et peut être modifié ici à tout moment.",
                '<strong>Akzeptieren oder ablehnen</strong> Sie die Analyse über die Schaltflächen unten — Ihre Wahl wird auf diesem Gerät gespeichert und kann hier jederzeit geändert werden.',
                '<strong>Acepte o rechace</strong> la analítica con los botones de abajo — su elección se recuerda en este dispositivo y puede cambiarse aquí en cualquier momento.',
                "<strong>Accetta o rifiuta</strong> l'analisi tramite i pulsanti qui sotto — la tua scelta viene memorizzata su questo dispositivo e può essere modificata qui in qualsiasi momento.",
                '<strong>Accepteer of weiger</strong> analyse met de knoppen hieronder — uw keuze wordt op dit apparaat onthouden en kan hier op elk moment worden gewijzigd.'),
            "<strong>Browser settings</strong> — you can also block or delete cookies through your browser's settings. Doing so will not affect your ability to read the site.": _t(
                "<strong>Réglages du navigateur</strong> — vous pouvez aussi bloquer ou supprimer les cookies via les réglages de votre navigateur. Cela n'affectera pas votre capacité à lire le site.",
                '<strong>Browsereinstellungen</strong> — Sie können Cookies auch über die Einstellungen Ihres Browsers blockieren oder löschen. Das beeinträchtigt nicht Ihre Möglichkeit, die Website zu lesen.',
                '<strong>Ajustes del navegador</strong> — también puede bloquear o eliminar cookies desde los ajustes de su navegador. Hacerlo no afectará a su capacidad para leer el sitio.',
                "<strong>Impostazioni del browser</strong> — puoi anche bloccare o eliminare i cookie dalle impostazioni del tuo browser. Farlo non pregiudicherà la tua capacità di leggere il sito.",
                '<strong>Browserinstellingen</strong> — u kunt cookies ook blokkeren of verwijderen via de instellingen van uw browser. Dat heeft geen invloed op uw mogelijkheid om de site te lezen.'),
            'Accept analytics': _t("Accepter l'analyse", 'Analyse akzeptieren', 'Aceptar analítica', "Accetta l'analisi", 'Analyse accepteren'),
            'Decline analytics': _t("Refuser l'analyse", 'Analyse ablehnen', 'Rechazar analítica', "Rifiuta l'analisi", 'Analyse weigeren'),
            'Data retention &amp; security': _t(
                'Conservation des données &amp; sécurité', 'Datenspeicherung &amp; Sicherheit',
                'Conservación de datos &amp; seguridad', 'Conservazione dei dati &amp; sicurezza',
                'Gegevensbewaring &amp; beveiliging'),
            'Aggregate analytics data is retained by our analytics provider for a limited period and then deleted or anonymised. Demo-request details are kept only as long as needed to respond and follow up.': _t(
                "Les données d'analyse agrégées sont conservées par notre prestataire d'analyse pendant une période limitée, puis supprimées ou anonymisées. Les détails des demandes de démo ne sont conservés que le temps nécessaire pour répondre et assurer le suivi.",
                'Aggregierte Analysedaten werden von unserem Analyseanbieter für einen begrenzten Zeitraum gespeichert und anschließend gelöscht oder anonymisiert. Angaben aus Demo-Anfragen werden nur so lange aufbewahrt, wie es für die Antwort und Nachverfolgung erforderlich ist.',
                'Los datos de analítica agregados los conserva nuestro proveedor de analítica durante un periodo limitado y luego se eliminan o se anonimizan. Los detalles de las solicitudes de demo se conservan solo el tiempo necesario para responder y hacer seguimiento.',
                'I dati analitici aggregati sono conservati dal nostro fornitore di analisi per un periodo limitato e poi eliminati o resi anonimi. I dettagli delle richieste di demo vengono conservati solo per il tempo necessario a rispondere e dare seguito.',
                'Geaggregeerde analysegegevens worden door onze analyseleverancier gedurende een beperkte periode bewaard en daarna verwijderd of geanonimiseerd. Gegevens van demoaanvragen worden alleen bewaard zolang dat nodig is om te reageren en op te volgen.'),
            'Changes to this notice': _t(
                'Modifications de cet avis', 'Änderungen an diesem Hinweis',
                'Cambios en este aviso', 'Modifiche a questa informativa',
                'Wijzigingen in deze kennisgeving'),
            'We may update this notice as our practices or the applicable rules change. The "last updated" date above shows when it was last revised.': _t(
                'Nous pouvons mettre à jour cet avis à mesure que nos pratiques ou les règles applicables évoluent. La date de « dernière mise à jour » ci-dessus indique quand il a été révisé pour la dernière fois.',
                'Wir können diesen Hinweis aktualisieren, wenn sich unsere Praktiken oder die geltenden Regeln ändern. Das Datum "zuletzt aktualisiert" oben zeigt, wann er zuletzt überarbeitet wurde.',
                'Podemos actualizar este aviso a medida que cambien nuestras prácticas o las normas aplicables. La fecha de "última actualización" que figura arriba indica cuándo se revisó por última vez.',
                "Possiamo aggiornare questa informativa man mano che le nostre pratiche o le regole applicabili cambiano. La data di \"ultimo aggiornamento\" qui sopra indica quando è stata rivista l'ultima volta.",
                'We kunnen deze kennisgeving bijwerken naarmate onze werkwijzen of de geldende regels veranderen. De datum "laatst bijgewerkt" hierboven geeft aan wanneer ze voor het laatst is herzien.'),
            'This notice is provided for transparency and general information. It is not legal advice. For questions about your information, contact <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a>.': _t(
                "Cet avis est fourni à des fins de transparence et d'information générale. Il ne constitue pas un avis juridique. Pour toute question concernant vos informations, contactez <a href=\"mailto:contact@avenlorconsulting.com\">contact@avenlorconsulting.com</a>.",
                'Dieser Hinweis dient der Transparenz und der allgemeinen Information. Er stellt keine Rechtsberatung dar. Bei Fragen zu Ihren Informationen wenden Sie sich an <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a>.',
                'Este aviso se ofrece con fines de transparencia e información general. No constituye asesoramiento jurídico. Si tiene preguntas sobre su información, escriba a <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a>.',
                'Questa informativa è fornita a scopo di trasparenza e informazione generale. Non costituisce consulenza legale. Per domande sulle tue informazioni, contatta <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a>.',
                'Deze kennisgeving wordt verstrekt voor transparantie en algemene informatie. Het is geen juridisch advies. Voor vragen over uw informatie kunt u contact opnemen met <a href="mailto:contact@avenlorconsulting.com">contact@avenlorconsulting.com</a>.'),
        },
    },

    # ==================================================================
    '/compare/spreadsheets/': {
        'src': 'compare/spreadsheets/index.html',
        't': {
            # ---- Meta ----
            'FulcrumGrid vs. Spreadsheets: When to Move Off Excel &amp; Google Sheets | FulcrumGrid': _t(
                'FulcrumGrid vs. tableurs : quand abandonner Excel &amp; Google Sheets | FulcrumGrid',
                'FulcrumGrid vs. Tabellenkalkulationen: Wann Sie Excel &amp; Google Sheets verlassen sollten | FulcrumGrid',
                'FulcrumGrid vs. hojas de cálculo: cuándo dejar Excel &amp; Google Sheets | FulcrumGrid',
                'FulcrumGrid vs. fogli di calcolo: quando abbandonare Excel &amp; Google Sheets | FulcrumGrid',
                'FulcrumGrid vs. spreadsheets: wanneer stap je over van Excel &amp; Google Sheets | FulcrumGrid'),
            'How FulcrumGrid compares to running your business on spreadsheets — where spreadsheets still work, where they break down (versioning, access, audit trail, automation), and what you gain by moving to purpose-built apps.': _t(
                "Comment FulcrumGrid se compare à la gestion de votre entreprise sur tableur — là où les tableurs fonctionnent encore, là où ils atteignent leurs limites (gestion des versions, accès, piste d'audit, automatisation), et ce que vous gagnez en passant à des applications sur mesure.",
                'Wie sich FulcrumGrid mit der Führung Ihres Unternehmens per Tabellenkalkulation vergleicht — wo Tabellenkalkulationen noch funktionieren, wo sie an ihre Grenzen stoßen (Versionierung, Zugriff, Audit-Trail, Automatisierung) und was Sie durch den Wechsel zu zweckgebauten Apps gewinnen.',
                'Cómo se compara FulcrumGrid con gestionar tu negocio en hojas de cálculo — dónde las hojas de cálculo siguen funcionando, dónde fallan (control de versiones, acceso, registro de auditoría, automatización) y qué ganas al pasar a aplicaciones a medida.',
                'Come si confronta FulcrumGrid con la gestione della tua azienda sui fogli di calcolo — dove i fogli di calcolo funzionano ancora, dove mostrano i loro limiti (versionamento, accessi, audit trail, automazione) e cosa guadagni passando ad applicazioni su misura.',
                'Hoe FulcrumGrid zich verhoudt tot het runnen van uw bedrijf op spreadsheets — waar spreadsheets nog werken, waar ze vastlopen (versiebeheer, toegang, audittrail, automatisering) en wat u wint door over te stappen op doelgerichte apps.'),
            # ---- Breadcrumb / hero ----
            'Home': _t('Accueil', 'Startseite', 'Inicio', 'Home', 'Home'),
            'vs. spreadsheets': _t('vs. tableurs', 'vs. Tabellenkalkulationen', 'vs. hojas de cálculo', 'vs. fogli di calcolo', 'vs. spreadsheets'),
            'Comparison': _t('Comparaison', 'Vergleich', 'Comparación', 'Confronto', 'Vergelijking'),
            'FulcrumGrid vs. <em>spreadsheets</em>': _t(
                'FulcrumGrid vs. <em>tableurs</em>',
                'FulcrumGrid vs. <em>Tabellenkalkulationen</em>',
                'FulcrumGrid vs. <em>hojas de cálculo</em>',
                'FulcrumGrid vs. <em>fogli di calcolo</em>',
                'FulcrumGrid vs. <em>rekenbladen</em>'),
            "Almost every business starts in a spreadsheet. Here's an honest look at where spreadsheets still work, where they break down, and what a purpose-built app gives you instead.": _t(
                "Presque toutes les entreprises commencent sur un tableur. Voici un regard honnête sur les cas où les tableurs fonctionnent encore, ceux où ils atteignent leurs limites, et ce qu'une application sur mesure vous apporte à la place.",
                'Fast jedes Unternehmen beginnt in einer Tabellenkalkulation. Hier ein ehrlicher Blick darauf, wo Tabellenkalkulationen noch funktionieren, wo sie an ihre Grenzen stoßen und was Ihnen eine zweckgebaute App stattdessen bietet.',
                'Casi todos los negocios empiezan en una hoja de cálculo. Aquí tiene una mirada honesta a dónde las hojas de cálculo siguen funcionando, dónde fallan y qué le ofrece a cambio una aplicación a medida.',
                "Quasi tutte le aziende iniziano in un foglio di calcolo. Ecco uno sguardo onesto su dove i fogli di calcolo funzionano ancora, dove mostrano i loro limiti e cosa ti offre invece un'applicazione su misura.",
                'Bijna elk bedrijf begint in een spreadsheet. Hier is een eerlijke blik op waar spreadsheets nog werken, waar ze vastlopen en wat een doelgerichte app u in plaats daarvan biedt.'),
            'Honest take': _t('Avis honnête', 'Ehrliche Einschätzung', 'Opinión honesta', 'Valutazione onesta', 'Eerlijke kijk'),
            # ---- Comparison table ----
            'Side by side': _t('Côte à côte', 'Direkter Vergleich', 'Cara a cara', 'Fianco a fianco', 'Naast elkaar'),
            'Spreadsheets': _t('Tableurs', 'Tabellenkalkulationen', 'Hojas de cálculo', 'Fogli di calcolo', 'Spreadsheets'),
            'Multiple people at once': _t('Plusieurs personnes en même temps', 'Mehrere Personen gleichzeitig', 'Varias personas a la vez', 'Più persone contemporaneamente', 'Meerdere mensen tegelijk'),
            'Version conflicts and “final_v3” chaos': _t(
                'Conflits de versions et chaos des “final_v3”',
                'Versionskonflikte und Chaos mit “final_v3”',
                'Conflictos de versiones y el caos de los “final_v3”',
                'Conflitti di versione e il caos dei “final_v3”',
                'Versieconflicten en “final_v3”-chaos'),
            'Real-time, multi-user by design': _t('Multi-utilisateur en temps réel par conception', 'Echtzeit, mehrbenutzerfähig von Grund auf', 'Multiusuario en tiempo real por diseño', 'Multiutente in tempo reale per progettazione', 'Realtime, multi-user vanuit het ontwerp'),
            'Access control': _t("Contrôle d'accès", 'Zugriffskontrolle', 'Control de acceso', 'Controllo degli accessi', 'Toegangsbeheer'),
            'All-or-nothing file sharing': _t('Partage de fichiers tout ou rien', 'Alles-oder-nichts-Dateifreigabe', 'Compartición de archivos de todo o nada', 'Condivisione di file tutto-o-niente', 'Alles-of-niets-bestandsdeling'),
            'Role-based access per person': _t('Accès par rôle pour chaque personne', 'Rollenbasierter Zugriff pro Person', 'Acceso por roles para cada persona', 'Accesso basato sui ruoli per ogni persona', 'Toegang op rol per persoon'),
            'Audit trail': _t("Piste d'audit", 'Audit-Trail', 'Registro de auditoría', 'Audit trail', 'Audittrail'),
            'None — edits are silent': _t('Aucune — les modifications sont silencieuses', 'Keiner — Änderungen erfolgen unbemerkt', 'Ninguno — las ediciones son silenciosas', 'Nessuno — le modifiche sono silenziose', 'Geen — bewerkingen zijn onzichtbaar'),
            'Full history of who changed what': _t('Historique complet de qui a modifié quoi', 'Vollständige Historie, wer was geändert hat', 'Historial completo de quién cambió qué', 'Cronologia completa di chi ha modificato cosa', 'Volledige geschiedenis van wie wat wijzigde'),
            'Automation': _t('Automatisation', 'Automatisierung', 'Automatización', 'Automazione', 'Automatisering'),
            'Manual formulas and copy-paste': _t('Formules manuelles et copier-coller', 'Manuelle Formeln und Copy-Paste', 'Fórmulas manuales y copiar y pegar', 'Formule manuali e copia-incolla', 'Handmatige formules en kopiëren-plakken'),
            'Automated reminders and workflows': _t('Rappels et flux de travail automatisés', 'Automatisierte Erinnerungen und Workflows', 'Recordatorios y flujos de trabajo automatizados', 'Promemoria e flussi di lavoro automatizzati', 'Geautomatiseerde herinneringen en workflows'),
            'Reporting': _t('Rapports', 'Berichte', 'Informes', 'Reportistica', 'Rapportage'),
            'Rebuilt by hand each time': _t('Reconstruits à la main à chaque fois', 'Jedes Mal von Hand neu erstellt', 'Rehechos a mano cada vez', 'Ricostruiti a mano ogni volta', 'Elke keer handmatig opnieuw opgebouwd'),
            'Real-time dashboards and reports': _t('Tableaux de bord et rapports en temps réel', 'Echtzeit-Dashboards und Berichte', 'Paneles e informes en tiempo real', 'Dashboard e report in tempo reale', 'Realtime dashboards en rapporten'),
            'Data integrity': _t('Intégrité des données', 'Datenintegrität', 'Integridad de los datos', 'Integrità dei dati', 'Gegevensintegriteit'),
            'One wrong cell breaks a formula': _t('Une cellule erronée casse une formule', 'Eine falsche Zelle zerstört eine Formel', 'Una celda equivocada rompe una fórmula', 'Una cella sbagliata rompe una formula', 'Eén verkeerde cel breekt een formule'),
            'Structured, validated records': _t('Des enregistrements structurés et validés', 'Strukturierte, validierte Datensätze', 'Registros estructurados y validados', 'Record strutturati e convalidati', 'Gestructureerde, gevalideerde records'),
            'Scaling': _t('Montée en charge', 'Skalierung', 'Escalado', 'Scalabilità', 'Schaalbaarheid'),
            'Slows and breaks as data grows': _t('Ralentit et casse à mesure que les données augmentent', 'Wird langsam und bricht, wenn die Daten wachsen', 'Se ralentiza y falla a medida que crecen los datos', 'Rallenta e si rompe con la crescita dei dati', 'Wordt traag en breekt naarmate de data groeit'),
            'Built to grow with you': _t('Conçu pour grandir avec vous', 'Gebaut, um mit Ihnen zu wachsen', 'Creado para crecer con usted', 'Costruito per crescere con te', 'Gebouwd om met u mee te groeien'),
            'Your data': _t('Vos données', 'Ihre Daten', 'Sus datos', 'I tuoi dati', 'Uw gegevens'),
            'Yours, but siloed in files': _t('À vous, mais cloisonnées dans des fichiers', 'Ihre, aber in Dateien isoliert', 'Suyos, pero aislados en archivos', 'Tuoi, ma isolati in file', 'Van u, maar opgesloten in bestanden'),
            'Yours, and exportable anytime': _t('À vous, et exportables à tout moment', 'Ihre, und jederzeit exportierbar', 'Suyos, y exportables en cualquier momento', 'Tuoi, ed esportabili in qualsiasi momento', 'Van u, en altijd exporteerbaar'),
            # ---- "Still the right tool" ----
            'When a spreadsheet is still the right tool': _t(
                'Quand un tableur reste le bon outil',
                'Wann eine Tabellenkalkulation noch das richtige Werkzeug ist',
                'Cuándo una hoja de cálculo sigue siendo la herramienta adecuada',
                'Quando un foglio di calcolo resta lo strumento giusto',
                'Wanneer een spreadsheet nog het juiste hulpmiddel is'),
            "Spreadsheets are excellent for quick models, throwaway calculations, and solo one-off analysis — fast, flexible, and familiar. FulcrumGrid isn't trying to replace that. The switch pays off once several people share the file, it becomes the system of record for a process, or a single wrong cell starts costing real money.": _t(
                "Les tableurs sont excellents pour les modèles rapides, les calculs jetables et l'analyse ponctuelle en solo — rapides, souples et familiers. FulcrumGrid ne cherche pas à remplacer cela. Le changement devient payant dès que plusieurs personnes partagent le fichier, qu'il devient le système de référence d'un processus, ou qu'une seule cellule erronée commence à coûter de l'argent.",
                'Tabellenkalkulationen sind hervorragend für schnelle Modelle, Wegwerf-Berechnungen und einmalige Einzelanalysen — schnell, flexibel und vertraut. FulcrumGrid will das nicht ersetzen. Der Wechsel lohnt sich, sobald mehrere Personen die Datei teilen, sie zum maßgeblichen System für einen Prozess wird oder eine einzige falsche Zelle anfängt, echtes Geld zu kosten.',
                'Las hojas de cálculo son excelentes para modelos rápidos, cálculos desechables y análisis puntuales en solitario — rápidas, flexibles y familiares. FulcrumGrid no pretende sustituir eso. El cambio compensa en cuanto varias personas comparten el archivo, este se convierte en el sistema de referencia de un proceso, o una sola celda equivocada empieza a costar dinero de verdad.',
                "I fogli di calcolo sono eccellenti per modelli rapidi, calcoli usa e getta e analisi occasionali in autonomia — veloci, flessibili e familiari. FulcrumGrid non cerca di sostituirli. Il passaggio conviene non appena più persone condividono il file, questo diventa il sistema di riferimento di un processo, oppure una singola cella sbagliata inizia a costare denaro vero.",
                'Spreadsheets zijn uitstekend voor snelle modellen, wegwerpberekeningen en eenmalige solo-analyses — snel, flexibel en vertrouwd. FulcrumGrid probeert dat niet te vervangen. De overstap loont zodra meerdere mensen het bestand delen, het het administratiesysteem voor een proces wordt, of één verkeerde cel echt geld begint te kosten.'),
            # ---- FAQ ----
            'Common questions': _t('Questions fréquentes', 'Häufige Fragen', 'Preguntas frecuentes', 'Domande frequenti', 'Veelgestelde vragen'),
            'Is FulcrumGrid a spreadsheet replacement?': _t(
                'FulcrumGrid remplace-t-il un tableur ?',
                'Ist FulcrumGrid ein Ersatz für Tabellenkalkulationen?',
                '¿Es FulcrumGrid un sustituto de las hojas de cálculo?',
                'FulcrumGrid è un sostituto dei fogli di calcolo?',
                'Is FulcrumGrid een vervanging voor spreadsheets?'),
            'For running a business process — invoicing, HR records, operations tracking — yes. FulcrumGrid replaces the fragile spreadsheets teams outgrow with structured, multi-user apps. For quick one-off analysis, a spreadsheet is still a fine tool.': _t(
                'Pour gérer un processus métier — facturation, dossiers RH, suivi des opérations — oui. FulcrumGrid remplace les tableurs fragiles que les équipes finissent par dépasser par des applications structurées et multi-utilisateurs. Pour une analyse ponctuelle rapide, un tableur reste un bon outil.',
                'Für die Abwicklung eines Geschäftsprozesses — Rechnungsstellung, HR-Daten, Betriebsverfolgung — ja. FulcrumGrid ersetzt die fragilen Tabellenkalkulationen, die Teams entwachsen, durch strukturierte, mehrbenutzerfähige Apps. Für eine schnelle einmalige Analyse ist eine Tabellenkalkulation weiterhin ein gutes Werkzeug.',
                'Para gestionar un proceso de negocio — facturación, registros de RR. HH., seguimiento de operaciones — sí. FulcrumGrid sustituye las frágiles hojas de cálculo que los equipos acaban superando por aplicaciones estructuradas y multiusuario. Para un análisis puntual rápido, una hoja de cálculo sigue siendo una buena herramienta.',
                "Per gestire un processo aziendale — fatturazione, dati HR, monitoraggio delle operazioni — sì. FulcrumGrid sostituisce i fragili fogli di calcolo che i team finiscono per superare con app strutturate e multiutente. Per un'analisi rapida e occasionale, un foglio di calcolo resta un ottimo strumento.",
                'Voor het draaien van een bedrijfsproces — facturatie, HR-gegevens, operationele tracking — ja. FulcrumGrid vervangt de kwetsbare spreadsheets die teams ontgroeien door gestructureerde, multi-user apps. Voor een snelle eenmalige analyse is een spreadsheet nog steeds een prima hulpmiddel.'),
            'Can I import my existing spreadsheets?': _t(
                'Puis-je importer mes tableurs existants ?',
                'Kann ich meine vorhandenen Tabellenkalkulationen importieren?',
                '¿Puedo importar mis hojas de cálculo existentes?',
                'Posso importare i miei fogli di calcolo esistenti?',
                'Kan ik mijn bestaande spreadsheets importeren?'),
            'Yes. You can bring your records in when you set up an app. Tell us what you have on the <a href="/contact/">contact page</a> and we’ll help you move.': _t(
                'Oui. Vous pouvez importer vos enregistrements lors de la configuration d\'une application. Dites-nous ce que vous avez sur la <a href="/contact/">page de contact</a> et nous vous aiderons à migrer.',
                'Ja. Sie können Ihre Datensätze mitbringen, wenn Sie eine App einrichten. Sagen Sie uns auf der <a href="/contact/">Kontaktseite</a>, was Sie haben, und wir helfen Ihnen beim Umzug.',
                'Sí. Puede traer sus registros al configurar una app. Cuéntenos qué tiene en la <a href="/contact/">página de contacto</a> y le ayudaremos a migrar.',
                'Sì. Puoi importare i tuoi record quando configuri un\'app. Dicci cosa hai nella <a href="/contact/">pagina dei contatti</a> e ti aiuteremo a migrare.',
                'Ja. U kunt uw records meenemen wanneer u een app instelt. Vertel ons wat u hebt op de <a href="/contact/">contactpagina</a> en we helpen u met de overstap.'),
            'When is a spreadsheet still the better choice?': _t(
                'Quand un tableur reste-t-il le meilleur choix ?',
                'Wann ist eine Tabellenkalkulation noch die bessere Wahl?',
                '¿Cuándo sigue siendo una hoja de cálculo la mejor opción?',
                'Quando un foglio di calcolo resta la scelta migliore?',
                'Wanneer is een spreadsheet nog de betere keuze?'),
            'For a quick model, a throwaway calculation, or a solo one-off analysis, a spreadsheet is fast and flexible. The moment several people share it, it becomes a system of record, or mistakes start to cost money, a purpose-built app pays off.': _t(
                "Pour un modèle rapide, un calcul jetable ou une analyse ponctuelle en solo, un tableur est rapide et souple. Dès que plusieurs personnes le partagent, qu'il devient un système de référence ou que les erreurs commencent à coûter de l'argent, une application sur mesure devient payante.",
                'Für ein schnelles Modell, eine Wegwerf-Berechnung oder eine einmalige Einzelanalyse ist eine Tabellenkalkulation schnell und flexibel. Sobald mehrere Personen sie teilen, sie zu einem maßgeblichen System wird oder Fehler anfangen, Geld zu kosten, zahlt sich eine zweckgebaute App aus.',
                'Para un modelo rápido, un cálculo desechable o un análisis puntual en solitario, una hoja de cálculo es rápida y flexible. En cuanto varias personas la comparten, se convierte en un sistema de referencia o los errores empiezan a costar dinero, una aplicación a medida compensa.',
                "Per un modello rapido, un calcolo usa e getta o un'analisi occasionale in autonomia, un foglio di calcolo è veloce e flessibile. Nel momento in cui più persone lo condividono, diventa un sistema di riferimento o gli errori iniziano a costare denaro, un'app su misura ripaga.",
                'Voor een snel model, een wegwerpberekening of een eenmalige solo-analyse is een spreadsheet snel en flexibel. Zodra meerdere mensen hem delen, hij een administratiesysteem wordt of fouten geld gaan kosten, betaalt een doelgerichte app zich terug.'),
            # ---- CTA ----
            'Outgrown your<br />spreadsheets?': _t(
                'Vos tableurs<br />sont dépassés ?',
                'Ihren Tabellenkalkulationen<br />entwachsen?',
                '¿Ha superado sus<br />hojas de cálculo?',
                'Hai superato i tuoi<br />fogli di calcolo?',
                'Uw spreadsheets<br />ontgroeid?'),
            "Tell us what you're running today and we'll show you the FulcrumGrid app that replaces it.": _t(
                "Dites-nous ce que vous utilisez aujourd'hui et nous vous montrerons l'application FulcrumGrid qui le remplace.",
                'Sagen Sie uns, was Sie heute nutzen, und wir zeigen Ihnen die FulcrumGrid-App, die es ersetzt.',
                'Cuéntenos qué utiliza hoy y le mostraremos la app de FulcrumGrid que lo sustituye.',
                "Dicci cosa usi oggi e ti mostreremo l'app FulcrumGrid che lo sostituisce.",
                'Vertel ons wat u vandaag gebruikt en we tonen u de FulcrumGrid-app die het vervangt.'),
            'See all products': _t('Voir tous les produits', 'Alle Produkte ansehen', 'Ver todos los productos', 'Vedi tutti i prodotti', 'Bekijk alle producten'),
        },
    },

    # ==================================================================
    '/404.html': {
        'src': '404.html',
        't': {
            'Page not found — FulcrumGrid': _t(
                'Page introuvable — FulcrumGrid',
                'Seite nicht gefunden — FulcrumGrid',
                'Página no encontrada — FulcrumGrid',
                'Pagina non trovata — FulcrumGrid',
                'Pagina niet gevonden — FulcrumGrid'),
            'Error 404': _t('Erreur 404', 'Fehler 404', 'Error 404', 'Errore 404', 'Fout 404'),
            "This page isn't on the grid": _t(
                "Cette page n'est pas sur la grille",
                'Diese Seite ist nicht im Grid',
                'Esta página no está en la cuadrícula',
                'Questa pagina non è nella griglia',
                'Deze pagina staat niet op het grid'),
            "The page you're looking for may have moved or never existed. Let's get you back on track.": _t(
                "La page que vous recherchez a peut-être été déplacée ou n'a jamais existé. Remettons-vous sur les rails.",
                'Die von Ihnen gesuchte Seite wurde möglicherweise verschoben oder hat nie existiert. Bringen wir Sie zurück auf den richtigen Weg.',
                'La página que busca puede haberse movido o no haber existido nunca. Volvamos a encaminarle.',
                'La pagina che cerchi potrebbe essere stata spostata o non essere mai esistita. Rimettiamoti sulla strada giusta.',
                'De pagina die u zoekt is mogelijk verplaatst of heeft nooit bestaan. Laten we u weer op weg helpen.'),
            'Back to FulcrumGrid': _t(
                'Retour à FulcrumGrid', 'Zurück zu FulcrumGrid', 'Volver a FulcrumGrid',
                'Torna a FulcrumGrid', 'Terug naar FulcrumGrid'),
        },
    },
}
