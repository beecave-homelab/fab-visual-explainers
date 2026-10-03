# Ontwerpspecificatie: drie FAB-prototypes van 3 oktober 2026, derde ronde

Deze specificatie is de bouwopdracht voor [Data Lineage](../visuals/gegevens_en_ketens/fab-data-lineage.html), [Release Impact Explorer](../visuals/wijziging_en_acceptatie/fab-release-impact-explorer.html) en [Adoptiekaart](../visuals/wijziging_en_acceptatie/fab-adoptiekaart.html). Ze legt vormgeving, synthetische data, regels en verwachte uitkomsten vast. De HTML is leidend; bij verschil geldt het bestand. [AGENTS.md](../AGENTS.md) blijft de centrale bron voor projectafspraken. De regressietests staan in `test/test_task_views.py` en `test/test_pages.py`.

Selectie: van de zeven open kandidaten adviseren de beheerkaartjes bij Functional Blueprint, Leverancierskaart, Eigenaarschapkaart en Stakeholder Impact Map om ze in bestaande views op te nemen. Data Lineage (één kritiek gegeven), Release Impact Explorer (keten bron → lokaal gevolg → doelgroep → test/actie → eigenaar) en Adoptiekaart (training bewijst geen vaardigheid) hebben een eigen hoofdvraag, bron, eigenaar en vervolgstap. De Release Impact Explorer neemt de doelgroepvraag van de Stakeholder Impact Map mee als filter; die kandidaat blijft open.

Alle data is synthetisch. Drempels (90 %, 85 %, steekproef 20), transformaties, laadmomenten en releasepunten zijn demo-afspraken, geen lokaal vastgestelde normen of leveranciersfunctionaliteit.

## Gemeenschappelijk

