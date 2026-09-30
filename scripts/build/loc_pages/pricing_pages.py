# -*- coding: utf-8 -*-
"""Translations for the four FulcrumGrid pricing pages (fr/de/es/it/nl).

Chrome (nav, footer, buttons, tagline, "Request a demo", "Pricing", "Contact",
"About", ...) is handled by the shared COMMON catalog and applied BEFORE this
per-page catalog. So a few phrases that embed a COMMON word are handled by
translating only the surviving substring:
  * "Pricing questions, answered"  -> COMMON turns "Pricing" into the localized
    word; we translate the tail " questions, answered".
  * "Contact sales"                -> COMMON turns "Contact"; we translate the
    tail " sales" (longest-first keeps it clear of "Talk to sales").
  * "About <Product>" CTA buttons  -> COMMON translates "About"; the product
    name stays, so nothing is declared here.
Keys are EXACT substrings of the committed English source (entities, apostrophes
and glyphs copied verbatim). Brand/product/tier names stay English.
"""

def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {}

# ---------------------------------------------------------------------------
# /pricing/
# ---------------------------------------------------------------------------
PAGE['/pricing/'] = {
    'src': 'pricing/index.html',
    't': {
        # ---- Meta (title/og:title use COMMON "Pricing") ----
        "Simple, scalable pricing for FulcrumGrid. Pay per app — HR Suite, Command Center, Collection — or bundle the whole grid. Every app includes a 14-day free trial.": _t(
            "Une tarification simple et évolutive pour FulcrumGrid. Payez par application — HR Suite, Command Center, Collection — ou regroupez toute la grille. Chaque application inclut un essai gratuit de 14 jours.",
            "Einfache, skalierbare Preise für FulcrumGrid. Zahlen Sie pro App — HR Suite, Command Center, Collection — oder bündeln Sie das ganze Grid. Jede App enthält eine 14-tägige kostenlose Testphase.",
            "Precios sencillos y escalables para FulcrumGrid. Pague por app — HR Suite, Command Center, Collection — o agrupe toda la cuadrícula. Cada app incluye una prueba gratuita de 14 días.",
            "Prezzi semplici e scalabili per FulcrumGrid. Paga per app — HR Suite, Command Center, Collection — o metti insieme tutta la griglia. Ogni app include una prova gratuita di 14 giorni.",
            "Eenvoudige, schaalbare prijzen voor FulcrumGrid. Betaal per app — HR Suite, Command Center, Collection — of bundel het hele grid. Elke app bevat een gratis proefperiode van 14 dagen."),
        "Pay per app, or bundle the whole grid. Every app includes a 14-day free trial.": _t(
            "Payez par application, ou regroupez toute la grille. Chaque application inclut un essai gratuit de 14 jours.",
            "Zahlen Sie pro App oder bündeln Sie das ganze Grid. Jede App enthält eine 14-tägige kostenlose Testphase.",
            "Pague por app o agrupe toda la cuadrícula. Cada app incluye una prueba gratuita de 14 días.",
            "Paga per app o metti insieme tutta la griglia. Ogni app include una prova gratuita di 14 giorni.",
            "Betaal per app of bundel het hele grid. Elke app bevat een gratis proefperiode van 14 dagen."),
        # ---- Hero ----
        "Priced <em>per app.</em>": _t(
            "Un prix <em>par application.</em>",
            "Preise <em>pro App.</em>",
            "Un precio <em>por app.</em>",
            "Un prezzo <em>per applicazione.</em>",
            "Een prijs <em>per applicatie.</em>"),
        "Pay only for the apps you use. Each FulcrumGrid app is priced on its own — start with one, add the rest as you grow, all on the same grid.": _t(
            "Ne payez que pour les applications que vous utilisez. Chaque application FulcrumGrid est tarifée séparément — commencez avec une, ajoutez les autres à mesure que vous grandissez, le tout sur la même grille.",
            "Zahlen Sie nur für die Apps, die Sie nutzen. Jede FulcrumGrid-App wird eigenständig bepreist — starten Sie mit einer und fügen Sie weitere hinzu, während Sie wachsen, alles auf demselben Grid.",
            "Pague solo por las apps que use. Cada app de FulcrumGrid tiene su propio precio — empiece con una y añada el resto a medida que crece, todo en la misma cuadrícula.",
            "Paga solo per le app che usi. Ogni app FulcrumGrid ha un prezzo a sé — inizia con una e aggiungi le altre man mano che cresci, tutto sulla stessa griglia.",
            "Betaal alleen voor de apps die u gebruikt. Elke FulcrumGrid-app heeft een eigen prijs — begin met één en voeg de rest toe naarmate u groeit, allemaal op hetzelfde grid."),
        # ---- Section: one price per app ----
        "One price per app": _t("Un prix par application", "Ein Preis pro App", "Un precio por app", "Un prezzo per app", "Eén prijs per app"),
        "Subscribe to the apps you need": _t(
            "Abonnez-vous aux applications dont vous avez besoin",
            "Abonnieren Sie die Apps, die Sie brauchen",
            "Suscríbase a las apps que necesita",
            "Abbonati alle app che ti servono",
            "Abonneer u op de apps die u nodig hebt"),
        "Each app stands on its own, with its own plan. Every one includes core dashboards, exports, and a 14-day free trial.": _t(
            "Chaque application est autonome, avec son propre forfait. Toutes incluent les tableaux de bord essentiels, les exports et un essai gratuit de 14 jours.",
            "Jede App steht für sich, mit ihrem eigenen Tarif. Alle enthalten zentrale Dashboards, Exporte und eine 14-tägige kostenlose Testphase.",
            "Cada app es independiente, con su propio plan. Todas incluyen paneles esenciales, exportaciones y una prueba gratuita de 14 días.",
            "Ogni app è indipendente, con il proprio piano. Tutte includono dashboard essenziali, esportazioni e una prova gratuita di 14 giorni.",
            "Elke app staat op zichzelf, met een eigen abonnement. Elk bevat kern-dashboards, exports en een gratis proefperiode van 14 dagen."),
        # ---- Price cards ----
        "Real-time operations dashboard": _t(
            "Tableau de bord des opérations en temps réel",
            "Echtzeit-Dashboard für den Betrieb",
            "Panel de operaciones en tiempo real",
            "Dashboard operativa in tempo reale",
            "Realtime operationeel dashboard"),
        "Receivables and payments, handled": _t(
            "Créances et paiements, maîtrisés",
            "Forderungen und Zahlungen, im Griff",
            "Cobros y pagos, resueltos",
            "Crediti e pagamenti, gestiti",
            "Vorderingen en betalingen, geregeld"),
        "People operations, hire to retire": _t(
            "Gestion des personnes, de l'embauche au départ",
            "Personalmanagement, von der Einstellung bis zum Ruhestand",
            "Gestión de personas, de la contratación a la jubilación",
            "Gestione del personale, dall'assunzione alla pensione",
            "Personeelsbeheer, van aanwerving tot pensioen"),
        # ---- Price / tier labels ----
        "<div class=\"pl-price\">Free</div>": _t(
            "<div class=\"pl-price\">Gratuit</div>",
            "<div class=\"pl-price\">Kostenlos</div>",
            "<div class=\"pl-price\">Gratis</div>",
            "<div class=\"pl-price\">Gratis</div>",
            "<div class=\"pl-price\">Gratis</div>"),
        "<div class=\"pl-price\">Custom</div>": _t(
            "<div class=\"pl-price\">Sur mesure</div>",
            "<div class=\"pl-price\">Individuell</div>",
            "<div class=\"pl-price\">Personalizado</div>",
            "<div class=\"pl-price\">Personalizzato</div>",
            "<div class=\"pl-price\">Op maat</div>"),
        # Tier proper-name stays English (consistent with FAQ usage).
        "<h4>Enterprise</h4>": _t(
            "<h4>Enterprise</h4>", "<h4>Enterprise</h4>", "<h4>Enterprise</h4>",
            "<h4>Enterprise</h4>", "<h4>Enterprise</h4>"),
        "from ": _t("à partir de ", "ab ", "desde ", "da ", "vanaf "),
        "/ month": _t("/ mois", "/ Monat", "/ mes", "/ mese", "/ maand"),
        "/ seat / month": _t("/ siège / mois", "/ Platz / Monat", "/ asiento / mes", "/ postazione / mese", "/ zitplaats / maand"),
        "/ user / month": _t("/ utilisateur / mois", "/ Nutzer / Monat", "/ usuario / mes", "/ utente / mese", "/ gebruiker / maand"),
        "Live KPIs &amp; custom dashboards": _t(
            "KPI en direct &amp; tableaux de bord personnalisés",
            "Live-KPIs &amp; individuelle Dashboards",
            "KPI en vivo &amp; paneles personalizados",
            "KPI in tempo reale &amp; dashboard personalizzate",
            "Live KPI's &amp; aangepaste dashboards"),
        "Alerts &amp; automated workflows": _t(
            "Alertes &amp; flux de travail automatisés",
            "Warnungen &amp; automatisierte Workflows",
            "Alertas &amp; flujos de trabajo automatizados",
            "Avvisi &amp; flussi di lavoro automatizzati",
            "Meldingen &amp; geautomatiseerde workflows"),
        "Reporting &amp; exports": _t(
            "Rapports &amp; exports", "Berichte &amp; Exporte", "Informes &amp; exportaciones",
            "Report &amp; esportazioni", "Rapportage &amp; exports"),
        "Email support": _t("Assistance par e-mail", "E-Mail-Support", "Soporte por correo", "Supporto via email", "E-mailondersteuning"),
        "See plans": _t("Voir les forfaits", "Tarife ansehen", "Ver planes", "Vedi i piani", "Bekijk abonnementen"),
        "Invoice &amp; ledger tracking": _t(
            "Suivi des factures &amp; du grand livre",
            "Rechnungs- &amp; Buchungsverfolgung",
            "Seguimiento de facturas &amp; libro mayor",
            "Monitoraggio fatture &amp; registro contabile",
            "Facturen- &amp; grootboekregistratie"),
        "Automated reminders &amp; plans": _t(
            "Relances &amp; plans automatisés",
            "Automatisierte Erinnerungen &amp; Zahlungspläne",
            "Recordatorios &amp; planes automatizados",
            "Solleciti &amp; piani automatizzati",
            "Geautomatiseerde herinneringen &amp; plannen"),
        "Payment reconciliation": _t(
            "Rapprochement des paiements", "Zahlungsabgleich", "Conciliación de pagos",
            "Riconciliazione dei pagamenti", "Afstemming van betalingen"),
        "Core HR &amp; time off": _t(
            "RH de base &amp; congés", "Kern-HR &amp; Abwesenheiten", "RR. HH. básicos &amp; ausencias",
            "HR di base &amp; ferie", "Kern-HR &amp; verlof"),
        "Expenses &amp; HR letters": _t(
            "Notes de frais &amp; courriers RH", "Spesen &amp; HR-Schreiben", "Gastos &amp; cartas de RR. HH.",
            "Note spese &amp; lettere HR", "Onkosten &amp; HR-brieven"),
        "Announcements &amp; recognition": _t(
            "Annonces &amp; reconnaissance", "Ankündigungen &amp; Anerkennung", "Anuncios &amp; reconocimiento",
            "Annunci &amp; riconoscimenti", "Aankondigingen &amp; erkenning"),
        "Each app is priced its own way — flat, per seat, or per workspace. Annual billing saves 20%. Every app includes a 14-day free trial.": _t(
            "Chaque application est tarifée à sa manière — forfait fixe, par siège ou par espace de travail. La facturation annuelle fait économiser 20 %. Chaque application inclut un essai gratuit de 14 jours.",
            "Jede App wird auf ihre eigene Weise bepreist — pauschal, pro Platz oder pro Workspace. Die jährliche Abrechnung spart 20 %. Jede App enthält eine 14-tägige kostenlose Testphase.",
            "Cada app se cobra a su manera — tarifa plana, por asiento o por espacio de trabajo. La facturación anual ahorra un 20 %. Cada app incluye una prueba gratuita de 14 días.",
            "Ogni app ha un prezzo a modo suo — forfait, per postazione o per spazio di lavoro. La fatturazione annuale fa risparmiare il 20%. Ogni app include una prova gratuita di 14 giorni.",
            "Elke app wordt op zijn eigen manier geprijsd — vast, per zitplaats of per werkruimte. Jaarlijkse facturering bespaart 20%. Elke app bevat een gratis proefperiode van 14 dagen."),
        # ---- Section: bundle ----
        "Running more than one?": _t("Vous en utilisez plusieurs ?", "Nutzen Sie mehrere?", "¿Usa más de una?", "Ne usi più di una?", "Gebruikt u er meer dan één?"),
        "Bundle the whole grid": _t("Regroupez toute la grille", "Bündeln Sie das ganze Grid", "Agrupe toda la cuadrícula", "Metti insieme tutta la griglia", "Bundel het hele grid"),
        "When you need several apps, one plan covers them all — cheaper than adding them up, with cross-app data and a single bill.": _t(
            "Quand vous avez besoin de plusieurs applications, un seul forfait les couvre toutes — moins cher que de les additionner, avec des données inter-applications et une facture unique.",
            "Wenn Sie mehrere Apps brauchen, deckt ein Tarif sie alle ab — günstiger als die Summe der einzelnen, mit app-übergreifenden Daten und einer einzigen Rechnung.",
            "Cuando necesita varias apps, un solo plan las cubre todas — más barato que sumarlas, con datos entre apps y una única factura.",
            "Quando ti servono più app, un unico piano le copre tutte — più conveniente che sommarle, con dati tra le app e un'unica fattura.",
            "Wanneer u meerdere apps nodig hebt, dekt één abonnement ze allemaal — goedkoper dan ze bij elkaar op te tellen, met app-overschrijdende data en één factuur."),
        "Best value": _t("Meilleur rapport qualité-prix", "Bestes Preis-Leistungs-Verhältnis", "Mejor valor", "Miglior rapporto qualità-prezzo", "Beste waarde"),
        "Whole grid": _t("Grille complète", "Ganzes Grid", "Cuadrícula completa", "Griglia completa", "Hele grid"),
        "Every app, one plan": _t("Toutes les applications, un seul forfait", "Alle Apps, ein Tarif", "Todas las apps, un solo plan", "Tutte le app, un unico piano", "Elke app, één abonnement"),
        "All apps included": _t("Toutes les applications incluses", "Alle Apps enthalten", "Todas las apps incluidas", "Tutte le app incluse", "Alle apps inbegrepen"),
        "Unlimited users": _t("Utilisateurs illimités", "Unbegrenzte Nutzer", "Usuarios ilimitados", "Utenti illimitati", "Onbeperkt aantal gebruikers"),
        "Cross-app data &amp; automations": _t(
            "Données inter-applications &amp; automatisations",
            "App-übergreifende Daten &amp; Automatisierungen",
            "Datos entre apps &amp; automatizaciones",
            "Dati tra le app &amp; automazioni",
            "App-overschrijdende data &amp; automatiseringen"),
        "Role-based access control": _t(
            "Contrôle d'accès basé sur les rôles", "Rollenbasierte Zugriffssteuerung", "Control de acceso basado en roles",
            "Controllo degli accessi basato sui ruoli", "Rolgebaseerde toegangscontrole"),
        "Priority support": _t("Assistance prioritaire", "Priorisierter Support", "Soporte prioritario", "Supporto prioritario", "Prioriteitsondersteuning"),
        "For large or regulated organizations": _t(
            "Pour les grandes organisations ou les secteurs réglementés",
            "Für große oder regulierte Organisationen",
            "Para organizaciones grandes o reguladas",
            "Per organizzazioni grandi o regolamentate",
            "Voor grote of gereguleerde organisaties"),
        "Everything in Whole grid": _t(
            "Tout ce que contient Grille complète", "Alles aus Ganzes Grid", "Todo lo de Cuadrícula completa",
            "Tutto ciò che c'è in Griglia completa", "Alles uit Hele grid"),
        "Advanced security &amp; admin controls": _t(
            "Sécurité avancée &amp; contrôles d'administration",
            "Erweiterte Sicherheit &amp; Admin-Steuerung",
            "Seguridad avanzada &amp; controles de administración",
            "Sicurezza avanzata &amp; controlli di amministrazione",
            "Geavanceerde beveiliging &amp; beheerinstellingen"),
        "Dedicated single-tenant environment": _t(
            "Environnement dédié à locataire unique", "Dedizierte Single-Tenant-Umgebung",
            "Entorno dedicado de un solo inquilino", "Ambiente dedicato single-tenant",
            "Toegewijde single-tenant-omgeving"),
        "On-premise / self-hosted option": _t(
            "Option sur site / auto-hébergée", "On-Premise-/selbstgehostete Option",
            "Opción on-premise / autoalojada", "Opzione on-premise / self-hosted",
            "On-premise / zelf-gehoste optie"),
        "Data residency in your region": _t(
            "Résidence des données dans votre région", "Datenspeicherung in Ihrer Region",
            "Residencia de datos en su región", "Residenza dei dati nella tua regione",
            "Dataresidentie in uw regio"),
        "SLA &amp; dedicated support": _t(
            "SLA &amp; assistance dédiée", "SLA &amp; dedizierter Support", "SLA &amp; soporte dedicado",
            "SLA &amp; supporto dedicato", "SLA &amp; toegewijde ondersteuning"),
        "Custom integrations": _t("Intégrations sur mesure", "Individuelle Integrationen", "Integraciones a medida", "Integrazioni su misura", "Integraties op maat"),
        "Guided onboarding": _t("Intégration accompagnée", "Begleitetes Onboarding", "Incorporación guiada", "Onboarding guidato", "Begeleide onboarding"),
        " sales": _t(" commercial", " Vertrieb", " ventas", " vendite", " verkoop"),
        # ---- FAQ ----
        " questions, answered": _t(
            " : vos questions, nos réponses", " – Ihre Fragen, beantwortet", ": preguntas frecuentes",
            ": domande e risposte", ": vragen beantwoord"),
        "Can I start with just one app?": _t(
            "Puis-je commencer avec une seule application ?", "Kann ich mit nur einer App starten?",
            "¿Puedo empezar con una sola app?", "Posso iniziare con una sola app?", "Kan ik met slechts één app beginnen?"),
        "Yes. Every app is priced on its own, so you can subscribe to just HR Suite, Command Center, or Collection and add the rest whenever you're ready.": _t(
            "Oui. Chaque application est tarifée séparément : vous pouvez vous abonner uniquement à HR Suite, Command Center ou Collection et ajouter le reste quand vous êtes prêt.",
            "Ja. Jede App wird eigenständig bepreist, sodass Sie nur HR Suite, Command Center oder Collection abonnieren und den Rest hinzufügen können, wann immer Sie bereit sind.",
            "Sí. Cada app tiene su propio precio, así que puede suscribirse solo a HR Suite, Command Center o Collection y añadir el resto cuando esté listo.",
            "Sì. Ogni app ha un prezzo a sé, quindi puoi abbonarti solo a HR Suite, Command Center o Collection e aggiungere il resto quando sei pronto.",
            "Ja. Elke app heeft een eigen prijs, dus u kunt zich abonneren op alleen HR Suite, Command Center of Collection en de rest toevoegen wanneer u er klaar voor bent."),
        "Can I add apps later?": _t(
            "Puis-je ajouter des applications plus tard ?", "Kann ich später Apps hinzufügen?",
            "¿Puedo añadir apps más tarde?", "Posso aggiungere app in seguito?", "Kan ik later apps toevoegen?"),
        "Absolutely. Adopt any FulcrumGrid app whenever you're ready — start with one and add more over time, at your own pace.": _t(
            "Absolument. Adoptez n'importe quelle application FulcrumGrid quand vous êtes prêt — commencez avec une et ajoutez-en d'autres au fil du temps, à votre rythme.",
            "Absolut. Führen Sie jede FulcrumGrid-App ein, wann immer Sie bereit sind — starten Sie mit einer und fügen Sie mit der Zeit weitere hinzu, in Ihrem eigenen Tempo.",
            "Por supuesto. Adopte cualquier app de FulcrumGrid cuando esté listo — empiece con una y añada más con el tiempo, a su propio ritmo.",
            "Assolutamente. Adotta qualsiasi app FulcrumGrid quando sei pronto — inizia con una e aggiungine altre nel tempo, al tuo ritmo.",
            "Absoluut. Neem elke FulcrumGrid-app in gebruik wanneer u er klaar voor bent — begin met één en voeg er na verloop van tijd meer toe, in uw eigen tempo."),
        "Is there a free trial?": _t(
            "Y a-t-il un essai gratuit ?", "Gibt es eine kostenlose Testphase?", "¿Hay una prueba gratuita?",
            "È disponibile una prova gratuita?", "Is er een gratis proefperiode?"),
        "Every plan includes a 14-day free trial with full features. No credit card required to start.": _t(
            "Chaque forfait inclut un essai gratuit de 14 jours avec toutes les fonctionnalités. Aucune carte bancaire requise pour commencer.",
            "Jeder Tarif enthält eine 14-tägige kostenlose Testphase mit vollem Funktionsumfang. Keine Kreditkarte erforderlich, um zu starten.",
            "Cada plan incluye una prueba gratuita de 14 días con todas las funciones. No se necesita tarjeta de crédito para empezar.",
            "Ogni piano include una prova gratuita di 14 giorni con tutte le funzionalità. Nessuna carta di credito richiesta per iniziare.",
            "Elk abonnement bevat een gratis proefperiode van 14 dagen met alle functies. Geen creditcard nodig om te beginnen."),
        "How does billing work?": _t(
            "Comment fonctionne la facturation ?", "Wie funktioniert die Abrechnung?", "¿Cómo funciona la facturación?",
            "Come funziona la fatturazione?", "Hoe werkt de facturering?"),
        "Each app is billed monthly its own way — flat per organization, per seat, or per workspace. Switch to annual billing to save 20%. You can change plans at any time.": _t(
            "Chaque application est facturée mensuellement à sa manière — forfait fixe par organisation, par siège ou par espace de travail. Passez à la facturation annuelle pour économiser 20 %. Vous pouvez changer de forfait à tout moment.",
            "Jede App wird monatlich auf ihre eigene Weise abgerechnet — pauschal pro Organisation, pro Platz oder pro Workspace. Wechseln Sie zur jährlichen Abrechnung, um 20 % zu sparen. Sie können den Tarif jederzeit ändern.",
            "Cada app se factura mensualmente a su manera — tarifa plana por organización, por asiento o por espacio de trabajo. Cambie a la facturación anual para ahorrar un 20 %. Puede cambiar de plan en cualquier momento.",
            "Ogni app viene fatturata mensilmente a modo suo — forfait per organizzazione, per postazione o per spazio di lavoro. Passa alla fatturazione annuale per risparmiare il 20%. Puoi cambiare piano in qualsiasi momento.",
            "Elke app wordt maandelijks op zijn eigen manier gefactureerd — vast per organisatie, per zitplaats of per werkruimte. Stap over op jaarlijkse facturering en bespaar 20%. U kunt op elk moment van abonnement wisselen."),
        "Do you offer discounts?": _t(
            "Proposez-vous des remises ?", "Bieten Sie Rabatte an?", "¿Ofrecen descuentos?",
            "Offrite sconti?", "Bieden jullie kortingen aan?"),
        "We offer special pricing for nonprofits, educational institutions, and early-stage startups. Reach out and we'll help find the right fit.": _t(
            "Nous proposons des tarifs spéciaux pour les associations, les établissements d'enseignement et les startups en phase de démarrage. Contactez-nous et nous vous aiderons à trouver la formule adaptée.",
            "Wir bieten Sonderkonditionen für gemeinnützige Organisationen, Bildungseinrichtungen und Start-ups in der Frühphase. Melden Sie sich, und wir helfen Ihnen, das Passende zu finden.",
            "Ofrecemos precios especiales para organizaciones sin ánimo de lucro, instituciones educativas y startups en fase inicial. Escríbanos y le ayudaremos a encontrar la opción adecuada.",
            "Offriamo prezzi speciali per organizzazioni no profit, istituti di istruzione e startup in fase iniziale. Contattaci e ti aiuteremo a trovare la soluzione giusta.",
            "We bieden speciale prijzen voor non-profitorganisaties, onderwijsinstellingen en startups in een vroege fase. Neem contact op en we helpen u de juiste keuze te vinden."),
        # ---- CTA ----
        "Not sure which plan fits?": _t(
            "Vous ne savez pas quel forfait choisir ?", "Nicht sicher, welcher Tarif passt?", "¿No sabe qué plan encaja?",
            "Non sai quale piano scegliere?", "Weet u niet welk abonnement past?"),
        "Tell us about your team and we'll recommend the right setup.": _t(
            "Parlez-nous de votre équipe et nous vous recommanderons la configuration idéale.",
            "Erzählen Sie uns von Ihrem Team, und wir empfehlen Ihnen das richtige Setup.",
            "Cuéntenos sobre su equipo y le recomendaremos la configuración adecuada.",
            "Parlaci del tuo team e ti consiglieremo la configurazione giusta.",
            "Vertel ons over uw team en we bevelen de juiste opzet aan."),
        "Talk to sales": _t("Parler au service commercial", "Mit dem Vertrieb sprechen", "Hablar con ventas", "Parla con le vendite", "Praat met verkoop"),
    },
}

