# Review: interactieve FAB-one-pagers voor de VVT

**Rol:** inhoudelijk reviewer, met aandacht voor de dagelijkse beheerpraktijk en informatiebeheer\
**Datum:** 1 oktober 2026\
**Bron:** `Ideeën voor interactieve FAB one-pagers.md`\
**Toetskader:** `functie-beschrijving-functioneel-applicatiebeheer.md`\
**Reviewtypen:** Developmental review (inhoud, selectie en samenhang) en Peer/Workshop review (bruikbaarheid voor de beoogde lezer)\
**Domein:** professionele hulpmiddelen voor functioneel applicatiebeheer in de VVT\
**Bronbescherming bij de oorspronkelijke beoordeling:** de twee Markdown-bronnen en de HTML-uitwerkingen zijn toen niet gewijzigd. De latere verwerking is afzonderlijk vastgelegd in §13.

**Status:** de reviewadviezen zijn verwerkt binnen de prototype-afbakening. De blijvende instructies zijn op 1 oktober 2026 gemigreerd naar [AGENTS.md](AGENTS.md); de algemene instructieblokken hieronder verwijzen daarheen. Conceptgebonden adviezen en oorspronkelijke bevindingen blijven bewaard als reviewcontext. §1–12 bewaren het oorspronkelijke oordeel en de toenmalige bevindingen; het zijn geen actuele lijsten met onopgeloste HTML-fouten. Zie §13 voor de afrondingscontrole, uitgevoerde tests en resterende lokale validatie.

## Afbakening en aannames

Deze review beantwoordt de vraag: **helpen de voorgestelde visuals een functioneel applicatiebeheerder in de VVT om zijn werk beter te doen, en voegt de interactieve vorm iets toe?**

De functiebeschrijving is het aangeleverde toetskader, niet een onafhankelijk gevalideerde beroepsstandaard. Het takenpakket verschilt per organisatie en per toegewezen applicatie. De lijst met leveranciers is daarom geen boodschappenlijst voor een visual en ook geen verplicht applicatiepakket.

Alle 35 concepten in de ideeënnotitie zijn inhoudelijk beoordeeld. Van de bestaande HTML-uitwerkingen zijn de relevante teksten, gegevensmodellen en interactielogica bekeken. De bron- en kennisvisuals zijn beoordeeld als herbruikbare presentatiepatronen. De oorspronkelijke beoordeling was **geen nieuwe browsertest**, toegankelijkheidsaudit, beveiligingsaudit of validatie met medewerkers. Bij de latere verwerking zijn wel gerichte browsertests uitgevoerd; die staan apart in §13. Eerdere testclaims uit de notitie zijn niet opnieuw vastgesteld. Productinformatie en wet- en regelgeving zijn niet extern gecontroleerd.

De beoordeling onderscheidt:

- **Vastgesteld:** wat de lokale documenten en HTML-bronnen laten zien.
- **Verwachte waarde:** een inhoudelijk onderbouwde inschatting van taakondersteuning.
- **Nog te bewijzen:** betere beslissingen, minder fouten, tijdwinst en minder onderhoudslast in de praktijk.

## Drie vragen voor de auteur

1. **Wat moet de lezer na het gebruik begrijpen, besluiten of doen?**\
   Kies per visual één hoofdtaak, bijvoorbeeld een ontbrekende cliëntmutatie herleiden, een acceptatietest voorbereiden of een autorisatie-uitzondering laten beoordelen. Alleen “overzicht krijgen” is te weinig om meerwaarde te toetsen.
1. **Wie is de primaire gebruiker, en wat weet die al?**\
   De hoofdgebruiker is hier de functioneel applicatiebeheerder. Kerngebruikers, servicedesk, proceseigenaren en leveranciers kunnen meelezen, maar hebben andere vragen. Een instructie voor een zorgmedewerker vraagt meestal een eenvoudiger route dan een ketenanalyse voor FAB en integratiebeheer.
1. **Wat moet bij herziening behouden blijven?**\
   Behoud het principe “overzicht → relatie/impact → detail/bewijs”, de concrete ketencasus en het onderscheid tussen prototype en gevalideerd hulpmiddel. Dat zijn de sterkste onderdelen van de verzameling.

## Hoofdoordeel

**Ja, de meeste FAB-concepten passen inhoudelijk bij de functie. Maar niet ieder concept verdient een zelfstandige one-pager, en de huidige voorkeursselectie is nog geen evenwichtige set voor de dagelijkse VVT-beheerpraktijk.**

De sterkste aansluiting zit in het verbinden van proces, applicatie, gegevens, rechten en verantwoordelijkheden. Vooral de Proces × Applicatie-map, Ketenkaart, Autorisatielandschap, Change Impact Map en Beheerbaarheid Scan ondersteunen herkenbare taken uit de functiebeschrijving. Het Applicatielandschap geeft daarvoor een bruikbare basis.

De verzameling is minder sterk in het aantonen van testdekking, het ondersteunen van gebruikers bij concrete handelingen en het veilig voortzetten van zorg bij uitval. Die onderwerpen worden wel genoemd of deels geraakt, maar krijgen minder gewicht dan wijzigingsanalyse en besluitvorming.

De belangrijkste stap is daarom **niet meer visualvormen bouwen, maar een kleinere samenhangende set koppelen aan echte beheertaken, actuele bronnen en een aantoonbaar bruikbare vervolgstap**.

**Gereedheidsoordeel:** geschikt als ideeënkader en prototypebibliotheek; nog niet voldoende onderbouwd als productierijpe FAB-gereedschapskist. De notitie erkent zelf terecht dat gebruikersvalidatie ontbreekt.

## 1. Inhoud en samenhang — Developmental review

### 1.1 De centrale vraag is goed; de selectie volgt die nog onvoldoende

De opening vraagt welke informatie FAB regelmatig moet overzien, uitleggen of bespreken. Dat is een goede taakgerichte vraag. Daarna verschuift de aandacht snel naar aantallen bestanden, vormnamen en beschikbare interacties. “Er is HTML” wordt zorgvuldig onderscheiden van “het is klaar”, maar er ontbreekt nog een even duidelijke onderbouwing van “dit ondersteunt deze taak”.

**Vindplaats:** ideeënnotitie, regels 13–30 en 107–145.

**Gevolg:** een lezer kan veel ontwerpen herkennen, maar kan niet snel bepalen welk hulpmiddel hij morgen nodig heeft en welk resultaat het moet opleveren.

**Aanbevolen actie:** voeg aan ieder concept een beheerkaartje toe met hoofdvraag, primaire gebruiker, gebruiksmoment, bron, inhoudelijk eigenaar en gewenste uitkomst. Zet taak en uitkomst vóór de beschrijving van de visualvorm.

### 1.2 De acht voorkeursconcepten dekken vooral veranderen en adviseren

De uitspraak dat de acht concepten “vrijwel de volledige FAB-cyclus” ondersteunen, is te ruim. Ze helpen bij begrijpen, impactanalyse, overdracht en besluiten. Maar expliciete dagelijkse taken zijn onderbelicht: gebruikersvragen omzetten in specificaties, acceptatietesten organiseren, instructies onderhouden, terugkerende fouten afhandelen en zorgcontinuïteit bewaken.

Er zijn elders in de verzameling wel incidentvisuals en een JML-uitwerking. Het probleem is dus niet dat alle operationele onderwerpen ontbreken, maar dat de **voorkeursselectie** ze minder zwaar laat meewegen. De notitie zegt bovendien zelf dat de Beheerbaarheid Scan geen volledige Test Coverage Map is.

**Vindplaats:** ideeënnotitie, regels 109–117 en 151; functiebeschrijving, regels 73–95 en 106–112.

**Gevolg:** wijzigingen en bestuurlijke gesprekken kunnen meer ontwerpenergie krijgen dan frequent terugkerend beheerwerk.

