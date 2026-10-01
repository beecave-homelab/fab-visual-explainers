"""Bewijsfasen, herstelvoorwaarden en overlap in drie zelfstandige taakviews."""

from playwright.sync_api import Page
from support import visual_path

FILES = ["fab-test-coverage-map.html", "fab-continuiteitskaart.html", "fab-data-quality-map.html"]


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
