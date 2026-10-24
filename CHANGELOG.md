# Changelog

Alle wijzigingen aan de bibliotheek en het onderhoud worden hier vastgelegd. Versies volgen `MAJOR.MINOR.PATCH`. De versie staat in `pyproject.toml` en `uv.lock`.

Dit overzicht begint op 18 oktober 2026 met de recente samengevoegde wijzigingen. Oudere wijzigingen blijven terug te vinden in de Git-historie. De bestaande versie `0.1.0` is nog niet als GitHub-release gepubliceerd. Een merge naar `main` is geen release.

## [Nog niet uitgebracht]

### Onderhoud

- Een codebase-overzicht toegevoegd met de projectstructuur, uitvoerpaden, configuratie en verificatiegrenzen; bereikbaar vanuit de ontwikkelgids.

- De README beschrijft nu hoe je de bibliotheek downloadt, opent en een voorbeeld kiest. Technische beheeruitleg staat in `docs/` ([#1](https://github.com/beecave-homelab/fab-visual-explainers/pull/1)).

- Testinstructies staan in `TESTING.md`; `test/README.md` bevat de testinventaris. Formattercontroles omvatten ook `docs/` ([#3](https://github.com/beecave-homelab/fab-visual-explainers/pull/3)).

- `install.sh` en `install-dependencies.sh` richten een ontwikkelomgeving in met de vastgelegde Python-afhankelijkheden en Playwright Chromium. De opties ondersteunen uv-bootstrap, Linux-systeempakketten en installatie zonder browser ([#5](https://github.com/beecave-homelab/fab-visual-explainers/pull/5)).

- Een changelog, agentafspraken, releasehandleiding en lokale versiecontrole toegevoegd. Agents werken voortaan de changelog bij als onderdeel van iedere repositorywijziging. De PR-controle met `--base` vergelijkt voortaan vanaf de merge-base van doelref en head, zodat een gevorderde doelbranch met eigen versiestijging of HTML-wijziging een geldige onderhouds-PR niet meer onterecht laat afkeuren ([#6](https://github.com/beecave-homelab/fab-visual-explainers/pull/6)).
