"""Releasebeleid toetst wijzigingen en bewijs, zonder een release te publiceren."""

import subprocess
from pathlib import Path

import pytest

from scripts.check_release_version import check_change, check_refs, check_version


def files(version: str = "0.1.0", *, pending: str = "", released: bool = False) -> dict[str, str]:
    """Maak een minimale consistente projectversie en changelog."""
    notes = f"# Changelog\n\n## [Nog niet uitgebracht]\n\n{pending}\n"
    if released:
        notes += f"\n## [{version}] - 2026-10-18\n\n### Gewijzigd\n\n- Een echte wijziging.\n"
    return {
        "pyproject.toml": f'[project]\nname = "library"\nversion = "{version}"\n',
        "uv.lock": f'[[package]]\nname = "library"\nversion = "{version}"\n',
        "CHANGELOG.md": notes,
    }


def test_version__unreleased_baseline_is_not_a_release() -> None:
    """De oorspronkelijke versie wordt niet automatisch een gepubliceerde release."""
    source = files(pending="### Onderhoud\n\n- Voeg releasebeleid toe.")
    assert check_version(source.__getitem__) == "0.1.0"
    with pytest.raises(ValueError, match="releasebeschrijving"):
        check_version(source.__getitem__, release=True)


@pytest.mark.parametrize("version", ["v0.1.0", "01.2.3", "1.2", "1.2.3-beta"])
def test_version__rejects_invalid_core_semver(version: str) -> None:
    """Alleen de afgesproken numerieke SemVer is geldig."""
    with pytest.raises(ValueError, match="project.version"):
        check_version(files(version).__getitem__)


def test_version__lockfile_must_match() -> None:
    """Een bump zonder overeenkomstige lockfile wordt afgewezen."""
    source = files()
    source["uv.lock"] = files("0.2.0")["uv.lock"]
    with pytest.raises(ValueError, match="uv.lock"):
        check_version(source.__getitem__)


@pytest.mark.parametrize("change", ["index.html", "visuals/category/new.html", "visuals/old.html"])
def test_change__html_requires_a_bump_including_deletion(change: str) -> None:
    """Toevoeging, wijziging en verwijdering vallen onder dezelfde padregel."""
    source = files()
    with pytest.raises(ValueError, match="hogere SemVer"):
        check_change(source.__getitem__, source.__getitem__, {change, "CHANGELOG.md"})


def test_change__higher_html_version_requires_empty_pending_and_dated_notes() -> None:
    """Een bump krijgt pas akkoord met een gedateerde beschrijving zonder restwerk."""
    base, head = files(), files("0.2.0", released=True)
    changed = {"index.html", "pyproject.toml", "uv.lock", "CHANGELOG.md"}
    assert check_change(base.__getitem__, head.__getitem__, changed)
    head["CHANGELOG.md"] = head["CHANGELOG.md"].replace("## [0.2.0]", "## [0.3.0]")
    with pytest.raises(ValueError, match="releasebeschrijving"):
        check_change(base.__getitem__, head.__getitem__, changed)
    head.update(files("0.2.0", pending="- Nog verwerken.", released=True))
    with pytest.raises(ValueError, match="Koppel"):
        check_change(base.__getitem__, head.__getitem__, changed)


@pytest.mark.parametrize("change", ["docs/guide.md", "test/test_one.py", "install.sh"])
def test_change__maintenance_needs_changelog_but_no_bump(change: str) -> None:
    """Onderhoud mag dezelfde versie houden, maar vraagt wel een changelogupdate."""
    base, head = files(), files(pending="### Onderhoud\n\n- Pas onderhoud aan.")
    assert not check_change(base.__getitem__, head.__getitem__, {change, "CHANGELOG.md"})
    with pytest.raises(ValueError, match="Werk CHANGELOG"):
        check_change(base.__getitem__, head.__getitem__, {change})