**Aanbevolen actie:** behoud de zes sterk taakgerichte voorkeursconcepten. Behandel Go/No-Go als onderdeel van een wijzigingsdossier en Decision Canvas als aanvullend overleginstrument. Geef testdekking, continuïteit en gegevenskwaliteit eerder een uitgewerkte VVT-casus.

### 1.3 De VVT-aansluiting zit in de gevolgen, niet in de applicatienamen

De fictieve wijkteamwijziging is een sterk voorbeeld: één codewijziging raakt inrichting, toegang, roosters, kostenplaatsen en rapportages. Dat is concreter dan een algemeen plaatje van systemen.

Tegelijk richt deze casus zich vooral op wijkverpleging en een teamconversie. De functie omvat ook verblijf, verzorging, externe ketenportalen en ondersteunende processen. Eén casus bewijst geen brede VVT-dekking. De Proces × Applicatie-map bevat daarnaast stellig geformuleerde demo-afspraken over indicatie, medicatieprofielen en declarabele prestaties. Die moeten niet als algemeen VVT-proces worden gelezen.

**Vindplaats:** ideeënnotitie, regels 48–57 en 113; functiebeschrijving, regels 22, 58 en 144–148; Proces × Applicatie-map, regels 404–463.

**Gevolg:** een herkenbare demo kan onbedoeld gezag krijgen als werkinstructie voor een andere organisatie of zorgvorm.

**Aanbevolen actie:** valideer de procesinhoud met de betreffende proceseigenaren en zorginhoudelijke deskundigen. Maak daarna een tweede casus voor zorg op een locatie of externe zorgoverdracht. Beschrijf welke afspraken lokaal gelden en welke onderdelen alleen de werking van het patroon demonstreren.

### 1.4 Samenhang vraagt gedeelde bronnen, niet alleen gedeelde voorbeeldnamen

Change Impact Map, Go/No-Go en Decision Canvas gebruiken dezelfde RFC en teamcodes. Dat maakt het verhaal begrijpelijk. De gegevens staan in de huidige bestanden wel afzonderlijk vastgelegd. Inhoudelijke samenhang is dus nog geen gedeeld dossier dat zichzelf actueel houdt.

**Vindplaats:** ideeënnotitie, regels 113 en 117; de afzonderlijke gegevensobjecten in de drie HTML-bestanden.

**Gevolg:** bij werkelijk gebruik kan een blocker in de cockpit opgelost zijn terwijl het canvas nog vermeldt dat die openstaat. Meerdere losse views kunnen extra registratiewerk veroorzaken.

**Aanbevolen actie:** laat verschillende weergaven verwijzen naar dezelfde wijziging, bevinding, eigenaar en bewijsbron. Gebruik waar beschikbaar bestaande registraties, bijvoorbeeld TOPdesk voor meldingen en wijzigingen en Saar voor de samenhang van processen en applicaties. De HTML-laag mag die informatie verduidelijken, maar moet niet stilzwijgend een tweede administratie worden.

### 1.5 De afsluitende vragen moeten toelatingscriteria worden

De open vragen over doel, bronnen, eigenaar en toegankelijkheid zijn precies de juiste vragen. Ze staan nu achteraan, nadat de voorkeursselectie al is gemaakt.

**Vindplaats:** ideeënnotitie, regels 155–161.

**Gevolg:** een aantrekkelijk ontwerp kan al ver uitgewerkt zijn voordat duidelijk is wie het bijhoudt of waarom interactie nodig is.

**Aanbevolen actie:** beoordeel die vragen vóór een concept wordt geselecteerd. Een onbekende bronhouder of onduidelijke vervolgstap is een reden om eerst te onderzoeken, niet om alvast een extra visual te bouwen.

## 2. Bruikbaarheid voor de beheerder — Peer/Workshop review

### 2.1 Wat al goed werkt: van relatie naar controlepunt

De Ketenkaart maakt onderscheid tussen ontvangst, inhoudelijke verwerking en rapportageverversing. Dat is waardevol: een groen technisch signaal hoeft niet te betekenen dat de cliëntmutatie goed is verwerkt. De kaart koppelt overdrachten aan een eigenaar en controlepunten en waarschuwt voor dubbele verwerking bij opnieuw aanbieden.

Het Applicatielandschap koppelt systemen aan processen, gebruikers en functionele controles. De Proces × Applicatie-map laat juist zien waar overtypen en aparte registraties plaatsvinden. Samen kunnen die vormen impliciete beheerkennis expliciet maken.

**Vindplaats:** Ketenkaart, regels 345–357 en 410–428; Applicatielandschap, regels 855–955; Proces × Applicatie-map, regels 441–463.

**Betekenis voor de gebruiker:** de visual helpt niet alleen bij kijken, maar bij het kiezen van de volgende controle en het uitleggen van een ketenprobleem.

**Aanbevolen actie:** behoud deze taakgerichte inhoud. Laat een FAB'er met een realistische, veilig geanonimiseerde melding aantonen of hij sneller het juiste controlepunt en de juiste eigenaar vindt dan met de bestaande documentatie.

### 2.2 Waar de gebruiker kan vastlopen: uitleg is nog geen werkhulpmiddel

De incidentvisuals, Serviceradar en Releaseatelier geven goede vragen per stap of perspectief. De interactie toont hoofdzakelijk vooraf geschreven uitleg. Antwoorden, bevindingen en vervolgacties worden daarin niet als dossier vastgelegd.

**Vindplaats:** incidentvisual, regels 584–661; Serviceradar, regels 111–136; Releaseatelier, regels 95–104.

**Betekenis voor de gebruiker:** als introductie of gesprekshulp werkt dit waarschijnlijk goed. Voor een ervaren beheerder kan steeds klikken naar bekende vragen langzamer zijn dan een vaste checklist of een goed ingericht ticketformulier.

**Aanbevolen actie:** benoem per uitwerking of het doel opleiding, overleg of uitvoering is. Maak de uitvoerende variant alleen interactief als selectie ook leidt naar relevante actuele informatie of een bruikbare overdracht. Een volledige, direct leesbare checklist blijft een serieuze alternatiefvorm.

### 2.3 De gebruiker moet kunnen zien wat de status betekent

De notitie zegt terecht dat een aangevinkte visual alleen als HTML beschikbaar is. Ook de HTML-uitwerkingen markeren veel gegevens als fictief. Dat voorkomt dat demo's direct voor werkelijkheid worden aangezien.

Toch kunnen signalen als “gereed”, “bewijs”, een dalende ernst of een berekend besluit sterker overkomen dan de onderbouwing rechtvaardigt. Een statusknop bewijst geen geslaagde test. Een bewijslabel is nog geen beoordeeld document. Een voorgestelde maatregel heeft het risico nog niet werkelijk verlaagd.

**Vindplaats:** ideeënnotitie, regels 17–22; Beheerbaarheid Scan, regels 480–522, 613 en 667–673; Change Impact Map, regels 350–413 en 464; Go/No-Go, regels 533–536.

**Betekenis voor de gebruiker:** een mooie samenvatting kan schijnzekerheid geven, juist op momenten waarop zorgcontinuïteit of privacy op het spel staat.

**Aanbevolen actie:** onderscheid voorgenomen, uitgevoerd, gecontroleerd en geaccepteerd. Toon bij bewijs ten minste bron, versie of datum, beoordelaar en uitkomst. Bij een ontbrekende controle hoort “onbekend” of “niet getoetst”, niet automatisch groen.

### 2.4 De rolgrens moet zichtbaar blijven

De functie beschrijft samenwerking met ICT, leveranciers, proceseigenaren en privacy- en beveiligingsdeskundigen. Bij externe portalen beheert FAB niet het achterliggende platform. De visuals moeten die verdeling ondersteunen.

