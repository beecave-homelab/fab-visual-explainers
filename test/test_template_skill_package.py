"""Een uitgepakte skill mag voor guidance geen checkout nodig hebben."""

import hashlib
import json
import posixpath
from pathlib import Path
from urllib.parse import urlsplit
from zipfile import ZipFile

from scripts.package_template_skill import LINK, NAME, ROOT, SOURCES, build_package, package_links


def test_package__guidance_links_survive_relocation(tmp_path: Path) -> None:
    output = build_package(ROOT, tmp_path / "skill.zip")
    isolated = tmp_path / "unrelated-task" / "installed-skills"
    with ZipFile(output) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(SOURCES) + 1
        archive.extractall(isolated)
    for path in isolated.rglob("*.md"):
        for match in LINK.finditer(path.read_text()):
            target = urlsplit(match["target"])
            if not target.scheme and target.path:
                assert (path.parent / target.path).is_file(), (path, match["target"])
    guide = (isolated / NAME / "references/template-reuse.md").read_text()
    # Alle bestandskaarten blijven naar hun volledige openbare HTML verwijzen.
    for match in LINK.finditer((ROOT / "docs/template-reuse.md").read_text()):
        target = urlsplit(match["target"])
        if target.path.startswith("../visuals/"):
            path = posixpath.normpath(posixpath.join("docs", target.path))
            assert f"/raw/master/{path}" in guide


def test_package__records_sources_and_rebuilds_deterministically(tmp_path: Path) -> None:
    first = build_package(ROOT, tmp_path / "first.zip")
    second = build_package(ROOT, tmp_path / "second.zip")
    assert first.read_bytes() == second.read_bytes()
    with ZipFile(first) as archive:
        provenance = json.loads(archive.read(f"{NAME}/references/provenance.json"))
        for destination, record in provenance["files"].items():
            assert SOURCES[record["source"]] == destination
            assert (
                record["sha256"]
                == hashlib.sha256((ROOT / record["source"]).read_bytes()).hexdigest()
            )


def test_package_links__preserves_fragments_and_external_sources() -> None:
    source = "docs/template-reuse.md"
    destination = "references/template-reuse.md"
    text = (
        "[regels](../AGENTS.md#templates-gebruiken-voor-een-bron) "
        "[skill](../.agents/skills/fab-html-template-reuse/SKILL.md) "
        "[bron](https://example.org/spec#focus) [hier](#selectie)"
    )
    result = package_links(text, source, destination)
    assert "(AGENTS.md#templates-gebruiken-voor-een-bron)" in result
    assert "(../SKILL.md)" in result
    assert "(https://example.org/spec#focus)" in result
    assert "(#selectie)" in result
