"""Gemeenschappelijke controles voor alle aanwezige zelfstandige HTML-prototypes."""

import re
from collections.abc import Callable
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import pytest
from playwright.sync_api import BrowserContext, Page, expect
from support import HTML_FILES, TASK_FILES, visual_path


class Document(HTMLParser):
    """Verzamel statische IDs en lokale links zonder HTML uit te voeren."""

    def __init__(self, path: Path) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.links: list[str] = []
        self.feed(path.read_text())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])


@pytest.mark.parametrize("filename", HTML_FILES)
def test_html__local_links_and_static_ids(filename: str) -> None:
    """Iedere lokale link bestaat en statische HTML-fragmenten zijn uniek."""
    path = visual_path(filename)
    document = Document(path)
    assert len(document.ids) == len(set(document.ids)), f"Dubbele statische IDs: {filename}"
    for href in document.links:
        url = urlsplit(href)
        if url.scheme or url.netloc:
            continue
        target = path.parent / unquote(url.path) if url.path else path
        assert target.is_file(), f"{filename}: ontbrekend doel {href}"
        if url.fragment and target.suffix == ".html":
            assert unquote(url.fragment) in Document(target).ids, (
                f"{filename}: ontbrekend fragment {href}"
            )


@pytest.mark.parametrize("filename", HTML_FILES)
def test_html__mobile_ids_and_management_context(page: Page, filename: str) -> None:
    """Initialisatie, beheergegevens en mobiele breedte werken voor iedere pagina."""
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    assert page.evaluate("""() => {
        const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
        return ids.length === new Set(ids).size;
    }"""), f"Dubbele dynamische IDs: {filename}"
    if filename not in TASK_FILES:
        card = page.locator(".review-context")
        expect(card).to_have_count(1)
        expect(card).to_contain_text(re.compile(r"\d{4}-\d{2}-\d{2}"))
    else:
        expect(
            page.locator("details").filter(
                has=page.locator("summary", has_text=re.compile(r"^Taak,"))
            )
        ).to_have_count(1)
    for width in (320, 390):
        page.set_viewport_size({"width": width, "height": 844})
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 2"), (
            f"{filename}: overflow bij {width}px"
        )


@pytest.mark.parametrize(
    ("filename", "selector"),
    [
        ("fab-releaseatelier.html", "#test-coverage"),
        ("incident-onepager.html", "#continuity"),
        ("incident-onepager-attent.html", "#continuity"),
        ("fab-ketenkaart.html", "#data-quality"),
        ("fab-beheerbaarheid-scan.html", "#scanChecklist"),
    ],
)
def test_critical_content__without_javascript(
    new_context: Callable[..., BrowserContext], filename: str, selector: str
) -> None:
    """Kritieke taakinhoud is leesbaar zonder JavaScript en in afdrukmodus."""
    page = new_context(java_script_enabled=False, viewport={"width": 390, "height": 844}).new_page()
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    expect(page.locator(selector)).to_be_visible()
    page.emulate_media(media="print")
    expect(page.locator(selector)).to_be_visible()


@pytest.mark.parametrize("filename", TASK_FILES)
def test_task_views__print_and_nojs(
    new_context: Callable[..., BrowserContext], filename: str, artifact: Callable[[str], str]
) -> None:
    """Afdruk en statische alternatieven houden alle scenario’s en voorwaarden bereikbaar."""
    for javascript in (True, False):
        page = new_context(
            java_script_enabled=javascript, viewport={"width": 320, "height": 900}
        ).new_page()
        page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
        expect(page.locator("h1")).to_be_visible()
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), filename
        if not javascript:
            expect(page.locator("#copy")).to_be_hidden()
        if filename == TASK_FILES[0]:
            expect(page.locator(".register article")).to_have_count(5)
            expect(page.locator(".register article").last).to_contain_text("noodplan")
        elif filename == TASK_FILES[1]:
            expect(page.locator(".readable ol li")).to_have_count(3)
            expect(page.locator(".checks")).to_be_visible()
        else:
            expect(page.locator(".register article")).to_have_count(3)
            if not javascript:
                expect(page.locator("#lens-caption")).to_contain_text("overlappen")
        page.emulate_media(media="print")
        expect(page.locator("#copy")).to_be_hidden()
        expect(page.locator("[data-action]:visible")).to_have_count(0)
        assert page.locator("details").evaluate_all("""nodes => nodes.every(node =>
            [...node.children].filter(child => child.tagName !== 'SUMMARY')
                .every(child => getComputedStyle(child).display !== 'none'))""")
        if javascript:
            page.pdf(
                path=artifact(filename.removesuffix(".html") + ".pdf"),
                format="A4",
                print_background=True,
            )


@pytest.mark.parametrize("filename", TASK_FILES)
@pytest.mark.parametrize("denied", [False, True], ids=["copy-success", "copy-denied"])
def test_task_views__clipboard_and_keyboard(page: Page, filename: str, denied: bool) -> None:
    """Export komt overeen met het scherm; weigering geeft een bereikbare kopieerfallback."""
    action = "throw new Error('Test denial')" if denied else "window.copiedText = text"
    page.add_init_script(
        f"Object.defineProperty(navigator, 'clipboard', {{value: {{writeText: async text => {{{action}}}}}}})"
    )
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    page.keyboard.press("Tab")
    expect(page.locator(".skip")).to_be_focused()
    page.keyboard.press("Enter")
    page.keyboard.press("Tab")
    assert page.evaluate("['SELECT', 'BUTTON', 'INPUT'].includes(document.activeElement.tagName)")
    page.locator("#copy").click()
    expect(page.locator("#export")).to_be_visible()
    text = page.locator("#export-text").input_value()
    assert len(text) > 800, "Export ontbreekt of is onvolledig"
    if denied:
        expect(page.locator("#export-text")).to_be_focused()
        expect(page.locator("#message")).to_contain_text("Kopiëren niet beschikbaar")
    else:
        expect(page.locator("#message")).to_contain_text("gekopieerd")
        assert page.evaluate("window.copiedText") == text
