# Codebase-overzicht

Dit document beschrijft de huidige code voor ontwikkelaars en coding agents. Lees [AGENTS.md](AGENTS.md) voor de geldende projectafspraken en [ontwikkelen en controleren](docs/ontwikkeling.md) voor de ontwikkelroute. De [README](README.md) is de ingang voor gebruikers.

## Projecttype en grenzen

FAB Visual Explainers is een statische bibliotheek met 32 zelfstandige HTML-prototypes voor 31 concepten. De twee incidentvarianten delen één concept. De primaire gebruikers zijn functioneel applicatiebeheerders die samenhang, gevolgen en bewijs willen verkennen of bespreken. De voorbeelden gebruiken synthetische gegevens; aanwezigheid of technische tests betekenen geen lokale inhoudelijke goedkeuring of gebruikersvalidatie.

De browser voert inline CSS en JavaScript uit. Er is geen backend, database, gedeelde JavaScript-module of HTML-buildstap. Python ondersteunt uitsluitend beheer en verificatie. `pyproject.toml` vereist Python 3.11 of hoger, heeft geen runtime-dependencies en schakelt packaging uit met `tool.uv.package = false`. De ontwikkelgroep bevat Playwright, pytest, Ruff, mdformat en djLint; `uv.lock` legt de versies vast.

## Repositorykaart

| Locatie                                   | Verantwoordelijkheid                                                                |
| ----------------------------------------- | ----------------------------------------------------------------------------------- |
| `index.html`                              | Landingspagina met opgeslagen catalogus, zoeken en categoriefilters.                |
| `visuals/`                                | Zelfstandige pagina's, verdeeld over zes taakcategorieën.                           |
| `scripts/visual_inventory.py`             | Gedeelde ontdekking van HTML en controle op unieke bestandsnamen.                   |
| `scripts/visual_library.py`               | Metadata uitlezen, catalogus renderen, lokale HTTP-server en generator.             |
| `scripts/package_template_skill.py`       | Hergebruikskill en guidance bundelen in een ZIP.                                    |
| `test/`                                   | Pytest-fixtures, inventaris- en scriptcontroles en browserregressies.               |
| `.agents/skills/fab-html-template-reuse/` | Instructies om een brongebonden presentatiekopie te maken.                          |
| `docs/`                                   | Beheer, ontwikkeling, hergebruik, ontwerpspecificaties en gedateerde reviews.       |
| `outputs/`                                | Git-genegeerde presentatiekopieën en skillpakketten; buiten de prototypeinventaris. |

`ideeen_voor_interactieve_fab_one_pagers.md` beschrijft concepten en kandidaten. De functiebeschrijving is het aangeleverde toetskader. Beide zijn inhoudelijke context, geen uitvoerbare configuratie.

## Ingangen en uitvoerpaden

### Een visual openen

Open `index.html` of een bestand onder `visuals/` rechtstreeks in de browser. De catalogus staat al in de HTML. Het inline script van `index.html` combineert zoektekst en gekozen categorie, verbergt niet-passende kaarten en werkt de resultaattelling bij. Het ontdekt geen bestanden op schijf. Zonder JavaScript blijven de opgeslagen links leesbaar; de afdrukstijl toont ook weggefilterde kaarten.

Ieder prototype beheert zijn eigen data, bediening, afdrukstijl en eventuele export. Er is geen gedeeld applicatiemodel dat veranderingen automatisch naar andere prototypes doorzet. Lokale links vereisen dat de mapstructuur behouden blijft.

Een concreet diagnosepad staat in `visuals/incident_en_continuiteit/fab-oorzaakopsporing.html`:

1. De inline lijsten `H` en `C` definiëren hypothesen en controles. Antwoorden, bewijs, beoordelingen en selectie staan in JavaScript-geheugen.
1. Antwoordknoppen wijzigen die toestand. `state()` verzamelt aanwijzingen en kiest de volgende onbeantwoorde controle op geschatte duur; antwoorden sluiten geen hypothese automatisch uit.
1. `render()` werkt de tabel, het detailpaneel en de hypotheselijst bij. Een expliciete beoordeling vraagt bron/versie, controledatum en beoordelaar. Gewijzigd bewijs maakt eerdere beoordelingen ongeldig.
1. `note()` maakt de export uit dezelfde toestand. Kopiëren gebruikt de Clipboard API en biedt bij weigering tekst om zelf te kopiëren. Herladen verliest de invoer; er wordt geen ticket of herstelactie uitgevoerd.