**Vindplaats:** functiebeschrijving, regels 58, 119 en 132–136; autorisatie- en rapportagevisuals bevatten eigenaren en acties per onderdeel.

**Betekenis voor de gebruiker:** “eigenaar” kan anders ten onrechte worden gelezen als degene die het risico accepteert, de zorginhoud bepaalt én de technische wijziging uitvoert.

**Aanbevolen actie:** onderscheid waar nodig proces- of gegevenseigenaar, functioneel beheerder, technisch uitvoerder, leverancier en beslisser. FAB signaleert en adviseert; goedkeuring van ruimere toegang, een zorgwerkwijze of een livegang blijft bij de afgesproken bevoegde rol.

## 3. Dekking van de functiebeschrijving

De verwijzingen in deze tabel gaan naar de regels van de aangeleverde functiebeschrijving. “Dekking” betekent inhoudelijke ondersteuning, niet bewezen effectiviteit.

| FAB-taak                                                                         | Passende concepten                                                            | Beoordeling en ontbrekende verdieping                                                                                                  |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Functionele inrichting en beheerafspraken onderhouden, regels 73 en 76           | Beheerbaarheid Scan, Proces × Applicatie-map, Omgevingsvergelijker            | Goede basis. Een concreet inrichtingsoverzicht met parameter, doel, afhankelijkheid en wijzigingshistorie verdient meer aandacht.      |
| Releases afstemmen en wijzigingen uitvoeren, regels 74 en 76                     | Releaseatelier, Change Impact Map, Release Impact Explorer, Go/No-Go          | Sterk vertegenwoordigd. Koppel de views aan één wijzigingsdossier.                                                                     |
| Rollen en autorisaties beheren, regel 75                                         | Autorisatielandschap, JML                                                     | Direct passend. Maak afgesproken rechten, feitelijke toegang en tijdelijke uitzonderingen onderscheidbaar.                             |
| Incidenten analyseren en afhandeling bewaken, regel 77                           | Incidentvisual, Serviceradar, Root Cause Map, Known Error, Escalatiekaart     | Sterke inhoudelijke aansluiting; samenvoegen vermindert zoekwerk. Oorzaakopsporing vereist minder stellige gevolgtrekkingen.           |
| Functionele koppelingen controleren, regel 78                                    | Ketenkaart, Data Quality Map, gerichte Data Lineage                           | Zeer passende visualtaak. Controle van inhoud, aantallen, actualiteit en eindverwerking is belangrijker dan technische uptime alleen.  |
| Prioriteiten afstemmen, regels 79 en 126                                         | Impact- en incidentviews, overzicht uit bestaande meldingenregistratie        | Zorgimpact helpt prioriteren. Bouw hiervoor niet automatisch een extra cockpit; benut de bestaande werkvoorraad.                       |
| Gebruikersvragen onderzoeken en registraties vereenvoudigen, regels 90, 91 en 95 | Proces × Applicatie-map, Data Quality Map, gerichte stakeholderanalyse        | Goede potentie, vooral bij dubbel werk. Maak het knelpunt en het gewenste verschil meetbaar.                                           |
| Adviezen onderbouwen, regel 92                                                   | Change Impact Map, Decision Canvas, Pilot Cockpit                             | Passend als gezamenlijk afwegingsinstrument; geen vervanging van een bevoegde beslissing.                                              |
| Instrueren, ondersteunen en documenteren, regels 93 en 94                        | Known Error, VraagKompas of Vraagdossier, Adoptiekaart                        | Nog te weinig concrete FAB-inhoud. Een kennisitem of werkinstructie is vaak de betere basis.                                           |
| Sector- en regelwijzigingen vertalen, regel 106                                  | Release Impact Explorer, gerichte bronvisual                                  | Geen reden voor een aparte wetgevingsvisual zonder casus. Wel behoefte aan bron → lokale gevolgen → actie → eigenaar.                  |
| Wensen vertalen naar functionele specificaties, regel 108                        | Releaseatelier-intake, Test Coverage Map                                      | De expliciete keten knelpunt → eis → inrichting → acceptatiecriterium is nog onvoldoende uitgewerkt.                                   |
| Nieuwe functionaliteit en koppelingen testen, regel 109                          | Test Coverage Map, Omgevingsvergelijker, Go/No-Go                             | Belangrijkste ontbrekende verdieping. Een groen livegangcriterium vertelt niet welke eis of kritieke praktijksituatie nog ongetest is. |
| Voortgang, ingebruikname, nazorg en overdracht, regels 110–112                   | Releaseatelier, Beheerbaarheid Scan, Go/No-Go, Adoptiekaart                   | Ruim aanwezig. Laat acties en bewijs uit bestaande registraties komen.                                                                 |
| Cliëntveiligheid, privacy en continuïteit, regels 16, 121 en 148                 | Continuïteitskaart, Autorisatielandschap, Risk & Control, keten- en testviews | Moet in alle relevante views terugkomen, niet alleen als losse risicokaart.                                                            |

## 4. Advies per bestaand concept

**Betekenis van het advies:** behouden en doorontwikkelen = sterke taakmatch; samenvoegen = nuttige inhoud, maar liever een onderdeel van een taakgerichte view; gericht inzetten = waarde afhankelijk van dossier en doelgroep; eerst herzien = inhoudelijke beperking vóór praktisch gebruik. Dit is geen cijfermatige of met gebruikers gevalideerde rangorde.

