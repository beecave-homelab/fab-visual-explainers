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
