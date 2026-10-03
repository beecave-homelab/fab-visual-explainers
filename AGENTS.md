# Projectafspraken

## Opzet

Deze map bevat 32 zelfstandige HTML-prototypes voor 31 concepten: 26 FAB-concepten en 5 bron-/kennispatronen. De twee incidentvarianten tonen dezelfde inhoud met andere vormgeving. CSS, JavaScript en synthetische voorbeelddata staan in ieder HTML-bestand; er is geen backend, buildstap of gekoppelde dossierregistratie.

De [ideeënnotitie](ideeen_voor_interactieve_fab_one_pagers.md) beschrijft de inventaris, selectie en actuele status. De blijvende werkafspraken uit de ideeënnotitie en de VVT-review zijn op 1 oktober 2026 hier samengebracht; AGENTS.md is daarvoor de centrale instructiebron. Het afzonderlijke reviewrapport is na verwerking verwijderd en blijft terug te vinden in de Git-historie. De functiebeschrijving is het aangeleverde toetskader, geen onafhankelijk gevalideerde beroepsstandaard.

De HTML staat onder `visuals/`, in `incident_en_continuiteit/`, `wijziging_en_acceptatie/`, `landschap_en_processen/`, `toegang/`, `gegevens_en_ketens/` en `bronnen_en_kennis/`. Kies één categorie op basis van de hoofdtaak; mapnamen gebruiken snake_case, bestaande HTML-bestandsnamen blijven behouden. Houd bestandsnamen binnen `visuals/` uniek. Werk bij verplaatsingen relatieve links (ook tussen categorieën en inclusief fragmenten) en documentverwijzingen bij.

## Toelating en selectie

- Een concept gaat pas door naar uitwerking als de hoofdtaak, primaire gebruiker, bron, inhoudelijk eigenaar en concrete vervolgstap duidelijk zijn. Onbekende bronhouder of onduidelijk resultaat: eerst onderzoek, geen extra visual.
- Interactie alleen als die de taak merkbaar verbetert: relaties, gevolgen of actuele informatie zichtbaar maken, of leiden naar de volgende controle, eigenaar of goedgekeurde noodwerkwijze. Alleen klikbare uitleg is geen verbetering; een direct leesbare checklist blijft een serieus alternatief. Benoem of de visual voor opleiding, overleg of uitvoering is.
- Houd het uitgangspunt overzicht → relatie/impact → detail/bewijs aan: begin met een scanbaar overzicht, laat een relevant onderdeel kiezen, toon relaties en gevolgen en bied daarna detail, bewijs, open punten en de volgende actie.
- FAB is de primaire gebruiker, tenzij de concrete opdracht anders bepaalt. Kerngebruikers, servicedesk, proceseigenaren, ICT en leveranciers hebben andere vragen en bevoegdheden; eindgebruikersinstructies vragen een eigen doelgroep en eenvoudiger route.
- Gebruik de functiebeschrijving taakgericht; het takenpakket verschilt per organisatie, zorgvorm en applicatie. Leveranciersnamen vormen geen verplicht applicatiepakket. Eén synthetische casus bewijst geen brede VVT-dekking.
- Verdiep bestaande taakgerichte ingangen en informatielagen vóór uitbreiding met losse pagina’s. Benut de bestaande werkvoorraad voor prioritering; bouw niet automatisch een extra cockpit. Selectieadviezen en open kandidaten in de ideeënnotitie zijn geen bouwopdracht.

## Minimale voorwaarden per operationele uitwerking

