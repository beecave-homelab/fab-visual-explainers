# Ontwikkelomgeving installeren

Gebruik Bash op macOS of Linux. Op Windows kun je de scripts vanuit WSL gebruiken. De scripts richten de ontwikkelomgeving in met Python 3.11 of hoger en uv. Voor het bekijken van de HTML-voorbeelden heb je deze installatie niet nodig.

Start vanuit de hoofdmap:

```sh
./install.sh
```

Dit script synchroniseert de ontwikkelafhankelijkheden uit `uv.lock` naar `.venv/`. uv zoekt een geschikte Python-versie en kan die downloaden als die ontbreekt. Daarna installeert het script de headless Chromium-browser die bij de vastgelegde Playwright-versie hoort. Het controleert de Python-tools en opent een testpagina in die browser. Het voert de regressiesuite niet uit.

## Een nieuwe lokale of cloudomgeving

Ontbreekt uv, gebruik dan:

```sh
./install.sh --install-uv
```

Deze optie haalt de [officiële uv-installer](https://docs.astral.sh/uv/getting-started/installation/) via HTTPS op. De installer plaatst uv in `~/.local/bin`, of in `UV_INSTALL_DIR` als je die variabele hebt ingesteld. De scripts wijzigen geen shellprofielen. Een bestaande uv-installatie blijft behouden. Je hoeft uv niet eerst aan `PATH` toe te voegen om de setup opnieuw uit te voeren.

Voor een Debian- of Ubuntu-cloudimage waar Chromium-systeembibliotheken ontbreken:

```sh
./install.sh --install-uv --with-system-deps
```

Met `--with-system-deps` installeert Playwright ook [Linux-systeempakketten](https://playwright.dev/python/docs/browsers#install-system-dependencies). Daarvoor zijn rootrechten of werkende sudo-rechten nodig. Deze optie is alleen beschikbaar op Linux. Gebruik bij andere Linux-distributies een door Playwright ondersteunde omgeving of regel de systeembibliotheken volgens de afspraken van die omgeving.

## Alleen afhankelijkheden of Python-tools

`install-dependencies.sh` installeert dezelfde afhankelijkheden, zonder de Python- en browsercontroles van `install.sh`. Beide scripts begrijpen dezelfde installatieopties en werken ook wanneer je ze vanuit een andere map aanroept.

```sh
./install-dependencies.sh
./install.sh --skip-browser
./install.sh --help
```

Met `--skip-browser` vervallen de browserdownload en browsercontrole. Gebruik dit voor tekst- of scriptwerk waarvoor geen browser nodig is. Voer vóór browsertests de setup opnieuw uit zonder deze optie. `--skip-browser` en `--with-system-deps` kunnen niet samen worden gebruikt.

## Caches, netwerk en fouten

De eerste installatie heeft netwerktoegang nodig voor pakketten en de browser. De scripts behouden de lockfile en gebruiken bij herhaling de beschikbare caches. uv controleert daarbij nog steeds de vastgelegde afhankelijkheden.

Gebruik `UV_CACHE_DIR` en `PLAYWRIGHT_BROWSERS_PATH` wanneer een cloudomgeving eigen cachepaden vereist. Geef bij latere tests dezelfde `PLAYWRIGHT_BROWSERS_PATH` mee. De scripts gebruiken uv en Playwright met de proxy- en certificaatinstellingen van de omgeving. Ze configureren zelf geen proxy of certificaten.

Playwright beheert standaard een gedeelde browsercache en kan oudere browserbuilds opruimen. Gebruik op een host met meerdere projecten een cache per checkout om die installaties gescheiden te houden:

```sh
export PLAYWRIGHT_BROWSERS_PATH="$PWD/.cache/ms-playwright"
./install.sh
```

Behoud deze variabele bij latere browsertests. De map `.cache/` wordt door Git genegeerd.

Een mislukte download, installatie of browsercontrole stopt de setup met een foutcode. Bij een geweigerde browserstart controleer je de sandboxregels van de omgeving. Volg daarnaast de machineafspraken in [AGENTS.md](../AGENTS.md). Een geslaagde setup bewijst dat de tools starten; ze bewijst niet dat alle prototypes zijn getest.

De [testinventaris](../test/README.md) beschrijft welke tests beschikbaar zijn.
