"""Ketenroutes, veilige export, toegankelijkheid en statische alternatieven."""

import json
import re
from collections.abc import Callable

from playwright.sync_api import BrowserContext, Page, expect
from support import ROOT

URL = (ROOT / "fab-ketenkaart.html").as_uri()


def test_ketenkaart__routes_keyboard_and_copy_fallback(
    page: Page, artifact: Callable[[str], str]
) -> None:
    """Routes en verstoringen geven de juiste controle; toetsenbord en fallback werken."""
    page.goto(URL, wait_until="networkidle")
    expect(page.locator("[data-node]")).to_have_count(6)
    expect(page.locator("[data-edge]")).to_have_count(5)
    expect(page.locator("#summaryTitle")).to_have_text("Bericht verwerkt")
    page.screenshot(path=artifact("fab-ketenkaart-desktop.png"), full_page=True)
    for node, title in {
        "ecd": "Cliëntdossier",
        "receive": "Ontvangst",
        "check": "Controle & vertaling",
        "finance": "Financieel",
        "dwh": "Datawarehouse",
        "bi": "BI-rapportage",
    }.items():
        page.locator(f'[data-node="{node}"]').click()
        expect(page.locator("#selectionTitle")).to_have_text(title)
        expect(page.locator(f'[data-node="{node}"]')).to_have_attribute("aria-pressed", "true")
        expect(page.locator("#selectionOwner")).not_to_be_empty()
    for edge in ["send", "validate", "book", "load", "report"]:
        page.locator(f'[data-edge="{edge}"]').click()
        expect(page.locator("#selectionKind")).to_have_text("Overdracht")
        expect(page.locator(f'[data-edge="{edge}"]')).to_have_attribute("aria-pressed", "true")
        page.locator("#tab-care").click()
        expect(page.locator("#panel-care")).to_be_visible()
        page.locator("#tab-proof").click()
        expect(page.locator("#panel-proof")).to_contain_text("Fictief bewijsfragment")
    page.locator("#resetButton").click()
    page.locator("#routeSelect").select_option("finance")
    expect(page.locator('[data-node="bi"]')).to_have_class("node dim")
    page.locator('[data-node="bi"]').click()
    expect(page.locator("#routeSelect")).to_have_value("all")
    page.locator("#routeSelect").select_option("finance")
    expect(page.locator("#selectionTitle")).to_have_text("Eén mutatie, twee afnemers")
    page.locator('[data-scenario="failure"]').click()
    expect(page.locator("#summaryTitle")).to_have_text("Ontvangen, niet verwerkt")
    page.locator('[data-node="check"]').click()
    expect(page.locator("#panel-data")).to_contain_text("ZT-099")
    expect(page.locator(".diagram-desktop .wire.blocked")).to_have_count(3)
    page.locator("#tab-proof").click()
    expect(page.locator("#panel-proof")).to_contain_text("UNKNOWN_TEAM")
    page.screenshot(path=artifact("fab-ketenkaart-failure.png"), full_page=True)
    for node in ["ecd", "receive", "check", "finance", "dwh", "bi"]:
        page.locator(f'[data-node="{node}"]').click()
        expect(page.locator("#panel-proof")).to_contain_text("Fictief bewijsfragment")
    page.locator("#tab-data").focus()
    page.keyboard.press("ArrowRight")
    expect(page.locator("#tab-care")).to_be_focused()
    page.keyboard.press("End")
    expect(page.locator("#tab-proof")).to_be_focused()
    page.keyboard.press("Home")
    expect(page.locator("#tab-data")).to_be_focused()
    page.evaluate(
        'Object.defineProperty(navigator, "clipboard", {value: undefined, configurable: true})'
    )
    page.locator("#copyButton").click()
    expect(page.locator("#copyFallback")).to_be_visible()
    expect(page.locator("#copyFallback")).to_have_value(
        re.compile(".*Onbekend team ZT-099.*", re.S)
    )
    page.locator("#resetButton").click()
    expect(page.locator("#copyFallback")).to_be_hidden()
    expect(page.locator("#tab-data")).to_have_attribute("aria-selected", "true")
    expect(page.locator("#routeSelect")).to_have_value("all")
    expect(page.locator("#summaryTitle")).to_have_text("Bericht verwerkt")
    page.locator('[data-node="ecd"]').focus()
    page.keyboard.press("Enter")
    expect(page.locator("#selectionTitle")).to_have_text("Cliëntdossier")
    assert (
        page.locator('[data-node="ecd"]').evaluate("(el) => getComputedStyle(el).outlineStyle")
        != "none"
    )


