# Photos needed

A standalone checklist, separate from `NEEDS-DATA.md` (which covers all
the non-photo data gaps). Each item names the exact file to replace or
add, and where it shows up on the site. Drop a file in at the given path
with the given filename and it's live on the next deploy, no code
changes needed for any of these except the ones marked "needs a code
change too."

## Replace existing photos

- ~~**Pozole Burrito**~~ **Resolved 2026-08-30, superseded 2026-09-03.**
  See the full 5-item menu photoshoot note below, replaced again as part
  of that matched set.
- ~~**Pozole**~~ **Resolved 2026-09-03.** New photo is a genuine **cup**
  shot (two MyPozole cups, market background), finally matching the
  spec's "cup, not bowl" requirement. See the 5-item photoshoot note
  below.

## Add new photos (no current photo at all)

- ~~**All 5 menu item photos**~~ **Resolved 2026-09-03.** Owner supplied
  a matched 5-photo set (Pozole, Pozole Burrito, Poztada, Poznachos,
  Pozfrito) via a Drive folder, plainly named per item (no AI-tool
  filename fingerprint this time, e.g. not "ChatGPT Image..."), consistent
  lighting/style across the set, and the burrito shot is byte-identical
  to the real phone photo already verified 2026-08-30. Replaced
  `src/assets/photos/{pozole,burrito,poztada,poznachos,pozfrito}.jpg`
  directly, no code changes needed since filenames matched exactly what
  `MenuTeaser.astro` and `menu/[item].astro` already import. Verified all
  5 load correctly (400x400, complete) via local preview.
- ~~**Take-home pouches, remaining 7 SKUs**~~ **Resolved 2026-09-03, with
  a caveat.** All 9 SKU pouch photos (Pork/Chicken/Vegan × White/Red/Green)
  are now live in `src/pages/where-to-buy/[id].astro`'s `photos` map
  (still 9 hardcoded imports, not restructured, works fine at this size).
  **Caveat, flagged to the owner and approved anyway 2026-09-03:** the
  Drive folder these came from ("take home edited" under Marketing) has
  every file named like `ChatGPT Image Sep 3, 2026, ...png`, the default
  export name from ChatGPT's image generator. These read as AI-generated
  packaging renders, not real photos of the physical printed pouches,
  which runs against this project's own standing rule (buildbrief section
  3, restated multiple times in this file): real photographs only, no
  generated imagery except white-style illustrative content. Owner was
  told this directly and said to use them anyway. Worth revisiting if
  real pouch photography ever happens, since as of now the whole
  Where to Buy product grid is AI-generated, not photographed.
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
- **Poznachos** (`poznachos.jpg`) — replaced 2026-09-03 as part of the
  5-item photoshoot set above, no concerns.

## How to actually replace one

Drop the new file at the exact path above (same filename), and it
overwrites the old one automatically on the next build. If you don't
have the repo checked out yourself, hand the files to Claude with which
one goes where and it's a two-minute swap, no design decisions needed.
