# -*- coding: utf-8 -*-
"""Per-page translations for the HR blog articles.

Keys are EXACT English substrings of the EN source HTML (entities such as
&amp;, &divide;, &times; and glyphs such as the em dash — preserved exactly).
Brand/product names (FulcrumGrid, Command Center, Collection, HR Suite, Blog,
FAQ) and acronyms conventionally kept (PTO, HR, KPI, SaaS, SOP) are left
untranslated; ordinary HR vocabulary is translated. Common chrome lives in
loc_catalog.COMMON, not here. JSON-LD text is intentionally left English.
"""


def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


# Shared segments that recur on every article (CTA button, back link, breadcrumb
# Home, and the og:image:alt). Repeated per page so the strict check passes.
_HOME = _t(">Accueil</a>", ">Startseite</a>", ">Inicio</a>", ">Home</a>", ">Home</a>")
_EXPLORE = _t("Découvrir HR Suite", "HR Suite entdecken", "Explorar HR Suite", "Esplora HR Suite", "Ontdek HR Suite")
_BACK = _t("Retour au blog", "Zurück zum Blog", "Volver al blog", "Torna al blog", "Terug naar de blog")
_ALT = _t("FulcrumGrid HR Suite — gestion du personnel",
          "FulcrumGrid HR Suite — Personalmanagement",
          "FulcrumGrid HR Suite — gestión de personas",
          "FulcrumGrid HR Suite — gestione del personale",
          "FulcrumGrid HR Suite — personeelsbeheer")
_FAQ_H = _t("Questions fréquentes", "Häufig gestellte Fragen", "Preguntas frecuentes", "Domande frequenti", "Veelgestelde vragen")


PAGE = {}

PAGE['/blog/employee-handbook/'] = {
    'src': 'blog/employee-handbook/index.html',
    't': {
        '>Home</a>': _HOME,
        'Explore HR Suite': _EXPLORE,
        'Back to the blog': _BACK,
        'FulcrumGrid HR Suite — people operations': _ALT,
        'Frequently asked questions': _FAQ_H,
        # ---- Title / meta ----
        'What Is an Employee Handbook? (And What to Put in It)': _t(
            "Qu'est-ce qu'un manuel de l'employé ? (Et que faut-il y mettre)",
            'Was ist ein Mitarbeiterhandbuch? (Und was gehört hinein)',
            '¿Qué es un manual del empleado? (Y qué incluir en él)',
            "Che cos'è un manuale del dipendente? (E cosa inserirvi)",
            'Wat is een personeelshandboek? (En wat erin te zetten)'),
        'What an employee handbook is, why every business needs one, and a section-by-section list of what to include — from policies to culture.': _t(
            "Ce qu'est un manuel de l'employé, pourquoi toute entreprise en a besoin, et une liste section par section de ce qu'il faut y inclure — des politiques à la culture.",
            'Was ein Mitarbeiterhandbuch ist, warum jedes Unternehmen eines braucht und eine Abschnitt-für-Abschnitt-Liste dessen, was hineingehört — von den Richtlinien bis zur Kultur.',
            'Qué es un manual del empleado, por qué toda empresa necesita uno y una lista, sección por sección, de lo que debe incluir — de las políticas a la cultura.',
            "Che cos'è un manuale del dipendente, perché ogni azienda ne ha bisogno e un elenco sezione per sezione di ciò che va incluso — dalle politiche alla cultura.",
            'Wat een personeelshandboek is, waarom elk bedrijf er een nodig heeft en een sectie-voor-sectie-lijst van wat erin hoort — van beleid tot cultuur.'),
        'An employee handbook sets the rules and the tone. Here is what it is and exactly what to put in it.': _t(
            "Un manuel de l'employé fixe les règles et donne le ton. Voici ce que c'est et exactement quoi y mettre.",
            'Ein Mitarbeiterhandbuch legt die Regeln fest und gibt den Ton an. Hier erfahren Sie, was es ist und was genau hineingehört.',
            'Un manual del empleado fija las reglas y marca el tono. Esto es lo que es y exactamente qué incluir en él.',
            "Un manuale del dipendente stabilisce le regole e dà il tono. Ecco che cos'è ed esattamente cosa inserirvi.",
            'Een personeelshandboek legt de regels vast en bepaalt de toon. Dit is wat het is en precies wat erin moet.'),
        # ---- Breadcrumb current / H2 ----
        'What is an employee handbook?': _t(
            "Qu'est-ce qu'un manuel de l'employé ?",
            'Was ist ein Mitarbeiterhandbuch?',
            '¿Qué es un manual del empleado?',
            "Che cos'è un manuale del dipendente?",
            'Wat is een personeelshandboek?'),
        # ---- Meta line (date + reading time) ----
        'September 13, 2026': _t('13 septembre 2026', '13. September 2026', '13 de septiembre de 2026', '13 settembre 2026', '13 september 2026'),
        '6 min read': _t('6 min de lecture', '6 Min. Lesezeit', '6 min de lectura', '6 min di lettura', '6 min leestijd'),
        # ---- Body ----
        'An employee handbook is the single place your team can go to learn how your company works — the rules, the benefits, the expectations, and the tone. Done well, it prevents a thousand small questions and protects both the business and its people. Done badly, or not at all, it leaves everyone guessing. Here is what a handbook is and what belongs in one.': _t(
            "Un manuel de l'employé est l'endroit unique où votre équipe peut apprendre comment fonctionne votre entreprise — les règles, les avantages, les attentes et le ton. Bien conçu, il évite mille petites questions et protège à la fois l'entreprise et ses collaborateurs. Mal conçu, ou absent, il laisse tout le monde dans le flou. Voici ce qu'est un manuel et ce qui doit y figurer.",
            'Ein Mitarbeiterhandbuch ist der eine Ort, an dem Ihr Team erfahren kann, wie Ihr Unternehmen funktioniert — die Regeln, die Leistungen, die Erwartungen und der Ton. Gut gemacht, verhindert es tausend kleine Fragen und schützt sowohl das Unternehmen als auch seine Mitarbeiter. Schlecht gemacht oder gar nicht, lässt es alle im Ungewissen. Hier erfahren Sie, was ein Handbuch ist und was hineingehört.',
            'Un manual del empleado es el único lugar al que su equipo puede acudir para saber cómo funciona su empresa — las reglas, los beneficios, las expectativas y el tono. Bien hecho, evita mil pequeñas preguntas y protege tanto a la empresa como a sus personas. Mal hecho, o inexistente, deja a todos adivinando. Esto es lo que es un manual y lo que debe figurar en él.',
            "Un manuale del dipendente è l'unico posto in cui il tuo team può scoprire come funziona la tua azienda — le regole, i benefici, le aspettative e il tono. Fatto bene, evita mille piccole domande e protegge sia l'azienda sia le sue persone. Fatto male, o del tutto assente, lascia tutti nell'incertezza. Ecco che cos'è un manuale e cosa deve contenere.",
            'Een personeelshandboek is de ene plek waar uw team terechtkan om te leren hoe uw bedrijf werkt — de regels, de voordelen, de verwachtingen en de toon. Goed gedaan voorkomt het duizend kleine vragen en beschermt het zowel het bedrijf als de mensen. Slecht gedaan, of helemaal niet, laat het iedereen gissen. Dit is wat een handboek is en wat erin thuishoort.'),
        "An employee handbook is a document that sets out your company's policies, procedures, benefits, and expectations for employees. It is part reference manual, part culture statement: it tells people both what they must do (rules and compliance) and how you do things (values and norms). It is usually given at onboarding and updated as the company grows.": _t(
            "Un manuel de l'employé est un document qui expose les politiques, les procédures, les avantages et les attentes de votre entreprise envers ses employés. Il est à la fois manuel de référence et déclaration de culture : il indique aux gens ce qu'ils doivent faire (règles et conformité) et comment vous faites les choses (valeurs et normes). Il est généralement remis lors de l'intégration et mis à jour à mesure que l'entreprise grandit.",
            'Ein Mitarbeiterhandbuch ist ein Dokument, das die Richtlinien, Abläufe, Leistungen und Erwartungen Ihres Unternehmens an die Mitarbeiter darlegt. Es ist teils Nachschlagewerk, teils Kulturbekenntnis: Es sagt den Menschen sowohl, was sie tun müssen (Regeln und Compliance), als auch, wie Sie die Dinge angehen (Werte und Normen). Es wird üblicherweise beim Onboarding ausgehändigt und mit dem Wachstum des Unternehmens aktualisiert.',
            'Un manual del empleado es un documento que expone las políticas, los procedimientos, los beneficios y las expectativas de su empresa hacia los empleados. Es en parte manual de referencia y en parte declaración de cultura: indica a las personas tanto lo que deben hacer (reglas y cumplimiento) como cómo hacen las cosas (valores y normas). Suele entregarse en la incorporación y se actualiza a medida que la empresa crece.',
            "Un manuale del dipendente è un documento che espone le politiche, le procedure, i benefici e le aspettative della tua azienda nei confronti dei dipendenti. È in parte manuale di riferimento, in parte dichiarazione di cultura: dice alle persone sia cosa devono fare (regole e conformità) sia come fate le cose (valori e norme). Di solito viene consegnato durante l'onboarding e aggiornato man mano che l'azienda cresce.",
            'Een personeelshandboek is een document dat het beleid, de procedures, de voordelen en de verwachtingen van uw bedrijf voor medewerkers uiteenzet. Het is deels naslagwerk, deels cultuurverklaring: het vertelt mensen zowel wat ze moeten doen (regels en naleving) als hoe u de dingen aanpakt (waarden en normen). Het wordt meestal bij de onboarding gegeven en bijgewerkt naarmate het bedrijf groeit.'),
        'Why every business needs one': _t(
            'Pourquoi toute entreprise en a besoin', 'Warum jedes Unternehmen eines braucht',
            'Por qué toda empresa necesita uno', 'Perché ogni azienda ne ha bisogno', 'Waarom elk bedrijf er een nodig heeft'),
        'A handbook creates consistency — the same rules for everyone — and a written record of the policies you have communicated, which matters if a dispute ever arises. It speeds up onboarding, reduces repetitive questions to HR, and sets expectations clearly so managers are not inventing answers on the spot. Even a small team benefits from writing it down.': _t(
            "Un manuel crée de la cohérence — les mêmes règles pour tous — et une trace écrite des politiques que vous avez communiquées, ce qui compte en cas de litige. Il accélère l'intégration, réduit les questions répétitives adressées aux HR et fixe clairement les attentes, de sorte que les managers n'improvisent pas les réponses. Même une petite équipe gagne à le mettre par écrit.",
            'Ein Handbuch schafft Konsistenz — dieselben Regeln für alle — und einen schriftlichen Nachweis der Richtlinien, die Sie kommuniziert haben, was im Streitfall wichtig ist. Es beschleunigt das Onboarding, reduziert wiederkehrende Fragen an HR und setzt Erwartungen klar, sodass Führungskräfte Antworten nicht aus dem Stegreif erfinden müssen. Selbst ein kleines Team profitiert davon, es schriftlich festzuhalten.',
            'Un manual crea coherencia — las mismas reglas para todos — y un registro escrito de las políticas que ha comunicado, lo que importa si alguna vez surge una disputa. Acelera la incorporación, reduce las preguntas repetitivas a HR y fija las expectativas con claridad, de modo que los responsables no improvisen respuestas. Incluso un equipo pequeño se beneficia de ponerlo por escrito.',
            "Un manuale crea coerenza — le stesse regole per tutti — e una traccia scritta delle politiche che hai comunicato, il che conta se dovesse mai sorgere una controversia. Accelera l'onboarding, riduce le domande ripetitive all'HR e fissa le aspettative con chiarezza, così i manager non improvvisano le risposte. Anche un piccolo team trae vantaggio dal metterlo per iscritto.",
            'Een handboek zorgt voor consistentie — dezelfde regels voor iedereen — en een schriftelijke vastlegging van het beleid dat u heeft gecommuniceerd, wat telt als er ooit een geschil ontstaat. Het versnelt de onboarding, vermindert herhaalde vragen aan HR en stelt verwachtingen helder, zodat managers geen antwoorden ter plekke hoeven te verzinnen. Zelfs een klein team heeft er baat bij om het op te schrijven.'),
        'What to include': _t('Ce qu\'il faut inclure', 'Was hineingehört', 'Qué incluir', 'Cosa includere', 'Wat op te nemen'),
        'A practical handbook usually covers:': _t(
            'Un manuel pratique couvre généralement :', 'Ein praktisches Handbuch deckt in der Regel ab:',
            'Un manual práctico suele cubrir:', 'Un manuale pratico di solito copre:', 'Een praktisch handboek behandelt doorgaans:'),
        '<strong>Welcome and culture</strong> — mission, values, and how you work.': _t(
            '<strong>Accueil et culture</strong> — mission, valeurs et façon de travailler.',
            '<strong>Willkommen und Kultur</strong> — Mission, Werte und Arbeitsweise.',
            '<strong>Bienvenida y cultura</strong> — misión, valores y forma de trabajar.',
            '<strong>Benvenuto e cultura</strong> — missione, valori e modo di lavorare.',
            '<strong>Welkom en cultuur</strong> — missie, waarden en hoe u werkt.'),
        '<strong>Employment basics</strong> — contracts, probation, working hours, and attendance.': _t(
            "<strong>Bases de l'emploi</strong> — contrats, période d'essai, horaires de travail et présence.",
            '<strong>Beschäftigungsgrundlagen</strong> — Verträge, Probezeit, Arbeitszeiten und Anwesenheit.',
            '<strong>Aspectos básicos del empleo</strong> — contratos, período de prueba, jornada laboral y asistencia.',
            '<strong>Nozioni di base sul rapporto di lavoro</strong> — contratti, periodo di prova, orario di lavoro e presenze.',
            '<strong>Basis van het dienstverband</strong> — contracten, proeftijd, werktijden en aanwezigheid.'),
        '<strong>Pay and benefits</strong> — payroll schedule, leave, health cover, and any allowances.': _t(
            '<strong>Rémunération et avantages</strong> — calendrier de paie, congés, couverture santé et éventuelles indemnités.',
            '<strong>Vergütung und Leistungen</strong> — Gehaltsabrechnungstermine, Urlaub, Krankenversicherung und etwaige Zulagen.',
            '<strong>Retribución y beneficios</strong> — calendario de nóminas, permisos, cobertura sanitaria y cualquier complemento.',
            '<strong>Retribuzione e benefici</strong> — calendario delle buste paga, congedi, copertura sanitaria ed eventuali indennità.',
            '<strong>Loon en voordelen</strong> — loonkalender, verlof, zorgdekking en eventuele toelagen.'),
        '<strong>Leave and time off</strong> — annual leave, sick leave, and how to request it.': _t(
            '<strong>Congés et absences</strong> — congés annuels, congés maladie et comment les demander.',
            '<strong>Urlaub und Abwesenheiten</strong> — Jahresurlaub, Krankheitsurlaub und wie man ihn beantragt.',
            '<strong>Permisos y ausencias</strong> — vacaciones anuales, baja por enfermedad y cómo solicitarlas.',
            '<strong>Congedi e assenze</strong> — ferie annuali, malattia e come richiederli.',
            '<strong>Verlof en vrije tijd</strong> — jaarlijks verlof, ziekteverlof en hoe het aan te vragen.'),
        '<strong>Conduct and expectations</strong> — code of conduct, communication, and the disciplinary process.': _t(
            '<strong>Conduite et attentes</strong> — code de conduite, communication et procédure disciplinaire.',
            '<strong>Verhalten und Erwartungen</strong> — Verhaltenskodex, Kommunikation und Disziplinarverfahren.',
            '<strong>Conducta y expectativas</strong> — código de conducta, comunicación y proceso disciplinario.',
            '<strong>Condotta e aspettative</strong> — codice di condotta, comunicazione e procedimento disciplinare.',
            '<strong>Gedrag en verwachtingen</strong> — gedragscode, communicatie en het disciplinaire proces.'),
        '<strong>Health, safety, and security</strong> — workplace safety and data / IT policies.': _t(
            '<strong>Santé, sécurité et sûreté</strong> — sécurité au travail et politiques de données / informatiques.',
            '<strong>Gesundheit, Sicherheit und Schutz</strong> — Arbeitssicherheit sowie Daten- / IT-Richtlinien.',
            '<strong>Salud, seguridad y protección</strong> — seguridad en el trabajo y políticas de datos / TI.',
            '<strong>Salute, sicurezza e protezione</strong> — sicurezza sul lavoro e politiche su dati / IT.',
            '<strong>Gezondheid, veiligheid en beveiliging</strong> — veiligheid op de werkplek en beleid voor data / IT.'),
        '<strong>Anti-discrimination and grievances</strong> — how issues are raised and handled.': _t(
            '<strong>Anti-discrimination et réclamations</strong> — comment les problèmes sont soulevés et traités.',
            '<strong>Antidiskriminierung und Beschwerden</strong> — wie Probleme angesprochen und behandelt werden.',
            '<strong>Antidiscriminación y reclamaciones</strong> — cómo se plantean y se gestionan los problemas.',
            '<strong>Anti-discriminazione e reclami</strong> — come vengono sollevati e gestiti i problemi.',
            '<strong>Antidiscriminatie en klachten</strong> — hoe kwesties worden aangekaart en afgehandeld.'),
        '<strong>Exit</strong> — notice periods and offboarding.': _t(
            '<strong>Départ</strong> — préavis et offboarding.',
            '<strong>Austritt</strong> — Kündigungsfristen und Offboarding.',
            '<strong>Salida</strong> — plazos de preaviso y offboarding.',
            '<strong>Uscita</strong> — periodi di preavviso e offboarding.',
            '<strong>Vertrek</strong> — opzegtermijnen en offboarding.'),
        'What to leave out': _t('Ce qu\'il faut laisser de côté', 'Was man weglassen sollte', 'Qué dejar fuera', 'Cosa lasciare fuori', 'Wat weg te laten'),
        'Keep individual contract terms (specific salaries), fast-changing operational detail, and anything better handled case by case out of the handbook — they date quickly and make it heavier than it needs to be. Link to living documents instead of pasting them in.': _t(
            "Gardez hors du manuel les clauses contractuelles individuelles (salaires précis), les détails opérationnels qui changent vite et tout ce qui se traite mieux au cas par cas — cela devient vite obsolète et alourdit inutilement le document. Créez des liens vers des documents vivants plutôt que de les y recopier.",
            'Halten Sie individuelle Vertragsbedingungen (konkrete Gehälter), sich schnell ändernde betriebliche Details und alles, was besser von Fall zu Fall gehandhabt wird, aus dem Handbuch heraus — sie veralten schnell und machen es unnötig umfangreich. Verlinken Sie auf lebende Dokumente, statt sie hineinzukopieren.',
            'Mantenga fuera del manual las condiciones contractuales individuales (salarios concretos), los detalles operativos que cambian rápido y todo lo que se gestiona mejor caso por caso — quedan obsoletos enseguida y lo hacen más pesado de lo necesario. Enlace a documentos vivos en lugar de pegarlos dentro.',
            "Tieni fuori dal manuale le condizioni contrattuali individuali (stipendi specifici), i dettagli operativi che cambiano in fretta e tutto ciò che è meglio gestire caso per caso — invecchiano in fretta e lo rendono più pesante del necessario. Collega a documenti vivi invece di incollarli dentro.",
            'Houd individuele contractvoorwaarden (specifieke salarissen), snel veranderende operationele details en alles wat beter per geval wordt afgehandeld buiten het handboek — die verouderen snel en maken het zwaarder dan nodig. Verwijs naar levende documenten in plaats van ze erin te plakken.'),
        'Keeping it current': _t('Le tenir à jour', 'Aktuell halten', 'Mantenerlo actualizado', 'Tenerlo aggiornato', 'Het actueel houden'),
        'A handbook is only useful if it is accurate. Review it at least once a year and whenever the law or a major policy changes, version it so people know what is current, and record that each employee has read and acknowledged it. A stale handbook that contradicts practice is worse than none.': _t(
            "Un manuel n'est utile que s'il est exact. Révisez-le au moins une fois par an et chaque fois que la loi ou une politique majeure change, versionnez-le pour que chacun sache ce qui est en vigueur, et consignez le fait que chaque employé l'a lu et accepté. Un manuel obsolète qui contredit la pratique est pire que pas de manuel du tout.",
            'Ein Handbuch ist nur nützlich, wenn es korrekt ist. Überprüfen Sie es mindestens einmal jährlich und immer dann, wenn sich das Gesetz oder eine wichtige Richtlinie ändert, versehen Sie es mit Versionen, damit alle wissen, was aktuell gilt, und dokumentieren Sie, dass jeder Mitarbeiter es gelesen und bestätigt hat. Ein veraltetes Handbuch, das der Praxis widerspricht, ist schlimmer als gar keines.',
            'Un manual solo es útil si es exacto. Revíselo al menos una vez al año y cada vez que cambie la ley o una política importante, versiónelo para que todos sepan qué está vigente y deje constancia de que cada empleado lo ha leído y aceptado. Un manual desfasado que contradice la práctica es peor que ninguno.',
            "Un manuale è utile solo se è accurato. Rivedilo almeno una volta l'anno e ogni volta che cambia la legge o una politica importante, versionalo affinché tutti sappiano cosa è in vigore e registra che ogni dipendente lo ha letto e accettato. Un manuale obsoleto che contraddice la pratica è peggio di nessun manuale.",
            'Een handboek is alleen nuttig als het klopt. Herzie het minstens één keer per jaar en telkens wanneer de wet of een belangrijk beleid verandert, voorzie het van versies zodat iedereen weet wat actueel is, en leg vast dat elke medewerker het heeft gelezen en bevestigd. Een verouderd handboek dat de praktijk tegenspreekt is erger dan geen handboek.'),
        # ---- FAQ ----
        'Is an employee handbook legally required?': _t(
            "Un manuel de l'employé est-il obligatoire par la loi ?",
            'Ist ein Mitarbeiterhandbuch gesetzlich vorgeschrieben?',
            '¿Es obligatorio por ley un manual del empleado?',
            'Un manuale del dipendente è obbligatorio per legge?',
            'Is een personeelshandboek wettelijk verplicht?'),
        'In most places a handbook itself is not legally required, but many of the individual policies it contains may be — and having them written down helps you stay compliant and consistent. Check the rules where you operate.': _t(
            "Dans la plupart des endroits, le manuel lui-même n'est pas obligatoire par la loi, mais beaucoup des politiques individuelles qu'il contient peuvent l'être — et les avoir par écrit vous aide à rester conforme et cohérent. Vérifiez les règles là où vous exercez.",
            'In den meisten Regionen ist das Handbuch selbst gesetzlich nicht vorgeschrieben, viele der einzelnen darin enthaltenen Richtlinien können es jedoch sein — und sie schriftlich festzuhalten hilft Ihnen, gesetzeskonform und konsistent zu bleiben. Prüfen Sie die Vorschriften an Ihrem Standort.',
            'En la mayoría de los lugares el manual en sí no es obligatorio por ley, pero muchas de las políticas concretas que contiene sí pueden serlo — y tenerlas por escrito le ayuda a mantenerse conforme y coherente. Compruebe las normas del lugar donde opera.',
            "Nella maggior parte dei casi il manuale in sé non è obbligatorio per legge, ma molte delle singole politiche che contiene possono esserlo — e averle per iscritto ti aiuta a restare conforme e coerente. Verifica le norme del luogo in cui operi.",
            'In de meeste plaatsen is het handboek zelf niet wettelijk verplicht, maar veel van de afzonderlijke beleidsregels die het bevat kunnen dat wel zijn — en ze op schrift hebben helpt u compliant en consistent te blijven. Controleer de regels op de plek waar u actief bent.'),
        'What is the difference between an employee handbook and an employment contract?': _t(
            "Quelle est la différence entre un manuel de l'employé et un contrat de travail ?",
            'Was ist der Unterschied zwischen einem Mitarbeiterhandbuch und einem Arbeitsvertrag?',
            '¿Cuál es la diferencia entre un manual del empleado y un contrato de trabajo?',
            'Qual è la differenza tra un manuale del dipendente e un contratto di lavoro?',
            'Wat is het verschil tussen een personeelshandboek en een arbeidsovereenkomst?'),
        'A contract is a binding agreement with one employee covering their specific terms. A handbook is a general reference of company-wide policies and culture that applies to everyone; it usually is not a contract in itself.': _t(
            "Un contrat est un accord contraignant avec un employé qui couvre ses conditions particulières. Un manuel est une référence générale des politiques et de la culture de toute l'entreprise, qui s'applique à tous ; il ne constitue généralement pas un contrat en soi.",
            'Ein Vertrag ist eine verbindliche Vereinbarung mit einem einzelnen Mitarbeiter, die dessen konkrete Bedingungen regelt. Ein Handbuch ist eine allgemeine Referenz für unternehmensweite Richtlinien und Kultur, die für alle gilt; es ist in der Regel selbst kein Vertrag.',
            'Un contrato es un acuerdo vinculante con un empleado que cubre sus condiciones concretas. Un manual es una referencia general de las políticas y la cultura de toda la empresa, que se aplica a todos; normalmente no es un contrato en sí mismo.',
            "Un contratto è un accordo vincolante con un singolo dipendente che ne copre le condizioni specifiche. Un manuale è un riferimento generale sulle politiche e sulla cultura dell'intera azienda, valido per tutti; di solito non è di per sé un contratto.",
            'Een contract is een bindende overeenkomst met één medewerker die diens specifieke voorwaarden dekt. Een handboek is een algemene referentie van bedrijfsbrede beleidsregels en cultuur die voor iedereen geldt; het is meestal op zichzelf geen contract.'),
        'How often should you update an employee handbook?': _t(
            "À quelle fréquence faut-il mettre à jour un manuel de l'employé ?",
            'Wie oft sollte man ein Mitarbeiterhandbuch aktualisieren?',
            '¿Con qué frecuencia debe actualizarse un manual del empleado?',
            'Con quale frequenza si dovrebbe aggiornare un manuale del dipendente?',
            'Hoe vaak moet u een personeelshandboek bijwerken?'),
        'At least once a year, and immediately whenever a law changes or you introduce or revise a major policy. Version each update and have employees acknowledge the current one.': _t(
            "Au moins une fois par an, et immédiatement dès qu'une loi change ou que vous introduisez ou révisez une politique majeure. Versionnez chaque mise à jour et faites accepter la version en vigueur par les employés.",
            'Mindestens einmal jährlich und sofort, sobald sich ein Gesetz ändert oder Sie eine wichtige Richtlinie einführen oder überarbeiten. Versehen Sie jede Aktualisierung mit einer Version und lassen Sie die Mitarbeiter die aktuelle bestätigen.',
            'Al menos una vez al año, e inmediatamente cada vez que cambie una ley o introduzca o revise una política importante. Versione cada actualización y haga que los empleados acepten la vigente.',
            "Almeno una volta l'anno e subito ogni volta che cambia una legge o che introduci o rivedi una politica importante. Versiona ogni aggiornamento e fai accettare ai dipendenti quello in vigore.",
            'Minstens één keer per jaar, en onmiddellijk telkens wanneer een wet verandert of u een belangrijk beleid invoert of herziet. Voorzie elke update van een versie en laat medewerkers de huidige bevestigen.'),
        # ---- Read next ----
        'A handbook pairs naturally with a strong start — see our <a href="/blog/employee-onboarding-checklist/">employee onboarding checklist</a>, <a href="/blog/pto-policy/">building a PTO policy</a>, and <a href="/blog/sop-guide-small-business/">writing SOPs your team follows</a>.': _t(
            'Un manuel va naturellement de pair avec un bon démarrage — consultez notre <a href="/blog/employee-onboarding-checklist/">liste de contrôle d\'intégration des employés</a>, <a href="/blog/pto-policy/">l\'élaboration d\'une politique de PTO</a> et <a href="/blog/sop-guide-small-business/">la rédaction de SOP que votre équipe applique</a>.',
            'Ein Handbuch passt natürlich zu einem starken Start — siehe unsere <a href="/blog/employee-onboarding-checklist/">Checkliste für das Mitarbeiter-Onboarding</a>, <a href="/blog/pto-policy/">das Erstellen einer PTO-Richtlinie</a> und <a href="/blog/sop-guide-small-business/">das Schreiben von SOPs, die Ihr Team befolgt</a>.',
            'Un manual encaja de forma natural con un buen comienzo — consulte nuestra <a href="/blog/employee-onboarding-checklist/">lista de incorporación de empleados</a>, <a href="/blog/pto-policy/">la creación de una política de PTO</a> y <a href="/blog/sop-guide-small-business/">la redacción de SOP que su equipo siga</a>.',
            'Un manuale si abbina naturalmente a un buon inizio — vedi la nostra <a href="/blog/employee-onboarding-checklist/">checklist di onboarding dei dipendenti</a>, <a href="/blog/pto-policy/">la creazione di una politica sui PTO</a> e <a href="/blog/sop-guide-small-business/">la stesura di SOP che il tuo team segue</a>.',
            'Een handboek past natuurlijk bij een sterke start — zie onze <a href="/blog/employee-onboarding-checklist/">onboardingchecklist voor medewerkers</a>, <a href="/blog/pto-policy/">het opstellen van een PTO-beleid</a> en <a href="/blog/sop-guide-small-business/">het schrijven van SOP\'s die uw team volgt</a>.'),
        # ---- CTA ----
        'Give every hire one source of truth': _t(
            'Offrez à chaque recrue une source unique de vérité',
            'Geben Sie jeder Neueinstellung eine einzige Quelle der Wahrheit',
            'Dé a cada nueva contratación una única fuente de verdad',
            "Dai a ogni nuovo assunto un'unica fonte di verità",
            'Geef elke nieuwe medewerker één bron van waarheid'),
        'HR Suite stores your policies, sends them at onboarding, and records who has acknowledged what — so your handbook is read, current, and easy to keep in sync.': _t(
            "HR Suite stocke vos politiques, les envoie lors de l'intégration et enregistre qui a accepté quoi — pour que votre manuel soit lu, à jour et facile à garder synchronisé.",
            'HR Suite speichert Ihre Richtlinien, versendet sie beim Onboarding und protokolliert, wer was bestätigt hat — damit Ihr Handbuch gelesen, aktuell und leicht synchron zu halten ist.',
            'HR Suite almacena sus políticas, las envía en la incorporación y registra quién ha aceptado qué — para que su manual se lea, esté actualizado y sea fácil de mantener sincronizado.',
            'HR Suite conserva le tue politiche, le invia durante l\'onboarding e registra chi ha accettato cosa — così il tuo manuale viene letto, è aggiornato e facile da mantenere sincronizzato.',
            'HR Suite bewaart uw beleid, verstuurt het bij de onboarding en registreert wie wat heeft bevestigd — zodat uw handboek gelezen wordt, actueel is en eenvoudig te synchroniseren blijft.'),
    },
}

