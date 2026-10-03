# Ontwerpspecificatie: drie FAB-prototypes van 3 oktober 2026

Deze specificatie is de bouwopdracht voor [Omgevingsvergelijker](../visuals/wijziging_en_acceptatie/fab-omgevingsvergelijker.html), [Known Error / Workaround Map](../visuals/incident_en_continuiteit/fab-known-error-map.html) en [Applicatie Life Cycle Map](../visuals/landschap_en_processen/fab-life-cycle-map.html). Ze legt de gekozen vormgeving, synthetische data, regels en verwachte uitkomsten vast. De HTML is leidend; bij verschil geldt het bestand. [AGENTS.md](../AGENTS.md) blijft de centrale bron voor projectafspraken. De regressietests staan in `test/test_task_views.py` en `test/test_pages.py`.

Na een visuele review zijn de volgende punten anders uitgewerkt dan hieronder beschreven:

- **Omgevingsvergelijker:** de platen zijn grafische balken zonder tekst; waarden staan eronder ("Beide: …" of per omgeving). Rijen die het gekozen testspoor niet raakt, zijn ingeklapt tot één regel zonder simulatieknoppen. Onder 850 px staat het oordeel vóór de lichtbak.
- **Known Error / Workaround Map:** de rode band "Herbeoordeling verlopen" ligt tussen het oogje en het KE-nummer en bedekt geen tekst.
- **Applicatie Life Cycle Map:** het peildatumlabel staat in de jaarrug; labels in de almanak zijn dekkende chips; de doorlooptijd is een aparte liniaal aan de rechterrand van de kolom; de afhankelijkheidslijn tablet-OS → ECD heeft het label "ECD 2026.4 eerst live".

Alle data is synthetisch. Doorlooptijden, de drempel van 8 weken en de regel van 14 dagen voor momentopnamen zijn demo-afspraken, geen lokaal vastgestelde normen.

Uitgangspunten bij de bouw: alle UI-tekst in natuurlijk Nederlands, zinshoofdletter, actieve werkwoorden.

## Gemeenschappelijk (volg het patroon van visuals/wijziging_en_acceptatie/fab-test-coverage-map.html)

Kopieer de *structuur en het no-JS/print-mechanisme* van fab-test-coverage-map.html, NIET de vormgeving:

- `<html lang="nl">`, meta description, title, alles inline (CSS + JS). Geen externe requests, geen webfonts: alleen lokale fontstacks.
- `.skip`-link als eerste focusbaar element naar de werk-sectie; na Enter op skip + Tab moet focus op een SELECT/BUTTON/INPUT landen.
- Smalle demo-strook bovenaan: links "FAB / <naam>", rechts sterk: "Synthetische demonstratie, geen ..." (zie per pagina).
- Interactieve controles in `.interactive`, verborgen zonder JS (zelfde `body.ready`-mechanisme als test-coverage) en in print.
- Knoppen `#reset` ("Herstel beginstand"), `#copy` ("Kopieer ..."), `#print` ("Druk af").
- `#message` role=status. `#export` section (hidden) met `#export-text` readonly textarea. Copy-gedrag exact als test-coverage: success → `#message` bevat "gekopieerd"; weigering/fout → export zichtbaar, focus op `#export-text`, `#message` bevat "Kopiëren niet beschikbaar". Export > 800 tekens, volgt de huidige simulatiestaat (scherm en export uit dezelfde functie), begint met naam / casus / "demo v1 / revisie 2026-10-03", Exportmoment, "Uitsluitend simulatie ...", en eindigt met "FAB adviseert; bevoegde rollen besluiten. Echte acties blijven in de bronregistratie."
- Alle simulatieknoppen hebben `data-action`; in print onzichtbaar.
- Statische referentiesectie (`.reference`) leesbaar zonder JS en in print met de VOLLEDIGE inhoud (register); daarin één `<details>` met `<summary>Taak, bronbeheer en grenzen</summary>` met alinea's **Gebruiker en uitkomst**, **Bron**, **Bewijs** (of **Regels**), **Praktijktoets**. In print alle details-inhoud zichtbaar.
- `<nav aria-label="Gerelateerde views">` met relatieve links (moeten bestaan), en `.foot` met de standaard-synthetisch-waarschuwing (zelfde strekking als test-coverage).
- Status altijd in woorden, nooit alleen kleur/positie. Zichtbare focus (`:focus-visible`), knoppen ≥44px, `prefers-reduced-motion` respecteren. Geen documentoverflow bij 320 en 390 px. Unieke IDs (ook dynamisch).
- Tekstweergave: alleen eigen geschreven data in innerHTML; geen gebruikersvrije tekstinvoer.
- Stijlverboden (design): geen ALL-CAPS labels/eyebrows (geen text-transform:uppercase), geen monospace data-labels, geen 'A · B · C'-metastrings, geen '→' achter link/knoptekst, geen identieke afgeronde kaarten met grijze schaduw, geen gradient-washes, geen #111/#0b0b0b. Eén opvallend element per pagina; rest rustig. Regel-lengte < 75ch.
- Datum-rekenen in UTC (Date.UTC), weergave als JJJJ-MM-DD.

