"""Geïsoleerde Chrome-contexten, lokale requests en automatische opruiming."""

from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


def pytest_configure(config: pytest.Config) -> None:
    """Assertions zijn noodzakelijk voor een zinvolle testrun."""
    if not __debug__:
        raise pytest.UsageError("Draai deze tests zonder python -O.")


@pytest.fixture(scope="session")
def browser() -> Iterator[Browser]:
    """Gebruik lokaal Chrome; sluit het ook na een mislukte test."""
    with sync_playwright() as playwright:
        instance = playwright.chromium.launch(channel="chrome", headless=True)
        try:
            yield instance
        finally:
            instance.close()


@pytest.fixture
def new_context(browser: Browser) -> Iterator[Callable[..., BrowserContext]]:
    """Track alle paginafouten en blokkeer externe afhankelijkheden per test."""
    contexts: list[BrowserContext] = []
    errors: list[str] = []
    external: list[str] = []

    def create(**options: Any) -> BrowserContext:
        defaults = {"viewport": {"width": 1440, "height": 1000}}
        context = browser.new_context(**(defaults | options))
        contexts.append(context)
        context.set_default_timeout(5000)
        context.set_default_navigation_timeout(10000)
        context.on(
            "page",
            lambda page: page.on("pageerror", lambda error: errors.append(f"{page.url}: {error}")),
        )

        def reject(route: Any) -> None:
            if not (
                route.request.url.startswith("https://fonts.googleapis.com/css2?")
                and route.request.frame.url.endswith("/incident-onepager.html")
            ):
                external.append(route.request.url)
            route.abort()

        context.route("http://**/*", reject)
        context.route("https://**/*", reject)
        return context

    try:
        yield create
    finally:
        for context in contexts:
            context.close()
    assert not errors, "JavaScript-fouten: " + "\n".join(errors)
    assert not external, "Externe requests in zelfstandig prototype: " + "\n".join(external)


@pytest.fixture
def page(new_context: Callable[..., BrowserContext]) -> Page:
    """Iedere test begint met een leeg profiel en eigen pagina."""
    return new_context().new_page()


@pytest.fixture
def artifact(tmp_path: Path) -> Callable[[str], str]:
    """Bewaar screenshots/PDF’s per test buiten de checkout."""
    return lambda name: str(tmp_path / name)
