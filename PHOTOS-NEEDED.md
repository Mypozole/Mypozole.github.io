# Photos needed

A standalone checklist, separate from `NEEDS-DATA.md` (which covers all
the non-photo data gaps). Each item names the exact file to replace or
add, and where it shows up on the site. Drop a file in at the given path
with the given filename and it's live on the next deploy, no code
changes needed for any of these except the ones marked "needs a code
change too."

## Replace existing photos

- **Pozole Burrito** — `src/assets/photos/burrito.jpg`. Flagged as
  possibly AI-generated, not confirmed either way. Shows on Home's menu
  grid and the Menu page.
- **Pozole** — `src/assets/photos/pozole.jpg`. Currently a bowl; the
  spec wants a **cup**, since that's how it's actually served at
  market/trailer. Shows on Home's menu grid and the Menu page.
- **Take-home pouch photos, retouching** — `src/assets/photos/takehome_pork_red.jpg`
  and `takehome_chicken_green.jpg`. Currently real phone photos, on the
  owner's to-do list for retouching. Show on the Where to Buy hub and
  each store's detail page.

## Add new photos (no current photo at all)

- **Poztada** — no filename reserved yet. Add
  `src/assets/photos/poztada.jpg`, then wire it into
  `src/components/MenuTeaser.astro`'s `photos` map (**needs a code
  change too**, one line). Currently shows a plain text placeholder on
  Home and Menu.
- **Take-home pouches, remaining 7 SKUs** — Pork White, Pork Green,
  Chicken White, Chicken Red, Vegan White, Vegan Red, Vegan Green. Only
  Pork Red and Chicken Green exist right now. Once the full 9-SKU set
  exists, `src/pages/where-to-buy/[id].astro`'s `photos` map should
  probably be restructured to something more scalable than 9 hardcoded
  imports (**needs a code change too**) rather than growing by hand each
  time.
- **Catering door photos**, one each for Home Catering, Office
  Catering, Events Catering. Placeholder slots are already built into
  `src/components/CateringTeaser.astro` (`data-photo-slot="catering-home"`,
  `"catering-office"`, `"catering-events"`), just empty color swatches
  right now. Shows on Home's catering teaser section.
- **Founder/story photo** — for the About Pozole page's founding-story
  section. Placeholder slot already built into
  `src/pages/about-pozole.astro` (`data-photo-slot="founder-photo"`),
  empty color swatch right now.

## Already settled, no action needed

- **Hero photo** (`hero.jpg`) — approved, just recropped 2026-08-25.
- **Logo** (`logo.png`) — the real transparent-background round logo,
  confirmed correct 2026-08-25.
- **Poznachos** (`poznachos.jpg`) — no concerns raised.

## How to actually replace one

Drop the new file at the exact path above (same filename), and it
overwrites the old one automatically on the next build. If you don't
have the repo checked out yourself, hand the files to Claude with which
one goes where and it's a two-minute swap, no design decisions needed.
