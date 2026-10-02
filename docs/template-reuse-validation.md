# Controle van templatehergebruik

Uitgevoerd op 02-10-2026. Dit rapport beschrijft de actuele controles bij toevoeging van de hergebruikgids en projectskill; het is geen operationele vrijgave of bewijs van gebruikerswaarde.

## Bibliotheek en instructies

- Alle 23 aanwezige HTML-bestanden hebben een bestandskaart. De genoemde JavaScript-dataankers en statische ID-ankers zijn tegen de actuele bestanden gecontroleerd. Documentlinks en Markdown-fragmenten bestaan.
- De skillstructuur, naam, routingbeschrijving, eigenaar en versie zijn gecontroleerd met `quick_validate.py`, `check-skill-layout.sh` en `check-skill-frontmatter.sh`: geslaagd.
- Markdown-opmaak van rootdocumenten, gids, skill en `test/README.md`: geslaagd. Ruff-check en -formatcontrole van `test/`, djLint-check van alle 23 HTML-bestanden en `git diff --check`: geslaagd.
- `git check-ignore outputs/example/index.html` bevestigt de uitvoeruitsluiting. `git diff --exit-code -- visuals` bevestigt dat geen bibliotheekorigineel gewijzigd is.
- `uv run --offline --locked pytest`: **82 geslaagd**, 90,44 seconden. Deze suite toetst de originelen, niet de gegenereerde kopieën.

## Directe hergebruikproeven

De auteur heeft de beschreven werkwijze zelf toegepast op tijdelijke kopieën met een synthetisch overlegdocument, onbekende eigenaar, ontbrekend bewijs, lange tekst en speciale tekens. Dit zijn technische stressfixtures, geen inhoudelijk gevalideerde documenten of onafhankelijke agent-evaluatie. Er is geen subagent gebruikt.

| Patroon            | Variatie en gedragscontrole                                                                                                                                                                                                        | Uitkomst |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Bronkaart          | Drie topics; selectie, bronpassage, volgende, zoekterm zonder resultaat en reset                                                                                                                                                   | Geslaagd |
| BronScanner        | Drie secties; vorige/volgende, correcte telling, zoeken zonder resultaat; demo-meters vervangen door onbekend/niet getoetst                                                                                                        | Geslaagd |
| Kennisatlas        | Drie nodes en één als voorstel gemarkeerde relatie; selectie en onzekerheidsfilter; lijst plus relatietabel                                                                                                                        | Geslaagd |
| Vraagdossier       | Drie vragen; drie leesdieptes, bewijsdetail openen/sluiten en bijpassende navigatielabels                                                                                                                                          | Geslaagd |
| VraagKompas        | Drie vraagroutes; drie modi, zoeken, vervolgvraag en bijpassende navigatielabels                                                                                                                                                   | Geslaagd |
| Decision Canvas    | Twee opties; onbekende voorwaarden geven geen rangorde; onvolledig bewijs wordt geweigerd; volledige synthetische beoordeling maakt één optie toelaatbaar; reset trekt die beoordeling terug; kopieerweigering geeft tekstfallback | Geslaagd |
| Continuïteitskaart | Twee uitvalsituaties; ontbrekend plan blokkeert bevestiging; vier gesimuleerde controles en afzonderlijke oefenbevestiging; gewijzigd plan wist controles en bevestiging; kopieerweigering geeft tekstfallback                     | Geslaagd |

Voor iedere kopie zijn gecontroleerd: geen JavaScript-fouten of externe aanvragen; unieke DOM-ID’s; bestaande lokale linkfragmenten; speciale tekens als tekst zonder geïnjecteerde afbeelding/eventhandler of beëindiging van het inline script; vertegenwoordigde knopfocus en Enter-activatie; geen documentbrede overloop op 320/390 pixels; complete statische registers zonder JavaScript, ook op 320 pixels; zichtbaarheid van die registers in print.

Alle zeven PDF’s zijn gegenereerd en met tekstextractie op het volledige bronregister, bijzondere brontekst en onbekende eigenaar gecontroleerd. Decision Canvas bevat ook ontbrekende voorwaarden en geen rangorde; Continuïteitskaart bevat herstelvoorwaarden en de ontbrekende afzonderlijke bevoegde bevestiging. De toegevoegde leeslaag heeft expliciet 11 pt printtekst; de PDFs gebruiken twee tot vijf pagina’s. Representatieve desktop-/mobielscreenshots en gerenderde PDF-pagina’s zijn bekeken, niet iedere pagina van iedere PDF.

De proeven bevestigden concrete aandachtspunten die in de gids zijn verwerkt: hardcoded sectietelling, afzonderlijke node-/relatielagen, lange koppen en bronpaden, behoud van geneste controlenodes zoals `#jumpText`, volledige statische alternatieven en expliciete printtekstgrootte. Noodzakelijke correcties zijn alleen in tijdelijke kopieën aangebracht.

## Tijdelijke bewijsbestanden en grenzen

De succesvolle eindrun staat in de OS-tijdelijke map `fab-reuse-validation-5aw_sbdv`: aangepaste HTML, desktop-/mobielscreenshots, PDF’s, `results.json`, `print-results.json` en `reuse-smoke.py`. De tijdelijke map kan later door het systeem worden verwijderd; deze bestanden zijn niet opgenomen in de repository of prototypeinventaris.

De uitvoerbestemming en bescherming tegen overschrijven zijn skillinstructies, geen technisch afgedwongen applicatiegedrag. De browserproeven dekken geselecteerde scenario’s en representatieve toetsenbordbediening; niet alle mogelijke bronstructuren, tabvolgordes, hulpmiddelen of printapparaten. Geen volledige toegankelijkheids-/beveiligingsaudit, lokale procesacceptatie, automatische skillselectietest, echte dossierkoppeling of gebruikersvalidatie is uitgevoerd. Het openbare WCAG-voorbeeld is een uitgewerkte mapping in de gids, geen afzonderlijk afgeleverd of geaudit WCAG-hulpmiddel.
