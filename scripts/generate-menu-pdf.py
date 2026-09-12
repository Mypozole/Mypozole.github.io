#!/usr/bin/env python3
"""
Generates the Full Menu PDF(s) from src/content/menu-items/*.json and
src/data/menu-extras.json, so the PDF can't drift out of sync with the
site's own menu content.

Usage: python3 scripts/generate-menu-pdf.py

Outputs:
  public/downloads/mypozole-full-menu.pdf         (no prices)
  public/downloads/mypozole-full-menu-priced.pdf  (with prices, real and
                                                     confirmed as of
                                                     MyPozole_Menu_Redesign.pdf,
                                                     2026-09-11)
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
EXTRAS_PATH = ROOT / "src" / "data" / "menu-extras.json"
OUT_DIR = ROOT / "public" / "downloads"

BROWN = HexColor("#511A0B")
TERRACOTTA = HexColor("#C46838")
RUST = HexColor("#8B3C1D")

FOOTER_TEXT = "MyPozole · San Diego, CA · info@mypozole.com · 858-752-9566"


def load_items():
    items = []
    for path in CONTENT_DIR.glob("*.json"):
        data = json.loads(path.read_text())
        data["id"] = path.stem
        items.append(data)
    items.sort(key=lambda d: d["order"])
    return items


def load_extras():
    return json.loads(EXTRAS_PATH.read_text())


def fmt_price(n):
    s = f"{n:.2f}"
    return f"${s[:-3]}" if s.endswith(".00") else f"${s}"


def build_pdf(items, extras, out_path, with_prices):
    styles = {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=26, textColor=BROWN, spaceAfter=2),
        "subtitle": ParagraphStyle("subtitle", fontName="Helvetica", fontSize=10.5, textColor=RUST, spaceAfter=14),
        "itemName": ParagraphStyle("itemName", fontName="Helvetica-Bold", fontSize=14, textColor=BROWN, spaceBefore=8, spaceAfter=2),
        "itemDesc": ParagraphStyle("itemDesc", fontName="Helvetica", fontSize=9, textColor=BROWN, leading=12.5, spaceAfter=5),
        "variantLine": ParagraphStyle("variantLine", fontName="Helvetica-Bold", fontSize=9.5, textColor=RUST, leading=13, spaceAfter=1),
        "variantNote": ParagraphStyle("variantNote", fontName="Helvetica-Oblique", fontSize=8.5, textColor=BROWN, leading=11.5, spaceAfter=5),
        "sectionHead": ParagraphStyle("sectionHead", fontName="Helvetica-Bold", fontSize=12, textColor=BROWN, spaceBefore=10, spaceAfter=6),
        "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, textColor=BROWN, leading=13.5, spaceAfter=4, alignment=TA_LEFT),
        "note": ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8.5, textColor=RUST, leading=12, spaceAfter=6),
        "footer": ParagraphStyle("footer", fontName="Helvetica", fontSize=8.5, textColor=RUST, alignment=1, spaceBefore=16),
    }

    story = [
        Paragraph("MyPozole", styles["title"]),
        Paragraph("Full Menu · A Full Meal in a Bowl · mypozole.com", styles["subtitle"]),
        Paragraph("Included with every order", styles["sectionHead"]),
        Paragraph(" · ".join(extras["includedWithEveryOrder"]), styles["body"]),
    ]

    for item in items:
        story.append(Paragraph(item["name"], styles["itemName"]))
        story.append(Paragraph(item["description"], styles["itemDesc"]))
        for v in item["variants"]:
            line = f"{v['label']} — {fmt_price(v['priceDollars'])}" if with_prices else v["label"]
            story.append(Paragraph(line, styles["variantLine"]))
            story.append(Paragraph(v["note"], styles["variantNote"]))

    story.append(Paragraph("Extras &amp; Add-ons", styles["sectionHead"]))
    extra_lines = [f"{e['label']} — {fmt_price(e['priceDollars'])}" for e in extras["extras"]] if with_prices \
        else [e["label"] for e in extras["extras"]]
    story.append(Paragraph(" · ".join(extra_lines), styles["body"]))

    if with_prices:
        vd = extras["volumeDiscounts"]
        story.append(Paragraph("Volume Discounts", styles["sectionHead"]))
        story.append(Paragraph(vd["appliesTo"], styles["body"]))
        tier_line = "   ".join(f"Buy {t['quantity']} — {fmt_price(t['totalDollars'])}" for t in vd["tiers"])
        story.append(Paragraph(tier_line, styles["variantLine"]))

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
    extras = load_extras()

    build_pdf(items, extras, OUT_DIR / "mypozole-full-menu.pdf", with_prices=False)
    print(f"Wrote {OUT_DIR / 'mypozole-full-menu.pdf'} (unpriced)")

    build_pdf(items, extras, OUT_DIR / "mypozole-full-menu-priced.pdf", with_prices=True)
    print(f"Wrote {OUT_DIR / 'mypozole-full-menu-priced.pdf'} (priced)")


if __name__ == "__main__":
    main()
