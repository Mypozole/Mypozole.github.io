# MyPozole website — full to-do list

Everything still open, in one place. Organized by what kind of work it
is, roughly in priority order within each section. `NEEDS-DATA.md` and
`PHOTOS-NEEDED.md` still exist with more technical detail/sourcing on
some of these, this file is the one to actually work from.

## Calendar (blocking real-time accuracy)

1. **Move or remove the Genentech event from "Food Truck (Public)."**
   It's currently the only thing making that calendar not 100% safe to
   show publicly, since it's restricted corporate vending, not open to
   walk-up customers. Either move it to a private calendar, or delete it
   from this one if it's stale.
2. **Exact stand/booth pins**, not just general market pins. Fine as-is
   for now, you already flagged this as a "when I get to it" item.
3. Decide whether any other future event types need a private/public
   split the way Food Truck did.

## Photos

See `PHOTOS-NEEDED.md` for exact file paths. Short version:

4. ~~Real Burrito photo~~ **Resolved 2026-09-03.** Replaced again with
   the new 5-item photoshoot set from your "menu items" Drive folder.
5. ~~Real Pozole cup photo~~ **Resolved 2026-09-03.** New photo from the
   same set is a real cup shot, not a bowl.
6. ~~Retouch the 2 existing take-home pouch photos~~ **Resolved
   2026-09-03.** Superseded by the full 9-SKU set, see item 7.
7. ~~The remaining 7 take-home SKU photos~~ **Resolved 2026-09-03.** All
   9 SKUs now live on Where to Buy.
8. ~~Poztada has no photo at all yet~~ **Resolved 2026-09-03.** Replaced
   again with the new 5-item photoshoot set.
9. Catering door photos, one each for Home/Office/Events (placeholder
   slots already built, just empty right now). Found a strong candidate
   for Events in your pictures folder (`IMG_9196.jpg`, the branded
   catering spread with Red Pork/Green Chicken/Jackfruit labels), not
   wired in yet, still need Home and Office candidates.
10. ~~Founder/story photo~~ **Resolved 2026-08-30.** You confirmed the
    photo you sent in chat is you (Jorge) and uploaded it to the
    Marketing folder in Drive, pulled it from there and it's live on
    the About Pozole page.

## Data and pricing, needs your confirmation

11. **Pork Red protein conflict**: the real pouch label photo shows 24g,
    the handoff brief's table says 25g. Site currently uses 24g (the
    photographed label). Confirm which is right.
12. ~~**Pozole Party minimum headcount**~~ **Resolved 2026-08-30.** You
    sent the real `MyPozole Catering Packages 2026.pdf`, turns out each
    package just has its own minimum (A: 40, B: 35, C: 30), no real
    conflict. Real pricing for all three is now live on `/catering/events`
    as comparison cards. One loose end: the older handoff docs said
    on-site trailer service was on hold pending San Diego County DEHQ
    licensing, worth a direct confirm that's resolved next time it comes
    up, see `NEEDS-DATA.md`.
13. **Online-order price per container**: the Menu page's order builder
    is using the $15.99 retail pouch price as a labeled estimate. If the
    real online/hot-order price is different, give me the number.
14. **16oz cup price**: no price exists anywhere for this format yet.
15. **Free delivery threshold**: the live site references "free delivery
    above a certain order size" but never says the amount.
16. SKU codes for all 9 products, none exist yet.
17. Ingredient lists and allergens (per the spec, these should stay
    low-visibility even once published, not featured).
18. Cup serving-size label fix: Chicken White's cup currently prints "1
    Cup (473mL)" instead of "1 Cup (454g)" like the other two whites,
    per the brief, this is a known/confirmed production issue.
19. **About Pozole's "how it's made" paragraph is placeholder copy.**
    Written from what the owner recalled secondhand (big cuts of pork
    browned then simmered, broth used for the hominy, learned from his
    mother), deliberately leaving out canned hominy and bouillon per the
    owner's call. Jorge giving a real, first-person rundown of the
    actual process would let this become real copy instead of a
    placeholder built from someone else's memory of watching him cook.

