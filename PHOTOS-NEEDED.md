# Photos needed

A standalone checklist, separate from `NEEDS-DATA.md` (which covers all
the non-photo data gaps). Each item names the exact file to replace or
add, and where it shows up on the site. Drop a file in at the given path
with the given filename and it's live on the next deploy, no code
changes needed for any of these except the ones marked "needs a code
change too."

## Replace existing photos

- ~~**Pozole Burrito**~~ **Resolved 2026-08-30.** Owner gave explicit
  permission to pull real photos from their Desktop/MyPozole/pictures
  folder. Replaced with `IMG_9940.jpg` (real overhead phone photo, cut
  burrito in its to-go container with chips and salsas) at
  `src/assets/photos/burrito.jpg`. The old possibly-AI photo is gone,
  wired into both `src/components/MenuTeaser.astro` and
  `src/pages/menu/[item].astro`, no other code change needed since the
  filename stayed the same.
- **Pozole** — `src/assets/photos/pozole.jpg`. Currently a bowl; the
  spec wants a **cup**, since that's how it's actually served at
  market/trailer. Shows on Home's menu grid and the Menu page.
- **Take-home pouch photos, retouching** — `src/assets/photos/takehome_pork_red.jpg`
  and `takehome_chicken_green.jpg`. Currently real phone photos, on the
  owner's to-do list for retouching. Show on the Where to Buy hub and
  each store's detail page.

## Add new photos (no current photo at all)

- ~~**Poztada**~~ **Resolved 2026-08-30.** Added `IMG_5136 (1).jpg`
  (real market photo, tostada held up with the farmers market blurred
  behind it) as `src/assets/photos/poztada.jpg`, wired into the
  `photos` map in both `src/components/MenuTeaser.astro` and
  `src/pages/menu/[item].astro`. Confirmed live via local preview.
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
  right now. Shows on Home's catering teaser section. **Strong candidate
  found 2026-08-30** for the Events door: `IMG_9196.jpg` in the owner's
  pictures folder, a real branded catering spread (Red Pork / Green
  Chicken / Jackfruit labeled trays). Not wired in yet, still needs the
  actual `CateringTeaser.astro` code change plus Home/Office candidates.
- ~~**Founder/story photo**~~ **Resolved 2026-08-30.** The owner sent it
  directly in chat (Jorge in a MyPozole cap and shirt, plating toppings
  at the market stand) and confirmed it's really him, then separately
  uploaded it to the "Marketing" folder in Drive. Pulled from Drive
  (file `999A93F6-7E51-4FAB-8AF7-1FCBFFF8A194.jpeg`), saved as
  `src/assets/photos/founder.jpg`, wired into `src/pages/about-pozole.astro`
  replacing the old empty `data-photo-slot` div with a real `<Image>`.

## Already settled, no action needed

- **Hero photo** (`hero.jpg`) — approved, just recropped 2026-08-25.
- **Logo** (`logo.png`) — the real transparent-background round logo,
  confirmed correct 2026-08-25.
- **Poznachos** (`poznachos.jpg`) — no concerns raised. (Note: the
  owner's pictures folder also has `IMG_5915.jpg`/`IMG_5918.jpg`, real
  alternate Poznachos shots, only worth swapping in if the current one
  is ever actually replaced, not needed on their own.)

## How to actually replace one

Drop the new file at the exact path above (same filename), and it
overwrites the old one automatically on the next build. If you don't
have the repo checked out yourself, hand the files to Claude with which
one goes where and it's a two-minute swap, no design decisions needed.
