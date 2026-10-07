"""Volledige bronalternatieven, navigatie, focus en betrouwbare kopieerfallbacks."""

from collections.abc import Callable

import pytest
from playwright.sync_api import BrowserContext, Page, expect
from support import HTML_FILES, visual_path

SOURCE_FILES = (
    "bron-scanner.html",
    "bronkaart-onepager.html",
    "kennisatlas.html",
    "vraagdossier.html",
    "vraagkompas.html",
)


@pytest.mark.parametrize("filename", SOURCE_FILES)
@pytest.mark.parametrize("javascript", [True, False], ids=["interactive", "nojs"])
def test_sources__complete_readable_print_route(
    new_context: Callable[..., BrowserContext], filename: str, javascript: bool
) -> None:
    """Elke bronsectie blijft bereikbaar op mobiel en bij afdruk, ook na filteren."""
    page = new_context(java_script_enabled=javascript).new_page()
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    register = page.locator("#source-register")
    if javascript:
        register.locator("summary").click()
    expect(register.locator("article").first).to_be_visible()
    expect(register.locator("article").last).to_be_visible()
    expect(register).to_contain_text("bronhouder onbekend")
    for width in (320, 390):
        page.set_viewport_size({"width": width, "height": 844})
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 2")
    # Close the register before printing: default browser details rendering hid its contents.
    register.locator("summary").click()
    expect(register.locator("article").last).to_be_hidden()
    page.emulate_media(media="print")
    for article in register.locator("article").all():
        expect(article).to_be_visible()
        assert article.bounding_box()["height"] > 20
    expect(page.locator("h1:visible")).to_have_count(0)


@pytest.mark.parametrize("filename", HTML_FILES)
def test_print__collapsed_readable_details_are_visible(page: Page, filename: str) -> None:
    """Controleer werkelijke zichtbaarheid van checklists en beheercontext in Chrome."""
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    page.locator("details").evaluate_all("nodes => nodes.forEach(node => node.open = false)")
    page.emulate_media(media="print")
    if filename == "fab-decision-canvas.html":
        expect(page.locator("#gateEditor form:visible")).to_have_count(0)
    for element in page.locator(
        ".review-context details > :is(p, ol, ul, table), "
        "#source-register > :is(p, ol, ul, table, article)"
    ).all():
        if element.text_content().strip():
            expect(element).to_be_visible()
            assert element.bounding_box()["height"] > 0


def test_scanner__filtered_navigation_empty_results_and_context(page: Page) -> None:
    """Zoeken, knoppen en pijltjes gebruiken dezelfde resultaten met focusbehoud."""
    page.goto(visual_path("bron-scanner.html").as_uri(), wait_until="networkidle")
    page.locator("#search").fill("bron")
    strips = page.locator(".strip:visible")
    indices = [strip.get_attribute("data-index") for strip in strips.all()]
    assert len(indices) > 1
    strips.first.click()
    for index in indices[1:]:
        page.locator("#next").click()
        expect(page.locator(f'.strip[data-index="{index}"]')).to_have_attribute(
            "aria-current", "true"
        )
    expect(page.locator("#next")).to_be_disabled()
    strips.last.focus()
    page.keyboard.press("ArrowLeft")
    expect(page.locator(f'.strip[data-index="{indices[-2]}"]')).to_be_focused()
    expect(page.locator(f'.strip[data-index="{indices[-2]}"]')).to_have_attribute(
        "aria-current", "true"
    )
    page.locator("#search").fill("geen-bestaande-sectie")
    expect(page.locator("#search-status")).to_contain_text("Geen secties")
    expect(page.locator(".focus")).to_be_hidden()
    page.locator("#search").fill("")
    expect(page.locator(".focus")).to_be_visible()
    expect(page.locator("#search")).to_be_focused()
    target = page.locator("#evidence a").first.get_attribute("href")
    page.locator("#evidence a").first.click()
    expect(page.locator(target)).to_be_visible()
    assert page.url.endswith(target)


