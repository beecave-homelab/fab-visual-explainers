---
type: reference
created: 2026-09-25
source: stdin
tags:
  - clipboard
app: obsidian
author: elvee
---

# Ideeën voor interactieve FAB one-pagers

## Onderzoek, doel en doelgroep

Deze notitie is op **1 oktober 2026** bijgewerkt op basis van een inhoudelijke VVT-review; de blijvende projectafspraken staan in [AGENTS.md](AGENTS.md) en het oorspronkelijke oordeel in de [VVT-review](review-fab-one-pagers-vvt.md). De [functiebeschrijving functioneel applicatiebeheer](functie-beschrijving-functioneel-applicatiebeheer.md) is het toetskader.

De centrale vraag is: **welke concrete beheertaak kan een functioneel applicatiebeheerder in de VVT beter uitvoeren met een interactieve one-pager dan met de huidige checklist, documentatie of registratie?**

De primaire gebruiker is de **functioneel applicatiebeheerder (FAB)**. Kerngebruikers, servicedesk, proceseigenaren, ICT en leveranciers kunnen meelezen of samenwerken, maar hebben andere vragen en bevoegdheden. Een instructie voor een zorgmedewerker vraagt een eenvoudiger route dan een ketenanalyse. Het takenpakket verschilt per organisatie, zorgvorm en toegewezen applicatie; de functiebeschrijving is geen onafhankelijk gevalideerde beroepsstandaard.

Het doel is een kleinere, samenhangende set rond herkenbare beheertaken, actuele bronnen en een bruikbare vervolgstap. Alleen overzicht bieden of een HTML-bestand hebben is onvoldoende. De verwachte waarde is nog niet in de praktijk aangetoond.

De verzameling bestaat uit **FAB-visuals voor processen, ketens, applicaties en beheerbaarheid**, en **bron- en kennisvisuals die omvangrijke documenten toegankelijk maken**. De tweede groep biedt herbruikbare lees- en interactiepatronen voor bijvoorbeeld leveranciersdocumentatie, evaluaties, beleidsstukken en wijzigingsdossiers; de huidige demo's zijn niet specifiek voor FAB ingevuld.

Het uitgangspunt blijft **overzicht → relatie/impact → detail/bewijs**. De visual maakt eerst het geheel begrijpelijk en laat daarna gericht inzoomen. Op 1 oktober 2026 zijn ook de HTML-prototypes bijgewerkt: beheerkaartjes en taakgerichte verwijzingen zijn toegevoegd, concrete voorbeelden verdiepen testdekking, continuïteit en gegevenskwaliteit, en de diagnose-, bewijs- en besluitlogica is herzien. Dit zijn demonstraties zonder actuele dossierkoppeling. Technische tests, lokale inhoudelijke validatie en bewezen gebruikerswaarde blijven aparte statussen.

## Projectafspraken

Toelating, ontwerp, bronbeheer, bewijs, bevoegdheden, beschermde informatie en toegankelijkheid zijn centraal vastgelegd in [AGENTS.md](AGENTS.md). Deze notitie bewaart de conceptinventaris, selectieadviezen, beheerkaartjes en het concrete validatieplan.

## Voorkeursselectie en samenhang

### Zes basisconcepten

> Applicatielandschap · Proces × Applicatie-map · Ketenkaart · Autorisatielandschap · Change Impact Map · Beheerbaarheid Scan

Deze zes verbinden proces, applicatie, gegevens, rechten en verantwoordelijkheden. Ze ondersteunen landschapbegrip, analyse, wijzigingsvoorbereiding en overdracht. **Ze dekken niet vanzelf de volledige FAB-cyclus**: eisen en acceptatietesten, concrete gebruikersinstructies, gegevenskwaliteit en zorgcontinuïteit vragen meer verdieping. De selectie berust op verwachte taakwaarde, niet op bewezen effectiviteit of een vaste set die iedere FAB'er dagelijks moet openen.

### Twee taakgerichte ingangen

- **Incident en continuïteit:** verbind Van melding naar oplossing met Serviceradar-perspectieven, veilige oorzaakopsporing, bekende fouten, escalatie en de goedgekeurde noodwerkwijze. Bij directe zorgimpact kan het afgesproken continuïteitsproces al starten terwijl de analyse nog loopt. De huidige incidentvisuals zijn vooral uitleg- en gesprekshulpen; voor uitvoering moeten ze naar actuele controles en een bruikbare overdracht leiden.
- **Wijziging en acceptatie:** gebruik Releaseatelier als ingang naar lokale release-impact, eisen, impactanalyse, testdekking, Go/No-Go en beheeracceptatie. Maak knelpunt → eis → inrichting → acceptatiecriterium expliciet. Eén wijzigingsdossier krijgt meerdere views, niet meerdere afzonderlijke administraties.

Verbind **JML aan autorisatiebeheer** en **gegevenskwaliteit en gerichte lineage aan de keten**. Eigenaarschap, risico's, leveranciersafspraken en doelgroepimpact worden waar mogelijk gedeelde informatielagen. Benut voor prioritering de bestaande werkvoorraad met zorgimpact; bouw niet automatisch nog een cockpit.

**Go/No-Go** is een view binnen het wijzigingsdossier. **Decision Canvas** blijft een aanvullend overleginstrument voor complexe keuzen: toets eerst harde voorwaarden en weeg daarna toelaatbare opties. Een korte besluitnotitie is bij een eenvoudige vraag vaak genoeg. Bron- en kennispatronen worden alleen ingezet als ze aantoonbaar helpen bij een concrete vraag; Kennisatlas blijft als zelfstandige FAB-tool voorlopig geparkeerd.

### Drie inhoudelijke prioriteiten

1. **Test Coverage Map:** laat zien welke eis en kritieke praktijksituatie wel of niet getest is, met omgeving, versie, resultaat, bevinding en akkoord. De Beheerbaarheid Scan en een groen livegangcriterium vervangen die herleidbaarheid niet.
1. **Continuïteitskaart:** verbind uitval aan getroffen zorgprocessen, een bevoegde noodwerkwijze, contactroute en herstelcontrole. De informatie moet ook zonder de getroffen applicatie beschikbaar zijn.
1. **Data Quality Map:** verbind kwaliteitsregels en vastgestelde afwijkingen aan gevolgen voor zorg, planning en verantwoording, met eigenaar en herstelroute.

