# -*- coding: utf-8 -*-
"""Per-page translations for the Consolidate product page.

Keys are EXACT English substrings of the EN source HTML (entities, straight
apostrophes, dashes and glyphs preserved). Brand/product names (FulcrumGrid,
Consolidate, HR Suite, Command Center, Collection, TMS, Assure, Close, CRM,
Daftra), standard/acronym tokens (API, KPI, MRR, FX, VAT, P&L, ZATCA, SSRF,
AES-256-GCM, PWA, SAR, IFRS, SAP Business One, Odoo, Oracle) and code-like
tokens are left untranslated. Common chrome lives in loc_catalog.COMMON.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/products/consolidate/': {
        'src': 'products/consolidate/index.html',
        't': {
            # ---- Meta ----
            "Consolidate is FulcrumGrid's operator dashboard for every company you run — revenue, cash, receivables, VAT and P&L from your accounting system, consolidated into one view. Connected to Daftra today.": _t(
                "Consolidate est le tableau de bord opérateur de FulcrumGrid pour chaque société que vous gérez — chiffre d'affaires, trésorerie, créances, TVA et P&L depuis votre système comptable, consolidés en une seule vue. Connecté à Daftra aujourd'hui.",
                "Consolidate ist das Betreiber-Dashboard von FulcrumGrid für jedes Unternehmen, das Sie führen — Umsatz, Liquidität, Forderungen, USt. und P&L aus Ihrem Buchhaltungssystem, konsolidiert in einer Ansicht. Heute mit Daftra verbunden.",
                "Consolidate es el panel de operador de FulcrumGrid para cada empresa que gestiona — ingresos, caja, cuentas por cobrar, IVA y P&L desde su sistema contable, consolidados en una sola vista. Conectado a Daftra hoy.",
                "Consolidate è la dashboard operatore di FulcrumGrid per ogni azienda che gestisci — ricavi, liquidità, crediti, IVA e P&L dal tuo sistema contabile, consolidati in un'unica vista. Collegato a Daftra oggi.",
                "Consolidate is het operatordashboard van FulcrumGrid voor elk bedrijf dat u runt — omzet, kas, vorderingen, btw en P&L uit uw boekhoudsysteem, geconsolideerd in één weergave. Vandaag verbonden met Daftra."),
            "Every company you run, on one dashboard — revenue, cash, receivables, VAT and P&L, consolidated from your books.": _t(
                "Chaque société que vous gérez, sur un seul tableau de bord — chiffre d'affaires, trésorerie, créances, TVA et P&L, consolidés depuis vos comptes.",
                "Jedes Unternehmen, das Sie führen, auf einem Dashboard — Umsatz, Liquidität, Forderungen, USt. und P&L, konsolidiert aus Ihren Büchern.",
                "Cada empresa que gestiona, en un solo panel — ingresos, caja, cuentas por cobrar, IVA y P&L, consolidados desde sus libros.",
                "Ogni azienda che gestisci, in un'unica dashboard — ricavi, liquidità, crediti, IVA e P&L, consolidati dai tuoi libri.",
                "Elk bedrijf dat u runt, op één dashboard — omzet, kas, vorderingen, btw en P&L, geconsolideerd uit uw boeken."),
            # ---- Hero ----
            "Finance · Available now": _t(
                "Finance · Disponible maintenant", "Finanzen · Jetzt verfügbar",
                "Finanzas · Ya disponible", "Finanza · Ora disponibile",
                "Financiën · Nu beschikbaar"),
            "Every company you run, on one dashboard.": _t(
                "Chaque société que vous gérez, sur un seul tableau de bord.",
                "Jedes Unternehmen, das Sie führen, auf einem Dashboard.",
                "Cada empresa que gestiona, en un solo panel.",
                "Ogni azienda che gestisci, in un'unica dashboard.",
                "Elk bedrijf dat u runt, op één dashboard."),
            "Consolidate pulls the commercial and financial figures out of your accounting system and brings them into one operator dashboard — revenue, cash, receivables, VAT and P&amp;L across every company you run, side by side and rolled up. Connected to Daftra today, with more sources landing behind the same seam.": _t(
                "Consolidate extrait les chiffres commerciaux et financiers de votre système comptable et les réunit dans un tableau de bord opérateur unique — chiffre d'affaires, trésorerie, créances, TVA et P&amp;L pour chaque société que vous gérez, côte à côte et consolidés. Connecté à Daftra aujourd'hui, avec d'autres sources à venir derrière le même connecteur.",
                "Consolidate zieht die kaufmännischen und finanziellen Kennzahlen aus Ihrem Buchhaltungssystem und bringt sie in ein einziges Betreiber-Dashboard — Umsatz, Liquidität, Forderungen, USt. und P&amp;L über jedes Unternehmen, das Sie führen, nebeneinander und konsolidiert. Heute mit Daftra verbunden, weitere Quellen folgen hinter demselben Anschluss.",
                "Consolidate extrae las cifras comerciales y financieras de su sistema contable y las reúne en un único panel de operador — ingresos, caja, cuentas por cobrar, IVA y P&amp;L de cada empresa que gestiona, una al lado de otra y consolidadas. Conectado a Daftra hoy, con más fuentes en camino detrás del mismo conector.",
                "Consolidate estrae i dati commerciali e finanziari dal tuo sistema contabile e li raccoglie in un'unica dashboard operatore — ricavi, liquidità, crediti, IVA e P&amp;L per ogni azienda che gestisci, affiancati e consolidati. Collegato a Daftra oggi, con altre fonti in arrivo dietro lo stesso connettore.",
                "Consolidate haalt de commerciële en financiële cijfers uit uw boekhoudsysteem en brengt ze samen in één operatordashboard — omzet, kas, vorderingen, btw en P&amp;L voor elk bedrijf dat u runt, naast elkaar en geconsolideerd. Vandaag verbonden met Daftra, met meer bronnen op komst achter dezelfde koppeling."),
            # ---- 01 · Pricing ----
            "01 · Pricing": _t("01 · Tarifs", "01 · Preise", "01 · Precios", "01 · Prezzi", "01 · Prijzen"),
            "Pricing — per company.": _t(
                "Tarifs — par société.", "Preise — pro Unternehmen.", "Precios — por empresa.",
                "Prezzi — per azienda.", "Prijzen — per bedrijf."),
            "Priced per company, with unlimited users — connect your companies and pay for the number you run. Annual billing saves 20%.": _t(
                "Tarifé par société, avec utilisateurs illimités — connectez vos sociétés et payez pour le nombre que vous gérez. La facturation annuelle fait économiser 20 %.",
                "Pro Unternehmen berechnet, mit unbegrenzten Nutzern — verbinden Sie Ihre Unternehmen und zahlen Sie für die Anzahl, die Sie führen. Jährliche Abrechnung spart 20 %.",
                "Precio por empresa, con usuarios ilimitados — conecte sus empresas y pague por el número que gestiona. La facturación anual ahorra un 20 %.",
                "Prezzo per azienda, con utenti illimitati — collega le tue aziende e paghi per il numero che gestisci. La fatturazione annuale fa risparmiare il 20%.",
                "Prijs per bedrijf, met onbeperkte gebruikers — koppel uw bedrijven en betaal voor het aantal dat u runt. Jaarlijkse facturering bespaart 20%."),
            "Per company / month": _t(
                "Par société / mois", "Pro Unternehmen / Monat", "Por empresa / mes",
                "Per azienda / mese", "Per bedrijf / maand"),
            "Unlimited users · 14-day free trial": _t(
                "Utilisateurs illimités · essai gratuit de 14 jours", "Unbegrenzte Nutzer · 14 Tage kostenlos testen",
                "Usuarios ilimitados · prueba gratuita de 14 días", "Utenti illimitati · prova gratuita di 14 giorni",
                "Onbeperkte gebruikers · 14 dagen gratis proberen"),
            "Starter · up to 3 companies": _t(
                "Starter · jusqu'à 3 sociétés", "Starter · bis zu 3 Unternehmen", "Starter · hasta 3 empresas",
                "Starter · fino a 3 aziende", "Starter · tot 3 bedrijven"),
            "Growth · up to 15": _t(
                "Growth · jusqu'à 15", "Growth · bis zu 15", "Growth · hasta 15", "Growth · fino a 15", "Growth · tot 15"),
            "Scale · up to 50": _t(
                "Scale · jusqu'à 50", "Scale · bis zu 50", "Scale · hasta 50", "Scale · fino a 50", "Scale · tot 50"),
            "Enterprise · 50+": _t(
                "Enterprise · 50+", "Enterprise · 50+", "Enterprise · 50+", "Enterprise · 50+", "Enterprise · 50+"),
            "Connected to Daftra today; more sources on the way.": _t(
                "Connecté à Daftra aujourd'hui ; d'autres sources arrivent.",
                "Heute mit Daftra verbunden; weitere Quellen folgen.",
                "Conectado a Daftra hoy; más fuentes en camino.",
                "Collegato a Daftra oggi; altre fonti in arrivo.",
                "Vandaag verbonden met Daftra; meer bronnen op komst."),
            "<b>Custom</b>": _t("<b>Sur mesure</b>", "<b>Individuell</b>", "<b>A medida</b>", "<b>Su misura</b>", "<b>Op maat</b>"),
            "What a demo covers": _t(
                "Ce que couvre une démo", "Was eine Demo abdeckt", "Qué cubre una demo",
                "Cosa copre una demo", "Wat een demo behandelt"),
            "In one short call": _t(
                "En un court appel", "In einem kurzen Gespräch", "En una breve llamada",
                "In una breve chiamata", "In één kort gesprek"),
            "Connecting your Daftra companies": _t(
                "La connexion de vos sociétés Daftra", "Das Verbinden Ihrer Daftra-Unternehmen",
                "La conexión de sus empresas de Daftra", "Il collegamento delle tue aziende Daftra",
                "Het koppelen van uw Daftra-bedrijven"),
            "The consolidated KPI dashboard": _t(
                "Le tableau de bord de KPI consolidés", "Das konsolidierte KPI-Dashboard",
                "El panel de KPI consolidados", "La dashboard dei KPI consolidati",
                "Het geconsolideerde KPI-dashboard"),
            "How snapshots and base-currency roll-up work": _t(
                "Le fonctionnement des instantanés et de la consolidation en devise de base",
                "Wie Snapshots und die Konsolidierung in der Basiswährung funktionieren",
                "Cómo funcionan las instantáneas y la consolidación en la divisa base",
                "Come funzionano gli snapshot e il consolidamento nella valuta base",
                "Hoe snapshots en consolidatie in de basisvaluta werken"),
            "Fit for the companies you run": _t(
                "L'adéquation aux sociétés que vous gérez", "Die Eignung für die Unternehmen, die Sie führen",
                "La adecuación a las empresas que gestiona", "L'idoneità per le aziende che gestisci",
                "De geschiktheid voor de bedrijven die u runt"),
            "Talk to sales ↗": _t(
                "Parler aux ventes ↗", "Mit dem Vertrieb sprechen ↗", "Hablar con ventas ↗",
                "Parla con le vendite ↗", "Praat met sales ↗"),
            # ---- 02 · Capabilities ----
            "02 · Capabilities": _t("02 · Capacités", "02 · Funktionen", "02 · Capacidades", "02 · Funzionalità", "02 · Mogelijkheden"),
            "The whole group, read from the books.": _t(
                "Tout le groupe, lu depuis les comptes.",
                "Die ganze Gruppe, aus den Büchern gelesen.",
                "Todo el grupo, leído desde los libros.",
                "L'intero gruppo, letto dai libri.",
                "De hele groep, gelezen uit de boeken."),
            "Commercial and financial figures only — no HR — consolidated across every company you connect.": _t(
                "Chiffres commerciaux et financiers uniquement — pas de RH — consolidés pour chaque société que vous connectez.",
                "Nur kaufmännische und finanzielle Kennzahlen — kein HR — konsolidiert über jedes Unternehmen, das Sie verbinden.",
                "Solo cifras comerciales y financieras — sin RR. HH. — consolidadas en cada empresa que conecta.",
                "Solo dati commerciali e finanziari — niente HR — consolidati su ogni azienda che colleghi.",
                "Alleen commerciële en financiële cijfers — geen HR — geconsolideerd over elk bedrijf dat u koppelt."),
            "One dashboard, every company": _t(
                "Un tableau de bord, chaque société", "Ein Dashboard, jedes Unternehmen",
                "Un panel, cada empresa", "Una dashboard, ogni azienda",
                "Eén dashboard, elk bedrijf"),
            "Revenue, collections, cash, receivables and payables for each company you run — side by side and consolidated into one view.": _t(
                "Chiffre d'affaires, encaissements, trésorerie, créances et dettes pour chaque société que vous gérez — côte à côte et consolidés en une seule vue.",
                "Umsatz, Zahlungseingänge, Liquidität, Forderungen und Verbindlichkeiten für jedes Unternehmen, das Sie führen — nebeneinander und in einer Ansicht konsolidiert.",
                "Ingresos, cobros, caja, cuentas por cobrar y por pagar de cada empresa que gestiona — una al lado de otra y consolidadas en una sola vista.",
                "Ricavi, incassi, liquidità, crediti e debiti per ogni azienda che gestisci — affiancati e consolidati in un'unica vista.",
                "Omzet, ontvangsten, kas, vorderingen en schulden voor elk bedrijf dat u runt — naast elkaar en geconsolideerd in één weergave."),
            "AR ageing": _t(
                "Balance âgée des créances", "Fälligkeitsanalyse der Forderungen", "Antigüedad de cuentas por cobrar",
                "Scadenzario crediti", "Ouderdomsanalyse vorderingen"),
            "Open receivables bucketed by age, so you can see what's current and what's slipping — per company and across the group.": _t(
                "Les créances ouvertes regroupées par ancienneté, pour voir ce qui est à jour et ce qui dérape — par société et pour tout le groupe.",
                "Offene Forderungen nach Alter gruppiert, damit Sie sehen, was aktuell ist und was ins Rutschen gerät — je Unternehmen und für die gesamte Gruppe.",
                "Las cuentas por cobrar abiertas agrupadas por antigüedad, para ver qué está al día y qué se retrasa — por empresa y en todo el grupo.",
                "I crediti aperti raggruppati per anzianità, per vedere cosa è corrente e cosa sta scivolando — per azienda e sull'intero gruppo.",
                "Openstaande vorderingen gegroepeerd op ouderdom, zodat u ziet wat actueel is en wat uitloopt — per bedrijf en over de hele groep."),
            "P&amp;L snapshot": _t(
                "Instantané du P&amp;L", "P&amp;L-Momentaufnahme", "Instantánea del P&amp;L",
                "Istantanea del P&amp;L", "P&amp;L-momentopname"),
            "Expenses, other income and a net figure read straight from your books, alongside revenue and cash.": _t(
                "Charges, autres produits et un résultat net lus directement depuis vos comptes, aux côtés du chiffre d'affaires et de la trésorerie.",
                "Aufwendungen, sonstige Erträge und ein Nettowert, direkt aus Ihren Büchern gelesen, neben Umsatz und Liquidität.",
                "Gastos, otros ingresos y una cifra neta leídos directamente desde sus libros, junto a ingresos y caja.",
                "Costi, altri ricavi e un valore netto letti direttamente dai tuoi libri, accanto a ricavi e liquidità.",
                "Kosten, overige inkomsten en een nettocijfer rechtstreeks uit uw boeken gelezen, naast omzet en kas."),
            "VAT &amp; ZATCA status": _t(
                "TVA &amp; statut ZATCA", "USt. &amp; ZATCA-Status", "IVA &amp; estado ZATCA",
                "IVA &amp; stato ZATCA", "Btw &amp; ZATCA-status"),
            "VAT derived from your invoices and purchases, with each company's ZATCA e-invoicing status surfaced (best-effort).": _t(
                "TVA déduite de vos factures et achats, avec le statut de facturation électronique ZATCA de chaque société mis en avant (au mieux).",
                "USt. aus Ihren Rechnungen und Einkäufen abgeleitet, mit dem ZATCA-E-Invoicing-Status jedes Unternehmens (nach bestem Bemühen).",
                "IVA derivado de sus facturas y compras, con el estado de facturación electrónica ZATCA de cada empresa a la vista (en la medida de lo posible).",
                "IVA ricavata dalle tue fatture e dai tuoi acquisti, con lo stato di fatturazione elettronica ZATCA di ogni azienda in evidenza (per quanto possibile).",
                "Btw afgeleid uit uw facturen en inkopen, met de ZATCA-e-facturatiestatus van elk bedrijf in beeld (naar beste vermogen)."),
            "Recurring revenue &amp; pipeline": _t(
                "Revenu récurrent &amp; pipeline", "Wiederkehrender Umsatz &amp; Pipeline", "Ingresos recurrentes &amp; pipeline",
                "Ricavo ricorrente &amp; pipeline", "Terugkerende omzet &amp; pipeline"),
            "MRR from subscriptions and an estimates-to-invoices conversion view, where your books carry them.": _t(
                "Le MRR des abonnements et une vue de conversion des devis en factures, là où vos comptes les portent.",
                "MRR aus Abonnements und eine Umwandlungsansicht von Angeboten zu Rechnungen, sofern Ihre Bücher sie führen.",
                "El MRR de las suscripciones y una vista de conversión de presupuestos a facturas, donde sus libros los recogen.",
                "L'MRR degli abbonamenti e una vista di conversione da preventivi a fatture, dove i tuoi libri li riportano.",
                "De MRR uit abonnementen en een conversieweergave van offertes naar facturen, waar uw boeken ze bevatten."),
            "Client insight": _t(
                "Connaissance clients", "Kundeneinblick", "Perspectiva de clientes",
                "Insight sui clienti", "Klantinzicht"),
            "Client counts, new-versus-returning cohorts and your top clients by value, drawn from invoice history.": _t(
                "Le nombre de clients, les cohortes nouveaux contre récurrents et vos meilleurs clients par valeur, tirés de l'historique des factures.",
                "Kundenzahlen, Kohorten neu gegen wiederkehrend und Ihre wertvollsten Kunden, aus der Rechnungshistorie gezogen.",
                "Recuento de clientes, cohortes de nuevos frente a recurrentes y sus mejores clientes por valor, extraídos del historial de facturas.",
                "Il numero di clienti, le coorti nuovi contro ricorrenti e i tuoi migliori clienti per valore, ricavati dallo storico delle fatture.",
                "Aantal klanten, cohorten nieuw versus terugkerend en uw beste klanten op waarde, afgeleid uit de factuurhistorie."),
            "Base-currency consolidation": _t(
                "Consolidation en devise de base", "Konsolidierung in der Basiswährung", "Consolidación en divisa base",
                "Consolidamento nella valuta base", "Consolidatie in basisvaluta"),
            "Each company keeps its own currency; you set a base currency and FX rates, and mixed-currency entities roll up into one comparable total.": _t(
                "Chaque société conserve sa propre devise ; vous définissez une devise de base et des taux de change, et les entités multidevises se consolident en un total unique comparable.",
                "Jedes Unternehmen behält seine eigene Währung; Sie legen eine Basiswährung und FX-Kurse fest, und Einheiten mit gemischten Währungen werden zu einer vergleichbaren Gesamtsumme konsolidiert.",
                "Cada empresa conserva su propia divisa; usted fija una divisa base y tipos de cambio, y las entidades multidivisa se consolidan en un único total comparable.",
                "Ogni azienda mantiene la propria valuta; imposti una valuta base e tassi di cambio, e le entità multivaluta si consolidano in un unico totale confrontabile.",
                "Elk bedrijf houdt zijn eigen valuta; u stelt een basisvaluta en FX-koersen in, en entiteiten met gemengde valuta's rollen op tot één vergelijkbaar totaal."),
            "Per-company drill-in": _t(
                "Zoom par société", "Drill-down je Unternehmen", "Desglose por empresa",
                "Drill-down per azienda", "Inzoomen per bedrijf"),
            "A companies table that opens any single entity's detail — from the group headline down to one company's figures.": _t(
                "Un tableau des sociétés qui ouvre le détail de n'importe quelle entité — du chiffre d'ensemble du groupe jusqu'aux chiffres d'une seule société.",
                "Eine Unternehmenstabelle, die das Detail jeder einzelnen Einheit öffnet — von der Gruppenkennzahl bis zu den Zahlen eines einzelnen Unternehmens.",
                "Una tabla de empresas que abre el detalle de cualquier entidad — desde la cifra global del grupo hasta las cifras de una sola empresa.",
                "Una tabella delle aziende che apre il dettaglio di qualsiasi singola entità — dal dato complessivo del gruppo fino ai numeri di una singola azienda.",
                "Een bedrijventabel die het detail van elke afzonderlijke entiteit opent — van het groepscijfer tot de cijfers van één bedrijf."),
            "Nightly snapshots": _t(
                "Instantanés nocturnes", "Nächtliche Snapshots", "Instantáneas nocturnas",
                "Snapshot notturni", "Nachtelijke snapshots"),
            "A worker pulls each company's figures on a schedule; the dashboard reads those snapshots, so it loads fast and never hammers your accounting system live.": _t(
                "Un processus récupère les chiffres de chaque société selon une planification ; le tableau de bord lit ces instantanés, il se charge donc vite et ne sollicite jamais votre système comptable en direct.",
                "Ein Worker ruft die Zahlen jedes Unternehmens planmäßig ab; das Dashboard liest diese Snapshots, lädt daher schnell und belastet Ihr Buchhaltungssystem nie live.",
                "Un proceso recupera las cifras de cada empresa según una programación; el panel lee esas instantáneas, por lo que carga rápido y nunca sobrecarga su sistema contable en vivo.",
                "Un worker recupera i numeri di ogni azienda in base a una pianificazione; la dashboard legge quegli snapshot, così si carica in fretta e non sovraccarica mai il tuo sistema contabile in diretta.",
                "Een worker haalt de cijfers van elk bedrijf volgens een schema op; het dashboard leest die snapshots, laadt dus snel en belast uw boekhoudsysteem nooit live."),
            "Encrypted keys, read-only": _t(
                "Clés chiffrées, en lecture seule", "Verschlüsselte Schlüssel, nur Lesezugriff", "Claves cifradas, solo lectura",
                "Chiavi crittografate, sola lettura", "Versleutelde sleutels, alleen-lezen"),
            "API keys are AES-256-GCM encrypted at rest and never sent back to the browser. Consolidate only reads your figures — it never writes to your books.": _t(
                "Les clés API sont chiffrées au repos en AES-256-GCM et ne sont jamais renvoyées au navigateur. Consolidate ne fait que lire vos chiffres — il n'écrit jamais dans vos comptes.",
                "API-Schlüssel werden im Ruhezustand mit AES-256-GCM verschlüsselt und nie an den Browser zurückgesendet. Consolidate liest nur Ihre Zahlen — es schreibt nie in Ihre Bücher.",
                "Las claves API se cifran en reposo con AES-256-GCM y nunca se devuelven al navegador. Consolidate solo lee sus cifras — nunca escribe en sus libros.",
                "Le chiavi API sono crittografate a riposo con AES-256-GCM e non vengono mai restituite al browser. Consolidate legge soltanto i tuoi numeri — non scrive mai nei tuoi libri.",
                "API-sleutels worden in rust versleuteld met AES-256-GCM en nooit terug naar de browser gestuurd. Consolidate leest alleen uw cijfers — het schrijft nooit in uw boeken."),
            "Hardened connections": _t(
                "Connexions renforcées", "Gehärtete Verbindungen", "Conexiones reforzadas",
                "Connessioni rafforzate", "Geharde verbindingen"),
            "Every data pull is host-pinned with SSRF protection, rejected redirects and strict size and time limits, behind an optional operator token.": _t(
                "Chaque récupération de données est épinglée à l'hôte avec protection SSRF, redirections rejetées et limites strictes de taille et de temps, derrière un jeton opérateur optionnel.",
                "Jeder Datenabruf ist host-gebunden mit SSRF-Schutz, abgewiesenen Weiterleitungen und strengen Größen- und Zeitlimits, hinter einem optionalen Betreiber-Token.",
                "Cada extracción de datos está fijada al host con protección SSRF, redirecciones rechazadas y límites estrictos de tamaño y tiempo, detrás de un token de operador opcional.",
                "Ogni estrazione di dati è vincolata all'host con protezione SSRF, reindirizzamenti rifiutati e limiti rigorosi di dimensione e tempo, dietro un token operatore opzionale.",
                "Elke dataopvraging is host-gebonden met SSRF-bescherming, geweigerde omleidingen en strikte grootte- en tijdslimieten, achter een optioneel operatortoken."),
            "Install it like an app": _t(
                "Installez-le comme une application", "Installieren Sie es wie eine App", "Instálelo como una app",
                "Installalo come un'app", "Installeer het als een app"),
            "An installable progressive web app with an offline fallback and opt-in push that tells you when a fresh snapshot is in.": _t(
                "Une application web progressive installable, avec un repli hors ligne et des notifications push optionnelles qui vous préviennent dès qu'un nouvel instantané est disponible.",
                "Eine installierbare Progressive Web App mit Offline-Fallback und optionalen Push-Benachrichtigungen, die Ihnen melden, sobald ein neuer Snapshot da ist.",
                "Una aplicación web progresiva instalable, con respaldo sin conexión y notificaciones push opcionales que le avisan cuando hay una nueva instantánea.",
                "Un'applicazione web progressiva installabile, con fallback offline e notifiche push opzionali che ti avvisano quando è pronto un nuovo snapshot.",
                "Een installeerbare progressive web app met offline-fallback en optionele pushmeldingen die u laten weten wanneer er een nieuwe snapshot is."),
            # ---- 03 · Built for ----
            "03 · Built for": _t("03 · Conçu pour", "03 · Entwickelt für", "03 · Diseñado para", "03 · Pensato per", "03 · Gebouwd voor"),
            "Built for the operator's chair.": _t(
                "Conçu pour le fauteuil de l'opérateur.",
                "Gebaut für den Stuhl des Betreibers.",
                "Diseñado para la silla del operador.",
                "Pensato per la poltrona dell'operatore.",
                "Gebouwd voor de stoel van de operator."),
            "Multi-company owners": _t(
                "Propriétaires multi-sociétés", "Eigentümer mehrerer Unternehmen", "Propietarios de varias empresas",
                "Titolari di più aziende", "Eigenaren van meerdere bedrijven"),
            "See every business you run side by side, without stitching spreadsheets together at month-end.": _t(
                "Voyez côte à côte chaque activité que vous dirigez, sans assembler des tableurs en fin de mois.",
                "Sehen Sie jedes Geschäft, das Sie führen, nebeneinander — ohne am Monatsende Tabellen zusammenzufügen.",
                "Vea una al lado de otra cada actividad que dirige, sin coser hojas de cálculo a fin de mes.",
                "Vedi affiancate tutte le attività che gestisci, senza cucire fogli di calcolo a fine mese.",
                "Zie elk bedrijf dat u runt naast elkaar, zonder aan het einde van de maand spreadsheets aan elkaar te plakken."),
            "Finance leadership": _t(
                "Direction financière", "Finanzleitung", "Dirección financiera",
                "Direzione finanziaria", "Financiële leiding"),
            "A consolidated read on revenue, cash, receivables and P&amp;L across the group, refreshed on a schedule.": _t(
                "Une lecture consolidée du chiffre d'affaires, de la trésorerie, des créances et du P&amp;L pour tout le groupe, actualisée selon une planification.",
                "Ein konsolidierter Blick auf Umsatz, Liquidität, Forderungen und P&amp;L der gesamten Gruppe, planmäßig aktualisiert.",
                "Una lectura consolidada de ingresos, caja, cuentas por cobrar y P&amp;L de todo el grupo, actualizada según una programación.",
                "Una lettura consolidata di ricavi, liquidità, crediti e P&amp;L dell'intero gruppo, aggiornata secondo una pianificazione.",
                "Een geconsolideerd beeld van omzet, kas, vorderingen en P&amp;L over de hele groep, volgens een schema ververst."),
            "Group controllers": _t(
                "Contrôleurs de groupe", "Konzerncontroller", "Controllers de grupo",
                "Controller di gruppo", "Groepscontrollers"),
            "Mixed currencies and entities rolled into one comparable view, each still drillable to its own detail.": _t(
                "Devises et entités mixtes réunies en une vue comparable, chacune restant explorable jusqu'à son propre détail.",
                "Gemischte Währungen und Einheiten in einer vergleichbaren Ansicht zusammengeführt, jede weiterhin bis ins eigene Detail aufschlüsselbar.",
                "Divisas y entidades mixtas reunidas en una vista comparable, cada una aún desglosable hasta su propio detalle.",
                "Valute ed entità miste riunite in una vista confrontabile, ognuna ancora esplorabile fino al proprio dettaglio.",
                "Gemengde valuta's en entiteiten samengebracht in één vergelijkbare weergave, elk nog inzoombaar tot het eigen detail."),
            # ---- 04 · Your sources ----
            "04 · Your sources": _t("04 · Vos sources", "04 · Ihre Quellen", "04 · Sus fuentes", "04 · Le tue fonti", "04 · Uw bronnen"),
            "Daftra today, more sources next.": _t(
                "Daftra aujourd'hui, d'autres sources ensuite.",
                "Daftra heute, weitere Quellen als Nächstes.",
                "Daftra hoy, más fuentes después.",
                "Daftra oggi, altre fonti in seguito.",
                "Daftra vandaag, meer bronnen hierna."),
            "Connect a company in Settings with its subdomain and API key — no migration, nothing to install on your side.": _t(
                "Connectez une société dans les Paramètres avec son sous-domaine et sa clé API — aucune migration, rien à installer de votre côté.",
                "Verbinden Sie ein Unternehmen in den Einstellungen mit seiner Subdomain und seinem API-Schlüssel — keine Migration, nichts auf Ihrer Seite zu installieren.",
                "Conecte una empresa en Ajustes con su subdominio y su clave API — sin migración, nada que instalar por su parte.",
                "Collega un'azienda nelle Impostazioni con il suo sottodominio e la sua chiave API — nessuna migrazione, niente da installare dalla tua parte.",
                "Koppel een bedrijf in Instellingen met zijn subdomein en API-sleutel — geen migratie, niets te installeren aan uw kant."),
            "Daftra — connected": _t(
                "Daftra — connecté", "Daftra — verbunden", "Daftra — conectado",
                "Daftra — collegato", "Daftra — verbonden"),
            "Point Consolidate at your Daftra companies and the commercial and financial figures flow in. Live today.": _t(
                "Pointez Consolidate vers vos sociétés Daftra et les chiffres commerciaux et financiers affluent. Disponible aujourd'hui.",
                "Richten Sie Consolidate auf Ihre Daftra-Unternehmen und die kaufmännischen und finanziellen Zahlen fließen ein. Heute verfügbar.",
                "Apunte Consolidate a sus empresas de Daftra y las cifras comerciales y financieras entran. Disponible hoy.",
                "Punta Consolidate alle tue aziende Daftra e i dati commerciali e finanziari affluiscono. Disponibile oggi.",
                "Richt Consolidate op uw Daftra-bedrijven en de commerciële en financiële cijfers stromen binnen. Vandaag beschikbaar."),
            "More sources, same seam": _t(
                "Plus de sources, le même connecteur", "Mehr Quellen, derselbe Anschluss", "Más fuentes, el mismo conector",
                "Più fonti, lo stesso connettore", "Meer bronnen, dezelfde koppeling"),
            "SAP Business One, Odoo and Oracle are on the way behind the same connector, so a new source is add-once, not a rebuild.": _t(
                "SAP Business One, Odoo et Oracle arrivent derrière le même connecteur : ajouter une source se fait une fois, sans tout reconstruire.",
                "SAP Business One, Odoo und Oracle kommen hinter demselben Connector, sodass eine neue Quelle einmal hinzugefügt wird, statt alles neu zu bauen.",
                "SAP Business One, Odoo y Oracle están en camino detrás del mismo conector, así que una fuente nueva se añade una vez, sin reconstruir.",
                "SAP Business One, Odoo e Oracle sono in arrivo dietro lo stesso connettore, così una nuova fonte si aggiunge una volta, senza ricostruire.",
                "SAP Business One, Odoo en Oracle zijn op komst achter dezelfde connector, dus een nieuwe bron is één keer toevoegen, geen herbouw."),
            "Multi-currency, one base": _t(
                "Multidevise, une base unique", "Multi-Währung, eine Basis", "Multidivisa, una base",
                "Multivaluta, un'unica base", "Multivaluta, één basis"),
            "Entities keep their own currency; set FX to a base currency for the consolidated total, with SAR as the default.": _t(
                "Les entités conservent leur devise ; définissez le change vers une devise de base pour le total consolidé, avec le SAR par défaut.",
                "Einheiten behalten ihre eigene Währung; legen Sie FX auf eine Basiswährung für die konsolidierte Gesamtsumme fest, mit SAR als Standard.",
                "Las entidades conservan su divisa; fije el cambio a una divisa base para el total consolidado, con SAR por defecto.",
                "Le entità mantengono la propria valuta; imposta il cambio verso una valuta base per il totale consolidato, con SAR come predefinita.",
                "Entiteiten houden hun eigen valuta; stel FX in naar een basisvaluta voor het geconsolideerde totaal, met SAR als standaard."),
            "Secure by default": _t(
                "Sécurisé par défaut", "Standardmäßig sicher", "Seguro por defecto",
                "Sicuro per impostazione predefinita", "Standaard veilig"),
            "Encrypted API keys, host-pinned read-only access and an optional operator token gating the whole dashboard.": _t(
                "Clés API chiffrées, accès en lecture seule épinglé à l'hôte et jeton opérateur optionnel protégeant tout le tableau de bord.",
                "Verschlüsselte API-Schlüssel, host-gebundener Nur-Lese-Zugriff und ein optionales Betreiber-Token, das das gesamte Dashboard schützt.",
                "Claves API cifradas, acceso de solo lectura fijado al host y un token de operador opcional que protege todo el panel.",
                "Chiavi API crittografate, accesso in sola lettura vincolato all'host e un token operatore opzionale che protegge l'intera dashboard.",
                "Versleutelde API-sleutels, host-gebonden alleen-lezentoegang en een optioneel operatortoken dat het hele dashboard afschermt."),
            # ---- 05 · The FulcrumGrid family ----
            "05 · The FulcrumGrid family": _t(
                "05 · La famille FulcrumGrid", "05 · Die FulcrumGrid-Familie", "05 · La familia FulcrumGrid",
                "05 · La famiglia FulcrumGrid", "05 · De FulcrumGrid-familie"),
            "Explore the rest of the grid.": _t(
                "Découvrez le reste de la grille.", "Entdecken Sie den Rest des Grids.",
                "Explore el resto de la cuadrícula.", "Esplora il resto della griglia.",
                "Ontdek de rest van het grid."),
            "Consolidate is one of several FulcrumGrid apps, each built to the same standard. Explore the others built for your operations.": _t(
                "Consolidate est l'une des nombreuses applications FulcrumGrid, chacune conçue selon le même standard. Découvrez les autres, conçues pour vos opérations.",
                "Consolidate ist eine von mehreren FulcrumGrid-Apps, jede nach demselben Standard gebaut. Entdecken Sie die anderen, gebaut für Ihren Betrieb.",
                "Consolidate es una de las varias aplicaciones de FulcrumGrid, cada una creada con el mismo estándar. Explore las demás, creadas para sus operaciones.",
                "Consolidate è una delle diverse app FulcrumGrid, ognuna costruita secondo lo stesso standard. Esplora le altre, costruite per le tue operazioni.",
                "Consolidate is een van de vele FulcrumGrid-apps, elk gebouwd volgens dezelfde standaard. Ontdek de andere, gebouwd voor uw operatie."),
            "People operations": _t(
                "Gestion du personnel", "Personalmanagement", "Gestión de personas",
                "Gestione del personale", "Personeelsbeheer"),
            "Operations dashboard": _t(
                "Tableau de bord des opérations", "Betriebs-Dashboard", "Panel de operaciones",
                "Dashboard operativa", "Operationeel dashboard"),
            "Receivables &amp; payments": _t(
                "Créances &amp; paiements", "Forderungen &amp; Zahlungen", "Cobros &amp; pagos",
                "Crediti &amp; pagamenti", "Vorderingen &amp; betalingen"),
            "Logistics &amp; finance": _t(
                "Logistique &amp; finances", "Logistik &amp; Finanzen", "Logística &amp; finanzas",
                "Logistica &amp; finanza", "Logistiek &amp; financiën"),
            "IFRS period-end": _t(
                "Clôture IFRS", "IFRS-Periodenende", "Cierre IFRS",
                "Fine periodo IFRS", "IFRS-periodeafsluiting"),
            "More apps →": _t(
                "Plus d'applications →", "Weitere Apps →", "Más apps →", "Altre app →", "Meer apps →"),
            "Assure, CRM &amp; more": _t(
                "Assure, CRM &amp; plus", "Assure, CRM &amp; mehr", "Assure, CRM &amp; más",
                "Assure, CRM &amp; altro", "Assure, CRM &amp; meer"),
            # ---- CTA ----
            "Every company.<br />One dashboard.": _t(
                "Chaque société.<br />Un seul tableau de bord.",
                "Jedes Unternehmen.<br />Ein Dashboard.",
                "Cada empresa.<br />Un solo panel.",
                "Ogni azienda.<br />Un'unica dashboard.",
                "Elk bedrijf.<br />Eén dashboard."),
            "See how Consolidate brings the figures from all your companies into a single operator view.": _t(
                "Voyez comment Consolidate réunit les chiffres de toutes vos sociétés dans une vue opérateur unique.",
                "Sehen Sie, wie Consolidate die Zahlen all Ihrer Unternehmen in einer einzigen Betreiberansicht zusammenführt.",
                "Vea cómo Consolidate reúne las cifras de todas sus empresas en una única vista de operador.",
                "Scopri come Consolidate riunisce i numeri di tutte le tue aziende in un'unica vista operatore.",
                "Zie hoe Consolidate de cijfers van al uw bedrijven samenbrengt in één operatorweergave."),
        },
    },
}