______________________________________________________________________

## 1. Omgevingsvergelijker

Bestand: `visuals/wijziging_en_acceptatie/fab-omgevingsvergelijker.html`
Title: "FAB Omgevingsvergelijker — geldt deze test ook in productie?"
Demo-strook rechts: "Synthetische demonstratie, geen configuratieregistratie"
H1: "Geldt dit testresultaat ook in productie?"
Intro: "Kies waar een test is uitgevoerd en welk testspoor je wilt meenemen. De vergelijking toont welke onderdelen van die test in productie anders zijn, of nog niet zijn vergeleken. Een geslaagde test in acceptatie bewijst niets over een onderdeel dat in productie verschilt."
Context-blok: "Zorgoverdracht naar een woonzorglocatie" / "CHG-DEMO-LOC-02 / zelfstandige demo v1" / "Productie vergeleken met de doelstand na livegang. Momentopnamen van 2026-09-30, peildatum 2026-10-03." / "Demo-afspraak: een momentopname ouder dan 14 dagen telt als verouderd."
Werksectie-titel (h2): "Productie naast de testomgeving"

### Visueel concept: drukproef-registratie (lichtbak)

Elke rij = een configuratie-onderdeel. Per rij twee doorschijnende "platen" over elkaar heen: testomgeving (cyaan) en productie-doelstand (magenta), met `mix-blend-mode: multiply`. Gelijk/beoogd → platen liggen exact op elkaar (registratie klopt, overlap wordt donker violet). Verschil → magenta plaat schuift ~20px op (misregistratie) en toont eigen waarde. Onbekend/verouderd → magenta plaat alleen gestippelde omtrek, geen vulling. Status staat ALTIJD als tekst rechts in de rij. Kleine registratiekruisjes (cirkel + kruis, SVG inline) in de hoeken van de lichtbak = het enige decoratieve element. Offset-overgang (transform .25s) alleen als reactie op keuze; uit bij reduced motion. Rijen die het gekozen testspoor niet raakt: lichter weergegeven met tekst "Niet geraakt door T-0x" (contrast tekst blijft ≥4.5:1).

Tokens:

- `--lightbox: #A9AFB3` (middengrijs canvas van de lichtbak)
- `--sheet: #F4F6F7` (pagina/vel)
- `--cyan: #0093C4` (alleen als plaatvulling, ~0.55 alpha; NIET als tekstkleur)
- `--magenta: #C8197A` (plaat + mag als tekst/accent)
- `--ink: #231F20` (registratiezwart)
- `--muted: #4E5559`
  Type: display `"Futura","Futura PT","Century Gothic",sans-serif` (h1 groot, gewicht 500, strak letterspacing -.02em); body `"Charter","Bitstream Charter","Sitka Text",Cambria,Georgia,serif`, 17px/1.6.
  Layout: links uitgelijnd. Breed: mast (h1 links, context rechts) → keuzeregel → lichtbak (≈2/3) + oordeelpaneel rechts (≈1/3, sticky). \<850px oordeel onder de lichtbak. \<480px rijen stapelen: naam, dan platen, dan status.

```
FAB / Omgevingsvergelijker                    Synthetische demonstratie...
Geldt dit testresultaat              | Zorgoverdracht naar een woonzorglocatie
ook in productie?                    | CHG-DEMO-LOC-02 ...
[Getest in: Acceptatie | Test]  [T-01][T-02][T-03][T-04][T-05]   [Herstel][Kopieer][Druk af]
+-- lichtbak --------------------------------+  +-- oordeel ---------+
| +  ECD-versie    [==cyaan==][==magenta==]  Gelijk     |  | Aanvullende test   |
|    Koppelpunt    [==cyaan==]   [==magenta==] Verschil |  | nodig ...          |
+--------------------------------------------+  +--------------------+
```

### Controles

- `#source` select "Getest in": `acc` "Acceptatie" (standaard), `tst` "Test".
- Testsporen als `button[data-track="T-01"]` … met `aria-pressed`; standaard T-01. Pijl-/Tab-bediening: gewone knoppen volstaan.
- Per aspectrij (alleen voor de huidige bronomgeving) twee knoppen:
  - `data-action="compare"` "Simuleer vergelijking door technisch beheer": zet `verified[env]=true`, snapshot env en prod op 2026-10-03, vergeleken door "Technisch beheer (demo), 2026-10-03". Disabled als al vergeleken én actueel.
  - `data-action="change"` "Simuleer gewijzigde productieconfiguratie": prodTarget krijgt suffix " (gewijzigd 2026-10-03)", verified voor alle envs false, rij-status wordt "Herbeoordeling nodig" (telt als onbekend).
- Aspectrij element: `[data-aspect="<id>"]`, statuscel `.state`.

### Data