PAGE['/blog/employee-onboarding-checklist/'] = {
    'src': 'blog/employee-onboarding-checklist/index.html',
    't': {
        '>Home</a>': _HOME,
        'Explore HR Suite': _EXPLORE,
        'Back to the blog': _BACK,
        'FulcrumGrid HR Suite — people operations': _ALT,
        # ---- Title / meta ----
        'Employee Onboarding Checklist: The First 30 Days': _t(
            "Liste de contrôle d'intégration des employés : les 30 premiers jours",
            'Checkliste für das Mitarbeiter-Onboarding: die ersten 30 Tage',
            'Lista de incorporación de empleados: los primeros 30 días',
            'Checklist di onboarding dei dipendenti: i primi 30 giorni',
            'Onboardingchecklist voor medewerkers: de eerste 30 dagen'),
        'Employee Onboarding Checklist': _t(
            "Liste de contrôle d'intégration des employés",
            'Checkliste für das Mitarbeiter-Onboarding',
            'Lista de incorporación de empleados',
            'Checklist di onboarding dei dipendenti',
            'Onboardingchecklist voor medewerkers'),
        'Employee onboarding checklist': _t(
            "Liste de contrôle d'intégration des employés",
            'Checkliste für das Mitarbeiter-Onboarding',
            'Lista de incorporación de empleados',
            'Checklist di onboarding dei dipendenti',
            'Onboardingchecklist voor medewerkers'),
        'A practical employee onboarding checklist covering the days before day one through the first 30 days — so new hires get productive faster and stay longer.': _t(
            "Une liste de contrôle d'intégration des employés concrète, des jours précédant le premier jour jusqu'aux 30 premiers jours — pour que les nouvelles recrues soient productives plus vite et restent plus longtemps.",
            'Eine praxisnahe Checkliste für das Mitarbeiter-Onboarding, von den Tagen vor dem ersten Tag bis zu den ersten 30 Tagen — damit neue Mitarbeiter schneller produktiv werden und länger bleiben.',
            'Una lista práctica de incorporación de empleados, desde los días previos al primer día hasta los primeros 30 días — para que las nuevas contrataciones sean productivas antes y se queden más tiempo.',
            'Una checklist pratica di onboarding dei dipendenti, dai giorni prima del primo giorno fino ai primi 30 giorni — così i nuovi assunti diventano produttivi più in fretta e restano più a lungo.',
            'Een praktische onboardingchecklist voor medewerkers, van de dagen vóór dag één tot en met de eerste 30 dagen — zodat nieuwe medewerkers sneller productief worden en langer blijven.'),
        'From before day one to the first 30 days — the steps that get new hires productive faster and keep them.': _t(
            'Des jours précédant le premier jour aux 30 premiers jours — les étapes qui rendent les nouvelles recrues productives plus vite et les fidélisent.',
            'Von vor dem ersten Tag bis zu den ersten 30 Tagen — die Schritte, die neue Mitarbeiter schneller produktiv machen und halten.',
            'Desde antes del primer día hasta los primeros 30 días — los pasos que hacen productivas antes a las nuevas contrataciones y las retienen.',
            'Da prima del primo giorno ai primi 30 giorni — i passi che rendono i nuovi assunti produttivi più in fretta e li trattengono.',
            'Van vóór dag één tot de eerste 30 dagen — de stappen die nieuwe medewerkers sneller productief maken en behouden.'),
        'August 25, 2026': _t('25 août 2026', '25. August 2026', '25 de agosto de 2026', '25 agosto 2026', '25 augustus 2026'),
        '6 min read': _t('6 min de lecture', '6 Min. Lesezeit', '6 min de lectura', '6 min di lettura', '6 min leestijd'),
        # ---- Body intro ----
        "A new hire decides how they feel about a job in the first few weeks — long before they've done their best work. Strong onboarding is the difference between someone who's contributing confidently by week three and someone who's still guessing where things are. It's also one of the cheapest ways to improve retention: people who have a structured first month are markedly more likely to stay.": _t(
            "Une nouvelle recrue se forge une opinion sur son poste dès les premières semaines — bien avant d'avoir donné le meilleur d'elle-même. Une intégration solide fait la différence entre quelqu'un qui contribue avec assurance dès la troisième semaine et quelqu'un qui cherche encore où sont les choses. C'est aussi l'un des moyens les moins coûteux d'améliorer la fidélisation : les personnes qui bénéficient d'un premier mois structuré sont nettement plus susceptibles de rester.",
            'Ein neuer Mitarbeiter entscheidet in den ersten Wochen, wie er zu einer Stelle steht — lange bevor er seine beste Arbeit geleistet hat. Ein gutes Onboarding ist der Unterschied zwischen jemandem, der ab Woche drei souverän beiträgt, und jemandem, der noch rät, wo alles ist. Es ist außerdem eine der günstigsten Möglichkeiten, die Bindung zu verbessern: Menschen mit einem strukturierten ersten Monat bleiben deutlich häufiger.',
            'Una nueva contratación decide cómo se siente respecto a un puesto en las primeras semanas — mucho antes de haber dado lo mejor de sí. Una buena incorporación marca la diferencia entre alguien que contribuye con confianza en la tercera semana y alguien que aún adivina dónde está todo. Es también una de las formas más baratas de mejorar la retención: quienes tienen un primer mes estructurado son notablemente más propensos a quedarse.',
            "Un nuovo assunto decide come si sente riguardo a un lavoro nelle prime settimane — molto prima di aver dato il meglio di sé. Un buon onboarding fa la differenza tra chi contribuisce con sicurezza dalla terza settimana e chi ancora indovina dove sono le cose. È anche uno dei modi più economici per migliorare la fidelizzazione: chi ha un primo mese strutturato è nettamente più propenso a restare.",
            'Een nieuwe medewerker bepaalt in de eerste weken hoe hij over een baan denkt — lang voordat hij zijn beste werk heeft geleverd. Sterke onboarding is het verschil tussen iemand die in week drie zelfverzekerd bijdraagt en iemand die nog gist waar alles staat. Het is ook een van de goedkoopste manieren om behoud te verbeteren: mensen met een gestructureerde eerste maand blijven aanzienlijk vaker.'),
        "Here's a practical onboarding checklist, organised by phase. The specifics vary by role, but the shape holds for almost any team.": _t(
            "Voici une liste de contrôle d'intégration concrète, organisée par phase. Les détails varient selon le poste, mais la structure reste valable pour presque toutes les équipes.",
            'Hier ist eine praxisnahe Onboarding-Checkliste, nach Phasen gegliedert. Die Details variieren je nach Rolle, aber die Struktur gilt für fast jedes Team.',
            'Aquí tiene una lista de incorporación práctica, organizada por fases. Los detalles varían según el puesto, pero la estructura sirve para casi cualquier equipo.',
            'Ecco una checklist di onboarding pratica, organizzata per fasi. I dettagli variano in base al ruolo, ma la struttura vale per quasi ogni team.',
            'Hier is een praktische onboardingchecklist, ingedeeld per fase. De details verschillen per functie, maar de opzet geldt voor bijna elk team.'),
        # ---- Before day one ----
        'Before day one': _t('Avant le premier jour', 'Vor dem ersten Tag', 'Antes del primer día', 'Prima del primo giorno', 'Vóór dag één'),
        'Send the signed offer, contract, and any policies to acknowledge — ideally with e-signature so nothing waits on paper.': _t(
            "Envoyez l'offre signée, le contrat et les éventuelles politiques à approuver — idéalement avec signature électronique, pour que rien n'attende sur papier.",
            'Senden Sie das unterzeichnete Angebot, den Vertrag und etwaige zu bestätigende Richtlinien — idealerweise mit E-Signatur, damit nichts auf Papier wartet.',
            'Envíe la oferta firmada, el contrato y cualquier política que deba aceptarse — idealmente con firma electrónica, para que nada quede esperando en papel.',
            'Invia l\'offerta firmata, il contratto ed eventuali politiche da accettare — idealmente con firma elettronica, così nulla resta in attesa su carta.',
            'Stuur het ondertekende aanbod, het contract en eventueel te bevestigen beleid — idealiter met e-handtekening, zodat niets op papier blijft wachten.'),
        'Provision accounts and access ahead of time: email, tools, and the systems the role needs on day one.': _t(
            "Créez les comptes et les accès à l'avance : e-mail, outils et systèmes dont le poste a besoin dès le premier jour.",
            'Richten Sie Konten und Zugänge im Voraus ein: E-Mail, Tools und die Systeme, die die Rolle am ersten Tag benötigt.',
            'Prepare cuentas y accesos con antelación: correo electrónico, herramientas y los sistemas que el puesto necesita el primer día.',
            'Predisponi in anticipo account e accessi: e-mail, strumenti e i sistemi che il ruolo richiede il primo giorno.',
            'Richt accounts en toegang vooraf in: e-mail, tools en de systemen die de functie op dag één nodig heeft.'),
        'Prepare equipment and a workspace (or ship hardware for remote hires with time to spare).': _t(
            "Préparez le matériel et un espace de travail (ou expédiez le matériel aux recrues à distance avec un peu d'avance).",
            'Bereiten Sie Ausrüstung und einen Arbeitsplatz vor (oder versenden Sie Hardware an Remote-Mitarbeiter mit etwas Vorlauf).',
            'Prepare el equipo y un puesto de trabajo (o envíe el hardware a las contrataciones remotas con tiempo de sobra).',
            'Prepara attrezzatura e postazione di lavoro (oppure spedisci l\'hardware ai nuovi assunti da remoto con un po\' di anticipo).',
            'Bereid apparatuur en een werkplek voor (of verstuur hardware naar externe medewerkers ruim op tijd).'),
        'Share a simple first-day plan and a welcome note so the new hire knows where to be and what to expect.': _t(
            "Partagez un plan simple pour le premier jour et un mot de bienvenue, pour que la nouvelle recrue sache où aller et à quoi s'attendre.",
            'Teilen Sie einen einfachen Plan für den ersten Tag und ein Willkommensschreiben, damit der neue Mitarbeiter weiß, wohin er muss und was ihn erwartet.',
            'Comparta un plan sencillo para el primer día y una nota de bienvenida, para que la nueva contratación sepa dónde estar y qué esperar.',
            'Condividi un semplice piano per il primo giorno e un messaggio di benvenuto, così il nuovo assunto sa dove andare e cosa aspettarsi.',
            'Deel een eenvoudig plan voor de eerste dag en een welkomstbericht, zodat de nieuwe medewerker weet waar hij moet zijn en wat hij kan verwachten.'),
        # ---- Day one ----
        'Day one': _t('Le premier jour', 'Der erste Tag', 'El primer día', 'Il primo giorno', 'Dag één'),
        'A real welcome — an introduction to the team and a named buddy or point of contact.': _t(
            "Un vrai accueil — une présentation à l'équipe et un parrain ou point de contact désigné.",
            'Ein echtes Willkommen — eine Vorstellung im Team und ein benannter Buddy oder Ansprechpartner.',
            'Una bienvenida de verdad — una presentación al equipo y un mentor o punto de contacto designado.',
            'Un vero benvenuto — una presentazione al team e un buddy o referente designato.',
            'Een echt welkom — een kennismaking met het team en een aangewezen buddy of aanspreekpunt.'),
        'Confirm access works and collect the remaining paperwork (tax, banking, emergency contact).': _t(
            "Vérifiez que les accès fonctionnent et recueillez les documents restants (impôts, coordonnées bancaires, contact d'urgence).",
            'Bestätigen Sie, dass die Zugänge funktionieren, und sammeln Sie die restlichen Unterlagen ein (Steuer, Bankverbindung, Notfallkontakt).',
            'Confirme que los accesos funcionan y recopile la documentación restante (impuestos, datos bancarios, contacto de emergencia).',
            'Verifica che gli accessi funzionino e raccogli i documenti restanti (fisco, dati bancari, contatto di emergenza).',
            'Bevestig dat de toegang werkt en verzamel de resterende documenten (belasting, bankgegevens, noodcontact).'),
        'Walk through the essentials: how the team communicates, where documents live, and who owns what.': _t(
            "Passez en revue l'essentiel : comment l'équipe communique, où se trouvent les documents et qui est responsable de quoi.",
            'Gehen Sie das Wesentliche durch: wie das Team kommuniziert, wo Dokumente liegen und wer wofür zuständig ist.',
            'Repase lo esencial: cómo se comunica el equipo, dónde están los documentos y quién es responsable de qué.',
            'Illustra l\'essenziale: come comunica il team, dove si trovano i documenti e chi è responsabile di cosa.',
            'Loop de essentie door: hoe het team communiceert, waar documenten staan en wie waarvoor verantwoordelijk is.'),
        'Set one small, achievable task so they end day one having done something real.': _t(
            "Confiez une petite tâche réalisable, pour qu'ils terminent le premier jour en ayant accompli quelque chose de concret.",
            'Geben Sie eine kleine, erreichbare Aufgabe, damit sie den ersten Tag mit etwas Konkretem beenden.',
            'Asigne una tarea pequeña y alcanzable, para que terminen el primer día habiendo hecho algo real.',
            'Assegna un piccolo compito realizzabile, così concludono il primo giorno avendo fatto qualcosa di concreto.',
            'Geef één kleine, haalbare taak, zodat ze dag één afsluiten met iets concreets gedaan.'),
        # ---- First week ----
        'The first week': _t('La première semaine', 'Die erste Woche', 'La primera semana', 'La prima settimana', 'De eerste week'),
        'Book the recurring one-to-one with their manager and a check-in with the buddy.': _t(
            "Planifiez l'entretien individuel récurrent avec leur manager et un point avec le parrain.",
            'Vereinbaren Sie das wiederkehrende Einzelgespräch mit der Führungskraft und einen Check-in mit dem Buddy.',
            'Programe la reunión individual periódica con su responsable y un seguimiento con el mentor.',
            'Fissa l\'incontro individuale ricorrente con il manager e un check-in con il buddy.',
            'Plan het terugkerende één-op-één-gesprek met hun manager en een check-in met de buddy.'),
        "Introduce the tools and processes they'll use daily — in context, not as a document dump.": _t(
            "Présentez les outils et processus qu'ils utiliseront au quotidien — en contexte, et non sous forme de déversement de documents.",
            'Führen Sie die Tools und Abläufe ein, die sie täglich nutzen werden — im Kontext, nicht als Dokumentenflut.',
            'Presente las herramientas y los procesos que usarán a diario — en contexto, no como un aluvión de documentos.',
            'Presenta gli strumenti e i processi che useranno ogni giorno — nel contesto, non come uno scarico di documenti.',
            'Introduceer de tools en processen die ze dagelijks gebruiken — in context, niet als een stortvloed aan documenten.'),
        'Clarify what success looks like for the first month, in plain terms.': _t(
            'Précisez, en termes simples, à quoi ressemble la réussite pour le premier mois.',
            'Klären Sie in einfachen Worten, wie Erfolg für den ersten Monat aussieht.',
            'Aclare, en términos sencillos, qué es el éxito en el primer mes.',
            'Chiarisci, in termini semplici, come si presenta il successo per il primo mese.',
            'Verduidelijk, in eenvoudige bewoordingen, hoe succes eruitziet voor de eerste maand.'),
        # ---- First 30 days ----
        'The first 30 days': _t('Les 30 premiers jours', 'Die ersten 30 Tage', 'Los primeros 30 días', 'I primi 30 giorni', 'De eerste 30 dagen'),
        "A structured 30-day check-in: what's going well, what's unclear, what they need.": _t(
            "Un bilan structuré à 30 jours : ce qui va bien, ce qui reste flou, ce dont ils ont besoin.",
            'Ein strukturierter 30-Tage-Check-in: was gut läuft, was unklar ist, was sie brauchen.',
            'Un seguimiento estructurado a los 30 días: qué va bien, qué no está claro, qué necesitan.',
            'Un check-in strutturato a 30 giorni: cosa va bene, cosa non è chiaro, di cosa hanno bisogno.',
            'Een gestructureerde check-in na 30 dagen: wat goed gaat, wat onduidelijk is, wat ze nodig hebben.'),
        "First real deliverables, with feedback that's specific and timely.": _t(
            'Premiers livrables réels, avec un retour précis et en temps voulu.',
            'Erste echte Arbeitsergebnisse, mit spezifischem und zeitnahem Feedback.',
            'Primeros entregables reales, con comentarios específicos y a tiempo.',
            'Primi deliverable reali, con feedback specifico e tempestivo.',
            'Eerste echte resultaten, met feedback die specifiek en tijdig is.'),
        'Confirm all compliance and admin items are complete and on file.': _t(
            'Vérifiez que tous les éléments de conformité et administratifs sont complets et archivés.',
            'Bestätigen Sie, dass alle Compliance- und Verwaltungspunkte vollständig und abgelegt sind.',
            'Confirme que todos los elementos de cumplimiento y administrativos están completos y archivados.',
            'Verifica che tutti gli elementi di conformità e amministrativi siano completi e archiviati.',
            'Bevestig dat alle compliance- en administratieve punten volledig en gearchiveerd zijn.'),
        # ---- Read next ----
        "None of this is complicated — but it's easy to drop a step when onboarding lives in someone's head. Turning the checklist into a repeatable template, with tasks and e-signatures built in, is what makes every new hire's first month consistent. (If you're still choosing a system to run it, our guide to <a href=\"/blog/hr-software-small-business/\">HR software for small businesses</a> covers what to look for.)": _t(
            "Rien de tout cela n'est compliqué — mais il est facile d'oublier une étape lorsque l'intégration ne tient que dans la tête de quelqu'un. Transformer la liste de contrôle en un modèle réutilisable, avec des tâches et des signatures électroniques intégrées, c'est ce qui rend cohérent le premier mois de chaque nouvelle recrue. (Si vous cherchez encore un système pour la gérer, notre guide sur le <a href=\"/blog/hr-software-small-business/\">logiciel HR pour petites entreprises</a> explique ce qu'il faut regarder.)",
            "Nichts davon ist kompliziert — aber es ist leicht, einen Schritt zu vergessen, wenn das Onboarding nur im Kopf einer Person existiert. Die Checkliste in eine wiederholbare Vorlage mit integrierten Aufgaben und E-Signaturen zu verwandeln, macht den ersten Monat jedes neuen Mitarbeiters einheitlich. (Wenn Sie noch ein System dafür suchen, erklärt unser Leitfaden zu <a href=\"/blog/hr-software-small-business/\">HR-Software für kleine Unternehmen</a>, worauf Sie achten sollten.)",
            "Nada de esto es complicado — pero es fácil saltarse un paso cuando la incorporación solo existe en la cabeza de alguien. Convertir la lista en una plantilla repetible, con tareas y firmas electrónicas integradas, es lo que hace coherente el primer mes de cada nueva contratación. (Si todavía está eligiendo un sistema para gestionarla, nuestra guía sobre <a href=\"/blog/hr-software-small-business/\">software de HR para pequeñas empresas</a> explica en qué fijarse.)",
            "Niente di tutto questo è complicato — ma è facile saltare un passaggio quando l'onboarding vive solo nella testa di qualcuno. Trasformare la checklist in un modello ripetibile, con attività e firme elettroniche integrate, è ciò che rende coerente il primo mese di ogni nuovo assunto. (Se stai ancora scegliendo un sistema per gestirlo, la nostra guida al <a href=\"/blog/hr-software-small-business/\">software HR per piccole imprese</a> spiega cosa cercare.)",
            "Niets hiervan is ingewikkeld — maar het is makkelijk om een stap over te slaan wanneer onboarding alleen in iemands hoofd bestaat. De checklist omzetten in een herbruikbaar sjabloon, met ingebouwde taken en e-handtekeningen, is wat de eerste maand van elke nieuwe medewerker consistent maakt. (Als u nog een systeem kiest om het uit te voeren, legt onze gids over <a href=\"/blog/hr-software-small-business/\">HR-software voor kleine bedrijven</a> uit waar u op moet letten.)"),
        # ---- CTA ----
        'Onboard the same way every time': _t(
            'Intégrez de la même façon à chaque fois',
            'Onboarden Sie jedes Mal auf dieselbe Weise',
            'Incorpore de la misma forma cada vez',
            'Fai l\'onboarding sempre allo stesso modo',
            'Onboard elke keer op dezelfde manier'),
        'HR Suite turns onboarding into repeatable checklists with e-signatures and automatic account setup — so no step gets missed and week one runs itself.': _t(
            "HR Suite transforme l'intégration en listes de contrôle réutilisables avec signatures électroniques et création automatique des comptes — pour qu'aucune étape ne soit oubliée et que la première semaine se déroule toute seule.",
            'HR Suite verwandelt das Onboarding in wiederholbare Checklisten mit E-Signaturen und automatischer Kontoeinrichtung — damit kein Schritt vergessen wird und die erste Woche wie von selbst läuft.',
            'HR Suite convierte la incorporación en listas repetibles con firmas electrónicas y creación automática de cuentas — para que no se salte ningún paso y la primera semana se gestione sola.',
            'HR Suite trasforma l\'onboarding in checklist ripetibili con firme elettroniche e configurazione automatica degli account — così nessun passaggio viene saltato e la prima settimana funziona da sola.',
            'HR Suite maakt van onboarding herbruikbare checklists met e-handtekeningen en automatische accountinstelling — zodat geen enkele stap wordt gemist en week één zichzelf runt.'),
    },
}