1. Een beheerkaart met één herkenbare hoofdvraag, primaire gebruiker, gebruiksmoment (opleiding, overleg of uitvoering), bronstatus, inhoudelijk eigenaar en concrete vervolgstap, zoals een testplan, escalatiepakket, beoordeelde uitzondering of controlelijst.
1. Bron, versie of peildatum, inhoudelijk eigenaar, geldigheid, herzieningsmoment en onderhoud zichtbaar; verouderde informatie herkenbaar. Niet toegewezen eigenaren blijven voorgestelde rollen, ontbrekende bronhouders blijven onbekend.
1. Zorgimpact onderscheiden: hinder, stilgevallen zorgondersteuning, privacyrisico en financiële gevolgen. Het aantal getroffen gebruikers bepaalt niet alleen de prioriteit.
1. Bewijs en onzekerheid: houd voorgenomen, uitgevoerd, gecontroleerd en geaccepteerd apart. Een bronlabel is geen beoordeeld bewijs; ontbrekende controle is onbekend/niet getoetst, niet groen. Technische ontvangst bewijst geen inhoudelijke verwerking; een geplande maatregel verlaagt het risico nog niet aantoonbaar. Toon bij bewijs fase, bron, versie of datum, controledatum, bevoegde beoordelaar en uitkomst/akkoord. Gewijzigd bewijs maakt eerder akkoord ongeldig.
1. Bevoegdheid zichtbaar: wie voert uit, toetst, keurt goed en accepteert restrisico. Onderscheid proces-/gegevenseigenaar, FAB, technisch uitvoerder, leverancier en beslisser; beheer van een extern portaal betekent geen beheer van het achterliggende platform. Een visual voert geen toegangswijziging, herverwerking of zorginhoudelijk besluit uit zonder het geldende proces.
1. Beschermde informatie: uitsluitend synthetische gegevens bij ontwerp en testen. Geen cliëntgegevens, BSN, medische gegevens, accounts, vertrouwelijke documenten of volledige logs in deelbare HTML. Ook applicatie-, account- en contactoverzichten kunnen vertrouwelijk zijn.
1. Toegankelijke alternatieven: kritieke informatie blijft bereikbaar zonder kleur, hover of complexe kaart. Toets toetsenbordbediening, mobiele weergave en een leesbare lijst of tabel. Continuïteitsinformatie krijgt een gecontroleerde offline of afdrukbare versie.
1. Geen tweede administratie: views verwijzen naar dezelfde wijziging, bevinding, eigenaar en bewijsbron. Hergebruik waar beschikbaar TOPdesk, Saar of de lokaal afgesproken registratie; deze systemen zijn geen verplichte afhankelijkheid. Acties en formele besluiten blijven in de bronregistratie. Vermijd ook een tweede adressen- of contractadministratie. Gedeelde voorbeeldreferenties zijn geen synchronisatie; gekopieerde samenvattingen hebben bron, versie en datum.

## Diagnose-, besluit- en definitielogica

- Oorzaakopsporing: antwoorden zijn aanwijzingen, geen automatische uitsluiting. Onbekend, gedateerd bewijs en meerdere mogelijke oorzaken blijven zichtbaar; herstel pas na bevestiging en met bevoegdheid.
- Besluitadvies: criteria, bevindingen, drempels, advies, samenvatting en export steunen op dezelfde gegevens en vastgestelde regels. Harde voorwaarden vóór weging; alleen toelaatbare opties rangschikken; onbevestigde aannames gemarkeerd. FAB onderzoekt, signaleert en adviseert; bevoegde rollen besluiten over toegang, zorgwerkwijze, livegang en restrisico.
- Rapportage- en kwaliteitsdefinities: leg teller, noemer, periode, populatie, uitsluitingen, peildatum en bronvelden vast. Geen totaalpercentage of score zonder afgesproken definitie; een geplande afspraak is niet hetzelfde als verleende zorg.
- Toegang: houd afgesproken modelrechten, feitelijke toegang en tijdelijke uitzonderingen apart. Maak team-/cliëntscope, noodzakelijkheid, goedkeuring, eindmoment en controle expliciet; een applicatieniveau of tijdvak bewijst geen effectieve toegang. Geen automatisch breder profiel of overnemen van rechten van een collega als standaardoplossing. Beoordeel noodtoegang volgens lokale afspraken; onderscheid in JML apparatuur, fysieke toegang en applicatierechten waar eindmomenten verschillen. Neem tijdelijke medewerkers, meerdere teamrollen en externe portalen mee als die lokaal voorkomen.
- Testdekking: verbind knelpunt → eis → inrichting → acceptatiecriterium met rol, scenario, test, omgeving, versie, uitkomst, bevinding, bewijscontrole en bevoegd akkoord. Neem negatieve autorisatie, foutscenario’s, dubbele aanbieding en terugval/herstel mee waar relevant. Een groen livegangcriterium of beheeracceptatie vervangt deze herleidbaarheid niet. Vergelijk configuratie, versies, koppelingen en testrollen per beschikbare omgeving; veronderstel geen aparte testomgeving bij ieder extern portaal.
- Keten- en gegevenskwaliteit: controleer inhoud, aantallen, actualiteit en eindverwerking naast technische ontvangst. Leg per kwaliteitsregel versie, eigenaar, gecontroleerde populatie, peildatum, afwijking, getroffen afnemers en veilige herstelroute vast. Houd overlappende afwijkingen apart om dubbeltelling te voorkomen; geen willekeurig totaalpercentage datakwaliteit. Herverwerking vraagt bevestiging en bevoegdheid en mag geen dubbele verwerking veroorzaken.
- Continuïteit en tijdelijke werkwijzen: leg getroffen zorgproces, toepassingsvoorwaarden, risico’s, bevoegde eigenaar, actuele contact-/escalatieroute, herbeoordeling en herstelcontroles vast. Verwijs naar het lokaal goedgekeurde noodplan; informatie moet ook zonder de getroffen applicatie bereikbaar zijn. Bij directe zorgimpact hoeft de analyse niet afgerond te zijn voordat het afgesproken continuïteitsproces start. Een afdruk of standalone HTML bewijst geen operationele bereikbaarheid.
- Bron-, adoptie- en pilotpatronen: maak de keten bron → lokale gevolgen → doelgroep → test/actie → eigenaar herleidbaar. Licht schalen, scores en informatiedichtheid toe; een ongemeten demo-index is geen betrouwbaarheidspercentage. Trainingdeelname bewijst geen vaardigheid of goede registratie. Leg voor pilots hypothese, scope, nulmeting, uitkomst, bijwerkingen en stopcriteria vast.