| Concept                                              | Concrete vraag voor FAB in de VVT                                                                          | Advies en voorwaarde                                                                                                                                                                                               |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Van melding naar oplossing, inclusief Attent-variant | Welke stap en overdracht zijn nodig om deze verstoring af te handelen?                                     | **Samenvoegen als incidentingang.** Goed voor uitleg en opleiding. De twee varianten zijn één concept, geen dubbele functionele dekking. Voor uitvoering moet de informatie aansluiten op de meldingenregistratie. |
| Releaseatelier                                       | Wat moet ik voor deze wijziging uitzoeken, testen, communiceren en overdragen?                             | **Samenvoegen als wijzigingsingang.** Laat impact, testdekking en livegangbewijs hiervandaan bereikbaar zijn. De huidige uitleg is nog geen actueel dossier.                                                       |
| Serviceradar                                         | Kijk ik te eenzijdig naar de applicatie, terwijl de oorzaak bij proces, data of leverancier ligt?          | **Samenvoegen met incidentanalyse.** De perspectieven zijn goed; een aparte radiale pagina is niet altijd nodig.                                                                                                   |
| Applicatielandschap                                  | Welke processen en systemen raken een wijziging of uitval van deze applicatie?                             | **Behouden en doorontwikkelen.** Sterk voor afstemming en overdracht. Houd afhankelijkheden, eigenaar en peildatum actueel; een statisch landschap is geen live storingsmonitor.                                   |
| Beheerbaarheid Scan                                  | Kan regulier beheer dit na oplevering daadwerkelijk dragen?                                                | **Behouden en doorontwikkelen.** Sterk bij inbeheername en overdracht. Bewijslabels en statusknoppen vervangen geen uitgevoerde controle. Vergelijk de ring met een eenvoudige controlelijst.                      |
| Ketenkaart                                           | Waar bleef een cliëntmutatie steken, en wie controleert de volgende stap?                                  | **Behouden en doorontwikkelen.** De combinatie van herleidbaarheid, inhoudelijke controle en eigenaar geeft duidelijke meerwaarde boven een lijst van koppelingen.                                                 |
| Change Impact Map                                    | Welke gevolgen van deze wijziging missen we nog in proces, toegang, gegevens of beheer?                    | **Behouden en doorontwikkelen.** Sterke visuele taak. Onderscheid verwachte vermindering van risico van aantoonbaar gerealiseerde maatregelen.                                                                     |
| Proces × Applicatie-map                              | Waar registreren zorgmedewerkers dubbel, waar vallen overdrachten weg en welke inrichting veroorzaakt dat? | **Behouden en doorontwikkelen.** Zeer goede aansluiting op minder administratieve lasten. Laat de lokale procesinhoud en rolverdeling valideren.                                                                   |
| Autorisatielandschap                                 | Welke rol heeft welke toegang en welke uitzonderingen moeten worden beoordeeld?                            | **Behouden en doorontwikkelen.** Toon naast het model ook team- of cliëntscope, tijdelijke rechten en verschillen met feitelijke toekenning. Beoordeel noodtoegang volgens lokale afspraken.                       |
| Go/No-Go Cockpit                                     | Welke nog openstaande voorwaarden maken deze livegang niet verantwoord?                                    | **Gericht inzetten binnen het wijzigingsdossier.** De vorm bundelt bewijs goed, maar de huidige advieslogica en statustoekenning vragen herziening. FAB levert een advies; de bevoegde rol beslist.                |
| Decision Canvas                                      | Welke invoeringsroute heeft onder welke voorwaarden de voorkeur?                                           | **Gericht inzetten bij relevante keuzen.** Eerst harde veiligheidsvoorwaarden toetsen, daarna pas voorkeuren wegen. Een korte besluitnotitie kan bij eenvoudige vragen beter werken.                               |
| Joiner-Mover-Leaver-flow                             | Welke toegang is te laat beschikbaar of blijft na een teamwissel of vertrek te lang actief?                | **Behouden en verbinden met autorisatiebeheer.** Het tijdsraster maakt overgangsrisico's inzichtelijk. De huidige demo toont tijdvakken, geen feitelijke IAM-controle of volledige HR→IAM→applicatieketen.         |
| Rapportage Lineage                                   | Welk bronveld of welke berekening verklaart deze afwijking in een rapport?                                 | **Gericht inzetten; eerst definities herzien.** Nuttig als FAB ook rapportageketens ondersteunt, samen met BI en de rapportage-eigenaar. Geen vanzelfsprekende dagelijkse kerntaak voor iedere FAB'er.             |
| Root Cause Map / Oorzaakopsporing                    | Welke hypothese onderzoeken we nu, en wat is al met bewijs uitgesloten?                                    | **Eerst herzien, daarna opnemen in incidentanalyse.** Het uitsluitingsraster is interessant, maar één overgebleven demo-hypothese is geen aangetoonde oorzaak.                                                     |
| Bronkaart                                            | Welke onderdelen van leveranciers- of beleidsdocumentatie hebben gevolgen voor mijn beheer?                | **Gericht inzetten als bronpatroon.** Alleen waardevol met actuele FAB-inhoud en controleerbare verwijzingen; geen zelfstandige dagelijkse beheertool.                                                             |
| BronScanner                                          | Waar in een omvangrijke bron staat de relevante onderbouwing?                                              | **Gericht inzetten als alternatief bronpatroon.** Informatiedichtheid en betrouwbaarheidspercentages vragen een uitgelegde basis. Een inhoudsopgave kan genoeg zijn.                                               |
| Kennisatlas                                          | Hoe hangen verklaringen, voorwaarden en bekende knelpunten samen?                                          | **Voorlopig parkeren als zelfstandige FAB-tool.** Kies dit alleen als een netwerk werkelijk een terugkerende beheer- of leervraag beantwoordt.                                                                     |
| Vraagdossier                                         | Wat moet ik weten, onderbouwen of besluiten over één beheervraag?                                          | **Gericht inzetten als kennis- of adviespatroon.** Goede koppeling van kort antwoord aan bewijs. Vergelijk dit met VraagKompas op hetzelfde dossier; bouw niet beide zonder aantoonbaar verschil.                  |
| VraagKompas                                          | Welke uitleg, instructie of bron heb ik nodig voor deze gebruikers- of beheervraag?                        | **Gericht inzetten als kennispatroon.** Kansrijk voor overdracht en kerngebruikersondersteuning. Een bestaande kennisbank blijft de bron; navigatie vervangt geen goede instructie.                                |

## 5. Advies per nog open kandidaat

| Kandidaat                    | Verwachte VVT-waarde                                                                                               | Advies voor de volgende stap                                                                                                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Lineage                 | Herleiden waar een kritisch gegeven is veranderd en welke afnemers het gebruiken.                                  | **Verdieping van Ketenkaart.** Begin met één kritisch gegeven en echte transformaties; geen brede lineagekaart bouwen zonder concrete controlevraag.                                                           |
| Data Quality Map             | Ontbrekende, verkeerde of te late registraties verbinden aan gevolgen voor zorg, planning en verantwoording.       | **Hoge inhoudelijke prioriteit.** Leg kwaliteitsregel, eigenaar, gecontroleerde populatie, peildatum, afwijking en herstelroute vast. Toon geen willekeurig percentage “datakwaliteit”.                        |
| Functional Blueprint         | Overzicht van proces, rol, applicatie, data en koppeling in lagen.                                                 | **Samenvoegen.** Grote overlap met Proces × Applicatie-map en Applicatielandschap. Voeg alleen een laag toe als die een nieuwe vraag beantwoordt.                                                              |
| Test Coverage Map            | Aantonen welke eisen en kritieke praktijkscenario's wel of niet getest zijn.                                       | **Hoge inhoudelijke prioriteit.** Verbind wens/eis, rol, scenario, test, omgeving, versie, uitkomst, bevinding en akkoord. Neem negatieve autorisatie- en foutscenario's mee.                                  |
| Omgevingsvergelijker         | Verklaren waarom een testresultaat in acceptatie niet geldt voor productie.                                        | **Gerichte verdieping bij testen.** Waardevol als er aparte omgevingen zijn. Vergelijk functionele configuratie, versies, koppelingen en testrollen; veronderstel geen testomgeving voor ieder extern portaal. |
| Release Impact Explorer      | Leverancierswijzigingen vertalen naar lokale gevolgen en noodzakelijke tests.                                      | **Samenvoegen met wijzigingsingang en impactanalyse.** Sterke taakmatch. Meerwaarde zit in releasepunt → lokale inrichting → doelgroep → test/actie, niet in nog een samenvatting.                             |
| Applicatie Life Cycle Map    | Tijdig zien welke upgrades, beëindiging van ondersteuning of vervanging beheerwerk vragen.                         | **Gericht inzetten voor planning.** Nuttig samen met ICT en leveranciers. Geen hogere eerste prioriteit dan kritieke werking en testdekking zonder actuele aanleiding.                                         |
| Known Error / Workaround Map | Een bekende verstoring herkennen en een gecontroleerde tijdelijke werkwijze vinden.                                | **Opnemen in incident- en kennisvoorziening.** Vermeld toepassingsvoorwaarden, risico, eigenaar en herbeoordeling. Een goed kennisitem kan beter zijn dan een netwerkkaart.                                    |
| Escalatiekaart               | Weten wie nu verantwoordelijk is en wanneer zorgproces, ICT of leverancier moet aanhaken.                          | **Opnemen in incident- en continuïteitsview.** Toon actuele contactroute, bevoegdheid en overdrachtsinformatie. Een eenvoudige beslisroute is vaak genoeg.                                                     |
| Continuïteitskaart           | Bij uitval weten welk zorgproces geraakt is, welke afgesproken noodwerkwijze geldt en hoe herstel wordt bevestigd. | **Hoge inhoudelijke prioriteit.** Moet ook zonder de getroffen applicatie bereikbaar zijn. Laat zorginhoudelijke noodwerkwijzen door bevoegde deskundigen vaststellen.                                         |
| Leverancierskaart            | De juiste partij, afspraken en vereiste meldinformatie vinden.                                                     | **Opnemen als detail van applicatie, keten of incident.** Vermijd een tweede adressen- of contractadministratie.                                                                                               |
| Risk & Control Map           | Zien welk risico nog bestaat nadat een maatregel is uitgevoerd en getoetst.                                        | **Opnemen in impact en beheerbaarheid.** Wel onderscheid tussen plan, uitvoering, bewijs en risicoacceptatie. Een generieke extra risicokaart is niet automatisch nodig.                                       |
| Eigenaarschapkaart           | Voorkomen dat een ketenprobleem tussen partijen blijft liggen.                                                     | **Gedeelde informatielaag.** Verantwoordelijkheden moeten bij ieder relevant proces, gegeven en systeem zichtbaar zijn; niet alleen op een losse kaart.                                                        |
| Stakeholder Impact Map       | Per doelgroep zien welke handeling, toegang of ondersteuning verandert.                                            | **Opnemen in Change Impact en communicatie.** Onderscheid zorgmedewerkers, planners, cliëntadministratie, cliënten/naasten en ketenpartners waar relevant.                                                     |
| Adoptiekaart                 | Zien of een nieuwe werkwijze niet alleen is uitgelegd, maar goed en veilig wordt gebruikt.                         | **Gerichte verdieping bij grotere invoeringen.** Deelname aan training is geen bewijs van vaardigheid of goede registratie. Kies vooraf welke praktijksignalen tellen.                                         |
| Pilot Cockpit                | Vaststellen of een beperkte invoering het bedoelde probleem echt vermindert.                                       | **Gericht inzetten.** Zinvol bij onzekerheid over werking of gebruik. Koppel nulmeting, uitkomst, bijwerkingen en stopcriteria; niet nodig bij iedere kleine wijziging.                                        |

