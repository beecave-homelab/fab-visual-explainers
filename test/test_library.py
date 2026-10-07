"""Bibliotheeknavigatie, actuele ontdekking en zelfstandige alternatieven."""

from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest
from playwright.sync_api import Page
from support import ROOT, discover_visuals

from scripts import visual_library as library


def test_library__server_discovers_changes_and_limits_files(tmp_path: Path) -> None:
    """Een draaiende server ontdekt toevoegingen en verwijderingen bij de volgende request."""
    (tmp_path / "index.html").write_text((ROOT / "index.html").read_text())
    directory = tmp_path / "visuals" / "nieuwe_categorie" / "verdieping"
    directory.mkdir(parents=True)
    (tmp_path / "private.txt").write_text("Niet serveren")
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(library.LibraryHandler, root=tmp_path))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    try:
        with urlopen(base) as response:
            assert "visual-title" not in response.read().decode().split(library.START)[1]
        visual = directory / "nieuw & veilig.html"
        visual.write_text(
            "<title>Nieuwe &amp; veilige visual</title><h1>&lt;img src=x onerror=alert(1)&gt;</h1>"
        )
        with urlopen(base) as response:
            document = response.read().decode()
            assert "Nieuwe &amp; veilige visual" in document
            assert "&lt;img src=x onerror=alert(1)&gt;" in document
            assert "nieuw%20%26%20veilig.html" in document
            assert response.headers["Cache-Control"] == "no-store"
        with urlopen(
            base + "/visuals/nieuwe_categorie/verdieping/nieuw%20%26%20veilig.html"
        ) as response:
            assert response.status == 200
        for path in (
            "/private.txt",
            "/scripts/visual_library.py",
            "/visuals/../../private.txt",
            "/visuals/",
        ):
            with pytest.raises(HTTPError) as error:
                urlopen(base + path)
            assert error.value.code == 404
        duplicate = tmp_path / "visuals" / visual.name
        duplicate.write_text("<title>Dubbele naam</title>")
        with pytest.raises(HTTPError) as error:
            urlopen(base)
        assert error.value.code == 500
        assert "Visual-inventaris ongeldig" in error.value.read().decode()
        duplicate.unlink()
        visual.unlink()
        with urlopen(base + "/index.html") as response:
            assert "Nieuwe &amp; veilige visual" not in response.read().decode()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def test_library__links_match_inventory_and_filters_keep_focus(page: Page) -> None:
    page.goto((ROOT / "index.html").as_uri())
    paths = {
        path.relative_to(ROOT).as_posix() for path in discover_visuals(ROOT / "visuals").values()
    }
    assert (
        set(
            page.locator(".visual a").evaluate_all(
                "links => links.map(a => decodeURI(a.getAttribute('href')))"
            )
        )
        == paths
    )
    for entry in library.discover():
        card = page.locator(f'.visual a[href="{entry["path"]}"]')
        assert (
            " ".join(card.locator(".visual-description").inner_text().split())
            == entry["description"]
        )
    ids = page.locator("[id]").evaluate_all("elements => elements.map(item => item.id)")
    assert len(ids) == len(set(ids))
    button = page.locator('[data-filter="toegang"]')
    button.focus()
    page.keyboard.press("Enter")
    assert button.evaluate("element => element === document.activeElement")
    assert page.locator(".visual:visible").count() == len(
        list((ROOT / "visuals/toegang").glob("*.html"))
    )
    page.locator('[data-filter="all"]').click()
    page.locator("#search").fill("continuïteit")
    assert page.locator(".visual:visible").count() > 0
    page.locator("#search").fill("<img src=x onerror=alert(1)>")
    assert page.locator("#empty").is_visible()
    assert page.locator(".visual:visible").count() == 0
    page.locator("#search").fill("")
    assert page.locator(".visual:visible").count() == len(paths)
    with page.expect_popup() as popup:
        page.locator(".visual a").first.click()
    popup.value.wait_for_load_state("networkidle")
    assert popup.value.locator("h1").count() > 0
    popup.value.close()