## Status en meerwaarde

- Houd vier statussen apart: aanwezig (het HTML-bestand bestaat), technisch getest, inhoudelijk beoordeeld en met gebruikers gevalideerd. Een vinkje betekent alleen dat het bestand er is.
- Toets meerwaarde met een kleine groep FAB’ers en relevante kerngebruikers/proceseigenaren op dezelfde taak tegen het bestaande hulpmiddel (checklist, ticket, kennisitem of documentatie), met realistische procescomplexiteit en synthetische gegevens. Vergelijk overlappende patronen op hetzelfde dossier; behoud beide alleen bij aantoonbaar nuttig verschil.
- Spreek succes- en stopcriteria vooraf af. Doorgaan vraagt minstens even juiste antwoorden, geen gemiste veiligheidskritieke informatie en aantoonbare verbetering van overzicht, uitvoering of overdracht. Stop of vereenvoudig als interactie vooral extra klikken of dubbele invoer oplevert, de bron niet actueel te houden is of het bestaande hulpmiddel even goed werkt.
- Meet juiste uitkomst, gemiste veiligheidsinformatie, zoektijd, juiste eigenaar, kwaliteit van overdracht en bewijs, voorbereiding, dubbele invoer, werk bij bronwijzigingen en herkenning van verouderde versies. Snelheid alleen volstaat niet; geen tijdwinstpercentages zonder basismetingen.
- Vóór praktijkgebruik blijven open toelatingsvoorwaarden: echte bronhouders en bevoegdheden aanwijzen en de registratie en versie-/geldigheidsbeheer bepalen; inhoud en diagnose-, bewijs-, besluit- en rapportageregels lokaal laten toetsen door bevoegde eigenaren; daarna praktijk- en volledige toegankelijkheidsvalidatie met gebruikers. Proceseigenaren en zorginhoudelijke deskundigen toetsen zorgprocessen en noodplannen; autorisatieverantwoordelijken toetsen toegang; rapportage-eigenaar en BI toetsen definities en berekeningen, FAB de bronregistraties. Toets gekozen apparaten, offline vindplaats en contactroute. Demo-afspraken zijn geen lokale zorgprotocollen; claim geen wettelijke naleving of leveranciersfunctionaliteit zonder verificatie.

## Wijzigingen

