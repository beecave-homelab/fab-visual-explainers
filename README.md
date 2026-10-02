# FAB HTML-visuals

Zelfstandige HTML-prototypes voor functioneel applicatiebeheer. Open een HTML-bestand rechtstreeks in de browser; er is geen backend of buildstap. De voorbeelden zijn synthetisch en niet vrijgegeven voor operationeel gebruik.

[AGENTS.md](AGENTS.md) bevat de projectafspraken. De [ideeënnotitie](ideeen_voor_interactieve_fab_one_pagers.md) beschrijft concepten en actuele status.

## Een document, rapport of toestand visualiseren

Gebruik de projectskill [fab-html-template-reuse](.agents/skills/fab-html-template-reuse/SKILL.md), bijvoorbeeld: “Gebruik $fab-html-template-reuse om dit openbare rapport voor FAB te visualiseren.” De [hergebruikgids](docs/template-reuse.md) helpt het patroon kiezen en geeft per HTML-bestand aan wat samen moet worden aangepast en behouden.

De skill leest templates uit deze checkout en maakt een brongebonden kopie. Zonder opgegeven bestemming komt die in `outputs/<document-slug>/index.html`; `outputs/` wordt door Git genegeerd en staat buiten de prototypeinventaris. De skill is projectlokaal, niet persoonlijk geïnstalleerd. Openbare of geschoonde broninformatie is toegestaan in presentatiekopieën; bibliotheekontwerp en tests blijven synthetisch. Zie [de twee werkstromen](AGENTS.md#templates-gebruiken-voor-een-bron) voor de grenzen.

## Indeling

De prototypes staan onder `visuals/`, ingedeeld naar hoofdtaak. Ieder bestand heeft één vaste plek; relaties tussen categorieën blijven via relatieve links bereikbaar. De bestaande HTML-bestandsnamen blijven behouden.

| Map onder `visuals/`        | HTML-bestanden |
| --------------------------- | -------------- |
| `incident_en_continuiteit/` | 5              |
| `wijziging_en_acceptatie/`  | 6              |
| `landschap_en_processen/`   | 2              |
| `toegang/`                  | 2              |
| `gegevens_en_ketens/`       | 3              |
| `bronnen_en_kennis/`        | 5              |

De ideeënnotitie bevat links naar alle prototypes. Documentatie en configuratie staan in de root; regressietests staan in `test/`.

## Ontwikkelen en controleren

Gebruik Python 3.11 of hoger, uv en lokaal Google Chrome:

```sh
uv sync --locked
uv run --locked pytest
uv run --locked ruff check test
uv run --locked ruff format --check test
uv run --locked mdformat --check *.md test/README.md
uv run --locked djlint --check visuals/
```

Dependencies en instellingen staan in `pyproject.toml`; versies zijn vastgelegd in `uv.lock`. Zie [test/README.md](test/README.md) voor gerichte tests, formattercommando’s, uitvoerbestanden en de grenzen van deze controles.