Productie-momentopname: 2026-09-30, bron "Configuratie-export productie, technisch beheer (demo)". Doelstand: bron "Wijzigingsplan CHG-DEMO-LOC-02 v1 (demo)".

| id         | naam                     | prodNow                                | prodTarget | acc (snap, verified)                      | tst (snap, verified)                                 |
| ---------- | ------------------------ | -------------------------------------- | ---------- | ----------------------------------------- | ---------------------------------------------------- |
| app        | ECD-versie               | 2026.3.2                               | 2026.3.2   | 2026.3.2 (2026-09-30, true)               | 2026.4.0 (2026-09-12, true)                          |
| connector  | Overdrachtsconnector     | 0.2                                    | 0.3        | 0.3 (2026-09-30, true)                    | 0.3 (2026-09-29, true)                               |
| mapping    | Locatie- en rolmapping   | 0.1                                    | 0.2        | 0.2 (2026-09-30, **false**)               | "0.2 met handmatige aanpassing" (2026-09-29, true)   |
| rolmodel   | Rolmodel en locatiescope | 0.1                                    | 0.2        | 0.2 (2026-09-30, true)                    | 0.2 (2026-09-29, true)                               |
| testroles  | Testrollen               | "Rollen per locatie, ook buiten scope" | idem       | idem (2026-09-30, true)                   | "Eén brede beheerrol" (2026-09-29, true)             |
| validation | Validatie locatiecode    | 0.1                                    | 0.2        | 0.2 (2026-09-30, true)                    | 0.2 (2026-09-29, true)                               |
| dedupe     | Herverwerkingsvenster    | 24 uur                                 | 24 uur     | 24 uur (2026-09-30, **false**)            | "5 minuten (verkort voor testen)" (2026-09-29, true) |
| endpoint   | Ontvangend koppelpunt    | "Extern portaal woonzorglocatie"       | idem       | "Leveranciersstub 1.4" (2026-09-30, true) | "Leveranciersstub 1.4" (2026-09-29, true)            |

Notities (tonen in rij-detail of oordeel wanneer relevant):

- testroles: "Productie gebruikt echte rollen. Vergelijk de rolopbouw, nooit echte accounts."
- endpoint: "Het externe portaal heeft geen eigen test- of acceptatieomgeving (demo-aanname). Vraag de leverancier om bewijs van de eigen portaaltest en spreek in het wijzigingsplan een nacontrole na livegang af. Test niet met echte cliëntgegevens buiten het afgesproken proces."
- dedupe tst: "Verkort venster maakt een dubbele aanbieding na 5 minuten niet zichtbaar."

Testsporen (namen gelijk aan Test Coverage Map):

- T-01 Volledige overdracht: app, connector, mapping, endpoint
- T-02 Geen inzage buiten locatiescope: app, rolmodel, testroles
- T-03 Ongeldige locatie afwijzen: connector, validation
- T-04 Herhaling niet dubbel verwerken: connector, dedupe, endpoint
- T-05 Terugval en aansluiting na herstel: geen vergelijkbare onderdelen → blocked

### Regels (één functie `status(aspect, env)`; scherm, oordeel en export gebruiken die)

Peildatum 2026-10-03, verouderd als (peildatum − snapshot) > 14 dagen, voor env-snapshot óf prod-snapshot.

1. Rij gewijzigd en nog niet opnieuw vergeleken → "Herbeoordeling nodig" (soort: onbekend)
1. verouderd → "Verouderd" (soort: onbekend)
1. niet verified → "Onbekend" met toelichting "Opgave, niet vergeleken" (soort: onbekend)
1. envWaarde === prodTarget en prodNow !== prodTarget → "Gelijk aan doelstand" (soort: ok; toelichting "verschil met huidige productie is de wijziging zelf")
1. envWaarde === prodTarget → "Gelijk" (soort: ok)
1. anders → "Verschil" (soort: verschil)

Oordeel voor gekozen spoor (`#verdict`, aria-live polite):

- T-05: "Niet beoordeelbaar. Oefenomgeving, noodplan en contactroute ontbreken in deze vergelijking. Vraag eerst het lokale noodplan op."
- ≥1 verschil: kop "Aanvullende test nodig", lijst verschillen met wat te doen; lijst daarnaast ook onbekende onderdelen onder "Eerst vaststellen".
- geen verschil, ≥1 onbekend: kop "Nog niet vast te stellen", lijst onbekende onderdelen.
- alles ok: kop "Geen bekend verschil", tekst: "Voor de onderdelen die dit testspoor raakt is geen verschil bekend. Daarmee is werking in productie nog niet bewezen: plan de nacontrole na livegang in het wijzigingsdossier."
  Daaronder `#tally` (tekst): "<n> onderdelen geraakt: <a> gelijk, <b> verschil, <c> onbekend."

Verwachte beginuitkomsten (worden getest):