Volg exact het gemeenschappelijke patroon uit de [eerste ronde](ontwerpspecificatie-prototypes-2026-10-03.md#gemeenschappelijk-volg-het-patroon-van-visualswijziging_en_acceptatiefab-test-coverage-maphtml) en de [tweede ronde](ontwerpspecificatie-prototypes-2026-10-03-ronde-2.md#gemeenschappelijk): inline CSS/JS, geen externe requests of webfonts (ook geen externe `url()`; een inline `data:`-SVG als patroon mag), `.skip`-link, demo-strook, `.interactive` alleen met `body.ready` en niet in print, `#reset` ("Herstel beginstand"), `#copy`, `#print` ("Druk af"), `#message` role=status, verborgen `#export` met readonly `#export-text`, identiek kopieergedrag en exportvorm (> 800 tekens, eerste regel `<naam> / <casus> / demo v1 / revisie 2026-10-03`, `Exportmoment`, regel met "Uitsluitend simulatie", slotregel "FAB adviseert; bevoegde rollen besluiten. Echte acties blijven in de bronregistratie."), `data-action` op alle simulatieknoppen, statische `.reference` met volledig register en één `<details>` "Taak, bronbeheer en grenzen" (alinea's **Gebruiker en uitkomst**, **Bron**, **Regels**, **Praktijktoets**), `<nav aria-label="Gerelateerde views">`, `.foot`, status altijd in woorden, focus zichtbaar, knoppen ≥ 44 px, `prefers-reduced-motion`, geen overflow bij 320/390 px, unieke ID's, alleen eigen data in `innerHTML`, datums als JJJJ-MM-DD (rekenen in UTC), peildatum 2026-10-03.

Stijlverboden: geen `text-transform:uppercase`, geen monospace, geen `A · B · C`-metastrings, geen `→` achter link- of knoptekst, geen identieke afgeronde kaarten met grijze schaduw, geen gradient-washes, geen #111/#0b0b0b. Eén opvallend element per pagina; de rest rustig. Regellengte < 75ch. Percentages met één decimaal en komma, altijd met teller en noemer.

______________________________________________________________________

## 1. Data Lineage

Bestand: `visuals/gegevens_en_ketens/fab-data-lineage.html`
Title: "FAB Data Lineage — waar veranderde dit gegeven?"
Demo-strook: links "FAB / Data Lineage", rechts "Synthetische demonstratie, geen lineageregistratie"
H1: "Waar veranderde de einddatum van de indicatie?"
Intro: "Volg één gegeven door de keten. Elke stempel toont welke waarde een systeem laat zien en welke vastgelegde transformatie het gegeven onderweg kreeg. Een verschil is pas verklaard als de waarden echt zijn vergeleken en de transformatie is vastgelegd."
Contextblok: "Einddatum indicatie" / "Aanleiding SIG-DEMO-0912: het BI-overzicht 'Indicaties die binnen 30 dagen verlopen' toont bij wijkteam Noord indicaties een dag eerder dan het zorgdossier." / "Lineage demo v1, revisie 2026-10-03. Gegevenseigenaar: gegevenseigenaar zorgadministratie (voorgestelde rol)." / "Gebruiksmoment: uitvoering bij een ketenafwijking, of overleg met BI."
Werksectie-h2: "Paspoort van het gegeven"

### Visueel concept: gegevenspaspoort

Een opengeslagen paspoort is het opvallende element. De pagina zelf is de bordeauxrode kaft (`--cover`). Daarop ligt het geopende paspoort: links de gegevenspagina (definitie van het gegeven: naam, betekenis "laatste dag met indicatie, tot en met", bron, gegevenseigenaar, gekozen steekproef met synthetische referentie en wijzigingsmoment in de bron), rechts de visumpagina's met vijf stempels in ketenvolgorde. Beide bladen hebben een fijn guillochepatroon (inline `data:`-SVG in `--guilloche`, lage dekking, geen kleurverloop) en een stiklijn in de rug. Paginanummers (blz. 1–5) zijn toegestaan: de stappen zijn een echte volgorde.

Iedere stempel heeft een eigen vorm per systeem (rond, rechthoekig, ovaal, achthoekig, rechthoekig met afgesneden hoeken) en staat licht gedraaid (−3° tot 4°, vast per stempel). Inkt `--stamp`. In de stempel: systeemnaam, getoonde waarde, vergelijkingsdatum. Vorm per status:

- Vergeleken en klopt: volle stempelrand en tekst.
- Onverklaard verschil: volle stempel met een schuine annuleringsbalk in `--void` en de woorden "Onverklaard verschil".
- Nog niet ververst: halve inktdekking (vervaagd), woorden "Nog niet ververst".
- Niet vergeleken: alleen een gestippeld leeg kader met "Niet vergeleken" en een vraagteken in plaats van de waarde.

Onder iedere stempel, op het blad zelf (nooit in de stempel alleen): transformatie naar deze stap met documentversie, verversingsmoment, statuszin in `.state`, vergelijkingsinformatie in `.compare-info` en de knop. Stappen tussen het laatste kloppende en het eerste afwijkende punt krijgen een doorlopende markeerlijn in `--void` langs de bladrand met de woorden "In het verschilgebied". Na een gebruikersactie mag een stempel kort "neerkomen" (schaal 1,04 → 1, ± .2s), uit bij reduced motion.

Tokens:

- `--cover:#5E1A2A` (pagina)
- `--leaf:#EAF0EC` (paspoortbladen)
- `--guilloche:#BFD2C9`
- `--ink:#1F2433`
- `--stamp:#4E3A86` (stempelinkt, links, focus)
- `--void:#B3243A` (annulering, verschilgebied; alleen naast woorden)
- `--muted:#56606B`
  Type: display `"Didot","Bodoni 72","Bodoni MT","Noto Serif Display",serif` (h1 gewicht 400, h2, systeemnamen in de stempels); body `"Palatino","Palatino Linotype","Book Antiqua",Georgia,serif` 16.5px/1.65. Links uitgelijnd. Tekst op de kaft in `--leaf`.

```
FAB / Data Lineage                      Synthetische demonstratie, geen lineageregistratie
Waar veranderde de einddatum      | Einddatum indicatie / SIG-DEMO-0912 ...
van de indicatie?                 |
[Steekproef: DEMO-IND-01 v] [Simuleer nachtelijke lading] [Herstel][Kopieer][Druk af]
+-- gegevenspagina ----+ | +-- visumpagina's ------------------------------+
| Einddatum indicatie  | | (ECD-stempel)       (Integratielaag-stempel)   |
| betekenis, bron,     | | blz. 1 ...          blz. 2 ...                 |
| eigenaar, steekproef | | (ZA-stempel)        (DWH-stempel)              |
|                      | | blz. 3 ...          blz. 4 ...                 |
|                      | | (BI-stempel ////)                              |
+----------------------+ +-----------------------------------------------+
#locus  Het gegeven veranderde tussen ... | #proposal
```

≥ 1100 px: gegevenspagina en visumpagina's naast elkaar, stempels in twee kolommen (leesvolgorde rij voor rij). < 760 px: gegevenspagina boven, stempels in één kolom. Print: geen kaftkleur en geen guilloche; stempels als omlijnde blokken met alle tekst.

### Data

Stappen (`.hop[data-hop="h1"]` … `h5`), vastgelegde transformatie naar deze stap, documentversie, verversing en eigenaar (voorgestelde rol):

| stap | naam                                  | vastgelegde transformatie                                                               | document                                  | verversing                   | eigenaar                             |
| ---- | ------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------- | ------------------------------------ |
| h1   | Zorgdossier (ECD)                     | Bron. Cliëntadministratie legt de einddatum vast uit het indicatiebesluit (tot en met). | Registratieafspraak indicaties v2 (demo)  | direct                       | Gegevenseigenaar zorgadministratie   |
| h2   | Integratielaag                        | Geen wijziging.                                                                         | Mappingdocument ECD–ZA v3, 2026-06-12     | direct bij bericht           | Integratiebeheer                     |
| h3   | Zorgadministratie                     | Plus 1 dag: opgeslagen als 'geldig tot' (exclusief). Lege waarde blijft leeg.           | Interfacespecificatie ZA v2.1, 2026-04-03 | direct bij bericht           | Functioneel beheer zorgadministratie |
| h4   | Datawarehouse                         | Min 1 dag: terug naar 'tot en met'. Lege waarde wordt 9999-12-31.                       | DWH-laadspecificatie v4, 2026-08-20       | nachtelijk, 2026-10-02 02:00 | BI-team                              |
| h5   | BI-overzicht verloopt binnen 30 dagen | Geen wijziging. 9999-12-31 verschijnt niet in het overzicht.                            | Rapportdefinitie RD-14 v2, 2026-09-01     | nachtelijk, 2026-10-02 03:00 | Rapportage-eigenaar met BI           |

Werkelijk gedrag (verborgen in de demo, bepaalt alleen wat een vergelijking laat zien): h2–h4 doen precies wat is vastgelegd; h5 trekt bij een datum nog eens 1 dag af (dubbele correctie); 9999-12-31 verschijnt ook werkelijk niet in het overzicht.

Afnemersgevolg (statisch bij h5): "Planners van de wijkteams zien een indicatie een dag eerder verlopen: hinder, mogelijk een te vroege herindicatieaanvraag. Geen zorginhoudelijk gevolg vastgesteld. Declaratie gebruikt de Zorgadministratie en is volgens deze lineage niet geraakt; dat is niet getoetst."

Steekproeven (`#sample`, standaard `DEMO-IND-01`), synthetisch, zonder cliëntgegevens:

| steekproef  | team  | waarde in ECD                         | gewijzigd in ECD | getoonde waarde h1 / h2 / h3 / h4 / h5 vóór lading                                    | vergeleken bij start (2026-10-02, FAB (demo)) |
| ----------- | ----- | ------------------------------------- | ---------------- | ------------------------------------------------------------------------------------- | --------------------------------------------- |
| DEMO-IND-01 | Noord | 2027-03-31                            | 2026-09-14 09:20 | 2027-03-31 / 2027-03-31 / 2027-04-01 / 2027-03-31 / 2027-03-30                        | h1, h3, h5                                    |
| DEMO-IND-02 | Noord | geen einddatum                        | 2026-08-30 11:05 | Geen einddatum / Geen einddatum / Geen einddatum / 9999-12-31 / Niet in het overzicht | h1                                            |
| DEMO-IND-03 | Zuid  | 2027-06-30 (verlengd, was 2026-12-31) | 2026-10-02 14:10 | 2027-06-30 / 2027-06-30 / 2027-07-01 / 2026-12-31 / 2026-12-30                        | h1, h5                                        |

Na de nachtelijke lading (h4 geladen 2026-10-03 02:00, h5 2026-10-03 03:00): DEMO-IND-03 toont h4 2027-06-30 en h5 2027-06-29; de andere steekproeven houden dezelfde waarden.

### Controles

- `#sample` "Steekproef": drie opties. Iedere steekproef houdt eigen vergelijkingen en een eigen voorstel; wisselen wist niets.
- Per stap h2–h5: `data-action="compare" data-hop="hN"` "Simuleer vergelijking". Enabled als de stap niet (geldig) vergeleken is en niet nog-niet-ververst is. Legt vast: "Vergeleken 2026-10-03 (simulatie) door FAB (demo), referentie <steekproef>". h1 heeft geen knop.
- `data-action="load"` "Simuleer nachtelijke lading": eenmalig, daarna disabled. Zet de verversing van h4 en h5 op 2026-10-03 02:00 en 03:00 en maakt in **alle** steekproeven een bestaande vergelijking van h4 en h5 ongeldig.
- `data-action="propose"` "Leg correctievoorstel vast": enabled als de plek aangrenzend is gelokaliseerd (regel 4a) en er voor die steekproef geen geldig voorstel is.
- `data-action="approve"` "Simuleer akkoord gegevenseigenaar": enabled bij een geldig voorstel zonder akkoord.

### Regels (één functie `trace(sample)`; stempels, statuszinnen, plek, voorstel, register-updates en export gebruiken die)

1. **Nog niet ververst:** een stap is nog niet ververst als het verversingsmoment vóór het wijzigingsmoment in de bron ligt (h1–h3 nooit). Dat geldt los van vergelijken; zo'n stap telt niet als basis en niet als afwijking.
1. **Basis:** de verwachte waarde van een geldig vergeleken, ververste stap volgt uit de dichtstbijzijnde eerdere geldig vergeleken, ververste stap (h1 altijd), door de vastgelegde transformaties van alle tussenliggende stappen en van deze stap toe te passen op de getoonde waarde van die basis.
1. **Statuszin (`.state`):**
   - h1: "Bron: <waarde>, vastgelegd <wijzigingsmoment>"
   - nog niet ververst: "Nog niet ververst: geladen <verversing>, bron gewijzigd <wijzigingsmoment>. Vergelijk opnieuw na de volgende lading."
   - niet vergeleken: "Niet vergeleken: onbekend"; na een ongeldig geworden vergelijking: "Niet vergeleken: opnieuw vergelijken, lading na de vorige vergelijking"
   - klopt met directe vorige stap als basis: "Klopt met de vastgelegde transformatie"; met een verdere basis: "Klopt met de vastgelegde transformaties vanaf <basisnaam>"
   - anders: "Onverklaard verschil: verwacht <verwacht>, getoond <getoond>"
1. **Plek (`#locus`, aria-live):** m = eerste stap met onverklaard verschil, p = zijn basis.
   - a. Geen stap strikt tussen p en m: "Het gegeven veranderde tussen <p> en <m> zonder vastgelegde transformatie. Verwacht <e>, getoond <o>."
   - b. Wel tussenstappen: "Het verschil ontstaat ergens tussen <p> en <m>. Vergelijk \<tussenstappen, gescheiden door komma's met 'en' voor de laatste> om de plek te versmallen."
   - c. Geen verschil en alle stappen geldig vergeleken en ververst: "Geen onverklaard verschil in steekproef <id>. Dat bewijst niet dat het gegeven voor alle cliënten klopt."
   - d. Geen verschil, anders: "Geen onverklaard verschil tussen de vergeleken stappen. Nog niet vergeleken: <n>. Nog niet ververst: <s>." (n telt stappen die niet geldig vergeleken en wel ververst zijn.)
   - Altijd gevolgd door: "Een vastgelegde transformatie verklaart een verschil, maar zegt niet dat de betekenis klopt. De gegevenseigenaar beoordeelt dat."
   - Stappen strikt tussen p en m, en p en m zelf, krijgen de markering "In het verschilgebied".
1. **Voorstel (`#proposal`), per steekproef, verbonden aan het paar (p, m):**
   - geen: "Nog geen correctievoorstel."
   - voorgesteld: "Correctievoorstel <steekproef>: <m> toont <o> waar de vastgelegde transformatie <e> geeft. Vraag <eigenaar van m> de berekening te herleiden en te herstellen, of de transformatie vast te leggen. Ter beoordeling aan de gegevenseigenaar zorgadministratie. Geen herverwerking of handmatige correctie zonder akkoord. Vastgelegd door FAB (demo), 2026-10-03; nog niet beoordeeld."
   - akkoord: dezelfde eerste zinnen, eindigend op "Akkoord gegevenseigenaar (simulatie), 2026-10-03. Uitvoering en controle volgen via de bronregistratie; herstel is nog niet aangetoond."
   - Als de huidige plek niet meer regel 4a met hetzelfde paar is: "Voorstel vervallen: de vergelijking waarop het steunde is niet meer geldig." `propose` wordt dan weer mogelijk zodra regel 4a opnieuw geldt.

### Verwachte uitkomsten (worden getest; met de hand nagerekend)

- Begin (DEMO-IND-01): h3 `.state` "Klopt met de vastgelegde transformaties vanaf Zorgdossier (ECD)"; h5 `.state` "Onverklaard verschil: verwacht 2027-03-31, getoond 2027-03-30"; h2 en h4 "Niet vergeleken: onbekend"; `#locus` bevat "ergens tussen Zorgadministratie en BI-overzicht verloopt binnen 30 dagen" en "Vergelijk Datawarehouse"; `propose` disabled.
- Compare h4 → h4 "Klopt met de vastgelegde transformatie"; `#locus` bevat "veranderde tussen Datawarehouse en BI-overzicht verloopt binnen 30 dagen"; `propose` enabled → `#proposal` bevat "nog niet beoordeeld" en "Rapportage-eigenaar met BI"; approve → bevat "Akkoord gegevenseigenaar (simulatie)" en "herstel is nog niet aangetoond".
- Daarna load → h5 "Niet vergeleken: opnieuw vergelijken, lading na de vorige vergelijking"; `#proposal` "Voorstel vervallen"; `#locus` bevat "Nog niet vergeleken: 3. Nog niet ververst: 0."; `load` disabled.
- Reset, DEMO-IND-02: `#locus` bevat "Nog niet vergeleken: 4. Nog niet ververst: 0."; compare h2–h5 → h4 "Klopt", h5 `.value` bevat "Niet in het overzicht"; `#locus` bevat "Geen onverklaard verschil in steekproef DEMO-IND-02" en "bewijst niet".
- Reset, DEMO-IND-03: h4 en h5 `.state` bevatten "Nog niet ververst: geladen 2026-10-02"; compare h4 en h5 disabled; `#locus` bevat "Nog niet vergeleken: 2. Nog niet ververst: 2."; load → h5 "Niet vergeleken: opnieuw vergelijken"; compare h5 → "Onverklaard verschil: verwacht 2027-06-30, getoond 2027-06-29"; `#locus` bevat "Vergelijk Integratielaag, Zorgadministratie en Datawarehouse".
- Wisselen van steekproef en terug behoudt de vergelijkingen van elke steekproef.
- Export begint met "Data Lineage / SIG-DEMO-0912 / demo v1 / revisie 2026-10-03" en bevat per steekproef per stap getoonde waarde, status en transformatie met document, de plek, het voorstel en het afnemersgevolg.
- Reset → beginstand (DEMO-IND-01, lading niet uitgevoerd, voorstellen gewist).

Statisch register: `.register article` × 3 (`id="lin-static-DEMO-IND-01"`, `-02`, `-03`) met per stap de getoonde waarde, de beginstatus en de vastgelegde transformatie met document, en de beginplek in woorden. Daarnaast een lijst van de vijf transformaties met documentversie en eigenaar, het afnemersgevolg en één alinea met de regels in volgorde.

Taak-details: **Gebruiker en uitkomst:** FAB bij een ketenafwijking, met integratiebeheer, BI en de gegevenseigenaar; de uitkomst is de plek waar het gegeven veranderde en een correctievoorstel ter beoordeling. FAB herverwerkt of corrigeert niets zelf. **Bron:** synthetische lineage en steekproeven, demo v1, revisie 2026-10-03; de echte lineageregistratie, mappingdocumenten en bronhouder (gegevenseigenaar zorgadministratie met ketenbeheer) zijn niet vastgesteld. Herzie bij een nieuwe documentversie, een gewijzigd laadschema of na herstel. **Regels:** alleen vergeleken waarden tellen; niet vergeleken is onbekend; een nog niet ververste stap is geen afwijking; vastgelegd is niet hetzelfde als juist; een lading na vergelijking maakt die vergelijking ongeldig; één steekproef bewijst niets over alle cliënten. **Praktijktoets:** vergelijk met de huidige koppeldocumentatie en een handmatige spoorzoektocht op tijd tot de juiste plek, juiste eigenaar en herkenning van verversingsverschillen.

Nav: `fab-ketenkaart.html` "Ketenkaart", `fab-data-quality-map.html` "Data Quality Map", `fab-rapportage-lineage.html` "Rapportage Lineage", `../landschap_en_processen/fab-applicatielandschap.html` "Applicatielandschap".

______________________________________________________________________

## 2. Release Impact Explorer

Bestand: `visuals/wijziging_en_acceptatie/fab-release-impact-explorer.html`
Title: "FAB Release Impact Explorer — wat betekent deze release bij ons?"
Demo-strook: links "FAB / Release Impact Explorer", rechts "Synthetische demonstratie, geen releaseregistratie"
H1: "Wat betekent deze release bij ons, en voor wie?"
Intro: "Elk releasepunt komt binnen in het inbakje. Pas na vergelijking met onze inrichting krijgt het een vak per doelgroep, met een test of actie en een eigenaar. 'Geen lokaal gevolg' vraagt net zo goed een onderbouwing."
Contextblok: "Leveranciersrelease ECD 2026.5 (fictief)" / `#notes-version`: "Releasenotes v1.0 van 2026-09-26" / "Installatie in acceptatie 2026-10-20, in productie 2026-11-16 (demo). Lokale inrichting: momentopname INR-DEMO van 2026-09-30." / "Eigenaar: wijzigingscoördinator met FAB (voorgestelde rollen). Gebruiksmoment: overleg bij de wijzigingsintake."
Werksectie-h2: "Postvakkenkast van de release"

### Visueel concept: postvakkenkast

Een postvakkenkast aan de muur is het opvallende element: een stalen kast (`--steel`, dikke kozijnlijnen, lichte binnenvakken `--cell`) met zes vakken voor de doelgroepen in twee rijen van drie. Elk vak heeft bovenaan een naamplaatje dat ook de filterknop is (`button[data-group-filter]`, met aantal: "Planners (2)"). In een vak staan papieren briefjes (`--slip`) die als tab boven de vakrand uitsteken: releasenummer en korte titel. Een releasepunt met gevolgen voor drie doelgroepen heeft drie briefjes.

Links van de kast hangt een draadmand "Inbakje" met de briefjes die nog niet vergeleken zijn of waarvan de inrichting onbekend is (sublabels in woorden: "Nog niet vergeleken", "Inrichting onbekend"). Onder de kast zit een lade "Geen lokaal gevolg, met onderbouwing". Het geselecteerde briefje is verhoogd en krijgt een rand in `--select`; de andere briefjes van hetzelfde punt krijgen een stippelrand. Een filter op doelgroep dimt de andere vakken (dekking .45, tekst blijft leesbaar) en vult `#group-view`. Een briefje schuift kort naar zijn nieuwe vak na een gebruikersactie (± .3s), uit bij reduced motion.

Rechts (≥ 1100 px, sticky) of onder de kast: detailpaneel `#detail` met de keten **Bron** (leverancierstekst als citaat, vindplaats en versie) → **Lokaal gevolg** (inrichting en regel) → **Doelgroepen** → **Test of actie** → **Eigenaar** → **Status** (`.state`) en de acties.

Tokens:

- `--wall:#D5DAD2` (pagina)
- `--steel:#5F6F66` (kastframe, naamplaatjes met tekst `--cell`)
- `--cell:#EEF1EC` (vakken, panelen)
- `--slip:#E9DDB5` (briefjes)
- `--ink:#1E2622`
- `--select:#1F5FA8` (selectie, focus, links)
- `--flag:#9C2F4F` (inrichting onbekend, vervallen beoordeling; alleen naast woorden)
  Type: display `"Arial Rounded MT Bold","Arial Rounded MT","Nunito",sans-serif` (h1, h2, naamplaatjes, releasenummers); body `"Geneva","Segoe UI","Noto Sans",sans-serif` 15px/1.6. Links uitgelijnd.

```
FAB / Release Impact Explorer          Synthetische demonstratie, geen releaseregistratie
Wat betekent deze release bij ons,  | Leveranciersrelease ECD 2026.5 ...
en voor wie?                        | Releasenotes v1.0 van 2026-09-26 ...
[Simuleer releasenotes v1.1] [Herstel][Kopieer][Druk af]      #tally / #open
+-Inbakje-+ +====== kast ===========================+ +-- #detail ----------+
| RN-05   | | [Zorgmedewerkers (3)] [Planners (2)]   | | Bron: "..."         |
| RN-07   | |  |RN-01| |RN-06|       |RN-02|         | | Lokaal gevolg ...   |
+---------+ | [Cliëntadmin. (0)] [Kerngebruikers (1)]| | Doelgroepen ...     |
            | [Functioneel beheer (3)] [Integratie]  | | [Simuleer ...]      |
            +=== lade: Geen lokaal gevolg: RN-03 RN-04 ===+ +-----------------+
#group-view   .points (leesbare lijst van alle punten met status)
```

< 760 px: de kast wordt een lijst van zes vakken onder elkaar, het inbakje erboven en de lade eronder; detail onder de kast. Print: geen kast; alle punten als lijst met status, doelgroepen, actie en eigenaar.

### Data

Doelgroepen (`data-group`): `zorg` "Zorgmedewerkers", `plan` "Planners", `cadm` "Cliëntadministratie", `kern` "Kerngebruikers", `fab` "Functioneel beheer", `keten` "Integratie en ketenpartners".

| punt  | titel                                                   | leverancierstekst (synthetisch)                                                                   | vindplaats | instelling en voorwaarde                                     | lokaal (INR-DEMO)          | doelgroepen      | zorgimpact                                                                        | test of actie                                                                                                 | eigenaar (voorgesteld)                 | bevestiger                     |
| ----- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------ | -------------------------- | ---------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------ |
| RN-01 | Medicatieaftekenlijst: reden verplicht bij niet gegeven | "Bij 'Niet gegeven' is een reden voortaan verplicht. Bestaande aftekeningen blijven ongewijzigd." | v1.0, §2.1 | Module medicatie; geldt als die aan staat                    | aan                        | zorg, kern, fab  | Zorgproces verandert: medicatieregistratie                                        | Test in acceptatie aftekenen met en zonder reden, ook de negatieve route; pas de werkinstructie medicatie aan | Proceseigenaar medicatieproces met FAB | Proceseigenaar medicatieproces |
| RN-02 | Planningsbericht: teamcode verplicht                    | "Berichten naar de planningskoppeling zonder teamcode worden geweigerd."                          | v1.0, §4.3 | Koppeling met planning; geldt als die aan staat              | aan                        | keten, fab, plan | Mogelijk stilgevallen zorgondersteuning: geweigerde berichten geven lege diensten | Ketentest met en zonder teamcode; controleer de mapping van teamcodes                                         | Integratiebeheer met FAB               | Proceseigenaar planning        |
| RN-03 | Cliëntportaal: inzage door naasten                      | "Naasten kunnen rapportages inzien als de cliënt daarvoor toestemming geeft."                     | v1.0, §5.2 | Inzage naasten in het cliëntportaal; geldt als die aan staat | uit                        | —                | —                                                                                 | —                                                                                                             | —                                      | —                              |
| RN-04 | Declaratie: nieuwe exportindeling                       | "De declaratie-export krijgt een nieuwe indeling volgens de demo-standaard 2027."                 | v1.0, §6.1 | Declaratiemodule van het ECD; geldt als die aan staat        | uit                        | —                | —                                                                                 | —                                                                                                             | —                                      | —                              |
| RN-05 | Zoeken in gearchiveerde rapportages                     | "De zoekfunctie doorzoekt ook gearchiveerde rapportages, binnen de bestaande autorisatie."        | v1.0, §3.4 | Archiefmodule; geldt als die aan staat                       | onbekend (nagevraagd: aan) | zorg, fab        | Privacyrisico: gearchiveerde rapportages verschijnen in zoekresultaten            | Negatieve autorisatietest op gearchiveerde dossiers; informeer zorgmedewerkers                                | Autorisatieverantwoordelijke met FAB   | Gegevenseigenaar cliëntdossier |
| RN-06 | Sneller openen van het dossier                          | "Het openen van een cliëntdossier is technisch verbeterd."                                        | v1.0, §1.2 | Geen instelling; geldt altijd                                | n.v.t.                     | fab              | Hinder als het misgaat                                                            | Regressietest dossier openen in acceptatie; geen communicatie nodig                                           | FAB                                    | Applicatie-eigenaar ECD        |
| RN-07 | Weekoverzicht planning standaard 14 dagen               | "Het weekoverzicht toont standaard 14 dagen in plaats van 7."                                     | v1.0, §4.1 | Module planning; geldt als die aan staat                     | aan                        | plan, kern       | Hinder: ander standaardoverzicht                                                  | Korte instructie voor planners; kerngebruiker test het weekoverzicht                                          | Proceseigenaar planning                | Proceseigenaar planning        |

Onderbouwing geen gevolg: RN-03 "Inzage naasten staat uit in onze inrichting (INR-DEMO 2026-09-30). Herbeoordelen als die instelling verandert." RN-04 "Declaratie loopt via de Zorgadministratie, niet via de declaratiemodule van het ECD (INR-DEMO 2026-09-30)."
Navraag RN-05 bij "Technisch beheer ECD".

Releasenotes v1.1 van 2026-10-02 (na `notes`):

- RN-03 wordt: tekst "Naasten kunnen rapportages inzien als de cliënt daarvoor toestemming geeft. Na installatie staat inzage naasten standaard aan bij organisaties die het cliëntportaal gebruiken.", vindplaats "v1.1, §5.2", instelling "Cliëntportaal in gebruik; geldt als dat zo is", lokaal aan, doelgroepen cadm, zorg, fab, zorgimpact "Privacyrisico: naasten krijgen mogelijk inzage zonder ingerichte toestemming", actie "Zet inzage naasten direct na installatie uit in acceptatie en productie, of richt de toestemming in; negatieve autorisatietest", eigenaar "Gegevenseigenaar cliëntdossier met privacy officer", bevestiger "Gegevenseigenaar cliëntdossier".
- Nieuw RN-08 "Inloggen: verouderde inlogmethode vervalt", tekst "Inloggen met een lokaal wachtwoord zonder tweede factor is na deze release niet meer mogelijk.", vindplaats "v1.1, §7.1", instelling "Lokale wachtwoorden in gebruik; geldt als dat zo is", lokaal aan (tijdelijke medewerkers, demo), doelgroepen zorg, kern, fab, zorgimpact "Mogelijk stilgevallen zorgondersteuning: tijdelijke medewerkers kunnen niet inloggen", actie "Test inloggen met een tijdelijk testaccount; regel vóór productie een andere inlogmethode", eigenaar "Applicatie-eigenaar ECD met IAM", bevestiger "Applicatie-eigenaar ECD".

Beginstand: RN-01 gevolg, bevestigd door Proceseigenaar medicatieproces op 2026-10-01; RN-02 en RN-06 gevolg, niet bevestigd; RN-03 en RN-04 geen gevolg (beoordeeld door FAB (demo) 2026-10-01); RN-05 en RN-07 nog niet vergeleken.

### Controles

- Briefjes: `button.slip[data-rn][data-group]`, met `data-group="inbox"` in het inbakje en `data-group="archive"` in de lade. Klik selecteert het punt (`aria-pressed`) en vult `#detail`. Begin: RN-05 geselecteerd.
- In `#detail`, voor het geselecteerde punt:
  - `data-action="compare"` "Simuleer vergelijking met de inrichting": alleen bij nog niet vergeleken.
  - `data-action="ask"` "Simuleer antwoord van <navraagrol>": alleen bij inrichting onbekend.
  - `data-action="confirm"` "Simuleer bevestiging door <bevestiger>": alleen bij lokaal gevolg, niet bevestigd.
- `data-action="notes"` "Simuleer releasenotes v1.1": eenmalig; `#notes-version` wordt "Releasenotes v1.1 van 2026-10-02".
- `button[data-group-filter]` per doelgroep: wisselt het filter (`aria-pressed`); nogmaals klikken heft het op. `#group-view` toont voor de gekozen doelgroep per punt met gevolg: titel, zorgimpact, test of actie, eigenaar en status; zonder filter: "Kies een doelgroep om te zien wat er voor die groep verandert."
- Leesbare lijst `.points li[data-rn]` van alle punten in volgorde, met `.state`, altijd zichtbaar (ook in print, met JS bijgewerkt).

### Regels (één functie `classify(point)`; kast, inbakje, lade, lijst, telling, detail en export gebruiken die)

1. Toestand nog niet vergeleken → inbakje; `.state` "Nog niet vergeleken met de inrichting". Na een vervallen beoordeling: "Releasenotes gewijzigd na beoordeling; opnieuw vergelijken".
1. Vergelijking: lokaal onbekend en niet nagevraagd → inbakje; `.state` "Inrichting onbekend: vraag na bij <navraagrol>". Anders: geldt altijd, of lokaal aan → lokaal gevolg; anders → geen lokaal gevolg.
1. Navraag → lokale waarde bekend; direct opnieuw indelen volgens regel 2, met toevoeging "Inrichting nagevraagd 2026-10-03 (simulatie)" in het detail.
1. Lokaal gevolg → één briefje per doelgroep; `.state` "Lokaal gevolg, door FAB beoordeeld; doelgroepimpact nog niet bevestigd" of "Lokaal gevolg, bevestigd door <bevestiger>, <datum>" (simulatie: 2026-10-03, met "(simulatie)").
1. Geen lokaal gevolg → lade; `.state` "Geen lokaal gevolg: <onderbouwing>".
1. Releasenotes v1.1: elk punt waarvan de tekst wijzigt (RN-03) gaat terug naar nog niet vergeleken met vervallen-melding en verliest bevestiging; RN-08 komt binnen als nog niet vergeleken.
1. `#tally` (aria-live): "<n> releasepunten: <a> nog niet vergeleken, <b> inrichting onbekend, <c> met lokaal gevolg waarvan <d> bevestigd, <e> zonder lokaal gevolg."
1. `#open`: als a + b + (c − d) > 0: "Open voor de intake: <a> nog niet vergeleken, <b> inrichting onbekend, \<c − d> gevolgen niet bevestigd."; anders "Geen open punten in dit overzicht. Dit is geen akkoord op de release; de wijzigingscoördinator beslist." Geen score of percentage.

### Verwachte uitkomsten (worden getest)

- Begin: `#tally` "7 releasepunten: 2 nog niet vergeleken, 0 inrichting onbekend, 3 met lokaal gevolg waarvan 1 bevestigd, 2 zonder lokaal gevolg."; `#open` bevat "2 gevolgen niet bevestigd"; `.slip[data-rn="RN-01"]` bestaat met `data-group` zorg, kern en fab; RN-03 `.state` bevat "Inzage naasten staat uit"; naamplaatje Zorgmedewerkers bevat "(1)", Planners "(1)", Functioneel beheer "(3)", Cliëntadministratie "(0)".
- RN-05 compare → `.state` "Inrichting onbekend: vraag na bij Technisch beheer ECD"; `#tally` bevat "1 nog niet vergeleken, 1 inrichting onbekend"; ask → "Lokaal gevolg, door FAB beoordeeld"; `.slip[data-rn="RN-05"][data-group="zorg"]` bestaat.
- RN-07 selecteren, compare → lokaal gevolg met briefjes in plan en kern; confirm → "bevestigd door Proceseigenaar planning".
- Filter `plan` → `#group-view` bevat "Planningsbericht: teamcode verplicht" en "Weekoverzicht planning"; niet "Medicatieaftekenlijst".
- Notes → `#notes-version` "Releasenotes v1.1 van 2026-10-02"; RN-03 `.state` "Releasenotes gewijzigd na beoordeling; opnieuw vergelijken"; RN-08 in het inbakje; `#tally` begint met "8 releasepunten"; RN-03 compare → lokaal gevolg met zorgimpact "Privacyrisico"; RN-03-briefje in `cadm`.
- Export begint met "Release Impact Explorer / ECD 2026.5 / demo v1 / revisie 2026-10-03" en bevat de versie van de releasenotes en per punt bron met vindplaats, lokale inrichting, status, doelgroepen, zorgimpact, test of actie, eigenaar en bevestiging.
- Reset → beginstand (v1.0, RN-05 geselecteerd, geen filter).

Statisch register: `.register article` × 7 (`id="rel-static-RN-01"` … `RN-07`) met leverancierstekst, vindplaats, instelling en lokale waarde, beginstatus, doelgroepen, zorgimpact, test of actie, eigenaar en bevestiger. Daarnaast een korte alinea over v1.1 (RN-03 gewijzigd, RN-08 nieuw) en één alinea met de indeelregels.

Taak-details: **Gebruiker en uitkomst:** FAB bij de wijzigingsintake, met de wijzigingscoördinator en proceseigenaren; de uitkomst is per releasepunt een lokaal gevolg of een onderbouwd 'geen gevolg', met doelgroep, test of actie en eigenaar. Geen akkoord op installatie of livegang. **Bron:** synthetische releasenotes en een synthetische inrichtingsmomentopname, demo v1, revisie 2026-10-03; de echte releasenotes, inrichtingsregistratie en bronhouder (wijzigingscoördinator met FAB) zijn niet vastgesteld. Herzie bij iedere nieuwe versie van de releasenotes of een gewijzigde inrichting. **Regels:** zonder vergelijking met de inrichting geen oordeel; onbekende inrichting blijft open; ook 'geen gevolg' heeft een onderbouwing; een gewijzigde releasetekst maakt de eerdere beoordeling ongeldig; FAB beoordeelt, de proceseigenaar bevestigt de doelgroepimpact. **Praktijktoets:** vergelijk met de huidige release-intake (releasenotes plus checklist) op gemiste lokale gevolgen, juiste doelgroep en eigenaar, en herkenning van gewijzigde releaseteksten.

Nav: `fab-releaseatelier.html` "Releaseatelier", `fab-change-impact-map.html` "Change Impact Map", `fab-test-coverage-map.html` "Testsporen en bewijs", `fab-omgevingsvergelijker.html` "Omgevingsvergelijker".

______________________________________________________________________

## 3. Adoptiekaart

Bestand: `visuals/wijziging_en_acceptatie/fab-adoptiekaart.html`
Title: "FAB Adoptiekaart — wordt de nieuwe werkwijze echt beheerst?"
Demo-strook: links "FAB / Adoptiekaart", rechts "Synthetische demonstratie, geen adoptiemeting"
H1: "Wordt de nieuwe werkwijze goed en veilig gebruikt?"
Intro: "Elke afdeling bouwt een muur van vijf lagen: bekend, getraind, gebruikt, beheerst en geborgd. Een laag ligt pas als het eigen signaal is gemeten en de grens haalt. Een laag boven een gat draagt niet: veel gebruik zonder aangetoonde beheersing is een risico, geen succes."
Contextblok: "Gestructureerde nachtoverdracht op de tablet, brede invoering na de pilot" / "ADOPT-DEMO-04, woonzorglocatie De Linde (fictief), vier afdelingen, live sinds 2026-09-07. Peilmoment 2026-10-03. Adoptieplan demo v1." / "Eigenaar: proceseigenaar zorg met opleidingsverantwoordelijke (voorgestelde rollen). FAB levert gebruiksgegevens en beheert de inrichting." / "Gebruiksmoment: nazorgoverleg."
Werksectie-h2: "Muren per afdeling"

Statisch blok "Lagen en signalen" (altijd zichtbaar, ook zonder JS), in volgorde van onder naar boven:

- **Bekend:** de teamleider bevestigt dat de werkwijze in het werkoverleg is uitgelegd. Bron: verslag werkoverleg.
- **Getraind:** vaste medewerkers met afgeronde e-learning én praktijkinstructie, grens 90 %. Bron: leerregistratie.
- **Gebruikt:** nachtdiensten van de laatste twee weken met de overdracht in het formulier, grens 85 %. Bron: gebruiksmeting in het ECD door FAB.
- **Beheerst:** ochtendoverdrachten in een steekproef zonder ontbrekend verplicht onderdeel, grens 90 %, steekproef minimaal 20. Bron: steekproef door de kwaliteitsmedewerker.
- **Geborgd:** werkinstructie vastgesteld én opgenomen in het inwerkprogramma van de afdeling. Bron: kwaliteitshandboek en inwerkprogramma.

### Visueel concept: metselwerk met maatlijnen

Vier muren naast elkaar (≥ 1000 px; 2 × 2 tussen 600 en 1000 px; onder elkaar daaronder) zijn het opvallende element. Elke muur is opgebouwd uit vijf lagen kalkzandsteen (`--block` met voegen in `--mortar`, getekend met een herhalend voegpatroon of inline SVG), Bekend onderaan, Geborgd als bovenste laag. DOM-volgorde is L1 → L5 (de leesvolgorde volgt de opbouw); visueel van onder naar boven.

- Ligt: volle laag met voegen, laagnaam en korte status in de laag.
- Gemeten, onder de grens of steekproef te klein: alleen het gemeten deel is gevuld (breedte = percentage), de rest is een lege uitsparing; een bouwkundige maatlijn in `--blueprint` (dunne lijn met korte schuine eindstreepjes) markeert de grens met tekst "grens 90 %".
- Niet gemeten: gestippelde omtrek, geen vulling, tekst "Niet gemeten".
- Draagt niet: een laag die ligt terwijl een lagere laag niet ligt, zweeft met een zichtbare spleet eronder; de spleet is gevuld met een geel-zwarte bouwlintarcering (`--tape` en `--ink`). De woorden staan in de laag zelf.
  Onder iedere muur: de stand (`.stand`), aandachtssignalen (`.signals`), het advies (`.advice`) en de acties. Een laag die na een gebruikersactie gaat liggen, zakt kort op zijn plek (± .3s), uit bij reduced motion.

Tokens:

- `--site:#D9DEE0` (pagina)
- `--block:#ECE8DC` (kalkzandsteen)
- `--mortar:#A7A69C`
- `--ink:#1C2630`
- `--blueprint:#2A5C8F` (maatlijnen, grens, focus, links)
- `--tape:#E8C547` (alleen in de arcering van 'draagt niet')
- `--muted:#55606A`
  Type: display `"Skia","Tw Cen MT","Century Gothic",sans-serif` (h1, h2, afdelingsnamen, laagnamen); body `"Hoefler Text","Constantia","Cambria",Georgia,serif` 16.5px/1.65. Links uitgelijnd.

```
FAB / Adoptiekaart                         Synthetische demonstratie, geen adoptiemeting
Wordt de nieuwe werkwijze goed   | Gestructureerde nachtoverdracht ... ADOPT-DEMO-04
en veilig gebruikt?              |
Lagen en signalen: bekend / getraind / gebruikt / beheerst / geborgd
[Simuleer gewijzigde werkinstructie][Simuleer vaststelling v2] [Herstel][Kopieer][Druk af]
#tally
 Esdoorn        Hazelaar          Beuk            Wilg
 [ Geborgd  ┆ ]  [ Geborgd  ┆ ]   [ Geborgd ┆ ]   [ Geborgd ┆ ]
 [ Beheerst  ]  [ Beheerst   ]   [ - - - - - ]   [ - - - - - ]
 [ Gebruikt  ]  [ Gebruikt   ]   [ Gebruikt  ]   [ Gebr. ┆   ]
 [ Getraind  ]  /////////////    [ Getraind  ]   [ Getr.  ┆  ]
 [ Bekend    ]  [ Getr. ┆ ]      [ Bekend    ]   [ - - - - - ]
 [ Bekend    ]
 stand, signalen, advies, acties per muur
```

Print: geen arcering of voegpatroon; per afdeling een tabel met laag, status, stand, signalen en advies.

### Data

| afdeling (`data-dept`) | L1 Bekend            | L2 Getraind | L3 Gebruikt | L4 Beheerst  | L5 inwerkprogramma | steekproef bij simulatie |
| ---------------------- | -------------------- | ----------- | ----------- | ------------ | ------------------ | ------------------------ |
| `esdoorn` Esdoorn      | bevestigd 2026-09-10 | 27 / 29     | 52 / 56     | 23 / 25      | nee                | —                        |
| `hazelaar` Hazelaar    | bevestigd 2026-09-10 | 25 / 28     | 50 / 56     | 18 / 20      | nee                | —                        |
| `beuk` Beuk            | bevestigd 2026-09-14 | 30 / 31     | 49 / 56     | niet gemeten | nee                | 17 / 22                  |
| `wilg` Wilg            | niet gemeten         | 22 / 30     | 31 / 56     | niet gemeten | nee                | 9 / 12                   |

Werkinstructie (gedeeld): "Werkinstructie nachtoverdracht v1, vastgesteld 2026-09-01 door proceseigenaar zorg (demo)".

### Controles

Per muur (`data-dept`):

- `data-action="confirm"` "Simuleer bevestiging door teamleider": alleen bij L1 niet gemeten → bevestigd 2026-10-03 (simulatie).
- `data-action="train"` "Simuleer extra praktijkinstructie (3 medewerkers)": alleen als L2 niet ligt → teller + 3, maximaal de noemer.
- `data-action="sample"` "Simuleer steekproef kwaliteitsmedewerker": alleen bij L4 niet gemeten en een steekproef in de data → L4 krijgt die waarde, "Kwaliteitsmedewerker (demo), 2026-10-03".
- `data-action="embed"` "Simuleer opname in het inwerkprogramma": alleen bij inwerkprogramma nee → ja, 2026-10-03 (simulatie).

Globaal:

- `data-action="instr-change"` "Simuleer gewijzigde werkinstructie": eenmalig. Werkinstructie wordt "v2, gewijzigd, nog niet vastgesteld"; L1 van alle afdelingen terug naar niet gemeten met de toevoeging "Werkinstructie gewijzigd: teamleider bevestigt opnieuw".
- `data-action="instr-adopt"` "Simuleer vaststelling werkinstructie v2 door proceseigenaar": alleen na `instr-change` en zolang v2 niet vastgesteld is → "Werkinstructie nachtoverdracht v2, vastgesteld 2026-10-03 (simulatie)".

### Regels (één functie `assess(dept)`; muren, register-updates, telling en export gebruiken die)

1. **Laagstatus (`.course[data-layer] .state`):**
   - L1: "Bevestigd door teamleider, <datum>" (ligt) of "Niet gemeten" (eventueel met de toevoeging uit `instr-change`).
   - L2–L4 niet gemeten: "Niet gemeten".
   - L4 met noemer < 20: "Gemeten, steekproef te klein: <n> van minimaal 20" (ligt niet).
   - L2–L4 gemeten: "Gemeten, haalt de grens: <t> van <n> (<p> %), grens <g> %" (ligt) of "Gemeten, onder de grens: <t> van <n> (<p> %), grens <g> %". Rekenen met onafgeronde waarden.
   - L5: ligt als de werkinstructie vastgesteld is én het inwerkprogramma ja is: "Werkinstructie vastgesteld en opgenomen in het inwerkprogramma". Anders "Niet aangetoond: werkinstructie gewijzigd, nog niet vastgesteld" of "Niet aangetoond: nog niet in het inwerkprogramma" (eerste die geldt).
   - Een laag die ligt terwijl een lagere laag niet ligt: status aangevuld met "Ligt, maar draagt niet: <naam van de laagste ontbrekende laag> ontbreekt".
1. **Stand (`.stand`):** de hoogste laag die ononderbroken vanaf Bekend ligt: "Stand: bekend" … "Stand: geborgd", of "Stand: nog niets aangetoond".
1. **Signalen (`.signals`):** "Gebruik zonder aangetoonde training" als L3 ligt en L2 niet; "Gebruik zonder aangetoonde beheersing" als L3 ligt en L4 niet. Geen signaal: "Geen aandachtssignaal".
1. **Advies (`.advice`), eerste die geldt:**
   1. L3 ligt en L2 niet → "Plan praktijkinstructie voor de nog niet getrainde medewerkers en controleer de overdrachten van deze afdeling extra."
   1. L3 ligt en L4 niet gemeten → "Laat de kwaliteitsmedewerker een steekproef doen: gebruik bewijst geen goede registratie."
   1. L3 ligt en L4 steekproef te klein → "Vergroot de steekproef tot minimaal 20 overdrachten."
   1. L3 ligt en L4 onder de grens → "Bespreek de ontbrekende onderdelen met het team en de kerngebruiker; pas zo nodig de instructie aan."
   1. Laagste ontbrekende laag L1 → "Vraag de teamleider de uitleg in het werkoverleg te bevestigen."; L2 → "Plan training en praktijkinstructie voor de nog niet getrainde medewerkers."; L3 → "Zoek met de kerngebruiker uit waarom het formulier niet wordt gebruikt."
   1. L5 ligt niet: werkinstructie niet vastgesteld → "Laat de gewijzigde werkinstructie vaststellen door de proceseigenaar."; anders → "Neem de werkinstructie op in het inwerkprogramma van de afdeling."
   1. Anders → "Borging aangetoond; plan een herbeoordeling over drie maanden (demo-afspraak)."
      Altijd gevolgd door "Advies, geen besluit. De proceseigenaar besluit over extra ondersteuning; trainingsdeelname bewijst geen vaardigheid."
1. **`#tally` (aria-live):** "Esdoorn: <stand>. Hazelaar: <stand>. Beuk: <stand>. Wilg: <stand>. <k> afdeling(en) met gebruik zonder aangetoonde training of beheersing." met `<stand>` in kleine letters zonder "Stand: " en "1 afdeling" / "<k> afdelingen" (ook "0 afdelingen"). Geen totaalscore of gemiddeld percentage over afdelingen.

### Verwachte uitkomsten (worden getest; met de hand nagerekend)

- Begin: `.stand` Esdoorn "Stand: beheerst", Hazelaar "Stand: bekend", Beuk "Stand: gebruikt", Wilg "Stand: nog niets aangetoond". Hazelaar L2 `.state` "Gemeten, onder de grens: 25 van 28 (89,3 %), grens 90 %"; Hazelaar L3 `.state` bevat "Gemeten, haalt de grens: 50 van 56 (89,3 %), grens 85 %" en "Ligt, maar draagt niet: Getraind ontbreekt"; Hazelaar `.signals` "Gebruik zonder aangetoonde training"; advies Hazelaar begint met "Plan praktijkinstructie"; Beuk advies begint met "Laat de kwaliteitsmedewerker"; Wilg advies begint met "Vraag de teamleider"; Esdoorn L5 "Niet aangetoond: nog niet in het inwerkprogramma", advies "Neem de werkinstructie op"; `#tally` "Esdoorn: beheerst. Hazelaar: bekend. Beuk: gebruikt. Wilg: nog niets aangetoond. 2 afdelingen met gebruik zonder aangetoonde training of beheersing."
- Hazelaar train → L2 "Gemeten, haalt de grens: 28 van 28 (100,0 %), grens 90 %"; stand "Stand: beheerst"; L3 zonder "draagt niet"; `train` disabled; `#tally` eindigt op "1 afdeling met gebruik zonder aangetoonde training of beheersing."
- Beuk sample → L4 "Gemeten, onder de grens: 17 van 22 (77,3 %), grens 90 %"; stand blijft "Stand: gebruikt"; advies begint met "Bespreek de ontbrekende onderdelen".
- Wilg sample → L4 "Gemeten, steekproef te klein: 12 van minimaal 20"; advies blijft "Vraag de teamleider"; Wilg train → "25 van 30 (83,3 %)", nog onder de grens; nogmaals → "28 van 30 (93,3 %)", haalt de grens.
- Esdoorn embed → stand "Stand: geborgd"; advies begint met "Borging aangetoond".
- Daarna instr-change → alle L1 "Niet gemeten" met "teamleider bevestigt opnieuw"; Esdoorn stand "Stand: nog niets aangetoond"; Esdoorn L2 bevat "Ligt, maar draagt niet: Bekend ontbreekt"; Esdoorn L5 "Niet aangetoond: werkinstructie gewijzigd, nog niet vastgesteld"; Esdoorn advies "Vraag de teamleider"; Esdoorn confirm → stand "Stand: beheerst", advies "Laat de gewijzigde werkinstructie vaststellen"; instr-adopt → stand "Stand: geborgd".
- Export begint met "Adoptiekaart / ADOPT-DEMO-04 / demo v1 / revisie 2026-10-03" en bevat de lagen met signaal, grens en bron, de werkinstructieversie en per afdeling iedere laagstatus, de stand, signalen en het advies.
- Reset → beginstand.

Statisch register: `.register article` × 4 (`id="adopt-static-esdoorn"` …) met per laag de beginstatus in woorden, stand, signalen en advies. Daarnaast één alinea met de regels in volgorde.

Taak-details: **Gebruiker en uitkomst:** FAB bij het nazorgoverleg met de proceseigenaar, opleidingsverantwoordelijke, kwaliteitsmedewerker en kerngebruikers; de uitkomst is per afdeling een ondersteuningsactie en zicht op borging. De proceseigenaar besluit. **Bron:** synthetische adoptiesignalen, demo v1, revisie 2026-10-03; de echte leerregistratie, gebruiksmeting, steekproefmethode en bronhouder (proceseigenaar met opleidings-/adoptieverantwoordelijke) zijn niet vastgesteld. Herzie na iedere meetperiode en bij een gewijzigde werkinstructie. **Regels:** elke laag heeft een eigen signaal; niet gemeten is onbekend, niet groen; trainingsdeelname bewijst geen vaardigheid en gebruik geen goede registratie; een laag boven een gat draagt niet; een gewijzigde werkinstructie vraagt opnieuw bekendmaking en vaststelling; geen totaalscore. **Praktijktoets:** vergelijk met het huidige nazorgverslag en de trainingslijst op herkenning van gebruik zonder beheersing, juiste ondersteuningsactie en eigenaar.

Nav: `fab-pilot-cockpit.html` "Pilot Cockpit", `fab-releaseatelier.html` "Releaseatelier", `fab-test-coverage-map.html` "Testsporen en bewijs", `../incident_en_continuiteit/fab-known-error-map.html` "Bekende fouten".

______________________________________________________________________

## Inventaris en documentatie

- Na toevoeging: **32 HTML-bestanden voor 31 concepten: 26 FAB-concepten en 5 bron- en kennisconcepten**, **4 open kandidaten** (Functional Blueprint, Leverancierskaart, Eigenaarschapkaart, Stakeholder Impact Map). Werk de aantallen bij in `AGENTS.md` (Opzet) en de ideeënnotitie (Bronbeschikbaarheid, Aanvullende templatekandidaten, Status en afbakening).
- Vink in de ideeënnotitie Data Lineage, Release Impact Explorer en Adoptiekaart af met een korte beschrijving van de aanwezige interactie en een bestandslink, zoals bij de eerdere rondes. Noem ze in de opsomming van uitgewerkte kandidaten en voeg aan de alinea onder "Drie inhoudelijke prioriteiten" een zin over deze derde ronde toe met een link naar deze specificatie. Vul de rij "Technisch getest" aan met de nieuwe scenario's. Vermeld bij Stakeholder Impact Map dat het doelgroepfilter van de Release Impact Explorer een deel van die vraag dekt; de kandidaat blijft open.
- Voeg in `docs/template-reuse.md` drie bestandskaarten toe in dezelfde vorm, en neem de patronen op in de selectietabel (ketenafwijking op één gegeven → Data Lineage; leveranciers- of releasedocument → Release Impact Explorer; invoering en nazorg → Adoptiekaart).
- Voeg de drie bestanden toe aan `TASK_FILES` in `test/support.py`, aan `FILES` in `test/test_task_views.py`, aan de print/no-JS-takken in `test/test_pages.py`, en werk de dekkingstabel in `test/README.md` bij.
