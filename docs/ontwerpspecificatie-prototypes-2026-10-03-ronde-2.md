# Ontwerpspecificatie: drie FAB-prototypes van 3 oktober 2026, tweede ronde

Deze specificatie is de bouwopdracht voor [Escalatiekaart](../visuals/incident_en_continuiteit/fab-escalatiekaart.html), [Risk & Control Map](../visuals/wijziging_en_acceptatie/fab-risk-control-map.html) en [Pilot Cockpit](../visuals/wijziging_en_acceptatie/fab-pilot-cockpit.html). Ze legt vormgeving, synthetische data, regels en verwachte uitkomsten vast. De HTML is leidend; bij verschil geldt het bestand. [AGENTS.md](../AGENTS.md) blijft de centrale bron voor projectafspraken. De regressietests staan in `test/test_task_views.py` en `test/test_pages.py`.

Alle data is synthetisch. Peilen, drempels, kansklassen, meetdefinities en termijnen (90 dagen contactroute, 12,0 % succesgrens, noemer 40) zijn demo-afspraken, geen lokaal vastgestelde normen.

## Gemeenschappelijk

Volg exact het gemeenschappelijke patroon uit de [eerste ronde](ontwerpspecificatie-prototypes-2026-10-03.md#gemeenschappelijk-volg-het-patroon-van-visualswijziging_en_acceptatiefab-test-coverage-maphtml): inline CSS/JS, geen externe requests of webfonts, `.skip`-link, demo-strook, `.interactive` alleen met `body.ready` en niet in print, `#reset` ("Herstel beginstand"), `#copy`, `#print` ("Druk af"), `#message` role=status, verborgen `#export` met readonly `#export-text`, identiek kopieergedrag en exportvorm (> 800 tekens, eerste regel `<naam> / <casus> / demo v1 / revisie 2026-10-03`, `Exportmoment`, regel met "Uitsluitend simulatie", slotregel "FAB adviseert; bevoegde rollen besluiten. Echte acties blijven in de bronregistratie."), `data-action` op alle simulatieknoppen, statische `.reference` met volledig register en één `<details>` "Taak, bronbeheer en grenzen" (alinea's **Gebruiker en uitkomst**, **Bron**, **Regels**, **Praktijktoets**), `<nav aria-label="Gerelateerde views">`, `.foot`, status altijd in woorden, focus zichtbaar, knoppen ≥ 44 px, `prefers-reduced-motion`, geen overflow bij 320/390 px, unieke ID's, alleen eigen data in `innerHTML`, datums in UTC als JJJJ-MM-DD, peildatum 2026-10-03.

Stijlverboden: geen `text-transform:uppercase`, geen monospace, geen `A · B · C`-metastrings (ook niet tussen links), geen `→` achter link- of knoptekst, geen identieke afgeronde kaarten met grijze schaduw, geen gradient-washes, geen #111/#0b0b0b. Eén opvallend element per pagina; de rest rustig. Regellengte < 75ch. Getallen in Nederlandse notatie (komma als decimaalteken) waar percentages verschijnen.

______________________________________________________________________

## 1. Escalatiekaart

Bestand: `visuals/incident_en_continuiteit/fab-escalatiekaart.html`
Title: "FAB Escalatiekaart — wie moet nu handelen?"
Demo-strook: links "FAB / Escalatiekaart", rechts "Synthetische demonstratie, geen contactregistratie"
H1: "Wie moet nu handelen, en met welke informatie?"
Intro: "Geef aan wat je over de verstoring weet. Het peil laat zien welke rol aan zet is en wat het escalatiepakket moet bevatten. Een overdracht telt pas als de ontvanger die heeft aangenomen."
Meldingsblok: "INC-DEMO-0427, ontvangen 2026-10-03 06:52" / citaat: "Op de afdelingen Esdoorn en Hazelaar laadt de medicatieaftekenlijst niet. Collega's tekenen nu niets af." / "Woonzorglocatie De Linde (fictief), ECD 2026.3. Gebruiksmoment: uitvoering bij triage en overleg, of opleiding."
Contextregel onder het meldingsblok: "Peilen, rollen en contactroutes zijn demo-afspraken. Een contactroute die langer dan 90 dagen niet is geverifieerd, telt als verouderd."
Werksectie-h2: "Peilschaal van de escalatie"

### Visueel concept: peilschaal

Een Nederlandse waterpeilschaal is het opvallende element. Links staat een staande schaal (± 120 px breed) met afwisselend rode en witte segmenten, per peil een groot cijfer 0–3 in de displayletter. Rechts van de schaal liggen vier peilrijen, van boven naar onder peil 3, 2, 1, 0, zodat het water van onder naar boven stijgt. Het water vult de schaalkolom van onderen tot en met de rij van het hoogste actieve peil (`--sea`, licht doorschijnend over de rode markering) en eindigt in een dunne golflijn (inline SVG) die horizontaal over de bovenrand van die peilrij doorloopt. De rijen hebben een eigen effen achtergrond, zodat tekst nooit op water staat; rijen onder de waterlijn krijgen een linkerrand in `--sea`. De hoogte verandert alleen na een gebruikersactie (transition ± .4s), uit bij reduced motion.

Onder de schaal staat een losse, smallere zijtak: "Parallel: privacy", met een eigen kleine schaal met de letter P. Die zijtak loopt naast de peilen en verhoogt het peil niet.

Rechts (≥ 1100 px, sticky) of onder de schaal (smaller) staat het pakketpaneel `#package`.

Tokens:

- `--foam:#E3EBE8` (pagina)
- `--paper:#FFFFFF` (rijen, panelen)
- `--sea:#2E5E66` (water, waterlijn, randen)
- `--shallow:#BFD3D1` (lichte watertint, niet-actieve schaal)
- `--mark:#C21F32` (rode schaalmarkering; mag ook als waarschuwingstekst op wit)
- `--ink:#18272B`
- `--silt:#5C6E6B` (secundaire tekst)
  Type: display `"PT Sans Narrow","Arial Narrow","Bahnschrift Condensed",sans-serif` gewicht 700 (h1, h2, peilcijfers, rolnamen); body `"Verdana","Tahoma","Segoe UI",sans-serif` 15.5px/1.6. Links uitgelijnd.

```
FAB / Escalatiekaart                         Synthetische demonstratie, geen ...
Wie moet nu handelen,            | INC-DEMO-0427, ontvangen ...
en met welke informatie?         | "Op de afdelingen ..."
[Vastgestelde gevolgen: □hinder □zorg □privacy □financieel] [Oorzaak][Werkwijze][Duur] [Herstel][Kopieer][Druk af]
+--schaal--+ +-- Peil 3 Continuïteit ------------------+  +-- Escalatiepakket --+
|    3     | | rol, taak, route, overdracht, acties    |  | velden met vinkjes  |
|▒▒▒ 2 ▒▒▒~~~~ Peil 2 Opschalen  (waterlijn) ~~~~~~~~~~|  | ...                 |
|▒▒▒ 1 ▒▒▒| | Peil 1 Analyseren                        |  +---------------------+
|▒▒▒ 0 ▒▒▒| | Peil 0 Registreren                       |
+----------+ +-----------------------------------------+
+-P-+ Parallel: privacy ...
#verdict  ...
```

< 700 px: schaal 48 px breed met alleen cijfers; rij-inhoud stapelt; pakket onder de schaal. Print: geen water of golflijn, alle peilen en de zijtak als tekst met status.

### Controles

- `fieldset.impact` met legend "Vastgestelde gevolgen" en checkboxes `input[data-impact]`: `hinder` "Hinder bij het werk", `zorg` "Zorgondersteuning stilgevallen", `privacy` "Mogelijk privacyrisico", `financieel` "Mogelijke financiële gevolgen". Standaard niets aangevinkt.
- `#cause` "Vermoedelijke oorzaak": `unknown` "Nog onbekend" (standaard), `local` "Lokale inrichting", `vendor` "Leverancierssoftware", `chain` "Koppeling of ketenpartner".
- `#workaround` "Goedgekeurde werkwijze": `unknown` "Nog niet nagegaan" (standaard), `applied` "Beschikbaar en toegepast", `none` "Niet beschikbaar".
- `#duration` "Duur tot nu": `lt1` "Korter dan 1 uur" (standaard), `1to4` "1 tot 4 uur", `gt4` "Langer dan 4 uur".
- Pakketvelden in `#package`: `input[data-field="f1"]` … `f18`, label = veldnaam, toelichting "Aanwezig in de melding". Eén gedeelde set `present` (dezelfde melding, geen tweede administratie). Het paneel toont de velden van het hoogste actieve peil (cumulatief) en, als de zijtak actief is, daaronder de privacyvelden.
- Peilrij: `[data-level="l0"]` … `l3`, zijtak `[data-level="pv"]`; status in `.state`, overdracht in `.handover`, route in `.route`.
- Per actieve rij l1, l2, l3, pv (niet l0):
  - `data-action="verify"` "Simuleer verificatie van de contactroute": route.verified = 2026-10-03, door "FAB (demo)". Disabled als de route actueel is.
  - `data-action="send"`: l1, l2, pv "Simuleer overdracht"; l3 "Simuleer start continuïteitsproces".
  - `data-action="accept"` "Simuleer aanname door <rol>". Alleen enabled bij status verstuurd.

### Data

| id  | titel                 | rol                                              | taak                                                                                              | contactroute (demo)                                                    | geverifieerd | pakketvelden |
| --- | --------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------ | ------------ |
| l0  | Peil 0 — Registreren  | Servicedesk                                      | Registreert de melding en doet de eerste triage.                                                  | Servicedesk-wachtrij in de meldingsregistratie (demo)                  | 2026-09-01   | f1–f4        |
| l1  | Peil 1 — Analyseren   | FAB zorgdossier                                  | Analyseert, zoekt een bekende fout en beoordeelt een goedgekeurde werkwijze.                      | FAB-wachtrij zorgdossier (demo)                                        | 2026-09-20   | f5–f8        |
| l2  | Peil 2 — Opschalen    | Applicatie-eigenaar zorgdossier                  | Beslist over prioriteit en de inzet van leverancier of integratiebeheer. FAB stelt het pakket op. | Leveranciersportaal, contractroute (demo)                              | 2026-05-14   | f9–f12       |
| l3  | Peil 3 — Continuïteit | Continuïteitscoördinator met proceseigenaar zorg | Start de lokaal goedgekeurde noodwerkwijze. De analyse loopt intussen door.                       | Bereikbaarheidsdienst continuïteit (demo), ook buiten het ECD vindbaar | onbekend     | f13–f15      |
| pv  | Parallel — Privacy    | Privacy officer via de lokale datalekprocedure   | Beoordeelt of er sprake is van een datalek. FAB beslist dat niet zelf.                            | Lokale datalekprocedure (demo)                                         | 2026-08-30   | f16–f18      |

Partner bij l2, afhankelijk van `#cause`: `vendor` → "Leverancier via de contractroute"; `chain` → "Integratiebeheer en ketenpartner"; `unknown` of `local` → "Technisch beheer; oorzaakrichting nog vaststellen".

Velden:

- f1 "Meldingsnummer en tijdstip", f2 "Rol van de melder, geen naam", f3 "Applicatie en versie", f4 "Wat de melder ziet, in eigen woorden"
- f5 "Getroffen zorgproces en afdelingen", f6 "Soort gevolg: hinder, zorg, privacy of financieel", f7 "Sinds wanneer, en of het nog loopt", f8 "Al genomen stappen en hun uitkomst"
- f9 "Stappen om het te reproduceren", f10 "Omgeving en versie waarin het optreedt", f11 "Voorbeeldreferentie zonder cliëntgegevens" (met vaste waarschuwing "Stuur geen namen, BSN, medische gegevens of volledige logs mee."), f12 "Aantal getroffen afdelingen of locaties"
- f13 "Welk zorgproces stilligt en waar", f14 "Verwijzing naar het goedgekeurde noodplan", f15 "Verwachte duur, of onbekend"
- f16 "Soort gegevens, zonder inhoud", f17 "Welke rollen mogelijk toegang hadden", f18 "Genomen beheersmaatregel"

Vereiste velden: l1 = f1–f8; l2 = f1–f12; l3 = f1–f15; pv = f1, f3, f16–f18.

### Regels (één functie `peil()`; schaal, rijen, pakket, oordeel en export gebruiken die)

1. Geen gevolg aangevinkt → hoogste peil 0; reden "Nog geen gevolg vastgesteld."
1. Een gevolg aangevinkt → l1 actief; reden "Er is een gevolg vastgesteld."
1. `cause` is `vendor` of `chain` → l2 actief; reden "De oorzaak ligt vermoedelijk bij de leverancier." respectievelijk "… bij een koppeling of ketenpartner."
1. `duration` is `gt4` en `workaround` is niet `applied` → l2 actief; reden "Langer dan 4 uur zonder toegepaste werkwijze."
1. `zorg` aangevinkt → l3 actief; reden "Zorgondersteuning is stilgevallen: start het continuïteitsproces nu, ook als de analyse nog loopt."
1. `privacy` aangevinkt → pv actief; reden "Mogelijk privacyrisico: leg dit parallel voor via de datalekprocedure."
1. `financieel` aangevinkt → geen extra peil; notitie "Mogelijke financiële gevolgen: vermeld dit in het pakket. De proceseigenaar financiën beoordeelt de gevolgen."

Hoogste peil = hoogste actieve van l1–l3, anders 0. Rijstatus (`.state`): hoogste actief → "Nu aan zet"; l0 bij hoogste peil ≥ 1 en andere actieve lagere peilen → "Betrokken"; niet actief → "Niet nodig volgens demo-regels"; pv actief → "Parallel aan zet". Een eerder overgedragen peil dat niet meer actief is, houdt zijn overdracht en toont "Niet nodig volgens demo-regels; eerder overgedragen, trek in via de bronregistratie".

Route actueel = geverifieerd bekend en (peildatum − geverifieerd) ≤ 90 dagen. Routetekst (`.route`): "<naam>. Geverifieerd <datum>" / "<naam>. Verouderd: laatst geverifieerd <datum>" / "<naam>. Niet geverifieerd".

Overdracht per peil (l1, l2, l3, pv): `none` → `sent` → `accepted`.

- l1, l2, pv: `send` alleen enabled als alle vereiste velden aanwezig zijn én de route actueel is.
- l3: `send` altijd enabled zolang l3 actief en status `none` is. Bij directe zorgimpact wacht de start niet op een volledig pakket of geverifieerde route.
- Een vereist veld uitvinken terwijl status `sent` of `accepted` is → status `none` met vlag `voided`. Een veld aanvinken maakt niets ongeldig.
- Overdrachtstekst (`.handover`):
  - `none`: "Nog niet overgedragen", plus bij een geblokkeerde verzending de eerste reden: "Pakket onvolledig: <n> ontbreken" of anders "Contactroute verouderd" / "Contactroute niet geverifieerd". Bij `voided` in plaats daarvan: "Pakket gewijzigd na overdracht; eerdere overdracht vervalt".
  - `sent`: l1/l2/pv "Overgedragen, nog niet aangenomen"; l3 "Continuïteitsproces gestart (simulatie), nog niet bevestigd door de coördinator", aangevuld met "Pakket onvolledig: <n> ontbreken. Vul aan tijdens de overdracht." en/of "Contactroute niet geverifieerd: gebruik de route uit het lokaal goedgekeurde noodplan." waar dat geldt.
  - `accepted`: "Aangenomen door <rol> (simulatie), 2026-10-03".

Oordeel `#verdict` (aria-live polite):

- Peil 0: "Peil 0. De servicedesk registreert en doet de eerste triage. Leg eerst vast welk gevolg de verstoring heeft."
- Anders: "Peil <n>. Nu aan zet: <rol>" (bij l2 met " (<partner>)") ". Volgende stap: <stap>." Stap: geblokkeerd door pakket → "vul het pakket aan (<n> ontbreken)"; geblokkeerd door route → "verifieer de contactroute"; `none` en mogelijk → "draag over met het pakket"; l3 `none` → "start het continuïteitsproces nu en vul het pakket aan tijdens de overdracht"; `sent` → "wacht op aanname en blijf eigenaar van de melding tot die er is"; `accepted` → "volg de afspraken van <rol>; de melding blijft in de bronregistratie".
- Zijtak actief: extra regel "Parallel: privacy officer via de datalekprocedure, <overdrachtstekst>."
- Lijst `<ul>` met alle redenen, daarna de financiële notitie als die geldt, en altijd: "Peilen en drempels zijn demo-afspraken, geen lokaal escalatiebeleid."

### Verwachte uitkomsten (worden getest)

- Begin: l0 `.state` "Nu aan zet"; l1–l3 "Niet nodig volgens demo-regels"; `#verdict` bevat "Peil 0".
- `hinder` aan → l1 "Nu aan zet", l0 "Betrokken"; l1 `send` disabled, `.handover` bevat "Pakket onvolledig: 8 ontbreken".
- f1–f8 aan → l1 `send` enabled; send → "Overgedragen, nog niet aangenomen"; accept → bevat "Aangenomen door FAB zorgdossier".
- f6 uit → l1 `.handover` "Pakket gewijzigd na overdracht; eerdere overdracht vervalt".
- f6 weer aan, `cause` = `vendor` → l2 "Nu aan zet", l1 "Betrokken", `#verdict` bevat "Leverancier via de contractroute"; f9–f12 aan → l2 `send` nog disabled, `.route` bevat "Verouderd: laatst geverifieerd 2026-05-14"; verify → `send` enabled.
- Reset, `hinder` aan, `duration` = `gt4` → l2 "Nu aan zet" met "Technisch beheer; oorzaakrichting nog vaststellen"; `workaround` = `applied` → l1 "Nu aan zet".
- Reset, alleen `zorg` aan → l3 "Nu aan zet"; l3 `send` enabled met leeg pakket; na send bevat `.handover` "Continuïteitsproces gestart" en "Pakket onvolledig: 15 ontbreken"; `.route` bevat "Niet geverifieerd".
- `privacy` aan → pv "Parallel aan zet"; `#verdict` bevat "datalekprocedure".
- Export begint met "Escalatiekaart / INC-DEMO-0427 / demo v1 / revisie 2026-10-03" en bevat per peil rol, status, route en overdracht, plus de aanwezige en ontbrekende velden.
- Reset → beginstand, alle vinkjes en overdrachten gewist.

Statisch register: `.register article` × 5 (`id="esc-static-l0"`, `-l1`, `-l2`, `-l3`, `-pv`) met rol, taak, wanneer het peil actief wordt (regel in woorden), contactroute met verificatiedatum en status op de peildatum, vereiste velden en de overdrachtsregel. Daarnaast één alinea met de regels in volgorde.

Taak-details: **Gebruiker en uitkomst:** FAB bij triage en ketenproblemen, met servicedesk, applicatie-eigenaar en continuïteitscoördinator; de uitkomst is een volledig escalatiepakket en een aangenomen overdracht, geen besluit over prioriteit, datalek of noodwerkwijze. **Bron:** synthetische rollen en contactroutes, demo v1, revisie 2026-10-03; de echte contact- en escalatieregistratie en de bronhouder (coördinator incident- en continuïteitsproces) zijn niet vastgesteld; deze kaart is geen tweede adresboek. Herzie bij een gewijzigde rol, contractroute of noodplan; verifieer routes minstens elk kwartaal (demo). **Regels:** gevolgen bepalen het peil, niet het aantal melders; bij stilgevallen zorgondersteuning start het continuïteitsproces direct; privacy loopt parallel; overgedragen is pas aangenomen na bevestiging; een gewijzigd pakket maakt een eerdere overdracht ongeldig; verouderde routes blijven zichtbaar. **Praktijktoets:** vergelijk met de huidige escalatielijst en het noodplan op juiste rol, volledigheid van het pakket, zoektijd en herkenning van verouderde routes.

Nav: `incident-onepager.html` "Van melding naar oplossing", `fab-known-error-map.html` "Bekende fouten", `fab-continuiteitskaart.html` "Continuïteit en noodwerkwijze", `fab-serviceradar.html` "Serviceradar".

______________________________________________________________________

## 2. Risk & Control Map

Bestand: `visuals/wijziging_en_acceptatie/fab-risk-control-map.html`
Title: "FAB Risk & Control Map — welk risico blijft over?"
Demo-strook: links "FAB / Risk & Control Map", rechts "Synthetische demonstratie, geen risicoregister"
H1: "Welk risico blijft over als de maatregelen echt zijn getoetst?"
Intro: "Elke rij volgt één risico door zijn maatregelen. Alleen een getoetste, werkzame maatregel maakt de lijn dunner of het gevolg kleiner. Een voorgenomen of alleen uitgevoerde maatregel laat het risico ongemoeid, hoe overtuigend het plan ook is."
Contextblok: "Teamindeling per wijk" / "RFC-2026-118, ECD 2026.4, beoogde livegang 2026-11-02" / "Risicoanalyse demo v1, revisie 2026-10-03. Kansklassen en gevolgsoorten zijn demo-afspraken, geen lokaal risicobeleid." / "Gebruiksmoment: overleg bij impactanalyse en overdracht."
Werksectie-h2: "Risico's door hun maatregelen"

### Visueel concept: Zwitserse-kaasmodel

Het kaasmodel van Reason, bekend uit patiëntveiligheid, is het opvallende element. Per risico een doorsnede (inline SVG, `viewBox` ± 640×150, schaalt mee; geen tekst in de SVG): links een kleine bronmarkering, dan per maatregel een staande plak (afgeronde parallellogram, lichte schuinte), rechts een gevolgvlak. Een horizontale risicolijn in `--hazard` loopt van links naar rechts door alle plakken.

- Voorgenomen: alleen gestippelde omtrek in `--ink`, geen vulling; de lijn loopt ongehinderd door.
- Uitgevoerd, niet getoetst of gewijzigd: vulling `--cheese` op ± 45 % dekking, met een gat precies op de lijn; de lijn gaat door het gat.
- Getoetst, werkzaam: volle vulling, randkleur `--rind`, geen gat op de lijn; na deze plak wordt de lijn dunner als de maatregel de kans verlaagt. De lijn stopt nooit: restrisico is nooit nul.
- Getoetst, niet werkzaam: volle vulling met een groot gat op de lijn.
- Elke plak heeft twee of drie vaste decoratieve gaten buiten de lijn.
  Lijndikte per segment volgt de aangetoonde kans tot dat punt: hoog 22, midden 13, laag 5. Een overgang in dikte of vulling alleen na een gebruikersactie, uit bij reduced motion.

Onder elke doorsnede een HTML-lijst van de maatregelen in dezelfde volgorde, met status in woorden, en rechts het restrisicoblok. Niets in de SVG is de enige informatiedrager.

Tokens:

- `--steel:#E6EBEF` (pagina)
- `--paper:#FBFCFD` (risicorijen)
- `--cheese:#E2B13C` (plakken)
- `--rind:#B5841C` (plakrand)
- `--ink:#1F2A36`
- `--hazard:#9E2A1F` (risicolijn; ook tekst "Ernstig restrisico")
- `--muted:#56626E`
  Type: display `"Athelas","Constantia","Hoefler Text",Georgia,serif` (h1 gewicht 500, risicotitels); body `"PT Sans","Corbel","Segoe UI",sans-serif` 17px/1.55. Links uitgelijnd.

```
FAB / Risk & Control Map                     Synthetische demonstratie, geen risicoregister
Welk risico blijft over als ...  | Teamindeling per wijk, RFC-2026-118 ...
[Herstel][Kopieer][Druk af]                            #tally: 3 risico's: ...
R1 Medewerker ziet cliënten buiten de eigen wijk               | Aangetoond restrisico
 ●══════[ plak C1 ]════[ plak C2 ]══════▶ gevolg                | Midden, privacyrisico
 C1 Rolmodel per wijk ingericht  Uitgevoerd, niet getoetst  [..] | Verwacht als alles werkt: ...
 C2 Inzage buiten wijk ...       Voorgenomen                [..] | [Simuleer acceptatie ...]
```

< 760 px: restrisicoblok onder de doorsnede, maatregelacties stapelen. Print: SVG mag blijven (zwart-wit leesbaar), alle statussen als tekst.

### Data

Kansklassen in volgorde: `laag` < `midden` < `hoog`. Gevolgsoorten zijn niet geordend; een maatregel die het gevolg beperkt, noemt het nieuwe gevolg expliciet.

| risico | titel                                                 | inherente kans | inherent gevolg                | risico-eigenaar (voorgestelde rol) | accepteert restrisico (voorgestelde rol) |
| ------ | ----------------------------------------------------- | -------------- | ------------------------------ | ---------------------------------- | ---------------------------------------- |
| R1     | Medewerker ziet cliënten buiten de eigen wijk         | midden         | Privacyrisico                  | Gegevenseigenaar cliëntdossier     | Gegevenseigenaar met privacy officer     |
| R2     | Onbekende teamcode in het ketenbericht naar financiën | hoog           | Financiële gevolgen            | Proceseigenaar financiën           | Proceseigenaar financiën                 |
| R3     | Wijkplanning toont lege diensten na de overgang       | midden         | Stilgevallen zorgondersteuning | Proceseigenaar zorg wijkteams      | Proceseigenaar zorg wijkteams            |

| maatregel | risico | naam                                                           | verwacht effect                                    | beginstatus | bewijs bij start                                                                                             |
| --------- | ------ | -------------------------------------------------------------- | -------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| C1        | R1     | Rolmodel per wijk ingericht                                    | kans naar laag                                     | uitgevoerd  | Uitvoering: configuratie-export acceptatie 2026-09-30 (demo). Toets gepland: negatieve autorisatietest T-02. |
| C2        | R1     | Inzage buiten de wijk vraagt een reden en wordt gelogd         | kans naar laag                                     | voorgenomen | Geen.                                                                                                        |
| C3        | R2     | Mappingtabel teamcodes bijgewerkt                              | kans naar laag                                     | werkzaam    | Ketentest K-07, v2, 2026-09-28, beoordeeld door Integratiebeheer (demo), uitkomst werkzaam.                  |
| C4        | R2     | Dagelijkse aansluitcontrole op aantallen                       | gevolg naar Hinder (herstel vóór de declaratierun) | uitgevoerd  | Uitvoering: eerste controle 2026-09-29 (demo). Niet getoetst.                                                |
| C5        | R3     | Overgang buiten piekuren met controlelijst per wijk            | kans naar laag                                     | voorgenomen | Geen.                                                                                                        |
| C6        | R3     | Terugval naar papieren dienstlijst volgens het lokale noodplan | gevolg naar Hinder                                 | voorgenomen | Geen. Toets geblokkeerd: "Toets niet mogelijk: het lokale noodplan ontbreekt in deze demo."                  |

### Controles

Per maatregel `.control[data-control="C1"]` met `.state` en `.evidence`:

- `data-action="execute"` "Simuleer uitvoering": alleen bij voorgenomen → uitgevoerd; bewijs "Uitvoering gemeld 2026-10-03 (simulatie)".
- `data-action="pass"` "Simuleer toets: werkzaam" en `data-action="fail"` "Simuleer toets: niet werkzaam": alleen bij uitgevoerd of gewijzigd, en niet bij C6. Bewijs: "Synthetische toets (simulatie), versie demo, 2026-10-03, beoordeeld door Test-/acceptatieverantwoordelijke (demo), uitkomst werkzaam/niet werkzaam".
- `data-action="change"` "Simuleer gewijzigde maatregel": alleen als de status niet voorgenomen is → status gewijzigd, eerder toetsbewijs vervalt.

Statuslabels: "Voorgenomen", "Uitgevoerd, niet getoetst", "Getoetst, werkzaam", "Getoetst, niet werkzaam", "Gewijzigd, opnieuw toetsen".

Per risico `[data-risk="R1"]` met `.residual`, `.expected` en `.acceptance`:

- `data-action="accept"` "Simuleer acceptatie restrisico door <acceptant>": enabled zolang niet geaccepteerd. Legt vast: aangetoond restrisico op dat moment, datum 2026-10-03 en het aantal niet getoetste maatregelen.
- Elke maatregelactie binnen dat risico maakt een acceptatie ongeldig: "Acceptatie vervallen: maatregel gewijzigd na acceptatie".

### Regels (één functie `residual(risk)`; doorsnede, lijst, telling en export gebruiken die)

- Aangetoond: kans = laagste van de inherente kans en de kanseffecten van maatregelen met status werkzaam; gevolg = gevolgeffect van de laatste werkzame gevolgmaatregel, anders het inherente gevolg.
- Verwacht: dezelfde berekening over alle maatregelen ongeacht status, altijd getoond als "Verwacht als alle maatregelen werken: <kans>, <gevolg>. Niet aangetoond."
- Ernstig aangetoond restrisico = (gevolg is Privacyrisico of Stilgevallen zorgondersteuning en kans is niet laag) of kans is hoog. Tekst in `.residual`: "Aangetoond restrisico: <Kans>, <gevolg>" plus bij ernstig "Ernstig restrisico: vraagt een expliciet besluit vóór livegang".
- Acceptatietekst: "Geaccepteerd (simulatie): aangetoond restrisico <kans>, <gevolg>, door <acceptant>, 2026-10-03" plus bij open maatregelen "; nog niet getoetste maatregelen: <n>". Zonder acceptatie: "Restrisico nog niet geaccepteerd".
- `#tally` (aria-live): "<n> risico's: <a> met geaccepteerd restrisico, <b> zonder acceptatie, <c> met ernstig aangetoond restrisico. <d> van <e> maatregelen getoetst." Getoetst = werkzaam of niet werkzaam. Geen score of percentage.

### Verwachte uitkomsten (worden getest)

- Begin: R1 `.residual` bevat "Midden, privacyrisico" en "Ernstig restrisico"; R1 `.expected` bevat "Laag, privacyrisico"; R2 `.residual` "Laag, financiële gevolgen", geen "Ernstig"; R3 `.residual` "Midden, stilgevallen zorgondersteuning" en "Ernstig"; C6 `pass` en `fail` disabled, C6 tekst bevat "noodplan ontbreekt"; `#tally` "3 risico's: 0 met geaccepteerd restrisico, 3 zonder acceptatie, 2 met ernstig aangetoond restrisico. 1 van 6 maatregelen getoetst."
- C1 pass → R1 "Laag, privacyrisico", niet ernstig; `#tally` bevat "1 met ernstig" en "2 van 6".
- Accept R1 → `.acceptance` bevat "Geaccepteerd (simulatie)" en "nog niet getoetste maatregelen: 1"; daarna C2 execute → "Acceptatie vervallen".
- C4 fail → C4 "Getoetst, niet werkzaam"; R2 blijft "Laag, financiële gevolgen".
- C3 change → C3 "Gewijzigd, opnieuw toetsen"; R2 "Hoog, financiële gevolgen" en "Ernstig".
- C6 execute → status "Uitgevoerd, niet getoetst"; `pass`/`fail` blijven disabled.
- Export begint met "Risk & Control Map / RFC-2026-118 / demo v1 / revisie 2026-10-03" en bevat per risico aangetoond en verwacht restrisico, maatregelen met status en bewijs, en acceptatie.
- Reset → beginstand.

Weergave in zinnen: kans met hoofdletter ("Midden, privacyrisico"); gevolg in kleine letters na de komma.

Statisch register: `.register article` × 3 (`id="risk-static-R1"` …) met inherente kans en gevolg, maatregelen met verwacht effect, beginstatus en bewijs, aangetoond en verwacht restrisico op de peildatum, risico-eigenaar, acceptant en open punten. Daarnaast één alinea met de rekenregels.

Taak-details: **Gebruiker en uitkomst:** FAB bij impactanalyse en overdracht, samen met risico-eigenaren; de uitkomst is een zichtbaar restrisico en een besluitvraag aan de bevoegde rol. FAB accepteert geen restrisico. **Bron:** synthetische risicoanalyse, demo v1, revisie 2026-10-03; het echte risicoregister of wijzigingsdossier en de bronhouders zijn niet vastgesteld. Herzie bij een gewijzigde maatregel, een nieuwe toets of vóór het Go/No-Go-moment. **Regels:** alleen een getoetste, werkzame maatregel verlaagt het aangetoonde restrisico; verwacht is niet aangetoond; een wijziging na acceptatie maakt die acceptatie ongeldig; geen totaalscore. **Praktijktoets:** vergelijk met de huidige risicoparagraaf in het wijzigingsdossier op gemiste ongeteste maatregelen, juiste acceptant en herkenning van vervallen acceptaties.

Nav: `fab-change-impact-map.html` "Change Impact Map", `fab-test-coverage-map.html` "Testsporen en bewijs", `fab-go-no-go-cockpit.html` "Go/No-Go", `fab-beheerbaarheid-scan.html` "Beheerbaarheid Scan".

______________________________________________________________________

## 3. Pilot Cockpit

Bestand: `visuals/wijziging_en_acceptatie/fab-pilot-cockpit.html`
Title: "FAB Pilot Cockpit — helpt de proef echt?"
Demo-strook: links "FAB / Pilot Cockpit", rechts "Synthetische demonstratie, geen meetregistratie"
H1: "Vermindert de proef het probleem echt?"
Intro: "De proef is vooraf vastgelegd: hypothese, meting, nulmeting en stopcriteria. Alleen gecontroleerde meetweken tellen mee. Een stopcriterium dat niet is gemeten, is niet groen maar onbekend."
Contextblok: "Gestructureerde nachtoverdracht op de tablet" / "PILOT-DEMO-04, teams Esdoorn en Hazelaar, woonzorglocatie De Linde (fictief)" / "Looptijd 8 weken vanaf 2026-08-10, peilmoment na week 7. Plan demo v1, revisie 2026-10-03." / "Pilot-eigenaar: proceseigenaar zorg (voorgestelde rol). FAB beheert de inrichting en levert de meetgegevens aan. Gebruiksmoment: pilotoverleg."
Werksectie-h2: "Meetweken op millimeterpapier"

Statisch blok "Vooraf vastgelegd" (altijd zichtbaar, ook zonder JS):

- **Hypothese:** "Als de nachtdienst de overdracht invult in het gestructureerde formulier, ontbreekt bij de ochtendoverdracht minder vaak een verplicht onderdeel."
- **Meting:** teller = ochtendoverdrachten met minstens één ontbrekend verplicht onderdeel (medicatie, valrisico, bijzonderheden); noemer = alle ochtendoverdrachten van de teams in die kalenderweek; populatie = cliënten van de genoemde teams; uitsluiting = overdrachten tijdens ECD-uitval volgens noodwerkwijze; bron = steekproefcontrole door de kwaliteitsmedewerker (demo) op het overdrachtsverslag in het ECD.
- **Nulmeting** (2026-07-13 t/m 2026-08-09): pilotteams 46 van 212 (21,7 %); vergelijkingsteams Beuk en Wilg 41 van 198 (20,7 %).
- **Succesgrens:** over minstens 4 meegetelde weken samen is het aandeel bij de pilotteams ten hoogste 12,0 %, én minstens 5,0 procentpunt lager dan bij de vergelijkingsteams over dezelfde weken.
- **Meetellen:** alleen gecontroleerde weken met een noemer van minstens 40 bij de pilotteams; weken 1 en 2 zijn inwerkperiode en tellen niet mee voor de succesgrens. Stopcriteria gelden voor alle weken.

### Visueel concept: millimeterpapier

Het opvallende element is een grafiek op millimeterpapier (inline SVG, `viewBox` ± 720×360): fijne lijnen elke 1 mm-eenheid in `--grid`, dikkere elke 5 in `--grid-major`, op `--paper`. X-as: een smalle kolom "Nulmeting" en daarna weken 1–8; y-as 0–30 %. SVG-tekst alleen voor aslabels (weeknummers, 0/10/20/30 %), minimaal 13 px in viewBox-eenheden.

- Nulmeting pilot: gearceerd horizontaal blok op 21,7 % in de nulmetingkolom.
- Inwerkweken 1–2: kolommen licht gearceerd in `--grid`, met in de legenda "Inwerkperiode, telt niet mee".
- Succesgrens: gestippelde horizontale lijn op 12,0 % in `--graphite`.
- Pilotteams in balpeninkt `--ballpoint`: gecontroleerd en meegeteld = getekend kruisje; aangeleverd, niet gecontroleerd = open cirkel; gecontroleerd maar niet meegeteld (noemer < 40) = cirkel met schuine streep; verbonden met een dunne lijn.
- Vergelijkingsteams in potlood `--graphite`: kleine vierkantjes, gestippelde verbindingslijn; zelfde vulling-logica (open = niet gecontroleerd).
- Weken na de gekozen week (`#week`) en week 8 zonder data verschijnen niet.
  Onder de grafiek een HTML-legenda en een HTML-weeklijst (`.week[data-week="1"]` … `8`) met teller/noemer per groep, status in woorden en acties. Rechts (≥ 1000 px) of onder de grafiek de noodrem (`#brakes`) en het advies.

Tokens:

- `--desk:#DDE5E0` (pagina)
- `--paper:#F7FAF6` (millimeterpapier, panelen)
- `--grid:#B9D8C2`, `--grid-major:#7FB394`
- `--graphite:#3B4045` (tekst, vergelijkingsteams)
- `--ballpoint:#1D4E9E` (pilotteams; ook linkkleur)
- `--stop:#B8360F` (geraakt stopcriterium, alleen naast woorden)
  Type: display `"Baskerville","Baskerville Old Face","Libre Baskerville",Georgia,serif` (h1, h2, adviezen); body `"Lucida Grande","Lucida Sans Unicode","Lucida Sans",Verdana,sans-serif` 15.5px/1.6. Links uitgelijnd.

```
FAB / Pilot Cockpit                         Synthetische demonstratie, geen meetregistratie
Vermindert de proef het       | Gestructureerde nachtoverdracht op de tablet ...
probleem echt?                |
Vooraf vastgelegd: hypothese / meting / nulmeting / succesgrens / meetellen
[Bekijk tot week ──●── 7] [Herstel][Kopieer][Druk af]
+-- millimeterpapier -----------------------+  +-- Noodrem ----------------+
| 30%                                       |  | S1 ... Niet geraakt       |
| 20% ▨▨  ×                                 |  | S2 ... Niet gemeten       |
| 12% ------------------- succesgrens -----  |  +-- Advies -----------------+
|  0%  N   1  2  3  4  5  6  7  8           |  | Nog niet te beoordelen    |
+-------------------------------------------+  +---------------------------+
week 1  Pilot 15 van 54 ...  Gecontroleerd, inwerkperiode  [..]
```

< 760 px: grafiek op volle breedte (schaalt mee), weeklijst stapelt, noodrem en advies onder de grafiek. Print: grafiek blijft, plus weektabel en criteria als tekst.

### Data

| week | pilot teller/noemer | pilot status     | vergelijking teller/noemer | vergelijking status | overdrachtstijd pilot (min, gem.) | servicedeskmeldingen formulier |
| ---- | ------------------- | ---------------- | -------------------------- | ------------------- | --------------------------------- | ------------------------------ |
| 1    | 15 / 54             | gecontroleerd    | 11 / 50                    | gecontroleerd       | 24                                | 6                              |
| 2    | 11 / 52             | gecontroleerd    | 10 / 49                    | gecontroleerd       | 22                                | 4                              |
| 3    | 8 / 55              | gecontroleerd    | 10 / 51                    | gecontroleerd       | 21                                | 2                              |
| 4    | 6 / 53              | gecontroleerd    | 9 / 48                     | gecontroleerd       | 20                                | 1                              |
| 5    | 5 / 51              | gecontroleerd    | 10 / 50                    | gecontroleerd       | 20                                | 1                              |
| 6    | 4 / 38              | aangeleverd      | 9 / 47                     | aangeleverd         | 19                                | 0                              |
| 7    | 5 / 52              | aangeleverd      | 10 / 50                    | aangeleverd         | 19                                | 1                              |
| 8    | —                   | nog niet gemeten | —                          | nog niet gemeten    | —                                 | —                              |

Nulmeting overdrachtstijd: gemiddeld 18 minuten per dienst. Week 6: noemer laag door vakantiesluiting van een afdeling (demo).

Stopcriteria (`#brakes li[data-brake="S1"]` …, status in `.state`):

| id  | criterium                                                                | gevolg bij geraakt | meting bij start                                             |
| --- | ------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------------ |
| S1  | Privacy-incident door het formulier                                      | stoppen            | Gemeten via de meldingsregistratie t/m week 7: geen incident |
| S2  | Overdracht niet beschikbaar bij storing, zonder werkende terugval        | stoppen            | Niet gemeten: terugvaltest niet uitgevoerd                   |
| S3  | Overdrachtstijd stijgt meer dan 10 minuten ten opzichte van de nulmeting | aanpassen          | Berekend over de meegetelde weken: gemiddelde − 18           |
| S4  | Meer dan 6 servicedeskmeldingen over het formulier in één week           | aanpassen          | Berekend over alle zichtbare weken                           |

### Controles

- `#week` range "Bekijk tot week", min 2, max 7, standaard 7; `#week-label` toont "week <n>". Alleen weken ≤ n tellen mee, ook voor stopcriteria S3/S4 en de vergelijking.
- Per week met status aangeleverd: `data-action="control" data-week="<n>"` "Simuleer controle door kwaliteitsmedewerker" → beide groepen gecontroleerd, "Kwaliteitsmedewerker (demo), 2026-10-03".
- Per week met status gecontroleerd: `data-action="correct" data-week="<n>"` "Simuleer correctie van de cijfers" → pilotteller + 2, beide groepen terug naar aangeleverd met toevoeging "gecorrigeerd, opnieuw controleren".
- `data-action="fallback-pass"` "Simuleer terugvaltest: geslaagd" → S2 "Niet geraakt (terugvaltest geslaagd 2026-10-03, simulatie)". `data-action="fallback-fail"` "Simuleer terugvaltest: mislukt" → S2 geraakt. Beide disabled zodra S2 gemeten is.
- `data-action="incident"` "Simuleer privacy-incident in week 7" → S1 geraakt. Disabled na gebruik.

### Regels (één functie `evaluate()`; grafiek, weeklijst, noodrem, advies en export gebruiken die)

1. Meegetelde weken = weken 3 t/m `#week` met pilotstatus gecontroleerd en pilotnoemer ≥ 40. Weekstatus in woorden: "Gecontroleerd, telt mee"; "Gecontroleerd, inwerkperiode, telt niet mee"; "Gecontroleerd, telt niet mee: noemer <n>, minder dan 40"; "Aangeleverd, niet gecontroleerd"; "Gecorrigeerd, opnieuw controleren"; "Nog niet gemeten".
1. Pilot-aandeel = som tellers / som noemers over de meegetelde weken; vergelijking over dezelfde weken (alleen als de vergelijkingsweek ook gecontroleerd is; anders telt die week voor beide groepen niet mee). Toon altijd teller en noemer naast het percentage, één decimaal met komma.
1. Primaire uitkomst:
   - minder dan 4 meegetelde weken → "Nog niet te beoordelen: <k> van minimaal 4 meetweken meegeteld."
   - pilot ≤ 12,0 % en (vergelijking − pilot) ≥ 5,0 procentpunt → "Aanwijzing voor effect: pilot <p> (<t> van <n>), vergelijking <q> (<t2> van <n2>), verschil <d> procentpunt."
   - anders → "Geen aanwijzing voor effect: pilot <p>, vergelijking <q>." Rekenen met onafgeronde waarden.
1. Stopcriteria: S1 en S2 volgens simulatie; S3 geraakt als het gemiddelde van de meegetelde weken − 18 > 10 (zonder meegetelde weken: "Niet gemeten"); S4 geraakt als een zichtbare week meer dan 6 meldingen heeft. Statustekst: "Geraakt", "Niet geraakt (<toelichting>)" of "Niet gemeten". Niet gemeten is nooit niet geraakt.
1. Advies `#advice` (aria-live), in deze volgorde:
   1. een stopcriterium "stoppen" geraakt → "Stoppen en voorleggen aan de pilot-eigenaar."
   1. een criterium "aanpassen" geraakt → "Aanpassen en voorleggen aan de pilot-eigenaar."
   1. primaire uitkomst nog niet te beoordelen → "Nog niet te beoordelen."
   1. geen aanwijzing voor effect → "Geen aanwijzing voor effect: bespreek aanpassen of stoppen."
   1. aanwijzing, maar een criterium niet gemeten → "Aanwijzing voor effect; doorgaan pas na meting van: <criteria>."
   1. anders → "Aanwijzing voor effect; voorleggen voor een besluit over doorgaan."
      Altijd gevolgd door "Advies, geen besluit. De pilot-eigenaar besluit; een aanwijzing is geen bewezen effect."

### Verwachte uitkomsten (worden getest; met de hand nagerekend)

- Begin (week 7): meegeteld weken 3, 4, 5; primaire uitkomst bevat "3 van minimaal 4"; S2 "Niet gemeten"; advies "Nog niet te beoordelen."; week 6 "Aangeleverd, niet gecontroleerd".
- Controle week 6 → week 6 "Gecontroleerd, telt niet mee: noemer 38, minder dan 40"; nog steeds 3 weken.
- Controle week 7 → meegeteld 3, 4, 5, 7: pilot 24 van 211 = 11,4 %, vergelijking 39 van 199 = 19,6 %, verschil 8,2 procentpunt → "Aanwijzing voor effect"; advies bevat "doorgaan pas na meting van" en "Overdracht niet beschikbaar bij storing".
- Daarna fallback-pass → advies "Aanwijzing voor effect; voorleggen voor een besluit over doorgaan."
- Daarna incident → advies "Stoppen en voorleggen aan de pilot-eigenaar."
- Reset, controle week 7, `#week` naar 5 → weer "Nog niet te beoordelen" (alleen 3, 4, 5).
- Reset, controle week 7, correctie week 3 → week 3 "Gecorrigeerd, opnieuw controleren"; meegeteld 4, 5, 7 → "Nog niet te beoordelen".
- S3 beginwaarde over 3, 4, 5: gemiddeld 20,3 min, +2,3 → "Niet geraakt"; S4: hoogste week 6 meldingen (week 1) → "Niet geraakt".
- Export begint met "Pilot Cockpit / PILOT-DEMO-04 / demo v1 / revisie 2026-10-03" en bevat hypothese, meetdefinitie, nulmeting, per week tellers, noemers en status, de primaire uitkomst, alle stopcriteria en het advies.
- Reset → beginstand.

Statisch register: `.register` met een echte `<table>` (caption) met kolommen Week / Pilot teller en noemer / Status / Vergelijking teller en noemer / Status / Overdrachtstijd / Meldingen, één `<tr data-static-week>` per week (8 rijen), plus een lijst van de vier stopcriteria met beginstatus en een alinea met het beginadvies en de rekenregels. In smalle schermen in een `overflow-x:auto`-wrapper zonder documentoverflow.

Taak-details: **Gebruiker en uitkomst:** FAB bij het pilotoverleg met de pilot-eigenaar en de kwaliteitsmedewerker; de uitkomst is een onderbouwd advies om door te gaan, aan te passen of te stoppen. De pilot-eigenaar besluit. **Bron:** synthetische meetweken, demo v1, revisie 2026-10-03; de echte meetregistratie, steekproefmethode en bronhouder zijn niet vastgesteld. Herzie bij iedere meetweek; een gewijzigde meetdefinitie vraagt een nieuwe nulmeting. **Regels:** alleen gecontroleerde weken tellen; percentages altijd met teller en noemer; vergelijking met teams zonder proef; niet gemeten is onbekend, niet groen; gebruik of trainingsdeelname bewijst geen effect. **Praktijktoets:** vergelijk met het huidige pilotverslag op herkenning van ongecontroleerde weken, gemiste stopcriteria en de kwaliteit van het advies.

Nav: `fab-releaseatelier.html` "Releaseatelier", `fab-test-coverage-map.html` "Testsporen en bewijs", `../gegevens_en_ketens/fab-rapportage-lineage.html` "Rapportage Lineage", `../incident_en_continuiteit/fab-continuiteitskaart.html` "Continuïteit en noodwerkwijze".

______________________________________________________________________

## Inventaris en documentatie

- Na toevoeging: **29 HTML-bestanden voor 28 concepten: 23 FAB-concepten en 5 bron- en kennisconcepten**, **7 open kandidaten**. Werk de aantallen bij in `AGENTS.md` (Opzet) en de ideeënnotitie (Bronbeschikbaarheid, Aanvullende templatekandidaten, Status en afbakening).
- Vink in de ideeënnotitie Escalatiekaart, Risk & Control Map en Pilot Cockpit af met een korte beschrijving van de aanwezige interactie en een bestandslink, zoals bij de eerdere ronde. Noem ze in de opsomming van uitgewerkte kandidaten en voeg aan de alinea onder "Drie inhoudelijke prioriteiten" een zin over deze tweede ronde toe met een link naar deze specificatie. Vul de rij "Technisch getest" aan met de nieuwe scenario's.
- Voeg in `docs/template-reuse.md` drie bestandskaarten toe in dezelfde vorm, en neem de patronen op in de selectietabel (incident → Escalatiekaart; wijzigingsdossier → Risk & Control Map en Pilot Cockpit).
- Voeg de drie bestanden toe aan `TASK_FILES` in `test/support.py`, aan `FILES` in `test/test_task_views.py`, aan de print/no-JS-takken in `test/test_pages.py`, en werk de dekkingstabel in `test/README.md` bij.
