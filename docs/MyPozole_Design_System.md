# MyPozole Design System

Foundation document for the website rebuild. Every page, component, and future addition inherits from this. Decided once here so it never needs re-deciding later.

---

## 1. Brand tokens

### Color

| Token | Hex | Use |
|---|---|---|
| `sand` | `#D6C8AF` | Primary background, warm neutral fields |
| `brown` | `#511A0B` | Primary text, headlines, high-contrast elements |
| `terracotta` | `#C46838` | Primary accent, CTAs, links, active states |
| `tan` | `#CD9F71` | Secondary accent, highlights, subtle fills |
| `rust` | `#8B3C1D` | Deep accent, hover and emphasis states |

Confirmed from the Canva brand kit. Terracotta remains the one color that means "act here," used sparingly. Tan and rust are secondary, for depth and interaction states, not additional focal points. If everything is terracotta, nothing is.

**This is the benchmark palette, not a closed set.** It's the anchor, not the entire kit. Tints, shades, and neutral surfaces (borders, disabled states, subtle backgrounds, hover fills) should be derived from these five values rather than introduced as new, unrelated colors. Every derived shade should trace back to one of the five above, so the site always reads as one consistent system even as more surfaces get built out.

### Type

- **Display / headline:** a warm editorial serif. Used for page titles, product names, section headers. Should feel handmade and founder-forward, not corporate.
- **Body / UI:** a clean grotesk. Used for everything else: body copy, labels, buttons, forms, nutrition data.

**Scale** (mobile-first, since most traffic is a phone at a market or in a kitchen):

| Level | Size | Use |
|---|---|---|
| Display | 40px / 1.1 | Hero headline only |
| H1 | 32px / 1.15 | Page title |
| H2 | 24px / 1.2 | Section header |
| H3 | 19px / 1.3 | Card title, subsection |
| Body | 16px / 1.6 | Paragraph text |
| Small | 14px / 1.5 | Labels, captions, fine print |

### Spacing

8px base unit. All padding, margin, and gaps are multiples of 8 (8, 16, 24, 32, 48, 64). Keeps every component visually related without anyone having to think about it.

### Logo

Round brown-background lockup is primary. Never stretch, never recolor, never place on a background that fights its own sand ring. Minimum clear space equal to the height of the steam lines in the mark.

---

## 2. Photography direction

**This site is built for phone photography, not a studio shoot.** That is a constraint to design around, not a gap to apologize for. Juice Jerky and Cien Chiles, the two reference brands Jorge named, both run on real, at-the-booth photography and it reads as more credible than polish would.

**Rules:**
- Overhead bowl shots, hands, steam, toppings laid out like a palette, Jorge at the stall. Documentary, not staged.
- All *generated or illustrative* imagery is white pozole blanco only. This is a standing accuracy rule and does not change.
- Red and green style products are real, in-market SKUs. They get real photographs, never generated images. The white-only rule governs illustration, not the product line itself.
- Crop and light product photography to match the bag and pouch packaging as closely as possible. Shelf recognition is rehearsed on the site before it happens in the store.
- No stock photography. If a real photo isn't available yet, use a solid color field in an existing token color rather than a generic placeholder.

**Grid implication:** components should look intentional with an imperfect, phone-shot image (slightly off-center, natural light, real background) rather than requiring a perfectly lit, symmetrical studio frame. Generous crop tolerance, not tight art-directed crops.

---

## 3. Voice and tone

Authentic, local, slightly imperfect. UGC-feeling, not sterile. Jorge does not need to sound polished, he needs to sound like Jorge.

**Copy principle:** lead with product identity, not format. "The pozole from the farmers market, now in your freezer," not "frozen pozole, ready in ten minutes."

**Proof point hierarchy**, in order of strength: six stores all reordering with zero returns, Jensen's moving 1 to 2 units a day, roughly 30,000 bowls produced last year, retailers requesting new SKUs.

**Numbers over adjectives.** Use the actual nutrition panel figures (24g protein, 300 calories) instead of words like "clean" or "healthy," which the current ingredient list can't fully back up yet.

**Hard rule:** no em dashes or en dashes anywhere in any website copy. Use commas, colons, periods, or reword.

---

## 4. Content model

Eight records. Every page is a view onto these, so growth means adding rows, not rebuilding pages.

| Record | Key fields | Powers |
|---|---|---|
| **Product** | protein, style, format (pouch/cup), size, price, SKU, nutrition panel, ingredients | Retail pages, order page, catering, wholesale sheet |
| **Location** | name, address, type (market/store/truck stop) | Bowl Finder, store locator, map |
| **Stock** | store x SKU, in-stock boolean | Store locator filtering |
| **Appearance** | date, time, location, calendar source | Schedule, live hero, map, Google listing |
| **Menu item** | name (Pozole, Poztada, Poznachos, Pozfrito, Burrito), description | Menu, truck, catering |
| **Topping** | name, included/extra, price if extra | Toppings builder, catering config |
| **Story** | title, body, category | Education hub, SEO |
| **Testimonial** | quote, source, store/market context | Any page needing proof |
| **Wholesale account** | store name, contact, velocity data | Buyer sell sheet |

### Calendar sourcing (confirmed)

- **Farmers Markets** (Google Calendar, recurring): public, feeds schedule and Bowl Finder
- **MyPozole Food Truck (Public)**: public stops, feeds schedule and Bowl Finder
- **MyPozole Food Truck (Private)**: corporate and private bookings, internal only, also a warm lead list for catering outreach
- **MyPozole Catering Calendar**: private capacity, never public

---

## 5. Core components

Eight or nine components render the entire site.

1. **Hero / Bowl Finder** — live, time-aware. Reads today's Appearance data. "We're at Little Italy Mercato until 2pm" with a green dot when active.
2. **Product card** — image, name, protein/style, price, link. Used in grids across retail, catering, menu.
3. **Location card** — name, address, map link, live open/closed state.
4. **Schedule row** — date, location, time, one-line status.
5. **Testimonial** — quote, attribution, minimal chrome.
6. **CTA band** — full-width, one action, terracotta accent.
7. **Form** — catering quote builder, wholesale sample request, contact. Consistent field style across all three.
8. **Nutrition panel** — renders directly from Product record fields, never hand-typed twice.
9. **Toppings builder** — interactive, visual, feeds into catering config and the eventual Pozole Box builder.

---

## 6. What this unlocks

Because pages read from records instead of being hand-built, all of the following are additions, not rebuilds:
- A new store or market (new Location + Stock rows)
- A new SKU or style (new Product row)
- Nationwide shipping (new fulfillment field on existing Product)
- A second product line or city (new records in the same shape)
- A Spanish-language site (new locale field, same records)

This is the "lasting foundation" goal from the brief. The hard thinking happens once, here.
