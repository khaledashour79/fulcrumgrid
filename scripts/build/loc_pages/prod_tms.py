# -*- coding: utf-8 -*-
"""Per-page translations for the TMS product page.

Keys are EXACT English substrings of the EN source HTML (entities, straight
apostrophes, dashes and glyphs preserved). Brand/product names (FulcrumGrid,
TMS, HR Suite, Command Center, Collection, Blog, FAQ), integration and
technology proper nouns (SAP Business One, Odoo, Oracle, Fusion, OIC, GPS,
SMS, OIDC, REST API) and code/currency labels (GCC, VAT, AR, AP, P&L, 3PL,
3D, SLA, ISO, SAR, AED, USD, CRM, ERP) are left untranslated. Common chrome
lives in loc_catalog.COMMON, not here.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/products/tms/': {
        'src': 'products/tms/index.html',
        't': {
            # ---- Meta ----
            "TMS is FulcrumGrid's logistics-operations and finance suite for GCC businesses — freight forwarding, customs, transport and fleet, container yards, parcel and warehousing, with built-in finance and VAT.": _t(
                "TMS est la suite logistique et financière de FulcrumGrid pour les entreprises du Golfe (GCC) — transit, douane, transport et flotte, parcs à conteneurs, colis et entreposage, avec une finance intégrée et la TVA.",
                "TMS ist die Logistik- und Finanzsuite von FulcrumGrid für Unternehmen in der GCC-Region — Spedition, Zoll, Transport und Flotte, Containeryards, Paket und Lagerhaltung, mit integrierter Finanzbuchhaltung und MwSt.",
                "TMS es la suite de operaciones logísticas y finanzas de FulcrumGrid para empresas del Golfo (GCC) — tránsito, aduanas, transporte y flota, patios de contenedores, paquetería y almacenamiento, con finanzas integradas e IVA.",
                "TMS è la suite di operazioni logistiche e finanza di FulcrumGrid per le aziende del Golfo (GCC) — spedizioni, dogana, trasporto e flotta, piazzali container, pacchi e magazzino, con finanza integrata e IVA.",
                "TMS is de logistiek- en financesuite van FulcrumGrid voor bedrijven in de GCC — expeditie, douane, transport en wagenpark, containeryards, pakketten en opslag, met ingebouwde finance en btw."),
            "A logistics-operations and finance suite for GCC businesses — forwarding, customs, transport, yards, parcel and warehousing, with built-in finance and VAT.": _t(
                "Une suite logistique et financière pour les entreprises du Golfe (GCC) — transit, douane, transport, parcs, colis et entreposage, avec une finance intégrée et la TVA.",
                "Eine Logistik- und Finanzsuite für Unternehmen in der GCC-Region — Spedition, Zoll, Transport, Yards, Paket und Lagerhaltung, mit integrierter Finanzbuchhaltung und MwSt.",
                "Una suite de operaciones logísticas y finanzas para empresas del Golfo (GCC) — tránsito, aduanas, transporte, patios, paquetería y almacenamiento, con finanzas integradas e IVA.",
                "Una suite di operazioni logistiche e finanza per le aziende del Golfo (GCC) — spedizioni, dogana, trasporto, piazzali, pacchi e magazzino, con finanza integrata e IVA.",
                "Een logistiek- en financesuite voor bedrijven in de GCC — expeditie, douane, transport, yards, pakketten en opslag, met ingebouwde finance en btw."),
            # ---- Hero ----
            "Logistics &amp; finance · Available now": _t(
                "Logistique &amp; finance · Disponible maintenant",
                "Logistik &amp; Finanzen · Jetzt verfügbar",
                "Logística &amp; finanzas · Ya disponible",
                "Logistica &amp; finanza · Ora disponibile",
                "Logistiek &amp; finance · Nu beschikbaar"),
            "Run your whole logistics operation — and its books — on one grid.": _t(
                "Pilotez toute votre activité logistique — et sa comptabilité — sur une seule grille.",
                "Steuern Sie Ihren gesamten Logistikbetrieb — und seine Buchhaltung — auf einem Grid.",
                "Gestione toda su operación logística — y su contabilidad — en una sola cuadrícula.",
                "Gestisci tutta la tua operatività logistica — e la sua contabilità — su un'unica griglia.",
                "Run uw hele logistieke operatie — en de boekhouding ervan — op één grid."),
            "FulcrumGrid TMS is a logistics-operations and finance suite for GCC businesses — freight forwarders, transport and fleet operators, container yards and depots, couriers, and 3PL warehouses. Arabic and English, multi-currency, multi-tenant.": _t(
                "FulcrumGrid TMS est une suite d'opérations logistiques et de finance pour les entreprises du Golfe (GCC) — transitaires, opérateurs de transport et de flotte, parcs et dépôts de conteneurs, coursiers et entrepôts 3PL. Arabe et anglais, multidevise, multi-locataire.",
                "FulcrumGrid TMS ist eine Suite für Logistikbetrieb und Finanzen für Unternehmen in der GCC-Region — Spediteure, Transport- und Flottenbetreiber, Containeryards und -depots, Kuriere und 3PL-Lager. Arabisch und Englisch, mehrwährungsfähig, mandantenfähig.",
                "FulcrumGrid TMS es una suite de operaciones logísticas y finanzas para empresas del Golfo (GCC) — transitarios, operadores de transporte y flota, patios y depósitos de contenedores, mensajería y almacenes 3PL. Árabe e inglés, multidivisa, multiinquilino.",
                "FulcrumGrid TMS è una suite di operazioni logistiche e finanza per le aziende del Golfo (GCC) — spedizionieri, operatori di trasporto e flotta, piazzali e depositi container, corrieri e magazzini 3PL. Arabo e inglese, multivaluta, multi-tenant.",
                "FulcrumGrid TMS is een suite voor logistieke operaties en finance voor bedrijven in de GCC — expediteurs, transport- en wagenparkexploitanten, containeryards en -depots, koeriers en 3PL-magazijnen. Arabisch en Engels, multivaluta, multi-tenant."),
            # ---- 01 · Pricing ----
            "Pricing — talk to sales.": _t(
                "Tarifs — parlez à l'équipe commerciale.",
                "Preise — sprechen Sie mit dem Vertrieb.",
                "Precios — hable con ventas.",
                "Prezzi — parla con il commerciale.",
                "Prijzen — praat met sales."),
            "A core Platform + Finance base, with operational modules added on as you need them.": _t(
                "Un socle Platform + Finance au cœur, avec des modules opérationnels ajoutés à mesure que vous en avez besoin.",
                "Ein Kern aus Platform + Finance, mit operativen Modulen, die Sie nach Bedarf hinzufügen.",
                "Una base central de Platform + Finance, con módulos operativos añadidos a medida que los necesita.",
                "Una base centrale Platform + Finance, con moduli operativi aggiunti man mano che ti servono.",
                "Een kern van Platform + Finance, met operationele modules die u toevoegt wanneer u ze nodig hebt."),
            "Platform + Finance base": _t(
                "Socle Platform + Finance",
                "Platform + Finance-Basis",
                "Base Platform + Finance",
                "Base Platform + Finance",
                "Platform + Finance-basis"),
            "The core every tenant runs on — the platform itself and a native finance ledger. Everything else is a module you add.": _t(
                "Le cœur sur lequel tourne chaque locataire — la plateforme elle-même et un grand livre financier natif. Tout le reste est un module que vous ajoutez.",
                "Der Kern, auf dem jeder Mandant läuft — die Plattform selbst und ein natives Finanzbuch. Alles andere ist ein Modul, das Sie hinzufügen.",
                "El núcleo sobre el que funciona cada inquilino — la plataforma en sí y un libro mayor financiero nativo. Todo lo demás es un módulo que añade.",
                "Il nucleo su cui gira ogni tenant — la piattaforma stessa e un libro mastro finanziario nativo. Tutto il resto è un modulo che aggiungi.",
                "De kern waarop elke tenant draait — het platform zelf en een native grootboek. Al het andere is een module die u toevoegt."),
            "Modules you switch on": _t(
                "Des modules que vous activez",
                "Module, die Sie aktivieren",
                "Módulos que activa",
                "Moduli che attivi",
                "Modules die u inschakelt"),
            "Forwarding, Transport, Yard, Parcel, Warehousing, Purchasing &amp; Inventory, Workshop, HR &amp; Payroll and Sales are add-on modules — switch each one on as your operation needs it.": _t(
                "Transit, Transport, Parc, Colis, Entreposage, Achats &amp; Stock, Atelier, RH &amp; Paie et Ventes sont des modules complémentaires — activez chacun quand votre activité en a besoin.",
                "Spedition, Transport, Yard, Paket, Lagerhaltung, Einkauf &amp; Bestand, Werkstatt, HR &amp; Lohn und Vertrieb sind Zusatzmodule — aktivieren Sie jedes, wenn Ihr Betrieb es braucht.",
                "Tránsito, Transporte, Patio, Paquetería, Almacenamiento, Compras &amp; Inventario, Taller, RR. HH. &amp; Nóminas y Ventas son módulos adicionales — active cada uno cuando su operación lo necesite.",
                "Spedizioni, Trasporto, Piazzale, Pacchi, Magazzino, Acquisti &amp; Inventario, Officina, HR &amp; Paghe e Vendite sono moduli aggiuntivi — attiva ciascuno quando la tua operatività lo richiede.",
                "Expeditie, Transport, Yard, Pakketten, Opslag, Inkoop &amp; Voorraad, Werkplaats, HR &amp; Loon en Sales zijn aanvullende modules — schakel elke module in wanneer uw operatie die nodig heeft."),
            # ---- 02 · Capabilities ----
            "Capabilities": _t("Capacités", "Funktionen", "Capacidades", "Funzionalità", "Mogelijkheden"),
            "Run the operation and the finance on one system.": _t(
                "Pilotez l'opération et la finance sur un seul système.",
                "Betrieb und Finanzen auf einem System steuern.",
                "Gestione la operación y las finanzas en un solo sistema.",
                "Gestisci l'operatività e la finanza su un unico sistema.",
                "Run de operatie en de finance op één systeem."),
            "Twelve capabilities, from the shipment file to the general ledger.": _t(
                "Douze capacités, du dossier d'expédition au grand livre général.",
                "Zwölf Funktionen, von der Sendungsakte bis zum Hauptbuch.",
                "Doce capacidades, desde el expediente de envío hasta el libro mayor.",
                "Dodici funzionalità, dal fascicolo di spedizione al libro mastro generale.",
                "Twaalf mogelijkheden, van het zendingsdossier tot het grootboek."),
            "Built-in finance": _t(
                "Finance intégrée", "Integrierte Finanzbuchhaltung", "Finanzas integradas", "Finanza integrata", "Ingebouwde finance"),
            "A native double-entry general ledger with AR, AP, bank reconciliation and job-level P&amp;L, so operations and accounting live on one system.": _t(
                "Un grand livre général natif en partie double avec comptes clients (AR), comptes fournisseurs (AP), rapprochement bancaire et P&amp;L au niveau du dossier, pour que les opérations et la comptabilité vivent sur un seul système.",
                "Ein natives doppeltes Hauptbuch mit Debitoren (AR), Kreditoren (AP), Bankabstimmung und P&amp;L auf Auftragsebene, sodass Betrieb und Buchhaltung auf einem System leben.",
                "Un libro mayor nativo de doble partida con cuentas por cobrar (AR), cuentas por pagar (AP), conciliación bancaria y P&amp;L a nivel de trabajo, para que las operaciones y la contabilidad vivan en un solo sistema.",
                "Un libro mastro generale nativo in partita doppia con clienti (AR), fornitori (AP), riconciliazione bancaria e P&amp;L a livello di commessa, così operatività e contabilità vivono su un unico sistema.",
                "Een native grootboek met dubbel boekhouden met debiteuren (AR), crediteuren (AP), bankreconciliatie en P&amp;L op opdrachtniveau, zodat operatie en boekhouding op één systeem leven."),
            "VAT engine &amp; returns": _t(
                "Moteur de TVA &amp; déclarations", "MwSt.-Engine &amp; Meldungen", "Motor de IVA &amp; declaraciones", "Motore IVA &amp; dichiarazioni", "Btw-engine &amp; aangiften"),
            "Output, input and import VAT kept as distinct accounts, with VAT-return preparation.": _t(
                "TVA collectée, déductible et à l'importation tenues comme des comptes distincts, avec préparation de la déclaration de TVA.",
                "Ausgangs-, Vorsteuer- und Einfuhr-MwSt. als getrennte Konten geführt, mit Vorbereitung der MwSt.-Meldung.",
                "IVA repercutido, soportado y de importación llevados como cuentas distintas, con preparación de la declaración de IVA.",
                "IVA a debito, a credito e all'importazione tenute come conti distinti, con preparazione della dichiarazione IVA.",
                "Verschuldigde, voorbelasting- en invoer-btw als aparte rekeningen bijgehouden, met voorbereiding van de btw-aangifte."),
            "Freight forwarding": _t(
                "Transit de fret", "Spedition", "Tránsito de carga", "Spedizioni", "Expeditie"),
            "Shipment files, cargo and containers, transport documents, tariffs and demurrage and detention — with GCC seaports, airports and border crossings built in.": _t(
                "Dossiers d'expédition, marchandises et conteneurs, documents de transport, tarifs, surestaries et détention — avec les ports maritimes, aéroports et points de passage frontaliers du Golfe (GCC) intégrés.",
                "Sendungsakten, Fracht und Container, Transportdokumente, Tarife sowie Liege- und Standgeld — mit integrierten Seehäfen, Flughäfen und Grenzübergängen der GCC-Region.",
                "Expedientes de envío, carga y contenedores, documentos de transporte, tarifas, demoras y detención — con puertos marítimos, aeropuertos y pasos fronterizos del Golfo (GCC) integrados.",
                "Fascicoli di spedizione, merci e container, documenti di trasporto, tariffe, controstallie e detention — con porti, aeroporti e valichi di frontiera del Golfo (GCC) integrati.",
                "Zendingsdossiers, lading en containers, transportdocumenten, tarieven, overligtijd en detentie — met zeehavens, luchthavens en grensovergangen in de GCC ingebouwd."),
            "Customs clearance": _t(
                "Dédouanement", "Zollabfertigung", "Despacho de aduanas", "Sdoganamento", "Douaneafhandeling"),
            "Declarations with customs duty kept separate from import VAT, and claimant records.": _t(
                "Déclarations avec les droits de douane tenus séparément de la TVA à l'importation, et fiches des déclarants.",
                "Zollanmeldungen, bei denen Zölle getrennt von der Einfuhr-MwSt. geführt werden, sowie Anmelderdaten.",
                "Declaraciones con los derechos de aduana mantenidos separados del IVA de importación, y fichas de los declarantes.",
                "Dichiarazioni con i dazi doganali tenuti separati dall'IVA all'importazione, e anagrafiche dei dichiaranti.",
                "Aangiften met douanerechten gescheiden van invoer-btw, en gegevens van de aangevers."),
            "Transport &amp; fleet": _t(
                "Transport &amp; flotte", "Transport &amp; Flotte", "Transporte &amp; flota", "Trasporto &amp; flotta", "Transport &amp; wagenpark"),
            "Container and cargo job orders, legs, carriers — your own or a vendor's — and a driver app.": _t(
                "Ordres de mission conteneurs et marchandises, segments, transporteurs — les vôtres ou ceux d'un prestataire — et une application pour le chauffeur.",
                "Auftragspositionen für Container und Fracht, Teilstrecken, Frachtführer — eigene oder eines Dienstleisters — und eine Fahrer-App.",
                "Órdenes de trabajo de contenedores y carga, tramos, transportistas — propios o de un proveedor — y una app para el conductor.",
                "Ordini di lavoro per container e merci, tratte, vettori — propri o di un fornitore — e un'app per l'autista.",
                "Opdrachten voor containers en lading, trajecten, vervoerders — eigen of van een leverancier — en een chauffeursapp."),
            "Container yard &amp; depot": _t(
                "Parc &amp; dépôt de conteneurs", "Containeryard &amp; Depot", "Patio &amp; depósito de contenedores", "Piazzale &amp; deposito container", "Containeryard &amp; depot"),
            "Gate-in and gate-out, occupancy, zones, multi-yard and storage billing — with a 3D yard view.": _t(
                "Entrées et sorties au portail, taux d'occupation, zones, multi-parcs et facturation du stockage — avec une vue 3D du parc.",
                "Gate-In und Gate-Out, Belegung, Zonen, Multi-Yard und Lagergebühren-Abrechnung — mit einer 3D-Yard-Ansicht.",
                "Entradas y salidas por la puerta, ocupación, zonas, multipatio y facturación del almacenaje — con una vista 3D del patio.",
                "Gate-in e gate-out, occupazione, zone, multi-piazzale e fatturazione dello stoccaggio — con una vista 3D del piazzale.",
                "Gate-in en gate-out, bezetting, zones, multi-yard en opslagfacturatie — met een 3D-weergave van de yard."),
            "Parcel &amp; express": _t(
                "Colis &amp; express", "Paket &amp; Express", "Paquetería &amp; exprés", "Pacchi &amp; express", "Pakketten &amp; express"),
            "Booking, hubs, first and last mile, cash-on-delivery, an SLA clock, a rate engine and tracking.": _t(
                "Prise de commande, hubs, premier et dernier kilomètre, paiement à la livraison, un minuteur de SLA, un moteur de tarification et le suivi.",
                "Buchung, Hubs, erste und letzte Meile, Nachnahme, eine SLA-Uhr, eine Tarif-Engine und Sendungsverfolgung.",
                "Reserva, hubs, primera y última milla, contra reembolso, un reloj de SLA, un motor de tarifas y seguimiento.",
                "Prenotazione, hub, primo e ultimo miglio, contrassegno, un cronometro SLA, un motore tariffario e tracciamento.",
                "Boeking, hubs, eerste en laatste mijl, rembours, een SLA-klok, een tariefengine en tracking."),
            "Warehousing &amp; 3PL": _t(
                "Entreposage &amp; 3PL", "Lagerhaltung &amp; 3PL", "Almacenamiento &amp; 3PL", "Magazzino &amp; 3PL", "Opslag &amp; 3PL"),
            "Addressable storage, putaway, pick, pack and ship, cycle counts and storage billing.": _t(
                "Stockage adressable, rangement, prélèvement, emballage et expédition, inventaires tournants et facturation du stockage.",
                "Adressierbarer Lagerplatz, Einlagerung, Kommissionieren, Verpacken und Versenden, Zyklusinventuren und Lagergebühren-Abrechnung.",
                "Almacenamiento direccionable, ubicación, picking, empaquetado y expedición, recuentos cíclicos y facturación del almacenaje.",
                "Stoccaggio indirizzabile, messa a dimora, prelievo, imballaggio e spedizione, inventari ciclici e fatturazione dello stoccaggio.",
                "Adresseerbare opslag, inslag, picken, inpakken en verzenden, cyclustellingen en opslagfacturatie."),
            "Purchasing &amp; inventory": _t(
                "Achats &amp; stock", "Einkauf &amp; Bestand", "Compras &amp; inventario", "Acquisti &amp; inventario", "Inkoop &amp; voorraad"),
            "Purchase orders, goods receipts, stock valuation and invoice matching.": _t(
                "Bons de commande, réceptions de marchandises, valorisation des stocks et rapprochement des factures.",
                "Bestellungen, Wareneingänge, Bestandsbewertung und Rechnungsabgleich.",
                "Órdenes de compra, recepciones de mercancías, valoración de existencias y conciliación de facturas.",
                "Ordini di acquisto, ricevute merci, valorizzazione delle scorte e matching delle fatture.",
                "Inkooporders, goederenontvangsten, voorraadwaardering en factuurmatching."),
            "Maintenance &amp; workshop": _t(
                "Maintenance &amp; atelier", "Wartung &amp; Werkstatt", "Mantenimiento &amp; taller", "Manutenzione &amp; officina", "Onderhoud &amp; werkplaats"),
            "Assets, work orders, preventive maintenance, and parts and labour.": _t(
                "Actifs, ordres de travail, maintenance préventive, pièces et main-d'œuvre.",
                "Anlagen, Arbeitsaufträge, vorbeugende Wartung sowie Teile und Arbeitszeit.",
                "Activos, órdenes de trabajo, mantenimiento preventivo, y piezas y mano de obra.",
                "Asset, ordini di lavoro, manutenzione preventiva, ricambi e manodopera.",
                "Activa, werkorders, preventief onderhoud, en onderdelen en arbeid."),
            "ERP connectors": _t(
                "Connecteurs ERP", "ERP-Konnektoren", "Conectores ERP", "Connettori ERP", "ERP-connectoren"),
            "Two-way connectors for SAP Business One, Odoo and Oracle (Fusion and OIC), plus GPS and telematics, SMS, OIDC single sign-on, webhooks and a REST API.": _t(
                "Des connecteurs bidirectionnels pour SAP Business One, Odoo et Oracle (Fusion et OIC), ainsi que GPS et télématique, SMS, authentification unique via OIDC, webhooks et une API REST.",
                "Bidirektionale Konnektoren für SAP Business One, Odoo und Oracle (Fusion und OIC), dazu GPS und Telematik, SMS, Single Sign-on via OIDC, Webhooks und eine REST-API.",
                "Conectores bidireccionales para SAP Business One, Odoo y Oracle (Fusion y OIC), además de GPS y telemática, SMS, inicio de sesión único por OIDC, webhooks y una API REST.",
                "Connettori bidirezionali per SAP Business One, Odoo e Oracle (Fusion e OIC), oltre a GPS e telematica, SMS, single sign-on tramite OIDC, webhook e una API REST.",
                "Tweerichtingsconnectoren voor SAP Business One, Odoo en Oracle (Fusion en OIC), plus GPS en telematica, SMS, single sign-on via OIDC, webhooks en een REST API."),
            "Multi-tenant &amp; multi-currency": _t(
                "Multi-locataire &amp; multidevise", "Mandantenfähig &amp; mehrwährungsfähig", "Multiinquilino &amp; multidivisa", "Multi-tenant &amp; multivaluta", "Multi-tenant &amp; multivaluta"),
            "Strict per-tenant isolation with row-level security, every amount in its own ISO currency, and Arabic and English with full right-to-left.": _t(
                "Une isolation stricte par locataire avec sécurité au niveau des lignes, chaque montant dans sa propre devise ISO, et l'arabe et l'anglais avec une prise en charge complète de droite à gauche.",
                "Strikte Mandantentrennung mit Sicherheit auf Zeilenebene, jeder Betrag in seiner eigenen ISO-Währung sowie Arabisch und Englisch mit vollständiger Rechts-nach-links-Unterstützung.",
                "Aislamiento estricto por inquilino con seguridad a nivel de fila, cada importe en su propia moneda ISO, y árabe e inglés con soporte completo de derecha a izquierda.",
                "Isolamento rigoroso per tenant con sicurezza a livello di riga, ogni importo nella propria valuta ISO, e arabo e inglese con pieno supporto da destra a sinistra.",
                "Strikte isolatie per tenant met beveiliging op rijniveau, elk bedrag in zijn eigen ISO-valuta, en Arabisch en Engels met volledige rechts-naar-links-ondersteuning."),
            # ---- 03 · Built for ----
            "Built for": _t("Conçu pour", "Entwickelt für", "Diseñado para", "Pensato per", "Gebouwd voor"),
            "Built for GCC logistics.": _t(
                "Conçu pour la logistique du Golfe (GCC).",
                "Für die Logistik der GCC-Region gebaut.",
                "Diseñado para la logística del Golfo (GCC).",
                "Costruito per la logistica del Golfo (GCC).",
                "Gebouwd voor GCC-logistiek."),
            "Freight forwarders": _t(
                "Transitaires", "Spediteure", "Transitarios", "Spedizionieri", "Expediteurs"),
            "Sea, air and land shipment files, customs clearance, and the finance behind them — in one place.": _t(
                "Dossiers d'expédition maritime, aérienne et terrestre, dédouanement et la finance qui les accompagne — au même endroit.",
                "Sendungsakten für See-, Luft- und Landtransport, Zollabfertigung und die Finanzen dahinter — an einem Ort.",
                "Expedientes de envío marítimo, aéreo y terrestre, despacho de aduanas y las finanzas detrás de ellos — en un solo lugar.",
                "Fascicoli di spedizione via mare, aria e terra, sdoganamento e la finanza che li sostiene — in un unico posto.",
                "Zendingsdossiers voor zee, lucht en weg, douaneafhandeling en de finance erachter — op één plek."),
            "Transport &amp; fleet operators": _t(
                "Opérateurs de transport &amp; de flotte", "Transport- &amp; Flottenbetreiber", "Operadores de transporte &amp; flota", "Operatori di trasporto &amp; flotta", "Transport- &amp; wagenparkexploitanten"),
            "Container and cargo job orders, legs, carriers and drivers — costed and invoiced as you go.": _t(
                "Ordres de mission conteneurs et marchandises, segments, transporteurs et chauffeurs — chiffrés et facturés au fil de l'eau.",
                "Auftragspositionen für Container und Fracht, Teilstrecken, Frachtführer und Fahrer — laufend kalkuliert und abgerechnet.",
                "Órdenes de trabajo de contenedores y carga, tramos, transportistas y conductores — costeados y facturados sobre la marcha.",
                "Ordini di lavoro per container e merci, tratte, vettori e autisti — valorizzati e fatturati man mano.",
                "Opdrachten voor containers en lading, trajecten, vervoerders en chauffeurs — gaandeweg gecalculeerd en gefactureerd."),
            "Container yards &amp; depots": _t(
                "Parcs &amp; dépôts de conteneurs", "Containeryards &amp; -depots", "Patios &amp; depósitos de contenedores", "Piazzali &amp; depositi container", "Containeryards &amp; -depots"),
            "Gate moves, occupancy and storage billing across one yard or many, with a 3D view of the yard.": _t(
                "Mouvements au portail, taux d'occupation et facturation du stockage sur un parc ou plusieurs, avec une vue 3D du parc.",
                "Gate-Bewegungen, Belegung und Lagergebühren-Abrechnung über einen oder mehrere Yards, mit einer 3D-Ansicht des Yards.",
                "Movimientos de puerta, ocupación y facturación del almacenaje en uno o varios patios, con una vista 3D del patio.",
                "Movimenti al gate, occupazione e fatturazione dello stoccaggio su uno o più piazzali, con una vista 3D del piazzale.",
                "Gate-bewegingen, bezetting en opslagfacturatie over één of meerdere yards, met een 3D-weergave van de yard."),
            "Couriers &amp; last-mile": _t(
                "Coursiers &amp; dernier kilomètre", "Kuriere &amp; letzte Meile", "Mensajería &amp; última milla", "Corrieri &amp; ultimo miglio", "Koeriers &amp; last-mile"),
            "Parcel booking, hubs, first and last mile, cash-on-delivery and an SLA clock, with live tracking.": _t(
                "Prise de commande de colis, hubs, premier et dernier kilomètre, paiement à la livraison et un minuteur de SLA, avec suivi en direct.",
                "Paketbuchung, Hubs, erste und letzte Meile, Nachnahme und eine SLA-Uhr, mit Live-Sendungsverfolgung.",
                "Reserva de paquetes, hubs, primera y última milla, contra reembolso y un reloj de SLA, con seguimiento en vivo.",
                "Prenotazione pacchi, hub, primo e ultimo miglio, contrassegno e un cronometro SLA, con tracciamento in tempo reale.",
                "Pakketboeking, hubs, eerste en laatste mijl, rembours en een SLA-klok, met live tracking."),
            "3PL &amp; warehouses": _t(
                "3PL &amp; entrepôts", "3PL &amp; Lager", "3PL &amp; almacenes", "3PL &amp; magazzini", "3PL &amp; magazijnen"),
            "Addressable storage, putaway, pick, pack and ship, and storage billing per client.": _t(
                "Stockage adressable, rangement, prélèvement, emballage et expédition, et facturation du stockage par client.",
                "Adressierbarer Lagerplatz, Einlagerung, Kommissionieren, Verpacken und Versenden sowie Lagergebühren-Abrechnung je Kunde.",
                "Almacenamiento direccionable, ubicación, picking, empaquetado y expedición, y facturación del almacenaje por cliente.",
                "Stoccaggio indirizzabile, messa a dimora, prelievo, imballaggio e spedizione, e fatturazione dello stoccaggio per cliente.",
                "Adresseerbare opslag, inslag, picken, inpakken en verzenden, en opslagfacturatie per klant."),
            # ---- 04 · Your region ----
            "Your region": _t("Votre région", "Ihre Region", "Su región", "La tua regione", "Uw regio"),
            "Built for the GCC.": _t(
                "Conçu pour le Golfe (GCC).",
                "Für die GCC-Region gebaut.",
                "Diseñado para el Golfo (GCC).",
                "Costruito per il Golfo (GCC).",
                "Gebouwd voor de GCC."),
            "Multi-tenant, multi-currency and Arabic-first — TMS works the way the Gulf works.": _t(
                "Multi-locataire, multidevise et arabe d'abord — TMS fonctionne comme le Golfe fonctionne.",
                "Mandantenfähig, mehrwährungsfähig und Arabisch zuerst — TMS arbeitet so, wie der Golf arbeitet.",
                "Multiinquilino, multidivisa y árabe primero — TMS funciona como funciona el Golfo.",
                "Multi-tenant, multivaluta e arabo prima di tutto — TMS funziona come funziona il Golfo.",
                "Multi-tenant, multivaluta en Arabisch-eerst — TMS werkt zoals de Golf werkt."),
            "Across the GCC": _t(
                "Dans tout le Golfe (GCC)", "In der gesamten GCC-Region", "En todo el Golfo (GCC)", "In tutto il Golfo (GCC)", "In de hele GCC"),
            "Saudi Arabia, the UAE, Kuwait, Qatar, Bahrain and Oman — one tenant per company, strictly isolated from the next.": _t(
                "Arabie saoudite, Émirats arabes unis, Koweït, Qatar, Bahreïn et Oman — un locataire par entreprise, strictement isolé des autres.",
                "Saudi-Arabien, die VAE, Kuwait, Katar, Bahrain und Oman — ein Mandant pro Unternehmen, strikt vom nächsten getrennt.",
                "Arabia Saudí, los EAU, Kuwait, Catar, Baréin y Omán — un inquilino por empresa, estrictamente aislado del siguiente.",
                "Arabia Saudita, Emirati Arabi Uniti, Kuwait, Qatar, Bahrein e Oman — un tenant per azienda, rigorosamente isolato dagli altri.",
                "Saoedi-Arabië, de VAE, Koeweit, Qatar, Bahrein en Oman — één tenant per bedrijf, strikt geïsoleerd van de volgende."),
            "Multi-currency": _t("Multidevise", "Mehrwährung", "Multidivisa", "Multivaluta", "Multivaluta"),
            "Every amount carries its own ISO currency, so you quote, cost and invoice in SAR, AED, USD or any currency your trade lanes use.": _t(
                "Chaque montant porte sa propre devise ISO : vous établissez vos devis, vos coûts et vos factures en SAR, AED, USD ou toute devise utilisée sur vos axes commerciaux.",
                "Jeder Betrag trägt seine eigene ISO-Währung, sodass Sie in SAR, AED, USD oder jeder Währung Ihrer Handelsrouten anbieten, kalkulieren und fakturieren.",
                "Cada importe lleva su propia moneda ISO, de modo que presupuesta, costea y factura en SAR, AED, USD o cualquier moneda que usen sus rutas comerciales.",
                "Ogni importo porta la propria valuta ISO, così preventivi, costi e fatture sono in SAR, AED, USD o in qualsiasi valuta usata dalle tue rotte commerciali.",
                "Elk bedrag heeft zijn eigen ISO-valuta, zodat u offreert, calculeert en factureert in SAR, AED, USD of elke valuta die uw handelsroutes gebruiken."),
            "Arabic &amp; English": _t(
                "Arabe &amp; anglais", "Arabisch &amp; Englisch", "Árabe &amp; inglés", "Arabo &amp; inglese", "Arabisch &amp; Engels"),
            "Arabic and English throughout, with full right-to-left — for your team and for the documents you issue.": _t(
                "L'arabe et l'anglais partout, avec une prise en charge complète de droite à gauche — pour votre équipe et pour les documents que vous émettez.",
                "Arabisch und Englisch durchgängig, mit vollständiger Rechts-nach-links-Unterstützung — für Ihr Team und für die Dokumente, die Sie ausstellen.",
                "Árabe e inglés en todo, con soporte completo de derecha a izquierda — para su equipo y para los documentos que emite.",
                "Arabo e inglese ovunque, con pieno supporto da destra a sinistra — per il tuo team e per i documenti che emetti.",
                "Arabisch en Engels overal, met volledige rechts-naar-links-ondersteuning — voor uw team en voor de documenten die u uitgeeft."),
            "VAT, kept straight": _t(
                "La TVA, tenue au clair", "MwSt., sauber geführt", "El IVA, bien ordenado", "IVA, tenuta in ordine", "Btw, netjes bijgehouden"),
            "Output, input and import VAT held as distinct accounts, with VAT-return preparation for your filings.": _t(
                "TVA collectée, déductible et à l'importation tenues comme des comptes distincts, avec préparation de la déclaration de TVA pour vos dépôts.",
                "Ausgangs-, Vorsteuer- und Einfuhr-MwSt. als getrennte Konten geführt, mit Vorbereitung der MwSt.-Meldung für Ihre Einreichungen.",
                "IVA repercutido, soportado y de importación llevados como cuentas distintas, con preparación de la declaración de IVA para sus presentaciones.",
                "IVA a debito, a credito e all'importazione tenute come conti distinti, con preparazione della dichiarazione IVA per i tuoi adempimenti.",
                "Verschuldigde, voorbelasting- en invoer-btw als aparte rekeningen, met voorbereiding van de btw-aangifte voor uw indieningen."),
            # ---- 05 · The FulcrumGrid family ----
            "The FulcrumGrid family": _t(
                "La famille FulcrumGrid", "Die FulcrumGrid-Familie", "La familia FulcrumGrid", "La famiglia FulcrumGrid", "De FulcrumGrid-familie"),
            "Explore the rest of the grid": _t(
                "Découvrez le reste de la grille", "Entdecken Sie den Rest des Grids", "Explore el resto de la cuadrícula", "Esplora il resto della griglia", "Ontdek de rest van het grid"),
            "TMS is one of several FulcrumGrid apps, each built to the same standard. Explore the others built for your operations.": _t(
                "TMS est l'une des nombreuses applications FulcrumGrid, chacune conçue selon le même standard. Découvrez les autres, conçues pour vos opérations.",
                "TMS ist eine von mehreren FulcrumGrid-Apps, jede nach demselben Standard gebaut. Entdecken Sie die anderen, gebaut für Ihren Betrieb.",
                "TMS es una de las varias aplicaciones de FulcrumGrid, cada una creada con el mismo estándar. Explore las demás, creadas para sus operaciones.",
                "TMS è una delle diverse app FulcrumGrid, ognuna costruita secondo lo stesso standard. Esplora le altre, costruite per le tue operazioni.",
                "TMS is een van de vele FulcrumGrid-apps, elk gebouwd volgens dezelfde standaard. Ontdek de andere, gebouwd voor uw operatie."),
            "People operations": _t(
                "Gestion des personnes", "Personalmanagement", "Gestión de personas", "Gestione del personale", "Personeelsbeheer"),
            "Operations dashboard": _t(
                "Tableau de bord des opérations", "Betriebs-Dashboard", "Panel de operaciones", "Dashboard operativa", "Operationeel dashboard"),
            "Receivables &amp; payments": _t(
                "Créances &amp; paiements", "Forderungen &amp; Zahlungen", "Cobros &amp; pagos", "Crediti &amp; pagamenti", "Vorderingen &amp; betalingen"),
            "More apps →": _t(
                "Plus d'applications →", "Weitere Apps →", "Más apps →", "Altre app →", "Meer apps →"),
            "Inventory, CRM &amp; more": _t(
                "Inventaire, CRM &amp; plus", "Lagerverwaltung, CRM &amp; mehr", "Inventario, CRM &amp; más", "Inventario, CRM &amp; altro", "Voorraad, CRM &amp; meer"),
            # ---- CTA ----
            "Run logistics and finance<br />on one grid.": _t(
                "Pilotez la logistique et la finance<br />sur une seule grille.",
                "Logistik und Finanzen steuern<br />auf einem Grid.",
                "Gestione la logística y las finanzas<br />en una sola cuadrícula.",
                "Gestisci logistica e finanza<br />su un'unica griglia.",
                "Run logistiek en finance<br />op één grid."),
            "See how TMS runs your whole logistics operation — and its books — from one system.": _t(
                "Découvrez comment TMS pilote toute votre activité logistique — et sa comptabilité — depuis un seul système.",
                "Sehen Sie, wie TMS Ihren gesamten Logistikbetrieb — und seine Buchhaltung — von einem System aus steuert.",
                "Vea cómo TMS gestiona toda su operación logística — y su contabilidad — desde un solo sistema.",
                "Guarda come TMS gestisce tutta la tua operatività logistica — e la sua contabilità — da un unico sistema.",
                "Zie hoe TMS uw hele logistieke operatie — en de boekhouding ervan — vanuit één systeem runt."),
        },
    },
}
