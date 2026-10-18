# FAB Visual Explainers

Interactieve voorbeelden voor functioneel applicatiebeheerders. Bekijk hoe een incident samenhangt met een zorgproces, welke gevolgen een wijziging heeft of waar een gegeven in de keten wordt gebruikt. Je kiest een onderdeel en kunt daarna de bijbehorende relaties, details en bewijsinformatie bekijken.

De bibliotheek is bedoeld om werkwijzen te verkennen en te bespreken met collega's, kerngebruikers en proceseigenaren. De voorbeelden bevatten synthetische gegevens en zijn niet vrijgegeven voor operationeel gebruik.

## Beginnen

Je hoeft niets te installeren om de voorbeelden te bekijken.

1. [Download de bibliotheek als ZIP](https://github.com/beecave-homelab/fab-visual-explainers/archive/refs/heads/main.zip).
1. Pak de ZIP volledig uit en behoud de mapstructuur.
1. Open `index.html` in je browser.
1. Zoek op een onderwerp of kies een categorie. Open vervolgens een visual in een nieuw tabblad.

Je kunt ook een afzonderlijk HTML-bestand uit `visuals/` openen. Bewaar de hele bibliotheek als je de verwijzingen naar andere voorbeelden wilt kunnen volgen.

## Welk voorbeeld past bij je vraag?

De bibliotheek bevat 32 visuals voor 31 concepten. De twee incidentvarianten tonen dezelfde inhoud in een andere vormgeving.

- Onderzoek een verstoring met het [Incidentoverzicht](visuals/incident_en_continuiteit/incident-onepager.html), [Oorzaakopsporing](visuals/incident_en_continuiteit/fab-oorzaakopsporing.html) of de [Continuïteitskaart](visuals/incident_en_continuiteit/fab-continuiteitskaart.html).
- Bekijk de gevolgen van een wijziging en de benodigde tests met de [Change Impact Map](visuals/wijziging_en_acceptatie/fab-change-impact-map.html) of [Test Coverage Map](visuals/wijziging_en_acceptatie/fab-test-coverage-map.html).
- Verken welke applicaties een proces ondersteunen met het [Applicatielandschap](visuals/landschap_en_processen/fab-applicatielandschap.html) of de [Proces × Applicatie-map](visuals/landschap_en_processen/fab-proces-applicatie-map.html).
- Bekijk toegangsrechten en rolwisselingen met het [Autorisatielandschap](visuals/toegang/fab-autorisatielandschap.html) of [Joiner-Mover-Leaver](visuals/toegang/fab-joiner-mover-leaver.html).
- Volg gegevens en onderzoek afwijkingen met de [Ketenkaart](visuals/gegevens_en_ketens/fab-ketenkaart.html) of [Data Quality Map](visuals/gegevens_en_ketens/fab-data-quality-map.html).
- Onderzoek een document of onderbouw een antwoord met [BronScanner](visuals/bronnen_en_kennis/bron-scanner.html) of [Vraagdossier](visuals/bronnen_en_kennis/vraagdossier.html).

Deze links tonen op GitHub de broncode. Open de bestanden uit de uitgepakte ZIP om de visuals te gebruiken. In `index.html` vind je alle voorbeelden met een korte beschrijving.

## Een visual gebruiken in overleg

Kies een voorbeeld dat past bij de vraag die je wilt bespreken. Bekijk eerst het overzicht en kies daarna een onderdeel om relaties en details te onderzoeken. Controleer bij een status of conclusie ook de bron, open vragen en bewijsinformatie.

Gebruik de voorbeelden om te bespreken welke informatie jullie nodig hebben en wie daarover gaat. Een groene status in een demonstratie is geen akkoord voor een echte wijziging, toegang of noodwerkwijze. Voor praktijkgebruik moeten bevoegde eigenaren de inhoud en regels lokaal toetsen. Ook gebruikerstests en een volledige toegankelijkheidscontrole blijven nodig.

## Je eigen document visualiseren

Je kunt een bestaand patroon gebruiken voor een openbaar rapport of een document waaruit vertrouwelijke informatie is verwijderd. De [hergebruikgids](docs/template-reuse.md) helpt je kiezen welk patroon bij je bron en hoofdvraag past.

Werk je met een AI-agent die skills ondersteunt? Gebruik dan de projectskill [fab-html-template-reuse](.agents/skills/fab-html-template-reuse/SKILL.md), bijvoorbeeld met deze opdracht:

> Gebruik $fab-html-template-reuse om dit openbare rapport voor functioneel applicatiebeheerders te visualiseren. Laat zien welke passages het antwoord op mijn vraag onderbouwen en welke vragen openblijven.

De skill maakt een afzonderlijke kopie. De oorspronkelijke voorbeelden blijven behouden. Binnen deze repository komt het resultaat standaard in `outputs/<document-slug>/index.html`. Een eigen presentatie is daarmee nog niet gepubliceerd of goedgekeurd voor praktijkgebruik.

Gebruik geen cliëntgegevens, accounts, volledige logs of vertrouwelijke documenten in deelbare HTML.

## Verder lezen

- [HTML-templates hergebruiken](docs/template-reuse.md) voor patroonkeuze en het aanpassen van een kopie.
- [Bibliotheek beheren](docs/bibliotheek-beheren.md) voor de lokale server en het bijwerken van het overzicht.
- [Ontwikkelen en controleren](docs/ontwikkeling.md) voor ontwikkelaars en bijdragers.
- [Testen en kwaliteitscontroles](TESTING.md) voor de testomgeving en uitvoering.

## Licentie

De code is beschikbaar onder de [MIT-licentie](LICENSE).
