"""Voorkom dat een verhuizing prototypes stilzwijgend uit de tests laat verdwijnen."""

from pathlib import Path

import pytest
from support import discover_visuals, visual_path


def test_inventory__discovers_nested_categories(tmp_path: Path) -> None:
    """Ook een prototype in een diepere categorie komt in de inventaris."""
    prototype = tmp_path / "categorie" / "subcategorie" / "voorbeeld.html"
    prototype.parent.mkdir(parents=True)
    prototype.write_text("<html></html>")
    assert discover_visuals(tmp_path) == {"voorbeeld.html": prototype}


def test_inventory__rejects_empty_directory(tmp_path: Path) -> None:
    """Een lege inventaris mag geen succesvolle run met nul HTML-tests opleveren."""
    with pytest.raises(ValueError, match="Geen HTML-prototypes"):
        discover_visuals(tmp_path)


def test_inventory__rejects_duplicate_names(tmp_path: Path) -> None:
    """Gelijke namen in verschillende categorieën mogen elkaar niet overschrijven."""
    for category in ("eerste", "tweede"):
        directory = tmp_path / category
        directory.mkdir()
        (directory / "voorbeeld.html").write_text("<html></html>")
    with pytest.raises(ValueError, match="Dubbele HTML-bestandsnaam"):
        discover_visuals(tmp_path)


def test_inventory__rejects_missing_requested_file() -> None:
    """Een gerichte test voor een ontbrekend prototype krijgt een duidelijke fout."""
    with pytest.raises(FileNotFoundError, match="HTML-prototype ontbreekt"):
        visual_path("ontbrekend-testprototype.html")


@pytest.mark.parametrize("consumer", ["tests", "library"])
def test_inventory__consumers_share_duplicate_rules(tmp_path: Path, consumer: str) -> None:
    from scripts import visual_library

    for category in ("a", "b"):
        path = tmp_path / "visuals" / category / "voorbeeld.html"
        path.parent.mkdir(parents=True)
        path.write_text("<title>Voorbeeld</title>")
    with pytest.raises(ValueError, match="Dubbele HTML-bestandsnaam"):
        if consumer == "library":
            visual_library.discover(tmp_path)
        else:
            discover_visuals(tmp_path / "visuals")


@pytest.mark.parametrize("consumer", ["tests", "library"])
def test_inventory__only_existing_files_inside_visuals(tmp_path: Path, consumer: str) -> None:
    """Buitenliggende, kapotte en directorylinks worden door beide routes genegeerd."""
    from scripts import visual_library

    directory = tmp_path / "visuals"
    directory.mkdir()
    outside = tmp_path / "private.html"
    outside.write_text("<title>Niet opnemen</title>")
    (directory / "outside.html").symlink_to(outside)
    (directory / "broken.html").symlink_to(tmp_path / "missing.html")
    (directory / "folder.html").mkdir()
    (directory / "linked-directory").symlink_to(tmp_path, target_is_directory=True)
    actual = directory / "nested" / "voorbeeld.html"
    actual.parent.mkdir()
    actual.write_text("<title>Voorbeeld</title>")
    alias = directory / "alias.html"
    alias.symlink_to(actual)
    expected = {alias, actual}
    if consumer == "library":
        assert {tmp_path / entry["path"] for entry in visual_library.discover(tmp_path)} == expected
    else:
        assert set(discover_visuals(directory).values()) == expected
