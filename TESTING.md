# Testen en kwaliteitscontroles

Dit document beschrijft hoe je de tests en kwaliteitscontroles uitvoert. De [testinventaris](test/README.md) beschrijft welke scenario's er zijn en wat ze controleren. Voer de opdrachten hieronder uit vanuit de hoofdmap van de repository.

## Omgeving

Voor automatische inrichting kun je [de installatiescripts](docs/installatie.md) gebruiken. De setup controleert de tools en browser, maar voert de regressiesuite niet uit.

Python 3.11 of hoger, uv en Google Chrome of de bij Playwright passende Chromium-installatie zijn nodig. `pyproject.toml` definieert de ontwikkelafhankelijkheden; `uv.lock` legt de opgeloste versies vast. Er is geen Python-applicatiepakket of buildstap voor de HTML.

```sh
uv sync --locked
uv run --locked pytest
```

De eerste installatie kan netwerktoegang nodig hebben. Na installatie kan `uv run --offline --locked pytest` worden gebruikt. Standaard (`--browser-channel auto`) gebruikt de suite lokaal Chrome. Alleen wanneer die distributie ontbreekt, probeert zij Playwright Chromium. De uitvoer meldt de gebruikte browser en versie; crashes, permissiefouten en ontbrekend Chromium blijven fouten. Er worden geen tests overgeslagen of assertions aangepast en tijdens pytest wordt niets geïnstalleerd.

Voor een review-host zonder Chrome, of een expliciete browservergelijking:

```sh
uv run --locked playwright install chromium
uv run --locked pytest --browser-channel chromium
uv run --locked pytest --browser-channel chrome
```

De laatste opdracht vereist Chrome en valt nooit terug. Chromium en Chrome kunnen door browserversie, fonts en besturingssysteem verschillende layoutuitkomsten geven. Een fallback maakt zulke failures niet automatisch omgevingsgebonden: reproduceer ze op dezelfde browser met de basisversie van de betrokken bestanden. Ontbrekende dependencies blijven fouten.

Volg daarnaast de uitvoeringsafspraken voor de machine waarop je test. Een startfout door de processandbox blijft een omgevingsfout.

## Gerichte uitvoering

```sh
uv run --locked pytest test/test_ketenkaart.py
uv run --locked pytest -k continuity
uv run --locked pytest --basetemp /tmp/fab-test-output
```

Gebruik voor `--basetemp` uitsluitend een aparte testmap: pytest verwijdert bestaande inhoud daarvan. Standaard beheert pytest tijdelijke uitvoer zelf. Screenshots en PDF's horen niet in de repository.

## Uitvoeringsvoorwaarden

Iedere test krijgt een eigen browsercontext. Externe HTTP(S)-requests worden geblokkeerd; onverwachte requests worden als fout gerapporteerd. De bekende Google Fonts-aanvraag van de algemene incidentpagina is een expliciete uitzondering op de foutmelding, maar wordt eveneens geblokkeerd zodat de lokale fallback wordt getoetst; JavaScript-fouten worden ook op aanvullende pagina's bijgehouden. Browsercontexten worden na succes en fouten gesloten. De tests gebruiken synthetische gegevens en wijzigen geen HTML-bronbestand.

Behoud bewijslast: maak een falende controle niet groen door de verwachting te verzwakken. Onderzoek of de test een verouderde aanname bevat of dat de pagina een regressie heeft. Testuitvoering bewijst geen volledige toegankelijkheidsaudit, lokale inhoudelijke goedkeuring of gebruikerswaarde.

## Formatter- en lintcommando's

```sh
uv run --locked ruff check test scripts
uv run --locked ruff format --check test scripts
uv run --locked mdformat --check *.md test/README.md docs
uv run --locked djlint --check visuals/ index.html
```

Opmaak bijwerken:

```sh
uv run --locked ruff check test scripts --fix
uv run --locked ruff format test scripts
uv run --locked mdformat *.md test/README.md docs
uv run --locked djlint --reformat visuals/ index.html
```

Ruff controleert Python, mdformat met GFM en frontmatter ondersteunt tabellen, checkboxes en YAML-metadata, djLint verzorgt HTML-opmaak. CSS en JavaScript binnen HTML worden niet door djLint geformatteerd. Voer na HTML-opmaak de browserregressies uit; formatterchecks beoordelen geen werking of visuele toegankelijkheid.