def test_ketenkaart__viewport_print_and_nojs(
    page: Page, artifact: Callable[[str], str], new_context: Callable[..., BrowserContext]
) -> None:
    """Ketenknoppen passen op de ondersteunde breedtes en blijven leesbaar op papier."""
    page.goto(URL, wait_until="networkidle")
    for width in [320, 375, 390, 600, 760, 768, 900, 1024, 1180, 1181, 1200, 1280, 1440, 1920]:
        page.set_viewport_size({"width": width, "height": 1000})
        page.locator("#resetButton").click()
        overflow = page.evaluate("document.documentElement.scrollWidth > innerWidth")
        assert not overflow, f"Page overflow at {width}"
        measurements = page.locator(".node").evaluate_all(
            "els => els.map(el => ({name: el.innerText, w: el.clientWidth, sw: el.scrollWidth, h: el.clientHeight, sh: el.scrollHeight}))"
        )
        bad = [m for m in measurements if m["sw"] > m["w"] + 1 or m["sh"] > m["h"] + 1]
        assert not bad, f"Node overflow at {width}: {json.dumps(bad)}"
        if width == 390:
            page.screenshot(path=artifact("fab-ketenkaart-mobile.png"), full_page=True)
            page.locator('[data-edge="load"]').click()
            expect(page.locator("#selectionTitle")).to_have_text("Teamtoewijzing laden")
            expect(page.locator("#selectionJump")).to_be_visible()
            page.locator("#selectionJump").click()
            expect(page.locator("#inspector")).to_be_focused()
            page.screenshot(path=artifact("fab-ketenkaart-mobile-selection.png"), full_page=True)
            page.locator('[data-scenario="failure"]').click()
            expect(page.locator("#summaryTitle")).to_have_text("Ontvangen, niet verwerkt")
    page.set_viewport_size({"width": 1440, "height": 1080})
    page.locator("#resetButton").click()
    page.emulate_media(media="print", reduced_motion="reduce")
    expect(page.locator(".toolbar")).to_be_hidden()
    expect(page.locator(".diagram-desktop")).to_be_visible()
    page.screenshot(path=artifact("fab-ketenkaart-print.png"), full_page=True)
    page.pdf(
        path=artifact("fab-ketenkaart-print.pdf"), prefer_css_page_size=True, print_background=True
    )
    page.emulate_media(media="screen")
    page.locator("#resetButton").click()
    nojs = new_context(java_script_enabled=False, viewport={"width": 390, "height": 844})
    static = nojs.new_page()
    static.goto(URL, wait_until="networkidle")
    expect(static.locator(".nojs")).to_be_visible()
    expect(static.locator(".diagram-mobile")).to_be_visible()
    expect(static.locator('[data-node="ecd"]')).to_be_disabled()
    expect(static.locator("#panel-data")).to_contain_text("Wat verandert")
    assert not static.evaluate("document.documentElement.scrollWidth > innerWidth")


def test_ketenkaart__accessible_svg_and_stale_clipboard(
    page: Page, artifact: Callable[[str], str]
) -> None:
    """SVG heeft labels en een vertraagde kopieeractie mag resetstatus niet overschrijven."""
    requests = []
    page.on("request", lambda request: requests.append(request.url))
    page.goto(URL, wait_until="networkidle")
    assert page.evaluate("""() => {
        const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
        return ids.length === new Set(ids).size;
    }""")
    assert page.evaluate("""() => [...document.querySelectorAll('svg[role="img"]')].every(svg =>
        svg.firstElementChild.tagName.toLowerCase() === 'title' &&
        svg.getAttribute('aria-labelledby').split(' ').every(id => document.getElementById(id)?.textContent.length > 0))""")
    page.evaluate(
        'Object.defineProperty(navigator, "clipboard", {value: {writeText: async text => {window.copied = text}}, configurable: true})'
    )
    page.locator('[data-node="finance"]').click()
    expect(page.locator("#panel-data")).to_contain_text("costCenter")
    page.locator("#copyButton").click()
    expect(page.locator("#copyStatus")).to_have_text("Ketensamenvatting gekopieerd.")
    assert "FAB Bedrijfsvoering" in page.evaluate("window.copied")
    page.evaluate(
        'Object.defineProperty(navigator, "clipboard", {value: {writeText: () => new Promise(resolve => {window.finishCopy = resolve})}, configurable: true})'
    )
    page.locator("#copyButton").click()
    page.locator("#resetButton").click()
    page.evaluate("window.finishCopy()")
    expect(page.locator("#copyStatus")).to_be_empty()
    assert all(url.startswith(ROOT.as_uri() + "/") for url in requests), requests
    page.set_viewport_size({"width": 320, "height": 740})
    page.locator('[data-scenario="failure"]').click()
    for node in ["ecd", "receive", "check", "finance", "dwh", "bi"]:
        item = page.locator(f'[data-node="{node}"]')
        item.click()
        assert item.evaluate(
            "(el) => el.scrollHeight <= el.clientHeight + 1 && el.scrollWidth <= el.clientWidth + 1"
        ), node
