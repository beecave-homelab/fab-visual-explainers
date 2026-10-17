# Tests en kwaliteitscontroles

Deze map bevat lokale browserregressies voor de zelfstandige HTML-prototypes. De tijdelijke scripts zijn geselecteerd en herwerkt naar afzonderlijke pytest-scenario’s. Diagnose-experimenten en previewservers zijn niet opgenomen.

De inventaris wordt recursief uit `visuals/` opgebouwd via `scripts/visual_inventory.py`, dezelfde module die de bibliotheekingang gebruikt. Bestandslinks buiten de visualmap, kapotte links en directorylinks worden niet opgenomen. Alleen de bibliotheek mag leeg zijn; dubbele namen geven ook daar een fout (HTTP 500 of een CLI-fout zonder het opgeslagen overzicht te overschrijven). `support.py` biedt `visual_path()` voor het openen van een prototype op unieke bestandsnaam, ongeacht de categorie. Een lege inventaris, dubbele bestandsnaam of ontbrekend gevraagd bestand geeft een fout.

## Omgeving

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

## Gerichte uitvoering

```sh
uv run --locked pytest test/test_ketenkaart.py
uv run --locked pytest -k continuity
uv run --locked pytest --basetemp /tmp/fab-test-output
```

Gebruik voor `--basetemp` uitsluitend een aparte testmap: pytest verwijdert bestaande inhoud daarvan. Standaard beheert pytest tijdelijke uitvoer zelf. Screenshots en PDF’s horen niet in de repository.

## Dekking

`test_library.py` toetst de landingspagina: actuele ontdekking van toevoegingen en verwijderingen, dubbele namen en herstel daarna, beide CLI-startwijzen en behoud van uitvoer bij fouten, nieuwe categorieën, veilige metadata en bestandsroutes, inventarislinks, zoek- en categoriefilters, focusbehoud, nieuw tabblad, 320/390/768/1440 px, werking zonder JavaScript en volledige afdruk na filtering. HTTP-controles gebruiken een eigen tijdelijke server op een door het besturingssysteem toegewezen poort; de server wordt altijd gestopt.

`test_browser_selection.py` controleert browserkeuze, de begrensde fallback en het behouden van startfouten zonder een browser te starten.

`test_install_scripts.py` controleert de installatiescripts met tijdelijke checkouts en vervangende externe opdrachten. De tests toetsen uv-bootstrap, lockfilegebruik, paden met spaties, browserkeuze, opties en foutafhandeling. Ze downloaden geen pakketten en starten geen browser. Zie [ontwikkelomgeving installeren](../docs/installatie.md) voor de installatieopties.

| Bestand                       | Doel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `test_inventory.py`           | Recursieve ontdekking, lege inventaris, dubbele namen, gedeelde padregels voor bibliotheek/tests en ontbrekende gevraagde prototypes.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `test_applicatielandschap.py` | Vaste SVG-positionering tijdens hover, klikselectie en toetsenbordbediening van alle applicatieblokken.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `test_responsive.py`          | Alle prototypes op tien breedtes van 320 tot 2560 px: documentoverflow en titels; gerichte tekst- en overlapcontroles, kaartselectie na resize, lage viewport en incidentinformatie zonder JavaScript.                                                                                                                                                                                                                                                                                                                                                      |
| `test_pages.py`               | Alle aanwezige HTML: lokale links, unieke IDs, mobiele breedte, beheerinformatie; kritieke inhoud zonder JavaScript; afdruk, statisch register en clipboard van taakviews.                                                                                                                                                                                                                                                                                                                                                                                  |
| `test_review_logic.py`        | Diagnose, Go/No-Go, optiekeuze, rapportagedefinities, autorisatie, JML, impact en procesbevoegdheden.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `test_review_edges.py`        | Drempels, afkeuring, onbekende uitkomsten, toetsenbord en exportfallbacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `test_management.py`          | Beheeracceptatie, gewijzigde bewijsbron, afkeuring en reset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `test_task_views.py`          | Testbewijs, herbeoordeling, filterfocus, continuïteitsvoorwaarden, overlappende kwaliteitsafwijkingen, omgevingsverschillen en -veroudering, bekende fouten met voorwaarden, levenscyclus-startdata, escalatiepeilen met route- en pakketoverdracht, getoetste maatregelen en restrisicoacceptatie, en meetweken met stopcriteria en pilotadvies; lineage-vergelijkingen met verversing, plek en vervallen voorstel; releasepunten met inbak, doelgroepfilter en gewijzigde releasenotes; en adoptielagen met drempels, draagkracht en instructiewijziging. |
| `test_source_patterns.py`     | Volledige bronlijsten zonder JavaScript en in afdruk, inhoudspariteit per bronselectie, alle Vraagdossier-leesdieptes en bewijsdetails vanuit het bronregister, veilige bronbewerkingen zonder scriptmutatie, werkelijke zichtbaarheid van ingeklapte details, zoekresultaten en navigatie, bewijsdialoog en focus, selectiestatus, veilige brontekst en blijvende exporttekst bij clipboardweigering.                                                                                                                                                      |
| `test_ketenkaart.py`          | Routes, verstoring, toetsenbord, mobiele grenzen, afdruk, SVG-labels en vertraagde clipboardacties.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

Iedere test krijgt een eigen browsercontext. Externe HTTP(S)-requests worden geblokkeerd; onverwachte requests worden als fout gerapporteerd. De bekende Google Fonts-aanvraag van de algemene incidentpagina is een expliciete uitzondering op de foutmelding, maar wordt eveneens geblokkeerd zodat de lokale fallback wordt getoetst; JavaScript-fouten worden ook op aanvullende pagina’s bijgehouden. Browsercontexten worden na succes en fouten gesloten. De tests gebruiken synthetische gegevens en wijzigen geen HTML-bronbestand.

Behoud bewijslast: maak een falende controle niet groen door de verwachting te verzwakken. Onderzoek of de test een verouderde aanname bevat of dat de pagina een regressie heeft. Testuitvoering bewijst geen volledige toegankelijkheidsaudit, lokale inhoudelijke goedkeuring of gebruikerswaarde.

## Formatter- en lintcommando’s

```sh
uv run --locked ruff check test scripts
uv run --locked ruff format --check test scripts
uv run --locked mdformat --check *.md test/README.md
uv run --locked djlint --check visuals/ index.html
```

Opmaak bijwerken:

```sh
uv run --locked ruff check test scripts --fix
uv run --locked ruff format test scripts
uv run --locked mdformat *.md test/README.md
uv run --locked djlint --reformat visuals/ index.html
```

Ruff controleert Python, mdformat met GFM en frontmatter ondersteunt tabellen, checkboxes en YAML-metadata, djLint verzorgt HTML-opmaak. CSS en JavaScript binnen HTML worden niet door djLint geformatteerd. Voer na HTML-opmaak de browserregressies uit; formatterchecks beoordelen geen werking of visuele toegankelijkheid.