Deze drie zijn eerst als synthetische verdieping van bestaande HTML uitgewerkt: testdekking van zorgoverdracht naar een woonzorglocatie in Releaseatelier, ECD-uitval op een woonzorglocatie in beide incidentvarianten, en kwaliteitsregels voor overdrachtsberichten in Ketenkaart. Op 1 oktober 2026 zijn daarnaast drie zelfstandige prototypes toegevoegd: [Test Coverage Map](fab-test-coverage-map.html), [Continuïteitskaart](fab-continuiteitskaart.html) en [Data Quality Map](fab-data-quality-map.html). Ze gebruiken dezelfde casusreferenties, maar hebben eigen demodata en synchroniseren niet. De precieze overlap in de kwaliteitslens is bewust verzonnen; de Ketenkaart stelt die overlap niet vast. Deze zelfstandige uitwerking volgt de ontwerpvraag, niet een aangetoonde behoefte aan meer losse tools. Laat inhoud en praktische meerwaarde toetsen tegenover het bestaande testplan, noodplan en kwaliteitsregister.

### Gedeelde casus is nog geen gedeelde bron

Change Impact Map, Go/No-Go en Decision Canvas gebruiken dezelfde fictieve wijziging (*Teamindeling per wijk*, RFC-2026-118, beoogde livegang 2 november 2026). De teamcodes sluiten aan op de Ketenkaart. Dit maakt de samenhang begrijpelijk, maar de gegevens zijn afzonderlijk vastgelegd: een opgeloste blocker wordt niet automatisch in alle views bijgewerkt. Voor werkelijk gebruik moeten wijziging, bevinding, eigenaar en bewijs naar dezelfde bronregistratie verwijzen.

De wijkteamcasus bewijst geen brede VVT-dekking. Er zijn aanvullende synthetische casussen voor zorgoverdracht en uitval op een woonzorglocatie toegevoegd; ook die zijn nog niet lokaal gevalideerd. Laat proceseigenaren en zorginhoudelijke deskundigen de inhoud toetsen vóór praktisch gebruik. Demo-afspraken over indicatie, medicatieprofielen, prestaties en teamcodes zijn geen algemene VVT-werkinstructies.

## Beheerkaartjes: taak vóór visualvorm

Voor **ieder concept hieronder is FAB de primaire gebruiker**. De genoemde inhoudelijk eigenaar is een voorgestelde rol om lokaal af te spreken, geen al toegewezen persoon en niet automatisch de beslisser. De bronnen zijn beoogde bronnen voor hergebruik; de huidige HTML-demo's vormen geen actuele dossierkoppeling. Voor zelfstandige eindgebruikersinstructies moet de doelgroep apart worden vastgesteld.

### Bestaande FAB-concepten

| Concept                           | Hoofdvraag en gebruiksmoment                                                                                   | Beoogde bron                                                                  | Inhoudelijk eigenaar                                           | Gewenste uitkomst en plaats in de set                                                                                                                                             |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Van melding naar oplossing        | Welke stap en overdracht volgt bij deze verstoring? Bij triage, afhandeling of opleiding.                      | Melding, afhandelafspraken en herstelbewijs.                                  | Coördinator incidentafhandeling met FAB.                       | Volgende actie en overdracht; incidentingang. De twee varianten tellen als één concept.                                                                                           |
| Releaseatelier                    | Wat moeten we uitzoeken, testen en overdragen? Bij intake en voortgang van een wijziging.                      | Wijzigingsdossier, eisen, tests en overdracht.                                | Wijzigingscoördinator met FAB.                                 | Compleet dossier met acties; wijzigingsingang, geen los actueel dossier in de huidige demo.                                                                                       |
| Serviceradar                      | Welk perspectief ontbreekt in onze analyse? Bij een verstoring over meerdere partijen.                         | Melding, procesafspraken, ketencontroles en leveranciersinformatie.           | Coördinator incidentafhandeling.                               | Gerichte volgende controle; samenvoegen met incidentanalyse.                                                                                                                      |
| Applicatielandschap               | Welke processen en systemen raakt wijziging of uitval? Bij impactanalyse en overdracht.                        | Applicatieregister, procesrelaties en koppeldocumentatie.                     | Verantwoordelijke applicatieregister met proceseigenaren.      | Betrokken systemen en eigenaren bepalen; basisconcept, geen live storingsmonitor.                                                                                                 |
| Beheerbaarheid Scan               | Kan regulier beheer de oplevering dragen? Bij inbeheername en overdracht.                                      | Beheerafspraken, configuratie, controles en beoordeeld bewijs.                | Verantwoordelijke beheeracceptatie.                            | Tekorten, eigenaar en overdrachtsadvies; basisconcept. Vergelijk de ring met een controlelijst.                                                                                   |
| Ketenkaart                        | Waar bleef een cliëntmutatie steken? Bij ontbrekende of verkeerde eindverwerking.                              | Berichtreferenties, mappings, controle-uitkomsten en herstelafspraken.        | Functioneel keteneigenaar met integratiebeheer.                | Juiste controle, eigenaar en veilige herstelroute; basisconcept. Controleer inhoud en eindverwerking, voorkom dubbele verwerking.                                                 |
| Change Impact Map                 | Welke gevolgen en maatregelen missen we? Bij wijzigingsanalyse.                                                | Wijzigingsdossier, proces-, rechten-, keten- en risicoinformatie.             | Verantwoordelijke impactanalyse met betrokken eigenaren.       | Herleidbare impactpunten en acties; basisconcept. Scheid verwachte van bewezen risicoreductie.                                                                                    |
| Proces × Applicatie-map           | Waar ontstaat dubbel werk of een gebrekkige overdracht? Bij gebruikersvragen en procesverbetering.             | Lokaal gevalideerd proces, registraties en inrichting.                        | Proceseigenaar met FAB en kerngebruikers.                      | Knelpunt, functionele eis en meetbaar gewenst verschil; basisconcept.                                                                                                             |
| Autorisatielandschap              | Welke toegang hoort bij de rol en welke uitzondering vraagt beoordeling? Bij hercertificering of rolwijziging. | Goedgekeurd rechtenmodel, feitelijke toekenningen en uitzonderingsregister.   | Autorisatieverantwoordelijke met proces- en gegevenseigenaren. | Verschillen en beoordeelde uitzonderingen; basisconcept. Neem team-/cliëntscope en noodtoegang mee.                                                                               |
| Go/No-Go Cockpit                  | Welke voorwaarden maken livegang nog onverantwoord? Bij het livegangbesluit.                                   | Eén wijzigingsdossier met actuele criteria, bevindingen en beoordeeld bewijs. | Verantwoordelijke livegangvoorbereiding; bevoegde rol beslist. | Controleerbaar advies; het formele besluit blijft in de bronregistratie. Advieslogica in het prototype herzien; lokaal vastgestelde regels en bevoegde goedkeuring blijven nodig. |
| Decision Canvas                   | Welke toelaatbare invoeringsroute heeft de voorkeur? Bij een complexe keuze.                                   | Opties, aannames, harde voorwaarden en onderbouwde afwegingen.                | Dossiereigenaar; bevoegde rol beslist.                         | Besluitnotitie met voorwaarden; aanvullende overlegview, geen dagelijks basisconcept.                                                                                             |
| Joiner-Mover-Leaver-flow          | Welke toegang komt te laat of blijft te lang actief? Bij indiensttreding, teamwissel en vertrek.               | HR-trigger, IAM-status, feitelijke applicatietoegang en lokale termijnen.     | Verantwoordelijke JML-proces met HR, IAM en FAB.               | Vastgestelde afwijking en herstelactie; verbinden met autorisatiebeheer. De demo toont tijdvakken, geen volledige IAM-controle.                                                   |
| Rapportage Lineage                | Welk bronveld of welke berekening verklaart de afwijking? Bij een rapportagevraag binnen de FAB-scope.         | Vastgestelde KPI-definitie, berekening, bronvelden en verversingsinformatie.  | Rapportage-eigenaar met BI; FAB beoordeelt bronregistraties.   | Herleidbare verklaring en correctieopdracht; demodefinities herzien, nog door rapportage-eigenaar en BI lokaal te toetsen.                                                        |
| Root Cause Map / Oorzaakopsporing | Welke hypothese toetsen we nu en wat is bewezen? Tijdens incidentanalyse.                                      | Hypothesen, controles, bewijs en controledatum uit het incidentdossier.       | Verantwoordelijke incidentanalyse met betrokken deskundigen.   | Onderbouwde volgende check; automatische uitsluiting verwijderd en met bewijsbeoordeling verbonden aan de incidentingang. Lokale validatie blijft nodig.                          |