- Bewaar de zelfstandige HTML-opzet en de bestaande vormgeving; voeg geen afhankelijkheden of extra visuals toe zonder concrete taak.
- Houd bij toevoeging of verwijdering aantallen bestanden, concepten en kandidaten, beheerkaartjes, lokale links en leesbare alternatieven actueel. Elk concept heeft één checkbox; de twee incidentvarianten tellen als één concept. Vink alleen af zodra het HTML-bestand aanwezig is en beschrijf aanwezige interacties los van aanbevelingen. Test kritieke informatie ook zonder JavaScript en in afdrukmodus.
- Markeer fictieve onderzoeksclaims en ongemeten scores als demonstraties. Claim geen lokale goedkeuring, productierijpheid of gebruikerswaarde zonder bewijs.

## Templates gebruiken voor een bron

Er zijn twee werkstromen. **Bibliotheekonderhoud** wijzigt de prototypes onder `visuals/` en volgt alle ontwikkel-, inventaris- en verificatieafspraken hierboven. **Templategebruik** maakt een afzonderlijke brongebonden kopie; de originele HTML, conceptinventaris en voorbeeldcasussen blijven daarbij ongewijzigd. Een opdracht om een document, rapport of toestand te visualiseren autoriseert die kopie, geen herontwerp van de bibliotheek.

- Gebruik de projectskill [fab-html-template-reuse](.agents/skills/fab-html-template-reuse/SKILL.md). De [hergebruikgids](docs/template-reuse.md) is de centrale bron voor patroonkeuze, bewerkgrenzen, alle bestandskaarten en het uitgewerkte voorbeeld.
- Bepaal hoofdvraag, doelgroep, gebruiksmoment en bron vóór selectie. Bij bronpresentatie kan de bronhouder onbekend blijven als dit zichtbaar is; dat autoriseert geen operationele werkwijze of formeel besluit. Verzin geen bron, eigenaar, bewijs, akkoord of score om het patroon te vullen.
- Ontwerp en tests blijven synthetisch. Een brongebonden presentatie mag openbare of door de gebruiker geschoonde informatie bevatten. Vertrouwelijk materiaal vraagt een geschikte openbare of geschoonde bron; maak het niet stilzwijgend deelbaar. Deze uitzondering geldt voor presentatiekopieën, niet voor operationele vrijgave.
- Sla zonder opgegeven bestemming op onder `outputs/<document-slug>/index.html`. Deze map wordt door Git genegeerd en telt niet mee als prototype. Controleer bestaande uitvoer; kies bij een andere bestaande opdracht een unieke slug. Werk dezelfde uitvoer alleen bij als de opdracht daarop betrekking heeft. Een expliciete bestemming buiten deze map gaat voor; respecteer toepasselijke werkafspraken en schrijfbevoegdheden daar.
- Vervang brongebonden inhoud in HTML én JavaScript: titel, samenvatting, passages, verwijzingen, versie/peildatum, eigenaar, geldigheid, statussen, detailpanelen en exports. Werk aantallen, sleutels, routes, relaties en leesbare alternatieven samen bij. Houd bronfeiten, interpretatie, voorstel en onbekend uit elkaar; vermeld bronvindplaatsen en de beperkte scope van de visual.
- Bewaar vormgeving, zelfstandige werking, toetsenbordbediening, veilige tekstweergave en diagnose-/bewijs-/besluitvoorwaarden. Pas alleen in de kopie de noodzakelijke indeling aan aan hoeveelheid of structuur van de bron. Wijzig inhoudelijke reken- of beslisregels uitsluitend met expliciete brondefinities; ontbrekende grondslag betekent onbekend of geen berekening.
- Een gekopieerde visual mag niet afhankelijk zijn van de checkout: herstel lokale links inclusief fragmenten, verwijder irrelevante demoverwijzingen en bied kritieke inhoud statisch en afdrukbaar aan. Geen nieuwe runtime-afhankelijkheden. Publiceren, delen en formele acties vallen buiten templategebruik.
- Controleer de gegenereerde kopie zelf volgens de hergebruikgids. De bestaande pytest-suite ontdekt alleen `visuals/` en bewijst geen kwaliteit van `outputs/`. Lever bestand, gekozen patroon, bronstatus, werkelijk uitgevoerde controles en resterende grenzen op.

