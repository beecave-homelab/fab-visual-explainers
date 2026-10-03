"""Bewijsfasen, omgevingverschillen, bekende fouten en levenscyclustermijnen in de taakviews."""

from playwright.sync_api import Page
from support import visual_path

FILES = [
    "fab-test-coverage-map.html",
    "fab-continuiteitskaart.html",
    "fab-data-quality-map.html",
    "fab-omgevingsvergelijker.html",
    "fab-known-error-map.html",
    "fab-life-cycle-map.html",
    "fab-escalatiekaart.html",
    "fab-risk-control-map.html",
    "fab-pilot-cockpit.html",
    "fab-data-lineage.html",
    "fab-release-impact-explorer.html",
    "fab-adoptiekaart.html",
]


def ensure(value: bool, message: str) -> None:
    """Geef een scenario-specifieke foutmelding bij een afwijking."""
    assert value, message


def open_file(page: Page, name: str) -> None:
    """Open een taakview uit de huidige checkout."""
    page.goto(visual_path(name).as_uri(), wait_until="networkidle")


def test_coverage__evidence_rejection_and_filter_focus(page: Page) -> None:
    """Uitvoering, bewijscontrole en bevoegd akkoord blijven afzonderlijke stappen."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[0])
    track = page.locator('[data-test="T-01"]')
    ensure(
        track.locator('[data-action="accept"]').is_disabled(), "Test: cannot accept absent evidence"
    )
    ensure(
        track.locator('[data-action="control"]').is_disabled(),
        "Test: cannot control absent execution",
    )
    track.locator('[data-action="pass"]').click()
    ensure(
        track.locator(".status").inner_text() == "Uitgevoerd, niet gecontroleerd",
        "Test: execution separate from control",
    )
    ensure(
        track.locator('[data-action="accept"]').is_disabled(),
        "Test: execution alone cannot be accepted",
    )
    track.locator('[data-action="control"]').click()
    track.locator('[data-action="accept"]').click()
    ensure(
        "4 van 5" in page.locator("#coverage").inner_text(),
        "Test: accepted track updates overall gaps",
    )
    page.locator("#copy").click()
    ensure(
        "Akkoord (simulatie)" in page.locator("#export-text").input_value(),
        "Test: export agrees with accepted status",
    )
    track.locator('[data-action="change"]').click()
    ensure(
        "Herbeoordeling nodig" == track.locator(".status").inner_text(),
        "Test: new evidence invalidates acceptance",
    )
    ensure("5 van 5" in page.locator("#coverage").inner_text(), "Test: evidence change reopens gap")
    ensure(
        "Vorig akkoord ongeldig" in page.locator("#export-text").input_value(),
        "Test: visible export refreshes after evidence change",
    )
    track.locator('[data-action="fail"]').click()
    ensure(
        track.locator('[data-action="accept"]').is_disabled(),
        "Test: failed test cannot be accepted",
    )
    ensure(
        "1 afgekeurd" in page.locator("#coverage").inner_text(), "Test: failure counted separately"
    )
    track.locator('[data-action="pass"]').click()
    track.locator('[data-action="control"]').click()
    track.locator('[data-action="reject"]').click()
    ensure(
        track.locator(".status").inner_text() == "Afgekeurd (simulatie)",
        "Test: explicit reviewer rejection supported",
    )
    page.locator('[data-select="T-05"]').click()
    ensure(
        page.locator('[data-test="T-05"] [data-action="pass"]').is_disabled(),
        "Test: continuity test blocked without local plan",
    )
    page.locator("#filter").select_option("risk")
    ensure(
        page.locator(".track:visible").count() == 2,
        "Test: risk filter shows privacy and continuity only",
    )
    page.locator("#reset").click()
    page.locator("#filter").select_option("open")
    track.locator('[data-action="pass"]').click()
    track.locator('[data-action="control"]').click()
    track.locator('[data-action="accept"]').click()
    ensure(not track.is_visible(), "Test: accepted track disappears from open filter")
    ensure(
        page.evaluate("document.activeElement.id") == "filter",
        "Test: focus returns to filter after accepted track disappears",
    )
    page.emulate_media(media="print")
    ensure(
        page.locator(".track:visible").count() == 5,
        "Test: print includes all current tracks regardless of filter",
    )
    page.emulate_media(media="screen")
    page.locator("#reset").click()
    page.locator('[data-select="T-02"]').focus()
    page.keyboard.press("Enter")
    ensure(page.locator("#detail-T-02").is_visible(), "Test: keyboard opens track")


def test_continuity__source_change_revokes_recovery(page: Page) -> None:
    """Uitvoering, bewijscontrole en bevoegd akkoord blijven afzonderlijke stappen."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[1])
    ensure(page.locator("#confirm").is_disabled(), "Continuity: absent source blocks confirmation")
    for item in page.locator("[data-check]").all():
        item.check()
    ensure(
        page.locator("#confirm").is_disabled(), "Continuity: four checks do not bypass absent plan"
    )
    page.locator("#plan").select_option("demo")
    ensure(
        page.locator("[data-check]:checked").count() == 0,
        "Continuity: source change clears stale checks",
    )
    for item in page.locator("[data-check]").all():
        item.check()
    page.locator("#confirm").click()
    ensure(
        "Hervatting bevestigd binnen de oefening" in page.locator("#recovery").inner_text(),
        "Continuity: separate authorized simulated confirmation",
    )
    ensure(
        "Gereedheid niet aangetoond" in page.locator("#readiness").inner_text(),
        "Continuity: simulation never implies local readiness",
    )
    page.emulate_media(media="print")
    ensure(
        page.locator(".check-state:visible").count() == 4,
        "Continuity: print includes each recovery control status",
    )
    ensure(
        page.locator(".check-state").evaluate_all(
            '(nodes)=>nodes.every(n=>n.textContent.includes("Gecontroleerd (simulatie)"))'
        ),
        "Continuity: printed control states agree with checked simulation",
    )
    page.emulate_media(media="screen")
    page.locator("#copy").click()
    ensure(
        "Hervatting bevestigd binnen de oefening" in page.locator("#export-text").input_value(),
        "Continuity: export matches confirmation",
    )
    page.locator('[data-check="tech"]').uncheck()
    ensure(
        "Hervatting niet bevestigd" in page.locator("#recovery").inner_text(),
        "Continuity: removing a check revokes confirmation",
    )
    page.locator("#outage").select_option("network")
    ensure(
        "netwerkshare" in page.locator("#offline").inner_text(),
        "Continuity: network outage changes offline requirement",
    )
    ensure(
        page.locator("[data-check]:checked").count() == 0,
        "Continuity: changed outage invalidates checks",
    )
    page.locator("#outage").select_option("iam")
    ensure(
        "gedeelde accounts" in page.locator("#technical-check").inner_text(),
        "Continuity: IAM scenario includes safe access boundary",
    )
    page.locator("#plan").select_option("changed")
    ensure(
        "Herbeoordeling nodig" in page.locator("#readiness").inner_text(),
        "Continuity: changed source requires reassessment",
    )
    ensure(page.locator("#confirm").is_disabled(), "Continuity: changed source blocks confirmation")
    ensure(
        "v2" in page.locator("#export-text").input_value(),
        "Continuity: visible export updates source version",
    )


