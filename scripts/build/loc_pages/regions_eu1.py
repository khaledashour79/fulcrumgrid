# -*- coding: utf-8 -*-
"""Per-page translations for the European REGION pages (batch eu1):
/regions/europe/, /regions/uk/, /regions/ireland/, /regions/france/.

Chrome (nav, footer, buttons, tagline, Request a demo, Email us, language
list) comes from the shared COMMON catalog and is NOT repeated here.
Keys are EXACT English substrings of the committed EN source, including
entities (&amp;), straight apostrophes, dashes (— –) and glyphs (· → ↗).
"""

def _t(fr, de, es, it, nl):
    return {'fr': fr, 'de': de, 'es': es, 'it': it, 'nl': nl}


PAGE = {}

PAGE['/regions/europe/'] = {
    'src': 'regions/europe/index.html',
    't': {
        # ---- Meta ----
        'FulcrumGrid in Europe — every app, built for your region | FulcrumGrid': _t(
            'FulcrumGrid en Europe — chaque application, conçue pour votre région | FulcrumGrid',
            'FulcrumGrid in Europa — jede App, gebaut für Ihre Region | FulcrumGrid',
            'FulcrumGrid en Europa — cada app, diseñada para su región | FulcrumGrid',
            'FulcrumGrid in Europa — ogni app, costruita per la tua regione | FulcrumGrid',
            'FulcrumGrid in Europa — elke app, gebouwd voor uw regio | FulcrumGrid'),
        'FulcrumGrid across Europe — Command Center, Collection and HR Suite — with multi-currency VAT-ready finance, SEPA payments and GDPR-grade data privacy.': _t(
            "FulcrumGrid dans toute l'Europe — Command Center, Collection et HR Suite — avec une finance multidevise prête pour la TVA, des paiements SEPA et une confidentialité des données au niveau du GDPR.",
            'FulcrumGrid in ganz Europa — Command Center, Collection und HR Suite — mit MwSt.-fähiger Mehrwährungs-Finanzverwaltung, SEPA-Zahlungen und Datenschutz auf GDPR-Niveau.',
            'FulcrumGrid en toda Europa — Command Center, Collection y HR Suite — con finanzas multidivisa preparadas para el IVA, pagos SEPA y privacidad de datos a nivel del GDPR.',
            "FulcrumGrid in tutta Europa — Command Center, Collection e HR Suite — con finanza multivaluta pronta per l'IVA, pagamenti SEPA e privacy dei dati a livello GDPR.",
            'FulcrumGrid in heel Europa — Command Center, Collection en HR Suite — met multivaluta, btw-klare financiën, SEPA-betalingen en gegevensprivacy op GDPR-niveau.'),
        # ---- Hero ----
        'Europe · EU': _t('Europe · UE', 'Europa · EU', 'Europa · UE', 'Europa · UE', 'Europa · EU'),
        'FulcrumGrid, built for <em style="font-style:normal;color:var(--color-accent)">Europe</em>': _t(
            'FulcrumGrid, conçu pour <em style="font-style:normal;color:var(--color-accent)">l\'Europe</em>',
            'FulcrumGrid, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Europa</em>',
            'FulcrumGrid, diseñado para <em style="font-style:normal;color:var(--color-accent)">Europa</em>',
            'FulcrumGrid, pensato per <em style="font-style:normal;color:var(--color-accent)">l\'Europa</em>',
            'FulcrumGrid, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Europa</em>'),
        'The whole grid runs across Europe — Command Center with multi-currency, VAT-ready finance; Collection with SEPA-friendly receivables; and HR Suite with SEPA payroll and GDPR-grade data privacy. One platform across your entities.': _t(
            "Toute la grille fonctionne dans toute l'Europe — Command Center avec une finance multidevise prête pour la TVA ; Collection avec un recouvrement compatible SEPA ; et HR Suite avec une paie SEPA et une confidentialité des données au niveau du GDPR. Une seule plateforme pour toutes vos entités.",
            'Das gesamte Grid läuft in ganz Europa — Command Center mit MwSt.-fähiger Mehrwährungs-Finanzverwaltung; Collection mit SEPA-freundlichem Forderungseinzug; und HR Suite mit SEPA-Gehaltsabrechnung und Datenschutz auf GDPR-Niveau. Eine Plattform über alle Ihre Gesellschaften hinweg.',
            'Toda la cuadrícula funciona en toda Europa — Command Center con finanzas multidivisa preparadas para el IVA; Collection con cobros compatibles con SEPA; y HR Suite con nóminas SEPA y privacidad de datos a nivel del GDPR. Una sola plataforma para todas sus entidades.',
            "Tutta la griglia funziona in tutta Europa — Command Center con finanza multivaluta pronta per l'IVA; Collection con recupero crediti compatibile con SEPA; e HR Suite con buste paga SEPA e privacy dei dati a livello GDPR. Un'unica piattaforma per tutte le tue entità.",
            "Het hele grid draait in heel Europa — Command Center met multivaluta, btw-klare financiën; Collection met SEPA-vriendelijke debiteuren; en HR Suite met SEPA-salarisadministratie en gegevensprivacy op GDPR-niveau. Eén platform voor al uw entiteiten."),
        # ---- Built-in section ----
        'Built in': _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd'),
        'Europe compliance, out of the box': _t(
            "Conformité Europe, prête à l'emploi", 'Europa-Compliance, sofort einsatzbereit',
            'Cumplimiento para Europa, listo para usar', "Conformità Europa, pronta all'uso",
            'Europa-compliance, kant-en-klaar'),
        'The modules that make HR Suite work the way Europe does — each part of the same platform, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière de l'Europe — chacun faisant partie de la même plateforme, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie Europa es tut — jedes Teil derselben Plattform, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Europa — cada uno parte de la misma plataforma, sin herramientas aparte.',
            "I moduli che fanno funzionare HR Suite come fa l'Europa — ognuno parte della stessa piattaforma, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Europa dat doet — elk onderdeel van hetzelfde platform, zonder losse tools.'),
        # ---- Features ----
        'SEPA payments': _t('Paiements SEPA', 'SEPA-Zahlungen', 'Pagos SEPA', 'Pagamenti SEPA', 'SEPA-betalingen'),
        'Export a SEPA credit-transfer file from a finalized pay run for upload to your bank, with IBANs validated on entry.': _t(
            "Exportez un fichier de virement SEPA à partir d'une paie finalisée, à téléverser vers votre banque, avec des IBAN validés à la saisie.",
            'Exportieren Sie aus einem abgeschlossenen Abrechnungslauf eine SEPA-Überweisungsdatei zum Hochladen bei Ihrer Bank, mit bei der Eingabe geprüften IBANs.',
            'Exporte un archivo de transferencia SEPA a partir de una nómina finalizada para subirlo a su banco, con los IBAN validados al introducirlos.',
            'Esporta un file di bonifico SEPA da un ciclo paga finalizzato da caricare sulla tua banca, con gli IBAN convalidati all\'inserimento.',
            "Exporteer een SEPA-overschrijvingsbestand uit een afgeronde salarisrun om te uploaden naar uw bank, met IBAN's die bij invoer worden gevalideerd."),
        'GDPR data-subject rights': _t(
            'Droits des personnes concernées (GDPR)', 'GDPR-Betroffenenrechte',
            'Derechos del interesado (GDPR)', "Diritti dell'interessato (GDPR)",
            'GDPR-rechten van betrokkenen'),
        'Built-in subject-access export (everything held about a person, as JSON) and selective erasure-with-retention, so DSARs are a workflow — with DPO contact and retention policies included.': _t(
            "Export d'accès aux données intégré (tout ce qui est détenu sur une personne, au format JSON) et effacement sélectif avec rétention, pour que les DSAR deviennent un flux de travail — avec contact du DPO et politiques de rétention inclus.",
            'Integrierter Auskunftsexport (alles, was über eine Person gespeichert ist, als JSON) und selektive Löschung mit Aufbewahrung, sodass DSARs zu einem Workflow werden — inklusive DPO-Kontakt und Aufbewahrungsrichtlinien.',
            'Exportación de acceso a datos integrada (todo lo que se guarda sobre una persona, en JSON) y supresión selectiva con retención, de modo que las DSAR sean un flujo de trabajo — con contacto del DPO y políticas de retención incluidos.',
            "Esportazione di accesso ai dati integrata (tutto ciò che è conservato su una persona, in formato JSON) e cancellazione selettiva con conservazione, così le DSAR diventano un flusso di lavoro — con contatto del DPO e criteri di conservazione inclusi.",
            "Ingebouwde export van inzage-in-gegevens (alles wat over een persoon wordt bewaard, als JSON) en selectieve wissing-met-bewaring, zodat DSAR's een workflow worden — inclusief DPO-contact en bewaarbeleid."),
        'Configurable local deductions': _t(
            'Retenues locales configurables', 'Konfigurierbare lokale Abzüge',
            'Deducciones locales configurables', 'Trattenute locali configurabili',
            'Configureerbare lokale inhoudingen'),
        "Model each country's income tax and social contributions as configurable, classified deduction types, so payslips and reports stay consistent across entities.": _t(
            "Modélisez l'impôt sur le revenu et les cotisations sociales de chaque pays sous forme de types de retenues configurables et classifiés, pour que bulletins de paie et rapports restent cohérents d'une entité à l'autre.",
            'Bilden Sie Einkommensteuer und Sozialabgaben jedes Landes als konfigurierbare, klassifizierte Abzugsarten ab, damit Gehaltsabrechnungen und Berichte über alle Gesellschaften hinweg konsistent bleiben.',
            'Modele el impuesto sobre la renta y las cotizaciones sociales de cada país como tipos de deducción configurables y clasificados, para que las nóminas y los informes se mantengan coherentes entre entidades.',
            "Modella l'imposta sul reddito e i contributi previdenziali di ogni paese come tipi di trattenuta configurabili e classificati, così buste paga e report restano coerenti tra le entità.",
            'Modelleer de inkomstenbelasting en sociale premies van elk land als configureerbare, geclassificeerde inhoudingssoorten, zodat loonstroken en rapporten consistent blijven tussen entiteiten.'),
        'Documents &amp; e-sign': _t(
            'Documents &amp; signature électronique', 'Dokumente &amp; E-Signatur',
            'Documentos &amp; firma electrónica', 'Documenti &amp; firma elettronica',
            'Documenten &amp; e-ondertekening'),
        'Contracts, letters and click-to-sign, with data-retention rules applied automatically.': _t(
            'Contrats, courriers et signature en un clic, avec application automatique des règles de rétention des données.',
            'Verträge, Schreiben und Signatur per Klick, mit automatisch angewendeten Regeln zur Datenaufbewahrung.',
            'Contratos, cartas y firma con un clic, con las reglas de retención de datos aplicadas automáticamente.',
            'Contratti, lettere e firma con un clic, con le regole di conservazione dei dati applicate automaticamente.',
            'Contracten, brieven en ondertekenen met één klik, met automatisch toegepaste regels voor gegevensbewaring.'),
        'Core HR &amp; self-service': _t(
            'RH de base &amp; libre-service', 'Kern-HR &amp; Self-Service',
            'RR. HH. básicos &amp; autoservicio', 'HR di base &amp; self-service',
            'Kern-HR &amp; selfservice'),
        'Employee records, onboarding, time off and self-service — the whole lifecycle on one platform.': _t(
            'Dossiers salariés, intégration, congés et libre-service — tout le cycle de vie sur une seule plateforme.',
            'Personalakten, Onboarding, Abwesenheiten und Self-Service — der gesamte Lebenszyklus auf einer Plattform.',
            'Expedientes de empleado, incorporación, ausencias y autoservicio — todo el ciclo de vida en una sola plataforma.',
            "Schede dipendente, onboarding, ferie e self-service — l'intero ciclo di vita su un'unica piattaforma.",
            'Personeelsdossiers, onboarding, verlof en selfservice — de hele levenscyclus op één platform.'),
        # ---- Price note (shared across the four pages) ----
        'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on.': _t(
            "Chaque module ici fait partie de HR Suite — paie avancée, fin d'année et conformité sur le plan Enterprise, ou ajoutés à n'importe quel plan en option par utilisateur.",
            'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Add-on pro Platz zu jedem Plan hinzufügbar.',
            'Cada módulo aquí forma parte de HR Suite — nóminas avanzadas, cierre de año y cumplimiento en el plan Enterprise, o añadidos a cualquier plan como complemento por usuario.',
            "Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura d'anno e conformità nel piano Enterprise, oppure aggiunti a qualsiasi piano come componente per postazione.",
            'Elke module hier maakt deel uit van HR Suite — geavanceerde salarisadministratie, jaarafsluiting en compliance in het Enterprise-plan, of aan elk plan toe te voegen als add-on per gebruiker.'),
        'See HR Suite pricing →': _t(
            'Voir les tarifs de HR Suite →', 'HR Suite Preise ansehen →',
            'Ver precios de HR Suite →', 'Vedi i prezzi di HR Suite →',
            'Bekijk prijzen van HR Suite →'),
        # ---- Countries section ----
        'Countries': _t('Pays', 'Länder', 'Países', 'Paesi', 'Landen'),
        'Countries in this region': _t(
            'Pays de cette région', 'Länder in dieser Region', 'Países de esta región',
            'Paesi di questa regione', 'Landen in deze regio'),
        'Pick a country for its statutory payroll and compliance detail — and it runs across the wider region too.': _t(
            "Choisissez un pays pour le détail de sa paie légale et de sa conformité — et cela fonctionne aussi dans l'ensemble de la région.",
            'Wählen Sie ein Land für die Details zu gesetzlicher Abrechnung und Compliance — und es funktioniert auch in der gesamten Region.',
            'Elija un país para ver el detalle de su nómina legal y su cumplimiento — y también funciona en toda la región.',
            'Scegli un paese per il dettaglio della sua busta paga di legge e della conformità — e funziona anche in tutta la regione.',
            'Kies een land voor de details van de wettelijke salarisverwerking en compliance — en het werkt ook in de bredere regio.'),
        # Cross-grid country names (tag-wrapped to avoid short-name collisions)
        '<h4>United Kingdom</h4>': _t('<h4>Royaume-Uni</h4>', '<h4>Vereinigtes Königreich</h4>', '<h4>Reino Unido</h4>', '<h4>Regno Unito</h4>', '<h4>Verenigd Koninkrijk</h4>'),
        '<h4>Ireland</h4>': _t('<h4>Irlande</h4>', '<h4>Irland</h4>', '<h4>Irlanda</h4>', '<h4>Irlanda</h4>', '<h4>Ierland</h4>'),
        '<h4>France</h4>': _t('<h4>France</h4>', '<h4>Frankreich</h4>', '<h4>Francia</h4>', '<h4>Francia</h4>', '<h4>Frankrijk</h4>'),
        '<h4>Germany</h4>': _t('<h4>Allemagne</h4>', '<h4>Deutschland</h4>', '<h4>Alemania</h4>', '<h4>Germania</h4>', '<h4>Duitsland</h4>'),
        '<h4>Spain</h4>': _t('<h4>Espagne</h4>', '<h4>Spanien</h4>', '<h4>España</h4>', '<h4>Spagna</h4>', '<h4>Spanje</h4>'),
        '<h4>Italy</h4>': _t('<h4>Italie</h4>', '<h4>Italien</h4>', '<h4>Italia</h4>', '<h4>Italia</h4>', '<h4>Italië</h4>'),
        '<h4>Netherlands</h4>': _t('<h4>Pays-Bas</h4>', '<h4>Niederlande</h4>', '<h4>Países Bajos</h4>', '<h4>Paesi Bassi</h4>', '<h4>Nederland</h4>'),
        # Cross-grid "served" labels (acronyms kept per rules)
        'PAYE · NI · P60/P45': _t('PAYE · NI · P60/P45', 'PAYE · NI · P60/P45', 'PAYE · NI · P60/P45', 'PAYE · NI · P60/P45', 'PAYE · NI · P60/P45'),
        'Leave · SEPA · GDPR': _t('Congés · SEPA · GDPR', 'Urlaub · SEPA · GDPR', 'Permisos · SEPA · GDPR', 'Ferie · SEPA · GDPR', 'Verlof · SEPA · GDPR'),
        '35h week · SEPA · GDPR': _t('Semaine 35h · SEPA · GDPR', '35-Std.-Woche · SEPA · GDPR', 'Semana de 35h · SEPA · GDPR', 'Settimana di 35h · SEPA · GDPR', '35-urige week · SEPA · GDPR'),
        'Overtime · SEPA · GDPR': _t('Heures supplémentaires · SEPA · GDPR', 'Überstunden · SEPA · GDPR', 'Horas extra · SEPA · GDPR', 'Straordinari · SEPA · GDPR', 'Overwerk · SEPA · GDPR'),
        # Regional footnote
        'Also runs across the region:': _t(
            'Fonctionne aussi dans toute la région :', 'Läuft auch in der gesamten Region:',
            'También funciona en toda la región:', 'Funziona anche in tutta la regione:',
            'Werkt ook in de hele regio:'),
        'Belgium · Portugal · Poland · Sweden · Denmark · Finland · Austria · Greece · and the rest of the EU / EEA — with configurable local payroll, end-of-service and multi-currency pay.': _t(
            "Belgique · Portugal · Pologne · Suède · Danemark · Finlande · Autriche · Grèce · et le reste de l'UE / EEE — avec paie locale configurable, indemnités de fin de contrat et paiements multidevises.",
            'Belgien · Portugal · Polen · Schweden · Dänemark · Finnland · Österreich · Griechenland · und den Rest der EU / des EWR — mit konfigurierbarer lokaler Abrechnung, Abfindung bei Vertragsende und Mehrwährungszahlungen.',
            'Bélgica · Portugal · Polonia · Suecia · Dinamarca · Finlandia · Austria · Grecia · y el resto de la UE / EEE — con nómina local configurable, liquidación por fin de contrato y pagos multidivisa.',
            "Belgio · Portogallo · Polonia · Svezia · Danimarca · Finlandia · Austria · Grecia · e il resto dell'UE / SEE — con busta paga locale configurabile, trattamento di fine rapporto e pagamenti multivaluta.",
            "België · Portugal · Polen · Zweden · Denemarken · Finland · Oostenrijk · Griekenland · en de rest van de EU / EER — met configureerbare lokale salarisverwerking, eindafrekening en betalingen in meerdere valuta's."),
        'Ask about your market →': _t(
            'Renseignez-vous sur votre marché →', 'Fragen Sie nach Ihrem Markt →',
            'Pregunte por su mercado →', 'Chiedi informazioni sul tuo mercato →',
            'Vraag naar uw markt →'),
        # ---- CTA ----
        'Run your European operation on one platform': _t(
            'Gérez votre activité européenne sur une seule plateforme',
            'Führen Sie Ihren europäischen Betrieb auf einer Plattform',
            'Gestione su operación europea en una sola plataforma',
            "Gestisci la tua attività europea su un'unica piattaforma",
            'Run uw Europese activiteiten op één platform'),
    },
}