@pytest.mark.parametrize("width", [320, 390, 768, 1440])
def test_library__responsive(page: Page, width: int, artifact) -> None:
    page.set_viewport_size({"width": width, "height": 1000})
    page.goto((ROOT / "index.html").as_uri())
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
    page.screenshot(path=artifact(f"library-{width}.png"))


def test_library__without_javascript_and_print(new_context, artifact) -> None:
    count = len(discover_visuals(ROOT / "visuals"))
    page = new_context(java_script_enabled=False).new_page()
    page.goto((ROOT / "index.html").as_uri())
    assert page.locator(".visual:visible").count() == count
    assert not page.locator(".search-panel").is_visible()
    page = new_context().new_page()
    page.goto((ROOT / "index.html").as_uri())
    page.locator("#search").fill("no-match")
    page.emulate_media(media="print")
    assert page.locator(".visual:visible").count() == count
    page.pdf(path=artifact("library.pdf"))


def test_library__descriptions_come_from_each_visual() -> None:
    """Iedere bestaande visual levert zelf een korte inhoudelijke toelichting."""
    entries = library.discover()
    for entry in entries:
        metadata = library.Metadata()
        metadata.feed((ROOT / entry["path"]).read_text())
        assert len(metadata.description.strip()) >= 35, entry["path"]
        assert entry["description"] == " ".join(metadata.description.split())
        assert entry["description"] != entry["title"]


def test_library__new_visual_uses_intro_when_metadata_missing(tmp_path: Path) -> None:
    """Nieuwe HTML zonder metadata gebruikt de eerste bruikbare inleiding na de hoofdkop."""
    directory = tmp_path / "visuals" / "toegang"
    directory.mkdir(parents=True)
    visual = directory / "nieuw.html"
    visual.write_text(
        "<title>Nieuwe visual</title><h1>Een<br>vraag</h1><p>JavaScript staat uit.</p><p>Bekijk de rollen, hun toegang en de voorwaarden die nog toetsing vragen.</p>"
    )
    entry = library.discover(tmp_path)[0]
    assert (
        entry["description"]
        == "Bekijk de rollen, hun toegang en de voorwaarden die nog toetsing vragen."
    )
    visual.write_text(
        '<meta name="description" content="De eigen beschrijving gaat voor de inleiding.">'
        + visual.read_text()
    )
    assert (
        library.discover(tmp_path)[0]["description"]
        == "De eigen beschrijving gaat voor de inleiding."
    )


@pytest.mark.parametrize("module", [False, True], ids=["script", "module"])
def test_library__generator_rejects_duplicates_without_overwriting(
    tmp_path: Path, module: bool
) -> None:
    """Beide CLI-startwijzen laden de inventaris en behouden uitvoer bij fouten."""
    import shutil
    import subprocess
    import sys

    scripts = tmp_path / "scripts"
    scripts.mkdir()
    for name in ("visual_library.py", "visual_inventory.py"):
        shutil.copyfile(ROOT / "scripts" / name, scripts / name)
    target = tmp_path / "index.html"
    target.write_text((ROOT / "index.html").read_text())
    first = tmp_path / "visuals" / "a" / "voorbeeld.html"
    first.parent.mkdir(parents=True)
    first.write_text('<title>Voorbeeld</title><meta name="description" content="Testinhoud">')
    command = [sys.executable]
    command += ["-m", "scripts.visual_library"] if module else [str(scripts / "visual_library.py")]
    command += ["--generate"]
    cwd = tmp_path if module else tmp_path.parent
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
    generated = target.read_text()
    assert 'href="visuals/a/voorbeeld.html"' in generated
    duplicate = tmp_path / "visuals" / "b" / first.name
    duplicate.parent.mkdir()
    duplicate.write_text(first.read_text())
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    assert result.returncode != 0
    assert "Dubbele HTML-bestandsnaam" in result.stderr
    assert target.read_text() == generated