def test_quality__overlap_and_controlled_repair(page: Page) -> None:
    """Uitvoering, bewijscontrole en bevoegd akkoord blijven afzonderlijke stappen."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[2])
    ensure(page.locator(".message-cell").count() == 120, "Quality: all 120 message positions drawn")
    ensure(
        "10 regelmarkeringen op 6 berichtposities" in page.locator("#union").inner_text(),
        "Quality: overlap deduplicated explicitly",
    )
    rule = page.locator('[data-rule="DQ-01"]')
    ensure(
        page.locator(".message-cell.active").count() == 3,
        "Quality: selected rule highlights its three positions",
    )
    ensure(
        rule.locator('[data-action="verify"]').is_disabled(),
        "Quality: absent execution cannot be checked",
    )
    rule.locator('[data-action="plan"]').click()
    ensure(
        page.locator(".message-cell.active").count() == 3,
        "Quality: proposed repair does not remove deviations",
    )
    rule.locator('[data-action="execute"]').click()
    ensure(
        page.locator(".message-cell.active").count() == 3,
        "Quality: execution alone does not prove resolution",
    )
    rule.locator('[data-action="verify"]').click()
    ensure(
        page.locator(".message-cell.active").count() == 0,
        "Quality: checked simulation clears selected flags",
    )
    ensure(
        "7 regelmarkeringen op 5 berichtposities" in page.locator("#union").inner_text(),
        "Quality: overlap remains in other rules",
    )
    page.locator("#copy").click()
    ensure(
        "DQ-01" in page.locator("#export-text").input_value()
        and "Aansluiting gecontroleerd" in page.locator("#export-text").input_value(),
        "Quality: export matches controlled status",
    )
    rule.locator('[data-action="change"]').click()
    ensure(
        page.locator(".message-cell.active").count() == 3,
        "Quality: changed rule restores unknown deviations",
    )
    ensure(
        "Herbeoordeling ontbreekt" in page.locator("#export-text").input_value(),
        "Quality: export marks invalidated control",
    )
    page.locator("#all").click()
    ensure(
        page.locator(".message-cell.active").count() == 6,
        "Quality: all lens uses unique positions not sum of rules",
    )
    page.locator('[data-select="DQ-03"]').focus()
    page.keyboard.press("Enter")
    ensure(page.locator("#detail-DQ-03").is_visible(), "Quality: keyboard opens rule")


def test_environments__staleness_and_reassessment(page: Page) -> None:
    """Verschil, veroudering en gewijzigde productie sturen oordeel en export."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[3])

    def state(aspect: str) -> str:
        """Lees de statuscel van een aspectrij."""
        return page.locator(f'[data-aspect="{aspect}"] .state').inner_text()

    ensure(state("app") == "Gelijk", "Environments: equal aspect is Gelijk")
    ensure(
        "Gelijk aan doelstand" in state("connector"),
        "Environments: change itself is not a difference",
    )
    ensure(
        "Onbekend" in state("mapping") and "Opgave, niet vergeleken" in state("mapping"),
        "Environments: unverified entry is unknown, not equal",
    )
    ensure("Verschil" in state("endpoint"), "Environments: supplier stub differs from portal")
    ensure(
        "Aanvullende test nodig" in page.locator("#verdict").inner_text(),
        "Environments: a difference requires an extra test",
    )
    page.locator('[data-track="T-02"]').focus()
    page.keyboard.press("Enter")
    ensure(
        "Geen bekend verschil" in page.locator("#verdict").inner_text(),
        "Environments: T-02 on acceptatie has no known difference",
    )
    page.locator("#source").select_option("tst")
    ensure("Verouderd" in state("app"), "Environments: snapshot older than 14 days is stale")
    ensure("Verschil" in state("testroles"), "Environments: broad test role differs")
    ensure(
        "Aanvullende test nodig" in page.locator("#verdict").inner_text(),
        "Environments: difference and staleness keep extra test verdict",
    )
    page.locator("#source").select_option("acc")
    page.locator('[data-track="T-01"]').click()
    page.locator('[data-aspect="mapping"] [data-action="compare"]').click()
    ensure(
        "Gelijk aan doelstand" in state("mapping"),
        "Environments: simulated comparison verifies entry",
    )
    ensure(
        "Aanvullende test nodig" in page.locator("#verdict").inner_text(),
        "Environments: remaining endpoint difference keeps verdict",
    )
    page.locator('[data-track="T-02"]').click()
    page.locator('[data-aspect="rolmodel"] [data-action="change"]').click()
    ensure(
        "Herbeoordeling nodig" in state("rolmodel"),
        "Environments: changed production invalidates comparison",
    )
    ensure(
        "Nog niet vast te stellen" in page.locator("#verdict").inner_text(),
        "Environments: reassessment counts as unknown",
    )
    page.locator("#copy").click()
    ensure(
        "Kopiëren niet beschikbaar" in page.locator("#message").inner_text(),
        "Environments: denied clipboard shows fallback",
    )
    exported = page.locator("#export-text").input_value()
    ensure(
        "Herbeoordeling nodig" in exported and "Nog niet vast te stellen" in exported,
        "Environments: export follows the simulated screen state",
    )
    page.emulate_media(media="print")
    ensure(
        page.locator("[data-action]:visible").count() == 0,
        "Environments: print hides simulation buttons",
    )
    ensure(
        page.locator(".register tr[data-static-aspect]:visible").count() == 8,
        "Environments: print shows the full register",
    )