## 6. Concrete inhoudelijke aandachtspunten in de uitwerkingen

Deze bevindingen gaan over de betrouwbaarheid van de aangeboden hulp. Ze zijn geen volledige code- of UX-review. De fictieve status van de demo's verzacht het risico, maar neemt het niet weg zodra iemand het patroon met echte gegevens gebruikt.

### 6.1 Oorzaakopsporing sluit te veel uit op basis van zwakke signalen

In check `c1` sluit “een collega uit hetzelfde team heeft het ook” een ontbrekend recht uit. Meerdere collega's kunnen juist dezelfde verkeerde rol hebben. In `c3` sluit “de leverancier meldt geen storing” een leveranciersstoring uit, terwijl een statusmelding kan ontbreken of achterlopen. Het raster biedt alleen ja/nee; er is geen afzonderlijke uitkomst voor niet onderzocht of onvoldoende bewijs. Eén resterende hypothese krijgt vervolgens een concrete herstelactie.

**Gevolg:** de beheerder kan een plausibele oorzaak te vroeg laten vallen. De footer waarschuwt daarvoor, maar de centrale belofte “tot er één overblijft” blijft stellig.

**Aanbevolen actie:** behandel zulke antwoorden als aanwijzingen, niet als logisch sluitend bewijs. Voeg onbekend/niet gecontroleerd, bewijs en controledatum toe. Houd rekening met meer dan één oorzaak. Laat een resterende hypothese bevestigen voordat een herstelactie wordt uitgevoerd. Rechten vergelijken is geen toestemming om die van een collega over te nemen.

**Bron:** [Oorzaakopsporing](fab-oorzaakopsporing.html), regels 134–155 en 176–212.

### 6.2 Go/No-Go heeft een aantoonbare tegenstelling tussen regel en samenvatting

In `advice()` staan P1 en P2 vast op respectievelijk 0 en 2. Ook als alle criteria “gereed” zijn, blijft het berekende advies daardoor “Go onder voorwaarden”. De samenvatting zegt bij diezelfde toestand dat het advies onvoorwaardelijk is. De zichtbare drempel wordt niet algemeen tegen een veranderende bevindingenlijst getoetst.

Status wijzigen verandert bovendien niet het oorspronkelijke bewijs of de tekst “nog niet gedraaid”. Dat is bruikbaar om de interactie te demonstreren, maar onvoldoende als besluitonderbouwing.

**Aanbevolen actie:** laat advies, samenvatting, criteria en bevindingen op dezelfde gegevens en vastgestelde regels steunen. Maak veiligheid en kritieke privacyvoorwaarden expliciet voor de betreffende casus. Leg bij acceptatie vast wie het bewijs heeft beoordeeld en wie het eventuele restrisico accepteert. Laat het formele besluit niet door een statusknop vervangen.

**Bron:** [Go/No-Go Cockpit](fab-go-no-go-cockpit.html), regels 447–491 en 533–536.

### 6.3 Decision Canvas weegt harde voorwaarden mee als voorkeur

De score is een optelsom van fictieve deelscores maal instelbare gewichten voor zorgcontinuïteit, beheerlast, datakwaliteit en doorlooptijd. Er is geen haalbaarheidspoort vóór de rangorde. Daardoor kan een snelle optie hoog scoren zonder dat haar veiligheids- of uitvoeringsvoorwaarden zijn vervuld.

Ook is bij punt `B-3` de BI-mapping nog niet bewezen, terwijl `unc: false` ervoor zorgt dat het detail dit “Bevestigd” noemt. Dat is een directe tegenstelling tussen de onzekerheidstekst en het label.

**Aanbevolen actie:** beoordeel eerst of een optie aan de harde voorwaarden voldoet. Weeg daarna alleen de toelaatbare opties. Maak de betekenis en onderbouwing van deelscores duidelijk en markeer onbevestigde aannames consequent. De bestaande waarschuwing “hulpmiddel, geen besluit” is goed, maar repareert een verkeerde status of rangorde niet.

**Bron:** [Decision Canvas](fab-decision-canvas.html), regels 311–315, 350–352, 449–453 en 509–516.

### 6.4 Rapportage Lineage heeft een goede vorm, maar onzuivere definities

De casus heet “wachttijd tot eerste zorgmoment”; het getal en de bron volgen de eerste ingeplande afspraak. Dat is niet vanzelf de eerste werkelijk verleende zorg. De demo noemt daarnaast “Bezettingsgraad” zowel gewerkte uren van contracturen als beschikbare behandeluren besteed aan cliëntcontact. Die begrippen vallen niet zonder nadere afspraken samen.

In de formule staan geregistreerde uren tegenover contracturen. Het ene gegeven is per dag, het andere per week, terwijl de berekening per maand wordt beschreven. Hoe perioden en eenheden gelijk worden gemaakt, is niet vastgelegd. De berekening voor open aanmeldingen heeft ook dossierstatus nodig om annuleringen uit te sluiten, maar dat veld staat niet als eigen afhankelijkheid in de getoonde herkomstketen.

**Aanbevolen actie:** kies één relevante, met de rapportage-eigenaar afgestemde vraag. Leg teller, noemer, tijdseenheid, populatie, uitsluitingen, peildatum en bronvelden vast. Laat BI de berekening en FAB de betrokken bronregistraties en functionele gevolgen beoordelen. Een gemarkeerde bronachterstand is nuttig, maar zegt niets over een inhoudelijk verkeerde KPI-definitie.

**Bron:** [Rapportage Lineage](fab-rapportage-lineage.html), regels 131–177.

### 6.5 Autorisatie en JML vragen lokale voorwaarden, niet algemene voorbeeldregels

Het Autorisatielandschap maakt modelrechten en uitzonderingen inzichtelijk, maar een niveau “Lezen” of “Muteren” per applicatie is te grof om effectieve toegang te bewijzen. In de JML-demo worden tijdvakken getoond; de footer benoemt terecht dat die niet aangeven hoeveel rechten iemand heeft. Automatische intrekking en overgangstermijnen zijn daar fictieve afspraken.