PAGE['/regions/uk/'] = {
    'src': 'regions/uk/index.html',
    't': {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for United Kingdom | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour le Royaume-Uni | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für das Vereinigte Königreich | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para el Reino Unido | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per il Regno Unito | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor het Verenigd Koninkrijk | FulcrumGrid'),
        'HR Suite for the UK — PAYE and National Insurance deductions, P60 and P45 statements, NINO validation, workplace pensions, and full HR on one platform.': _t(
            'HR Suite pour le Royaume-Uni — retenues PAYE et National Insurance, attestations P60 et P45, validation NINO, retraites professionnelles, et RH complète sur une seule plateforme.',
            'HR Suite für das Vereinigte Königreich — PAYE- und National-Insurance-Abzüge, P60- und P45-Bescheinigungen, NINO-Validierung, betriebliche Renten und vollständiges HR auf einer Plattform.',
            'HR Suite para el Reino Unido — deducciones de PAYE y National Insurance, certificados P60 y P45, validación de NINO, pensiones de empresa y RR. HH. completos en una sola plataforma.',
            "HR Suite per il Regno Unito — trattenute PAYE e National Insurance, attestazioni P60 e P45, validazione NINO, pensioni aziendali e HR completo su un'unica piattaforma.",
            'HR Suite voor het Verenigd Koninkrijk — PAYE- en National Insurance-inhoudingen, P60- en P45-overzichten, NINO-validatie, bedrijfspensioenen en volledige HR op één platform.'),
        # ---- Hero ----
        'United Kingdom · UK': _t('Royaume-Uni · UK', 'Vereinigtes Königreich · UK', 'Reino Unido · UK', 'Regno Unito · UK', 'Verenigd Koninkrijk · UK'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">the UK</em>': _t(
            'RH &amp; paie, conçues pour <em style="font-style:normal;color:var(--color-accent)">le Royaume-Uni</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">das Vereinigte Königreich</em>',
            'RR. HH. &amp; nóminas, diseñados para <em style="font-style:normal;color:var(--color-accent)">el Reino Unido</em>',
            'HR &amp; buste paga, creati per <em style="font-style:normal;color:var(--color-accent)">il Regno Unito</em>',
            'HR &amp; salaris, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">het Verenigd Koninkrijk</em>'),
        'HR Suite runs your UK workforce end to end — PAYE and National Insurance on a configurable payroll, P60 and P45 statements, NINO validation, pensions, and full employee records.': _t(
            'HR Suite gère vos effectifs britanniques de bout en bout — PAYE et National Insurance sur une paie configurable, attestations P60 et P45, validation NINO, retraites et dossiers salariés complets.',
            'HR Suite steuert Ihre britische Belegschaft durchgängig — PAYE und National Insurance auf einer konfigurierbaren Abrechnung, P60- und P45-Bescheinigungen, NINO-Validierung, Renten und vollständige Personalakten.',
            'HR Suite gestiona su plantilla del Reino Unido de principio a fin — PAYE y National Insurance en una nómina configurable, certificados P60 y P45, validación de NINO, pensiones y expedientes de empleado completos.',
            "HR Suite gestisce il tuo personale nel Regno Unito dall'inizio alla fine — PAYE e National Insurance su una busta paga configurabile, attestazioni P60 e P45, validazione NINO, pensioni e schede dipendente complete.",
            'HR Suite runt uw Britse personeelsbestand van begin tot eind — PAYE en National Insurance op een configureerbare salarisverwerking, P60- en P45-overzichten, NINO-validatie, pensioenen en volledige personeelsdossiers.'),
        'Explore HR Suite': _t('Découvrir HR Suite', 'HR Suite entdecken', 'Explorar HR Suite', 'Esplora HR Suite', 'Ontdek HR Suite'),
        'See HR Suite pricing': _t('Voir les tarifs de HR Suite', 'HR Suite Preise ansehen', 'Ver precios de HR Suite', 'Vedi i prezzi di HR Suite', 'Bekijk prijzen van HR Suite'),
        # ---- Built-in section ----
        'Built in': _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd'),
        'United Kingdom compliance, out of the box': _t(
            "Conformité Royaume-Uni, prête à l'emploi", 'Compliance für das Vereinigte Königreich, sofort einsatzbereit',
            'Cumplimiento para el Reino Unido, listo para usar', "Conformità Regno Unito, pronta all'uso",
            'Compliance voor het Verenigd Koninkrijk, kant-en-klaar'),
        'The modules that make HR Suite work the way United Kingdom does — each part of the same platform, no separate tools.': _t(
            'Les modules qui font fonctionner HR Suite à la manière du Royaume-Uni — chacun faisant partie de la même plateforme, sans outils séparés.',
            'Die Module, die HR Suite so arbeiten lassen, wie das Vereinigte Königreich es tut — jedes Teil derselben Plattform, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace el Reino Unido — cada uno parte de la misma plataforma, sin herramientas aparte.',
            'I moduli che fanno funzionare HR Suite come fa il Regno Unito — ognuno parte della stessa piattaforma, senza strumenti separati.',
            'De modules die HR Suite laten werken zoals het Verenigd Koninkrijk dat doet — elk onderdeel van hetzelfde platform, zonder losse tools.'),
        # ---- Features ----
        'PAYE &amp; National Insurance': _t(
            'PAYE &amp; National Insurance', 'PAYE &amp; National Insurance',
            'PAYE &amp; National Insurance', 'PAYE &amp; National Insurance',
            'PAYE &amp; National Insurance'),
        'Pay runs with deductions classified as PAYE income tax (rest-of-UK and Scottish rates) and National Insurance, on a configurable engine that keeps payslips and reports aligned.': _t(
            'Des paies avec retenues classées en impôt sur le revenu PAYE (taux du reste du Royaume-Uni et taux écossais) et National Insurance, sur un moteur configurable qui garde bulletins de paie et rapports alignés.',
            'Abrechnungsläufe mit Abzügen, klassifiziert als PAYE-Einkommensteuer (Sätze des übrigen Vereinigten Königreichs und schottische Sätze) und National Insurance, auf einer konfigurierbaren Engine, die Gehaltsabrechnungen und Berichte im Einklang hält.',
            'Nóminas con deducciones clasificadas como impuesto sobre la renta PAYE (tipos del resto del Reino Unido y tipos escoceses) y National Insurance, sobre un motor configurable que mantiene alineados nóminas e informes.',
            'Cicli paga con trattenute classificate come imposta sul reddito PAYE (aliquote del resto del Regno Unito e aliquote scozzesi) e National Insurance, su un motore configurabile che mantiene allineati buste paga e report.',
            'Salarisruns met inhoudingen die worden geclassificeerd als PAYE-inkomstenbelasting (tarieven voor de rest van het Verenigd Koninkrijk en Schotse tarieven) en National Insurance, op een configureerbare engine die loonstroken en rapporten op één lijn houdt.'),
        'P60 &amp; P45 statements': _t(
            'Attestations P60 &amp; P45', 'P60- &amp; P45-Bescheinigungen',
            'Certificados P60 &amp; P45', 'Attestazioni P60 &amp; P45', 'P60- &amp; P45-overzichten'),
        'Generate P60 (year-end) and P45 (leaver) statements from your finalized pay runs — statements from your own records, not the official HMRC form or an RTI submission.': _t(
            "Générez des attestations P60 (fin d'année) et P45 (départ) à partir de vos paies finalisées — des attestations issues de vos propres données, et non le formulaire officiel HMRC ni une soumission RTI.",
            'Erstellen Sie P60- (Jahresende) und P45-Bescheinigungen (Austritt) aus Ihren abgeschlossenen Abrechnungsläufen — Bescheinigungen aus Ihren eigenen Aufzeichnungen, nicht das offizielle HMRC-Formular oder eine RTI-Meldung.',
            'Genere certificados P60 (cierre de año) y P45 (baja) a partir de sus nóminas finalizadas — certificados a partir de sus propios registros, no el formulario oficial de HMRC ni un envío RTI.',
            'Genera attestazioni P60 (fine anno) e P45 (cessazione) dai tuoi cicli paga finalizzati — attestazioni dai tuoi stessi dati, non il modulo ufficiale HMRC né un invio RTI.',
            'Genereer P60- (jaareinde) en P45-overzichten (uitdiensttreding) uit uw afgeronde salarisruns — overzichten uit uw eigen administratie, niet het officiële HMRC-formulier of een RTI-indiening.'),
        'NINO validation': _t('Validation du NINO', 'NINO-Validierung', 'Validación de NINO', 'Validazione NINO', 'NINO-validatie'),
        'National Insurance numbers are checksum-validated on entry, so employee records stay clean and payroll-ready.': _t(
            'Les numéros National Insurance sont validés par somme de contrôle à la saisie, pour que les dossiers salariés restent propres et prêts pour la paie.',
            'National-Insurance-Nummern werden bei der Eingabe per Prüfsumme validiert, sodass Personalakten sauber und abrechnungsbereit bleiben.',
            'Los números de National Insurance se validan por suma de comprobación al introducirlos, de modo que los expedientes de empleado se mantengan limpios y listos para la nómina.',
            'I numeri National Insurance vengono validati tramite checksum all\'inserimento, così le schede dipendente restano pulite e pronte per la busta paga.',
            'National Insurance-nummers worden bij invoer met een checksum gevalideerd, zodat personeelsdossiers schoon en klaar voor salarisverwerking blijven.'),
        'Pensions &amp; deductions': _t(
            'Retraites &amp; retenues', 'Renten &amp; Abzüge', 'Pensiones &amp; deducciones',
            'Pensioni &amp; trattenute', 'Pensioenen &amp; inhoudingen'),
        'Model workplace pension and other pre- and post-tax deductions on the same engine, with employer contributions tracked as company cost.': _t(
            "Modélisez la retraite professionnelle et d'autres retenues avant et après impôt sur le même moteur, avec les cotisations patronales suivies comme coût de l'entreprise.",
            'Bilden Sie betriebliche Rente und weitere Abzüge vor und nach Steuern auf derselben Engine ab, wobei Arbeitgeberbeiträge als Unternehmenskosten erfasst werden.',
            'Modele la pensión de empresa y otras deducciones antes y después de impuestos en el mismo motor, con las aportaciones del empleador registradas como coste de la empresa.',
            'Modella la pensione aziendale e altre trattenute al lordo e al netto delle imposte sullo stesso motore, con i contributi del datore di lavoro registrati come costo aziendale.',
            'Modelleer bedrijfspensioen en andere inhoudingen vóór en na belasting op dezelfde engine, met werkgeversbijdragen bijgehouden als bedrijfskosten.'),
        'Core HR &amp; self-service': _t(
            'RH de base &amp; libre-service', 'Kern-HR &amp; Self-Service',
            'RR. HH. básicos &amp; autoservicio', 'HR di base &amp; self-service',
            'Kern-HR &amp; selfservice'),
        'Employee records, onboarding, time off, documents and employee self-service — the whole lifecycle on one platform.': _t(
            'Dossiers salariés, intégration, congés, documents et libre-service employé — tout le cycle de vie sur une seule plateforme.',
            'Personalakten, Onboarding, Abwesenheiten, Dokumente und Mitarbeiter-Self-Service — der gesamte Lebenszyklus auf einer Plattform.',
            'Expedientes de empleado, incorporación, ausencias, documentos y autoservicio del empleado — todo el ciclo de vida en una sola plataforma.',
            "Schede dipendente, onboarding, ferie, documenti e self-service dipendente — l'intero ciclo di vita su un'unica piattaforma.",
            'Personeelsdossiers, onboarding, verlof, documenten en selfservice voor medewerkers — de hele levenscyclus op één platform.'),
        # ---- Price note ----
        'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on.': _t(
            "Chaque module ici fait partie de HR Suite — paie avancée, fin d'année et conformité sur le plan Enterprise, ou ajoutés à n'importe quel plan en option par utilisateur.",
            'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Add-on pro Platz zu jedem Plan hinzufügbar.',
            'Cada módulo aquí forma parte de HR Suite — nóminas avanzadas, cierre de año y cumplimiento en el plan Enterprise, o añadidos a cualquier plan como complemento por usuario.',
            "Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura d'anno e conformità nel piano Enterprise, oppure aggiunti a qualsiasi piano come componente per postazione.",
            'Elke module hier maakt deel uit van HR Suite — geavanceerde salarisadministratie, jaarafsluiting en compliance in het Enterprise-plan, of aan elk plan toe te voegen als add-on per gebruiker.'),
        'See HR Suite pricing →': _t(
            'Voir les tarifs de HR Suite →', 'HR Suite Preise ansehen →',
            'Ver precios de HR Suite →', 'Vedi i prezzi di HR Suite →',
            'Bekijk prijzen van HR Suite →'),
        # ---- CTA ----
        'Run UK HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie britanniques comme il se doit',
            'HR &amp; Gehaltsabrechnung im Vereinigten Königreich richtig aufsetzen',
            'Gestione los RR. HH. &amp; las nóminas del Reino Unido como es debido',
            'Gestisci HR &amp; buste paga nel Regno Unito nel modo giusto',
            'Regel HR &amp; salaris in het Verenigd Koninkrijk op de juiste manier'),
        'See HR Suite handle UK PAYE, National Insurance, and year-end for your team.': _t(
            "Voyez HR Suite gérer le PAYE britannique, la National Insurance et la fin d'année de votre équipe.",
            'Sehen Sie, wie HR Suite PAYE, National Insurance und Jahresende für Ihr Team im Vereinigten Königreich erledigt.',
            'Vea cómo HR Suite gestiona el PAYE del Reino Unido, la National Insurance y el cierre de año de su equipo.',
            "Guarda HR Suite gestire il PAYE del Regno Unito, la National Insurance e la chiusura d'anno del tuo team.",
            'Zie hoe HR Suite de Britse PAYE, National Insurance en het jaareinde voor uw team afhandelt.'),
    },
}

