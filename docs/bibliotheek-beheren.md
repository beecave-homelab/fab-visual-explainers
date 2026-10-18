# Bibliotheek beheren

Om de bestaande voorbeelden te bekijken, open je `index.html` rechtstreeks in je browser. Deze pagina legt uit hoe je het overzicht bijwerkt wanneer je visuals toevoegt of aanpast. Zie [de README](../README.md) voor downloaden en gebruik.

## Een actueel overzicht via de lokale server

Start vanuit de hoofdmap van de repository:

```sh
python3 scripts/visual_library.py
```

Open daarna [de lokale bibliotheek](http://127.0.0.1:8765/). De server leest bij iedere paginalading alle HTML-bestanden onder `visuals/`, inclusief submappen en nieuwe categorieën. Voeg een bestand toe, verwijder of verplaats het, en ververs het overzicht.

De server gebruikt alleen de Python-standaardbibliotheek, luistert uitsluitend lokaal en serveert de landingspagina en HTML onder `visuals/`. Stop met `Ctrl+C`. Gebruik bij een bezette poort bijvoorbeeld `python3 scripts/visual_library.py --port 8766` en open de URL die het script toont. De prototypes blijven zelfstandig te openen.

## Titels en beschrijvingen

Namen komen uit de HTML-titel. Beschrijvingen komen uit `<meta name="description" content="…">` in ieder HTML-bestand. Elk prototype moet in de `<head>` precies één van deze beschrijvingen hebben. Beschrijf kort wat de gebruiker kan bekijken of onderzoeken.

Ontbreekt die metadata, dan gebruikt het overzicht de eerste bruikbare inleiding na de hoofdkop, en anders de hoofdkop zelf. Die terugval vervangt de verplichte metadata niet. Er is geen aparte beschrijvingenlijst om bij te houden.

## Het opgeslagen overzicht bijwerken

`index.html` kan rechtstreeks worden geopend, met zoeken, filters en alle opgeslagen links. Die kopie ontdekt geen nieuwe bestanden vanuit de browser. Werk het opgeslagen overzicht na toevoeging, verwijdering, verplaatsing of wijziging van een titel of beschrijving bij met:

```sh
python3 scripts/visual_library.py --generate
```

De HTML tussen `catalog:start` en `catalog:end` is gegenereerd. Pas vormgeving en interactie buiten dat blok aan. Alle links blijven zonder JavaScript beschikbaar. Afdrukken toont de volledige bibliotheek, ook wanneer een zoekfilter actief is.

Controleer beschrijvingen, inventarislinks en bibliotheekgedrag met:

```sh
uv run --locked pytest test/test_library.py
```

Zie [TESTING.md](../TESTING.md) voor de testomgeving en verdere controles.

## Indeling en telling

De prototypes staan onder `visuals/`, ingedeeld naar hoofdtaak. Ieder bestand heeft één vaste plek en een unieke bestandsnaam. Werk bij verplaatsingen relatieve links, fragmenten en documentverwijzingen bij.

| Map onder `visuals/`        | HTML-bestanden |
| --------------------------- | -------------- |
| `incident_en_continuiteit/` | 7              |
| `wijziging_en_acceptatie/`  | 11             |
| `landschap_en_processen/`   | 3              |
| `toegang/`                  | 2              |
| `gegevens_en_ketens/`       | 4              |
| `bronnen_en_kennis/`        | 5              |

De bibliotheek bevat 32 HTML-bestanden voor 31 concepten. De twee incidentvarianten tellen als één concept en hebben elk een eigen ingang. De landingspagina buiten `visuals/` telt niet als extra prototype. De [ideeënnotitie](../ideeen_voor_interactieve_fab_one_pagers.md) bevat de inventaris, selectie en actuele status.