# ---------------------------------------------------------------------------
# /pricing/command-center/
# ---------------------------------------------------------------------------
PAGE['/pricing/command-center/'] = {
    'src': 'pricing/command-center/index.html',
    't': {
        # ---- Meta (title/og:title/og:description/JSON-LD description) ----
        "Command Center pricing &amp; plans | FulcrumGrid": _t(
            "Tarifs &amp; forfaits Command Center | FulcrumGrid",
            "Command Center Preise &amp; Tarife | FulcrumGrid",
            "Precios &amp; planes de Command Center | FulcrumGrid",
            "Prezzi &amp; piani di Command Center | FulcrumGrid",
            "Command Center-prijzen &amp; abonnementen | FulcrumGrid"),
        "Command Center pricing — Pilot, Growth, and Enterprise plans — with a module-by-module breakdown of what's included at each tier.": _t(
            "Tarifs de Command Center — forfaits Pilot, Growth et Enterprise — avec un détail module par module de ce qui est inclus à chaque niveau.",
            "Command Center Preise — Tarife Pilot, Growth und Enterprise — mit einer modulweisen Aufschlüsselung dessen, was in jeder Stufe enthalten ist.",
            "Precios de Command Center — planes Pilot, Growth y Enterprise — con un desglose módulo a módulo de lo que se incluye en cada nivel.",
            "Prezzi di Command Center — piani Pilot, Growth ed Enterprise — con un dettaglio modulo per modulo di ciò che è incluso in ogni livello.",
            "Command Center-prijzen — Pilot-, Growth- en Enterprise-abonnementen — met een module-voor-module-overzicht van wat op elk niveau is inbegrepen."),
        "Command Center pricing — plans and modules | FulcrumGrid": _t(
            "Tarifs de Command Center — forfaits et modules | FulcrumGrid",
            "Command Center Preise — Tarife und Module | FulcrumGrid",
            "Precios de Command Center — planes y módulos | FulcrumGrid",
            "Prezzi di Command Center — piani e moduli | FulcrumGrid",
            "Command Center-prijzen — abonnementen en modules | FulcrumGrid"),
        # ---- Breadcrumb (JSON-LD only; not a visible node) ----
        "Home": _t("Accueil", "Startseite", "Inicio", "Home", "Home"),
        # ---- Hero ----
        "Command Center <em>pricing.</em>": _t(
            "Command Center <em>tarifs.</em>",
            "Command Center <em>Preise.</em>",
            "Command Center <em>precios.</em>",
            "Command Center <em>prezzi.</em>",
            "Command Center <em>prijzen.</em>"),
        # ---- Section eyebrow + heading ----
        "01 · Plans": _t("01 · Forfaits", "01 · Tarife", "01 · Planes", "01 · Piani", "01 · Abonnementen"),
        "Priced per plan.": _t(
            "Un prix par forfait.", "Preise pro Tarif.", "Un precio por plan.",
            "Un prezzo per piano.", "Een prijs per abonnement."),
        # ---- Plan cards: tier proper-names stay English; price label translated ----
        "<h4>Pilot</h4>": _t("<h4>Pilot</h4>", "<h4>Pilot</h4>", "<h4>Pilot</h4>", "<h4>Pilot</h4>", "<h4>Pilot</h4>"),
        "<h4>Growth</h4>": _t("<h4>Growth</h4>", "<h4>Growth</h4>", "<h4>Growth</h4>", "<h4>Growth</h4>", "<h4>Growth</h4>"),
        "<h4>Enterprise</h4>": _t("<h4>Enterprise</h4>", "<h4>Enterprise</h4>", "<h4>Enterprise</h4>", "<h4>Enterprise</h4>", "<h4>Enterprise</h4>"),
        "<th scope=\"col\" class=\"val\">Pilot</th>": _t(
            "<th scope=\"col\" class=\"val\">Pilot</th>", "<th scope=\"col\" class=\"val\">Pilot</th>", "<th scope=\"col\" class=\"val\">Pilot</th>",
            "<th scope=\"col\" class=\"val\">Pilot</th>", "<th scope=\"col\" class=\"val\">Pilot</th>"),
        "<th scope=\"col\" class=\"val col-hi\">Growth</th>": _t(
            "<th scope=\"col\" class=\"val col-hi\">Growth</th>", "<th scope=\"col\" class=\"val col-hi\">Growth</th>", "<th scope=\"col\" class=\"val col-hi\">Growth</th>",
            "<th scope=\"col\" class=\"val col-hi\">Growth</th>", "<th scope=\"col\" class=\"val col-hi\">Growth</th>"),
        "<th scope=\"col\" class=\"val\">Enterprise</th>": _t(
            "<th scope=\"col\" class=\"val\">Enterprise</th>", "<th scope=\"col\" class=\"val\">Enterprise</th>", "<th scope=\"col\" class=\"val\">Enterprise</th>",
            "<th scope=\"col\" class=\"val\">Enterprise</th>", "<th scope=\"col\" class=\"val\">Enterprise</th>"),
        "<span class=\"amt\">Custom</span>": _t(
            "<span class=\"amt\">Sur mesure</span>", "<span class=\"amt\">Individuell</span>", "<span class=\"amt\">Personalizado</span>",
            "<span class=\"amt\">Personalizzato</span>", "<span class=\"amt\">Op maat</span>"),
        "Run strategy, finance, and governance from one command center — priced by plan, from a piloting team to a multi-department, regulated organization.": _t(
            "Pilotez stratégie, finance et gouvernance depuis un seul centre de commande — tarifé par forfait, de l'équipe pilote à l'organisation multi-services et réglementée.",
            "Steuern Sie Strategie, Finanzen und Governance von einer einzigen Kommandozentrale aus — nach Tarif bepreist, vom pilotierenden Team bis zur abteilungsübergreifenden, regulierten Organisation.",
            "Gestione estrategia, finanzas y gobernanza desde un único centro de mando — con precio por plan, desde un equipo piloto hasta una organización multidepartamental y regulada.",
            "Gestisci strategia, finanza e governance da un unico centro di comando — con prezzo per piano, dal team pilota all'organizzazione multi-reparto e regolamentata.",
            "Bestuur strategie, financiën en governance vanuit één commandocentrum — geprijsd per abonnement, van een pilotteam tot een multidepartementale, gereguleerde organisatie."),
        # ---- Cards ----
        "Small team piloting": _t("Petite équipe en phase pilote", "Kleines Team im Pilotbetrieb", "Equipo pequeño en piloto", "Piccolo team in fase pilota", "Klein team in pilot"),
        "Scaling company": _t("Entreprise en croissance", "Wachsendes Unternehmen", "Empresa en crecimiento", "Azienda in crescita", "Groeiend bedrijf"),
        "Multi-dept / regulated": _t("Multi-services / réglementé", "Mehrere Abteilungen / reguliert", "Multidepartamental / regulado", "Multi-reparto / regolamentato", "Meerdere afdelingen / gereguleerd"),
        "/ month": _t("/ mois", "/ Monat", "/ mes", "/ mese", "/ maand"),
        "Most popular": _t("Le plus populaire", "Am beliebtesten", "Más popular", "Il più popolare", "Meest populair"),
        "Start free trial": _t("Démarrer l'essai gratuit", "Kostenlos testen", "Iniciar prueba gratuita", "Inizia la prova gratuita", "Start gratis proefperiode"),
        "Up to 10 users · 3 departments": _t(
            "Jusqu'à 10 utilisateurs · 3 services", "Bis zu 10 Nutzer · 3 Abteilungen", "Hasta 10 usuarios · 3 departamentos",
            "Fino a 10 utenti · 3 reparti", "Tot 10 gebruikers · 3 afdelingen"),
        "Strategy: OKRs, KPIs, projects": _t(
            "Stratégie : OKR, KPI, projets", "Strategie: OKRs, KPIs, Projekte", "Estrategia: OKR, KPI, proyectos",
            "Strategia: OKR, KPI, progetti", "Strategie: OKR's, KPI's, projecten"),
        "Finance: P&amp;L, BS, cash flow, budget": _t(
            "Finance : compte de résultat, bilan, trésorerie, budget",
            "Finanzen: GuV, Bilanz, Cashflow, Budget",
            "Finanzas: cuenta de resultados, balance, flujo de caja, presupuesto",
            "Finanza: conto economico, stato patrimoniale, flusso di cassa, budget",
            "Financiën: winst-en-verliesrekening, balans, kasstroom, budget"),
        "Compliance · email support": _t(
            "Conformité · assistance par e-mail", "Compliance · E-Mail-Support", "Cumplimiento · soporte por correo",
            "Conformità · supporto via email", "Compliance · e-mailondersteuning"),
        "Up to 50 users · unlimited departments": _t(
            "Jusqu'à 50 utilisateurs · services illimités", "Bis zu 50 Nutzer · unbegrenzte Abteilungen",
            "Hasta 50 usuarios · departamentos ilimitados", "Fino a 50 utenti · reparti illimitati",
            "Tot 50 gebruikers · onbeperkt aantal afdelingen"),
        "Everything in Pilot + risk": _t(
            "Tout ce que contient Pilot + risque", "Alles aus Pilot + Risiko", "Todo lo de Pilot + riesgo",
            "Tutto ciò che c'è in Pilot + rischio", "Alles uit Pilot + risico"),
        "AI assistant, auto-summary &amp; anomalies": _t(
            "Assistant IA, résumé automatique &amp; anomalies",
            "KI-Assistent, Auto-Zusammenfassung &amp; Anomalien",
            "Asistente de IA, resumen automático &amp; anomalías",
            "Assistente IA, riepilogo automatico &amp; anomalie",
            "AI-assistent, automatische samenvatting &amp; afwijkingen"),
        "1 ERP connection · innovation pipeline": _t(
            "1 connexion ERP · pipeline d'innovation", "1 ERP-Verbindung · Innovationspipeline", "1 conexión ERP · pipeline de innovación",
            "1 connessione ERP · pipeline di innovazione", "1 ERP-verbinding · innovatiepijplijn"),
        "Unlimited users &amp; departments": _t(
            "Utilisateurs &amp; services illimités", "Unbegrenzte Nutzer &amp; Abteilungen", "Usuarios &amp; departamentos ilimitados",
            "Utenti &amp; reparti illimitati", "Onbeperkt aantal gebruikers &amp; afdelingen"),
        "Unlimited + scheduled ERP pull": _t(
            "Illimité + extraction ERP planifiée", "Unbegrenzt + geplanter ERP-Abruf", "Ilimitado + extracción ERP programada",
            "Illimitato + estrazione ERP pianificata", "Onbeperkt + geplande ERP-ophaling"),
        "Custom domain + your TLS": _t(
            "Domaine personnalisé + votre TLS", "Individuelle Domain + Ihr TLS", "Dominio personalizado + su TLS",
            "Dominio personalizzato + il tuo TLS", "Aangepast domein + uw TLS"),
        "SLA + onboarding · log export": _t(
            "SLA + intégration · export des journaux", "SLA + Onboarding · Protokollexport", "SLA + incorporación · exportación de registros",
            "SLA + onboarding · esportazione dei log", "SLA + onboarding · logexport"),
        "Flat monthly price per organization (suggested). Annual billing saves 20%. Every plan includes a 14-day free trial.": _t(
            "Prix mensuel forfaitaire par organisation (suggéré). La facturation annuelle fait économiser 20 %. Chaque forfait inclut un essai gratuit de 14 jours.",
            "Pauschaler Monatspreis pro Organisation (empfohlen). Die jährliche Abrechnung spart 20 %. Jeder Tarif enthält eine 14-tägige kostenlose Testphase.",
            "Precio mensual fijo por organización (sugerido). La facturación anual ahorra un 20 %. Cada plan incluye una prueba gratuita de 14 días.",
            "Prezzo mensile forfettario per organizzazione (suggerito). La fatturazione annuale fa risparmiare il 20%. Ogni piano include una prova gratuita di 14 giorni.",
            "Vaste maandprijs per organisatie (voorgesteld). Jaarlijkse facturering bespaart 20%. Elk abonnement bevat een gratis proefperiode van 14 dagen."),
        " sales": _t(" commercial", " Vertrieb", " ventas", " vendite", " verkoop"),
        # ---- Modules table ----
        "What's included": _t("Ce qui est inclus", "Was enthalten ist", "Qué incluye", "Cosa è incluso", "Wat is inbegrepen"),
        "Modules by plan": _t("Modules par forfait", "Module nach Tarif", "Módulos por plan", "Moduli per piano", "Modules per abonnement"),
        "Every Command Center module, and where it unlocks across the plans.": _t(
            "Chaque module de Command Center, et où il se débloque à travers les forfaits.",
            "Jedes Command Center-Modul und wo es über die Tarife hinweg freigeschaltet wird.",
            "Cada módulo de Command Center y dónde se desbloquea en los planes.",
            "Ogni modulo di Command Center e dove si sblocca nei piani.",
            "Elke Command Center-module en waar deze binnen de abonnementen wordt ontgrendeld."),
        "<th scope=\"col\">Module</th>": _t(
            "<th scope=\"col\">Module</th>", "<th scope=\"col\">Modul</th>", "<th scope=\"col\">Módulo</th>",
            "<th scope=\"col\">Modulo</th>", "<th scope=\"col\">Module</th>"),
        "<th scope=\"row\">Users</th>": _t(
            "<th scope=\"row\">Utilisateurs</th>", "<th scope=\"row\">Nutzer</th>", "<th scope=\"row\">Usuarios</th>",
            "<th scope=\"row\">Utenti</th>", "<th scope=\"row\">Gebruikers</th>"),
        "<th scope=\"row\">Departments</th>": _t(
            "<th scope=\"row\">Services</th>", "<th scope=\"row\">Abteilungen</th>", "<th scope=\"row\">Departamentos</th>",
            "<th scope=\"row\">Reparti</th>", "<th scope=\"row\">Afdelingen</th>"),
        "<th scope=\"row\">Strategy (OKRs, KPIs, Projects)</th>": _t(
            "<th scope=\"row\">Stratégie (OKR, KPI, projets)</th>", "<th scope=\"row\">Strategie (OKRs, KPIs, Projekte)</th>",
            "<th scope=\"row\">Estrategia (OKR, KPI, proyectos)</th>", "<th scope=\"row\">Strategia (OKR, KPI, progetti)</th>",
            "<th scope=\"row\">Strategie (OKR's, KPI's, projecten)</th>"),
        "<th scope=\"row\">Finance (P&amp;L, BS, CF, Budget)</th>": _t(
            "<th scope=\"row\">Finance (résultat, bilan, trésorerie, budget)</th>",
            "<th scope=\"row\">Finanzen (GuV, Bilanz, CF, Budget)</th>",
            "<th scope=\"row\">Finanzas (resultados, balance, CF, presupuesto)</th>",
            "<th scope=\"row\">Finanza (CE, SP, CF, budget)</th>",
            "<th scope=\"row\">Financiën (W&amp;V, balans, CF, budget)</th>"),
        "<th scope=\"row\">Governance (Compliance + Risk)</th>": _t(
            "<th scope=\"row\">Gouvernance (conformité + risque)</th>", "<th scope=\"row\">Governance (Compliance + Risiko)</th>",
            "<th scope=\"row\">Gobernanza (cumplimiento + riesgo)</th>", "<th scope=\"row\">Governance (conformità + rischio)</th>",
            "<th scope=\"row\">Governance (compliance + risico)</th>"),
        "<th scope=\"row\">Innovation pipeline</th>": _t(
            "<th scope=\"row\">Pipeline d'innovation</th>", "<th scope=\"row\">Innovationspipeline</th>", "<th scope=\"row\">Pipeline de innovación</th>",
            "<th scope=\"row\">Pipeline di innovazione</th>", "<th scope=\"row\">Innovatiepijplijn</th>"),
        "<th scope=\"row\">AI assistant + auto-summary + anomalies</th>": _t(
            "<th scope=\"row\">Assistant IA + résumé auto + anomalies</th>",
            "<th scope=\"row\">KI-Assistent + Auto-Zusammenfassung + Anomalien</th>",
            "<th scope=\"row\">Asistente de IA + resumen automático + anomalías</th>",
            "<th scope=\"row\">Assistente IA + riepilogo automatico + anomalie</th>",
            "<th scope=\"row\">AI-assistent + automatische samenvatting + afwijkingen</th>"),
        "<th scope=\"row\">ERP integrations (SAP · QBO · Odoo · Oracle)</th>": _t(
            "<th scope=\"row\">Intégrations ERP (SAP · QBO · Odoo · Oracle)</th>",
            "<th scope=\"row\">ERP-Integrationen (SAP · QBO · Odoo · Oracle)</th>",
            "<th scope=\"row\">Integraciones ERP (SAP · QBO · Odoo · Oracle)</th>",
            "<th scope=\"row\">Integrazioni ERP (SAP · QBO · Odoo · Oracle)</th>",
            "<th scope=\"row\">ERP-integraties (SAP · QBO · Odoo · Oracle)</th>"),
        "<th scope=\"row\">Contracts, Loans &amp; Rents</th>": _t(
            "<th scope=\"row\">Contrats, prêts &amp; loyers</th>", "<th scope=\"row\">Verträge, Darlehen &amp; Mieten</th>",
            "<th scope=\"row\">Contratos, préstamos &amp; alquileres</th>", "<th scope=\"row\">Contratti, prestiti &amp; affitti</th>",
            "<th scope=\"row\">Contracten, leningen &amp; huren</th>"),
        "<th scope=\"row\">Announcements / broadcast</th>": _t(
            "<th scope=\"row\">Annonces / diffusion</th>", "<th scope=\"row\">Ankündigungen / Broadcast</th>", "<th scope=\"row\">Anuncios / difusión</th>",
            "<th scope=\"row\">Annunci / broadcast</th>", "<th scope=\"row\">Aankondigingen / uitzending</th>"),
        "<th scope=\"row\">Branded domain</th>": _t(
            "<th scope=\"row\">Domaine de marque</th>", "<th scope=\"row\">Marken-Domain</th>", "<th scope=\"row\">Dominio de marca</th>",
            "<th scope=\"row\">Dominio con brand</th>", "<th scope=\"row\">Merkdomein</th>"),
        "<th scope=\"row\">Activity log retention</th>": _t(
            "<th scope=\"row\">Conservation du journal d'activité</th>", "<th scope=\"row\">Aufbewahrung des Aktivitätsprotokolls</th>",
            "<th scope=\"row\">Retención del registro de actividad</th>", "<th scope=\"row\">Conservazione del registro attività</th>",
            "<th scope=\"row\">Bewaartermijn activiteitenlogboek</th>"),
        "<th scope=\"row\">Support</th>": _t(
            "<th scope=\"row\">Assistance</th>", "<th scope=\"row\">Support</th>", "<th scope=\"row\">Soporte</th>",
            "<th scope=\"row\">Supporto</th>", "<th scope=\"row\">Ondersteuning</th>"),
        "<th scope=\"row\">Deployment</th>": _t(
            "<th scope=\"row\">Déploiement</th>", "<th scope=\"row\">Bereitstellung</th>", "<th scope=\"row\">Despliegue</th>",
            "<th scope=\"row\">Distribuzione</th>", "<th scope=\"row\">Implementatie</th>"),
        "Dedicated / on-premise": _t(
            "Dédié / sur site", "Dediziert / on-premise", "Dedicado / on-premise",
            "Dedicato / on-premise", "Dedicated / on-premise"),
        # ---- table cell values ----
        "up to 10": _t("jusqu'à 10", "bis zu 10", "hasta 10", "fino a 10", "tot 10"),
        "up to 50": _t("jusqu'à 50", "bis zu 50", "hasta 50", "fino a 50", "tot 50"),
        "Unlimited + scheduled pull": _t(
            "Illimité + extraction planifiée", "Unbegrenzt + geplanter Abruf", "Ilimitado + extracción programada",
            "Illimitato + estrazione pianificata", "Onbeperkt + geplande ophaling"),
        "Unlimited + export": _t(
            "Illimité + export", "Unbegrenzt + Export", "Ilimitado + exportación", "Illimitato + esportazione", "Onbeperkt + export"),
        "Unlimited": _t("Illimité", "Unbegrenzt", "Ilimitado", "Illimitato", "Onbeperkt"),
        "Compliance only": _t("Conformité uniquement", "Nur Compliance", "Solo cumplimiento", "Solo conformità", "Alleen compliance"),
        "Both": _t("Les deux", "Beide", "Ambos", "Entrambi", "Beide"),
        "1 connection": _t("1 connexion", "1 Verbindung", "1 conexión", "1 connessione", "1 verbinding"),
        "Notify only": _t("Notification uniquement", "Nur benachrichtigen", "Solo notificar", "Solo notifica", "Alleen melden"),
        "+ Require-ack": _t("+ Accusé requis", "+ Bestätigung erforderlich", "+ Requiere confirmación", "+ Conferma richiesta", "+ Bevestiging vereist"),
        "Shared apex": _t("Domaine racine partagé", "Gemeinsame Apex-Domain", "Ápex compartido", "Apex condiviso", "Gedeeld apex-domein"),
        "Subdomain": _t("Sous-domaine", "Subdomain", "Subdominio", "Sottodominio", "Subdomein"),
        "Custom + TLS": _t("Personnalisé + TLS", "Individuell + TLS", "Personalizado + TLS", "Personalizzato + TLS", "Aangepast + TLS"),
        "30 days": _t("30 jours", "30 Tage", "30 días", "30 giorni", "30 dagen"),
        "1 year": _t("1 an", "1 Jahr", "1 año", "1 anno", "1 jaar"),
        "SLA + onboarding": _t("SLA + intégration", "SLA + Onboarding", "SLA + incorporación", "SLA + onboarding", "SLA + onboarding"),
        "Email": _t("E-mail", "E-Mail", "Correo", "Email", "E-mail"),
        "Priority": _t("Prioritaire", "Priorität", "Prioridad", "Prioritario", "Prioriteit"),
        # ---- FAQ ----
        "Command Center pricing, answered": _t(
            "Tarifs de Command Center, expliqués", "Command Center Preise, erklärt", "Precios de Command Center, explicados",
            "Prezzi di Command Center, spiegati", "Command Center-prijzen, uitgelegd"),
        "Can I change plans later?": _t(
            "Puis-je changer de forfait plus tard ?", "Kann ich den Tarif später wechseln?", "¿Puedo cambiar de plan más tarde?",
            "Posso cambiare piano in seguito?", "Kan ik later van abonnement wisselen?"),
        "Yes — move up or down between the plans at any time. Changes take effect on your next billing cycle.": _t(
            "Oui — passez à un niveau supérieur ou inférieur entre les forfaits à tout moment. Les changements prennent effet au cycle de facturation suivant.",
            "Ja — wechseln Sie jederzeit zwischen den Tarifen nach oben oder unten. Änderungen werden zum nächsten Abrechnungszyklus wirksam.",
            "Sí — suba o baje entre los planes en cualquier momento. Los cambios se aplican en su próximo ciclo de facturación.",
            "Sì — passa a un livello superiore o inferiore tra i piani in qualsiasi momento. Le modifiche hanno effetto dal ciclo di fatturazione successivo.",
            "Ja — schakel op elk moment omhoog of omlaag tussen de abonnementen. Wijzigingen gaan in bij uw volgende factureringscyclus."),
        "How are users counted?": _t(
            "Comment les utilisateurs sont-ils comptés ?", "Wie werden Nutzer gezählt?", "¿Cómo se cuentan los usuarios?",
            "Come vengono conteggiati gli utenti?", "Hoe worden gebruikers geteld?"),
        "A user is anyone with a login to Command Center. You're billed per active user, per month.": _t(
            "Un utilisateur est toute personne disposant d'un identifiant Command Center. Vous êtes facturé par utilisateur actif, par mois.",
            "Ein Nutzer ist jede Person mit einem Login für Command Center. Die Abrechnung erfolgt pro aktivem Nutzer und Monat.",
            "Un usuario es cualquier persona con acceso a Command Center. Se factura por usuario activo, al mes.",
            "Un utente è chiunque abbia un accesso a Command Center. La fatturazione è per utente attivo, al mese.",
            "Een gebruiker is iedereen met een login voor Command Center. U wordt gefactureerd per actieve gebruiker, per maand."),
        "Do I need other FulcrumGrid apps?": _t(
            "Ai-je besoin d'autres applications FulcrumGrid ?", "Brauche ich andere FulcrumGrid-Apps?", "¿Necesito otras apps de FulcrumGrid?",
            "Ho bisogno di altre app FulcrumGrid?", "Heb ik andere FulcrumGrid-apps nodig?"),
        "Is there a free trial?": _t(
            "Y a-t-il un essai gratuit ?", "Gibt es eine kostenlose Testphase?", "¿Hay una prueba gratuita?",
            "È disponibile una prova gratuita?", "Is er een gratis proefperiode?"),
        "No. Command Center works on its own. If you run several apps, the <a href=\"/pricing/\">whole-grid bundle</a> is cheaper than subscribing to each.": _t(
            "Non. Command Center fonctionne de manière autonome. Si vous utilisez plusieurs applications, le <a href=\"/pricing/\">forfait grille complète</a> revient moins cher que de vous abonner à chacune.",
            "Nein. Command Center funktioniert eigenständig. Wenn Sie mehrere Apps nutzen, ist das <a href=\"/pricing/\">Ganzes-Grid-Bundle</a> günstiger, als jede einzeln zu abonnieren.",
            "No. Command Center funciona por sí solo. Si usa varias apps, el <a href=\"/pricing/\">paquete de cuadrícula completa</a> es más barato que suscribirse a cada una.",
            "No. Command Center funziona da solo. Se usi più app, il <a href=\"/pricing/\">pacchetto griglia completa</a> costa meno che abbonarsi a ciascuna.",
            "Nee. Command Center werkt op zichzelf. Als u meerdere apps gebruikt, is de <a href=\"/pricing/\">hele-grid-bundel</a> goedkoper dan u op elke app apart te abonneren."),
        "Every plan includes a 14-day free trial with full features. No credit card required to start.": _t(
            "Chaque forfait inclut un essai gratuit de 14 jours avec toutes les fonctionnalités. Aucune carte bancaire requise pour commencer.",
            "Jeder Tarif enthält eine 14-tägige kostenlose Testphase mit vollem Funktionsumfang. Keine Kreditkarte erforderlich, um zu starten.",
            "Cada plan incluye una prueba gratuita de 14 días con todas las funciones. No se necesita tarjeta de crédito para empezar.",
            "Ogni piano include una prova gratuita di 14 giorni con tutte le funzionalità. Nessuna carta di credito richiesta per iniziare.",
            "Elk abonnement bevat een gratis proefperiode van 14 dagen met alle functies. Geen creditcard nodig om te beginnen."),
        # ---- CTA ----
        "See Command Center on your data": _t(
            "Voyez Command Center sur vos données", "Sehen Sie Command Center mit Ihren Daten", "Vea Command Center con sus datos",
            "Vedi Command Center sui tuoi dati", "Zie Command Center op uw data"),
        "Tell us how your team runs today and we'll show you the right plan in action.": _t(
            "Dites-nous comment votre équipe travaille aujourd'hui et nous vous montrerons le bon forfait en action.",
            "Sagen Sie uns, wie Ihr Team heute arbeitet, und wir zeigen Ihnen den richtigen Tarif in Aktion.",
            "Cuéntenos cómo trabaja su equipo hoy y le mostraremos el plan adecuado en acción.",
            "Dicci come lavora oggi il tuo team e ti mostreremo il piano giusto in azione.",
            "Vertel ons hoe uw team vandaag werkt en we tonen u het juiste abonnement in actie."),
    },
}

