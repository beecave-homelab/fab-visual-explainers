"""Paneelbreedte, tekst en kaartgeometrie op telefoon, tablet en desktop."""

from collections.abc import Callable

import pytest
from playwright.sync_api import BrowserContext, Page
from support import HTML_FILES, visual_path

WIDTHS = (320, 390, 768, 1024, 1120, 1180, 1280, 1440, 1920, 2560)
MAPS = {
    "fab-change-impact-map.html": ".stage .pt, .stage .src-block",
    "fab-serviceradar.html": ".radar .node, .radar .core",
    "incident-onepager.html": ".process .node",
    "incident-onepager-attent.html": ".process .node",
    "kennisatlas.html": ".atlas-map .atlas-node",
    "bronkaart-onepager.html": ".topic-map .map-node, .topic-map .map-center",
    "vraagkompas.html": ".question-ring .q, .question-ring .center",
}
LABELS = {
    "fab-rapportage-lineage.html": ".node b, .node .val",
    "bron-scanner.html": ".strip .copy b, .strip .count",
    "fab-autorisatielandschap.html": ".lvl-txt, .actual-hint, .exc-badge",
    "fab-change-impact-map.html": ".pt strong, .pt-meta",
    "fab-go-no-go-cockpit.html": ".crit-txt, .crit-status",
}


@pytest.mark.parametrize("filename", HTML_FILES)
def test_responsive__content_fits_panels(page: Page, filename: str) -> None:
    """Geen documentoverflow, afgekapt opschrift of overlappende kaartbediening."""
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    for width in WIDTHS:
        page.set_viewport_size({"width": width, "height": 900})
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 2"), (
            f"{filename}: documentoverflow bij {width}px"
        )
        errors = page.locator("h1, " + LABELS.get(filename, "h1")).evaluate_all("""els => {
            const errors = [];
            for (const el of els) {
                if (!el.checkVisibility() || el.closest('svg')) continue;
                const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
                const boxes = [];
                while (walker.nextNode()) {
                    const node = walker.currentNode;
                    if (!node.textContent.trim() || !node.parentElement.checkVisibility()) continue;
                    const range = document.createRange();
                    range.selectNodeContents(node);
                    boxes.push(...range.getClientRects());
                }
                let parent = el;
                while (parent && parent !== document.body) {
                    const rect = parent.getBoundingClientRect();
                    const css = getComputedStyle(parent);
                    const clips = ['hidden', 'clip'].includes(css.overflowX)
                        || ['hidden', 'clip'].includes(css.overflowY);
                    if ((parent === el || clips) && boxes.some(text => text.width > 0 &&
                        (text.left < rect.left - 2 || text.right > rect.right + 2 ||
                        (clips && (text.top < rect.top - 2 || text.bottom > rect.bottom + 2))))) {
                        errors.push(el.textContent.trim());
                        break;
                    }
                    parent = parent.parentElement;
                }
            }
            return errors;
        }""")
        assert not errors, f"{filename} bij {width}px: afgekapt {errors}"
        if filename in MAPS:
            overlaps = page.locator(MAPS[filename]).evaluate_all("""els => {
                const visible = els.filter(el => el.checkVisibility());
                const errors = [];
                for (let i = 0; i < visible.length; i++) {
                    const a = visible[i].getBoundingClientRect();
                    for (const other of visible.slice(i + 1)) {
                        const b = other.getBoundingClientRect();
                        if (Math.min(a.right, b.right) - Math.max(a.left, b.left) > 2 &&
                            Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > 2) {
                            errors.push([visible[i].textContent.trim(), other.textContent.trim()]);
                        }
                    }
                }
                return errors;
            }""")
            assert not overlaps, f"{filename} bij {width}px: overlap {overlaps}"


