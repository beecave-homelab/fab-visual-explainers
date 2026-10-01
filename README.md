# FAB HTML-visuals

Zelfstandige HTML-prototypes voor functioneel applicatiebeheer. Open een HTML-bestand rechtstreeks in de browser; er is geen backend of buildstap. De voorbeelden zijn synthetisch en niet vrijgegeven voor operationeel gebruik.

[AGENTS.md](AGENTS.md) bevat de projectafspraken. De [ideeënnotitie](Ideee%CC%88n%20voor%20interactieve%20FAB%20one-pagers.md) beschrijft concepten en actuele status.

## Ontwikkelen en controleren

Gebruik Python 3.11 of hoger, uv en lokaal Google Chrome:

```sh
uv sync --locked
uv run --locked pytest
uv run --locked ruff check test
uv run --locked ruff format --check test
uv run --locked mdformat --check *.md test/README.md
uv run --locked djlint --check *.html
```

Dependencies en instellingen staan in `pyproject.toml`; versies zijn vastgelegd in `uv.lock`. Zie [test/README.md](test/README.md) voor gerichte tests, formattercommando’s, uitvoerbestanden en de grenzen van deze controles.