- acc/T-01: app Gelijk, connector "Gelijk aan doelstand", mapping Onbekend, endpoint Verschil → "Aanvullende test nodig"
- acc/T-02 → "Geen bekend verschil"
- tst/T-02: app Verouderd, testroles Verschil → "Aanvullende test nodig"
- acc/T-01 na compare op mapping: mapping Gelijk aan doelstand; oordeel nog steeds "Aanvullende test nodig" (endpoint)
- acc/T-02 na change op rolmodel → "Nog niet vast te stellen"; export bevat "Herbeoordeling nodig"

Statisch register (`.register`, zonder JS zichtbaar): een echte `<table>` met caption, kolommen Onderdeel / Productie nu / Doelstand / Acceptatie / Test / Raakt testsporen, één `<tr data-static-aspect>` per aspect (8 rijen), plus een korte alinea per testspoor met beginoordeel voor Acceptatie en Test, en de endpoint-notitie. In smalle schermen mag de tabel in een `overflow-x:auto` wrapper (geen documentoverflow).
Taak-details: Gebruiker en uitkomst: FAB bereidt acceptatie voor en legt verschillen en aanvullende tests vast voor de test-/acceptatieverantwoordelijke; technisch beheer en leverancier leveren de configuratiegegevens. Bron: synthetische momentopnamen; echte bronhouder en configuratieregistratie niet vastgesteld; herzie bij iedere versie-, configuratie- of koppelwijziging en vóór ieder acceptatiemoment. Regels: verschil → aanvullende test; ongecontroleerd of verouderd → onbekend, niet gelijk; "geen bekend verschil" is geen productiebewijs. Praktijktoets: vergelijk met de huidige omgevingslijst/het testplan op gemiste verschillen en onderhoudslast.
Nav: `fab-test-coverage-map.html` "Testsporen en bewijs", `fab-releaseatelier.html#test-coverage` "Broncasus in Releaseatelier", `../landschap_en_processen/fab-life-cycle-map.html` "Versies en ondersteuningstermijnen".

______________________________________________________________________

## 2. Known Error / Workaround Map ("Bekende fouten")

Bestand: `visuals/incident_en_continuiteit/fab-known-error-map.html`
Title: "FAB Bekende fouten — welke tijdelijke werkwijze mag hier?"
Demo-strook rechts: "Synthetische demonstratie, geen kennisbank"
H1: "Past deze melding bij een bekende fout?"
Intro: "Vink aan wat je in de melding herkent. Een passend kenmerk is een aanwijzing, geen diagnose. Een tijdelijke werkwijze mag je alleen gebruiken als die goedgekeurd en actueel is en de toepassingsvoorwaarden kloppen."
Meldingsblok (synthetisch): "INC-DEMO-0412, ontvangen 2026-10-03 07:10" / citaat melder: "Bij de ochtendoverdracht is de aftekenlijst op de gedeelde tablet leeg. Gisteravond werkte hij nog." / "Locatie: woonzorg De Linde (fictief). Gebruiksmoment: uitvoering bij triage, of opleiding."
Werksectie-h2: "Bekende fouten aan het bord"

### Visueel concept: werkplaatsbord met hanglabels

Een geperforeerd bord (pegboard) waaraan per bekende fout een hanglabel hangt: manilla label met oogje (cirkel) en touwtje naar een haak; afgeschuinde bovenhoeken (clip-path), lichte rotatie mag NIET (leesbaarheid). Label toont: KE-nummer, titel, applicatie, één statusregel in woorden, en een afscheurstrook onderaan "Past bij x van y kenmerken" of "Geen aanwijzing". Status-uitdrukking:

- geldig goedgekeurd: gewoon manilla.
- herbeoordeling verlopen: diagonale rode band over het label met tekst "Herbeoordeling verlopen" (de band is de enige echte kleurstunt).
- concept: wit label met gestippelde rand, tekst "Concept, niet goedgekeurd".
- uitgesloten door kenmerk: label krijgt doorgehaalde afscheurstrook + tekst "Kenmerk past niet".
  Klik/Enter op label (`button[data-select="KE-DEMO-07"]`, aria-expanded/aria-controls) opent het detail ("bijsluiter") onder het bord: `#detail-<id>`.
  Tokens:
- `--wall: #D8DCD6` (pagina)
- `--board: #45534F` (bord) met radial-gradient gaatjespatroon `--hole: #36423F`
- `--tag: #EBD59C` (manilla), `--tag-edge: #C9AF6B`
- `--ink: #2B2219`
- `--void: #B3261E`
  Type: display `"Rockwell","Roboto Slab","Sitka Heading",Cambria,serif` (h1, KE-titels); body `"Optima","Candara","Segoe UI",sans-serif` 17px/1.55.
  Layout: mast (h1 links, melding rechts als papiertje met lichte rand) → kenmerken als checkbox-chips + versie-select → bord (4 labels naast elkaar; 2×2 \<900px; 1 kolom \<480px) → detail → `#verdict` → export → referentie.

### Controles

