#!/usr/bin/env python3
"""
Generates the Full Menu PDF(s) from src/content/menu-items/*.json, so the
PDF can't drift out of sync with the site's own menu content.

Usage: python3 scripts/generate-menu-pdf.py

Outputs:
  public/downloads/mypozole-full-menu.pdf         (no prices — always built)
  public/downloads/mypozole-full-menu-priced.pdf  (with prices — only built
                                                     if every item below has
                                                     a real price filled in)

No per-item prices exist yet for the market/trailer items (Pozole, Pozole
Burrito, Poztada, Poznachos, Pozfrito) or for Take Home Pozole — see
ITEM_PRICES below. Fill those in with real confirmed numbers to also get
the priced PDF; until then this script only produces the unpriced one.
"""
import json
import pathlib

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "src" / "content" / "menu-items"
OUT_DIR = ROOT / "public" / "downloads"

BROWN = HexColor("#511A0B")
TERRACOTTA = HexColor("#C46838")
RUST = HexColor("#8B3C1D")

# Real, confirmed per-item prices go here (e.g. "pozole": 9.00). Leave a
# name out (or set it to None) and the priced PDF is skipped rather than
# guessed at. None of these are confirmed yet.
ITEM_PRICES = {
    "pozole": None,
    "takehome-pozole": None,
    "pozole-burrito": None,
    "poztada": None,
    "poznachos": None,
    "pozfrito": None,
}

VARIETIES_TEXT = (
    "Pork — the traditional recipe, slow cooked 8 hours. Chicken — white and dark "
    "meat, slow cooked 8 hours, a slightly leaner option. Vegan (Jackfruit) — slow cooked "
    "in a vegetable base broth, plant based."
)
VARIETIES_NOTE = "Every Pozole style (White, Red, Green) is available in all three proteins."
TOPPINGS_TEXT = (
    "Shredded cabbage, chopped radishes, chopped onions, chopped jalapeños, cilantro, "
    "crushed tostadas, oregano, red pepper flakes, fresh squeezed lime juice, and avocado "
    "(available at an additional cost)."
)
FOOTER_TEXT = "MyPozole · San Diego, CA · info@mypozole.com · 858-752-9566"


def load_items():
    items = []
    for path in CONTENT_DIR.glob("*.json"):
        data = json.loads(path.read_text())
        data["id"] = path.stem
        items.append(data)
    items.sort(key=lambda d: d["order"])
    return items


def build_pdf(items, out_path, with_prices):
    styles = {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=26, textColor=BROWN, spaceAfter=2),
        "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=10.5, textColor=RUST, spaceAfter=18),
        "itemName": ParagraphStyle("itemName", fontName="Helvetica-Bold", fontSize=14, textColor=BROWN, spaceAfter=2),
        "badge": ParagraphStyle("badge", fontName="Helvetica-Bold", fontSize=8, textColor=TERRACOTTA, spaceAfter=6),
        "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, textColor=BROWN, leading=13.5, spaceAfter=4, alignment=TA_LEFT),
        "note": ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8.5, textColor=RUST, leading=12, spaceAfter=14),
        "sectionHead": ParagraphStyle("sectionHead", fontName="Helvetica-Bold", fontSize=12, textColor=BROWN, spaceBefore=10, spaceAfter=6),
        "footer": ParagraphStyle("footer", fontName="Helvetica", fontSize=8.5, textColor=RUST, alignment=1, spaceBefore=16),
    }

    story = [
        Paragraph("MyPozole", styles["title"]),
        Paragraph("Full Menu · A Full Meal in a Bowl · mypozole.com", styles["subtitle"]),
    ]

    for item in items:
        badge = "DELIVERY OR PICKUP" if item["fulfillment"] == "delivery-or-pickup" else "MARKET AND TRAILER ONLY"
        name = item["name"]
        if with_prices:
            price = ITEM_PRICES.get(item["id"])
            if price is not None:
                name = f"{name} — ${price:.2f}"
        story.append(Paragraph(name, styles["itemName"]))
        story.append(Paragraph(badge, styles["badge"]))
        story.append(Paragraph(item["longDescription"], styles["body"]))
        story.append(Paragraph(item["fulfillmentNote"], styles["note"]))

    story.append(Paragraph("Pozole Varieties", styles["sectionHead"]))
    story.append(Paragraph(VARIETIES_TEXT, styles["body"]))
    story.append(Paragraph(VARIETIES_NOTE, styles["note"]))

    story.append(Paragraph("Toppings, added by you at the table", styles["sectionHead"]))
    story.append(Paragraph(TOPPINGS_TEXT, styles["body"]))

    story.append(Paragraph(FOOTER_TEXT, styles["footer"]))

    doc = SimpleDocTemplate(
        str(out_path), pagesize=LETTER,
        topMargin=0.65 * inch, bottomMargin=0.65 * inch,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
    )
    doc.build(story)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    items = load_items()

    build_pdf(items, OUT_DIR / "mypozole-full-menu.pdf", with_prices=False)
    print(f"Wrote {OUT_DIR / 'mypozole-full-menu.pdf'} (unpriced)")

    missing = [i["id"] for i in items if ITEM_PRICES.get(i["id"]) is None]
    if missing:
        print(f"Skipped priced PDF, no confirmed price for: {', '.join(missing)}")
    else:
        build_pdf(items, OUT_DIR / "mypozole-full-menu-priced.pdf", with_prices=True)
        print(f"Wrote {OUT_DIR / 'mypozole-full-menu-priced.pdf'} (priced)")


if __name__ == "__main__":
    main()