def test_dossier__evidence_keyboard_return_and_selection(page: Page) -> None:
    """Bewijs is met toetsenbord te openen en te sluiten zonder verloren focus."""
    page.goto(visual_path("vraagdossier.html").as_uri(), wait_until="networkidle")
    opener = page.locator("#evidenceList button").first
    opener.focus()
    page.keyboard.press("Enter")
    expect(page.locator("#closeEvidence")).to_be_focused()
    page.keyboard.press("Escape")
    expect(opener).to_be_focused()
    expect(page.locator("#evidencePopover")).to_be_hidden()
    opener.click()
    page.locator("#closeEvidence").click()
    expect(opener).to_be_focused()
    page.locator('[data-question="uncertainty"]').click()
    expect(page.locator('[data-question="uncertainty"]')).to_have_attribute("aria-pressed", "true")
    page.locator('[data-depth="source"]').click()
    expect(page.locator('[data-depth="source"]')).to_have_attribute("aria-pressed", "true")


def test_knowledge__selection_routes_and_related_focus(page: Page) -> None:
    """Selectiestatus volgt de inhoud en een vervangen vervolgknop verliest geen focus."""
    page.goto(visual_path("kennisatlas.html").as_uri(), wait_until="networkidle")
    expect(page.locator("#atlasEvidence li")).not_to_have_count(0)
    assert (
        page.locator("#source-relations li").all_text_contents()
        == page.locator(".atlas-relations li").all_text_contents()
    )
    page.locator('.map-chip[data-route="risk"]').click()
    expect(page.locator("#atlasStats")).to_contain_text("gedimd")
    expect(page.locator('.map-chip[data-route="risk"]')).to_have_attribute("aria-pressed", "true")
    page.locator('[data-node="quality"]').click()
    expect(page.locator('[data-node="quality"]')).to_have_attribute("aria-pressed", "true")
    page.goto(visual_path("vraagkompas.html").as_uri(), wait_until="networkidle")
    page.locator('#related button[data-id="what"]').click()
    expect(page.locator('.q[data-id="what"]')).to_be_focused()
    page.keyboard.press("ArrowDown")
    expect(page.locator('.q[data-id="evidence"]')).to_be_focused()
    expect(page.locator('.q[data-id="evidence"]')).to_have_attribute("aria-pressed", "true")


@pytest.mark.parametrize(
    "filename", ["fab-rapportage-lineage.html", "fab-joiner-mover-leaver.html"]
)
@pytest.mark.parametrize("denied", [True, False], ids=["denied", "unavailable"])
def test_legacy_exports__denial_retains_complete_text(
    page: Page, filename: str, denied: bool
) -> None:
    """Clipboardweigering laat selecteerbare tekst staan, zonder vals succesbericht."""
    clipboard = "{writeText:async()=>{throw new Error('denied')}}" if denied else "undefined"
    page.add_init_script(
        "Object.defineProperty(navigator,'clipboard',{value:" + clipboard + "});"
        "document.execCommand = () => false;"
    )
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    page.locator("#copy").click()
    expect(page.locator("#manualCopy")).to_be_visible()
    expect(page.locator("#manualCopy")).to_be_focused()
    expect(page.locator("#status")).to_contain_text("handmatig")
    text = page.locator("#manualCopy").input_value()
    assert "demo v2" in text
    assert len(text) > 600
    page.locator("#copy").click()
    expect(page.locator("#manualCopy")).to_have_count(1)
    assert page.locator("#manualCopy").input_value().splitlines()[0] == text.splitlines()[0]


