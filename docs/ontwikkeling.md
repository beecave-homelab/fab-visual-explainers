# Ontwikkelen en controleren

De prototypes zijn zelfstandige HTML-bestanden met inline CSS, JavaScript en synthetische voorbeelddata. Er is geen backend of buildstap. Ontwikkeltools zijn alleen nodig om bestanden te wijzigen en te controleren.

Lees vóór een bijdrage de [projectafspraken](../AGENTS.md). De [ideeënnotitie](../ideeen_voor_interactieve_fab_one_pagers.md) beschrijft de concepten en actuele status. De [functiebeschrijving](../functie-beschrijving-functioneel-applicatiebeheer.md) is het aangeleverde toetskader, geen onafhankelijk gevalideerde beroepsstandaard.

## Ontwikkelomgeving

Gebruik Python 3.11 of hoger en uv. Voor browserregressies is Google Chrome of Playwright Chromium nodig. Zie [de testdocumentatie](../test/README.md#omgeving) voor browserkeuze en installatie. Volg daarnaast de uitvoeringsafspraken in [AGENTS.md](../AGENTS.md) voor de machine waarop je test.

Voer vanuit de hoofdmap uit:

```sh
uv sync --locked
uv run --locked pytest
uv run --locked ruff check test scripts
uv run --locked ruff format --check test scripts
uv run --locked mdformat --check *.md test/README.md docs
uv run --locked djlint --check visuals/ index.html
```

Dependencies en instellingen staan in `pyproject.toml`. `uv.lock` legt de versies vast. Zie [tests en kwaliteitscontroles](../test/README.md) voor gerichte tests, formattercommando's, tijdelijke uitvoer en de grenzen van deze controles.

## Waar staat wat?

| Locatie                                   | Inhoud                                                                                  |
| ----------------------------------------- | --------------------------------------------------------------------------------------- |
| `visuals/`                                | Zelfstandige prototypes, ingedeeld naar hoofdtaak.                                      |
| `index.html`                              | Doorzoekbare ingang met een opgeslagen overzicht van de bibliotheek.                    |
| `scripts/`                                | Inventarisatie, lokale bibliotheekserver en het verpakken van de hergebruikskill.       |
| `test/`                                   | Pytest-scenario's en documentatie over testdekking en uitvoering.                       |
| `docs/`                                   | Hergebruikgids, beheeruitleg, ontwerpspecificaties en reviewverslagen.                  |
| `.agents/skills/fab-html-template-reuse/` | Projectskill voor het maken van brongebonden kopieën.                                   |
| `outputs/`                                | Git-genegeerde uitvoer van hergebruik en skillpakketten, buiten de prototypeinventaris. |

## Bibliotheek of presentatiekopie wijzigen

Een wijziging aan `visuals/` is bibliotheekonderhoud. Houd bij toevoegingen en verwijderingen de inventaris, aantallen, beheerkaarten en links bij. Werk na wijzigingen aan titels of beschrijvingen ook het opgeslagen overzicht bij. Zie [bibliotheek beheren](bibliotheek-beheren.md).

Een brongebonden presentatie is een afzonderlijke kopie. Laat de oorspronkelijke prototypes en voorbeeldcasussen daarbij ongewijzigd. De [hergebruikgids](template-reuse.md) beschrijft patroonkeuze, bewerkgrenzen en verificatie van de kopie. De bestaande pytest-suite ontdekt alleen `visuals/` en bewijst geen kwaliteit van bestanden onder `outputs/`.

## De hergebruikskill verpakken

Binnen deze repository leest de projectskill de lokale guidance en `visuals/`, zonder netwerk. Buiten de repository kan hij een aangewezen lokale of cloudmap, een beschikbare checkout of de openbare repository gebruiken.

Maak een overdraagbaar skillpakket met:

```sh
python3 scripts/package_template_skill.py
```

Het pakket komt in `outputs/skill-packages/fab-html-template-reuse.zip`. Het bevat de skill en gebundelde guidance, zonder visuals. De ZIP werkt zonder checkout. De projectskill is niet persoonlijk geïnstalleerd. Zie de [hergebruikgids](template-reuse.md#zip-installeren-en-gebruiken) voor installatie en gebruik buiten deze repository.

## Wat controles aantonen

Houd aanwezig, technisch getest, inhoudelijk beoordeeld en met gebruikers gevalideerd apart. Een geslaagde browsercheck bewijst geen volledige toegankelijkheid of lokale goedkeuring voor praktijkgebruik.

De [visuele review van 4 oktober 2026](visual-review-2026-10-04.md) beschrijft sterke punten, verbeteringen en resterende grenzen per prototype. Dit verslag legt de bevindingen van die review vast. Het bewijst niet dat latere wijzigingen zijn getest.
