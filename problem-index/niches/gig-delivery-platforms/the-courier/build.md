# Build: A Net Earnings Instrument Across Platforms

**Niche:** [[niches/gig-delivery-platforms/the-courier/profile|The Courier]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compute a courier's net earnings per engaged hour by zone, hour and platform from their own trip data, and forecast which hours next week are worth working.
**Tags:** #time-series-forecasting #gradient-boosting #descriptive-statistics #confidence-intervals #evaluation-metrics #feature-engineering #worker-facing #quick-win
**Contested on:** Whether trip-level net economics can be reconstructed accurately enough, across platforms, to guide where and when someone works.

## The Problem

A courier deciding when and where to work is deciding among zones, hours and platforms. The information available to them is gross earnings history on each app separately, promotional banners, and whatever they remember. What they need is net earnings per hour of engaged time, by zone and hour, compared across the apps they run — and nobody computes it, including them.

The cost side is what makes it hard and what makes it matter. Mileage is the dominant expense and accumulates on deadhead driving, repositioning and returns as much as on paid segments. A zone that pays well per delivery but requires long drives between them can net less than a dense zone with smaller offers, and the courier has no way to tell which is which except by working both for weeks.

## Why Nobody Has Built This

The platforms have no reason to, and would resist a tool that tells couriers to log into a competitor at 6pm.

Third parties have built parts of it and stopped short of the whole. Mileage trackers capture distance without attributing it to platforms, zones or specific deliveries, which makes them a tax tool rather than a decision tool. Earnings aggregators capture gross across apps without the cost side. The missing piece is trip-level attribution — knowing that these 4.2 miles belonged to this delivery on this platform in this zone — which requires continuous location capture, careful battery management, and reconstruction of the trip structure from a location trace plus whatever the apps expose.

There is also a data access problem that has worsened: platform APIs are limited, screen-scraping is fragile and against terms, and the tooling that exists survives on email receipt parsing and user-permitted screen reading.

## What to Build

A courier-side instrument that reconstructs net economics from the courier's own data and turns it into a weekly plan.

**Trip reconstruction.** Continuous location capture, segmented into deliveries by the platform's own notifications and receipts where available and by movement patterns where not. Each segment attributed: platform, zone, merchant, engaged interval, paid amount, distance driven including the deadhead before and after. Battery-efficient location capture is the unglamorous engineering that determines whether the product is usable at all.

**Net computation.** Earnings minus mileage at a courier-configured rate that reflects their actual vehicle — fuel, maintenance, depreciation, insurance — rather than a standard deduction figure. Report per engaged hour and per online hour separately, because the gap between them is idle time and is itself the most informative number for choosing zones.

**Comparison.** Net per engaged hour by zone, hour, day and platform, with confidence intervals that widen where the courier has thin data. This is where the value is: a courier who has run three apps for a month has enough data to learn that Saturday lunch in one zone on one app dominates everything else they do, and cannot currently see it.

**Forecast.** Next week's expected net rate by zone and hour, from the courier's own history plus observable conditions — weather, local events, promotional periods. Aggregated across users, the forecast becomes far stronger, which is the network effect that makes this a business rather than a utility.

**Tax as a by-product.** Trip-level mileage attributed and categorised produces a defensible deduction record with no additional effort, which is the feature that gets people to install and keep it running through the weeks it needs to become useful.

Build the aggregate layer carefully and with consent. Pooled data from thousands of couriers produces zone and merchant intelligence — which merchants run long, which zones pay, which promotions are real — that no individual can generate. That is the durable asset and it must be built on explicit, revocable consent, because the whole proposition is a tool that works for the courier rather than on them.

## Target Customer

Full-time and near-full-time couriers, who are numerous, decide daily where to work, and already pay for mileage and tax tools. Also worker organisations and researchers, for whom consented aggregate data is the only credible route to the net earnings figures the ongoing policy argument keeps demanding and nobody can supply.

## Impact If Built

A courier can answer the question their week turns on — where and when is my time actually worth the most — with evidence rather than folklore. Deadhead mileage becomes visible, which is where most of the unrecognised cost sits. And the industry acquires an independent, consented measurement of what gig delivery actually nets, which currently exists only inside the platforms and only in fragments.