PAGE['/blog/employee-time-tracking/'] = {
    'src': 'blog/employee-time-tracking/index.html',
    't': {
        '>Home</a>': _HOME,
        'Explore HR Suite': _EXPLORE,
        'Back to the blog': _BACK,
        'FulcrumGrid HR Suite — people operations': _ALT,
        # ---- Title / meta ----
        'Employee Time Tracking: A Practical Guide': _t(
            'Suivi du temps des employés : un guide pratique',
            'Zeiterfassung für Mitarbeiter: ein praktischer Leitfaden',
            'Control horario de empleados: una guía práctica',
            'Monitoraggio del tempo dei dipendenti: una guida pratica',
            'Tijdregistratie van medewerkers: een praktische gids'),
        'Employee time tracking': _t(
            'Suivi du temps des employés',
            'Zeiterfassung für Mitarbeiter',
            'Control horario de empleados',
            'Monitoraggio del tempo dei dipendenti',
            'Tijdregistratie van medewerkers'),
        'How to track employee time without micromanaging — methods, what to log, overtime rules, and how it ties into payroll and PTO.': _t(
            'Comment suivre le temps des employés sans microgérer — méthodes, quoi enregistrer, règles sur les heures supplémentaires et lien avec la paie et le PTO.',
            'Wie Sie die Arbeitszeit von Mitarbeitern erfassen, ohne zu mikromanagen — Methoden, was zu erfassen ist, Überstundenregeln und wie es mit Gehaltsabrechnung und PTO zusammenhängt.',
            'Cómo controlar el tiempo de los empleados sin microgestionar — métodos, qué registrar, reglas de horas extra y cómo se conecta con las nóminas y el PTO.',
            'Come monitorare il tempo dei dipendenti senza microgestire — metodi, cosa registrare, regole sugli straordinari e come si collega a buste paga e PTO.',
            'Hoe u de tijd van medewerkers bijhoudt zonder micromanagen — methoden, wat te registreren, regels voor overuren en hoe het samenhangt met loonadministratie en PTO.'),
        'Methods, what to actually log, overtime rules, and how time tracking should connect to payroll and PTO — without turning into surveillance.': _t(
            'Méthodes, ce qu\'il faut réellement enregistrer, règles sur les heures supplémentaires et comment le suivi du temps devrait se connecter à la paie et au PTO — sans virer à la surveillance.',
            'Methoden, was tatsächlich zu erfassen ist, Überstundenregeln und wie Zeiterfassung mit Gehaltsabrechnung und PTO verbunden sein sollte — ohne zur Überwachung zu werden.',
            'Métodos, qué registrar realmente, reglas de horas extra y cómo debería conectarse el control horario con las nóminas y el PTO — sin convertirse en vigilancia.',
            'Metodi, cosa registrare davvero, regole sugli straordinari e come il monitoraggio del tempo dovrebbe collegarsi a buste paga e PTO — senza trasformarsi in sorveglianza.',
            'Methoden, wat u echt moet registreren, regels voor overuren en hoe tijdregistratie zou moeten aansluiten op loonadministratie en PTO — zonder in toezicht te veranderen.'),
        'September 7, 2026': _t('7 septembre 2026', '7. September 2026', '7 de septiembre de 2026', '7 settembre 2026', '7 september 2026'),
        '6 min read': _t('6 min de lecture', '6 Min. Lesezeit', '6 min de lectura', '6 min di lettura', '6 min leestijd'),
        # ---- Body ----
        'Time tracking has a trust problem before it even starts: employees hear "we\'re tracking your hours" and think surveillance, while managers hear "we need accurate time data" and think payroll and billing accuracy. Both are right, and the gap between them closes the moment tracking is built around a clear, stated purpose instead of vague oversight.': _t(
            'Le suivi du temps a un problème de confiance avant même de commencer : les employés entendent « nous suivons vos heures » et pensent surveillance, tandis que les managers entendent « il nous faut des données de temps exactes » et pensent exactitude de la paie et de la facturation. Les deux ont raison, et l\'écart entre eux se comble dès que le suivi s\'articule autour d\'un objectif clair et annoncé plutôt que d\'un contrôle flou.',
            'Die Zeiterfassung hat ein Vertrauensproblem, noch bevor sie beginnt: Mitarbeiter hören „wir erfassen eure Stunden" und denken an Überwachung, während Führungskräfte „wir brauchen genaue Zeitdaten" hören und an korrekte Gehaltsabrechnung und Abrechnung denken. Beide haben recht, und die Kluft zwischen ihnen schließt sich in dem Moment, in dem die Erfassung um einen klaren, erklärten Zweck herum aufgebaut wird statt um vage Kontrolle.',
            'El control horario tiene un problema de confianza antes incluso de empezar: los empleados oyen «estamos controlando vuestras horas» y piensan en vigilancia, mientras que los responsables oyen «necesitamos datos de tiempo precisos» y piensan en la exactitud de las nóminas y la facturación. Ambos tienen razón, y la brecha entre ellos se cierra en cuanto el control se construye en torno a un propósito claro y declarado en lugar de una supervisión vaga.',
            'Il monitoraggio del tempo ha un problema di fiducia prima ancora di iniziare: i dipendenti sentono «stiamo monitorando le vostre ore» e pensano alla sorveglianza, mentre i manager sentono «ci servono dati sul tempo accurati» e pensano all\'accuratezza di buste paga e fatturazione. Entrambi hanno ragione, e il divario tra loro si chiude nel momento in cui il monitoraggio è costruito attorno a uno scopo chiaro e dichiarato invece che su un controllo vago.',
            'Tijdregistratie heeft een vertrouwensprobleem nog voor het begint: medewerkers horen "we houden je uren bij" en denken aan toezicht, terwijl managers "we hebben nauwkeurige tijdgegevens nodig" horen en denken aan correcte loonadministratie en facturatie. Beiden hebben gelijk, en de kloof daartussen sluit op het moment dat registratie wordt opgebouwd rond een helder, uitgesproken doel in plaats van vaag toezicht.'),
        "Decide why you're tracking time — it changes everything else": _t(
            'Décidez pourquoi vous suivez le temps — cela change tout le reste',
            'Entscheiden Sie, warum Sie die Zeit erfassen — das ändert alles Übrige',
            'Decida por qué controla el tiempo — cambia todo lo demás',
            'Decidi perché monitori il tempo — cambia tutto il resto',
            'Bepaal waarom u tijd registreert — dat verandert al het andere'),
        'The right approach depends entirely on what the data is for. <strong>Payroll accuracy</strong> for hourly staff needs precise clock-in/clock-out records. <strong>Client billing</strong> needs time tied to a project or task, not just a total for the day. <strong>Capacity planning</strong> needs a rough sense of where hours go, not minute-by-minute logs. Pick the wrong method for your actual purpose and you\'ll either collect too little detail to be useful or so much that nobody keeps it up.': _t(
            "La bonne approche dépend entièrement de l'usage prévu des données. L'<strong>exactitude de la paie</strong> pour le personnel horaire exige des relevés précis d'arrivée et de départ. La <strong>facturation client</strong> exige un temps rattaché à un projet ou une tâche, pas seulement un total pour la journée. La <strong>planification des capacités</strong> exige une idée approximative de la répartition des heures, pas des relevés minute par minute. Choisissez la mauvaise méthode pour votre objectif réel et vous collecterez soit trop peu de détails pour être utile, soit tellement que personne ne tiendra le rythme.",
            'Der richtige Ansatz hängt ganz davon ab, wofür die Daten dienen. <strong>Korrekte Gehaltsabrechnung</strong> für Stundenkräfte braucht präzise Kommen/Gehen-Aufzeichnungen. <strong>Kundenabrechnung</strong> braucht Zeit, die einem Projekt oder einer Aufgabe zugeordnet ist, nicht nur eine Tagessumme. <strong>Kapazitätsplanung</strong> braucht ein grobes Gefühl dafür, wohin die Stunden fließen, keine minutengenauen Protokolle. Wählen Sie die falsche Methode für Ihren tatsächlichen Zweck, sammeln Sie entweder zu wenig Details, um nützlich zu sein, oder so viele, dass niemand sie pflegt.',
            'El enfoque correcto depende por completo de para qué son los datos. La <strong>exactitud de las nóminas</strong> del personal por horas necesita registros precisos de entrada y salida. La <strong>facturación a clientes</strong> necesita tiempo vinculado a un proyecto o tarea, no solo un total del día. La <strong>planificación de la capacidad</strong> necesita una idea aproximada de adónde van las horas, no registros minuto a minuto. Elija el método equivocado para su propósito real y recopilará o bien muy poco detalle para que sirva, o tanto que nadie lo mantenga.',
            "L'approccio giusto dipende interamente dallo scopo dei dati. L'<strong>accuratezza delle buste paga</strong> per il personale a ore richiede registrazioni precise di entrata e uscita. La <strong>fatturazione ai clienti</strong> richiede tempo legato a un progetto o a un'attività, non solo un totale giornaliero. La <strong>pianificazione della capacità</strong> richiede un'idea approssimativa di dove vanno le ore, non registri minuto per minuto. Scegli il metodo sbagliato per il tuo scopo reale e raccoglierai o troppo pochi dettagli per essere utile, o così tanti che nessuno li tiene aggiornati.",
            'De juiste aanpak hangt volledig af van waar de gegevens voor dienen. <strong>Correcte loonadministratie</strong> voor uurmedewerkers vereist nauwkeurige in- en uitklokregistraties. <strong>Facturatie aan klanten</strong> vereist tijd gekoppeld aan een project of taak, niet alleen een dagtotaal. <strong>Capaciteitsplanning</strong> vereist een globaal beeld van waar de uren heen gaan, geen minuut-voor-minuutlogs. Kies de verkeerde methode voor uw werkelijke doel en u verzamelt óf te weinig detail om nuttig te zijn, óf zoveel dat niemand het bijhoudt.'),
        'The three common methods': _t('Les trois méthodes courantes', 'Die drei gängigen Methoden', 'Los tres métodos comunes', 'I tre metodi comuni', 'De drie gangbare methoden'),
        '<strong>Clock in/out</strong> — a timestamp at the start and end of a shift. Simple, standard for hourly and shift-based roles, and usually a legal requirement where minimum-wage or overtime rules apply.': _t(
            "<strong>Pointage entrée/sortie</strong> — un horodatage au début et à la fin d'un poste. Simple, standard pour les rôles horaires et postés, et généralement une obligation légale là où s'appliquent des règles de salaire minimum ou d'heures supplémentaires.",
            '<strong>Kommen/Gehen-Stempelung</strong> — ein Zeitstempel zu Beginn und Ende einer Schicht. Einfach, Standard für Stunden- und Schichtrollen und meist gesetzlich vorgeschrieben, wo Mindestlohn- oder Überstundenregeln gelten.',
            '<strong>Fichar entrada/salida</strong> — una marca de tiempo al inicio y al final de un turno. Sencillo, estándar para puestos por horas y por turnos, y por lo general una exigencia legal donde se aplican reglas de salario mínimo u horas extra.',
            '<strong>Timbratura entrata/uscita</strong> — un timestamp all\'inizio e alla fine di un turno. Semplice, standard per i ruoli a ore e a turni e di solito un obbligo di legge dove si applicano regole su salario minimo o straordinari.',
            '<strong>In-/uitklokken</strong> — een tijdstempel aan het begin en einde van een dienst. Eenvoudig, standaard voor uur- en ploegenfuncties en meestal een wettelijke verplichting waar regels voor minimumloon of overuren gelden.'),
        '<strong>Timesheets</strong> — hours logged against projects, clients, or tasks, usually filled in daily or weekly. Best when the "why" is billing or project costing, since it captures where time went, not just how much there was.': _t(
            "<strong>Feuilles de temps</strong> — heures imputées à des projets, clients ou tâches, généralement remplies chaque jour ou chaque semaine. Idéal lorsque le « pourquoi » est la facturation ou le calcul du coût des projets, car cela capture où le temps est passé, pas seulement combien il y en a eu.",
            '<strong>Stundenzettel</strong> — Stunden, die Projekten, Kunden oder Aufgaben zugeordnet und meist täglich oder wöchentlich ausgefüllt werden. Am besten, wenn das „Warum" Abrechnung oder Projektkalkulation ist, da erfasst wird, wohin die Zeit ging, nicht nur wie viel es war.',
            '<strong>Hojas de horas</strong> — horas imputadas a proyectos, clientes o tareas, normalmente rellenadas a diario o semanalmente. Lo mejor cuando el «porqué» es la facturación o el cálculo de costes de proyectos, ya que capta adónde fue el tiempo, no solo cuánto hubo.',
            '<strong>Timesheet</strong> — ore imputate a progetti, clienti o attività, di solito compilate ogni giorno o ogni settimana. Ideali quando il «perché» è la fatturazione o il calcolo dei costi di progetto, perché catturano dove è andato il tempo, non solo quanto ce n\'è stato.',
            '<strong>Urenstaten</strong> — uren geboekt op projecten, klanten of taken, meestal dagelijks of wekelijks ingevuld. Het best wanneer het "waarom" facturatie of projectkostprijs is, omdat het vastlegt waar de tijd heen ging, niet alleen hoeveel er was.'),
        '<strong>Automatic tracking</strong> — software that detects activity or app usage in the background. Highest detail, highest trust cost — use it deliberately and disclose it, or skip it for a lighter method.': _t(
            "<strong>Suivi automatique</strong> — logiciel qui détecte l'activité ou l'usage des applications en arrière-plan. Le plus de détails, le plus grand coût en confiance — utilisez-le délibérément et annoncez-le, ou renoncez-y au profit d'une méthode plus légère.",
            '<strong>Automatische Erfassung</strong> — Software, die Aktivität oder App-Nutzung im Hintergrund erkennt. Höchster Detailgrad, höchste Vertrauenskosten — setzen Sie sie bewusst ein und legen Sie sie offen, oder verzichten Sie zugunsten einer leichteren Methode.',
            '<strong>Seguimiento automático</strong> — software que detecta la actividad o el uso de aplicaciones en segundo plano. Máximo detalle, máximo coste en confianza — úselo de forma deliberada y comuníquelo, o prescinda de él en favor de un método más ligero.',
            "<strong>Monitoraggio automatico</strong> — software che rileva l'attività o l'uso delle app in background. Massimo dettaglio, massimo costo in fiducia — usalo in modo deliberato e dichiaralo, oppure rinuncia a favore di un metodo più leggero.",
            '<strong>Automatische registratie</strong> — software die activiteit of app-gebruik op de achtergrond detecteert. Meeste detail, hoogste vertrouwenskosten — gebruik het bewust en maak het kenbaar, of sla het over voor een lichtere methode.'),
        "Most small teams don't need the heaviest option. Match the method to the decision the data will actually inform.": _t(
            "La plupart des petites équipes n'ont pas besoin de l'option la plus lourde. Adaptez la méthode à la décision que les données éclaireront réellement.",
            'Die meisten kleinen Teams brauchen nicht die aufwändigste Option. Passen Sie die Methode an die Entscheidung an, die die Daten tatsächlich stützen sollen.',
            'La mayoría de los equipos pequeños no necesitan la opción más pesada. Ajuste el método a la decisión que los datos van a fundamentar realmente.',
            "La maggior parte dei piccoli team non ha bisogno dell'opzione più pesante. Adatta il metodo alla decisione che i dati informeranno davvero.",
            'De meeste kleine teams hebben de zwaarste optie niet nodig. Stem de methode af op de beslissing die de gegevens werkelijk zullen onderbouwen.'),
        'What to actually log': _t('Ce qu\'il faut réellement enregistrer', 'Was tatsächlich zu erfassen ist', 'Qué registrar realmente', 'Cosa registrare davvero', 'Wat u echt moet registreren'),
        'Keep the record itself simple: who, what date, start and end time (or total hours), and — if billing or costing matters — which project or client. Resist the urge to capture more "just in case." Extra fields that don\'t map to a real use tend to go unfilled, which quietly undermines trust in the whole system once people notice the data is incomplete anyway.': _t(
            "Gardez l'enregistrement lui-même simple : qui, quelle date, heure de début et de fin (ou total des heures) et — si la facturation ou le calcul des coûts compte — quel projet ou client. Résistez à l'envie d'en capturer plus « au cas où ». Les champs supplémentaires qui ne correspondent à aucun usage réel restent souvent vides, ce qui sape discrètement la confiance dans tout le système dès que l'on remarque que les données sont de toute façon incomplètes.",
            'Halten Sie die Aufzeichnung selbst einfach: wer, welches Datum, Beginn und Ende (oder Gesamtstunden) und — wenn Abrechnung oder Kalkulation zählt — welches Projekt oder welcher Kunde. Widerstehen Sie dem Drang, mehr „für alle Fälle" zu erfassen. Zusätzliche Felder ohne echten Nutzen bleiben meist unausgefüllt, was das Vertrauen in das gesamte System still untergräbt, sobald man bemerkt, dass die Daten ohnehin unvollständig sind.',
            'Mantenga el registro en sí sencillo: quién, qué fecha, hora de inicio y fin (o total de horas) y — si importan la facturación o el cálculo de costes — qué proyecto o cliente. Resista la tentación de capturar más «por si acaso». Los campos adicionales que no responden a un uso real suelen quedar sin rellenar, lo que socava en silencio la confianza en todo el sistema en cuanto la gente nota que los datos están incompletos de todos modos.',
            "Mantieni la registrazione stessa semplice: chi, quale data, ora di inizio e fine (o totale delle ore) e — se contano fatturazione o calcolo dei costi — quale progetto o cliente. Resisti alla tentazione di catturare di più «per ogni evenienza». I campi aggiuntivi che non corrispondono a un uso reale tendono a restare vuoti, il che mina silenziosamente la fiducia nell'intero sistema non appena ci si accorge che i dati sono comunque incompleti.",
            'Houd de registratie zelf eenvoudig: wie, welke datum, begin- en eindtijd (of totaal aantal uren) en — als facturatie of kostprijs telt — welk project of welke klant. Weersta de neiging om meer vast te leggen "voor het geval dat". Extra velden die niet aan een echt gebruik beantwoorden blijven vaak leeg, wat het vertrouwen in het hele systeem stilletjes ondermijnt zodra mensen merken dat de gegevens toch onvolledig zijn.'),
        'Overtime rules need to be explicit, not assumed': _t(
            'Les règles sur les heures supplémentaires doivent être explicites, pas supposées',
            'Überstundenregeln müssen ausdrücklich sein, nicht vorausgesetzt',
            'Las reglas de horas extra deben ser explícitas, no supuestas',
            'Le regole sugli straordinari devono essere esplicite, non presunte',
            'Regels voor overuren moeten expliciet zijn, niet verondersteld'),
        'Define, in writing, what counts as overtime — hours beyond a daily or weekly threshold — and whether it requires pre-approval. A policy that exists only as "management\'s discretion" produces disputes precisely when they\'re most expensive: after the extra hours have already been worked. State the threshold, the rate, and the approval process before anyone needs to use them.': _t(
            "Définissez, par écrit, ce qui compte comme heures supplémentaires — les heures au-delà d'un seuil quotidien ou hebdomadaire — et si elles requièrent une approbation préalable. Une politique qui n'existe que sous la forme « à la discrétion de la direction » génère des litiges précisément quand ils coûtent le plus cher : une fois les heures supplémentaires déjà effectuées. Indiquez le seuil, le taux et le processus d'approbation avant que quiconque n'en ait besoin.",
            'Legen Sie schriftlich fest, was als Überstunde zählt — Stunden über einer täglichen oder wöchentlichen Schwelle — und ob eine vorherige Genehmigung nötig ist. Eine Regelung, die nur als „Ermessen des Managements" existiert, erzeugt Streit genau dann, wenn er am teuersten ist: nachdem die zusätzlichen Stunden bereits geleistet wurden. Nennen Sie Schwelle, Satz und Genehmigungsprozess, bevor jemand sie braucht.',
            'Defina, por escrito, qué cuenta como horas extra — las horas por encima de un umbral diario o semanal — y si requieren aprobación previa. Una política que solo existe como «a criterio de la dirección» produce disputas justo cuando son más caras: después de que las horas extra ya se hayan trabajado. Indique el umbral, la tarifa y el proceso de aprobación antes de que nadie necesite usarlos.',
            "Definisci, per iscritto, cosa conta come straordinario — le ore oltre una soglia giornaliera o settimanale — e se richiede un'approvazione preventiva. Una politica che esiste solo come «a discrezione della direzione» produce controversie proprio quando sono più costose: dopo che le ore extra sono già state svolte. Indica la soglia, la tariffa e il processo di approvazione prima che qualcuno debba usarli.",
            'Leg schriftelijk vast wat als overuren telt — uren boven een dagelijkse of wekelijkse drempel — en of vooraf goedkeuring nodig is. Een beleid dat alleen bestaat als "ter beoordeling van het management" veroorzaakt geschillen juist wanneer die het duurst zijn: nadat de extra uren al zijn gewerkt. Vermeld de drempel, het tarief en het goedkeuringsproces voordat iemand ze nodig heeft.'),
        'Connect it to payroll and PTO, not a separate system': _t(
            'Connectez-le à la paie et au PTO, pas à un système distinct',
            'Verbinden Sie es mit Gehaltsabrechnung und PTO, nicht mit einem separaten System',
            'Conéctelo a las nóminas y al PTO, no a un sistema aparte',
            'Collegalo a buste paga e PTO, non a un sistema separato',
            'Koppel het aan loonadministratie en PTO, niet aan een apart systeem'),
        'Time data that lives apart from payroll gets re-entered, mistyped, and disputed. When tracked hours flow directly into pay calculations — and when <a href="/blog/pto-policy/">PTO balances</a> are visible in the same place as worked hours — an employee can see one accurate picture instead of reconciling two systems that occasionally disagree about how much they actually worked or have left.': _t(
            'Des données de temps qui vivent à l\'écart de la paie sont ressaisies, mal saisies et contestées. Lorsque les heures suivies alimentent directement les calculs de paie — et que les <a href="/blog/pto-policy/">soldes de PTO</a> sont visibles au même endroit que les heures travaillées — un employé peut voir une seule image exacte au lieu de réconcilier deux systèmes qui, parfois, ne s\'accordent pas sur ce qu\'il a réellement travaillé ou sur ce qu\'il lui reste.',
            'Zeitdaten, die getrennt von der Gehaltsabrechnung liegen, werden erneut eingegeben, vertippt und angefochten. Wenn erfasste Stunden direkt in die Lohnberechnung einfließen — und <a href="/blog/pto-policy/">PTO-Salden</a> am selben Ort wie die geleisteten Stunden sichtbar sind — sieht ein Mitarbeiter ein einziges korrektes Bild, statt zwei Systeme abzugleichen, die sich gelegentlich uneins sind, wie viel er tatsächlich gearbeitet hat oder ihm noch zusteht.',
            'Los datos de tiempo que viven aparte de las nóminas se vuelven a introducir, se teclean mal y se disputan. Cuando las horas registradas fluyen directamente a los cálculos de pago — y los <a href="/blog/pto-policy/">saldos de PTO</a> son visibles en el mismo lugar que las horas trabajadas — un empleado puede ver una única imagen exacta en lugar de conciliar dos sistemas que a veces discrepan sobre cuánto ha trabajado realmente o cuánto le queda.',
            'I dati sul tempo che vivono separati dalle buste paga vengono reinseriti, digitati male e contestati. Quando le ore rilevate confluiscono direttamente nei calcoli della retribuzione — e i <a href="/blog/pto-policy/">saldi PTO</a> sono visibili nello stesso posto delle ore lavorate — un dipendente può vedere un\'unica immagine accurata invece di riconciliare due sistemi che a volte non concordano su quanto ha davvero lavorato o su quanto gli resta.',
            'Tijdgegevens die los van de loonadministratie staan, worden opnieuw ingevoerd, verkeerd getypt en betwist. Wanneer geregistreerde uren rechtstreeks in de loonberekeningen stromen — en <a href="/blog/pto-policy/">PTO-saldi</a> op dezelfde plek zichtbaar zijn als de gewerkte uren — kan een medewerker één nauwkeurig beeld zien in plaats van twee systemen te verzoenen die het soms oneens zijn over hoeveel hij echt heeft gewerkt of nog over heeft.'),
        'Keeping it from feeling like surveillance': _t(
            'Éviter que cela ne ressemble à de la surveillance',
            'Verhindern, dass es sich wie Überwachung anfühlt',
            'Evitar que se sienta como vigilancia',
            'Evitare che sembri sorveglianza',
            'Voorkomen dat het als toezicht aanvoelt'),
        '<strong>Tell people why</strong> — a stated purpose ("this feeds payroll and client invoices") reads very differently from silence.': _t(
            '<strong>Dites aux gens pourquoi</strong> — un objectif annoncé (« cela alimente la paie et les factures clients ») se lit très différemment du silence.',
            '<strong>Sagen Sie den Leuten warum</strong> — ein erklärter Zweck („das fließt in Gehaltsabrechnung und Kundenrechnungen") liest sich ganz anders als Schweigen.',
            '<strong>Diga a la gente por qué</strong> — un propósito declarado («esto alimenta las nóminas y las facturas de clientes») se lee muy distinto del silencio.',
            '<strong>Di\' alle persone il perché</strong> — uno scopo dichiarato («questo alimenta buste paga e fatture ai clienti») si legge in modo molto diverso dal silenzio.',
            '<strong>Vertel mensen waarom</strong> — een uitgesproken doel ("dit voedt de loonadministratie en klantfacturen") leest heel anders dan stilte.'),
        "<strong>Track work, not people</strong> — log hours and tasks, not screenshots or keystroke counts, unless there's a specific, disclosed reason.": _t(
            "<strong>Suivez le travail, pas les personnes</strong> — enregistrez les heures et les tâches, pas des captures d'écran ni le comptage des frappes, sauf raison précise et annoncée.",
            '<strong>Erfassen Sie Arbeit, nicht Menschen</strong> — protokollieren Sie Stunden und Aufgaben, nicht Screenshots oder Tastenanschläge, es sei denn, es gibt einen konkreten, offengelegten Grund.',
            '<strong>Mida el trabajo, no a las personas</strong> — registre horas y tareas, no capturas de pantalla ni recuentos de pulsaciones, salvo que haya una razón concreta y comunicada.',
            '<strong>Monitora il lavoro, non le persone</strong> — registra ore e attività, non screenshot o conteggi dei tasti, salvo un motivo specifico e dichiarato.',
            '<strong>Registreer werk, geen mensen</strong> — leg uren en taken vast, geen screenshots of toetsaanslagen, tenzij er een specifieke, kenbaar gemaakte reden is.'),
        '<strong>Make the data visible to the employee too</strong> — a one-way system that only managers can see breeds more suspicion than one everyone can check.': _t(
            "<strong>Rendez aussi les données visibles pour l'employé</strong> — un système à sens unique que seuls les managers voient nourrit plus de méfiance qu'un système que chacun peut consulter.",
            '<strong>Machen Sie die Daten auch für den Mitarbeiter sichtbar</strong> — ein Einwegsystem, das nur Führungskräfte sehen, weckt mehr Misstrauen als eines, das jeder prüfen kann.',
            '<strong>Haga los datos visibles también para el empleado</strong> — un sistema unidireccional que solo ven los responsables genera más recelo que uno que todos pueden consultar.',
            '<strong>Rendi i dati visibili anche al dipendente</strong> — un sistema a senso unico che solo i manager possono vedere alimenta più sospetto di uno che tutti possono controllare.',
            '<strong>Maak de gegevens ook zichtbaar voor de medewerker</strong> — een eenrichtingssysteem dat alleen managers kunnen zien, wekt meer wantrouwen dan een dat iedereen kan controleren.'),
        # ---- Read next ----
        'Time tracking works best as part of the same system that already runs onboarding and PTO, not a separate tool bolted on top. If you\'re setting this up alongside a new hire\'s first weeks, pair it with our <a href="/blog/employee-onboarding-checklist/">employee onboarding checklist</a>, and see our guide to <a href="/blog/hr-software-small-business/">choosing HR software for a small business</a> for what to look for in a system that ties time, PTO, and payroll together.': _t(
            'Le suivi du temps fonctionne le mieux comme partie intégrante du même système qui gère déjà l\'intégration et le PTO, pas comme un outil distinct rajouté par-dessus. Si vous le mettez en place en parallèle des premières semaines d\'une nouvelle recrue, associez-le à notre <a href="/blog/employee-onboarding-checklist/">liste de contrôle d\'intégration des employés</a>, et consultez notre guide sur le <a href="/blog/hr-software-small-business/">choix d\'un logiciel HR pour une petite entreprise</a> pour savoir ce qu\'il faut rechercher dans un système qui relie temps, PTO et paie.',
            'Zeiterfassung funktioniert am besten als Teil desselben Systems, das bereits Onboarding und PTO abwickelt, nicht als separates, obendrauf geschnalltes Tool. Wenn Sie sie parallel zu den ersten Wochen eines neuen Mitarbeiters einrichten, kombinieren Sie sie mit unserer <a href="/blog/employee-onboarding-checklist/">Checkliste für das Mitarbeiter-Onboarding</a>, und lesen Sie unseren Leitfaden zur <a href="/blog/hr-software-small-business/">Auswahl von HR-Software für ein kleines Unternehmen</a>, worauf Sie bei einem System achten sollten, das Zeit, PTO und Gehaltsabrechnung verbindet.',
            'El control horario funciona mejor como parte del mismo sistema que ya gestiona la incorporación y el PTO, no como una herramienta aparte añadida encima. Si lo pone en marcha junto con las primeras semanas de una nueva contratación, combínelo con nuestra <a href="/blog/employee-onboarding-checklist/">lista de incorporación de empleados</a>, y consulte nuestra guía para <a href="/blog/hr-software-small-business/">elegir software de HR para una pequeña empresa</a> sobre qué buscar en un sistema que une tiempo, PTO y nóminas.',
            "Il monitoraggio del tempo funziona meglio come parte dello stesso sistema che già gestisce onboarding e PTO, non come uno strumento separato aggiunto sopra. Se lo imposti insieme alle prime settimane di un nuovo assunto, abbinalo alla nostra <a href=\"/blog/employee-onboarding-checklist/\">checklist di onboarding dei dipendenti</a>, e consulta la nostra guida alla <a href=\"/blog/hr-software-small-business/\">scelta del software HR per una piccola impresa</a> per capire cosa cercare in un sistema che unisce tempo, PTO e buste paga.",
            'Tijdregistratie werkt het best als onderdeel van hetzelfde systeem dat al onboarding en PTO uitvoert, niet als een los tool dat erbovenop wordt gezet. Als u dit inricht naast de eerste weken van een nieuwe medewerker, combineer het dan met onze <a href="/blog/employee-onboarding-checklist/">onboardingchecklist voor medewerkers</a>, en bekijk onze gids over het <a href="/blog/hr-software-small-business/">kiezen van HR-software voor een klein bedrijf</a> voor waar u op moet letten in een systeem dat tijd, PTO en loonadministratie samenbrengt.'),
        # ---- CTA ----
        'Time, PTO, and payroll in one place': _t(
            'Temps, PTO et paie au même endroit',
            'Zeit, PTO und Gehaltsabrechnung an einem Ort',
            'Tiempo, PTO y nóminas en un solo lugar',
            'Tempo, PTO e buste paga in un unico posto',
            'Tijd, PTO en loonadministratie op één plek'),
        'HR Suite tracks hours alongside PTO balances and payroll — so employees see one accurate record instead of reconciling separate systems.': _t(
            'HR Suite suit les heures aux côtés des soldes de PTO et de la paie — pour que les employés voient un seul relevé exact au lieu de réconcilier des systèmes distincts.',
            'HR Suite erfasst Stunden zusammen mit PTO-Salden und Gehaltsabrechnung — damit Mitarbeiter eine einzige korrekte Aufzeichnung sehen, statt separate Systeme abzugleichen.',
            'HR Suite registra las horas junto con los saldos de PTO y las nóminas — para que los empleados vean un único registro exacto en lugar de conciliar sistemas separados.',
            'HR Suite rileva le ore insieme ai saldi PTO e alle buste paga — così i dipendenti vedono un unico registro accurato invece di riconciliare sistemi separati.',
            'HR Suite houdt uren bij naast PTO-saldi en loonadministratie — zodat medewerkers één nauwkeurig overzicht zien in plaats van aparte systemen te verzoenen.'),
    },
}

