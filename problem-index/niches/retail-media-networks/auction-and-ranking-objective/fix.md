# The Promoted Product That Is Out of Stock

**Niche:** [[niches/retail-media-networks/auction-and-ranking-objective/profile|Auction & Ranking Objective]]
**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Type:** Fix (Pain Point)
**One-liner:** The top sponsored result is unavailable at the shopper's store, so the retailer charged a brand to show an advertisement for something the shopper cannot buy.
**Tags:** #data-integration #evaluation-metrics #automation #revenue-impact #descriptive-statistics #quick-win #workflow-orchestration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to rank a sponsored slot by the retailer's real economics rather than by bid times predicted click — and whoever expresses that objective properly earns more from the same inventory while giving the shopper a better page.

## The Problem
A shopper searching for a product at their local store sees a sponsored result at the top for an item that store does not have. They tap it, discover it is unavailable, and go back — or worse, add it, and find out at fulfilment. The brand paid for that placement. The retailer charged for it. The shopper's trip was degraded. The stock position was known precisely by a system in the same company, and the advertisement decisioning did not consult it, because inventory lives in merchandising and the media stack was integrated to the catalogue rather than to the stock ledger.

## Why It's Still Broken
The media platform integrates to product data rather than to store-level inventory, which was the quick integration at launch and became permanent. Store-level availability changes constantly and the media stack has no pipeline for it. Suppressing unavailable products reduces auction density and therefore short-term revenue, which nobody volunteers for. And the failure is absorbed by the shopper, who does not file a ticket.

## What a Fix Looks Like
Connect the stock ledger to the auction. Filter sponsored candidates on availability at the shopper's fulfilling location, which is the fix, is a single integration, and eliminates the most visible quality failure in the category outright. Use availability confidence rather than a binary, since stock data is imperfect and a threshold is more honest than a filter that trusts a stale count. Degrade gradually — deprioritise before excluding — so thin categories do not empty out entirely. Credit brands automatically for impressions served on unavailable inventory, which is fair, builds trust, and is a compelling reason for the brand to keep spending. Alert the brand when their advertised product is widely unavailable, since they usually do not know and frequently can fix it. Feed the pattern back to merchandising, because a persistently advertised and persistently unavailable product is a supply problem the media data has surfaced first. Extend to online fulfilment constraints, as delivery windows and shipping restrictions create the same failure in a different form. Measure the rate of unavailable impressions as a standing quality metric, which is currently unmeasured and is a direct indicator of how disconnected the two systems are. Handle substitution by promoting an available alternative from the same brand where one exists, which turns a dead placement into a sale. And quantify the lost trip value, because the short-term revenue argument against filtering only survives while the other side of the ledger is unmeasured.

## Who Feels the Pain
Shoppers whose search returns things they cannot buy; brands paying for impressions that cannot convert; and retailers degrading trips to earn a placement fee on nothing.

## Impact If Fixed
Stock position is known precisely by a system in the same company and the auction does not consult it, because the integration went to the catalogue rather than the ledger. Filtering on fulfilling-location availability is one integration that removes the category's most visible quality failure.
