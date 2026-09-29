# -*- coding: utf-8 -*-
"""Per-page translations for the finance/Collection blog pages:

  /blog/                                    -> blog/index.html
  /blog/accounts-receivable-best-practices/ -> .../index.html
  /blog/accounts-receivable-vs-payable/     -> .../index.html
  /blog/invoice-payment-terms/              -> .../index.html
  /blog/payment-reminder-email/             -> .../index.html
  /blog/reduce-days-sales-outstanding/      -> .../index.html
  /blog/what-is-dunning/                    -> .../index.html

Conventions (see loc_catalog.py):
  * Brand/product names stay English: FulcrumGrid, Command Center, Collection,
    HR Suite, Blog, FAQ. Kept acronyms: DSO, AR, AP, KPI, OKR, SOP, PTO, HR,
    ERP, SaaS, DPO, EOM, CIA, PIA, Net 30, etc. Currency codes and numbers
    stay as-is.
  * Keys are the EXACT English text as it appears in the EN source, including
    inline tags, &amp;, straight apostrophes, em dashes (—) and en dashes (–).
  * Chrome/global strings live in the shared COMMON catalog and are NOT
    repeated here (nav, footer, buttons, "Request a demo", the tagline, etc.).
  * JSON-LD structured-data text is intentionally left English (matches how the
    other pages were handled); only human-visible copy is translated.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# ---- Shared across all six article pages ------------------------------------

_OG_ALT_COLLECTION = _t(
    'FulcrumGrid Collection — créances et paiements',
    'FulcrumGrid Collection — Forderungen und Zahlungen',
    'FulcrumGrid Collection — cobros y pagos',
    'FulcrumGrid Collection — crediti e pagamenti',
    'FulcrumGrid Collection — vorderingen en betalingen')

_HOME = _t('<a href="/">Accueil</a>', '<a href="/">Startseite</a>',
           '<a href="/">Inicio</a>', '<a href="/">Home</a>', '<a href="/">Home</a>')

_BACK_TO_BLOG = _t('Retour au blog', 'Zurück zum Blog', 'Volver al blog',
                   'Torna al blog', 'Terug naar de blog')

_EXPLORE_COLLECTION = _t('Découvrir Collection', 'Collection entdecken',
                         'Explorar Collection', 'Esplora Collection',
                         'Ontdek Collection')

_MIN_READ_6 = _t('6 min de lecture', '6 Min. Lesezeit', '6 min de lectura',
                 '6 min di lettura', '6 min lezen')
_MIN_READ_7 = _t('7 min de lecture', '7 Min. Lesezeit', '7 min de lectura',
                 '7 min di lettura', '7 min lezen')
_MIN_READ_5 = _t('5 min de lecture', '5 Min. Lesezeit', '5 min de lectura',
                 '5 min di lettura', '5 min lezen')

_ARTICLE_SHARED = {
    'FulcrumGrid Collection — receivables and payments': _OG_ALT_COLLECTION,
    '<a href="/">Home</a>': _HOME,
    'Back to the blog': _BACK_TO_BLOG,
    'Explore Collection': _EXPLORE_COLLECTION,
}

# ---- Article titles reused on the index cards -------------------------------

_T_VS_PAYABLE = _t(
    "Comptes clients ou comptes fournisseurs : quelle est la différence ?",
    'Forderungen vs. Verbindlichkeiten: Was ist der Unterschied?',
    'Cuentas por cobrar vs. cuentas por pagar: ¿cuál es la diferencia?',
    'Crediti verso clienti e debiti verso fornitori: qual è la differenza?',
    'Debiteuren versus crediteuren: wat is het verschil?')

_T_DUNNING = _t(
    "Qu'est-ce que la relance de paiement ? Comment fonctionne le processus de relance",
    'Was ist Mahnwesen? So funktioniert der Mahnprozess',
    '¿Qué es la gestión de cobros? Cómo funciona el proceso de reclamación',
    "Che cos'è il sollecito di pagamento? Come funziona il processo di sollecito",
    'Wat is aanmaning? Hoe het aanmaningsproces werkt')

_T_INVOICE_TERMS = _t(
    'Les conditions de paiement des factures expliquées (Net 30, 2/10 Net 30 &amp; plus)',
    'Zahlungsbedingungen auf Rechnungen erklärt (Net 30, 2/10 Net 30 &amp; mehr)',
    'Las condiciones de pago de facturas explicadas (Net 30, 2/10 Net 30 &amp; más)',
    'Le condizioni di pagamento delle fatture spiegate (Net 30, 2/10 Net 30 &amp; altro)',
    'Betalingsvoorwaarden op facturen uitgelegd (Net 30, 2/10 Net 30 &amp; meer)')

_T_REMINDER_EMAIL = _t(
    'Comment rédiger un e-mail de relance de paiement (avec 5 modèles)',
    'So schreiben Sie eine Zahlungserinnerung per E-Mail (mit 5 Vorlagen)',
    'Cómo redactar un correo de recordatorio de pago (con 5 plantillas)',
    'Come scrivere un\'e-mail di sollecito di pagamento (con 5 modelli)',
    'Hoe u een betalingsherinnering per e-mail schrijft (met 5 sjablonen)')

_T_BEST_PRACTICES = _t(
    'Bonnes pratiques de gestion des comptes clients : une check-list pour être payé à temps',
    'Best Practices für Forderungsmanagement: eine Checkliste, um pünktlich bezahlt zu werden',
    'Buenas prácticas de cuentas por cobrar: una lista de comprobación para cobrar a tiempo',
    'Buone pratiche per la gestione dei crediti: una checklist per farsi pagare puntualmente',
    'Best practices voor debiteurenbeheer: een checklist om op tijd betaald te worden')

_T_REDUCE_DSO = _t(
    'Comment réduire le Days Sales Outstanding (DSO) : 7 étapes pratiques',
    'So senken Sie die Days Sales Outstanding (DSO): 7 praktische Schritte',
    'Cómo reducir los Days Sales Outstanding (DSO): 7 pasos prácticos',
    'Come ridurre i Days Sales Outstanding (DSO): 7 passi pratici',
    'Hoe u de Days Sales Outstanding (DSO) verlaagt: 7 praktische stappen')


PAGE = {
    # =========================================================================
    '/blog/': {
        'src': 'blog/index.html',
        't': {
            # ---- Meta / hero ----
            'Practical guides on operations, receivables, and people operations — from the team building FulcrumGrid\'s business apps.': _t(
                "Des guides pratiques sur les opérations, les créances et la gestion des ressources humaines — par l'équipe qui construit les applications métier de FulcrumGrid.",
                'Praktische Leitfäden zu Betrieb, Forderungen und Personalmanagement — vom Team, das die Business-Apps von FulcrumGrid baut.',
                'Guías prácticas sobre operaciones, cobros y gestión de personas — del equipo que crea las aplicaciones de negocio de FulcrumGrid.',
                'Guide pratiche su operazioni, crediti e gestione del personale — dal team che costruisce le applicazioni aziendali di FulcrumGrid.',
                'Praktische gidsen over operatie, vorderingen en personeelsbeheer — van het team dat de bedrijfsapps van FulcrumGrid bouwt.'),
            'The FulcrumGrid blog — practical guides for operators': _t(
                'Le blog FulcrumGrid — des guides pratiques pour les opérationnels',
                'Der FulcrumGrid-Blog — praktische Leitfäden für Operators',
                'El blog de FulcrumGrid — guías prácticas para operadores',
                'Il blog di FulcrumGrid — guide pratiche per chi gestisce le operazioni',
                'De FulcrumGrid-blog — praktische gidsen voor operators'),
            'Practical guides on operations, receivables, and people operations — from the team building FulcrumGrid.': _t(
                "Des guides pratiques sur les opérations, les créances et la gestion des ressources humaines — par l'équipe qui construit FulcrumGrid.",
                'Praktische Leitfäden zu Betrieb, Forderungen und Personalmanagement — vom Team, das FulcrumGrid baut.',
                'Guías prácticas sobre operaciones, cobros y gestión de personas — del equipo que crea FulcrumGrid.',
                'Guide pratiche su operazioni, crediti e gestione del personale — dal team che costruisce FulcrumGrid.',
                'Praktische gidsen over operatie, vorderingen en personeelsbeheer — van het team dat FulcrumGrid bouwt.'),
            'Practical guides on operations, receivables, and people operations.': _t(
                'Des guides pratiques sur les opérations, les créances et la gestion des ressources humaines.',
                'Praktische Leitfäden zu Betrieb, Forderungen und Personalmanagement.',
                'Guías prácticas sobre operaciones, cobros y gestión de personas.',
                'Guide pratiche su operazioni, crediti e gestione del personale.',
                'Praktische gidsen over operatie, vorderingen en personeelsbeheer.'),
            'The FulcrumGrid blog': _t(
                'Le blog FulcrumGrid', 'Der FulcrumGrid-Blog', 'El blog de FulcrumGrid',
                'Il blog di FulcrumGrid', 'De FulcrumGrid-blog'),
            '<a href="/">Home</a>': _HOME,
            'Resources': _t('Ressources', 'Ressourcen', 'Recursos', 'Risorse', 'Bronnen'),
            'Follow FulcrumGrid on Google — add us to your Preferred Sources': _t(
                'Suivez FulcrumGrid sur Google — ajoutez-nous à vos sources préférées',
                'Folgen Sie FulcrumGrid auf Google — fügen Sie uns zu Ihren bevorzugten Quellen hinzu',
                'Siga a FulcrumGrid en Google — añádanos a sus fuentes preferidas',
                'Segui FulcrumGrid su Google — aggiungici alle tue fonti preferite',
                'Volg FulcrumGrid op Google — voeg ons toe aan uw voorkeursbronnen'),
            # ---- Category tag (Operations only; Collection/HR kept) ----
            '<span class="post-cat">Operations</span>': _t(
                '<span class="post-cat">Opérations</span>',
                '<span class="post-cat">Betrieb</span>',
                '<span class="post-cat">Operaciones</span>',
                '<span class="post-cat">Operazioni</span>',
                '<span class="post-cat">Bedrijfsvoering</span>'),
            # ---- Card titles ----
            "Accounts Receivable vs Accounts Payable: What's the Difference?": _T_VS_PAYABLE,
            "Gross Pay vs Net Pay: What's the Difference?": _t(
                'Salaire brut ou salaire net : quelle est la différence ?',
                'Bruttolohn vs. Nettolohn: Was ist der Unterschied?',
                'Salario bruto vs. salario neto: ¿cuál es la diferencia?',
                'Retribuzione lorda e netta: qual è la differenza?',
                'Brutoloon versus nettoloon: wat is het verschil?'),
            'What Is an Employee Handbook? (And What to Put in It)': _t(
                "Qu'est-ce qu'un livret d'accueil du salarié ? (Et que faut-il y mettre)",
                'Was ist ein Mitarbeiterhandbuch? (Und was gehört hinein)',
                '¿Qué es un manual del empleado? (Y qué incluir en él)',
                "Che cos'è un manuale del dipendente? (E cosa metterci dentro)",
                'Wat is een personeelshandboek? (En wat erin hoort)'),
            'KPIs vs OKRs: What\'s the Difference and When to Use Each': _t(
                'KPI ou OKR : quelle est la différence et quand utiliser chacun',
                'KPIs vs. OKRs: Was ist der Unterschied und wann setzt man welche ein',
                'KPIs vs. OKRs: cuál es la diferencia y cuándo usar cada uno',
                'KPI e OKR: qual è la differenza e quando usare ciascuno',
                'KPI\'s versus OKR\'s: wat is het verschil en wanneer gebruikt u welke'),
            'What Is Dunning? How the Dunning Process Works': _T_DUNNING,
            'How to Calculate PTO Accrual: Formulas, Rates &amp; Examples': _t(
                'Comment calculer le cumul des congés (PTO) : formules, taux &amp; exemples',
                'So berechnen Sie die PTO-Ansammlung: Formeln, Sätze &amp; Beispiele',
                'Cómo calcular la acumulación de PTO: fórmulas, tasas &amp; ejemplos',
                'Come calcolare la maturazione delle ferie (PTO): formule, tassi &amp; esempi',
                'Zo berekent u de PTO-opbouw: formules, tarieven &amp; voorbeelden'),
            'Employee Time Tracking: A Practical Guide': _t(
                'Le suivi du temps des employés : un guide pratique',
                'Arbeitszeiterfassung: ein praktischer Leitfaden',
                'Control horario de los empleados: una guía práctica',
                'Rilevazione delle presenze dei dipendenti: una guida pratica',
                'Tijdregistratie van medewerkers: een praktische gids'),
            "Performance Review Questions: A Manager's Template": _t(
                "Questions d'entretien annuel : un modèle pour le manager",
                'Fragen für das Mitarbeitergespräch: eine Vorlage für Führungskräfte',
                'Preguntas para la evaluación de desempeño: una plantilla para managers',
                'Domande per la valutazione delle performance: un modello per il manager',
                'Vragen voor het functioneringsgesprek: een sjabloon voor managers'),
            'Invoice Payment Terms Explained (Net 30, 2/10 Net 30 &amp; More)': _T_INVOICE_TERMS,
            'How to Write SOPs Your Team Actually Follows': _t(
                'Comment rédiger des SOP que votre équipe suit vraiment',
                'So schreiben Sie SOPs, die Ihr Team wirklich befolgt',
                'Cómo redactar SOPs que su equipo realmente sigue',
                'Come scrivere SOP che il tuo team segue davvero',
                'Hoe u SOP\'s schrijft die uw team echt volgt'),
            'How to Run a Weekly Operations Review (Agenda + Template)': _t(
                'Comment mener une revue hebdomadaire des opérations (ordre du jour + modèle)',
                'So führen Sie ein wöchentliches Operations-Review durch (Agenda + Vorlage)',
                'Cómo dirigir una revisión semanal de operaciones (agenda + plantilla)',
                'Come condurre una revisione settimanale delle operazioni (agenda + modello)',
                'Hoe u een wekelijkse operations-review houdt (agenda + sjabloon)'),
            'How to Write a Payment Reminder Email (with 5 Templates)': _T_REMINDER_EMAIL,
            "How to Build a PTO Policy That's Fair and Simple to Run": _t(
                'Comment bâtir une politique de congés (PTO) équitable et simple à gérer',
                'So gestalten Sie eine PTO-Richtlinie, die fair und einfach zu handhaben ist',
                'Cómo crear una política de PTO justa y sencilla de gestionar',
                'Come costruire una policy sulle ferie (PTO) equa e semplice da gestire',
                'Hoe u een PTO-beleid opstelt dat eerlijk en eenvoudig uit te voeren is'),
            'Accounts Receivable Best Practices: A Checklist for Getting Paid on Time': _T_BEST_PRACTICES,
            'Employee Onboarding Checklist: The First 30 Days': _t(
                "Check-list d'intégration des nouveaux employés : les 30 premiers jours",
                'Onboarding-Checkliste für neue Mitarbeiter: die ersten 30 Tage',
                'Lista de comprobación de incorporación de empleados: los primeros 30 días',
                "Checklist di onboarding dei dipendenti: i primi 30 giorni",
                'Onboarding-checklist voor medewerkers: de eerste 30 dagen'),
            'Spreadsheets vs. Business Software: When to Make the Switch': _t(
                'Tableurs ou logiciels métier : quand faire le changement',
                'Tabellenkalkulation vs. Business-Software: wann der Wechsel lohnt',
                'Hojas de cálculo vs. software de negocio: cuándo dar el paso',
                'Fogli di calcolo o software gestionale: quando fare il passaggio',
                'Spreadsheets versus bedrijfssoftware: wanneer overstappen'),
            'How to Reduce Days Sales Outstanding (DSO): 7 Practical Steps': _T_REDUCE_DSO,
            "HR Software for Small Businesses: A Practical Buyer's Guide": _t(
                "Logiciels RH pour petites entreprises : un guide d'achat pratique",
                'HR-Software für kleine Unternehmen: ein praktischer Kaufratgeber',
                'Software de RR. HH. para pequeñas empresas: una guía de compra práctica',
                "Software HR per piccole imprese: una guida pratica all'acquisto",
                'HR-software voor kleine bedrijven: een praktische aankoopgids'),
            'What to Track in an Operations Dashboard (and What to Ignore)': _t(
                "Que suivre dans un tableau de bord des opérations (et que ignorer)",
                'Was Sie in einem Operations-Dashboard verfolgen sollten (und was nicht)',
                'Qué medir en un panel de operaciones (y qué ignorar)',
                'Cosa monitorare in una dashboard operativa (e cosa ignorare)',
                'Wat u bijhoudt in een operations-dashboard (en wat u negeert)'),
            # ---- Card excerpts ----
            'What AR and AP mean, how they sit on your balance sheet, how they affect cash flow, and how to keep both under control.': _t(
                "Ce que signifient AR et AP, leur place au bilan, leur effet sur la trésorerie et comment garder les deux sous contrôle.",
                'Was AR und AP bedeuten, wie sie in Ihrer Bilanz stehen, wie sie den Cashflow beeinflussen und wie Sie beide im Griff behalten.',
                'Qué significan AR y AP, cómo aparecen en el balance, cómo afectan al flujo de caja y cómo mantener ambos bajo control.',
                'Cosa significano AR e AP, come figurano nel bilancio, come incidono sul flusso di cassa e come tenere entrambi sotto controllo.',
                'Wat AR en AP betekenen, hoe ze op uw balans staan, hoe ze de cashflow beïnvloeden en hoe u beide onder controle houdt.'),
            'What gross pay and net pay mean, the deductions that separate them, and how to work out take-home pay for salaried and hourly staff.': _t(
                'Ce que signifient le salaire brut et le salaire net, les retenues qui les séparent, et comment calculer le net à payer pour les salariés au forfait et à l\'heure.',
                'Was Brutto- und Nettolohn bedeuten, welche Abzüge sie trennen und wie Sie den Nettoverdienst für Fest- und Stundenlöhner berechnen.',
                'Qué significan el salario bruto y el neto, las deducciones que los separan y cómo calcular el sueldo neto para personal asalariado y por horas.',
                'Cosa significano retribuzione lorda e netta, le trattenute che le separano e come calcolare la paga netta per dipendenti a stipendio fisso e a ore.',
                'Wat brutoloon en nettoloon betekenen, de inhoudingen die ze scheiden en hoe u het nettoloon berekent voor vaste en uurmedewerkers.'),
            'What an employee handbook is, why it matters, and a section-by-section list of what belongs in it — from policies and pay to culture and conduct.': _t(
                "Ce qu'est un livret d'accueil du salarié, pourquoi il compte, et une liste section par section de ce qui doit y figurer — des règles et de la paie à la culture et à la conduite.",
                'Was ein Mitarbeiterhandbuch ist, warum es wichtig ist, und eine Liste Abschnitt für Abschnitt, was hineingehört — von Richtlinien und Vergütung bis Kultur und Verhalten.',
                'Qué es un manual del empleado, por qué importa y una lista sección por sección de lo que debe contener — desde políticas y salario hasta cultura y conducta.',
                'Che cos\'è un manuale del dipendente, perché è importante e un elenco sezione per sezione di cosa deve contenere — dalle policy alla retribuzione, dalla cultura alla condotta.',
                'Wat een personeelshandboek is, waarom het ertoe doet en een lijst per onderdeel van wat erin hoort — van beleid en beloning tot cultuur en gedrag.'),
            'What KPIs and OKRs are, how they differ, and when to use ongoing metrics versus goal-setting to run and grow your operation.': _t(
                'Ce que sont les KPI et les OKR, en quoi ils diffèrent, et quand utiliser des indicateurs continus plutôt que la fixation d\'objectifs pour piloter et développer votre activité.',
                'Was KPIs und OKRs sind, wie sie sich unterscheiden und wann Sie laufende Kennzahlen statt Zielsetzung nutzen, um Ihren Betrieb zu steuern und auszubauen.',
                'Qué son los KPIs y los OKRs, en qué se diferencian y cuándo usar métricas continuas frente a la fijación de objetivos para dirigir y hacer crecer su operación.',
                'Cosa sono i KPI e gli OKR, in cosa differiscono e quando usare metriche continue anziché la definizione di obiettivi per gestire e far crescere la tua attività.',
                'Wat KPI\'s en OKR\'s zijn, hoe ze verschillen en wanneer u doorlopende metrieken versus doelstellingen gebruikt om uw operatie te runnen en te laten groeien.'),
            'What dunning means, how the dunning process works, and how to build a reminder sequence that collects overdue invoices without damaging relationships.': _t(
                'Ce que signifie la relance de paiement, comment fonctionne le processus de relance et comment bâtir une séquence de rappels qui recouvre les factures en retard sans nuire aux relations.',
                'Was Mahnwesen bedeutet, wie der Mahnprozess funktioniert und wie Sie eine Erinnerungssequenz aufbauen, die überfällige Rechnungen eintreibt, ohne Beziehungen zu schädigen.',
                'Qué significa la gestión de cobros, cómo funciona el proceso de reclamación y cómo crear una secuencia de recordatorios que cobre las facturas vencidas sin dañar las relaciones.',
                'Cosa significa il sollecito di pagamento, come funziona il processo di sollecito e come costruire una sequenza di promemoria che recupera le fatture scadute senza rovinare i rapporti.',
                'Wat aanmaning betekent, hoe het aanmaningsproces werkt en hoe u een herinneringsreeks opbouwt die achterstallige facturen int zonder relaties te schaden.'),
            'The PTO accrual formula, rates by pay period, hourly vs salaried, and worked examples you can copy — plus a quick FAQ.': _t(
                'La formule de cumul des congés (PTO), les taux par période de paie, à l\'heure ou au forfait, et des exemples concrets à copier — plus une FAQ rapide.',
                'Die PTO-Ansammlungsformel, Sätze je Abrechnungszeitraum, Stunden- vs. Festlohn und durchgerechnete Beispiele zum Kopieren — plus eine kurze FAQ.',
                'La fórmula de acumulación de PTO, las tasas por periodo de pago, por horas vs. asalariado, y ejemplos resueltos que puede copiar — más una breve FAQ.',
                'La formula di maturazione delle ferie (PTO), i tassi per periodo di paga, a ore vs. stipendio fisso, ed esempi svolti da copiare — più una breve FAQ.',
                'De PTO-opbouwformule, tarieven per loonperiode, uur- versus vast dienstverband en uitgewerkte voorbeelden om te kopiëren — plus een korte FAQ.'),
            'How to track employee time without micromanaging — methods, what to log, overtime rules, and how it ties into payroll and PTO.': _t(
                'Comment suivre le temps des employés sans microgestion — méthodes, quoi enregistrer, règles des heures supplémentaires, et le lien avec la paie et les congés (PTO).',
                'So erfassen Sie Arbeitszeit ohne Mikromanagement — Methoden, was zu protokollieren ist, Überstundenregeln und die Verbindung zu Lohn und PTO.',
                'Cómo controlar el tiempo de los empleados sin microgestión — métodos, qué registrar, reglas de horas extra y su vínculo con la nómina y el PTO.',
                'Come monitorare il tempo dei dipendenti senza microgestione — metodi, cosa registrare, regole sugli straordinari e il legame con buste paga e PTO.',
                'Hoe u werktijd van medewerkers bijhoudt zonder micromanagement — methoden, wat te loggen, overurenregels en de link met loon en PTO.'),
            "Ready-to-use self-review, manager, and 1:1 growth questions — plus how to run a review that's fair, specific, and actually useful.": _t(
                'Des questions prêtes à l\'emploi pour l\'auto-évaluation, le manager et les entretiens 1:1 de développement — plus comment mener un entretien juste, précis et vraiment utile.',
                'Sofort einsetzbare Fragen für Selbstbeurteilung, Führungskraft und 1:1-Entwicklungsgespräche — plus wie Sie ein faires, konkretes und wirklich nützliches Gespräch führen.',
                'Preguntas listas para usar de autoevaluación, para el manager y para 1:1 de desarrollo — más cómo dirigir una evaluación justa, concreta y realmente útil.',
                'Domande pronte all\'uso per l\'autovalutazione, per il manager e per i 1:1 di crescita — più come condurre una valutazione equa, concreta e davvero utile.',
                'Kant-en-klare vragen voor zelfevaluatie, manager en 1-op-1-groeigesprekken — plus hoe u een eerlijk, concreet en echt nuttig gesprek voert.'),
            'What Net 30, due on receipt, EOM, and 2/10 Net 30 actually mean — and how to pick terms that keep your cash flowing.': _t(
                'Ce que signifient réellement Net 30, paiement à réception, EOM et 2/10 Net 30 — et comment choisir des conditions qui maintiennent votre trésorerie.',
                'Was Net 30, Zahlung bei Erhalt, EOM und 2/10 Net 30 wirklich bedeuten — und wie Sie Bedingungen wählen, die Ihren Cashflow am Laufen halten.',
                'Qué significan realmente Net 30, pago a la recepción, EOM y 2/10 Net 30 — y cómo elegir condiciones que mantengan su flujo de caja.',
                'Cosa significano davvero Net 30, pagamento alla ricezione, EOM e 2/10 Net 30 — e come scegliere condizioni che mantengono il flusso di cassa.',
                'Wat Net 30, betaling bij ontvangst, EOM en 2/10 Net 30 echt betekenen — en hoe u voorwaarden kiest die uw cashflow op peil houden.'),
            'Format, ownership, review cadence, and the mistakes that turn a standard operating procedure into a document nobody opens.': _t(
                'Format, responsabilité, fréquence de révision, et les erreurs qui transforment une procédure standard en document que personne n\'ouvre.',
                'Format, Verantwortlichkeit, Überprüfungsrhythmus und die Fehler, die eine Standardarbeitsanweisung in ein Dokument verwandeln, das niemand öffnet.',
                'Formato, responsabilidad, cadencia de revisión y los errores que convierten un procedimiento operativo estándar en un documento que nadie abre.',
                'Formato, responsabilità, cadenza di revisione e gli errori che trasformano una procedura operativa standard in un documento che nessuno apre.',
                'Formaat, eigenaarschap, herzieningsritme en de fouten die een standaardwerkinstructie veranderen in een document dat niemand opent.'),
            'A repeatable agenda, the metrics to open with, and the rules that keep the weekly ops review short and decision-focused.': _t(
                'Un ordre du jour reproductible, les indicateurs par lesquels commencer, et les règles qui gardent la revue hebdomadaire courte et centrée sur la décision.',
                'Eine wiederholbare Agenda, die Kennzahlen zum Einstieg und die Regeln, die das wöchentliche Ops-Review kurz und entscheidungsorientiert halten.',
                'Una agenda repetible, las métricas con las que empezar y las reglas que mantienen la revisión semanal breve y centrada en la decisión.',
                'Un\'agenda ripetibile, le metriche con cui aprire e le regole che tengono la revisione settimanale breve e orientata alle decisioni.',
                'Een herhaalbare agenda, de metrieken om mee te openen en de regels die de wekelijkse ops-review kort en besluitgericht houden.'),
            'Tone, timing, and 5 copy-paste templates for polite reminders that actually get invoices paid — before, on, and after the due date.': _t(
                'Le ton, le timing et 5 modèles à copier-coller pour des rappels polis qui font réellement payer les factures — avant, à et après l\'échéance.',
                'Ton, Timing und 5 Copy-and-paste-Vorlagen für höfliche Erinnerungen, die Rechnungen wirklich bezahlt machen — vor, an und nach dem Fälligkeitsdatum.',
                'Tono, momento y 5 plantillas para copiar y pegar de recordatorios corteses que de verdad hacen cobrar las facturas — antes, en y después del vencimiento.',
                'Tono, tempistica e 5 modelli pronti da copiare per promemoria cortesi che fanno davvero pagare le fatture — prima, alla e dopo la scadenza.',
                'Toon, timing en 5 kant-en-klare sjablonen voor beleefde herinneringen die facturen echt betaald krijgen — voor, op en na de vervaldatum.'),
            'Accrual vs. lump sum, carryover, approvals — the decisions behind a paid time off policy people trust and you can actually run.': _t(
                'Cumul ou attribution en bloc, report, approbations — les décisions derrière une politique de congés payés à laquelle on fait confiance et que vous pouvez réellement gérer.',
                'Ansammlung vs. Einmalgutschrift, Übertrag, Genehmigungen — die Entscheidungen hinter einer Urlaubsrichtlinie, der man vertraut und die Sie wirklich umsetzen können.',
                'Acumulación vs. asignación única, arrastre, aprobaciones — las decisiones tras una política de días libres retribuidos en la que se confía y que puede gestionar de verdad.',
                'Maturazione vs. assegnazione in blocco, riporto, approvazioni — le decisioni dietro una policy sulle ferie retribuite di cui ci si fida e che puoi davvero gestire.',
                'Opbouw versus vast bedrag, overdracht, goedkeuringen — de beslissingen achter een verlofbeleid dat vertrouwd wordt en dat u echt kunt uitvoeren.'),
            'Invoicing, follow-up, reconciliation, reporting — the habits that keep cash flowing and receivables under control.': _t(
                'Facturation, relance, rapprochement, reporting — les habitudes qui maintiennent la trésorerie et gardent les créances sous contrôle.',
                'Rechnungsstellung, Nachfassen, Abstimmung, Reporting — die Gewohnheiten, die den Cashflow am Laufen und Forderungen unter Kontrolle halten.',
                'Facturación, seguimiento, conciliación, informes — los hábitos que mantienen el flujo de caja y los cobros bajo control.',
                'Fatturazione, solleciti, riconciliazione, reporting — le abitudini che mantengono il flusso di cassa e i crediti sotto controllo.',
                'Factureren, opvolgen, afletten, rapporteren — de gewoonten die de cashflow op gang en vorderingen onder controle houden.'),
            'From before day one to the first 30 days — the steps that get new hires productive faster and keep them.': _t(
                'De la veille du premier jour aux 30 premiers jours — les étapes qui rendent les nouveaux plus vite productifs et qui les fidélisent.',
                'Von vor dem ersten Tag bis zu den ersten 30 Tagen — die Schritte, die neue Mitarbeiter schneller produktiv machen und halten.',
                'Desde antes del primer día hasta los primeros 30 días — los pasos que hacen productivos antes a los nuevos empleados y los retienen.',
                'Da prima del primo giorno ai primi 30 giorni — i passi che rendono produttivi più in fretta i nuovi assunti e li trattengono.',
                'Van vóór dag één tot de eerste 30 dagen — de stappen die nieuwe medewerkers sneller productief maken en behouden.'),
            "Every business starts in a spreadsheet. Here's how to tell when you've outgrown it — and how to switch without the disruption.": _t(
                'Toute entreprise commence dans un tableur. Voici comment savoir que vous l\'avez dépassé — et comment changer sans perturbation.',
                'Jedes Unternehmen beginnt in einer Tabelle. So erkennen Sie, wann Sie ihr entwachsen sind — und wie Sie ohne Störung wechseln.',
                'Todo negocio empieza en una hoja de cálculo. Así sabrá cuándo se le ha quedado pequeña — y cómo cambiar sin interrupciones.',
                'Ogni azienda inizia in un foglio di calcolo. Ecco come capire quando lo hai superato — e come cambiare senza disagi.',
                'Elk bedrijf begint in een spreadsheet. Zo weet u wanneer u eruit bent gegroeid — en hoe u overstapt zonder verstoring.'),
            "DSO is the clearest signal of how fast you turn invoices into cash. Here's how to bring it down — without hiring a bigger team.": _t(
                'Le DSO est le signal le plus clair de la vitesse à laquelle vous transformez les factures en trésorerie. Voici comment le réduire — sans embaucher une plus grande équipe.',
                'Der DSO ist das klarste Signal dafür, wie schnell Sie Rechnungen in Bargeld verwandeln. So senken Sie ihn — ohne ein größeres Team einzustellen.',
                'El DSO es la señal más clara de la rapidez con que convierte las facturas en efectivo. Así lo reduce — sin contratar un equipo más grande.',
                'Il DSO è il segnale più chiaro della velocità con cui trasformi le fatture in liquidità. Ecco come ridurlo — senza assumere un team più grande.',
                'De DSO is het duidelijkste signaal van hoe snel u facturen in geld omzet. Zo brengt u hem omlaag — zonder een groter team aan te nemen.'),
            "The features that actually matter when you're choosing your first HR system — and the ones you can safely skip.": _t(
                'Les fonctionnalités qui comptent vraiment au moment de choisir votre premier système RH — et celles que vous pouvez ignorer sans risque.',
                'Die Funktionen, die beim Auswählen Ihres ersten HR-Systems wirklich zählen — und jene, die Sie bedenkenlos weglassen können.',
                'Las funciones que de verdad importan al elegir su primer sistema de RR. HH. — y las que puede omitir sin problema.',
                'Le funzionalità che contano davvero quando scegli il tuo primo sistema HR — e quelle che puoi tranquillamente tralasciare.',
                'De functies die er echt toe doen bij het kiezen van uw eerste HR-systeem — en die welke u gerust kunt overslaan.'),
            "A dashboard full of numbers isn't the goal. Here are the operational metrics that actually drive decisions.": _t(
                'Un tableau de bord rempli de chiffres n\'est pas le but. Voici les indicateurs opérationnels qui guident réellement les décisions.',
                'Ein Dashboard voller Zahlen ist nicht das Ziel. Das sind die operativen Kennzahlen, die Entscheidungen wirklich lenken.',
                'Un panel lleno de números no es el objetivo. Estas son las métricas operativas que de verdad impulsan las decisiones.',
                'Una dashboard piena di numeri non è l\'obiettivo. Ecco le metriche operative che guidano davvero le decisioni.',
                'Een dashboard vol cijfers is niet het doel. Dit zijn de operationele metrieken die beslissingen echt sturen.'),
            # ---- Reading time ----
            '6 min read': _MIN_READ_6,
            '7 min read': _MIN_READ_7,
            '5 min read': _MIN_READ_5,
            # ---- Card dates ----
            'Sep 15, 2026': _t('15 sept. 2026', '15. Sep. 2026', '15 sept. 2026', '15 set. 2026', '15 sep. 2026'),
            'Sep 14, 2026': _t('14 sept. 2026', '14. Sep. 2026', '14 sept. 2026', '14 set. 2026', '14 sep. 2026'),
            'Sep 13, 2026': _t('13 sept. 2026', '13. Sep. 2026', '13 sept. 2026', '13 set. 2026', '13 sep. 2026'),
            'Sep 12, 2026': _t('12 sept. 2026', '12. Sep. 2026', '12 sept. 2026', '12 set. 2026', '12 sep. 2026'),
            'Sep 11, 2026': _t('11 sept. 2026', '11. Sep. 2026', '11 sept. 2026', '11 set. 2026', '11 sep. 2026'),
            'Sep 9, 2026': _t('9 sept. 2026', '9. Sep. 2026', '9 sept. 2026', '9 set. 2026', '9 sep. 2026'),
            'Sep 7, 2026': _t('7 sept. 2026', '7. Sep. 2026', '7 sept. 2026', '7 set. 2026', '7 sep. 2026'),
            'Sep 1, 2026': _t('1 sept. 2026', '1. Sep. 2026', '1 sept. 2026', '1 set. 2026', '1 sep. 2026'),
            'Aug 31, 2026': _t('31 août 2026', '31. Aug. 2026', '31 ago. 2026', '31 ago. 2026', '31 aug. 2026'),
            'Aug 30, 2026': _t('30 août 2026', '30. Aug. 2026', '30 ago. 2026', '30 ago. 2026', '30 aug. 2026'),
            'Aug 25, 2026': _t('25 août 2026', '25. Aug. 2026', '25 ago. 2026', '25 ago. 2026', '25 aug. 2026'),
            'Aug 24, 2026': _t('24 août 2026', '24. Aug. 2026', '24 ago. 2026', '24 ago. 2026', '24 aug. 2026'),
        },
    },

    # =========================================================================
    '/blog/what-is-dunning/': {
        'src': 'blog/what-is-dunning/index.html',
        't': {
            **_ARTICLE_SHARED,
            'September 11, 2026': _t('11 septembre 2026', '11. September 2026', '11 de septiembre de 2026', '11 settembre 2026', '11 september 2026'),
            '6 min read': _MIN_READ_6,
            # ---- Title / meta / og / breadcrumb ----
            'What Is Dunning? How the Dunning Process Works': _T_DUNNING,
            'What dunning means, how a dunning process works, and how to build a polite, effective sequence that collects overdue invoices without losing customers.': _t(
                'Ce que signifie la relance de paiement, comment fonctionne un processus de relance et comment bâtir une séquence polie et efficace qui recouvre les factures en retard sans perdre de clients.',
                'Was Mahnwesen bedeutet, wie ein Mahnprozess funktioniert und wie Sie eine höfliche, wirksame Sequenz aufbauen, die überfällige Rechnungen eintreibt, ohne Kunden zu verlieren.',
                'Qué significa la gestión de cobros, cómo funciona un proceso de reclamación y cómo crear una secuencia cortés y eficaz que cobre las facturas vencidas sin perder clientes.',
                'Cosa significa il sollecito di pagamento, come funziona un processo di sollecito e come costruire una sequenza cortese ed efficace che recupera le fatture scadute senza perdere clienti.',
                'Wat aanmaning betekent, hoe een aanmaningsproces werkt en hoe u een beleefde, doeltreffende reeks opbouwt die achterstallige facturen int zonder klanten te verliezen.'),
            'Dunning is the structured process of chasing overdue invoices. Here is how it works and how to do it well.': _t(
                'La relance de paiement est le processus structuré de recouvrement des factures en retard. Voici comment elle fonctionne et comment bien la mener.',
                'Mahnwesen ist der strukturierte Prozess, überfällige Rechnungen nachzuverfolgen. So funktioniert er und so machen Sie ihn gut.',
                'La gestión de cobros es el proceso estructurado de reclamar las facturas vencidas. Así funciona y así se hace bien.',
                'Il sollecito di pagamento è il processo strutturato per recuperare le fatture scadute. Ecco come funziona e come farlo bene.',
                'Aanmaning is het gestructureerde proces om achterstallige facturen op te volgen. Zo werkt het en zo doet u het goed.'),
            'What is dunning?': _t("Qu'est-ce que la relance de paiement ?", 'Was ist Mahnwesen?', '¿Qué es la gestión de cobros?', "Che cos'è il sollecito di pagamento?", 'Wat is aanmaning?'),
            # ---- Body ----
            '"Dunning" is an old word for a modern problem: getting paid for invoices that have gone past due. A dunning process is simply the structured, repeatable way a business follows up on overdue payments — the sequence of reminders that turns "we\'ll pay soon" into money in the account. Done with a system, it collects more and strains fewer relationships.': _t(
                '« Relance » désigne une réalité simple : se faire payer les factures qui ont dépassé leur échéance. Un processus de relance n\'est que la manière structurée et reproductible dont une entreprise suit les paiements en retard — la séquence de rappels qui transforme « on paie bientôt » en argent sur le compte. Mené avec un système, il recouvre davantage et tend moins les relations.',
                'Mahnwesen steht für ein einfaches Ziel: für Rechnungen bezahlt zu werden, deren Frist verstrichen ist. Ein Mahnprozess ist lediglich die strukturierte, wiederholbare Art, wie ein Unternehmen überfälligen Zahlungen nachgeht — die Sequenz von Erinnerungen, die aus „wir zahlen bald" Geld auf dem Konto macht. Mit einem System durchgeführt, treibt er mehr ein und belastet weniger Beziehungen.',
                '«Reclamar» describe una realidad sencilla: cobrar las facturas que han pasado su vencimiento. Un proceso de reclamación no es más que la forma estructurada y repetible en que una empresa da seguimiento a los pagos vencidos — la secuencia de recordatorios que convierte «pagamos pronto» en dinero en la cuenta. Hecho con un sistema, cobra más y tensa menos las relaciones.',
                '«Sollecitare» descrive una realtà semplice: farsi pagare le fatture che hanno superato la scadenza. Un processo di sollecito non è altro che il modo strutturato e ripetibile con cui un\'azienda dà seguito ai pagamenti scaduti — la sequenza di promemoria che trasforma «paghiamo presto» in denaro sul conto. Fatto con un sistema, recupera di più e logora meno i rapporti.',
                '«Aanmanen» beschrijft een eenvoudig doel: betaald worden voor facturen die de vervaldatum voorbij zijn. Een aanmaningsproces is simpelweg de gestructureerde, herhaalbare manier waarop een bedrijf achterstallige betalingen opvolgt — de reeks herinneringen die «we betalen snel» omzet in geld op de rekening. Met een systeem uitgevoerd, int het meer en belast het minder relaties.'),
            'What does "dunning" mean?': _t('Que signifie « relance de paiement » ?', 'Was bedeutet „Mahnwesen"?', '¿Qué significa «gestión de cobros»?', 'Cosa significa «sollecito di pagamento»?', 'Wat betekent «aanmaning»?'),
            'Dunning is the process of communicating with customers to collect money they owe on overdue invoices. A "dunning notice" or "dunning letter" is one of those reminders. The term is old, but the idea is everyday accounts-receivable work: following up, consistently and politely, until an invoice is paid.': _t(
                'La relance de paiement est le processus qui consiste à communiquer avec les clients pour recouvrer les sommes dues sur des factures en retard. Un « avis de relance » ou une « lettre de relance » est l\'un de ces rappels. Le terme est ancien, mais l\'idée relève du quotidien de la gestion des comptes clients : relancer, avec constance et courtoisie, jusqu\'à ce qu\'une facture soit payée.',
                'Mahnwesen ist der Prozess, mit Kunden zu kommunizieren, um Geld einzutreiben, das sie auf überfällige Rechnungen schulden. Ein „Mahnschreiben" oder eine „Mahnung" ist eine dieser Erinnerungen. Der Begriff ist alt, doch die Idee ist alltägliche Debitorenarbeit: konsequent und höflich nachzufassen, bis eine Rechnung bezahlt ist.',
                'La gestión de cobros es el proceso de comunicarse con los clientes para cobrar el dinero que adeudan en facturas vencidas. Un «aviso de reclamación» o una «carta de reclamación» es uno de esos recordatorios. El término es antiguo, pero la idea es el trabajo cotidiano de las cuentas por cobrar: dar seguimiento, con constancia y cortesía, hasta que una factura se paga.',
                'Il sollecito di pagamento è il processo di comunicare con i clienti per recuperare il denaro che devono su fatture scadute. Un «avviso di sollecito» o una «lettera di sollecito» è uno di questi promemoria. Il termine è antico, ma l\'idea è il lavoro quotidiano sui crediti verso clienti: dare seguito, con costanza e cortesia, finché una fattura non è pagata.',
                'Aanmaning is het proces van communiceren met klanten om geld te innen dat zij verschuldigd zijn op achterstallige facturen. Een «aanmaning» of «aanmaningsbrief» is een van die herinneringen. De term is oud, maar het idee is alledaags debiteurenwerk: consistent en beleefd opvolgen totdat een factuur betaald is.'),
            'How the dunning process works': _t('Comment fonctionne le processus de relance', 'So funktioniert der Mahnprozess', 'Cómo funciona el proceso de reclamación', 'Come funziona il processo di sollecito', 'Hoe het aanmaningsproces werkt'),
            'A dunning process is a planned sequence of reminders that escalate gently over time. A typical flow:': _t(
                'Un processus de relance est une séquence planifiée de rappels qui montent en intensité progressivement. Un déroulé typique :',
                'Ein Mahnprozess ist eine geplante Sequenz von Erinnerungen, die im Lauf der Zeit sanft eskalieren. Ein typischer Ablauf:',
                'Un proceso de reclamación es una secuencia planificada de recordatorios que se intensifican poco a poco con el tiempo. Un flujo típico:',
                'Un processo di sollecito è una sequenza pianificata di promemoria che si intensificano gradualmente nel tempo. Un flusso tipico:',
                'Een aanmaningsproces is een geplande reeks herinneringen die in de loop van de tijd geleidelijk oplopen. Een typisch verloop:'),
            '<strong>Before due date</strong> — a friendly heads-up that payment is coming up.': _t(
                '<strong>Avant l\'échéance</strong> — un rappel amical annonçant que le paiement approche.',
                '<strong>Vor dem Fälligkeitsdatum</strong> — ein freundlicher Hinweis, dass die Zahlung ansteht.',
                '<strong>Antes del vencimiento</strong> — un aviso amable de que el pago se acerca.',
                '<strong>Prima della scadenza</strong> — un avviso cordiale che il pagamento è imminente.',
                '<strong>Vóór de vervaldatum</strong> — een vriendelijke heads-up dat de betaling eraan komt.'),
            '<strong>On the due date</strong> — a simple "it\'s due today" note with a payment link.': _t(
                '<strong>Le jour de l\'échéance</strong> — un simple message « c\'est dû aujourd\'hui » avec un lien de paiement.',
                '<strong>Am Fälligkeitstag</strong> — eine schlichte „heute fällig"-Notiz mit einem Zahlungslink.',
                '<strong>El día del vencimiento</strong> — una simple nota de «vence hoy» con un enlace de pago.',
                '<strong>Il giorno della scadenza</strong> — una semplice nota «scade oggi» con un link di pagamento.',
                '<strong>Op de vervaldatum</strong> — een eenvoudige «vandaag verschuldigd»-notitie met een betaallink.'),
            '<strong>A few days overdue</strong> — a polite reminder that the invoice is now past due.': _t(
                '<strong>Quelques jours de retard</strong> — un rappel poli indiquant que la facture est maintenant en retard.',
                '<strong>Einige Tage überfällig</strong> — eine höfliche Erinnerung, dass die Rechnung nun überfällig ist.',
                '<strong>Unos días de retraso</strong> — un recordatorio cortés de que la factura ya está vencida.',
                '<strong>Qualche giorno di ritardo</strong> — un promemoria cortese che la fattura è ormai scaduta.',
                '<strong>Enkele dagen te laat</strong> — een beleefde herinnering dat de factuur nu achterstallig is.'),
            '<strong>Further overdue</strong> — a firmer message referencing your terms and any late fee.': _t(
                '<strong>Retard plus marqué</strong> — un message plus ferme rappelant vos conditions et toute pénalité de retard.',
                '<strong>Weiter überfällig</strong> — eine bestimmtere Nachricht mit Verweis auf Ihre Bedingungen und etwaige Verzugsgebühren.',
                '<strong>Más vencida</strong> — un mensaje más firme que menciona sus condiciones y cualquier recargo por mora.',
                '<strong>Ulteriore ritardo</strong> — un messaggio più fermo che richiama le tue condizioni e le eventuali penali di mora.',
                '<strong>Verder achterstallig</strong> — een striktere boodschap die verwijst naar uw voorwaarden en eventuele boete voor te laat betalen.'),
            '<strong>Final notice</strong> — a clear statement of next steps before escalation.': _t(
                '<strong>Avis final</strong> — un exposé clair des prochaines étapes avant escalade.',
                '<strong>Letzte Mahnung</strong> — eine klare Darstellung der nächsten Schritte vor der Eskalation.',
                '<strong>Aviso final</strong> — una declaración clara de los próximos pasos antes de escalar.',
                '<strong>Avviso finale</strong> — un\'esposizione chiara dei prossimi passi prima dell\'escalation.',
                '<strong>Laatste aanmaning</strong> — een duidelijke uiteenzetting van de volgende stappen vóór escalatie.'),
            'Each step keeps the same clarity: which invoice, how much, and a one-click way to pay.': _t(
                'Chaque étape garde la même clarté : quelle facture, quel montant, et un moyen de payer en un clic.',
                'Jeder Schritt behält dieselbe Klarheit: welche Rechnung, wie viel und eine Zahlmöglichkeit mit einem Klick.',
                'Cada paso mantiene la misma claridad: qué factura, cuánto y una forma de pagar con un clic.',
                'Ogni passaggio mantiene la stessa chiarezza: quale fattura, quanto e un modo per pagare con un clic.',
                'Elke stap behoudt dezelfde helderheid: welke factuur, hoeveel en een manier om met één klik te betalen.'),
            'Automated vs manual dunning': _t('Relance automatisée ou manuelle', 'Automatisiertes vs. manuelles Mahnwesen', 'Reclamación automatizada vs. manual', 'Sollecito automatizzato vs. manuale', 'Geautomatiseerd versus handmatig aanmanen'),
            'Manual dunning — chasing each invoice by hand — works until you have more than a handful of customers, then it slips. Automated dunning sends the right message at the right interval on its own, so nothing falls through the cracks and no one has to remember to follow up. Automation also keeps the tone consistent and the timing disciplined, which is exactly what collects.': _t(
                'La relance manuelle — suivre chaque facture à la main — fonctionne jusqu\'à ce que vous ayez plus d\'une poignée de clients, puis elle déraille. La relance automatisée envoie le bon message au bon intervalle d\'elle-même, si bien que rien ne passe entre les mailles et que personne n\'a à penser à relancer. L\'automatisation garde aussi le ton constant et le timing rigoureux, ce qui est précisément ce qui recouvre.',
                'Manuelles Mahnen — jede Rechnung von Hand nachzuverfolgen — funktioniert, bis Sie mehr als eine Handvoll Kunden haben, dann gerät es ins Rutschen. Automatisiertes Mahnen sendet von selbst die richtige Nachricht im richtigen Abstand, sodass nichts durchrutscht und niemand ans Nachfassen denken muss. Die Automatisierung hält zudem den Ton konsistent und das Timing diszipliniert — genau das, was eintreibt.',
                'La reclamación manual — perseguir cada factura a mano — funciona hasta que tiene más de un puñado de clientes; entonces se descontrola. La reclamación automatizada envía por sí sola el mensaje correcto en el intervalo correcto, de modo que nada se escapa y nadie tiene que acordarse de dar seguimiento. La automatización también mantiene el tono constante y el ritmo disciplinado, que es justo lo que cobra.',
                'Il sollecito manuale — inseguire ogni fattura a mano — funziona finché non hai più di una manciata di clienti, poi sfugge di mano. Il sollecito automatizzato invia da solo il messaggio giusto all\'intervallo giusto, così nulla cade nelle crepe e nessuno deve ricordarsi di dare seguito. L\'automazione mantiene anche il tono coerente e la tempistica disciplinata, che è esattamente ciò che fa incassare.',
                'Handmatig aanmanen — elke factuur met de hand opvolgen — werkt tot u meer dan een handvol klanten hebt, dan glipt het weg. Geautomatiseerd aanmanen stuurt vanzelf de juiste boodschap op het juiste interval, zodat er niets tussendoor glipt en niemand hoeft te onthouden om op te volgen. Automatisering houdt ook de toon consistent en de timing gedisciplineerd, wat precies is wat int.'),
            'How to dun without damaging relationships': _t('Relancer sans nuire aux relations', 'Wie Sie mahnen, ohne Beziehungen zu schädigen', 'Cómo reclamar sin dañar las relaciones', 'Come sollecitare senza rovinare i rapporti', 'Hoe u aanmaant zonder relaties te schaden'),
            '<strong>Stay polite early.</strong> Most late payment is an oversight, not a refusal — assume good faith at first.': _t(
                '<strong>Restez poli au début.</strong> La plupart des retards de paiement sont un oubli, pas un refus — présumez la bonne foi au départ.',
                '<strong>Bleiben Sie anfangs höflich.</strong> Die meisten verspäteten Zahlungen sind ein Versehen, keine Verweigerung — gehen Sie zunächst von gutem Willen aus.',
                '<strong>Sea cortés al principio.</strong> La mayoría de los pagos tardíos son un descuido, no una negativa — presuma buena fe al inicio.',
                '<strong>Rimani cortese all\'inizio.</strong> La maggior parte dei ritardi di pagamento è una dimenticanza, non un rifiuto — presumi la buona fede all\'inizio.',
                '<strong>Blijf in het begin beleefd.</strong> De meeste late betalingen zijn een vergissing, geen weigering — ga eerst uit van goede trouw.'),
            '<strong>Be specific.</strong> Every message should name the invoice, amount, due date, and payment link.': _t(
                '<strong>Soyez précis.</strong> Chaque message doit indiquer la facture, le montant, l\'échéance et le lien de paiement.',
                '<strong>Seien Sie konkret.</strong> Jede Nachricht sollte Rechnung, Betrag, Fälligkeitsdatum und Zahlungslink nennen.',
                '<strong>Sea específico.</strong> Cada mensaje debe indicar la factura, el importe, el vencimiento y el enlace de pago.',
                '<strong>Sii specifico.</strong> Ogni messaggio dovrebbe indicare la fattura, l\'importo, la scadenza e il link di pagamento.',
                '<strong>Wees specifiek.</strong> Elk bericht moet de factuur, het bedrag, de vervaldatum en de betaallink noemen.'),
            '<strong>Escalate on a schedule</strong>, not on emotion — consistency reads as professional, not aggressive.': _t(
                '<strong>Faites monter le ton selon un calendrier</strong>, pas selon l\'émotion — la constance est perçue comme professionnelle, pas agressive.',
                '<strong>Eskalieren Sie nach Zeitplan</strong>, nicht nach Emotion — Konsequenz wirkt professionell, nicht aggressiv.',
                '<strong>Escale según un calendario</strong>, no según la emoción — la constancia se percibe como profesional, no agresiva.',
                '<strong>Aumenta la pressione secondo un calendario</strong>, non secondo l\'emozione — la costanza appare professionale, non aggressiva.',
                '<strong>Escaleer volgens een schema</strong>, niet op emotie — consistentie komt professioneel over, niet agressief.'),
            '<strong>Make paying trivially easy</strong> — a payment link beats "please remit to…" every time.': _t(
                '<strong>Rendez le paiement extrêmement simple</strong> — un lien de paiement l\'emporte à chaque fois sur « veuillez régler à… ».',
                '<strong>Machen Sie das Bezahlen kinderleicht</strong> — ein Zahlungslink schlägt „bitte überweisen Sie an…" jedes Mal.',
                '<strong>Haga que pagar sea trivialmente fácil</strong> — un enlace de pago le gana a «sírvase remitir a…» siempre.',
                '<strong>Rendi il pagamento estremamente facile</strong> — un link di pagamento batte «si prega di rimettere a…» ogni volta.',
                '<strong>Maak betalen kinderlijk eenvoudig</strong> — een betaallink verslaat «gelieve over te maken naar…» elke keer.'),
            'When dunning is not enough': _t('Quand la relance ne suffit pas', 'Wenn Mahnen nicht genügt', 'Cuando reclamar no basta', 'Quando il sollecito non basta', 'Wanneer aanmanen niet genoeg is'),
            'If a full sequence passes with no response and no dialogue, it is time to escalate — a phone call, a payment plan, pausing further work, or, as a last resort, a formal collections or legal route. A good dunning process makes this rare by catching most late payers early and giving them an easy way to pay.': _t(
                'Si une séquence complète s\'écoule sans réponse ni dialogue, il est temps d\'escalader — un appel téléphonique, un échéancier, la suspension des travaux ou, en dernier recours, une voie de recouvrement formelle ou juridique. Un bon processus de relance rend cela rare en repérant tôt la plupart des mauvais payeurs et en leur offrant un moyen simple de payer.',
                'Verstreicht eine vollständige Sequenz ohne Reaktion und ohne Dialog, ist es Zeit zu eskalieren — ein Telefonat, ein Zahlungsplan, das Aussetzen weiterer Arbeit oder, als letztes Mittel, ein formeller Inkasso- oder Rechtsweg. Ein guter Mahnprozess macht das selten, weil er die meisten Spätzahler früh erfasst und ihnen einen einfachen Zahlweg gibt.',
                'Si una secuencia completa transcurre sin respuesta ni diálogo, es hora de escalar — una llamada, un plan de pago, pausar más trabajo o, como último recurso, una vía formal de cobro o legal. Un buen proceso de reclamación hace que esto sea raro al detectar pronto a la mayoría de los morosos y darles una forma fácil de pagar.',
                'Se un\'intera sequenza passa senza risposta né dialogo, è tempo di procedere all\'escalation — una telefonata, un piano di pagamento, la sospensione di ulteriore lavoro o, come ultima risorsa, una via formale di recupero o legale. Un buon processo di sollecito rende ciò raro individuando presto la maggior parte dei cattivi pagatori e offrendo loro un modo semplice di pagare.',
                'Als een volledige reeks verstrijkt zonder reactie en zonder dialoog, is het tijd om te escaleren — een telefoontje, een betalingsregeling, verder werk pauzeren of, als laatste redmiddel, een formele incasso- of juridische route. Een goed aanmaningsproces maakt dit zeldzaam door de meeste wanbetalers vroeg te signaleren en hun een eenvoudige manier van betalen te bieden.'),
            'Frequently asked questions': _t('Foire aux questions', 'Häufig gestellte Fragen', 'Preguntas frecuentes', 'Domande frequenti', 'Veelgestelde vragen'),
            'What is a dunning notice?': _t("Qu'est-ce qu'un avis de relance ?", 'Was ist ein Mahnschreiben?', '¿Qué es un aviso de reclamación?', "Che cos'è un avviso di sollecito?", 'Wat is een aanmaning?'),
            'A dunning notice is a reminder sent to a customer about an overdue invoice. It states which invoice is unpaid, the amount, and how to pay, and it is usually one step in a larger dunning sequence that escalates over time.': _t(
                'Un avis de relance est un rappel envoyé à un client au sujet d\'une facture en retard. Il précise quelle facture est impayée, le montant et comment payer, et constitue généralement une étape d\'une séquence de relance plus large qui monte en intensité au fil du temps.',
                'Ein Mahnschreiben ist eine Erinnerung an einen Kunden zu einer überfälligen Rechnung. Es nennt, welche Rechnung offen ist, den Betrag und wie zu zahlen ist, und ist meist ein Schritt in einer größeren Mahnsequenz, die mit der Zeit eskaliert.',
                'Un aviso de reclamación es un recordatorio enviado a un cliente sobre una factura vencida. Indica qué factura está impagada, el importe y cómo pagar, y suele ser un paso de una secuencia de reclamación más amplia que se intensifica con el tiempo.',
                'Un avviso di sollecito è un promemoria inviato a un cliente riguardo a una fattura scaduta. Indica quale fattura è insoluta, l\'importo e come pagare, ed è di solito un passaggio di una sequenza di sollecito più ampia che si intensifica nel tempo.',
                'Een aanmaning is een herinnering die aan een klant wordt gestuurd over een achterstallige factuur. Ze vermeldt welke factuur onbetaald is, het bedrag en hoe te betalen, en is meestal één stap in een grotere aanmaningsreeks die na verloop van tijd oploopt.'),
            'What is the difference between dunning and collections?': _t('Quelle est la différence entre relance et recouvrement ?', 'Was ist der Unterschied zwischen Mahnwesen und Inkasso?', '¿Cuál es la diferencia entre reclamación y recobro?', 'Qual è la differenza tra sollecito e recupero crediti?', 'Wat is het verschil tussen aanmanen en incasso?'),
            'Dunning is the routine, in-house process of reminding customers about overdue invoices. Collections usually refers to a later, more formal stage — often involving a dedicated team or an outside agency — once normal reminders have failed.': _t(
                'La relance est le processus courant, mené en interne, qui consiste à rappeler aux clients leurs factures en retard. Le recouvrement désigne généralement une étape ultérieure et plus formelle — impliquant souvent une équipe dédiée ou une agence externe — une fois que les rappels ordinaires ont échoué.',
                'Mahnwesen ist der routinemäßige, interne Prozess, Kunden an überfällige Rechnungen zu erinnern. Inkasso bezeichnet meist eine spätere, formellere Stufe — oft mit einem eigenen Team oder einer externen Agentur —, wenn normale Erinnerungen gescheitert sind.',
                'La reclamación es el proceso rutinario e interno de recordar a los clientes sus facturas vencidas. El recobro suele referirse a una etapa posterior y más formal — a menudo con un equipo dedicado o una agencia externa — una vez que los recordatorios normales han fallado.',
                'Il sollecito è il processo di routine, interno, di ricordare ai clienti le fatture scadute. Il recupero crediti di solito indica una fase successiva e più formale — spesso con un team dedicato o un\'agenzia esterna — quando i normali promemoria hanno fallito.',
                'Aanmanen is het routinematige, interne proces om klanten aan achterstallige facturen te herinneren. Incasso verwijst meestal naar een latere, formelere fase — vaak met een specifiek team of een extern bureau — zodra gewone herinneringen zijn mislukt.'),
            'How many dunning reminders should you send?': _t('Combien de rappels de relance faut-il envoyer ?', 'Wie viele Mahnungen sollten Sie senden?', '¿Cuántos recordatorios de reclamación conviene enviar?', 'Quanti solleciti conviene inviare?', 'Hoeveel aanmaningen moet u sturen?'),
            'There is no fixed number, but a common sequence is four to five messages — a pre-due reminder, a due-date note, and two or three escalating follow-ups — ending with a clear final notice before you escalate further.': _t(
                'Il n\'y a pas de nombre fixe, mais une séquence courante compte quatre à cinq messages — un rappel avant échéance, une note le jour de l\'échéance et deux ou trois relances en escalade — se terminant par un avis final clair avant d\'aller plus loin.',
                'Es gibt keine feste Zahl, aber eine gängige Sequenz umfasst vier bis fünf Nachrichten — eine Erinnerung vor Fälligkeit, eine Notiz am Fälligkeitstag und zwei bis drei eskalierende Nachfassaktionen — abgeschlossen mit einer klaren letzten Mahnung, bevor Sie weiter eskalieren.',
                'No hay un número fijo, pero una secuencia habitual son cuatro o cinco mensajes — un recordatorio previo al vencimiento, una nota el día del vencimiento y dos o tres seguimientos en escalada — que termina con un aviso final claro antes de escalar más.',
                'Non c\'è un numero fisso, ma una sequenza comune conta da quattro a cinque messaggi — un promemoria prima della scadenza, una nota il giorno della scadenza e due o tre solleciti in escalation — che si chiude con un chiaro avviso finale prima di procedere oltre.',
                'Er is geen vast aantal, maar een gangbare reeks bestaat uit vier tot vijf berichten — een herinnering vóór de vervaldatum, een notitie op de vervaldatum en twee of drie oplopende opvolgingen — eindigend met een duidelijke laatste aanmaning voordat u verder escaleert.'),
            'Dunning is one piece of getting paid on time — see our guides to <a href="/blog/payment-reminder-email/">writing payment reminder emails</a>, <a href="/blog/accounts-receivable-best-practices/">accounts receivable best practices</a>, and <a href="/blog/reduce-days-sales-outstanding/">reducing days sales outstanding</a>.': _t(
                'La relance n\'est qu\'un maillon pour être payé à temps — consultez nos guides sur <a href="/blog/payment-reminder-email/">la rédaction d\'e-mails de relance de paiement</a>, les <a href="/blog/accounts-receivable-best-practices/">bonnes pratiques de gestion des comptes clients</a> et la <a href="/blog/reduce-days-sales-outstanding/">réduction du Days Sales Outstanding</a>.',
                'Mahnwesen ist nur ein Baustein, um pünktlich bezahlt zu werden — sehen Sie unsere Leitfäden zum <a href="/blog/payment-reminder-email/">Schreiben von Zahlungserinnerungen</a>, zu <a href="/blog/accounts-receivable-best-practices/">Best Practices im Forderungsmanagement</a> und zum <a href="/blog/reduce-days-sales-outstanding/">Senken der Days Sales Outstanding</a>.',
                'La reclamación es solo una pieza de cobrar a tiempo — consulte nuestras guías sobre <a href="/blog/payment-reminder-email/">cómo redactar correos de recordatorio de pago</a>, las <a href="/blog/accounts-receivable-best-practices/">buenas prácticas de cuentas por cobrar</a> y la <a href="/blog/reduce-days-sales-outstanding/">reducción de los Days Sales Outstanding</a>.',
                'Il sollecito è solo un tassello del farsi pagare puntualmente — consulta le nostre guide su <a href="/blog/payment-reminder-email/">come scrivere e-mail di sollecito di pagamento</a>, le <a href="/blog/accounts-receivable-best-practices/">buone pratiche per la gestione dei crediti</a> e la <a href="/blog/reduce-days-sales-outstanding/">riduzione dei Days Sales Outstanding</a>.',
                'Aanmanen is maar één onderdeel van op tijd betaald worden — zie onze gidsen over <a href="/blog/payment-reminder-email/">het schrijven van betalingsherinneringen</a>, <a href="/blog/accounts-receivable-best-practices/">best practices voor debiteurenbeheer</a> en het <a href="/blog/reduce-days-sales-outstanding/">verlagen van de days sales outstanding</a>.'),
            'Put your dunning on autopilot': _t('Mettez votre relance en pilote automatique', 'Bringen Sie Ihr Mahnwesen auf Autopilot', 'Ponga su gestión de cobros en piloto automático', 'Metti i tuoi solleciti in pilota automatico', 'Zet uw aanmaningen op de automatische piloot'),
            'Collection sends the right reminder at the right time for every overdue invoice, tracks who has paid, and keeps the tone consistent — so you collect more without chasing by hand.': _t(
                'Collection envoie le bon rappel au bon moment pour chaque facture en retard, suit qui a payé et garde le ton constant — vous recouvrez donc davantage sans relancer à la main.',
                'Collection sendet für jede überfällige Rechnung die richtige Erinnerung zur richtigen Zeit, verfolgt, wer bezahlt hat, und hält den Ton konsistent — so treiben Sie mehr ein, ohne von Hand nachzufassen.',
                'Collection envía el recordatorio correcto en el momento correcto para cada factura vencida, controla quién ha pagado y mantiene el tono constante — así cobra más sin perseguir a mano.',
                'Collection invia il promemoria giusto al momento giusto per ogni fattura scaduta, tiene traccia di chi ha pagato e mantiene il tono coerente — così incassi di più senza inseguire a mano.',
                'Collection stuurt voor elke achterstallige factuur de juiste herinnering op het juiste moment, houdt bij wie heeft betaald en houdt de toon consistent — zo int u meer zonder handmatig achteraan te zitten.'),
        },
    },

    # =========================================================================
    '/blog/accounts-receivable-best-practices/': {
        'src': 'blog/accounts-receivable-best-practices/index.html',
        't': {
            **_ARTICLE_SHARED,
            'August 25, 2026': _t('25 août 2026', '25. August 2026', '25 de agosto de 2026', '25 agosto 2026', '25 augustus 2026'),
            '6 min read': _MIN_READ_6,
            # ---- Title / meta / breadcrumb ----
            'Accounts Receivable Best Practices': _t(
                'Bonnes pratiques de gestion des comptes clients',
                'Best Practices für Forderungsmanagement',
                'Buenas prácticas de cuentas por cobrar',
                'Buone pratiche per la gestione dei crediti',
                'Best practices voor debiteurenbeheer'),
            'A practical accounts receivable checklist: the invoicing, follow-up, reconciliation, and reporting habits that keep cash flowing and DSO low.': _t(
                'Une check-list pratique pour les comptes clients : les habitudes de facturation, de relance, de rapprochement et de reporting qui maintiennent la trésorerie et gardent le DSO bas.',
                'Eine praktische Checkliste für Forderungen: die Gewohnheiten bei Rechnungsstellung, Nachfassen, Abstimmung und Reporting, die den Cashflow am Laufen und den DSO niedrig halten.',
                'Una lista de comprobación práctica de cuentas por cobrar: los hábitos de facturación, seguimiento, conciliación e informes que mantienen el flujo de caja y el DSO bajo.',
                'Una checklist pratica per i crediti verso clienti: le abitudini di fatturazione, sollecito, riconciliazione e reporting che mantengono il flusso di cassa e il DSO basso.',
                'Een praktische debiteurenchecklist: de gewoonten voor factureren, opvolgen, afletten en rapporteren die de cashflow op gang en de DSO laag houden.'),
            'Accounts Receivable Best Practices: A Checklist for Getting Paid on Time': _T_BEST_PRACTICES,
            'The invoicing, follow-up, and reporting habits that keep cash flowing and receivables under control.': _t(
                'Les habitudes de facturation, de relance et de reporting qui maintiennent la trésorerie et gardent les créances sous contrôle.',
                'Die Gewohnheiten bei Rechnungsstellung, Nachfassen und Reporting, die den Cashflow am Laufen und Forderungen unter Kontrolle halten.',
                'Los hábitos de facturación, seguimiento e informes que mantienen el flujo de caja y los cobros bajo control.',
                'Le abitudini di fatturazione, sollecito e reporting che mantengono il flusso di cassa e i crediti sotto controllo.',
                'De gewoonten voor factureren, opvolgen en rapporteren die de cashflow op gang en vorderingen onder controle houden.'),
            'Accounts receivable best practices': _t(
                'Bonnes pratiques de gestion des comptes clients',
                'Best Practices im Forderungsmanagement',
                'Buenas prácticas de cuentas por cobrar',
                'Buone pratiche per la gestione dei crediti',
                'Best practices voor debiteurenbeheer'),
            # ---- Body ----
            "Accounts receivable is where a lot of profit quietly leaks out. The sale is made, the work is delivered — and then the money sits in limbo because the invoice went out late, the follow-up never happened, or a small dispute stalled the whole thing. None of that is a customer problem. It's a process problem, and process problems are fixable.": _t(
                'Les comptes clients sont l\'endroit où beaucoup de profit fuit discrètement. La vente est conclue, le travail est livré — puis l\'argent reste en suspens parce que la facture est partie en retard, que la relance n\'a jamais eu lieu ou qu\'un petit litige a tout bloqué. Rien de tout cela n\'est un problème de client. C\'est un problème de processus, et les problèmes de processus se corrigent.',
                'Bei den Forderungen versickert leise viel Gewinn. Der Verkauf ist gemacht, die Arbeit geliefert — und dann bleibt das Geld in der Schwebe, weil die Rechnung zu spät hinausging, das Nachfassen ausblieb oder ein kleiner Streit alles ins Stocken brachte. Nichts davon ist ein Kundenproblem. Es ist ein Prozessproblem, und Prozessprobleme lassen sich beheben.',
                'Las cuentas por cobrar son donde se escapa en silencio mucho beneficio. La venta se cierra, el trabajo se entrega — y luego el dinero queda en el limbo porque la factura salió tarde, el seguimiento nunca ocurrió o una pequeña disputa lo paralizó todo. Nada de eso es un problema del cliente. Es un problema de proceso, y los problemas de proceso tienen solución.',
                'I crediti verso clienti sono il punto in cui molto profitto si disperde silenziosamente. La vendita è conclusa, il lavoro consegnato — e poi il denaro resta in sospeso perché la fattura è partita in ritardo, il sollecito non è mai avvenuto o una piccola contestazione ha bloccato tutto. Nulla di questo è un problema del cliente. È un problema di processo, e i problemi di processo si risolvono.',
                'Bij debiteuren lekt stilletjes veel winst weg. De verkoop is gesloten, het werk geleverd — en dan blijft het geld in het ongewisse omdat de factuur te laat de deur uit ging, de opvolging nooit gebeurde of een klein geschil alles blokkeerde. Niets daarvan is een klantprobleem. Het is een procesprobleem, en procesproblemen zijn oplosbaar.'),
            "Here's a practical checklist of accounts receivable best practices, grouped by stage. Treat it as a standard your team runs every month, not a one-off cleanup.": _t(
                'Voici une check-list pratique de bonnes pratiques de gestion des comptes clients, regroupées par étape. Considérez-la comme un standard que votre équipe applique chaque mois, pas comme un nettoyage ponctuel.',
                'Hier ist eine praktische Checkliste mit Best Practices für das Forderungsmanagement, nach Phasen gruppiert. Betrachten Sie sie als Standard, den Ihr Team jeden Monat durchläuft, nicht als einmalige Aufräumaktion.',
                'Aquí tiene una lista práctica de buenas prácticas de cuentas por cobrar, agrupadas por etapa. Trátela como un estándar que su equipo aplica cada mes, no como una limpieza puntual.',
                'Ecco una checklist pratica di buone pratiche per la gestione dei crediti, raggruppate per fase. Consideratela uno standard che il tuo team applica ogni mese, non una pulizia una tantum.',
                'Hier is een praktische checklist met best practices voor debiteurenbeheer, gegroepeerd per fase. Behandel het als een standaard die uw team elke maand doorloopt, niet als een eenmalige opschoning.'),
            '1. Invoicing': _t('1. Facturation', '1. Rechnungsstellung', '1. Facturación', '1. Fatturazione', '1. Factureren'),
            '<strong>Invoice the moment the work is done.</strong> Every day between delivery and invoice is a day added to your collection cycle for no reason.': _t(
                '<strong>Facturez dès que le travail est terminé.</strong> Chaque jour entre la livraison et la facture est un jour ajouté sans raison à votre cycle de recouvrement.',
                '<strong>Stellen Sie die Rechnung aus, sobald die Arbeit erledigt ist.</strong> Jeder Tag zwischen Lieferung und Rechnung verlängert Ihren Inkassozyklus grundlos um einen Tag.',
                '<strong>Facture en cuanto el trabajo esté hecho.</strong> Cada día entre la entrega y la factura es un día añadido sin motivo a su ciclo de cobro.',
                '<strong>Fattura nel momento in cui il lavoro è concluso.</strong> Ogni giorno tra la consegna e la fattura è un giorno aggiunto senza motivo al tuo ciclo di incasso.',
                '<strong>Factureer zodra het werk klaar is.</strong> Elke dag tussen levering en factuur is een dag die zonder reden aan uw incassocyclus wordt toegevoegd.'),
            '<strong>Make invoices unambiguous.</strong> Clear line items, the exact amount, the due date, and accepted payment methods. Ambiguity is what triggers the disputes that stall payment.': _t(
                '<strong>Rendez les factures sans ambiguïté.</strong> Des lignes claires, le montant exact, l\'échéance et les moyens de paiement acceptés. L\'ambiguïté est ce qui déclenche les litiges qui bloquent le paiement.',
                '<strong>Machen Sie Rechnungen eindeutig.</strong> Klare Positionen, der genaue Betrag, das Fälligkeitsdatum und akzeptierte Zahlungsmethoden. Uneindeutigkeit löst die Streitigkeiten aus, die Zahlungen ins Stocken bringen.',
                '<strong>Haga las facturas inequívocas.</strong> Líneas claras, el importe exacto, el vencimiento y los métodos de pago aceptados. La ambigüedad es lo que desencadena las disputas que frenan el pago.',
                '<strong>Rendi le fatture inequivocabili.</strong> Voci chiare, l\'importo esatto, la scadenza e i metodi di pagamento accettati. L\'ambiguità è ciò che scatena le contestazioni che bloccano il pagamento.',
                '<strong>Maak facturen ondubbelzinnig.</strong> Duidelijke regels, het exacte bedrag, de vervaldatum en geaccepteerde betaalmethoden. Dubbelzinnigheid is wat de geschillen veroorzaakt die de betaling stilleggen.'),
            '<strong>Include a payment link.</strong> The easier it is to pay in the moment, the more invoices get paid in the moment.': _t(
                '<strong>Ajoutez un lien de paiement.</strong> Plus il est facile de payer sur le moment, plus les factures sont réglées sur le moment.',
                '<strong>Fügen Sie einen Zahlungslink bei.</strong> Je einfacher das Bezahlen im Moment ist, desto mehr Rechnungen werden im Moment bezahlt.',
                '<strong>Incluya un enlace de pago.</strong> Cuanto más fácil sea pagar en el momento, más facturas se pagan en el momento.',
                '<strong>Includi un link di pagamento.</strong> Più è facile pagare sul momento, più fatture vengono pagate sul momento.',
                '<strong>Voeg een betaallink toe.</strong> Hoe makkelijker het is om meteen te betalen, hoe meer facturen meteen betaald worden.'),
            '2. Terms and expectations': _t('2. Conditions et attentes', '2. Bedingungen und Erwartungen', '2. Condiciones y expectativas', '2. Condizioni e aspettative', '2. Voorwaarden en verwachtingen'),
            '<strong>Agree terms before the work starts</strong>, not on the invoice. Payment terms should never be a surprise.': _t(
                '<strong>Convenez des conditions avant le début du travail</strong>, pas sur la facture. Les conditions de paiement ne devraient jamais être une surprise.',
                '<strong>Vereinbaren Sie die Bedingungen vor Arbeitsbeginn</strong>, nicht auf der Rechnung. Zahlungsbedingungen sollten nie eine Überraschung sein.',
                '<strong>Acuerde las condiciones antes de empezar el trabajo</strong>, no en la factura. Las condiciones de pago nunca deberían ser una sorpresa.',
                '<strong>Concorda le condizioni prima che inizi il lavoro</strong>, non sulla fattura. Le condizioni di pagamento non dovrebbero mai essere una sorpresa.',
                '<strong>Spreek de voorwaarden af voordat het werk begint</strong>, niet op de factuur. Betalingsvoorwaarden mogen nooit een verrassing zijn.'),
            '<strong>State the due date as a date</strong>, not a "Net 30" buried in the footer. Concrete dates get paid; jargon gets ignored.': _t(
                '<strong>Indiquez l\'échéance sous forme de date</strong>, pas un « Net 30 » perdu en pied de page. Les dates concrètes sont payées ; le jargon est ignoré.',
                '<strong>Nennen Sie das Fälligkeitsdatum als Datum</strong>, nicht als „Net 30" in der Fußzeile versteckt. Konkrete Daten werden bezahlt; Fachjargon wird ignoriert.',
                '<strong>Indique el vencimiento como una fecha</strong>, no un «Net 30» escondido en el pie. Las fechas concretas se pagan; la jerga se ignora.',
                '<strong>Indica la scadenza come una data</strong>, non un «Net 30» nascosto nel piè di pagina. Le date concrete vengono pagate; il gergo viene ignorato.',
                '<strong>Vermeld de vervaldatum als een datum</strong>, geen «Net 30» verstopt in de voettekst. Concrete data worden betaald; jargon wordt genegeerd.'),
            '<strong>Set a clear late policy</strong> and apply it consistently. Predictability trains good behaviour.': _t(
                '<strong>Définissez une politique de retard claire</strong> et appliquez-la avec constance. La prévisibilité forge de bons comportements.',
                '<strong>Legen Sie eine klare Verzugsregelung fest</strong> und wenden Sie sie konsequent an. Berechenbarkeit erzieht gutes Verhalten.',
                '<strong>Establezca una política de morosidad clara</strong> y aplíquela con constancia. La previsibilidad educa buenos comportamientos.',
                '<strong>Stabilisci una policy chiara sui ritardi</strong> e applicala con costanza. La prevedibilità educa buoni comportamenti.',
                '<strong>Stel een duidelijk beleid voor te laat betalen op</strong> en pas het consequent toe. Voorspelbaarheid kweekt goed gedrag.'),
            '3. Follow-up': _t('3. Relance', '3. Nachfassen', '3. Seguimiento', '3. Sollecito', '3. Opvolging'),
            '<strong>Automate the reminder sequence.</strong> A nudge a few days before the due date prevents more late payments than any amount of chasing afterward.': _t(
                '<strong>Automatisez la séquence de rappels.</strong> Un petit rappel quelques jours avant l\'échéance prévient plus de retards que n\'importe quelle relance ultérieure.',
                '<strong>Automatisieren Sie die Erinnerungssequenz.</strong> Ein Anstoß wenige Tage vor dem Fälligkeitsdatum verhindert mehr verspätete Zahlungen als jedes Nachfassen danach.',
                '<strong>Automatice la secuencia de recordatorios.</strong> Un empujón unos días antes del vencimiento previene más pagos tardíos que cualquier persecución posterior.',
                '<strong>Automatizza la sequenza di promemoria.</strong> Una spinta qualche giorno prima della scadenza previene più ritardi di qualsiasi inseguimento successivo.',
                '<strong>Automatiseer de herinneringsreeks.</strong> Een zetje enkele dagen vóór de vervaldatum voorkomt meer late betalingen dan welke achtervolging achteraf ook.'),
            '<strong>Escalate on a schedule</strong>, not on a whim. Pre-due, on-due, and a defined post-due cadence mean nothing slips because someone was busy.': _t(
                '<strong>Faites monter le ton selon un calendrier</strong>, pas au gré de l\'humeur. Avant échéance, à l\'échéance et une cadence définie après échéance : rien ne passe entre les mailles parce que quelqu\'un était occupé.',
                '<strong>Eskalieren Sie nach Zeitplan</strong>, nicht nach Laune. Vor Fälligkeit, bei Fälligkeit und ein festgelegter Rhythmus nach Fälligkeit sorgen dafür, dass nichts durchrutscht, weil jemand beschäftigt war.',
                '<strong>Escale según un calendario</strong>, no según el capricho. Antes del vencimiento, en el vencimiento y una cadencia definida posterior hacen que nada se escape porque alguien estuviera ocupado.',
                '<strong>Aumenta la pressione secondo un calendario</strong>, non a capriccio. Prima della scadenza, alla scadenza e una cadenza definita dopo la scadenza fanno sì che nulla sfugga perché qualcuno era occupato.',
                '<strong>Escaleer volgens een schema</strong>, niet naar luim. Vóór de vervaldatum, op de vervaldatum en een vast ritme daarna zorgen dat er niets tussendoor glipt omdat iemand het druk had.'),
            '<strong>Log every promise to pay.</strong> "I\'ll pay Friday" is only useful if it\'s recorded against the account and followed up on.': _t(
                '<strong>Consignez chaque promesse de paiement.</strong> « Je paie vendredi » n\'est utile que si c\'est enregistré sur le compte et suivi.',
                '<strong>Protokollieren Sie jede Zahlungszusage.</strong> „Ich zahle Freitag" nützt nur, wenn es beim Konto vermerkt und nachverfolgt wird.',
                '<strong>Registre cada promesa de pago.</strong> «Pago el viernes» solo sirve si queda anotado en la cuenta y se le da seguimiento.',
                '<strong>Registra ogni promessa di pagamento.</strong> «Pago venerdì» è utile solo se viene annotato sul conto e seguito.',
                '<strong>Leg elke betalingstoezegging vast.</strong> «Ik betaal vrijdag» is alleen nuttig als het bij de rekening wordt vastgelegd en opgevolgd.'),
            '4. Reconciliation and disputes': _t('4. Rapprochement et litiges', '4. Abstimmung und Streitfälle', '4. Conciliación y disputas', '4. Riconciliazione e contestazioni', '4. Afletting en geschillen'),
            "<strong>Match payments to invoices promptly</strong> so your receivables figure is always accurate — you can't manage what you can't trust.": _t(
                '<strong>Rapprochez rapidement les paiements des factures</strong> pour que le montant de vos créances soit toujours exact — on ne peut pas piloter ce en quoi on ne peut pas avoir confiance.',
                '<strong>Ordnen Sie Zahlungen umgehend den Rechnungen zu</strong>, damit Ihr Forderungsbestand stets korrekt ist — man kann nicht steuern, worauf man sich nicht verlassen kann.',
                '<strong>Concilie los pagos con las facturas con prontitud</strong> para que la cifra de sus cobros sea siempre exacta — no se puede gestionar aquello en lo que no se puede confiar.',
                '<strong>Abbina prontamente i pagamenti alle fatture</strong> perché la cifra dei tuoi crediti sia sempre esatta — non puoi gestire ciò di cui non ti puoi fidare.',
                '<strong>Koppel betalingen snel aan facturen</strong> zodat uw debiteurenstand altijd klopt — je kunt niet beheren wat je niet kunt vertrouwen.'),
            '<strong>Resolve disputes fast.</strong> A stalled invoice is often one unanswered question away from being paid. Route disputes to an owner immediately.': _t(
                '<strong>Réglez vite les litiges.</strong> Une facture bloquée n\'est souvent qu\'à une question sans réponse d\'être payée. Attribuez immédiatement les litiges à un responsable.',
                '<strong>Lösen Sie Streitfälle schnell.</strong> Eine stockende Rechnung ist oft nur eine unbeantwortete Frage vom Bezahltwerden entfernt. Leiten Sie Streitfälle sofort an einen Verantwortlichen.',
                '<strong>Resuelva las disputas rápido.</strong> Una factura estancada suele estar a una pregunta sin responder de ser pagada. Asigne las disputas a un responsable de inmediato.',
                '<strong>Risolvi in fretta le contestazioni.</strong> Una fattura bloccata è spesso a una domanda senza risposta dall\'essere pagata. Assegna subito le contestazioni a un responsabile.',
                '<strong>Los geschillen snel op.</strong> Een vastgelopen factuur is vaak maar één onbeantwoorde vraag verwijderd van betaling. Wijs geschillen meteen aan een eigenaar toe.'),
            '5. Reporting': _t('5. Reporting', '5. Reporting', '5. Informes', '5. Reporting', '5. Rapportage'),
            '<strong>Run an aging report</strong> that buckets balances by 0–30, 31–60, 61–90, and 90+ days, so effort goes where recovery is most at risk.': _t(
                '<strong>Établissez une balance âgée</strong> qui ventile les soldes par 0–30, 31–60, 61–90 et plus de 90 jours, afin que l\'effort aille là où le recouvrement est le plus menacé.',
                '<strong>Erstellen Sie einen Fälligkeitsbericht</strong>, der Salden in 0–30, 31–60, 61–90 und 90+ Tage einteilt, damit der Aufwand dorthin fließt, wo die Einbringung am stärksten gefährdet ist.',
                '<strong>Elabore un informe de antigüedad</strong> que agrupe los saldos por 0–30, 31–60, 61–90 y más de 90 días, para que el esfuerzo vaya donde el recobro está más en riesgo.',
                '<strong>Prepara uno scadenzario</strong> che raggruppi i saldi in 0–30, 31–60, 61–90 e oltre 90 giorni, così lo sforzo va dove il recupero è più a rischio.',
                '<strong>Maak een ouderdomsanalyse</strong> die saldi indeelt in 0–30, 31–60, 61–90 en 90+ dagen, zodat de inspanning gaat waar inning het meest op het spel staat.'),
            '<strong>Track DSO monthly</strong> and watch the trend. (For the levers that move it, see our guide on <a href="/blog/reduce-days-sales-outstanding/">reducing Days Sales Outstanding</a>.)': _t(
                '<strong>Suivez le DSO chaque mois</strong> et observez la tendance. (Pour les leviers qui l\'influencent, consultez notre guide sur la <a href="/blog/reduce-days-sales-outstanding/">réduction du Days Sales Outstanding</a>.)',
                '<strong>Verfolgen Sie den DSO monatlich</strong> und beobachten Sie den Trend. (Zu den Hebeln, die ihn bewegen, siehe unseren Leitfaden zum <a href="/blog/reduce-days-sales-outstanding/">Senken der Days Sales Outstanding</a>.)',
                '<strong>Controle el DSO mensualmente</strong> y observe la tendencia. (Para las palancas que lo mueven, consulte nuestra guía sobre la <a href="/blog/reduce-days-sales-outstanding/">reducción de los Days Sales Outstanding</a>.)',
                '<strong>Monitora il DSO ogni mese</strong> e osserva la tendenza. (Per le leve che lo muovono, consulta la nostra guida sulla <a href="/blog/reduce-days-sales-outstanding/">riduzione dei Days Sales Outstanding</a>.)',
                '<strong>Volg de DSO maandelijks</strong> en houd de trend in de gaten. (Voor de hefbomen die hem bewegen, zie onze gids over het <a href="/blog/reduce-days-sales-outstanding/">verlagen van de Days Sales Outstanding</a>.)'),
            'The through-line is the same as with most operational problems: consistency beats effort. A team that runs this checklist the same way every month — ideally with the routine parts automated — collects faster and more predictably than one that works twice as hard on an ad-hoc basis.': _t(
                'Le fil rouge est le même que pour la plupart des problèmes opérationnels : la constance l\'emporte sur l\'effort. Une équipe qui applique cette check-list de la même manière chaque mois — idéalement avec les parties routinières automatisées — recouvre plus vite et de façon plus prévisible qu\'une équipe qui travaille deux fois plus au coup par coup.',
                'Der rote Faden ist derselbe wie bei den meisten operativen Problemen: Konsequenz schlägt Anstrengung. Ein Team, das diese Checkliste jeden Monat auf dieselbe Weise durchläuft — idealerweise mit automatisierten Routineteilen —, treibt schneller und berechenbarer ein als eines, das ad hoc doppelt so hart arbeitet.',
                'El hilo conductor es el mismo que en la mayoría de los problemas operativos: la constancia gana al esfuerzo. Un equipo que aplica esta lista de la misma manera cada mes — idealmente con las partes rutinarias automatizadas — cobra más rápido y de forma más previsible que uno que trabaja el doble de forma improvisada.',
                'Il filo conduttore è lo stesso della maggior parte dei problemi operativi: la costanza batte lo sforzo. Un team che applica questa checklist allo stesso modo ogni mese — idealmente con le parti di routine automatizzate — incassa più in fretta e in modo più prevedibile di uno che lavora il doppio in modo estemporaneo.',
                'De rode draad is dezelfde als bij de meeste operationele problemen: consistentie wint van inspanning. Een team dat deze checklist elke maand op dezelfde manier doorloopt — idealiter met de routineonderdelen geautomatiseerd — int sneller en voorspelbaarder dan een team dat ad hoc twee keer zo hard werkt.'),
            'Turn the checklist into a system': _t(
                'Transformez la check-list en système',
                'Machen Sie aus der Checkliste ein System',
                'Convierta la lista en un sistema',
                'Trasforma la checklist in un sistema',
                'Maak van de checklist een systeem'),
            'Collection runs invoicing, automated reminders, reconciliation, and aging reports in one place — so these best practices happen by default, not by memory.': _t(
                'Collection gère la facturation, les rappels automatisés, le rapprochement et les balances âgées au même endroit — pour que ces bonnes pratiques se produisent par défaut, et non de mémoire.',
                'Collection erledigt Rechnungsstellung, automatisierte Erinnerungen, Abstimmung und Fälligkeitsberichte an einem Ort — damit diese Best Practices standardmäßig geschehen, nicht aus dem Gedächtnis.',
                'Collection gestiona la facturación, los recordatorios automatizados, la conciliación y los informes de antigüedad en un solo lugar — para que estas buenas prácticas ocurran por defecto, no de memoria.',
                'Collection gestisce fatturazione, promemoria automatizzati, riconciliazione e scadenzari in un unico posto — così queste buone pratiche avvengono per impostazione predefinita, non a memoria.',
                'Collection regelt factureren, geautomatiseerde herinneringen, afletten en ouderdomsanalyses op één plek — zodat deze best practices standaard gebeuren, niet uit het geheugen.'),
        },
    },

    # =========================================================================
    '/blog/accounts-receivable-vs-payable/': {
        'src': 'blog/accounts-receivable-vs-payable/index.html',
        't': {
            **_ARTICLE_SHARED,
            'September 15, 2026': _t('15 septembre 2026', '15. September 2026', '15 de septiembre de 2026', '15 settembre 2026', '15 september 2026'),
            '6 min read': _MIN_READ_6,
            # ---- Title / meta / breadcrumb ----
            "Accounts Receivable vs Accounts Payable: What's the Difference?": _T_VS_PAYABLE,
            'A plain-English guide to accounts receivable vs accounts payable — what each means, how they hit your balance sheet and cash flow, and how to manage both.': _t(
                'Un guide clair sur les comptes clients et les comptes fournisseurs — ce que chacun signifie, leur effet sur le bilan et la trésorerie, et comment gérer les deux.',
                'Ein verständlicher Leitfaden zu Forderungen vs. Verbindlichkeiten — was jede bedeutet, wie sie Bilanz und Cashflow treffen und wie Sie beide steuern.',
                'Una guía en lenguaje claro sobre cuentas por cobrar vs. cuentas por pagar — qué significa cada una, cómo afectan al balance y al flujo de caja, y cómo gestionar ambas.',
                'Una guida in parole semplici su crediti verso clienti e debiti verso fornitori — cosa significa ciascuno, come incidono su bilancio e flusso di cassa e come gestirli entrambi.',
                'Een heldere gids over debiteuren versus crediteuren — wat elk betekent, hoe ze uw balans en cashflow raken en hoe u beide beheert.'),
            'AR is money owed to you; AP is money you owe. Here is how they differ and why both decide your cash flow.': _t(
                'AR est l\'argent qui vous est dû ; AP est l\'argent que vous devez. Voici en quoi ils diffèrent et pourquoi les deux déterminent votre trésorerie.',
                'AR ist Geld, das Ihnen geschuldet wird; AP ist Geld, das Sie schulden. So unterscheiden sie sich und warum beide Ihren Cashflow bestimmen.',
                'AR es el dinero que le deben; AP es el dinero que usted debe. Así se diferencian y por qué ambos deciden su flujo de caja.',
                'AR è il denaro che ti è dovuto; AP è il denaro che devi. Ecco in cosa differiscono e perché entrambi decidono il tuo flusso di cassa.',
                'AR is geld dat u tegoed hebt; AP is geld dat u verschuldigd bent. Zo verschillen ze en waarom beide uw cashflow bepalen.'),
            'Accounts receivable vs accounts payable': _t(
                'Comptes clients ou comptes fournisseurs',
                'Forderungen vs. Verbindlichkeiten',
                'Cuentas por cobrar vs. cuentas por pagar',
                'Crediti verso clienti e debiti verso fornitori',
                'Debiteuren versus crediteuren'),
            # ---- Body ----
            'If you run a business, two ledgers quietly decide whether you have cash in the bank: what customers owe you, and what you owe everyone else. Those are accounts receivable and accounts payable. They sound like accounting jargon, but understanding the difference — and managing both deliberately — is the heart of healthy cash flow.': _t(
                'Si vous dirigez une entreprise, deux registres décident discrètement si vous avez de l\'argent en banque : ce que les clients vous doivent, et ce que vous devez à tous les autres. Ce sont les comptes clients et les comptes fournisseurs. Cela sonne comme du jargon comptable, mais comprendre la différence — et gérer les deux délibérément — est au cœur d\'une trésorerie saine.',
                'Wenn Sie ein Unternehmen führen, entscheiden zwei Konten leise darüber, ob Geld auf dem Konto ist: was Kunden Ihnen schulden und was Sie allen anderen schulden. Das sind Forderungen und Verbindlichkeiten. Es klingt nach Buchhaltungsjargon, doch den Unterschied zu verstehen — und beides bewusst zu steuern — ist das Herzstück eines gesunden Cashflows.',
                'Si dirige un negocio, dos libros deciden en silencio si tiene efectivo en el banco: lo que los clientes le deben y lo que usted debe a los demás. Son las cuentas por cobrar y las cuentas por pagar. Suena a jerga contable, pero entender la diferencia — y gestionar ambas con intención — es el corazón de un flujo de caja sano.',
                'Se gestisci un\'azienda, due registri decidono in silenzio se hai liquidità in banca: ciò che i clienti ti devono e ciò che devi a tutti gli altri. Sono i crediti verso clienti e i debiti verso fornitori. Sembra gergo contabile, ma capire la differenza — e gestire entrambi in modo consapevole — è il cuore di un flusso di cassa sano.',
                'Als u een bedrijf runt, bepalen twee grootboeken stilletjes of u geld op de bank hebt: wat klanten u schuldig zijn en wat u aan alle anderen schuldig bent. Dat zijn debiteuren en crediteuren. Het klinkt als boekhoudjargon, maar het verschil begrijpen — en beide bewust beheren — is het hart van een gezonde cashflow.'),
            'What is accounts receivable?': _t('Que sont les comptes clients ?', 'Was sind Forderungen?', '¿Qué son las cuentas por cobrar?', 'Cosa sono i crediti verso clienti?', 'Wat zijn debiteuren?'),
            'Accounts receivable (AR) is money your customers owe you for goods or services you have already delivered but have not been paid for yet. It shows up on your balance sheet as a <strong>current asset</strong>, because it is cash you expect to collect soon. Every unpaid invoice you have sent is part of your AR.': _t(
                'Les comptes clients (AR) désignent l\'argent que vos clients vous doivent pour des biens ou services déjà livrés mais pas encore payés. Ils figurent au bilan comme un <strong>actif circulant</strong>, car c\'est de la trésorerie que vous comptez encaisser bientôt. Chaque facture impayée que vous avez émise fait partie de votre AR.',
                'Forderungen (AR) sind Gelder, die Ihre Kunden Ihnen für bereits gelieferte, aber noch nicht bezahlte Waren oder Leistungen schulden. In der Bilanz erscheinen sie als <strong>Umlaufvermögen</strong>, denn es ist Geld, das Sie bald einzunehmen erwarten. Jede von Ihnen versandte offene Rechnung ist Teil Ihrer AR.',
                'Las cuentas por cobrar (AR) son el dinero que sus clientes le deben por bienes o servicios que ya ha entregado pero por los que aún no le han pagado. Aparecen en el balance como un <strong>activo corriente</strong>, porque es efectivo que espera cobrar pronto. Cada factura impagada que ha enviado forma parte de su AR.',
                'I crediti verso clienti (AR) sono il denaro che i tuoi clienti ti devono per beni o servizi già consegnati ma non ancora pagati. Compaiono nel bilancio come <strong>attività corrente</strong>, perché è liquidità che prevedi di incassare presto. Ogni fattura insoluta che hai inviato fa parte dei tuoi AR.',
                'Debiteuren (AR) is geld dat uw klanten u verschuldigd zijn voor goederen of diensten die u al hebt geleverd maar waarvoor u nog niet bent betaald. Het staat op uw balans als een <strong>vlottend activum</strong>, want het is geld dat u binnenkort verwacht te innen. Elke onbetaalde factuur die u hebt verzonden, is onderdeel van uw AR.'),
            'What is accounts payable?': _t('Que sont les comptes fournisseurs ?', 'Was sind Verbindlichkeiten?', '¿Qué son las cuentas por pagar?', 'Cosa sono i debiti verso fornitori?', 'Wat zijn crediteuren?'),
            'Accounts payable (AP) is the mirror image: money you owe to suppliers and vendors for things you have received but not yet paid for. It is a <strong>current liability</strong> on your balance sheet. Every bill sitting in your inbox waiting to be paid is part of your AP.': _t(
                'Les comptes fournisseurs (AP) en sont l\'image inversée : l\'argent que vous devez à des fournisseurs et prestataires pour des choses reçues mais pas encore payées. C\'est un <strong>passif courant</strong> au bilan. Chaque facture en attente de paiement dans votre boîte de réception fait partie de votre AP.',
                'Verbindlichkeiten (AP) sind das Spiegelbild: Geld, das Sie Lieferanten und Anbietern für Erhaltenes, aber noch nicht Bezahltes schulden. In der Bilanz ist es eine <strong>kurzfristige Verbindlichkeit</strong>. Jede Rechnung in Ihrem Posteingang, die auf Bezahlung wartet, ist Teil Ihrer AP.',
                'Las cuentas por pagar (AP) son la imagen especular: dinero que usted debe a proveedores y suministradores por cosas que ha recibido pero aún no ha pagado. Es un <strong>pasivo corriente</strong> en su balance. Cada factura en su bandeja de entrada esperando pago forma parte de su AP.',
                'I debiti verso fornitori (AP) sono l\'immagine speculare: denaro che devi a fornitori e venditori per cose ricevute ma non ancora pagate. Nel bilancio è una <strong>passività corrente</strong>. Ogni fattura nella tua casella in attesa di pagamento fa parte dei tuoi AP.',
                'Crediteuren (AP) is het spiegelbeeld: geld dat u verschuldigd bent aan leveranciers voor zaken die u hebt ontvangen maar nog niet hebt betaald. Het is een <strong>kortlopende schuld</strong> op uw balans. Elke rekening in uw inbox die op betaling wacht, is onderdeel van uw AP.'),
            'The key difference, in one line': _t('La différence essentielle, en une ligne', 'Der entscheidende Unterschied, in einer Zeile', 'La diferencia clave, en una línea', 'La differenza chiave, in una riga', 'Het belangrijkste verschil, in één regel'),
            'AR is money coming in; AP is money going out. AR is an asset you collect; AP is a liability you settle. One invoice can be both at once — it is AR for the business that sent it and AP for the business that received it.': _t(
                'AR est l\'argent qui entre ; AP est l\'argent qui sort. AR est un actif que vous encaissez ; AP est un passif que vous réglez. Une même facture peut être les deux à la fois — elle est AR pour l\'entreprise qui l\'a émise et AP pour celle qui l\'a reçue.',
                'AR ist Geld, das hereinkommt; AP ist Geld, das hinausgeht. AR ist ein Vermögenswert, den Sie einziehen; AP ist eine Verbindlichkeit, die Sie begleichen. Ein und dieselbe Rechnung kann beides zugleich sein — sie ist AR für das Unternehmen, das sie versendet hat, und AP für das, das sie erhalten hat.',
                'AR es dinero que entra; AP es dinero que sale. AR es un activo que usted cobra; AP es un pasivo que usted liquida. Una misma factura puede ser ambas a la vez — es AR para la empresa que la envió y AP para la que la recibió.',
                'AR è denaro in entrata; AP è denaro in uscita. AR è un\'attività che incassi; AP è una passività che saldi. Una stessa fattura può essere entrambe insieme — è AR per l\'azienda che l\'ha inviata e AP per quella che l\'ha ricevuta.',
                'AR is geld dat binnenkomt; AP is geld dat uitgaat. AR is een activum dat u int; AP is een schuld die u vereffent. Eén factuur kan beide tegelijk zijn — het is AR voor het bedrijf dat ze verzond en AP voor het bedrijf dat ze ontving.'),
            'How they affect your cash flow': _t('Comment ils influencent votre trésorerie', 'Wie sie Ihren Cashflow beeinflussen', 'Cómo afectan a su flujo de caja', 'Come incidono sul tuo flusso di cassa', 'Hoe ze uw cashflow beïnvloeden'),
            'Cash flow lives in the timing gap between the two. If your customers pay you on Net 60 but your suppliers expect Net 15, you are financing that 45-day gap out of your own pocket. Managing AR (collecting faster) and AP (paying on your own terms, without being late) is how you keep the gap from squeezing you. Two useful measures: <strong>DSO</strong> (days sales outstanding) tracks how fast you collect AR; <strong>DPO</strong> (days payable outstanding) tracks how long you take to pay AP.': _t(
                'La trésorerie se joue dans l\'écart de timing entre les deux. Si vos clients vous paient à Net 60 mais que vos fournisseurs attendent un Net 15, vous financez cet écart de 45 jours de votre propre poche. Gérer l\'AR (encaisser plus vite) et l\'AP (payer à vos conditions, sans être en retard), c\'est ainsi que vous empêchez cet écart de vous étrangler. Deux mesures utiles : le <strong>DSO</strong> (days sales outstanding) mesure la vitesse à laquelle vous encaissez l\'AR ; le <strong>DPO</strong> (days payable outstanding) mesure le temps que vous mettez à payer l\'AP.',
                'Der Cashflow lebt in der zeitlichen Lücke zwischen beiden. Zahlen Ihre Kunden auf Net 60, erwarten Ihre Lieferanten aber Net 15, finanzieren Sie diese Lücke von 45 Tagen aus eigener Tasche. Die AR zu steuern (schneller einziehen) und die AP (zu Ihren Bedingungen zahlen, ohne in Verzug zu geraten) hält die Lücke davon ab, Sie zu erdrücken. Zwei nützliche Kennzahlen: <strong>DSO</strong> (days sales outstanding) misst, wie schnell Sie AR einziehen; <strong>DPO</strong> (days payable outstanding) misst, wie lange Sie brauchen, um AP zu zahlen.',
                'El flujo de caja vive en el desfase temporal entre ambas. Si sus clientes le pagan a Net 60 pero sus proveedores esperan Net 15, usted financia ese desfase de 45 días de su propio bolsillo. Gestionar el AR (cobrar más rápido) y el AP (pagar en sus propias condiciones, sin retrasarse) es como evita que el desfase le ahogue. Dos medidas útiles: el <strong>DSO</strong> (days sales outstanding) mide la rapidez con que cobra el AR; el <strong>DPO</strong> (days payable outstanding) mide cuánto tarda en pagar el AP.',
                'Il flusso di cassa vive nel divario temporale tra i due. Se i tuoi clienti ti pagano a Net 60 ma i tuoi fornitori si aspettano Net 15, finanzi quel divario di 45 giorni di tasca tua. Gestire l\'AR (incassare più in fretta) e l\'AP (pagare alle tue condizioni, senza essere in ritardo) è così che impedisci al divario di soffocarti. Due misure utili: il <strong>DSO</strong> (days sales outstanding) misura quanto in fretta incassi l\'AR; il <strong>DPO</strong> (days payable outstanding) misura quanto tempo impieghi a pagare l\'AP.',
                'Cashflow leeft in de tijdskloof tussen de twee. Als uw klanten u op Net 60 betalen maar uw leveranciers Net 15 verwachten, financiert u die kloof van 45 dagen uit eigen zak. De AR beheren (sneller innen) en de AP (op uw eigen voorwaarden betalen, zonder te laat te zijn) is hoe u voorkomt dat de kloof u in de tang neemt. Twee nuttige maatstaven: <strong>DSO</strong> (days sales outstanding) meet hoe snel u AR int; <strong>DPO</strong> (days payable outstanding) meet hoe lang u erover doet om AP te betalen.'),
            'How to manage both well': _t('Comment bien gérer les deux', 'Wie Sie beide gut steuern', 'Cómo gestionar bien ambas', 'Come gestire bene entrambi', 'Hoe u beide goed beheert'),
            '<strong>Invoice promptly and clearly</strong>, with due dates and payment links — the faster an invoice goes out, the faster it comes back.': _t(
                '<strong>Facturez rapidement et clairement</strong>, avec des échéances et des liens de paiement — plus une facture part vite, plus vite elle revient.',
                '<strong>Stellen Sie Rechnungen zügig und klar aus</strong>, mit Fälligkeitsdaten und Zahlungslinks — je schneller eine Rechnung hinausgeht, desto schneller kommt sie zurück.',
                '<strong>Facture con prontitud y claridad</strong>, con vencimientos y enlaces de pago — cuanto antes sale una factura, antes vuelve.',
                '<strong>Fattura con prontezza e chiarezza</strong>, con scadenze e link di pagamento — prima esce una fattura, prima torna.',
                '<strong>Factureer snel en duidelijk</strong>, met vervaldata en betaallinks — hoe sneller een factuur de deur uit gaat, hoe sneller ze terugkomt.'),
            '<strong>Track AR by age</strong> so you know what is overdue and chase it on a set cadence.': _t(
                '<strong>Suivez l\'AR par ancienneté</strong> pour savoir ce qui est en retard et le relancer selon une cadence définie.',
                '<strong>Verfolgen Sie die AR nach Alter</strong>, damit Sie wissen, was überfällig ist, und es in festem Rhythmus nachfassen.',
                '<strong>Controle el AR por antigüedad</strong> para saber qué está vencido y reclamarlo con una cadencia definida.',
                '<strong>Monitora l\'AR per anzianità</strong> così sai cosa è scaduto e lo solleciti con una cadenza definita.',
                '<strong>Volg de AR op ouderdom</strong> zodat u weet wat achterstallig is en het op een vast ritme opvolgt.'),
            '<strong>Schedule AP</strong> so you pay on time — protecting supplier relationships and any early-pay discounts — without paying early for no reason.': _t(
                '<strong>Planifiez l\'AP</strong> pour payer à temps — en préservant les relations fournisseurs et les escomptes pour paiement anticipé — sans payer en avance sans raison.',
                '<strong>Planen Sie die AP</strong>, damit Sie pünktlich zahlen — zum Schutz der Lieferantenbeziehungen und etwaiger Skonti — ohne grundlos vorzeitig zu zahlen.',
                '<strong>Programe el AP</strong> para pagar a tiempo — protegiendo las relaciones con proveedores y los descuentos por pronto pago — sin pagar antes sin motivo.',
                '<strong>Programma l\'AP</strong> per pagare in tempo — proteggendo i rapporti con i fornitori e gli eventuali sconti per pagamento anticipato — senza pagare in anticipo senza motivo.',
                '<strong>Plan de AP</strong> zodat u op tijd betaalt — ter bescherming van leveranciersrelaties en eventuele kortingen voor vroeg betalen — zonder zonder reden vroeg te betalen.'),
            "<strong>Reconcile both regularly</strong> so your books reflect reality, not last month's guess.": _t(
                '<strong>Rapprochez les deux régulièrement</strong> pour que vos livres reflètent la réalité, pas l\'estimation du mois dernier.',
                '<strong>Stimmen Sie beide regelmäßig ab</strong>, damit Ihre Bücher die Realität abbilden, nicht die Schätzung des Vormonats.',
                '<strong>Concilie ambas con regularidad</strong> para que sus libros reflejen la realidad, no la conjetura del mes pasado.',
                '<strong>Riconcilia entrambi con regolarità</strong> perché i tuoi libri riflettano la realtà, non la stima del mese scorso.',
                '<strong>Flet beide regelmatig af</strong> zodat uw boeken de werkelijkheid weergeven, niet de schatting van vorige maand.'),
            'Frequently asked questions': _t('Foire aux questions', 'Häufig gestellte Fragen', 'Preguntas frecuentes', 'Domande frequenti', 'Veelgestelde vragen'),
            'Is accounts receivable an asset or a liability?': _t('Les comptes clients sont-ils un actif ou un passif ?', 'Sind Forderungen ein Vermögenswert oder eine Verbindlichkeit?', '¿Las cuentas por cobrar son un activo o un pasivo?', 'I crediti verso clienti sono un\'attività o una passività?', 'Zijn debiteuren een activum of een schuld?'),
            'Accounts receivable is a current asset. It represents money owed to your business that you expect to collect, usually within a year, so it counts toward what your business owns.': _t(
                'Les comptes clients sont un actif circulant. Ils représentent l\'argent dû à votre entreprise que vous comptez encaisser, généralement dans l\'année, et comptent donc parmi ce que votre entreprise possède.',
                'Forderungen sind Umlaufvermögen. Sie stehen für Geld, das Ihrem Unternehmen geschuldet wird und das Sie in der Regel binnen eines Jahres einzuziehen erwarten, und zählen daher zu dem, was Ihr Unternehmen besitzt.',
                'Las cuentas por cobrar son un activo corriente. Representan dinero adeudado a su empresa que espera cobrar, normalmente en un año, así que cuenta como parte de lo que su empresa posee.',
                'I crediti verso clienti sono un\'attività corrente. Rappresentano denaro dovuto alla tua azienda che prevedi di incassare, di solito entro un anno, quindi rientrano in ciò che la tua azienda possiede.',
                'Debiteuren zijn een vlottend activum. Ze vertegenwoordigen geld dat uw bedrijf tegoed heeft en dat u verwacht te innen, meestal binnen een jaar, dus het telt mee met wat uw bedrijf bezit.'),
            'Is accounts payable a debit or a credit?': _t('Les comptes fournisseurs sont-ils un débit ou un crédit ?', 'Sind Verbindlichkeiten eine Soll- oder eine Habenbuchung?', '¿Las cuentas por pagar son un débito o un crédito?', 'I debiti verso fornitori sono un dare o un avere?', 'Zijn crediteuren een debet- of een creditpost?'),
            'Accounts payable is a liability, so it normally carries a credit balance. It increases with a credit when you record a new bill and decreases with a debit when you pay it.': _t(
                'Les comptes fournisseurs sont un passif, ils portent donc normalement un solde créditeur. Ils augmentent par un crédit lorsque vous enregistrez une nouvelle facture et diminuent par un débit lorsque vous la payez.',
                'Verbindlichkeiten sind eine Verbindlichkeit und weisen daher normalerweise einen Habensaldo aus. Sie erhöhen sich durch eine Habenbuchung, wenn Sie eine neue Rechnung erfassen, und verringern sich durch eine Sollbuchung, wenn Sie sie bezahlen.',
                'Las cuentas por pagar son un pasivo, así que normalmente presentan un saldo acreedor. Aumentan con un crédito cuando registra una nueva factura y disminuyen con un débito cuando la paga.',
                'I debiti verso fornitori sono una passività, quindi normalmente presentano un saldo in avere. Aumentano con un avere quando registri una nuova fattura e diminuiscono con un dare quando la paghi.',
                'Crediteuren zijn een schuld, dus ze hebben normaal een creditsaldo. Ze nemen toe met een creditboeking wanneer u een nieuwe rekening vastlegt en af met een debetboeking wanneer u ze betaalt.'),
            'Can something be both AR and AP?': _t('Une même chose peut-elle être à la fois AR et AP ?', 'Kann etwas zugleich AR und AP sein?', '¿Algo puede ser a la vez AR y AP?', 'Qualcosa può essere sia AR sia AP?', 'Kan iets zowel AR als AP zijn?'),
            'Not for the same company on the same transaction, but a single invoice is AR for the seller and AP for the buyer. If you both buy from and sell to the same partner, you may carry AR and AP with them at the same time.': _t(
                'Pas pour la même entreprise sur la même transaction, mais une seule facture est AR pour le vendeur et AP pour l\'acheteur. Si vous achetez à un même partenaire et lui vendez à la fois, vous pouvez porter avec lui de l\'AR et de l\'AP en même temps.',
                'Nicht für dasselbe Unternehmen bei derselben Transaktion, aber eine einzelne Rechnung ist AR für den Verkäufer und AP für den Käufer. Wenn Sie beim selben Partner sowohl einkaufen als auch an ihn verkaufen, können Sie gleichzeitig AR und AP mit ihm führen.',
                'No para la misma empresa en la misma transacción, pero una sola factura es AR para el vendedor y AP para el comprador. Si a la vez compra y vende al mismo socio, puede mantener AR y AP con él al mismo tiempo.',
                'Non per la stessa azienda nella stessa transazione, ma una singola fattura è AR per il venditore e AP per l\'acquirente. Se acquisti e vendi allo stesso partner, puoi avere con lui AR e AP nello stesso momento.',
                'Niet voor hetzelfde bedrijf op dezelfde transactie, maar één factuur is AR voor de verkoper en AP voor de koper. Als u zowel inkoopt bij als verkoopt aan dezelfde partner, kunt u tegelijk AR en AP met hem hebben.'),
            'Collecting AR faster is a discipline of its own — see our guides to <a href="/blog/accounts-receivable-best-practices/">accounts receivable best practices</a>, <a href="/blog/reduce-days-sales-outstanding/">reducing days sales outstanding</a>, and <a href="/blog/invoice-payment-terms/">choosing invoice payment terms</a>.': _t(
                'Encaisser l\'AR plus vite est une discipline à part entière — consultez nos guides sur les <a href="/blog/accounts-receivable-best-practices/">bonnes pratiques de gestion des comptes clients</a>, la <a href="/blog/reduce-days-sales-outstanding/">réduction du days sales outstanding</a> et le <a href="/blog/invoice-payment-terms/">choix des conditions de paiement des factures</a>.',
                'Die AR schneller einzuziehen ist eine Disziplin für sich — sehen Sie unsere Leitfäden zu <a href="/blog/accounts-receivable-best-practices/">Best Practices im Forderungsmanagement</a>, zum <a href="/blog/reduce-days-sales-outstanding/">Senken der days sales outstanding</a> und zur <a href="/blog/invoice-payment-terms/">Wahl der Zahlungsbedingungen auf Rechnungen</a>.',
                'Cobrar el AR más rápido es una disciplina en sí misma — consulte nuestras guías sobre las <a href="/blog/accounts-receivable-best-practices/">buenas prácticas de cuentas por cobrar</a>, la <a href="/blog/reduce-days-sales-outstanding/">reducción de los days sales outstanding</a> y la <a href="/blog/invoice-payment-terms/">elección de las condiciones de pago de facturas</a>.',
                'Incassare l\'AR più in fretta è una disciplina a sé — consulta le nostre guide sulle <a href="/blog/accounts-receivable-best-practices/">buone pratiche per la gestione dei crediti</a>, sulla <a href="/blog/reduce-days-sales-outstanding/">riduzione dei days sales outstanding</a> e sulla <a href="/blog/invoice-payment-terms/">scelta delle condizioni di pagamento delle fatture</a>.',
                'De AR sneller innen is een discipline op zich — zie onze gidsen over <a href="/blog/accounts-receivable-best-practices/">best practices voor debiteurenbeheer</a>, het <a href="/blog/reduce-days-sales-outstanding/">verlagen van de days sales outstanding</a> en het <a href="/blog/invoice-payment-terms/">kiezen van betalingsvoorwaarden op facturen</a>.'),
            'Turn receivables into cash on time': _t(
                'Transformez les créances en trésorerie à temps',
                'Verwandeln Sie Forderungen pünktlich in Bargeld',
                'Convierta los cobros en efectivo a tiempo',
                'Trasforma i crediti in liquidità puntualmente',
                'Zet vorderingen op tijd om in geld'),
            'Collection tracks every invoice by age, automates reminders, and reconciles payments — so your accounts receivable stops aging and starts arriving.': _t(
                'Collection suit chaque facture par ancienneté, automatise les rappels et rapproche les paiements — pour que vos comptes clients cessent de vieillir et commencent à rentrer.',
                'Collection verfolgt jede Rechnung nach Alter, automatisiert Erinnerungen und stimmt Zahlungen ab — damit Ihre Forderungen nicht mehr altern, sondern eingehen.',
                'Collection controla cada factura por antigüedad, automatiza los recordatorios y concilia los pagos — para que sus cuentas por cobrar dejen de envejecer y empiecen a llegar.',
                'Collection monitora ogni fattura per anzianità, automatizza i promemoria e riconcilia i pagamenti — così i tuoi crediti smettono di invecchiare e iniziano ad arrivare.',
                'Collection volgt elke factuur op ouderdom, automatiseert herinneringen en flet betalingen af — zodat uw debiteuren stoppen met verouderen en beginnen binnen te komen.'),
        },
    },

    # =========================================================================
    '/blog/invoice-payment-terms/': {
        'src': 'blog/invoice-payment-terms/index.html',
        't': {
            **_ARTICLE_SHARED,
            'September 1, 2026': _t('1 septembre 2026', '1. September 2026', '1 de septiembre de 2026', '1 settembre 2026', '1 september 2026'),
            '7 min read': _MIN_READ_7,
            # ---- Title / meta / breadcrumb ----
            'Invoice Payment Terms Explained (Net 30, 2/10 Net 30 &amp; More)': _T_INVOICE_TERMS,
            'A plain-English guide to invoice payment terms — Net 30, Net 15, due on receipt, EOM, 2/10 Net 30 early-payment discounts, and deposits — and how to choose the right ones.': _t(
                'Un guide clair sur les conditions de paiement des factures — Net 30, Net 15, paiement à réception, EOM, escomptes 2/10 Net 30 et acomptes — et comment choisir les bonnes.',
                'Ein verständlicher Leitfaden zu Zahlungsbedingungen auf Rechnungen — Net 30, Net 15, Zahlung bei Erhalt, EOM, 2/10 Net 30-Skonti und Anzahlungen — und wie Sie die richtigen wählen.',
                'Una guía en lenguaje claro sobre las condiciones de pago de facturas — Net 30, Net 15, pago a la recepción, EOM, descuentos por pronto pago 2/10 Net 30 y anticipos — y cómo elegir las adecuadas.',
                'Una guida in parole semplici sulle condizioni di pagamento delle fatture — Net 30, Net 15, pagamento alla ricezione, EOM, sconti per pagamento anticipato 2/10 Net 30 e acconti — e come scegliere quelle giuste.',
                'Een heldere gids over betalingsvoorwaarden op facturen — Net 30, Net 15, betaling bij ontvangst, EOM, kortingen voor vroeg betalen 2/10 Net 30 en aanbetalingen — en hoe u de juiste kiest.'),
            'What Net 30, due on receipt, EOM, and 2/10 Net 30 actually mean — and how to pick terms that keep your cash flowing.': _t(
                'Ce que signifient réellement Net 30, paiement à réception, EOM et 2/10 Net 30 — et comment choisir des conditions qui maintiennent votre trésorerie.',
                'Was Net 30, Zahlung bei Erhalt, EOM und 2/10 Net 30 wirklich bedeuten — und wie Sie Bedingungen wählen, die Ihren Cashflow am Laufen halten.',
                'Qué significan realmente Net 30, pago a la recepción, EOM y 2/10 Net 30 — y cómo elegir condiciones que mantengan su flujo de caja.',
                'Cosa significano davvero Net 30, pagamento alla ricezione, EOM e 2/10 Net 30 — e come scegliere condizioni che mantengono il flusso di cassa.',
                'Wat Net 30, betaling bij ontvangst, EOM en 2/10 Net 30 echt betekenen — en hoe u voorwaarden kiest die uw cashflow op peil houden.'),
            'Invoice payment terms explained': _t(
                'Les conditions de paiement des factures expliquées',
                'Zahlungsbedingungen auf Rechnungen erklärt',
                'Las condiciones de pago de facturas explicadas',
                'Le condizioni di pagamento delle fatture spiegate',
                'Betalingsvoorwaarden op facturen uitgelegd'),
            # ---- Body ----
            'Payment terms are the quiet agreement that decides <em>when</em> you get paid — and they matter as much to your cash flow as the price itself. Set them clearly and you get predictable income; leave them vague and you get slow payers, disputes, and awkward chases. This guide explains the common terms in plain English and how to choose the ones that fit your business.': _t(
                'Les conditions de paiement sont l\'accord discret qui décide <em>quand</em> vous êtes payé — et elles comptent autant pour votre trésorerie que le prix lui-même. Définissez-les clairement et vous obtenez des revenus prévisibles ; laissez-les floues et vous récoltez des mauvais payeurs, des litiges et des relances gênantes. Ce guide explique les conditions courantes en termes simples et comment choisir celles qui conviennent à votre entreprise.',
                'Zahlungsbedingungen sind die stille Vereinbarung, die entscheidet, <em>wann</em> Sie bezahlt werden — und sie zählen für Ihren Cashflow ebenso wie der Preis selbst. Legen Sie sie klar fest, erhalten Sie berechenbare Einnahmen; lassen Sie sie vage, bekommen Sie Spätzahler, Streitigkeiten und unangenehmes Nachfassen. Dieser Leitfaden erklärt die gängigen Bedingungen verständlich und wie Sie die passenden für Ihr Unternehmen wählen.',
                'Las condiciones de pago son el acuerdo silencioso que decide <em>cuándo</em> le pagan — y para su flujo de caja importan tanto como el propio precio. Defínalas con claridad y obtendrá ingresos previsibles; déjelas vagas y tendrá pagadores lentos, disputas y reclamaciones incómodas. Esta guía explica las condiciones habituales en lenguaje claro y cómo elegir las que encajan con su negocio.',
                'Le condizioni di pagamento sono l\'accordo silenzioso che decide <em>quando</em> vieni pagato — e per il tuo flusso di cassa contano quanto il prezzo stesso. Definiscile con chiarezza e otterrai entrate prevedibili; lasciale vaghe e avrai pagatori lenti, contestazioni e solleciti imbarazzanti. Questa guida spiega le condizioni comuni in parole semplici e come scegliere quelle adatte alla tua azienda.',
                'Betalingsvoorwaarden zijn de stille afspraak die bepaalt <em>wanneer</em> u betaald wordt — en voor uw cashflow tellen ze net zo zwaar als de prijs zelf. Stel ze duidelijk vast en u krijgt voorspelbare inkomsten; laat ze vaag en u krijgt trage betalers, geschillen en ongemakkelijke aanmaningen. Deze gids legt de gangbare voorwaarden in gewone taal uit en hoe u die kiest die bij uw bedrijf passen.'),
            'What "payment terms" actually means': _t('Ce que signifient vraiment les « conditions de paiement »', 'Was „Zahlungsbedingungen" wirklich bedeuten', 'Qué significan realmente las «condiciones de pago»', 'Cosa significano davvero le «condizioni di pagamento»', 'Wat «betalingsvoorwaarden» eigenlijk betekent'),
            'Payment terms are the conditions you set for getting paid: how long the customer has, when the clock starts, which methods you accept, and any discount or penalty attached. They belong on the invoice — but ideally they\'re agreed <strong>before</strong> the work starts, so nothing is a surprise.': _t(
                'Les conditions de paiement sont les modalités que vous fixez pour être payé : de combien de temps dispose le client, quand le compte à rebours démarre, quels moyens vous acceptez, et tout escompte ou pénalité associé. Elles ont leur place sur la facture — mais idéalement elles sont convenues <strong>avant</strong> le début du travail, pour qu\'il n\'y ait aucune surprise.',
                'Zahlungsbedingungen sind die Konditionen, die Sie fürs Bezahltwerden festlegen: wie lange der Kunde Zeit hat, wann die Frist beginnt, welche Methoden Sie akzeptieren und jeder damit verbundene Rabatt oder jede Strafe. Sie gehören auf die Rechnung — idealerweise aber werden sie <strong>vor</strong> Arbeitsbeginn vereinbart, damit nichts überrascht.',
                'Las condiciones de pago son los términos que fija para cobrar: cuánto tiempo tiene el cliente, cuándo empieza a contar el plazo, qué métodos acepta y cualquier descuento o penalización asociado. Su sitio está en la factura — pero lo ideal es acordarlas <strong>antes</strong> de empezar el trabajo, para que nada sea una sorpresa.',
                'Le condizioni di pagamento sono i termini che stabilisci per farti pagare: quanto tempo ha il cliente, quando parte il conteggio, quali metodi accetti e ogni sconto o penale associato. Vanno sulla fattura — ma idealmente si concordano <strong>prima</strong> che inizi il lavoro, così nulla è una sorpresa.',
                'Betalingsvoorwaarden zijn de voorwaarden die u stelt om betaald te worden: hoeveel tijd de klant heeft, wanneer de klok start, welke methoden u accepteert en elke bijbehorende korting of boete. Ze horen op de factuur — maar idealiter worden ze <strong>vóór</strong> de start van het werk afgesproken, zodat niets een verrassing is.'),
            'The common terms, decoded': _t('Les conditions courantes, décodées', 'Die gängigen Bedingungen, entschlüsselt', 'Las condiciones habituales, descifradas', 'Le condizioni comuni, decodificate', 'De gangbare voorwaarden, ontcijferd'),
            '<strong>Due on receipt</strong> — payment is expected as soon as the invoice arrives. Best for one-off jobs or new customers.': _t(
                '<strong>Paiement à réception</strong> — le paiement est attendu dès l\'arrivée de la facture. Idéal pour les missions ponctuelles ou les nouveaux clients.',
                '<strong>Zahlung bei Erhalt</strong> — die Zahlung wird erwartet, sobald die Rechnung eintrifft. Am besten für einmalige Aufträge oder neue Kunden.',
                '<strong>Pago a la recepción</strong> — se espera el pago en cuanto llega la factura. Ideal para trabajos puntuales o clientes nuevos.',
                '<strong>Pagamento alla ricezione</strong> — il pagamento è atteso non appena arriva la fattura. Ideale per lavori una tantum o clienti nuovi.',
                '<strong>Betaling bij ontvangst</strong> — betaling wordt verwacht zodra de factuur binnenkomt. Het best voor eenmalige klussen of nieuwe klanten.'),
            '<strong>Net 7 / Net 15 / Net 30 / Net 60</strong> — payment is due that many days after the invoice date. <strong>Net 30</strong> is the most common in B2B; shorter terms (Net 7–15) pull cash in faster.': _t(
                '<strong>Net 7 / Net 15 / Net 30 / Net 60</strong> — le paiement est dû ce nombre de jours après la date de facture. <strong>Net 30</strong> est le plus courant en B2B ; des délais plus courts (Net 7–15) font rentrer la trésorerie plus vite.',
                '<strong>Net 7 / Net 15 / Net 30 / Net 60</strong> — die Zahlung ist so viele Tage nach dem Rechnungsdatum fällig. <strong>Net 30</strong> ist im B2B am gängigsten; kürzere Fristen (Net 7–15) holen das Geld schneller herein.',
                '<strong>Net 7 / Net 15 / Net 30 / Net 60</strong> — el pago vence ese número de días después de la fecha de la factura. <strong>Net 30</strong> es el más común en B2B; los plazos más cortos (Net 7–15) hacen entrar el efectivo más rápido.',
                '<strong>Net 7 / Net 15 / Net 30 / Net 60</strong> — il pagamento è dovuto quel numero di giorni dopo la data della fattura. <strong>Net 30</strong> è il più comune nel B2B; termini più brevi (Net 7–15) fanno entrare la liquidità più in fretta.',
                '<strong>Net 7 / Net 15 / Net 30 / Net 60</strong> — de betaling is dat aantal dagen na de factuurdatum verschuldigd. <strong>Net 30</strong> is het gangbaarst in B2B; kortere termijnen (Net 7–15) halen geld sneller binnen.'),
            '<strong>EOM (end of month)</strong> — due at the end of the month the invoice was issued. "Net 30 EOM" means 30 days after month-end.': _t(
                '<strong>EOM (fin de mois)</strong> — dû à la fin du mois d\'émission de la facture. « Net 30 EOM » signifie 30 jours après la fin du mois.',
                '<strong>EOM (Monatsende)</strong> — fällig am Ende des Monats, in dem die Rechnung ausgestellt wurde. „Net 30 EOM" bedeutet 30 Tage nach Monatsende.',
                '<strong>EOM (fin de mes)</strong> — vence al final del mes en que se emitió la factura. «Net 30 EOM» significa 30 días después del fin de mes.',
                '<strong>EOM (fine mese)</strong> — dovuto alla fine del mese in cui è stata emessa la fattura. «Net 30 EOM» significa 30 giorni dopo la fine del mese.',
                '<strong>EOM (einde maand)</strong> — verschuldigd aan het einde van de maand waarin de factuur is uitgereikt. «Net 30 EOM» betekent 30 dagen na het maandeinde.'),
            '<strong>CIA / PIA</strong> — "cash in advance" / "payment in advance." The full amount is paid before you deliver. Common for custom or high-risk work.': _t(
                '<strong>CIA / PIA</strong> — « cash in advance » / « payment in advance ». La totalité est payée avant que vous ne livriez. Courant pour les travaux sur mesure ou à risque élevé.',
                '<strong>CIA / PIA</strong> — „cash in advance" / „payment in advance". Der volle Betrag wird vor der Lieferung bezahlt. Üblich bei maßgeschneiderten oder risikoreichen Arbeiten.',
                '<strong>CIA / PIA</strong> — «cash in advance» / «payment in advance». El importe completo se paga antes de que usted entregue. Habitual en trabajos a medida o de alto riesgo.',
                '<strong>CIA / PIA</strong> — «cash in advance» / «payment in advance». L\'intero importo si paga prima che tu consegni. Comune per lavori su misura o ad alto rischio.',
                '<strong>CIA / PIA</strong> — «cash in advance» / «payment in advance». Het volledige bedrag wordt betaald voordat u levert. Gebruikelijk bij maatwerk of werk met een hoog risico.'),
            '<strong>Deposit / 50% upfront</strong> — part paid before work begins, the balance on completion. Protects you on larger projects.': _t(
                '<strong>Acompte / 50 % à l\'avance</strong> — une partie payée avant le début du travail, le solde à l\'achèvement. Vous protège sur les projets plus importants.',
                '<strong>Anzahlung / 50 % im Voraus</strong> — ein Teil vor Arbeitsbeginn, der Rest bei Fertigstellung. Schützt Sie bei größeren Projekten.',
                '<strong>Anticipo / 50 % por adelantado</strong> — una parte pagada antes de empezar, el resto al finalizar. Le protege en proyectos más grandes.',
                '<strong>Acconto / 50% in anticipo</strong> — una parte pagata prima dell\'inizio del lavoro, il saldo al completamento. Ti protegge sui progetti più grandi.',
                '<strong>Aanbetaling / 50% vooraf</strong> — een deel betaald voordat het werk begint, het saldo bij oplevering. Beschermt u bij grotere projecten.'),
            '<strong>Milestone billing</strong> — payment tied to stages of delivery, so cash arrives as the work progresses.': _t(
                '<strong>Facturation par jalons</strong> — le paiement est lié aux étapes de livraison, si bien que la trésorerie arrive à mesure que le travail avance.',
                '<strong>Meilenstein-Abrechnung</strong> — die Zahlung ist an Lieferstufen gekoppelt, sodass das Geld mit dem Arbeitsfortschritt eingeht.',
                '<strong>Facturación por hitos</strong> — el pago se vincula a etapas de entrega, de modo que el efectivo llega a medida que avanza el trabajo.',
                '<strong>Fatturazione a milestone</strong> — il pagamento è legato alle fasi di consegna, così la liquidità arriva man mano che il lavoro procede.',
                '<strong>Facturering per mijlpaal</strong> — de betaling is gekoppeld aan leverfasen, zodat geld binnenkomt naarmate het werk vordert.'),
            '<strong>Retainer</strong> — a recurring fixed amount, billed ahead, for ongoing work.': _t(
                '<strong>Forfait récurrent (retainer)</strong> — un montant fixe récurrent, facturé d\'avance, pour un travail continu.',
                '<strong>Retainer</strong> — ein wiederkehrender Festbetrag, im Voraus abgerechnet, für laufende Arbeit.',
                '<strong>Iguala (retainer)</strong> — un importe fijo recurrente, facturado por adelantado, para trabajo continuo.',
                '<strong>Retainer</strong> — un importo fisso ricorrente, fatturato in anticipo, per lavoro continuativo.',
                '<strong>Retainer</strong> — een terugkerend vast bedrag, vooraf gefactureerd, voor doorlopend werk.'),
            'Early-payment discounts: "2/10 Net 30"': _t('Escomptes pour paiement anticipé : « 2/10 Net 30 »', 'Skonti für frühe Zahlung: „2/10 Net 30"', 'Descuentos por pronto pago: «2/10 Net 30»', 'Sconti per pagamento anticipato: «2/10 Net 30»', 'Kortingen voor vroeg betalen: «2/10 Net 30»'),
            'This is the one that confuses people. <strong>2/10 Net 30</strong> means: the full amount is due in 30 days, but if the customer pays within 10 days, they take a 2% discount. It\'s a tool to pull cash in sooner. Just weigh the cost — offering 2% to be paid 20 days early is a real discount, so use it where faster cash is worth more than the margin.': _t(
                'C\'est celle qui embrouille les gens. <strong>2/10 Net 30</strong> signifie : le montant total est dû sous 30 jours, mais si le client paie dans les 10 jours, il bénéficie d\'un escompte de 2 %. C\'est un outil pour faire rentrer la trésorerie plus tôt. Pesez simplement le coût — offrir 2 % pour être payé 20 jours plus tôt est un vrai escompte, alors utilisez-le là où une trésorerie plus rapide vaut plus que la marge.',
                'Diese verwirrt die Leute. <strong>2/10 Net 30</strong> bedeutet: Der volle Betrag ist in 30 Tagen fällig, doch zahlt der Kunde binnen 10 Tagen, erhält er 2 % Skonto. Es ist ein Mittel, um Geld früher hereinzuholen. Wägen Sie nur die Kosten ab — 2 % anzubieten, um 20 Tage früher bezahlt zu werden, ist ein echter Rabatt, also nutzen Sie ihn dort, wo schnelleres Geld mehr wert ist als die Marge.',
                'Esta es la que confunde a la gente. <strong>2/10 Net 30</strong> significa: el importe total vence en 30 días, pero si el cliente paga dentro de 10 días, obtiene un 2 % de descuento. Es una herramienta para adelantar el efectivo. Solo sopese el coste — ofrecer un 2 % por cobrar 20 días antes es un descuento real, así que úselo donde el efectivo más rápido valga más que el margen.',
                'Questa è quella che confonde le persone. <strong>2/10 Net 30</strong> significa: l\'intero importo è dovuto in 30 giorni, ma se il cliente paga entro 10 giorni ottiene uno sconto del 2%. È uno strumento per anticipare la liquidità. Valuta solo il costo — offrire il 2% per essere pagato 20 giorni prima è uno sconto reale, quindi usalo dove la liquidità più veloce vale più del margine.',
                'Dit is degene die mensen in de war brengt. <strong>2/10 Net 30</strong> betekent: het volledige bedrag is binnen 30 dagen verschuldigd, maar als de klant binnen 10 dagen betaalt, krijgt hij 2% korting. Het is een middel om geld eerder binnen te halen. Weeg alleen de kosten af — 2% bieden om 20 dagen eerder betaald te worden is een echte korting, dus gebruik het waar sneller geld meer waard is dan de marge.'),
            'Start the clock on the right date': _t('Démarrez le compte à rebours à la bonne date', 'Starten Sie die Frist am richtigen Datum', 'Empiece el reloj en la fecha correcta', 'Fai partire il conteggio dalla data giusta', 'Laat de klok op de juiste datum starten'),
            '"Net 30" is meaningless if no one agrees what day zero is. Make it explicit: is it 30 days from the <strong>invoice date</strong>, the <strong>delivery date</strong>, or receipt of the invoice? Better still, state the actual due date ("Due: October 1, 2026") on the invoice. Specific dates get paid; relative terms get interpreted.': _t(
                '« Net 30 » ne veut rien dire si personne ne s\'accorde sur le jour zéro. Rendez-le explicite : est-ce 30 jours à partir de la <strong>date de facture</strong>, de la <strong>date de livraison</strong> ou de la réception de la facture ? Mieux encore, indiquez la date d\'échéance réelle (« Échéance : 1 octobre 2026 ») sur la facture. Les dates précises sont payées ; les termes relatifs sont interprétés.',
                '„Net 30" ist bedeutungslos, wenn niemand sich einig ist, was Tag null ist. Machen Sie es eindeutig: sind es 30 Tage ab <strong>Rechnungsdatum</strong>, <strong>Lieferdatum</strong> oder Rechnungseingang? Besser noch: Nennen Sie das tatsächliche Fälligkeitsdatum („Fällig: 1. Oktober 2026") auf der Rechnung. Konkrete Daten werden bezahlt; relative Angaben werden ausgelegt.',
                '«Net 30» no significa nada si nadie acuerda cuál es el día cero. Hágalo explícito: ¿son 30 días desde la <strong>fecha de la factura</strong>, la <strong>fecha de entrega</strong> o la recepción de la factura? Mejor aún, indique la fecha de vencimiento real («Vence: 1 de octubre de 2026») en la factura. Las fechas concretas se pagan; los términos relativos se interpretan.',
                '«Net 30» non significa nulla se nessuno concorda su quale sia il giorno zero. Rendilo esplicito: sono 30 giorni dalla <strong>data della fattura</strong>, dalla <strong>data di consegna</strong> o dalla ricezione della fattura? Meglio ancora, indica la data di scadenza effettiva («Scadenza: 1 ottobre 2026») sulla fattura. Le date specifiche vengono pagate; i termini relativi vengono interpretati.',
                '«Net 30» betekent niets als niemand het eens is over dag nul. Maak het expliciet: is het 30 dagen vanaf de <strong>factuurdatum</strong>, de <strong>leverdatum</strong> of de ontvangst van de factuur? Beter nog, vermeld de werkelijke vervaldatum («Vervalt: 1 oktober 2026») op de factuur. Concrete data worden betaald; relatieve termen worden geïnterpreteerd.'),
            'How to choose your terms': _t('Comment choisir vos conditions', 'Wie Sie Ihre Bedingungen wählen', 'Cómo elegir sus condiciones', 'Come scegliere le tue condizioni', 'Hoe u uw voorwaarden kiest'),
            '<strong>Match your own cash cycle.</strong> If you pay suppliers on Net 15, collecting on Net 60 quietly finances your customers.': _t(
                '<strong>Alignez-vous sur votre propre cycle de trésorerie.</strong> Si vous payez vos fournisseurs à Net 15, encaisser à Net 60 finance discrètement vos clients.',
                '<strong>Passen Sie sich Ihrem eigenen Cash-Zyklus an.</strong> Zahlen Sie Lieferanten auf Net 15, finanziert das Einziehen auf Net 60 stillschweigend Ihre Kunden.',
                '<strong>Ajústese a su propio ciclo de caja.</strong> Si paga a proveedores a Net 15, cobrar a Net 60 financia en silencio a sus clientes.',
                '<strong>Allineati al tuo ciclo di cassa.</strong> Se paghi i fornitori a Net 15, incassare a Net 60 finanzia in silenzio i tuoi clienti.',
                '<strong>Sluit aan op uw eigen geldcyclus.</strong> Als u leveranciers op Net 15 betaalt, financiert innen op Net 60 stilletjes uw klanten.'),
            '<strong>Shorter for new or risky customers</strong>, more generous for trusted, high-value ones.': _t(
                '<strong>Plus courtes pour les clients nouveaux ou à risque</strong>, plus généreuses pour ceux de confiance et à forte valeur.',
                '<strong>Kürzer für neue oder riskante Kunden</strong>, großzügiger für vertrauenswürdige, hochwertige.',
                '<strong>Más cortas para clientes nuevos o de riesgo</strong>, más generosas para los de confianza y alto valor.',
                '<strong>Più brevi per clienti nuovi o rischiosi</strong>, più generose per quelli fidati e di alto valore.',
                '<strong>Korter voor nieuwe of risicovolle klanten</strong>, ruimer voor vertrouwde klanten met hoge waarde.'),
            '<strong>Add a late-payment policy</strong> (a fee or interest) and state it up front — then apply it consistently.': _t(
                '<strong>Ajoutez une politique de retard de paiement</strong> (des frais ou des intérêts) et annoncez-la d\'emblée — puis appliquez-la avec constance.',
                '<strong>Fügen Sie eine Verzugsregelung hinzu</strong> (Gebühr oder Zinsen) und nennen Sie sie von Anfang an — und wenden Sie sie dann konsequent an.',
                '<strong>Añada una política de morosidad</strong> (una tarifa o intereses) y anúnciela por adelantado — y luego aplíquela con constancia.',
                '<strong>Aggiungi una policy sui ritardi di pagamento</strong> (una commissione o interessi) e dichiarala fin dall\'inizio — poi applicala con costanza.',
                '<strong>Voeg een beleid voor te laat betalen toe</strong> (een vergoeding of rente) en vermeld het vooraf — en pas het dan consequent toe.'),
            '<strong>Make paying effortless</strong> — accepted methods and a payment link on every invoice.': _t(
                '<strong>Rendez le paiement sans effort</strong> — les moyens acceptés et un lien de paiement sur chaque facture.',
                '<strong>Machen Sie das Bezahlen mühelos</strong> — akzeptierte Methoden und ein Zahlungslink auf jeder Rechnung.',
                '<strong>Haga que pagar no cueste esfuerzo</strong> — métodos aceptados y un enlace de pago en cada factura.',
                '<strong>Rendi il pagamento senza sforzo</strong> — metodi accettati e un link di pagamento su ogni fattura.',
                '<strong>Maak betalen moeiteloos</strong> — geaccepteerde methoden en een betaallink op elke factuur.'),
            'Good terms only help if they\'re actually collected. The habits that turn terms into on-time cash — clear invoices, a reminder cadence, and a tight collection process — are covered in our guides to <a href="/blog/payment-reminder-email/">writing payment reminder emails</a>, <a href="/blog/accounts-receivable-best-practices/">accounts receivable best practices</a>, and <a href="/blog/reduce-days-sales-outstanding/">reducing days sales outstanding</a>.': _t(
                'De bonnes conditions n\'aident que si elles sont effectivement recouvrées. Les habitudes qui transforment les conditions en trésorerie ponctuelle — des factures claires, une cadence de rappels et un processus de recouvrement rigoureux — sont détaillées dans nos guides sur <a href="/blog/payment-reminder-email/">la rédaction d\'e-mails de relance de paiement</a>, les <a href="/blog/accounts-receivable-best-practices/">bonnes pratiques de gestion des comptes clients</a> et la <a href="/blog/reduce-days-sales-outstanding/">réduction du days sales outstanding</a>.',
                'Gute Bedingungen helfen nur, wenn sie auch eingezogen werden. Die Gewohnheiten, die Bedingungen in pünktliches Geld verwandeln — klare Rechnungen, ein Erinnerungsrhythmus und ein straffer Inkassoprozess — behandeln unsere Leitfäden zum <a href="/blog/payment-reminder-email/">Schreiben von Zahlungserinnerungen</a>, zu <a href="/blog/accounts-receivable-best-practices/">Best Practices im Forderungsmanagement</a> und zum <a href="/blog/reduce-days-sales-outstanding/">Senken der days sales outstanding</a>.',
                'Unas buenas condiciones solo ayudan si de verdad se cobran. Los hábitos que convierten las condiciones en efectivo puntual — facturas claras, una cadencia de recordatorios y un proceso de cobro riguroso — se tratan en nuestras guías sobre <a href="/blog/payment-reminder-email/">cómo redactar correos de recordatorio de pago</a>, las <a href="/blog/accounts-receivable-best-practices/">buenas prácticas de cuentas por cobrar</a> y la <a href="/blog/reduce-days-sales-outstanding/">reducción de los days sales outstanding</a>.',
                'Buone condizioni aiutano solo se vengono davvero incassate. Le abitudini che trasformano le condizioni in liquidità puntuale — fatture chiare, una cadenza di promemoria e un processo di incasso rigoroso — sono trattate nelle nostre guide su <a href="/blog/payment-reminder-email/">come scrivere e-mail di sollecito di pagamento</a>, le <a href="/blog/accounts-receivable-best-practices/">buone pratiche per la gestione dei crediti</a> e la <a href="/blog/reduce-days-sales-outstanding/">riduzione dei days sales outstanding</a>.',
                'Goede voorwaarden helpen alleen als ze ook echt worden geïnd. De gewoonten die voorwaarden omzetten in tijdig geld — duidelijke facturen, een herinneringsritme en een strak incassoproces — komen aan bod in onze gidsen over <a href="/blog/payment-reminder-email/">het schrijven van betalingsherinneringen</a>, <a href="/blog/accounts-receivable-best-practices/">best practices voor debiteurenbeheer</a> en het <a href="/blog/reduce-days-sales-outstanding/">verlagen van de days sales outstanding</a>.'),
            'Set terms once, collect them automatically': _t(
                'Définissez les conditions une fois, recouvrez-les automatiquement',
                'Bedingungen einmal festlegen, automatisch einziehen',
                'Fije las condiciones una vez, cóbrelas automáticamente',
                'Imposta le condizioni una volta, incassale automaticamente',
                'Stel voorwaarden één keer in, int ze automatisch'),
            'Collection puts your terms, due dates, payment links, and reminder sequences on every invoice — so the terms you agree actually turn into cash on time.': _t(
                'Collection place vos conditions, échéances, liens de paiement et séquences de rappel sur chaque facture — pour que les conditions convenues se transforment réellement en trésorerie à temps.',
                'Collection setzt Ihre Bedingungen, Fälligkeitsdaten, Zahlungslinks und Erinnerungssequenzen auf jede Rechnung — damit die vereinbarten Bedingungen wirklich pünktlich zu Geld werden.',
                'Collection coloca sus condiciones, vencimientos, enlaces de pago y secuencias de recordatorio en cada factura — para que las condiciones que acuerda se conviertan de verdad en efectivo a tiempo.',
                'Collection mette le tue condizioni, le scadenze, i link di pagamento e le sequenze di promemoria su ogni fattura — così le condizioni che concordi si trasformano davvero in liquidità puntuale.',
                'Collection zet uw voorwaarden, vervaldata, betaallinks en herinneringsreeksen op elke factuur — zodat de voorwaarden die u afspreekt echt op tijd geld worden.'),
        },
    },

    # =========================================================================
    '/blog/payment-reminder-email/': {
        'src': 'blog/payment-reminder-email/index.html',
        't': {
            **_ARTICLE_SHARED,
            'August 30, 2026': _t('30 août 2026', '30. August 2026', '30 de agosto de 2026', '30 agosto 2026', '30 augustus 2026'),
            '7 min read': _MIN_READ_7,
            # ---- Title / meta / breadcrumb ----
            'How to Write a Payment Reminder Email': _t(
                'Comment rédiger un e-mail de relance de paiement',
                'So schreiben Sie eine Zahlungserinnerung per E-Mail',
                'Cómo redactar un correo de recordatorio de pago',
                'Come scrivere un\'e-mail di sollecito di pagamento',
                'Hoe u een betalingsherinnering per e-mail schrijft'),
            'How to write a payment reminder email that gets you paid — tone, timing, and 5 copy-paste templates for before, on, and after the due date.': _t(
                'Comment rédiger un e-mail de relance de paiement qui vous fait payer — le ton, le timing et 5 modèles à copier-coller pour avant, à et après l\'échéance.',
                'So schreiben Sie eine Zahlungserinnerung per E-Mail, die bezahlt wird — Ton, Timing und 5 Copy-and-paste-Vorlagen für vor, an und nach dem Fälligkeitsdatum.',
                'Cómo redactar un correo de recordatorio de pago que le haga cobrar — tono, momento y 5 plantillas para copiar y pegar para antes, en y después del vencimiento.',
                'Come scrivere un\'e-mail di sollecito di pagamento che ti fa incassare — tono, tempistica e 5 modelli pronti da copiare per prima, alla e dopo la scadenza.',
                'Hoe u een betalingsherinnering per e-mail schrijft die u betaald krijgt — toon, timing en 5 kant-en-klare sjablonen voor vóór, op en na de vervaldatum.'),
            'How to Write a Payment Reminder Email (with 5 Templates)': _T_REMINDER_EMAIL,
            'Tone, timing, and 5 copy-paste templates for polite payment reminders that actually get invoices paid.': _t(
                'Le ton, le timing et 5 modèles à copier-coller pour des relances de paiement polies qui font réellement payer les factures.',
                'Ton, Timing und 5 Copy-and-paste-Vorlagen für höfliche Zahlungserinnerungen, die Rechnungen wirklich bezahlt machen.',
                'Tono, momento y 5 plantillas para copiar y pegar de recordatorios de pago corteses que de verdad hacen cobrar las facturas.',
                'Tono, tempistica e 5 modelli pronti da copiare per solleciti di pagamento cortesi che fanno davvero pagare le fatture.',
                'Toon, timing en 5 kant-en-klare sjablonen voor beleefde betalingsherinneringen die facturen echt betaald krijgen.'),
            'How to write a payment reminder email': _t(
                'Comment rédiger un e-mail de relance de paiement',
                'So schreiben Sie eine Zahlungserinnerung per E-Mail',
                'Cómo redactar un correo de recordatorio de pago',
                'Come scrivere un\'e-mail di sollecito di pagamento',
                'Hoe u een betalingsherinnering per e-mail schrijft'),
            # ---- Body ----
            "Most late payments aren't refusals to pay — they're invoices that slipped down someone's inbox. A clear, well-timed reminder is the single most effective thing you can do to get paid, and it works far better when it's polite, specific, and consistent rather than apologetic or aggressive.": _t(
                'La plupart des retards de paiement ne sont pas des refus de payer — ce sont des factures qui ont glissé au fond d\'une boîte de réception. Un rappel clair et bien synchronisé est la chose la plus efficace que vous puissiez faire pour être payé, et il fonctionne bien mieux lorsqu\'il est poli, précis et constant plutôt que penaud ou agressif.',
                'Die meisten verspäteten Zahlungen sind keine Zahlungsverweigerungen — es sind Rechnungen, die im Posteingang nach unten gerutscht sind. Eine klare, gut getimte Erinnerung ist das Wirksamste, was Sie tun können, um bezahlt zu werden, und sie wirkt weit besser, wenn sie höflich, konkret und konsequent statt entschuldigend oder aggressiv ist.',
                'La mayoría de los pagos tardíos no son negativas a pagar — son facturas que se hundieron en la bandeja de entrada de alguien. Un recordatorio claro y bien sincronizado es lo más eficaz que puede hacer para cobrar, y funciona mucho mejor cuando es cortés, concreto y constante en lugar de disculpándose o agresivo.',
                'La maggior parte dei ritardi di pagamento non sono rifiuti di pagare — sono fatture scivolate in fondo alla casella di qualcuno. Un promemoria chiaro e ben tempestivo è la cosa più efficace che puoi fare per farti pagare, e funziona molto meglio quando è cortese, specifico e coerente anziché scusante o aggressivo.',
                'De meeste late betalingen zijn geen weigering om te betalen — het zijn facturen die onderin iemands inbox zijn weggezakt. Een duidelijke, goed getimede herinnering is het meest effectieve wat u kunt doen om betaald te worden, en werkt veel beter wanneer ze beleefd, specifiek en consistent is in plaats van verontschuldigend of agressief.'),
            'Below are the principles that make a reminder work, followed by five templates you can copy, adapt, and reuse — from a friendly nudge before the due date to a firm final notice.': _t(
                'Voici les principes qui font qu\'un rappel fonctionne, suivis de cinq modèles que vous pouvez copier, adapter et réutiliser — du petit rappel amical avant l\'échéance à l\'avis final ferme.',
                'Nachfolgend die Prinzipien, die eine Erinnerung wirksam machen, gefolgt von fünf Vorlagen, die Sie kopieren, anpassen und wiederverwenden können — vom freundlichen Anstoß vor der Fälligkeit bis zur bestimmten letzten Mahnung.',
                'A continuación, los principios que hacen que un recordatorio funcione, seguidos de cinco plantillas que puede copiar, adaptar y reutilizar — desde un empujón amable antes del vencimiento hasta un aviso final firme.',
                'Di seguito i principi che rendono efficace un promemoria, seguiti da cinque modelli che puoi copiare, adattare e riutilizzare — da una spinta cordiale prima della scadenza a un fermo avviso finale.',
                'Hieronder de principes die een herinnering doen werken, gevolgd door vijf sjablonen die u kunt kopiëren, aanpassen en hergebruiken — van een vriendelijk zetje vóór de vervaldatum tot een stevige laatste aanmaning.'),
            'What makes a payment reminder work': _t('Ce qui fait qu\'une relance de paiement fonctionne', 'Was eine Zahlungserinnerung wirksam macht', 'Qué hace que un recordatorio de pago funcione', 'Cosa rende efficace un sollecito di pagamento', 'Wat een betalingsherinnering doet werken'),
            '<strong>Be specific.</strong> Always include the invoice number, amount, and due date. Vague reminders get vague responses.': _t(
                '<strong>Soyez précis.</strong> Indiquez toujours le numéro de facture, le montant et l\'échéance. Les rappels vagues obtiennent des réponses vagues.',
                '<strong>Seien Sie konkret.</strong> Nennen Sie stets Rechnungsnummer, Betrag und Fälligkeitsdatum. Vage Erinnerungen bekommen vage Antworten.',
                '<strong>Sea específico.</strong> Incluya siempre el número de factura, el importe y el vencimiento. Los recordatorios vagos obtienen respuestas vagas.',
                '<strong>Sii specifico.</strong> Indica sempre il numero di fattura, l\'importo e la scadenza. Promemoria vaghi ottengono risposte vaghe.',
                '<strong>Wees specifiek.</strong> Vermeld altijd het factuurnummer, het bedrag en de vervaldatum. Vage herinneringen krijgen vage reacties.'),
            '<strong>Make paying effortless.</strong> Include a payment link or clear instructions in every message. Every extra step is a reason to defer.': _t(
                '<strong>Rendez le paiement sans effort.</strong> Incluez un lien de paiement ou des instructions claires dans chaque message. Chaque étape supplémentaire est une raison de remettre à plus tard.',
                '<strong>Machen Sie das Bezahlen mühelos.</strong> Fügen Sie in jede Nachricht einen Zahlungslink oder klare Anweisungen ein. Jeder zusätzliche Schritt ist ein Grund aufzuschieben.',
                '<strong>Haga que pagar no cueste esfuerzo.</strong> Incluya un enlace de pago o instrucciones claras en cada mensaje. Cada paso extra es una razón para postergar.',
                '<strong>Rendi il pagamento senza sforzo.</strong> Includi un link di pagamento o istruzioni chiare in ogni messaggio. Ogni passaggio in più è un motivo per rimandare.',
                '<strong>Maak betalen moeiteloos.</strong> Voeg in elk bericht een betaallink of duidelijke instructies toe. Elke extra stap is een reden om uit te stellen.'),
            '<strong>Keep the tone matched to the stage.</strong> Friendly before and around the due date; firmer as it ages. Skipping straight to stern damages relationships; staying soft forever gets ignored.': _t(
                '<strong>Adaptez le ton à l\'étape.</strong> Amical avant et autour de l\'échéance ; plus ferme à mesure que le retard s\'installe. Passer directement à la sévérité nuit aux relations ; rester toujours doux se fait ignorer.',
                '<strong>Passen Sie den Ton an die Phase an.</strong> Freundlich vor und um die Fälligkeit; bestimmter, je älter die Rechnung wird. Direkt streng zu werden schädigt Beziehungen; ewig sanft zu bleiben wird ignoriert.',
                '<strong>Ajuste el tono a la etapa.</strong> Amable antes y en torno al vencimiento; más firme a medida que envejece. Saltar directamente a lo severo daña las relaciones; quedarse siempre blando se ignora.',
                '<strong>Adatta il tono alla fase.</strong> Cordiale prima e attorno alla scadenza; più fermo man mano che invecchia. Passare subito al severo danneggia i rapporti; restare morbidi per sempre viene ignorato.',
                '<strong>Stem de toon af op de fase.</strong> Vriendelijk vóór en rond de vervaldatum; strenger naarmate ze veroudert. Meteen streng worden schaadt relaties; eeuwig zacht blijven wordt genegeerd.'),
            '<strong>Send on a schedule, not a mood.</strong> A predictable cadence — before due, on the due date, then at set intervals — means nothing slips because someone was busy.': _t(
                '<strong>Envoyez selon un calendrier, pas selon l\'humeur.</strong> Une cadence prévisible — avant l\'échéance, le jour de l\'échéance, puis à intervalles définis — fait que rien ne passe entre les mailles parce que quelqu\'un était occupé.',
                '<strong>Senden Sie nach Zeitplan, nicht nach Laune.</strong> Ein berechenbarer Rhythmus — vor Fälligkeit, am Fälligkeitstag, dann in festen Abständen — sorgt dafür, dass nichts durchrutscht, weil jemand beschäftigt war.',
                '<strong>Envíe según un calendario, no según el ánimo.</strong> Una cadencia previsible — antes del vencimiento, en el vencimiento y luego a intervalos definidos — hace que nada se escape porque alguien estuviera ocupado.',
                '<strong>Invia secondo un calendario, non secondo l\'umore.</strong> Una cadenza prevedibile — prima della scadenza, alla scadenza, poi a intervalli definiti — fa sì che nulla sfugga perché qualcuno era occupato.',
                '<strong>Verstuur volgens een schema, niet naar humeur.</strong> Een voorspelbaar ritme — vóór de vervaldatum, op de vervaldatum en daarna op vaste intervallen — zorgt dat er niets tussendoor glipt omdat iemand het druk had.'),
            '<strong>Make it easy to reply.</strong> Invite questions. A stalled invoice is often one unanswered query away from being paid.': _t(
                '<strong>Facilitez la réponse.</strong> Invitez aux questions. Une facture bloquée n\'est souvent qu\'à une question sans réponse d\'être payée.',
                '<strong>Machen Sie das Antworten leicht.</strong> Laden Sie zu Fragen ein. Eine stockende Rechnung ist oft nur eine unbeantwortete Rückfrage vom Bezahltwerden entfernt.',
                '<strong>Facilite la respuesta.</strong> Invite a preguntar. Una factura estancada suele estar a una consulta sin responder de ser pagada.',
                '<strong>Rendi facile rispondere.</strong> Invita a fare domande. Una fattura bloccata è spesso a una domanda senza risposta dall\'essere pagata.',
                '<strong>Maak antwoorden makkelijk.</strong> Nodig uit tot vragen. Een vastgelopen factuur is vaak maar één onbeantwoorde vraag verwijderd van betaling.'),
            'The 5 templates': _t('Les 5 modèles', 'Die 5 Vorlagen', 'Las 5 plantillas', 'I 5 modelli', 'De 5 sjablonen'),
            '1. Before the due date (friendly heads-up)': _t('1. Avant l\'échéance (rappel amical)', '1. Vor dem Fälligkeitsdatum (freundlicher Hinweis)', '1. Antes del vencimiento (aviso amable)', '1. Prima della scadenza (avviso cordiale)', '1. Vóór de vervaldatum (vriendelijke heads-up)'),
            'Subject: Invoice #[1024] due [Friday, Sep 5]<br /><br />Hi [Name],<br />Just a friendly reminder that invoice #[1024] for [$1,200] is due on [Sep 5]. You can pay securely here: [payment link]. Anything you need from our side, just reply to this email.<br />Thanks so much,<br />[Your name]': _t(
                'Objet : Facture n° [1024] à échéance le [vendredi 5 sept.]<br /><br />Bonjour [Name],<br />Un simple rappel amical : la facture n° [1024] de [$1,200] arrive à échéance le [5 sept.]. Vous pouvez payer en toute sécurité ici : [payment link]. Si vous avez besoin de quoi que ce soit de notre côté, répondez simplement à cet e-mail.<br />Merci beaucoup,<br />[Your name]',
                'Betreff: Rechnung Nr. [1024] fällig am [Freitag, 5. Sep.]<br /><br />Hallo [Name],<br />nur eine freundliche Erinnerung, dass die Rechnung Nr. [1024] über [$1,200] am [5. Sep.] fällig ist. Sie können hier sicher bezahlen: [payment link]. Falls Sie etwas von unserer Seite brauchen, antworten Sie einfach auf diese E-Mail.<br />Vielen Dank,<br />[Your name]',
                'Asunto: Factura n.º [1024] con vencimiento [viernes 5 de sept.]<br /><br />Hola [Name]:<br />Solo un recordatorio amable de que la factura n.º [1024] por [$1,200] vence el [5 de sept.]. Puede pagar de forma segura aquí: [payment link]. Si necesita algo de nuestra parte, basta con responder a este correo.<br />Muchas gracias,<br />[Your name]',
                'Oggetto: Fattura n. [1024] in scadenza [venerdì 5 set.]<br /><br />Ciao [Name],<br />solo un promemoria cordiale che la fattura n. [1024] di [$1,200] scade il [5 set.]. Puoi pagare in sicurezza qui: [payment link]. Se ti serve qualcosa da parte nostra, rispondi semplicemente a questa e-mail.<br />Grazie mille,<br />[Your name]',
                'Onderwerp: Factuur nr. [1024] vervalt [vrijdag 5 sep.]<br /><br />Hallo [Name],<br />slechts een vriendelijke herinnering dat factuur nr. [1024] voor [$1,200] vervalt op [5 sep.]. U kunt hier veilig betalen: [payment link]. Hebt u iets van onze kant nodig, beantwoord dan gewoon deze e-mail.<br />Hartelijk dank,<br />[Your name]'),
            '2. On the due date': _t('2. Le jour de l\'échéance', '2. Am Fälligkeitstag', '2. El día del vencimiento', '2. Il giorno della scadenza', '2. Op de vervaldatum'),
            "Subject: Invoice #[1024] is due today<br /><br />Hi [Name],<br />A quick note that invoice #[1024] for [$1,200] is due today. Here's the link to pay: [payment link]. If it's already on the way, please ignore this — and thank you.<br />Best,<br />[Your name]": _t(
                'Objet : La facture n° [1024] est due aujourd\'hui<br /><br />Bonjour [Name],<br />Un mot rapide : la facture n° [1024] de [$1,200] est due aujourd\'hui. Voici le lien pour payer : [payment link]. Si le paiement est déjà en route, ignorez ce message — et merci.<br />Cordialement,<br />[Your name]',
                'Betreff: Rechnung Nr. [1024] ist heute fällig<br /><br />Hallo [Name],<br />nur eine kurze Notiz: Die Rechnung Nr. [1024] über [$1,200] ist heute fällig. Hier der Link zum Bezahlen: [payment link]. Falls die Zahlung schon unterwegs ist, ignorieren Sie dies bitte — und danke.<br />Beste Grüße,<br />[Your name]',
                'Asunto: La factura n.º [1024] vence hoy<br /><br />Hola [Name]:<br />Una nota rápida: la factura n.º [1024] por [$1,200] vence hoy. Aquí tiene el enlace para pagar: [payment link]. Si ya está en camino, ignore este mensaje — y gracias.<br />Un saludo,<br />[Your name]',
                'Oggetto: La fattura n. [1024] scade oggi<br /><br />Ciao [Name],<br />una nota rapida: la fattura n. [1024] di [$1,200] scade oggi. Ecco il link per pagare: [payment link]. Se è già in arrivo, ignora pure questo messaggio — e grazie.<br />Cordiali saluti,<br />[Your name]',
                'Onderwerp: Factuur nr. [1024] vervalt vandaag<br /><br />Hallo [Name],<br />een korte notitie: factuur nr. [1024] voor [$1,200] vervalt vandaag. Hier is de betaallink: [payment link]. Als de betaling al onderweg is, negeer dit dan — en dank u.<br />Met vriendelijke groet,<br />[Your name]'),
            '3. A few days overdue (gentle follow-up)': _t('3. Quelques jours de retard (relance en douceur)', '3. Einige Tage überfällig (sanftes Nachfassen)', '3. Unos días de retraso (seguimiento suave)', '3. Qualche giorno di ritardo (sollecito gentile)', '3. Enkele dagen te laat (zachte opvolging)'),
            "Subject: Invoice #[1024] — now a few days past due<br /><br />Hi [Name],<br />I wanted to follow up on invoice #[1024] for [$1,200], which was due on [Sep 5]. If there's any issue or question holding it up, let me know and I'll sort it quickly. Otherwise you can pay here: [payment link].<br />Thanks,<br />[Your name]": _t(
                'Objet : Facture n° [1024] — désormais quelques jours de retard<br /><br />Bonjour [Name],<br />Je souhaitais faire le point sur la facture n° [1024] de [$1,200], qui était due le [5 sept.]. Si un problème ou une question la bloque, dites-le-moi et je réglerai cela rapidement. Sinon, vous pouvez payer ici : [payment link].<br />Merci,<br />[Your name]',
                'Betreff: Rechnung Nr. [1024] — jetzt einige Tage überfällig<br /><br />Hallo [Name],<br />ich wollte zur Rechnung Nr. [1024] über [$1,200] nachfassen, die am [5. Sep.] fällig war. Falls ein Problem oder eine Frage sie aufhält, sagen Sie Bescheid, und ich kläre es rasch. Andernfalls können Sie hier bezahlen: [payment link].<br />Danke,<br />[Your name]',
                'Asunto: Factura n.º [1024] — ahora con unos días de retraso<br /><br />Hola [Name]:<br />Quería hacer seguimiento de la factura n.º [1024] por [$1,200], que vencía el [5 de sept.]. Si hay algún problema o duda que la esté frenando, dígamelo y lo resolveré rápido. De lo contrario, puede pagar aquí: [payment link].<br />Gracias,<br />[Your name]',
                'Oggetto: Fattura n. [1024] — ora in ritardo di qualche giorno<br /><br />Ciao [Name],<br />volevo dare seguito alla fattura n. [1024] di [$1,200], che scadeva il [5 set.]. Se c\'è un problema o una domanda che la blocca, fammelo sapere e lo risolvo in fretta. Altrimenti puoi pagare qui: [payment link].<br />Grazie,<br />[Your name]',
                'Onderwerp: Factuur nr. [1024] — nu enkele dagen te laat<br /><br />Hallo [Name],<br />ik wilde de factuur nr. [1024] voor [$1,200] opvolgen, die verviel op [5 sep.]. Als er een probleem of vraag is die het ophoudt, laat het me weten en ik regel het snel. Anders kunt u hier betalen: [payment link].<br />Bedankt,<br />[Your name]'),
            '4. Two weeks overdue (firm but professional)': _t('4. Deux semaines de retard (ferme mais professionnel)', '4. Zwei Wochen überfällig (bestimmt, aber professionell)', '4. Dos semanas de retraso (firme pero profesional)', '4. Due settimane di ritardo (fermo ma professionale)', '4. Twee weken te laat (stevig maar professioneel)'),
            "Subject: Second reminder — invoice #[1024] past due<br /><br />Hi [Name],<br />Invoice #[1024] for [$1,200] is now two weeks past its due date of [Sep 5]. Please arrange payment at your earliest convenience: [payment link]. If there's a reason for the delay, I'd appreciate a quick note so we can find a way forward.<br />Regards,<br />[Your name]": _t(
                'Objet : Deuxième rappel — facture n° [1024] en retard<br /><br />Bonjour [Name],<br />La facture n° [1024] de [$1,200] a maintenant deux semaines de retard sur son échéance du [5 sept.]. Merci d\'organiser le paiement dès que possible : [payment link]. S\'il y a une raison au retard, un petit mot serait apprécié afin que nous trouvions une solution.<br />Cordialement,<br />[Your name]',
                'Betreff: Zweite Erinnerung — Rechnung Nr. [1024] überfällig<br /><br />Hallo [Name],<br />die Rechnung Nr. [1024] über [$1,200] ist nun zwei Wochen über ihr Fälligkeitsdatum vom [5. Sep.] hinaus. Bitte veranlassen Sie die Zahlung baldmöglichst: [payment link]. Gibt es einen Grund für die Verzögerung, wäre eine kurze Nachricht hilfreich, damit wir einen Weg finden.<br />Mit freundlichen Grüßen,<br />[Your name]',
                'Asunto: Segundo recordatorio — factura n.º [1024] vencida<br /><br />Hola [Name]:<br />La factura n.º [1024] por [$1,200] lleva ya dos semanas vencida desde su fecha del [5 de sept.]. Le ruego que gestione el pago cuanto antes: [payment link]. Si hay algún motivo para el retraso, agradecería una nota breve para encontrar una salida.<br />Saludos,<br />[Your name]',
                'Oggetto: Secondo sollecito — fattura n. [1024] scaduta<br /><br />Ciao [Name],<br />la fattura n. [1024] di [$1,200] è ormai in ritardo di due settimane rispetto alla scadenza del [5 set.]. Ti chiedo di predisporre il pagamento quanto prima: [payment link]. Se c\'è un motivo per il ritardo, gradirei una breve nota così da trovare una soluzione.<br />Cordiali saluti,<br />[Your name]',
                'Onderwerp: Tweede herinnering — factuur nr. [1024] achterstallig<br /><br />Hallo [Name],<br />factuur nr. [1024] voor [$1,200] is nu twee weken over de vervaldatum van [5 sep.] heen. Gelieve de betaling zo spoedig mogelijk te regelen: [payment link]. Is er een reden voor de vertraging, dan stel ik een kort bericht op prijs zodat we een oplossing kunnen vinden.<br />Met vriendelijke groet,<br />[Your name]'),
            '5. Final notice': _t('5. Avis final', '5. Letzte Mahnung', '5. Aviso final', '5. Avviso finale', '5. Laatste aanmaning'),
            "Subject: Final reminder — invoice #[1024], [30] days overdue<br /><br />Hi [Name],<br />Despite previous reminders, invoice #[1024] for [$1,200] remains unpaid [30] days after its due date. Please settle it by [date] to avoid [late fees / a pause in service / referral for collection] as set out in our terms. You can pay here: [payment link]. I'd much rather resolve this directly — please reply if anything is standing in the way.<br />Regards,<br />[Your name]": _t(
                'Objet : Dernier rappel — facture n° [1024], [30] jours de retard<br /><br />Bonjour [Name],<br />Malgré nos précédents rappels, la facture n° [1024] de [$1,200] reste impayée [30] jours après son échéance. Merci de la régler avant le [date] pour éviter [des pénalités de retard / une suspension du service / un transfert en recouvrement] comme prévu dans nos conditions. Vous pouvez payer ici : [payment link]. Je préférerais de loin régler cela directement — répondez si quoi que ce soit fait obstacle.<br />Cordialement,<br />[Your name]',
                'Betreff: Letzte Erinnerung — Rechnung Nr. [1024], [30] Tage überfällig<br /><br />Hallo [Name],<br />trotz vorheriger Erinnerungen ist die Rechnung Nr. [1024] über [$1,200] [30] Tage nach Fälligkeit weiterhin offen. Bitte begleichen Sie sie bis zum [date], um [Verzugsgebühren / eine Aussetzung des Service / eine Übergabe an das Inkasso] gemäß unseren Bedingungen zu vermeiden. Sie können hier bezahlen: [payment link]. Weit lieber würde ich das direkt klären — antworten Sie bitte, falls etwas im Weg steht.<br />Mit freundlichen Grüßen,<br />[Your name]',
                'Asunto: Recordatorio final — factura n.º [1024], [30] días de retraso<br /><br />Hola [Name]:<br />A pesar de recordatorios anteriores, la factura n.º [1024] por [$1,200] sigue sin pagarse [30] días después de su vencimiento. Le ruego que la liquide antes del [date] para evitar [recargos por mora / una pausa en el servicio / la derivación a cobro] según lo establecido en nuestras condiciones. Puede pagar aquí: [payment link]. Preferiría con mucho resolver esto directamente — responda si algo lo impide.<br />Saludos,<br />[Your name]',
                'Oggetto: Sollecito finale — fattura n. [1024], [30] giorni di ritardo<br /><br />Ciao [Name],<br />nonostante i precedenti solleciti, la fattura n. [1024] di [$1,200] risulta ancora insoluta [30] giorni dopo la scadenza. Ti chiedo di saldarla entro il [date] per evitare [penali di mora / una sospensione del servizio / l\'invio al recupero crediti] come previsto dalle nostre condizioni. Puoi pagare qui: [payment link]. Preferirei di gran lunga risolvere direttamente — rispondi se qualcosa lo impedisce.<br />Cordiali saluti,<br />[Your name]',
                'Onderwerp: Laatste herinnering — factuur nr. [1024], [30] dagen te laat<br /><br />Hallo [Name],<br />ondanks eerdere herinneringen blijft factuur nr. [1024] voor [$1,200] [30] dagen na de vervaldatum onbetaald. Gelieve deze vóór [date] te voldoen om [boetes voor te laat betalen / een onderbreking van de dienst / doorverwijzing naar incasso] te vermijden zoals vastgelegd in onze voorwaarden. U kunt hier betalen: [payment link]. Ik los dit veel liever rechtstreeks op — reageer als er iets in de weg staat.<br />Met vriendelijke groet,<br />[Your name]'),
            'Templates get you consistency; sending them by hand gets you inconsistency again the moment things get busy. The real win is automating the sequence so each reminder goes out at the right moment without anyone remembering to send it. That\'s part of a broader system — see our guides to <a href="/blog/reduce-days-sales-outstanding/">reducing days sales outstanding</a> and <a href="/blog/accounts-receivable-best-practices/">accounts receivable best practices</a> for how the reminders fit into the whole cash-collection picture.': _t(
                'Les modèles apportent de la constance ; les envoyer à la main ramène l\'incohérence dès que l\'activité s\'intensifie. Le vrai gain, c\'est d\'automatiser la séquence pour que chaque rappel parte au bon moment sans que personne n\'ait à y penser. Cela fait partie d\'un système plus large — consultez nos guides sur la <a href="/blog/reduce-days-sales-outstanding/">réduction du days sales outstanding</a> et les <a href="/blog/accounts-receivable-best-practices/">bonnes pratiques de gestion des comptes clients</a> pour voir comment les rappels s\'inscrivent dans l\'ensemble du recouvrement.',
                'Vorlagen bringen Konsistenz; sie von Hand zu versenden bringt die Inkonsistenz zurück, sobald es hektisch wird. Der echte Gewinn ist, die Sequenz zu automatisieren, damit jede Erinnerung zum richtigen Zeitpunkt hinausgeht, ohne dass jemand daran denken muss. Das ist Teil eines größeren Systems — sehen Sie unsere Leitfäden zum <a href="/blog/reduce-days-sales-outstanding/">Senken der days sales outstanding</a> und zu <a href="/blog/accounts-receivable-best-practices/">Best Practices im Forderungsmanagement</a>, wie die Erinnerungen ins gesamte Inkasso passen.',
                'Las plantillas le dan constancia; enviarlas a mano le devuelve la incoherencia en cuanto hay ajetreo. La verdadera ventaja es automatizar la secuencia para que cada recordatorio salga en el momento justo sin que nadie tenga que acordarse. Forma parte de un sistema más amplio — consulte nuestras guías sobre la <a href="/blog/reduce-days-sales-outstanding/">reducción de los days sales outstanding</a> y las <a href="/blog/accounts-receivable-best-practices/">buenas prácticas de cuentas por cobrar</a> para ver cómo encajan los recordatorios en todo el cobro.',
                'I modelli danno costanza; inviarli a mano riporta l\'incoerenza appena le cose si fanno frenetiche. Il vero vantaggio è automatizzare la sequenza così che ogni promemoria parta al momento giusto senza che nessuno debba ricordarsene. Fa parte di un sistema più ampio — consulta le nostre guide sulla <a href="/blog/reduce-days-sales-outstanding/">riduzione dei days sales outstanding</a> e sulle <a href="/blog/accounts-receivable-best-practices/">buone pratiche per la gestione dei crediti</a> per capire come i promemoria si inseriscono nell\'intero incasso.',
                'Sjablonen geven u consistentie; ze met de hand versturen geeft u weer inconsistentie zodra het druk wordt. De echte winst is de reeks automatiseren zodat elke herinnering op het juiste moment uitgaat zonder dat iemand eraan hoeft te denken. Dat is onderdeel van een breder systeem — zie onze gidsen over het <a href="/blog/reduce-days-sales-outstanding/">verlagen van de days sales outstanding</a> en <a href="/blog/accounts-receivable-best-practices/">best practices voor debiteurenbeheer</a> voor hoe de herinneringen in het hele incassoproces passen.'),
            'Let the reminders send themselves': _t(
                'Laissez les rappels s\'envoyer d\'eux-mêmes',
                'Lassen Sie die Erinnerungen sich selbst versenden',
                'Deje que los recordatorios se envíen solos',
                'Lascia che i promemoria si inviino da soli',
                'Laat de herinneringen zichzelf versturen'),
            'Collection runs automated reminder sequences with payment links built in — polite before the due date, firmer as invoices age — so you get paid faster without chasing.': _t(
                'Collection exécute des séquences de rappels automatisées avec liens de paiement intégrés — polies avant l\'échéance, plus fermes à mesure que les factures vieillissent — pour que vous soyez payé plus vite sans relancer.',
                'Collection führt automatisierte Erinnerungssequenzen mit integrierten Zahlungslinks aus — höflich vor der Fälligkeit, bestimmter, je älter die Rechnungen werden — damit Sie schneller bezahlt werden, ohne nachzufassen.',
                'Collection ejecuta secuencias de recordatorios automatizadas con enlaces de pago integrados — corteses antes del vencimiento, más firmes a medida que envejecen las facturas — para que cobre más rápido sin perseguir.',
                'Collection esegue sequenze di promemoria automatizzate con link di pagamento integrati — cortesi prima della scadenza, più fermi man mano che le fatture invecchiano — così incassi più in fretta senza inseguire.',
                'Collection voert geautomatiseerde herinneringsreeksen uit met ingebouwde betaallinks — beleefd vóór de vervaldatum, strenger naarmate facturen verouderen — zodat u sneller betaald wordt zonder achtervolging.'),
        },
    },

    # =========================================================================
    '/blog/reduce-days-sales-outstanding/': {
        'src': 'blog/reduce-days-sales-outstanding/index.html',
        't': {
            **_ARTICLE_SHARED,
            'August 24, 2026': _t('24 août 2026', '24. August 2026', '24 de agosto de 2026', '24 agosto 2026', '24 augustus 2026'),
            '6 min read': _MIN_READ_6,
            # ---- Title / meta / breadcrumb ----
            'How to Reduce Days Sales Outstanding (DSO)': _t(
                'Comment réduire le Days Sales Outstanding (DSO)',
                'So senken Sie die Days Sales Outstanding (DSO)',
                'Cómo reducir los Days Sales Outstanding (DSO)',
                'Come ridurre i Days Sales Outstanding (DSO)',
                'Hoe u de Days Sales Outstanding (DSO) verlaagt'),
            'A practical guide to lowering DSO: how to calculate it, the seven levers that move it, and how to get invoices paid faster without hiring a bigger team.': _t(
                'Un guide pratique pour abaisser le DSO : comment le calculer, les sept leviers qui l\'influencent et comment faire payer les factures plus vite sans agrandir l\'équipe.',
                'Ein praktischer Leitfaden zum Senken des DSO: wie Sie ihn berechnen, die sieben Hebel, die ihn bewegen, und wie Sie Rechnungen schneller bezahlt bekommen, ohne ein größeres Team einzustellen.',
                'Una guía práctica para bajar el DSO: cómo calcularlo, las siete palancas que lo mueven y cómo cobrar las facturas más rápido sin contratar un equipo más grande.',
                'Una guida pratica per abbassare il DSO: come calcolarlo, le sette leve che lo muovono e come farsi pagare le fatture più in fretta senza assumere un team più grande.',
                'Een praktische gids om de DSO te verlagen: hoe u hem berekent, de zeven hefbomen die hem bewegen en hoe u facturen sneller betaald krijgt zonder een groter team aan te nemen.'),
            'How to Reduce Days Sales Outstanding (DSO): 7 Practical Steps': _T_REDUCE_DSO,
            'How to calculate DSO and the seven levers that bring it down — get invoices paid faster.': _t(
                'Comment calculer le DSO et les sept leviers qui le font baisser — faites payer les factures plus vite.',
                'Wie Sie den DSO berechnen und die sieben Hebel, die ihn senken — Rechnungen schneller bezahlt bekommen.',
                'Cómo calcular el DSO y las siete palancas que lo reducen — cobre las facturas más rápido.',
                'Come calcolare il DSO e le sette leve che lo riducono — fatti pagare le fatture più in fretta.',
                'Hoe u de DSO berekent en de zeven hefbomen die hem omlaag brengen — krijg facturen sneller betaald.'),
            'Reduce DSO': _t('Réduire le DSO', 'DSO senken', 'Reducir el DSO', 'Ridurre il DSO', 'DSO verlagen'),
            # ---- Body ----
            "Days Sales Outstanding (DSO) is the average number of days it takes to collect payment after a sale. It's one of the clearest signals of financial health in any business that invoices customers: a low DSO means cash comes in quickly, a high or rising DSO means money you've already earned is stuck on someone else's balance sheet.": _t(
                'Le Days Sales Outstanding (DSO) est le nombre moyen de jours nécessaires pour encaisser un paiement après une vente. C\'est l\'un des signaux les plus clairs de la santé financière de toute entreprise qui facture ses clients : un DSO faible signifie que la trésorerie rentre vite, un DSO élevé ou en hausse signifie que de l\'argent déjà gagné est bloqué dans le bilan de quelqu\'un d\'autre.',
                'Days Sales Outstanding (DSO) ist die durchschnittliche Anzahl an Tagen, die es dauert, nach einem Verkauf die Zahlung einzuziehen. Es ist eines der klarsten Signale für die finanzielle Gesundheit jedes Unternehmens, das Kunden Rechnungen stellt: ein niedriger DSO bedeutet, dass Geld schnell hereinkommt, ein hoher oder steigender DSO bedeutet, dass bereits verdientes Geld in der Bilanz eines anderen feststeckt.',
                'Los Days Sales Outstanding (DSO) son el número medio de días que se tarda en cobrar tras una venta. Es una de las señales más claras de la salud financiera de cualquier negocio que factura a clientes: un DSO bajo significa que el efectivo entra rápido, un DSO alto o en aumento significa que dinero ya ganado está atrapado en el balance de otra persona.',
                'I Days Sales Outstanding (DSO) sono il numero medio di giorni necessari a incassare il pagamento dopo una vendita. È uno dei segnali più chiari della salute finanziaria di qualsiasi azienda che fattura ai clienti: un DSO basso significa che la liquidità entra in fretta, un DSO alto o in crescita significa che denaro già guadagnato è bloccato nel bilancio di qualcun altro.',
                'Days Sales Outstanding (DSO) is het gemiddelde aantal dagen dat het duurt om na een verkoop betaling te innen. Het is een van de duidelijkste signalen van financiële gezondheid in elk bedrijf dat klanten factureert: een lage DSO betekent dat geld snel binnenkomt, een hoge of stijgende DSO betekent dat al verdiend geld vastzit op de balans van iemand anders.'),
            "The good news is that DSO is highly controllable. Most of what drives it isn't your customers — it's your own process. Here's how to measure it, then seven levers that consistently bring it down.": _t(
                'La bonne nouvelle, c\'est que le DSO est très maîtrisable. L\'essentiel de ce qui le détermine, ce ne sont pas vos clients — c\'est votre propre processus. Voici comment le mesurer, puis sept leviers qui le font baisser de façon constante.',
                'Die gute Nachricht: Der DSO ist gut steuerbar. Das meiste, was ihn treibt, sind nicht Ihre Kunden — es ist Ihr eigener Prozess. So messen Sie ihn, und dann sieben Hebel, die ihn zuverlässig senken.',
                'La buena noticia es que el DSO es muy controlable. La mayor parte de lo que lo impulsa no son sus clientes — es su propio proceso. Aquí tiene cómo medirlo y luego siete palancas que lo reducen de forma constante.',
                'La buona notizia è che il DSO è molto controllabile. La maggior parte di ciò che lo determina non sono i tuoi clienti — è il tuo stesso processo. Ecco come misurarlo, e poi sette leve che lo abbassano in modo costante.',
                'Het goede nieuws is dat de DSO goed te sturen is. Het meeste dat hem aandrijft zijn niet uw klanten — het is uw eigen proces. Zo meet u hem, en daarna zeven hefbomen die hem consequent omlaag brengen.'),
            'How to calculate DSO': _t('Comment calculer le DSO', 'So berechnen Sie den DSO', 'Cómo calcular el DSO', 'Come calcolare il DSO', 'Hoe u de DSO berekent'),
            'The standard formula, measured over a period (usually a month or quarter):': _t(
                'La formule standard, mesurée sur une période (généralement un mois ou un trimestre) :',
                'Die Standardformel, gemessen über einen Zeitraum (meist ein Monat oder Quartal):',
                'La fórmula estándar, medida sobre un periodo (normalmente un mes o un trimestre):',
                'La formula standard, misurata su un periodo (di solito un mese o un trimestre):',
                'De standaardformule, gemeten over een periode (meestal een maand of kwartaal):'),
            'DSO = (Accounts Receivable ÷ Total Credit Sales) × Number of Days': _t(
                'DSO = (Comptes clients ÷ Total des ventes à crédit) × Nombre de jours',
                'DSO = (Forderungen ÷ gesamte Kreditverkäufe) × Anzahl der Tage',
                'DSO = (Cuentas por cobrar ÷ Total de ventas a crédito) × Número de días',
                'DSO = (Crediti verso clienti ÷ Totale vendite a credito) × Numero di giorni',
                'DSO = (Debiteuren ÷ Totale kredietverkopen) × Aantal dagen'),
            'If you have $120,000 in receivables, $600,000 in credit sales over 90 days, your DSO is (120,000 ÷ 600,000) × 90 = <strong>18 days</strong>. Track it monthly. The trend matters more than the absolute number — a DSO creeping up month over month is an early warning long before it becomes a cash-flow problem.': _t(
                'Si vous avez $120,000 de créances et $600,000 de ventes à crédit sur 90 jours, votre DSO est de (120,000 ÷ 600,000) × 90 = <strong>18 jours</strong>. Suivez-le chaque mois. La tendance compte plus que le chiffre absolu — un DSO qui grimpe mois après mois est une alerte précoce, bien avant de devenir un problème de trésorerie.',
                'Wenn Sie $120,000 an Forderungen und $600,000 an Kreditverkäufen über 90 Tage haben, beträgt Ihr DSO (120,000 ÷ 600,000) × 90 = <strong>18 Tage</strong>. Verfolgen Sie ihn monatlich. Der Trend zählt mehr als die absolute Zahl — ein Monat für Monat steigender DSO ist ein Frühwarnsignal, lange bevor er zum Cashflow-Problem wird.',
                'Si tiene $120,000 en cuentas por cobrar y $600,000 en ventas a crédito en 90 días, su DSO es (120,000 ÷ 600,000) × 90 = <strong>18 días</strong>. Contrólelo mensualmente. La tendencia importa más que el número absoluto — un DSO que sube mes a mes es una alerta temprana mucho antes de convertirse en un problema de flujo de caja.',
                'Se hai $120,000 di crediti e $600,000 di vendite a credito su 90 giorni, il tuo DSO è (120,000 ÷ 600,000) × 90 = <strong>18 giorni</strong>. Monitoralo ogni mese. La tendenza conta più del numero assoluto — un DSO che sale mese dopo mese è un segnale d\'allarme precoce, molto prima che diventi un problema di flusso di cassa.',
                'Als u $120,000 aan debiteuren hebt en $600,000 aan kredietverkopen over 90 dagen, is uw DSO (120,000 ÷ 600,000) × 90 = <strong>18 dagen</strong>. Volg hem maandelijks. De trend telt meer dan het absolute getal — een DSO die maand na maand oploopt is een vroeg waarschuwingssignaal, lang voordat het een cashflowprobleem wordt.'),
            'Seven ways to bring DSO down': _t('Sept façons de faire baisser le DSO', 'Sieben Wege, den DSO zu senken', 'Siete formas de reducir el DSO', 'Sette modi per abbassare il DSO', 'Zeven manieren om de DSO omlaag te brengen'),
            '<strong>Invoice immediately and accurately.</strong> The clock starts when the invoice is sent, not when the work is done. Every day of delay in issuing, and every error that triggers a dispute, is a day added to DSO. Automate invoice generation so it happens the moment a job closes.': _t(
                '<strong>Facturez immédiatement et sans erreur.</strong> Le compte à rebours démarre à l\'envoi de la facture, pas à la fin du travail. Chaque jour de retard dans l\'émission, et chaque erreur qui déclenche un litige, ajoute un jour au DSO. Automatisez la génération des factures pour qu\'elle ait lieu dès qu\'une mission se termine.',
                '<strong>Stellen Sie sofort und fehlerfrei Rechnungen aus.</strong> Die Frist beginnt mit dem Versand der Rechnung, nicht mit dem Abschluss der Arbeit. Jeder Tag Verzögerung beim Ausstellen und jeder Fehler, der einen Streit auslöst, ist ein Tag mehr beim DSO. Automatisieren Sie die Rechnungserstellung, sodass sie in dem Moment geschieht, in dem ein Auftrag abgeschlossen wird.',
                '<strong>Facture de inmediato y con exactitud.</strong> El reloj empieza cuando se envía la factura, no cuando se termina el trabajo. Cada día de retraso en emitirla, y cada error que provoca una disputa, es un día añadido al DSO. Automatice la generación de facturas para que ocurra en cuanto se cierra un trabajo.',
                '<strong>Fattura subito e con precisione.</strong> Il conteggio parte quando la fattura viene inviata, non quando il lavoro è concluso. Ogni giorno di ritardo nell\'emissione, e ogni errore che scatena una contestazione, è un giorno aggiunto al DSO. Automatizza la generazione delle fatture così che avvenga nel momento in cui un lavoro si chiude.',
                '<strong>Factureer onmiddellijk en nauwkeurig.</strong> De klok start wanneer de factuur wordt verzonden, niet wanneer het werk klaar is. Elke dag vertraging bij het opmaken, en elke fout die een geschil veroorzaakt, is een dag extra bij de DSO. Automatiseer het aanmaken van facturen zodat het gebeurt op het moment dat een klus wordt afgesloten.'),
            '<strong>Set clear terms — and put the due date front and centre.</strong> "Net 30" buried in the footer gets ignored. State the exact due date prominently, along with accepted payment methods and what happens if it\'s missed.': _t(
                '<strong>Fixez des conditions claires — et mettez l\'échéance bien en évidence.</strong> Un « Net 30 » perdu en pied de page est ignoré. Indiquez la date d\'échéance exacte de manière visible, avec les moyens de paiement acceptés et ce qui se passe en cas de dépassement.',
                '<strong>Legen Sie klare Bedingungen fest — und stellen Sie das Fälligkeitsdatum in den Vordergrund.</strong> Ein „Net 30" in der Fußzeile wird ignoriert. Nennen Sie das genaue Fälligkeitsdatum gut sichtbar, samt akzeptierter Zahlungsmethoden und den Folgen bei Versäumnis.',
                '<strong>Fije condiciones claras — y ponga el vencimiento en primer plano.</strong> Un «Net 30» escondido en el pie se ignora. Indique la fecha de vencimiento exacta de forma destacada, junto con los métodos de pago aceptados y qué ocurre si se incumple.',
                '<strong>Stabilisci condizioni chiare — e metti la scadenza bene in vista.</strong> Un «Net 30» nascosto nel piè di pagina viene ignorato. Indica la data di scadenza esatta in modo evidente, insieme ai metodi di pagamento accettati e a cosa succede se non viene rispettata.',
                '<strong>Stel duidelijke voorwaarden op — en zet de vervaldatum vooraan en centraal.</strong> Een «Net 30» verstopt in de voettekst wordt genegeerd. Vermeld de exacte vervaldatum prominent, samen met geaccepteerde betaalmethoden en wat er gebeurt als ze wordt gemist.'),
            '<strong>Automate reminders before and after the due date.</strong> A polite nudge three days before the due date prevents far more late payments than chasing after the fact. Schedule a sequence — pre-due, on-due, and escalating post-due — so nothing depends on someone remembering to follow up.': _t(
                '<strong>Automatisez les rappels avant et après l\'échéance.</strong> Un rappel poli trois jours avant l\'échéance prévient bien plus de retards que les relances après coup. Programmez une séquence — avant échéance, à l\'échéance et en escalade après échéance — pour que rien ne dépende de la mémoire de quelqu\'un.',
                '<strong>Automatisieren Sie Erinnerungen vor und nach der Fälligkeit.</strong> Ein höflicher Anstoß drei Tage vor der Fälligkeit verhindert weit mehr verspätete Zahlungen als Nachfassen im Nachhinein. Planen Sie eine Sequenz — vor Fälligkeit, bei Fälligkeit und eskalierend nach Fälligkeit — damit nichts davon abhängt, dass sich jemand ans Nachfassen erinnert.',
                '<strong>Automatice recordatorios antes y después del vencimiento.</strong> Un empujón cortés tres días antes del vencimiento previene muchos más pagos tardíos que perseguir después. Programe una secuencia — antes del vencimiento, en el vencimiento y en escalada después — para que nada dependa de que alguien recuerde dar seguimiento.',
                '<strong>Automatizza i promemoria prima e dopo la scadenza.</strong> Una spinta cortese tre giorni prima della scadenza previene molti più ritardi che inseguire a posteriori. Programma una sequenza — prima della scadenza, alla scadenza e in escalation dopo — così nulla dipende dal fatto che qualcuno si ricordi di dare seguito.',
                '<strong>Automatiseer herinneringen vóór en na de vervaldatum.</strong> Een beleefd zetje drie dagen vóór de vervaldatum voorkomt veel meer late betalingen dan achteraf achtervolgen. Plan een reeks — vóór de vervaldatum, op de vervaldatum en oplopend daarna — zodat niets afhangt van of iemand eraan denkt op te volgen.'),
            '<strong>Make paying effortless.</strong> Every extra step loses payments. Offer multiple methods and include a direct payment link on the invoice itself.': _t(
                '<strong>Rendez le paiement sans effort.</strong> Chaque étape supplémentaire fait perdre des paiements. Proposez plusieurs moyens et incluez un lien de paiement direct sur la facture elle-même.',
                '<strong>Machen Sie das Bezahlen mühelos.</strong> Jeder zusätzliche Schritt kostet Zahlungen. Bieten Sie mehrere Methoden an und fügen Sie einen direkten Zahlungslink auf der Rechnung selbst ein.',
                '<strong>Haga que pagar no cueste esfuerzo.</strong> Cada paso extra pierde pagos. Ofrezca varios métodos e incluya un enlace de pago directo en la propia factura.',
                '<strong>Rendi il pagamento senza sforzo.</strong> Ogni passaggio in più fa perdere pagamenti. Offri più metodi e includi un link di pagamento diretto sulla fattura stessa.',
                '<strong>Maak betalen moeiteloos.</strong> Elke extra stap kost betalingen. Bied meerdere methoden aan en zet een directe betaallink op de factuur zelf.'),
            '<strong>Offer early-payment incentives where the margin allows.</strong> A small discount for paying within ten days (e.g. "2/10 net 30") can meaningfully pull cash forward for customers who are simply optimising their own timing.': _t(
                '<strong>Offrez des incitations au paiement anticipé lorsque la marge le permet.</strong> Un petit escompte pour un paiement sous dix jours (p. ex. « 2/10 net 30 ») peut réellement avancer la trésorerie pour des clients qui ne font qu\'optimiser leur propre calendrier.',
                '<strong>Bieten Sie Anreize für frühe Zahlung, wo die Marge es zulässt.</strong> Ein kleiner Rabatt für Zahlung binnen zehn Tagen (z. B. „2/10 net 30") kann Geld spürbar vorziehen — bei Kunden, die lediglich ihr eigenes Timing optimieren.',
                '<strong>Ofrezca incentivos por pronto pago cuando el margen lo permita.</strong> Un pequeño descuento por pagar en diez días (p. ej. «2/10 net 30») puede adelantar el efectivo de forma notable con clientes que simplemente optimizan sus propios plazos.',
                '<strong>Offri incentivi al pagamento anticipato dove il margine lo consente.</strong> Un piccolo sconto per il pagamento entro dieci giorni (ad es. «2/10 net 30») può anticipare la liquidità in modo significativo con clienti che stanno solo ottimizzando i propri tempi.',
                '<strong>Bied prikkels voor vroeg betalen waar de marge het toelaat.</strong> Een kleine korting voor betaling binnen tien dagen (bijv. «2/10 net 30») kan geld merkbaar naar voren halen bij klanten die simpelweg hun eigen timing optimaliseren.'),
            '<strong>Segment your receivables by risk and age.</strong> Not every overdue account deserves the same treatment. An aging report that groups balances by 0–30, 31–60, 61–90, and 90+ days lets you focus effort where recovery is most at risk.': _t(
                '<strong>Segmentez vos créances par risque et par ancienneté.</strong> Tous les comptes en retard ne méritent pas le même traitement. Une balance âgée qui regroupe les soldes par 0–30, 31–60, 61–90 et plus de 90 jours vous permet de concentrer l\'effort là où le recouvrement est le plus menacé.',
                '<strong>Segmentieren Sie Ihre Forderungen nach Risiko und Alter.</strong> Nicht jedes überfällige Konto verdient dieselbe Behandlung. Ein Fälligkeitsbericht, der Salden nach 0–30, 31–60, 61–90 und 90+ Tagen gruppiert, lässt Sie den Aufwand dort bündeln, wo die Einbringung am stärksten gefährdet ist.',
                '<strong>Segmente sus cobros por riesgo y antigüedad.</strong> No toda cuenta vencida merece el mismo trato. Un informe de antigüedad que agrupa los saldos por 0–30, 31–60, 61–90 y más de 90 días le permite concentrar el esfuerzo donde el recobro está más en riesgo.',
                '<strong>Segmenta i tuoi crediti per rischio e anzianità.</strong> Non ogni conto scaduto merita lo stesso trattamento. Uno scadenzario che raggruppa i saldi in 0–30, 31–60, 61–90 e oltre 90 giorni ti permette di concentrare lo sforzo dove il recupero è più a rischio.',
                '<strong>Segmenteer uw vorderingen op risico en ouderdom.</strong> Niet elke achterstallige rekening verdient dezelfde behandeling. Een ouderdomsanalyse die saldi groepeert in 0–30, 31–60, 61–90 en 90+ dagen laat u de inspanning richten waar inning het meest op het spel staat.'),
            '<strong>Track promises to pay and disputes in one place.</strong> When a customer says "I\'ll pay Friday" or flags a line item, that needs to be logged against the account — not lost in an inbox. A clear history per account is what turns collections from guesswork into a process.': _t(
                '<strong>Suivez les promesses de paiement et les litiges au même endroit.</strong> Quand un client dit « je paie vendredi » ou signale une ligne, cela doit être consigné sur le compte — pas perdu dans une boîte de réception. Un historique clair par compte est ce qui transforme le recouvrement de la devinette en un processus.',
                '<strong>Erfassen Sie Zahlungszusagen und Streitfälle an einem Ort.</strong> Wenn ein Kunde „ich zahle Freitag" sagt oder eine Position beanstandet, muss das beim Konto vermerkt werden — nicht in einem Posteingang verloren gehen. Eine klare Historie je Konto verwandelt das Inkasso von Rätselraten in einen Prozess.',
                '<strong>Registre las promesas de pago y las disputas en un solo lugar.</strong> Cuando un cliente dice «pago el viernes» o marca una línea, eso debe anotarse en la cuenta — no perderse en una bandeja de entrada. Un historial claro por cuenta es lo que convierte el cobro de una adivinanza en un proceso.',
                '<strong>Registra le promesse di pagamento e le contestazioni in un unico posto.</strong> Quando un cliente dice «pago venerdì» o segnala una voce, va annotato sul conto — non perso in una casella. Una cronologia chiara per conto è ciò che trasforma il recupero da indovinello in processo.',
                '<strong>Houd betalingstoezeggingen en geschillen op één plek bij.</strong> Wanneer een klant zegt «ik betaal vrijdag» of een regel aanmerkt, moet dat bij de rekening worden vastgelegd — niet verloren gaan in een inbox. Een duidelijke geschiedenis per rekening is wat incasso van giswerk in een proces verandert.'),
            'The pattern behind all seven': _t('Le schéma commun aux sept', 'Das Muster hinter allen sieben', 'El patrón detrás de las siete', 'Lo schema dietro tutte e sette', 'Het patroon achter alle zeven'),
            'Notice that none of these require a bigger team — they require a <em>consistent, auditable process</em>. Manual collections break down because they depend on individuals remembering to act. The businesses with the lowest DSO are the ones that have automated the routine follow-ups and reserved human attention for the accounts that genuinely need it.': _t(
                'Remarquez qu\'aucun de ces leviers ne nécessite une équipe plus grande — ils exigent un <em>processus cohérent et auditable</em>. Le recouvrement manuel s\'effondre parce qu\'il dépend d\'individus se souvenant d\'agir. Les entreprises au DSO le plus bas sont celles qui ont automatisé les relances de routine et réservé l\'attention humaine aux comptes qui en ont vraiment besoin.',
                'Beachten Sie, dass keiner davon ein größeres Team erfordert — sie erfordern einen <em>konsistenten, prüfbaren Prozess</em>. Manuelles Inkasso bricht zusammen, weil es davon abhängt, dass Einzelne ans Handeln denken. Die Unternehmen mit dem niedrigsten DSO sind jene, die die Routine-Nachfassaktionen automatisiert und die menschliche Aufmerksamkeit den Konten vorbehalten haben, die sie wirklich brauchen.',
                'Observe que ninguna de ellas requiere un equipo más grande — requieren un <em>proceso coherente y auditable</em>. El cobro manual se viene abajo porque depende de que las personas recuerden actuar. Los negocios con el DSO más bajo son los que han automatizado los seguimientos rutinarios y reservado la atención humana para las cuentas que de verdad la necesitan.',
                'Nota che nessuna di queste richiede un team più grande — richiedono un <em>processo coerente e verificabile</em>. Il recupero manuale crolla perché dipende dal fatto che le persone si ricordino di agire. Le aziende con il DSO più basso sono quelle che hanno automatizzato i solleciti di routine e riservato l\'attenzione umana ai conti che ne hanno davvero bisogno.',
                'Merk op dat geen van deze een groter team vereist — ze vereisen een <em>consistent, controleerbaar proces</em>. Handmatig incasso valt uit elkaar omdat het afhangt van individuen die eraan denken te handelen. De bedrijven met de laagste DSO zijn die welke de routinematige opvolgingen hebben geautomatiseerd en menselijke aandacht hebben gereserveerd voor de rekeningen die het echt nodig hebben.'),
            "That's exactly what a dedicated receivables tool is for: tracking every invoice, automating the reminder sequence, and giving you an aging view so you always know where the cash is.": _t(
                'C\'est exactement à cela que sert un outil dédié aux créances : suivre chaque facture, automatiser la séquence de rappels et vous offrir une vue par ancienneté pour que vous sachiez toujours où se trouve la trésorerie.',
                'Genau dafür ist ein spezialisiertes Forderungstool da: jede Rechnung zu verfolgen, die Erinnerungssequenz zu automatisieren und Ihnen eine Fälligkeitsansicht zu geben, damit Sie stets wissen, wo das Geld ist.',
                'Para eso sirve exactamente una herramienta dedicada de cobros: controlar cada factura, automatizar la secuencia de recordatorios y darle una vista por antigüedad para que siempre sepa dónde está el efectivo.',
                'È esattamente a questo che serve uno strumento dedicato ai crediti: monitorare ogni fattura, automatizzare la sequenza di promemoria e offrirti una vista per anzianità così sai sempre dov\'è la liquidità.',
                'Daar dient een specifiek debiteurentool precies voor: elke factuur volgen, de herinneringsreeks automatiseren en u een ouderdomsweergave geven zodat u altijd weet waar het geld is.'),
            'Put your receivables on autopilot': _t(
                'Mettez vos créances en pilote automatique',
                'Bringen Sie Ihre Forderungen auf Autopilot',
                'Ponga sus cobros en piloto automático',
                'Metti i tuoi crediti in pilota automatico',
                'Zet uw vorderingen op de automatische piloot'),
            'Collection tracks every invoice, automates reminders and payment plans, and reconciles payments — so DSO comes down and nothing slips.': _t(
                'Collection suit chaque facture, automatise les rappels et les échéanciers, et rapproche les paiements — pour que le DSO baisse et que rien ne passe entre les mailles.',
                'Collection verfolgt jede Rechnung, automatisiert Erinnerungen und Zahlungspläne und stimmt Zahlungen ab — damit der DSO sinkt und nichts durchrutscht.',
                'Collection controla cada factura, automatiza recordatorios y planes de pago, y concilia los pagos — para que el DSO baje y nada se escape.',
                'Collection monitora ogni fattura, automatizza promemoria e piani di pagamento e riconcilia i pagamenti — così il DSO scende e nulla sfugge.',
                'Collection volgt elke factuur, automatiseert herinneringen en betalingsregelingen en flet betalingen af — zodat de DSO daalt en er niets tussendoor glipt.'),
        },
    },
}