PAGE['/blog/gross-pay-vs-net-pay/'] = {
    'src': 'blog/gross-pay-vs-net-pay/index.html',
    't': {
        '>Home</a>': _HOME,
        'Explore HR Suite': _EXPLORE,
        'Back to the blog': _BACK,
        'FulcrumGrid HR Suite — people operations': _ALT,
        'Frequently asked questions': _FAQ_H,
        # ---- Title / meta ----
        "Gross Pay vs Net Pay: What's the Difference?": _t(
            'Salaire brut ou salaire net : quelle différence ?',
            'Bruttolohn oder Nettolohn: Was ist der Unterschied?',
            'Salario bruto frente a salario neto: ¿cuál es la diferencia?',
            'Retribuzione lorda o netta: qual è la differenza?',
            'Brutoloon versus nettoloon: wat is het verschil?'),
        'Gross pay vs net pay': _t(
            'Salaire brut ou salaire net',
            'Bruttolohn oder Nettolohn',
            'Salario bruto frente a salario neto',
            'Retribuzione lorda o netta',
            'Brutoloon versus nettoloon'),
        'A clear explanation of gross pay vs net pay — what each includes, what gets deducted in between, and how to calculate take-home pay.': _t(
            'Une explication claire du salaire brut face au salaire net — ce que chacun comprend, ce qui est déduit entre les deux et comment calculer le salaire net à payer.',
            'Eine klare Erklärung von Bruttolohn und Nettolohn — was jeder umfasst, was dazwischen abgezogen wird und wie man den Auszahlungsbetrag berechnet.',
            'Una explicación clara del salario bruto frente al neto — qué incluye cada uno, qué se deduce en medio y cómo calcular el salario neto a percibir.',
            'Una spiegazione chiara della retribuzione lorda rispetto a quella netta — cosa comprende ciascuna, cosa viene trattenuto nel mezzo e come calcolare il netto in busta.',
            'Een heldere uitleg van brutoloon versus nettoloon — wat elk omvat, wat er tussenin wordt ingehouden en hoe u het nettoloon berekent.'),
        'Gross pay is what you earn before deductions; net pay is what lands in the bank. Here is what happens in between.': _t(
            'Le salaire brut est ce que vous gagnez avant déductions ; le salaire net est ce qui arrive sur le compte. Voici ce qui se passe entre les deux.',
            'Der Bruttolohn ist, was Sie vor Abzügen verdienen; der Nettolohn ist, was auf dem Konto landet. Hier erfahren Sie, was dazwischen passiert.',
            'El salario bruto es lo que gana antes de las deducciones; el salario neto es lo que llega al banco. Esto es lo que ocurre en medio.',
            'La retribuzione lorda è ciò che guadagni prima delle trattenute; quella netta è ciò che arriva in banca. Ecco cosa succede nel mezzo.',
            'Het brutoloon is wat u verdient vóór inhoudingen; het nettoloon is wat op de bank belandt. Dit is wat er tussenin gebeurt.'),
        'September 14, 2026': _t('14 septembre 2026', '14. September 2026', '14 de septiembre de 2026', '14 settembre 2026', '14 september 2026'),
        '5 min read': _t('5 min de lecture', '5 Min. Lesezeit', '5 min de lectura', '5 min di lettura', '5 min leestijd'),
        # ---- Body ----
        'Every payslip tells two stories: the salary you agreed to, and the amount that actually reaches the employee\'s bank account. Those are gross pay and net pay, and the gap between them is where taxes, contributions, and deductions live. Getting the difference right matters for budgeting, for payroll, and for every "why is my pay less than my offer?" conversation.': _t(
            'Chaque bulletin de paie raconte deux histoires : le salaire convenu et le montant qui parvient réellement sur le compte bancaire de l\'employé. Ce sont le salaire brut et le salaire net, et c\'est dans l\'écart entre les deux que vivent les impôts, les cotisations et les déductions. Bien comprendre la différence compte pour le budget, pour la paie et pour chaque conversation du type « pourquoi mon salaire est-il inférieur à mon offre ? ».',
            'Jede Gehaltsabrechnung erzählt zwei Geschichten: das vereinbarte Gehalt und den Betrag, der tatsächlich auf dem Bankkonto des Mitarbeiters ankommt. Das sind Bruttolohn und Nettolohn, und in der Lücke dazwischen leben Steuern, Beiträge und Abzüge. Den Unterschied richtig zu verstehen ist wichtig für die Budgetplanung, für die Gehaltsabrechnung und für jedes Gespräch nach dem Motto „warum ist mein Lohn niedriger als mein Angebot?".',
            'Cada nómina cuenta dos historias: el salario acordado y el importe que realmente llega a la cuenta bancaria del empleado. Son el salario bruto y el salario neto, y en la diferencia entre ambos viven los impuestos, las cotizaciones y las deducciones. Entender bien la diferencia importa para el presupuesto, para las nóminas y para cada conversación del tipo «¿por qué mi salario es menor que mi oferta?».',
            'Ogni busta paga racconta due storie: lo stipendio concordato e l\'importo che arriva davvero sul conto bancario del dipendente. Sono la retribuzione lorda e quella netta, e nel divario tra le due vivono imposte, contributi e trattenute. Capire bene la differenza conta per il budget, per le buste paga e per ogni conversazione del tipo «perché la mia paga è inferiore all\'offerta?».',
            'Elke loonstrook vertelt twee verhalen: het afgesproken salaris en het bedrag dat daadwerkelijk op de bankrekening van de medewerker terechtkomt. Dat zijn het brutoloon en het nettoloon, en in het gat daartussen leven belastingen, bijdragen en inhoudingen. Het verschil goed begrijpen telt voor de begroting, voor de loonadministratie en voor elk gesprek in de trant van "waarom is mijn loon lager dan mijn aanbod?".'),
        'What is gross pay?': _t('Qu\'est-ce que le salaire brut ?', 'Was ist der Bruttolohn?', '¿Qué es el salario bruto?', 'Che cos\'è la retribuzione lorda?', 'Wat is brutoloon?'),
        'Gross pay is the full amount an employee earns <strong>before any deductions</strong>. For a salaried worker it is the annual salary divided across pay periods; for an hourly worker it is hours worked times the hourly rate, plus any overtime, bonuses, or allowances. It is the headline number in an offer letter.': _t(
            "Le salaire brut est le montant total qu'un employé gagne <strong>avant toute déduction</strong>. Pour un salarié, c'est le salaire annuel réparti sur les périodes de paie ; pour un travailleur horaire, ce sont les heures travaillées multipliées par le taux horaire, plus les éventuelles heures supplémentaires, primes ou indemnités. C'est le chiffre mis en avant dans une lettre d'offre.",
            'Der Bruttolohn ist der volle Betrag, den ein Mitarbeiter <strong>vor allen Abzügen</strong> verdient. Bei einem Gehaltsempfänger ist es das über die Abrechnungszeiträume verteilte Jahresgehalt; bei einem Stundenarbeiter sind es die geleisteten Stunden mal dem Stundensatz, zuzüglich etwaiger Überstunden, Boni oder Zulagen. Es ist die hervorgehobene Zahl in einem Angebotsschreiben.',
            'El salario bruto es el importe total que un empleado gana <strong>antes de cualquier deducción</strong>. Para un asalariado es el salario anual repartido entre los períodos de pago; para un trabajador por horas son las horas trabajadas por la tarifa horaria, más las horas extra, primas o complementos que haya. Es la cifra destacada en una carta de oferta.',
            "La retribuzione lorda è l'importo totale che un dipendente guadagna <strong>prima di qualsiasi trattenuta</strong>. Per un dipendente a stipendio è lo stipendio annuo ripartito tra i periodi di paga; per un lavoratore a ore sono le ore lavorate per la tariffa oraria, più eventuali straordinari, bonus o indennità. È la cifra in evidenza in una lettera di offerta.",
            'Het brutoloon is het volledige bedrag dat een medewerker verdient <strong>vóór eventuele inhoudingen</strong>. Voor een medewerker met salaris is het het jaarsalaris verdeeld over de loonperioden; voor een uurmedewerker zijn het de gewerkte uren maal het uurtarief, plus eventuele overuren, bonussen of toelagen. Het is het opvallende getal in een aanbiedingsbrief.'),
        'What is net pay?': _t('Qu\'est-ce que le salaire net ?', 'Was ist der Nettolohn?', '¿Qué es el salario neto?', 'Che cos\'è la retribuzione netta?', 'Wat is nettoloon?'),
        'Net pay — often called take-home pay — is what is left <strong>after every deduction</strong> comes out of gross pay. It is the number that actually lands in the bank. Net pay is always less than or equal to gross pay.': _t(
            "Le salaire net — souvent appelé salaire net à payer — est ce qui reste <strong>après que chaque déduction</strong> a été retirée du salaire brut. C'est le montant qui arrive réellement sur le compte. Le salaire net est toujours inférieur ou égal au salaire brut.",
            'Der Nettolohn — oft Auszahlungsbetrag genannt — ist das, was <strong>nach jedem Abzug</strong> vom Bruttolohn übrig bleibt. Es ist die Zahl, die tatsächlich auf dem Konto landet. Der Nettolohn ist immer kleiner als oder gleich dem Bruttolohn.',
            'El salario neto — a menudo llamado salario a percibir — es lo que queda <strong>después de que cada deducción</strong> sale del salario bruto. Es la cifra que realmente llega al banco. El salario neto es siempre menor o igual que el bruto.',
            "La retribuzione netta — spesso chiamata netto in busta — è ciò che resta <strong>dopo che ogni trattenuta</strong> è stata sottratta dalla retribuzione lorda. È la cifra che arriva davvero in banca. La retribuzione netta è sempre minore o uguale a quella lorda.",
            'Het nettoloon — vaak het uit te betalen loon genoemd — is wat overblijft <strong>nadat elke inhouding</strong> van het brutoloon af is. Het is het getal dat daadwerkelijk op de bank belandt. Het nettoloon is altijd kleiner dan of gelijk aan het brutoloon.'),
        'What gets deducted in between?': _t('Qu\'est-ce qui est déduit entre les deux ?', 'Was wird dazwischen abgezogen?', '¿Qué se deduce en medio?', 'Cosa viene trattenuto nel mezzo?', 'Wat wordt er tussenin ingehouden?'),
        'The deductions that turn gross into net vary by country, but usually include:': _t(
            'Les déductions qui transforment le brut en net varient selon le pays, mais comprennent généralement :',
            'Die Abzüge, die Brutto in Netto verwandeln, variieren je nach Land, umfassen aber meist:',
            'Las deducciones que convierten el bruto en neto varían según el país, pero suelen incluir:',
            'Le trattenute che trasformano il lordo in netto variano da paese a paese, ma di solito comprendono:',
            'De inhoudingen die bruto in netto veranderen verschillen per land, maar omvatten meestal:'),
        '<strong>Income tax or withholding</strong>, where it applies.': _t(
            "<strong>L'impôt sur le revenu ou la retenue à la source</strong>, là où il s'applique.",
            '<strong>Einkommensteuer oder Lohnsteuereinbehalt</strong>, wo sie anfallen.',
            '<strong>El impuesto sobre la renta o la retención</strong>, donde se aplique.',
            "<strong>L'imposta sul reddito o la ritenuta</strong>, dove si applica.",
            '<strong>Inkomstenbelasting of loonheffing</strong>, waar die van toepassing is.'),
        '<strong>Social insurance or pension contributions</strong> — for example, GOSI in Saudi Arabia.': _t(
            '<strong>Les cotisations de sécurité sociale ou de retraite</strong> — par exemple, la GOSI en Arabie saoudite.',
            '<strong>Sozialversicherungs- oder Rentenbeiträge</strong> — zum Beispiel die GOSI in Saudi-Arabien.',
            '<strong>Las cotizaciones a la seguridad social o a pensiones</strong> — por ejemplo, la GOSI en Arabia Saudí.',
            "<strong>I contributi previdenziali o pensionistici</strong> — per esempio, la GOSI in Arabia Saudita.",
            '<strong>Sociale­verzekerings- of pensioenbijdragen</strong> — bijvoorbeeld de GOSI in Saoedi-Arabië.'),
        '<strong>Employee benefit contributions</strong> — health insurance, retirement, and similar.': _t(
            '<strong>Les cotisations aux avantages sociaux</strong> — assurance santé, retraite et similaires.',
            '<strong>Beiträge zu Mitarbeiterleistungen</strong> — Krankenversicherung, Altersvorsorge und Ähnliches.',
            '<strong>Las aportaciones a beneficios del empleado</strong> — seguro médico, jubilación y similares.',
            '<strong>I contributi ai benefici per i dipendenti</strong> — assicurazione sanitaria, previdenza e simili.',
            '<strong>Bijdragen aan werknemersvoordelen</strong> — zorgverzekering, pensioen en dergelijke.'),
        '<strong>Voluntary or court-ordered deductions</strong>, such as loan repayments.': _t(
            '<strong>Les déductions volontaires ou ordonnées par un tribunal</strong>, comme les remboursements de prêts.',
            '<strong>Freiwillige oder gerichtlich angeordnete Abzüge</strong>, etwa Kreditrückzahlungen.',
            '<strong>Las deducciones voluntarias o dictadas por un tribunal</strong>, como la devolución de préstamos.',
            '<strong>Le trattenute volontarie o disposte da un tribunale</strong>, come i rimborsi di prestiti.',
            '<strong>Vrijwillige of door de rechter opgelegde inhoudingen</strong>, zoals aflossingen van leningen.'),
        "Some of these are the employee's share; employers often pay an additional share on top that never appears in the employee's gross.": _t(
            "Certaines de ces déductions sont la part de l'employé ; les employeurs paient souvent une part supplémentaire par-dessus qui n'apparaît jamais dans le brut de l'employé.",
            'Einige davon sind der Anteil des Mitarbeiters; Arbeitgeber zahlen oft einen zusätzlichen Anteil obendrauf, der nie im Brutto des Mitarbeiters erscheint.',
            'Algunas de estas son la parte del empleado; los empleadores a menudo pagan una parte adicional encima que nunca aparece en el bruto del empleado.',
            "Alcune di queste sono la quota del dipendente; i datori di lavoro spesso pagano una quota aggiuntiva che non compare mai nel lordo del dipendente.",
            "Sommige hiervan zijn het aandeel van de medewerker; werkgevers betalen er vaak een extra aandeel bovenop dat nooit in het bruto van de medewerker verschijnt."),
        'How to calculate net pay': _t('Comment calculer le salaire net', 'So berechnen Sie den Nettolohn', 'Cómo calcular el salario neto', 'Come calcolare la retribuzione netta', 'Hoe u het nettoloon berekent'),
        'Start with gross pay, then subtract each deduction in the order your local rules require. In simple terms: <strong>Net pay = Gross pay − total deductions.</strong> The detail is in knowing which deductions apply, what each rate is, and which are capped — which is exactly why payroll is worth automating rather than doing by hand each month.': _t(
            "Partez du salaire brut, puis soustrayez chaque déduction dans l'ordre exigé par vos règles locales. En termes simples : <strong>Salaire net = Salaire brut − total des déductions.</strong> Toute la subtilité consiste à savoir quelles déductions s'appliquent, quel est chaque taux et lesquelles sont plafonnées — c'est précisément pourquoi il vaut la peine d'automatiser la paie plutôt que de la faire à la main chaque mois.",
            'Beginnen Sie mit dem Bruttolohn und ziehen Sie dann jeden Abzug in der von Ihren lokalen Vorschriften geforderten Reihenfolge ab. Einfach ausgedrückt: <strong>Nettolohn = Bruttolohn − Summe der Abzüge.</strong> Der Kniff besteht darin, zu wissen, welche Abzüge gelten, wie hoch jeder Satz ist und welche gedeckelt sind — genau deshalb lohnt es sich, die Gehaltsabrechnung zu automatisieren, statt sie jeden Monat von Hand zu machen.',
            'Empiece por el salario bruto y luego reste cada deducción en el orden que exijan sus normas locales. En términos sencillos: <strong>Salario neto = Salario bruto − total de deducciones.</strong> El detalle está en saber qué deducciones se aplican, cuál es cada tipo y cuáles tienen tope — que es justamente por lo que vale la pena automatizar las nóminas en lugar de hacerlas a mano cada mes.',
            "Parti dalla retribuzione lorda, poi sottrai ogni trattenuta nell'ordine richiesto dalle tue norme locali. In parole semplici: <strong>Retribuzione netta = Retribuzione lorda − totale delle trattenute.</strong> Il dettaglio sta nel sapere quali trattenute si applicano, qual è ciascuna aliquota e quali hanno un tetto — ed è esattamente per questo che vale la pena automatizzare le buste paga anziché farle a mano ogni mese.",
            'Begin met het brutoloon en trek dan elke inhouding af in de volgorde die uw lokale regels vereisen. Eenvoudig gezegd: <strong>Nettoloon = Brutoloon − totaal van de inhoudingen.</strong> Het detail zit in weten welke inhoudingen van toepassing zijn, wat elk tarief is en welke een maximum hebben — precies daarom is het de moeite waard de loonadministratie te automatiseren in plaats van die elke maand met de hand te doen.'),
        'Why the difference matters': _t('Pourquoi la différence compte', 'Warum der Unterschied zählt', 'Por qué importa la diferencia', 'Perché la differenza conta', 'Waarom het verschil telt'),
        "For employees, it is the difference between the offer and the reality — worth explaining clearly at hiring. For employers, gross pay plus the employer's own contributions is the true cost of employment, which is usually higher than the salary figure alone. Budget on total cost, communicate on net pay, and keep the calculation transparent on every payslip.": _t(
            "Pour les employés, c'est la différence entre l'offre et la réalité — qu'il vaut la peine d'expliquer clairement à l'embauche. Pour les employeurs, le salaire brut plus les cotisations patronales représente le coût réel de l'emploi, généralement supérieur au seul chiffre du salaire. Budgétez sur le coût total, communiquez sur le salaire net et gardez le calcul transparent sur chaque bulletin de paie.",
            'Für Mitarbeiter ist es der Unterschied zwischen Angebot und Wirklichkeit — den man bei der Einstellung klar erklären sollte. Für Arbeitgeber ist der Bruttolohn plus die eigenen Arbeitgeberbeiträge der wahre Beschäftigungsaufwand, der meist höher ist als die reine Gehaltszahl. Kalkulieren Sie mit den Gesamtkosten, kommunizieren Sie über den Nettolohn und halten Sie die Berechnung auf jeder Abrechnung transparent.',
            'Para los empleados es la diferencia entre la oferta y la realidad — que conviene explicar con claridad al contratar. Para los empleadores, el salario bruto más las cotizaciones propias del empleador es el coste real del empleo, que suele ser mayor que la cifra del salario por sí sola. Presupueste sobre el coste total, comunique sobre el salario neto y mantenga el cálculo transparente en cada nómina.',
            "Per i dipendenti è la differenza tra l'offerta e la realtà — che conviene spiegare con chiarezza in fase di assunzione. Per i datori di lavoro, la retribuzione lorda più i contributi a carico del datore è il vero costo del lavoro, di solito più alto della sola cifra dello stipendio. Fai il budget sul costo totale, comunica sul netto e mantieni il calcolo trasparente su ogni busta paga.",
            'Voor medewerkers is het het verschil tussen het aanbod en de werkelijkheid — dat u bij aanwerving duidelijk moet uitleggen. Voor werkgevers is het brutoloon plus de eigen werkgeversbijdragen de werkelijke kost van het dienstverband, meestal hoger dan het salariscijfer alleen. Begroot op de totale kost, communiceer over het nettoloon en houd de berekening transparant op elke loonstrook.'),
        # ---- FAQ ----
        'Is gross pay or net pay higher?': _t(
            'Est-ce le salaire brut ou le salaire net qui est le plus élevé ?',
            'Ist der Bruttolohn oder der Nettolohn höher?',
            '¿Es más alto el salario bruto o el neto?',
            'È più alta la retribuzione lorda o quella netta?',
            'Is het brutoloon of het nettoloon hoger?'),
        'Gross pay is always higher, or equal. Net pay is gross pay minus deductions, so it can never exceed gross pay.': _t(
            'Le salaire brut est toujours supérieur, ou égal. Le salaire net correspond au salaire brut moins les déductions, il ne peut donc jamais dépasser le salaire brut.',
            'Der Bruttolohn ist immer höher oder gleich. Der Nettolohn ist der Bruttolohn abzüglich der Abzüge, kann den Bruttolohn also nie übersteigen.',
            'El salario bruto es siempre mayor, o igual. El salario neto es el bruto menos las deducciones, así que nunca puede superar al bruto.',
            'La retribuzione lorda è sempre maggiore, o uguale. La retribuzione netta è quella lorda meno le trattenute, quindi non può mai superare la lorda.',
            'Het brutoloon is altijd hoger, of gelijk. Het nettoloon is het brutoloon min de inhoudingen, dus het kan het brutoloon nooit overschrijden.'),
        'Does gross pay include overtime and bonuses?': _t(
            'Le salaire brut inclut-il les heures supplémentaires et les primes ?',
            'Umfasst der Bruttolohn Überstunden und Boni?',
            '¿Incluye el salario bruto las horas extra y las primas?',
            'La retribuzione lorda include straordinari e bonus?',
            'Omvat het brutoloon overuren en bonussen?'),
        'Yes. Gross pay is total earnings for the period, including base pay plus any overtime, bonuses, commissions, and taxable allowances, before deductions.': _t(
            'Oui. Le salaire brut correspond au total des gains de la période, y compris le salaire de base plus les éventuelles heures supplémentaires, primes, commissions et indemnités imposables, avant déductions.',
            'Ja. Der Bruttolohn ist der Gesamtverdienst des Zeitraums, einschließlich Grundlohn zuzüglich etwaiger Überstunden, Boni, Provisionen und steuerpflichtiger Zulagen, vor Abzügen.',
            'Sí. El salario bruto es el total de ingresos del período, incluido el salario base más las horas extra, primas, comisiones y complementos imponibles que haya, antes de deducciones.',
            'Sì. La retribuzione lorda è il totale dei guadagni del periodo, comprensivo della paga base più eventuali straordinari, bonus, provvigioni e indennità imponibili, prima delle trattenute.',
            'Ja. Het brutoloon is de totale verdienste over de periode, inclusief basisloon plus eventuele overuren, bonussen, commissies en belastbare toelagen, vóór inhoudingen.'),
        "What is the difference between an employee's net pay and the employer's cost?": _t(
            "Quelle est la différence entre le salaire net d'un employé et le coût pour l'employeur ?",
            'Was ist der Unterschied zwischen dem Nettolohn eines Mitarbeiters und den Kosten für den Arbeitgeber?',
            '¿Cuál es la diferencia entre el salario neto de un empleado y el coste para el empleador?',
            "Qual è la differenza tra la retribuzione netta di un dipendente e il costo per il datore di lavoro?",
            'Wat is het verschil tussen het nettoloon van een medewerker en de kost voor de werkgever?'),
        "Net pay is what the employee receives. The employer's cost is gross pay plus the employer's own contributions, such as its share of social insurance, so total employment cost is higher than both gross and net pay.": _t(
            "Le salaire net est ce que l'employé reçoit. Le coût pour l'employeur est le salaire brut plus les cotisations patronales, comme sa part de la sécurité sociale ; le coût total de l'emploi est donc supérieur au salaire brut comme au salaire net.",
            'Der Nettolohn ist das, was der Mitarbeiter erhält. Die Arbeitgeberkosten sind der Bruttolohn plus die eigenen Arbeitgeberbeiträge, etwa sein Anteil an der Sozialversicherung, sodass die Gesamtbeschäftigungskosten höher sind als Brutto- und Nettolohn.',
            'El salario neto es lo que recibe el empleado. El coste para el empleador es el salario bruto más las cotizaciones propias del empleador, como su parte de la seguridad social, de modo que el coste total del empleo es mayor que el salario bruto y el neto.',
            "La retribuzione netta è ciò che riceve il dipendente. Il costo per il datore di lavoro è la retribuzione lorda più i contributi a carico del datore, come la sua quota di previdenza sociale, quindi il costo totale del lavoro è più alto sia del lordo sia del netto.",
            'Het nettoloon is wat de medewerker ontvangt. De kost voor de werkgever is het brutoloon plus de eigen werkgeversbijdragen, zoals diens aandeel in de sociale verzekering, zodat de totale arbeidskost hoger is dan zowel het bruto- als het nettoloon.'),
        # ---- Read next ----
        'Pay sits alongside the rest of people operations — see our guides to <a href="/blog/employee-time-tracking/">employee time tracking</a>, <a href="/blog/how-to-calculate-pto-accrual/">calculating PTO accrual</a>, and <a href="/blog/hr-software-small-business/">choosing HR software</a>.': _t(
            'La rémunération va de pair avec le reste de la gestion du personnel — consultez nos guides sur le <a href="/blog/employee-time-tracking/">suivi du temps des employés</a>, le <a href="/blog/how-to-calculate-pto-accrual/">calcul de l\'acquisition de PTO</a> et le <a href="/blog/hr-software-small-business/">choix d\'un logiciel HR</a>.',
            'Die Vergütung gehört zum übrigen Personalmanagement — siehe unsere Leitfäden zur <a href="/blog/employee-time-tracking/">Zeiterfassung für Mitarbeiter</a>, zum <a href="/blog/how-to-calculate-pto-accrual/">Berechnen der PTO-Ansammlung</a> und zur <a href="/blog/hr-software-small-business/">Auswahl von HR-Software</a>.',
            'La retribución va de la mano con el resto de la gestión de personas — consulte nuestras guías sobre el <a href="/blog/employee-time-tracking/">control horario de empleados</a>, el <a href="/blog/how-to-calculate-pto-accrual/">cálculo de la acumulación de PTO</a> y la <a href="/blog/hr-software-small-business/">elección de software de HR</a>.',
            'La retribuzione va di pari passo con il resto della gestione del personale — vedi le nostre guide al <a href="/blog/employee-time-tracking/">monitoraggio del tempo dei dipendenti</a>, al <a href="/blog/how-to-calculate-pto-accrual/">calcolo della maturazione dei PTO</a> e alla <a href="/blog/hr-software-small-business/">scelta del software HR</a>.',
            'Loon gaat hand in hand met de rest van personeelsbeheer — zie onze gidsen over <a href="/blog/employee-time-tracking/">tijdregistratie van medewerkers</a>, het <a href="/blog/how-to-calculate-pto-accrual/">berekenen van PTO-opbouw</a> en het <a href="/blog/hr-software-small-business/">kiezen van HR-software</a>.'),
        # ---- CTA ----
        'Run payroll without the spreadsheet math': _t(
            'Gérez la paie sans les calculs de tableur',
            'Rechnen Sie Gehälter ab ohne Tabellenkalkulation',
            'Ejecute las nóminas sin las cuentas de hoja de cálculo',
            'Elabora le buste paga senza i calcoli del foglio di calcolo',
            'Verwerk de loonadministratie zonder het rekenwerk in spreadsheets'),
        'HR Suite calculates gross-to-net for every employee, applies the right deductions, and produces clear payslips — so pay is accurate, compliant, and easy to explain.': _t(
            'HR Suite calcule le passage du brut au net pour chaque employé, applique les bonnes déductions et produit des bulletins de paie clairs — pour une rémunération exacte, conforme et facile à expliquer.',
            'HR Suite berechnet für jeden Mitarbeiter den Weg vom Brutto zum Netto, wendet die richtigen Abzüge an und erstellt klare Gehaltsabrechnungen — damit die Vergütung korrekt, konform und leicht erklärbar ist.',
            'HR Suite calcula del bruto al neto para cada empleado, aplica las deducciones correctas y genera nóminas claras — para que la retribución sea exacta, conforme y fácil de explicar.',
            'HR Suite calcola dal lordo al netto per ogni dipendente, applica le trattenute giuste e produce buste paga chiare — così la retribuzione è accurata, conforme e facile da spiegare.',
            'HR Suite berekent voor elke medewerker van bruto naar netto, past de juiste inhoudingen toe en maakt heldere loonstroken — zodat het loon nauwkeurig, compliant en makkelijk uit te leggen is.'),
    },
}