@pytest.mark.parametrize("date", ["2026-02-30", "18-10-2026", ""])
def test_version__rejects_invalid_release_date(date: str) -> None:
    """Een datum moet bestaan en de afgesproken notatie volgen."""
    source = files(released=True)
    source["CHANGELOG.md"] = source["CHANGELOG.md"].replace("2026-10-18", date)
    with pytest.raises(ValueError):
        check_version(source.__getitem__, release=True)


def test_version__rejects_duplicate_sections_and_empty_release_notes() -> None:
    """Dubbele versies en lege rubrieken zijn geen releasebeschrijving."""
    source = files(released=True)
    source["CHANGELOG.md"] += "\n## [0.1.0] - 2026-10-18\n- Dubbel.\n"
    with pytest.raises(ValueError, match="Dubbele"):
        check_version(source.__getitem__)
    source = files(released=True)
    source["CHANGELOG.md"] = source["CHANGELOG.md"].replace("- Een echte wijziging.", "")
    with pytest.raises(ValueError, match="releasebeschrijving"):
        check_version(source.__getitem__, release=True)


def test_refs__uses_commits_and_detects_renamed_html(tmp_path: Path) -> None:
    """Een echte Git-vergelijking ontdekt ook een verplaatst HTML-bestand."""

    def git(*args: str) -> str:
        return subprocess.check_output(["git", "-C", str(tmp_path), *args], text=True).strip()

    git("init", "-q")
    git("config", "user.name", "Synthetic test")
    git("config", "user.email", "test@example.invalid")
    for name, value in files().items():
        (tmp_path / name).write_text(value)
    (tmp_path / "index.html").write_text("<h1>Synthetic</h1>")
    git("add", ".")
    git("commit", "-qm", "Initial synthetic tree")
    base = git("rev-parse", "HEAD")
    (tmp_path / "index.html").rename(tmp_path / "other.html")
    (tmp_path / "CHANGELOG.md").write_text(files(pending="- Verplaats HTML.")["CHANGELOG.md"])
    git("add", ".")
    git("commit", "-qm", "Move HTML without bump")
    # An uncommitted valid bump cannot repair an invalid committed change.
    (tmp_path / "pyproject.toml").write_text(files("0.2.0")["pyproject.toml"])
    with pytest.raises(ValueError, match="hogere SemVer"):
        check_refs(base, root=tmp_path)
    with pytest.raises(subprocess.CalledProcessError):
        check_refs("missing-ref", root=tmp_path)


@pytest.mark.parametrize(("before", "after"), [("0.1.9", "0.1.10"), ("0.9.0", "0.10.0")])
def test_change__compares_version_numbers_numerically(before: str, after: str) -> None:
    """Meercijferige minor- en patchversies worden niet als tekst vergeleken."""
    base, head = files(before), files(after, released=True)
    assert check_change(base.__getitem__, head.__getitem__, {"index.html", "CHANGELOG.md"})


def test_change__rejects_version_downgrade_even_for_maintenance() -> None:
    """Onderhoud is geen reden om een bibliotheekversie terug te zetten."""
    with pytest.raises(ValueError, match="mag niet dalen"):
        check_change(files("0.2.0").__getitem__, files().__getitem__, {"CHANGELOG.md"})


def test_change__rejects_reused_release_description() -> None:
    """Een vooraf bestaande sectie is geen nieuwe releasebeschrijving."""
    base = files()
    head = files("0.2.0", released=True)
    base["CHANGELOG.md"] = head["CHANGELOG.md"]
    with pytest.raises(ValueError, match="werk deze bij"):
        check_change(base.__getitem__, head.__getitem__, {"index.html", "CHANGELOG.md"})


def test_version__rejects_missing_unreleased_and_duplicate_project_lock() -> None:
    """De centrale sectie en precies één projectvermelding zijn verplicht."""
    source = files()
    source["CHANGELOG.md"] = "# Changelog\n"
    with pytest.raises(ValueError, match="ontbreekt"):
        check_version(source.__getitem__)
    source = files()
    source["uv.lock"] += source["uv.lock"]
    with pytest.raises(ValueError, match="niet uniek"):
        check_version(source.__getitem__)
