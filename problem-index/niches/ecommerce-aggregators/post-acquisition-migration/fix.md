# The Stock Gap Nobody Planned For

**Niche:** [[niches/ecommerce-aggregators/post-acquisition-migration/profile|Post-Acquisition Migration]]
**Industry:** [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** Fix (Pain Point)
**One-liner:** Moving fulfilment from the seller's arrangement to the acquirer's creates a period where stock is in transit and listings go unavailable, and a marketplace treats unavailability as a reason to stop showing a listing.
**Tags:** #workflow-orchestration #time-series-forecasting #evaluation-metrics #revenue-impact #confidence-intervals #automation #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to move a brand onto the acquirer's infrastructure without disturbing the ranking it was bought for — and whoever does that keeps the asset, because the migration is a predictable, self-inflicted loss the sector treats as routine.

## The Problem
Stock is transferred from the seller's fulfilment arrangement to the acquirer's. For five days the units are in transit and the listings show as unavailable. The marketplace stops displaying them, the organic position lapses, competitors take the position, and when stock arrives the listings restart from a worse rank with no sales velocity. Recovering the position takes months of advertising spend and sometimes never fully happens. The gap was entirely predictable from the transfer plan, the remedy is holding a buffer or staging the transfer, and it is the most avoidable damage in the whole model.

## Why It's Still Broken
The transfer is a logistics task planned by people whose success criterion is the stock arriving, not the listing staying live. The ranking consequence of unavailability is known to marketplace operators and not to logistics planners. Holding a buffer costs working capital at a moment when the acquirer has just spent heavily. And the damage appears weeks later as a ranking decline attributed to the migration in general.

## What a Fix Looks Like
Never let the listing go unavailable. Stage the transfer so a portion of stock moves first and the remainder covers sales until the new location is live, which is the fix, costs a little working capital and inventory handling, and prevents the single most avoidable loss in the model. Forecast the gap explicitly from the transfer plan and the sales rate, so the required buffer is a calculation rather than a hope. Keep the original fulfilment arrangement live in parallel where the seller will cooperate, which is frequently negotiable as part of the transaction and is cheap. Move high-velocity listings last and separately, since the damage concentrates in the listings that matter most. Monitor availability daily through the transition with an immediate escalation, because a listing that goes unavailable for a day is recoverable and one that goes for a week is not. Build stock continuity into the purchase agreement as a seller obligation, which costs nothing and is easier to agree before completion than after. Report availability days lost per migration as the operational metric. And forecast the recovery cost, so the decision to save on the buffer is made against the advertising spend it will require.

## Who Feels the Pain
Acquirers whose newly bought ranking lapses during their own transfer; operations teams blamed for a decline caused by a logistics plan; and investors whose acquisition case assumed continuity.

## Impact If Fixed
The gap is predictable from the transfer plan and the remedy is a staged move with a buffer. Moving high-velocity listings last concentrates the protection where the damage would be worst, and a stock continuity obligation costs nothing if agreed before completion.