## Verificatie

De permanente pytest-browserregressies staan in `test/`; [test/README.md](test/README.md) beschrijft dekking, gerichte uitvoering en tijdelijke uitvoer. `pyproject.toml` definieert de ontwikkelafhankelijkheden en kwaliteitsinstellingen; `uv.lock` legt versies vast. De tooling voegt geen runtime-afhankelijkheid of buildstap aan de HTML toe.

Python 3.11 of hoger, uv en lokaal geïnstalleerd Google Chrome zijn vereist:

```sh
uv sync --locked
uv run --locked pytest
uv run --locked ruff check test
uv run --locked ruff format --check test
uv run --locked mdformat --check *.md test/README.md
uv run --locked djlint --check visuals/
```

Gebruik na installatie desgewenst `uv run --offline --locked pytest`. Werk dependencies bewust via `pyproject.toml` en `uv lock` bij; commit de lockfile samen met dependencywijzigingen. Er is geen Markdown-build of Python-distributie.

De tests gebruiken `sync_playwright()` en `chromium.launch(channel='chrome', headless=True)`, openen bestanden via `Path.as_uri()` en wachten op `networkidle`. Iedere test heeft een eigen browsercontext; onverwachte externe requests en JavaScript-fouten laten de test falen. De bekende Google Fonts-aanvraag van de algemene incidentpagina wordt geblokkeerd; die pagina wordt met lokale fallbackfonts getoetst. Screenshots en PDF’s gaan naar pytest-tijdelijke mappen. Gebruik `--basetemp` uitsluitend voor een aparte testmap, omdat pytest de bestaande inhoud verwijdert.

De tests ontdekken HTML recursief onder `visuals/`; `test/support.py` zoekt bestanden op unieke bestandsnaam. Een lege inventaris, dubbele bestandsnaam of ontbrekend gevraagd prototype geeft een fout. Gebruik deze centrale padresolver bij nieuwe tests.

Pas nieuwe tests aan de bestaande fixtures en scenario-indeling aan. Geen browserwerk tijdens module-import, absolute gebruikerspaden, vaste serverpoorten of ongecontroleerde CSS-experimenten in de tests. Test gedrag en veiligheidsvoorwaarden, niet historische tellingen of een vaste revisiedatum. Onderzoek falende assertions; verzwak geen inhoudelijke verwachting alleen om een groene run te krijgen. Sluit eigen browsercontexten en servers ook bij fouten.

Ruff controleert en formatteert Python; mdformat met GFM en frontmatter formatteert Markdown met behoud van YAML-metadata; djLint formatteert HTML met behoud van inline CSS/JavaScript. Voer na HTML-opmaak de browsertests uit en controleer bij visueel relevante wijzigingen de weergave. Gebruik voor formatterwijzigingen de commando’s in `test/README.md`. Voor aanvullende HTTP-tests kan `python3 -m http.server --bind 127.0.0.1 8765 --directory /absoluut/pad/naar/deze/map` dienen; stop alleen een server die je zelf hebt gestart.

Controleer JavaScript-fouten, unieke DOM-ID’s, lokale links inclusief fragmenten, documentbreedte bij 320 en 390 pixels, toetsenbordbediening van gewijzigde controles, afdrukbaarheid en kopieerfallbacks. Bij diagnose- en besluitviews: toets ontbrekend bewijs, afkeuring, herbeoordeling, drempels, niet-toelaatbare opties en overeenstemming tussen scherm en export. Controleer bij gewijzigde invoer ook veilige tekstweergave en reset; bij filters en tabs het behoud van toetsenbordfocus. Een afdruk mag meerdere pagina’s gebruiken; claim niet zonder controle dat de pagina op één A4 past. Leg vast welke bestanden, scenario’s en controles daadwerkelijk zijn getest en welke grenzen gelden. Tijdelijke diagnose-experimenten horen niet automatisch in de permanente suite; historische testclaims bewijzen geen actuele teststatus. Browserchecks zijn geen volledige toegankelijkheids-, beveiligings- of printaudit of gebruikersvalidatie.
