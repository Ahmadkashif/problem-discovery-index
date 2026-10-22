# Store-Level Shrink Attribution With Uncertainty

**Niche:** [[niches/greeting-card-publishers/scan-based-trading-settlement/profile|Scan-Based Trading Settlement & Shrink]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A publisher on scan-based trading knows its total shrink to the dollar and almost nothing about where it happens or why, so it negotiates the shrink allowance blind.
**Tags:** #bayesian-inference #change-point-detection #hypothesis-testing #gaussian-mixture-models #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche (deduction-recovery and reconciliation vendors, EDI analytics providers and publishers' own settlement teams) is fighting to pin each store's missing cards under scan-based trading to a cause the retailer will accept in settlement, and whoever recovers the most disputed shrink per store takes the publisher's settlement work.

## The Problem
Shrink is computed as shipped minus scanned minus returned, in aggregate, per period. Inside that number are theft, damage, cards scanned under the wrong UPC, shipments never received or never stocked, and miscounted seasonal returns. Each has a different owner (the retailer's loss prevention, the cashier, the receiving dock, the merchandiser, the publisher's own counting) and only some are recoverable in settlement.

## Why Nobody Has Built This
Per store and pocket, the counts are tiny and noisy, and the feeds (shipments, scans, merchandiser counts, returns) arrive at different grains from different systems. Deduction tools work at invoice level. The handful of card publishers big enough to need this have handled it with finance teams and negotiation.

## What to Build
A unit-flow model per store and pocket that estimates expected on-hand from shipments, scans and counts, attributes the gap to likely causes using their signatures (one UPC suddenly selling across many pockets suggests scan substitution; a whole shipment's designs never scanning suggests a stocking failure; steady loss across high-value cards suggests theft), and reports each store's shrink with an interval. Settlement packs cite the evidence per store.

## Target Customer
Retail finance and customer settlement directors at card publishers with large scan-based accounts, and the deduction-recovery firms they hire on contingency, for whom store-level evidence is the difference between a claim the retailer pays and one it rejects.

## Impact If Built
Recoverable shrink is recovered, operational causes are fixed at the store, and the next shrink allowance is negotiated on evidence.