def test_known_errors__signs_conditions_and_approval(page: Page) -> None:
    """Kenmerken zijn aanwijzingen; goedkeuring, versie en voorwaarden begrenzen gebruik."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[4])
    ensure(
        page.locator(".tear").all_inner_texts() == ["Geen aanwijzing"] * 4,
        "Known errors: no sign means no indication",
    )
    ensure(
        "Geen goedgekeurde werkwijze toepasbaar" in page.locator("#verdict").inner_text(),
        "Known errors: empty triage verdict",
    )
    page.locator('[data-select="KE-DEMO-03"]').focus()
    page.keyboard.press("Enter")
    ensure(
        page.locator("#detail-KE-DEMO-03").is_visible(),
        "Known errors: keyboard opens hang tag",
    )
    page.locator('[data-select="KE-DEMO-07"]').click()
    for sign in ("s1", "s2", "s3"):
        page.locator(f'[data-sign="{sign}"]').check()
    tag7 = page.locator('[data-select="KE-DEMO-07"]')
    ensure(
        "Past bij 3 van 3 kenmerken" in tag7.inner_text(),
        "Known errors: matched signs counted on tear strip",
    )
    outcome = page.locator("#detail-KE-DEMO-07 .outcome")
    ensure(
        "Niet als goedgekeurd gebruiken" in outcome.inner_text(),
        "Known errors: expired review blocks approved use",
    )
    ensure(
        page.locator("#detail-KE-DEMO-07 [data-condition]").first.is_disabled(),
        "Known errors: conditions stay disabled while review expired",
    )
    page.locator('[data-action="reconfirm"][data-ke="KE-DEMO-07"]').click()
    ensure(
        "Controleer de toepassingsvoorwaarden" in outcome.inner_text(),
        "Known errors: reconfirmed item still needs its conditions",
    )
    for box in page.locator("#detail-KE-DEMO-07 [data-condition]").all():
        box.check()
    ensure(
        "Toepasbaar binnen deze oefening" in outcome.inner_text(),
        "Known errors: all confirmed conditions allow use",
    )
    page.locator("#copy").click()
    ensure(
        "Toepasbaar binnen deze oefening" in page.locator("#export-text").input_value(),
        "Known errors: export matches simulated approval",
    )
    page.locator('[data-sign="s7"]').check()
    ensure(
        "Kenmerk past niet" in outcome.inner_text()
        and "continuïteitsroute" in outcome.inner_text(),
        "Known errors: excluded sign blocks use and points to continuity route",
    )
    ensure(
        page.locator("#detail-KE-DEMO-07 [data-condition]:checked").count() == 0,
        "Known errors: changed signs reset confirmations",
    )
    page.locator('[data-sign="s7"]').uncheck()
    page.locator("#version").select_option("2026.4")
    ensure(
        "Geldigheid voor ECD 2026.4 niet vastgesteld" in outcome.inner_text(),
        "Known errors: unassessed version is not usable",
    )
    page.locator('[data-sign="s5"]').check()
    ensure(
        "Alleen escalatieroute" in page.locator("#detail-KE-DEMO-11 .outcome").inner_text()
        and "Verwijder of herverwerk niets zelf" in page.locator("#detail-KE-DEMO-11").inner_text(),
        "Known errors: concept item offers escalation only",
    )
    page.locator('[data-sign="s6"]').check()
    page.locator('[data-select="KE-DEMO-14"]').click()
    page.locator('[data-action="revise"][data-ke="KE-DEMO-14"]').click()
    ensure(
        "Concept" in page.locator("#detail-KE-DEMO-14").inner_text()
        and "eerdere goedkeuring ongeldig" in page.locator("#detail-KE-DEMO-14").inner_text(),
        "Known errors: changed workaround invalidates earlier approval",
    )
    page.locator("#reset").click()
    ensure(
        page.locator(".tear").all_inner_texts() == ["Geen aanwijzing"] * 4,
        "Known errors: reset restores the starting board",
    )
    page.emulate_media(media="print")
    ensure(
        page.locator("[data-action]:visible").count() == 0,
        "Known errors: print hides simulation buttons",
    )
    ensure(
        page.locator(".register article:visible").count() == 4,
        "Known errors: print shows every known error",
    )


def test_lifecycle__dates_thresholds_and_dependencies(page: Page) -> None:
    """Uiterlijke start, afhankelijkheid en onbevestigde bronnen sturen de status."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[5])
    states = page.locator(".stateline").all_inner_texts()
    ensure(
        "Start uiterlijk verstreken" in states[0],
        "Lifecycle: tablet dependency pulls ECD start past the peildatum",
    )
    ensure(
        states[1] == "Start binnen 8 weken (op basis van onbevestigde opgave)",
        "Lifecycle: unconfirmed source stays visible",
    )
    ensure(states[2] == "Einddatum onbekend", "Lifecycle: unknown end gives no calculation")
    ensure(states[3] == "Bewaken", "Lifecycle: distant start stays on watch")
    ensure(states[4] == "Start binnen 8 weken", "Lifecycle: tablet OS within threshold")
    ensure(
        "1 verstreken, 2 binnen 8 weken, 1 bewaken, 0 buiten ondersteuning, 1 einddatum onbekend"
        in page.locator("#summary").inner_text(),
        "Lifecycle: summary counts each status",
    )
    page.locator('[data-select="tabletos"]').focus()
    page.keyboard.press("Enter")
    ensure(
        page.locator("#detail-tabletos").is_visible(),
        "Lifecycle: keyboard opens column detail",
    )
    page.locator("#date").focus()
    for _ in range(4):
        page.keyboard.press("ArrowRight")
    ensure(
        page.locator("#date-label").inner_text() == "2027-02-01",
        "Lifecycle: arrow keys move the peildatum",
    )
    states = page.locator(".stateline").all_inner_texts()
    ensure(
        states[1].startswith("Buiten ondersteuning")
        and states[4].startswith("Buiten ondersteuning"),
        "Lifecycle: past the end means unsupported",
    )
    page.locator("#reset").click()
    page.locator('[data-action="roadmap"]').click()
    ensure(
        "Bewaken (op basis van onbevestigde opgave)"
        in page.locator(".stateline").all_inner_texts()[1],
        "Lifecycle: later roadmap pushes start beyond threshold",
    )
    ensure(
        "Herbeoordeling nodig" in page.locator("#detail-rooster").inner_text(),
        "Lifecycle: changed roadmap requires reassessment",
    )
    page.locator('[data-action="confirm"]').click()
    ensure(
        page.locator(".stateline").all_inner_texts()[1] == "Bewaken",
        "Lifecycle: confirmation removes the unconfirmed marker",
    )
    page.locator('[data-select="connector"]').click()
    page.locator('[data-action="enddate"]').click()
    ensure(
        page.locator(".stateline").all_inner_texts()[2] == "Bewaken",
        "Lifecycle: fixed end date enables a calculated start",
    )
    page.locator("#copy").click()
    exported = page.locator("#export-text").input_value()
    ensure(
        "Vastgesteld in wijzigingsplan (simulatie)" in exported
        and "Bevestigd (simulatie)" in exported,
        "Lifecycle: export follows the simulated source state",
    )
    page.emulate_media(media="print")
    ensure(
        page.locator("[data-action]:visible").count() == 0,
        "Lifecycle: print hides simulation buttons",
    )
    ensure(
        page.locator(".register article:visible").count() == 5,
        "Lifecycle: print shows every register entry",
    )