PAGE['/blog/how-to-calculate-pto-accrual/'] = {
    'src': 'blog/how-to-calculate-pto-accrual/index.html',
    't': {
        '>Home</a>': _HOME,
        'Explore HR Suite': _EXPLORE,
        'Back to the blog': _BACK,
        'FulcrumGrid HR Suite — people operations': _ALT,
        'Frequently asked questions': _FAQ_H,
        # ---- Title / meta ----
        'How to Calculate PTO Accrual: Formulas, Rates &amp; Examples': _t(
            'Comment calculer l\'acquisition de PTO : formules, taux &amp; exemples',
            'So berechnen Sie die PTO-Ansammlung: Formeln, Sätze &amp; Beispiele',
            'Cómo calcular la acumulación de PTO: fórmulas, tasas &amp; ejemplos',
            'Come calcolare la maturazione dei PTO: formule, tassi &amp; esempi',
            'PTO-opbouw berekenen: formules, tempo\'s &amp; voorbeelden'),
        'How to calculate PTO accrual': _t(
            "Comment calculer l'acquisition de PTO",
            'So berechnen Sie die PTO-Ansammlung',
            'Cómo calcular la acumulación de PTO',
            'Come calcolare la maturazione dei PTO',
            'PTO-opbouw berekenen'),
        'How to calculate PTO accrual step by step — the formula, accrual rates by pay period, hourly vs salaried, and worked examples you can copy. Plus a quick FAQ.': _t(
            "Comment calculer l'acquisition de PTO étape par étape — la formule, les taux d'acquisition par période de paie, horaire ou salarié, et des exemples chiffrés à copier. Plus une FAQ rapide.",
            'So berechnen Sie die PTO-Ansammlung Schritt für Schritt — die Formel, Ansammlungssätze je Abrechnungszeitraum, Stunden- vs. Gehaltskräfte und durchgerechnete Beispiele zum Kopieren. Plus eine kurze FAQ.',
            'Cómo calcular la acumulación de PTO paso a paso — la fórmula, las tasas de acumulación por período de pago, por horas frente a asalariado y ejemplos resueltos que puede copiar. Además, una FAQ rápida.',
            'Come calcolare la maturazione dei PTO passo dopo passo — la formula, i tassi di maturazione per periodo di paga, a ore o a stipendio ed esempi svolti da copiare. In più, una breve FAQ.',
            'PTO-opbouw stap voor stap berekenen — de formule, opbouwtempo\'s per loonperiode, uur- versus salarismedewerkers en uitgewerkte voorbeelden om te kopiëren. Plus een korte FAQ.'),
        'The PTO accrual formula, rates by pay period, hourly vs salaried, and worked examples you can copy.': _t(
            "La formule d'acquisition de PTO, les taux par période de paie, horaire ou salarié, et des exemples chiffrés à copier.",
            'Die PTO-Ansammlungsformel, Sätze je Abrechnungszeitraum, Stunden- vs. Gehaltskräfte und durchgerechnete Beispiele zum Kopieren.',
            'La fórmula de acumulación de PTO, las tasas por período de pago, por horas frente a asalariado y ejemplos resueltos que puede copiar.',
            'La formula di maturazione dei PTO, i tassi per periodo di paga, a ore o a stipendio ed esempi svolti da copiare.',
            'De PTO-opbouwformule, tempo\'s per loonperiode, uur- versus salarismedewerkers en uitgewerkte voorbeelden om te kopiëren.'),
        'September 9, 2026': _t('9 septembre 2026', '9. September 2026', '9 de septiembre de 2026', '9 settembre 2026', '9 september 2026'),
        '6 min read': _t('6 min de lecture', '6 Min. Lesezeit', '6 min de lectura', '6 min di lettura', '6 min leestijd'),
        # ---- Body ----
        "<strong>The short answer:</strong> to calculate PTO accrual, divide the paid time off an employee earns in a year by the time they work in a year. Per hour worked, that's <strong>annual PTO hours &divide; annual work hours</strong>. Per paycheck, it's <strong>annual PTO hours &divide; number of pay periods</strong>. Everything below is just applying that with real numbers.": _t(
            "<strong>La réponse courte :</strong> pour calculer l'acquisition de PTO, divisez les congés payés qu'un employé acquiert dans l'année par le temps qu'il travaille dans l'année. Par heure travaillée, c'est <strong>heures de PTO annuelles &divide; heures de travail annuelles</strong>. Par paie, c'est <strong>heures de PTO annuelles &divide; nombre de périodes de paie</strong>. Tout ce qui suit ne fait qu'appliquer cela avec des chiffres réels.",
            '<strong>Die kurze Antwort:</strong> Um die PTO-Ansammlung zu berechnen, teilen Sie die bezahlte Freizeit, die ein Mitarbeiter in einem Jahr erwirbt, durch die Zeit, die er in einem Jahr arbeitet. Pro geleisteter Stunde ist das <strong>jährliche PTO-Stunden &divide; jährliche Arbeitsstunden</strong>. Pro Gehaltsabrechnung ist es <strong>jährliche PTO-Stunden &divide; Anzahl der Abrechnungszeiträume</strong>. Alles Weitere wendet das nur mit echten Zahlen an.',
            '<strong>La respuesta corta:</strong> para calcular la acumulación de PTO, divida el tiempo libre remunerado que un empleado acumula en un año entre el tiempo que trabaja en un año. Por hora trabajada, es <strong>horas anuales de PTO &divide; horas anuales de trabajo</strong>. Por nómina, es <strong>horas anuales de PTO &divide; número de períodos de pago</strong>. Todo lo que sigue no es más que aplicar eso con números reales.',
            "<strong>La risposta breve:</strong> per calcolare la maturazione dei PTO, dividi le ferie retribuite che un dipendente matura in un anno per il tempo che lavora in un anno. Per ora lavorata, è <strong>ore annue di PTO &divide; ore annue di lavoro</strong>. Per busta paga, è <strong>ore annue di PTO &divide; numero di periodi di paga</strong>. Tutto ciò che segue non fa che applicarlo con numeri reali.",
            '<strong>Het korte antwoord:</strong> om PTO-opbouw te berekenen, deelt u het betaald verlof dat een medewerker in een jaar opbouwt door de tijd die hij in een jaar werkt. Per gewerkt uur is dat <strong>jaarlijkse PTO-uren &divide; jaarlijkse werkuren</strong>. Per loonstrook is het <strong>jaarlijkse PTO-uren &divide; aantal loonperioden</strong>. Alles hieronder past dat gewoon toe met echte getallen.'),
        'What is PTO accrual?': _t("Qu'est-ce que l'acquisition de PTO ?", 'Was ist PTO-Ansammlung?', '¿Qué es la acumulación de PTO?', 'Che cos\'è la maturazione dei PTO?', 'Wat is PTO-opbouw?'),
        "PTO accrual means employees earn their paid time off gradually as they work, rather than receiving the whole year's balance up front. Someone might earn a few hours every paycheck, so by mid-year they've banked roughly half their annual allowance. It's the fairer, more common alternative to a lump-sum grant — especially for hourly staff and new hires.": _t(
            "L'acquisition de PTO signifie que les employés acquièrent leurs congés payés progressivement à mesure qu'ils travaillent, plutôt que de recevoir d'emblée le solde de toute l'année. Une personne peut acquérir quelques heures à chaque paie, de sorte qu'à la mi-année elle a accumulé environ la moitié de son droit annuel. C'est l'alternative plus équitable et plus courante à une attribution forfaitaire — surtout pour le personnel horaire et les nouvelles recrues.",
            'PTO-Ansammlung bedeutet, dass Mitarbeiter ihre bezahlte Freizeit schrittweise mit ihrer Arbeit erwerben, statt das Guthaben des ganzen Jahres im Voraus zu erhalten. Jemand erwirbt vielleicht ein paar Stunden pro Gehaltsabrechnung, sodass er zur Jahresmitte etwa die Hälfte seines Jahresanspruchs angesammelt hat. Es ist die fairere, gängigere Alternative zu einer Einmalgewährung — besonders für Stundenkräfte und neue Mitarbeiter.',
            'La acumulación de PTO significa que los empleados acumulan su tiempo libre remunerado de forma gradual a medida que trabajan, en lugar de recibir el saldo de todo el año por adelantado. Alguien puede acumular unas horas en cada nómina, de modo que a mitad de año ha reunido aproximadamente la mitad de su asignación anual. Es la alternativa más justa y habitual a una concesión de una sola vez — sobre todo para el personal por horas y las nuevas contrataciones.',
            "La maturazione dei PTO significa che i dipendenti maturano le loro ferie retribuite gradualmente man mano che lavorano, invece di ricevere in anticipo il saldo dell'intero anno. Qualcuno può maturare qualche ora a ogni busta paga, così a metà anno ha accumulato all'incirca metà della sua dotazione annuale. È l'alternativa più equa e più comune a un'assegnazione forfettaria — soprattutto per il personale a ore e i nuovi assunti.",
            'PTO-opbouw betekent dat medewerkers hun betaald verlof geleidelijk opbouwen naarmate ze werken, in plaats van het saldo van het hele jaar vooraf te ontvangen. Iemand bouwt misschien een paar uur op per loonstrook, zodat hij halverwege het jaar ongeveer de helft van zijn jaarlijkse tegoed heeft opgebouwd. Het is het eerlijkere, gangbaardere alternatief voor een toekenning ineens — vooral voor uurmedewerkers en nieuwe medewerkers.'),
        'The PTO accrual formula': _t("La formule d'acquisition de PTO", 'Die PTO-Ansammlungsformel', 'La fórmula de acumulación de PTO', 'La formula di maturazione dei PTO', 'De PTO-opbouwformule'),
        "Start with two numbers: how much PTO the employee gets per year, and the period you're accruing over. Then:": _t(
            "Commencez par deux chiffres : combien de PTO l'employé reçoit par an et la période sur laquelle vous calculez l'acquisition. Ensuite :",
            'Beginnen Sie mit zwei Zahlen: wie viel PTO der Mitarbeiter pro Jahr erhält und über welchen Zeitraum Sie ansammeln. Dann:',
            'Empiece con dos cifras: cuánto PTO recibe el empleado al año y el período sobre el que acumula. Luego:',
            'Parti da due numeri: quanto PTO riceve il dipendente all\'anno e il periodo su cui calcoli la maturazione. Poi:',
            'Begin met twee getallen: hoeveel PTO de medewerker per jaar krijgt en de periode waarover u opbouwt. Dan:'),
        '<strong>Per hour worked:</strong> annual PTO hours &divide; annual work hours': _t(
            '<strong>Par heure travaillée :</strong> heures de PTO annuelles &divide; heures de travail annuelles',
            '<strong>Pro geleisteter Stunde:</strong> jährliche PTO-Stunden &divide; jährliche Arbeitsstunden',
            '<strong>Por hora trabajada:</strong> horas anuales de PTO &divide; horas anuales de trabajo',
            '<strong>Per ora lavorata:</strong> ore annue di PTO &divide; ore annue di lavoro',
            '<strong>Per gewerkt uur:</strong> jaarlijkse PTO-uren &divide; jaarlijkse werkuren'),
        '<strong>Per pay period:</strong> annual PTO hours &divide; number of pay periods in the year': _t(
            "<strong>Par période de paie :</strong> heures de PTO annuelles &divide; nombre de périodes de paie dans l'année",
            '<strong>Pro Abrechnungszeitraum:</strong> jährliche PTO-Stunden &divide; Anzahl der Abrechnungszeiträume im Jahr',
            '<strong>Por período de pago:</strong> horas anuales de PTO &divide; número de períodos de pago en el año',
            "<strong>Per periodo di paga:</strong> ore annue di PTO &divide; numero di periodi di paga nell'anno",
            '<strong>Per loonperiode:</strong> jaarlijkse PTO-uren &divide; aantal loonperioden in het jaar'),
        'A standard full-time year is <strong>2,080 hours</strong> (40 hours &times; 52 weeks). Pay periods depend on your schedule: 52 weekly, 26 biweekly, 24 semi-monthly, or 12 monthly.': _t(
            'Une année standard à temps plein compte <strong>2,080 heures</strong> (40 heures &times; 52 semaines). Les périodes de paie dépendent de votre calendrier : 52 par semaine, 26 toutes les deux semaines, 24 deux fois par mois ou 12 par mois.',
            'Ein normales Vollzeitjahr hat <strong>2,080 Stunden</strong> (40 Stunden &times; 52 Wochen). Die Abrechnungszeiträume hängen von Ihrem Zeitplan ab: 52 wöchentlich, 26 zweiwöchentlich, 24 halbmonatlich oder 12 monatlich.',
            'Un año estándar a tiempo completo son <strong>2,080 horas</strong> (40 horas &times; 52 semanas). Los períodos de pago dependen de su calendario: 52 semanales, 26 cada dos semanas, 24 dos veces al mes o 12 mensuales.',
            'Un anno standard a tempo pieno è di <strong>2,080 ore</strong> (40 ore &times; 52 settimane). I periodi di paga dipendono dal tuo calendario: 52 settimanali, 26 ogni due settimane, 24 due volte al mese o 12 mensili.',
            'Een standaard voltijdjaar is <strong>2,080 uur</strong> (40 uur &times; 52 weken). De loonperioden hangen af van uw schema: 52 wekelijks, 26 tweewekelijks, 24 twee keer per maand of 12 maandelijks.'),
        'How to calculate the accrual rate per hour worked': _t(
            "Comment calculer le taux d'acquisition par heure travaillée",
            'So berechnen Sie den Ansammlungssatz pro geleisteter Stunde',
            'Cómo calcular la tasa de acumulación por hora trabajada',
            'Come calcolare il tasso di maturazione per ora lavorata',
            'Hoe u het opbouwtempo per gewerkt uur berekent'),
        'Use this when PTO should track actual hours — the standard approach for hourly and part-time staff.': _t(
            "Utilisez ceci lorsque le PTO doit suivre les heures réelles — l'approche standard pour le personnel horaire et à temps partiel.",
            'Verwenden Sie dies, wenn PTO die tatsächlichen Stunden abbilden soll — der Standardansatz für Stunden- und Teilzeitkräfte.',
            'Use esto cuando el PTO deba seguir las horas reales — el enfoque estándar para el personal por horas y a tiempo parcial.',
            "Usa questo quando i PTO devono seguire le ore effettive — l'approccio standard per il personale a ore e part-time.",
            'Gebruik dit wanneer PTO de werkelijke uren moet volgen — de standaardaanpak voor uur- en deeltijdmedewerkers.'),
        '<strong>Example:</strong> a full-time employee gets 10 days (80 hours) of PTO a year.': _t(
            '<strong>Exemple :</strong> un employé à temps plein reçoit 10 jours (80 heures) de PTO par an.',
            '<strong>Beispiel:</strong> Ein Vollzeitmitarbeiter erhält 10 Tage (80 Stunden) PTO pro Jahr.',
            '<strong>Ejemplo:</strong> un empleado a tiempo completo recibe 10 días (80 horas) de PTO al año.',
            "<strong>Esempio:</strong> un dipendente a tempo pieno riceve 10 giorni (80 ore) di PTO all'anno.",
            '<strong>Voorbeeld:</strong> een voltijdmedewerker krijgt 10 dagen (80 uur) PTO per jaar.'),
        '80 PTO hours &divide; 2,080 work hours = <strong>0.0385 hours of PTO per hour worked</strong>': _t(
            '80 heures de PTO &divide; 2,080 heures de travail = <strong>0.0385 heure de PTO par heure travaillée</strong>',
            '80 PTO-Stunden &divide; 2,080 Arbeitsstunden = <strong>0.0385 Stunden PTO pro geleisteter Stunde</strong>',
            '80 horas de PTO &divide; 2,080 horas de trabajo = <strong>0.0385 horas de PTO por hora trabajada</strong>',
            '80 ore di PTO &divide; 2,080 ore di lavoro = <strong>0.0385 ore di PTO per ora lavorata</strong>',
            '80 PTO-uur &divide; 2,080 werkuur = <strong>0.0385 uur PTO per gewerkt uur</strong>'),
        'So an 80-hour biweekly paycheck earns 80 &times; 0.0385 = <strong>~3.08 hours</strong> of PTO': _t(
            'Ainsi, une paie de 80 heures versée toutes les deux semaines rapporte 80 &times; 0.0385 = <strong>~3.08 heures</strong> de PTO',
            'Eine zweiwöchentliche Gehaltsabrechnung über 80 Stunden ergibt also 80 &times; 0.0385 = <strong>~3.08 Stunden</strong> PTO',
            'Así, una nómina de 80 horas cada dos semanas genera 80 &times; 0.0385 = <strong>~3.08 horas</strong> de PTO',
            'Così una busta paga di 80 ore ogni due settimane matura 80 &times; 0.0385 = <strong>~3.08 ore</strong> di PTO',
            'Zo levert een tweewekelijkse loonstrook van 80 uur 80 &times; 0.0385 = <strong>~3.08 uur</strong> PTO op'),
        'A part-timer who worked 50 hours that period earns 50 &times; 0.0385 = <strong>~1.92 hours</strong>': _t(
            'Un employé à temps partiel qui a travaillé 50 heures sur la période acquiert 50 &times; 0.0385 = <strong>~1.92 heure</strong>',
            'Eine Teilzeitkraft, die in diesem Zeitraum 50 Stunden gearbeitet hat, erwirbt 50 &times; 0.0385 = <strong>~1.92 Stunden</strong>',
            'Un empleado a tiempo parcial que trabajó 50 horas en ese período genera 50 &times; 0.0385 = <strong>~1.92 horas</strong>',
            'Un part-time che ha lavorato 50 ore nel periodo matura 50 &times; 0.0385 = <strong>~1.92 ore</strong>',
            'Een deeltijdmedewerker die die periode 50 uur werkte, bouwt 50 &times; 0.0385 = <strong>~1.92 uur</strong> op'),
        'How to calculate accrual per pay period': _t(
            "Comment calculer l'acquisition par période de paie",
            'So berechnen Sie die Ansammlung pro Abrechnungszeitraum',
            'Cómo calcular la acumulación por período de pago',
            'Come calcolare la maturazione per periodo di paga',
            'Hoe u de opbouw per loonperiode berekent'),
        'Use this for salaried staff, where each paycheck simply adds a fixed amount.': _t(
            'Utilisez ceci pour le personnel salarié, où chaque paie ajoute simplement un montant fixe.',
            'Verwenden Sie dies für Gehaltsempfänger, bei denen jede Abrechnung einfach einen festen Betrag hinzufügt.',
            'Use esto para el personal asalariado, donde cada nómina simplemente suma una cantidad fija.',
            'Usa questo per il personale a stipendio, dove ogni busta paga aggiunge semplicemente un importo fisso.',
            'Gebruik dit voor medewerkers met salaris, waar elke loonstrook simpelweg een vast bedrag toevoegt.'),
        '<strong>Example:</strong> the same 80 hours of annual PTO, paid biweekly (26 periods):': _t(
            '<strong>Exemple :</strong> les mêmes 80 heures de PTO annuel, versées toutes les deux semaines (26 périodes) :',
            '<strong>Beispiel:</strong> dieselben 80 Stunden Jahres-PTO, zweiwöchentlich ausgezahlt (26 Zeiträume):',
            '<strong>Ejemplo:</strong> las mismas 80 horas de PTO anual, pagadas cada dos semanas (26 períodos):',
            '<strong>Esempio:</strong> le stesse 80 ore di PTO annuo, pagate ogni due settimane (26 periodi):',
            '<strong>Voorbeeld:</strong> dezelfde 80 uur jaarlijkse PTO, tweewekelijks uitbetaald (26 perioden):'),
        '80 &divide; 26 = <strong>~3.08 hours per paycheck</strong>': _t(
            '80 &divide; 26 = <strong>~3.08 heures par paie</strong>',
            '80 &divide; 26 = <strong>~3.08 Stunden pro Abrechnung</strong>',
            '80 &divide; 26 = <strong>~3.08 horas por nómina</strong>',
            '80 &divide; 26 = <strong>~3.08 ore per busta paga</strong>',
            '80 &divide; 26 = <strong>~3.08 uur per loonstrook</strong>'),
        'Weekly (52): 80 &divide; 52 = ~1.54 hours': _t(
            'Hebdomadaire (52) : 80 &divide; 52 = ~1.54 heure',
            'Wöchentlich (52): 80 &divide; 52 = ~1.54 Stunden',
            'Semanal (52): 80 &divide; 52 = ~1.54 horas',
            'Settimanale (52): 80 &divide; 52 = ~1.54 ore',
            'Wekelijks (52): 80 &divide; 52 = ~1.54 uur'),
        'Semi-monthly (24): 80 &divide; 24 = ~3.33 hours': _t(
            'Deux fois par mois (24) : 80 &divide; 24 = ~3.33 heures',
            'Halbmonatlich (24): 80 &divide; 24 = ~3.33 Stunden',
            'Dos veces al mes (24): 80 &divide; 24 = ~3.33 horas',
            'Due volte al mese (24): 80 &divide; 24 = ~3.33 ore',
            'Twee keer per maand (24): 80 &divide; 24 = ~3.33 uur'),
        'Monthly (12): 80 &divide; 12 = ~6.67 hours': _t(
            'Mensuel (12) : 80 &divide; 12 = ~6.67 heures',
            'Monatlich (12): 80 &divide; 12 = ~6.67 Stunden',
            'Mensual (12): 80 &divide; 12 = ~6.67 horas',
            'Mensile (12): 80 &divide; 12 = ~6.67 ore',
            'Maandelijks (12): 80 &divide; 12 = ~6.67 uur'),
        'For a more generous 15-day (120-hour) policy, just swap the numerator: 120 &divide; 26 = ~4.62 hours biweekly; 20 days (160 hours) = 160 &divide; 26 = ~6.15 hours.': _t(
            'Pour une politique plus généreuse de 15 jours (120 heures), il suffit de changer le numérateur : 120 &divide; 26 = ~4.62 heures toutes les deux semaines ; 20 jours (160 heures) = 160 &divide; 26 = ~6.15 heures.',
            'Für eine großzügigere Regelung von 15 Tagen (120 Stunden) tauschen Sie einfach den Zähler: 120 &divide; 26 = ~4.62 Stunden zweiwöchentlich; 20 Tage (160 Stunden) = 160 &divide; 26 = ~6.15 Stunden.',
            'Para una política más generosa de 15 días (120 horas), basta con cambiar el numerador: 120 &divide; 26 = ~4.62 horas cada dos semanas; 20 días (160 horas) = 160 &divide; 26 = ~6.15 horas.',
            'Per una politica più generosa di 15 giorni (120 ore), basta cambiare il numeratore: 120 &divide; 26 = ~4.62 ore ogni due settimane; 20 giorni (160 ore) = 160 &divide; 26 = ~6.15 ore.',
            'Voor een genereuzer beleid van 15 dagen (120 uur) verwisselt u gewoon de teller: 120 &divide; 26 = ~4.62 uur tweewekelijks; 20 dagen (160 uur) = 160 &divide; 26 = ~6.15 uur.'),
        'Three rules that keep accrual clean': _t(
            "Trois règles qui gardent l'acquisition propre",
            'Drei Regeln, die die Ansammlung sauber halten',
            'Tres reglas que mantienen limpia la acumulación',
            'Tre regole che mantengono pulita la maturazione',
            'Drie regels die de opbouw zuiver houden'),
        '<strong>Set a cap or carryover rule.</strong> Decide the maximum balance an employee can bank, and whether unused time rolls over, is paid out, or is lost at year-end. Without a cap, balances grow into a real liability.': _t(
            "<strong>Fixez un plafond ou une règle de report.</strong> Décidez du solde maximum qu'un employé peut accumuler et si le temps non utilisé est reporté, payé ou perdu en fin d'année. Sans plafond, les soldes deviennent un vrai passif.",
            '<strong>Legen Sie eine Obergrenze oder Übertragungsregel fest.</strong> Entscheiden Sie, welches Höchstguthaben ein Mitarbeiter ansammeln kann und ob nicht genutzte Zeit übertragen, ausgezahlt oder zum Jahresende verfällt. Ohne Obergrenze werden Guthaben zu einer echten Verbindlichkeit.',
            '<strong>Establezca un tope o una regla de traspaso.</strong> Decida el saldo máximo que un empleado puede acumular y si el tiempo no usado se traspasa, se abona o se pierde a fin de año. Sin un tope, los saldos se convierten en un pasivo real.',
            '<strong>Fissa un tetto o una regola di riporto.</strong> Decidi il saldo massimo che un dipendente può accumulare e se il tempo non usato viene riportato, pagato o perso a fine anno. Senza un tetto, i saldi diventano una vera passività.',
            '<strong>Stel een maximum of overdrachtsregel in.</strong> Bepaal het maximale saldo dat een medewerker kan opbouwen en of ongebruikte tijd wordt overgedragen, uitbetaald of aan het einde van het jaar vervalt. Zonder maximum groeien saldi uit tot een echte verplichting.'),
        '<strong>Decide what hours count.</strong> Does PTO accrue on overtime? On other paid leave? Most policies accrue on regular hours only — write it down and apply it consistently.': _t(
            "<strong>Décidez quelles heures comptent.</strong> Le PTO s'acquiert-il sur les heures supplémentaires ? Sur d'autres congés payés ? La plupart des politiques n'accumulent que sur les heures normales — mettez-le par écrit et appliquez-le de façon cohérente.",
            '<strong>Entscheiden Sie, welche Stunden zählen.</strong> Sammelt sich PTO auf Überstunden an? Auf anderen bezahlten Urlaub? Die meisten Regelungen sammeln nur auf reguläre Stunden an — halten Sie es schriftlich fest und wenden Sie es konsequent an.',
            '<strong>Decida qué horas cuentan.</strong> ¿El PTO se acumula sobre las horas extra? ¿Sobre otros permisos retribuidos? La mayoría de las políticas acumulan solo sobre las horas normales — póngalo por escrito y aplíquelo de forma coherente.',
            '<strong>Decidi quali ore contano.</strong> I PTO maturano sugli straordinari? Su altri congedi retribuiti? La maggior parte delle politiche matura solo sulle ore ordinarie — mettilo per iscritto e applicalo in modo coerente.',
            '<strong>Bepaal welke uren meetellen.</strong> Bouwt PTO op over overuren? Over ander betaald verlof? De meeste regelingen bouwen alleen op over normale uren — leg het vast en pas het consistent toe.'),
        "<strong>Round the same way for everyone.</strong> Pick a rounding rule (say, to two decimals or the nearest quarter-hour) and use it across the board so no one's balance drifts.": _t(
            "<strong>Arrondissez de la même façon pour tous.</strong> Choisissez une règle d'arrondi (par exemple, à deux décimales ou au quart d'heure le plus proche) et appliquez-la à tous, pour qu'aucun solde ne dérive.",
            '<strong>Runden Sie für alle gleich.</strong> Wählen Sie eine Rundungsregel (etwa auf zwei Dezimalstellen oder die nächste Viertelstunde) und wenden Sie sie durchgängig an, damit kein Guthaben abdriftet.',
            '<strong>Redondee igual para todos.</strong> Elija una regla de redondeo (por ejemplo, a dos decimales o al cuarto de hora más cercano) y aplíquela a todos, para que ningún saldo se desvíe.',
            "<strong>Arrotonda allo stesso modo per tutti.</strong> Scegli una regola di arrotondamento (ad esempio, a due decimali o al quarto d'ora più vicino) e usala per tutti, così nessun saldo va alla deriva.",
            '<strong>Rond voor iedereen op dezelfde manier af.</strong> Kies een afrondingsregel (bijvoorbeeld op twee decimalen of het dichtstbijzijnde kwartier) en pas die overal toe, zodat niemands saldo afwijkt.'),
        # ---- FAQ ----
        'How many PTO days is two weeks?': _t(
            'Combien de jours de PTO représentent deux semaines ?',
            'Wie viele PTO-Tage sind zwei Wochen?',
            '¿Cuántos días de PTO son dos semanas?',
            'Quanti giorni di PTO sono due settimane?',
            'Hoeveel PTO-dagen zijn twee weken?'),
        'For a full-time employee working 8-hour days, two weeks of PTO is 10 working days, or 80 hours. Most companies track PTO in hours rather than days so it works cleanly for part-time and hourly staff too.': _t(
            "Pour un employé à temps plein travaillant des journées de 8 heures, deux semaines de PTO représentent 10 jours ouvrés, soit 80 heures. La plupart des entreprises suivent le PTO en heures plutôt qu'en jours, pour que cela fonctionne aussi proprement pour le personnel à temps partiel et horaire.",
            'Für einen Vollzeitmitarbeiter mit 8-Stunden-Tagen sind zwei Wochen PTO 10 Arbeitstage oder 80 Stunden. Die meisten Unternehmen erfassen PTO in Stunden statt in Tagen, damit es auch für Teilzeit- und Stundenkräfte sauber funktioniert.',
            'Para un empleado a tiempo completo con jornadas de 8 horas, dos semanas de PTO son 10 días laborables, o 80 horas. La mayoría de las empresas registran el PTO en horas en lugar de días para que funcione con claridad también para el personal a tiempo parcial y por horas.',
            'Per un dipendente a tempo pieno con giornate di 8 ore, due settimane di PTO sono 10 giorni lavorativi, ovvero 80 ore. La maggior parte delle aziende registra i PTO in ore anziché in giorni, così funziona in modo pulito anche per il personale part-time e a ore.',
            'Voor een voltijdmedewerker met werkdagen van 8 uur zijn twee weken PTO 10 werkdagen, oftewel 80 uur. De meeste bedrijven houden PTO bij in uren in plaats van dagen, zodat het ook voor deeltijd- en uurmedewerkers netjes werkt.'),
        'How do you calculate a PTO accrual rate per hour worked?': _t(
            "Comment calcule-t-on un taux d'acquisition de PTO par heure travaillée ?",
            'Wie berechnet man einen PTO-Ansammlungssatz pro geleisteter Stunde?',
            '¿Cómo se calcula una tasa de acumulación de PTO por hora trabajada?',
            'Come si calcola un tasso di maturazione dei PTO per ora lavorata?',
            'Hoe berekent u een PTO-opbouwtempo per gewerkt uur?'),
        "Divide the annual PTO hours by the number of hours worked in a year. For 80 hours (10 days) of PTO and a 2,080-hour work year, that's 80 &divide; 2,080 = 0.0385 hours of PTO earned per hour worked.": _t(
            "Divisez les heures de PTO annuelles par le nombre d'heures travaillées dans l'année. Pour 80 heures (10 jours) de PTO et une année de travail de 2,080 heures, cela donne 80 &divide; 2,080 = 0.0385 heure de PTO acquise par heure travaillée.",
            'Teilen Sie die jährlichen PTO-Stunden durch die Anzahl der in einem Jahr geleisteten Stunden. Bei 80 Stunden (10 Tagen) PTO und einem Arbeitsjahr von 2,080 Stunden ergibt das 80 &divide; 2,080 = 0.0385 Stunden PTO pro geleisteter Stunde.',
            'Divida las horas anuales de PTO entre el número de horas trabajadas en un año. Para 80 horas (10 días) de PTO y un año laboral de 2,080 horas, eso es 80 &divide; 2,080 = 0.0385 horas de PTO ganadas por hora trabajada.',
            'Dividi le ore annue di PTO per il numero di ore lavorate in un anno. Per 80 ore (10 giorni) di PTO e un anno lavorativo di 2,080 ore, è 80 &divide; 2,080 = 0.0385 ore di PTO maturate per ora lavorata.',
            'Deel de jaarlijkse PTO-uren door het aantal in een jaar gewerkte uren. Voor 80 uur (10 dagen) PTO en een werkjaar van 2,080 uur is dat 80 &divide; 2,080 = 0.0385 uur PTO per gewerkt uur.'),
        'What is a typical PTO accrual rate?': _t(
            "Quel est un taux d'acquisition de PTO typique ?",
            'Wie hoch ist ein typischer PTO-Ansammlungssatz?',
            '¿Cuál es una tasa de acumulación de PTO típica?',
            'Qual è un tasso di maturazione dei PTO tipico?',
            'Wat is een typisch PTO-opbouwtempo?'),
        'Many employers offer 10 to 20 days (80 to 160 hours) of PTO per year, often rising with tenure. On a biweekly schedule that works out to roughly 3.08 to 6.15 hours accrued each pay period.': _t(
            "De nombreux employeurs offrent de 10 à 20 jours (80 à 160 heures) de PTO par an, souvent en augmentant avec l'ancienneté. Sur un calendrier de paie toutes les deux semaines, cela revient à environ 3.08 à 6.15 heures acquises à chaque période de paie.",
            'Viele Arbeitgeber bieten 10 bis 20 Tage (80 bis 160 Stunden) PTO pro Jahr, oft steigend mit der Betriebszugehörigkeit. Bei einem zweiwöchentlichen Zeitplan ergibt das etwa 3.08 bis 6.15 Stunden, die pro Abrechnungszeitraum angesammelt werden.',
            'Muchos empleadores ofrecen de 10 a 20 días (80 a 160 horas) de PTO al año, que suelen aumentar con la antigüedad. En un calendario de pago cada dos semanas, eso equivale a entre 3.08 y 6.15 horas acumuladas en cada período de pago.',
            "Molti datori di lavoro offrono da 10 a 20 giorni (80-160 ore) di PTO all'anno, spesso in aumento con l'anzianità. Con un calendario di paga ogni due settimane, ciò equivale a circa 3.08-6.15 ore maturate a ogni periodo di paga.",
            'Veel werkgevers bieden 10 tot 20 dagen (80 tot 160 uur) PTO per jaar, vaak oplopend met de anciënniteit. Bij een tweewekelijks schema komt dat neer op ongeveer 3.08 tot 6.15 uur die per loonperiode wordt opgebouwd.'),
        'Does PTO accrue on overtime hours?': _t(
            "Le PTO s'acquiert-il sur les heures supplémentaires ?",
            'Sammelt sich PTO auf Überstunden an?',
            '¿El PTO se acumula sobre las horas extra?',
            'I PTO maturano sulle ore di straordinario?',
            'Bouwt PTO op over overuren?'),
        "That's a policy choice. Many employers accrue PTO only on regular hours up to a set cap and exclude overtime — but you should define it clearly in your policy and apply it the same way for everyone.": _t(
            "C'est un choix de politique. De nombreux employeurs n'accumulent le PTO que sur les heures normales jusqu'à un plafond défini et excluent les heures supplémentaires — mais vous devez le définir clairement dans votre politique et l'appliquer de la même façon pour tous.",
            'Das ist eine Frage der Regelung. Viele Arbeitgeber sammeln PTO nur auf reguläre Stunden bis zu einer festgelegten Obergrenze an und schließen Überstunden aus — aber Sie sollten es in Ihrer Regelung klar definieren und für alle gleich anwenden.',
            'Es una decisión de política. Muchos empleadores acumulan PTO solo sobre las horas normales hasta un tope fijado y excluyen las horas extra — pero debe definirlo con claridad en su política y aplicarlo igual para todos.',
            'È una scelta di policy. Molti datori di lavoro maturano i PTO solo sulle ore ordinarie fino a un tetto stabilito ed escludono gli straordinari — ma dovresti definirlo chiaramente nella tua policy e applicarlo allo stesso modo per tutti.',
            'Dat is een beleidskeuze. Veel werkgevers bouwen PTO alleen op over normale uren tot een vastgesteld maximum en sluiten overuren uit — maar u moet het duidelijk in uw beleid vastleggen en voor iedereen op dezelfde manier toepassen.'),
        # ---- Read next ----
        "The math is simple; keeping every balance right across a whole team, every pay period, is where it gets fiddly. That's what a system is for — accruing automatically, applying your caps and carryover rules, and showing each person their live balance. For the policy decisions behind the numbers, see our guide to <a href=\"/blog/pto-policy/\">building a PTO policy</a>, and if you're setting up people operations from scratch, our <a href=\"/blog/employee-onboarding-checklist/\">employee onboarding checklist</a> and guide to <a href=\"/blog/hr-software-small-business/\">HR software for small businesses</a> cover the rest.": _t(
            "Le calcul est simple ; garder chaque solde juste pour toute une équipe, à chaque période de paie, voilà où cela devient délicat. C'est à cela que sert un système — acquérir automatiquement, appliquer vos plafonds et vos règles de report, et montrer à chacun son solde en direct. Pour les décisions de politique derrière les chiffres, consultez notre guide sur <a href=\"/blog/pto-policy/\">l'élaboration d'une politique de PTO</a>, et si vous mettez en place la gestion du personnel de zéro, notre <a href=\"/blog/employee-onboarding-checklist/\">liste de contrôle d'intégration des employés</a> et notre guide sur le <a href=\"/blog/hr-software-small-business/\">logiciel HR pour petites entreprises</a> couvrent le reste.",
            "Die Rechnung ist einfach; jeden Saldo für ein ganzes Team in jedem Abrechnungszeitraum korrekt zu halten, wird zur Fummelei. Genau dafür ist ein System da — automatisch ansammeln, Ihre Obergrenzen und Übertragungsregeln anwenden und jedem seinen Live-Saldo zeigen. Für die Regelungsentscheidungen hinter den Zahlen siehe unseren Leitfaden zum <a href=\"/blog/pto-policy/\">Erstellen einer PTO-Richtlinie</a>, und wenn Sie das Personalmanagement von Grund auf aufbauen, decken unsere <a href=\"/blog/employee-onboarding-checklist/\">Checkliste für das Mitarbeiter-Onboarding</a> und unser Leitfaden zu <a href=\"/blog/hr-software-small-business/\">HR-Software für kleine Unternehmen</a> den Rest ab.",
            "El cálculo es simple; mantener cada saldo correcto en todo un equipo, en cada período de pago, es donde se vuelve engorroso. Para eso sirve un sistema — acumular automáticamente, aplicar sus topes y reglas de traspaso y mostrar a cada persona su saldo en directo. Para las decisiones de política detrás de los números, consulte nuestra guía sobre <a href=\"/blog/pto-policy/\">la creación de una política de PTO</a>, y si está montando la gestión de personas desde cero, nuestra <a href=\"/blog/employee-onboarding-checklist/\">lista de incorporación de empleados</a> y nuestra guía sobre <a href=\"/blog/hr-software-small-business/\">software de HR para pequeñas empresas</a> cubren el resto.",
            "Il calcolo è semplice; tenere ogni saldo corretto per un intero team, a ogni periodo di paga, è dove diventa complicato. È a questo che serve un sistema — maturare automaticamente, applicare i tuoi tetti e le regole di riporto e mostrare a ciascuno il proprio saldo in tempo reale. Per le decisioni di policy dietro i numeri, vedi la nostra guida alla <a href=\"/blog/pto-policy/\">creazione di una politica sui PTO</a>, e se stai impostando la gestione del personale da zero, la nostra <a href=\"/blog/employee-onboarding-checklist/\">checklist di onboarding dei dipendenti</a> e la guida al <a href=\"/blog/hr-software-small-business/\">software HR per piccole imprese</a> coprono il resto.",
            "De rekensom is eenvoudig; elk saldo correct houden voor een heel team, elke loonperiode, daar wordt het priegelig. Daar is een systeem voor — automatisch opbouwen, uw maxima en overdrachtsregels toepassen en iedereen zijn actuele saldo tonen. Voor de beleidskeuzes achter de cijfers, zie onze gids over <a href=\"/blog/pto-policy/\">het opstellen van een PTO-beleid</a>, en als u personeelsbeheer vanaf nul opzet, dekken onze <a href=\"/blog/employee-onboarding-checklist/\">onboardingchecklist voor medewerkers</a> en gids over <a href=\"/blog/hr-software-small-business/\">HR-software voor kleine bedrijven</a> de rest."),
        # ---- CTA ----
        'Let accruals run themselves': _t(
            'Laissez les acquisitions se gérer seules',
            'Lassen Sie Ansammlungen sich selbst erledigen',
            'Deje que las acumulaciones se gestionen solas',
            'Lascia che le maturazioni si gestiscano da sole',
            'Laat opbouw zichzelf regelen'),
        'HR Suite accrues PTO automatically on your schedule, applies your caps and carryover rules, and shows every employee their live balance — no spreadsheets, no month-end reconciling.': _t(
            'HR Suite acquiert le PTO automatiquement selon votre calendrier, applique vos plafonds et vos règles de report, et montre à chaque employé son solde en direct — sans tableurs, sans rapprochement de fin de mois.',
            'HR Suite sammelt PTO automatisch nach Ihrem Zeitplan an, wendet Ihre Obergrenzen und Übertragungsregeln an und zeigt jedem Mitarbeiter seinen Live-Saldo — keine Tabellen, kein Abgleich zum Monatsende.',
            'HR Suite acumula el PTO automáticamente según su calendario, aplica sus topes y reglas de traspaso y muestra a cada empleado su saldo en directo — sin hojas de cálculo, sin conciliaciones de fin de mes.',
            'HR Suite matura i PTO automaticamente secondo il tuo calendario, applica i tuoi tetti e le regole di riporto e mostra a ogni dipendente il proprio saldo in tempo reale — niente fogli di calcolo, niente riconciliazioni di fine mese.',
            'HR Suite bouwt PTO automatisch op volgens uw schema, past uw maxima en overdrachtsregels toe en toont elke medewerker zijn actuele saldo — geen spreadsheets, geen maandafsluiting.'),
    },
}