# ---------------------------------------------------------------------------
# /pricing/collection/
# ---------------------------------------------------------------------------
PAGE['/pricing/collection/'] = {
    'src': 'pricing/collection/index.html',
    't': {
        # ---- Meta ----
        "Collection pricing &amp; plans | FulcrumGrid": _t(
            "Tarifs &amp; forfaits Collection | FulcrumGrid",
            "Collection Preise &amp; Tarife | FulcrumGrid",
            "Precios &amp; planes de Collection | FulcrumGrid",
            "Prezzi &amp; piani di Collection | FulcrumGrid",
            "Collection-prijzen &amp; abonnementen | FulcrumGrid"),
        "Collection pricing plans — Starter, Professional, Business, and Enterprise / Agency — with a module-by-module breakdown of what's included at each tier.": _t(
            "Forfaits de Collection — Starter, Professional, Business et Enterprise / Agency — avec un détail module par module de ce qui est inclus à chaque niveau.",
            "Collection Preistarife — Starter, Professional, Business und Enterprise / Agency — mit einer modulweisen Aufschlüsselung dessen, was in jeder Stufe enthalten ist.",
            "Planes de precios de Collection — Starter, Professional, Business y Enterprise / Agency — con un desglose módulo a módulo de lo que se incluye en cada nivel.",
            "Piani tariffari di Collection — Starter, Professional, Business ed Enterprise / Agency — con un dettaglio modulo per modulo di ciò che è incluso in ogni livello.",
            "Prijsabonnementen van Collection — Starter, Professional, Business en Enterprise / Agency — met een module-voor-module-overzicht van wat op elk niveau is inbegrepen."),
        "Collection pricing — plans and modules | FulcrumGrid": _t(
            "Tarifs de Collection — forfaits et modules | FulcrumGrid",
            "Collection Preise — Tarife und Module | FulcrumGrid",
            "Precios de Collection — planes y módulos | FulcrumGrid",
            "Prezzi di Collection — piani e moduli | FulcrumGrid",
            "Collection-prijzen — abonnementen en modules | FulcrumGrid"),
        # ---- Breadcrumb (JSON-LD only) / hero ----
        "Home": _t("Accueil", "Startseite", "Inicio", "Home", "Home"),
        "Collection <em>pricing.</em>": _t(
            "Collection <em>tarifs.</em>",
            "Collection <em>Preise.</em>",
            "Collection <em>precios.</em>",
            "Collection <em>prezzi.</em>",
            "Collection <em>prijzen.</em>"),
        # ---- Section eyebrow + heading ----
        "01 · Plans": _t("01 · Forfaits", "01 · Tarife", "01 · Planes", "01 · Piani", "01 · Abonnementen"),
        "Priced per plan.": _t(
            "Un prix par forfait.", "Preise pro Tarif.", "Un precio por plan.",
            "Un prezzo per piano.", "Een prijs per abonnement."),
        # ---- Plan cards: tier proper-names stay English; price labels translated ----
        "Starter": _t("Starter", "Starter", "Starter", "Starter", "Starter"),
        "Professional": _t("Professional", "Professional", "Professional", "Professional", "Professional"),
        "Business": _t("Business", "Business", "Business", "Business", "Business"),
        "Enterprise / Agency": _t("Enterprise / Agency", "Enterprise / Agency", "Enterprise / Agency", "Enterprise / Agency", "Enterprise / Agency"),
        "<span class=\"amt\">Free</span>": _t(
            "<span class=\"amt\">Gratuit</span>", "<span class=\"amt\">Kostenlos</span>", "<span class=\"amt\">Gratis</span>",
            "<span class=\"amt\">Gratis</span>", "<span class=\"amt\">Gratis</span>"),
        "<span class=\"amt\">Custom</span>": _t(
            "<span class=\"amt\">Sur mesure</span>", "<span class=\"amt\">Individuell</span>", "<span class=\"amt\">Personalizado</span>",
            "<span class=\"amt\">Personalizzato</span>", "<span class=\"amt\">Op maat</span>"),
        "Receivables and collections, priced by plan — from a small in-house AR team to a multi-client agency. Every plan runs on the same secure grid.": _t(
            "Créances et recouvrement, tarifés par forfait — d'une petite équipe de recouvrement interne à une agence multi-clients. Chaque forfait s'exécute sur la même grille sécurisée.",
            "Forderungen und Inkasso, nach Tarif bepreist — vom kleinen internen Forderungsteam bis zur Agentur mit mehreren Mandanten. Jeder Tarif läuft auf demselben sicheren Grid.",
            "Cobros y recobros, con precio por plan — desde un pequeño equipo interno de cuentas por cobrar hasta una agencia multicliente. Cada plan se ejecuta en la misma cuadrícula segura.",
            "Crediti e recupero crediti, con prezzo per piano — da un piccolo team interno di crediti a un'agenzia multi-cliente. Ogni piano gira sulla stessa griglia sicura.",
            "Vorderingen en incasso, geprijsd per abonnement — van een klein intern debiteurenteam tot een multiclient-bureau. Elk abonnement draait op hetzelfde beveiligde grid."),
        # ---- Cards ----
        "Small in-house AR teams": _t("Petites équipes de recouvrement internes", "Kleine interne Forderungsteams", "Equipos internos pequeños de cuentas por cobrar", "Piccoli team crediti interni", "Kleine interne debiteurenteams"),
        "Debtors, accounts, invoices &amp; payments": _t(
            "Débiteurs, comptes, factures &amp; paiements", "Schuldner, Konten, Rechnungen &amp; Zahlungen", "Deudores, cuentas, facturas &amp; pagos",
            "Debitori, conti, fatture &amp; pagamenti", "Debiteuren, rekeningen, facturen &amp; betalingen"),
        "Workspace · tasks · promises · disputes": _t(
            "Espace de travail · tâches · promesses · litiges", "Workspace · Aufgaben · Zahlungszusagen · Streitfälle", "Espacio de trabajo · tareas · promesas · disputas",
            "Spazio di lavoro · attività · promesse · contestazioni", "Werkruimte · taken · toezeggingen · geschillen"),
        "Dashboard · audit trail · MFA": _t(
            "Tableau de bord · piste d'audit · MFA", "Dashboard · Audit-Trail · MFA", "Panel · registro de auditoría · MFA",
            "Dashboard · audit trail · MFA", "Dashboard · audittrail · MFA"),
        "3 seats · email support": _t(
            "3 sièges · assistance par e-mail", "3 Plätze · E-Mail-Support", "3 asientos · soporte por correo",
            "3 postazioni · supporto via email", "3 zitplaatsen · e-mailondersteuning"),
        "Growing collection teams": _t("Équipes de recouvrement en croissance", "Wachsende Inkasso-Teams", "Equipos de cobros en crecimiento", "Team di recupero crediti in crescita", "Groeiende incassoteams"),
        "/ month": _t("/ mois", "/ Monat", "/ mes", "/ mese", "/ maand"),
        "Most popular": _t("Le plus populaire", "Am beliebtesten", "Más popular", "Il più popolare", "Meest populair"),
        "Start free trial": _t("Démarrer l'essai gratuit", "Kostenlos testen", "Iniciar prueba gratuita", "Inizia la prova gratuita", "Start gratis proefperiode"),
        "Everything in Starter": _t("Tout ce que contient Starter", "Alles aus Starter", "Todo lo de Starter", "Tutto ciò che c'è in Starter", "Alles uit Starter"),
        "Strategies &amp; templates automation": _t(
            "Automatisation des stratégies &amp; modèles", "Automatisierung von Strategien &amp; Vorlagen", "Automatización de estrategias &amp; plantillas",
            "Automazione di strategie &amp; modelli", "Automatisering van strategieën &amp; sjablonen"),
        "Custom roles (RBAC), approvals / SoD, import": _t(
            "Rôles personnalisés (RBAC), approbations / SoD, import", "Individuelle Rollen (RBAC), Genehmigungen / SoD, Import", "Roles personalizados (RBAC), aprobaciones / SoD, importación",
            "Ruoli personalizzati (RBAC), approvazioni / SoD, importazione", "Aangepaste rollen (RBAC), goedkeuringen / SoD, import"),
        "Advanced analytics · 15 seats · priority": _t(
            "Analytique avancée · 15 sièges · prioritaire", "Erweiterte Analysen · 15 Plätze · vorrangig", "Analítica avanzada · 15 asientos · prioridad",
            "Analisi avanzate · 15 postazioni · prioritario", "Geavanceerde analyses · 15 zitplaatsen · prioriteit"),
        "Large ops / compliance-heavy": _t("Grandes opérations / forte conformité", "Großer Betrieb / compliance-intensiv", "Grandes operaciones / mucho cumplimiento", "Grandi operazioni / molta conformità", "Grote operaties / compliance-intensief"),
        "Everything in Professional": _t("Tout ce que contient Professional", "Alles aus Professional", "Todo lo de Professional", "Tutto ciò che c'è in Professional", "Alles uit Professional"),
        "Legal &amp; tiered settlements": _t(
            "Contentieux &amp; règlements échelonnés", "Rechtliches &amp; gestaffelte Vergleiche", "Legal &amp; acuerdos escalonados",
            "Legale &amp; transazioni a livelli", "Juridisch &amp; getrapte schikkingen"),
        "Integrations: API, REST v1, webhooks, sandbox": _t(
            "Intégrations : API, REST v1, webhooks, sandbox", "Integrationen: API, REST v1, Webhooks, Sandbox", "Integraciones: API, REST v1, webhooks, sandbox",
            "Integrazioni: API, REST v1, webhook, sandbox", "Integraties: API, REST v1, webhooks, sandbox"),
        "Custom domain · unlimited seats · SLA": _t(
            "Domaine personnalisé · sièges illimités · SLA", "Individuelle Domain · unbegrenzte Plätze · SLA", "Dominio personalizado · asientos ilimitados · SLA",
            "Dominio personalizzato · postazioni illimitate · SLA", "Aangepast domein · onbeperkt aantal zitplaatsen · SLA"),
        "Collection agencies &amp; multi-client": _t(
            "Agences de recouvrement &amp; multi-clients", "Inkassobüros &amp; mehrere Mandanten", "Agencias de cobros &amp; multicliente",
            "Agenzie di recupero crediti &amp; multi-cliente", "Incassobureaus &amp; multiclient"),
        "Everything in Business": _t("Tout ce que contient Business", "Alles aus Business", "Todo lo de Business", "Tutto ciò che c'è in Business", "Alles uit Business"),
        "Agency mode: creditors + trust accounting": _t(
            "Mode agence : créanciers + comptabilité fiduciaire", "Agentur-Modus: Gläubiger + Treuhandbuchhaltung", "Modo agencia: acreedores + contabilidad fiduciaria",
            "Modalità agenzia: creditori + contabilità fiduciaria", "Bureaumodus: crediteuren + derdengeldenadministratie"),
        "Creditor portal · per-tenant subdomains": _t(
            "Portail créancier · sous-domaines par locataire", "Gläubigerportal · Subdomains pro Mandant", "Portal de acreedores · subdominios por inquilino",
            "Portale creditori · sottodomini per tenant", "Crediteurenportaal · subdomeinen per tenant"),
        "Unlimited seats · dedicated support": _t(
            "Sièges illimités · assistance dédiée", "Unbegrenzte Plätze · dedizierter Support", "Asientos ilimitados · soporte dedicado",
            "Postazioni illimitate · supporto dedicato", "Onbeperkt aantal zitplaatsen · toegewijde ondersteuning"),
        "Flat monthly price per workspace (suggested). Seats included as shown; Enterprise / Agency is custom-quoted.": _t(
            "Prix mensuel forfaitaire par espace de travail (suggéré). Sièges inclus comme indiqué ; Enterprise / Agency fait l'objet d'un devis personnalisé.",
            "Pauschaler Monatspreis pro Workspace (empfohlen). Plätze wie angegeben enthalten; Enterprise / Agency wird individuell angeboten.",
            "Precio mensual fijo por espacio de trabajo (sugerido). Asientos incluidos como se indica; Enterprise / Agency se cotiza a medida.",
            "Prezzo mensile forfettario per spazio di lavoro (suggerito). Postazioni incluse come indicato; Enterprise / Agency è quotato su misura.",
            "Vaste maandprijs per werkruimte (voorgesteld). Zitplaatsen inbegrepen zoals getoond; Enterprise / Agency wordt op maat geoffreerd."),
        " sales": _t(" commercial", " Vertrieb", " ventas", " vendite", " verkoop"),
        # ---- Modules table ----
        "What's included": _t("Ce qui est inclus", "Was enthalten ist", "Qué incluye", "Cosa è incluso", "Wat is inbegrepen"),
        "Modules by plan": _t("Modules par forfait", "Module nach Tarif", "Módulos por plan", "Moduli per piano", "Modules per abonnement"),
        "Every Collection module, and where it unlocks across the plans.": _t(
            "Chaque module de Collection, et où il se débloque à travers les forfaits.",
            "Jedes Collection-Modul und wo es über die Tarife hinweg freigeschaltet wird.",
            "Cada módulo de Collection y dónde se desbloquea en los planes.",
            "Ogni modulo di Collection e dove si sblocca nei piani.",
            "Elke Collection-module en waar deze binnen de abonnementen wordt ontgrendeld."),
        "<th scope=\"col\">Module</th>": _t(
            "<th scope=\"col\">Module</th>", "<th scope=\"col\">Modul</th>", "<th scope=\"col\">Módulo</th>",
            "<th scope=\"col\">Modulo</th>", "<th scope=\"col\">Module</th>"),
        "<th scope=\"row\">Debtors · Accounts · Invoices · Payments</th>": _t(
            "<th scope=\"row\">Débiteurs · Comptes · Factures · Paiements</th>", "<th scope=\"row\">Schuldner · Konten · Rechnungen · Zahlungen</th>",
            "<th scope=\"row\">Deudores · Cuentas · Facturas · Pagos</th>", "<th scope=\"row\">Debitori · Conti · Fatture · Pagamenti</th>",
            "<th scope=\"row\">Debiteuren · Rekeningen · Facturen · Betalingen</th>"),
        "<th scope=\"row\">Workspace · Tasks · Promises · Disputes</th>": _t(
            "<th scope=\"row\">Espace de travail · Tâches · Promesses · Litiges</th>", "<th scope=\"row\">Workspace · Aufgaben · Zahlungszusagen · Streitfälle</th>",
            "<th scope=\"row\">Espacio de trabajo · Tareas · Promesas · Disputas</th>", "<th scope=\"row\">Spazio di lavoro · Attività · Promesse · Contestazioni</th>",
            "<th scope=\"row\">Werkruimte · Taken · Toezeggingen · Geschillen</th>"),
        "<th scope=\"row\">Email + debtor portal</th>": _t(
            "<th scope=\"row\">E-mail + portail débiteur</th>", "<th scope=\"row\">E-Mail + Schuldnerportal</th>", "<th scope=\"row\">Correo + portal del deudor</th>",
            "<th scope=\"row\">Email + portale debitore</th>", "<th scope=\"row\">E-mail + debiteurenportaal</th>"),
        "<th scope=\"row\">Custom branding</th>": _t(
            "<th scope=\"row\">Personnalisation de marque</th>", "<th scope=\"row\">Individuelles Branding</th>", "<th scope=\"row\">Marca personalizada</th>",
            "<th scope=\"row\">Personalizzazione del brand</th>", "<th scope=\"row\">Aangepaste branding</th>"),
        "<th scope=\"row\">Strategies + Templates (automation)</th>": _t(
            "<th scope=\"row\">Stratégies + Modèles (automatisation)</th>", "<th scope=\"row\">Strategien + Vorlagen (Automatisierung)</th>",
            "<th scope=\"row\">Estrategias + Plantillas (automatización)</th>", "<th scope=\"row\">Strategie + Modelli (automazione)</th>",
            "<th scope=\"row\">Strategieën + Sjablonen (automatisering)</th>"),
        "<th scope=\"row\">Custom Roles (RBAC) · Approvals/SoD · Import</th>": _t(
            "<th scope=\"row\">Rôles personnalisés (RBAC) · Approbations/SoD · Import</th>", "<th scope=\"row\">Individuelle Rollen (RBAC) · Genehmigungen/SoD · Import</th>",
            "<th scope=\"row\">Roles personalizados (RBAC) · Aprobaciones/SoD · Importación</th>", "<th scope=\"row\">Ruoli personalizzati (RBAC) · Approvazioni/SoD · Importazione</th>",
            "<th scope=\"row\">Aangepaste rollen (RBAC) · Goedkeuringen/SoD · Import</th>"),
        "<th scope=\"row\">Advanced analytics (A/B, forecast)</th>": _t(
            "<th scope=\"row\">Analytique avancée (A/B, prévisions)</th>", "<th scope=\"row\">Erweiterte Analysen (A/B, Prognose)</th>",
            "<th scope=\"row\">Analítica avanzada (A/B, previsión)</th>", "<th scope=\"row\">Analisi avanzate (A/B, previsioni)</th>",
            "<th scope=\"row\">Geavanceerde analyses (A/B, prognose)</th>"),
        "<th scope=\"row\">ERP connection (SAP Business One)</th>": _t(
            "<th scope=\"row\">Connexion ERP (SAP Business One)</th>", "<th scope=\"row\">ERP-Verbindung (SAP Business One)</th>",
            "<th scope=\"row\">Conexión ERP (SAP Business One)</th>", "<th scope=\"row\">Connessione ERP (SAP Business One)</th>",
            "<th scope=\"row\">ERP-verbinding (SAP Business One)</th>"),
        "<th scope=\"row\">Legal · Settlements (tiered)</th>": _t(
            "<th scope=\"row\">Contentieux · Règlements (échelonnés)</th>", "<th scope=\"row\">Rechtliches · Vergleiche (gestaffelt)</th>",
            "<th scope=\"row\">Legal · Acuerdos (escalonados)</th>", "<th scope=\"row\">Legale · Transazioni (a livelli)</th>",
            "<th scope=\"row\">Juridisch · Schikkingen (getrapt)</th>"),
        "<th scope=\"row\">Integrations: API keys · REST v1 · webhooks · sandbox</th>": _t(
            "<th scope=\"row\">Intégrations : clés API · REST v1 · webhooks · sandbox</th>", "<th scope=\"row\">Integrationen: API-Schlüssel · REST v1 · Webhooks · Sandbox</th>",
            "<th scope=\"row\">Integraciones: claves API · REST v1 · webhooks · sandbox</th>", "<th scope=\"row\">Integrazioni: chiavi API · REST v1 · webhook · sandbox</th>",
            "<th scope=\"row\">Integraties: API-sleutels · REST v1 · webhooks · sandbox</th>"),
        "<th scope=\"row\">Custom domain</th>": _t(
            "<th scope=\"row\">Domaine personnalisé</th>", "<th scope=\"row\">Individuelle Domain</th>", "<th scope=\"row\">Dominio personalizado</th>",
            "<th scope=\"row\">Dominio personalizzato</th>", "<th scope=\"row\">Aangepast domein</th>"),
        "<th scope=\"row\">Agency mode: Creditors + Trust accounting</th>": _t(
            "<th scope=\"row\">Mode agence : Créanciers + Comptabilité fiduciaire</th>", "<th scope=\"row\">Agentur-Modus: Gläubiger + Treuhandbuchhaltung</th>",
            "<th scope=\"row\">Modo agencia: Acreedores + Contabilidad fiduciaria</th>", "<th scope=\"row\">Modalità agenzia: Creditori + Contabilità fiduciaria</th>",
            "<th scope=\"row\">Bureaumodus: Crediteuren + Derdengeldenadministratie</th>"),
        "<th scope=\"row\">Seats / support</th>": _t(
            "<th scope=\"row\">Sièges / assistance</th>", "<th scope=\"row\">Plätze / Support</th>", "<th scope=\"row\">Asientos / soporte</th>",
            "<th scope=\"row\">Postazioni / supporto</th>", "<th scope=\"row\">Zitplaatsen / ondersteuning</th>"),
        # ---- table cell values ----
        "3 seats · email": _t("3 sièges · e-mail", "3 Plätze · E-Mail", "3 asientos · correo", "3 postazioni · email", "3 zitplaatsen · e-mail"),
        "15 seats · priority": _t("15 sièges · prioritaire", "15 Plätze · vorrangig", "15 asientos · prioridad", "15 postazioni · prioritario", "15 zitplaatsen · prioriteit"),
        "Unlimited · SLA": _t("Illimité · SLA", "Unbegrenzt · SLA", "Ilimitado · SLA", "Illimitato · SLA", "Onbeperkt · SLA"),
        "Unlimited · dedicated": _t("Illimité · dédié", "Unbegrenzt · dediziert", "Ilimitado · dedicado", "Illimitato · dedicato", "Onbeperkt · toegewijd"),
        # ---- FAQ ----
        "Collection pricing, answered": _t(
            "Tarifs de Collection, expliqués", "Collection Preise, erklärt", "Precios de Collection, explicados",
            "Prezzi di Collection, spiegati", "Collection-prijzen, uitgelegd"),
        "Can I change plans later?": _t(
            "Puis-je changer de forfait plus tard ?", "Kann ich den Tarif später wechseln?", "¿Puedo cambiar de plan más tarde?",
            "Posso cambiare piano in seguito?", "Kan ik later van abonnement wisselen?"),
        "Yes — move up or down between the plans at any time. Changes take effect on your next billing cycle.": _t(
            "Oui — passez à un niveau supérieur ou inférieur entre les forfaits à tout moment. Les changements prennent effet au cycle de facturation suivant.",
            "Ja — wechseln Sie jederzeit zwischen den Tarifen nach oben oder unten. Änderungen werden zum nächsten Abrechnungszyklus wirksam.",
            "Sí — suba o baje entre los planes en cualquier momento. Los cambios se aplican en su próximo ciclo de facturación.",
            "Sì — passa a un livello superiore o inferiore tra i piani in qualsiasi momento. Le modifiche hanno effetto dal ciclo di fatturazione successivo.",
            "Ja — schakel op elk moment omhoog of omlaag tussen de abonnementen. Wijzigingen gaan in bij uw volgende factureringscyclus."),
        "How are users counted?": _t(
            "Comment les utilisateurs sont-ils comptés ?", "Wie werden Nutzer gezählt?", "¿Cómo se cuentan los usuarios?",
            "Come vengono conteggiati gli utenti?", "Hoe worden gebruikers geteld?"),
        "A user is anyone with a login to Collection. You're billed per active user, per month.": _t(
            "Un utilisateur est toute personne disposant d'un identifiant Collection. Vous êtes facturé par utilisateur actif, par mois.",
            "Ein Nutzer ist jede Person mit einem Login für Collection. Die Abrechnung erfolgt pro aktivem Nutzer und Monat.",
            "Un usuario es cualquier persona con acceso a Collection. Se factura por usuario activo, al mes.",
            "Un utente è chiunque abbia un accesso a Collection. La fatturazione è per utente attivo, al mese.",
            "Een gebruiker is iedereen met een login voor Collection. U wordt gefactureerd per actieve gebruiker, per maand."),
        "Do I need other FulcrumGrid apps?": _t(
            "Ai-je besoin d'autres applications FulcrumGrid ?", "Brauche ich andere FulcrumGrid-Apps?", "¿Necesito otras apps de FulcrumGrid?",
            "Ho bisogno di altre app FulcrumGrid?", "Heb ik andere FulcrumGrid-apps nodig?"),
        "Is there a free trial?": _t(
            "Y a-t-il un essai gratuit ?", "Gibt es eine kostenlose Testphase?", "¿Hay una prueba gratuita?",
            "È disponibile una prova gratuita?", "Is er een gratis proefperiode?"),
        "No. Collection works on its own. If you run several apps, the <a href=\"/pricing/\">whole-grid bundle</a> is cheaper than subscribing to each.": _t(
            "Non. Collection fonctionne de manière autonome. Si vous utilisez plusieurs applications, le <a href=\"/pricing/\">forfait grille complète</a> revient moins cher que de vous abonner à chacune.",
            "Nein. Collection funktioniert eigenständig. Wenn Sie mehrere Apps nutzen, ist das <a href=\"/pricing/\">Ganzes-Grid-Bundle</a> günstiger, als jede einzeln zu abonnieren.",
            "No. Collection funciona por sí solo. Si usa varias apps, el <a href=\"/pricing/\">paquete de cuadrícula completa</a> es más barato que suscribirse a cada una.",
            "No. Collection funziona da solo. Se usi più app, il <a href=\"/pricing/\">pacchetto griglia completa</a> costa meno che abbonarsi a ciascuna.",
            "Nee. Collection werkt op zichzelf. Als u meerdere apps gebruikt, is de <a href=\"/pricing/\">hele-grid-bundel</a> goedkoper dan u op elke app apart te abonneren."),
        "Every plan includes a 14-day free trial with full features. No credit card required to start.": _t(
            "Chaque forfait inclut un essai gratuit de 14 jours avec toutes les fonctionnalités. Aucune carte bancaire requise pour commencer.",
            "Jeder Tarif enthält eine 14-tägige kostenlose Testphase mit vollem Funktionsumfang. Keine Kreditkarte erforderlich, um zu starten.",
            "Cada plan incluye una prueba gratuita de 14 días con todas las funciones. No se necesita tarjeta de crédito para empezar.",
            "Ogni piano include una prova gratuita di 14 giorni con tutte le funzionalità. Nessuna carta di credito richiesta per iniziare.",
            "Elk abonnement bevat een gratis proefperiode van 14 dagen met alle functies. Geen creditcard nodig om te beginnen."),
        # ---- CTA ----
        "See Collection on your data": _t(
            "Voyez Collection sur vos données", "Sehen Sie Collection mit Ihren Daten", "Vea Collection con sus datos",
            "Vedi Collection sui tuoi dati", "Zie Collection op uw data"),
        "Tell us how your team runs today and we'll show you the right plan in action.": _t(
            "Dites-nous comment votre équipe travaille aujourd'hui et nous vous montrerons le bon forfait en action.",
            "Sagen Sie uns, wie Ihr Team heute arbeitet, und wir zeigen Ihnen den richtigen Tarif in Aktion.",
            "Cuéntenos cómo trabaja su equipo hoy y le mostraremos el plan adecuado en acción.",
            "Dicci come lavora oggi il tuo team e ti mostreremo il piano giusto in azione.",
            "Vertel ons hoe uw team vandaag werkt en we tonen u het juiste abonnement in actie."),
    },
}

