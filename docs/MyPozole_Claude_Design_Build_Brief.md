# MyPozole Website Build Brief

For Claude Design. Everything below is confirmed with the owners, not speculative. Where a decision is still open, it's flagged as such.

---

## 1. What this site is for

MyPozole is five businesses wearing one website: farmers markets and food trailer (90.7% of revenue), retail (4.7%), catering (3.9%), and the website itself (0.75%). The website cannot out-earn the markets directly. Its job is to be the conveyor belt that moves people off the 90.7% and onto retail, catering, and eventually national shipping.

**Priority order confirmed by Jorge:** catering leads on the website, since it's the only channel a site can close end-to-end. Farmers markets second, since that's where 90% of customers already are and where the funnel starts. Retail leads on distribution strategy, not on the website itself, since a website cannot close a retail sale, only point at a freezer aisle.

**Success metric:** not website revenue. A market customer who buys a bag at Jensen's three days later is a win the analytics will never show directly. Design for that handoff, not for checkout volume.

**The stack:** Astro (framework) + Cloudflare Pages (hosting, free tier) + Sveltia CMS at /admin (Jorge's editing interface) + Stripe Checkout (payments) + Formspree (forms). Static-first, edge-hosted, fast on one bar of signal in a parking lot.

**The maintenance constraint that shapes everything:** Eduardo builds it and works through the kinks, then Jorge takes over. If Jorge can't make a change in 60 seconds on his phone, it doesn't belong in his workflow. The schedule updates through Google Calendar, which he already uses. Everything else changes monthly at most.

---

## 2. Content model

Eight record types. Every page is a view onto these. Growth means adding rows, not rebuilding pages.

### Product
protein (pork / chicken / vegan), style (white / red / green), format (32oz pouch / 16oz cup), price, SKU, full nutrition panel, ingredient list, allergens.

**Confirmed nutrition data, per serving (454g):**

| SKU | Cal | Fat | Chol | Sodium | Carb | Fiber | Sugar | Protein |
|---|---|---|---|---|---|---|---|---|
| Pork White | 300 | 9g | 70mg | 750mg | 28g | 5g | 4g | 24g |
| Pork Red | 310 | 9g | 70mg | 750mg | 30g | 5g | 6g | 25g |
| Pork Green | 300 | 9g | 70mg | 750mg | 29g | 5g | 5g | 24g |
| Chicken White | 270 | 5g | 85mg | 740mg | 28g | 5g | 4g | 25g |
| Chicken Red | 280 | 5g | 85mg | 750mg | 30g | 5g | 6g | 26g |
| Chicken Green | 270 | 6g | 85mg | 740mg | 29g | 5g | 5g | 25g |
| Vegan White | 180 | 1.5g | 0mg | 690mg | 39g | 5g | 13g | 3g |
| Vegan Red | 200 | 2g | 0mg | 690mg | 41g | 6g | 15g | 4g |
| Vegan Green | 190 | 2g | 0mg | 690mg | 40g | 6g | 14g | 3g |

**Copy rule:** lead with protein, fiber, and calories, all strong numbers. Never lead with sodium, which sits around 30% DV across the board. Never place the vegan SKU's protein number next to pork or chicken's in a comparison table, since 3g next to 24g reads as a defect rather than a different, honest product. Red style carries 50% daily Vitamin A across all three proteins. Green style carries meaningfully more Vitamin C. Both are real, panel-backed hooks currently unused anywhere.

**Known issue, flag for Jorge, not a design blocker:** pouch labels appear to be on the pre-2016 FDA format (no Added Sugars line, Calories from Fat instead of current format). The 16oz cup labels are on the current format. Worth a compliance check before the next print run. Also, net weight math: 2 servings at 454g should total 907g, not the 454g printed on some pouch fronts.

### Stock
store × SKU × in-stock boolean. Confirmed distribution as of this build:

| Store | Pork W | Pork R | Pork G | Chick W | Chick R | Chick G | Vegan W | Vegan R | Vegan G |
|---|---|---|---|---|---|---|---|---|---|
| Jensen's | Y | | | Y | Y | Y | Y | | |
| Seaside | Y | Y | | | Y | | Y | | |
| Windmill Farms | Y | | | Y | | | | | |
| Boney's | Y | | | Y | | | | | |
| Valley Farm | Y | | | Y | | | | | |
| SD Vegan Market | | | | | | | Y | Y | Y |

No two stores carry the same assortment. The store locator must filter live against this table, not just list six addresses.

### Location
name, address, type (market / store / truck stop), live pin coordinates where available (see Appearance).

### Appearance
date, time, location, calendar source, menu availability tag (full menu / frozen retail / samples only). Powers Find MyPozole and the schedule page.

**Calendar architecture, confirmed final:**

| Calendar | Feeds | Classification rule |
|---|---|---|
| Farmers Markets | Public schedule | Always public |
| Food Truck (Public) | Public schedule | Open selling to the public |
| Food Truck (Private) | Find MyPozole, shown with company name (e.g. "Illumina," "Neurocrine") and a clear "not open to the public" note, since it's vending on a restricted campus, not a hidden booking | Vending at a corporate site, access restricted to that company |
| Pop-up Special Events | Public schedule | Always public by definition |
| In Store Demos | Store locator "next demo" | n/a |
| Catering Calendar | Internal only, plus a blocked "Private Event" slot on Find MyPozole with hours only, no company name, since MyPozole is not marketing that event | Fully private booking, MyPozole not responsible for promotion |

The test for classification: can a member of the public walk up and buy something? Venue never decides this, access does. A vending event at a school is public. A booked private party at a public park is Catering.

**Location precision:** farmers markets should use a dropped pin rather than a street address where the market is large enough that an address alone leaves someone wandering. Truck stops and store demos are precise enough with a street address already.

### Menu item
name (Pozole, Poztada, Poznachos, Pozfrito, Pozole Burrito), description, format availability.

**Naming principle, confirmed by direct experience:** a Poz-prefixed name only works when it's a light twist on an already-familiar word (tostada, nachos). The Pozole Burrito was left undescribed by an invented name specifically because no natural Poz-word fit, and that plain naming eliminated the confusion the other invented names sometimes cause. Apply this test to any future item, including the Pozole Box: if no natural word exists to twist, use the plain description instead of forcing a coined name.

### Topping
name, included or extra, price if extra. Feeds the toppings builder concept and any future catering configurator.

### Story
title, body, category. Education content, SEO layer, built last.

### Testimonial
quote, source, market or store context.

### Wholesale account
store name, contact, velocity data, current stock (links to Stock table).

---

## 3. Design tokens

### Color

| Token | Hex | Use |
|---|---|---|
| sand | #D6C8AF | Primary background |
| brown | #511A0B | Primary text, headlines |
| terracotta | #C46838 | Primary accent, CTAs, active states |
| tan | #CD9F71 | Secondary accent, highlights |
| rust | #8B3C1D | Deep accent, hover and emphasis states |

Confirmed from the Canva brand kit. Terracotta remains the primary "act here" accent, used sparingly. Tan and rust are secondary, for depth and state changes, not competing focal points.

**This is the benchmark palette, not a closed set.** Tints, shades, and neutral surfaces (borders, disabled states, subtle backgrounds, hover fills) should be derived from these five values rather than introduced as unrelated new colors. Every derived shade should trace back to one of the five above.

### Type
Warm editorial serif for display and headlines. Clean grotesk for everything else. Scale defined in the Design System doc, mobile-first, 8px spacing unit throughout.

### Photography
Built for phone photography, not a studio shoot, matching the Juice Jerky and Cien Chiles reference points Jorge named. Overhead bowls, hands, steam, toppings laid out like a palette, Jorge at the stall. All generated or illustrative imagery is white pozole blanco only, a standing accuracy rule. Red and green SKUs are real, in-market products and get real photographs, never generated ones.

### Voice
Authentic, founder-forward, UGC-feeling. No em dashes or en dashes anywhere in any copy. Numbers over adjectives: use "24g protein" instead of "clean," since the current ingredient list can't fully back health-adjective claims until reformulation lands.

Full detail on all of the above lives in `MyPozole_Design_System.md`, already delivered and confirmed.

---

## 4. Key features

### Find MyPozole
Live, time-aware hero component. Reads the three merged public calendars (Farmers Markets, Food Truck Public, Pop-up Special Events). Shows current or next stop, a green dot when live, and a menu-availability tag so a visitor knows whether to expect a full menu, frozen retail, or samples only. Uses dropped-pin coordinates at markets where available, falls back to street address elsewhere.

### Store locator
Filters live against the Stock table. Must support filtering by protein and style, since assortment varies completely store to store. Shows next scheduled demo per store, pulled from the In Store Demos calendar. Includes an "ask your store to stock it" generator that produces a pre-written request and captures the interaction for the wholesale pipeline.

### Catering, two doors plus a private-events prompt
**Door 1, default and highest priority:** drop-off quote builder. Quarts, protein split, date picker enforcing real lead times (24hr for 4-12 quarts, 48hr for 13-50, contact above 50), $64 floor at the $16/quart, 4-quart minimum, delivery zip check, deposit at booking. Built from the confirmed 2026 catering PDF pricing.

**Door 2:** Pozole Party request form for Packages A, B, C (on-site service, per-person pricing, 30-40 person minimums). This is a request, not an instant booking, since it requires a human touch for the 50% deposit and 60-day cancellation terms, and because on-site trailer service is currently on hold pending San Diego County DEHQ licensing. Do not present on-site service as available until that's resolved.

**Private and corporate bookings on Find MyPozole, two distinct treatments:**

- **Restricted vending (Food Truck Private)**, like Illumina or Neurocrine: shown with the company name, so employees of that company know where to find the truck, but clearly labeled "not open to the public" so nobody else shows up expecting to be served. This is vending with restricted access, not a hidden event.
- **Fully private catering (Catering Calendar)**: MyPozole is not responsible for marketing these, so they appear only as a blocked "Private Event" slot with hours, no company name shown at all.

No client-naming decision pending for the second category, since nothing is ever named there. The first category is intentionally named, since the whole point is letting that company's staff find the truck.

### Pozole Box
A full pozole dinner kit: broth and protein, hominy, toppings in individual containers, salsas separate, tostadas, oregano and lime, and a printed card with heating instructions and hosting tips. Sized 4/8/12. Named plainly, not with an invented Poz-word, per the naming principle above. Strongest candidate for a seasonal pre-order push around Sept 16, Christmas Eve, and New Year's, the two months that already account for roughly $9,700 of the year's $12,600 in catering revenue.

### Wholesale / buyer page
Velocity data (Jensen's moving 1-2 units daily, roughly 30,000 bowls produced last year, six stores all reordering with zero returns), case pack, margin, lead time, certifications, downloadable sell sheet, sample request form. Highest-value visitor to the site currently served nothing.

### QR landing page
Already live and printed on packaging. Story, Jorge, the family recipe, then two commercial paths: where else to buy it, and catering. Recommend building this first since it's the only asset already unblocked and in market.

---

## 5. Build order

1. **QR landing page.** Live, unblocked, proves the design system on a real page.
2. **Find MyPozole + schedule.** Serves 90.7% of the customer base.
3. **Store locator + product pages.** Converts market customers to retail.
4. **Catering, both doors.** Highest-value closeable transaction on the site.
5. **Wholesale / buyer page.** Opens doors seven through twenty.
6. **Pozole Box.** Site's own reason to exist, high order value, seasonal.
7. **Education / Story content.** Slow-burn SEO, built last, compounds over time.

---

## 6. Open items before or during build

- Classification going forward is confirmed: an event is Catering only if it cannot be attended by the general public. Everything else, including vending at a school like John Muir, is public. No further reclassification decision pending, this is now the standing rule.
- Resolved: private and corporate events do not get a dedicated marketing section. They appear on Find MyPozole as a blocked "Private Event" listing with hours only, no client name. This shows the truck is in demand without exposing any client details.
- Reformulation is a long-term project, not part of this build. Note only: it is in progress to open up more retail opportunities and will likely land at some point in the future.
- **Ingredient list visibility, confirmed:** do not feature the ingredient list prominently anywhere on the site for now. It's legally required on the retail product itself and stays there, but the website should not draw extra attention to it, particularly for farmers market shoppers who wouldn't otherwise scrutinize it. If a product page needs an ingredient list for compliance reasons, keep it low-visibility (e.g. a collapsed section or footnote) rather than a featured block. Revisit once reformulation lands.
- Pouch FDA format and net-weight math: confirmed real issues, will be corrected on the next label print run. No longer an open question, just a known fix in progress.
- **16oz cups, caught before production:** serving size units are inconsistent across the three proteins. Pork White and Vegan White correctly list "1 Cup (454g)," matching the container's actual weight. Chicken White instead lists "1 Cup (473mL)," which is volume-based, inconsistent with the other two, and internally off besides, since 473mL is roughly two standard cups, not one. Fix before these go to production: standardize all three on "1 Cup (454g)."