def test_escalation__levels_routes_and_handover(page: Page) -> None:
    """Gevolgen bepalen het peil; pakket en actuele route begrenzen de overdracht."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[6])

    def level(n: str):
        """Peilrij of privacytak op peil n."""
        return page.locator(f'section[data-level="{n}"]')

    ensure(
        level("l0").locator(".state").inner_text() == "Nu aan zet",
        "Escalation: servicedesk starts on duty",
    )
    for n in ("l1", "l2", "l3", "pv"):
        ensure(
            level(n).locator(".state").inner_text() == "Niet nodig volgens demo-regels",
            f"Escalation: {n} inactive without an established impact",
        )
        ensure(
            level(n).locator("[data-action]:enabled").count() == 0,
            f"Escalation: {n} offers no actions while inactive",
        )
    ensure(
        "Peil 0" in page.locator("#verdict").inner_text(),
        "Escalation: empty state stays at level 0",
    )
    page.locator('[data-impact="hinder"]').check()
    ensure(
        level("l1").locator(".state").inner_text() == "Nu aan zet"
        and level("l0").locator(".state").inner_text() == "Betrokken",
        "Escalation: an established impact puts analysis on duty",
    )
    ensure(
        level("l1").locator('[data-action="send"]').is_disabled()
        and "Pakket onvolledig: 8 ontbreken" in level("l1").locator(".handover").inner_text(),
        "Escalation: incomplete package blocks handover",
    )
    for f in range(1, 9):
        page.locator(f'[data-field="f{f}"]').check()
    ensure(
        level("l1").locator('[data-action="send"]').is_enabled(),
        "Escalation: complete package enables handover",
    )
    level("l1").locator('[data-action="send"]').click()
    ensure(
        "Overgedragen, nog niet aangenomen" in level("l1").locator(".handover").inner_text(),
        "Escalation: sent is not yet accepted",
    )
    level("l1").locator('[data-action="accept"]').click()
    ensure(
        "Aangenomen door FAB zorgdossier" in level("l1").locator(".handover").inner_text(),
        "Escalation: acceptance confirms the handover",
    )
    page.locator('[data-field="f6"]').uncheck()
    ensure(
        "Pakket gewijzigd na overdracht; eerdere overdracht vervalt"
        in level("l1").locator(".handover").inner_text(),
        "Escalation: removed required field voids the handover",
    )
    page.locator('[data-field="f6"]').check()
    page.locator("#cause").select_option("vendor")
    ensure(
        level("l2").locator(".state").inner_text() == "Nu aan zet"
        and level("l1").locator(".state").inner_text() == "Betrokken",
        "Escalation: supplier cause escalates to the application owner",
    )
    ensure(
        "Leverancier via de contractroute" in page.locator("#verdict").inner_text(),
        "Escalation: verdict names the supplier partner",
    )
    for f in range(9, 13):
        page.locator(f'[data-field="f{f}"]').check()
    ensure(
        level("l2").locator('[data-action="send"]').is_disabled()
        and "Verouderd: laatst geverifieerd 2026-05-14"
        in level("l2").locator(".route").inner_text(),
        "Escalation: stale route still blocks a complete package",
    )
    level("l2").locator('[data-action="verify"]').click()
    ensure(
        level("l2").locator('[data-action="send"]').is_enabled(),
        "Escalation: verification reopens the route",
    )
    page.locator("#reset").click()
    page.locator('[data-impact="hinder"]').check()
    page.locator("#duration").select_option("gt4")
    ensure(
        level("l2").locator(".state").inner_text() == "Nu aan zet"
        and "Technisch beheer; oorzaakrichting nog vaststellen" in level("l2").inner_text(),
        "Escalation: long outage without workaround escalates with unknown partner",
    )
    page.locator("#workaround").select_option("applied")
    ensure(
        level("l1").locator(".state").inner_text() == "Nu aan zet",
        "Escalation: applied workaround de-escalates to analysis",
    )
    page.locator("#reset").click()
    page.locator('[data-impact="zorg"]').check()
    ensure(
        level("l3").locator(".state").inner_text() == "Nu aan zet",
        "Escalation: halted care support activates continuity",
    )
    ensure(
        level("l3").locator('[data-action="send"]').is_enabled(),
        "Escalation: continuity start waits for no package",
    )
    level("l3").locator('[data-action="send"]').click()
    ensure(
        "Continuïteitsproces gestart" in level("l3").locator(".handover").inner_text()
        and "Pakket onvolledig: 15 ontbreken" in level("l3").locator(".handover").inner_text()
        and "Niet geverifieerd" in level("l3").locator(".route").inner_text(),
        "Escalation: started continuity still shows gaps and unverified route",
    )
    page.locator('[data-impact="privacy"]').check()
    ensure(
        level("pv").locator(".state").inner_text() == "Parallel aan zet"
        and "datalekprocedure" in page.locator("#verdict").inner_text(),
        "Escalation: privacy risk runs parallel without raising the level",
    )
    page.locator("#copy").click()
    exported = page.locator("#export-text").input_value()
    ensure(
        exported.startswith("Escalatiekaart / INC-DEMO-0427 / demo v1 / revisie 2026-10-03"),
        "Escalation: export header identifies the simulation",
    )
    ensure(
        "FAB zorgdossier" in exported
        and "Overdracht" in exported
        and "aanwezig" in exported
        and "Ontbrekend" in exported,
        "Escalation: export lists roles, states, routes, handovers and package fields",
    )
    page.locator("#reset").click()
    ensure(
        "Peil 0" in page.locator("#verdict").inner_text()
        and page.locator("[data-field]:checked").count() == 0,
        "Escalation: reset restores the starting state",
    )


def test_risk_controls__only_tested_controls_lower_residual(page: Page) -> None:
    """Alleen getoetste werkzame maatregelen verlagen het aangetoonde restrisico."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[7])

    def risk(n: str):
        """Risicoartikel n."""
        return page.locator(f'article[data-risk="{n}"]')

    def control(n: str):
        """Maatregelregel n."""
        return page.locator(f'li[data-control="{n}"]')

    ensure(
        "Midden, privacyrisico" in risk("R1").locator(".residual").inner_text()
        and "Ernstig restrisico" in risk("R1").locator(".residual").inner_text(),
        "Risk: untested privacy risk stays severe",
    )
    ensure(
        "Laag, privacyrisico" in risk("R1").locator(".expected").inner_text(),
        "Risk: expected residual shown separately",
    )
    ensure(
        "Laag, financiële gevolgen" in risk("R2").locator(".residual").inner_text()
        and "Ernstig" not in risk("R2").locator(".residual").inner_text(),
        "Risk: tested control lowers demonstrated residual",
    )
    ensure(
        "Midden, stilgevallen zorgondersteuning" in risk("R3").locator(".residual").inner_text()
        and "Ernstig" in risk("R3").locator(".residual").inner_text(),
        "Risk: proposed measures leave the severe residual",
    )
    ensure(
        control("C6").locator('[data-action="pass"]').is_disabled()
        and control("C6").locator('[data-action="fail"]').is_disabled()
        and "noodplan ontbreekt" in control("C6").inner_text(),
        "Risk: missing local plan blocks testing",
    )
    ensure(
        "3 risico's: 0 met geaccepteerd restrisico, 3 zonder acceptatie, 2 met ernstig"
        " aangetoond restrisico. 1 van 6 maatregelen getoetst."
        == page.locator("#tally").inner_text(),
        "Risk: tally counts acceptances, severe residuals and tested controls",
    )
    control("C1").locator('[data-action="pass"]').click()
    ensure(
        "Laag, privacyrisico" in risk("R1").locator(".residual").inner_text()
        and "Ernstig" not in risk("R1").locator(".residual").inner_text(),
        "Risk: tested working control lowers demonstrated residual",
    )
    ensure(
        "1 met ernstig" in page.locator("#tally").inner_text()
        and "2 van 6" in page.locator("#tally").inner_text(),
        "Risk: tally follows the tested control",
    )
    risk("R1").locator('[data-action="accept"]').click()
    ensure(
        "Geaccepteerd (simulatie)" in risk("R1").locator(".acceptance").inner_text()
        and "nog niet getoetste maatregelen: 1" in risk("R1").locator(".acceptance").inner_text(),
        "Risk: acceptance records residual and open controls",
    )
    control("C2").locator('[data-action="execute"]').click()
    ensure(
        "Acceptatie vervallen" in risk("R1").locator(".acceptance").inner_text(),
        "Risk: control change after acceptance voids it",
    )
    control("C4").locator('[data-action="fail"]').click()
    ensure(
        "Getoetst, niet werkzaam" in control("C4").locator(".state").inner_text()
        and "Laag, financiële gevolgen" in risk("R2").locator(".residual").inner_text(),
        "Risk: failed control leaves residual on the working one",
    )
    control("C3").locator('[data-action="change"]').click()
    ensure(
        "Gewijzigd, opnieuw toetsen" in control("C3").locator(".state").inner_text()
        and "Hoog, financiële gevolgen" in risk("R2").locator(".residual").inner_text()
        and "Ernstig" in risk("R2").locator(".residual").inner_text(),
        "Risk: changed control loses its demonstrated effect",
    )
    control("C6").locator('[data-action="execute"]').click()
    ensure(
        "Uitgevoerd, niet getoetst" in control("C6").locator(".state").inner_text()
        and control("C6").locator('[data-action="pass"]').is_disabled()
        and control("C6").locator('[data-action="fail"]').is_disabled(),
        "Risk: executed fallback stays untestable without a plan",
    )
    page.locator("#copy").click()
    exported = page.locator("#export-text").input_value()
    ensure(
        exported.startswith("Risk & Control Map / RFC-2026-118 / demo v1 / revisie 2026-10-03")
        and "Aangetoond restrisico" in exported
        and "Verwacht als alle maatregelen werken" in exported
        and "Acceptatie" in exported,
        "Risk: export carries residual, expectation and acceptance",
    )
    page.locator("#reset").click()
    ensure(
        "1 van 6 maatregelen getoetst" in page.locator("#tally").inner_text(),
        "Risk: reset restores the starting state",
    )


