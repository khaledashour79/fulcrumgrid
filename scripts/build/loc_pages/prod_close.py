# -*- coding: utf-8 -*-
"""Per-page translations for the Close product page.

Keys are EXACT English substrings of the EN source HTML (entities, straight
apostrophes, dashes and glyphs preserved). Brand/product names (FulcrumGrid,
Close, Command Center, Collection, HR Suite, Blog, FAQ), standard/acronym
labels (IFRS, IAS 19, IFRS 9, IFRS 16, SOCPA, PDPL, RTL, ERP, CSV, Excel,
SAP Business One, ISO-4217, SAR, KSA) and code-like tokens are left
untranslated. Common chrome lives in loc_catalog.COMMON, not here.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/products/close/': {
        'src': 'products/close/index.html',
        't': {
            # ---- Meta ----
            "Close — FulcrumGrid": _t(
                "Close — FulcrumGrid", "Close — FulcrumGrid", "Close — FulcrumGrid",
                "Close — FulcrumGrid", "Close — FulcrumGrid"),
            "Close is FulcrumGrid's calculation layer for IFRS period-end estimates — IAS 19, IFRS 9 and IFRS 16 — with frozen inputs, versioned assumptions and reproducible, audit-ready runs for Saudi finance teams.": _t(
                "Close est la couche de calcul de FulcrumGrid pour les estimations IFRS de fin de période — IAS 19, IFRS 9 et IFRS 16 — avec des entrées figées, des hypothèses versionnées et des exécutions reproductibles et prêtes pour l'audit, pour les équipes financières saoudiennes.",
                "Close ist die Berechnungsebene von FulcrumGrid für IFRS-Schätzungen zum Periodenende — IAS 19, IFRS 9 und IFRS 16 — mit eingefrorenen Eingaben, versionierten Annahmen und reproduzierbaren, prüfungsbereiten Läufen für saudische Finanzteams.",
                "Close es la capa de cálculo de FulcrumGrid para las estimaciones IFRS de cierre de periodo — IAS 19, IFRS 9 e IFRS 16 — con entradas congeladas, supuestos versionados y ejecuciones reproducibles y listas para auditoría, para equipos financieros saudíes.",
                "Close è il livello di calcolo di FulcrumGrid per le stime IFRS di fine periodo — IAS 19, IFRS 9 e IFRS 16 — con input congelati, ipotesi versionate ed elaborazioni riproducibili e pronte per la revisione, per i team finanziari sauditi.",
                "Close is de rekenlaag van FulcrumGrid voor IFRS-schattingen bij periodeafsluiting — IAS 19, IFRS 9 en IFRS 16 — met bevroren invoer, geversioneerde aannames en reproduceerbare, auditklare runs voor Saoedische financiële teams."),
            "The calculation layer for IFRS period-end estimates — IAS 19, IFRS 9 and IFRS 16 — with a full audit trail.": _t(
                "La couche de calcul des estimations IFRS de fin de période — IAS 19, IFRS 9 et IFRS 16 — avec une piste d'audit complète.",
                "Die Berechnungsebene für IFRS-Schätzungen zum Periodenende — IAS 19, IFRS 9 und IFRS 16 — mit vollständigem Audit-Trail.",
                "La capa de cálculo para las estimaciones IFRS de cierre de periodo — IAS 19, IFRS 9 e IFRS 16 — con una pista de auditoría completa.",
                "Il livello di calcolo per le stime IFRS di fine periodo — IAS 19, IFRS 9 e IFRS 16 — con una pista di controllo completa.",
                "De rekenlaag voor IFRS-schattingen bij periodeafsluiting — IAS 19, IFRS 9 en IFRS 16 — met een volledig audittrail."),
            # ---- Hero ----
            "Finance · Available now": _t(
                "Finance · Disponible maintenant", "Finanzen · Jetzt verfügbar",
                "Finanzas · Ya disponible", "Finanza · Ora disponibile",
                "Financiën · Nu beschikbaar"),
            "Close the books, with the proof attached.": _t(
                "Clôturez les comptes, preuve à l'appui.",
                "Schließen Sie die Bücher — mit beigefügtem Nachweis.",
                "Cierre los libros, con la prueba adjunta.",
                "Chiudi i conti, con la prova allegata.",
                "Sluit de boeken, met het bewijs erbij."),
            "Close is the calculation layer for your IFRS period-end estimates — IAS 19, IFRS 9 and IFRS 16 — with every input frozen, every assumption evidenced, and every run reproducible down to the hash. A preparer's workspace for Saudi finance teams, built to stand up to an audit.": _t(
                "Close est la couche de calcul de vos estimations IFRS de fin de période — IAS 19, IFRS 9 et IFRS 16 — avec chaque entrée figée, chaque hypothèse justifiée et chaque exécution reproductible jusqu'au hash. Un espace de travail pour le préparateur, destiné aux équipes financières saoudiennes et conçu pour résister à un audit.",
                "Close ist die Berechnungsebene für Ihre IFRS-Schätzungen zum Periodenende — IAS 19, IFRS 9 und IFRS 16 — mit jeder eingefrorenen Eingabe, jeder belegten Annahme und jedem bis auf den Hash reproduzierbaren Lauf. Ein Arbeitsbereich für den Ersteller, für saudische Finanzteams, gebaut, um einer Prüfung standzuhalten.",
                "Close es la capa de cálculo de sus estimaciones IFRS de cierre de periodo — IAS 19, IFRS 9 e IFRS 16 — con cada entrada congelada, cada supuesto justificado y cada ejecución reproducible hasta el hash. Un espacio de trabajo para el preparador, para equipos financieros saudíes, creado para resistir una auditoría.",
                "Close è il livello di calcolo delle tue stime IFRS di fine periodo — IAS 19, IFRS 9 e IFRS 16 — con ogni input congelato, ogni ipotesi documentata e ogni elaborazione riproducibile fino all'hash. Uno spazio di lavoro per chi prepara, per i team finanziari sauditi, costruito per reggere a una revisione.",
                "Close is de rekenlaag voor uw IFRS-schattingen bij periodeafsluiting — IAS 19, IFRS 9 en IFRS 16 — met elke invoer bevroren, elke aanname onderbouwd en elke run reproduceerbaar tot op de hash. Een werkruimte voor de opsteller, voor Saoedische financiële teams, gebouwd om een audit te doorstaan."),
            # ---- 01 · Pricing ----
            "01 · Pricing": _t("01 · Tarifs", "01 · Preise", "01 · Precios", "01 · Prezzi", "01 · Prijzen"),
            "Pricing — talk to sales.": _t(
                "Tarifs — parlez-en aux ventes.",
                "Preise — sprechen Sie mit dem Vertrieb.",
                "Precios — hable con ventas.",
                "Prezzi — parla con le vendite.",
                "Prijzen — praat met sales."),
            "Close has no public price. We scope it to your reporting entities and your close, then quote it.": _t(
                "Close n'a pas de prix public. Nous en définissons le périmètre selon vos entités déclarantes et votre clôture, puis nous établissons un devis.",
                "Close hat keinen öffentlichen Preis. Wir schneiden ihn auf Ihre berichtenden Einheiten und Ihren Abschluss zu und erstellen dann ein Angebot.",
                "Close no tiene precio público. Definimos su alcance según sus entidades informantes y su cierre, y luego lo presupuestamos.",
                "Close non ha un prezzo pubblico. Ne definiamo l'ambito in base alle tue entità che redigono il bilancio e alla tua chiusura, poi lo preventiviamo.",
                "Close heeft geen openbare prijs. We bepalen de scope op basis van uw rapporterende entiteiten en uw afsluiting en brengen dan een offerte uit."),
            "<h4>Close</h4>": _t("<h4>Close</h4>", "<h4>Close</h4>", "<h4>Close</h4>", "<h4>Close</h4>", "<h4>Close</h4>"),
            "Priced per engagement": _t(
                "Tarifé par mission", "Preis pro Mandat", "Precio por encargo",
                "Prezzo per incarico", "Prijs per opdracht"),
            "Talk to sales ↗": _t(
                "Parler aux ventes ↗", "Mit dem Vertrieb sprechen ↗", "Hablar con ventas ↗",
                "Parla con le vendite ↗", "Praat met sales ↗"),
            "Talk to sales": _t(
                "Parler aux ventes", "Mit dem Vertrieb sprechen", "Hablar con ventas",
                "Parla con le vendite", "Praat met sales"),
            "No published price yet. Tell us how you close and we'll put a number to it.": _t(
                "Pas encore de prix publié. Dites-nous comment vous clôturez et nous y mettrons un chiffre.",
                "Noch kein veröffentlichter Preis. Sagen Sie uns, wie Sie abschließen, und wir nennen eine Zahl.",
                "Aún no hay precio publicado. Cuéntenos cómo cierra y le pondremos una cifra.",
                "Nessun prezzo pubblicato ancora. Dicci come chiudi e gli daremo un numero.",
                "Nog geen gepubliceerde prijs. Vertel ons hoe u afsluit en we zetten er een bedrag op."),
            "What a demo covers": _t(
                "Ce que couvre une démo", "Was eine Demo abdeckt", "Qué cubre una demo",
                "Cosa copre una demo", "Wat een demo behandelt"),
            "In one short call": _t(
                "En un court appel", "In einem kurzen Gespräch", "En una breve llamada",
                "In una breve chiamata", "In één kort gesprek"),
            "Your period-end estimates": _t(
                "Vos estimations de fin de période", "Ihre Schätzungen zum Periodenende",
                "Sus estimaciones de cierre de periodo", "Le tue stime di fine periodo",
                "Uw schattingen bij periodeafsluiting"),
            "The audit pack and sign-off trail": _t(
                "Le dossier d'audit et la piste d'approbation", "Das Prüfungspaket und der Freigabe-Trail",
                "El paquete de auditoría y la pista de aprobación", "Il pacchetto di revisione e la pista delle approvazioni",
                "Het auditpakket en het goedkeuringsspoor"),
            "How a run stays reproducible": _t(
                "Comment une exécution reste reproductible", "Wie ein Lauf reproduzierbar bleibt",
                "Cómo una ejecución sigue siendo reproducible", "Come un'elaborazione resta riproducibile",
                "Hoe een run reproduceerbaar blijft"),
            "Fit for your reporting entities": _t(
                "L'adéquation à vos entités déclarantes", "Die Eignung für Ihre berichtenden Einheiten",
                "La adecuación a sus entidades informantes", "L'idoneità per le tue entità che redigono il bilancio",
                "De geschiktheid voor uw rapporterende entiteiten"),
            # ---- 02 · Capabilities ----
            "02 · Capabilities": _t("02 · Capacités", "02 · Funktionen", "02 · Capacidades", "02 · Funzionalità", "02 · Mogelijkheden"),
            "IFRS estimates, built to be proven.": _t(
                "Des estimations IFRS, conçues pour être prouvées.",
                "IFRS-Schätzungen, gebaut, um belegt zu werden.",
                "Estimaciones IFRS, creadas para ser demostradas.",
                "Stime IFRS, costruite per essere dimostrate.",
                "IFRS-schattingen, gebouwd om te worden bewezen."),
            "Every period-end calculation, from a frozen input to a signed-off audit pack.": _t(
                "Chaque calcul de fin de période, d'une entrée figée à un dossier d'audit approuvé.",
                "Jede Berechnung zum Periodenende, von einer eingefrorenen Eingabe bis zum freigegebenen Prüfungspaket.",
                "Cada cálculo de cierre de periodo, desde una entrada congelada hasta un paquete de auditoría aprobado.",
                "Ogni calcolo di fine periodo, da un input congelato a un pacchetto di revisione approvato.",
                "Elke berekening bij periodeafsluiting, van een bevroren invoer tot een goedgekeurd auditpakket."),
            "IFRS period-end engines": _t(
                "Moteurs IFRS de fin de période", "IFRS-Engines zum Periodenende",
                "Motores IFRS de cierre de periodo", "Motori IFRS di fine periodo",
                "IFRS-engines voor periodeafsluiting"),
            "IAS 19 end-of-service benefits, IFRS 9 expected credit loss and IFRS 16 leases, in one workspace.": _t(
                "Indemnités de fin de service IAS 19, perte de crédit attendue IFRS 9 et contrats de location IFRS 16, dans un seul espace de travail.",
                "IAS-19-Leistungen bei Dienstende, erwarteter Kreditverlust nach IFRS 9 und Leasingverhältnisse nach IFRS 16, in einem Arbeitsbereich.",
                "Beneficios por fin de servicio IAS 19, pérdida crediticia esperada IFRS 9 y arrendamientos IFRS 16, en un solo espacio de trabajo.",
                "Benefici di fine servizio IAS 19, perdita attesa su crediti IFRS 9 e leasing IFRS 16, in un unico spazio di lavoro.",
                "IAS 19-vergoedingen bij einde dienstverband, verwacht kredietverlies volgens IFRS 9 en leases volgens IFRS 16, in één werkruimte."),
            "Controlled close": _t(
                "Clôture contrôlée", "Kontrollierter Abschluss", "Cierre controlado",
                "Chiusura controllata", "Gecontroleerde afsluiting"),
            "Open, review and lock each reporting period; reopening needs a second approver and a logged reason.": _t(
                "Ouvrez, examinez et verrouillez chaque période de reporting ; la réouverture exige un second approbateur et un motif consigné.",
                "Öffnen, prüfen und sperren Sie jede Berichtsperiode; die Wiedereröffnung erfordert einen zweiten Genehmiger und einen protokollierten Grund.",
                "Abra, revise y bloquee cada periodo de informe; la reapertura exige un segundo aprobador y un motivo registrado.",
                "Apri, verifica e blocca ogni periodo di rendicontazione; la riapertura richiede un secondo approvatore e un motivo registrato.",
                "Open, controleer en vergrendel elke rapportageperiode; heropenen vereist een tweede goedkeurder en een gelogde reden."),
            "Frozen input snapshots": _t(
                "Instantanés d'entrées figés", "Eingefrorene Eingabe-Snapshots",
                "Instantáneas de entradas congeladas", "Snapshot di input congelati",
                "Bevroren invoer-snapshots"),
            "Source data is validated and frozen with a content hash, so a later change to the source never alters a past result.": _t(
                "Les données source sont validées et figées avec un hash de contenu, de sorte qu'une modification ultérieure de la source n'altère jamais un résultat passé.",
                "Quelldaten werden validiert und mit einem Inhalts-Hash eingefroren, sodass eine spätere Änderung an der Quelle ein vergangenes Ergebnis nie verändert.",
                "Los datos de origen se validan y congelan con un hash de contenido, de modo que un cambio posterior en el origen nunca altera un resultado pasado.",
                "I dati di origine vengono convalidati e congelati con un hash del contenuto, così una modifica successiva alla fonte non altera mai un risultato passato.",
                "Brongegevens worden gevalideerd en bevroren met een content-hash, zodat een latere wijziging aan de bron nooit een eerder resultaat verandert."),
            "Versioned assumptions with evidence": _t(
                "Hypothèses versionnées avec justificatifs", "Versionierte Annahmen mit Nachweisen",
                "Supuestos versionados con evidencias", "Ipotesi versionate con prove",
                "Geversioneerde aannames met bewijs"),
            "Every discount rate or growth assumption carries a rationale and an attached evidence file, and must be approved before it's used.": _t(
                "Chaque taux d'actualisation ou hypothèse de croissance s'accompagne d'une justification et d'un fichier de preuve joint, et doit être approuvé avant d'être utilisé.",
                "Jeder Abzinsungssatz und jede Wachstumsannahme trägt eine Begründung und eine angehängte Nachweisdatei und muss vor der Verwendung genehmigt werden.",
                "Cada tasa de descuento o supuesto de crecimiento lleva una justificación y un archivo de evidencia adjunto, y debe aprobarse antes de usarse.",
                "Ogni tasso di sconto o ipotesi di crescita porta con sé una motivazione e un file di prova allegato, e deve essere approvato prima dell'uso.",
                "Elke disconteringsvoet of groeiaanname draagt een onderbouwing en een bijgevoegd bewijsbestand, en moet worden goedgekeurd voordat hij wordt gebruikt."),
            "Reproducible runs": _t(
                "Exécutions reproductibles", "Reproduzierbare Läufe", "Ejecuciones reproducibles",
                "Elaborazioni riproducibili", "Reproduceerbare runs"),
            "Every calculation re-runs to a byte-identical result hash, provable to an auditor.": _t(
                "Chaque calcul se réexécute vers un hash de résultat identique octet par octet, démontrable à un auditeur.",
                "Jede Berechnung läuft erneut zu einem byte-identischen Ergebnis-Hash, einem Prüfer nachweisbar.",
                "Cada cálculo se reejecuta hasta un hash de resultado idéntico byte a byte, demostrable ante un auditor.",
                "Ogni calcolo viene rielaborato fino a un hash del risultato identico byte per byte, dimostrabile a un revisore.",
                "Elke berekening draait opnieuw naar een byte-identieke resultaat-hash, aantoonbaar aan een auditor."),
            "Segregation of duties": _t(
                "Séparation des tâches", "Funktionstrennung", "Separación de funciones",
                "Separazione dei compiti", "Functiescheiding"),
            "The same person can't both prepare and approve an estimate.": _t(
                "La même personne ne peut pas à la fois préparer et approuver une estimation.",
                "Dieselbe Person kann eine Schätzung nicht zugleich erstellen und genehmigen.",
                "La misma persona no puede preparar y aprobar una estimación a la vez.",
                "La stessa persona non può sia preparare sia approvare una stima.",
                "Dezelfde persoon kan een schatting niet zowel opstellen als goedkeuren."),
            "External actuary sign-off": _t(
                "Approbation par un actuaire externe", "Freigabe durch externen Aktuar",
                "Aprobación de un actuario externo", "Approvazione di un attuario esterno",
                "Goedkeuring door externe actuaris"),
            "IAS 19 runs carry a dedicated actuary review and sign-off stage.": _t(
                "Les exécutions IAS 19 comportent une étape dédiée de revue et d'approbation par un actuaire.",
                "IAS-19-Läufe enthalten eine eigene Phase für die Prüfung und Freigabe durch einen Aktuar.",
                "Las ejecuciones IAS 19 incluyen una etapa dedicada de revisión y aprobación por un actuario.",
                "Le elaborazioni IAS 19 prevedono una fase dedicata di revisione e approvazione di un attuario.",
                "IAS 19-runs bevatten een aparte fase voor beoordeling en goedkeuring door een actuaris."),
            "Tracked adjustments": _t(
                "Ajustements tracés", "Nachverfolgte Anpassungen", "Ajustes trazados",
                "Rettifiche tracciate", "Getraceerde aanpassingen"),
            "Manual overrides are recorded as separate lines with a reason and an approver, never typed over the computed figures.": _t(
                "Les ajustements manuels sont enregistrés comme des lignes distinctes avec un motif et un approbateur, jamais saisis par-dessus les chiffres calculés.",
                "Manuelle Übersteuerungen werden als separate Zeilen mit Grund und Genehmiger erfasst, nie über die berechneten Zahlen geschrieben.",
                "Las anulaciones manuales se registran como líneas separadas con un motivo y un aprobador, nunca escritas encima de las cifras calculadas.",
                "Le forzature manuali sono registrate come righe separate con un motivo e un approvatore, mai digitate sopra le cifre calcolate.",
                "Handmatige overschrijvingen worden vastgelegd als aparte regels met een reden en een goedkeurder, nooit over de berekende cijfers heen getypt."),
            "Draft journal vouchers": _t(
                "Pièces comptables provisoires", "Buchungsbelege im Entwurf", "Comprobantes de diario en borrador",
                "Bozze di registrazioni contabili", "Concept-journaalposten"),
            "Balanced, tie-to-results journals exported as CSV or Excel for your ERP.": _t(
                "Des écritures équilibrées, rapprochées aux résultats, exportées en CSV ou Excel pour votre ERP.",
                "Ausgeglichene, mit den Ergebnissen abgestimmte Buchungen, als CSV oder Excel für Ihr ERP exportiert.",
                "Asientos equilibrados y conciliados con los resultados, exportados como CSV o Excel para su ERP.",
                "Registrazioni bilanciate e riconciliate con i risultati, esportate in CSV o Excel per il tuo ERP.",
                "Sluitende, op de resultaten aansluitende boekingen, geëxporteerd als CSV of Excel voor uw ERP."),
            "One-click audit pack": _t(
                "Dossier d'audit en un clic", "Prüfungspaket mit einem Klick", "Paquete de auditoría con un clic",
                "Pacchetto di revisione con un clic", "Auditpakket met één klik"),
            "A bilingual Excel pack per run — inputs, assumptions, workings, sensitivities and the sign-off trail — with a hash manifest.": _t(
                "Un dossier Excel bilingue par exécution — entrées, hypothèses, calculs, sensibilités et piste d'approbation — avec un manifeste de hash.",
                "Ein zweisprachiges Excel-Paket je Lauf — Eingaben, Annahmen, Berechnungen, Sensitivitäten und Freigabe-Trail — mit einem Hash-Manifest.",
                "Un paquete Excel bilingüe por ejecución — entradas, supuestos, cálculos, sensibilidades y pista de aprobación — con un manifiesto de hash.",
                "Un pacchetto Excel bilingue per elaborazione — input, ipotesi, calcoli, sensibilità e pista delle approvazioni — con un manifest di hash.",
                "Een tweetalig Excel-pakket per run — invoer, aannames, berekeningen, gevoeligheden en het goedkeuringsspoor — met een hash-manifest."),
            "PDPL-grade access control": _t(
                "Contrôle d'accès de niveau PDPL", "Zugriffskontrolle auf PDPL-Niveau", "Control de acceso de nivel PDPL",
                "Controllo degli accessi a livello PDPL", "Toegangscontrole op PDPL-niveau"),
            "Every view, export or download of personal data is gated and written to an append-only access log.": _t(
                "Chaque consultation, export ou téléchargement de données personnelles est contrôlé et inscrit dans un journal d'accès en ajout seul.",
                "Jede Ansicht, jeder Export und jeder Download personenbezogener Daten ist abgesichert und wird in ein reines Anfüge-Zugriffsprotokoll geschrieben.",
                "Cada visualización, exportación o descarga de datos personales está controlada y se registra en un log de acceso de solo adición.",
                "Ogni visualizzazione, esportazione o download di dati personali è protetto e registrato in un log di accesso a sola aggiunta.",
                "Elke weergave, export of download van persoonsgegevens is afgeschermd en wordt weggeschreven naar een alleen-toevoegen toegangslog."),
            "Arabic-first, RTL": _t(
                "L'arabe d'abord, RTL", "Arabisch zuerst, RTL", "Árabe primero, RTL",
                "Arabo prima di tutto, RTL", "Arabisch-eerst, RTL"),
            "The whole workspace is built right-to-left, with full Arabic and English and multi-currency (ISO-4217, SAR default).": _t(
                "Tout l'espace de travail est conçu de droite à gauche, avec l'arabe et l'anglais complets et le multidevise (ISO-4217, SAR par défaut).",
                "Der gesamte Arbeitsbereich ist rechts-nach-links aufgebaut, mit vollständigem Arabisch und Englisch und Multi-Währung (ISO-4217, SAR als Standard).",
                "Todo el espacio de trabajo está construido de derecha a izquierda, con árabe e inglés completos y multidivisa (ISO-4217, SAR por defecto).",
                "L'intero spazio di lavoro è costruito da destra a sinistra, con arabo e inglese completi e multivaluta (ISO-4217, SAR come predefinita).",
                "De hele werkruimte is rechts-naar-links opgebouwd, met volledig Arabisch en Engels en multivaluta (ISO-4217, SAR als standaard)."),
            # ---- 03 · Built for ----
            "03 · Built for": _t("03 · Conçu pour", "03 · Entwickelt für", "03 · Diseñado para", "03 · Pensato per", "03 · Gebouwd voor"),
            "Built for the preparer's chair.": _t(
                "Conçu pour le fauteuil du préparateur.",
                "Gebaut für den Stuhl des Erstellers.",
                "Diseñado para la silla del preparador.",
                "Pensato per chi prepara il bilancio.",
                "Gebouwd voor de stoel van de opsteller."),
            "Finance teams": _t(
                "Équipes financières", "Finanzteams", "Equipos financieros",
                "Team finanziari", "Financiële teams"),
            "Prepare IAS 19, IFRS 9 and IFRS 16 estimates for KSA listed and public-interest companies, ready for review.": _t(
                "Préparez les estimations IAS 19, IFRS 9 et IFRS 16 pour les sociétés cotées et d'intérêt public d'Arabie saoudite (KSA), prêtes pour la revue.",
                "Erstellen Sie IAS-19-, IFRS-9- und IFRS-16-Schätzungen für börsennotierte und im öffentlichen Interesse stehende Unternehmen in Saudi-Arabien (KSA), bereit zur Prüfung.",
                "Prepare las estimaciones IAS 19, IFRS 9 e IFRS 16 para empresas cotizadas y de interés público de Arabia Saudí (KSA), listas para su revisión.",
                "Prepara le stime IAS 19, IFRS 9 e IFRS 16 per le società quotate e di interesse pubblico dell'Arabia Saudita (KSA), pronte per la revisione.",
                "Stel IAS 19-, IFRS 9- en IFRS 16-schattingen op voor beursgenoteerde en organisaties van openbaar belang in Saoedi-Arabië (KSA), klaar voor beoordeling."),
            "Group controllers": _t(
                "Contrôleurs de groupe", "Konzerncontroller", "Controllers de grupo",
                "Controller di gruppo", "Groepscontrollers"),
            "Consolidate period-end estimates across entities with one lock, one trail and one audit pack.": _t(
                "Consolidez les estimations de fin de période entre entités avec un seul verrou, une seule piste et un seul dossier d'audit.",
                "Konsolidieren Sie Schätzungen zum Periodenende über Einheiten hinweg mit einer Sperre, einem Trail und einem Prüfungspaket.",
                "Consolide las estimaciones de cierre de periodo entre entidades con un solo bloqueo, una sola pista y un solo paquete de auditoría.",
                "Consolida le stime di fine periodo tra le entità con un solo blocco, un'unica pista e un unico pacchetto di revisione.",
                "Consolideer schattingen bij periodeafsluiting over entiteiten heen met één vergrendeling, één spoor en één auditpakket."),
            "IFRS reporting": _t(
                "Reporting IFRS", "IFRS-Berichterstattung", "Información financiera IFRS",
                "Reporting IFRS", "IFRS-rapportage"),
            "Hand your auditor reproducible numbers and a full evidence trail instead of a folder of spreadsheets.": _t(
                "Remettez à votre auditeur des chiffres reproductibles et une piste de preuves complète au lieu d'un dossier de tableurs.",
                "Übergeben Sie Ihrem Prüfer reproduzierbare Zahlen und einen vollständigen Nachweis-Trail statt eines Ordners voller Tabellen.",
                "Entregue a su auditor cifras reproducibles y una pista de evidencias completa en lugar de una carpeta de hojas de cálculo.",
                "Consegna al tuo revisore numeri riproducibili e una pista di prove completa invece di una cartella di fogli di calcolo.",
                "Geef uw auditor reproduceerbare cijfers en een volledig bewijsspoor in plaats van een map vol spreadsheets."),
            # ---- 04 · Your region ----
            "04 · Your region": _t("04 · Votre région", "04 · Ihre Region", "04 · Su región", "04 · La tua regione", "04 · Uw regio"),
            "Built for Saudi Arabia.": _t(
                "Conçu pour l'Arabie saoudite.", "Für Saudi-Arabien gebaut.", "Diseñado para Arabia Saudí.",
                "Costruito per l'Arabia Saudita.", "Gebouwd voor Saoedi-Arabië."),
            "SOCPA-endorsed IFRS, Arabic-first, and multi-currency — Close works the way KSA finance works.": _t(
                "IFRS adoptées par la SOCPA, l'arabe d'abord et le multidevise — Close fonctionne comme la finance en KSA.",
                "Von SOCPA anerkannte IFRS, Arabisch zuerst und Multi-Währung — Close arbeitet so, wie das Finanzwesen in KSA arbeitet.",
                "IFRS avaladas por la SOCPA, árabe primero y multidivisa — Close funciona como funcionan las finanzas en KSA.",
                "IFRS approvati dalla SOCPA, arabo prima di tutto e multivaluta — Close funziona come funziona la finanza in KSA.",
                "Door SOCPA onderschreven IFRS, Arabisch-eerst en multivaluta — Close werkt zoals financiën in KSA werkt."),
            "SOCPA-endorsed IFRS": _t(
                "IFRS adoptées par la SOCPA", "Von SOCPA anerkannte IFRS", "IFRS avaladas por la SOCPA",
                "IFRS approvati dalla SOCPA", "Door SOCPA onderschreven IFRS"),
            "Built for the IFRS standards as endorsed by SOCPA for Saudi reporting entities.": _t(
                "Conçu pour les normes IFRS telles qu'adoptées par la SOCPA pour les entités déclarantes saoudiennes.",
                "Gebaut für die IFRS-Standards, wie von SOCPA für saudische berichtende Einheiten anerkannt.",
                "Diseñado para las normas IFRS tal como las avala la SOCPA para las entidades informantes saudíes.",
                "Costruito per gli standard IFRS come approvati dalla SOCPA per le entità saudite che redigono il bilancio.",
                "Gebouwd voor de IFRS-standaarden zoals onderschreven door SOCPA voor Saoedische rapporterende entiteiten."),
            "Arabic-first, right-to-left": _t(
                "L'arabe d'abord, de droite à gauche", "Arabisch zuerst, rechts nach links",
                "Árabe primero, de derecha a izquierda", "Arabo prima di tutto, da destra a sinistra",
                "Arabisch-eerst, rechts-naar-links"),
            "The whole workspace runs right-to-left, in full Arabic and English.": _t(
                "Tout l'espace de travail fonctionne de droite à gauche, en arabe et en anglais complets.",
                "Der gesamte Arbeitsbereich läuft rechts-nach-links, in vollständigem Arabisch und Englisch.",
                "Todo el espacio de trabajo funciona de derecha a izquierda, en árabe e inglés completos.",
                "L'intero spazio di lavoro funziona da destra a sinistra, in arabo e inglese completi.",
                "De hele werkruimte werkt rechts-naar-links, in volledig Arabisch en Engels."),
            "Multi-currency": _t(
                "Multidevise", "Multi-Währung", "Multidivisa", "Multivaluta", "Multivaluta"),
            "Figures carry their own ISO-4217 currency, with SAR as the default.": _t(
                "Les montants portent leur propre devise ISO-4217, avec le SAR par défaut.",
                "Beträge tragen ihre eigene ISO-4217-Währung, mit SAR als Standard.",
                "Las cifras llevan su propia divisa ISO-4217, con SAR por defecto.",
                "Gli importi portano la propria valuta ISO-4217, con SAR come predefinita.",
                "Bedragen dragen hun eigen ISO-4217-valuta, met SAR als standaard."),
            "Hands off to your ERP": _t(
                "Passe le relais à votre ERP", "Übergibt an Ihr ERP", "Pasa el relevo a su ERP",
                "Passa il testimone al tuo ERP", "Draagt over aan uw ERP"),
            "Draft journal vouchers export as CSV or Excel for SAP Business One or any ledger — Close prepares, your ERP posts.": _t(
                "Les pièces comptables provisoires s'exportent en CSV ou Excel pour SAP Business One ou tout grand livre — Close prépare, votre ERP comptabilise.",
                "Buchungsbelege im Entwurf lassen sich als CSV oder Excel für SAP Business One oder jedes Hauptbuch exportieren — Close erstellt, Ihr ERP bucht.",
                "Los comprobantes de diario en borrador se exportan como CSV o Excel para SAP Business One o cualquier libro mayor — Close prepara, su ERP contabiliza.",
                "Le bozze di registrazioni contabili si esportano in CSV o Excel per SAP Business One o qualsiasi partitario — Close prepara, il tuo ERP contabilizza.",
                "Concept-journaalposten exporteren als CSV of Excel voor SAP Business One of elk grootboek — Close bereidt voor, uw ERP boekt."),
            # ---- 05 · The FulcrumGrid family ----
            "05 · The FulcrumGrid family": _t(
                "05 · La famille FulcrumGrid", "05 · Die FulcrumGrid-Familie", "05 · La familia FulcrumGrid",
                "05 · La famiglia FulcrumGrid", "05 · De FulcrumGrid-familie"),
            "Explore the rest of the grid.": _t(
                "Découvrez le reste de la grille.", "Entdecken Sie den Rest des Grids.",
                "Explore el resto de la cuadrícula.", "Esplora il resto della griglia.",
                "Ontdek de rest van het grid."),
            "Close is one of several FulcrumGrid apps, each built to the same standard. Explore the others built for your operations.": _t(
                "Close est l'une des nombreuses applications FulcrumGrid, chacune conçue selon le même standard. Découvrez les autres, conçues pour vos opérations.",
                "Close ist eine von mehreren FulcrumGrid-Apps, jede nach demselben Standard gebaut. Entdecken Sie die anderen, gebaut für Ihren Betrieb.",
                "Close es una de las varias aplicaciones de FulcrumGrid, cada una creada con el mismo estándar. Explore las demás, creadas para sus operaciones.",
                "Close è una delle diverse app FulcrumGrid, ognuna costruita secondo lo stesso standard. Esplora le altre, costruite per le tue operazioni.",
                "Close is een van de vele FulcrumGrid-apps, elk gebouwd volgens dezelfde standaard. Ontdek de andere, gebouwd voor uw operatie."),
            "People operations": _t(
                "Gestion du personnel", "Personalmanagement", "Gestión de personas",
                "Gestione del personale", "Personeelsbeheer"),
            "Operations dashboard": _t(
                "Tableau de bord des opérations", "Betriebs-Dashboard", "Panel de operaciones",
                "Dashboard operativa", "Operationeel dashboard"),
            "Receivables &amp; payments": _t(
                "Créances &amp; paiements", "Forderungen &amp; Zahlungen", "Cobros &amp; pagos",
                "Crediti &amp; pagamenti", "Vorderingen &amp; betalingen"),
            "More apps →": _t(
                "Plus d'applications →", "Weitere Apps →", "Más apps →", "Altre app →", "Meer apps →"),
            "Inventory, CRM &amp; more": _t(
                "Inventaire, CRM &amp; plus", "Lagerverwaltung, CRM &amp; mehr", "Inventario, CRM &amp; más",
                "Inventario, CRM &amp; altro", "Voorraad, CRM &amp; meer"),
            # ---- CTA ----
            "Close with confidence.<br />Every period.": _t(
                "Clôturez en confiance.<br />Chaque période.",
                "Schließen Sie mit Zuversicht ab.<br />Jede Periode.",
                "Cierre con confianza.<br />Cada periodo.",
                "Chiudi con fiducia.<br />Ogni periodo.",
                "Sluit af met vertrouwen.<br />Elke periode."),
            "See how Close turns your period-end estimates into numbers your auditor can reproduce.": _t(
                "Voyez comment Close transforme vos estimations de fin de période en chiffres que votre auditeur peut reproduire.",
                "Sehen Sie, wie Close Ihre Schätzungen zum Periodenende in Zahlen verwandelt, die Ihr Prüfer reproduzieren kann.",
                "Vea cómo Close convierte sus estimaciones de cierre de periodo en cifras que su auditor puede reproducir.",
                "Scopri come Close trasforma le tue stime di fine periodo in numeri che il tuo revisore può riprodurre.",
                "Zie hoe Close uw schattingen bij periodeafsluiting omzet in cijfers die uw auditor kan reproduceren."),
        },
    },
}