PAGE['/blog/hr-software-small-business/'] = {
    'src': 'blog/hr-software-small-business/index.html',
    't': {
        '>Home</a>': _HOME,
        'Explore HR Suite': _EXPLORE,
        'Back to the blog': _BACK,
        'FulcrumGrid HR Suite — people operations': _ALT,
        # ---- Title / meta ----
        "HR Software for Small Businesses: A Practical Buyer's Guide": _t(
            "Logiciel HR pour petites entreprises : guide d'achat pratique",
            'HR-Software für kleine Unternehmen: ein praktischer Kaufratgeber',
            'Software de HR para pequeñas empresas: una guía de compra práctica',
            "Software HR per piccole imprese: una guida pratica all'acquisto",
            'HR-software voor kleine bedrijven: een praktische aankoopgids'),
        'HR Software for Small Businesses': _t(
            'Logiciel HR pour petites entreprises',
            'HR-Software für kleine Unternehmen',
            'Software de HR para pequeñas empresas',
            'Software HR per piccole imprese',
            'HR-software voor kleine bedrijven'),
        'HR software for small business': _t(
            'Logiciel HR pour petites entreprises',
            'HR-Software für kleine Unternehmen',
            'Software de HR para pequeñas empresas',
            'Software HR per piccole imprese',
            'HR-software voor kleine bedrijven'),
        'Choosing your first HR system? The features that matter for a small business, the ones you can skip, and how to evaluate options without overbuying.': _t(
            "Vous choisissez votre premier système HR ? Les fonctionnalités qui comptent pour une petite entreprise, celles dont vous pouvez vous passer et comment évaluer les options sans surinvestir.",
            'Sie wählen Ihr erstes HR-System? Die Funktionen, die für ein kleines Unternehmen zählen, die, die Sie weglassen können, und wie Sie Optionen bewerten, ohne zu viel zu kaufen.',
            '¿Está eligiendo su primer sistema de HR? Las funciones que importan para una pequeña empresa, las que puede omitir y cómo evaluar opciones sin comprar de más.',
            'Stai scegliendo il tuo primo sistema HR? Le funzionalità che contano per una piccola impresa, quelle che puoi tralasciare e come valutare le opzioni senza comprare troppo.',
            'Kiest u uw eerste HR-systeem? De functies die tellen voor een klein bedrijf, die u kunt overslaan en hoe u opties beoordeelt zonder te veel te kopen.'),
        'The features that actually matter when choosing your first HR system — and the ones you can safely skip.': _t(
            'Les fonctionnalités qui comptent vraiment au moment de choisir votre premier système HR — et celles que vous pouvez sans risque laisser de côté.',
            'Die Funktionen, die bei der Wahl Ihres ersten HR-Systems wirklich zählen — und die, die Sie bedenkenlos weglassen können.',
            'Las funciones que de verdad importan al elegir su primer sistema de HR — y las que puede omitir sin problema.',
            'Le funzionalità che contano davvero quando scegli il tuo primo sistema HR — e quelle che puoi tranquillamente tralasciare.',
            'De functies die er echt toe doen bij het kiezen van uw eerste HR-systeem — en die u gerust kunt overslaan.'),
        'August 24, 2026': _t('24 août 2026', '24. August 2026', '24 de agosto de 2026', '24 agosto 2026', '24 augustus 2026'),
        '7 min read': _t('7 min de lecture', '7 Min. Lesezeit', '7 min de lectura', '7 min di lettura', '7 min leestijd'),
        # ---- Body ----
        "The first HR system a small business buys is usually bought too late — after a payroll mistake, a compliance scare, or the day someone can't remember who's on holiday next week. It's also frequently the wrong size: either a spreadsheet that's quietly falling apart, or an enterprise platform with 200 features you'll never touch.": _t(
            "Le premier système HR qu'une petite entreprise achète l'est généralement trop tard — après une erreur de paie, une frayeur de conformité ou le jour où plus personne ne se souvient qui est en congé la semaine prochaine. Il est aussi souvent de la mauvaise taille : soit un tableur qui s'effrite discrètement, soit une plateforme d'entreprise avec 200 fonctionnalités auxquelles vous ne toucherez jamais.",
            'Das erste HR-System, das ein kleines Unternehmen kauft, wird meist zu spät gekauft — nach einem Fehler in der Gehaltsabrechnung, einem Compliance-Schreck oder an dem Tag, an dem sich niemand mehr erinnert, wer nächste Woche im Urlaub ist. Es hat außerdem häufig die falsche Größe: entweder eine Tabelle, die still zerfällt, oder eine Unternehmensplattform mit 200 Funktionen, die Sie nie anrühren werden.',
            'El primer sistema de HR que compra una pequeña empresa suele comprarse demasiado tarde — tras un error de nómina, un susto de cumplimiento o el día en que nadie recuerda quién está de vacaciones la semana que viene. También suele ser del tamaño equivocado: o una hoja de cálculo que se desmorona en silencio, o una plataforma empresarial con 200 funciones que nunca tocará.',
            "Il primo sistema HR che una piccola impresa acquista di solito viene comprato troppo tardi — dopo un errore in busta paga, uno spavento sulla conformità o il giorno in cui nessuno ricorda chi è in ferie la settimana prossima. Spesso è anche della dimensione sbagliata: o un foglio di calcolo che si sgretola in silenzio, o una piattaforma enterprise con 200 funzionalità che non toccherai mai.",
            'Het eerste HR-systeem dat een klein bedrijf koopt, wordt meestal te laat gekocht — na een fout in de loonadministratie, een compliance-schrik of de dag dat niemand zich nog herinnert wie er volgende week met vakantie is. Het heeft ook vaak de verkeerde maat: ofwel een spreadsheet die stilletjes uit elkaar valt, ofwel een enterpriseplatform met 200 functies die u nooit zult aanraken.'),
        "Here's how to choose something that fits — the features that genuinely matter at small scale, the ones you can defer, and how to evaluate options without overpaying.": _t(
            "Voici comment choisir quelque chose d'adapté — les fonctionnalités qui comptent réellement à petite échelle, celles que vous pouvez reporter et comment évaluer les options sans payer trop cher.",
            'So wählen Sie etwas Passendes — die Funktionen, die im kleinen Maßstab wirklich zählen, die, die Sie aufschieben können, und wie Sie Optionen bewerten, ohne zu viel zu zahlen.',
            'Así se elige algo que encaje — las funciones que importan de verdad a pequeña escala, las que puede posponer y cómo evaluar opciones sin pagar de más.',
            'Ecco come scegliere qualcosa di adatto — le funzionalità che contano davvero su piccola scala, quelle che puoi rimandare e come valutare le opzioni senza pagare troppo.',
            'Zo kiest u iets dat past — de functies die er op kleine schaal echt toe doen, die u kunt uitstellen en hoe u opties beoordeelt zonder te veel te betalen.'),
        'The features that actually matter': _t(
            'Les fonctionnalités qui comptent vraiment', 'Die Funktionen, die wirklich zählen',
            'Las funciones que de verdad importan', 'Le funzionalità che contano davvero', 'De functies die er echt toe doen'),
        'For a team under roughly 100 people, these are the ones that earn their keep from day one:': _t(
            'Pour une équipe de moins de 100 personnes environ, voici celles qui justifient leur place dès le premier jour :',
            'Für ein Team von unter etwa 100 Personen sind das die, die sich vom ersten Tag an bezahlt machen:',
            'Para un equipo de menos de unas 100 personas, estas son las que se ganan su sitio desde el primer día:',
            'Per un team di meno di circa 100 persone, ecco quelle che si ripagano fin dal primo giorno:',
            'Voor een team van minder dan ongeveer 100 mensen zijn dit de functies die zich vanaf dag één terugbetalen:'),
        "<strong>A single employee record.</strong> One secure profile per person — documents, role, compensation, and history — so you're never digging through email threads and shared drives to answer a simple question.": _t(
            "<strong>Un dossier unique par employé.</strong> Un profil sécurisé par personne — documents, poste, rémunération et historique — pour ne jamais fouiller des fils d'e-mails et des disques partagés afin de répondre à une simple question.",
            '<strong>Eine einzige Mitarbeiterakte.</strong> Ein sicheres Profil pro Person — Dokumente, Rolle, Vergütung und Verlauf — damit Sie nie E-Mail-Verläufe und geteilte Laufwerke durchsuchen müssen, um eine einfache Frage zu beantworten.',
            '<strong>Un único expediente por empleado.</strong> Un perfil seguro por persona — documentos, puesto, retribución e historial — para no rebuscar nunca en hilos de correo y unidades compartidas para responder a una pregunta simple.',
            "<strong>Una scheda dipendente unica.</strong> Un profilo sicuro per persona — documenti, ruolo, retribuzione e storico — così non devi mai frugare tra thread di e-mail e dischi condivisi per rispondere a una domanda semplice.",
            '<strong>Eén medewerkersdossier.</strong> Eén beveiligd profiel per persoon — documenten, functie, beloning en geschiedenis — zodat u nooit door e-mailthreads en gedeelde schijven hoeft te spitten om een simpele vraag te beantwoorden.'),
        '<strong>Onboarding checklists.</strong> New hires involve the same dozen steps every time. A repeatable checklist with e-signatures turns a chaotic first week into a routine one.': _t(
            "<strong>Listes de contrôle d'intégration.</strong> Les nouvelles recrues impliquent la même douzaine d'étapes à chaque fois. Une liste de contrôle réutilisable avec signatures électroniques transforme une première semaine chaotique en une semaine de routine.",
            '<strong>Onboarding-Checklisten.</strong> Neueinstellungen umfassen jedes Mal dieselben zwölf Schritte. Eine wiederholbare Checkliste mit E-Signaturen macht aus einer chaotischen ersten Woche eine routinierte.',
            '<strong>Listas de incorporación.</strong> Las nuevas contrataciones implican la misma docena de pasos cada vez. Una lista repetible con firmas electrónicas convierte una primera semana caótica en una de rutina.',
            "<strong>Checklist di onboarding.</strong> Ogni nuovo assunto comporta ogni volta la stessa dozzina di passaggi. Una checklist ripetibile con firme elettroniche trasforma una prima settimana caotica in una di routine.",
            '<strong>Onboardingchecklists.</strong> Nieuwe medewerkers vergen elke keer dezelfde tiental stappen. Een herbruikbare checklist met e-handtekeningen maakt van een chaotische eerste week een routineweek.'),
        '<strong>Leave and time-off management.</strong> Requests, approvals, balances, and a shared calendar. This alone eliminates most of the back-and-forth that clogs a small HR function.': _t(
            "<strong>Gestion des congés et absences.</strong> Demandes, approbations, soldes et un calendrier partagé. Cela seul élimine l'essentiel des allers-retours qui encombrent une petite fonction HR.",
            '<strong>Urlaubs- und Abwesenheitsverwaltung.</strong> Anträge, Genehmigungen, Salden und ein gemeinsamer Kalender. Das allein beseitigt den Großteil des Hin und Her, das eine kleine HR-Funktion verstopft.',
            '<strong>Gestión de permisos y ausencias.</strong> Solicitudes, aprobaciones, saldos y un calendario compartido. Esto por sí solo elimina la mayor parte del ir y venir que atasca una pequeña función de HR.',
            "<strong>Gestione di congedi e assenze.</strong> Richieste, approvazioni, saldi e un calendario condiviso. Questo da solo elimina la maggior parte dei rimpalli che intasano una piccola funzione HR.",
            '<strong>Beheer van verlof en vrije tijd.</strong> Aanvragen, goedkeuringen, saldi en een gedeelde agenda. Dit alleen al elimineert het meeste heen-en-weer dat een kleine HR-functie verstopt.'),
        '<strong>Payroll or clean payroll export.</strong> Whether the tool runs payroll or feeds your provider, the numbers should flow without re-keying — the biggest source of costly errors.': _t(
            "<strong>Paie ou export de paie propre.</strong> Que l'outil gère la paie ou alimente votre prestataire, les chiffres doivent circuler sans ressaisie — la principale source d'erreurs coûteuses.",
            '<strong>Gehaltsabrechnung oder sauberer Abrechnungsexport.</strong> Ob das Tool die Gehaltsabrechnung durchführt oder Ihren Anbieter speist, die Zahlen sollten ohne erneutes Eintippen fließen — die größte Quelle kostspieliger Fehler.',
            '<strong>Nóminas o exportación limpia de nóminas.</strong> Tanto si la herramienta ejecuta las nóminas como si alimenta a su proveedor, las cifras deben fluir sin volver a teclearlas — la mayor fuente de errores costosos.',
            "<strong>Buste paga o esportazione pulita delle buste paga.</strong> Che lo strumento elabori le buste paga o alimenti il tuo fornitore, i numeri devono fluire senza reinserimento — la più grande fonte di errori costosi.",
            '<strong>Loonadministratie of schone loonexport.</strong> Of het tool de loonadministratie uitvoert of uw provider voedt, de cijfers moeten stromen zonder opnieuw te typen — de grootste bron van kostbare fouten.'),
        "<strong>Self-service for employees.</strong> Payslips, personal details, and time-off requests people can handle themselves. Every self-service action is an email HR doesn't have to answer.": _t(
            "<strong>Libre-service pour les employés.</strong> Bulletins de paie, données personnelles et demandes de congés que chacun peut gérer soi-même. Chaque action en libre-service est un e-mail auquel les HR n'ont pas à répondre.",
            '<strong>Self-Service für Mitarbeiter.</strong> Gehaltsabrechnungen, persönliche Daten und Urlaubsanträge, die die Leute selbst erledigen können. Jede Self-Service-Aktion ist eine E-Mail, die HR nicht beantworten muss.',
            '<strong>Autoservicio para los empleados.</strong> Nóminas, datos personales y solicitudes de ausencia que cada uno puede gestionar por sí mismo. Cada acción de autoservicio es un correo que HR no tiene que responder.',
            "<strong>Self-service per i dipendenti.</strong> Buste paga, dati personali e richieste di ferie che le persone possono gestire da sole. Ogni azione self-service è un'e-mail a cui l'HR non deve rispondere.",
            '<strong>Selfservice voor medewerkers.</strong> Loonstroken, persoonlijke gegevens en verlofaanvragen die mensen zelf kunnen afhandelen. Elke selfservice-actie is een e-mail die HR niet hoeft te beantwoorden.'),
        'Nice to have — but not day one': _t(
            'Souhaitable — mais pas dès le premier jour',
            'Wünschenswert — aber nicht am ersten Tag',
            'Conveniente — pero no el primer día',
            'Comodo da avere — ma non dal primo giorno',
            'Prettig om te hebben — maar niet op dag één'),
        "These are worth having eventually, but shouldn't drive your first decision: performance-review cycles, org-chart visualisation, applicant tracking, and learning management. If a tool includes them cleanly, good — but don't pay a premium for features you won't switch on for a year.": _t(
            "Cela vaut la peine de les avoir un jour, mais elles ne devraient pas guider votre première décision : cycles d'évaluation de la performance, visualisation de l'organigramme, suivi des candidatures et gestion de la formation. Si un outil les intègre proprement, tant mieux — mais ne payez pas un supplément pour des fonctionnalités que vous n'activerez pas avant un an.",
            'Diese lohnen sich irgendwann, sollten aber Ihre erste Entscheidung nicht bestimmen: Leistungsbeurteilungszyklen, Organigramm-Visualisierung, Bewerbermanagement und Lernmanagement. Wenn ein Tool sie sauber enthält, gut — aber zahlen Sie keinen Aufpreis für Funktionen, die Sie ein Jahr lang nicht einschalten werden.',
            'Vale la pena tenerlas con el tiempo, pero no deberían dirigir su primera decisión: ciclos de evaluación del desempeño, visualización del organigrama, seguimiento de candidatos y gestión de la formación. Si una herramienta las incluye con limpieza, bien — pero no pague un extra por funciones que no activará en un año.',
            "Vale la pena averle prima o poi, ma non dovrebbero guidare la tua prima decisione: cicli di valutazione delle performance, visualizzazione dell'organigramma, gestione delle candidature e gestione della formazione. Se uno strumento le include in modo pulito, bene — ma non pagare un sovrapprezzo per funzionalità che non attiverai per un anno.",
            'Deze zijn uiteindelijk de moeite waard, maar mogen niet uw eerste beslissing sturen: beoordelingscycli, visualisatie van het organigram, sollicitantvolging en leerbeheer. Als een tool ze netjes bevat, prima — maar betaal geen meerprijs voor functies die u een jaar lang niet zult inschakelen.'),
        'What you can safely skip (for now)': _t(
            'Ce que vous pouvez sans risque laisser de côté (pour l\'instant)',
            'Was Sie (vorerst) bedenkenlos weglassen können',
            'Lo que puede omitir sin problema (por ahora)',
            'Cosa puoi tranquillamente tralasciare (per ora)',
            'Wat u gerust kunt overslaan (voorlopig)'),
        'Advanced workforce analytics, succession planning, and heavy custom-workflow builders are built for organisations with dedicated HR teams. At small scale they add cost and complexity without a matching payoff.': _t(
            "Les analyses avancées des effectifs, la planification de la relève et les lourds générateurs de flux de travail personnalisés sont conçus pour des organisations dotées d'équipes HR dédiées. À petite échelle, ils ajoutent coût et complexité sans contrepartie équivalente.",
            'Erweiterte Personalanalysen, Nachfolgeplanung und schwergewichtige Builder für individuelle Workflows sind für Organisationen mit eigenen HR-Teams gemacht. Im kleinen Maßstab bringen sie Kosten und Komplexität ohne entsprechenden Nutzen.',
            'Los análisis avanzados de plantilla, la planificación de sucesiones y los pesados creadores de flujos de trabajo personalizados están hechos para organizaciones con equipos de HR dedicados. A pequeña escala añaden coste y complejidad sin una recompensa equivalente.',
            'Le analisi avanzate della forza lavoro, la pianificazione delle successioni e i pesanti costruttori di flussi di lavoro personalizzati sono pensati per organizzazioni con team HR dedicati. Su piccola scala aggiungono costo e complessità senza un ritorno adeguato.',
            'Geavanceerde personeelsanalyses, opvolgingsplanning en zware bouwers voor aangepaste workflows zijn gemaakt voor organisaties met toegewijde HR-teams. Op kleine schaal voegen ze kosten en complexiteit toe zonder een bijpassende opbrengst.'),
        'How to evaluate options': _t('Comment évaluer les options', 'So bewerten Sie Optionen', 'Cómo evaluar las opciones', 'Come valutare le opzioni', 'Hoe u opties beoordeelt'),
        '<strong>Start from your actual process.</strong> List what your team does in a month — hires, time-off, payroll runs, reviews — and check each tool against that list, not its marketing.': _t(
            "<strong>Partez de votre processus réel.</strong> Dressez la liste de ce que votre équipe fait en un mois — embauches, congés, cycles de paie, évaluations — et confrontez chaque outil à cette liste, pas à son marketing.",
            '<strong>Gehen Sie von Ihrem tatsächlichen Prozess aus.</strong> Listen Sie auf, was Ihr Team in einem Monat tut — Einstellungen, Abwesenheiten, Abrechnungsläufe, Beurteilungen — und prüfen Sie jedes Tool anhand dieser Liste, nicht anhand seines Marketings.',
            '<strong>Parta de su proceso real.</strong> Enumere lo que su equipo hace en un mes — contrataciones, ausencias, procesos de nómina, evaluaciones — y compare cada herramienta con esa lista, no con su marketing.',
            "<strong>Parti dal tuo processo reale.</strong> Elenca ciò che il tuo team fa in un mese — assunzioni, ferie, elaborazioni di buste paga, valutazioni — e confronta ogni strumento con quell'elenco, non con il suo marketing.",
            '<strong>Vertrek vanuit uw werkelijke proces.</strong> Maak een lijst van wat uw team in een maand doet — aanwervingen, verlof, loonruns, beoordelingen — en toets elk tool aan die lijst, niet aan zijn marketing.'),
        '<strong>Test the boring paths.</strong> Run a real onboarding and a real leave request in the trial. The daily tasks matter more than the flashy dashboard.': _t(
            "<strong>Testez les parcours ennuyeux.</strong> Effectuez une vraie intégration et une vraie demande de congé pendant l'essai. Les tâches quotidiennes comptent plus que le tableau de bord tape-à-l'œil.",
            '<strong>Testen Sie die langweiligen Pfade.</strong> Führen Sie in der Testphase ein echtes Onboarding und einen echten Urlaubsantrag durch. Die täglichen Aufgaben zählen mehr als das schicke Dashboard.',
            '<strong>Pruebe los caminos aburridos.</strong> Realice una incorporación real y una solicitud de ausencia real durante la prueba. Las tareas diarias importan más que el panel llamativo.',
            "<strong>Prova i percorsi noiosi.</strong> Esegui un onboarding reale e una vera richiesta di ferie durante la prova. Le attività quotidiane contano più della dashboard appariscente.",
            '<strong>Test de saaie paden.</strong> Voer tijdens de proef een echte onboarding en een echte verlofaanvraag uit. De dagelijkse taken tellen meer dan het opvallende dashboard.'),
        '<strong>Check the exit.</strong> Can you export your data cleanly? Your records should always be portable and yours.': _t(
            "<strong>Vérifiez la sortie.</strong> Pouvez-vous exporter vos données proprement ? Vos dossiers doivent toujours être portables et vous appartenir.",
            '<strong>Prüfen Sie den Ausstieg.</strong> Können Sie Ihre Daten sauber exportieren? Ihre Datensätze sollten immer portierbar sein und Ihnen gehören.',
            '<strong>Compruebe la salida.</strong> ¿Puede exportar sus datos con limpieza? Sus registros deben ser siempre portables y suyos.',
            "<strong>Controlla l'uscita.</strong> Puoi esportare i tuoi dati in modo pulito? I tuoi dati devono sempre essere portabili e tuoi.",
            '<strong>Controleer de uitgang.</strong> Kunt u uw gegevens netjes exporteren? Uw gegevens moeten altijd overdraagbaar en van u zijn.'),
        "<strong>Price it at your real headcount</strong>, including the growth you expect this year, so a per-user plan doesn't surprise you later.": _t(
            "<strong>Chiffrez-le à votre effectif réel</strong>, en incluant la croissance que vous prévoyez cette année, pour qu'un forfait par utilisateur ne vous surprenne pas plus tard.",
            '<strong>Kalkulieren Sie es mit Ihrer echten Mitarbeiterzahl</strong>, einschließlich des Wachstums, das Sie dieses Jahr erwarten, damit ein Pro-Nutzer-Tarif Sie später nicht überrascht.',
            '<strong>Póngale precio según su plantilla real</strong>, incluido el crecimiento que espera este año, para que un plan por usuario no le sorprenda después.',
            '<strong>Valútalo sul tuo organico reale</strong>, includendo la crescita che prevedi quest\'anno, così un piano per utente non ti sorprende dopo.',
            '<strong>Prijs het op uw werkelijke personeelsbestand</strong>, inclusief de groei die u dit jaar verwacht, zodat een plan per gebruiker u later niet verrast.'),
        'The right first HR system is the one that covers the essentials well, stays out of the way, and grows with you — not the one with the longest feature list.': _t(
            "Le bon premier système HR est celui qui couvre bien l'essentiel, se fait discret et grandit avec vous — pas celui qui a la plus longue liste de fonctionnalités.",
            'Das richtige erste HR-System ist das, das die Grundlagen gut abdeckt, sich zurückhält und mit Ihnen wächst — nicht das mit der längsten Funktionsliste.',
            'El primer sistema de HR adecuado es el que cubre bien lo esencial, no estorba y crece con usted — no el que tiene la lista de funciones más larga.',
            "Il primo sistema HR giusto è quello che copre bene l'essenziale, non intralcia e cresce con te — non quello con la lista di funzionalità più lunga.",
            'Het juiste eerste HR-systeem is dat wat de essentie goed dekt, niet in de weg zit en met u meegroeit — niet dat met de langste functielijst.'),
        # ---- CTA ----
        'People operations, without the bloat': _t(
            'La gestion du personnel, sans le superflu',
            'Personalmanagement, ohne den Ballast',
            'Gestión de personas, sin lo superfluo',
            'Gestione del personale, senza il superfluo',
            'Personeelsbeheer, zonder de ballast'),
        'HR Suite covers the essentials — records, onboarding, payroll, time, leave, and performance — in one compliant, easy-to-run place.': _t(
            "HR Suite couvre l'essentiel — dossiers, intégration, paie, temps, congés et performance — dans un seul espace conforme et simple à administrer.",
            'HR Suite deckt die Grundlagen ab — Akten, Onboarding, Gehaltsabrechnung, Zeit, Abwesenheiten und Leistung — an einem konformen, einfach zu betreibenden Ort.',
            'HR Suite cubre lo esencial — expedientes, incorporación, nóminas, tiempo, ausencias y desempeño — en un único lugar conforme y fácil de usar.',
            "HR Suite copre l'essenziale — schede, onboarding, buste paga, tempo, ferie e performance — in un unico luogo conforme e facile da usare.",
            'HR Suite dekt de essentie — dossiers, onboarding, loonadministratie, tijd, verlof en prestaties — op één conforme, eenvoudig te beheren plek.'),
    },
}

