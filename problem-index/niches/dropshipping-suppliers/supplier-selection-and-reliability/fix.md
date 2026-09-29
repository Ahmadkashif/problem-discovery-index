# The Supplier Who Was Good Until Last Month

**Niche:** [[niches/dropshipping-suppliers/supplier-selection-and-reliability/profile|Supplier Selection & Reliability Signals]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** A supplier's performance collapses in week one and the lifetime average absorbs it for four months while merchants keep sending orders into it.
**Tags:** #change-point-detection #time-series-forecasting #evaluation-metrics #confidence-intervals #revenue-impact #hypothesis-testing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to tell a merchant whether a specific supplier will actually perform on a specific product before they commit their storefront to it — and whoever produces a signal that predicts downstream outcomes replaces the star rating the whole category runs on.

## The Problem
A supplier changes a factory, loses a staff member, switches a shipping partner or starts substituting a cheaper component. From that week, fulfilment slips and returns climb. The displayed rating, computed over eleven thousand historical orders, moves by two hundredths of a star. Merchants keep selecting them, keep sending orders, and keep absorbing refunds and chargebacks for months until enough individual merchants independently conclude something is wrong. The change was plainly visible in the platform's own data within days, and the metric was constructed in a way that guarantees it is invisible.

## Why It's Still Broken
Lifetime averaging is the default construction and its lag is not thought of as a property. Nobody monitors suppliers for change because monitoring implies acting, and acting means removing revenue. Merchant complaints arrive individually and are handled individually, so the pattern is never assembled. And the harm is distributed across many merchants, none of whom sees enough to raise it convincingly.

## What a Fix Looks Like
Monitor for change and act on it. Run change detection on each supplier's rolling fulfilment, delivery, return and dispute rates, which is the entire fix and is a standard technique applied to data the platform already has — the reason it is absent is not difficulty. Weight recent orders far more heavily in any displayed score, so the number moves when reality does. Alert merchants who are currently selling that supplier's products the moment a break is detected, since they are the people who can act and they currently find out through refund requests. Distinguish a supplier-level break from a product-level or destination-level one, because the responses differ and blanket alarms destroy trust in the alerting. Assemble merchant complaints into supplier-level signals rather than resolving them one at a time, which is where the evidence already exists in support tickets. Pause new listings from a supplier under investigation rather than waiting for confirmation, which limits the blast radius at little cost. Tell the supplier what was detected, since a large share of breaks are unintentional and fixable. Track recovery and reinstatement explicitly, so the mechanism is corrective rather than terminal. And report time-from-break-to-detection as the platform's own operating metric, because that interval is where all the merchant harm lives.

## Who Feels the Pain
Merchants funding refunds and chargebacks for months; end customers receiving late or wrong goods; and platforms losing merchants who blame the platform rather than the supplier, correctly.

## Impact If Fixed
Lifetime averaging guarantees the collapse is invisible, and the break was plain in the platform's own data within days. Change detection on rolling rates plus alerting the merchants currently selling that supplier turns a four-month loss into a one-week one.
