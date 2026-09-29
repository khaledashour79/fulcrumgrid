# -*- coding: utf-8 -*-
"""Per-page translations for the Products index, HR Suite, and Coming soon pages.

Keys are EXACT English substrings of the EN source HTML (entities, curly
apostrophes, dashes and glyphs preserved). Brand/product names (FulcrumGrid,
Command Center, Collection, HR Suite, Blog, FAQ) and code/currency labels are
left untranslated. Common chrome lives in loc_catalog.COMMON, not here.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/products/hr-suite/': {
        'src': 'products/hr-suite/index.html',
        't': {
            # ---- Meta ----
            "HR Suite is FulcrumGrid's people-operations app — employee records, onboarding, payroll, time and attendance, leave, and performance in one compliant system.": _t(
                "HR Suite est l'application de gestion du personnel de FulcrumGrid — dossiers des employés, intégration, paie, temps et présences, congés et performance dans un seul système conforme.",
                "HR Suite ist die Personalmanagement-App von FulcrumGrid — Mitarbeiterakten, Onboarding, Gehaltsabrechnung, Zeit und Anwesenheit, Abwesenheiten und Leistung in einem konformen System.",
                "HR Suite es la aplicación de gestión de personas de FulcrumGrid — expedientes de empleados, incorporación, nóminas, control horario y de asistencia, ausencias y desempeño en un único sistema conforme.",
                "HR Suite è l'app di gestione del personale di FulcrumGrid — schede dei dipendenti, onboarding, buste paga, presenze e orari, ferie e performance in un unico sistema conforme.",
                "HR Suite is de personeelsbeheer-app van FulcrumGrid — medewerkersdossiers, onboarding, loonadministratie, tijd en aanwezigheid, verlof en prestaties in één conform systeem."),
            "People operations from hire to retire: records, onboarding, payroll, time, leave, and performance.": _t(
                "La gestion du personnel, de l'embauche au départ : dossiers, intégration, paie, temps, congés et performance.",
                "Personalmanagement von der Einstellung bis zum Ruhestand: Akten, Onboarding, Gehaltsabrechnung, Zeit, Abwesenheiten und Leistung.",
                "Gestión de personas, de la contratación a la jubilación: expedientes, incorporación, nóminas, tiempo, ausencias y desempeño.",
                "Gestione del personale, dall'assunzione alla pensione: schede, onboarding, buste paga, tempo, ferie e performance.",
                "Personeelsbeheer van aanwerving tot pensioen: dossiers, onboarding, loonadministratie, tijd, verlof en prestaties."),
            "FulcrumGrid HR Suite — people operations from hire to retire": _t(
                "FulcrumGrid HR Suite — la gestion du personnel, de l'embauche au départ",
                "FulcrumGrid HR Suite — Personalmanagement von der Einstellung bis zum Ruhestand",
                "FulcrumGrid HR Suite — gestión de personas, de la contratación a la jubilación",
                "FulcrumGrid HR Suite — gestione del personale, dall'assunzione alla pensione",
                "FulcrumGrid HR Suite — personeelsbeheer van aanwerving tot pensioen"),
            # ---- Breadcrumb ----
            ">Home</a>": _t(">Accueil</a>", ">Startseite</a>", ">Inicio</a>", ">Home</a>", ">Home</a>"),
            # ---- Hero ----
            "Available now": _t("Disponible maintenant", "Jetzt verfügbar", "Ya disponible", "Ora disponibile", "Nu beschikbaar"),
            "</span> People</p>": _t("</span> Personnel</p>", "</span> Personal</p>", "</span> Personas</p>", "</span> Personale</p>", "</span> Personeel</p>"),
            "People operations,<br /><span class=\"p-grad\">handled.</span>": _t(
                "La gestion du personnel,<br /><span class=\"p-grad\">maîtrisée.</span>",
                "Personalmanagement,<br /><span class=\"p-grad\">gemeistert.</span>",
                "Gestión de personas,<br /><span class=\"p-grad\">resuelta.</span>",
                "Gestione del personale,<br /><span class=\"p-grad\">gestita.</span>",
                "Personeelsbeheer,<br /><span class=\"p-grad\">geregeld.</span>"),
            "HR Suite runs your team from hire to retire. Keep every employee record, onboard in a click, run payroll, track time and leave, and manage performance — all in one compliant, easy-to-run place.": _t(
                "HR Suite pilote votre équipe de l'embauche au départ. Conservez chaque dossier d'employé, intégrez en un clic, gérez la paie, suivez le temps et les congés, et pilotez la performance — le tout dans un seul espace conforme et simple à administrer.",
                "HR Suite steuert Ihr Team von der Einstellung bis zum Ruhestand. Führen Sie jede Mitarbeiterakte, onboarden Sie mit einem Klick, rechnen Sie Gehälter ab, erfassen Sie Zeit und Abwesenheiten und steuern Sie die Leistung — alles an einem konformen, einfach zu betreibenden Ort.",
                "HR Suite gestiona su equipo de la contratación a la jubilación. Mantenga cada expediente de empleado, incorpore con un clic, ejecute nóminas, controle el tiempo y las ausencias y gestione el desempeño — todo en un único lugar conforme y fácil de usar.",
                "HR Suite gestisce il tuo team dall'assunzione alla pensione. Conserva ogni scheda dipendente, fai l'onboarding con un clic, elabora le buste paga, monitora tempo e ferie e gestisci la performance — tutto in un unico luogo conforme e facile da usare.",
                "HR Suite runt uw team van aanwerving tot pensioen. Bewaar elk medewerkersdossier, onboard met één klik, verwerk de loonadministratie, volg tijd en verlof en beheer prestaties — allemaal op één conforme, eenvoudig te beheren plek."),
            "Open HR Suite": _t("Ouvrir HR Suite", "HR Suite öffnen", "Abrir HR Suite", "Apri HR Suite", "HR Suite openen"),
            # ---- Pricing ----
            "HR Suite pricing": _t("Tarifs HR Suite", "HR Suite Preise", "Precios de HR Suite", "Prezzi di HR Suite", "HR Suite-prijzen"),
            "/ seat / month": _t("/ poste / mois", "/ Platz / Monat", "/ puesto / mes", "/ postazione / mese", "/ gebruiker / maand"),
            "Billed per active seat (Starter plan). 14-day free trial, no card required.": _t(
                "Facturé par poste actif (forfait Starter). Essai gratuit de 14 jours, sans carte bancaire.",
                "Abrechnung pro aktivem Platz (Starter-Tarif). 14 Tage kostenlos testen, keine Karte erforderlich.",
                "Facturado por puesto activo (plan Starter). Prueba gratuita de 14 días, sin tarjeta.",
                "Fatturato per postazione attiva (piano Starter). Prova gratuita di 14 giorni, senza carta.",
                "Gefactureerd per actieve gebruiker (Starter-abonnement). 14 dagen gratis proberen, geen kaart nodig."),
            "Start free trial": _t("Démarrer l'essai gratuit", "Kostenlos testen", "Iniciar prueba gratuita", "Inizia la prova gratuita", "Start gratis proefperiode"),
            "See full pricing ↗": _t("Voir tous les tarifs ↗", "Alle Preise ansehen ↗", "Ver precios completos ↗", "Vedi tutti i prezzi ↗", "Bekijk alle prijzen ↗"),
            "Core HR &amp; time off": _t("RH de base &amp; congés", "Kern-HR &amp; Abwesenheiten", "RR. HH. esenciales &amp; ausencias", "HR di base &amp; ferie", "Kern-HR &amp; verlof"),
            "Expenses &amp; HR letters": _t("Notes de frais &amp; courriers RH", "Spesen &amp; HR-Schreiben", "Gastos &amp; cartas de RR. HH.", "Spese &amp; lettere HR", "Onkosten &amp; HR-brieven"),
            "Announcements, recognition &amp; probation": _t(
                "Annonces, reconnaissance &amp; période d'essai",
                "Ankündigungen, Anerkennung &amp; Probezeit",
                "Anuncios, reconocimiento &amp; periodo de prueba",
                "Annunci, riconoscimenti &amp; periodo di prova",
                "Aankondigingen, erkenning &amp; proeftijd"),
            "Email support": _t("Assistance par e-mail", "E-Mail-Support", "Soporte por correo", "Supporto via e-mail", "E-mailondersteuning"),
            # ---- Capabilities ----
            "Capabilities": _t("Capacités", "Funktionen", "Capacidades", "Funzionalità", "Mogelijkheden"),
            "The whole employee lifecycle": _t(
                "Tout le cycle de vie de l'employé", "Der gesamte Mitarbeiter-Lebenszyklus",
                "Todo el ciclo de vida del empleado", "L'intero ciclo di vita del dipendente",
                "De volledige levenscyclus van de medewerker"),
            "One system for everything HR, from the offer letter onward.": _t(
                "Un seul système pour toute la RH, dès la lettre d'offre.",
                "Ein System für alles rund um HR, ab dem Angebotsschreiben.",
                "Un único sistema para todo lo de RR. HH., desde la carta de oferta.",
                "Un unico sistema per tutta l'area HR, a partire dalla lettera di offerta.",
                "Eén systeem voor alles rond HR, vanaf de aanbiedingsbrief."),
            "Employee records": _t("Dossiers des employés", "Mitarbeiterakten", "Expedientes de empleados", "Schede dei dipendenti", "Medewerkersdossiers"),
            "A single, secure profile for every employee — documents, roles, compensation, and history in one file.": _t(
                "Un profil unique et sécurisé pour chaque employé — documents, rôles, rémunération et historique dans un seul dossier.",
                "Ein einziges, sicheres Profil für jeden Mitarbeiter — Dokumente, Rollen, Vergütung und Verlauf in einer Akte.",
                "Un perfil único y seguro para cada empleado — documentos, funciones, remuneración e historial en un solo archivo.",
                "Un profilo unico e sicuro per ogni dipendente — documenti, ruoli, retribuzione e cronologia in un unico file.",
                "Eén beveiligd profiel voor elke medewerker — documenten, rollen, beloning en geschiedenis in één dossier."),
            "<h3>Onboarding</h3>": _t("<h3>Intégration</h3>", "<h3>Onboarding</h3>", "<h3>Incorporación</h3>", "<h3>Onboarding</h3>", "<h3>Onboarding</h3>"),
            "Turn a new hire into a set-up teammate with checklists, e-signatures, and automatic account provisioning.": _t(
                "Transformez une nouvelle recrue en coéquipier opérationnel grâce aux listes de contrôle, aux signatures électroniques et à la création automatique des comptes.",
                "Machen Sie aus einer neuen Einstellung ein startklares Teammitglied — mit Checklisten, elektronischen Signaturen und automatischer Kontoeinrichtung.",
                "Convierta a un nuevo empleado en un compañero listo para trabajar con listas de verificación, firmas electrónicas y aprovisionamiento automático de cuentas.",
                "Trasforma un nuovo assunto in un collega pronto a partire con checklist, firme elettroniche e creazione automatica degli account.",
                "Maak van een nieuwe medewerker een startklare collega met checklists, e-handtekeningen en automatische accountaanmaak."),
            "<h3>Payroll</h3>": _t("<h3>Paie</h3>", "<h3>Gehaltsabrechnung</h3>", "<h3>Nóminas</h3>", "<h3>Buste paga</h3>", "<h3>Loonadministratie</h3>"),
            "Run accurate payroll on schedule, with earnings, deductions, and payslips generated for every cycle.": _t(
                "Exécutez une paie exacte dans les délais, avec les gains, les retenues et les bulletins de paie générés à chaque cycle.",
                "Rechnen Sie Gehälter präzise und pünktlich ab — mit Bezügen, Abzügen und Gehaltsabrechnungen für jeden Zyklus.",
                "Ejecute nóminas precisas a tiempo, con ingresos, deducciones y recibos generados en cada ciclo.",
                "Elabora buste paga precise e puntuali, con retribuzioni, trattenute e cedolini generati a ogni ciclo.",
                "Verwerk nauwkeurige loonadministratie op tijd, met verdiensten, inhoudingen en loonstroken voor elke cyclus."),
            "Time &amp; attendance": _t("Temps &amp; présences", "Zeit &amp; Anwesenheit", "Tiempo &amp; asistencia", "Presenze &amp; orari", "Tijd &amp; aanwezigheid"),
            "Clock-ins, timesheets, and shift tracking that flow straight into payroll — no double entry.": _t(
                "Pointages, feuilles de temps et suivi des équipes qui alimentent directement la paie — sans double saisie.",
                "Stempelungen, Zeiterfassung und Schichtverfolgung, die direkt in die Gehaltsabrechnung einfließen — ohne Doppelerfassung.",
                "Fichajes, hojas de horas y control de turnos que pasan directamente a nóminas — sin doble captura.",
                "Timbrature, fogli presenze e monitoraggio dei turni che confluiscono direttamente nelle buste paga — senza doppia immissione.",
                "Klokregistraties, urenstaten en ploegenregistratie die rechtstreeks naar de loonadministratie stromen — zonder dubbele invoer."),
            "Leave management": _t("Gestion des congés", "Abwesenheitsverwaltung", "Gestión de ausencias", "Gestione delle ferie", "Verlofbeheer"),
            "Requests, approvals, and balances for every leave type — with a shared calendar the whole team can see.": _t(
                "Demandes, approbations et soldes pour chaque type de congé — avec un calendrier partagé visible par toute l'équipe.",
                "Anträge, Genehmigungen und Salden für jede Abwesenheitsart — mit einem gemeinsamen Kalender, den das ganze Team sieht.",
                "Solicitudes, aprobaciones y saldos para cada tipo de ausencia — con un calendario compartido que ve todo el equipo.",
                "Richieste, approvazioni e saldi per ogni tipo di assenza — con un calendario condiviso visibile a tutto il team.",
                "Aanvragen, goedkeuringen en saldi voor elk verloftype — met een gedeelde agenda die het hele team ziet."),
            "Performance &amp; reviews": _t("Performance &amp; évaluations", "Leistung &amp; Beurteilungen", "Desempeño &amp; evaluaciones", "Performance &amp; valutazioni", "Prestaties &amp; beoordelingen"),
            "Goals, feedback, and review cycles that keep growth conversations on track and on record.": _t(
                "Objectifs, retours et cycles d'évaluation qui gardent les échanges sur la progression cadrés et documentés.",
                "Ziele, Feedback und Beurteilungszyklen, die Entwicklungsgespräche auf Kurs und dokumentiert halten.",
                "Objetivos, comentarios y ciclos de evaluación que mantienen las conversaciones de crecimiento encaminadas y registradas.",
                "Obiettivi, feedback e cicli di valutazione che tengono i colloqui di crescita in linea e documentati.",
                "Doelen, feedback en beoordelingscycli die groeigesprekken op koers en vastgelegd houden."),
            # ---- Built for ----
            "Built for": _t("Conçu pour", "Entwickelt für", "Diseñado para", "Pensato per", "Gebouwd voor"),
            "For the people who look after people": _t(
                "Pour celles et ceux qui prennent soin des équipes",
                "Für die Menschen, die sich um Menschen kümmern",
                "Para quienes cuidan de las personas",
                "Per chi si prende cura delle persone",
                "Voor de mensen die voor mensen zorgen"),
            "HR &amp; People teams": _t("Équipes RH &amp; People", "HR- &amp; People-Teams", "Equipos de RR. HH. &amp; People", "Team HR &amp; People", "HR- &amp; People-teams"),
            "Run the whole function from one system instead of stitching together five separate tools.": _t(
                "Pilotez toute la fonction depuis un seul système au lieu d'assembler cinq outils distincts.",
                "Steuern Sie die gesamte Funktion aus einem System, statt fünf einzelne Tools zusammenzustückeln.",
                "Gestione toda la función desde un solo sistema en lugar de unir cinco herramientas distintas.",
                "Gestisci l'intera funzione da un unico sistema invece di mettere insieme cinque strumenti separati.",
                "Run de hele functie vanuit één systeem in plaats van vijf losse tools aan elkaar te knopen."),
            "<h3>Managers</h3>": _t("<h3>Managers</h3>", "<h3>Führungskräfte</h3>", "<h3>Responsables</h3>", "<h3>Manager</h3>", "<h3>Managers</h3>"),
            "Approve leave, review timesheets, and run performance check-ins without leaving your workflow.": _t(
                "Approuvez les congés, vérifiez les feuilles de temps et menez les points de performance sans quitter votre flux de travail.",
                "Genehmigen Sie Abwesenheiten, prüfen Sie Zeiterfassungen und führen Sie Leistungsgespräche, ohne Ihren Arbeitsablauf zu verlassen.",
                "Apruebe ausencias, revise hojas de horas y realice revisiones de desempeño sin salir de su flujo de trabajo.",
                "Approva le ferie, controlla i fogli presenze e conduci i check-in sulla performance senza uscire dal tuo flusso di lavoro.",
                "Keur verlof goed, controleer urenstaten en houd prestatiegesprekken zonder uw workflow te verlaten."),
            "<h3>Employees</h3>": _t("<h3>Employés</h3>", "<h3>Mitarbeitende</h3>", "<h3>Empleados</h3>", "<h3>Dipendenti</h3>", "<h3>Medewerkers</h3>"),
            "Self-service for payslips, time off, and personal details — answers without an email to HR.": _t(
                "Libre-service pour les bulletins de paie, les congés et les informations personnelles — des réponses sans écrire à la RH.",
                "Self-Service für Gehaltsabrechnungen, Abwesenheiten und persönliche Daten — Antworten ohne E-Mail an die HR.",
                "Autoservicio para recibos de nómina, ausencias y datos personales — respuestas sin escribir a RR. HH.",
                "Self-service per cedolini, ferie e dati personali — risposte senza scrivere all'HR.",
                "Selfservice voor loonstroken, verlof en persoonlijke gegevens — antwoorden zonder een e-mail naar HR."),
            # ---- Compliance / regions ----
            "Compliance": _t("Conformité", "Compliance", "Cumplimiento", "Conformità", "Compliance"),
            "Built for global payroll": _t("Conçu pour la paie mondiale", "Für die weltweite Gehaltsabrechnung gebaut", "Diseñado para la nómina global", "Costruito per le buste paga globali", "Gebouwd voor wereldwijde loonadministratie"),
            "Payroll, statutory year-end, and compliance tuned to each market — across the Gulf, the UK, the US and Europe. Pick yours.": _t(
                "Paie, clôture annuelle légale et conformité adaptées à chaque marché — dans le Golfe, au Royaume-Uni, aux États-Unis et en Europe. Choisissez le vôtre.",
                "Gehaltsabrechnung, gesetzlicher Jahresabschluss und Compliance, abgestimmt auf jeden Markt — in der Golfregion, im Vereinigten Königreich, in den USA und in Europa. Wählen Sie Ihren.",
                "Nóminas, cierre anual legal y cumplimiento ajustados a cada mercado — en el Golfo, el Reino Unido, EE. UU. y Europa. Elija el suyo.",
                "Buste paga, chiusura annuale di legge e conformità su misura per ogni mercato — nel Golfo, nel Regno Unito, negli Stati Uniti e in Europa. Scegli il tuo.",
                "Loonadministratie, wettelijke jaarafsluiting en compliance afgestemd op elke markt — in de Golfregio, het VK, de VS en Europa. Kies de uwe."),
            "<h3>North America</h3>": _t("<h3>Amérique du Nord</h3>", "<h3>Nordamerika</h3>", "<h3>Norteamérica</h3>", "<h3>Nord America</h3>", "<h3>Noord-Amerika</h3>"),
            "United States · Canada": _t("États-Unis · Canada", "USA · Kanada", "Estados Unidos · Canadá", "Stati Uniti · Canada", "Verenigde Staten · Canada"),
            "<h3>Europe</h3>": _t("<h3>Europe</h3>", "<h3>Europa</h3>", "<h3>Europa</h3>", "<h3>Europa</h3>", "<h3>Europa</h3>"),
            "<h3>The GCC</h3>": _t("<h3>Le GCC</h3>", "<h3>Der GCC</h3>", "<h3>El GCC</h3>", "<h3>Il GCC</h3>", "<h3>De GCC</h3>"),
            "Saudi · UAE · Qatar · Kuwait · Bahrain · Oman": _t(
                "Arabie saoudite · EAU · Qatar · Koweït · Bahreïn · Oman",
                "Saudi-Arabien · VAE · Katar · Kuwait · Bahrain · Oman",
                "Arabia Saudí · EAU · Catar · Kuwait · Baréin · Omán",
                "Arabia Saudita · EAU · Qatar · Kuwait · Bahrein · Oman",
                "Saoedi-Arabië · VAE · Qatar · Koeweit · Bahrein · Oman"),
            "<h3>Middle East</h3>": _t("<h3>Moyen-Orient</h3>", "<h3>Naher Osten</h3>", "<h3>Oriente Medio</h3>", "<h3>Medio Oriente</h3>", "<h3>Midden-Oosten</h3>"),
            "Egypt · Jordan · Levant": _t("Égypte · Jordanie · Levant", "Ägypten · Jordanien · Levante", "Egipto · Jordania · Levante", "Egitto · Giordania · Levante", "Egypte · Jordanië · Levant"),
            "See all regions →": _t("Voir toutes les régions →", "Alle Regionen ansehen →", "Ver todas las regiones →", "Vedi tutte le regioni →", "Bekijk alle regio's →"),
            # ---- FulcrumGrid family ----
            "The FulcrumGrid family": _t("La famille FulcrumGrid", "Die FulcrumGrid-Familie", "La familia FulcrumGrid", "La famiglia FulcrumGrid", "De FulcrumGrid-familie"),
            "Explore the rest of the grid": _t("Découvrez le reste de la grille", "Entdecken Sie den Rest des Grids", "Explore el resto de la cuadrícula", "Esplora il resto della griglia", "Ontdek de rest van het grid"),
            "HR Suite is one of several FulcrumGrid apps, each built to the same standard. Explore the others built for your operations.": _t(
                "HR Suite est l'une des nombreuses applications FulcrumGrid, chacune conçue selon le même standard. Découvrez les autres, conçues pour vos opérations.",
                "HR Suite ist eine von mehreren FulcrumGrid-Apps, jede nach demselben Standard gebaut. Entdecken Sie die anderen, gebaut für Ihren Betrieb.",
                "HR Suite es una de las varias aplicaciones de FulcrumGrid, cada una creada con el mismo estándar. Explore las demás, creadas para sus operaciones.",
                "HR Suite è una delle diverse app FulcrumGrid, ognuna costruita secondo lo stesso standard. Esplora le altre, costruite per le tue operazioni.",
                "HR Suite is een van de vele FulcrumGrid-apps, elk gebouwd volgens dezelfde standaard. Ontdek de andere, gebouwd voor uw operatie."),
            "Operations dashboard": _t("Tableau de bord des opérations", "Betriebs-Dashboard", "Panel de operaciones", "Dashboard operativa", "Operationeel dashboard"),
            "Receivables &amp; payments": _t("Créances &amp; paiements", "Forderungen &amp; Zahlungen", "Cobros &amp; pagos", "Crediti &amp; pagamenti", "Vorderingen &amp; betalingen"),
            "<h3>More apps</h3>": _t("<h3>Plus d'applications</h3>", "<h3>Weitere Apps</h3>", "<h3>Más apps</h3>", "<h3>Altre app</h3>", "<h3>Meer apps</h3>"),
            "Inventory, CRM &amp; more": _t("Inventaire, CRM &amp; plus", "Lagerverwaltung, CRM &amp; mehr", "Inventario, CRM &amp; más", "Inventario, CRM &amp; altro", "Voorraad, CRM &amp; meer"),
            # ---- CTA ----
            "Run your people ops on one platform": _t(
                "Pilotez votre gestion du personnel sur une seule plateforme",
                "Führen Sie Ihr Personalmanagement auf einer Plattform",
                "Gestione sus operaciones de personas en una sola plataforma",
                "Gestisci le tue operazioni sul personale su un'unica piattaforma",
                "Run uw personeelsoperatie op één platform"),
            "See HR Suite handle the full employee lifecycle for your team.": _t(
                "Voyez HR Suite gérer tout le cycle de vie de l'employé pour votre équipe.",
                "Erleben Sie, wie HR Suite den gesamten Mitarbeiter-Lebenszyklus für Ihr Team abwickelt.",
                "Vea cómo HR Suite gestiona todo el ciclo de vida del empleado para su equipo.",
                "Guarda HR Suite gestire l'intero ciclo di vita del dipendente per il tuo team.",
                "Zie hoe HR Suite de volledige levenscyclus van de medewerker voor uw team afhandelt."),
        },
    },

    '/products/': {
        'src': 'products/index.html',
        't': {
            # ---- Meta ----
            "Explore the FulcrumGrid family of purpose-built business apps — Command Center, Collection, HR Suite, and more, all on one platform.": _t(
                "Découvrez la famille FulcrumGrid d'applications métier sur mesure — Command Center, Collection, HR Suite et plus, le tout sur une seule plateforme.",
                "Entdecken Sie die FulcrumGrid-Familie zweckgebauter Business-Apps — Command Center, Collection, HR Suite und mehr, alle auf einer Plattform.",
                "Explore la familia FulcrumGrid de aplicaciones de negocio a medida — Command Center, Collection, HR Suite y más, todo en una sola plataforma.",
                "Esplora la famiglia FulcrumGrid di applicazioni aziendali su misura — Command Center, Collection, HR Suite e altro, tutto su un'unica piattaforma.",
                "Ontdek de FulcrumGrid-familie van doelgerichte bedrijfsapps — Command Center, Collection, HR Suite en meer, allemaal op één platform."),
            "FulcrumGrid — purpose-built business apps for every operation": _t(
                "FulcrumGrid — des applications métier sur mesure pour chaque opération",
                "FulcrumGrid — zweckgebaute Business-Apps für jeden Betrieb",
                "FulcrumGrid — aplicaciones de negocio a medida para cada operación",
                "FulcrumGrid — applicazioni aziendali su misura per ogni operazione",
                "FulcrumGrid — doelgerichte bedrijfsapps voor elke operatie"),
            # ---- Breadcrumb ----
            ">Home</a>": _t(">Accueil</a>", ">Startseite</a>", ">Inicio</a>", ">Home</a>", ">Home</a>"),
            # ---- Hero ----
            "The grid of apps": _t("La grille d'applications", "Das Grid der Apps", "La cuadrícula de apps", "La griglia di app", "Het grid van apps"),
            "Purpose-built apps for <span class=\"p-grad\">every operation</span>": _t(
                "Des applications sur mesure pour <span class=\"p-grad\">chaque opération</span>",
                "Zweckgebaute Apps für <span class=\"p-grad\">jeden Betrieb</span>",
                "Aplicaciones a medida para <span class=\"p-grad\">cada operación</span>",
                "App su misura per <span class=\"p-grad\">ogni operazione</span>",
                "Doelgerichte apps voor <span class=\"p-grad\">elke operatie</span>"),
            "Each FulcrumGrid app solves a real problem on its own — and they all run on one platform, with the same clean experience. Start with one today and add the rest as you grow.": _t(
                "Chaque application FulcrumGrid résout à elle seule un vrai problème — et elles fonctionnent toutes sur une seule plateforme, avec la même expérience épurée. Commencez par une aujourd'hui et ajoutez les autres à mesure que vous grandissez.",
                "Jede FulcrumGrid-App löst für sich ein echtes Problem — und alle laufen auf einer Plattform, mit demselben klaren Erlebnis. Starten Sie heute mit einer und fügen Sie die übrigen hinzu, wenn Sie wachsen.",
                "Cada app de FulcrumGrid resuelve por sí sola un problema real — y todas funcionan en una sola plataforma, con la misma experiencia limpia. Empiece hoy con una y añada el resto a medida que crece.",
                "Ogni app FulcrumGrid risolve da sola un problema reale — e girano tutte su un'unica piattaforma, con la stessa esperienza pulita. Inizia oggi con una e aggiungi le altre man mano che cresci.",
                "Elke FulcrumGrid-app lost op zichzelf een echt probleem op — en ze draaien allemaal op één platform, met dezelfde heldere ervaring. Begin vandaag met één en voeg de rest toe naarmate u groeit."),
            "Translucent cobalt filaments converging at a single fulcrum point": _t(
                "Des filaments cobalt translucides convergeant vers un unique point d'appui",
                "Durchscheinende kobaltblaue Fäden, die in einem einzigen Angelpunkt zusammenlaufen",
                "Filamentos cobalto translúcidos que convergen en un único punto de apoyo",
                "Filamenti cobalto traslucidi che convergono in un unico fulcro",
                "Doorschijnende kobaltblauwe filamenten die samenkomen in één draaipunt"),
            # ---- Product cards ----
            "Available now": _t("Disponible maintenant", "Jetzt verfügbar", "Ya disponible", "Ora disponibile", "Nu beschikbaar"),
            "Explore <span aria-hidden=\"true\">→</span>": _t(
                "Découvrir <span aria-hidden=\"true\">→</span>",
                "Entdecken <span aria-hidden=\"true\">→</span>",
                "Explorar <span aria-hidden=\"true\">→</span>",
                "Esplora <span aria-hidden=\"true\">→</span>",
                "Ontdekken <span aria-hidden=\"true\">→</span>"),
            "Real-time operations dashboard. Monitor every metric, workflow, and alert across your business from a single control room.": _t(
                "Tableau de bord des opérations en temps réel. Surveillez chaque indicateur, flux de travail et alerte de votre entreprise depuis une salle de contrôle unique.",
                "Echtzeit-Dashboard für den Betrieb. Überwachen Sie jede Kennzahl, jeden Workflow und jede Warnung Ihres Unternehmens aus einem einzigen Kontrollraum.",
                "Panel de operaciones en tiempo real. Supervise cada métrica, flujo de trabajo y alerta de su negocio desde una única sala de control.",
                "Dashboard operativa in tempo reale. Monitora ogni metrica, flusso di lavoro e avviso della tua azienda da un'unica sala di controllo.",
                "Realtime operationeel dashboard. Volg elke metriek, workflow en melding in uw bedrijf vanuit één controlekamer."),
            "Live KPIs &amp; custom dashboards": _t("KPI en direct &amp; tableaux de bord personnalisés", "Live-KPIs &amp; individuelle Dashboards", "KPI en vivo &amp; paneles personalizados", "KPI in tempo reale &amp; dashboard personalizzate", "Live KPI's &amp; aangepaste dashboards"),
            "Alerts &amp; automated workflows": _t("Alertes &amp; flux de travail automatisés", "Warnungen &amp; automatisierte Workflows", "Alertas &amp; flujos automatizados", "Avvisi &amp; flussi di lavoro automatizzati", "Meldingen &amp; geautomatiseerde workflows"),
            "Reporting &amp; exports": _t("Rapports &amp; exports", "Berichte &amp; Exporte", "Informes &amp; exportaciones", "Report &amp; esportazioni", "Rapportage &amp; exports"),
            "Receivables and payments, handled. Track invoices, automate reminders, and recover revenue with clear, auditable collection workflows.": _t(
                "Créances et paiements, maîtrisés. Suivez les factures, automatisez les relances et récupérez vos revenus avec des flux de recouvrement clairs et auditables.",
                "Forderungen und Zahlungen, im Griff. Verfolgen Sie Rechnungen, automatisieren Sie Erinnerungen und holen Sie Umsätze mit klaren, prüfbaren Inkasso-Workflows zurück.",
                "Cobros y pagos, resueltos. Controle facturas, automatice recordatorios y recupere ingresos con flujos de cobro claros y auditables.",
                "Crediti e pagamenti, gestiti. Monitora le fatture, automatizza i solleciti e recupera i ricavi con flussi di incasso chiari e verificabili.",
                "Vorderingen en betalingen, geregeld. Volg facturen, automatiseer herinneringen en haal omzet binnen met heldere, controleerbare incassoworkflows."),
            "Invoice &amp; ledger tracking": _t("Suivi des factures &amp; du grand livre", "Rechnungs- &amp; Buchungsverfolgung", "Seguimiento de facturas &amp; libro mayor", "Monitoraggio fatture &amp; partitario", "Facturen- &amp; grootboekregistratie"),
            "Automated reminders &amp; plans": _t("Relances &amp; plans automatisés", "Automatisierte Erinnerungen &amp; Zahlungspläne", "Recordatorios &amp; planes automatizados", "Solleciti &amp; piani automatizzati", "Geautomatiseerde herinneringen &amp; plannen"),
            "Payment reconciliation": _t("Rapprochement des paiements", "Zahlungsabgleich", "Conciliación de pagos", "Riconciliazione dei pagamenti", "Betalingsreconciliatie"),
            "People operations from hire to retire. Manage employees, payroll, time off, and performance in one compliant, easy-to-run suite.": _t(
                "La gestion du personnel, de l'embauche au départ. Gérez les employés, la paie, les congés et la performance dans une suite unique, conforme et simple à administrer.",
                "Personalmanagement von der Einstellung bis zum Ruhestand. Verwalten Sie Mitarbeiter, Gehaltsabrechnung, Abwesenheiten und Leistung in einer konformen, einfach zu betreibenden Suite.",
                "Gestión de personas, de la contratación a la jubilación. Gestione empleados, nóminas, ausencias y desempeño en una suite conforme y fácil de usar.",
                "Gestione del personale, dall'assunzione alla pensione. Gestisci dipendenti, buste paga, ferie e performance in un'unica suite conforme e facile da usare.",
                "Personeelsbeheer van aanwerving tot pensioen. Beheer medewerkers, loonadministratie, verlof en prestaties in één conforme, eenvoudig te beheren suite."),
            "Employee records &amp; onboarding": _t("Dossiers des employés &amp; intégration", "Mitarbeiterakten &amp; Onboarding", "Expedientes de empleados &amp; incorporación", "Schede dei dipendenti &amp; onboarding", "Medewerkersdossiers &amp; onboarding"),
            "Payroll &amp; time tracking": _t("Paie &amp; suivi du temps", "Gehaltsabrechnung &amp; Zeiterfassung", "Nóminas &amp; control horario", "Buste paga &amp; monitoraggio del tempo", "Loonadministratie &amp; tijdregistratie"),
            "Performance &amp; reviews": _t("Performance &amp; évaluations", "Leistung &amp; Beurteilungen", "Desempeño &amp; evaluaciones", "Performance &amp; valutazioni", "Prestaties &amp; beoordelingen"),
            "More on the grid": _t("Plus sur la grille", "Mehr im Grid", "Más en la cuadrícula", "Altro sulla griglia", "Meer op het grid"),
            "Inventory, CRM, Analytics, and Procurement are in the works. Built on the same platform, so they plug straight in.": _t(
                "Inventaire, CRM, Analytique et Achats sont en préparation. Conçus sur la même plateforme, ils s'intègrent directement.",
                "Lagerverwaltung, CRM, Analysen und Beschaffung sind in Arbeit. Auf derselben Plattform gebaut, fügen sie sich direkt ein.",
                "Inventario, CRM, Analítica y Compras están en desarrollo. Creados en la misma plataforma, se integran directamente.",
                "Inventario, CRM, Analisi e Approvvigionamento sono in lavorazione. Costruiti sulla stessa piattaforma, si integrano subito.",
                "Voorraad, CRM, Analyse en Inkoop zijn in ontwikkeling. Gebouwd op hetzelfde platform, zodat ze direct aansluiten."),
            "Inventory &amp; Assets": _t("Inventaire &amp; actifs", "Lagerverwaltung &amp; Anlagen", "Inventario &amp; activos", "Inventario &amp; asset", "Voorraad &amp; activa"),
            "CRM &amp; Sales": _t("CRM &amp; ventes", "CRM &amp; Vertrieb", "CRM &amp; ventas", "CRM &amp; vendite", "CRM &amp; verkoop"),
            "Analytics &amp; Procurement": _t("Analytique &amp; achats", "Analysen &amp; Beschaffung", "Analítica &amp; compras", "Analisi &amp; approvvigionamento", "Analyse &amp; inkoop"),
            # ---- Custom apps CTA ----
            "Built for you": _t("Conçu pour vous", "Für Sie entwickelt", "Diseñado para usted", "Pensato per te", "Voor u gebouwd"),
            "Don't see your exact workflow?": _t(
                "Vous ne voyez pas votre flux de travail exact ?",
                "Ihr genauer Workflow ist nicht dabei?",
                "¿No encuentra su flujo de trabajo exacto?",
                "Non trovi il tuo flusso di lavoro esatto?",
                "Ziet u uw exacte workflow niet?"),
            "Beyond our ready-made apps, we build customized business apps tailored to your specific use case — on the same secure, auditable platform as the rest of the grid.": _t(
                "Au-delà de nos applications prêtes à l'emploi, nous concevons des applications métier personnalisées, adaptées à votre cas d'usage précis — sur la même plateforme sécurisée et auditable que le reste de la grille.",
                "Über unsere fertigen Apps hinaus entwickeln wir maßgeschneiderte Business-Apps für Ihren konkreten Anwendungsfall — auf derselben sicheren, prüfbaren Plattform wie der Rest des Grids.",
                "Más allá de nuestras apps listas para usar, creamos aplicaciones de negocio personalizadas y adaptadas a su caso de uso concreto — en la misma plataforma segura y auditable que el resto de la cuadrícula.",
                "Oltre alle nostre app pronte all'uso, sviluppiamo applicazioni aziendali personalizzate su misura per il tuo caso d'uso specifico — sulla stessa piattaforma sicura e verificabile del resto della griglia.",
                "Naast onze kant-en-klare apps bouwen we op maat gemaakte bedrijfsapps, afgestemd op uw specifieke use case — op hetzelfde veilige, controleerbare platform als de rest van het grid."),
            "Explore custom apps": _t("Découvrir les applications sur mesure", "Individuelle Apps entdecken", "Explorar apps a medida", "Esplora le app su misura", "Ontdek apps op maat"),
            # ---- Ready CTA ----
            "Ready to run on one grid?": _t("Prêt à tout piloter sur une seule grille ?", "Bereit, auf einem Grid zu arbeiten?", "¿Listo para operar en una sola cuadrícula?", "Pronto a lavorare su un'unica griglia?", "Klaar om op één grid te werken?"),
            "Tell us what your team needs and we'll show you FulcrumGrid in action.": _t(
                "Dites-nous ce dont votre équipe a besoin et nous vous montrerons FulcrumGrid en action.",
                "Sagen Sie uns, was Ihr Team braucht, und wir zeigen Ihnen FulcrumGrid in Aktion.",
                "Cuéntenos qué necesita su equipo y le mostraremos FulcrumGrid en acción.",
                "Dicci di cosa ha bisogno il tuo team e ti mostreremo FulcrumGrid in azione.",
                "Vertel ons wat uw team nodig heeft en we tonen u FulcrumGrid in actie."),
            "See pricing": _t("Voir les tarifs", "Preise ansehen", "Ver precios", "Vedi i prezzi", "Bekijk prijzen"),
            "vs. spreadsheets": _t("vs. tableurs", "vs. Tabellen", "vs. hojas de cálculo", "vs. fogli di calcolo", "vs. spreadsheets"),
        },
    },

    '/products/coming-soon/': {
        'src': 'products/coming-soon/index.html',
        't': {
            # ---- Meta ----
            "More FulcrumGrid apps in active development — Inventory, CRM, Analytics, and Procurement — built on the same platform. Get early access.": _t(
                "D'autres applications FulcrumGrid en développement actif — Inventaire, CRM, Analytique et Achats — conçues sur la même plateforme. Obtenez un accès anticipé.",
                "Weitere FulcrumGrid-Apps in aktiver Entwicklung — Lagerverwaltung, CRM, Analysen und Beschaffung — auf derselben Plattform gebaut. Sichern Sie sich frühen Zugang.",
                "Más aplicaciones de FulcrumGrid en desarrollo activo — Inventario, CRM, Analítica y Compras — creadas en la misma plataforma. Consiga acceso anticipado.",
                "Altre app FulcrumGrid in fase di sviluppo attivo — Inventario, CRM, Analisi e Approvvigionamento — costruite sulla stessa piattaforma. Ottieni l'accesso anticipato.",
                "Meer FulcrumGrid-apps in actieve ontwikkeling — Voorraad, CRM, Analyse en Inkoop — gebouwd op hetzelfde platform. Krijg vroege toegang."),
            "Inventory, CRM, Analytics, and Procurement — coming to the grid.": _t(
                "Inventaire, CRM, Analytique et Achats — bientôt sur la grille.",
                "Lagerverwaltung, CRM, Analysen und Beschaffung — bald im Grid.",
                "Inventario, CRM, Analítica y Compras — próximamente en la cuadrícula.",
                "Inventario, CRM, Analisi e Approvvigionamento — presto sulla griglia.",
                "Voorraad, CRM, Analyse en Inkoop — binnenkort op het grid."),
            "FulcrumGrid — more apps coming to the grid": _t(
                "FulcrumGrid — d'autres applications bientôt sur la grille",
                "FulcrumGrid — weitere Apps bald im Grid",
                "FulcrumGrid — más apps próximamente en la cuadrícula",
                "FulcrumGrid — altre app presto sulla griglia",
                "FulcrumGrid — meer apps binnenkort op het grid"),
            # ---- Breadcrumb ----
            ">Home</a>": _t(">Accueil</a>", ">Startseite</a>", ">Inicio</a>", ">Home</a>", ">Home</a>"),
            # ---- Hero ----
            "Roadmap": _t("Feuille de route", "Roadmap", "Hoja de ruta", "Roadmap", "Roadmap"),
            "In development": _t("En développement", "In Entwicklung", "En desarrollo", "In sviluppo", "In ontwikkeling"),
            "More apps, <span class=\"p-grad\">coming to the grid</span>": _t(
                "D'autres applications, <span class=\"p-grad\">bientôt sur la grille</span>",
                "Weitere Apps, <span class=\"p-grad\">bald im Grid</span>",
                "Más apps, <span class=\"p-grad\">próximamente en la cuadrícula</span>",
                "Altre app, <span class=\"p-grad\">presto sulla griglia</span>",
                "Meer apps, <span class=\"p-grad\">binnenkort op het grid</span>"),
            "New apps are in active development — each built to the same standard as the apps you already know. Get early access as they land.": _t(
                "De nouvelles applications sont en développement actif — chacune conçue selon le même standard que les applications que vous connaissez déjà. Obtenez un accès anticipé dès leur arrivée.",
                "Neue Apps sind in aktiver Entwicklung — jede nach demselben Standard gebaut wie die Apps, die Sie bereits kennen. Sichern Sie sich frühen Zugang, sobald sie erscheinen.",
                "Hay nuevas apps en desarrollo activo — cada una creada con el mismo estándar que las apps que ya conoce. Consiga acceso anticipado en cuanto lleguen.",
                "Nuove app sono in fase di sviluppo attivo — ognuna costruita secondo lo stesso standard delle app che già conosci. Ottieni l'accesso anticipato non appena arrivano.",
                "Er zijn nieuwe apps in actieve ontwikkeling — elk gebouwd volgens dezelfde standaard als de apps die u al kent. Krijg vroege toegang zodra ze verschijnen."),
            "Get early access": _t("Obtenir un accès anticipé", "Frühen Zugang sichern", "Conseguir acceso anticipado", "Ottieni l'accesso anticipato", "Vroege toegang krijgen"),
            "Available apps": _t("Applications disponibles", "Verfügbare Apps", "Apps disponibles", "App disponibili", "Beschikbare apps"),
            # ---- Roadmap cards ----
            "On the roadmap": _t("Sur la feuille de route", "Auf der Roadmap", "En la hoja de ruta", "Nella roadmap", "Op de roadmap"),
            "What's next on the grid": _t("Ce qui arrive sur la grille", "Was als Nächstes ins Grid kommt", "Lo próximo en la cuadrícula", "Cosa arriva sulla griglia", "Wat er nu op het grid komt"),
            "Inventory &amp; Assets": _t("Inventaire &amp; actifs", "Lagerverwaltung &amp; Anlagen", "Inventario &amp; activos", "Inventario &amp; asset", "Voorraad &amp; activa"),
            "Track stock, assets, and locations in real time, with the clarity you'd expect from a FulcrumGrid app.": _t(
                "Suivez le stock, les actifs et les emplacements en temps réel, avec la clarté que vous attendez d'une application FulcrumGrid.",
                "Verfolgen Sie Bestand, Anlagen und Standorte in Echtzeit — mit der Klarheit, die Sie von einer FulcrumGrid-App erwarten.",
                "Controle existencias, activos y ubicaciones en tiempo real, con la claridad que espera de una app de FulcrumGrid.",
                "Monitora scorte, asset e sedi in tempo reale, con la chiarezza che ti aspetti da un'app FulcrumGrid.",
                "Volg voorraad, activa en locaties in realtime, met de helderheid die u van een FulcrumGrid-app verwacht."),
            "CRM &amp; Sales": _t("CRM &amp; ventes", "CRM &amp; Vertrieb", "CRM &amp; ventas", "CRM &amp; vendite", "CRM &amp; verkoop"),
            "Manage leads, deals, and customer relationships from first touch to closed won.": _t(
                "Gérez les prospects, les affaires et les relations clients, du premier contact à la conclusion.",
                "Verwalten Sie Leads, Deals und Kundenbeziehungen vom ersten Kontakt bis zum Abschluss.",
                "Gestione oportunidades, negociaciones y relaciones con clientes desde el primer contacto hasta el cierre.",
                "Gestisci lead, trattative e relazioni con i clienti dal primo contatto alla chiusura.",
                "Beheer leads, deals en klantrelaties van eerste contact tot gesloten deal."),
            "<h3>Analytics</h3>": _t("<h3>Analytique</h3>", "<h3>Analysen</h3>", "<h3>Analítica</h3>", "<h3>Analisi</h3>", "<h3>Analyse</h3>"),
            "Deep analytics and custom reports for your business — clear numbers you can trust.": _t(
                "Des analyses approfondies et des rapports personnalisés pour votre entreprise — des chiffres clairs et fiables.",
                "Tiefgehende Analysen und individuelle Berichte für Ihr Unternehmen — klare Zahlen, denen Sie vertrauen können.",
                "Analítica profunda e informes personalizados para su negocio — cifras claras en las que puede confiar.",
                "Analisi approfondite e report personalizzati per la tua azienda — numeri chiari e affidabili.",
                "Diepgaande analyses en aangepaste rapporten voor uw bedrijf — heldere cijfers waarop u kunt vertrouwen."),
            "<h3>Procurement</h3>": _t("<h3>Achats</h3>", "<h3>Beschaffung</h3>", "<h3>Compras</h3>", "<h3>Approvvigionamento</h3>", "<h3>Inkoop</h3>"),
            "Purchase orders, vendors, and approvals in one clear, auditable workflow.": _t(
                "Bons de commande, fournisseurs et approbations dans un flux de travail unique, clair et auditable.",
                "Bestellungen, Lieferanten und Genehmigungen in einem klaren, prüfbaren Workflow.",
                "Órdenes de compra, proveedores y aprobaciones en un flujo de trabajo único, claro y auditable.",
                "Ordini d'acquisto, fornitori e approvazioni in un unico flusso di lavoro chiaro e verificabile.",
                "Inkooporders, leveranciers en goedkeuringen in één heldere, controleerbare workflow."),
            # ---- Notify CTA / form ----
            "Be first to know": _t("Soyez informé en premier", "Erfahren Sie es als Erste", "Sea el primero en saberlo", "Sii il primo a saperlo", "Wees als eerste op de hoogte"),
            "Leave your details and we'll let you know the moment these apps go live.": _t(
                "Laissez vos coordonnées et nous vous préviendrons dès que ces applications seront disponibles.",
                "Hinterlassen Sie Ihre Kontaktdaten und wir informieren Sie, sobald diese Apps live gehen.",
                "Deje sus datos y le avisaremos en cuanto estas apps estén disponibles.",
                "Lascia i tuoi dati e ti avviseremo appena queste app saranno disponibili.",
                "Laat uw gegevens achter en we laten het u weten zodra deze apps live gaan."),
            "Which app are you interested in? (optional)": _t(
                "Quelle application vous intéresse ? (facultatif)",
                "Für welche App interessieren Sie sich? (optional)",
                "¿Qué app le interesa? (opcional)",
                "Quale app ti interessa? (facoltativo)",
                "In welke app bent u geïnteresseerd? (optioneel)"),
            "Which app are you interested in?": _t(
                "Quelle application vous intéresse ?",
                "Für welche App interessieren Sie sich?",
                "¿Qué app le interesa?",
                "Quale app ti interessa?",
                "In welke app bent u geïnteresseerd?"),
            ">A custom app</option>": _t(
                ">Une application sur mesure</option>",
                ">Eine individuelle App</option>",
                ">Una app a medida</option>",
                ">Un'app su misura</option>",
                ">Een app op maat</option>"),
            "Not sure — please recommend one for me": _t(
                "Je ne sais pas — recommandez-m'en une",
                "Nicht sicher — bitte empfehlen Sie mir eine",
                "No estoy seguro — recomiéndeme una",
                "Non sono sicuro — consigliamene una",
                "Weet ik niet — beveel er een voor mij aan"),
            "Your name": _t("Votre nom", "Ihr Name", "Su nombre", "Il tuo nome", "Uw naam"),
            "Work email": _t("E-mail professionnel", "Geschäftliche E-Mail", "Correo de trabajo", "E-mail di lavoro", "Werk-e-mail"),
            "Notify me": _t("Prévenez-moi", "Benachrichtigen Sie mich", "Avísenme", "Avvisami", "Houd me op de hoogte"),
            "Or email us at": _t("Ou écrivez-nous à", "Oder schreiben Sie uns an", "O escríbanos a", "Oppure scrivici a", "Of mail ons op"),
        },
    },
}
