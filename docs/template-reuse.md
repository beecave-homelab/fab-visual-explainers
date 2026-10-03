# HTML-templates hergebruiken

Deze gids is de centrale selectie- en bewerkkaart voor de prototypes. Gebruik hem met [AGENTS.md](../AGENTS.md#templates-gebruiken-voor-een-bron) en de [projectskill](../.agents/skills/fab-html-template-reuse/SKILL.md). Inspecteer altijd de actuele HTML; de kaarten benoemen zoekankers, geen stabiele regelnummers of universele dataschema's.

## Selectie op hoofdvraag

| Vraag of bronstructuur                               | Eerste keuze                                                                                                                                                    | Wanneer een andere vorm beter past                                                                                                                            |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hoofdthema's met passages, betekenis en open vragen  | Bronkaart                                                                                                                                                       | BronScanner als hoofdstukvolgorde leidend is.                                                                                                                 |
| Lang document dat per sectie onderzocht wordt        | BronScanner                                                                                                                                                     | Bronkaart als thematische ordening belangrijker is.                                                                                                           |
| Inzichten met expliciete verbanden                   | Kennisatlas                                                                                                                                                     | Geen netwerk tekenen als de bron relaties niet onderbouwt; kies dan Bronkaart.                                                                                |
| Eén adviesvraag met conclusie, context en bewijs     | Vraagdossier                                                                                                                                                    | VraagKompas bij meerdere zelfstandige gebruikersvragen.                                                                                                       |
| Meerdere gebruikersvragen over dezelfde bron         | VraagKompas                                                                                                                                                     | Een lijst of kennisitem bij een korte lineaire instructie.                                                                                                    |
| Incident, analyse of continuïteit                    | Incidentvisual, Serviceradar, Oorzaakopsporing, Continuïteitskaart, Known Error Map of Escalatiekaart                                                           | Kies proces, perspectief, hypothesen, nood-/herstelvoorwaarden, bekende fouten of escalatie en overdracht als hoofdtaak.                                      |
| Wijzigingsdossier of besluitvoorbereiding            | Releaseatelier, Change Impact Map, Test Coverage Map, Omgevingsvergelijker, Beheerbaarheid Scan, Go/No-Go, Decision Canvas, Risk & Control Map of Pilot Cockpit | Kies respectievelijk fasen, gevolgen, tests, omgevingsverschillen, beheeracceptatie, livegangvoorwaarden, toelaatbare opties, restrisico of pilotbeoordeling. |
| Systemen, processen en verantwoordelijkheden         | Applicatielandschap, Proces × Applicatie-map of Life Cycle Map                                                                                                  | Ketenkaart bij berichtverwerking; Rapportage Lineage bij een KPI-definitie; Life Cycle Map bij ondersteuningstermijnen.                                       |
| Toegang en overgangsmomenten                         | Autorisatielandschap of Joiner-Mover-Leaver                                                                                                                     | Rechtenmatrix voor model/feitelijk/uitzondering; tijdlijn voor afzonderlijke eindmomenten.                                                                    |
| Gegevensstromen, afwijkingen of rapportagedefinities | Ketenkaart, Data Quality Map of Rapportage Lineage                                                                                                              | Geen totaalscore toevoegen zonder expliciete brondefinitie.                                                                                                   |

De twee incidentvarianten hebben hetzelfde inhoudelijke patroon. De vijf bron-/kennispatronen passen ook bij openbare documenten buiten FAB; pas de doelgroep en beheerkaart daarop aan. Operationele patronen zijn geen generieke rapportdecoratie: ontbrekende beslis-, bewijs- of herstelvoorwaarden mogen niet worden ingevuld met verzonnen zekerheden.

## Bewerkgrenzen en bestemming

Kopieer het gekozen bestand naar de expliciete bestemming, anders `outputs/<document-slug>/index.html`. Houd `visuals/`, inventaris en bibliotheekoriginelen intact. `outputs/` is Git-genegeerd, geen veilige opslaggarantie: plaats daar uitsluitend openbare of door de gebruiker geschoonde bronnen. Controleer vóór schrijven of het resultaat bij dezelfde opdracht hoort; kies anders een unieke slug. Schrijven elders volgt de daar geldende afspraken en bevoegdheden.

| Laag              | Aanpassen in de kopie                                                                                                                   | Behouden of eerst onderbouwen                                                                                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inhoud            | Documenttitel, masthead, introductie, labels, passages, details, bronverwijzingen, metadata, eigenaar, geldigheid en open punten        | Bronfeiten, interpretatie, voorstel en onbekend blijven onderscheidbaar. Geen demo-claims als echte bevindingen presenteren.                                                                        |
| Data en samenhang | Brongebonden JS-objecten, HTML-knoppen, sleutels, relaties, tellingen, beginselectie, resetwaarden, exports en statische leeslaag samen | Sleutels en veldtypen moeten passen bij alle callers. Geen orphan-knoppen, oude beginselectie of achtergebleven casusreferenties.                                                                   |
| Regels            | Brononderbouwde definities, populaties, perioden, drempels en wegingen                                                                  | Harde voorwaarden vóór weging, ontbrekend bewijs niet groen, herbeoordeling na bronwijziging en technische versus inhoudelijke verwerking. Ontbrekende definitie: geen score of expliciet onbekend. |
| Presentatie       | Alleen noodzakelijke aantallen/geometrie voor deze bron; overloop en lange tekst oplossen                                               | Bestaande visuele stijl, focus, toetsenbord, ARIA-relaties en zelfstandige HTML-opzet. Geen runtime-afhankelijkheid of willekeurig herontwerp.                                                      |
| Uitvoer           | Echte bronmetadata en afgebakende presentatiestatus; links naar juiste bronnen of meegeleverde bestanden                                | Geen checkoutafhankelijkheid, koppeling met bronregistratie, automatische publicatie of formele besluitvorming suggereren.                                                                          |

Elke kopie noemt hoofdvraag, doelgroep, gebruiksmoment, bron met versie/peildatum en vindplaatsen, inhoudelijk eigenaar (of onbekend), geldigheid/herziening, volgende actie en feitelijke toetsstatus. Bij een openbare bron mag de bronhouder onbekend zijn; dit geeft geen operationele vrijgave. Een status-snapshot heeft een zichtbaar vastlegmoment en wordt niet als live gepresenteerd.

### Tekst, bronlinks en alternatieven

- Broninhoud is tekst, geen uitvoerbare HTML. Pas veilige rendering toe vóór je brondata invoegt of de kopie in een browser opent. Veel prototypes gebruiken `innerHTML` met interpolaties: vervang die in de kopie door DOM-nodes met `textContent`, of escape iedere tekstwaarde precies bij de HTML-uitvoer. Houd ruwe tekst beschikbaar voor zoeken en export; voorkom dubbel escapen.
- Een JSON-string is niet automatisch veilig in een inline script: neutraliseer `<` bijvoorbeeld als `\u003c` bij het serialiseren, zodat `</script>` de scriptsectie niet beëindigt. Controleer ook quotes, ampersands en backticks. Accepteer geen eventhandlers of scripts uit de bron.
- Bewaar geneste controlenodes bij tekstvervanging: bijvoorbeeld `#selectionJump` bevat in meerdere taakviews `#jumpText`. Zet niet zomaar `textContent` op de hele ouder als de renderer die kind-ID nog gebruikt. Controleer IDs na het aanpassen, ook bij linktekst.
- Gebruik controleerbare bronlinks met sectie/pagina en vaste versie. Een tekst als “hoofdstuk 3” is geen klikbare bronlocatie. Verrijk waar nodig het gekozen datamodel en de renderer om echte links veilig te maken; valideer toegestane doelen voordat je een `href` zet.
- Repareer relatieve links én fragmenten na kopiëren. Verwijder navigatie naar irrelevante demo's; kopieer niet de hele bibliotheek om links te laten werken. Het resultaat moet op een andere plek kunnen openen zonder checkout. Externe bronlinks zijn toegestaan, automatisch laden van fonts/scripts/data niet; vervang in de algemene incidentkopie Google Fonts door de bestaande lokale fallback.
- Inspecteer de **daadwerkelijke** statische inhoud. Een door JavaScript gevulde lijst werkt niet zonder JavaScript. Voeg in de kopie een complete leesbare lijst/tabel toe met dezelfde inhoud en bronverwijzingen; toon die bij JavaScript uit en in print. Verberg daar niet-werkende controles. Een `<noscript>`-waarschuwing alleen is onvoldoende.
- De vijf bron-/kennispatronen hebben geen eigen `@media print` of volledige no-JS-leeslaag. Voeg die in de kopie toe. Een compact beginpaneel is geen alternatief voor alle achterliggende passages.
- Scores, relaties en simulated controles zijn geen gemeten betrouwbaarheid, bewezen oorzaak of bevoegd akkoord. In een echte toestandsweergave mogen oefenknoppen nooit de echte bronstatus wijzigen; laat ze weg of plaats ze in een expliciet afzonderlijke simulatie met aparte export.

## Bestandskaarten

De statische laag omvat bij **ieder** bestand ook `<title>`, hoofdkop, introductie, beheerkaart, datums, demo-waarschuwingen, casusnamen en lokale links. Hieronder staan de aanvullende locaties per bestand. “Export: geen” betekent dat het origineel geen kopieerexport biedt; voeg die niet automatisch toe.

### bronkaart-onepager.html

[Open origineel](../visuals/bronnen_en_kennis/bronkaart-onepager.html). **Taak:** Hoofdthema’s van een bron met kern, bewijs en open punten.

- **Statische inhoud:** Thematische ankers `context`, `finding`, `evidence`, `impact`, `questions`; initiële detailtekst en bronknop.
- **JavaScript-data:** `topics`: `id`, `kind`, `label`, `summary`, `bullets`, `fragment`, `status`.
- **Samen aanpassen:** `selectedId`, `visibleIds`, `renderNavigation()`, `selectTopic()`, reset en volgende-knop; thematische ankers zijn ook statische IDs.
- **Regels en export:** Geen berekening of export. `supported` is een inhoudslabel, geen onafhankelijk gecontroleerd bewijs. Fragmentinterpolatie en bullets veilig renderen.
- **Leeslaag en afdruk:** Geen volledige no-JS-leeslaag/printregels; maak een statisch register voor alle topics.

### bron-scanner.html

[Open origineel](../visuals/bronnen_en_kennis/bron-scanner.html). **Taak:** Sectievolgorde van een lang document met samenvatting en bewijsspoor.

- **Statische inhoud:** Sectietitel, metering-labels, intro en initiële quote/bewijsblokken.
- **JavaScript-data:** `data`: secties met `title`, `weight`, `confidence`, `evidence`, `impact`, `summary`, `takeaways`, `quote`, `why`, `caution`, `related`, `proofs`.
- **Samen aanpassen:** `active`, `renderMap()`, `select()`, `filter()`, vorige/volgende en voortgang; **`${index+1}/8` is hardcoded**, vervang door `data.length`.
- **Regels en export:** `label()` gebruikt drempels 88/75; bars en indices zijn handgekozen demo’s. Geen onderbouwde schaal: verwijder meters én bijbehorende rendercode/labels in de kopie, geen nul als schijnmeting. Export: geen.
- **Leeslaag en afdruk:** Geen volledige no-JS-leeslaag/printregels; register voor alle secties met vindplaatsen en zonder fictieve bewijspercentages.

### kennisatlas.html

[Open origineel](../visuals/bronnen_en_kennis/kennisatlas.html). **Taak:** Inzichten met brononderbouwde relaties.

- **Statische inhoud:** `.atlas-node`, `data-node`, `data-route-kind`, routelabels, SVG `.connections`-paden en `#atlasStats`.
- **JavaScript-data:** `atlasData`: `type`, `title`, `summary`, `why`, `evidence`, `source`.
- **Samen aanpassen:** Data-object, HTML-nodekeys, labels/posities en SVG-verbindingen zijn afzonderlijk vastgelegd; `setAtlasNode()` en `applyRoute()` gebruiken ze samen. Statische aantallen en beginpaneel apart vervangen. Lange koppen, kaartlabels en node-labels kunnen de mobiele indeling laten overlopen; pas in de kopie waar nodig de positie/breedte of een gestapelde leesroute aan, met relaties ook in de relatietabel.
- **Regels en export:** Geen automatische relatie-afleiding, berekening of export. Teken alleen aangetoonde of expliciet voorgestelde relaties, geen causaal effect uit co-occurrence.
- **Leeslaag en afdruk:** Geen volledige no-JS-leeslaag/printregels; lijst van alle inzichten plus expliciete relatietabel, niet alleen geselecteerd detail.

### vraagdossier.html

[Open origineel](../visuals/bronnen_en_kennis/vraagdossier.html). **Taak:** Eén adviesvraag op meerdere leesdieptes.

- **Statische inhoud:** `.question-button` met `data-question`, `.depth-tabs` met `data-depth`, startpaneel en bewijs-popover.
- **JavaScript-data:** `dossierData`: `question`, `title`, `short`, `medium`, `source`, `takeaway`, `trail`, `evidence` (`kind`, `tag`, `text`, `detail`).
- **Samen aanpassen:** `currentQuestion`, `currentDepth`, HTML-vraagkeys, `renderDossier()` en `openEvidence()`; bewijsindex en bronpad moeten bij de gekozen vraag horen. Lange bronpaden vragen controle van minimale kolombreedte en regelafbreking in `.brief-body` en `.source-strip`.
- **Regels en export:** `briefCount` telt bewijsitems, geen bewijskracht. Geen score/export. Sluiten/nieuwe selectie mag geen vorige bewijsinhoud zichtbaar laten.
- **Leeslaag en afdruk:** Geen volledige no-JS-leeslaag/printregels; statische vragen met alle dieptes, bewijsdetails en bronpaden.

### vraagkompas.html

[Open origineel](../visuals/bronnen_en_kennis/vraagkompas.html). **Taak:** Meerdere zelfstandige lezersvragen met vervolgroutes.

- **Statische inhoud:** `.q`/`data-id`, `.mode`/`data-mode`, initiële antwoorden en documentomvang.
- **JavaScript-data:** `items`: `title`, `short`, `bullets`, `source`, `refs`, `related`; `order`.
- **Samen aanpassen:** `active`, `mode`, `order`, HTML-knoppen en `related`-doelkeys samen wijzigen; lange documentkoppen en bronstempels vragen regelafbreking en minimale kolombreedte in `.mast`/`.source-stamp`; pijlnavigatie en zoeken volgen `order`.
- **Regels en export:** Geen score/export. Zoeken kiest de eerste match en wist selectie niet bij lege zoektekst; beloof geen volledige resultatenlijst. Vervang hardcoded demo-bronuitleg in de source-renderbranch.
- **Leeslaag en afdruk:** Geen volledige no-JS-leeslaag/printregels; statische antwoorden, passages, verwijzingen en vervolgvraagrelaties.

### incident-onepager.html

[Open origineel](../visuals/incident_en_continuiteit/incident-onepager.html). **Taak:** Incidentproces van melding tot nazorg.

- **Statische inhoud:** Procesknoppen, initial detail, `#readableIncident`, `#incidentChecklist` en `#continuity`.
- **JavaScript-data:** `steps`: `title`, `lead`, `items`, `ready`.
- **Samen aanpassen:** HTML-procesnodes, stapindex, `renderStep()` en `setMode()`; beide incidentvarianten gebruiken hetzelfde inhoudelijke patroon.
- **Regels en export:** Geen berekening/export; behoud zorgimpact en goedgekeurde noodwerkwijze. Algemene variant laadt Google Fonts: schakel die aanvraag uit in de kopie.
- **Leeslaag en afdruk:** Print aanwezig; JS vult checklist. Controleer alle stappen statisch en de afzonderlijke continuïteitscasus.

### incident-onepager-attent.html

[Open origineel](../visuals/incident_en_continuiteit/incident-onepager-attent.html). **Taak:** Zelfde incidentproces met alternatieve vormgeving.

- **Statische inhoud:** Procesknoppen, initial detail, `#readableIncident`, `#incidentChecklist` en `#continuity`.
- **JavaScript-data:** `steps`: `title`, `lead`, `items`, `ready`.
- **Samen aanpassen:** HTML-procesnodes, stapindex, `renderStep()` en `setMode()`; kies één variant tenzij de opdracht beide vraagt.
- **Regels en export:** Geen berekening/export; dezelfde inhoudelijke grenzen als de algemene variant.
- **Leeslaag en afdruk:** Print aanwezig; JS vult checklist. Controleer alle stappen statisch en de afzonderlijke continuïteitscasus.

### fab-serviceradar.html

[Open origineel](../visuals/incident_en_continuiteit/fab-serviceradar.html). **Taak:** Incidentonderzoek langs betrokken perspectieven.

- **Statische inhoud:** Radarnodes met `data-key`, beginperspectief, `#readableRadar` en `#radarChecklist`.
- **JavaScript-data:** `data`: `code`, `kicker`, `title`, `lead`, `questions`, `gate`.
- **Samen aanpassen:** Nodekeys, geometrie, `render()` en beginselectie `melder`; JS-checklist wordt uit data gebouwd.
- **Regels en export:** Geen berekening/export; perspectief is geen bevoegdheids- of oorzaakbewijs.
- **Leeslaag en afdruk:** Print aanwezig; checklist is JS-gegenereerd. Voeg alle perspectieven statisch toe indien niet volledig aanwezig.

### fab-oorzaakopsporing.html

[Open origineel](../visuals/incident_en_continuiteit/fab-oorzaakopsporing.html). **Taak:** Meerdere hypothesen onderzoeken zonder onbewezen uitsluiting.

- **Statische inhoud:** Hypotheselabels, vraagformulieren, `#assessment`, toelichting en notitie.
- **JavaScript-data:** `H`, `C`, `labels`, `ans`; inspecteer bewijsvelden en antwoordcodes in `state()`.
- **Samen aanpassen:** Hypothese-IDs, vraagverwijzingen en antwoorden samen wijzigen; reset/undo en `note()`.
- **Regels en export:** Antwoorden zijn aanwijzingen, geen definitieve uitsluiting. `state()`/`render()` en export via `note()` moeten dezelfde bewijsstatus volgen; ontbrekende/daterende beoordeling niet als bevestigd behandelen.
- **Leeslaag en afdruk:** Print aanwezig; controleer of alle hypothesen en controles zonder JS leesbaar zijn; voeg register toe waar nodig.

### fab-continuiteitskaart.html

[Open origineel](../visuals/incident_en_continuiteit/fab-continuiteitskaart.html). **Taak:** Uitval, veilige tijdelijke werkwijze en afzonderlijke herstelcontroles.

- **Statische inhoud:** `#outage`/`#plan`-opties, vier `[data-check]`-controles, planmetadata, overdracht en `.readable`-routes.
- **JavaScript-data:** `scenarios` (`name`, `impact`, `technical`, `offline`, `dependency`), `labels`, `approved`.
- **Samen aanpassen:** Scenarioselectie, `render()`, `checks()`, reset bij gewijzigde bron/uitval en `#confirm`; planmetadata zit ook hardcoded in `render()` en `summary()`.
- **Regels en export:** Vier controles plus afzonderlijke bevestiging; gewijzigd bewijs trekt bevestiging in. `summary()`/`#export-text` mogen geen fictief plan of echt herstelakkoord suggereren. Simulatie blijft apart van snapshot.
- **Leeslaag en afdruk:** Print en statische routes aanwezig; werk alle routes, vier controles, contact-/offlinevoorwaarden en bronmetadata samen bij.

### fab-releaseatelier.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-releaseatelier.html). **Taak:** Wijzigingsdossier per fase.

- **Statische inhoud:** `.phase`/`data-key`, beginfase, `#readableRelease`, `#releaseChecklist`, `#test-coverage`.
- **JavaScript-data:** `data`: fasevelden zoals `boardTitle`, `mainText`, `decisionText`, `artifactText`, `list`, `questions`, `ready`, `sign`.
- **Samen aanpassen:** Fasekeys, `render()` en beginselectie `intake`; `ready` gebruikt `|` als scheiding, geen gewone vrije tekst.
- **Regels en export:** Geen berekening/export; faseovergang is uitleg, geen formeel akkoord. Zelfstandige testcasus en criteria ook vervangen.
- **Leeslaag en afdruk:** Print aanwezig; checklist wordt met JS gevuld. Testdekking bevat aparte statische inhoud; houd volledige fasen statisch bereikbaar.

### fab-change-impact-map.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-change-impact-map.html). **Taak:** Directe en afgeleide gevolgen van een wijziging.

- **Statische inhoud:** `data-pt`, matrixlabels, modeselectie en detailtabs.
- **JavaScript-data:** `AREAS`, `ORDERS`, `POINTS`, `LINKS`, `CX`, `CY`, `REVIEW`, `WIRE_D`.
- **Samen aanpassen:** Pointkeys, statische SVG-nodes, coördinaten, wire-paden en links samen wijzigen; severiteitsfilter, beginselectie en reset.
- **Regels en export:** `curSev()` onderscheidt huidige ernst en hypothetische `sevMet`; een geplande maatregel bewijst geen risicoreductie. Copy-handler bevat ook hardcoded RFC/livegang.
- **Leeslaag en afdruk:** Noscript en print aanwezig; waarschuwing is geen volledig register. Controleer alle gevolgen/maatregelen/bewijs statisch.

### fab-test-coverage-map.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-test-coverage-map.html). **Taak:** Herleidbaarheid eis → inrichting → scenario → toets/akkoord.

- **Statische inhoud:** `.register`-artikelen, omgeving-/casusreferenties en filterlabels.
- **JavaScript-data:** `tests`: `id`, `eis`, `name`, `mapping`, `scenario`, `expect`, `risk`, `owner`, `reviewer`, `blocked`; `states`.
- **Samen aanpassen:** Test-ID, statische register-ID, `initialize()`, `draw()`, geselecteerde test en filter samen bijwerken.
- **Regels en export:** `valid()` vraagt actuele bewijsversie, geslaagde uitvoering en akkoord; `initialize()` zet alles op gepland. Voor echte snapshot expliciete bronstatus laden en simulatie scheiden. `summary()` bevat hardcoded omgeving/casus.
- **Leeslaag en afdruk:** Print en statisch register aanwezig; werk alle testartikelen tegelijk bij, ook negatieve/fout-/terugvalscenario’s waar relevant.

### fab-omgevingsvergelijker.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-omgevingsvergelijker.html). **Taak:** testresultaat naast de productiedoelstand leggen per configuratie-onderdeel.

- **Statische inhoud:** `.register`-tabel met `tr[data-static-aspect]` per onderdeel, beginoordelen per testspoor in `.tracknotes` en de koppelpunt-/testrolnotities.
- **JavaScript-data:** `INITIAL` (per onderdeel `prodNow`, `prodTarget`, `env.acc`/`env.tst` met `v`, `snap`, `verified`, `note`), `TRACKS` (aspecten per spoor), `PEIL` en `PROD_SNAP`.
- **Samen aanpassen:** omgevingskeys (`acc`/`tst` met `ENVNAME`), aspect- en spoor-ID's, `initialize()`, `draw()`, beginselectie `track`/`env` en reset samen bijwerken; rij-ID's (`data-aspect`) en statische `data-static-aspect` moeten overeenkomen.
- **Regels en export:** `statusOf()` geeft per onderdeel en omgeving Gelijk, Gelijk aan doelstand, Verschil, Onbekend, Verouderd of Herbeoordeling nodig; verouderd (> 14 dagen) en ongecontroleerd tellen als onbekend, nooit als gelijk. `verdictParts()`, scherm en `summary()` gebruiken diezelfde status; een verschil vraagt een aanvullende test en "geen bekend verschil" is geen productiebewijs.
- **Leeslaag en afdruk:** Print en statische tabel aanwezig; werk tabel, spoorteksten en notities samen bij met de data.

### fab-known-error-map.html

[Open origineel](../visuals/incident_en_continuiteit/fab-known-error-map.html). **Taak:** meldingskenmerken koppelen aan bekende fouten en goedgekeurde tijdelijke werkwijzen.

- **Statische inhoud:** kenmerk-checkboxes `data-sign`, versie-select `#version`, `.register article` per kennisitem (`ke-static-<nr>`) en het meldingsblok.
- **JavaScript-data:** `INITIAL` (per item `signs`, `excludes`, `workaround`/`noWorkaround`, `conditions`, `impact`, `kind`, `versions`, `approval`, `review`, `structural`, `owner`, `escalation`, `links`), `SIGNS` en `PEIL`.
- **Samen aanpassen:** kenmerk- en item-ID's, `initialize()`, `draw()`, beginselectie, `data-condition`-voorwaarden en de acties `reconfirm`/`revise` samen bijwerken; label (`data-select`), detail (`#detail-<id>`) en register-ID moeten overeenkomen.
- **Regels en export:** `assess()` volgt vaste volgorde: uitgesloten kenmerk, geen aanwijzing, concept, verlopen herbeoordeling, onbeoordeelde versie, openstaande voorwaarden, pas dan toepasbaar. Scherm, `#verdict` en `summary()` gebruiken diezelfde uitkomst; gewijzigde kenmerken of status resetten bevestigde voorwaarden.
- **Leeslaag en afdruk:** Print en statisch register aanwezig; werk kenmerken, uitsluitingen, werkwijze, voorwaarden en escalatie per item samen bij.

### fab-escalatiekaart.html

[Open origineel](../visuals/incident_en_continuiteit/fab-escalatiekaart.html). **Taak:** peil, rol en escalatiepakket bepalen bij een verstoring.

- **Statische inhoud:** impact-checkboxes `data-impact`, selects `#cause`/`#workaround`/`#duration`, `.register article` per peil (`esc-static-l0` … `-pv`) en het meldingsblok.
- **JavaScript-data:** `LEVELS` (per peil `role`, `task`, `route`, `verified`, `fields`, `req`, `sendLabel`), `FIELDS`, `PEIL` en `DAYS`.
- **Samen aanpassen:** peil-ID's (`data-level`, `#esc-static-<id>`), veld-ID's `f1`–`f18`, `initialize()`, `draw()`, `peil()`, partnerkeuze bij `#cause` en de acties `verify`/`send`/`accept` samen bijwerken; schaal-, water- en golfposities volgen het hoogste peil.
- **Regels en export:** `peil()` levert actieve peilen, redenen en hoogste peil; `routeStatus()` rekent verouderd (> 90 dagen) en niet geverifieerd als onbruikbaar voor l1/l2/pv, nooit voor de continuïteitsstart. `handoverText()`, `#verdict` en `summary()` gebruiken dezelfde uitkomst; een uitgevinkt vereist veld maakt een eerdere overdracht ongeldig.
- **Leeslaag en afdruk:** Print en statisch register aanwezig; werk peilen, rollen, routes, veldvereisten en overdrachtsregels samen bij.

### fab-beheerbaarheid-scan.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-beheerbaarheid-scan.html). **Taak:** Beheeracceptatie met afzonderlijke bewijscontrole.

- **Statische inhoud:** Domeinlabels, ring, beheerkaart, assessment en `#scanChecklist`.
- **JavaScript-data:** `INITIAL` met domeinen en checks; inspecteer afgeleide werkdata en beoordelingen.
- **Samen aanpassen:** Domein/check-ID, ringsegment, selectie, reset naar INITIAL, checklist en `buildSummaryText()`.
- **Regels en export:** `accepted()` en statusberekening vereisen beoordelingsmetadata; bronlabel is geen akkoord. Bronwijziging trekt acceptatie in; export dezelfde status.
- **Leeslaag en afdruk:** Noscript, checklist en print aanwezig; controleer dat elke gewijzigde check met bewijs/actie statisch terugkomt.

### fab-go-no-go-cockpit.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-go-no-go-cockpit.html). **Taak:** Livegangadvies met criteria, bevindingen en drempels.

- **Statische inhoud:** Tijdlijn, groepslabels, statuseditor en evidence-formulier.
- **JavaScript-data:** `GROUPS` (items), `RULES`, `FINDINGS`, `STATUS_LABEL`.
- **Samen aanpassen:** Criteria-ID, groep, bevindingen, bewijsbeoordeling, `saveCriterion()`, reset en adviesweergave.
- **Regels en export:** `advice()` volgt harde voorwaarden en bevindingendrempels; onbekend/afgekeurd niet groen. Copy-handler en scherm dezelfde redenen; geen formeel besluit.
- **Leeslaag en afdruk:** Noscript en print aanwezig; voeg volledige criterialijst, bevindingen en regels toe als fallback slechts waarschuwing is.

### fab-decision-canvas.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-decision-canvas.html). **Taak:** Opties vergelijken ná toetsing van harde voorwaarden.

- **Statische inhoud:** Aspectlabels, gewichtsinputs `[data-weight]`, tabs en startdetail.
- **JavaScript-data:** `ASPECTS`, `ASPECT_SUB`, `OPTIONS` (scores/gates), `POINTS`, `weights`, `WEIGHT_LABEL`, `initialGates`.
- **Samen aanpassen:** Optiekeys, pointkeys met optie/aspectindex, gewichtskeys en resetwaarden op beide plekken samen; canvasgeometrie afhankelijk van indeling.
- **Regels en export:** `admissible`, `weightedScore`, `scores()` en `rankingText()`; alleen toelaatbare opties rangschikken. Geen brondefinitie: geen numerieke rangorde. Gate-bronwijziging trekt akkoord in. Copy-handler heeft eigen casusmetadata.
- **Leeslaag en afdruk:** Noscript en print aanwezig; statisch register voor opties, harde voorwaarden, scores/grondslag en aannames; geen fictieve acceptatie.

### fab-risk-control-map.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-risk-control-map.html). **Taak:** risico's volgen door maatregelen met bewijs en aangetoond restrisico.

- **Statische inhoud:** contextblok met casusreferenties, `.register article` per risico (`risk-static-R1` …) met inherente kans, maatregelen, restrisico en open punten.
- **JavaScript-data:** `RISKS` (`kans`, `gevolg`, `owner`, `acceptor`), `CONTROLS` (`risk`, `effect`, `status`, `evidence`, `blocked`), `STATUS_LABEL`, `KANS`/`DIKTE` en `PEIL`.
- **Samen aanpassen:** risico- en maatregel-ID's (`data-risk`, `data-control`, `risk-static-<id>`), `initialize()`, `draw()`, `sliceSvg()` en de acties `execute`/`pass`/`fail`/`change`/`accept` samen bijwerken; geblokkeerde maatregelen (`blocked`) krijgen nooit toetsknoppen.
- **Regels en export:** `residual()` rekent aangetoond (alleen werkzame maatregelen) en verwacht (alle maatregelen) apart; `severe()` volgt vaste drempels, geen totaalscore. `#tally`, scherm en `summary()` gebruiken dezelfde uitkomst; iedere maatregelactie maakt een eerdere acceptatie ongeldig.
- **Leeslaag en afdruk:** Print en statisch register aanwezig; de SVG-doorsnede is nooit de enige informatiedrager — werk lijst, bewijs en register tegelijk bij.

### fab-pilot-cockpit.html

[Open origineel](../visuals/wijziging_en_acceptatie/fab-pilot-cockpit.html). **Taak:** meetweken, stopcriteria en advies voor een begrensde proef.

- **Statische inhoud:** blok "Vooraf vastgelegd" (hypothese, meting, nulmeting, succesgrens, meetellen), `.register`-tabel met `tr[data-static-week]` per week en de stopcriterialijst.
- **JavaScript-data:** `INITIAL_WEEKS` (`pt`/`pn`, `ct`/`cn`, `ps`/`cs`, `time`, `mel`), `BRAKES`, `#week` en `PEIL`.
- **Samen aanpassen:** weeknummers (`data-week`, `data-static-week`), stopcriterium-ID's (`data-brake`), `initialize()`, `draw()`, `drawChart()` en de acties `control`/`correct`/`fallback-pass`/`fallback-fail`/`incident` samen bijwerken; teller/noemer en grafiekposities volgen uit dezelfde data.
- **Regels en export:** `counted()` selecteert meegetelde weken (gecontroleerd, noemer ≥ 40, week 3 t/m peilmoment, vergelijking gecontroleerd); `outcome()`, `brakeStates()` en `advice()` gebruiken diezelfde set. Niet gemeten is onbekend, niet groen; percentages altijd met teller en noemer.
- **Leeslaag en afdruk:** Print, statische tabel en criteria aanwezig; werk weken, statussen, stopcriteria en rekenregels samen bij.

### fab-applicatielandschap.html

[Open origineel](../visuals/landschap_en_processen/fab-applicatielandschap.html). **Taak:** Systemen, afhankelijkheden en eigenaren bespreken.

- **Statische inhoud:** Legenda, routefilters, uitleglade en `#staticFallback`.
- **JavaScript-data:** `apps` (incl. `x`, `y`, `w`, `h`), `links`, `routeMeta`.
- **Samen aanpassen:** App-ID, link-endpoints, routekinds, statuslabels en kaartgeometrie; mobiele centrering, zoeken/reset en relatieroute.
- **Regels en export:** Geen score/export; status en criticality vragen bron/peildatum. Een verbinding bewijst geen leverancierfunctionaliteit.
- **Leeslaag en afdruk:** Print en staticFallback aanwezig; pas lijst én kaart aan, niet alleen apps/links.

### fab-proces-applicatie-map.html

[Open origineel](../visuals/landschap_en_processen/fab-proces-applicatie-map.html). **Taak:** Processtappen, systemen, overdrachten en bevoegdheden.

- **Statische inhoud:** `data-cell`, `#rolSelect`, overdracht-toggle en matrix/SVG.
- **JavaScript-data:** `APPS`, `STEPS`, `CELLS`, `EDGES`, `VALIDATION`, `CX`, `CY`, `APPY`.
- **Samen aanpassen:** Appkeys, stapindices, cellkeys, rolefilters, coördinaten en lijnen; roltoelichting blijft bij dezelfde stap.
- **Regels en export:** Geen totaalscore; `VALIDATION` houdt lokale toetsstatus bij. Copy-handler bevat casus- en procesmetadata; technische uitvoerder beslist niet over zorginhoud.
- **Leeslaag en afdruk:** Noscript en print aanwezig; controleer volledige proces-/overdrachtstabel zonder JS, niet alleen fallbackmelding.

### fab-autorisatielandschap.html

[Open origineel](../visuals/toegang/fab-autorisatielandschap.html). **Taak:** Modelrechten, feitelijke scope en tijdelijke uitzonderingen.

- **Statische inhoud:** Matrix `[data-cell]` en niveaudata, rol-/applabels en sensitiviteitsfilter.
- **JavaScript-data:** `ROLES`, `APPS`, `LVL`, `ACCESS_META`, `ACCESS`, `GROUNDS`, `GROUPS`, `EXC`, `BEWIJS`, `LOGS`.
- **Samen aanpassen:** `ACCESS` wordt uit statische matrixdata opgebouwd; rol-appsleutels, model/feitelijk, uitzonderingen en gevoeligheid samen bijwerken.
- **Regels en export:** `accessRows()` en copy-handler onderscheiden model, feitelijk, noodzakelijkheid, scope, akkoord/eindmoment. Een gelijk niveau bewijst geen geldige toegang; onbekend blijft onbekend.
- **Leeslaag en afdruk:** Noscript en print aanwezig; volledige matrix én uitzonderingsdetails statisch aanbieden, geen echte accounts opnemen.

### fab-joiner-mover-leaver.html

[Open origineel](../visuals/toegang/fab-joiner-mover-leaver.html). **Taak:** Afgesproken en feitelijke overgangsmomenten vergelijken.

- **Statische inhoud:** Scenarioknoppen, plan/feitelijk-toggle en tijdlijnlabels.
- **JavaScript-data:** `S`: `min`, `max`, `date`, `zero`, `title`, `story`, `rows` (`plan`, `act`, `how`, `owner`, `note`, `cp`, `slip`); `META`, `OPEN`, `FROM`.
- **Samen aanpassen:** Scenario-ID, dagbereik, geselecteerde rij en startdag; `build()`/`update()` en datumrekenwerk.
- **Regels en export:** `iv()` gebruikt inclusieve einddag, beëindiging begin volgende dag; OPEN/FROM zijn sentinels, geen echte termijnen. `list()` is export. Tijdvak bewijst geen effectieve toegang.
- **Leeslaag en afdruk:** Print aanwezig; tijdlijn wordt met JS opgebouwd. Voeg volledige plan-/feitelijke tabel met eindmomenten en onbekende scope toe.

### fab-ketenkaart.html

[Open origineel](../visuals/gegevens_en_ketens/fab-ketenkaart.html). **Taak:** Berichtpad en afzonderlijke technische/inhoudelijke verwerking.

- **Statische inhoud:** Desktop én mobiele SVG, routekeuze, tabs en `#data-quality`.
- **JavaScript-data:** `nodes`, `edges`, `routes`, `normalStates`, `failureStates`, `fields`, `tabs`.
- **Samen aanpassen:** Node-ID, edge-ID, routepad, twee SVG-versies en foutscenario samen aanpassen; route-/selectiereset en mobiele focus.
- **Regels en export:** Technische ontvangst is geen eindverwerking; kwaliteitsoverlap niet afleiden uit losse tellingen. Copy-handler exporteert route/status/bron; log is synthetisch, nooit volledige echte logs.
- **Leeslaag en afdruk:** Noscript en print aanwezig; kwaliteitscasus is afzonderlijke statische inhoud. Controleer alle routes/foutdetails en kwaliteit in leeslaag.

### fab-data-quality-map.html

[Open origineel](../visuals/gegevens_en_ketens/fab-data-quality-map.html). **Taak:** Regelafwijkingen, overlap en veilige herstelroute.

- **Statische inhoud:** Populatiecaption, peildatum, overlaplens en `.register`.
- **JavaScript-data:** `rules`: `id`, `name`, `field`, `definition`, `positions`, `owner`, `effect`, `consumers`, `action`, `control`; `stateNames`.
- **Samen aanpassen:** Regel-ID en register-ID, gecontroleerde populatie, overlap-/unietelling en state/reset samen wijzigen.
- **Regels en export:** `totals()`/`remaining()` gebruiken verzonnen overlappende positions; alleen brononderbouwde overlap tellen, anders onbekend. Regeldefinitie/tijdsdrempel en bevoegd herstel apart toetsen; `summary()` heeft bronmetadata.
- **Leeslaag en afdruk:** Print en statisch register aanwezig; populatie, afwijkingen, afnemers en herstelvoorwaarden consistent met interactie bijwerken.

### fab-life-cycle-map.html

[Open origineel](../visuals/landschap_en_processen/fab-life-cycle-map.html). **Taak:** ondersteuningstermijnen en uiterlijke startdata per applicatie-onderdeel.

- **Statische inhoud:** `.register article` per onderdeel (`lc-static-<id>`) met beide termijnen, bron en bronstatus, doorlooptijd met opbouw, afhankelijkheid, berekende start, status op peildatum, eigenaar en volgende actie; de rekenregel staat in de introtekst.
- **JavaScript-data:** `INITIAL` (per onderdeel `version`, `full`, `end`, `source`, `srcStatus`, `confirmed`, `weeks`, `leadText`, `dep`, `depNote`, `owner`), `PEIL`, schuifbereik `D0`–`D1` en `MN`.
- **Samen aanpassen:** onderdeel-ID's (`data-select`, `#detail-<id>`, `lc-static-<id>`), kolomgeometrie (`x()`, `y()`), afhankelijkheidslijn, `initialize()`, `draw()`, beginselectie en de acties `confirm`/`roadmap`/`enddate` samen bijwerken.
- **Regels en export:** `plan()` berekent uiterlijke start als einde − doorlooptijd en laat de ECD-afhankelijkheid eerder schuiven; statussen volgen vaste volgorde (onbekend, buiten ondersteuning, verstreken, binnen 8 weken, bewaken) en een onbevestigde bron blijft gemarkeerd. Scherm, `#summary`-telling en `summary()` gebruiken dezelfde uitkomst; gepland is niet uitgevoerd.
- **Leeslaag en afdruk:** Print, smalle-schermlijst (`.almanac-list`) en statisch register aanwezig; werk alle termijnen, opbouw en uitkomsten samen bij.

### fab-rapportage-lineage.html

[Open origineel](../visuals/gegevens_en_ketens/fab-rapportage-lineage.html). **Taak:** KPI → berekening → veld → bron verklaren.

- **Statische inhoud:** Laaglabels, chips, beginselectie en definitietoelichting.
- **JavaScript-data:** `LAYERS`, `DEFINITION`, `N` (node `l`, `down` en bron-/definitievelden).
- **Samen aanpassen:** Node-ID, `down`-verwijzingen, laagindex, selectie `k1` en verbindingen `drawVeins()`; stale-bronsimulatie.
- **Regels en export:** Waarden zijn voorbeelden, geen live KPI-berekening. Teller/noemer/periode/populatie/uitsluitingen expliciet maken; `summary()` export consistent met node/bronstatus.
- **Leeslaag en afdruk:** Print aanwezig; lagen worden met JS opgebouwd. Voeg volledige KPI-definitie-/lineagetabel toe zonder JS.

## Uitgewerkt voorbeeld: openbare bron

**Opdracht:** presenteer twee openbare WCAG 2.2-criteria als bronkaart voor FAB, ter voorbereiding van een gesprek over bediening. Geen applicatie-audit, geen score en geen nalevingsverklaring.

**Bron:** [WCAG 2.2, vaste W3C Recommendation van 12 december 2024](https://www.w3.org/TR/2024/REC-WCAG22-20241212/). Gebruik [2.1.1 Keyboard](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#keyboard) en [2.4.7 Focus Visible](https://www.w3.org/TR/2024/REC-WCAG22-20241212/#focus-visible). De eerste gaat over toetsenbordbediening met een beschreven uitzondering; de tweede over zichtbare focus bij toetsenbordbediening. Houd de volledige criteria via de bronlinks bereikbaar. Dit voorbeeld bevat Nederlandse parafrases, geen letterlijke vertaling of volledig normenkader.

1. Kopieer Bronkaart naar `outputs/wcag-22-bediening/index.html`. Hoofdvraag: “Welke bronvoorwaarden zijn relevant voor onze bedieningscontrole?” Doelgroep FAB, gebruiksmoment overleg; lokale inhoudelijk eigenaar onbekend, lokale toets niet uitgevoerd, herziening bij bron-/applicatiewijziging. Verwijs voor formele toetsing naar de bevoegde lokale eigenaar.
1. Vervang masthead, documentomvang, fictieve evaluatie, pilot-/tijdwinstclaims, demo-versie en alle vijf demo-topics. Maak bijvoorbeeld drie topics met IDs `keyboard`, `focus`, `local-check`. Werk `selectedId`, reset en statische ankers mee bij. Vermeld nadrukkelijk dat slechts twee criteria behandeld worden.
1. Vul de velden volgens deze kaart; verrijk de renderer met een veilig opgebouwd bronanker indien nodig. Houd dezelfde kaart en detailopzet, maar maak geen ontbrekend veld kunstmatig zeker.

| Topic / veld                         | Inhoud uit bron of interpretatie                                                 | Status                                         |
| ------------------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------- |
| `keyboard.label` / `summary`         | Toetsenbordbediening; parafrase van 2.1.1 met de uitzondering behouden           | Bronvoorwaarde, lokale uitvoering onbekend     |
| `keyboard.fragment` en bronlink      | Korte parafrase plus vaste URL met `#keyboard`; label “parafrase”                | Geen verzonnen letterlijk citaat               |
| `focus.label` / `summary` / bronlink | Zichtbare focus; parafrase van 2.4.7 en URL met `#focus-visible`                 | Bronvoorwaarde, lokale toets niet uitgevoerd   |
| `local-check.bullets`                | Voorstel: doorloop relevante controles met toetsenbord en leg uitkomst/bron vast | Voorstel van de visual, geen W3C-testresultaat |
| `local-check.fragment`               | Geen lokaal testverslag beschikbaar; inhoudelijk eigenaar nog aan te wijzen      | Onbekend; geen groene acceptatiestatus         |

4. Verwijder de oude fictieve bronpassages en eventuele irrelevante demoverwijzingen. Voeg dezelfde drie topics met bronlinks als statisch register toe; toon dat ook in print en zonder JavaScript. Voeg geen betrouwbaarheidsscore of percentage “WCAG-conform” toe.
1. Test zoektermen voor beide criteria, alle drie selecties, volgende/reset, onbekende lokale status, special characters en lang bronlabel. Controleer mobiel, toetsenbord, print en no-JS. Lever de beperkte scope, bronversie en werkelijk uitgevoerde checks mee.

## Verificatie van een gegenereerde kopie

De bestaande suite scant `visuals/`, niet `outputs/`. Gebruik het bestaande Playwright/Chrome-patroon uit [test/README.md](../test/README.md) voor gerichte checks op het **expliciete uitvoerpad**, bijvoorbeeld in een tijdelijk script buiten de repository. Maak geen permanente test die een gebruikersrapport of vaste uitvoerslug vereist.

| Controle                   | Acceptatie                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bron en restanten          | Iedere claim heeft een vindplaats of is zichtbaar interpretatie/voorstel/onbekend. Zoek ook in scripts en export naar oude demo-titel, RFC, datum, fictieve quotes, score- en pilotclaims.                                                                                                                                                                                          |
| Samenhang                  | Alle selecties, vraagdieptes, zoek-/filterroutes en vervolgvraagdoelen werken; tellingen en begin/resetselectie kloppen bij andere aantallen. Lege zoekuitkomst en ontbrekend bewijs breken de view niet.                                                                                                                                                                           |
| Veilige tekst              | Lange tekst, `&`, quotes, `<`, backticks en `</script>` worden als tekst getoond; geen geïnjecteerde tags, handlers of scripts. Bronlinks hebben bedoelde veilige doelen.                                                                                                                                                                                                           |
| Regels                     | Onbekend, afkeuring en gewijzigde bron leiden niet tot schijnakkoord. Alleen toelaatbare opties rangschikken; drempels/grenswaarden volgen dezelfde brondefinitie.                                                                                                                                                                                                                  |
| Export en reset            | Indien aanwezig: scherm en export dezelfde bron, status, onzekerheid en regels; kopieerweigering geeft bereikbare tekst. Reset herstelt de bedoelde bron-/simulatietoestand en focus.                                                                                                                                                                                               |
| Browser en bestanden       | Geen JavaScript-fouten, dubbele DOM-ID’s, onbedoelde externe requests of kapotte lokale links/fragmenten. Verplaats kopie voor controle buiten de checkout.                                                                                                                                                                                                                         |
| Mobiel en toetsenbord      | Geen documentbrede overloop bij 320/390 pixels. Gewijzigde controles bereikbaar met Tab/Enter; filters/tabs behouden bruikbare focus. Bekijk ook een desktopscreenshot.                                                                                                                                                                                                             |
| Zonder JavaScript en print | Alle kritieke broninhoud/voorwaarden in lijst of tabel leesbaar; geen lege panelen als enige informatiebron. Print alle noodzakelijke details, ook buiten huidige selectie. Geef de toegevoegde leeslaag expliciet een leesbare printtekstgrootte (bijvoorbeeld 11 pt); enkele operationele printstijlen erven kleine tekst. Inspecteer een PDF; meerdere pagina’s zijn toegestaan. |

Voer tooling alleen uit als beschikbaar en rapporteer anders de beperking. De ontwikkeldependencies zijn geen HTML-runtimevereiste. Browserchecks bewijzen geen volledige toegankelijkheid, juridische naleving, inhoudelijke acceptatie, bereikbaarheid van een echt noodplan of gebruikerswaarde.

**Oplevering:** klikbaar uitvoerpad; gekozen origineel; bronversie/peildatum en scope; controles met uitkomst; inhoudelijk onbekende zaken en niet uitgevoerde checks. Publicatie, delen en formele besluiten blijven afzonderlijke opdrachten.

De uitgevoerde controles bij introductie van deze gids staan in [het validatierapport](template-reuse-validation.md). Historische proeven vervangen geen controle van een nieuwe bronkopie.
