"""Regressies voor de inhoudelijke diagnose-, besluit- en toegangspatronen."""

from playwright.sync_api import Page
from support import accept_gate, copy_text, open_page


def test_oorzaakopsporing__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "oorzaakopsporing")
    for cid, answer in [("c1", "y"), ("c3", "n"), ("c7", "y"), ("c2", "u")]:
        page.locator(f'[data-c="{cid}"][data-a="{answer}"]').click()
    assert page.locator("th.h").count() == 7
    assert page.locator("th.h.out").count() == 0
    assert "Zeven hypothesen" in page.locator("#verdict").inner_text()
    form = page.locator("#assessment")
    form.locator('[name="result"]').select_option(label="Bevestigd met bewijs")
    form.locator('[name="source"]').fill("Synthetisch TEST-log v1")
    form.locator('[name="date"]').fill("2026-10-26")
    form.locator('[name="reviewer"]').fill("Fictieve testbeoordelaar")
    form.locator('[type="submit"]').click()
    assert "Bevestigd met bewijs" in page.locator(".h .st").first.inner_text()
    page.locator('[data-e="c1"][data-field="source"]').fill("<img src=x onerror=alert(1)>")
    assert "Niet bevestigd" in page.locator(".h .st").first.inner_text()
    page.locator('[data-h="A"]').click()
    assert page.locator('input[data-e="c1"][data-field="source"]').input_value().startswith("<img")
    assert page.locator("img").count() == 0
    text = copy_text(page, "#copy")
    assert (
        "Onbekend / niet gecontroleerd" in text
        and "Controledatum" not in text
        and "controledatum" in text
    )
    assert "Geen toestemming voor herstel" in text


def test_go_no_go_cockpit__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "go-no-go-cockpit")
    assert page.locator("#advText").inner_text() == "No-go"
    assert page.locator("[data-crit]").count() == 20
    page.locator('[data-crit="k1"]').click()
    page.locator('[data-setstatus="gereed"]').click()
    assert page.locator('[data-crit="k1"]').get_attribute("data-status") == "blocker"
    page.evaluate("""() => {
      for(const b of document.querySelectorAll('[data-crit]')) {
        b.click(); const f=document.querySelector('#criterionEvidence');
        for(const [k,v] of Object.entries({stage:'geaccepteerd',source:'Synthetisch TEST-verslag',version:'test v1',date:'2026-10-26',reviewer:'Fictieve bevoegde beoordelaar',outcome:'akkoord'})) f.elements[k].value=v;
        document.querySelector('[data-setstatus="gereed"]').click();
      }
    }""")
    assert page.locator("#advText").inner_text() == "Go onder voorwaarden"
    assert "2 × P2" in page.locator("#summaryText").inner_text()
    assert "onvoorwaardelijk" not in page.locator("#summaryText").inner_text()
    for fid in ["B-1", "B-2"]:
        page.evaluate(
            """id => { const f=document.querySelector(`[data-finding="${id}"]`); f.elements.state.value='gesloten'; f.requestSubmit(); }""",
            fid,
        )
    assert page.locator("#advText").inner_text() == "Go"
    assert page.locator('[data-p="2"] b').inner_text() == "0"
    page.locator("#addFinding").click()
    assert page.locator("#advText").inner_text() == "No-go"
    assert page.locator('[data-p="1"] b').inner_text() == "1"
    text = copy_text(page, "#copyButton")
    assert "1 × P1" in text and "Formeel besluit: niet vastgelegd" in text
    page.locator("#resetButton").click()
    assert page.locator('[data-p="1"] b').inner_text() == "0"
    assert page.locator("#advText").inner_text() == "No-go"
    assert page.locator('[data-crit="v1"]').get_attribute("data-status") == "onbekend"


def test_decision_canvas__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "decision-canvas")
    assert page.locator("#summaryTitle").inner_text() == "Geen optie toelaatbaar"
    assert "Geen optie is toelaatbaar" in copy_text(page, "#copyButton")
    page.locator('[data-pt="B-3"]').click()
    page.locator("#tab-onz").click()
    assert "Aanname — nog niet bevestigd" in page.locator("#panel-onz").inner_text()
    page.evaluate(
        """() => { const f=document.querySelector('[data-gate="A-0"]'); f.elements.status.value='akkoord'; f.requestSubmit(); }"""
    )
    assert "ontbreken" in page.locator('[data-gate="A-0"] [role="status"]').text_content()
    for o in ["A", "B"]:
        for n in range(3):
            accept_gate(page, o, n)
    assert "Optie B scoort het hoogst" in page.locator("#summaryText").inner_text()
    page.evaluate(
        """() => document.querySelectorAll('[data-weight]').forEach(i=>{i.value=0;i.dispatchEvent(new Event('input',{bubbles:true}));})"""
    )
    assert "Gelijke stand: opties A, B" in page.locator("#summaryText").inner_text()
    assert "Gelijke stand: opties A, B" in copy_text(page, "#copyButton")
    assert "C = " not in page.evaluate("window.testCopy")
    page.locator("#resetButton").click()
    assert page.locator("#summaryTitle").inner_text() == "Geen optie toelaatbaar"