def test_pilot__counted_weeks_brakes_and_advice(page: Page) -> None:
    """Alleen gecontroleerde weken tellen; niet gemeten is onbekend, niet groen."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async () => {throw new Error('Forced test denial')}}})"
    )
    open_file(page, FILES[8])

    def brake(n: str):
        """Statustekst van stopcriterium n."""
        return page.locator(f'li[data-brake="{n}"] .state')

    points = page.evaluate(
        """() => {
          const pl = [...document.querySelectorAll('#chart polyline')]
            .find(el => !el.getAttribute('stroke-dasharray'));
          return pl.getAttribute('points').trim().split(/\\s+/)
            .map(pair => pair.split(',').map(Number));
        }"""
    )
    ensure(
        len(points) == 7
        and all(120 < x < 700 and 20 < y < 320 for x, y in points)
        and all(points[i][0] < points[i + 1][0] for i in range(6)),
        "Pilot: chart marks every visible week in its own column, not week 8",
    )
    ensure(
        "3 van minimaal 4" in page.locator("#advice").inner_text()
        and "Nog niet te beoordelen" in page.locator("#advice").inner_text(),
        "Pilot: three counted weeks cannot be assessed",
    )
    ensure(
        "Niet gemeten" in brake("S2").inner_text(),
        "Pilot: unperformed fallback test stays unknown",
    )
    ensure(
        "Niet geraakt" in brake("S3").inner_text() and "Niet geraakt" in brake("S4").inner_text(),
        "Pilot: measured brakes below threshold",
    )
    ensure(
        "Aangeleverd, niet gecontroleerd" in page.locator('li[data-week="6"]').inner_text(),
        "Pilot: delivered week is not counted",
    )
    page.locator('[data-action="control"][data-week="6"]').click()
    ensure(
        "Gecontroleerd, telt niet mee: noemer 38, minder dan 40"
        in page.locator('li[data-week="6"]').inner_text()
        and "3 van minimaal 4" in page.locator("#advice").inner_text(),
        "Pilot: checked week under denominator threshold stays out",
    )
    page.locator('[data-action="control"][data-week="7"]').click()
    ensure(
        "Aanwijzing voor effect" in page.locator("#advice").inner_text()
        and "doorgaan pas na meting van" in page.locator("#advice").inner_text()
        and "Overdracht niet beschikbaar bij storing" in page.locator("#advice").inner_text(),
        "Pilot: indication waits for the unmeasured brake",
    )
    page.locator('[data-action="fallback-pass"]').click()
    ensure(
        "Aanwijzing voor effect; voorleggen voor een besluit over doorgaan"
        in page.locator("#advice").inner_text(),
        "Pilot: measured brakes release the indication",
    )
    page.locator('[data-action="incident"]').click()
    ensure(
        "Stoppen en voorleggen aan de pilot-eigenaar" in page.locator("#advice").inner_text(),
        "Pilot: hit stop criterion overrides the indication",
    )
    page.locator("#reset").click()
    page.locator('[data-action="control"][data-week="7"]').click()
    page.locator("#week").fill("5")
    ensure(
        "Nog niet te beoordelen" in page.locator("#advice").inner_text(),
        "Pilot: earlier cutoff leaves three counted weeks",
    )
    page.locator("#reset").click()
    page.locator('[data-action="control"][data-week="7"]').click()
    page.locator('[data-action="correct"][data-week="3"]').click()
    ensure(
        "Gecorrigeerd, opnieuw controleren" in page.locator('li[data-week="3"]').inner_text()
        and "Nog niet te beoordelen" in page.locator("#advice").inner_text(),
        "Pilot: correction returns the week to unchecked",
    )
    page.locator("#copy").click()
    exported = page.locator("#export-text").input_value()
    ensure(
        exported.startswith("Pilot Cockpit / PILOT-DEMO-04 / demo v1 / revisie 2026-10-03")
        and "Hypothese" in exported
        and "Nulmeting" in exported
        and "Stopcriterium" in exported
        and "Advies" in exported,
        "Pilot: export carries definition, weeks, brakes and advice",
    )
    page.locator("#reset").click()
    ensure(
        "Nog niet te beoordelen" in page.locator("#advice").inner_text(),
        "Pilot: reset restores the starting state",
    )


def test_lineage__stale_hops_diff_and_proposal(page: Page) -> None:
    """Alleen geldig vergeleken, ververste stappen tellen; een lading maakt vergelijkingen ongeldig."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async text => {window.copiedText = text;}}})"
    )
    open_file(page, FILES[9])

    def hop(n: str):
        """Stempelblok van stap n."""
        return page.locator(f'[data-hop="{n}"]')

    ensure(
        hop("h3").locator(".state").inner_text()
        == "Klopt met de vastgelegde transformaties vanaf Zorgdossier (ECD)",
        "Lineage: h3 traces back to the dossier past uncompared h2",
    )
    ensure(
        hop("h5").locator(".state").inner_text()
        == "Onverklaard verschil: verwacht 2027-03-31, getoond 2027-03-30",
        "Lineage: double day-shift at the BI step is unexplained",
    )
    ensure(
        hop("h2").locator(".state").inner_text() == "Niet vergeleken: onbekend"
        and hop("h4").locator(".state").inner_text() == "Niet vergeleken: onbekend",
        "Lineage: uncompared steps stay unknown",
    )
    ensure(
        "ergens tussen Zorgadministratie en BI-overzicht verloopt binnen 30 dagen"
        in page.locator("#locus").inner_text()
        and "Vergelijk Datawarehouse" in page.locator("#locus").inner_text(),
        "Lineage: locus names the enclosing compared pair and the gap",
    )
    ensure(
        page.locator('[data-action="propose"]').is_disabled(),
        "Lineage: no proposal before adjacent localization",
    )
    hop("h4").locator('[data-action="compare"]').click()
    ensure(
        hop("h4").locator(".state").inner_text() == "Klopt met de vastgelegde transformatie",
        "Lineage: h4 matches its documented transform",
    )
    ensure(
        "veranderde tussen Datawarehouse en BI-overzicht verloopt binnen 30 dagen"
        in page.locator("#locus").inner_text(),
        "Lineage: locus narrows to the adjacent pair",
    )
    page.locator('[data-action="propose"]').click()
    ensure(
        "nog niet beoordeeld" in page.locator("#proposal").inner_text()
        and "Rapportage-eigenaar met BI" in page.locator("#proposal").inner_text(),
        "Lineage: proposal names the step owner and stays unreviewed",
    )
    page.locator('[data-action="approve"]').click()
    ensure(
        "Akkoord gegevenseigenaar (simulatie)" in page.locator("#proposal").inner_text()
        and "herstel is nog niet aangetoond" in page.locator("#proposal").inner_text(),
        "Lineage: approval does not claim repair",
    )
    page.locator('[data-action="load"]').click()
    ensure(
        hop("h5").locator(".state").inner_text()
        == "Niet vergeleken: opnieuw vergelijken, lading na de vorige vergelijking",
        "Lineage: nightly load voids the h5 comparison",
    )
    ensure(
        "Voorstel vervallen" in page.locator("#proposal").inner_text(),
        "Lineage: proposal falls away when its comparison is void",
    )
    ensure(
        "Nog niet vergeleken: 3. Nog niet ververst: 0." in page.locator("#locus").inner_text(),
        "Lineage: locus counts uncompared and stale steps separately",
    )
    ensure(
        page.locator('[data-action="load"]').is_disabled(),
        "Lineage: the nightly load runs once",
    )
    page.locator("#sample").select_option("DEMO-IND-02")
    page.locator("#sample").select_option("DEMO-IND-01")
    ensure(
        "opnieuw vergelijken" in hop("h5").locator(".state").inner_text()
        and "Voorstel vervallen" in page.locator("#proposal").inner_text(),
        "Lineage: switching samples keeps each sample's comparisons and proposal",
    )
    page.locator("#reset").click()
    page.locator("#sample").select_option("DEMO-IND-02")
    ensure(
        "Nog niet vergeleken: 4. Nog niet ververst: 0." in page.locator("#locus").inner_text(),
        "Lineage: second sample starts with four uncompared steps",
    )
    for n in ("h2", "h3", "h4", "h5"):
        hop(n).locator('[data-action="compare"]').click()
    ensure(
        "Klopt" in hop("h4").locator(".state").inner_text()
        and "Niet in het overzicht" in hop("h5").locator(".value").inner_text(),
        "Lineage: empty source date stays explainable through the chain",
    )
    ensure(
        "Geen onverklaard verschil in steekproef DEMO-IND-02" in page.locator("#locus").inner_text()
        and "bewijst niet" in page.locator("#locus").inner_text(),
        "Lineage: a clean sample proves nothing for all clients",
    )
    page.locator("#reset").click()
    page.locator("#sample").select_option("DEMO-IND-03")
    ensure(
        "Nog niet ververst: geladen 2026-10-02" in hop("h4").locator(".state").inner_text()
        and "Nog niet ververst: geladen 2026-10-02" in hop("h5").locator(".state").inner_text(),
        "Lineage: steps loaded before the source change are stale",
    )
    ensure(
        hop("h4").locator('[data-action="compare"]').is_disabled()
        and hop("h5").locator('[data-action="compare"]').is_disabled(),
        "Lineage: stale steps cannot be compared yet",
    )
    ensure(
        "Nog niet vergeleken: 2. Nog niet ververst: 2." in page.locator("#locus").inner_text(),
        "Lineage: stale steps are counted separately",
    )
    page.locator('[data-action="load"]').click()
    ensure(
        "opnieuw vergelijken" in hop("h5").locator(".state").inner_text(),
        "Lineage: the earlier h5 comparison is void after loading",
    )
    hop("h5").locator('[data-action="compare"]').click()
    ensure(
        hop("h5").locator(".state").inner_text()
        == "Onverklaard verschil: verwacht 2027-06-30, getoond 2027-06-29",
        "Lineage: renewed sample still shows the undocumented day-shift",
    )
    ensure(
        "Vergelijk Integratielaag, Zorgadministratie en Datawarehouse"
        in page.locator("#locus").inner_text(),
        "Lineage: all uncompared intermediate steps narrow the locus",
    )
    page.locator("#copy").click()
    exported = page.locator("#export-text").input_value()
    ensure(
        exported.startswith("Data Lineage / SIG-DEMO-0912 / demo v1 / revisie 2026-10-03")
        and "2027-06-29" in exported
        and "DWH-laadspecificatie v4" in exported
        and "Afnemersgevolg" in exported,
        "Lineage: export carries values, states, transforms and impact per sample",
    )
    page.locator("#reset").click()
    ensure(
        hop("h5").locator(".state").inner_text()
        == "Onverklaard verschil: verwacht 2027-03-31, getoond 2027-03-30"
        and page.locator('[data-action="load"]').is_enabled(),
        "Lineage: reset restores the starting state",
    )