Dit beschrijft die pagina; andere prototypes hebben eigen regels en toestand. Wijzig diagnose- of besluitlogica altijd samen met bewijsweergave, export en relevante scenario's.

### Catalogus genereren of serveren

`python3 scripts/visual_library.py --generate` volgt dit pad:

1. `discover_visuals()` uit `visual_inventory.py` zoekt recursief naar `*.html` onder `visuals/`. Bestandslinks buiten de map worden genegeerd; dubbele bestandsnamen geven `InventoryError`. De tests weigeren ook een lege inventaris; de catalogus mag die tonen.
1. `discover()` leest tekstmetadata via `Metadata`, zonder bron-JavaScript uit te voeren. Beschrijvingen komen uit de description-meta, met inleiding of hoofdkop als terugval. De tests eisen voor ieder bestaand prototype precies één inhoudelijke description-meta.
1. `render_catalog()` groepeert kaarten per categorie, sorteert op titel en escapet tekst en attributen. Onbekende categorieën krijgen een afgeleid label.
1. `render_index()` vervangt uitsluitend het blok tussen `catalog:start` en `catalog:end` in `index.html`. `--generate` schrijft het resultaat naar dat bestand. Een inventarisfout stopt vóór schrijven.

Zonder `--generate` start hetzelfde script `ThreadingHTTPServer` op `127.0.0.1:8765`; `--port` kiest een andere poort. `LibraryHandler` rendert de ingang opnieuw bij iedere request, zonder `index.html` op schijf te wijzigen. Het serveert daarnaast uitsluitend bestaande `.html`-bestanden binnen `visuals/`, geen directorylisting of overige checkoutbestanden. Antwoorden krijgen `Cache-Control: no-store`; een dubbele naam geeft voor de ingang HTTP 500. `Ctrl+C` sluit de server.

De server biedt geen schrijf-API, authenticatie of registratiesynchronisatie. Hij is een lokaal hulpmiddel voor de bibliotheek. Zie [bibliotheek beheren](docs/bibliotheek-beheren.md) voor gebruik.

### Een overdraagbare skill bundelen

`python3 scripts/package_template_skill.py` leest de projectskill, `AGENTS.md` en `docs/template-reuse.md`. `build_package()` herschrijft relatieve Markdown-links buiten codevoorbeelden: gebundelde bronnen blijven lokaal bereikbaar, overige repositorylinks krijgen een openbare URL. Het pakket bevat ook bronpaden en SHA-256-hashes in `references/provenance.json`.

De uitvoer is standaard `outputs/skill-packages/fab-html-template-reuse.zip`; `--output` kiest een andere bestemming en een bestaand bestand wordt vervangen. Gesorteerde inhoud, vaste ZIP-tijdstempels en rechten maken dezelfde invoer reproduceerbaar. Dit proces haalt geen templates op en bundelt geen visuals. Het gebruik van de skill buiten de checkout heeft eigen bronroutes; zie de [hergebruikgids](docs/template-reuse.md).

## Ontwikkelomgeving en configuratie

De HTML vereist een browser, geen Python-installatie of externe dienst. De algemene incidentpagina verwijst naar Google Fonts; de browsertests blokkeren die aanvraag en controleren met lokale fallbackfonts. Behandel zelfstandig openen daarom niet als bewijs dat ieder prototype volledig zonder netwerk is getest.

De repository bevat daarnaast `install.sh` en `install-dependencies.sh`. Deze Bash-scripts richten een ontwikkelomgeving in via `uv sync --locked` en installeren standaard Playwright headless Chromium. `install.sh` controleert daarna imports en een browserstart, maar voert geen regressiesuite uit. Opties voor uv-installatie, Linux-systeembibliotheken en het overslaan van de browser staan in [de installatiegids](docs/installatie.md). De scripts zijn ontwikkelhulpmiddelen, geen runtime voor de HTML.

| Instelling                    | Toepassing                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------- |
| `pyproject.toml` en `uv.lock` | Python-versiegrens, ontwikkeltools, pytest-, Ruff- en djLint-instellingen.                  |
| `UV_CACHE_DIR`                | Cachepad voor uv, bijvoorbeeld in een beperkte taakomgeving.                                |
| `PLAYWRIGHT_BROWSERS_PATH`    | Browserinstallatiepad; gebruik dezelfde waarde bij installatie en tests.                    |
| `UV_INSTALL_DIR`              | Installatiepad voor uv bij `--install-uv`; standaard `~/.local/bin`.                        |
| `--browser-channel`           | Pytest-browserkeuze: `auto`, `chrome` of `chromium`, geïmplementeerd in `test/conftest.py`. |

