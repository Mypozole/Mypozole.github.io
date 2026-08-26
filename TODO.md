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

4. Real Burrito photo (current one may be AI-generated, unconfirmed).
5. Real Pozole **cup** photo (site currently shows a bowl, spec wants a cup).
6. Retouch the 2 existing take-home pouch photos (Pork Red, Chicken Green).
7. The remaining 7 take-home SKU photos (Pork White/Green, Chicken
   White/Red, Vegan White/Red/Green). You mentioned this is in progress.
8. Poztada has no photo at all yet, not even a placeholder-quality one.
9. Catering door photos, one each for Home/Office/Events (placeholder
   slots already built, just empty right now).
10. Founder/story photo for the About Pozole page (placeholder slot
    already built).

## Data and pricing, needs your confirmation

11. **Pork Red protein conflict**: the real pouch label photo shows 24g,
    the handoff brief's table says 25g. Site currently uses 24g (the
    photographed label). Confirm which is right.
12. **Pozole Party minimum headcount**: two source docs disagree, 30 vs
    30-40 people. Not published as a specific number anywhere yet because
    of this.
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
27. **Live reviews widget** (Google/Yelp), needs whichever service's
    account/API access, not something I can set up myself.
28. **Real checkout/payments** (Stripe), needs a real Stripe account.
    Right now every "order" flow (Catering, Online Order) collects the
    request and estimate, then a human confirms and takes payment
    separately, nothing charges automatically yet.
29. **Sveltia CMS** (Jorge's own no-code editing panel), on hold per your
    request, revisit whenever you want to pick it back up.

## Infrastructure, lower priority

30. GitHub → Netlify auto-deploy isn't wired up yet, I'm still running a
    manual build + deploy from here each time. Worth doing eventually so
    a push to `main` goes live on its own.
31. Domain cutover (mypozole.com pointing at this site) is still blocked
    on GoDaddy account recovery, tracked separately, not site work.
