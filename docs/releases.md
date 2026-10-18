# Releases voorbereiden

Een release legt een versie van de hele bibliotheek vast. `project.version` in `pyproject.toml` is de bron voor het versienummer. De projectvermelding in `uv.lock` moet dezelfde versie hebben. Losse visuals krijgen geen afzonderlijke releaseversie.

## Wijzigingen verzamelen

Werk bij iedere wijziging `CHANGELOG.md` bij onder `Nog niet uitgebracht`. Gebruik voor documentatie, tests, scripts en CI de rubriek `Onderhoud`. De [agentafspraken](../AGENTS.md#changelog-en-versies) maken dit een vaste stap vóór oplevering.

De bestaande versie is `0.1.0`. Er zijn bij invoering van dit beleid geen gepubliceerde releases of tags. Het eerste changelogoverzicht beschrijft recente wijzigingen; het reconstrueert niet de volledige projecthistorie.

## Versie kiezen en controleren

Een wijziging aan `index.html` of HTML onder `visuals/` naar `main` vereist een hogere SemVer. Nieuwe functionaliteit verhoogt minor, een bugfix verhoogt patch. Beslis bij breaking changes welke versie nodig is, met aandacht voor de status vóór `1.0.0`. Een opmaakwijziging in HTML telt ook als productwijziging. Alleen onderhoud vraagt geen productbump.

Pas `project.version` aan en werk daarna de lockfile bij:

```sh
uv lock
```

Controleer de lockfile-diff. De wijziging vraagt geen dependency-update. Maak in de changelog een sectie `## [X.Y.Z] - YYYY-MM-DD` voor de gekozen versie en voorbereidingsdatum. Neem daarin de productwijziging en het verzamelde onderhoud op. Laat `Nog niet uitgebracht` leeg. De datum betekent niet dat de release al gepubliceerd is.

Controleer de lokale bestanden:

```sh
uv run --locked python scripts/check_release_version.py
uv run --locked python scripts/check_release_version.py --release
```

Zonder `--release` mag de changelog nog ongepubliceerde wijzigingen bevatten en hoeft de bestaande basisversie nog geen gedateerde sectie te hebben. Met `--release` zijn een gedateerde beschrijving voor de huidige versie en een lege sectie `Nog niet uitgebracht` verplicht.

Haal de actuele doelbranch op en controleer na het committen de volledige PR-diff:

```sh
git fetch github main
uv run --locked python scripts/check_release_version.py --base github/main --head HEAD
```

Vervang `github/main` door de echte doelref wanneer de checkout andere remotenamen gebruikt. Ontbrekende refs zijn een fout. De controle vergelijkt commits en ziet geen ongecommitteerde bestanden. Iedere gewijzigde commitreeks vereist een changelogwijziging. Bij HTML-wijzigingen controleert het script ook de versiestijging en de nieuwe releasebeschrijving. Het bepaalt niet of een wijziging minor of patch is.

Voer daarnaast de relevante controles uit [TESTING.md](../TESTING.md). De lokale versiecontrole vervangt geen tests, review of toestemming voor publicatie. Er is op dit moment geen CI-workflow die deze controle automatisch uitvoert.

## Publiceren

Publiceer alleen op verzoek van de gebruiker, vanaf een gecontroleerde commit die op `main` staat. Controleer vooraf dat de bedoelde versie en tag nog niet zijn gepubliceerd. Gebruik het versienummer zonder `v`-prefix als tag en koppel die aan de exacte gecontroleerde commit, zodat een bewegende branch niet de release bepaalt.

Neem de bijbehorende changelogsectie over als releasenotities. GitHub levert bronarchieven bij de tag. Een extra downloadpakket of automatische publicatieworkflow valt buiten dit startbeleid.

Controleer na publicatie de release-URL, tag, commit en beschikbare bestanden. Een conceptrelease of lokale tag is geen gepubliceerde release.
