# Still needed before launch

Per START_HERE.md's hard rule: never invent a fact, leave it visibly marked as
missing instead. This is the running list of what the content layer is
missing on purpose. Check this before writing a page that touches any of
these areas.

## Blocking-ish (referenced by multiple pages)

- ~~**Toppings.**~~ **Resolved 2026-08-25.** Real photos of the actual
  pouch label (found in Drive) list the topping set directly: cabbage,
  radishes, onions, jalapeños, cilantro, oregano, red pepper flakes,
  limes, avocado. Now in `src/content/toppings/`. Still no per-topping
  price (label just says "toppings not included," customer supplies
  them), that part is still unconfirmed.
- **Testimonials.** The brief says the reviews strip should be a live widget
  pulled from Google/Yelp, not static copy, so `src/content/testimonials/`
  is intentionally empty. If a static fallback is ever wanted, it needs real
  quotes, not written-for-the-site ones.
- **Founding story body.** `src/content/stories/founding-story.json` has the
  record shape but no body text. Needs sourcing from three named articles
  (SDVoyager, el Restaurante, Roaming Hunger) that weren't included in the
  handoff packet.

## Product record gaps

- **SKU codes** for all 9 products: not given anywhere.
- **Ingredient lists and allergens**: not given. Also, per the brief, these
  should stay low-visibility on the site even once available (a collapsed
  section or footnote), not a featured block.
- **16oz cup price**: the $15.99 verified from mypozole.com/retail is for the
  32oz retail pouch. No cup price is given anywhere.
- **Online-order per-unit price**: the Menu page's order builder
  (`src/components/OnlineOrderBuilder.astro`) uses the $15.99 retail
  pouch price as a labeled estimate, since no confirmed price exists for
  the "32oz Prepackaged" hot online-order container specifically. May or
  may not be the same price as the retail pouch, confirm before this
  becomes a real checkout.
- **Cup serving-size fix**: the brief flags that Chicken White's cup label
  wrongly lists "1 Cup (473mL)" (volume-based) instead of "1 Cup (454g)"
  like the other two whites. Confirmed as a real production issue, not yet
  reflected in any product record here since cup-format products aren't
  modeled yet.
- **Pork Red protein conflict, flagged 2026-08-25**: a real photo of the
  actual pouch label shows 24g protein per serving. The handoff brief's
  nutrition table says 25g. `src/content/products/pork-red.json` uses the
  photographed label's 24g as the more direct primary source, but this is
  a genuine conflict between two sources, not resolved, confirm with Jorge
  before it's load-bearing anywhere (e.g. a cross-SKU comparison chart).
  Also worth noting: that same photo shows net weight correctly printed
  as 907g, so the brief's separate "net weight math is off" warning may
  already be fixed on this print run, also not fully confirmed.

## Wholesale record gaps

- **Case pack, margin, lead time, certifications**: all listed as fields the
  Wholesale page needs, none have values anywhere in the packet.
- **Sell sheet file**: referenced as downloadable, doesn't exist yet as an
  asset.

## Location gaps

- **Street addresses.** mypozole.com/retail gives city + a Google Maps
  short link per store, not a street address. The Maps links are real and
  usable for "get directions" style CTAs; a typed street address for display
  would need to come from following each Maps link through or from Jorge
  directly.
- **Farmers markets, truck stops, corporate vending sites.** None of these
  are static content, per the brief's own architecture: they come live from
  Google Calendar. **Resolved 2026-08-25** for Farmers Markets, Food Truck
  (Public), and Pop-up Special Events, all three are now live in
  `src/components/FindMyPozole.astro`, real calendar IDs in Netlify env
  vars (see [[mypozole_website_setup]]). In Store Demos is wired into
  `src/pages/where-to-buy.astro` for "next demo" per store, though the
  calendar is empty right now so nothing shows yet, untested against
  real data. Catering Calendar stays internal-only, not wired to the site
  at all, correctly.

  **Still a real problem, flagged 2026-08-25:** the "Food Truck (Public)"
  calendar (renamed from "MyPozole Food Truck (2)") still contains a
  "Genetech Inc." (Genentech) event, appearing twice. This is the
  classification guide's own textbook example of a **private**,
  restricted-vending stop, not public. Renaming the calendar didn't
  remove it. As long as it's in this calendar, it will show on the site
  as if the public can walk up, which the guide says is wrong. Needs to
  either move to a private calendar or get removed from this one.