# ---------------------------------------------------------------------------
# /pricing/hr-suite/
# ---------------------------------------------------------------------------
PAGE['/pricing/hr-suite/'] = {
    'src': 'pricing/hr-suite/index.html',
    't': {
        # ---- Meta ----
        "HR Suite pricing &amp; plans | FulcrumGrid": _t(
            "Tarifs &amp; forfaits HR Suite | FulcrumGrid",
            "HR Suite Preise &amp; Tarife | FulcrumGrid",
            "Precios &amp; planes de HR Suite | FulcrumGrid",
            "Prezzi &amp; piani di HR Suite | FulcrumGrid",
            "HR Suite-prijzen &amp; abonnementen | FulcrumGrid"),
        "HR Suite pricing — Starter, Growth, and Enterprise — with a module-by-module breakdown, including payroll and compliance.": _t(
            "Tarifs de HR Suite — Starter, Growth et Enterprise — avec un détail module par module, y compris la paie et la conformité.",
            "HR Suite Preise — Starter, Growth und Enterprise — mit einer modulweisen Aufschlüsselung, einschließlich Gehaltsabrechnung und Compliance.",
            "Precios de HR Suite — Starter, Growth y Enterprise — con un desglose módulo a módulo, incluidas nóminas y cumplimiento.",
            "Prezzi di HR Suite — Starter, Growth ed Enterprise — con un dettaglio modulo per modulo, inclusi buste paga e conformità.",
            "HR Suite-prijzen — Starter, Growth en Enterprise — met een module-voor-module-overzicht, inclusief loonadministratie en compliance."),
        "HR Suite pricing — plans and modules | FulcrumGrid": _t(
            "Tarifs de HR Suite — forfaits et modules | FulcrumGrid",
            "HR Suite Preise — Tarife und Module | FulcrumGrid",
            "Precios de HR Suite — planes y módulos | FulcrumGrid",
            "Prezzi di HR Suite — piani e moduli | FulcrumGrid",
            "HR Suite-prijzen — abonnementen en modules | FulcrumGrid"),
        # ---- Breadcrumb (JSON-LD only) / hero ----
        "Home": _t("Accueil", "Startseite", "Inicio", "Home", "Home"),
        "HR Suite <em>pricing.</em>": _t(
            "HR Suite <em>tarifs.</em>",
            "HR Suite <em>Preise.</em>",
            "HR Suite <em>precios.</em>",
            "HR Suite <em>prezzi.</em>",
            "HR Suite <em>prijzen.</em>"),
        # ---- Section eyebrow + heading ----
        "01 · Plans": _t("01 · Forfaits", "01 · Tarife", "01 · Planes", "01 · Piani", "01 · Abonnementen"),
        "Priced per plan.": _t(
            "Un prix par forfait.", "Preise pro Tarif.", "Un precio por plan.",
            "Un prezzo per piano.", "Een prijs per abonnement."),
        # ---- Tier proper-names + product names stay English ----
        "Starter": _t("Starter", "Starter", "Starter", "Starter", "Starter"),
        "Growth": _t("Growth", "Growth", "Growth", "Growth", "Growth"),
        "Enterprise": _t("Enterprise", "Enterprise", "Enterprise", "Enterprise", "Enterprise"),
        "GOSI": _t("GOSI", "GOSI", "GOSI", "GOSI", "GOSI"),
        "SAP Business One": _t("SAP Business One", "SAP Business One", "SAP Business One", "SAP Business One", "SAP Business One"),
        "HR from hire to retire — 35 modules on one grid, with Core HR always on. Priced per seat, packaged into three plans plus à-la-carte add-ons.": _t(
            "Les RH de l'embauche au départ — 35 modules sur une seule grille, avec les RH de base toujours activées. Tarifé par siège, réparti en trois forfaits plus des options à la carte.",
            "HR von der Einstellung bis zum Ruhestand — 35 Module auf einem Grid, mit stets aktivem Kern-HR. Bepreist pro Platz, gebündelt in drei Tarife plus à-la-carte-Add-ons.",
            "RR. HH. de la contratación a la jubilación — 35 módulos en una sola cuadrícula, con RR. HH. básicos siempre activos. Con precio por asiento, agrupados en tres planes más complementos a la carta.",
            "HR dall'assunzione alla pensione — 35 moduli su un'unica griglia, con HR di base sempre attivo. Con prezzo per postazione, raggruppati in tre piani più add-on à la carte.",
            "HR van aanwerving tot pensioen — 35 modules op één grid, met Kern-HR altijd aan. Geprijsd per zitplaats, gebundeld in drie abonnementen plus à-la-carte add-ons."),
        # ---- Cards ----
        "Small teams getting HR in order": _t("Petites équipes qui structurent leurs RH", "Kleine Teams, die ihre HR ordnen", "Equipos pequeños que ordenan sus RR. HH.", "Piccoli team che mettono ordine nell'HR", "Kleine teams die hun HR op orde brengen"),
        "/ seat / mo": _t("/ siège / mois", "/ Platz / Mon.", "/ asiento / mes", "/ postazione / mese", "/ zitplaats / mnd"),
        "Most popular": _t("Le plus populaire", "Am beliebtesten", "Más popular", "Il più popolare", "Meest populair"),
        "All modules": _t("Tous les modules", "Alle Module", "Todos los módulos", "Tutti i moduli", "Alle modules"),
        "Start free trial": _t("Démarrer l'essai gratuit", "Kostenlos testen", "Iniciar prueba gratuita", "Inizia la prova gratuita", "Start gratis proefperiode"),
        "Up to 10 people": _t("Jusqu'à 10 personnes", "Bis zu 10 Personen", "Hasta 10 personas", "Fino a 10 persone", "Tot 10 personen"),
        "Core HR &amp; time off": _t(
            "RH de base &amp; congés", "Kern-HR &amp; Abwesenheiten", "RR. HH. básicos &amp; ausencias",
            "HR di base &amp; ferie", "Kern-HR &amp; verlof"),
        "Expenses &amp; HR letters": _t(
            "Notes de frais &amp; courriers RH", "Spesen &amp; HR-Schreiben", "Gastos &amp; cartas de RR. HH.",
            "Note spese &amp; lettere HR", "Onkosten &amp; HR-brieven"),
        "Announcements, recognition &amp; probation": _t(
            "Annonces, reconnaissance &amp; période d'essai", "Ankündigungen, Anerkennung &amp; Probezeit", "Anuncios, reconocimiento &amp; período de prueba",
            "Annunci, riconoscimenti &amp; periodo di prova", "Aankondigingen, erkenning &amp; proeftijd"),
        "A real HR function, day to day": _t("Une véritable fonction RH, au quotidien", "Eine echte HR-Funktion, Tag für Tag", "Una verdadera función de RR. HH., día a día", "Una vera funzione HR, giorno per giorno", "Een echte HR-functie, dag in dag uit"),
        "Up to 50 people": _t("Jusqu'à 50 personnes", "Bis zu 50 Personen", "Hasta 50 personas", "Fino a 50 persone", "Tot 50 personen"),
        "Attendance, overtime &amp; timesheets": _t(
            "Présence, heures supplémentaires &amp; feuilles de temps", "Anwesenheit, Überstunden &amp; Zeiterfassung", "Asistencia, horas extra &amp; hojas de horas",
            "Presenze, straordinari &amp; fogli ore", "Aanwezigheid, overuren &amp; urenstaten"),
        "Onboarding, documents &amp; performance": _t(
            "Intégration, documents &amp; performance", "Onboarding, Dokumente &amp; Leistung", "Incorporación, documentos &amp; desempeño",
            "Onboarding, documenti &amp; performance", "Onboarding, documenten &amp; prestaties"),
        "Requests, assets, helpdesk &amp; benefits": _t(
            "Demandes, actifs, assistance &amp; avantages", "Anfragen, Assets, Helpdesk &amp; Benefits", "Solicitudes, activos, soporte &amp; beneficios",
            "Richieste, asset, helpdesk &amp; benefit", "Verzoeken, activa, helpdesk &amp; secundaire arbeidsvoorwaarden"),
        "Payroll, compliance & everything at scale": _t(
            "Paie, conformité et tout à grande échelle", "Gehaltsabrechnung, Compliance und alles im großen Maßstab", "Nóminas, cumplimiento y todo a gran escala",
            "Buste paga, conformità e tutto su larga scala", "Loonadministratie, compliance en alles op schaal"),
        "Unlimited people": _t("Personnes illimitées", "Unbegrenzte Personen", "Personas ilimitadas", "Persone illimitate", "Onbeperkt aantal personen"),
        "Payroll &amp; end-of-service": _t(
            "Paie &amp; indemnité de fin de service", "Gehaltsabrechnung &amp; Abfindung", "Nóminas &amp; fin de servicio",
            "Buste paga &amp; fine servizio", "Loonadministratie &amp; einde dienstverband"),
        "Recruitment, learning &amp; analytics": _t(
            "Recrutement, formation &amp; analytique", "Rekrutierung, Lernen &amp; Analysen", "Contratación, formación &amp; analítica",
            "Selezione, formazione &amp; analisi", "Werving, leren &amp; analyses"),
        "SSO / SCIM, AI helper &amp; SAP": _t(
            "SSO / SCIM, assistant IA &amp; SAP", "SSO / SCIM, KI-Helfer &amp; SAP", "SSO / SCIM, asistente de IA &amp; SAP",
            "SSO / SCIM, assistente IA &amp; SAP", "SSO / SCIM, AI-helper &amp; SAP"),
        "Per seat, per month. Core HR is included on every plan. Every plan includes a 14-day free trial; any module not in your plan is available as a per-seat add-on.": _t(
            "Par siège, par mois. Les RH de base sont incluses dans chaque forfait. Chaque forfait inclut un essai gratuit de 14 jours ; tout module absent de votre forfait est disponible en option par siège.",
            "Pro Platz, pro Monat. Kern-HR ist in jedem Tarif enthalten. Jeder Tarif enthält eine 14-tägige kostenlose Testphase; jedes Modul, das nicht in Ihrem Tarif enthalten ist, ist als Add-on pro Platz verfügbar.",
            "Por asiento, al mes. RR. HH. básicos incluidos en todos los planes. Cada plan incluye una prueba gratuita de 14 días; cualquier módulo que no esté en su plan está disponible como complemento por asiento.",
            "Per postazione, al mese. L'HR di base è incluso in ogni piano. Ogni piano include una prova gratuita di 14 giorni; qualsiasi modulo non incluso nel tuo piano è disponibile come add-on per postazione.",
            "Per zitplaats, per maand. Kern-HR is inbegrepen bij elk abonnement. Elk abonnement bevat een gratis proefperiode van 14 dagen; elke module die niet in uw abonnement zit, is beschikbaar als add-on per zitplaats."),
        # ---- Modules table ----
        "What's included": _t("Ce qui est inclus", "Was enthalten ist", "Qué incluye", "Cosa è incluso", "Wat is inbegrepen"),
        "Modules by plan": _t("Modules par forfait", "Module nach Tarif", "Módulos por plan", "Moduli per piano", "Modules per abonnement"),
        "Every HR Suite module, and where it unlocks across the three plans.  ✓ included · ＋ available as a per-seat add-on. Plans are cumulative.": _t(
            "Chaque module de HR Suite, et où il se débloque à travers les trois forfaits.  ✓ inclus · ＋ disponible en option par siège. Les forfaits sont cumulatifs.",
            "Jedes HR Suite-Modul und wo es über die drei Tarife hinweg freigeschaltet wird.  ✓ enthalten · ＋ als Add-on pro Platz verfügbar. Die Tarife sind kumulativ.",
            "Cada módulo de HR Suite y dónde se desbloquea en los tres planes.  ✓ incluido · ＋ disponible como complemento por asiento. Los planes son acumulativos.",
            "Ogni modulo di HR Suite e dove si sblocca nei tre piani.  ✓ incluso · ＋ disponibile come add-on per postazione. I piani sono cumulativi.",
            "Elke HR Suite-module en waar deze binnen de drie abonnementen wordt ontgrendeld.  ✓ inbegrepen · ＋ beschikbaar als add-on per zitplaats. De abonnementen zijn cumulatief."),
        "Available as add-on": _t("Disponible en option", "Als Add-on verfügbar", "Disponible como complemento", "Disponibile come add-on", "Beschikbaar als add-on"),
        "<th scope=\"col\">Module</th>": _t(
            "<th scope=\"col\">Module</th>", "<th scope=\"col\">Modul</th>", "<th scope=\"col\">Módulo</th>",
            "<th scope=\"col\">Modulo</th>", "<th scope=\"col\">Module</th>"),
        # group headers
        "<th colspan=\"4\">Always included</th>": _t(
            "<th colspan=\"4\">Toujours inclus</th>", "<th colspan=\"4\">Immer enthalten</th>", "<th colspan=\"4\">Siempre incluido</th>",
            "<th colspan=\"4\">Sempre incluso</th>", "<th colspan=\"4\">Altijd inbegrepen</th>"),
        "<th colspan=\"4\">People &amp; everyday self-service</th>": _t(
            "<th colspan=\"4\">Personnes &amp; self-service au quotidien</th>", "<th colspan=\"4\">Personen &amp; alltäglicher Self-Service</th>",
            "<th colspan=\"4\">Personas &amp; autoservicio diario</th>", "<th colspan=\"4\">Persone &amp; self-service quotidiano</th>",
            "<th colspan=\"4\">Personen &amp; dagelijkse selfservice</th>"),
        "<th colspan=\"4\">Time, attendance &amp; operations</th>": _t(
            "<th colspan=\"4\">Temps, présence &amp; opérations</th>", "<th colspan=\"4\">Zeit, Anwesenheit &amp; Betrieb</th>",
            "<th colspan=\"4\">Tiempo, asistencia &amp; operaciones</th>", "<th colspan=\"4\">Tempo, presenze &amp; operazioni</th>",
            "<th colspan=\"4\">Tijd, aanwezigheid &amp; operatie</th>"),
        "<th colspan=\"4\">Payroll &amp; compliance</th>": _t(
            "<th colspan=\"4\">Paie &amp; conformité</th>", "<th colspan=\"4\">Gehaltsabrechnung &amp; Compliance</th>",
            "<th colspan=\"4\">Nóminas &amp; cumplimiento</th>", "<th colspan=\"4\">Buste paga &amp; conformità</th>",
            "<th colspan=\"4\">Loonadministratie &amp; compliance</th>"),
        "<th colspan=\"4\">Talent, engagement &amp; integrations</th>": _t(
            "<th colspan=\"4\">Talent, engagement &amp; intégrations</th>", "<th colspan=\"4\">Talent, Engagement &amp; Integrationen</th>",
            "<th colspan=\"4\">Talento, compromiso &amp; integraciones</th>", "<th colspan=\"4\">Talento, coinvolgimento &amp; integrazioni</th>",
            "<th colspan=\"4\">Talent, betrokkenheid &amp; integraties</th>"),
        # row labels
        "<th scope=\"row\">Core HR</th>": _t(
            "<th scope=\"row\">RH de base</th>", "<th scope=\"row\">Kern-HR</th>", "<th scope=\"row\">RR. HH. básicos</th>",
            "<th scope=\"row\">HR di base</th>", "<th scope=\"row\">Kern-HR</th>"),
        "<th scope=\"row\">Time off</th>": _t(
            "<th scope=\"row\">Congés</th>", "<th scope=\"row\">Abwesenheiten</th>", "<th scope=\"row\">Ausencias</th>",
            "<th scope=\"row\">Ferie</th>", "<th scope=\"row\">Verlof</th>"),
        "<th scope=\"row\">HR requests</th>": _t(
            "<th scope=\"row\">Demandes RH</th>", "<th scope=\"row\">HR-Anfragen</th>", "<th scope=\"row\">Solicitudes de RR. HH.</th>",
            "<th scope=\"row\">Richieste HR</th>", "<th scope=\"row\">HR-verzoeken</th>"),
        "<th scope=\"row\">Expenses</th>": _t(
            "<th scope=\"row\">Notes de frais</th>", "<th scope=\"row\">Spesen</th>", "<th scope=\"row\">Gastos</th>",
            "<th scope=\"row\">Note spese</th>", "<th scope=\"row\">Onkosten</th>"),
        "<th scope=\"row\">Documents &amp; e-sign</th>": _t(
            "<th scope=\"row\">Documents &amp; signature électronique</th>", "<th scope=\"row\">Dokumente &amp; E-Signatur</th>",
            "<th scope=\"row\">Documentos &amp; firma electrónica</th>", "<th scope=\"row\">Documenti &amp; firma elettronica</th>",
            "<th scope=\"row\">Documenten &amp; e-handtekening</th>"),
        "<th scope=\"row\">HR letters</th>": _t(
            "<th scope=\"row\">Courriers RH</th>", "<th scope=\"row\">HR-Schreiben</th>", "<th scope=\"row\">Cartas de RR. HH.</th>",
            "<th scope=\"row\">Lettere HR</th>", "<th scope=\"row\">HR-brieven</th>"),
        "<th scope=\"row\">Announcements</th>": _t(
            "<th scope=\"row\">Annonces</th>", "<th scope=\"row\">Ankündigungen</th>", "<th scope=\"row\">Anuncios</th>",
            "<th scope=\"row\">Annunci</th>", "<th scope=\"row\">Aankondigingen</th>"),
        "<th scope=\"row\">Recognition</th>": _t(
            "<th scope=\"row\">Reconnaissance</th>", "<th scope=\"row\">Anerkennung</th>", "<th scope=\"row\">Reconocimiento</th>",
            "<th scope=\"row\">Riconoscimenti</th>", "<th scope=\"row\">Erkenning</th>"),
        "<th scope=\"row\">Probation</th>": _t(
            "<th scope=\"row\">Période d'essai</th>", "<th scope=\"row\">Probezeit</th>", "<th scope=\"row\">Período de prueba</th>",
            "<th scope=\"row\">Periodo di prova</th>", "<th scope=\"row\">Proeftijd</th>"),
        "<th scope=\"row\">Onboarding</th>": _t(
            "<th scope=\"row\">Intégration</th>", "<th scope=\"row\">Onboarding</th>", "<th scope=\"row\">Incorporación</th>",
            "<th scope=\"row\">Onboarding</th>", "<th scope=\"row\">Onboarding</th>"),
        "<th scope=\"row\">Time &amp; attendance</th>": _t(
            "<th scope=\"row\">Temps &amp; présence</th>", "<th scope=\"row\">Zeit &amp; Anwesenheit</th>", "<th scope=\"row\">Tiempo &amp; asistencia</th>",
            "<th scope=\"row\">Tempo &amp; presenze</th>", "<th scope=\"row\">Tijd &amp; aanwezigheid</th>"),
        "<th scope=\"row\">Overtime</th>": _t(
            "<th scope=\"row\">Heures supplémentaires</th>", "<th scope=\"row\">Überstunden</th>", "<th scope=\"row\">Horas extra</th>",
            "<th scope=\"row\">Straordinari</th>", "<th scope=\"row\">Overuren</th>"),
        "<th scope=\"row\">Credential tracking</th>": _t(
            "<th scope=\"row\">Suivi des habilitations</th>", "<th scope=\"row\">Nachweisverfolgung</th>", "<th scope=\"row\">Seguimiento de credenciales</th>",
            "<th scope=\"row\">Monitoraggio delle credenziali</th>", "<th scope=\"row\">Certificaatbewaking</th>"),
        "<th scope=\"row\">Bulk renewals</th>": _t(
            "<th scope=\"row\">Renouvellements en masse</th>", "<th scope=\"row\">Massenverlängerungen</th>", "<th scope=\"row\">Renovaciones masivas</th>",
            "<th scope=\"row\">Rinnovi in blocco</th>", "<th scope=\"row\">Bulkvernieuwingen</th>"),
        "<th scope=\"row\">Employment contracts</th>": _t(
            "<th scope=\"row\">Contrats de travail</th>", "<th scope=\"row\">Arbeitsverträge</th>", "<th scope=\"row\">Contratos laborales</th>",
            "<th scope=\"row\">Contratti di lavoro</th>", "<th scope=\"row\">Arbeidsovereenkomsten</th>"),
        "<th scope=\"row\">Assets</th>": _t(
            "<th scope=\"row\">Actifs</th>", "<th scope=\"row\">Assets</th>", "<th scope=\"row\">Activos</th>",
            "<th scope=\"row\">Asset</th>", "<th scope=\"row\">Activa</th>"),
        "<th scope=\"row\">HR helpdesk</th>": _t(
            "<th scope=\"row\">Assistance RH</th>", "<th scope=\"row\">HR-Helpdesk</th>", "<th scope=\"row\">Soporte de RR. HH.</th>",
            "<th scope=\"row\">Helpdesk HR</th>", "<th scope=\"row\">HR-helpdesk</th>"),
        "<th scope=\"row\">Disciplinary</th>": _t(
            "<th scope=\"row\">Discipline</th>", "<th scope=\"row\">Disziplinarmaßnahmen</th>", "<th scope=\"row\">Disciplina</th>",
            "<th scope=\"row\">Provvedimenti disciplinari</th>", "<th scope=\"row\">Disciplinaire zaken</th>"),
        "<th scope=\"row\">Benefits</th>": _t(
            "<th scope=\"row\">Avantages</th>", "<th scope=\"row\">Benefits</th>", "<th scope=\"row\">Beneficios</th>",
            "<th scope=\"row\">Benefit</th>", "<th scope=\"row\">Secundaire arbeidsvoorwaarden</th>"),
        "<th scope=\"row\">Performance</th>": _t(
            "<th scope=\"row\">Performance</th>", "<th scope=\"row\">Leistung</th>", "<th scope=\"row\">Desempeño</th>",
            "<th scope=\"row\">Performance</th>", "<th scope=\"row\">Prestaties</th>"),
        "<th scope=\"row\">Positions / establishment</th>": _t(
            "<th scope=\"row\">Postes / organigramme</th>", "<th scope=\"row\">Stellen / Stellenplan</th>", "<th scope=\"row\">Puestos / plantilla</th>",
            "<th scope=\"row\">Posizioni / organico</th>", "<th scope=\"row\">Functies / formatie</th>"),
        "<th scope=\"row\">Payroll</th>": _t(
            "<th scope=\"row\">Paie</th>", "<th scope=\"row\">Gehaltsabrechnung</th>", "<th scope=\"row\">Nóminas</th>",
            "<th scope=\"row\">Buste paga</th>", "<th scope=\"row\">Loonadministratie</th>"),
        "<th scope=\"row\">End-of-service (EOSB)</th>": _t(
            "<th scope=\"row\">Fin de service (EOSB)</th>", "<th scope=\"row\">Abfindung (EOSB)</th>", "<th scope=\"row\">Fin de servicio (EOSB)</th>",
            "<th scope=\"row\">Fine servizio (EOSB)</th>", "<th scope=\"row\">Einde dienstverband (EOSB)</th>"),
        "<th scope=\"row\">Housing advance</th>": _t(
            "<th scope=\"row\">Avance logement</th>", "<th scope=\"row\">Wohnungsvorschuss</th>", "<th scope=\"row\">Anticipo de vivienda</th>",
            "<th scope=\"row\">Anticipo alloggio</th>", "<th scope=\"row\">Huisvestingsvoorschot</th>"),
        "<th scope=\"row\">Compensation review</th>": _t(
            "<th scope=\"row\">Révision des rémunérations</th>", "<th scope=\"row\">Vergütungsüberprüfung</th>", "<th scope=\"row\">Revisión salarial</th>",
            "<th scope=\"row\">Revisione delle retribuzioni</th>", "<th scope=\"row\">Beloningsevaluatie</th>"),
        "<th scope=\"row\">Analytics</th>": _t(
            "<th scope=\"row\">Analytique</th>", "<th scope=\"row\">Analysen</th>", "<th scope=\"row\">Analítica</th>",
            "<th scope=\"row\">Analisi</th>", "<th scope=\"row\">Analyses</th>"),
        "<th scope=\"row\">Recruitment (ATS)</th>": _t(
            "<th scope=\"row\">Recrutement (ATS)</th>", "<th scope=\"row\">Rekrutierung (ATS)</th>", "<th scope=\"row\">Contratación (ATS)</th>",
            "<th scope=\"row\">Selezione (ATS)</th>", "<th scope=\"row\">Werving (ATS)</th>"),
        "<th scope=\"row\">Careers page</th>": _t(
            "<th scope=\"row\">Page carrières</th>", "<th scope=\"row\">Karriereseite</th>", "<th scope=\"row\">Página de empleo</th>",
            "<th scope=\"row\">Pagina lavora con noi</th>", "<th scope=\"row\">Vacaturepagina</th>"),
        "<th scope=\"row\">Succession &amp; development</th>": _t(
            "<th scope=\"row\">Succession &amp; développement</th>", "<th scope=\"row\">Nachfolge &amp; Entwicklung</th>", "<th scope=\"row\">Sucesión &amp; desarrollo</th>",
            "<th scope=\"row\">Successione &amp; sviluppo</th>", "<th scope=\"row\">Opvolging &amp; ontwikkeling</th>"),
        "<th scope=\"row\">Engagement surveys</th>": _t(
            "<th scope=\"row\">Enquêtes d'engagement</th>", "<th scope=\"row\">Engagement-Umfragen</th>", "<th scope=\"row\">Encuestas de compromiso</th>",
            "<th scope=\"row\">Sondaggi di coinvolgimento</th>", "<th scope=\"row\">Betrokkenheidsenquêtes</th>"),
        "<th scope=\"row\">Learning (LMS)</th>": _t(
            "<th scope=\"row\">Formation (LMS)</th>", "<th scope=\"row\">Lernen (LMS)</th>", "<th scope=\"row\">Formación (LMS)</th>",
            "<th scope=\"row\">Formazione (LMS)</th>", "<th scope=\"row\">Leren (LMS)</th>"),
        "<th scope=\"row\">AI helper</th>": _t(
            "<th scope=\"row\">Assistant IA</th>", "<th scope=\"row\">KI-Helfer</th>", "<th scope=\"row\">Asistente de IA</th>",
            "<th scope=\"row\">Assistente IA</th>", "<th scope=\"row\">AI-helper</th>"),
        "<th scope=\"row\">SSO &amp; SCIM</th>": _t(
            "<th scope=\"row\">SSO &amp; SCIM</th>", "<th scope=\"row\">SSO &amp; SCIM</th>", "<th scope=\"row\">SSO &amp; SCIM</th>",
            "<th scope=\"row\">SSO &amp; SCIM</th>", "<th scope=\"row\">SSO &amp; SCIM</th>"),
        "<th scope=\"row\">Deployment</th>": _t(
            "<th scope=\"row\">Déploiement</th>", "<th scope=\"row\">Bereitstellung</th>", "<th scope=\"row\">Despliegue</th>",
            "<th scope=\"row\">Distribuzione</th>", "<th scope=\"row\">Implementatie</th>"),
        "Dedicated / on-premise": _t(
            "Dédié / sur site", "Dediziert / on-premise", "Dedicado / on-premise",
            "Dedicato / on-premise", "Dedicated / on-premise"),
        # ---- Saudi note ----
        "Operating in Saudi Arabia?": _t(
            "Vous opérez en Arabie saoudite ?",
            "Sie sind in Saudi-Arabien tätig?",
            "¿Opera en Arabia Saudí?",
            "Operi in Arabia Saudita?",
            "Actief in Saoedi-Arabië?"),
        "Built for KSA compliance.": _t(
            "Conçu pour la conformité KSA.",
            "Für die KSA-Compliance gebaut.",
            "Diseñado para el cumplimiento en KSA.",
            "Progettato per la conformità KSA.",
            "Gebouwd voor KSA-compliance."),
        "WPS wage files, GOSI, end-of-service &amp; Nitaqat are built in.": _t(
            "Les fichiers de paie WPS, la GOSI, l'indemnité de fin de service &amp; Nitaqat sont intégrés.",
            "WPS-Lohndateien, GOSI, Abfindung &amp; Nitaqat sind integriert.",
            "Los archivos salariales WPS, GOSI, fin de servicio &amp; Nitaqat están integrados.",
            "I file salariali WPS, GOSI, fine servizio &amp; Nitaqat sono integrati.",
            "WPS-loonbestanden, GOSI, einde dienstverband &amp; Nitaqat zijn ingebouwd."),
        "See Saudi compliance →": _t(
            "Voir la conformité saoudienne →", "Saudi-Compliance ansehen →", "Ver el cumplimiento saudí →",
            "Vedi la conformità saudita →", "Bekijk Saoedische compliance →"),
        # ---- FAQ ----
        "HR Suite pricing, answered": _t(
            "Tarifs de HR Suite, expliqués", "HR Suite Preise, erklärt", "Precios de HR Suite, explicados",
            "Prezzi di HR Suite, spiegati", "HR Suite-prijzen, uitgelegd"),
        "Can I change plans later?": _t(
            "Puis-je changer de forfait plus tard ?", "Kann ich den Tarif später wechseln?", "¿Puedo cambiar de plan más tarde?",
            "Posso cambiare piano in seguito?", "Kan ik later van abonnement wisselen?"),
        "Yes — move up or down between the plans at any time. Changes take effect on your next billing cycle.": _t(
            "Oui — passez à un niveau supérieur ou inférieur entre les forfaits à tout moment. Les changements prennent effet au cycle de facturation suivant.",
            "Ja — wechseln Sie jederzeit zwischen den Tarifen nach oben oder unten. Änderungen werden zum nächsten Abrechnungszyklus wirksam.",
            "Sí — suba o baje entre los planes en cualquier momento. Los cambios se aplican en su próximo ciclo de facturación.",
            "Sì — passa a un livello superiore o inferiore tra i piani in qualsiasi momento. Le modifiche hanno effetto dal ciclo di fatturazione successivo.",
            "Ja — schakel op elk moment omhoog of omlaag tussen de abonnementen. Wijzigingen gaan in bij uw volgende factureringscyclus."),
        "How are users counted?": _t(
            "Comment les utilisateurs sont-ils comptés ?", "Wie werden Nutzer gezählt?", "¿Cómo se cuentan los usuarios?",
            "Come vengono conteggiati gli utenti?", "Hoe worden gebruikers geteld?"),
        "A user is anyone with a login to HR Suite. You're billed per active user, per month.": _t(
            "Un utilisateur est toute personne disposant d'un identifiant HR Suite. Vous êtes facturé par utilisateur actif, par mois.",
            "Ein Nutzer ist jede Person mit einem Login für HR Suite. Die Abrechnung erfolgt pro aktivem Nutzer und Monat.",
            "Un usuario es cualquier persona con acceso a HR Suite. Se factura por usuario activo, al mes.",
            "Un utente è chiunque abbia un accesso a HR Suite. La fatturazione è per utente attivo, al mese.",
            "Een gebruiker is iedereen met een login voor HR Suite. U wordt gefactureerd per actieve gebruiker, per maand."),
        "Do I need other FulcrumGrid apps?": _t(
            "Ai-je besoin d'autres applications FulcrumGrid ?", "Brauche ich andere FulcrumGrid-Apps?", "¿Necesito otras apps de FulcrumGrid?",
            "Ho bisogno di altre app FulcrumGrid?", "Heb ik andere FulcrumGrid-apps nodig?"),
        "Is there a free trial?": _t(
            "Y a-t-il un essai gratuit ?", "Gibt es eine kostenlose Testphase?", "¿Hay una prueba gratuita?",
            "È disponibile una prova gratuita?", "Is er een gratis proefperiode?"),
        "No. HR Suite works on its own. If you run several apps, the <a href=\"/pricing/\">whole-grid bundle</a> is cheaper than subscribing to each.": _t(
            "Non. HR Suite fonctionne de manière autonome. Si vous utilisez plusieurs applications, le <a href=\"/pricing/\">forfait grille complète</a> revient moins cher que de vous abonner à chacune.",
            "Nein. HR Suite funktioniert eigenständig. Wenn Sie mehrere Apps nutzen, ist das <a href=\"/pricing/\">Ganzes-Grid-Bundle</a> günstiger, als jede einzeln zu abonnieren.",
            "No. HR Suite funciona por sí solo. Si usa varias apps, el <a href=\"/pricing/\">paquete de cuadrícula completa</a> es más barato que suscribirse a cada una.",
            "No. HR Suite funziona da solo. Se usi più app, il <a href=\"/pricing/\">pacchetto griglia completa</a> costa meno che abbonarsi a ciascuna.",
            "Nee. HR Suite werkt op zichzelf. Als u meerdere apps gebruikt, is de <a href=\"/pricing/\">hele-grid-bundel</a> goedkoper dan u op elke app apart te abonneren."),
        "Every plan includes a 14-day free trial with full features. No credit card required to start.": _t(
            "Chaque forfait inclut un essai gratuit de 14 jours avec toutes les fonctionnalités. Aucune carte bancaire requise pour commencer.",
            "Jeder Tarif enthält eine 14-tägige kostenlose Testphase mit vollem Funktionsumfang. Keine Kreditkarte erforderlich, um zu starten.",
            "Cada plan incluye una prueba gratuita de 14 días con todas las funciones. No se necesita tarjeta de crédito para empezar.",
            "Ogni piano include una prova gratuita di 14 giorni con tutte le funzionalità. Nessuna carta di credito richiesta per iniziare.",
            "Elk abonnement bevat een gratis proefperiode van 14 dagen met alle functies. Geen creditcard nodig om te beginnen."),
        # ---- CTA ----
        "See HR Suite on your data": _t(
            "Voyez HR Suite sur vos données", "Sehen Sie HR Suite mit Ihren Daten", "Vea HR Suite con sus datos",
            "Vedi HR Suite sui tuoi dati", "Zie HR Suite op uw data"),
        "Tell us how your team runs today and we'll show you the right plan in action.": _t(
            "Dites-nous comment votre équipe travaille aujourd'hui et nous vous montrerons le bon forfait en action.",
            "Sagen Sie uns, wie Ihr Team heute arbeitet, und wir zeigen Ihnen den richtigen Tarif in Aktion.",
            "Cuéntenos cómo trabaja su equipo hoy y le mostraremos el plan adecuado en acción.",
            "Dicci come lavora oggi il tuo team e ti mostreremo il piano giusto in azione.",
            "Vertel ons hoe uw team vandaag werkt en we tonen u het juiste abonnement in actie."),
    },
}
