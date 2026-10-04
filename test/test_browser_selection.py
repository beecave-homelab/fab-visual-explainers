"""Browserfallback mag echte startproblemen niet verhullen."""

from typing import Any

import pytest
from conftest import launch_browser
from playwright.sync_api import Error


class BrowserLauncher:
    def __init__(self, failures: list[Error]) -> None:
        self.failures = failures
        self.calls: list[dict[str, Any]] = []
        self.instance = object()

    def launch(self, **options: Any) -> object:
        self.calls.append(options)
        if self.failures:
            raise self.failures.pop(0)
        return self.instance


def test_auto_prefers_chrome() -> None:
    launcher = BrowserLauncher([])
    instance, selected = launch_browser(launcher, "auto")
    assert instance is launcher.instance
    assert selected == "Google Chrome"
    assert launcher.calls == [{"channel": "chrome", "headless": True}]


def test_auto_falls_back_only_when_chrome_is_missing() -> None:
    launcher = BrowserLauncher([Error("Chromium distribution 'chrome' is not found at /chrome")])
    instance, selected = launch_browser(launcher, "auto")
    assert instance is launcher.instance
    assert "Chrome ontbreekt" in selected
    assert launcher.calls == [{"channel": "chrome", "headless": True}, {"headless": True}]


@pytest.mark.parametrize("channel", ["auto", "chrome"])
@pytest.mark.parametrize("message", ["Browser crashed", "Permission denied"])
def test_start_errors_do_not_trigger_fallback(channel: str, message: str) -> None:
    launcher = BrowserLauncher([Error(message)])
    with pytest.raises(Error, match=message):
        launch_browser(launcher, channel)
    assert len(launcher.calls) == 1


def test_explicit_chrome_requires_chrome() -> None:
    launcher = BrowserLauncher([Error("Chromium distribution 'chrome' is not found")])
    with pytest.raises(Error, match="not found"):
        launch_browser(launcher, "chrome")
    assert len(launcher.calls) == 1


def test_explicit_chromium_does_not_attempt_chrome() -> None:
    launcher = BrowserLauncher([])
    instance, selected = launch_browser(launcher, "chromium")
    assert instance is launcher.instance
    assert selected == "Playwright Chromium"
    assert launcher.calls == [{"headless": True}]


def test_missing_fallback_browser_stays_an_error() -> None:
    launcher = BrowserLauncher(
        [Error("Chromium distribution 'chrome' is not found"), Error("Executable doesn't exist")]
    )
    with pytest.raises(Error, match="Executable doesn't exist"):
        launch_browser(launcher, "auto")
    assert len(launcher.calls) == 2