PAGE['/regions/ireland/'] = {
    'src': 'regions/ireland/index.html',
    't': {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for Ireland | FulcrumGrid': _t(
            "HR Suite — RH &amp; paie pour l'Irlande | FulcrumGrid",
            'HR Suite — HR &amp; Gehaltsabrechnung für Irland | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Irlanda | FulcrumGrid',
            "HR Suite — HR &amp; buste paga per l'Irlanda | FulcrumGrid",
            'HR Suite — HR &amp; salarisadministratie voor Ierland | FulcrumGrid'),
        'HR Suite for Ireland — statutory leave and holidays, SEPA pay files, GDPR rights, configurable local payroll (PAYE/PRSI/USC) in EUR, and full HR.': _t(
            "HR Suite pour l'Irlande — congés et jours fériés légaux, fichiers de paiement SEPA, droits GDPR, paie locale configurable (PAYE/PRSI/USC) en EUR, et RH complète.",
            'HR Suite für Irland — gesetzlicher Urlaub und Feiertage, SEPA-Zahlungsdateien, GDPR-Rechte, konfigurierbare lokale Abrechnung (PAYE/PRSI/USC) in EUR und vollständiges HR.',
            'HR Suite para Irlanda — permisos y festivos legales, archivos de pago SEPA, derechos del GDPR, nómina local configurable (PAYE/PRSI/USC) en EUR y RR. HH. completos.',
            "HR Suite per l'Irlanda — ferie e festività di legge, file di pagamento SEPA, diritti GDPR, busta paga locale configurabile (PAYE/PRSI/USC) in EUR e HR completo.",
            'HR Suite voor Ierland — wettelijk verlof en feestdagen, SEPA-betaalbestanden, GDPR-rechten, configureerbare lokale salarisverwerking (PAYE/PRSI/USC) in EUR en volledige HR.'),
        # ---- Hero ----
        'Ireland · IE': _t('Irlande · IE', 'Irland · IE', 'Irlanda · IE', 'Irlanda · IE', 'Ierland · IE'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">Ireland</em>': _t(
            'RH &amp; paie, conçues pour <em style="font-style:normal;color:var(--color-accent)">l\'Irlande</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Irland</em>',
            'RR. HH. &amp; nóminas, diseñados para <em style="font-style:normal;color:var(--color-accent)">Irlanda</em>',
            'HR &amp; buste paga, creati per <em style="font-style:normal;color:var(--color-accent)">l\'Irlanda</em>',
            'HR &amp; salaris, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Ierland</em>'),
        'HR Suite runs your Ireland workforce — statutory leave and the local holiday calendar, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.': _t(
            "HR Suite gère vos effectifs en Irlande — congés légaux et calendrier des jours fériés locaux, fichiers de paiement SEPA, droits des personnes concernées au titre du GDPR, paie locale configurable en EUR, et dossiers salariés complets.",
            'HR Suite steuert Ihre Belegschaft in Irland — gesetzlicher Urlaub und lokaler Feiertagskalender, SEPA-Zahlungsdateien, GDPR-Betroffenenrechte, konfigurierbare lokale Abrechnung in EUR und vollständige Personalakten.',
            'HR Suite gestiona su plantilla en Irlanda — permisos legales y calendario de festivos locales, archivos de pago SEPA, derechos del interesado según el GDPR, nómina local configurable en EUR y expedientes de empleado completos.',
            "HR Suite gestisce il tuo personale in Irlanda — ferie di legge e calendario delle festività locali, file di pagamento SEPA, diritti dell'interessato ai sensi del GDPR, busta paga locale configurabile in EUR e schede dipendente complete.",
            'HR Suite runt uw personeelsbestand in Ierland — wettelijk verlof en de lokale feestdagenkalender, SEPA-betaalbestanden, GDPR-rechten van betrokkenen, configureerbare lokale salarisverwerking in EUR en volledige personeelsdossiers.'),
        'Explore HR Suite': _t('Découvrir HR Suite', 'HR Suite entdecken', 'Explorar HR Suite', 'Esplora HR Suite', 'Ontdek HR Suite'),
        'See HR Suite pricing': _t('Voir les tarifs de HR Suite', 'HR Suite Preise ansehen', 'Ver precios de HR Suite', 'Vedi i prezzi di HR Suite', 'Bekijk prijzen van HR Suite'),
        # ---- Built-in section ----
        'Built in': _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd'),
        'Ireland compliance, out of the box': _t(
            "Conformité Irlande, prête à l'emploi", 'Irland-Compliance, sofort einsatzbereit',
            'Cumplimiento para Irlanda, listo para usar', "Conformità Irlanda, pronta all'uso",
            'Ierland-compliance, kant-en-klaar'),
        'The modules that make HR Suite work the way Ireland does — each part of the same platform, no separate tools.': _t(
            "Les modules qui font fonctionner HR Suite à la manière de l'Irlande — chacun faisant partie de la même plateforme, sans outils séparés.",
            'Die Module, die HR Suite so arbeiten lassen, wie Irland es tut — jedes Teil derselben Plattform, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Irlanda — cada uno parte de la misma plataforma, sin herramientas aparte.',
            "I moduli che fanno funzionare HR Suite come fa l'Irlanda — ognuno parte della stessa piattaforma, senza strumenti separati.",
            'De modules die HR Suite laten werken zoals Ierland dat doet — elk onderdeel van hetzelfde platform, zonder losse tools.'),
        # ---- Features ----
        'Statutory leave &amp; holidays': _t(
            'Congés légaux &amp; jours fériés', 'Gesetzlicher Urlaub &amp; Feiertage',
            'Permisos legales &amp; festivos', 'Ferie di legge &amp; festività',
            'Wettelijk verlof &amp; feestdagen'),
        'Statutory annual leave and the Irish public-holiday calendar, built in.': _t(
            'Congés annuels légaux et calendrier irlandais des jours fériés, intégrés.',
            'Gesetzlicher Jahresurlaub und der irische Feiertagskalender, integriert.',
            'Vacaciones anuales legales y el calendario irlandés de festivos, integrados.',
            'Ferie annuali di legge e il calendario irlandese delle festività, integrati.',
            'Wettelijke jaarlijkse vakantie en de Ierse feestdagenkalender, ingebouwd.'),
        'SEPA payments': _t('Paiements SEPA', 'SEPA-Zahlungen', 'Pagos SEPA', 'Pagamenti SEPA', 'SEPA-betalingen'),
        'Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.': _t(
            "Exportez un fichier de virement SEPA à partir d'une paie finalisée, avec des IBAN validés à la saisie.",
            'Exportieren Sie aus einem abgeschlossenen Abrechnungslauf eine SEPA-Überweisungsdatei, mit bei der Eingabe geprüften IBANs.',
            'Exporte un archivo de transferencia SEPA a partir de una nómina finalizada, con los IBAN validados al introducirlos.',
            "Esporta un file di bonifico SEPA da un ciclo paga finalizzato, con gli IBAN convalidati all'inserimento.",
            "Exporteer een SEPA-overschrijvingsbestand uit een afgeronde salarisrun, met IBAN's die bij invoer worden gevalideerd."),
        'GDPR data-subject rights': _t(
            'Droits des personnes concernées (GDPR)', 'GDPR-Betroffenenrechte',
            'Derechos del interesado (GDPR)', "Diritti dell'interessato (GDPR)",
            'GDPR-rechten van betrokkenen'),
        'Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.': _t(
            "Export d'accès aux données et effacement sélectif avec rétention, avec contact du DPO et politiques de rétention intégrés.",
            'Auskunftsexport und selektive Löschung mit Aufbewahrung, mit integriertem DPO-Kontakt und Aufbewahrungsrichtlinien.',
            'Exportación de acceso a datos y supresión selectiva con retención, con contacto del DPO y políticas de retención integrados.',
            'Esportazione di accesso ai dati e cancellazione selettiva con conservazione, con contatto del DPO e criteri di conservazione integrati.',
            'Export van inzage-in-gegevens en selectieve wissing-met-bewaring, met ingebouwd DPO-contact en bewaarbeleid.'),
        'Local payroll &amp; core HR': _t(
            'Paie locale &amp; RH de base', 'Lokale Abrechnung &amp; Kern-HR',
            'Nómina local &amp; RR. HH. básicos', 'Busta paga locale &amp; HR di base',
            'Lokale salarisverwerking &amp; kern-HR'),
        'Model Irish income tax (PAYE), PRSI and USC as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.': _t(
            "Modélisez l'impôt sur le revenu irlandais (PAYE), la PRSI et l'USC comme des retenues configurables et classifiées — avec dossiers salariés, intégration, congés et libre-service, en EUR.",
            'Bilden Sie die irische Einkommensteuer (PAYE), PRSI und USC als konfigurierbare, klassifizierte Abzüge ab — mit Personalakten, Onboarding, Abwesenheiten und Self-Service, in EUR.',
            'Modele el impuesto sobre la renta irlandés (PAYE), el PRSI y el USC como deducciones configurables y clasificadas — con expedientes de empleado, incorporación, ausencias y autoservicio, en EUR.',
            "Modella l'imposta sul reddito irlandese (PAYE), PRSI e USC come trattenute configurabili e classificate — con schede dipendente, onboarding, ferie e self-service, in EUR.",
            'Modelleer de Ierse inkomstenbelasting (PAYE), PRSI en USC als configureerbare, geclassificeerde inhoudingen — met personeelsdossiers, onboarding, verlof en selfservice, in EUR.'),
        # ---- Price note ----
        'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on.': _t(
            "Chaque module ici fait partie de HR Suite — paie avancée, fin d'année et conformité sur le plan Enterprise, ou ajoutés à n'importe quel plan en option par utilisateur.",
            'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Add-on pro Platz zu jedem Plan hinzufügbar.',
            'Cada módulo aquí forma parte de HR Suite — nóminas avanzadas, cierre de año y cumplimiento en el plan Enterprise, o añadidos a cualquier plan como complemento por usuario.',
            "Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura d'anno e conformità nel piano Enterprise, oppure aggiunti a qualsiasi piano come componente per postazione.",
            'Elke module hier maakt deel uit van HR Suite — geavanceerde salarisadministratie, jaarafsluiting en compliance in het Enterprise-plan, of aan elk plan toe te voegen als add-on per gebruiker.'),
        'See HR Suite pricing →': _t(
            'Voir les tarifs de HR Suite →', 'HR Suite Preise ansehen →',
            'Ver precios de HR Suite →', 'Vedi i prezzi di HR Suite →',
            'Bekijk prijzen van HR Suite →'),
        # ---- CTA ----
        'Run Ireland HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie irlandaises comme il se doit',
            'Irisches HR &amp; Gehaltsabrechnung richtig aufsetzen',
            'Gestione los RR. HH. &amp; las nóminas de Irlanda como es debido',
            'Gestisci HR &amp; buste paga irlandesi nel modo giusto',
            'Regel Ierse HR &amp; salaris op de juiste manier'),
        'See HR Suite handle Irish leave, SEPA and GDPR for your team.': _t(
            'Voyez HR Suite gérer les congés irlandais, le SEPA et le GDPR de votre équipe.',
            'Sehen Sie, wie HR Suite irischen Urlaub, SEPA und GDPR für Ihr Team erledigt.',
            'Vea cómo HR Suite gestiona los permisos irlandeses, SEPA y el GDPR de su equipo.',
            'Guarda HR Suite gestire le ferie irlandesi, il SEPA e il GDPR del tuo team.',
            'Zie hoe HR Suite Iers verlof, SEPA en het GDPR voor uw team afhandelt.'),
    },
}

