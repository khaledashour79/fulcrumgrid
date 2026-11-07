# -*- coding: utf-8 -*-
"""Per-page translations for the HR Time & Cost Savings Calculator (/calculator/).

Keys are EXACT English substrings of the EN source HTML (entities, curly
quotes/apostrophes, em-dash —, minus −, ×, ÷ and middot · preserved). Brand
and code labels kept English on every locale (FulcrumGrid, HR Suite, SAR,
Iqama, AI/IA/KI, CV). The calculator's dynamic result strings (group names,
units, warnings) live in assets/js/calculator.js, keyed by <html lang>.
Common chrome lives in loc_catalog.COMMON.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {
    '/calculator/': {
        'src': 'calculator/index.html',
        't': {
            # ---- Head ----
            "HR Time &amp; Cost Savings Calculator | FulcrumGrid": _t(
                "Calculateur de temps et de coûts RH | FulcrumGrid",
                "HR-Zeit- und Kostenrechner | FulcrumGrid",
                "Calculadora de tiempo y costes de RR. HH. | FulcrumGrid",
                "Calcolatore di tempo e costi HR | FulcrumGrid",
                "HR-tijd- en kostencalculator | FulcrumGrid"),
            "Estimate the administrative hours your HR team could reclaim with FulcrumGrid. Answer five quick questions and adjust the assumptions — an illustrative, transparent estimate.": _t(
                "Estimez les heures administratives que votre équipe RH pourrait récupérer avec FulcrumGrid. Répondez à cinq questions rapides et ajustez les hypothèses — une estimation illustrative et transparente.",
                "Schätzen Sie die administrativen Stunden, die Ihr HR-Team mit FulcrumGrid zurückgewinnen könnte. Beantworten Sie fünf kurze Fragen und passen Sie die Annahmen an — eine illustrative, transparente Schätzung.",
                "Estime las horas administrativas que su equipo de RR. HH. podría recuperar con FulcrumGrid. Responda cinco preguntas rápidas y ajuste los supuestos — una estimación ilustrativa y transparente.",
                "Stima le ore amministrative che il tuo team HR potrebbe recuperare con FulcrumGrid. Rispondi a cinque domande veloci e modifica le ipotesi — una stima illustrativa e trasparente.",
                "Schat de administratieve uren die uw HR-team met FulcrumGrid kan terugwinnen. Beantwoord vijf korte vragen en pas de aannames aan — een illustratieve, transparante schatting."),
            "Estimate the administrative hours your HR team could reclaim with FulcrumGrid — an illustrative, transparent, adjustable estimate.": _t(
                "Estimez les heures administratives que votre équipe RH pourrait récupérer avec FulcrumGrid — une estimation illustrative, transparente et ajustable.",
                "Schätzen Sie die administrativen Stunden, die Ihr HR-Team mit FulcrumGrid zurückgewinnen könnte — eine illustrative, transparente, anpassbare Schätzung.",
                "Estime las horas administrativas que su equipo de RR. HH. podría recuperar con FulcrumGrid — una estimación ilustrativa, transparente y ajustable.",
                "Stima le ore amministrative che il tuo team HR potrebbe recuperare con FulcrumGrid — una stima illustrativa, trasparente e modificabile.",
                "Schat de administratieve uren die uw HR-team met FulcrumGrid kan terugwinnen — een illustratieve, transparante, aanpasbare schatting."),

            # ---- Hero ----
            "HR Suite · Savings calculator": _t(
                "HR Suite · Calculateur d'économies", "HR Suite · Einsparungsrechner", "HR Suite · Calculadora de ahorro",
                "HR Suite · Calcolatore di risparmio", "HR Suite · Besparingscalculator"),
            "How much time could your HR team save?": _t(
                "Combien de temps votre équipe RH pourrait-elle gagner ?", "Wie viel Zeit könnte Ihr HR-Team sparen?",
                "¿Cuánto tiempo podría ahorrar su equipo de RR. HH.?", "Quanto tempo potrebbe risparmiare il tuo team HR?",
                "Hoeveel tijd kan uw HR-team besparen?"),
            "Answer five quick questions to estimate the administrative hours your business could reclaim. Everything stays in your browser — no sign-up, no data leaves this page.": _t(
                "Répondez à cinq questions rapides pour estimer les heures administratives que votre entreprise pourrait récupérer. Tout reste dans votre navigateur — sans inscription, aucune donnée ne quitte cette page.",
                "Beantworten Sie fünf kurze Fragen, um die administrativen Stunden zu schätzen, die Ihr Unternehmen zurückgewinnen könnte. Alles bleibt in Ihrem Browser — ohne Anmeldung, keine Daten verlassen diese Seite.",
                "Responda cinco preguntas rápidas para estimar las horas administrativas que su empresa podría recuperar. Todo permanece en su navegador — sin registro, ningún dato sale de esta página.",
                "Rispondi a cinque domande veloci per stimare le ore amministrative che la tua azienda potrebbe recuperare. Tutto resta nel tuo browser — senza registrazione, nessun dato lascia questa pagina.",
                "Beantwoord vijf korte vragen om de administratieve uren te schatten die uw bedrijf kan terugwinnen. Alles blijft in uw browser — zonder aanmelding, geen gegevens verlaten deze pagina."),

            # ---- Inputs card ----
            "Your business": _t("Votre entreprise", "Ihr Unternehmen", "Su empresa", "La tua azienda", "Uw bedrijf"),
            "Enter what you know. For the activity questions, use “Not sure — use an estimate” and edit later.": _t(
                "Saisissez ce que vous savez. Pour les questions d'activité, utilisez « Pas sûr — utiliser une estimation » et modifiez plus tard.",
                "Geben Sie ein, was Sie wissen. Nutzen Sie bei den Aktivitätsfragen „Nicht sicher — Schätzung verwenden“ und bearbeiten Sie es später.",
                "Introduzca lo que sepa. Para las preguntas de actividad, use «No estoy seguro — usar una estimación» y edítelo después.",
                "Inserisci ciò che sai. Per le domande sulle attività, usa «Non sei sicuro — usa una stima» e modifica in seguito.",
                "Voer in wat u weet. Gebruik bij de activiteitsvragen 'Niet zeker — gebruik een schatting' en pas het later aan."),
            "Number of employees": _t("Nombre d'employés", "Anzahl der Mitarbeiter", "Número de empleados", "Numero di dipendenti", "Aantal werknemers"),
            "· current headcount": _t("· effectif actuel", "· aktuelle Belegschaft", "· plantilla actual", "· organico attuale", "· huidig personeelsbestand"),
            "Employees hired annually": _t("Employés recrutés par an", "Jährlich eingestellte Mitarbeiter", "Empleados contratados al año", "Dipendenti assunti all'anno", "Werknemers per jaar aangenomen"),
            "· hires / year": _t("· recrutements / an", "· Einstellungen / Jahr", "· contrataciones / año", "· assunzioni / anno", "· aanwervingen / jaar"),
            "Not sure — use an estimate": _t("Pas sûr — utiliser une estimation", "Nicht sicher — Schätzung verwenden", "No estoy seguro — usar una estimación", "Non sei sicuro — usa una stima", "Niet zeker — gebruik een schatting"),
            "Estimated": _t("Estimé", "Geschätzt", "Estimado", "Stimato", "Geschat"),
            "Average applications per vacancy": _t("Candidatures moyennes par poste", "Durchschnittliche Bewerbungen pro Stelle", "Solicitudes medias por vacante", "Candidature medie per posizione", "Gemiddeld aantal sollicitaties per vacature"),
            "· applications / vacancy": _t("· candidatures / poste", "· Bewerbungen / Stelle", "· solicitudes / vacante", "· candidature / posizione", "· sollicitaties / vacature"),
            "Iqama renewals processed annually": _t("Renouvellements d'iqama traités par an", "Jährlich bearbeitete Iqama-Erneuerungen", "Renovaciones de iqama procesadas al año", "Rinnovi dell'iqama elaborati all'anno", "Jaarlijks verwerkte iqama-verlengingen"),
            "· renewals / year": _t("· renouvellements / an", "· Erneuerungen / Jahr", "· renovaciones / año", "· rinnovi / anno", "· verlengingen / jaar"),
            "Not in Saudi Arabia? Turn": _t("Pas en Arabie saoudite ? Désactivez", "Nicht in Saudi-Arabien? Deaktivieren Sie", "¿No está en Arabia Saudí? Desactive", "Non sei in Arabia Saudita? Disattiva", "Niet in Saoedi-Arabië? Schakel"),
            "Iqama renewals": _t("Renouvellements d'iqama", "Iqama-Erneuerungen", "Renovaciones de iqama", "Rinnovi dell'iqama", "Iqama-verlengingen"),
            "off under “Features to include”.": _t("sous « Fonctionnalités à inclure ».", "unter „Einzubeziehende Funktionen“ aus.", "en «Funciones a incluir».", "in «Funzioni da includere».", "uit onder 'Functies om op te nemen'."),
            "Employee letters requested monthly": _t("Lettres d'employés demandées par mois", "Monatlich angeforderte Mitarbeiterschreiben", "Cartas de empleados solicitadas al mes", "Lettere per dipendenti richieste al mese", "Maandelijks aangevraagde werknemersbrieven"),
            "· letters / month": _t("· lettres / mois", "· Schreiben / Monat", "· cartas / mes", "· lettere / mese", "· brieven / maand"),

            # ---- Features card ----
            "Features to include": _t("Fonctionnalités à inclure", "Einzubeziehende Funktionen", "Funciones a incluir", "Funzioni da includere", "Functies om op te nemen"),
            "Already automate an activity? Turn it off, or enter your real current time under “Adjust assumptions”.": _t(
                "Vous automatisez déjà une activité ? Désactivez-la, ou saisissez votre temps réel actuel sous « Ajuster les hypothèses ».",
                "Automatisieren Sie eine Aktivität bereits? Deaktivieren Sie sie oder geben Sie Ihre tatsächliche aktuelle Zeit unter „Annahmen anpassen“ ein.",
                "¿Ya automatiza una actividad? Desactívela o introduzca su tiempo actual real en «Ajustar los supuestos».",
                "Automatizzi già un'attività? Disattivala o inserisci il tuo tempo attuale reale in «Modifica le ipotesi».",
                "Automatiseert u een activiteit al? Schakel deze uit of voer uw werkelijke huidige tijd in onder 'Aannames aanpassen'."),
            "Recruitment (CV screening &amp; interviews)": _t("Recrutement (tri des CV &amp; entretiens)", "Einstellung (CV-Screening &amp; Interviews)", "Contratación (cribado de CV &amp; entrevistas)", "Reclutamento (screening CV &amp; colloqui)", "Werving (cv-screening &amp; interviews)"),
            "Payroll preparation": _t("Préparation de la paie", "Gehaltsabrechnung", "Preparación de nóminas", "Preparazione delle buste paga", "Loonadministratie"),
            "Employee letters": _t("Lettres d'employés", "Mitarbeiterschreiben", "Cartas de empleados", "Lettere per dipendenti", "Werknemersbrieven"),
            "Attendance &amp; overtime validation": _t("Validation présence &amp; heures sup.", "Anwesenheits- &amp; Überstundenprüfung", "Validación de asistencia &amp; horas extra", "Convalida presenze &amp; straordinari", "Validatie aanwezigheid &amp; overuren"),
            "Performance reviews": _t("Évaluations de performance", "Leistungsbeurteilungen", "Evaluaciones de desempeño", "Valutazioni delle prestazioni", "Prestatiebeoordelingen"),
            "Loan &amp; advance processing": _t("Traitement des prêts &amp; avances", "Bearbeitung von Darlehen &amp; Vorschüssen", "Gestión de préstamos &amp; anticipos", "Gestione prestiti &amp; anticipi", "Verwerking van leningen &amp; voorschotten"),
            "Final settlement / EOSB": _t("Solde de tout compte / EOSB", "Endabrechnung / EOSB", "Liquidación final / EOSB", "Liquidazione finale / EOSB", "Eindafrekening / EOSB"),
            "Air-ticket entitlements": _t("Droits aux billets d'avion", "Flugticket-Ansprüche", "Derechos a billetes de avión", "Diritti ai biglietti aerei", "Vliegticketrechten"),
            "GL / ERP payroll postings": _t("Écritures de paie GL / ERP", "GL- / ERP-Lohnbuchungen", "Asientos de nómina GL / ERP", "Scritture paga GL / ERP", "GL- / ERP-loonboekingen"),

            # ---- Adjust assumptions ----
            "Adjust assumptions": _t("Ajuster les hypothèses", "Annahmen anpassen", "Ajustar los supuestos", "Modifica le ipotesi", "Aannames aanpassen"),
            "Processing times include the remaining human review. Recorded interviews replace only the initial screening step modeled here, not every hiring interview. Iqama savings concern administration, not government fees. Letter savings assume eligible templates and automation are configured.": _t(
                "Les temps de traitement incluent la revue humaine restante. Les entretiens enregistrés ne remplacent que l'étape de présélection initiale modélisée ici, pas tous les entretiens de recrutement. Les économies sur l'iqama concernent l'administration, pas les frais gouvernementaux. Les économies sur les lettres supposent que des modèles éligibles et l'automatisation sont configurés.",
                "Die Bearbeitungszeiten umfassen die verbleibende menschliche Prüfung. Aufgezeichnete Interviews ersetzen nur den hier modellierten ersten Screening-Schritt, nicht jedes Einstellungsinterview. Iqama-Einsparungen betreffen die Verwaltung, nicht die behördlichen Gebühren. Einsparungen bei Schreiben setzen voraus, dass geeignete Vorlagen und Automatisierung konfiguriert sind.",
                "Los tiempos de procesamiento incluyen la revisión humana restante. Las entrevistas grabadas solo sustituyen el paso de cribado inicial modelado aquí, no todas las entrevistas de contratación. El ahorro en iqama concierne a la administración, no a las tasas gubernamentales. El ahorro en cartas supone que hay plantillas elegibles y automatización configuradas.",
                "I tempi di elaborazione includono la revisione umana residua. I colloqui registrati sostituiscono solo la fase di screening iniziale qui modellata, non ogni colloquio di assunzione. I risparmi sull'iqama riguardano l'amministrazione, non le tasse governative. I risparmi sulle lettere presuppongono che siano configurati modelli idonei e l'automazione.",
                "De verwerkingstijden omvatten de resterende menselijke beoordeling. Opgenomen interviews vervangen alleen de hier gemodelleerde initiële screeningsstap, niet elk sollicitatiegesprek. Besparingen op iqama betreffen de administratie, niet de overheidskosten. Besparingen op brieven veronderstellen dat geschikte sjablonen en automatisering zijn geconfigureerd."),
            "Activity": _t("Activité", "Aktivität", "Actividad", "Attività", "Activiteit"),
            "Manual min.": _t("Min. manuel", "Min. manuell", "Min. manual", "Min. manuale", "Min. handmatig"),
            "With platform min.": _t("Min. avec la plateforme", "Min. mit Plattform", "Min. con la plataforma", "Min. con la piattaforma", "Min. met platform"),
            "Initial CV screening": _t("Présélection initiale des CV", "Erstes CV-Screening", "Cribado inicial de CV", "Screening iniziale dei CV", "Initiële cv-screening"),
            "Initial interview vs recorded-interview review": _t("Entretien initial vs revue d'entretien enregistré", "Erstinterview vs. Prüfung eines aufgezeichneten Interviews", "Entrevista inicial vs revisión de entrevista grabada", "Colloquio iniziale vs revisione del colloquio registrato", "Eerste interview vs. beoordeling van opgenomen interview"),
            "Payroll prep per employee / cycle": _t("Prépa paie par employé / cycle", "Gehaltsabrechnung pro Mitarbeiter / Zyklus", "Prep. nómina por empleado / ciclo", "Prep. buste paga per dipendente / ciclo", "Loonvoorbereiding per werknemer / cyclus"),
            "Iqama renewal administration": _t("Administration du renouvellement d'iqama", "Verwaltung der Iqama-Erneuerung", "Administración de la renovación de iqama", "Amministrazione del rinnovo dell'iqama", "Beheer van iqama-verlenging"),
            "Employee letter prep &amp; delivery": _t("Prépa &amp; remise des lettres d'employés", "Erstellung &amp; Zustellung von Mitarbeiterschreiben", "Prep. &amp; entrega de cartas de empleados", "Prep. &amp; consegna delle lettere per dipendenti", "Opstellen &amp; bezorgen van werknemersbrieven"),
            "Attendance &amp; overtime review per employee / month": _t("Revue présence &amp; heures sup. par employé / mois", "Anwesenheits- &amp; Überstundenprüfung pro Mitarbeiter / Monat", "Revisión de asistencia &amp; horas extra por empleado / mes", "Revisione presenze &amp; straordinari per dipendente / mese", "Controle aanwezigheid &amp; overuren per werknemer / maand"),
            "Performance review admin per employee / cycle": _t("Admin. d'évaluation par employé / cycle", "Beurteilungsadministration pro Mitarbeiter / Zyklus", "Admin. de evaluación por empleado / ciclo", "Admin. valutazione per dipendente / ciclo", "Beoordelingsadmin. per werknemer / cyclus"),
            "Loan / advance request processing": _t("Traitement des demandes de prêt / avance", "Bearbeitung von Darlehens- / Vorschussanträgen", "Gestión de solicitudes de préstamo / anticipo", "Gestione richieste di prestito / anticipo", "Verwerking van lening- / voorschotaanvragen"),
            "Final settlement / EOSB per leaver": _t("Solde de tout compte / EOSB par partant", "Endabrechnung / EOSB pro Austritt", "Liquidación final / EOSB por baja", "Liquidazione finale / EOSB per uscita", "Eindafrekening / EOSB per vertrekker"),
            "Air-ticket entitlement processing": _t("Traitement des droits aux billets d'avion", "Bearbeitung von Flugticket-Ansprüchen", "Gestión de derechos a billetes de avión", "Gestione dei diritti ai biglietti aerei", "Verwerking van vliegticketrechten"),
            "GL / ERP posting per payroll cycle": _t("Écriture GL / ERP par cycle de paie", "GL- / ERP-Buchung pro Abrechnungszyklus", "Asiento GL / ERP por ciclo de nómina", "Scrittura GL / ERP per ciclo paga", "GL- / ERP-boeking per loonronde"),
            "Initial interviews per hire": _t("Entretiens initiaux par recrutement", "Erstinterviews pro Einstellung", "Entrevistas iniciales por contratación", "Colloqui iniziali per assunzione", "Eerste interviews per aanwerving"),
            "Performance review cycles / year": _t("Cycles d'évaluation / an", "Beurteilungszyklen / Jahr", "Ciclos de evaluación / año", "Cicli di valutazione / anno", "Beoordelingscycli / jaar"),
            "Staff requesting a loan / advance per year": _t("Personnel demandant un prêt / avance par an", "Mitarbeiter mit Darlehens- / Vorschussantrag pro Jahr", "Personal que solicita préstamo / anticipo al año", "Personale che richiede prestito / anticipo all'anno", "Personeel dat per jaar een lening / voorschot aanvraagt"),
            "Annual staff turnover": _t("Rotation annuelle du personnel", "Jährliche Personalfluktuation", "Rotación anual de personal", "Turnover annuo del personale", "Jaarlijks personeelsverloop"),
            "Air-ticket cycles per expat / year": _t("Cycles de billets par expatrié / an", "Ticket-Zyklen pro Expat / Jahr", "Ciclos de billetes por expatriado / año", "Cicli di biglietti per espatriato / anno", "Ticketcycli per expat / jaar"),
            "GL / ERP postings / year": _t("Écritures GL / ERP / an", "GL- / ERP-Buchungen / Jahr", "Asientos GL / ERP / año", "Scritture GL / ERP / anno", "GL- / ERP-boekingen / jaar"),
            "· % of headcount": _t("· % de l'effectif", "· % der Belegschaft", "· % de la plantilla", "· % dell'organico", "· % van het personeelsbestand"),
            "Fully loaded staff cost": _t("Coût complet du personnel", "Vollkosten pro Mitarbeiter", "Coste total del personal", "Costo pieno del personale", "Volledig belaste personeelskosten"),
            "Productive staff hours": _t("Heures productives du personnel", "Produktive Arbeitsstunden", "Horas productivas del personal", "Ore produttive del personale", "Productieve personeelsuren"),
            "· per month": _t("· par mois", "· pro Monat", "· al mes", "· al mese", "· per maand"),
            "Expected realization / adoption factor": _t("Facteur de réalisation / adoption attendu", "Erwarteter Realisierungs-/Adoptionsfaktor", "Factor de realización / adopción esperado", "Fattore di realizzazione / adozione previsto", "Verwachte realisatie-/adoptiefactor"),
            "Fallback estimates are illustrative calculator assumptions, not industry benchmarks or verified customer results: annual hires 12% of headcount, 50 applications per vacancy, Iqama renewals 80% of headcount (one per expatriate employee per year), monthly letters 20% of headcount.": _t(
                "Les estimations par défaut sont des hypothèses illustratives du calculateur, pas des références sectorielles ni des résultats clients vérifiés : recrutements annuels 12 % de l'effectif, 50 candidatures par poste, renouvellements d'iqama 80 % de l'effectif (un par employé expatrié et par an), lettres mensuelles 20 % de l'effectif.",
                "Die Ausweich-Schätzungen sind illustrative Annahmen des Rechners, keine Branchen-Benchmarks oder verifizierte Kundenergebnisse: jährliche Einstellungen 12 % der Belegschaft, 50 Bewerbungen pro Stelle, Iqama-Erneuerungen 80 % der Belegschaft (eine pro ausländischem Mitarbeiter und Jahr), monatliche Schreiben 20 % der Belegschaft.",
                "Las estimaciones por defecto son supuestos ilustrativos de la calculadora, no referencias del sector ni resultados verificados de clientes: contrataciones anuales 12 % de la plantilla, 50 solicitudes por vacante, renovaciones de iqama 80 % de la plantilla (una por empleado expatriado al año), cartas mensuales 20 % de la plantilla.",
                "Le stime predefinite sono ipotesi illustrative del calcolatore, non benchmark di settore o risultati verificati dei clienti: assunzioni annuali 12% dell'organico, 50 candidature per posizione, rinnovi dell'iqama 80% dell'organico (uno per dipendente espatriato all'anno), lettere mensili 20% dell'organico.",
                "De terugvalschattingen zijn illustratieve aannames van de calculator, geen sectorbenchmarks of geverifieerde klantresultaten: jaarlijkse aanwervingen 12% van het personeelsbestand, 50 sollicitaties per vacature, iqama-verlengingen 80% van het personeelsbestand (één per expatmedewerker per jaar), maandelijkse brieven 20% van het personeelsbestand."),

            # ---- Optional costs ----
            "Compare against your costs (optional)": _t("Comparer à vos coûts (facultatif)", "Mit Ihren Kosten vergleichen (optional)", "Comparar con sus costes (opcional)", "Confronta con i tuoi costi (facoltativo)", "Vergelijk met uw kosten (optioneel)"),
            "Leave blank to see capacity value only. Enter your own figures to model a net benefit — nothing is shown until you do. Don’t deduct anything already bundled in the subscription twice.": _t(
                "Laissez vide pour ne voir que la valeur de capacité. Saisissez vos propres chiffres pour modéliser un bénéfice net — rien ne s'affiche tant que vous ne le faites pas. Ne déduisez pas deux fois ce qui est déjà inclus dans l'abonnement.",
                "Leer lassen, um nur den Kapazitätswert zu sehen. Geben Sie eigene Zahlen ein, um einen Nettonutzen zu modellieren — bis dahin wird nichts angezeigt. Ziehen Sie nichts doppelt ab, was bereits im Abonnement enthalten ist.",
                "Deje en blanco para ver solo el valor de capacidad. Introduzca sus propias cifras para modelar un beneficio neto — no se muestra nada hasta que lo haga. No deduzca dos veces lo que ya está incluido en la suscripción.",
                "Lascia vuoto per vedere solo il valore di capacità. Inserisci le tue cifre per modellare un beneficio netto — non viene mostrato nulla finché non lo fai. Non dedurre due volte ciò che è già incluso nell'abbonamento.",
                "Laat leeg om alleen de capaciteitswaarde te zien. Voer uw eigen cijfers in om een netto voordeel te modelleren — er wordt niets getoond totdat u dat doet. Trek niets dubbel af dat al in het abonnement zit."),
            "Annual subscription": _t("Abonnement annuel", "Jahresabonnement", "Suscripción anual", "Abbonamento annuale", "Jaarabonnement"),
            "Additional annual AI / interview / integration costs": _t("Coûts annuels supplémentaires IA / entretiens / intégration", "Zusätzliche jährliche KI- / Interview- / Integrationskosten", "Costes anuales adicionales de IA / entrevistas / integración", "Costi annuali aggiuntivi IA / colloqui / integrazione", "Extra jaarlijkse AI- / interview- / integratiekosten"),
            "One-time implementation": _t("Mise en œuvre unique", "Einmalige Einrichtung", "Implementación única", "Implementazione una tantum", "Eenmalige implementatie"),

            # ---- Results ----
            "Currency": _t("Devise", "Währung", "Moneda", "Valuta", "Valuta"),
            "Converted at indicative fixed rates for display.": _t(
                "Converti à des taux fixes indicatifs pour l'affichage.",
                "Zur Anzeige zu indikativen Festkursen umgerechnet.",
                "Convertido a tipos fijos indicativos para la visualización.",
                "Convertito a tassi fissi indicativi per la visualizzazione.",
                "Omgerekend tegen indicatieve vaste koersen voor weergave."),
            "Hours released / month": _t("Heures libérées / mois", "Freigesetzte Stunden / Monat", "Horas liberadas / mes", "Ore liberate / mese", "Vrijgekomen uren / maand"),
            "Hours released / year": _t("Heures libérées / an", "Freigesetzte Stunden / Jahr", "Horas liberadas / año", "Ore liberate / anno", "Vrijgekomen uren / jaar"),
            "Estimated annual value of staff time": _t("Valeur annuelle estimée du temps du personnel", "Geschätzter Jahreswert der Mitarbeiterzeit", "Valor anual estimado del tiempo del personal", "Valore annuo stimato del tempo del personale", "Geschatte jaarlijkse waarde van personeelstijd"),
            "/ month · potential administrative capacity released": _t("/ mois · capacité administrative potentielle libérée", "/ Monat · potenziell freigesetzte Verwaltungskapazität", "/ mes · capacidad administrativa potencial liberada", "/ mese · capacità amministrativa potenziale liberata", "/ maand · potentieel vrijgekomen administratieve capaciteit"),
            "Feature breakdown": _t("Détail par fonctionnalité", "Aufschlüsselung nach Funktion", "Desglose por función", "Dettaglio per funzione", "Uitsplitsing per functie"),
            "Contribution by feature": _t("Contribution par fonctionnalité", "Beitrag nach Funktion", "Contribución por función", "Contributo per funzione", "Bijdrage per functie"),
            "Adoption sensitivity": _t("Sensibilité à l'adoption", "Adoptions-Sensitivität", "Sensibilidad de adopción", "Sensibilità all'adozione", "Adoptiegevoeligheid"),
            "An adoption sensitivity, not a statistical confidence interval — the same inputs at 50% and 100% realization alongside your editable base case.": _t(
                "Une sensibilité à l'adoption, pas un intervalle de confiance statistique — les mêmes données à 50 % et 100 % de réalisation, à côté de votre scénario de base modifiable.",
                "Eine Adoptions-Sensitivität, kein statistisches Konfidenzintervall — dieselben Eingaben bei 50 % und 100 % Realisierung neben Ihrem bearbeitbaren Basisfall.",
                "Una sensibilidad de adopción, no un intervalo de confianza estadístico — las mismas entradas al 50 % y 100 % de realización junto a su caso base editable.",
                "Una sensibilità all'adozione, non un intervallo di confidenza statistico — gli stessi dati al 50% e 100% di realizzazione accanto al tuo caso base modificabile.",
                "Een adoptiegevoeligheid, geen statistisch betrouwbaarheidsinterval — dezelfde invoer bij 50% en 100% realisatie naast uw bewerkbare basisscenario."),
            "Book a demo to validate your estimate": _t("Réservez une démo pour valider votre estimation", "Buchen Sie eine Demo, um Ihre Schätzung zu validieren", "Reserve una demo para validar su estimación", "Prenota una demo per convalidare la tua stima", "Boek een demo om uw schatting te valideren"),
            "Illustrative estimate based on your inputs and adjustable assumptions. Staff time released does not necessarily reduce payroll expenditure. Actual results depend on your existing processes, configuration, and adoption. Subscription, usage, and implementation costs are excluded unless explicitly shown.": _t(
                "Estimation illustrative basée sur vos données et des hypothèses ajustables. Le temps de personnel libéré ne réduit pas nécessairement les dépenses de paie. Les résultats réels dépendent de vos processus existants, de votre configuration et de votre adoption. Les coûts d'abonnement, d'utilisation et de mise en œuvre sont exclus sauf indication explicite.",
                "Illustrative Schätzung auf Basis Ihrer Eingaben und anpassbarer Annahmen. Freigesetzte Mitarbeiterzeit senkt nicht zwangsläufig die Lohnkosten. Die tatsächlichen Ergebnisse hängen von Ihren bestehenden Prozessen, Ihrer Konfiguration und Ihrer Akzeptanz ab. Abonnement-, Nutzungs- und Einrichtungskosten sind ausgeschlossen, sofern nicht ausdrücklich angegeben.",
                "Estimación ilustrativa basada en sus datos y supuestos ajustables. El tiempo de personal liberado no reduce necesariamente el gasto en nóminas. Los resultados reales dependen de sus procesos existentes, su configuración y su adopción. Los costes de suscripción, uso e implementación se excluyen salvo que se muestren explícitamente.",
                "Stima illustrativa basata sui tuoi dati e su ipotesi modificabili. Il tempo del personale liberato non riduce necessariamente la spesa per le buste paga. I risultati reali dipendono dai tuoi processi esistenti, dalla configurazione e dall'adozione. I costi di abbonamento, utilizzo e implementazione sono esclusi salvo quando mostrati esplicitamente.",
                "Illustratieve schatting op basis van uw invoer en aanpasbare aannames. Vrijgekomen personeelstijd verlaagt niet noodzakelijk de loonuitgaven. De werkelijke resultaten hangen af van uw bestaande processen, configuratie en adoptie. Abonnements-, gebruiks- en implementatiekosten zijn uitgesloten, tenzij expliciet getoond."),

            # ---- How this is calculated ----
            "How this is calculated": _t("Comment c'est calculé", "So wird das berechnet", "Cómo se calcula", "Come viene calcolato", "Hoe dit wordt berekend"),
            "Annual activity volumes.": _t("Volumes d'activité annuels.", "Jährliche Aktivitätsvolumina.", "Volúmenes de actividad anuales.", "Volumi di attività annuali.", "Jaarlijkse activiteitsvolumes."),
            "CV screening = annual hires × applications per vacancy. Initial interviews = annual hires × initial interviews per hire. Payroll = headcount × 12 cycles. Iqama renewals = renewals entered. Letters = monthly requests × 12.": _t(
                "Tri des CV = recrutements annuels × candidatures par poste. Entretiens initiaux = recrutements annuels × entretiens initiaux par recrutement. Paie = effectif × 12 cycles. Renouvellements d'iqama = renouvellements saisis. Lettres = demandes mensuelles × 12.",
                "CV-Screening = jährliche Einstellungen × Bewerbungen pro Stelle. Erstinterviews = jährliche Einstellungen × Erstinterviews pro Einstellung. Gehaltsabrechnung = Belegschaft × 12 Zyklen. Iqama-Erneuerungen = eingegebene Erneuerungen. Schreiben = monatliche Anfragen × 12.",
                "Cribado de CV = contrataciones anuales × solicitudes por vacante. Entrevistas iniciales = contrataciones anuales × entrevistas iniciales por contratación. Nómina = plantilla × 12 ciclos. Renovaciones de iqama = renovaciones introducidas. Cartas = solicitudes mensuales × 12.",
                "Screening CV = assunzioni annuali × candidature per posizione. Colloqui iniziali = assunzioni annuali × colloqui iniziali per assunzione. Buste paga = organico × 12 cicli. Rinnovi dell'iqama = rinnovi inseriti. Lettere = richieste mensili × 12.",
                "Cv-screening = jaarlijkse aanwervingen × sollicitaties per vacature. Eerste interviews = jaarlijkse aanwervingen × eerste interviews per aanwerving. Loonadministratie = personeelsbestand × 12 cycli. Iqama-verlengingen = ingevoerde verlengingen. Brieven = maandelijkse aanvragen × 12."),
            "Per enabled activity.": _t("Par activité activée.", "Pro aktivierter Aktivität.", "Por actividad activada.", "Per attività attivata.", "Per ingeschakelde activiteit."),
            "Annual hours released = volume × (manual minutes − platform minutes) ÷ 60 × realization factor. Hourly staff cost = fully loaded monthly cost ÷ productive monthly hours. Annual capacity value = hours released × hourly cost. Monthly = annual ÷ 12.": _t(
                "Heures libérées par an = volume × (minutes manuelles − minutes avec la plateforme) ÷ 60 × facteur de réalisation. Coût horaire du personnel = coût mensuel complet ÷ heures productives mensuelles. Valeur de capacité annuelle = heures libérées × coût horaire. Mensuel = annuel ÷ 12.",
                "Freigesetzte Stunden pro Jahr = Volumen × (manuelle Minuten − Plattform-Minuten) ÷ 60 × Realisierungsfaktor. Stundensatz pro Mitarbeiter = monatliche Vollkosten ÷ produktive Monatsstunden. Jährlicher Kapazitätswert = freigesetzte Stunden × Stundensatz. Monatlich = jährlich ÷ 12.",
                "Horas liberadas al año = volumen × (minutos manuales − minutos con la plataforma) ÷ 60 × factor de realización. Coste por hora del personal = coste mensual total ÷ horas productivas mensuales. Valor de capacidad anual = horas liberadas × coste por hora. Mensual = anual ÷ 12.",
                "Ore liberate all'anno = volume × (minuti manuali − minuti con la piattaforma) ÷ 60 × fattore di realizzazione. Costo orario del personale = costo mensile pieno ÷ ore produttive mensili. Valore di capacità annuo = ore liberate × costo orario. Mensile = annuo ÷ 12.",
                "Vrijgekomen uren per jaar = volume × (handmatige minuten − platformminuten) ÷ 60 × realisatiefactor. Uurkosten personeel = volledige maandkosten ÷ productieve maanduren. Jaarlijkse capaciteitswaarde = vrijgekomen uren × uurkosten. Maandelijks = jaarlijks ÷ 12."),
            "CV screening and interview review are calculated separately and combined under Recruitment. We deliberately exclude blanket productivity percentages, avoided fines, hiring-quality gains, payroll-error savings, and approval-chasing or accounting work — those could overlap with the four feature groups.": _t(
                "Le tri des CV et la revue des entretiens sont calculés séparément et combinés sous Recrutement. Nous excluons délibérément les pourcentages de productivité globaux, les amendes évitées, les gains de qualité de recrutement, les économies sur les erreurs de paie et la relance des approbations ou le travail comptable — cela pourrait chevaucher les quatre groupes de fonctionnalités.",
                "CV-Screening und Interview-Prüfung werden separat berechnet und unter Einstellung zusammengefasst. Wir schließen bewusst pauschale Produktivitätsprozentsätze, vermiedene Bußgelder, Gewinne bei der Einstellungsqualität, Einsparungen bei Gehaltsabrechnungsfehlern sowie das Nachverfolgen von Genehmigungen oder Buchhaltungsarbeit aus — diese könnten sich mit den vier Funktionsgruppen überschneiden.",
                "El cribado de CV y la revisión de entrevistas se calculan por separado y se combinan en Contratación. Excluimos deliberadamente los porcentajes de productividad generales, las multas evitadas, las mejoras en la calidad de contratación, el ahorro por errores de nómina y la persecución de aprobaciones o el trabajo contable — podrían solaparse con los cuatro grupos de funciones.",
                "Lo screening dei CV e la revisione dei colloqui sono calcolati separatamente e combinati sotto Reclutamento. Escludiamo deliberatamente le percentuali di produttività generiche, le sanzioni evitate, i guadagni di qualità delle assunzioni, i risparmi sugli errori di busta paga e il sollecito delle approvazioni o il lavoro contabile — potrebbero sovrapporsi ai quattro gruppi di funzioni.",
                "Cv-screening en interviewbeoordeling worden apart berekend en samengevoegd onder Werving. We sluiten bewust algemene productiviteitspercentages, vermeden boetes, winst in wervingskwaliteit, besparingen op loonfouten en het najagen van goedkeuringen of boekhoudwerk uit — die zouden kunnen overlappen met de vier functiegroepen."),
        }
    }
}
