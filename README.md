# FAB HTML-visuals

Zelfstandige HTML-prototypes voor functioneel applicatiebeheer. Open een HTML-bestand rechtstreeks in de browser; er is geen backend of buildstap. De voorbeelden zijn synthetisch en niet vrijgegeven voor operationeel gebruik.

[AGENTS.md](AGENTS.md) bevat de projectafspraken. De [ideeënnotitie](ideeen_voor_interactieve_fab_one_pagers.md) beschrijft concepten en actuele status.

## Alle visuals bekijken

De [landingspagina](index.html) geeft een doorzoekbaar overzicht per onderwerp. Elke visual opent in een nieuw tabblad. De pagina staat buiten `visuals/` en telt niet als extra prototype.

Start de lokale bibliotheek vanuit deze map om nieuwe visuals automatisch te laten opnemen:

```sh
python3 scripts/visual_library.py
```

Open daarna [de lokale bibliotheek](http://127.0.0.1:8765/). De server leest bij iedere paginalading alle `.html`-bestanden onder `visuals/`, inclusief submappen en nieuwe categorieën. Voeg een bestand toe, verwijder of verplaats het, en ververs het overzicht. Namen komen uit de HTML-titel; beschrijvingen uit `<meta name="description" content="…">` in ieder HTML-bestand. Geef nieuwe visuals hierin een korte toelichting op wat je kunt bekijken of onderzoeken. Ontbreekt die metadata, dan gebruikt het overzicht de eerste bruikbare inleiding na de hoofdkop, en anders de hoofdkop zelf. Er is geen aparte bestandslijst om bij te houden. De twee incidentvarianten hebben een eigen ingang.

De server gebruikt alleen de Python-standaardbibliotheek, luistert uitsluitend lokaal en serveert de landingspagina en HTML onder `visuals/`. Stop met `Ctrl+C`. Gebruik bij een bezette poort bijvoorbeeld `python3 scripts/visual_library.py --port 8766` en open de URL die het script toont. De prototypes blijven zelfstandig te openen; deze server is een optionele bladerhulp.

`index.html` kan ook rechtstreeks worden geopend, met zoeken, filters en alle opgeslagen links. Die kopie ontdekt geen nieuwe bestanden vanuit de browser. Werk het opgeslagen overzicht na bibliotheekwijzigingen bij met:

```sh
python3 scripts/visual_library.py --generate
```

De HTML tussen `catalog:start` en `catalog:end` is gegenereerd; pas vormgeving en interactie erbuiten aan. Alle links blijven zonder JavaScript beschikbaar. Afdrukken toont de volledige bibliotheek, ook wanneer een zoekfilter actief is.

## Een document, rapport of toestand visualiseren

Gebruik de projectskill [fab-html-template-reuse](.agents/skills/fab-html-template-reuse/SKILL.md), bijvoorbeeld: “Gebruik $fab-html-template-reuse om dit openbare rapport voor FAB te visualiseren.” De [hergebruikgids](docs/template-reuse.md) helpt het patroon kiezen en geeft per HTML-bestand aan wat samen moet worden aangepast en behouden.

De skill leest templates uit deze checkout en maakt een brongebonden kopie. Zonder opgegeven bestemming komt die in `outputs/<document-slug>/index.html`; `outputs/` wordt door Git genegeerd en staat buiten de prototypeinventaris. De skill is projectlokaal, niet persoonlijk geïnstalleerd. Openbare of geschoonde broninformatie is toegestaan in presentatiekopieën; bibliotheekontwerp en tests blijven synthetisch. Zie [de twee werkstromen](AGENTS.md#templates-gebruiken-voor-een-bron) voor de grenzen.

## Indeling

De prototypes staan onder `visuals/`, ingedeeld naar hoofdtaak. Ieder bestand heeft één vaste plek; relaties tussen categorieën blijven via relatieve links bereikbaar. De bestaande HTML-bestandsnamen blijven behouden.

| Map onder `visuals/`        | HTML-bestanden |
| --------------------------- | -------------- |
| `incident_en_continuiteit/` | 7              |
| `wijziging_en_acceptatie/`  | 11             |
| `landschap_en_processen/`   | 3              |
| `toegang/`                  | 2              |
| `gegevens_en_ketens/`       | 4              |
| `bronnen_en_kennis/`        | 5              |

De bibliotheek bevat 32 HTML-bestanden voor 31 concepten; de twee incidentvarianten tellen als één concept. De [visuele review van 4 oktober 2026](docs/visual-review-2026-10-04.md) beschrijft sterke punten, verbeteringen en resterende grenzen per prototype.

De ideeënnotitie bevat links naar alle prototypes. Documentatie en configuratie staan in de root; regressietests staan in `test/`.

## Ontwikkelen en controleren

Gebruik Python 3.11 of hoger, uv en lokaal Google Chrome:

```sh
uv sync --locked
uv run --locked pytest
uv run --locked ruff check test scripts
uv run --locked ruff format --check test scripts
uv run --locked mdformat --check *.md test/README.md
uv run --locked djlint --check visuals/ index.html
```

Dependencies en instellingen staan in `pyproject.toml`; versies zijn vastgelegd in `uv.lock`. Zie [test/README.md](test/README.md) voor gerichte tests, formattercommando’s, uitvoerbestanden en de grenzen van deze controles.