## Catering gaps

- ~~**Pozole Party minimum headcount conflict.**~~ **Resolved 2026-08-30.**
  Jorge sent the real `MyPozole Catering Packages 2026.pdf` directly. Turns
  out there was no real conflict, each of the three packages just has its
  own minimum: Package A 40, Package B 35, Package C 30. Full real pricing,
  inclusions, and add-ons for all three are now in
  `src/data/catering-pricing.json` and live on `/catering/events` as
  comparison cards.
  **Still open:** the earlier handoff docs (`MyPozole_Sitemap.md` section
  3c, `MyPozole_Claude_Design_Build_Brief.md` section 4) both said on-site
  trailer service was on hold pending San Diego County DEHQ licensing, and
  neither `TODO.md` nor Jorge's TODO answers confirmed that's resolved.
  The new page doesn't claim it's licensed either way, it presents the
  real pricing with a "request to book, a human confirms" CTA (matching
  every other catering flow on the site, none of which auto-charge
  anyway), so this isn't blocking, but worth a direct confirm from Jorge
  next time it comes up.
- **Free delivery threshold.** The live online-ordering page references free
  delivery above some order size but never states the amount.

## Photos still needed (per START_HERE.md, "still needed, not blocking")

The bag itself, both cup sizes at market, a side angle on Poznachos, a shot
of the Burrito with salsa being added. The handoff packet's `/photos` folder
has logo, an overhead hero bowl shot, and burrito/poznachos/pozole menu
shots only, no Pozfrito photo at all yet.

- **Menu photo, Pozole Burrito**: flagged 2026-08-25, the current photo
  (`src/assets/photos/burrito.jpg`, from the earlier mockup) may itself be
  AI-generated, not confirmed either way. Needs a real replacement photo.
- **Menu photo, Pozole**: per MyPozole_Sitemap.md section 5, at-market
  photography should show a **cup**, not a bowl, since that's how it's
  actually served there. Current `pozole.jpg` shows a bowl. Needs a real
  cup photo to be accurate.
- **Take-home package photos, 2 uploaded 2026-08-25** (Pork Red, Chicken
  Green pouches), used as placeholders on Where to Buy. Owner flagged
  these need retouching, added to their to-do list, not urgent.
- **Take-home package, 9 SKUs coming**: owner is preparing photos for all
  9 SKUs (pork/chicken/vegan x white/green/red), not just the 2 already
  uploaded. When those land, `src/pages/where-to-buy.astro`'s photo strip
  should probably become a per-SKU gallery instead of two hardcoded
  images, worth restructuring once the full set exists rather than
  hardcoding a 9th, 10th photo the same way.

**Trust issue, flagged 2026-08-24:** START_HERE.md states as a hard rule
that every photo in the packet is real, no AI-generated images. The owner
(and Jorge) flagged the packet's `hero_overhead_bowl.jpg` AND
`menu_burrito.jpg` AND `menu_pozole.jpg` as reading like AI-generated
images, despite that claim, that's 3 of the packet's 4 non-logo photos.
**None of the handoff packet's `/photos` are in use anymore.** All menu
and hero photos were reverted to the earlier mockup build's set
(`src/assets/photos/hero.jpg`, `burrito.jpg`, `pozole.jpg`,
`poznachos.jpg`, `pozfrito.jpg`, recovered from git history at commit
16622fe), which Jorge had already reviewed and preferred anyway. Poztada
still has no photo in either set, still a placeholder. Do not pull any
photo back in from the handoff packet without the owner or Jorge
explicitly re-confirming it looks real first, the packet's own
self-certification is not reliable here.

## Not in this packet, needed for the real build's stack

Netlify hosting, Sveltia CMS auth, Stripe Checkout, and Formspree all need
real accounts and credentials before they can be wired up. Nothing here can
create those accounts; they need to come from whoever owns (or will own)
each service.

**Deviation from the handoff brief, confirmed with the owner 2026-08-24:**
`MyPozole_Claude_Design_Build_Brief.md` names Cloudflare Pages as the
hosting target. The owner had already settled on Netlify in an earlier,
separate back-and-forth and confirmed there's no real reason to switch, so
this build uses **Netlify**, not Cloudflare Pages. Nothing else in the
stack (Astro, Sveltia CMS, Stripe, Formspree) depends on which one, so this
is a one-line swap wherever the brief's wording assumes Cloudflare.