### Bestaande bron- en kennispatronen

| Concept      | Hoofdvraag en gebruiksmoment                                                                     | Beoogde bron                                           | Inhoudelijk eigenaar                                  | Gewenste uitkomst en plaats in de set                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Bronkaart    | Welke bronpassages hebben gevolgen voor beheer? Bij het beoordelen van omvangrijke documentatie. | Actuele leveranciers- of beleidsbron met vindplaatsen. | Eigenaar van het betreffende beheerdossier.           | Lokale gevolgen en acties; gericht bronpatroon, geen zelfstandige dagelijkse beheertool.                             |
| BronScanner  | Waar staat de onderbouwing? Bij gericht brononderzoek.                                           | Versiebeheerde bron en controleerbare verwijzingen.    | Bron- of dossiereigenaar.                             | Terugvindbaar bewijs; vergelijk met een inhoudsopgave. Licht informatiedichtheid en betrouwbaarheidspercentages toe. |
| Kennisatlas  | Hoe hangen verklaringen en voorwaarden samen? Bij een terugkerende leer- of beheervraag.         | Gevalideerde kennisitems en hun onderbouwde relaties.  | Kennisverantwoordelijke met inhoudelijke deskundigen. | Begrip van relevante samenhang; voorlopig parkeren als zelfstandige FAB-tool.                                        |
| Vraagdossier | Wat moet ik weten of onderbouwen bij één vraag? Bij advies of kennisoverdracht.                  | Kennisbank of beheerdossier met bronverwijzingen.      | Eigenaar kennisitem of dossier.                       | Onderbouwd antwoord; gericht inzetten en op hetzelfde dossier vergelijken met VraagKompas.                           |
| VraagKompas  | Welke instructie of bron past bij deze vraag? Bij ondersteuning en overdracht.                   | Actuele kennisbank en goedgekeurde instructies.        | Kennisitemeigenaar met FAB en kerngebruikers.         | Juiste instructie met voorwaarden; navigatie vult de kennisbank aan, maar vervangt die niet.                         |

### Aanvullende concepten en open kandidaten