Er is geen applicatieconfiguratiebestand, geheimenconfiguratie, containerlaag of CI-workflow in deze checkout aangetroffen. De lokale tooling bepaalt zijn repositorypad vanuit het scriptbestand. De optionele server bindt uitsluitend aan loopback. De eerste toolinstallatie vraagt netwerk; de HTML zelf heeft geen pakketinstallatie nodig.

## Verificatie en onderhoud

Start vanuit de hoofdmap. De vastgelegde afhankelijkheden kunnen met `uv sync --locked` worden gesynchroniseerd. Voor browsertests moet de bijbehorende Chromium-testbrowser geïnstalleerd zijn, bijvoorbeeld met `uv run --locked playwright install chromium --only-shell`.

```sh
uv run --locked pytest --browser-channel chromium
uv run --locked ruff check test scripts
uv run --locked ruff format --check test scripts
uv run --locked mdformat --check project-overview.md
uv run --locked djlint --check visuals/ index.html
```

De standaard `auto`-keuze in de fixture probeert Chrome en valt alleen bij een ontbrekende Chrome-distributie terug op Playwright Chromium. `--browser-channel chromium` kiest de beheerde testbrowser expliciet. Volg daarnaast de uitvoeringsafspraken van de testomgeving; een startfout is geen geslaagde test.

`test/support.py` gebruikt dezelfde inventaris als de server en zoekt prototypes op unieke bestandsnaam. `test/conftest.py` start één browser per sessie en geeft tests eigen contexten. Onverwachte externe HTTP(S)-requests en JavaScript-fouten laten de betrokken test falen; contexten worden ook bij fouten gesloten. Screenshots en PDF's gaan naar pytest-tijdelijke mappen.

De [testinventaris](test/README.md) beschrijft de scenario's; [TESTING.md](TESTING.md) bevat de uitvoeringscommando's. Er zijn browsercontroles voor onder meer mobiele breedte, toetsenbord, ontbrekend bewijs, herbeoordeling, exports, geen JavaScript en afdruk. Inventaris en skillverpakking hebben ook controles zonder browser. Er is geen afzonderlijke typecheck- of coverage-opdracht geconfigureerd in `pyproject.toml`. Een geslaagde gerichte run bewijst geen volledige suite of gebruikersvalidatie.

Werk bij iedere wijziging `CHANGELOG.md` bij. Alleen onderhoud aan documentatie vraagt geen productversiestijging. HTML-wijzigingen vragen wel een hogere SemVer in `pyproject.toml` en `uv.lock`, plus een gedateerde changelogsectie. `scripts/check_release_version.py --base github/main --head HEAD` controleert de gecommitteerde wijziging vanaf de merge-base; zie [releases voorbereiden](docs/releases.md). Er is geen automatische releaseworkflow.

Houd bij bibliotheekwijzigingen metadata, lokale links en inventaris samen actueel; genereer daarna het opgeslagen overzicht opnieuw. Brongebonden presentaties horen afzonderlijk onder `outputs/<document-slug>/index.html` en vragen eigen verificatie: de prototypeontdekking omvat ze niet. Acties en formele besluiten blijven in de afgesproken bronregistratie; demo-invoer maakt daarvan geen tweede administratie.

## Documentatiekaart

- [README](README.md): downloaden, openen en gebruiken.
- [AGENTS.md](AGENTS.md): centrale ontwikkel-, inhouds- en verificatieafspraken.
- [Ontwikkelen en controleren](docs/ontwikkeling.md): setup en kwaliteitscommando's.
- [Bibliotheek beheren](docs/bibliotheek-beheren.md): server, metadata en catalogus bijwerken.
- [Installatie](docs/installatie.md): installatiescripts en omgevingsopties.
- [Testuitvoering](TESTING.md): browserkeuze, commando's en testgrenzen.
- [Testinventaris](test/README.md): beschikbare scenario's.
- [Releases](docs/releases.md) en [changelog](CHANGELOG.md): versiebeleid en wijzigingshistorie.
- [Hergebruikgids](docs/template-reuse.md): patroonkeuze, presentatiekopieën en overdraagbare skill.
- [Ideeënnotitie](ideeen_voor_interactieve_fab_one_pagers.md): inventaris en inhoudelijke werkvoorraad.

Gedateerde ontwerpspecificaties en reviews onder `docs/` beschrijven hun eigen beoordelingsmoment. Ze zijn geen bewijs voor de huidige teststatus en vervangen de uitvoerbare code of centrale projectafspraken niet.