def test_rapportage_lineage__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "rapportage-lineage")
    assert "eerste geplande afspraak" in page.locator(".case").inner_text()
    page.locator('[data-id="c2"]').click()
    assert "Dossierstatus op peildatum" in page.locator("#detail").inner_text()
    page.locator('[data-id="c3"]').click()
    assert "weekcontracturen per kalenderdag / 7" in page.locator("#detail").inner_text()
    assert "bij noemer 0" in page.locator("#detail").inner_text().lower()
    page.locator('[data-s="s1"]').click()
    assert page.locator('[data-id="k2"]').get_attribute("class").find("taint") >= 0
    page.locator('[data-id="k2"]').click()
    assert "gesimuleerde bronachterstand" in copy_text(page, "#copy")


def test_autorisatielandschap__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "autorisatielandschap")
    page.locator('[data-cell="pl-ecd"]').click()
    assert "Afwijking" in page.locator("#panel-recht").inner_text()
    page.locator('[data-cell="sup-ecd"]').click()
    assert page.locator('[data-cell="sup-ecd"] .lvl-txt').inner_text() == "Geen"
    assert "Einddatum" in page.locator("#panel-recht").inner_text()
    assert "sessiescope" in page.locator("#panel-recht").inner_text()
    text = copy_text(page, "#copyButton")
    assert "scope" in text and "Peildatum" in text and "bevoegde" in text
    page.locator('[data-cell="vig-ecd"]').click()
    assert "Onbekend / niet gecontroleerd" in page.locator("#panel-recht").inner_text()


def test_joiner_mover_leaver__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "joiner-mover-leaver")
    page.locator('[data-k="mover"]').click()
    page.locator("#v-real").click()
    page.locator(".name", has_text="ECD, rol team Noord").click()
    assert "tot en met dag −1" in page.locator("#rowpanel").inner_text()
    assert "Scope" in page.locator("#rowpanel").inner_text()
    page.locator('[data-k="leaver"]').click()
    assert page.locator(".name", has_text="Laptop in bezit").count() == 1
    assert page.locator(".name", has_text="Toegangspas actief").count() == 1
    page.locator(".name", has_text="Toegangspas actief").click()
    assert "stopt aan begin dag +1" in page.locator("#rowpanel").inner_text()
    text = copy_text(page, "#copy")
    assert (
        "fysieke toegang" in text
        and "apparatuur" in text
        and "Geen feitelijke toegangsverklaring" in text
    )


def test_change_impact_map__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "change-impact-map")
    page.locator('[data-pt="auth"]').click()
    page.locator("#tab-maatregel").click()
    assert "geen automatisch breder profiel" in page.locator("#panel-maatregel").inner_text()
    page.locator('[data-mode="met"]').click()
    assert "16 voorgenomen maatregelen" in page.locator("#summaryText").inner_text()
    assert "geen bewezen risicoreductie" in page.locator("#summaryText").inner_text()
    assert "niet aangetoond" in page.locator("#panel-maatregel").inner_text().lower()


def test_proces_applicatie_map__evidence_and_safe_advice(page: Page) -> None:
    """Bewijs, bevoegdheid en samenvatting blijven consistent binnen deze casus."""
    open_page(page, "proces-applicatie-map")
    assert (
        "geen zorgprotocol"
        in page.locator('[aria-label="Lokale validatie vereist"]').inner_text().lower()
    )
    page.locator('[data-cell="indicatie"]').click()
    page.locator("#tab-over").click()
    assert "lokaal bevoegde" in page.locator("#panel-over").inner_text()
    page.locator('[data-cell="medicatieprofiel"]').click()
    assert "geen instructie" in page.locator("#panel-over").inner_text()
    assert "Niet lokaal gevalideerd" in copy_text(page, "#copyButton")
