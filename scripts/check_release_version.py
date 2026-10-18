"""Controleer changelog, bibliotheekversie en HTML-wijzigingen vóór een release."""

import argparse
import re
import subprocess
import tomllib
from collections.abc import Callable
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
Reader = Callable[[str], str]


def sections(text: str) -> dict[str, tuple[str, str]]:
    """Lees unieke changelogsecties en controleer echte kalenderdatums."""
    headings = list(re.finditer(r"^## \[([^\]]+)\](.*)$", text, re.MULTILINE))
    result = {}
    for index, heading in enumerate(headings):
        name, suffix = heading[1], heading[2]
        if name in result:
            raise ValueError(f"Dubbele changelogsectie: {name}")
        if name == "Nog niet uitgebracht":
            if suffix.strip():
                raise ValueError("Nog niet uitgebracht krijgt geen versiedatum.")
        else:
            if not re.fullmatch(VERSION, name) or not re.fullmatch(r" - \d{4}-\d{2}-\d{2}", suffix):
                raise ValueError("Gebruik ## [X.Y.Z] - YYYY-MM-DD voor versies.")
            date.fromisoformat(suffix[3:])
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        result[name] = (suffix, text[heading.end() : end].strip())
    if "Nog niet uitgebracht" not in result:
        raise ValueError("De sectie Nog niet uitgebracht ontbreekt.")
    return result


def check_version(read: Reader, *, release: bool = False) -> str:
    """De gewone controle laat een nog niet uitgebrachte basisversie toe."""
    project = tomllib.loads(read("pyproject.toml"))["project"]
    version = project["version"]
    if not isinstance(version, str) or not re.fullmatch(VERSION, version):
        raise ValueError("project.version moet MAJOR.MINOR.PATCH zonder v-prefix zijn.")
    packages = tomllib.loads(read("uv.lock"))["package"]
    matches = [item for item in packages if item["name"] == project["name"]]
    if len(matches) != 1 or matches[0].get("version") != version:
        raise ValueError("De projectversie in uv.lock wijkt af of is niet uniek.")
    notes = sections(read("CHANGELOG.md"))
    if release:
        if version not in notes or not re.search(r"^- \S", notes[version][1], re.MULTILINE):
            raise ValueError("De gedateerde releasebeschrijving voor de huidige versie ontbreekt.")
        if notes["Nog niet uitgebracht"][1]:
            raise ValueError("Koppel Nog niet uitgebracht eerst aan de releaseversie.")
    return version


def check_change(read_base: Reader, read_head: Reader, changed: set[str]) -> bool:
    """Iedere wijziging krijgt een changelog; HTML vereist ook een hogere versie."""
    version = check_version(read_head)
    meaningful = changed - {"CHANGELOG.md"}
    if meaningful and "CHANGELOG.md" not in changed:
        raise ValueError("Werk CHANGELOG.md bij in dezelfde wijziging.")
    product = any(
        path == "index.html" or (path.startswith("visuals/") and path.endswith(".html"))
        for path in changed
    )
    old = tomllib.loads(read_base("pyproject.toml"))["project"]["version"]
    if not isinstance(old, str) or not re.fullmatch(VERSION, old):
        raise ValueError("De basisversie is geen geldige SemVer.")
    before, after = tuple(map(int, old.split("."))), tuple(map(int, version.split(".")))
    if after < before:
        raise ValueError("De bibliotheekversie mag niet dalen.")
    if product:
        if after <= before:
            raise ValueError("Een HTML-wijziging naar main vereist een hogere SemVer.")
        check_version(read_head, release=True)
        previous = read_base("CHANGELOG.md")
        old_notes = sections(previous) if previous else {}
        if old_notes.get(version) == sections(read_head("CHANGELOG.md"))[version]:
            raise ValueError("Voeg de changelogsectie voor de nieuwe versie toe of werk deze bij.")
    return product


def git(root: Path, *args: str) -> str:
    """Gebruik argumenten zonder shell; ontbrekende refs blijven fouten."""
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE).decode()


def check_refs(base: str, head: str = "HEAD", *, root: Path = ROOT) -> bool:
    """Controleer commits, inclusief verwijderde en hernoemde HTML-bestanden."""
    base_sha, head_sha = [
        git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}").strip()
        for ref in (base, head)
    ]
    paths = set(git(root, "ls-tree", "-r", "--name-only", base_sha).splitlines())
    changed = set(
        git(root, "diff", "--no-renames", "--name-only", "-z", base_sha, head_sha, "--")
        .rstrip("\0")
        .split("\0")
    ) - {""}
    return check_change(
        lambda name: git(root, "show", f"{base_sha}:{name}") if name in paths else "",
        lambda name: git(root, "show", f"{head_sha}:{name}"),
        changed,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true", help="Eis een publiceerbare changelog")
    parser.add_argument("--base", help="Opgehaalde doelref voor controle van de PR-diff")
    parser.add_argument("--head", default="HEAD", help="Te controleren commit, samen met --base")
    args = parser.parse_args()
    try:
        if args.base:
            product = check_refs(args.base, args.head)
            if args.release:
                check_version(lambda name: git(ROOT, "show", f"{args.head}:{name}"), release=True)
            print("HTML-versiecontrole geslaagd." if product else "Onderhoudscontrole geslaagd.")
        else:
            if args.head != "HEAD":
                raise ValueError("Gebruik --head samen met --base.")
            check_version(lambda name: (ROOT / name).read_text(), release=args.release)
            print("Releasecontrole geslaagd." if args.release else "Versie en changelog geldig.")
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Versiecontrole mislukt: {exc}\n")


if __name__ == "__main__":
    main()