@pytest.mark.parametrize("filename", MAPS)
def test_responsive__keyboard_selection_after_resize(page: Page, filename: str) -> None:
    """Alle kaartknoppen blijven na omschakelen met Enter selecteerbaar."""
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    for width in (1440, 390, 1024):
        page.set_viewport_size({"width": width, "height": 844})
        buttons = page.locator(MAPS[filename])
        for button in buttons.all():
            if button.evaluate("el => el.tagName !== 'BUTTON'"):
                continue
            button.focus()
            button.press("Enter")
            assert button.evaluate("el => el === document.activeElement")
            assert button.evaluate("""el => el.classList.contains('active')
                || el.getAttribute('aria-pressed') === 'true'""")


@pytest.mark.parametrize("filename", ("incident-onepager.html", "incident-onepager-attent.html"))
def test_responsive__short_screen_and_nojs(
    new_context: Callable[..., BrowserContext], filename: str
) -> None:
    """Een lage viewport en ontbrekend JavaScript verbergen geen titel of noodinformatie."""
    page = new_context(
        java_script_enabled=False, viewport={"width": 1280, "height": 600}
    ).new_page()
    page.goto(visual_path(filename).as_uri(), wait_until="networkidle")
    assert page.locator("h1").evaluate("el => el.scrollWidth <= el.clientWidth + 2")
    assert page.locator("#continuity").is_visible()
    page.emulate_media(media="print")
    assert page.locator("#continuity").is_visible()


@pytest.mark.parametrize("width", (1181, 1280, 1440, 1920))
def test_change_map__source_and_axis_labels_remain_separate(page: Page, width: int) -> None:
    """De wijzigingsomschrijving en assen bedekken geen impactpunt of elkaar."""
    page.set_viewport_size({"width": width, "height": 900})
    page.goto(visual_path("fab-change-impact-map.html").as_uri(), wait_until="networkidle")
    conflicts = page.evaluate("""() => {
        const labels = [...document.querySelectorAll('.src-block, .row-head, .col-head')];
        const points = [...document.querySelectorAll('.pt')];
        const conflicts = [];
        const overlap = (a, b) => Math.min(a.right, b.right) > Math.max(a.left, b.left) + 1
            && Math.min(a.bottom, b.bottom) > Math.max(a.top, b.top) + 1;
        for (let i = 0; i < labels.length; i++) {
            const a = labels[i].getBoundingClientRect();
            for (const other of [...labels.slice(i + 1), ...points]) {
                if (overlap(a, other.getBoundingClientRect())) {
                    conflicts.push([labels[i].textContent.trim(), other.textContent.trim()]);
                }
            }
        }
        return conflicts;
    }""")
    assert not conflicts, f"Overlap bij {width}px: {conflicts}"
    assert page.locator(".src-block").evaluate("""el => {
        const box = el.getBoundingClientRect();
        return [...el.children].every(child => {
            const range = document.createRange();
            range.selectNodeContents(child);
            const text = range.getBoundingClientRect();
            return text.left >= box.left + 10 && text.right <= box.right - 10
                && text.top >= box.top + 10 && text.bottom <= box.bottom - 10;
        });
    }"""), "De bronomschrijving heeft onvoldoende ruimte binnen haar kader"
    assert page.locator(".stage").evaluate("""el => {
        const box = el.getBoundingClientRect();
        return [...el.querySelectorAll('.row-head, .col-head')].every(label => {
            const text = label.getBoundingClientRect();
            return text.left >= box.left + 2 && text.right <= box.right - 2
                && text.top >= box.top + 2 && text.bottom <= box.bottom - 2;
        });
    }"""), "Een aslabel wordt afgesneden aan de rand van de kaart"


@pytest.mark.parametrize("width", (390, 1180))
def test_change_map__severity_marks_stay_with_mobile_points(page: Page, width: int) -> None:
    page.set_viewport_size({"width": width, "height": 900})
    page.goto(visual_path("fab-change-impact-map.html").as_uri(), wait_until="networkidle")
    assert page.locator(".stage").evaluate("""el =>
        [...el.querySelectorAll('.pt')].every(point => {
            const box = point.getBoundingClientRect();
            const mark = point.querySelector('.mark').getBoundingClientRect();
            return mark.left >= box.left && mark.right <= box.right
                && mark.top >= box.top && mark.bottom <= box.bottom;
        })
    """), "Een ernstmarkering staat buiten het bijbehorende impactpunt"