- Kenmerk-checkboxes `input[data-sign="s1"]` … met labels:
  - s1 "Gedeelde tablet of werkplek"
  - s2 "Na dienstwissel of opnieuw openen"
  - s3 "Lijst of overzicht is leeg"
  - s4 "Weergave toont de verkeerde datum"
  - s5 "Bericht of registratie dubbel zichtbaar"
  - s6 "Rapportage na nachtelijke verversing"
  - s7 "Meerdere cliënten of teams tegelijk geraakt"
  - s8 "Registratie lijkt verdwenen of gewijzigd"
- `#version` select "Versie bij melder": `2026.3` (standaard) "ECD 2026.3", `2026.4` "ECD 2026.4", `unknown` "Onbekend".
- In detail: toepassingsvoorwaarden als checkboxes `input[data-condition]` ("Bevestigd met melder"). Disabled tenzij de KE status "Controleer de toepassingsvoorwaarden" heeft.
- `data-action="reconfirm"` "Simuleer herbevestiging door kennisitemeigenaar" (alleen bij verlopen): status goedgekeurd, versie +1, herbeoordeling 2027-01-15, "Kennisitemeigenaar (demo), 2026-10-03".
- `data-action="revise"` "Simuleer gewijzigde werkwijze": versie +1, status "Concept, niet goedgekeurd" (eerdere goedkeuring ongeldig), condities gereset.
- Bij wijziging van kenmerken, versie of KE-status: toegepaste condities van die KE resetten.

### Data (peildatum 2026-10-03)