De Change Impact Map noemt als restmaatregel “bij twijfel tijdelijk een breder profiel”. Dat is geen neutrale standaardoplossing voor een toegangsknelpunt: het kan juist de privacy-impact vergroten.

**Aanbevolen actie:** maak scope, goedkeuring, noodzakelijkheid, einddatum en controle van feitelijke toegang expliciet. Neem bij validatie ook tijdelijke medewerkers, meerdere teamrollen en externe portalen mee als die in de organisatie voorkomen. Kies voor goedgekeurde uitzonderingen met begrenzing en toezicht, niet automatisch voor bredere toegang. Splits in JML bezit van apparatuur, fysieke toegang en applicatierechten waar hun eindmoment verschilt.

**Bronnen:** [Autorisatielandschap](fab-autorisatielandschap.html), regels 436–483; [Joiner-Mover-Leaver](fab-joiner-mover-leaver.html), regels 166–211; [Change Impact Map](fab-change-impact-map.html), regels 370–373.

## 7. Interactie en operationele voorwaarden — gemigreerd

De herbruikbare instructies uit deze sectie staan nu in [toelating en selectie](AGENTS.md#toelating-en-selectie) en [minimale voorwaarden per operationele uitwerking](AGENTS.md#minimale-voorwaarden-per-operationele-uitwerking) in AGENTS.md. De aanvullende regels per taak staan bij [diagnose-, besluit- en definitielogica](AGENTS.md#diagnose--besluit--en-definitielogica). Deze verwijzingen vervangen de dubbele instructielijst.

## 8. Aanbevolen samenhang en selectie

### Behoud zes basisconcepten

- **Applicatielandschap:** waar het proces en de systemen samenkomen.
- **Proces × Applicatie-map:** waar mensen registreren en waar overdrachten ontstaan.
- **Ketenkaart:** wat met een gegeven of bericht gebeurt en wie dat controleert.
- **Autorisatielandschap:** welke toegang bedoeld is en welke uitzonderingen aandacht vragen.
- **Change Impact Map:** welke gevolgen en maatregelen bij een wijziging horen.
- **Beheerbaarheid Scan:** of inrichting, ondersteuning en overdracht voldoende zijn geborgd.

Dit is een inhoudelijk onderbouwde basis, geen vaste set die iedere FAB'er dagelijks moet openen.

### Maak twee taakgerichte ingangen

**Incident en continuïteit:** verbind melding, Serviceradar-perspectieven, veilige oorzaakopsporing, bekende fouten, escalatie en de afgesproken noodwerkwijze. Bij directe zorgimpact hoeft de beheerder niet eerst een volledige analyse af te ronden voordat het afgesproken continuïteitsproces start.

**Wijziging en acceptatie:** gebruik Releaseatelier als ingang naar lokale release-impact, eisen, impactanalyse, testdekking, Go/No-Go en overdracht. Eén dossier kan verschillende views hebben zonder dat iedere view een los gegevensbestand wordt.

Verbind JML aan autorisatiebeheer. Voeg gegevenskwaliteit en waar nodig gegevens- of rapportageherkomst toe aan de relevante keten. Gebruik een bronpatroon alleen waar een omvangrijke bron werkelijk uitleg nodig heeft. Decision Canvas blijft een aanvullende view voor complexe keuzen, niet het centrum van het dagelijkse beheer.

## 9. Wat moet in de ideeënnotitie worden herzien?

Dit waren adviezen voor de volgende revisie; de bronnotitie was bij de oorspronkelijke beoordeling niet aangepast. Inmiddels zijn de inventarisatie, selectie en status herzien; zie §13.

| Onderdeel                                       | Bevinding                                                                                                                                                                                                                                                                                                                      | Aanbevolen auteursactie                                                                                                                                                                                                                                            |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bronbeschikbaarheid en status, regels 15 en 149 | De map bevat nu 20 HTML-bestanden voor 19 concepten: 14 FAB-concepten en 5 bron-/kennisconcepten. De tweede incidentvariant verklaart het extra bestand. De genoemde 17/16 en 11 FAB zijn verouderd. De checkboxes zelf kloppen al: JML, Rapportage Lineage en Root Cause Map staan op regels 79, 81 en 93 terecht aangevinkt. | Werk alleen de lopende tekst op regels 15 en 149 bij naar 20 bestanden, 19 concepten, 14 FAB en 5 bron/kennis. Pas de checkboxes niet aan.                                                                                                                         |
| Aanvullende kandidaten, regel 74                | De introductie zegt dat deze richtingen nog geen eigen HTML-bestand hebben, terwijl JML, Rapportage Lineage en Root Cause Map in die sectie aangevinkt zijn en naar bestaande HTML wijzen. De opsomming van verplaatste visuals noemt die drie niet.                                                                           | Herschrijf regel 74, zodat die geen uitgewerkte concepten meer als “nog geen HTML” aanduidt. Verplaats de drie uitgewerkte concepten óf vermeld expliciet dat ze in de kandidatenlijst zijn blijven staan. Er zijn 19 aangevinkte concepten en 16 open kandidaten. |
| Voorkeursselectie, regels 109–117               | De brede cyclusclaim is niet volledig onderbouwd; meerdere dagelijkse functietaken blijven buiten de selectie.                                                                                                                                                                                                                 | Beschrijf waarom de zes basisconcepten belangrijk zijn en waarom testen, continuïteit en gegevenskwaliteit verdieping vragen.                                                                                                                                      |
| Beschrijving van interacties, regels 123–132    | De vorm is goed beschreven, maar taakresultaat en onderhoudslast ontbreken per concept.                                                                                                                                                                                                                                        | Voeg hoofdvraag, bron, eigenaar, gebruiksmoment en vervolgstap toe.                                                                                                                                                                                                |
| Status en testclaims, regel 149                 | Eerdere browserchecks worden genoemd, maar zijn geen gebruikersvalidatie of bewijs van VVT-meerwaarde.                                                                                                                                                                                                                         | Houd technische teststatus, inhoudelijke validatie en praktijkwaarde apart.                                                                                                                                                                                        |
| Open vragen, regels 155–161                     | Dit zijn sterke selectievragen, maar ze staan na de conceptkeuze.                                                                                                                                                                                                                                                              | Gebruik ze vooraf als toelatingscriteria; sluit af met concrete keuzes voor de volgende validatieronde.                                                                                                                                                            |

Een mogelijke nieuwe volgorde is: doel en doelgroep → FAB-taken en selectiecriteria → basisconcepten en taakgerichte ingangen → overige patronen → actuele beschikbaarheid en validatiestatus → concrete volgende toetsen. Dat maakt de notitie bruikbaarder als beslisdocument zonder de ideeënvoorraad weg te gooien.

## 10. Hoe tonen we de meerwaarde aan?

De werkwijze, meetpunten en succes-/stopcriteria zijn gemigreerd naar [status en meerwaarde](AGENTS.md#status-en-meerwaarde). De onderstaande tabel bewaart de oorspronkelijk voorgestelde praktijkvergelijkingen; er zijn hier geen meetresultaten vastgelegd.

| Praktijktaak                                                | Vergelijking                                                       | Wat vastleggen                                                                                                                            |
| ----------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Een ontvangen maar niet verwerkte cliëntmutatie onderzoeken | Ketenkaart tegenover huidige koppeldocumentatie en meldinformatie  | Tijd tot het juiste controlepunt, juistheid van de eigenaar, kwaliteit van de escalatie en gemiste ketenstappen.                          |
| Een nieuwe wijk- of teamrol beoordelen                      | Autorisatielandschap/JML tegenover huidige matrix en controlelijst | Herkende overmatige of ontbrekende toegang, juist begrepen tijdvakken, bewijs van toekenning en noodzakelijke vervolgactie.               |
| Een wijziging klaarzetten voor acceptatie                   | Impact- en Test Coverage-view tegenover huidig wijzigingsdossier   | Ontdekte ongeteste kritieke scenario's, herleidbaarheid naar eisen, volledigheid van bewijs en begrip van blockers.                       |
| Uitval van een zorgkritische applicatie bespreken           | Continuïteitsview tegenover huidig noodplan                        | Juiste contact- en besluitroute, bereikbaarheid zonder getroffen systeem, herkenning van grenzen van de noodwerkwijze en herstelcontrole. |
| Een bekende gebruikersvraag beantwoorden                    | VraagKompas of Vraagdossier tegenover het bestaande kennisitem     | Juiste instructie, zoektijd, begrip van voorwaarden en onderhoudswerk na een wijziging in de bron.                                        |

## 11. Aanbevolen vervolgreview en grenzen

De validatievolgorde en toetsrollen staan nu in [AGENTS.md](AGENTS.md#status-en-meerwaarde); de technische controles en hun grenzen in [verificatie](AGENTS.md#verificatie).

Deze review heeft geen zorgprotocol, wettelijke naleving of leveranciersfunctionaliteit gecertificeerd. Bij de oorspronkelijke beoordeling zijn de Markdown- en HTML-bestanden niet gewijzigd. De latere verwerking in de ideeënnotitie en prototypes is vastgelegd in §13; de functiebeschrijving is ongewijzigd gebleven. Alle prioriteiten blijven adviezen; aantoonbare gebruikerswaarde moet nog worden vastgesteld.

## 12. Revisieprioriteiten

1. **Herzie eerst de stellige diagnose- en besluitlogica.** Pak de uitsluitingsregels, de Go/No-Go-tegenstrijdigheid, de haalbaarheid van besluitopties en de rapportagedefinities aan voordat deze patronen echte beheerbeslissingen ondersteunen.
1. **Verbind de selectie expliciet aan de functie.** Behoud de zes basisconcepten, maak incident en wijziging de taakgerichte ingangen en behandel Decision Canvas en bronvisuals als gerichte aanvullingen.
1. **Werk drie onderbelichte taken inhoudelijk uit.** Geef Test Coverage, Continuïteit en Data Quality een concrete VVT-casus. Bepaal pas daarna of ieder onderwerp een eigen one-pager nodig heeft. Verbind de bestaande JML-uitwerking aan autorisatiebeheer.
1. **Maak bronbeheer en bevoegdheden onderdeel van ieder ontwerp.** Leg eigenaar, datum, bewijs, goedkeuring en onderhoud vast. Voorkom dat losse HTML-bestanden de afgesproken registraties gaan dupliceren.
1. **Werk de inventarisatie en status bij.** Corrigeer de tellingen op regels 15 en 149 en de introductie van de kandidatenlijst op regel 74; de checkboxes zelf kloppen al. Houd aanwezig, technisch getest, inhoudelijk beoordeeld en met gebruikers gevalideerd apart.
1. **Toets de daadwerkelijke meerwaarde vóór verdere verbreding.** Vergelijk op dezelfde taak met bestaande checklists, tickets, kennisitems en documentatie. Ga door met vormen die juistheid, overzicht of overdracht verbeteren zonder onredelijke onderhoudslast.

## 13. Afrondingscontrole na verwerking

**Datum: 1 oktober 2026. Status: afgerond voor de prototype-revisie; niet vrijgegeven voor operationeel gebruik.**

De conclusies zijn opnieuw vergeleken met de aanwezige HTML. De specifieke correcties uit §6 waren grotendeels al verwerkt. De aanvullende controle vond nog ontbrekende bewijsborging in de Beheerbaarheid Scan, beheercontext in de HTML, verbindingen tussen de taakgerichte ingangen en concrete uitwerking van testdekking, continuïteit en gegevenskwaliteit. Die punten zijn nu opgepakt. De functiebeschrijving is niet aangepast; de ideeënnotitie geeft de huidige status weer.

### 13.1 Wat is verwerkt?

| Reviewconclusie                                                                                                | Huidige verwerking                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Status en grens                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Taak, doelgroep, gebruiksmoment, bron, eigenaar en gewenste uitkomst vóór de visualvorm (§1.1, §1.5, §2.2, §7) | Alle 20 HTML-bestanden hebben een beheerkaart met hoofdvraag, gebruiker, bronstatus, revisiedatum, voorgestelde verantwoordelijkheden, concrete vervolgstap en onderhouds-/toelatingsafspraken. Opleiding, overleg en operationele beperkingen zijn benoemd.                                                                                                                                                                                                                                                                                                                             | Verwerkt als prototypecontext. Echte bronhouders en lokale geldigheid zijn niet verzonnen; ontbreken staat expliciet vermeld.                                                                                                                                         |
| Samenhangende selectie en twee taakgerichte ingangen (§1.2, §4, §8, §9)                                        | Incidentbeeld verwijst naar Serviceradar, Oorzaakopsporing, Ketenkaart en het kennispatroon. Releaseatelier verwijst naar impact, livegangadvies, beheeracceptatie en optiekeuze. JML en Autorisatielandschap verwijzen naar elkaar. De ideeënnotitie behoudt zes basisconcepten en gerichte aanvullingen.                                                                                                                                                                                                                                                                               | Verwerkt als navigatie en taakindeling, zonder extra losse visuals. De twee incidentvarianten blijven één concept.                                                                                                                                                    |
| Gedeelde casus is geen gedeeld dossier (§1.4)                                                                  | De wijzigingsviews vermelden de gedeelde RFC-2026-118, eigen bronstatus en het ontbreken van synchronisatie. Releaseatelier benoemt apart CHG-184 en CHG-DEMO-LOC-02. Het misleidende “deelt gegevens” in Decision Canvas is verduidelijkt.                                                                                                                                                                                                                                                                                                                                              | Prototypegrens expliciet gemaakt. Een echte koppeling met TOPdesk, Saar of een andere afgesproken bron blijft een vervolgstap vóór productie; er is geen bronadapter of tweede administratie gebouwd.                                                                 |
| Meer VVT-breedte en drie onderbelichte taken (§1.2–1.3, §3, §5, §12.3)                                         | [Releaseatelier](fab-releaseatelier.html#test-coverage) bevat vijf eisen/tests voor zorgoverdracht naar een woonzorglocatie: normale verwerking, negatieve autorisatie, ontbrekend veld, dubbele aanbieding en terugval/herstel. [Incidentbeeld](incident-onepager.html#continuity) en de [Attent-variant](incident-onepager-attent.html#continuity) bevatten een ECD-uitvalcasus op een locatie. [Ketenkaart](fab-ketenkaart.html#data-quality) bevat drie kwaliteitsregels met 120 synthetische berichten, populatie, mapping, peildatum, afwijking, eigenaar en veilige herstelroute. | Inhoudelijk uitgewerkt binnen bestaande pagina’s. Testuitkomsten zijn niet uitgevoerd; cijfers zijn illustraties. Geen lokaal zorgprotocol, goedgekeurd noodplan of brede VVT-dekking geclaimd. De 16 kandidaten blijven open voor eventuele zelfstandige uitwerking. |
| Bewijslabels en statusknoppen mogen geen schijnzekerheid geven (§2.3, §4, §7)                                  | Beheerbaarheid Scan telt geen bronlabels als beoordeeld bewijs. De acht eerder groene controles beginnen als niet getoetst. Geaccepteerd vraagt fase, bron, versie, controledatum, bevoegde beoordelaar en akkoord. Wijziging van de beoordeling maakt eerder akkoord ongeldig; afkeuring is een blocker. Samenvatting en export tonen dezelfde beoordeling, met handmatige kopieerfallback en bescherming tegen verouderde exportfeedback.                                                                                                                                              | Verwerkt en getest. Het blijft een sessiesimulatie, geen echte bewijsbeoordeling of formeel overdrachtsbesluit.                                                                                                                                                       |
| Veilige oorzaakopsporing (§6.1)                                                                                | Antwoorden geven aanwijzingen, geen automatische uitsluitingen. Onbekend, gedateerd bewijs, beoordelaar, herbeoordeling en meerdere mogelijke oorzaken blijven zichtbaar. Herstel vereist afzonderlijke bevestiging en bevoegdheid.                                                                                                                                                                                                                                                                                                                                                      | Eerdere verwerking opnieuw getest; zwakke signalen sluiten rechten- of leveranciersproblemen niet uit.                                                                                                                                                                |
| Go/No-Go zonder tegenstrijdige regels (§6.2)                                                                   | Criteria en veranderende bevindingen sturen dezelfde advies-, samenvattings- en exportlogica. Harde zorg-/privacyvoorwaarden, bewijsmetadata en risicoacceptatie zijn apart zichtbaar.                                                                                                                                                                                                                                                                                                                                                                                                   | Eerdere verwerking opnieuw getest voor onbekend, afkeuring, P1, P2-drempel, voorwaarden, Go en reset. De bevoegde rol beslist buiten de simulatie.                                                                                                                    |
| Harde voorwaarden vóór voorkeurweging (§6.3)                                                                   | Decision Canvas rangschikt alleen toelaatbare opties. Onbekend bewijs verhindert toelating; de BI-mapping B-3 is een aanname. De schaal is toegelicht; ook gelijke stand en een lege rangorde worden consistent weergegeven.                                                                                                                                                                                                                                                                                                                                                             | Eerdere verwerking opnieuw getest, ook zonder JavaScript. Deelscores blijven fictieve inschattingen.                                                                                                                                                                  |
| Juiste rapportagedefinities (§6.4)                                                                             | Geplande afspraak is geen verleende zorg. Definities, teller/noemer, gelijke perioden, uitsluitingen en bronvelden zijn verduidelijkt; dossierstatus is een eigen afhankelijkheid.                                                                                                                                                                                                                                                                                                                                                                                                       | Eerdere verwerking opnieuw getest. Rapportage-eigenaar en BI moeten de betekenis en berekening nog lokaal goedkeuren.                                                                                                                                                 |
| Toegang, JML, rolgrenzen en risicoreductie (§2.4, §6.5, §7)                                                    | Modelrechten en gesimuleerde feitelijke toegang staan apart met scope, noodzakelijkheid, goedkeuring, eindmoment en controle. JML onderscheidt apparatuur, fysieke toegang en applicatierechten. Geen automatisch breder profiel; Change Impact toont maatregelen als voorgenomen en risicoreductie als hypothetisch. Proces × Applicatie-map markeert demoproces en bevoegde zorginhoudelijke rollen.                                                                                                                                                                                   | Eerdere verwerking opnieuw getest en aan de taakgerichte ingangen verbonden. Geen echte IAM-controle, toegangswijziging, lokaal akkoord of gerealiseerde maatregel geclaimd.                                                                                          |
| Leesbare alternatieven en veilige informatie (§2.2, §4, §7)                                                    | Incidentbeeld, Serviceradar en Releaseatelier hebben volledige leesbare checklists naast de klikroute; Beheerbaarheid Scan heeft vijftien direct leesbare controles. Nieuwe test-/kwaliteitsinhoud gebruikt tabellen; continuïteitsinformatie blijft offline en zonder JavaScript leesbaar en is afdrukbaar. De kennis-/bronpatronen hebben een zichtbare waarschuwing bij verzonnen onderzoek en pilotclaims. BronScanner toont een ongemeten demo-index in plaats van een betrouwbaarheidspercentage.                                                                                  | Verwerkt als alternatieve presentatie. Het actuele lokale noodplan en echte contactroutes ontbreken nog; een standalone HTML of afdruk bewijst geen operationele bereikbaarheid.                                                                                      |
| Actuele inventaris en gescheiden validatiestatus (§9, §12.5)                                                   | De ideeënnotitie vermeldt 20 bestanden, 19 concepten, 14 FAB- en 5 bron-/kennisconcepten, plus 16 kandidaten. Stale meldingen “nog niet in de HTML opgelost” zijn vervangen door de huidige verwerking en vervolgstappen.                                                                                                                                                                                                                                                                                                                                                                | Verwerkt. Aanwezig, technisch getest, inhoudelijk beoordeeld en met gebruikers gevalideerd blijven afzonderlijk.                                                                                                                                                      |

### 13.2 Wat is daadwerkelijk getest?

Drie gerichte Python Playwright-scripts zijn met lokaal Chrome in headless-modus uitgevoerd; alle drie zijn geslaagd:

- `/tmp/fab-review-closure-test.py`: bewijsborging van Beheerbaarheid Scan, herbeoordeling, afkeuring, reset, toetsenbordbediening en kopieerfallback; op alle 20 HTML-bestanden één beheerkaart, revisiedatum, unieke DOM-ID’s, geldige lokale links inclusief fragmenten, documentbreedte bij 320 en 390 pixels en geen JavaScript-fouten. Ook vijf testscenario’s, drie kwaliteitsregels, volledige checklists, afdrukbare incident-/continuïteitsinformatie en bereikbaarheid van de kritieke aanvullingen zonder JavaScript zijn gecontroleerd.
- `/tmp/fab-review-test.py`: regressies voor Oorzaakopsporing, Go/No-Go, Decision Canvas, Rapportage Lineage, Autorisatielandschap, JML, Change Impact en Proces × Applicatie-map; inclusief ontbrekend bewijs, veilige verwerking van ingevoerde tekst, hardepoortlogica, dynamische bevindingen, bronafhankelijkheden, daggrenzen, bevoegde rolverdeling, export, mobiel en afdrukmodus.
- `/tmp/fab-review-extra-test.py`: aanvullende controles op P2-drempel en afkeuring, ontbrekende risicoacceptatie, toetsenbordnavigatie van tabs, kopieerfallbacks, lege rangorde zonder JavaScript en onbekende diagnose-uitkomsten.

De aanvullende cases en het bewijsformulier zijn ook via browserscreenshots bekeken. Tijdens de controle zijn mobiele breedteproblemen in Applicatielandschap, Vraagdossier, Autorisatielandschap en beide incidentvarianten herleid tot minimale inhoudsbreedte, niet-afbrekende koppen of niet-omlopende flexrijen en gecorrigeerd. De beheercontext van Applicatielandschap is ook op desktop bereikbaar gemaakt; de vaste werkruimte verborg die anders buiten de pagina.

Dit zijn gerichte technische controles, **geen volledige toegankelijkheids-, beveiligings- of printaudit**. Een afdrukbare aanvulling mag meerdere pagina’s gebruiken; de eerdere claim “één A4” is niet voor de uitgebreide pagina’s overgenomen. De tijdelijke testscripts staan buiten de projectmap; `AGENTS.md` bewaart de projectopzet en de herbruikbare verificatieafspraken.

### 13.3 Wat blijft buiten deze afronding?

De open toelatingsvoorwaarden voor werkelijk gebruik zijn gemigreerd naar [AGENTS.md](AGENTS.md#status-en-meerwaarde). Lokale goedkeuring, echte bronintegratie en praktijk-/toegankelijkheidsvalidatie waren bij deze afronding niet aangetoond.

**Eindconclusie:** de resterende, uitvoerbare HTML-conclusies uit deze review zijn verwerkt en gericht technisch gecontroleerd. De review is daarmee afgerond als prototype-revisie. Lokale goedkeuring, bronintegratie en bewezen gebruikerswaarde blijven bewust open toelatingsvoorwaarden, niet stilzwijgend afgeronde reviewpunten.
