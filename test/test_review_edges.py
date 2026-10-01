"""Grensgevallen voor drempels, afkeuring, toetsenbord en kopieerfallbacks."""

from collections.abc import Callable

from playwright.sync_api import BrowserContext, Page
from support import ROOT


def test_go_no_go_cockpit__rejection_keyboard_and_fallback(
    page: Page, artifact: Callable[[str], str], new_context: Callable[..., BrowserContext]
) -> None:
    """Afkeuring of onbekend bewijs kan niet via de bediening worden omzeild."""
    page.goto((ROOT / "fab-go-no-go-cockpit.html").as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate("""() => {
      for(const b of document.querySelectorAll('[data-crit]')) {
        b.click(); const f=document.querySelector('#criterionEvidence');
        for(const [k,v] of Object.entries({stage:'geaccepteerd',source:'TEST-synthetisch',version:'test v1',date:'2026-10-26',reviewer:'Fictieve bevoegde testrol',outcome:'akkoord'})) f.elements[k].value=v;
        document.querySelector('[data-setstatus="gereed"]').click();
      }
      const f=document.querySelector('[data-finding="B-3"]');f.elements.priority.value=2;f.requestSubmit();
    }""")
    assert page.locator("#advText").inner_text() == "No-go"
    assert "boven de grens" in page.locator("#advWhy").inner_text()
    assert "zonder beoordeelde workaround" in page.locator("#advWhy").inner_text()
    page.locator('[data-crit="f1"]').click()
    page.locator('#criterionEvidence [name="outcome"]').select_option("afgekeurd")
    page.locator('[data-setstatus="vw"]').click()
    assert page.locator("#advText").inner_text() == "No-go"
    assert "blocker" in page.locator("#advWhy").inner_text()
    assert page.locator('[data-crit="f1"]').get_attribute("data-status") == "blocker"
    assert page.locator("#selectionKind").inner_text() == "Functioneel · Blocker"
    assert page.locator('#criterionEvidence [name="stage"]').input_value() == "gecontroleerd"
    page.locator("#tab-crit").focus()
    page.keyboard.press("ArrowRight")
    assert page.locator("#tab-bewijs").get_attribute("aria-selected") == "true"
    page.locator("#tab-crit").click()
    page.locator("#inspector").screenshot(path=artifact("fab-go-no-go-review.png"))
    page.evaluate(
        "Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw new Error('test denied')}}})"
    )
    page.locator("#copyButton").click()
    assert page.locator("#copyFallback").is_visible()
    assert "No-go" in page.locator("#copyFallback").input_value()


def test_decision_canvas__rejection_keyboard_and_fallback(
    page: Page, artifact: Callable[[str], str], new_context: Callable[..., BrowserContext]
) -> None:
    """Afkeuring of onbekend bewijs kan niet via de bediening worden omzeild."""
    page.goto((ROOT / "fab-decision-canvas.html").as_uri())
    page.wait_for_load_state("networkidle")
    page.locator("#gateEditor").screenshot(path=artifact("fab-decision-review.png"))
    page.evaluate(
        "Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw new Error('test denied')}}})"
    )
    page.locator("#copyButton").click()
    assert "Geen optie is toelaatbaar" in page.locator("#copyFallback").input_value()
    page.locator("#tab-ond").focus()
    page.keyboard.press("End")
    assert page.locator("#tab-bron").get_attribute("aria-selected") == "true"
    nojs = new_context(java_script_enabled=False).new_page()
    nojs.goto((ROOT / "fab-decision-canvas.html").as_uri(), wait_until="networkidle")
    assert nojs.locator("#summaryTitle").inner_text() == "Geen optie toelaatbaar"
    nojs.close()


def test_oorzaakopsporing__rejection_keyboard_and_fallback(
    page: Page, artifact: Callable[[str], str], new_context: Callable[..., BrowserContext]
) -> None:
    """Afkeuring of onbekend bewijs kan niet via de bediening worden omzeild."""
    page.goto((ROOT / "fab-oorzaakopsporing.html").as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate(
        "Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw new Error('test denied')}}})"
    )
    page.locator("#copy").click()
    assert page.locator("#manualCopy").is_visible()
    assert "Geen automatische uitsluitingen" in page.locator("#manualCopy").input_value()
    for cid in ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]:
        page.locator(f'[data-c="{cid}"][data-a="u"]').click()
    assert "Alle checks bekeken" in page.locator("#verdict").inner_text()
    assert page.locator("th.h.out").count() == 0
    page.locator("#undo").click()
    assert "Volgende check" in page.locator("#verdict").inner_text()