PAGE['/blog/performance-review-questions/'] = {
    'src': 'blog/performance-review-questions/index.html',
    't': {
        '>Home</a>': _HOME,
        'Explore HR Suite': _EXPLORE,
        'Back to the blog': _BACK,
        'FulcrumGrid HR Suite — people operations': _ALT,
        # ---- Title / meta ----
        "Performance Review Questions: A Manager's Template": _t(
            "Questions d'évaluation de la performance : un modèle pour les managers",
            'Fragen für die Leistungsbeurteilung: eine Vorlage für Führungskräfte',
            'Preguntas para la evaluación del desempeño: una plantilla para responsables',
            'Domande per la valutazione delle performance: un modello per i manager',
            'Vragen voor het functioneringsgesprek: een sjabloon voor managers'),
        'Performance review questions': _t(
            "Questions d'évaluation de la performance",
            'Fragen für die Leistungsbeurteilung',
            'Preguntas para la evaluación del desempeño',
            'Domande per la valutazione delle performance',
            'Vragen voor het functioneringsgesprek'),
        "Ready-to-use performance review questions for managers — self-review, manager, and 1:1 growth questions, plus how to run a review that's fair and useful.": _t(
            "Des questions d'évaluation de la performance prêtes à l'emploi pour les managers — questions d'auto-évaluation, du manager et de développement en 1:1, plus comment mener une évaluation juste et utile.",
            'Sofort einsetzbare Fragen für die Leistungsbeurteilung für Führungskräfte — Fragen zur Selbstbeurteilung, für die Führungskraft und zur Entwicklung im 1:1, plus wie man eine faire und nützliche Beurteilung führt.',
            'Preguntas para la evaluación del desempeño listas para usar, para responsables — preguntas de autoevaluación, del responsable y de desarrollo en el 1:1, además de cómo llevar una evaluación justa y útil.',
            "Domande per la valutazione delle performance pronte all'uso per i manager — domande di autovalutazione, del manager e di crescita in 1:1, più come condurre una valutazione equa e utile.",
            'Kant-en-klare vragen voor het functioneringsgesprek voor managers — vragen voor zelfevaluatie, de manager en groei in de 1:1, plus hoe u een eerlijk en nuttig gesprek voert.'),
        "Self-review, manager, and growth questions you can copy — plus how to run a review that's fair, specific, and actually useful.": _t(
            "Des questions d'auto-évaluation, du manager et de développement à copier — plus comment mener une évaluation juste, précise et vraiment utile.",
            'Fragen zur Selbstbeurteilung, für die Führungskraft und zur Entwicklung zum Kopieren — plus wie man eine faire, konkrete und wirklich nützliche Beurteilung führt.',
            'Preguntas de autoevaluación, del responsable y de desarrollo que puede copiar — además de cómo llevar una evaluación justa, específica y de verdad útil.',
            'Domande di autovalutazione, del manager e di crescita da copiare — più come condurre una valutazione equa, specifica e davvero utile.',
            'Vragen voor zelfevaluatie, de manager en groei die u kunt kopiëren — plus hoe u een gesprek voert dat eerlijk, specifiek en echt nuttig is.'),
        'September 7, 2026': _t('7 septembre 2026', '7. September 2026', '7 de septiembre de 2026', '7 settembre 2026', '7 september 2026'),
        '7 min read': _t('7 min de lecture', '7 Min. Lesezeit', '7 min de lectura', '7 min di lettura', '7 min leestijd'),
        # ---- Body ----
        "A performance review is only as good as the questions behind it. Ask vague ones and you get a box-ticking exercise nobody values; ask sharp, specific ones and you get an honest conversation that actually helps someone grow. Below is a template you can copy — organised into the three parts of a good review: the employee's self-review, the manager's assessment, and a forward-looking growth conversation.": _t(
            "Une évaluation de la performance ne vaut que par les questions qui la sous-tendent. Posez des questions vagues et vous obtenez un exercice de case à cocher que personne n'apprécie ; posez des questions nettes et précises et vous obtenez une conversation honnête qui aide vraiment quelqu'un à progresser. Voici un modèle à copier — organisé selon les trois parties d'une bonne évaluation : l'auto-évaluation de l'employé, l'appréciation du manager et une conversation de développement tournée vers l'avenir.",
            'Eine Leistungsbeurteilung ist nur so gut wie die Fragen dahinter. Stellen Sie vage Fragen, erhalten Sie eine Abhak-Übung, die niemand schätzt; stellen Sie scharfe, konkrete Fragen, erhalten Sie ein ehrliches Gespräch, das jemandem wirklich beim Wachsen hilft. Unten finden Sie eine Vorlage zum Kopieren — gegliedert in die drei Teile einer guten Beurteilung: die Selbstbeurteilung des Mitarbeiters, die Einschätzung der Führungskraft und ein nach vorn gerichtetes Entwicklungsgespräch.',
            'Una evaluación del desempeño solo vale lo que valen las preguntas que la sustentan. Haga preguntas vagas y obtendrá un ejercicio de marcar casillas que nadie valora; haga preguntas nítidas y específicas y obtendrá una conversación honesta que de verdad ayuda a alguien a crecer. A continuación tiene una plantilla que puede copiar — organizada en las tres partes de una buena evaluación: la autoevaluación del empleado, la valoración del responsable y una conversación de desarrollo orientada al futuro.',
            "Una valutazione delle performance vale solo quanto le domande che la reggono. Poni domande vaghe e ottieni un esercizio di spunta delle caselle che nessuno apprezza; poni domande nette e specifiche e ottieni una conversazione onesta che aiuta davvero qualcuno a crescere. Di seguito trovi un modello da copiare — organizzato nelle tre parti di una buona valutazione: l'autovalutazione del dipendente, la valutazione del manager e una conversazione di crescita rivolta al futuro.",
            'Een functioneringsgesprek is alleen zo goed als de vragen erachter. Stel vage vragen en u krijgt een vinkjesoefening die niemand waardeert; stel scherpe, specifieke vragen en u krijgt een eerlijk gesprek dat iemand echt helpt groeien. Hieronder staat een sjabloon dat u kunt kopiëren — ingedeeld in de drie delen van een goed gesprek: de zelfevaluatie van de medewerker, de beoordeling van de manager en een toekomstgericht groeigesprek.'),
        'Before you start: three ground rules': _t(
            'Avant de commencer : trois règles de base', 'Bevor Sie beginnen: drei Grundregeln',
            'Antes de empezar: tres reglas básicas', 'Prima di iniziare: tre regole di base', 'Voordat u begint: drie basisregels'),
        "<strong>No surprises.</strong> A review should summarise feedback the person has already heard through the year, not spring it on them. If something is new, that's a coaching failure, not a review moment.": _t(
            "<strong>Pas de surprises.</strong> Une évaluation doit résumer les retours que la personne a déjà entendus au cours de l'année, pas les lui assener. Si quelque chose est nouveau, c'est un échec d'accompagnement, pas un moment d'évaluation.",
            '<strong>Keine Überraschungen.</strong> Eine Beurteilung sollte Rückmeldungen zusammenfassen, die die Person im Laufe des Jahres bereits gehört hat, und sie ihr nicht überfallartig präsentieren. Wenn etwas neu ist, ist das ein Versäumnis im Coaching, kein Beurteilungsmoment.',
            '<strong>Sin sorpresas.</strong> Una evaluación debe resumir los comentarios que la persona ya ha oído a lo largo del año, no soltárselos de golpe. Si algo es nuevo, es un fallo de acompañamiento, no un momento de evaluación.',
            "<strong>Nessuna sorpresa.</strong> Una valutazione dovrebbe riassumere i feedback che la persona ha già sentito nel corso dell'anno, non piombarle addosso. Se qualcosa è nuovo, è un fallimento nel coaching, non un momento di valutazione.",
            '<strong>Geen verrassingen.</strong> Een gesprek moet feedback samenvatten die de persoon al gedurende het jaar heeft gehoord, niet onverwacht op tafel leggen. Als iets nieuw is, is dat een coachingfout, geen beoordelingsmoment.'),
        '<strong>Specific over general.</strong> "Great communicator" helps no one. "Your launch note gave three teams what they needed in one place" is feedback someone can build on.': _t(
            "<strong>Précis plutôt que général.</strong> « Excellent communicant » n'aide personne. « Votre note de lancement a donné à trois équipes ce dont elles avaient besoin, au même endroit » est un retour sur lequel on peut bâtir.",
            '<strong>Konkret statt allgemein.</strong> „Guter Kommunikator" hilft niemandem. „Ihre Launch-Notiz hat drei Teams an einem Ort gegeben, was sie brauchten" ist Feedback, auf dem man aufbauen kann.',
            '<strong>Específico antes que general.</strong> «Gran comunicador» no ayuda a nadie. «Tu nota de lanzamiento dio a tres equipos lo que necesitaban en un solo sitio» es un comentario sobre el que se puede construir.',
            "<strong>Specifico anziché generico.</strong> «Ottimo comunicatore» non aiuta nessuno. «La tua nota di lancio ha dato a tre team ciò di cui avevano bisogno in un unico posto» è un feedback su cui si può costruire.",
            '<strong>Specifiek boven algemeen.</strong> "Goede communicator" helpt niemand. "Je lanceringsnotitie gaf drie teams op één plek wat ze nodig hadden" is feedback waarop iemand kan voortbouwen.'),
        "<strong>Balance backward and forward.</strong> Half the review is what happened; half is what's next. Don't let it become only a grade.": _t(
            "<strong>Équilibrez passé et avenir.</strong> La moitié de l'évaluation porte sur ce qui s'est passé ; l'autre moitié sur la suite. Ne la laissez pas se réduire à une simple note.",
            '<strong>Halten Sie Rückblick und Ausblick im Gleichgewicht.</strong> Die Hälfte der Beurteilung ist, was geschehen ist; die Hälfte, was als Nächstes kommt. Lassen Sie sie nicht zu einer reinen Note werden.',
            '<strong>Equilibre pasado y futuro.</strong> La mitad de la evaluación es lo que ocurrió; la otra mitad, lo que viene. No deje que se convierta solo en una nota.',
            "<strong>Bilancia passato e futuro.</strong> Metà della valutazione riguarda ciò che è successo; metà ciò che verrà. Non lasciare che diventi solo un voto.",
            '<strong>Balanceer terugblik en vooruitblik.</strong> De helft van het gesprek gaat over wat er is gebeurd; de helft over wat er komt. Laat het niet slechts een cijfer worden.'),
        '1. Self-review questions (send these first)': _t(
            "1. Questions d'auto-évaluation (à envoyer en premier)",
            '1. Fragen zur Selbstbeurteilung (zuerst versenden)',
            '1. Preguntas de autoevaluación (envíelas primero)',
            '1. Domande di autovalutazione (invia queste per prime)',
            '1. Vragen voor zelfevaluatie (stuur deze eerst)'),
        'Have the employee answer these a few days ahead — it sets the agenda and surfaces gaps between how they and you see the period.': _t(
            "Faites répondre l'employé à ces questions quelques jours à l'avance — cela fixe l'ordre du jour et fait apparaître les écarts entre sa vision et la vôtre de la période.",
            'Lassen Sie den Mitarbeiter diese ein paar Tage im Voraus beantworten — das setzt die Agenda und legt Unterschiede offen, wie er und Sie den Zeitraum sehen.',
            'Haga que el empleado responda a estas unos días antes — marca la agenda y saca a la luz las diferencias entre cómo ve él y cómo ve usted el período.',
            "Fai rispondere al dipendente a queste domande qualche giorno prima — imposta l'agenda e fa emergere le differenze tra come lui e come tu vedete il periodo.",
            'Laat de medewerker deze een paar dagen van tevoren beantwoorden — het bepaalt de agenda en brengt verschillen aan het licht tussen hoe hij en u de periode zien.'),
        'What are you most proud of since the last review, and why?': _t(
            'De quoi êtes-vous le plus fier depuis la dernière évaluation, et pourquoi ?',
            'Worauf sind Sie seit der letzten Beurteilung am stolzesten, und warum?',
            '¿De qué está más orgulloso desde la última evaluación y por qué?',
            "Di cosa sei più orgoglioso dall'ultima valutazione, e perché?",
            'Waar bent u het meest trots op sinds het vorige gesprek, en waarom?'),
        'Which goals did you meet, and which fell short — what got in the way?': _t(
            "Quels objectifs avez-vous atteints, et lesquels n'ont pas abouti — qu'est-ce qui a fait obstacle ?",
            'Welche Ziele haben Sie erreicht und welche verfehlt — was stand im Weg?',
            '¿Qué objetivos cumplió y cuáles se quedaron cortos — qué se interpuso?',
            'Quali obiettivi hai raggiunto e quali no — cosa ti ha ostacolato?',
            'Welke doelen hebt u gehaald en welke niet — wat stond in de weg?'),
        'Where did you grow a skill or take on something new?': _t(
            'Où avez-vous développé une compétence ou pris en charge quelque chose de nouveau ?',
            'Wo haben Sie eine Fähigkeit ausgebaut oder etwas Neues übernommen?',
            '¿Dónde desarrolló una habilidad o asumió algo nuevo?',
            'Dove hai sviluppato una competenza o assunto qualcosa di nuovo?',
            'Waar hebt u een vaardigheid ontwikkeld of iets nieuws opgepakt?'),
        'What part of your role energises you most? What drains you?': _t(
            'Quelle partie de votre poste vous stimule le plus ? Qu\'est-ce qui vous épuise ?',
            'Welcher Teil Ihrer Rolle gibt Ihnen am meisten Energie? Was zehrt an Ihnen?',
            '¿Qué parte de su puesto le da más energía? ¿Qué le agota?',
            'Quale parte del tuo ruolo ti dà più energia? Cosa ti sfinisce?',
            'Welk deel van uw functie geeft u de meeste energie? Wat put u uit?'),
        'Where do you want to develop next, and what support would help?': _t(
            'Dans quelle direction souhaitez-vous évoluer ensuite, et quel soutien vous aiderait ?',
            'Wohin möchten Sie sich als Nächstes entwickeln, und welche Unterstützung würde helfen?',
            '¿Hacia dónde quiere desarrollarse a continuación y qué apoyo le ayudaría?',
            'In quale direzione vuoi crescere adesso, e quale supporto ti aiuterebbe?',
            'Waarin wilt u zich hierna ontwikkelen, en welke ondersteuning zou helpen?'),
        '2. Manager assessment questions (your prep)': _t(
            "2. Questions d'appréciation du manager (votre préparation)",
            '2. Fragen zur Einschätzung der Führungskraft (Ihre Vorbereitung)',
            '2. Preguntas de valoración del responsable (su preparación)',
            '2. Domande di valutazione del manager (la tua preparazione)',
            '2. Vragen voor de beoordeling door de manager (uw voorbereiding)'),
        'Answer these for yourself, backed by specific examples and notes from the period — not just the last few weeks.': _t(
            "Répondez-y pour vous-même, en vous appuyant sur des exemples précis et des notes de la période — pas seulement des dernières semaines.",
            'Beantworten Sie diese für sich selbst, gestützt auf konkrete Beispiele und Notizen aus dem Zeitraum — nicht nur aus den letzten Wochen.',
            'Respóndalas para usted mismo, con ejemplos concretos y notas del período — no solo de las últimas semanas.',
            'Rispondi a queste per te stesso, con esempi specifici e appunti del periodo — non solo delle ultime settimane.',
            'Beantwoord deze voor uzelf, onderbouwd met specifieke voorbeelden en notities uit de periode — niet alleen de laatste paar weken.'),
        'Did they deliver on the goals we agreed? Where did they exceed or miss, and why?': _t(
            'A-t-il tenu les objectifs convenus ? Où a-t-il dépassé ou manqué, et pourquoi ?',
            'Hat er die vereinbarten Ziele erreicht? Wo hat er übertroffen oder verfehlt, und warum?',
            '¿Cumplió los objetivos que acordamos? ¿Dónde superó o falló, y por qué?',
            'Ha raggiunto gli obiettivi concordati? Dove ha superato o mancato, e perché?',
            'Heeft hij de afgesproken doelen gehaald? Waar overtrof of miste hij, en waarom?'),
        "What's the single strongest example of their impact this period?": _t(
            'Quel est le meilleur exemple unique de son impact durant cette période ?',
            'Was ist das eine stärkste Beispiel für seine Wirkung in diesem Zeitraum?',
            '¿Cuál es el ejemplo más contundente de su impacto en este período?',
            'Qual è il singolo esempio più forte del suo impatto in questo periodo?',
            'Wat is het allersterkste voorbeeld van zijn impact deze periode?'),
        'Where is the one most valuable area to improve — and is it a skill, a habit, or a resourcing issue?': _t(
            "Quel est le domaine d'amélioration le plus utile — et s'agit-il d'une compétence, d'une habitude ou d'un problème de ressources ?",
            'Wo liegt der wertvollste Bereich zur Verbesserung — und ist es eine Fähigkeit, eine Gewohnheit oder ein Ressourcenproblem?',
            '¿Cuál es el área de mejora más valiosa — y es una habilidad, un hábito o un problema de recursos?',
            "Qual è l'area di miglioramento più preziosa — ed è una competenza, un'abitudine o un problema di risorse?",
            'Wat is het waardevolste verbeterpunt — en is het een vaardigheid, een gewoonte of een kwestie van middelen?'),
        'How do they work with the team — do they make those around them better?': _t(
            "Comment travaille-t-il avec l'équipe — rend-il meilleurs ceux qui l'entourent ?",
            'Wie arbeitet er mit dem Team — macht er die Menschen um sich herum besser?',
            '¿Cómo trabaja con el equipo — hace mejores a quienes le rodean?',
            'Come lavora con il team — rende migliori quelli intorno a sé?',
            'Hoe werkt hij met het team samen — maakt hij de mensen om hem heen beter?'),
        "Are they in the right role and scope for where they're headed?": _t(
            "Est-il dans le bon rôle et le bon périmètre pour l'endroit où il se dirige ?",
            'Ist er in der richtigen Rolle und dem richtigen Aufgabenbereich für seinen weiteren Weg?',
            '¿Está en el puesto y el alcance adecuados para hacia dónde se dirige?',
            'È nel ruolo e nell\'ambito giusti per dove è diretto?',
            'Zit hij in de juiste rol en reikwijdte voor waar hij naartoe gaat?'),
        '3. Growth &amp; forward-looking questions (the conversation)': _t(
            "3. Questions de développement &amp; tournées vers l'avenir (la conversation)",
            '3. Fragen zu Entwicklung &amp; Zukunft (das Gespräch)',
            '3. Preguntas de desarrollo &amp; orientadas al futuro (la conversación)',
            '3. Domande di crescita &amp; rivolte al futuro (la conversazione)',
            '3. Vragen over groei &amp; toekomst (het gesprek)'),
        "What do you want to be doing 12 months from now — and what's the first step?": _t(
            'Que voulez-vous faire dans 12 mois — et quelle est la première étape ?',
            'Was möchten Sie in 12 Monaten tun — und was ist der erste Schritt?',
            '¿Qué quiere estar haciendo dentro de 12 meses — y cuál es el primer paso?',
            'Cosa vuoi fare tra 12 mesi — e qual è il primo passo?',
            'Wat wilt u over 12 maanden doen — en wat is de eerste stap?'),
        'What are the two or three priorities that matter most next quarter?': _t(
            'Quelles sont les deux ou trois priorités les plus importantes pour le prochain trimestre ?',
            'Was sind die zwei oder drei wichtigsten Prioritäten für das nächste Quartal?',
            '¿Cuáles son las dos o tres prioridades más importantes para el próximo trimestre?',
            'Quali sono le due o tre priorità più importanti per il prossimo trimestre?',
            'Wat zijn de twee of drie prioriteiten die volgend kwartaal het meest tellen?'),
        'What can I do differently as your manager to help you do your best work?': _t(
            'Que puis-je faire différemment en tant que manager pour vous aider à donner le meilleur de vous-même ?',
            'Was kann ich als Ihre Führungskraft anders machen, damit Sie Ihre beste Arbeit leisten?',
            '¿Qué puedo hacer diferente como su responsable para ayudarle a dar lo mejor de sí?',
            'Cosa posso fare di diverso come tuo manager per aiutarti a dare il meglio?',
            'Wat kan ik als uw manager anders doen om u te helpen uw beste werk te leveren?'),
        "Is anything getting in your way that we haven't talked about?": _t(
            "Y a-t-il quelque chose qui vous freine dont nous n'avons pas parlé ?",
            'Steht Ihnen etwas im Weg, worüber wir noch nicht gesprochen haben?',
            '¿Hay algo que le esté frenando de lo que no hayamos hablado?',
            "C'è qualcosa che ti ostacola di cui non abbiamo parlato?",
            'Staat er iets in uw weg waar we het nog niet over hebben gehad?'),
        'What does success look like for you — beyond just hitting targets?': _t(
            'À quoi ressemble la réussite pour vous — au-delà de la simple atteinte des objectifs ?',
            'Wie sieht Erfolg für Sie aus — über das bloße Erreichen von Zielen hinaus?',
            '¿Cómo es el éxito para usted — más allá de solo alcanzar los objetivos?',
            'Come si presenta il successo per te — al di là del semplice raggiungimento degli obiettivi?',
            'Hoe ziet succes er voor u uit — meer dan alleen doelen halen?'),
        'Rating scales: keep them simple': _t(
            'Échelles de notation : gardez-les simples', 'Bewertungsskalen: halten Sie sie einfach',
            'Escalas de valoración: manténgalas simples', 'Scale di valutazione: mantienile semplici', 'Beoordelingsschalen: houd ze eenvoudig'),
        'If you use ratings, a 3- or 5-point scale with clear definitions beats a vague 1–10. Whatever you pick, anchor each level in behaviour ("consistently exceeds," "meets," "developing") and apply it the same way for everyone — consistency is what makes a scale fair.': _t(
            "Si vous utilisez des notes, une échelle à 3 ou 5 niveaux avec des définitions claires vaut mieux qu'un vague 1–10. Quel que soit votre choix, ancrez chaque niveau dans un comportement (« dépasse systématiquement », « atteint », « en développement ») et appliquez-le de la même façon pour tous — c'est la cohérence qui rend une échelle juste.",
            'Wenn Sie Bewertungen verwenden, ist eine 3- oder 5-stufige Skala mit klaren Definitionen besser als ein vages 1–10. Was auch immer Sie wählen, verankern Sie jede Stufe in Verhalten („übertrifft durchgängig", „erfüllt", „in Entwicklung") und wenden Sie es für alle gleich an — Konsistenz macht eine Skala fair.',
            'Si usa calificaciones, una escala de 3 o 5 puntos con definiciones claras supera a un vago 1–10. Sea cual sea su elección, ancle cada nivel en un comportamiento («supera de forma constante», «cumple», «en desarrollo») y aplíquelo igual para todos — la coherencia es lo que hace justa una escala.',
            "Se usi le valutazioni, una scala a 3 o 5 punti con definizioni chiare batte un vago 1–10. Qualunque cosa scelga, ancóra ogni livello a un comportamento («supera costantemente», «soddisfa», «in sviluppo») e applicalo allo stesso modo per tutti — è la coerenza a rendere equa una scala.",
            'Als u beoordelingen gebruikt, verslaat een schaal van 3 of 5 punten met heldere definities een vage 1–10. Wat u ook kiest, veranker elk niveau in gedrag ("overtreft consequent", "voldoet", "in ontwikkeling") en pas het voor iedereen op dezelfde manier toe — consistentie maakt een schaal eerlijk.'),
        # ---- Read next ----
        "Good questions are step one; running reviews the same way for everyone — on a schedule, with a record you can look back on — is what makes them fair and useful over time. That's easier when reviews, goals, and history live in one system rather than scattered documents. It also builds on the fundamentals we cover in our <a href=\"/blog/employee-onboarding-checklist/\">employee onboarding checklist</a> and <a href=\"/blog/pto-policy/\">PTO policy guide</a> — and if you're still choosing a system to run it all, our guide to <a href=\"/blog/hr-software-small-business/\">HR software for small businesses</a> covers what to look for.": _t(
            "Les bonnes questions ne sont que la première étape ; mener les évaluations de la même façon pour tous — selon un calendrier, avec une trace que l'on peut consulter — voilà ce qui les rend justes et utiles dans la durée. C'est plus facile quand les évaluations, les objectifs et l'historique vivent dans un seul système plutôt que dans des documents épars. Cela s'appuie aussi sur les fondamentaux que nous abordons dans notre <a href=\"/blog/employee-onboarding-checklist/\">liste de contrôle d'intégration des employés</a> et notre <a href=\"/blog/pto-policy/\">guide de politique de PTO</a> — et si vous cherchez encore un système pour tout gérer, notre guide sur le <a href=\"/blog/hr-software-small-business/\">logiciel HR pour petites entreprises</a> explique ce qu'il faut regarder.",
            "Gute Fragen sind der erste Schritt; Beurteilungen für alle gleich durchzuführen — nach einem Zeitplan, mit einer Aufzeichnung, auf die man zurückblicken kann — macht sie mit der Zeit fair und nützlich. Das ist einfacher, wenn Beurteilungen, Ziele und Verlauf in einem System liegen statt in verstreuten Dokumenten. Es baut auch auf den Grundlagen auf, die wir in unserer <a href=\"/blog/employee-onboarding-checklist/\">Checkliste für das Mitarbeiter-Onboarding</a> und unserem <a href=\"/blog/pto-policy/\">Leitfaden zur PTO-Richtlinie</a> behandeln — und wenn Sie noch ein System zur Verwaltung von allem suchen, erklärt unser Leitfaden zu <a href=\"/blog/hr-software-small-business/\">HR-Software für kleine Unternehmen</a>, worauf Sie achten sollten.",
            "Las buenas preguntas son el primer paso; llevar las evaluaciones de la misma forma para todos — con un calendario, con un registro que se pueda consultar — es lo que las hace justas y útiles con el tiempo. Es más fácil cuando las evaluaciones, los objetivos y el historial viven en un solo sistema en lugar de en documentos dispersos. También se apoya en los fundamentos que tratamos en nuestra <a href=\"/blog/employee-onboarding-checklist/\">lista de incorporación de empleados</a> y nuestra <a href=\"/blog/pto-policy/\">guía de política de PTO</a> — y si todavía está eligiendo un sistema para gestionarlo todo, nuestra guía sobre <a href=\"/blog/hr-software-small-business/\">software de HR para pequeñas empresas</a> explica en qué fijarse.",
            "Le buone domande sono il primo passo; condurre le valutazioni allo stesso modo per tutti — secondo un calendario, con una traccia che puoi rivedere — è ciò che le rende eque e utili nel tempo. È più facile quando valutazioni, obiettivi e storico vivono in un unico sistema anziché in documenti sparsi. Si basa anche sui fondamentali che trattiamo nella nostra <a href=\"/blog/employee-onboarding-checklist/\">checklist di onboarding dei dipendenti</a> e nella nostra <a href=\"/blog/pto-policy/\">guida alla politica sui PTO</a> — e se stai ancora scegliendo un sistema per gestire tutto, la nostra guida al <a href=\"/blog/hr-software-small-business/\">software HR per piccole imprese</a> spiega cosa cercare.",
            "Goede vragen zijn stap één; gesprekken voor iedereen op dezelfde manier voeren — volgens een schema, met een verslag dat u kunt teruglezen — is wat ze na verloop van tijd eerlijk en nuttig maakt. Dat is makkelijker wanneer gesprekken, doelen en geschiedenis in één systeem staan in plaats van in verspreide documenten. Het bouwt ook voort op de basis die we behandelen in onze <a href=\"/blog/employee-onboarding-checklist/\">onboardingchecklist voor medewerkers</a> en onze <a href=\"/blog/pto-policy/\">gids voor PTO-beleid</a> — en als u nog een systeem kiest om het allemaal uit te voeren, legt onze gids over <a href=\"/blog/hr-software-small-business/\">HR-software voor kleine bedrijven</a> uit waar u op moet letten."),
        # ---- CTA ----
        'Run reviews the same way, every cycle': _t(
            'Menez les évaluations de la même façon, à chaque cycle',
            'Führen Sie Beurteilungen jedes Mal auf dieselbe Weise durch',
            'Lleve las evaluaciones de la misma forma, cada ciclo',
            'Conduci le valutazioni allo stesso modo, a ogni ciclo',
            'Voer gesprekken elke cyclus op dezelfde manier'),
        'HR Suite keeps performance reviews, goals, and history in one place — structured questions, a consistent scale, and a record you can revisit — so every review is fair and nothing gets lost.': _t(
            "HR Suite conserve les évaluations de la performance, les objectifs et l'historique au même endroit — questions structurées, échelle cohérente et une trace consultable — pour que chaque évaluation soit juste et que rien ne se perde.",
            'HR Suite hält Leistungsbeurteilungen, Ziele und Verlauf an einem Ort — strukturierte Fragen, eine einheitliche Skala und eine Aufzeichnung, auf die Sie zurückgreifen können — damit jede Beurteilung fair ist und nichts verloren geht.',
            'HR Suite mantiene las evaluaciones del desempeño, los objetivos y el historial en un solo lugar — preguntas estructuradas, una escala coherente y un registro que puede revisar — para que cada evaluación sea justa y no se pierda nada.',
            'HR Suite tiene le valutazioni delle performance, gli obiettivi e lo storico in un unico posto — domande strutturate, una scala coerente e una traccia che puoi rivedere — così ogni valutazione è equa e nulla va perso.',
            'HR Suite houdt functioneringsgesprekken, doelen en geschiedenis op één plek — gestructureerde vragen, een consistente schaal en een verslag dat u opnieuw kunt bekijken — zodat elk gesprek eerlijk is en niets verloren gaat.'),
    },
}
