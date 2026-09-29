# Vendor Scorecard Practice

**Niche:** [[niches/dropshipping-suppliers/supplier-selection-and-reliability/profile|Supplier Selection & Reliability Signals]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise procurement has decades of supplier performance management with scorecards, corrective action and qualification tiers, and dropshipping uses consumer star ratings.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #compliance #workflow-orchestration #gradient-boosting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell a merchant whether a specific supplier will actually perform on a specific product before they commit their storefront to it — and whoever produces a signal that predicts downstream outcomes replaces the star rating the whole category runs on.

## The Problem
Large buyers have a mature discipline for exactly this question. Supplier scorecards measure on-time-in-full delivery, quality acceptance, responsiveness and corrective action closure; suppliers sit in qualification tiers with defined entry and exit criteria; performance reviews are periodic and evidenced; and poor performers are put on improvement plans before being removed. Dropshipping platforms have the same relationship at far higher volume with far better instrumentation, and manage it with a five-star average computed from voluntary reviews.

## What Already Exists
Supplier performance scorecards with weighted metric frameworks; on-time-in-full measurement; qualification and tiering schemes; corrective action and improvement plan workflow; and supplier risk monitoring.

## The Customization Gap
The adaptation is from a procurement team managing dozens of suppliers to a platform intermediating thousands for merchants who have no leverage. It requires: (1) scoring computed entirely from observed transaction data rather than from buyer-submitted assessments, since there is no procurement team to fill in a scorecard — this is both the constraint and the advantage, because the platform observes more than any buyer ever could; (2) per-merchant relevance, as the merchant cares about their products and destinations rather than the supplier's aggregate; (3) tiering that gates what a supplier may be listed for rather than producing a review meeting, since the enforcement mechanism is listing eligibility rather than a contract; (4) statistical care at low volumes, because most supplier-product-destination cells are sparse and procurement practice assumes enough volume to ignore this; and (5) a corrective action loop that works without a commercial relationship, which is the genuinely missing piece and the reason bad suppliers simply persist.

## Target Customer
Dropshipping and sourcing platforms, ecommerce aggregators, and supplier management vendors for whom high-volume intermediated supply is unserved.

## Impact If Solved
Procurement scorecards assume a team that fills them in, and the platform observes more than any buyer could without asking anyone. Listing eligibility replaces the contract as the enforcement mechanism, and sparse supplier-product-destination cells need statistical care procurement practice never had to apply.
