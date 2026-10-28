# The Catalog Says "Dealer Only"

**Niche:** [[niches/auto-parts-distributors/ev-hybrid-parts-supply/profile|EV & Hybrid Repair Parts Supply]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Fix (Pain Point)
**One-liner:** When a hybrid or EV lookup finds nothing, the counter says "dealer only" and the request vanishes, so suppliers never see the demand they could fill.
**Tags:** #large-language-models #k-nearest-neighbors #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to supply the parts independent shops need to keep hybrids and EVs out of the dealer, and whoever fills the largest share of hybrid and EV repair-part requests from aftermarket stock takes the account.

## The Problem
Lookup screens record sales, not misses. A hybrid inverter pump request that finds no aftermarket listing ends with a shrug, and the shop buys from the dealer. Across thousands of stores those misses are the clearest signal of which EV and hybrid parts the aftermarket should develop, and they are discarded.

## Why It's Still Broken
Business systems have no field for a lost lookup, counters are too busy to log one, and suppliers rely on dealer sales data they cannot see.

## What a Fix Looks Like
Log every lookup that returns no candidate or ends without a sale, with the decoded vehicle and the part type requested; aggregate misses by configuration and region; share the anonymised totals with suppliers and programme groups as a monthly "uncovered demand" list. A cross-reference step checks whether an existing part from another application would fit.

## Who Feels the Pain
Counter staff turning shops away; shops sending customers back to the dealer; suppliers guessing which lines to build.

## Impact If Fixed
If logged misses led suppliers to cover ~20 high-demand EV and hybrid applications a year sooner (estimate), distributors would capture repairs worth several million dollars a year that now go to dealers.