## Wholesale page, currently a placeholder section

19. Case pack size.
20. Margin.
21. Lead time.
22. Certifications, if any.
23. A real downloadable sell sheet file (doesn't exist yet).

## Content sourcing

24. **Founding story**: currently sourced only from Jorge's SDVoyager
    interview (real, verified, already live). The handoff packet also
    named "el Restaurante" and "Roaming Hunger" as sources, I couldn't
    locate the first and the second returned an access error. If you
    have either article directly, send it and I'll fold in anything new.
25. Two soft numbers in the founding story ("pozole is on a tiny fraction
    of restaurant menus," "few people have heard of it") are deliberately
    vague because I couldn't verify the interview's own source for the
    original stats (2%, 27%). If you know where those numbers came from,
    I can make the copy more specific.

## Bigger, not-yet-started features

26. **Toppings builder** (interactive), the real topping list exists now
    (from the pouch label), but no per-topping pricing, and no UI built
    yet.
27. **Live reviews widget** (Google/Yelp) — in progress 2026-08-30, you
    created a Featurable account. Once you connect your Google Business
    Profile in Featurable and build a widget there, send me the embed
    snippet (script tag + div, or an iframe URL) and I'll drop it into
    the testimonials section, no API key needed for a standard embed.
28. ~~**Real checkout/payments**~~ **Live 2026-09-02.** Switched to Square
    (Jorge's real, active account) instead of Stripe, using
    `CreatePaymentLink` for a real Square-hosted checkout page. Home/Office
    Catering (50% deposit) and the online order builder both redirect to
    a real Square checkout and were tested end to end with a real $5 test
    link. Backend is `Mypozole/mypozole-payments` on Vercel (under the
    `mypozole` team account, not personal), since GitHub Pages can't run
    server code, deployed at `mypozole-payments-mypozole.vercel.app`.
    `SQUARE_ACCESS_TOKEN` is set. Events Catering (Pozole Party) still
    isn't wired to payments, it has no real request form yet, just a
    mailto link, that's a separate future build.
    **Loose end:** there's also an old, unconfigured deploy of this same
    code sitting at `mypozole-payments.vercel.app` under Eduardo's
    personal Vercel account (`busta2`), from before we moved it to your
    team account. It has no Square token set and nothing points at it
    anymore, safe to delete whenever, or just ignore it.
29. **Sveltia CMS** (Jorge's own no-code editing panel), on hold per your
    request, revisit whenever you want to pick it back up.

## Shipped 2026-09-02, from your call notes

- ~~Find MyPozole, month out instead of a week, address on every row~~
  **Done.** Now fetches a full month, every row (not just the top card)
  shows its real address as a tappable maps link.
- ~~Menu, clickable + downloadable PDF~~ **Done, updated 2026-09-11** to
  open in-browser (`target="_blank"`, no forced `download`) instead of
  forcing a download. Full menu PDF (no photos, no invented prices) at
  `/downloads/mypozole-full-menu.pdf`, linked from the Menu page. Now
  generated by `scripts/generate-menu-pdf.py` from the live
  `menu-items` content instead of being hand-built, so it can't drift.
  Per-item pages were already real, clickable pages before this, not
  new.
- **Vending menu PDF, still open.** You wanted this sourced from an
  existing Canva file, no prices, no photos. I searched Canva and the
  only file literally named "Vending sign" turned out to be an unrelated
  generic stock template, not real MyPozole content. You said you'd check
  Canva and send the real title, still waiting on that.
- ~~Online ordering, explicit it's prepackaged~~ **Done.** Added an
  unmissable banner directly in the order builder, on top of the
  existing fine print.
- ~~Where to Buy, retail locations~~ **Confirmed already live** with all
  6 real stores and real Maps links, no changes needed.
- ~~QR landing page~~ **Done**, live at `/link`. Instagram/Facebook/Twitter,
  real Google and Yelp review links (verified live), mailing list signup
  (discount copy isolated in `src/data/qr-page.json` for easy edits),
  and the "Want to order?" / "Want to learn about pozole?" paths.

## Shipped 2026-09-11, Jorge's pre-launch punch list

- ~~Square checkout email-contact bug~~ **Fixed and verified.** Dropped
  `buyer_email` pre-population (needed a Square OAuth scope we don't
  have) instead of requesting broader access. Real end-to-end test
  reached a genuine Square checkout page.
- ~~Retail pouches as a separate orderable option~~ **Done.** New
  `RetailPouchOrderBuilder.astro` on `/menu#order`, real confirmed
  $15.99/pouch, all 9 SKUs, tested end to end (real Formspree
  submission + real Square checkout page reached). **Flagging the
  assumption Jorge asked about:** treated the take-home quart and the
  retail pouch as two distinct products (separate content entries,
  separate builders); say so if that's wrong. Also reused the take-home
  item's $40 minimum / $10 delivery fee for pouch orders since no
  separate terms exist, worth confirming.
- ~~Hide reviews until Featurable works~~ **Done.** Removed
  `<ReviewsStrip />` from the homepage (file kept, just unused) and
  added `FollowReviewTeaser.astro` (follow links + direct Google/Yelp
  review links) in its place, right after At the Market as asked.
- ~~Bigger nav logo~~ **Done.** `Nav.astro` logo and nav bar sized up.
- ~~Remove homepage Wholesale block~~ **Done.** Wholesale stays
  footer-only.
- ~~Where to Buy photo grid~~ **Done.** All 9 SKUs shown evenly sized
  in a 3x3 grid; clicking one now shows which stores carry it (real
  Stock data, reversed by SKU).
- ~~Live-events equal weight~~ **Done.** `FindMyPozole.astro` now gives
  every simultaneously-live event full prominence, no more
  primary/secondary split.
- ~~Catering forms actually deliver~~ **Verified.** Tested Home and
  Office Catering individually with real submissions, both reached a
  real Square checkout page. Events has no form by design (quote-only,
  `showDropOff={false}`), nothing to test there.
- **Wholesale freezer photo label** — diagnosed, reported, not yet
  fixed. See `NEEDS-DATA.md`, "Wholesale/freezer photo label."
- ~~Take Home Pozole added to Full Menu~~ **Done.** Split "Pozole" into
  a market-only hot item and a new `takehome-pozole` delivery/pickup
  entry, appears on `/menu`, its own page, and the regenerated PDF.
- ~~Priced vs. unpriced Full Menu PDF~~ **Partly done, blocked.**
  `scripts/generate-menu-pdf.py` can build both, but there's no real
  price anywhere for any market/trailer item or Take Home Pozole, so
  only the unpriced PDF exists and is linked. See `NEEDS-DATA.md`.
- ~~"Market Take-Home Quart" → "Take Home Pozole" rename~~ **Done** via
  the content split above; that exact phrase didn't actually appear
  anywhere in the codebase already, the concept just didn't have a
  name/page of its own yet.

## Infrastructure, lower priority

30. ~~GitHub auto-deploy~~ **Resolved 2026-08-26.** Netlify's free-tier
    credits ran out from repeated manual deploys, so primary hosting
    moved to GitHub Pages (`https://mypozole.github.io`), with a real
    GitHub Actions workflow, push to `main` now deploys automatically.
    Netlify site is still live as a frozen backup until its Sep 19
    billing reset, no action needed there unless you want to keep paying
    attention to it.
31. Domain cutover (mypozole.com pointing at this site) is still blocked
    on GoDaddy account recovery, tracked separately, not site work. Once
    unblocked, nameservers should point at GitHub Pages, not Netlify.
