"""Applicatieblokken blijven op hun routes staan tijdens aanwijzen en selecteren."""

import re
from collections.abc import Callable

import pytest
from playwright.sync_api import Page, expect
from support import open_page


@pytest.mark.parametrize("width", [1440, 1920])
def test_applicatielandschap__hover_keeps_nodes_on_routes(
    page: Page, width: int, artifact: Callable[[str], str]
) -> None:
    """CSS-hover mag de SVG-positionering niet vervangen, ook niet tijdens animatie."""
    page.set_viewport_size({"width": width, "height": 1000})
    open_page(page, "applicatielandschap")
    nodes = page.locator(".app-node")
    for node in nodes.all():
        page.mouse.move(0, 0)
        baseline = node.evaluate("el => {const m = el.getCTM(); return [m.e, m.f];}")
        node.hover()
        samples = node.evaluate(
            """el => new Promise(resolve => {
                const samples = [], start = performance.now();
                function sample() {
                    const m = el.getCTM();
                    samples.push([m.e, m.f]);
                    if (performance.now() - start < 400) requestAnimationFrame(sample);
                    else resolve(samples);
                }
                sample();
            })"""
        )
        for position in samples:
            assert position == pytest.approx(baseline, abs=0.1), node.get_attribute("data-id")
        node.click()
        expect(node).to_have_class(re.compile(r".*is-selected.*"))
        node.focus()
        page.keyboard.press("Enter")
        expect(node).to_be_focused()
        page.keyboard.press("Space")
        expect(node).to_have_class(re.compile(r".*is-selected.*"))
    page.locator('.app-node[data-id="ecd"]').click()
    page.locator('.app-node[data-id="finance"]').hover()
    page.screenshot(path=artifact(f"landschap-hover-{width}.png"), full_page=True)
