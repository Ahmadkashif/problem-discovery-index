# The Territory That Loses Money and Nobody Knows Which

**Niche:** [[niches/field-service-software/rural-service-territories/profile|Rural & Long-Drive Service Territories]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** A rural service business serves a wide area at one price and has never computed profitability by geography, so it does not know which parts of its territory pay for themselves and which are carried by the rest.
**Tags:** #descriptive-statistics #linear-regression #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #automation #quick-win
**Contested on:** Every serious competitor selling into low-density territories is fighting to make a day of service profitable when half of it is spent driving — and whoever raises revenue per drive hour most takes the account.

## The Problem
An owner knows that the far end of the county is a nuisance and serves it anyway, out of obligation, habit and a belief that the work contributes something. Whether it does is unknown, because revenue is tracked by job and cost is tracked by period, and nothing allocates drive time, fuel, vehicle wear and the opportunity cost of a consumed day to the geography that consumed them. When the business is under pressure the owner responds by raising prices everywhere or working longer, because the specific answer — this area loses money at current pricing and this one is the best work we do — has never been computed.

## Why It's Still Broken
Job costing in these products stops at labour and parts, and drive time is either untracked or recorded as an undifferentiated cost of doing business. Allocating it requires joining dispatch records, vehicle telematics or timestamps, and revenue by job — all present, none joined. And there is a reluctance specific to small communities: an owner who discovers that a whole area is unprofitable has to decide whether to stop serving neighbours, which is a decision people would rather not be forced into by a spreadsheet.

## What a Fix Looks Like
Allocate the full cost of a visit, including travel, and report by geography. Drive time per job is computable from dispatch timestamps or from vehicle data; fuel and vehicle cost per mile is a known rate; the opportunity cost of consumed capacity can be expressed as revenue per available hour. Report contribution per job and aggregate it by area, customer type and service line, with enough granularity to see that the problem is a specific corridor rather than a whole direction. Then present the levers rather than the verdict: this area works if jobs are batched into planned trips, or if a travel charge is applied, or if it is served monthly instead of on demand. Most owners, given the number, choose a change in how they serve an area rather than abandoning it — which is why the measurement is useful rather than brutal.

## Who Feels the Pain
Owners working longer to fix a margin problem they cannot locate; technicians driving routes that consume their day for little return; and distant customers whose service is quietly deteriorating because serving them is unrewarding.

## Impact If Fixed
Geographic contribution analysis is arithmetic on data the business already has and typically identifies a minority of the territory consuming a disproportionate share of capacity. The usual outcome is a change in how that area is served rather than an exit, which keeps the customers and recovers the capacity — an option the owner could not see without the number.