@pytest.mark.parametrize(
    ("filename", "marker", "mutation", "selector"),
    [
        (
            "bron-scanner.html",
            '  const app = document.getElementById("app");',
            "data[0].title=payload;data[0].takeaways=[payload];data[0].proofs=[[payload,payload]];",
            "#takeaways",
        ),
        (
            "bronkaart-onepager.html",
            "    const scanList = document.getElementById('scanList');",
            "topics[1].label=payload;topics[1].bullets=[payload];topics[1].fragment=payload;",
            "#detailList",
        ),
        (
            "kennisatlas.html",
            "  const atlasNodes = [...document.querySelectorAll('.atlas-node')];",
            "atlasData.adoption.evidence=[payload];",
            "#atlasEvidence",
        ),
        (
            "vraagkompas.html",
            '  const order=["why","what","evidence","risk","action","who"];',
            "items.why.short=payload;items.why.refs=[[payload,payload]];",
            "#response",
        ),
    ],
)
def test_sources__source_text_is_rendered_as_text(
    page: Page, filename: str, marker: str, mutation: str, selector: str
) -> None:
    """Brontekst met HTML-tekens mag geen element of eventhandler in de visual worden."""
    import json

    payload = '<img data-injected="yes" src="x" onerror="window.injected=true"> & bron'
    source = visual_path(filename).read_text()
    assert marker in source
    source = source.replace(
        marker, "const payload=" + json.dumps(payload) + ";" + mutation + marker, 1
    )
    page.route(
        visual_path(filename).as_uri(),
        lambda route: route.fulfill(body=source, content_type="text/html"),
    )
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    expect(page.locator(selector)).to_contain_text(payload)
    expect(page.locator("[data-injected]")).to_have_count(0)
    assert page.evaluate("window.injected !== true")


@pytest.mark.parametrize(
    ("filename", "navigation", "title", "content"),
    [
        (
            "bron-scanner.html",
            ".strip",
            "#title",
            "#summary, #takeaways li, #quote, #why, #caution, #related, #evidence b, #evidence p",
        ),
        (
            "bronkaart-onepager.html",
            ".scan-item",
            "#detailTitle",
            "#detailSummary, #detailList li",
        ),
        (
            "kennisatlas.html",
            ".atlas-node",
            "#atlasTitle",
            "#atlasSummary, #atlasWhy, #atlasEvidence li, #atlasSource",
        ),
        (
            "vraagdossier.html",
            ".question-button",
            "#briefTitle",
            "#briefDeck, #briefBody p, #sourceTrail, #evidenceList .tag, #evidenceList p",
        ),
        (
            "vraagkompas.html",
            ".q",
            "#questionTitle",
            "#response .big, #sources b, #sources p",
        ),
    ],
)
def test_sources__readable_route_matches_each_interactive_selection(
    page: Page, filename: str, navigation: str, title: str, content: str
) -> None:
    """Voorkom dat een bronwijziging alleen de interactieve of alleen de leeslaag bereikt."""
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    choices = page.locator(navigation)
    register = page.locator("#source-register article[data-source-key]")
    expect(register).to_have_count(choices.count())
    for choice in choices.all():
        choice.click()
        heading = page.locator(title).inner_text()
        article = register.filter(
            has=page.get_by_role("heading", name=heading, exact=True, include_hidden=True)
        )
        expect(article).to_have_count(1)
        static_text = article.text_content()
        for value in page.locator(content).all_text_contents():
            assert value.strip() in static_text, f"{filename}, {heading}: ontbreekt {value!r}"


