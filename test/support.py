"""Gedeelde testhandelingen; geen browserwerk tijdens import."""

from pathlib import Path

from playwright.sync_api import Page

ROOT = Path(__file__).resolve().parent.parent
HTML_FILES = tuple(sorted(path.name for path in ROOT.glob("*.html")))
TASK_FILES = (
    "fab-test-coverage-map.html",
    "fab-continuiteitskaart.html",
    "fab-data-quality-map.html",
)


def open_page(page: Page, name: str) -> None:
    """Open een FAB-pagina vanuit de checkout."""
    page.goto((ROOT / f"fab-{name}.html").as_uri(), wait_until="networkidle")


def copy_text(page: Page, button: str) -> str:
    """Vang de echte exporttekst af op de clipboardgrens."""
    page.evaluate(
        "Object.defineProperty(navigator, 'clipboard', {configurable:true, value:{writeText:async text => {window.testCopy=text;}}})"
    )
    page.locator(button).click()
    page.wait_for_function('typeof window.testCopy === "string"')
    return page.evaluate("window.testCopy")


def accept_gate(page: Page, option: str, number: int) -> None:
    """Vul synthetisch bewijs in via het formulier; laat de applicatie zelf besluiten."""
    form = page.locator(f'[data-gate="{option}-{number}"]')
    form.evaluate("form => {form.closest('details').open = true;}")
    form.locator('[name="status"]').select_option("akkoord")
    for key, value in {
        "source": "Synthetisch testbewijs",
        "version": "test v1",
        "date": "2026-10-26",
        "reviewer": "Fictieve testbeoordelaar",
    }.items():
        form.locator(f'[name="{key}"]').fill(value)
    form.evaluate("form => form.requestSubmit()")
