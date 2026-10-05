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
            # ---- Hero ----
            "Available now": _t("Disponible maintenant", "Jetzt verfügbar", "Ya disponible", "Ora disponibile", "Nu beschikbaar"),
            ">People ·": _t(">Personnel ·", ">Personal ·", ">Personas ·", ">Personale ·", ">Personeel ·"),
            "People operations, handled.": _t(
                "La gestion du personnel, maîtrisée.",
                "Personalmanagement, gemeistert.",
                "Gestión de personas, resuelta.",
                "Gestione del personale, gestita.",
                "Personeelsbeheer, geregeld."),
            "HR Suite runs your team from hire to retire. Keep every employee record, onboard in a click, run payroll, track time and leave, and manage performance — all in one compliant, easy-to-run place.": _t(
                "HR Suite pilote votre équipe de l'embauche au départ. Conservez chaque dossier d'employé, intégrez en un clic, gérez la paie, suivez le temps et les congés, et pilotez la performance — le tout dans un seul espace conforme et simple à administrer.",
                "HR Suite steuert Ihr Team von der Einstellung bis zum Ruhestand. Führen Sie jede Mitarbeiterakte, onboarden Sie mit einem Klick, rechnen Sie Gehälter ab, erfassen Sie Zeit und Abwesenheiten und steuern Sie die Leistung — alles an einem konformen, einfach zu betreibenden Ort.",
                "HR Suite gestiona su equipo de la contratación a la jubilación. Mantenga cada expediente de empleado, incorpore con un clic, ejecute nóminas, controle el tiempo y las ausencias y gestione el desempeño — todo en un único lugar conforme y fácil de usar.",
                "HR Suite gestisce il tuo team dall'assunzione alla pensione. Conserva ogni scheda dipendente, fai l'onboarding con un clic, elabora le buste paga, monitora tempo e ferie e gestisci la performance — tutto in un unico luogo conforme e facile da usare.",
                "HR Suite runt uw team van aanwerving tot pensioen. Bewaar elk medewerkersdossier, onboard met één klik, verwerk de loonadministratie, volg tijd en verlof en beheer prestaties — allemaal op één conforme, eenvoudig te beheren plek."),
            "Open HR Suite": _t("Ouvrir HR Suite", "HR Suite öffnen", "Abrir HR Suite", "Apri HR Suite", "HR Suite openen"),
            # ---- Flagship · AI Copilot & Agents ----
            "New · AI Copilot &amp; Agents": _t(
                "Nouveau · Copilote IA &amp; agents", "Neu · KI-Copilot &amp; Agenten",
                "Nuevo · Copiloto de IA &amp; agentes", "Novità · Copilota IA &amp; agenti",
                "Nieuw · AI-copilot &amp; agents"),
            "AI that works the way HR has to.": _t(
                "Une IA qui fonctionne comme la RH l'exige.",
                "KI, die so arbeitet, wie HR es muss.",
                "IA que funciona como RR. HH. lo exige.",
                "Un'IA che lavora come deve farlo l'HR.",
                "AI die werkt zoals HR dat moet."),
            "A copilot on every page, AI reviews grounded in the record, and acting agents that never move without a human approval — on the model and data boundary you choose.": _t(
                "Un copilote sur chaque page, des analyses IA ancrées dans le dossier et des agents actifs qui n'agissent jamais sans l'approbation d'une personne — sur le modèle et la frontière de données que vous choisissez.",
                "Ein Copilot auf jeder Seite, KI-Analysen direkt am Datensatz und handelnde Agenten, die sich nie ohne menschliche Freigabe bewegen — auf dem Modell und der Datengrenze Ihrer Wahl.",
                "Un copiloto en cada página, análisis de IA anclados en el registro y agentes que actúan pero nunca se mueven sin la aprobación de una persona — sobre el modelo y el límite de datos que usted elija.",
                "Un copilota su ogni pagina, analisi IA ancorate al record e agenti operativi che non si muovono mai senza l'approvazione di una persona — sul modello e sul confine dei dati che scegli.",
                "Een copilot op elke pagina, AI-analyses verankerd in het record en handelende agents die nooit iets doen zonder menselijke goedkeuring — op het model en de datagrens die u kiest."),
            "Copilot on every page": _t(
                "Un copilote sur chaque page", "Ein Copilot auf jeder Seite",
                "Un copiloto en cada página", "Un copilota su ogni pagina",
                "Een copilot op elke pagina"),
            "Ask about any policy in plain language and get an answer drawn only from the policies you're allowed to see, cited to the source. If no policy covers it, it says so — it never guesses.": _t(
                "Posez une question sur n'importe quelle politique en langage courant et obtenez une réponse tirée uniquement des politiques que vous êtes autorisé à voir, avec la source citée. Si aucune politique ne couvre la question, il le dit — il ne devine jamais.",
                "Fragen Sie in natürlicher Sprache nach einer Richtlinie und erhalten Sie eine Antwort, die nur aus den Richtlinien stammt, die Sie sehen dürfen — mit Quellenangabe. Deckt keine Richtlinie die Frage ab, sagt er es — er rät nie.",
                "Pregunte sobre cualquier política en lenguaje natural y obtenga una respuesta extraída solo de las políticas que puede ver, citada a la fuente. Si ninguna política lo cubre, lo dice — nunca adivina.",
                "Chiedi di qualsiasi policy in linguaggio naturale e ottieni una risposta tratta solo dalle policy che puoi vedere, con la fonte citata. Se nessuna policy copre la domanda, lo dice — non tira mai a indovinare.",
                "Vraag in gewone taal naar een beleidsregel en krijg een antwoord dat alleen is gebaseerd op het beleid dat u mag zien, met bronvermelding. Dekt geen enkel beleid de vraag, dan zegt het dat — het gokt nooit."),
            "AI reviews, in context": _t(
                "Des analyses IA, en contexte", "KI-Analysen, im Kontext",
                "Análisis de IA, en contexto", "Analisi IA, nel contesto",
                "AI-analyses, in context"),
            "A grounded summary right on the record — review an employee, summarize a candidate, explain a pay-run variance, triage attendance exceptions. Read-only: it summarizes, it never changes the record.": _t(
                "Un résumé étayé directement sur le dossier — évaluer un employé, résumer un candidat, expliquer un écart de paie, trier les anomalies de présence. En lecture seule : il résume, il ne modifie jamais le dossier.",
                "Eine fundierte Zusammenfassung direkt am Datensatz — einen Mitarbeiter prüfen, einen Kandidaten zusammenfassen, eine Abweichung im Gehaltslauf erklären, Anwesenheitsausnahmen sichten. Nur Lesezugriff: Er fasst zusammen, er ändert den Datensatz nie.",
                "Un resumen fundamentado directamente en el registro — revisar a un empleado, resumir a un candidato, explicar una variación de nómina, clasificar excepciones de asistencia. Solo lectura: resume, nunca cambia el registro.",
                "Una sintesi fondata direttamente sul record — valutare un dipendente, riassumere un candidato, spiegare uno scostamento di un ciclo paga, smistare le eccezioni di presenza. Sola lettura: sintetizza, non modifica mai il record.",
                "Een onderbouwde samenvatting direct op het record — een medewerker beoordelen, een kandidaat samenvatten, een afwijking in een loonrun verklaren, aanwezigheidsuitzonderingen triëren. Alleen-lezen: het vat samen, het wijzigt het record nooit."),
            "Acting agents, human-approved": _t(
                "Des agents actifs, approuvés par un humain", "Handelnde Agenten, von Menschen freigegeben",
                "Agentes que actúan, aprobados por una persona", "Agenti operativi, approvati da una persona",
                "Handelende agents, door mensen goedgekeurd"),
            "Agents like AI shortlist propose a change; nothing happens until a person approves it in the Approvals inbox. Whoever ran the agent can't approve it — the same separation of duties as money.": _t(
                "Des agents comme la présélection IA proposent un changement ; rien ne se produit tant qu'une personne ne l'a pas approuvé dans la boîte des approbations. Celui qui a lancé l'agent ne peut pas l'approuver — la même séparation des tâches que pour l'argent.",
                "Agenten wie die KI-Vorauswahl schlagen eine Änderung vor; nichts geschieht, bis eine Person sie im Genehmigungs-Posteingang freigibt. Wer den Agenten gestartet hat, kann ihn nicht freigeben — dieselbe Funktionstrennung wie bei Geld.",
                "Agentes como la preselección por IA proponen un cambio; nada ocurre hasta que una persona lo aprueba en la bandeja de aprobaciones. Quien ejecutó el agente no puede aprobarlo — la misma separación de funciones que con el dinero.",
                "Agenti come la preselezione IA propongono una modifica; non accade nulla finché una persona non la approva nella casella delle approvazioni. Chi ha avviato l'agente non può approvarla — la stessa separazione dei compiti del denaro.",
                "Agents zoals AI-shortlist stellen een wijziging voor; er gebeurt niets tot een persoon het goedkeurt in de goedkeuringeninbox. Wie de agent uitvoerde, kan het niet goedkeuren — dezelfde functiescheiding als bij geld."),
            "Low-stakes steps only": _t(
                "Uniquement des actions à faible enjeu", "Nur risikoarme Schritte",
                "Solo pasos de bajo riesgo", "Solo passaggi a basso rischio",
                "Alleen stappen met laag risico"),
            "Agents take only reversible, low-stakes steps such as a pipeline move. Money, employment status, ratings and government actions are never available to an AI agent.": _t(
                "Les agents n'effectuent que des actions réversibles et à faible enjeu, comme un déplacement dans le pipeline. L'argent, le statut d'emploi, les évaluations et les démarches administratives ne sont jamais accessibles à un agent IA.",
                "Agenten führen nur reversible, risikoarme Schritte aus, etwa eine Verschiebung in der Pipeline. Geld, Beschäftigungsstatus, Bewertungen und Behördenvorgänge stehen einem KI-Agenten nie zur Verfügung.",
                "Los agentes solo realizan pasos reversibles y de bajo riesgo, como mover una etapa del pipeline. El dinero, la situación laboral, las valoraciones y los trámites ante la Administración nunca están disponibles para un agente de IA.",
                "Gli agenti eseguono solo passaggi reversibili e a basso rischio, come uno spostamento nella pipeline. Denaro, stato occupazionale, valutazioni e adempimenti verso la pubblica amministrazione non sono mai accessibili a un agente IA.",
                "Agents voeren alleen omkeerbare stappen met laag risico uit, zoals een verplaatsing in de pipeline. Geld, dienstverband, beoordelingen en overheidshandelingen zijn nooit beschikbaar voor een AI-agent."),
            "Your model, your data": _t(
                "Votre modèle, vos données", "Ihr Modell, Ihre Daten",
                "Su modelo, sus datos", "Il tuo modello, i tuoi dati",
                "Uw model, uw data"),
            "Try it on a capped shared key, bring your own OpenAI, Anthropic or Azure key, or point it at a self-hosted model so data never leaves your infrastructure. Keys are encrypted and isolated per tenant.": _t(
                "Essayez-la avec une clé partagée plafonnée, apportez votre propre clé OpenAI, Anthropic ou Azure, ou pointez-la vers un modèle auto-hébergé pour que les données ne quittent jamais votre infrastructure. Les clés sont chiffrées et isolées par locataire.",
                "Testen Sie sie mit einem gedeckelten gemeinsamen Schlüssel, bringen Sie Ihren eigenen OpenAI-, Anthropic- oder Azure-Schlüssel mit oder richten Sie sie auf ein selbst gehostetes Modell, damit Daten Ihre Infrastruktur nie verlassen. Schlüssel werden verschlüsselt und pro Mandant isoliert.",
                "Pruébela con una clave compartida con tope, use su propia clave de OpenAI, Anthropic o Azure, o apúntela a un modelo autoalojado para que los datos nunca salgan de su infraestructura. Las claves se cifran y se aíslan por inquilino.",
                "Provala con una chiave condivisa con tetto massimo, porta la tua chiave OpenAI, Anthropic o Azure, oppure puntala a un modello self-hosted così i dati non lasciano mai la tua infrastruttura. Le chiavi sono cifrate e isolate per tenant.",
                "Probeer het met een gedeelde sleutel met limiet, gebruik uw eigen OpenAI-, Anthropic- of Azure-sleutel, of wijs het naar een zelf-gehost model zodat data uw infrastructuur nooit verlaat. Sleutels worden versleuteld en per tenant geïsoleerd."),
            "Governed &amp; auditable": _t(
                "Encadrée &amp; auditable", "Gesteuert &amp; prüfbar",
                "Gobernada &amp; auditable", "Governata &amp; verificabile",
                "Beheerst &amp; controleerbaar"),
            "AI is off until you turn it on, gated by the Act with AI permission, with an Agent Center log of every request — metadata only, so it holds no employee data.": _t(
                "L'IA est désactivée tant que vous ne l'activez pas, protégée par l'autorisation « Agir avec l'IA », avec un journal du Centre des agents pour chaque requête — métadonnées uniquement, sans aucune donnée d'employé.",
                "Die KI ist aus, bis Sie sie einschalten, abgesichert durch die Berechtigung „Mit KI handeln“, mit einem Agent-Center-Protokoll jeder Anfrage — nur Metadaten, also ohne Mitarbeiterdaten.",
                "La IA está desactivada hasta que la active, protegida por el permiso «Actuar con IA», con un registro del Centro de Agentes de cada solicitud — solo metadatos, sin datos de empleados.",
                "L'IA è disattivata finché non la attivi, protetta dall'autorizzazione «Agire con l'IA», con un registro dell'Agent Center per ogni richiesta — solo metadati, quindi senza dati dei dipendenti.",
                "AI staat uit tot u het inschakelt, beveiligd door de machtiging 'Handelen met AI', met een Agent Center-logboek van elke aanvraag — alleen metadata, dus zonder medewerkersgegevens."),
            # ---- Pricing ----
            "HR Suite pricing": _t("Tarifs HR Suite", "HR Suite Preise", "Precios de HR Suite", "Prezzi di HR Suite", "HR Suite-prijzen"),
            "Per seat / month": _t("Par poste / mois", "Pro Platz / Monat", "Por puesto / mes", "Per postazione / mese", "Per gebruiker / maand"),
            "<span>Starter</span>": _t("<span>Starter</span>", "<span>Starter</span>", "<span>Starter</span>", "<span>Starter</span>", "<span>Starter</span>"),
            "Core HR on the Starter plan. 14-day free trial, no card required.": _t(
                "RH de base sur le forfait Starter. Essai gratuit de 14 jours, sans carte bancaire.",
                "Kern-HR im Starter-Tarif. 14 Tage kostenlos testen, keine Karte erforderlich.",
                "RR. HH. esenciales en el plan Starter. Prueba gratuita de 14 días, sin tarjeta.",
                "HR di base nel piano Starter. Prova gratuita di 14 giorni, senza carta.",
                "Kern-HR op het Starter-abonnement. 14 dagen gratis proberen, geen kaart nodig."),
            "Included": _t("Inclus", "Enthalten", "Incluido", "Incluso", "Inbegrepen"),
            "On the Starter plan": _t("Sur le forfait Starter", "Im Starter-Tarif", "En el plan Starter", "Nel piano Starter", "Op het Starter-abonnement"),
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
            "<h4>Onboarding</h4>": _t("<h4>Intégration</h4>", "<h4>Onboarding</h4>", "<h4>Incorporación</h4>", "<h4>Onboarding</h4>", "<h4>Onboarding</h4>"),
            "Turn a new hire into a set-up teammate with checklists, e-signatures, and automatic account provisioning.": _t(
                "Transformez une nouvelle recrue en coéquipier opérationnel grâce aux listes de contrôle, aux signatures électroniques et à la création automatique des comptes.",
                "Machen Sie aus einer neuen Einstellung ein startklares Teammitglied — mit Checklisten, elektronischen Signaturen und automatischer Kontoeinrichtung.",
                "Convierta a un nuevo empleado en un compañero listo para trabajar con listas de verificación, firmas electrónicas y aprovisionamiento automático de cuentas.",
                "Trasforma un nuovo assunto in un collega pronto a partire con checklist, firme elettroniche e creazione automatica degli account.",
                "Maak van een nieuwe medewerker een startklare collega met checklists, e-handtekeningen en automatische accountaanmaak."),
            "<h4>Payroll</h4>": _t("<h4>Paie</h4>", "<h4>Gehaltsabrechnung</h4>", "<h4>Nóminas</h4>", "<h4>Buste paga</h4>", "<h4>Loonadministratie</h4>"),
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
            "<h4>Managers</h4>": _t("<h4>Managers</h4>", "<h4>Führungskräfte</h4>", "<h4>Responsables</h4>", "<h4>Manager</h4>", "<h4>Managers</h4>"),
            "Approve leave, review timesheets, and run performance check-ins without leaving your workflow.": _t(
                "Approuvez les congés, vérifiez les feuilles de temps et menez les points de performance sans quitter votre flux de travail.",
                "Genehmigen Sie Abwesenheiten, prüfen Sie Zeiterfassungen und führen Sie Leistungsgespräche, ohne Ihren Arbeitsablauf zu verlassen.",
                "Apruebe ausencias, revise hojas de horas y realice revisiones de desempeño sin salir de su flujo de trabajo.",
                "Approva le ferie, controlla i fogli presenze e conduci i check-in sulla performance senza uscire dal tuo flusso di lavoro.",
                "Keur verlof goed, controleer urenstaten en houd prestatiegesprekken zonder uw workflow te verlaten."),
            "<h4>Employees</h4>": _t("<h4>Employés</h4>", "<h4>Mitarbeitende</h4>", "<h4>Empleados</h4>", "<h4>Dipendenti</h4>", "<h4>Medewerkers</h4>"),
            "Self-service for payslips, time off, and personal details — answers without an email to HR.": _t(
                "Libre-service pour les bulletins de paie, les congés et les informations personnelles — des réponses sans écrire à la RH.",
                "Self-Service für Gehaltsabrechnungen, Abwesenheiten und persönliche Daten — Antworten ohne E-Mail an die HR.",
                "Autoservicio para recibos de nómina, ausencias y datos personales — respuestas sin escribir a RR. HH.",
                "Self-service per cedolini, ferie e dati personali — risposte senza scrivere all'HR.",
                "Selfservice voor loonstroken, verlof en persoonlijke gegevens — antwoorden zonder een e-mail naar HR."),
            # ---- Compliance / regions ----
            "04 · Compliance": _t("04 · Conformité", "04 · Compliance", "04 · Cumplimiento", "04 · Conformità", "04 · Compliance"),
            "Built for global payroll": _t("Conçu pour la paie mondiale", "Für die weltweite Gehaltsabrechnung gebaut", "Diseñado para la nómina global", "Costruito per le buste paga globali", "Gebouwd voor wereldwijde loonadministratie"),
            "Payroll, statutory year-end, and compliance tuned to each market — across the Gulf, the UK, the US and Europe. Pick yours.": _t(
                "Paie, clôture annuelle légale et conformité adaptées à chaque marché — dans le Golfe, au Royaume-Uni, aux États-Unis et en Europe. Choisissez le vôtre.",
                "Gehaltsabrechnung, gesetzlicher Jahresabschluss und Compliance, abgestimmt auf jeden Markt — in der Golfregion, im Vereinigten Königreich, in den USA und in Europa. Wählen Sie Ihren.",
                "Nóminas, cierre anual legal y cumplimiento ajustados a cada mercado — en el Golfo, el Reino Unido, EE. UU. y Europa. Elija el suyo.",
                "Buste paga, chiusura annuale di legge e conformità su misura per ogni mercato — nel Golfo, nel Regno Unito, negli Stati Uniti e in Europa. Scegli il tuo.",
                "Loonadministratie, wettelijke jaarafsluiting en compliance afgestemd op elke markt — in de Golfregio, het VK, de VS en Europa. Kies de uwe."),
            "North America →": _t("Amérique du Nord →", "Nordamerika →", "Norteamérica →", "Nord America →", "Noord-Amerika →"),
            "United States · Canada": _t("États-Unis · Canada", "USA · Kanada", "Estados Unidos · Canadá", "Stati Uniti · Canada", "Verenigde Staten · Canada"),
            "Europe →": _t("Europe →", "Europa →", "Europa →", "Europa →", "Europa →"),
            "UK · SEPA · GDPR": _t("UK · SEPA · RGPD", "UK · SEPA · DSGVO", "UK · SEPA · RGPD", "UK · SEPA · GDPR", "UK · SEPA · AVG"),
            "The GCC →": _t("Le GCC →", "Der GCC →", "El GCC →", "Il GCC →", "De GCC →"),
            "Saudi · UAE · Qatar · Kuwait · Bahrain · Oman": _t(
                "Arabie saoudite · EAU · Qatar · Koweït · Bahreïn · Oman",
                "Saudi-Arabien · VAE · Katar · Kuwait · Bahrain · Oman",
                "Arabia Saudí · EAU · Catar · Kuwait · Baréin · Omán",
                "Arabia Saudita · EAU · Qatar · Kuwait · Bahrein · Oman",
                "Saoedi-Arabië · VAE · Qatar · Koeweit · Bahrein · Oman"),
            "Middle East →": _t("Moyen-Orient →", "Naher Osten →", "Oriente Medio →", "Medio Oriente →", "Midden-Oosten →"),
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
            "More apps →": _t("Plus d'applications →", "Weitere Apps →", "Más apps →", "Altre app →", "Meer apps →"),
            "Inventory, CRM &amp; more": _t("Inventaire, CRM &amp; plus", "Lagerverwaltung, CRM &amp; mehr", "Inventario, CRM &amp; más", "Inventario, CRM &amp; altro", "Voorraad, CRM &amp; meer"),
            # ---- CTA ----
            "Run your people ops<br />on one grid.": _t(
                "Pilotez votre gestion du personnel<br />sur une seule grille.",
                "Führen Sie Ihr Personalmanagement<br />auf einem Grid.",
                "Gestione sus operaciones de personas<br />en una sola cuadrícula.",
                "Gestisci le tue operazioni sul personale<br />su un'unica griglia.",
                "Run uw personeelsoperatie<br />op één grid."),
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
            "Explore the FulcrumGrid family of purpose-built business apps — HR Suite, Command Center, Collection, and more, all on one grid.": _t(
                "Découvrez la famille FulcrumGrid d'applications métier sur mesure — HR Suite, Command Center, Collection et plus, le tout sur une seule grille.",
                "Entdecken Sie die FulcrumGrid-Familie zweckgebauter Business-Apps — HR Suite, Command Center, Collection und mehr, alle auf einem Grid.",
                "Explore la familia FulcrumGrid de aplicaciones de negocio a medida — HR Suite, Command Center, Collection y más, todo en una sola cuadrícula.",
                "Esplora la famiglia FulcrumGrid di applicazioni aziendali su misura — HR Suite, Command Center, Collection e altro, tutto su un'unica griglia.",
                "Ontdek de FulcrumGrid-familie van doelgerichte bedrijfsapps — HR Suite, Command Center, Collection en meer, allemaal op één grid."),
            # ---- Hero ----
            "The grid of apps": _t("La grille d'applications", "Das Grid der Apps", "La cuadrícula de apps", "La griglia di app", "Het grid van apps"),
            "Purpose-built apps for every operation.": _t(
                "Des applications sur mesure pour chaque opération.",
                "Zweckgebaute Apps für jeden Betrieb.",
                "Aplicaciones a medida para cada operación.",
                "App su misura per ogni operazione.",
                "Doelgerichte apps voor elke operatie."),
            "Three apps live today, each solving a real problem on its own — all on one grid.": _t(
                "Trois applications sont déjà disponibles, chacune résolvant à elle seule un vrai problème — le tout sur une seule grille.",
                "Drei Apps sind heute schon live, jede löst für sich ein echtes Problem — alle auf einem Grid.",
                "Tres apps ya disponibles hoy, cada una resolviendo por sí sola un problema real — todo en una sola cuadrícula.",
                "Tre app già disponibili oggi, ognuna risolve da sola un problema reale — tutto su un'unica griglia.",
                "Vandaag zijn er drie apps live, elk lost op zichzelf een echt probleem op — allemaal op één grid."),
            "Each FulcrumGrid app solves a real problem on its own — and they all run on one grid, with the same clean experience. Start with one today and add the rest as you grow.": _t(
                "Chaque application FulcrumGrid résout à elle seule un vrai problème — et elles fonctionnent toutes sur une seule grille, avec la même expérience épurée. Commencez par une aujourd'hui et ajoutez les autres à mesure que vous grandissez.",
                "Jede FulcrumGrid-App löst für sich ein echtes Problem — und alle laufen auf einem Grid, mit demselben klaren Erlebnis. Starten Sie heute mit einer und fügen Sie die übrigen hinzu, wenn Sie wachsen.",
                "Cada app de FulcrumGrid resuelve por sí sola un problema real — y todas funcionan en una sola cuadrícula, con la misma experiencia limpia. Empiece hoy con una y añada el resto a medida que crece.",
                "Ogni app FulcrumGrid risolve da sola un problema reale — e girano tutte su un'unica griglia, con la stessa esperienza pulita. Inizia oggi con una e aggiungi le altre man mano che cresci.",
                "Elke FulcrumGrid-app lost op zichzelf een echt probleem op — en ze draaien allemaal op één grid, met dezelfde heldere ervaring. Begin vandaag met één en voeg de rest toe naarmate u groeit."),
            # ---- Product cards ----
            "Available now": _t("Disponible maintenant", "Jetzt verfügbar", "Ya disponible", "Ora disponibile", "Nu beschikbaar"),
            "Receivables": _t("Créances", "Forderungen", "Cobros", "Crediti", "Vorderingen"),
            "People": _t("Personnel", "Personal", "Personas", "Personale", "Personeel"),
            "Operations": _t("Opérations", "Betrieb", "Operaciones", "Operazioni", "Operaties"),
            "Explore →": _t("Découvrir →", "Entdecken →", "Explorar →", "Esplora →", "Ontdekken →"),
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
            "Close, TMS, Voice and Assure are coming soon — with CRM, Agents, Real Estate and Workshop on the roadmap. Built on the same grid, so they plug straight in.": _t(
                "Close, TMS, Voice et Assure arrivent bientôt — avec CRM, Agents, Immobilier et Atelier sur la feuille de route. Conçus sur la même grille, ils s'intègrent directement.",
                "Close, TMS, Voice und Assure kommen bald — mit CRM, Agenten, Immobilien und Werkstatt auf der Roadmap. Auf demselben Grid gebaut, fügen sie sich direkt ein.",
                "Close, TMS, Voice y Assure llegan pronto — con CRM, Agentes, Inmobiliaria y Taller en la hoja de ruta. Creados en la misma cuadrícula, se integran directamente.",
                "Close, TMS, Voice e Assure sono in arrivo — con CRM, Agenti, Immobiliare e Officina nella roadmap. Costruiti sulla stessa griglia, si integrano subito.",
                "Close, TMS, Voice en Assure komen binnenkort — met CRM, Agents, Vastgoed en Werkplaats op de roadmap. Gebouwd op hetzelfde grid, zodat ze direct aansluiten."),
            "Close, TMS, Voice &amp; Assure — coming soon": _t(
                "Close, TMS, Voice &amp; Assure — bientôt",
                "Close, TMS, Voice &amp; Assure — demnächst",
                "Close, TMS, Voice &amp; Assure — próximamente",
                "Close, TMS, Voice &amp; Assure — in arrivo",
                "Close, TMS, Voice &amp; Assure — binnenkort"),
            "CRM &amp; Agents — on the roadmap": _t(
                "CRM &amp; Agents — sur la feuille de route",
                "CRM &amp; Agenten — auf der Roadmap",
                "CRM &amp; Agentes — en la hoja de ruta",
                "CRM &amp; Agenti — nella roadmap",
                "CRM &amp; Agents — op de roadmap"),
            "Real Estate &amp; Workshop — on the roadmap": _t(
                "Immobilier &amp; Atelier — sur la feuille de route",
                "Immobilien &amp; Werkstatt — auf der Roadmap",
                "Inmobiliaria &amp; Taller — en la hoja de ruta",
                "Immobiliare &amp; Officina — nella roadmap",
                "Vastgoed &amp; Werkplaats — op de roadmap"),
            '<span class="tag tag-outline">Agents</span>': _t(
                '<span class="tag tag-outline">Agents</span>',
                '<span class="tag tag-outline">Agenten</span>',
                '<span class="tag tag-outline">Agentes</span>',
                '<span class="tag tag-outline">Agenti</span>',
                '<span class="tag tag-outline">Agents</span>'),
            '<span class="tag tag-outline">Real Estate</span>': _t(
                '<span class="tag tag-outline">Immobilier</span>',
                '<span class="tag tag-outline">Immobilien</span>',
                '<span class="tag tag-outline">Inmobiliaria</span>',
                '<span class="tag tag-outline">Immobiliare</span>',
                '<span class="tag tag-outline">Vastgoed</span>'),
            '<span class="tag tag-outline">Workshop</span>': _t(
                '<span class="tag tag-outline">Atelier</span>',
                '<span class="tag tag-outline">Werkstatt</span>',
                '<span class="tag tag-outline">Taller</span>',
                '<span class="tag tag-outline">Officina</span>',
                '<span class="tag tag-outline">Werkplaats</span>'),
            # ---- Custom apps CTA ----
            "Built for you": _t("Conçu pour vous", "Für Sie entwickelt", "Diseñado para usted", "Pensato per te", "Voor u gebouwd"),
            "Don't see your exact workflow?": _t(
                "Vous ne voyez pas votre flux de travail exact ?",
                "Ihr genauer Workflow ist nicht dabei?",
                "¿No encuentra su flujo de trabajo exacto?",
                "Non trovi il tuo flusso di lavoro esatto?",
                "Ziet u uw exacte workflow niet?"),
            "Beyond our ready-made apps, we build customized business apps tailored to your specific use case — on the same secure, auditable foundation as the rest of the grid.": _t(
                "Au-delà de nos applications prêtes à l'emploi, nous concevons des applications métier personnalisées, adaptées à votre cas d'usage précis — sur le même socle sécurisé et auditable que le reste de la grille.",
                "Über unsere fertigen Apps hinaus entwickeln wir maßgeschneiderte Business-Apps für Ihren konkreten Anwendungsfall — auf demselben sicheren, prüfbaren Fundament wie der Rest des Grids.",
                "Más allá de nuestras apps listas para usar, creamos aplicaciones de negocio personalizadas y adaptadas a su caso de uso concreto — sobre la misma base segura y auditable que el resto de la cuadrícula.",
                "Oltre alle nostre app pronte all'uso, sviluppiamo applicazioni aziendali personalizzate su misura per il tuo caso d'uso specifico — sulle stesse fondamenta sicure e verificabili del resto della griglia.",
                "Naast onze kant-en-klare apps bouwen we op maat gemaakte bedrijfsapps, afgestemd op uw specifieke use case — op hetzelfde veilige, controleerbare fundament als de rest van het grid."),
            "Explore custom apps": _t("Découvrir les applications sur mesure", "Individuelle Apps entdecken", "Explorar apps a medida", "Esplora le app su misura", "Ontdek apps op maat"),
            # ---- Ready CTA ----
            "Ready to run<br />on one grid?": _t(
                "Prêt à tout piloter<br />sur une seule grille ?",
                "Bereit, alles auf<br />einem Grid zu betreiben?",
                "¿Listo para operar<br />en una sola cuadrícula?",
                "Pronto a lavorare<br />su un'unica griglia?",
                "Klaar om op<br />één grid te werken?"),
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
            "More FulcrumGrid apps in active development — Close, TMS, Voice and Assure coming soon, with CRM, Agents, Real Estate and Workshop on the roadmap — built on the same grid. Get early access.": _t(
                "D'autres applications FulcrumGrid en développement actif — Close, TMS, Voice et Assure bientôt, avec CRM, Agents, Immobilier et Atelier sur la feuille de route — conçues sur la même grille. Obtenez un accès anticipé.",
                "Weitere FulcrumGrid-Apps in aktiver Entwicklung — Close, TMS, Voice und Assure demnächst, mit CRM, Agenten, Immobilien und Werkstatt auf der Roadmap — auf demselben Grid gebaut. Sichern Sie sich frühen Zugang.",
                "Más aplicaciones de FulcrumGrid en desarrollo activo — Close, TMS, Voice y Assure próximamente, con CRM, Agentes, Inmobiliaria y Taller en la hoja de ruta — creadas en la misma cuadrícula. Consiga acceso anticipado.",
                "Altre app FulcrumGrid in fase di sviluppo attivo — Close, TMS, Voice e Assure in arrivo, con CRM, Agenti, Immobiliare e Officina nella roadmap — costruite sulla stessa griglia. Ottieni l'accesso anticipato.",
                "Meer FulcrumGrid-apps in actieve ontwikkeling — Close, TMS, Voice en Assure binnenkort, met CRM, Agents, Vastgoed en Werkplaats op de roadmap — gebouwd op hetzelfde grid. Krijg vroege toegang."),
            "Close, TMS, Voice and Assure — coming to the grid.": _t(
                "Close, TMS, Voice et Assure — bientôt sur la grille.",
                "Close, TMS, Voice und Assure — bald im Grid.",
                "Close, TMS, Voice y Assure — próximamente en la cuadrícula.",
                "Close, TMS, Voice e Assure — presto sulla griglia.",
                "Close, TMS, Voice en Assure — binnenkort op het grid."),
            # ---- Hero ----
            "Roadmap": _t("Feuille de route", "Roadmap", "Hoja de ruta", "Roadmap", "Roadmap"),
            "In development": _t("En développement", "In Entwicklung", "En desarrollo", "In sviluppo", "In ontwikkeling"),
            "More apps, coming to the grid": _t(
                "D'autres applications, bientôt sur la grille",
                "Weitere Apps, bald im Grid",
                "Más apps, próximamente en la cuadrícula",
                "Altre app, presto sulla griglia",
                "Meer apps, binnenkort op het grid"),
            "New apps are in active development — each built to the same standard as the apps you already know. Get early access as they land.": _t(
                "De nouvelles applications sont en développement actif — chacune conçue selon le même standard que les applications que vous connaissez déjà. Obtenez un accès anticipé dès leur arrivée.",
                "Neue Apps sind in aktiver Entwicklung — jede nach demselben Standard gebaut wie die Apps, die Sie bereits kennen. Sichern Sie sich frühen Zugang, sobald sie erscheinen.",
                "Hay nuevas apps en desarrollo activo — cada una creada con el mismo estándar que las apps que ya conoce. Consiga acceso anticipado en cuanto lleguen.",
                "Nuove app sono in fase di sviluppo attivo — ognuna costruita secondo lo stesso standard delle app che già conosci. Ottieni l'accesso anticipato non appena arrivano.",
                "Er zijn nieuwe apps in actieve ontwikkeling — elk gebouwd volgens dezelfde standaard als de apps die u al kent. Krijg vroege toegang zodra ze verschijnen."),
            "Get early access": _t("Obtenir un accès anticipé", "Frühen Zugang sichern", "Conseguir acceso anticipado", "Ottieni l'accesso anticipato", "Vroege toegang krijgen"),
            "Available apps": _t("Applications disponibles", "Verfügbare Apps", "Apps disponibles", "App disponibili", "Beschikbare apps"),
            "Explore available apps": _t("Découvrir les applications disponibles", "Verfügbare Apps entdecken", "Explorar las apps disponibles", "Esplora le app disponibili", "Ontdek de beschikbare apps"),
            # ---- 01 · Coming soon ----
            "On the roadmap": _t("Sur la feuille de route", "Auf der Roadmap", "En la hoja de ruta", "Nella roadmap", "Op de roadmap"),
            "Coming soon to the grid.": _t(
                "Bientôt sur la grille.",
                "Bald im Grid.",
                "Próximamente en la cuadrícula.",
                "Presto sulla griglia.",
                "Binnenkort op het grid."),
            "Next off the line — each built to the same standard as the apps already on the grid.": _t(
                "Les prochaines de la série — chacune conçue selon le même standard que les applications déjà sur la grille.",
                "Als Nächstes vom Band — jede nach demselben Standard gebaut wie die Apps, die bereits im Grid sind.",
                "Las siguientes de la serie — cada una creada con el mismo estándar que las apps que ya están en la cuadrícula.",
                "Le prossime della serie — ognuna costruita secondo lo stesso standard delle app già presenti sulla griglia.",
                "De volgende van de lijn — elk gebouwd volgens dezelfde standaard als de apps die al op het grid staan."),
            "A focused deal-closing workspace — quotes, approvals and e-signatures, so deals don't stall at the finish line.": _t(
                "Un espace de travail dédié à la conclusion des affaires — devis, approbations et signatures électroniques, pour que les affaires ne calent pas sur la ligne d'arrivée.",
                "Ein fokussierter Arbeitsbereich für den Geschäftsabschluss — Angebote, Genehmigungen und E-Signaturen, damit Deals auf der Zielgeraden nicht ins Stocken geraten.",
                "Un espacio de trabajo centrado en cerrar acuerdos — presupuestos, aprobaciones y firmas electrónicas, para que los tratos no se atasquen en la meta.",
                "Uno spazio di lavoro dedicato alla chiusura delle trattative — preventivi, approvazioni e firme elettroniche, perché gli affari non si blocchino sul traguardo.",
                "Een gerichte werkruimte om deals te sluiten — offertes, goedkeuringen en e-handtekeningen, zodat deals niet vastlopen op de finish."),
            "Transport management — plan and dispatch routes, track shipments and reconcile freight, all in one place.": _t(
                "Gestion du transport — planifiez et affectez les tournées, suivez les expéditions et rapprochez les frais de fret, le tout au même endroit.",
                "Transportmanagement — planen und disponieren Sie Routen, verfolgen Sie Sendungen und gleichen Sie Frachtkosten ab, alles an einem Ort.",
                "Gestión del transporte — planifique y asigne rutas, rastree envíos y concilie fletes, todo en un solo lugar.",
                "Gestione dei trasporti — pianifica e assegna le rotte, traccia le spedizioni e riconcilia i noli, tutto in un unico posto.",
                "Transportbeheer — plan en verdeel routes, volg zendingen en verreken vracht, allemaal op één plek."),
            "Business voice — calls, call logging and IVR tied to your records, so every conversation stays on file.": _t(
                "Téléphonie d'entreprise — appels, journalisation des appels et SVI liés à vos dossiers, pour que chaque conversation reste archivée.",
                "Geschäftstelefonie — Anrufe, Anrufprotokollierung und IVR, verknüpft mit Ihren Datensätzen, damit jedes Gespräch dokumentiert bleibt.",
                "Telefonía empresarial — llamadas, registro de llamadas e IVR vinculados a sus registros, para que cada conversación quede archivada.",
                "Telefonia aziendale — chiamate, registrazione delle chiamate e IVR collegati ai tuoi archivi, così ogni conversazione resta agli atti.",
                "Zakelijke telefonie — gesprekken, gesprekslogboeken en IVR gekoppeld aan uw gegevens, zodat elk gesprek bewaard blijft."),
            "Quality and compliance assurance — inspections, checklists and corrective actions, tracked end to end.": _t(
                "Assurance qualité et conformité — inspections, listes de contrôle et actions correctives, suivies de bout en bout.",
                "Qualitäts- und Compliance-Sicherung — Inspektionen, Checklisten und Korrekturmaßnahmen, durchgängig nachverfolgt.",
                "Garantía de calidad y cumplimiento — inspecciones, listas de verificación y acciones correctivas, con seguimiento de principio a fin.",
                "Garanzia di qualità e conformità — ispezioni, checklist e azioni correttive, tracciate dall'inizio alla fine.",
                "Kwaliteits- en nalevingsborging — inspecties, checklists en corrigerende maatregelen, van begin tot eind gevolgd."),
            # ---- 02 · On the roadmap ----
            "Further out on the roadmap.": _t(
                "Plus loin sur la feuille de route.",
                "Weiter draußen auf der Roadmap.",
                "Más adelante en la hoja de ruta.",
                "Più avanti nella roadmap.",
                "Verderop op de roadmap."),
            "Planned for the grid — shaping up now, and on the way.": _t(
                "Prévues pour la grille — en préparation, et en chemin.",
                "Für das Grid geplant — nehmen Gestalt an und sind unterwegs.",
                "Planeadas para la cuadrícula — tomando forma ahora, y en camino.",
                "Previste per la griglia — in via di definizione, e in arrivo.",
                "Gepland voor het grid — krijgen nu vorm en zijn onderweg."),
            "Manage leads, deals, and customer relationships from first touch to closed won.": _t(
                "Gérez les prospects, les affaires et les relations clients, du premier contact à la conclusion.",
                "Verwalten Sie Leads, Deals und Kundenbeziehungen vom ersten Kontakt bis zum Abschluss.",
                "Gestione oportunidades, negociaciones y relaciones con clientes desde el primer contacto hasta el cierre.",
                "Gestisci lead, trattative e relazioni con i clienti dal primo contatto alla chiusura.",
                "Beheer leads, deals en klantrelaties van eerste contact tot gesloten deal."),
            "<h4>Agents</h4>": _t("<h4>Agents</h4>", "<h4>Agenten</h4>", "<h4>Agentes</h4>", "<h4>Agenti</h4>", "<h4>Agents</h4>"),
            "A workspace for agents and field teams — assignments, pipelines and commissions in one view.": _t(
                "Un espace de travail pour les agents et les équipes terrain — affectations, pipelines et commissions dans une seule vue.",
                "Ein Arbeitsbereich für Agenten und Außendienstteams — Zuweisungen, Pipelines und Provisionen in einer Ansicht.",
                "Un espacio de trabajo para agentes y equipos de campo — asignaciones, pipelines y comisiones en una sola vista.",
                "Uno spazio di lavoro per agenti e team sul campo — assegnazioni, pipeline e commissioni in un'unica vista.",
                "Een werkruimte voor agents en buitendienstteams — toewijzingen, pipelines en commissies in één overzicht."),
            "<h4>Real Estate</h4>": _t("<h4>Immobilier</h4>", "<h4>Immobilien</h4>", "<h4>Inmobiliaria</h4>", "<h4>Immobiliare</h4>", "<h4>Vastgoed</h4>"),
            "Properties, listings, leases and tenants — the operations of real estate on one grid.": _t(
                "Biens, annonces, baux et locataires — les opérations de l'immobilier sur une seule grille.",
                "Immobilien, Angebote, Mietverträge und Mieter — der Immobilienbetrieb auf einem Grid.",
                "Propiedades, anuncios, arrendamientos e inquilinos — las operaciones inmobiliarias en una sola cuadrícula.",
                "Immobili, annunci, contratti di locazione e inquilini — le operazioni immobiliari su un'unica griglia.",
                "Panden, advertenties, huurcontracten en huurders — de vastgoedoperatie op één grid."),
            "<h4>Workshop</h4>": _t("<h4>Atelier</h4>", "<h4>Werkstatt</h4>", "<h4>Taller</h4>", "<h4>Officina</h4>", "<h4>Werkplaats</h4>"),
            "Run a workshop or service center — jobs, parts, technicians and invoicing, start to finish.": _t(
                "Gérez un atelier ou un centre de service — interventions, pièces, techniciens et facturation, du début à la fin.",
                "Betreiben Sie eine Werkstatt oder ein Servicecenter — Aufträge, Teile, Techniker und Rechnungsstellung, von Anfang bis Ende.",
                "Gestione un taller o centro de servicio — trabajos, piezas, técnicos y facturación, de principio a fin.",
                "Gestisci un'officina o un centro assistenza — interventi, ricambi, tecnici e fatturazione, dall'inizio alla fine.",
                "Beheer een werkplaats of servicecentrum — opdrachten, onderdelen, technici en facturatie, van begin tot eind."),
            # ---- Notify CTA ----
            "Be first to know": _t("Soyez informé en premier", "Erfahren Sie es als Erste", "Sea el primero en saberlo", "Sii il primo a saperlo", "Wees als eerste op de hoogte"),
            "Tell us what your team needs and we'll let you know the moment these apps go live.": _t(
                "Dites-nous ce dont votre équipe a besoin et nous vous préviendrons dès que ces applications seront disponibles.",
                "Sagen Sie uns, was Ihr Team braucht, und wir informieren Sie, sobald diese Apps live gehen.",
                "Cuéntenos qué necesita su equipo y le avisaremos en cuanto estas apps estén disponibles.",
                "Dicci di cosa ha bisogno il tuo team e ti avviseremo appena queste app saranno disponibili.",
                "Vertel ons wat uw team nodig heeft en we laten het u weten zodra deze apps live gaan."),
            "Or email us at": _t("Ou écrivez-nous à", "Oder schreiben Sie uns an", "O escríbanos a", "Oppure scrivici a", "Of mail ons op"),
        },
    },
}
