# Tests en kwaliteitscontroles

Deze map bevat lokale browserregressies voor de zelfstandige HTML-prototypes. De tijdelijke scripts zijn geselecteerd en herwerkt naar afzonderlijke pytest-scenario’s. Diagnose-experimenten en previewservers zijn niet opgenomen.

De inventaris wordt recursief uit `visuals/` opgebouwd. `support.py` biedt `visual_path()` voor het openen van een prototype op unieke bestandsnaam, ongeacht de categorie. Een lege inventaris, dubbele bestandsnaam of ontbrekend gevraagd bestand geeft een fout.

## Omgeving

Python 3.11 of hoger, uv en lokaal geïnstalleerd Google Chrome zijn nodig. `pyproject.toml` definieert de ontwikkelafhankelijkheden; `uv.lock` legt de opgeloste versies vast. Er is geen Python-applicatiepakket of buildstap voor de HTML.

```sh
uv sync --locked
uv run --locked pytest
```

De eerste installatie kan netwerktoegang nodig hebben. Na installatie kan `uv run --offline --locked pytest` worden gebruikt. Ontbrekend Chrome of ontbrekende dependencies zijn fouten, geen stilzwijgend overgeslagen tests.

## Gerichte uitvoering

```sh
uv run --locked pytest test/test_ketenkaart.py
uv run --locked pytest -k continuity
uv run --locked pytest --basetemp /tmp/fab-test-output
```

Gebruik voor `--basetemp` uitsluitend een aparte testmap: pytest verwijdert bestaande inhoud daarvan. Standaard beheert pytest tijdelijke uitvoer zelf. Screenshots en PDF’s horen niet in de repository.

## Dekking

`test_library.py` toetst de landingspagina: actuele ontdekking van toevoegingen en verwijderingen, nieuwe categorieën, veilige metadata en bestandsroutes, inventarislinks, zoek- en categoriefilters, focusbehoud, nieuw tabblad, 320/390/768/1440 px, werking zonder JavaScript en volledige afdruk na filtering. HTTP-controles gebruiken een eigen tijdelijke server op een door het besturingssysteem toegewezen poort; de server wordt altijd gestopt.

| Bestand                       | Doel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `test_inventory.py`           | Recursieve ontdekking, lege inventaris, dubbele namen en ontbrekende gevraagde prototypes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `test_applicatielandschap.py` | Vaste SVG-positionering tijdens hover, klikselectie en toetsenbordbediening van alle applicatieblokken.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `test_responsive.py`          | Alle prototypes op tien breedtes van 320 tot 2560 px: documentoverflow en titels; gerichte tekst- en overlapcontroles, kaartselectie na resize, lage viewport en incidentinformatie zonder JavaScript.                                                                                                                                                                                                                                                                                                                                                      |
| `test_pages.py`               | Alle aanwezige HTML: lokale links, unieke IDs, mobiele breedte, beheerinformatie; kritieke inhoud zonder JavaScript; afdruk, statisch register en clipboard van taakviews.                                                                                                                                                                                                                                                                                                                                                                                  |
| `test_review_logic.py`        | Diagnose, Go/No-Go, optiekeuze, rapportagedefinities, autorisatie, JML, impact en procesbevoegdheden.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `test_review_edges.py`        | Drempels, afkeuring, onbekende uitkomsten, toetsenbord en exportfallbacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `test_management.py`          | Beheeracceptatie, gewijzigde bewijsbron, afkeuring en reset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `test_task_views.py`          | Testbewijs, herbeoordeling, filterfocus, continuïteitsvoorwaarden, overlappende kwaliteitsafwijkingen, omgevingsverschillen en -veroudering, bekende fouten met voorwaarden, levenscyclus-startdata, escalatiepeilen met route- en pakketoverdracht, getoetste maatregelen en restrisicoacceptatie, en meetweken met stopcriteria en pilotadvies; lineage-vergelijkingen met verversing, plek en vervallen voorstel; releasepunten met inbak, doelgroepfilter en gewijzigde releasenotes; en adoptielagen met drempels, draagkracht en instructiewijziging. |
| `test_source_patterns.py`     | Volledige bronlijsten zonder JavaScript en in afdruk, inhoudspariteit per bronselectie, werkelijke zichtbaarheid van ingeklapte details, zoekresultaten en navigatie, bewijsdialoog en focus, selectiestatus, veilige brontekst en blijvende exporttekst bij clipboardweigering.                                                                                                                                                                                                                                                                            |
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