PAGE['/regions/france/'] = {
    'src': 'regions/france/index.html',
    't': {
        # ---- Meta ----
        'HR Suite — HR &amp; payroll for France | FulcrumGrid': _t(
            'HR Suite — RH &amp; paie pour la France | FulcrumGrid',
            'HR Suite — HR &amp; Gehaltsabrechnung für Frankreich | FulcrumGrid',
            'HR Suite — RR. HH. &amp; nóminas para Francia | FulcrumGrid',
            'HR Suite — HR &amp; buste paga per la Francia | FulcrumGrid',
            'HR Suite — HR &amp; salarisadministratie voor Frankrijk | FulcrumGrid'),
        'HR Suite for France — statutory 35-hour-week overtime, SEPA pay files, GDPR rights, configurable local payroll in EUR, and full HR.': _t(
            'HR Suite pour la France — heures supplémentaires sur la base légale des 35 heures, fichiers de paiement SEPA, droits GDPR, paie locale configurable en EUR, et RH complète.',
            'HR Suite für Frankreich — Überstunden auf Basis der gesetzlichen 35-Stunden-Woche, SEPA-Zahlungsdateien, GDPR-Rechte, konfigurierbare lokale Abrechnung in EUR und vollständiges HR.',
            'HR Suite para Francia — horas extra según la semana legal de 35 horas, archivos de pago SEPA, derechos del GDPR, nómina local configurable en EUR y RR. HH. completos.',
            'HR Suite per la Francia — straordinari sulla base della settimana legale di 35 ore, file di pagamento SEPA, diritti GDPR, busta paga locale configurabile in EUR e HR completo.',
            'HR Suite voor Frankrijk — overwerk op basis van de wettelijke 35-urige werkweek, SEPA-betaalbestanden, GDPR-rechten, configureerbare lokale salarisverwerking in EUR en volledige HR.'),
        # ---- Hero ----
        'France · FR': _t('France · FR', 'Frankreich · FR', 'Francia · FR', 'Francia · FR', 'Frankrijk · FR'),
        'HR &amp; payroll, built for <em style="font-style:normal;color:var(--color-accent)">France</em>': _t(
            'RH &amp; paie, conçues pour <em style="font-style:normal;color:var(--color-accent)">la France</em>',
            'HR &amp; Gehaltsabrechnung, entwickelt für <em style="font-style:normal;color:var(--color-accent)">Frankreich</em>',
            'RR. HH. &amp; nóminas, diseñados para <em style="font-style:normal;color:var(--color-accent)">Francia</em>',
            'HR &amp; buste paga, creati per <em style="font-style:normal;color:var(--color-accent)">la Francia</em>',
            'HR &amp; salaris, gebouwd voor <em style="font-style:normal;color:var(--color-accent)">Frankrijk</em>'),
        'HR Suite runs your France workforce — overtime priced to the statutory 35-hour week, SEPA pay files, GDPR data-subject rights, configurable local payroll in EUR, and full employee records.': _t(
            "HR Suite gère vos effectifs en France — heures supplémentaires valorisées selon la semaine légale de 35 heures, fichiers de paiement SEPA, droits des personnes concernées au titre du GDPR, paie locale configurable en EUR, et dossiers salariés complets.",
            'HR Suite steuert Ihre Belegschaft in Frankreich — Überstunden bewertet nach der gesetzlichen 35-Stunden-Woche, SEPA-Zahlungsdateien, GDPR-Betroffenenrechte, konfigurierbare lokale Abrechnung in EUR und vollständige Personalakten.',
            'HR Suite gestiona su plantilla en Francia — horas extra valoradas según la semana legal de 35 horas, archivos de pago SEPA, derechos del interesado según el GDPR, nómina local configurable en EUR y expedientes de empleado completos.',
            "HR Suite gestisce il tuo personale in Francia — straordinari valorizzati secondo la settimana legale di 35 ore, file di pagamento SEPA, diritti dell'interessato ai sensi del GDPR, busta paga locale configurabile in EUR e schede dipendente complete.",
            'HR Suite runt uw personeelsbestand in Frankrijk — overwerk gewaardeerd volgens de wettelijke 35-urige werkweek, SEPA-betaalbestanden, GDPR-rechten van betrokkenen, configureerbare lokale salarisverwerking in EUR en volledige personeelsdossiers.'),
        'Explore HR Suite': _t('Découvrir HR Suite', 'HR Suite entdecken', 'Explorar HR Suite', 'Esplora HR Suite', 'Ontdek HR Suite'),
        'See HR Suite pricing': _t('Voir les tarifs de HR Suite', 'HR Suite Preise ansehen', 'Ver precios de HR Suite', 'Vedi i prezzi di HR Suite', 'Bekijk prijzen van HR Suite'),
        # ---- Built-in section ----
        'Built in': _t('Intégré', 'Integriert', 'Integrado', 'Integrato', 'Ingebouwd'),
        'France compliance, out of the box': _t(
            "Conformité France, prête à l'emploi", 'Frankreich-Compliance, sofort einsatzbereit',
            'Cumplimiento para Francia, listo para usar', "Conformità Francia, pronta all'uso",
            'Frankrijk-compliance, kant-en-klaar'),
        'The modules that make HR Suite work the way France does — each part of the same platform, no separate tools.': _t(
            'Les modules qui font fonctionner HR Suite à la manière de la France — chacun faisant partie de la même plateforme, sans outils séparés.',
            'Die Module, die HR Suite so arbeiten lassen, wie Frankreich es tut — jedes Teil derselben Plattform, keine separaten Tools.',
            'Los módulos que hacen que HR Suite funcione como lo hace Francia — cada uno parte de la misma plataforma, sin herramientas aparte.',
            'I moduli che fanno funzionare HR Suite come fa la Francia — ognuno parte della stessa piattaforma, senza strumenti separati.',
            'De modules die HR Suite laten werken zoals Frankrijk dat doet — elk onderdeel van hetzelfde platform, zonder losse tools.'),
        # ---- Features ----
        'Overtime — 35-hour week': _t(
            'Heures supplémentaires — semaine de 35 heures', 'Überstunden — 35-Stunden-Woche',
            'Horas extra — semana de 35 horas', 'Straordinari — settimana di 35 ore',
            'Overwerk — 35-urige werkweek'),
        'Overtime priced to the statutory 35-hour week — +25% for the first eight hours (36–43) and +50% beyond, with collective-agreement rates configurable.': _t(
            'Heures supplémentaires valorisées selon la semaine légale de 35 heures — +25 % pour les huit premières heures (36–43) et +50 % au-delà, avec des taux conventionnels configurables.',
            'Überstunden bewertet nach der gesetzlichen 35-Stunden-Woche — +25 % für die ersten acht Stunden (36–43) und +50 % darüber hinaus, mit konfigurierbaren tarifvertraglichen Sätzen.',
            'Horas extra valoradas según la semana legal de 35 horas — +25 % para las primeras ocho horas (36–43) y +50 % a partir de ahí, con tipos de convenio colectivo configurables.',
            'Straordinari valorizzati secondo la settimana legale di 35 ore — +25% per le prime otto ore (36–43) e +50% oltre, con aliquote da contratto collettivo configurabili.',
            'Overwerk gewaardeerd volgens de wettelijke 35-urige werkweek — +25% voor de eerste acht uur (36–43) en +50% daarboven, met configureerbare cao-tarieven.'),
        'SEPA payments': _t('Paiements SEPA', 'SEPA-Zahlungen', 'Pagos SEPA', 'Pagamenti SEPA', 'SEPA-betalingen'),
        'Export a SEPA credit-transfer file from a finalized pay run, with IBANs validated on entry.': _t(
            "Exportez un fichier de virement SEPA à partir d'une paie finalisée, avec des IBAN validés à la saisie.",
            'Exportieren Sie aus einem abgeschlossenen Abrechnungslauf eine SEPA-Überweisungsdatei, mit bei der Eingabe geprüften IBANs.',
            'Exporte un archivo de transferencia SEPA a partir de una nómina finalizada, con los IBAN validados al introducirlos.',
            "Esporta un file di bonifico SEPA da un ciclo paga finalizzato, con gli IBAN convalidati all'inserimento.",
            "Exporteer een SEPA-overschrijvingsbestand uit een afgeronde salarisrun, met IBAN's die bij invoer worden gevalideerd."),
        'GDPR data-subject rights': _t(
            'Droits des personnes concernées (GDPR)', 'GDPR-Betroffenenrechte',
            'Derechos del interesado (GDPR)', "Diritti dell'interessato (GDPR)",
            'GDPR-rechten van betrokkenen'),
        'Subject-access export and selective erasure-with-retention, with DPO contact and retention policies built in.': _t(
            "Export d'accès aux données et effacement sélectif avec rétention, avec contact du DPO et politiques de rétention intégrés.",
            'Auskunftsexport und selektive Löschung mit Aufbewahrung, mit integriertem DPO-Kontakt und Aufbewahrungsrichtlinien.',
            'Exportación de acceso a datos y supresión selectiva con retención, con contacto del DPO y políticas de retención integrados.',
            'Esportazione di accesso ai dati e cancellazione selettiva con conservazione, con contatto del DPO e criteri di conservazione integrati.',
            'Export van inzage-in-gegevens en selectieve wissing-met-bewaring, met ingebouwd DPO-contact en bewaarbeleid.'),
        'Local payroll &amp; core HR': _t(
            'Paie locale &amp; RH de base', 'Lokale Abrechnung &amp; Kern-HR',
            'Nómina local &amp; RR. HH. básicos', 'Busta paga locale &amp; HR di base',
            'Lokale salarisverwerking &amp; kern-HR'),
        'Model French income tax and social contributions as configurable, classified deductions — with employee records, onboarding, time off and self-service, in EUR.': _t(
            "Modélisez l'impôt sur le revenu et les cotisations sociales français comme des retenues configurables et classifiées — avec dossiers salariés, intégration, congés et libre-service, en EUR.",
            'Bilden Sie die französische Einkommensteuer und Sozialabgaben als konfigurierbare, klassifizierte Abzüge ab — mit Personalakten, Onboarding, Abwesenheiten und Self-Service, in EUR.',
            'Modele el impuesto sobre la renta francés y las cotizaciones sociales como deducciones configurables y clasificadas — con expedientes de empleado, incorporación, ausencias y autoservicio, en EUR.',
            "Modella l'imposta sul reddito francese e i contributi previdenziali come trattenute configurabili e classificate — con schede dipendente, onboarding, ferie e self-service, in EUR.",
            'Modelleer de Franse inkomstenbelasting en sociale premies als configureerbare, geclassificeerde inhoudingen — met personeelsdossiers, onboarding, verlof en selfservice, in EUR.'),
        # ---- Price note ----
        'Every module here is part of HR Suite — advanced payroll, year-end and compliance on the Enterprise plan, or added to any plan as a per-seat add-on.': _t(
            "Chaque module ici fait partie de HR Suite — paie avancée, fin d'année et conformité sur le plan Enterprise, ou ajoutés à n'importe quel plan en option par utilisateur.",
            'Jedes Modul hier ist Teil von HR Suite — erweiterte Gehaltsabrechnung, Jahresabschluss und Compliance im Enterprise-Plan oder als Add-on pro Platz zu jedem Plan hinzufügbar.',
            'Cada módulo aquí forma parte de HR Suite — nóminas avanzadas, cierre de año y cumplimiento en el plan Enterprise, o añadidos a cualquier plan como complemento por usuario.',
            "Ogni modulo qui fa parte di HR Suite — buste paga avanzate, chiusura d'anno e conformità nel piano Enterprise, oppure aggiunti a qualsiasi piano come componente per postazione.",
            'Elke module hier maakt deel uit van HR Suite — geavanceerde salarisadministratie, jaarafsluiting en compliance in het Enterprise-plan, of aan elk plan toe te voegen als add-on per gebruiker.'),
        'See HR Suite pricing →': _t(
            'Voir les tarifs de HR Suite →', 'HR Suite Preise ansehen →',
            'Ver precios de HR Suite →', 'Vedi i prezzi di HR Suite →',
            'Bekijk prijzen van HR Suite →'),
        # ---- CTA ----
        'Run France HR &amp; payroll the right way': _t(
            'Gérez la RH &amp; la paie françaises comme il se doit',
            'Französisches HR &amp; Gehaltsabrechnung richtig aufsetzen',
            'Gestione los RR. HH. &amp; las nóminas de Francia como es debido',
            'Gestisci HR &amp; buste paga francesi nel modo giusto',
            'Regel Franse HR &amp; salaris op de juiste manier'),
        'See HR Suite handle French overtime, SEPA and GDPR for your team.': _t(
            'Voyez HR Suite gérer les heures supplémentaires françaises, le SEPA et le GDPR de votre équipe.',
            'Sehen Sie, wie HR Suite französische Überstunden, SEPA und GDPR für Ihr Team erledigt.',
            'Vea cómo HR Suite gestiona las horas extra francesas, SEPA y el GDPR de su equipo.',
            'Guarda HR Suite gestire gli straordinari francesi, il SEPA e il GDPR del tuo team.',
            'Zie hoe HR Suite Frans overwerk, SEPA en het GDPR voor uw team afhandelt.'),
    },
}