KE-DEMO-03 "Rooster toont gisteren na middernacht" — Roosterportaal, versies ["4.2"] (n.v.t. ECD; versie-select geldt alleen voor ECD-items: voor KE-03 toon "Roosterportaal 4.2" en negeer #version). signs [s2,s4], excludes [s8, s7]. Workaround: "Ververs de dagweergave en controleer de datum bovenaan voordat je de dienst leest." Voorwaarden: ["Alleen de weergave is fout; er is niets geregistreerd of gewijzigd", "Na verversen staat de juiste datum bovenaan"]. Zorgimpact: hinder. Status: goedgekeurd, kennisitem v2, goedgekeurd door "Proceseigenaar planning (demo)" 2026-07-01, herbeoordeling 2026-12-01. Structureel: "Leveranciersmelding LEV-DEMO-221; herstel gepland in 4.3. Gepland is nog niet opgelost." Eigenaar: kennisitemeigenaar planning (voorgestelde rol). Escalatie: "Blijft de datum fout na verversen? Behandel als nieuwe verstoring en zet door naar FAB planning."
KE-DEMO-07 "Aftekenlijst leeg na dienstwissel op gedeelde tablet" — ECD, versies ["2026.3"]. signs [s1,s2,s3], excludes [s7, s8]. Workaround: "Laat de medewerker volledig uitloggen en opnieuw inloggen op de tablet. Controleer daarna of de lijst gevuld is." Voorwaarden: ["Het gaat om een gedeelde tablet met ECD 2026.3", "Na opnieuw inloggen is de lijst gevuld", "Andere medewerkers en cliënten hebben hun lijst wel"]. Zorgimpact: "Stilgevallen zorgondersteuning; mogelijk zorgrisico". Status: goedgekeurd v2 door "Proceseigenaar zorg (demo)" 2026-03-15, herbeoordeling **2026-09-15** (verlopen). Structureel: "Probleem PRB-DEMO-031 bij leverancier, oplossing nog niet gepland." Eigenaar: kennisitemeigenaar zorgdossier (voorgestelde rol). Escalatie: "Blijft de lijst leeg? Escaleer direct als zorgkritische verstoring en volg de lokaal goedgekeurde noodwerkwijze. Teken niet op papier af tenzij het lokale noodplan dat voorschrijft." Extra link naar `fab-continuiteitskaart.html`.
KE-DEMO-11 "Overdrachtsbericht dubbel zichtbaar in ontvangend portaal" — Overdrachtskoppeling, versies ["0.2"] (negeer #version, toon "Connector 0.2"). signs [s5], excludes [s8]. Workaround: geen voor gebruikers. Tekst: "Geen tijdelijke werkwijze voor gebruikers. Verwijder of herverwerk niets zelf; meld het bericht met referentie aan integratiebeheer." Voorwaarden: []. Zorgimpact: "Risico op dubbele registratie; mogelijk financiële gevolgen". Status: concept v1, niet goedgekeurd. Structureel: "Wordt opgelost met connector 0.3 (CHG-DEMO-LOC-02); nog niet getest in productie." Eigenaar: integratiebeheer met proceseigenaar. Links: `../gegevens_en_ketens/fab-ketenkaart.html`, `../wijziging_en_acceptatie/fab-omgevingsvergelijker.html`.
KE-DEMO-14 "Bezettingsrapportage toont nul na nachtelijke verversing" — Rapportageplatform, versies ["9"] (negeer #version). signs [s6, s3], excludes [s8]. Workaround: "Gebruik de rapportage van de vorige dag en vermeld die peildatum in elke overdracht of verantwoording." Voorwaarden: ["De verversingstijd in de rapportage is van vóór vandaag", "De vorige dagrapportage is volledig"]. Zorgimpact: "Verantwoording en planning; geen directe zorgimpact bekend". Status: goedgekeurd v1 door "Rapportage-eigenaar (demo)" 2026-08-20, herbeoordeling 2026-11-20. Structureel: "Bewaking op mislukte verversing ingericht door BI; werking niet gecontroleerd." Eigenaar: rapportage-eigenaar met BI.

### Regels (één functie `assess(ke)`; label, detail, verdict en export gebruiken die)

Volgorde:

1. matched = signs ∩ aangevinkt; excluded = excludes ∩ aangevinkt.
1. excluded ≠ ∅ → "Kenmerk past niet" — tekst: "Niet toepassen: '<kenmerk>' wijst op iets anders. Behandel als nieuwe verstoring." (Bij KE-07 + s7: voeg toe "Meerdere cliënten geraakt: start bij zorgimpact de afgesproken continuïteitsroute.")
1. matched = ∅ → "Geen aanwijzing".
1. status concept → "Alleen escalatieroute" ("Nog niet goedgekeurd").
1. herbeoordeling < peildatum → "Niet als goedgekeurd gebruiken" (label-band "Herbeoordeling verlopen"); tekst noemt escalatie naar kennisitemeigenaar.
1. ECD-item en #version ∉ versies → "Geldigheid voor <versie> niet vastgesteld" (bij unknown: "Versie onbekend: vraag de versie na").
1. Workaround zonder voorwaarden → n.v.t.; anders niet alle voorwaarden bevestigd → "Controleer de toepassingsvoorwaarden".
1. alle bevestigd → "Toepasbaar binnen deze oefening" + "Leg de toepassing vast in de melding en koppel die aan <KE>. Volg de herbeoordeling."
   `#verdict` (aria-live) vat samen: welke KE's een aanwijzing hebben en hun uitkomst; als geen enkele KE toepasbaar: "Geen goedgekeurde werkwijze toepasbaar. Volg de gewone triage en escalatie." Zorgimpact van de best passende KE altijd vermelden.

Verwachte uitkomsten (getest):

- begin: alle labels "Geen aanwijzing"; verdict bevat "Geen goedgekeurde werkwijze toepasbaar".
- s1+s2+s3 → KE-07 label "Past bij 3 van 3 kenmerken", uitkomst bevat "Niet als goedgekeurd gebruiken"; voorwaarden disabled.
- reconfirm KE-07 → "Controleer de toepassingsvoorwaarden"; alle 3 voorwaarden aan → "Toepasbaar binnen deze oefening"; export bevat dat.
- daarna s7 aan → KE-07 "Kenmerk past niet", tekst bevat "continuïteitsroute"; voorwaarden gereset.
- s7 uit, versie 2026.4 → KE-07 bevat "Geldigheid voor ECD 2026.4 niet vastgesteld".
- s5 → KE-11 "Alleen escalatieroute", tekst bevat "Verwijder of herverwerk niets zelf".
- revise op KE-14 (na s6) → concept, eerdere goedkeuring ongeldig.
- reset → begin.
  Statisch register: `.register article` × 4 (één per KE, `id="ke-static-<nr>"`), met kenmerken, uitsluitingen, werkwijze, voorwaarden, zorgimpact, status/versie/goedkeuring/herbeoordeling, structurele oplossing, eigenaar, escalatie.
  Taak-details: Gebruiker: FAB en tweede lijn bij triage of terugkerende meldingen; uitkomst: goedgekeurde instructie of escalatie. Bron: synthetische kennisitems, demo v1 revisie 2026-10-03; echte kennisbank (bijv. TOPdesk of lokaal afgesproken registratie) en kennisitemeigenaren niet vastgesteld; herzie bij nieuwe versie, gewijzigde werkwijze of verlopen herbeoordeling. Regels: kenmerken zijn aanwijzingen; verlopen, concept of andere versie = niet gebruiken; structurele oplossing gepland ≠ opgelost. Praktijktoets: vergelijk met het bestaande kennisitem op juiste instructie, gemiste uitsluitingen en zoektijd.
  Nav: `incident-onepager.html` "Van melding naar oplossing", `fab-oorzaakopsporing.html` "Oorzaakopsporing", `fab-continuiteitskaart.html` "Continuïteit en noodwerkwijze".

______________________________________________________________________

## 3. Applicatie Life Cycle Map

Bestand: `visuals/landschap_en_processen/fab-life-cycle-map.html`
Title: "FAB Life Cycle Map — welke upgrade vraagt nu actie?"
Demo-strook rechts: "Synthetische demonstratie, geen contractregistratie"
H1: "Welke versie loopt af voordat we klaar kunnen zijn?"
Intro: "Het einde van de ondersteuning is niet het moment om te beginnen. Per onderdeel staat wanneer je uiterlijk moet starten, gerekend met de doorlooptijd van testen, opleiden en invoeren. Een geplande wijziging verandert die datum niet; alleen uitvoering op schema verlaagt het risico."
Context: "Vijf onderdelen van een fictieve VVT-organisatie" / "Peildatum 2026-10-03 / demo v1" / "Doorlooptijden zijn demo-inschattingen van FAB, niet afgestemd met leveranciers of ICT." / "Demo-drempel: start binnen 8 weken telt als actie nodig."
Werksectie-h2: "Almanak van ondersteuning"

### Visueel concept: verticale almanak

Tijd loopt van boven naar beneden (maanden okt 2026 t/m jun 2028 = 21 maandregels). Links een rug met grote jaartallen in DIN Condensed (2026 / 2027 / 2028, ~64–96px, gewicht 700, ink op 85%): HET opvallende element. Kolommen = 5 onderdelen. Per kolom:

- volledige ondersteuning: massieve band (ink 85%);
- alleen beveiligingsupdates: gearceerde band (repeating-linear-gradient 45°, ink);
- einde: dikke horizontale streep + datumlabel;
- doorlooptijd: dunne haak/liniaal naast de band van "uiterlijk starten" tot einde;
- "uiterlijk starten": inkeping + label met datum, in signaalgeel `--signal` met ink-tekst;
- onbekende einddatum: band loopt uit in stippellijn met tekst "Einddatum onbekend".
- Afhankelijkheid tablet-OS → ECD: een gestippelde verbindingslijn van OS-kolom naar ECD-kolom met label "ECD 2026.4 eerst live".
  Horizontale "peildatum"-lijn over alle kolommen in signaalgeel (4px, met ink-label "Peildatum 2026-10-03"); beweegt met de schuif (transition alleen bij gebruikersactie, uit bij reduced motion).
  Kolomkop = button `[data-select="ecd"]` (aria-expanded/aria-controls) opent detailpaneel `#detail-<id>`; statuslabel in woorden onder de kop (`.state`).
  \<760px: almanak wordt vervangen door per onderdeel een gestapelde rij (naam, status, horizontale mini-balk met zelfde codering, en de datums als tekst). Geen documentoverflow.
  Tokens:
- `--concrete: #D9D7D2` (pagina)
- `--page: #F3F2EF` (almanakvel)
- `--ink: #22262B`
- `--signal: #F2B705` (peildatum + uiterlijk starten; nooit tekstkleur op licht)
- `--late: #A23B2A` (tekstkleur voor "Start uiterlijk verstreken"/"Buiten ondersteuning" naast woorden)
- `--rule: #B9B6AF`
  Type: display `"DIN Condensed","DIN Alternate","Bahnschrift Condensed","Arial Narrow",sans-serif` (jaartallen, h1, kolomkoppen; `font-variant-numeric: tabular-nums`); body `"Seravek","Corbel","Segoe UI",sans-serif` 17px/1.5. Geen uppercase.

### Controles

- `#date` range "Bekijk per datum": stappen 0..20; 0 = 2026-10-03, n = eerste van de maand (2026-11-01 … 2028-06-01). Label `#date-label` toont de datum. Pijltjestoetsen werken (native).
- Per onderdeel in detail:
  - `data-action="confirm"` "Simuleer bevestiging door contractbeheer": bronstatus "Bevestigd (simulatie), contractbeheer (demo) 2026-10-03". Alleen voor onbevestigde bron.
  - `data-action="roadmap"` "Simuleer gewijzigde roadmap": alleen roosterportaal: einde wordt 2027-03-31, bronstatus "Herbeoordeling nodig: nieuwe opgave, niet bevestigd".
  - Connector: `data-action="enddate"` "Simuleer vastgestelde einddatum": einde 2027-01-31, bronstatus "Vastgesteld in wijzigingsplan (simulatie)".
- Selectie: standaard roosterportaal geopend.

### Data

| id        | naam                          | versie | volledige ondersteuning tot | beveiliging tot (einde) | bron + bronstatus                                                                              | doorlooptijd (weken, opbouw)                     | afhankelijk                                                                   | eigenaar (voorgestelde rol)                    |
| --------- | ----------------------------- | ------ | --------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------- |
| ecd       | Zorgdossier (ECD)             | 2026.3 | 2027-03-31                  | 2027-09-30              | Leveranciersroadmap 2026-09 (demo); bevestigd door contractbeheer (demo) 2026-09-20            | 16 (test 6, opleiding 4, invoering en nazorg 6)  | —                                                                             | Applicatie-eigenaar zorgdossier                |
| rooster   | Roosterportaal                | 4.2    | 2026-12-31                  | 2026-12-31              | Leveranciersmail 2026-08 (demo); onbevestigde opgave, niet in contractregistratie              | 12 (test 4, opleiding 2, invoering 6)            | —                                                                             | Applicatie-eigenaar planning                   |
| connector | Overdrachtsconnector          | 0.2    | onbekend                    | onbekend                | Wijzigingsplan CHG-DEMO-LOC-02 (demo): 0.2 vervalt na livegang van 0.3, datum niet vastgesteld | 8                                                | —                                                                             | Functioneel keteneigenaar met integratiebeheer |
| bi        | Rapportageplatform            | 9      | 2027-12-31                  | 2028-06-30              | Productlevenscyclus fabrikant, peildatum 2026-09-01 (demo); bevestigd                          | 26 (migratie rapporten 14, test 8, overdracht 4) | —                                                                             | Rapportage-eigenaar met BI                     |
| tabletos  | Besturingssysteem zorgtablets | 15     | 2026-10-31                  | 2027-01-31              | Fabrikantpagina, peildatum 2026-09-01 (demo); bevestigd door ICT (demo)                        | 10 (uitrol ICT)                                  | ECD 2026.4 moet live zijn vóór de uitrol (versie 16 werkt pas met ECD 2026.4) | ICT-werkplekbeheer met FAB                     |

"Einde" voor rekenen = beveiliging tot (laatste ondersteuning).

### Regels (één functie `plan(item, D)`; kolom, lijst, detail, export gebruiken die)

- ownStart = einde − doorlooptijd·7 dagen.
- Afhankelijkheid: ecd.start = min(ecd.ownStart, tabletos.start − ecd.doorlooptijd·7). Toon de reden: "Door afhankelijkheid van het besturingssysteem van de zorgtablets".
- Status bij datum D (in deze volgorde):
  1. geen einde → "Einddatum onbekend" (geen berekening; actie: "Vraag de einddatum op bij de functioneel keteneigenaar en leg die vast in het wijzigingsplan.")
  1. D > einde → "Buiten ondersteuning"
  1. D ≥ start → "Start uiterlijk verstreken"
  1. start − D ≤ 56 dagen → "Start binnen 8 weken"
  1. anders → "Bewaken"
- Onbevestigde bron: statustekst krijgt toevoeging "(op basis van onbevestigde opgave)".
- Volgende actie per status: verstreken → "Escaleer naar <eigenaar>; laat de bevoegde rol een tijdelijke maatregel en het restrisico beoordelen."; binnen 8 weken → "Start de voorbereiding: plan test, opleiding en invoering met <eigenaar>."; bewaken → "Herbeoordeel bij nieuwe roadmap of uiterlijk \<start − 8 weken>."; buiten → "Gebruik is niet meer ondersteund; escaleer naar <eigenaar> en leg het restrisico voor aan de bevoegde rol."

Verwachte uitkomsten (getest; gecontroleerd met de hand):

- D=2026-10-03: rooster start 2026-10-08 → "Start binnen 8 weken (op basis van onbevestigde opgave)"; tabletos start 2026-11-22 → "Start binnen 8 weken"; ecd ownStart 2026-12-09, effectief 2026-08-02 → "Start uiterlijk verstreken"; bi start = 2028-06-30 − 182 dagen → "Bewaken"; connector "Einddatum onbekend".
- rooster roadmap → einde 2027-03-31, start 2027-01-06 → "Bewaken (op basis van onbevestigde opgave)"; bronstatus "Herbeoordeling nodig".
- confirm rooster → toevoeging verdwijnt.
- connector enddate → einde 2027-01-31, start 2026-12-06 → "Bewaken"? (2026-12-06 − 2026-10-03 = 64 dagen > 56 → "Bewaken").
- slider naar 2027-02-01 (stap 4) → rooster (origineel) "Buiten ondersteuning"; tabletos "Buiten ondersteuning".
- `#summary` (aria-live) telt: "<a> verstreken, <b> binnen 8 weken, <c> bewaken, <d> buiten ondersteuning, <e> einddatum onbekend. Geen planning of besluit."
  Statisch register: `.register article` × 5 (`id="lc-static-<id>"`) met versie, beide datums, bron en bronstatus, doorlooptijd met opbouw, afhankelijkheid, berekende uiterlijke start (op peildatum 2026-10-03), status op peildatum, eigenaar, volgende actie. Plus de rekenregel in één alinea.
  Taak-details: Gebruiker: FAB bij beheerplanning en kwartaaloverleg met applicatie-eigenaren, ICT en contractbeheer; uitkomst: tijdig gestarte upgrade of geëscaleerd restrisico. Bron: synthetische termijnen; echte bron is contract-/leveranciersregistratie (geen tweede contractadministratie), bronhouders niet vastgesteld; herzie bij nieuwe roadmap, contractwijziging of iedere kwartaalplanning. Regels: uiterlijke start = einde − doorlooptijd; afhankelijkheden schuiven eerder; onbevestigde opgave blijft zichtbaar; gepland is niet uitgevoerd; drempel 8 weken is demo. Praktijktoets: vergelijk met de huidige versie-/contractlijst op gemiste afhankelijkheden en te late signalering.
  Nav: `fab-applicatielandschap.html` "Applicatielandschap", `../wijziging_en_acceptatie/fab-omgevingsvergelijker.html` "Omgevingsvergelijker", `../wijziging_en_acceptatie/fab-releaseatelier.html` "Releaseatelier".
