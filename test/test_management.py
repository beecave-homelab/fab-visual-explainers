"""Beheeracceptatie vraagt gecontroleerd bewijs en vervalt na wijziging."""

from playwright.sync_api import Page
from support import open_page


def test_management__changed_evidence_revokes_acceptance(page: Page) -> None:
    """Bronlabels zijn geen bewijs; akkoord vervalt na bronwijziging."""
    open_page(page, "beheerbaarheid-scan")
    assert page.locator("#evidenceCount").inner_text() == "0", (
        "Een bronlabel is geen beoordeeld bewijs"
    )
    assert page.locator("#unknownCount").inner_text() == "8"
    page.locator('[data-state="ready"]').click()
    assert page.locator("#readyCount").inner_text() == "0"
    form = page.locator("#checkAssessment")
    for name, value in {
        "source": "Synthetisch TEST-register",
        "version": "test v1",
        "date": "2026-10-01",
        "reviewer": "Fictieve proceseigenaar",
    }.items():
        form.locator(f'[name="{name}"]').fill(value)
    form.locator('[name="stage"]').select_option("geaccepteerd")
    form.locator('[name="outcome"]').select_option("akkoord")
    page.locator('[data-state="ready"]').click()
    assert page.locator("#readyCount").inner_text() == "1"
    assert page.locator("#evidenceCount").inner_text() == "1"
    form.locator('[name="source"]').fill("<img src=x onerror=alert(1)>")
    assert page.locator("#readyCount").inner_text() == "0"
    assert page.locator("img").count() == 0
    form.locator('[name="outcome"]').select_option("afgekeurd")
    page.locator('[data-state="ready"]').click()
    assert page.locator("#domainStatus").inner_text() == "Blocker"
    page.evaluate(
        "Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw new Error('test denied')}}})"
    )
    page.locator("#copyBtn").click()
    assert page.locator("#copyFallback").is_visible()
    assert "beoordelaar" in page.locator("#copyFallback").input_value()
    page.locator("#resetBtn").click()
    assert page.locator("#copyFallback").is_hidden()
    assert page.locator("#evidenceCount").inner_text() == "0"
    page.locator('#ring [data-id="test"]').focus()
    page.keyboard.press("Enter")
    assert page.locator("#domainTitle").inner_text() == "Testen"
    page.locator('[data-state="unknown"]').focus()
    page.keyboard.press("Space")
    assert page.locator("#domainStatus").inner_text() == "Niet getoetst"