def test_dossier__all_depths_and_evidence_follow_register(page: Page) -> None:
    """Iedere vraag, leesdiepte en bewijsdetail leest dezelfde statische broninhoud."""
    page.goto(visual_path("vraagdossier.html").as_uri(), wait_until="networkidle")
    for article in page.locator("#source-register article[data-source-key]").all():
        key = article.get_attribute("data-source-key")
        question = page.locator(f'[data-question="{key}"]')
        question.click()
        expect(question).to_be_focused()
        expect(question.locator("span")).to_have_text(
            article.locator('[data-field="question"]').text_content()
        )
        for depth, body_field in (("short", "medium"), ("medium", "source"), ("source", None)):
            button = page.locator(f'[data-depth="{depth}"]')
            button.click()
            expect(button).to_be_focused()
            expect(button).to_have_attribute("aria-pressed", "true")
            expect(page.locator("#evidencePopover")).to_be_hidden()
            expect(page.locator("#briefDeck")).to_have_text(
                article.locator(f'[data-field="{depth}"]').text_content()
            )
            if body_field:
                expect(page.locator("#briefBody > p")).to_have_text(
                    article.locator(f'[data-field="{body_field}"]').text_content()
                )
            else:
                expect(page.locator("#briefBody > p")).to_contain_text("Bronlaag actief")
            for field, selector in (
                ("title", "#briefTitle"),
                ("question", "#briefQuestion"),
                ("takeaway", "#briefBody .margin-note"),
                ("trail", "#sourceTrail"),
            ):
                expect(page.locator(selector)).to_contain_text(
                    article.locator(f'[data-field="{field}"]').text_content()
                )
            evidence = article.locator("[data-evidence-item]")
            expect(page.locator("#evidenceList button")).to_have_count(evidence.count())
            for index, item in enumerate(evidence.all()):
                opener = page.locator("#evidenceList button").nth(index)
                expect(opener).to_contain_text(item.locator('[data-field="text"]').text_content())
                opener.focus()
                page.keyboard.press("Enter")
                expect(page.locator("#closeEvidence")).to_be_focused()
                expect(page.locator("#evidenceTitle")).to_have_text(
                    item.locator('[data-field="tag"]').text_content()
                )
                expect(page.locator("#evidenceDetail")).to_have_text(
                    item.locator('[data-field="detail"]').text_content()
                )
                page.keyboard.press("Escape")
                expect(opener).to_be_focused()
                expect(page.locator("#evidencePopover")).to_be_hidden()
            # A new question/depth must dismiss the old detail without stealing focus.
            page.locator("#evidenceList button").first.click()


@pytest.mark.parametrize("javascript", [True, False], ids=["interactive", "nojs"])
def test_dossier__editing_register_updates_every_reading_route(
    new_context: Callable[..., BrowserContext], javascript: bool
) -> None:
    """Bewerk de echte inhoudsbron; test geen private JavaScript-variabelen."""
    import html
    import re

    payload = '<img data-injected="yes" src="x" onerror="window.injected=true"> & bron'
    source = visual_path("vraagdossier.html").read_text()
    fields = (
        "title",
        "question",
        "short",
        "medium",
        "source",
        "takeaway",
        "trail",
        "tag",
        "text",
        "detail",
        "kind",
    )
    for field in fields:
        source, count = re.subn(
            rf'(<(?:h3|p|span) data-field="{field}">).*?(</(?:h3|p|span)>)',
            lambda match, field=field: match[1] + html.escape(payload + " " + field) + match[2],
            source,
            count=1,
            flags=re.S,
        )
        assert count == 1
    page = new_context(java_script_enabled=javascript).new_page()
    page.route(
        visual_path("vraagdossier.html").as_uri(),
        lambda route: route.fulfill(body=source, content_type="text/html"),
    )
    page.goto(visual_path("vraagdossier.html").as_uri(), wait_until="networkidle")
    if javascript:
        expect(page.locator("#briefTitle")).to_have_text(payload + " title")
        expect(page.locator('[data-question="main"] span')).to_have_text(payload + " question")
        for depth in ("short", "medium", "source"):
            page.locator(f'[data-depth="{depth}"]').click()
            expect(page.locator("#briefDeck")).to_have_text(payload + " " + depth)
        expect(page.locator("#briefBody")).to_contain_text(payload + " takeaway")
        expect(page.locator("#sourceTrail")).to_have_text(payload + " trail")
        opener = page.locator("#evidenceList button").first
        expect(opener).to_contain_text(payload + " text")
        expect(page.locator("#evidenceList .evidence-item").first).to_have_attribute(
            "data-kind", payload + " kind"
        )
        opener.click()
        expect(page.locator("#evidenceTitle")).to_have_text(payload + " tag")
        expect(page.locator("#evidenceDetail")).to_have_text(payload + " detail")
    else:
        expect(page.locator("#dossier")).to_be_hidden()
        expect(page.locator("#source-register article").first).to_be_visible()
    page.emulate_media(media="print")
    article = page.locator("#source-register article").first
    expect(article).to_be_visible()
    for field in fields:
        expect(article).to_contain_text(payload + " " + field)
    expect(page.locator("[data-injected]")).to_have_count(0)
    assert page.evaluate("window.injected !== true")
