"""Ontdek zelfstandige visuals en serveer een actuele, lokale bibliotheek."""

import argparse
import html
import re
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

if __package__:
    from .visual_inventory import InventoryError, discover_visuals
else:
    from visual_inventory import InventoryError, discover_visuals

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"
CATEGORIES = {
    "incident_en_continuiteit": (
        "Incident & continuïteit",
        "Verstoring begrijpen, herstel organiseren en zorg laten doorgaan.",
    ),
    "wijziging_en_acceptatie": (
        "Wijziging & acceptatie",
        "Gevolgen onderzoeken, testen en een besluit voorbereiden.",
    ),
    "landschap_en_processen": (
        "Landschap & processen",
        "Samenhang tussen applicaties, processen en versies bekijken.",
    ),
    "toegang": ("Toegang", "Rollen, rechten en veranderingen in toegang onderzoeken."),
    "gegevens_en_ketens": (
        "Gegevens & ketens",
        "Gegevens volgen en kwaliteit en verwerking controleren.",
    ),
    "bronnen_en_kennis": (
        "Bronnen & kennis",
        "Broninformatie verkennen vanuit een overzicht of een vraag.",
    ),
}


class Metadata(HTMLParser):
    """Lees alleen tekstmetadata; voer broninhoud nooit uit."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.heading = ""
        self.description = ""
        self.intro = ""
        self.active = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "meta" and attributes.get("name", "").lower() == "description":
            self.description = attributes.get("content") or ""
        if tag == "br" and self.active:
            self.handle_data(" ")
        elif not self.active and (
            (tag == "title" and not self.title) or (tag == "h1" and not self.heading)
        ):
            self.active = "title" if tag == "title" else "heading"
        elif tag == "p" and self.heading and not self.intro and not self.active:
            self.active = "intro"

    def handle_endtag(self, tag):
        if (
            (self.active == "title" and tag == "title")
            or (self.active == "heading" and tag == "h1")
            or (self.active == "intro" and tag == "p")
        ):
            if self.active == "intro" and (
                len(self.intro.strip()) < 30 or "JavaScript staat uit" in self.intro
            ):
                self.intro = ""
            self.active = None

    def handle_data(self, data):
        if self.active:
            setattr(self, self.active, getattr(self, self.active) + data)


def discover(root=ROOT):
    """Vind nieuwe categorieën en bestanden zonder een handmatige bestandslijst."""
    entries = []
    for path in discover_visuals(root / "visuals", allow_empty=True).values():
        metadata = Metadata()
        metadata.feed(path.read_text(encoding="utf-8"))
        relative = path.relative_to(root)
        category = relative.parts[1] if len(relative.parts) > 2 else "overig"
        title = " ".join(metadata.title.split()) or path.stem.replace("-", " ")
        title = re.split(r"\s[—·]\s", title, maxsplit=1)[0]
        title = re.sub(r"^FAB\s+", "", title)
        if path.name == "incident-onepager-attent.html":
            title += " (Attent)"
        elif path.name == "incident-onepager.html":
            title += " (algemeen)"
        entries.append(
            {
                "category": category,
                "title": title,
                "description": " ".join(
                    (metadata.description or metadata.intro or metadata.heading).split()
                ),
                "path": relative.as_posix(),
            }
        )
    return entries


def render_catalog(root=ROOT):
    entries = discover(root)
    groups = list(CATEGORIES) + sorted({entry["category"] for entry in entries} - CATEGORIES.keys())
    categories = []
    sections = []
    for category in groups:
        items = [entry for entry in entries if entry["category"] == category]
        if not items:
            continue
        label, description = CATEGORIES.get(
            category, (category.replace("_", " ").capitalize(), "Visuals in deze categorie.")
        )
        escaped_category = html.escape(category, quote=True)
        categories.append(
            f'<button type="button" data-filter="{escaped_category}" aria-pressed="false"><span>{html.escape(label)}</span><span class="category-count">{len(items)}</span></button>'
        )
        cards = []
        for entry in sorted(items, key=lambda item: item["title"].casefold()):
            search = html.escape(" ".join(entry.values()).casefold(), quote=True)
            href = html.escape(quote(entry["path"], safe="/"), quote=True)
            cards.append(f'''<article class="visual" data-search="{search}">
  <a href="{href}" target="_blank" rel="noopener" aria-label="{html.escape(entry["title"], quote=True)} (nieuw tabblad)">
    <span class="visual-title">{html.escape(entry["title"])}</span>
    <span class="visual-description">{html.escape(entry["description"])}</span>
    <span class="visual-open">Open visual <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M10 4H4v16h16v-6"/></svg></span>
  </a>
</article>''')
        sections.append(f'''<section class="category" data-category="{escaped_category}" aria-labelledby="heading-{escaped_category}">
  <div class="category-heading"><h2 id="heading-{escaped_category}">{html.escape(label)}</h2><p>{html.escape(description)}</p></div>
  <div class="visual-grid">{"".join(cards)}</div>
</section>''')
    return f"""<div class="library-layout">
  <aside class="navigation" aria-label="Categorieën">
    <h2>Kies je onderwerp</h2>
    <div class="filters" hidden>
      <button type="button" data-filter="all" aria-pressed="true"><span>Alle visuals</span><span class="category-count">{len(entries)}</span></button>
      {"".join(categories)}
    </div>
    <p class="library-note">Prototypes met synthetische voorbeelden. Aanwezigheid zegt niets over inhoudelijke goedkeuring of validatie met gebruikers.</p>
    <a class="refresh" href="index.html">Overzicht verversen</a>
  </aside>
  <div class="library-content">
    <p id="result-count" role="status">{len(entries)} visuals om te verkennen</p>
    <p id="empty" hidden>Geen visuals gevonden. Probeer een ander zoekwoord of kies alle onderwerpen.</p>
    {"".join(sections) if entries else "<p>Voeg een HTML-bestand toe onder visuals/ en ververs dit overzicht.</p>"}
  </div>
</div>"""


def render_index(root=ROOT):
    template = (root / "index.html").read_text(encoding="utf-8")
    before, rest = template.split(START, 1)
    _, after = rest.split(END, 1)
    return before + START + "\n" + render_catalog(root) + "\n" + END + after


class LibraryHandler(SimpleHTTPRequestHandler):
    """Serveer uitsluitend de ingang en visuals, nooit checkoutconfiguratie."""

    def __init__(self, *args, root=ROOT, **kwargs):
        self.root = root.resolve()
        super().__init__(*args, directory=str(self.root), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_head(self):
        request_path = unquote(urlsplit(self.path).path)
        if request_path in ("/", "/index.html"):
            try:
                content = render_index(self.root).encode("utf-8")
            except InventoryError:
                self.send_error(500, "Visual-inventaris ongeldig: controleer dubbele bestandsnamen")
                return None
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            return BytesIO(content)
        candidate = (self.root / request_path.lstrip("/")).resolve()
        if (
            not candidate.is_relative_to(self.root / "visuals")
            or candidate.suffix != ".html"
            or not candidate.is_file()
        ):
            self.send_error(404, "Bestand niet gevonden")
            return None
        return super().send_head()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--generate", action="store_true", help="Werk de rechtstreeks te openen index.html bij"
    )
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.generate:
        try:
            content = render_index()
        except InventoryError as error:
            parser.error(str(error))
        (ROOT / "index.html").write_text(content, encoding="utf-8")
        print("index.html bijgewerkt")
        return
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(LibraryHandler, root=ROOT))
    print(f"Open http://127.0.0.1:{server.server_port}/ — stop met Ctrl+C", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
