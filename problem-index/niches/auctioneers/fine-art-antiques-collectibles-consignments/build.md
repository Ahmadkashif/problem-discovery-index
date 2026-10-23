# An Estimate and Attribution Record Graded by the Hammer

**Niche:** [[niches/auctioneers/fine-art-antiques-collectibles-consignments/profile|Fine Art, Antiques & Collectibles Consignments]]
**Industry:** [[industries/auctioneers|Auctioneers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A specialist house publishes an estimate for every lot and a hammer for every sale, and does not keep a calibrated scorecard of which specialists, categories and estimate levels it gets right.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #causal-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to persuade a consignor that it will put a valuable piece in front of the bidders who will pay most for it, and whoever's attribution and estimate are confirmed by the hammer, rather than undercut by a passed lot or a post-sale re-attribution, takes the account.

## The Problem
Specialists set estimates to win consignments and to attract bidders. Too high and the lot passes, damaging the piece's marketability for years; too low and the consignor feels misled, even if the hammer is strong. Attributions ("attributed to", "circle of", "after") carry the largest price effects and the greatest risk of later challenge. The house holds every estimate, attribution and hammer it has ever published but uses them for comparables, not for grading itself.

## Why Nobody Has Built This
Specialists resist being scored, the passed lots that carry the clearest signal are excluded from most analyses, and estimates double as marketing. Academic studies have measured bias at the global houses; nobody sells the measurement to the houses themselves.

## What to Build
A scorecard from the house's archive: estimate calibration by specialist, category and price band, with passed lots treated as censored outcomes; time-to-resale and re-offer outcomes for passed pieces; attribution-level price effects and challenge rates; and a pre-sale check that flags estimates far from the model's range.

## Target Customer
Heads of specialist departments and owners of regional fine art and collectibles houses competing for consignments against larger rivals.

## Impact If Built
Estimates consignors can trust because the house can show its record, fewer passed lots, and evidence to win consignments without overpromising.
