"""Bundel de hergebruikskill en centrale guidance zonder templates of checkout."""

import argparse
import hashlib
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
NAME = "fab-html-template-reuse"
PUBLIC = "https://git.beecave-homelab.com/beecave/fab-html-visuals"
SOURCES = {
    f".agents/skills/{NAME}/SKILL.md": "SKILL.md",
    "AGENTS.md": "references/AGENTS.md",
    "docs/template-reuse.md": "references/template-reuse.md",
}
LINK = re.compile(r"(?P<prefix>\[[^\]\n]*\]\()(?P<target>[^\s)]+)(?P<suffix>\))")


def package_links(content: str, source: str, destination: str) -> str:
    """Behoud gebundelde links; maak overige repositorylinks openbaar bruikbaar."""

    def replace(match: re.Match[str]) -> str:
        target = match["target"]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match[0]
        path = posixpath.normpath(posixpath.join(posixpath.dirname(source), parsed.path))
        if path in SOURCES:
            target = posixpath.relpath(SOURCES[path], posixpath.dirname(destination) or ".")
        else:
            mode = "raw" if path.startswith("visuals/") and path.endswith(".html") else "src"
            target = f"{PUBLIC}/{mode}/master/{path}"
        if parsed.fragment:
            target += f"#{parsed.fragment}"
        return match["prefix"] + target + match["suffix"]

    return LINK.sub(replace, content)


def build_package(root: Path, output: Path) -> Path:
    """Genereer een reproduceerbare ZIP; guidance blijft in de centrale bronnen."""
    files: dict[str, bytes] = {}
    provenance = {}
    for source, destination in SOURCES.items():
        original = (root / source).read_bytes()
        files[destination] = package_links(original.decode("utf-8"), source, destination).encode(
            "utf-8"
        )
        provenance[destination] = {
            "source": source,
            "sha256": hashlib.sha256(original).hexdigest(),
        }
    files["references/provenance.json"] = (
        json.dumps({"repository": PUBLIC, "files": provenance}, indent=2) + "\n"
    ).encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for destination, content in sorted(files.items()):
            entry = ZipInfo(f"{NAME}/{destination}", date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, content)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "outputs" / "skill-packages" / f"{NAME}.zip",
        help="ZIP-bestemming (bestaand pakket op dit pad wordt opnieuw gegenereerd)",
    )
    args = parser.parse_args()
    print(build_package(ROOT, args.output).resolve())


if __name__ == "__main__":
    main()