| Concept                      | Hoofdvraag en gebruiksmoment                                                                         | Beoogde bron                                                                                                           | Inhoudelijk eigenaar                                         | Gewenste uitkomst en plaats in de set                                                                                                                                   |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Lineage                 | Waar is dit kritieke gegeven veranderd? Bij een ketenafwijking.                                      | Bronveld, transformaties en afnemers.                                                                                  | Gegevenseigenaar met ketenbeheer.                            | Controle op één gegeven; verdieping van Ketenkaart, geen brede kaart zonder concrete vraag.                                                                             |
| Data Quality Map             | Welke verkeerde, ontbrekende of late registratie raakt zorg of verantwoording? Bij gegevenscontrole. | Kwaliteitsregel, gecontroleerde populatie, peildatum en afwijkingen.                                                   | Gegevenseigenaar met FAB en betrokken proceseigenaar.        | Afwijking en herstelroute; hoge prioriteit. Geen onverklaard totaalpercentage datakwaliteit.                                                                            |
| Functional Blueprint         | Welke extra informatielaag beantwoordt een nog open vraag? Bij proces- of impactanalyse.             | Gedeelde proces-, applicatie- en ketenbronnen.                                                                         | Proces- en applicatie-eigenaren.                             | Alleen ontbrekende samenhang toevoegen; samenvoegen met bestaande basisconcepten.                                                                                       |
| Test Coverage Map            | Welke eis of kritieke praktijksituatie is nog niet getest? Bij acceptatievoorbereiding.              | Knelpunt, eis, inrichting, acceptatiecriterium, rol, scenario, test, omgeving, versie, uitkomst, bevinding en akkoord. | Test-/acceptatieverantwoordelijke met FAB en kerngebruikers. | Herleidbaar testplan en zichtbare gaten; hoge prioriteit. Neem negatieve autorisatie- en foutscenario's mee.                                                            |
| Omgevingsvergelijker         | Geldt dit testresultaat ook voor productie? Bij afwijking of acceptatie.                             | Configuratie, versies, koppelingen en testrollen per beschikbare omgeving.                                             | FAB met technisch beheer en leverancier.                     | Verschillen en aanvullende tests; verdieping van testen. Veronderstel geen aparte testomgeving bij elk extern portaal.                                                  |
| Release Impact Explorer      | Wat betekent dit releasepunt lokaal? Bij leveranciers- of sectorwijzigingen.                         | Release-/beleidsbron, lokale inrichting en procesafspraken.                                                            | FAB met proces- of beleidseigenaar.                          | Bron → lokaal gevolg → doelgroep → test/actie → eigenaar; samenvoegen met wijzigingsingang en impactanalyse.                                                            |
| Applicatie Life Cycle Map    | Welke upgrade of beëindiging vraagt tijdig actie? Bij beheerplanning.                                | Ondersteuningstermijnen, versies en migratieafspraken.                                                                 | Applicatie-eigenaar met ICT en leverancier.                  | Planning en verantwoordelijke; gericht inzetten bij actuele aanleiding.                                                                                                 |
| Known Error / Workaround Map | Welke bekende fout en veilige tijdelijke werkwijze passen hier? Bij terugkerende meldingen.          | Kennisitem, diagnose, toepassingsvoorwaarden, risico en herbeoordeling.                                                | Kennisitemeigenaar met FAB en proceseigenaar.                | Goedgekeurde instructie of escalatie; opnemen in incident- en kennisvoorziening.                                                                                        |
| Escalatiekaart               | Wie moet nu handelen en met welke informatie? Bij incident of ketenprobleem.                         | Actuele contactroute, bevoegdheden en overdrachtsafspraken.                                                            | Coördinator incident-/continuïteitsproces.                   | Escalatiepakket en geaccepteerde overdracht; opnemen in incident en continuïteit.                                                                                       |
| Continuïteitskaart           | Hoe gaat de zorg veilig verder en hoe bevestigen we herstel? Bij uitval en oefening.                 | Goedgekeurd noodplan, afhankelijkheden en herstelcontroles.                                                            | Proceseigenaar met bevoegde zorginhoudelijke deskundigen.    | Bereikbare noodwerkwijze en herstelcontrole; hoge prioriteit, ook buiten de getroffen applicatie beschikbaar.                                                           |
| Leverancierskaart            | Welke partij en afspraak gelden voor dit probleem? Bij melding of leveranciersoverleg.               | Bestaande leveranciers-/contractregistratie en meldvereisten.                                                          | Leveranciers- of contractverantwoordelijke.                  | Juiste contactroute en meldinformatie; detail van applicatie, keten of incident, geen tweede adressenboek.                                                              |
| Risk & Control Map           | Welk risico resteert na uitvoering en toetsing? Bij impactanalyse en overdracht.                     | Risico, maatregel, uitvoeringsbewijs, toets en acceptatie.                                                             | Risico-eigenaar; bevoegde rol accepteert restrisico.         | Zichtbaar restrisico en besluit; opnemen in impact en beheerbaarheid.                                                                                                   |
| Eigenaarschapkaart           | Wie voert uit, toetst en beslist? Bij overdracht en ketenproblemen.                                  | Vastgestelde verantwoordelijkheden voor proces, data, applicatie en techniek.                                          | Betrokken proces-, gegevens- en applicatie-eigenaren.        | Ondubbelzinnige overdracht; gedeelde informatielaag, niet alleen een losse kaart.                                                                                       |
| Stakeholder Impact Map       | Wat verandert per doelgroep? Bij wijziging en communicatie.                                          | Impactanalyse en lokale rollen/werkafspraken.                                                                          | Wijzigingscoördinator met proceseigenaar.                    | Gerichte communicatie en instructie; onderdeel van Change Impact. Neem relevante zorgmedewerkers, planners, cliëntadministratie, cliënten/naasten en ketenpartners mee. |
| Adoptiekaart                 | Wordt de nieuwe werkwijze goed en veilig gebruikt? Bij grotere invoeringen en nazorg.                | Vooraf gekozen praktijksignalen, gebruiks- en kwaliteitsmetingen.                                                      | Proceseigenaar met opleidings-/adoptieverantwoordelijke.     | Ondersteuningsactie en borging; gerichte verdieping. Trainingdeelname bewijst geen vaardigheid.                                                                         |
| Pilot Cockpit                | Vermindert de beperkte invoering het probleem echt? Bij onzekere werking of gebruik.                 | Hypothese, scope, nulmeting, uitkomst, bijwerkingen en stopcriteria.                                                   | Pilot-/proceseigenaar.                                       | Onderbouwd doorgaan, aanpassen of stoppen; gericht inzetten, niet voor iedere kleine wijziging.                                                                         |

## Bronbeschikbaarheid en voortgang

In deze map staan **23 HTML-bestanden voor 22 concepten: 17 FAB-concepten en 5 bron- en kennisconcepten**. De incidentvisual heeft twee varianten. Daarnaast zijn er **13 open kandidaten**.

Elke visual heeft één checkbox in de inventarisatie:

- **Aangevinkt** betekent dat een HTML-uitwerking in deze map aanwezig is.
- **Niet aangevinkt** betekent dat de HTML-uitwerking nog openstaat.

