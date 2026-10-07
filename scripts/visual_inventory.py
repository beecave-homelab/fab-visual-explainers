"""Gedeelde bestandsinventaris voor de bibliotheek en prototypecontroles."""

from pathlib import Path


class InventoryError(ValueError):
    """De visual-inventaris is leeg of bevat ambigue bestandsnamen."""


def discover_visuals(directory: Path, *, allow_empty: bool = False) -> dict[str, Path]:
    """Vind unieke HTML-bestanden binnen directory, ook in geneste categorieën.

    Bewaar de oorspronkelijke paden voor links. Volg geen directory-symlinks;
    negeer bestandslinks buiten de visualmap en links zonder bestaand bestand.
    Alleen de bibliotheek mag een lege inventaris tonen.
    """
    root = directory.resolve()
    paths: dict[str, Path] = {}
    for path in sorted(directory.rglob("*.html")):
        if not path.resolve().is_relative_to(root) or not path.is_file():
            continue
        if path.name in paths:
            raise InventoryError(f"Dubbele HTML-bestandsnaam: {paths[path.name]} en {path}")
        paths[path.name] = path
    if not paths and not allow_empty:
        raise InventoryError(f"Geen HTML-prototypes gevonden in {directory}")
    return paths
