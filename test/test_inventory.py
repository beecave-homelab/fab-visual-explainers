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