Een vinkje zegt niet dat de visual klaar is voor productie of met gebruikers is gevalideerd. Werking, toegankelijkheid en printweergave moeten bij doorontwikkeling nog worden getoetst. Het bijhouden van checkboxes en inventaris volgt [AGENTS.md](AGENTS.md#wijzigingen). De beschrijvingen hieronder geven de bestaande inhoud en interacties weer; aanbevelingen zijn geen al doorgevoerde verbeteringen.

## Uitgewerkte HTML-visuals

### FAB-processen, ketens en beheer

- [x] **Van melding naar oplossing** — Incidentafhandeling in vijf klikbare stappen: melding, triage, analyse, herstel en leren. Per stap verschijnen vragen, overdrachtsinformatie en voorwaarden om verder te gaan. De gebruiker kan wisselen tussen context- en focusmodus.
  - Bestanden: [algemene variant](incident-onepager.html) en [Attent-variant](incident-onepager-attent.html).
- [x] **Releaseatelier** — Een wijzigingsdossier met vijf fasen: intake, impact, testen, communicatie en nazorg. Een klik op een fase toont de bijbehorende vragen, werkstukken, beslisregels en voorwaarden voor de volgende stap. De voorbeeldcasus gaat over nieuwe teamrollen in een roosterportaal.
  - Bestand: [fab-releaseatelier.html](fab-releaseatelier.html).
- [x] **Serviceradar** — Een dienst in verstoring staat centraal, met zes klikbare perspectieven: melder, proces, applicatie, data, koppeling en leverancier. Per perspectief verschijnen diagnosevragen en het volgende beslismoment. Dit is een operationeel ketenbeeld voor incidentregie, geen technische integratiekaart.
  - Bestand: [fab-serviceradar.html](fab-serviceradar.html).
- [x] **Applicatielandschap** — Een netwerkkaart met negen systemen en hun gegevensstromen in een fictieve zorgorganisatie. De gebruiker kan zoeken op naam of functie, vier soorten gegevensstromen aan- of uitzetten en directe of ketenbrede afhankelijkheden uitlichten. Het detailpaneel toont functies, gebruikers, eigenaarschap, kritikaliteit, processen en FAB-controlepunten.
  - Bestand: [fab-applicatielandschap.html](fab-applicatielandschap.html).
- [x] **Beheerbaarheid Scan** — Een klikbare beheerring rond configureren, testen, monitoren, ondersteunen en borgen. De vijf domeinen bevatten vijftien controles met verwachte bronreferenties en de status geaccepteerd, niet getoetst, aandacht of blocker. Acceptatie vraagt volledige beoordelingsgegevens; bronlabels tellen niet als bewijs. De gebruiker kan beoordelingen simuleren, de volledige checklist lezen en een samenvatting kopiëren. De voorbeeldcasus is een cliëntportaalrelease.
  - Bestand: [fab-beheerbaarheid-scan.html](fab-beheerbaarheid-scan.html).
- [x] **Ketenkaart / Integration Map** — Een lichtblauw schakelbord volgt een fictieve cliëntmutatie vanuit het ECD via ontvangst en controle naar financiën, het datawarehouse en BI. Een klik op een systeem of overdracht licht de bijbehorende routes uit en toont gegevens, eigenaar, beheer- en herstelafspraken en fictieve bewijsfragmenten. De gebruiker kan een afnemer kiezen, wisselen tussen de normale stroom en een onbekende teamcode, en een ketensamenvatting kopiëren. Op mobiel staat de keten verticaal.
  - Bestand: [fab-ketenkaart.html](fab-ketenkaart.html). Op 1 oktober 2026 opnieuw uitgewerkt op basis van de eerder beschreven casus; dit is een nieuwe implementatie, niet het teruggevonden oorspronkelijke bestand.
- [x] **Change Impact Map** — Een rimpelrooster voor de fictieve wijziging *Teamindeling per wijk* (ECD 2026.4, RFC-2026-118). Zes beheergebieden (proces, gebruiker, data, koppeling, rapportage, beheer) staan tegenover drie ordes van effect (direct, afgeleid, randvoorwaarde). Zestien impactpunten met ernst zijn via lijnen van oorzaak naar gevolg verbonden. Een selectie licht de hele keten van oorzaken en gevolgen uit. De gebruiker kan wisselen tussen de situatie zonder en met maatregelen, filteren op ernst en een impactsamenvatting kopiëren.
  - Bestand: [fab-change-impact-map.html](fab-change-impact-map.html).
- [x] **Proces × Applicatie-map** — Een matrix van zes processtappen (van aanmelding tot eerste zorgmoment) en vijf applicaties. Per cel staat welke registratie in die stap ontstaat. Pijlen tonen elf overdrachten, waarvan drie handmatig. De gebruiker kan een stap, applicatie, registratie of overdracht kiezen, filteren op rol en alleen de handmatige overdrachten tonen. Het detailpaneel toont velden, rollen, risico's bij de overdracht en FAB-controlepunten. Op mobiel staan de overdrachten onder de stappen.
  - Bestand: [fab-proces-applicatie-map.html](fab-proces-applicatie-map.html).
- [x] **Autorisatielandschap** — Een matrix van acht rollen en zes applicaties met vier toegangsniveaus, gevoeligheidsklassen per applicatie (medisch, BSN, financieel) en lopende uitzonderingen: tijdelijke rechten, break-the-glass, een conflict in functiescheiding en een verlopen hercertificering. De gebruiker kan een rol, applicatie of recht kiezen, alleen de uitzonderingen tonen, filteren op gevoeligheid en een hercertificeringslijst kopiëren. De voorbeeldcasus is de kwartaalhercertificering van Q4 2026.
  - Bestand: [fab-autorisatielandschap.html](fab-autorisatielandschap.html).
- [x] **Go/No-Go Cockpit** — Een besluitstrip met het berekende advies (go, go onder voorwaarden of no-go) en een tijdlijn met beslismomenten tot en met de nazorg. Daaronder staan achttien criteria in zes groepen en de open bevindingen P1–P4, vergeleken met een zichtbare drempel. De gebruiker kan de status van een criterium wijzigen; het advies wordt dan direct opnieuw berekend. Een besluitadvies is te kopiëren. De voorbeeldcasus is de livegang van *Teamindeling per wijk*.
  - Bestand: [fab-go-no-go-cockpit.html](fab-go-no-go-cockpit.html).
- [x] **Decision Canvas** — De besluitvraag *Hoe voeren we de teamindeling per wijk in?* met drie opties (in één keer, gefaseerd per regio of uitstel) en vijf invalshoeken: feiten, risico's, afhankelijkheden, inspanning en gevolgen voor gebruikers. Aannames zijn gemarkeerd. Met vier schuifregelaars stelt de gebruiker de weging in; de scores en de volgorde worden direct opnieuw berekend. Het canvas meldt nadrukkelijk dat het een hulpmiddel is en geen besluit. Een besluitnotitie is te kopiëren.
  - Bestand: [fab-decision-canvas.html](fab-decision-canvas.html).

### Bronnen, kennis en vraaggestuurd lezen

- [x] **Bronkaart** — Een grote bron teruggebracht tot vijf hoofdthema's, een themakaart en een detailpaneel. Zoeken en selecteren verbinden de kern met context, bewijs, effecten en onzekerheden. Bronfragmenten verschijnen op verzoek; de voorbeeldbron is een fictieve evaluatie van digitale dienstverlening.
  - Bestand: [bronkaart-onepager.html](bronkaart-onepager.html).
- [x] **BronScanner** — Een bron als verticale strook met acht secties. De strook toont de relatieve informatiedichtheid; een selectie opent de samenvatting, kernpunten, een citaat, onderbouwing, impact en aandachtspunten. Een apart bewijsspoor blijft naast de inhoud zichtbaar. Zoeken en vorige/volgende helpen bij het verkennen.
  - Bestand: [bron-scanner.html](bron-scanner.html).
- [x] **Kennisatlas** — Een netwerk van acht inzichten met verbanden tussen oorzaken, effecten, randvoorwaarden, bewijs en onzekerheden. Leesroutes en filters leggen de nadruk op een gekozen invalshoek. Een klik op een knooppunt toont de samenvatting, relevantie, onderbouwing en bronverwijzing zonder de kaart te verlaten.
  - Bestand: [kennisatlas.html](kennisatlas.html).
- [x] **Vraagdossier** — Een document geordend rond vijf beslisvragen: kernconclusie, verklaring, betekenis, voorwaarden en grenzen. De gebruiker kiest een antwoord in 30 seconden, meer context in 2 minuten of de bronlaag. Losse bewijsstroken openen een toelichting; het bronpad blijft zichtbaar.
  - Bestand: [vraagdossier.html](vraagdossier.html).
- [x] **VraagKompas** — Zes vraaggestuurde leesroutes rond aanleiding, verandering, bewijs, risico's, acties en betrokkenen. Per vraag zijn een kort antwoord, onderbouwing en brontekst beschikbaar, met bronverwijzingen en logische vervolgvragen. Een zoekvraag helpt om de passende ingang te vinden.
  - Bestand: [vraagkompas.html](vraagkompas.html).

## Aanvullende templatekandidaten

Deze thematische lijst bevat **13 open kandidaten** en zes inmiddels uitgewerkte concepten: **Joiner-Mover-Leaver-flow**, **Rapportage Lineage**, **Root Cause Map**, **Data Quality Map**, **Test Coverage Map** en **Continuïteitskaart**. Die zes blijven hier voor de samenhang staan; hun vinkje betekent uitsluitend dat het HTML-bestand aanwezig is. De beheerkaartjes hierboven geven per concept het advies voor doorontwikkeling.

Inhoudelijke overlap betekent niet dat een kandidaat al is uitgewerkt. Een open kandidaat kan een uitbreiding, informatielaag of andere invalshoek worden in plaats van een aparte one-pager. De zes basisconcepten, Go/No-Go Cockpit en Decision Canvas staan in de eerdere inventarisatie. Ieder concept houdt één checkbox.

### Landschap, processen, toegang en gegevens

- [ ] **Data Lineage** — Waar gegevens ontstaan, wijzigen, worden doorgestuurd en uiteindelijk gebruikt.
- [x] **Joiner-Mover-Leaver-flow** — Medewerker van HR-trigger via IAM naar het toekennen, wijzigen en intrekken van accounts en rechten. Uitgewerkt als dagenraster met schuifregelaar en vergelijking tussen bedoeld en werkelijk verloop. Bestand: [fab-joiner-mover-leaver.html](fab-joiner-mover-leaver.html).
- [x] **Data Quality Map** — Een controlelens over 120 synthetische overdrachtsberichten, met drie kwaliteitsregels, expliciete demo-overlap, betrokken afnemers en veilige herstelroutes. Voorstel, uitvoering en aansluitcontrole zijn afzonderlijk te simuleren; een gewijzigde regelversie vraagt herbeoordeling. Geen totaalpercentage datakwaliteit. Bestand: [fab-data-quality-map.html](fab-data-quality-map.html).
- [x] **Rapportage Lineage** — KPI/dashboard → berekening → gegevensveld → bronsysteem. Uitgewerkt als doorsnede in vier lagen, met simulatie van achterlopende bronnen. Bestand: [fab-rapportage-lineage.html](fab-rapportage-lineage.html).
- [ ] **Functional Blueprint** — Proces, gebruiker, applicatie, data en koppeling als aan- en uitzetbare informatielagen.

### Wijzigingen, testen en livegang

- [x] **Test Coverage Map** — Vijf herleidbare testsporen voor zorgoverdracht naar een woonzorglocatie: eis/inrichting, scenario, uitvoering, bewijscontrole en bevoegd akkoord. Uitvoering, mislukking, controle, akkoord en afkeuring zijn apart te simuleren; gewijzigde bewijsversies maken eerdere acceptatie ongeldig. Terugvaltest blijft geblokkeerd zonder lokaal noodplan. Bestand: [fab-test-coverage-map.html](fab-test-coverage-map.html).
- [ ] **Omgevingsvergelijker** — Verschillen tussen productie-, test- en acceptatieomgevingen.
- [ ] **Release Impact Explorer** — Release notes vertaald naar impact voor processen, gebruikers en beheer.
- [ ] **Applicatie Life Cycle Map** — Versies, upgrades, EOL, projecten, migraties en vervanging.

### Incidenten, ondersteuning en continuïteit

- [x] **Root Cause Map** — Symptomen, hypothesen, checks en afzonderlijke bewijsbeoordeling. Antwoorden geven aanwijzingen, geen automatische uitsluitingen of bewezen oorzaak. Het raster ondersteunt een volgende check en houdt onbekend en meerdere oorzaken mogelijk. Bestand: [fab-oorzaakopsporing.html](fab-oorzaakopsporing.html).
- [ ] **Known Error / Workaround Map** — Bekende verstoringen, diagnose, workaround en structurele oplossing.
- [ ] **Escalatiekaart** — Wie wanneer verantwoordelijk wordt bij incidenten en ketenproblemen.
- [x] **Continuïteitskaart** — Een uitklapbare oefenkaart met parallelle banen voor zorgregie en technisch herstel. Wisselen tussen ECD-, netwerk- en IAM-uitval toont andere bereikbaarheidseisen; planstatus, vier herstelcontroles en afzonderlijke bevoegde bevestiging zijn te simuleren. Bevat geen echt noodplan of contactroute; gereedheid blijft niet aangetoond. Bestand: [fab-continuiteitskaart.html](fab-continuiteitskaart.html).

### Eigenaarschap, risico's en besluitvorming

- [ ] **Leverancierskaart** — Leveranciers, applicaties, support, SLA's en afhankelijkheden.
- [ ] **Risk & Control Map** — Risico's gekoppeld aan maatregelen, bewijs, eigenaar en restrisico.
- [ ] **Eigenaarschapkaart** — Verantwoordelijkheden voor processen, applicaties, data, techniek en leveranciers.
- [ ] **Stakeholder Impact Map** — Wat een wijziging betekent voor iedere betrokken doelgroep.
- [ ] **Adoptiekaart** — Bekend → getraind → gebruikt → beheerst → geborgd.
- [ ] **Pilot Cockpit** — Hypothese, scope, nulmeting, voortgang, bevindingen en besluitcriteria.

## Uitwerking voor hergebruik

### Ontwerpvoorstel

Het ontwerp- en interactiepatroon staat in [AGENTS.md](AGENTS.md#toelating-en-selectie).

De bestaande uitwerkingen bieden concrete patronen: een klikbare proceslijn in de incidentvisual en Releaseatelier, radiale perspectieven in Serviceradar, een filterbare netwerkkaart in Applicatielandschap, een beheerring met controles in de Beheerbaarheid Scan, een rimpelrooster met oorzaak-gevolglijnen in de Change Impact Map, matrices in de Proces × Applicatie-map en het Autorisatielandschap, een live herberekend advies in Go/No-Go en instelbare weging in Decision Canvas. Bronkaart en Kennisatlas verbinden overzicht met verdieping; BronScanner houdt de bronstructuur zichtbaar. Vraagdossier en VraagKompas bieden vraaggestuurde navigatie met leesdieptes en bronverwijzingen.

Filters of informatielagen per rol, status of omgeving kunnen dit ondersteunen. Het Applicatielandschap heeft al filters voor soorten gegevensstromen; niet alle genoemde filtervormen zijn aanwezig. De selectievoorwaarden staan in [AGENTS.md](AGENTS.md#toelating-en-selectie).

### Verwachte bijdrage en grenzen

- **Applicatielandschap** maakt functies en afhankelijkheden bespreekbaar, maar vervangt geen gerichte lineage of feitelijke toegangscontrole.
- **Proces × Applicatie-map** verbindt stappen met systemen, rollen en overdrachten en helpt dubbel registreren onderzoeken.
- **Ketenkaart** volgt gegevens en verantwoordelijkheden door een koppeling heen. Ontvangst, inhoudelijke verwerking en rapportageverversing blijven afzonderlijke controles.
- **Autorisatielandschap** maakt bedoelde toegang en uitzonderingen inzichtelijk; JML verdiept de overgangsmomenten.
- **Change Impact Map** helpt gevolgen over beheergebieden overzien; maatregelen en bewijs moeten onderscheiden blijven.
- **Beheerbaarheid Scan** richt de aandacht op configuratie, testen, monitoring en ondersteuning na oplevering, maar is geen volledige Test Coverage Map.
- **Go/No-Go** bundelt criteria, bewijs en blockers; de demologica gebruikt nu dezelfde criteria en veranderende bevindingen voor advies en samenvatting. Dit is geen actuele dossierkoppeling of formeel besluit.
- **Decision Canvas** ordent opties en afwegingen bij complexe keuzen; de bevoegde rol blijft beslissen.

Welke vorm het meest oplevert hangt af van de concrete beheer- of besluitvraag. Geen kandidaat is een toezegging dat het onderwerp een eigen one-pager nodig heeft.

## Status en afbakening

Deze notitie is een **ideeënkader en prototypebibliotheek**, geen productierijpe FAB-gereedschapskist. Er zijn **22 concepten met HTML: 17 FAB-concepten en 5 bron- en kennisconcepten**, samen **23 bestanden** door de twee incidentvarianten. Er blijven **13 open kandidaten**. De vier statussoorten uit [AGENTS.md](AGENTS.md#status-en-meerwaarde) zijn hier als volgt vastgelegd:

| Status                     | Wat hier is vastgelegd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Wat dat niet bewijst                                                                                                                                                                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aanwezig                   | De aangevinkte inventarisatie verwijst naar een HTML-bestand.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Productierijpheid, juistheid of gebruikerswaarde.                                                                                                                                                                                             |
| Technisch getest           | Bij verwerking op 1 oktober 2026 zijn gerichte Playwright/Chrome-controles uitgevoerd op de oorspronkelijke HTML-prototypes, met regressietests voor diagnose-, bewijs-, autorisatie- en besluitlogica. De verificatieafspraken en grenzen staan in `AGENTS.md`. De drie later toegevoegde zelfstandige prototypes zijn apart gecontroleerd op bewijsfasen, afkeuring, bronwijzigingen, filterfocus, overlap, herstelvoorwaarden, export, lokale links, unieke ID’s, mobiel, toetsenbord, afdrukweergave en leesbaarheid zonder JavaScript. | Een volledige toegankelijkheidsaudit, lokale procesvalidatie of bewezen gebruikerswaarde. De eerdere claim “één A4” geldt niet automatisch voor de nu uitgebreidere pagina’s; de nieuwe aanvullingen mogen meerdere afdrukpagina’s gebruiken. |
| Inhoudelijk beoordeeld     | De VVT-review van 1 oktober 2026 ([reviewrapport](review-fab-one-pagers-vvt.md)) toetste de concepten aan de functiebeschrijving en noemde beperkingen in de uitwerkingen. De eerdere notitie vermeldt inhoudelijk akkoord op het Ketenkaart-concept van 26 september 2026.                                                                                                                                                                                                                                                                 | Lokale procesvalidatie, certificering of akkoord op de nieuwe Ketenkaart van 1 oktober 2026. Het oorspronkelijke bestand ontbrak; het eerdere akkoord gaat niet automatisch over.                                                             |
| Met gebruikers gevalideerd | Gebruikersvalidatie is niet vastgelegd.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Betere beslissingen, minder fouten, tijdwinst of aanvaardbare onderhoudslast.                                                                                                                                                                 |

De functiebeschrijving is het aangeleverde toetskader. Productinformatie, wet- en regelgeving, lokale zorgprotocollen en leveranciersfunctionaliteit zijn niet extern gevalideerd.

## Verwerkte HTML-herzieningen en grenzen vóór praktisch gebruik

De technische en inhoudelijke prototype-aanpassingen uit de review zijn verwerkt. De actuele status staat in de statussectie hierboven; de kwaliteitseisen en verificatieafspraken staan in `AGENTS.md`.

- **Oorzaakopsporing:** antwoorden zijn aanwijzingen, zonder automatische uitsluiting. Onbekend, gedateerd bewijs, herbeoordeling en meerdere mogelijke oorzaken zijn expliciet. Geen diagnose of herstelbevoegdheid via een knop.
- **Go/No-Go:** criteria, veranderende bevindingen, drempels, advies en samenvatting gebruiken één demomodel. Acceptatie vraagt bewijsmetadata; harde zorg-/privacyvoorwaarden en bevoegde risicoacceptatie zijn zichtbaar.
- **Decision Canvas:** harde voorwaarden gaan vóór de weging; alleen toelaatbare opties worden gerangschikt. Scores zijn toegelicht en de onbewezen BI-mapping is als aanname gemarkeerd.
- **Rapportage Lineage:** geplande afspraak is onderscheiden van verleende zorg; demodefinities, perioden, populatie, uitsluitingen en bronvelden zijn verduidelijkt, inclusief dossierstatus. Lokale goedkeuring door rapportage-eigenaar en BI ontbreekt nog.
- **Autorisatie, JML en Change Impact:** model en gesimuleerde feitelijke toegang zijn apart met scope, noodzakelijkheid, goedkeuring, eindmoment en controle. Apparatuur en fysieke toegang hebben aparte eindmomenten. Geen automatisch breder profiel; maatregelen blijven voorgenomen, niet bewezen gerealiseerd.
- **Beheerbaarheid Scan:** bronlabels tellen niet meer als beoordeeld bewijs. Niet getoetst is niet groen; geaccepteerd vraagt fase, bron, versie, controledatum, bevoegde beoordelaar en akkoord. Gewijzigd bewijs maakt eerder akkoord ongeldig; een volledige checklist en kopieerfallback zijn beschikbaar.
- **Samenhang en taakverdieping:** de oorspronkelijke 20 HTML-bestanden hebben taak-/broninformatie, bevoegdheidsgrenzen en onderhoudsafspraken. Incident- en wijzigingsviews verwijzen naar elkaar; JML en autorisatie zijn verbonden. Testdekking, continuïteit en gegevenskwaliteit zijn eerst in bestaande pagina’s verdiept. De drie later toegevoegde zelfstandige prototypes hebben eigen beheerkaartjes, leesbare alternatieven en verwijzingen naar die broncasussen; er is geen gesynchroniseerde administratie.
- **Bron- en kennispatronen:** fictieve onderzoeken, pilotclaims en scores zijn uitdrukkelijk als verzonnen gemarkeerd. BronScanner gebruikt een ongemeten demo-index, geen betrouwbaarheidspercentage.
- **Nog vóór werkelijk gebruik:** wijs echte bronhouders aan, valideer procesinhoud en noodplannen met bevoegde deskundigen, sluit aan op de bestaande registraties en toets de meerwaarde met gebruikers. Geen prototype is daardoor productierijp verklaard.

## Volgende validatieronde

### Concrete vergelijkingen

De volgorde, bevoegde toetsrollen en succes-/stopcriteria staan in [AGENTS.md](AGENTS.md#status-en-meerwaarde). Voor deze verzameling ligt de volgende validatieronde bij de test-, continuïteits- en kwaliteitscasussen en de verbonden JML-/autorisatieviews. VraagKompas en Vraagdossier worden op hetzelfde dossier vergeleken. Onderstaande taken vormen het concrete vergelijkingsplan; uitvoering en resultaten zijn nog niet vastgelegd.

| Praktijktaak                                            | Vergelijking met bestaand hulpmiddel                                   | Vast te leggen resultaat                                                                                                |
| ------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Ontvangen maar niet verwerkte cliëntmutatie onderzoeken | Ketenkaart tegenover koppeldocumentatie en meldinformatie.             | Tijd tot juiste controle, juiste eigenaar, kwaliteit van escalatie en gemiste ketenstappen.                             |
| Nieuwe wijk- of teamrol beoordelen                      | Autorisatielandschap/JML tegenover huidige matrix en controlelijst.    | Herkende overmatige of ontbrekende toegang, begrip van tijdvakken, bewijs en vervolgactie.                              |
| Wijziging klaarzetten voor acceptatie                   | Impact- en Test Coverage-view tegenover huidig wijzigingsdossier.      | Ongeteste kritieke scenario's, herleidbaarheid naar eisen, bewijs en begrip van blockers.                               |
| Uitval van een zorgkritische applicatie bespreken       | Continuïteitsview tegenover huidig noodplan.                           | Juiste contact- en besluitroute, bereikbaarheid zonder getroffen systeem, grenzen van noodwerkwijze en herstelcontrole. |
| Afwijkende kritieke registratie onderzoeken             | Data Quality-verdieping tegenover huidige controlelijst of rapportage. | Herkende afwijking, getroffen afnemers, juiste eigenaar en veilige herstelroute.                                        |
| Bekende gebruikersvraag beantwoorden                    | VraagKompas of Vraagdossier tegenover het bestaande kennisitem.        | Juiste instructie, zoektijd, begrip van voorwaarden en onderhoud na bronwijziging.                                      |

Basismetingen en aangetoonde gebruikerswaarde ontbreken nog.

## Relatie met bestaand materiaal

De ideeën sluiten inhoudelijk aan op de \[[Article - In Beheer Name Checklist - Voor het onboarden van nieuwe applicaties|checklist voor functioneel applicatiebeheer bij nieuwe applicaties]\]. Die checklist ordent aandachtspunten in tekst; een interactieve visual zou voor een concrete casus relaties, impact en bewijs kunnen aanvullen. Die aanvulling is een mogelijkheid om te onderzoeken, geen bestaande koppeling of vastgesteld project.