def test_release_impact__inbox_cells_and_drawer(page: Page) -> None:
    """Vergelijking met de inrichting bepaalt het vak; gewijzigde notes maken beoordelingen ongeldig."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async text => {window.copiedText = text;}}})"
    )
    open_file(page, FILES[10])

    def point(n: str):
        """Leesrij van releasepunt n."""
        return page.locator(f'.points li[data-rn="{n}"]')

    ensure(
        page.locator("#tally").inner_text()
        == "7 releasepunten: 2 nog niet vergeleken, 0 inrichting onbekend, "
        "3 met lokaal gevolg waarvan 1 bevestigd, 2 zonder lokaal gevolg.",
        "Release: starting tally counts every class",
    )
    ensure(
        "2 gevolgen niet bevestigd" in page.locator("#open").inner_text(),
        "Release: unconfirmed impacts stay open for the intake",
    )
    for group in ("zorg", "kern", "fab"):
        ensure(
            page.locator(f'.slip[data-rn="RN-01"][data-group="{group}"]').count() == 1,
            f"Release: RN-01 slip present for {group}",
        )
    ensure(
        "Inzage naasten staat uit" in point("RN-03").locator(".state").inner_text(),
        "Release: no-impact point keeps its written rationale",
    )
    ensure(
        "(1)" in page.locator('[data-group-filter="zorg"]').inner_text()
        and "(1)" in page.locator('[data-group-filter="plan"]').inner_text()
        and "(3)" in page.locator('[data-group-filter="fab"]').inner_text()
        and "(0)" in page.locator('[data-group-filter="cadm"]').inner_text(),
        "Release: nameplates count slips per audience",
    )
    page.locator("#detail").locator('[data-action="compare"]').click()
    ensure(
        "Inrichting onbekend: vraag na bij Technisch beheer ECD"
        in page.locator("#detail").locator(".state").inner_text(),
        "Release: unknown local setting asks the named role",
    )
    ensure(
        "1 nog niet vergeleken, 1 inrichting onbekend" in page.locator("#tally").inner_text(),
        "Release: unknown setting is counted separately",
    )
    page.locator("#detail").locator('[data-action="ask"]').click()
    ensure(
        "Lokaal gevolg, door FAB beoordeeld"
        in page.locator("#detail").locator(".state").inner_text()
        and page.locator('.slip[data-rn="RN-05"][data-group="zorg"]').count() == 1,
        "Release: answered inquiry files the point per audience",
    )
    page.locator('.slip[data-rn="RN-07"][data-group="inbox"]').click()
    page.locator("#detail").locator('[data-action="compare"]').click()
    ensure(
        page.locator('.slip[data-rn="RN-07"][data-group="plan"]').count() == 1
        and page.locator('.slip[data-rn="RN-07"][data-group="kern"]').count() == 1,
        "Release: RN-07 gets a slip for planners and key users",
    )
    page.locator("#detail").locator('[data-action="confirm"]').click()
    ensure(
        "bevestigd door Proceseigenaar planning"
        in page.locator("#detail").locator(".state").inner_text(),
        "Release: confirmation is recorded by the named role",
    )
    page.locator('[data-group-filter="plan"]').click()
    ensure(
        "Planningsbericht: teamcode verplicht" in page.locator("#group-view").inner_text()
        and "Weekoverzicht planning" in page.locator("#group-view").inner_text()
        and "Medicatieaftekenlijst" not in page.locator("#group-view").inner_text(),
        "Release: the audience filter lists only that group's points",
    )
    page.locator('[data-action="notes"]').click()
    ensure(
        page.locator("#notes-version").inner_text() == "Releasenotes v1.1 van 2026-10-02",
        "Release: notes simulation updates the version",
    )
    ensure(
        "Releasenotes gewijzigd na beoordeling; opnieuw vergelijken"
        in point("RN-03").locator(".state").inner_text(),
        "Release: changed note text voids the earlier assessment",
    )
    ensure(
        page.locator('.slip[data-rn="RN-08"][data-group="inbox"]').count() == 1
        and page.locator("#tally").inner_text().startswith("8 releasepunten"),
        "Release: RN-08 arrives uncompared and the tally grows",
    )
    page.locator('.slip[data-rn="RN-03"][data-group="inbox"]').click()
    page.locator("#detail").locator('[data-action="compare"]').click()
    ensure(
        "Lokaal gevolg" in page.locator("#detail").locator(".state").inner_text()
        and "Privacyrisico" in page.locator("#detail").inner_text()
        and page.locator('.slip[data-rn="RN-03"][data-group="cadm"]').count() == 1,
        "Release: changed RN-03 gets an impact with a cadm slip",
    )
    page.locator("#copy").click()
    exported = page.locator("#export-text").input_value()
    ensure(
        exported.startswith("Release Impact Explorer / ECD 2026.5 / demo v1 / revisie 2026-10-03")
        and "v1.1" in exported
        and "v1.0, §2.1" in exported
        and "Bevestiging" in exported,
        "Release: export carries notes version, locations, states and confirmation",
    )
    page.locator("#reset").click()
    ensure(
        page.locator("#notes-version").inner_text() == "Releasenotes v1.0 van 2026-09-26"
        and page.locator("#tally").inner_text().startswith("7 releasepunten")
        and "Releasenotes v1.1" not in page.locator("#notes-version").inner_text(),
        "Release: reset restores v1.0 and the starting state",
    )


def test_adoption__layers_signals_and_advice(page: Page) -> None:
    """Een laag ligt pas op gemeten signaal; gebruik zonder beheersing blijft een risico."""
    page.add_init_script(
        "Object.defineProperty(navigator, 'clipboard', {configurable: true, value: {writeText: async text => {window.copiedText = text;}}})"
    )
    open_file(page, FILES[11])

    def wall(dept: str):
        """Muursectie van een afdeling."""
        return page.locator(f'[data-dept="{dept}"]')

    def layer(dept: str, n: str):
        """Laag n van een afdelingsmuur."""
        return wall(dept).locator(f'[data-layer="{n}"]')

    ensure(
        wall("esdoorn").locator(".stand").inner_text() == "Stand: beheerst"
        and wall("hazelaar").locator(".stand").inner_text() == "Stand: bekend"
        and wall("beuk").locator(".stand").inner_text() == "Stand: gebruikt"
        and wall("wilg").locator(".stand").inner_text() == "Stand: nog niets aangetoond",
        "Adoption: stands follow the highest unbroken layer",
    )
    ensure(
        layer("hazelaar", "l2").locator(".state").inner_text()
        == "Gemeten, onder de grens: 25 van 28 (89,3 %), grens 90 %",
        "Adoption: training under the threshold does not lie",
    )
    ensure(
        "Gemeten, haalt de grens: 50 van 56 (89,3 %), grens 85 %"
        in layer("hazelaar", "l3").locator(".state").inner_text()
        and "Ligt, maar draagt niet: Getraind ontbreekt"
        in layer("hazelaar", "l3").locator(".state").inner_text(),
        "Adoption: use above a gap does not carry",
    )
    ensure(
        wall("hazelaar").locator(".signals").inner_text() == "Gebruik zonder aangetoonde training",
        "Adoption: signal names the missing training",
    )
    ensure(
        wall("hazelaar").locator(".advice").inner_text().startswith("Plan praktijkinstructie")
        and wall("beuk").locator(".advice").inner_text().startswith("Laat de kwaliteitsmedewerker")
        and wall("wilg").locator(".advice").inner_text().startswith("Vraag de teamleider"),
        "Adoption: each wall gets its fitting support advice",
    )
    ensure(
        "Niet aangetoond: nog niet in het inwerkprogramma"
        in layer("esdoorn", "l5").locator(".state").inner_text()
        and "Neem de werkinstructie op" in wall("esdoorn").locator(".advice").inner_text(),
        "Adoption: anchoring requires the inwork programme",
    )
    ensure(
        page.locator("#tally").inner_text()
        == "Esdoorn: beheerst. Hazelaar: bekend. Beuk: gebruikt. "
        "Wilg: nog niets aangetoond. 2 afdelingen met gebruik zonder "
        "aangetoonde training of beheersing.",
        "Adoption: tally counts risk signals without a total score",
    )
    wall("hazelaar").locator('[data-action="train"]').click()
    ensure(
        "28 van 28 (100,0 %), grens 90 %" in layer("hazelaar", "l2").locator(".state").inner_text()
        and wall("hazelaar").locator(".stand").inner_text() == "Stand: beheerst"
        and "draagt niet" not in layer("hazelaar", "l3").locator(".state").inner_text()
        and wall("hazelaar").locator('[data-action="train"]').is_disabled()
        and page.locator("#tally")
        .inner_text()
        .endswith("1 afdeling met gebruik zonder aangetoonde training of beheersing."),
        "Adoption: extra training lets the layer lie and the wall carry",
    )
    wall("beuk").locator('[data-action="sample"]').click()
    ensure(
        "Gemeten, onder de grens: 17 van 22 (77,3 %), grens 90 %"
        in layer("beuk", "l4").locator(".state").inner_text()
        and wall("beuk").locator(".stand").inner_text() == "Stand: gebruikt"
        and wall("beuk")
        .locator(".advice")
        .inner_text()
        .startswith("Bespreek de ontbrekende onderdelen"),
        "Adoption: a failing mastery sample keeps the stand at gebruikt",
    )
    wall("wilg").locator('[data-action="sample"]').click()
    ensure(
        "Gemeten, steekproef te klein: 12 van minimaal 20"
        in layer("wilg", "l4").locator(".state").inner_text()
        and wall("wilg").locator(".advice").inner_text().startswith("Vraag de teamleider"),
        "Adoption: too-small sample stays short of evidence",
    )
    wall("wilg").locator('[data-action="train"]').click()
    ensure(
        "25 van 30 (83,3 %)" in layer("wilg", "l2").locator(".state").inner_text(),
        "Adoption: first training round stays under the threshold",
    )
    wall("wilg").locator('[data-action="train"]').click()
    ensure(
        "28 van 30 (93,3 %)" in layer("wilg", "l2").locator(".state").inner_text(),
        "Adoption: second training round reaches the threshold",
    )
    wall("esdoorn").locator('[data-action="embed"]').click()
    ensure(
        wall("esdoorn").locator(".stand").inner_text() == "Stand: geborgd"
        and wall("esdoorn").locator(".advice").inner_text().startswith("Borging aangetoond"),
        "Adoption: embedding in the inwork programme completes the wall",
    )
    page.locator('[data-action="instr-change"]').click()
    ensure(
        all(
            "teamleider bevestigt opnieuw" in layer(dept, "l1").locator(".state").inner_text()
            and "Niet gemeten" in layer(dept, "l1").locator(".state").inner_text()
            for dept in ("esdoorn", "hazelaar", "beuk", "wilg")
        ),
        "Adoption: a changed instruction unmeasures every Bekend layer",
    )
    ensure(
        wall("esdoorn").locator(".stand").inner_text() == "Stand: nog niets aangetoond"
        and "Ligt, maar draagt niet: Bekend ontbreekt"
        in layer("esdoorn", "l2").locator(".state").inner_text()
        and "Niet aangetoond: werkinstructie gewijzigd, nog niet vastgesteld"
        in layer("esdoorn", "l5").locator(".state").inner_text()
        and wall("esdoorn").locator(".advice").inner_text().startswith("Vraag de teamleider"),
        "Adoption: changed instruction breaks the base and the anchoring",
    )
    wall("esdoorn").locator('[data-action="confirm"]').click()
    ensure(
        wall("esdoorn").locator(".stand").inner_text() == "Stand: beheerst"
        and "Laat de gewijzigde werkinstructie vaststellen"
        in wall("esdoorn").locator(".advice").inner_text(),
        "Adoption: reconfirmed uitleg restores the stand, not the anchoring",
    )
    page.locator('[data-action="instr-adopt"]').click()
    ensure(
        wall("esdoorn").locator(".stand").inner_text() == "Stand: geborgd",
        "Adoption: establishing v2 completes the anchored wall",
    )
    page.locator("#copy").click()
    exported = page.locator("#export-text").input_value()
    ensure(
        exported.startswith("Adoptiekaart / ADOPT-DEMO-04 / demo v1 / revisie 2026-10-03")
        and "grens 90 %" in exported
        and "werkinstructie" in exported.lower()
        and "Advies" in exported,
        "Adoption: export carries layers, instruction version, stands and advice",
    )
    page.locator("#reset").click()
    ensure(
        wall("hazelaar").locator(".stand").inner_text() == "Stand: bekend"
        and "2 afdelingen" in page.locator("#tally").inner_text(),
        "Adoption: reset restores the starting state",
    )
