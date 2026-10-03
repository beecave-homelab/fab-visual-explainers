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
