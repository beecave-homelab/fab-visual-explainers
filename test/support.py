"""Gedeelde testhandelingen; geen browserwerk tijdens import."""

from pathlib import Path

from playwright.sync_api import Page

ROOT = Path(__file__).resolve().parent.parent
VISUALS = ROOT / "visuals"


def discover_visuals(directory: Path) -> dict[str, Path]:
    """Vind alle prototypes en weiger een lege inventaris of ambigue namen."""
    paths: dict[str, Path] = {}
    for path in sorted(directory.rglob("*.html")):
        if path.name in paths:
            raise ValueError(f"Dubbele HTML-bestandsnaam: {paths[path.name]} en {path}")
        paths[path.name] = path
    if not paths:
        raise ValueError(f"Geen HTML-prototypes gevonden in {directory}")
    return paths


HTML_PATHS = discover_visuals(VISUALS)
HTML_FILES = tuple(HTML_PATHS)


def visual_path(filename: str) -> Path:
    """Zoek een prototype op unieke bestandsnaam, onafhankelijk van de categorie."""
    try:
        return HTML_PATHS[filename]
    except KeyError as error:
        raise FileNotFoundError(f"HTML-prototype ontbreekt: {filename}") from error


TASK_FILES = (
    "fab-test-coverage-map.html",
    "fab-continuiteitskaart.html",
    "fab-data-quality-map.html",
    "fab-omgevingsvergelijker.html",
    "fab-known-error-map.html",
    "fab-life-cycle-map.html",
    "fab-escalatiekaart.html",
    "fab-risk-control-map.html",
    "fab-pilot-cockpit.html",
    "fab-data-lineage.html",
    "fab-release-impact-explorer.html",
    "fab-adoptiekaart.html",
)


def open_page(page: Page, name: str) -> None:
    """Open een FAB-pagina vanuit de checkout."""
    page.goto(visual_path(f"fab-{name}.html").as_uri(), wait_until="networkidle")


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
