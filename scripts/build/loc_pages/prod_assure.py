# -*- coding: utf-8 -*-
"""Per-page translations for the Assure product page.

Keys are EXACT English substrings of the EN source HTML (entities, straight
apostrophes, dashes and glyphs preserved). Brand/product names (FulcrumGrid,
Assure, Command Center, Collection, HR Suite) and code/standard labels (NCA
ECC-2, PDPL, CMA, ISO 27001, NIST CSF, AWS, Azure, GCP, OIDC, API, CSV, PDF,
TPRM, DSAR, RoPA, DPIA, GRC) are left untranslated inside the surrounding copy.
Common chrome (nav, footer, buttons like "Request a demo"/"Email us") lives in
loc_catalog.COMMON, not here.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/products/assure/': {
        'src': 'products/assure/index.html',
        't': {
            # ---- Title (brand kept; registered so the oracle treats it as handled) ----
            "Assure — FulcrumGrid": _t(
                "Assure — FulcrumGrid", "Assure — FulcrumGrid", "Assure — FulcrumGrid",
                "Assure — FulcrumGrid", "Assure — FulcrumGrid"),
            # ---- Hero ----
            "Governance · Available now": _t(
                "Gouvernance · Disponible maintenant",
                "Governance · Jetzt verfügbar",
                "Gobernanza · Ya disponible",
                "Governance · Ora disponibile",
                "Governance · Nu beschikbaar"),
            "Compliance you can prove.": _t(
                "Une conformité que vous pouvez prouver.",
                "Compliance, die Sie beweisen können.",
                "Un cumplimiento que puede demostrar.",
                "Una conformità che puoi dimostrare.",
                "Compliance die u kunt bewijzen."),
            "Assure maps Saudi regulatory obligations to the controls that satisfy them, then drives the evidence end to end — generated on schedule, reviewed by a second pair of eyes, and locked so it holds up to an audit. Governance, risk and compliance, built for Saudi regulation.": _t(
                "Assure relie les obligations réglementaires saoudiennes aux contrôles qui les satisfont, puis pilote les preuves de bout en bout — générées dans les délais, revues par un second regard et verrouillées pour résister à un audit. Gouvernance, risque et conformité, conçus pour la réglementation saoudienne.",
                "Assure ordnet saudische regulatorische Pflichten den Kontrollen zu, die sie erfüllen, und steuert dann die Nachweise von Anfang bis Ende — termingerecht erzeugt, nach dem Vier-Augen-Prinzip geprüft und so gesperrt, dass sie einer Prüfung standhalten. Governance, Risiko und Compliance, gebaut für die saudische Regulierung.",
                "Assure vincula las obligaciones regulatorias saudíes con los controles que las satisfacen y luego dirige las evidencias de principio a fin — generadas a tiempo, revisadas por un segundo par de ojos y bloqueadas para que resistan una auditoría. Gobernanza, riesgo y cumplimiento, diseñados para la regulación saudí.",
                "Assure collega gli obblighi normativi sauditi ai controlli che li soddisfano, poi guida le evidenze dall'inizio alla fine — generate nei tempi previsti, riviste da un secondo paio di occhi e bloccate per reggere a un audit. Governance, rischio e conformità, costruiti per la normativa saudita.",
                "Assure koppelt Saoedische regelgevingsverplichtingen aan de controles die eraan voldoen en stuurt vervolgens het bewijs van begin tot eind — op tijd gegenereerd, beoordeeld door een tweede paar ogen en vergrendeld zodat het een audit doorstaat. Governance, risico en compliance, gebouwd voor Saoedische regelgeving."),
            # ---- 01 · Pricing ----
            "01 · Pricing": _t("01 · Tarifs", "01 · Preise", "01 · Precios", "01 · Prezzi", "01 · Prijzen"),
            "Pricing — talk to sales.": _t(
                "Tarifs — parlez-en aux ventes.",
                "Preise — sprechen Sie mit dem Vertrieb.",
                "Precios — hable con ventas.",
                "Prezzi — parla con le vendite.",
                "Prijzen — praat met sales."),
            "Assure is self-hosted and priced to your estate — the legal entities you run, the frameworks in scope and the people who use it. Tell us your scope and we'll put a figure to it.": _t(
                "Assure est auto-hébergé et tarifé selon votre périmètre — les entités juridiques que vous gérez, les référentiels concernés et les personnes qui l'utilisent. Indiquez-nous votre périmètre et nous y mettrons un prix.",
                "Assure wird selbst gehostet und nach Ihrem Bestand bepreist — den Rechtsträgern, die Sie betreiben, den einbezogenen Rahmenwerken und den Menschen, die es nutzen. Nennen Sie uns Ihren Umfang, und wir beziffern ihn.",
                "Assure es autoalojado y su precio se ajusta a su alcance — las entidades jurídicas que gestiona, los marcos incluidos y las personas que lo usan. Díganos su alcance y le pondremos una cifra.",
                "Assure è self-hosted e il prezzo è calibrato sul tuo perimetro — le entità giuridiche che gestisci, i framework inclusi e le persone che lo usano. Dicci il tuo perimetro e gli daremo un prezzo.",
                "Assure is zelf-gehost en geprijsd naar uw omvang — de rechtspersonen die u beheert, de kaders in scope en de mensen die het gebruiken. Vertel ons uw scope en we zetten er een bedrag op."),
            "Talk to sales": _t(
                "Parlez-en aux ventes", "Mit dem Vertrieb sprechen", "Hablar con ventas",
                "Parla con le vendite", "Praat met sales"),
            # ---- 02 · Capabilities ----
            "02 · Capabilities": _t("02 · Capacités", "02 · Funktionen", "02 · Capacidades", "02 · Funzionalità", "02 · Mogelijkheden"),
            "Governance, risk and compliance in one system.": _t(
                "Gouvernance, risque et conformité dans un seul système.",
                "Governance, Risiko und Compliance in einem System.",
                "Gobernanza, riesgo y cumplimiento en un solo sistema.",
                "Governance, rischio e conformità in un unico sistema.",
                "Governance, risico en compliance in één systeem."),
            "Every obligation mapped to a control, every control backed by evidence — the whole GRC cycle, tracked and enforced.": _t(
                "Chaque obligation reliée à un contrôle, chaque contrôle étayé par des preuves — tout le cycle GRC, suivi et appliqué.",
                "Jede Pflicht einer Kontrolle zugeordnet, jede Kontrolle durch Nachweise belegt — der gesamte GRC-Zyklus, nachverfolgt und durchgesetzt.",
                "Cada obligación vinculada a un control, cada control respaldado por evidencias — todo el ciclo de GRC, con seguimiento y aplicado.",
                "Ogni obbligo collegato a un controllo, ogni controllo supportato da evidenze — l'intero ciclo GRC, monitorato e applicato.",
                "Elke verplichting gekoppeld aan een control, elke control onderbouwd met bewijs — de volledige GRC-cyclus, gevolgd en afgedwongen."),
            "Saudi regulatory catalog": _t(
                "Catalogue réglementaire saoudien", "Saudischer Regulierungskatalog",
                "Catálogo regulatorio saudí", "Catalogo normativo saudita",
                "Saoedische regelgevingscatalogus"),
            "Obligations arrive pre-mapped for NCA ECC-2, PDPL, CMA Corporate Governance and the Companies Law, alongside ISO 27001 and NIST CSF — applied per legal entity by a scope gate.": _t(
                "Les obligations arrivent déjà reliées à NCA ECC-2, PDPL, la gouvernance d'entreprise de la CMA et la loi sur les sociétés, aux côtés d'ISO 27001 et du NIST CSF — appliquées par entité juridique via une barrière de périmètre.",
                "Die Pflichten kommen bereits zugeordnet für NCA ECC-2, PDPL, CMA Corporate Governance und das Gesellschaftsrecht, neben ISO 27001 und NIST CSF — angewendet je Rechtsträger durch ein Scope-Gate.",
                "Las obligaciones llegan ya vinculadas a NCA ECC-2, PDPL, el Gobierno Corporativo de la CMA y la Ley de Sociedades, junto a ISO 27001 y NIST CSF — aplicadas por entidad jurídica mediante una puerta de alcance.",
                "Gli obblighi arrivano già mappati per NCA ECC-2, PDPL, la Corporate Governance della CMA e la legge sulle società, insieme a ISO 27001 e NIST CSF — applicati per entità giuridica tramite un gate di perimetro.",
                "De verplichtingen komen al gekoppeld voor NCA ECC-2, PDPL, CMA Corporate Governance en de vennootschapswet, naast ISO 27001 en NIST CSF — toegepast per rechtspersoon via een scope-gate."),
            "Recurring obligation engine": _t(
                "Moteur d'obligations récurrentes", "Engine für wiederkehrende Pflichten",
                "Motor de obligaciones recurrentes", "Motore degli obblighi ricorrenti",
                "Engine voor terugkerende verplichtingen"),
            "Compliance tasks are generated automatically on both the Hijri and Gregorian calendars, so nothing lapses between reviews.": _t(
                "Les tâches de conformité sont générées automatiquement selon les calendriers hégirien et grégorien, pour que rien n'expire entre deux revues.",
                "Compliance-Aufgaben werden automatisch nach dem Hidschri- und dem gregorianischen Kalender erzeugt, damit zwischen den Prüfungen nichts verfällt.",
                "Las tareas de cumplimiento se generan automáticamente en los calendarios hégira y gregoriano, para que nada caduque entre revisiones.",
                "Le attività di conformità vengono generate automaticamente sui calendari islamico e gregoriano, così nulla scade tra una revisione e l'altra.",
                "Compliance-taken worden automatisch gegenereerd op zowel de Hijri- als de Gregoriaanse kalender, zodat er tussen beoordelingen niets verloopt."),
            "Maker-checker workflow": _t(
                "Flux maker-checker", "Maker-Checker-Workflow", "Flujo maker-checker",
                "Flusso maker-checker", "Maker-checker-workflow"),
            "Submit, review, approve: every piece of evidence moves through a segregation of duties the database enforces, not just the screen.": _t(
                "Soumettre, revoir, approuver : chaque preuve passe par une séparation des tâches imposée par la base de données, et pas seulement par l'écran.",
                "Einreichen, prüfen, freigeben: Jeder Nachweis durchläuft eine Funktionstrennung, die die Datenbank erzwingt, nicht nur der Bildschirm.",
                "Enviar, revisar, aprobar: cada evidencia pasa por una separación de funciones que impone la base de datos, no solo la pantalla.",
                "Invia, rivedi, approva: ogni evidenza attraversa una separazione dei compiti imposta dal database, non solo dallo schermo.",
                "Indienen, beoordelen, goedkeuren: elk bewijsstuk doorloopt een functiescheiding die de database afdwingt, niet alleen het scherm."),
            "Immutable evidence vault": _t(
                "Coffre de preuves inaltérable", "Unveränderlicher Nachweis-Tresor",
                "Bóveda de evidencias inmutable", "Caveau delle evidenze immutabile",
                "Onveranderlijke bewijskluis"),
            "Every uploaded file is content-hashed on arrival, so it can't be altered or deleted after the fact.": _t(
                "Chaque fichier téléversé est haché par son contenu à l'arrivée, de sorte qu'il ne peut être ni modifié ni supprimé après coup.",
                "Jede hochgeladene Datei erhält beim Eingang einen Inhalts-Hash, sodass sie nachträglich weder verändert noch gelöscht werden kann.",
                "Cada archivo subido recibe un hash de su contenido al llegar, de modo que no puede alterarse ni eliminarse después.",
                "Ogni file caricato riceve un hash del contenuto all'arrivo, così non può essere alterato o eliminato in seguito.",
                "Elk geüpload bestand krijgt bij binnenkomst een content-hash, zodat het achteraf niet kan worden gewijzigd of verwijderd."),
            "Controls &amp; crosswalk": _t(
                "Contrôles &amp; correspondance", "Kontrollen &amp; Crosswalk",
                "Controles &amp; correspondencia", "Controlli &amp; crosswalk",
                "Controls &amp; crosswalk"),
            "Rate each control's implementation and maturity, and map one control to several frameworks so the same evidence is reused, not re-collected.": _t(
                "Évaluez la mise en œuvre et la maturité de chaque contrôle, et reliez un même contrôle à plusieurs référentiels pour que la même preuve soit réutilisée, pas recollectée.",
                "Bewerten Sie Umsetzung und Reife jeder Kontrolle und ordnen Sie eine Kontrolle mehreren Rahmenwerken zu, damit derselbe Nachweis wiederverwendet statt neu erhoben wird.",
                "Valore la implementación y la madurez de cada control, y vincule un mismo control a varios marcos para que la misma evidencia se reutilice en lugar de volver a recopilarse.",
                "Valuta l'implementazione e la maturità di ogni controllo e collega un singolo controllo a più framework, così la stessa evidenza viene riutilizzata invece di essere raccolta di nuovo.",
                "Beoordeel de implementatie en volwassenheid van elke control en koppel één control aan meerdere kaders, zodat hetzelfde bewijs wordt hergebruikt in plaats van opnieuw verzameld."),
            "Risk register": _t(
                "Registre des risques", "Risikoregister", "Registro de riesgos",
                "Registro dei rischi", "Risicoregister"),
            "Score risks inherent and residual, attach treatment plans, and time-box risk acceptance so it auto-reopens when it expires.": _t(
                "Notez les risques inhérents et résiduels, associez des plans de traitement et limitez dans le temps l'acceptation du risque, qui se rouvre automatiquement à son expiration.",
                "Bewerten Sie Risiken inhärent und residual, hängen Sie Maßnahmenpläne an und befristen Sie die Risikoakzeptanz, sodass sie bei Ablauf automatisch wieder geöffnet wird.",
                "Puntúe los riesgos inherentes y residuales, adjunte planes de tratamiento y limite en el tiempo la aceptación del riesgo, que se reabre automáticamente al vencer.",
                "Valuta i rischi inerenti e residui, allega piani di trattamento e limita nel tempo l'accettazione del rischio, che si riapre automaticamente alla scadenza.",
                "Scoor risico's inherent en residueel, voeg behandelplannen toe en begrens risicoacceptatie in de tijd, zodat die bij het verlopen automatisch heropent."),
            "Cyber posture": _t(
                "Posture cyber", "Cyber-Posture", "Postura cibernética",
                "Postura cyber", "Cyberpostuur"),
            "Outside-in vulnerability scans and inside-out cloud posture across AWS, Azure and GCP, with findings auto-assigned remediation SLAs by severity.": _t(
                "Des analyses de vulnérabilités de l'extérieur et une posture cloud de l'intérieur sur AWS, Azure et GCP, avec des SLA de remédiation attribués automatiquement aux constats selon leur gravité.",
                "Vulnerability-Scans von außen und Cloud-Posture von innen über AWS, Azure und GCP, wobei Funde automatisch Behebungs-SLAs nach Schweregrad erhalten.",
                "Escaneos de vulnerabilidades de fuera hacia dentro y postura de nube de dentro hacia fuera en AWS, Azure y GCP, con SLA de remediación asignados automáticamente a los hallazgos según su gravedad.",
                "Scansioni delle vulnerabilità dall'esterno e postura cloud dall'interno su AWS, Azure e GCP, con SLA di remediation assegnati automaticamente ai rilievi in base alla gravità.",
                "Vulnerability-scans van buitenaf en cloudpostuur van binnenuit over AWS, Azure en GCP, met bevindingen die automatisch remediatie-SLA's krijgen op basis van ernst."),
            "PDPL privacy toolkit": _t(
                "Boîte à outils de confidentialité PDPL", "PDPL-Datenschutz-Toolkit",
                "Kit de privacidad PDPL", "Toolkit privacy PDPL", "PDPL-privacytoolkit"),
            "Handle data-subject requests (DSAR) and keep Records of Processing Activities (RoPA), with DPIA flags where processing needs a closer look.": _t(
                "Traitez les demandes des personnes concernées (DSAR) et tenez les registres des activités de traitement (RoPA), avec des indicateurs d'AIPD là où le traitement mérite un examen plus poussé.",
                "Bearbeiten Sie Betroffenenanfragen (DSAR) und führen Sie Verzeichnisse von Verarbeitungstätigkeiten (RoPA), mit DSFA-Kennzeichen, wo eine Verarbeitung genauer betrachtet werden muss.",
                "Gestione las solicitudes de los interesados (DSAR) y mantenga los Registros de Actividades de Tratamiento (RoPA), con indicadores de EIPD donde el tratamiento requiera una mirada más detenida.",
                "Gestisci le richieste degli interessati (DSAR) e mantieni i Registri delle Attività di Trattamento (RoPA), con contrassegni DPIA dove il trattamento richiede un esame più attento.",
                "Behandel verzoeken van betrokkenen (DSAR) en houd Verwerkingsregisters (RoPA) bij, met DPIA-markeringen waar een verwerking nader moet worden bekeken."),
            "Vendor risk (TPRM)": _t(
                "Risque fournisseurs (TPRM)", "Lieferantenrisiko (TPRM)",
                "Riesgo de proveedores (TPRM)", "Rischio fornitori (TPRM)",
                "Leveranciersrisico (TPRM)"),
            "A third-party register with risk tiers, data-shared flags and a reassessment cadence, so vendor risk stays current.": _t(
                "Un registre des tiers avec niveaux de risque, indicateurs de données partagées et cadence de réévaluation, pour que le risque fournisseurs reste à jour.",
                "Ein Register für Dritte mit Risikostufen, Kennzeichen für geteilte Daten und einem Neubewertungs-Rhythmus, damit das Lieferantenrisiko aktuell bleibt.",
                "Un registro de terceros con niveles de riesgo, indicadores de datos compartidos y una cadencia de reevaluación, para que el riesgo de proveedores se mantenga al día.",
                "Un registro delle terze parti con livelli di rischio, contrassegni di dati condivisi e una cadenza di rivalutazione, così il rischio fornitori resta aggiornato.",
                "Een register van derden met risiconiveaus, markeringen voor gedeelde data en een herbeoordelingscadans, zodat leveranciersrisico actueel blijft."),
            "Incident management": _t(
                "Gestion des incidents", "Incident-Management", "Gestión de incidentes",
                "Gestione degli incidenti", "Incidentbeheer"),
            "Track severity and timeline, with a regulatory-notification deadline clock running from the moment an incident is logged.": _t(
                "Suivez la gravité et la chronologie, avec un compte à rebours de l'échéance de notification réglementaire qui démarre dès l'enregistrement de l'incident.",
                "Verfolgen Sie Schweregrad und Zeitverlauf, mit einer Frist-Uhr für die regulatorische Meldung, die ab dem Erfassen eines Vorfalls läuft.",
                "Realice el seguimiento de la gravedad y la cronología, con un reloj de plazo de notificación regulatoria que arranca en el momento en que se registra el incidente.",
                "Monitora gravità e cronologia, con un conto alla rovescia per la scadenza di notifica alle autorità che parte dal momento in cui l'incidente viene registrato.",
                "Volg ernst en tijdlijn, met een deadlineklok voor de melding aan de toezichthouder die loopt vanaf het moment dat een incident wordt vastgelegd."),
            "Attestations": _t(
                "Attestations", "Attestierungen", "Certificaciones", "Attestazioni", "Attestaties"),
            "Run sign-off campaigns that collect signatures and issue certificates when each attestation completes.": _t(
                "Lancez des campagnes de validation qui recueillent les signatures et délivrent des certificats à la clôture de chaque attestation.",
                "Führen Sie Freigabe-Kampagnen durch, die Unterschriften sammeln und Zertifikate ausstellen, sobald jede Attestierung abgeschlossen ist.",
                "Ejecute campañas de aprobación que recojan firmas y emitan certificados al completarse cada certificación.",
                "Avvia campagne di sign-off che raccolgono le firme ed emettono certificati al completamento di ogni attestazione.",
                "Voer sign-off-campagnes uit die handtekeningen verzamelen en certificaten uitgeven zodra elke attestatie is voltooid."),
            "Audit-ready &amp; secure": _t(
                "Prêt pour l'audit &amp; sécurisé", "Prüfbereit &amp; sicher",
                "Listo para auditoría &amp; seguro", "Pronto per l'audit &amp; sicuro",
                "Auditklaar &amp; veilig"),
            "An append-only audit trail, CSV and PDF reports, OIDC single sign-on, API tokens and per-tenant isolation with row-level security — in Arabic and English.": _t(
                "Une piste d'audit en ajout seul, des rapports CSV et PDF, l'authentification unique OIDC, des jetons d'API et une isolation par locataire avec sécurité au niveau des lignes — en arabe et en anglais.",
                "Ein Audit-Trail nur zum Anhängen, CSV- und PDF-Berichte, OIDC-Single-Sign-on, API-Tokens und Mandantentrennung mit Sicherheit auf Zeilenebene — auf Arabisch und Englisch.",
                "Una pista de auditoría de solo anexado, informes CSV y PDF, inicio de sesión único OIDC, tokens de API y aislamiento por inquilino con seguridad a nivel de fila — en árabe e inglés.",
                "Una pista di audit solo in aggiunta, report CSV e PDF, single sign-on OIDC, token API e isolamento per tenant con sicurezza a livello di riga — in arabo e inglese.",
                "Een append-only audittrail, CSV- en PDF-rapporten, OIDC-eenmalige aanmelding, API-tokens en isolatie per tenant met beveiliging op rijniveau — in het Arabisch en Engels."),
            # ---- 03 · Built for ----
            "03 · Built for": _t("03 · Conçu pour", "03 · Entwickelt für", "03 · Diseñado para", "03 · Pensato per", "03 · Gebouwd voor"),
            "For the people who answer to the regulator.": _t(
                "Pour celles et ceux qui répondent devant le régulateur.",
                "Für die Menschen, die der Aufsichtsbehörde Rechenschaft schulden.",
                "Para quienes responden ante el regulador.",
                "Per chi deve rispondere all'autorità di vigilanza.",
                "Voor de mensen die verantwoording afleggen aan de toezichthouder."),
            "Compliance &amp; GRC leads": _t(
                "Responsables conformité &amp; GRC", "Compliance- &amp; GRC-Verantwortliche",
                "Responsables de cumplimiento &amp; GRC", "Responsabili compliance &amp; GRC",
                "Compliance- &amp; GRC-leads"),
            "Own the obligation calendar and the control library, and see at a glance what's covered, what's due and what's overdue.": _t(
                "Pilotez le calendrier des obligations et la bibliothèque de contrôles, et voyez d'un coup d'œil ce qui est couvert, ce qui est dû et ce qui est en retard.",
                "Steuern Sie den Pflichtenkalender und die Kontrollbibliothek und sehen Sie auf einen Blick, was abgedeckt, was fällig und was überfällig ist.",
                "Lleve el calendario de obligaciones y la biblioteca de controles, y vea de un vistazo qué está cubierto, qué vence y qué está vencido.",
                "Gestisci il calendario degli obblighi e la libreria dei controlli e vedi a colpo d'occhio cosa è coperto, cosa è in scadenza e cosa è scaduto.",
                "Beheer de verplichtingenkalender en de controlbibliotheek, en zie in één oogopslag wat gedekt is, wat verschuldigd is en wat te laat is."),
            "Risk owners": _t(
                "Propriétaires de risques", "Risikoverantwortliche", "Propietarios de riesgos",
                "Titolari dei rischi", "Risico-eigenaren"),
            "Score and treat risk in one register, with residual ratings and acceptances that don't quietly expire.": _t(
                "Notez et traitez le risque dans un seul registre, avec des notations résiduelles et des acceptations qui n'expirent pas en silence.",
                "Bewerten und behandeln Sie Risiken in einem Register, mit Restbewertungen und Akzeptanzen, die nicht klammheimlich verfallen.",
                "Puntúe y trate el riesgo en un solo registro, con valoraciones residuales y aceptaciones que no caducan en silencio.",
                "Valuta e tratta il rischio in un unico registro, con valutazioni residue e accettazioni che non scadono in silenzio.",
                "Scoor en behandel risico in één register, met residuele beoordelingen en accepteringen die niet stilletjes verlopen."),
            "Security &amp; IT teams": _t(
                "Équipes sécurité &amp; informatique", "Sicherheits- &amp; IT-Teams",
                "Equipos de seguridad &amp; TI", "Team sicurezza &amp; IT",
                "Beveiligings- &amp; IT-teams"),
            "Turn posture findings and incidents into tracked work with deadlines, mapped straight to the controls they affect.": _t(
                "Transformez les constats de posture et les incidents en travail suivi avec échéances, directement relié aux contrôles concernés.",
                "Verwandeln Sie Posture-Funde und Vorfälle in nachverfolgte Arbeit mit Fristen, direkt den betroffenen Kontrollen zugeordnet.",
                "Convierta los hallazgos de postura y los incidentes en trabajo con seguimiento y plazos, vinculado directamente a los controles que afectan.",
                "Trasforma i rilievi di postura e gli incidenti in attività tracciate con scadenze, collegate direttamente ai controlli che toccano.",
                "Zet postuurbevindingen en incidenten om in gevolgd werk met deadlines, direct gekoppeld aan de controls die ze raken."),
            "Internal audit": _t(
                "Audit interne", "Interne Revision", "Auditoría interna",
                "Audit interno", "Interne audit"),
            "Pull the evidence, the crosswalk and the append-only trail you need to test controls and sign off with confidence.": _t(
                "Extrayez les preuves, la correspondance et la piste en ajout seul dont vous avez besoin pour tester les contrôles et valider en toute confiance.",
                "Rufen Sie die Nachweise, den Crosswalk und den Append-only-Trail ab, die Sie brauchen, um Kontrollen zu testen und mit Zuversicht abzuzeichnen.",
                "Extraiga las evidencias, la correspondencia y la pista de solo anexado que necesita para probar controles y dar el visto bueno con confianza.",
                "Estrai le evidenze, la crosswalk e la pista solo in aggiunta che ti servono per testare i controlli e approvare con fiducia.",
                "Haal het bewijs, de crosswalk en de append-only-trail op die u nodig hebt om controls te testen en met vertrouwen af te tekenen."),
            # ---- 04 · Your region ----
            "04 · Your region": _t("04 · Votre région", "04 · Ihre Region", "04 · Su región", "04 · La tua regione", "04 · Uw regio"),
            "Built for Saudi regulation.": _t(
                "Conçu pour la réglementation saoudienne.",
                "Gebaut für die saudische Regulierung.",
                "Diseñado para la regulación saudí.",
                "Costruito per la normativa saudita.",
                "Gebouwd voor Saoedische regelgeving."),
            "Assure's obligation catalog is mapped to the Kingdom's regulators and law, so the controls, the calendar and the evidence all speak to KSA compliance out of the box.": _t(
                "Le catalogue d'obligations d'Assure est relié aux régulateurs et au droit du Royaume, de sorte que les contrôles, le calendrier et les preuves répondent d'emblée à la conformité en Arabie saoudite.",
                "Der Pflichtenkatalog von Assure ist den Aufsichtsbehörden und dem Recht des Königreichs zugeordnet, sodass Kontrollen, Kalender und Nachweise von Anfang an auf die Compliance in Saudi-Arabien ausgerichtet sind.",
                "El catálogo de obligaciones de Assure está vinculado a los reguladores y la legislación del Reino, de modo que los controles, el calendario y las evidencias responden desde el primer momento al cumplimiento en Arabia Saudí.",
                "Il catalogo degli obblighi di Assure è collegato alle autorità e alla legge del Regno, così controlli, calendario ed evidenze parlano fin da subito alla conformità in Arabia Saudita.",
                "De verplichtingencatalogus van Assure is gekoppeld aan de toezichthouders en wetgeving van het Koninkrijk, zodat de controls, de kalender en het bewijs direct aansluiten op compliance in KSA."),
            "Saudi regulators, pre-mapped": _t(
                "Régulateurs saoudiens, déjà reliés", "Saudische Aufsichtsbehörden, vorab zugeordnet",
                "Reguladores saudíes, ya vinculados", "Autorità saudite, già mappate",
                "Saoedische toezichthouders, vooraf gekoppeld"),
            "Obligations for NCA ECC-2, PDPL, CMA Corporate Governance and the Companies Law arrive already mapped to controls, ready to apply per legal entity.": _t(
                "Les obligations de NCA ECC-2, PDPL, la gouvernance d'entreprise de la CMA et la loi sur les sociétés arrivent déjà reliées aux contrôles, prêtes à être appliquées par entité juridique.",
                "Die Pflichten aus NCA ECC-2, PDPL, CMA Corporate Governance und dem Gesellschaftsrecht kommen bereits den Kontrollen zugeordnet und sind bereit zur Anwendung je Rechtsträger.",
                "Las obligaciones de NCA ECC-2, PDPL, el Gobierno Corporativo de la CMA y la Ley de Sociedades llegan ya vinculadas a los controles, listas para aplicarse por entidad jurídica.",
                "Gli obblighi di NCA ECC-2, PDPL, la Corporate Governance della CMA e la legge sulle società arrivano già mappati ai controlli, pronti da applicare per entità giuridica.",
                "De verplichtingen voor NCA ECC-2, PDPL, CMA Corporate Governance en de vennootschapswet komen al gekoppeld aan controls, klaar om per rechtspersoon toe te passen."),
            "Hijri &amp; Gregorian calendars": _t(
                "Calendriers hégirien &amp; grégorien", "Hidschri- &amp; gregorianischer Kalender",
                "Calendarios hégira &amp; gregoriano", "Calendari islamico &amp; gregoriano",
                "Hijri- &amp; Gregoriaanse kalender"),
            "The obligation engine runs on both calendars, so recurring duties fall due on the dates your regulators actually use.": _t(
                "Le moteur d'obligations fonctionne sur les deux calendriers, de sorte que les tâches récurrentes échoient aux dates que vos régulateurs utilisent réellement.",
                "Die Pflichten-Engine läuft auf beiden Kalendern, sodass wiederkehrende Pflichten an den Daten fällig werden, die Ihre Aufsichtsbehörden tatsächlich verwenden.",
                "El motor de obligaciones funciona en ambos calendarios, de modo que los deberes recurrentes vencen en las fechas que sus reguladores usan realmente.",
                "Il motore degli obblighi funziona su entrambi i calendari, così i doveri ricorrenti scadono nelle date che le tue autorità usano davvero.",
                "De verplichtingen-engine draait op beide kalenders, zodat terugkerende plichten vervallen op de data die uw toezichthouders daadwerkelijk gebruiken."),
            "Arabic &amp; English": _t(
                "Arabe &amp; anglais", "Arabisch &amp; Englisch", "Árabe &amp; inglés",
                "Arabo &amp; inglese", "Arabisch &amp; Engels"),
            "The platform works in Arabic and English throughout, so compliance teams and auditors read the same record in their own language.": _t(
                "La plateforme fonctionne entièrement en arabe et en anglais, de sorte que les équipes de conformité et les auditeurs lisent le même dossier dans leur propre langue.",
                "Die Plattform funktioniert durchgehend auf Arabisch und Englisch, sodass Compliance-Teams und Prüfer denselben Datensatz in ihrer eigenen Sprache lesen.",
                "La plataforma funciona íntegramente en árabe e inglés, de modo que los equipos de cumplimiento y los auditores leen el mismo registro en su propio idioma.",
                "La piattaforma funziona interamente in arabo e inglese, così i team di conformità e gli auditor leggono lo stesso record nella propria lingua.",
                "Het platform werkt volledig in het Arabisch en Engels, zodat compliance-teams en auditors hetzelfde record in hun eigen taal lezen."),
            "Self-hosted in the Kingdom": _t(
                "Auto-hébergé dans le Royaume", "Selbst gehostet im Königreich",
                "Autoalojado en el Reino", "Self-hosted nel Regno",
                "Zelf-gehost in het Koninkrijk"),
            "Assure is self-hosted, so regulated data can stay inside KSA and inside the infrastructure you already trust.": _t(
                "Assure est auto-hébergé, de sorte que les données réglementées peuvent rester en Arabie saoudite et au sein de l'infrastructure à laquelle vous faites déjà confiance.",
                "Assure wird selbst gehostet, sodass regulierte Daten in Saudi-Arabien und innerhalb der Infrastruktur bleiben können, der Sie bereits vertrauen.",
                "Assure es autoalojado, de modo que los datos regulados pueden permanecer en Arabia Saudí y dentro de la infraestructura en la que ya confía.",
                "Assure è self-hosted, così i dati regolamentati possono restare in Arabia Saudita e all'interno dell'infrastruttura di cui ti fidi già.",
                "Assure is zelf-gehost, zodat gereguleerde data binnen KSA en binnen de infrastructuur die u al vertrouwt kan blijven."),
            # ---- 05 · The FulcrumGrid family ----
            "05 · The FulcrumGrid family": _t("05 · La famille FulcrumGrid", "05 · Die FulcrumGrid-Familie", "05 · La familia FulcrumGrid", "05 · La famiglia FulcrumGrid", "05 · De FulcrumGrid-familie"),
            "Explore the rest of the grid.": _t(
                "Découvrez le reste de la grille.", "Entdecken Sie den Rest des Grids.",
                "Explore el resto de la cuadrícula.", "Esplora il resto della griglia.",
                "Ontdek de rest van het grid."),
            "Assure is one of several FulcrumGrid apps, each built to the same standard. Explore the others built for your operations.": _t(
                "Assure est l'une des nombreuses applications FulcrumGrid, chacune conçue selon le même standard. Découvrez les autres, conçues pour vos opérations.",
                "Assure ist eine von mehreren FulcrumGrid-Apps, jede nach demselben Standard gebaut. Entdecken Sie die anderen, gebaut für Ihren Betrieb.",
                "Assure es una de las varias aplicaciones de FulcrumGrid, cada una creada con el mismo estándar. Explore las demás, creadas para sus operaciones.",
                "Assure è una delle diverse app FulcrumGrid, ognuna costruita secondo lo stesso standard. Esplora le altre, costruite per le tue operazioni.",
                "Assure is een van de vele FulcrumGrid-apps, elk gebouwd volgens dezelfde standaard. Ontdek de andere, gebouwd voor uw operatie."),
            "People operations": _t("Gestion du personnel", "Personalmanagement", "Gestión de personas", "Gestione del personale", "Personeelsbeheer"),
            "Operations dashboard": _t("Tableau de bord des opérations", "Betriebs-Dashboard", "Panel de operaciones", "Dashboard operativa", "Operationeel dashboard"),
            "Receivables &amp; payments": _t("Créances &amp; paiements", "Forderungen &amp; Zahlungen", "Cobros &amp; pagos", "Crediti &amp; pagamenti", "Vorderingen &amp; betalingen"),
            "Logistics &amp; finance": _t("Logistique &amp; finances", "Logistik &amp; Finanzen", "Logística &amp; finanzas", "Logistica &amp; finanza", "Logistiek &amp; financiën"),
            "IFRS period-end": _t("Clôture IFRS", "IFRS-Periodenabschluss", "Cierre IFRS", "Chiusura IFRS", "IFRS-periodeafsluiting"),
            "More apps →": _t("Plus d'applications →", "Weitere Apps →", "Más apps →", "Altre app →", "Meer apps →"),
            "Inventory, CRM &amp; more": _t("Inventaire, CRM &amp; plus", "Lagerverwaltung, CRM &amp; mehr", "Inventario, CRM &amp; más", "Inventario, CRM &amp; altro", "Voorraad, CRM &amp; meer"),
            # ---- CTA ----
            "Prove it,<br />don't just claim it.": _t(
                "Prouvez-le,<br />ne vous contentez pas de l'affirmer.",
                "Beweisen Sie es,<br />behaupten Sie es nicht nur.",
                "Demuéstrelo,<br />no se limite a afirmarlo.",
                "Dimostralo,<br />non limitarti a dichiararlo.",
                "Bewijs het,<br />beweer het niet alleen."),
            "See how Assure turns Saudi regulatory obligations into controls, evidence and an audit trail that holds up.": _t(
                "Découvrez comment Assure transforme les obligations réglementaires saoudiennes en contrôles, preuves et piste d'audit qui tiennent la route.",
                "Sehen Sie, wie Assure saudische regulatorische Pflichten in Kontrollen, Nachweise und einen Audit-Trail verwandelt, der standhält.",
                "Vea cómo Assure convierte las obligaciones regulatorias saudíes en controles, evidencias y una pista de auditoría que se sostiene.",
                "Scopri come Assure trasforma gli obblighi normativi sauditi in controlli, evidenze e una pista di audit che regge.",
                "Zie hoe Assure Saoedische regelgevingsverplichtingen omzet in controls, bewijs en een audittrail die standhoudt."),
        },
    },
}
