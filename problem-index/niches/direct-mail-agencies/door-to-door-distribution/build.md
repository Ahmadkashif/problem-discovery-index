# Per-Door Coverage Verification

**Niche:** [[niches/direct-mail-agencies/door-to-door-distribution/profile|Door-to-Door & Door-Hanger Distribution]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Distributors prove that a walker was in the neighbourhood; clients are paying for proof that each door got a piece.
**Tags:** #hidden-markov-models #dbscan #cnns #object-detection #evaluation-metrics #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to prove to the client that every paid door got the piece — coverage evidenced street by street, with dumped bundles caught before the client finds them — and whoever sells verified doors rather than walked routes takes the account.

## The Problem
A pizza franchise buys 20,000 doors at a price per door. The distributor sends a map of GPS dots and a few photos. When one route's coupons never come back, the client asks whether it was walked; the distributor can show the walker was on the street but not which doors received hangers, and refunds or argues.

## Why Nobody Has Built This
Phone GPS is too noisy to resolve individual doors on its own, address-point data is uneven, and distributors are small firms without engineering teams. The national networks subcontract, so the data sits with dozens of local crews.

## What to Build
A coverage engine that map-matches walker traces to street segments and address points, models which side of the street was worked from pace and stop pattern, flags dwell clusters away from doors (dumping) and impossible speeds (driving), checks verification photos for a hanger on a door, and reports per-door status as covered, legitimately excluded or missed — live to crew leaders and as a proof report to the client.

## Target Customer
Distribution firm owners and national network operators; franchise local-marketing managers who buy door-to-door at scale.

## Impact If Built
Verified coverage lets distributors re-walk gaps the same day, price on delivered doors, and win clients who currently prefer EDDM only because a postage statement feels like proof.
