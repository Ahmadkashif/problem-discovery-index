# A Price Per Shot Read From the Plate

**Niche:** [[niches/postproduction-studios/episodic-invisible-effects/profile|Episodic & Invisible Effects]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Boutique vendors price cleanup shots by category, and a "simple screen replacement" can take ten times the category's hours if the camera moves and a hand crosses the screen.
**Tags:** #tacit-knowledge-ml #cnns #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to turn around hundreds of cleanup, screen-replacement and set-extension shots per episode inside a weekly post schedule at a known cost per shot, and whoever prices those shots closest to their real effort keeps the series.

## The Problem
An episodic package arrives with a breakdown: 240 shots, categorised as paint-out, screen replacement, sky replacement, set extension, muzzle flash. The vendor bids a rate per category. The experienced supervisor scans the plates and knows which "simple" shots aren't: the handheld screen replacement with fingers crossing the glass, the sign removal behind moving traffic, the sky replacement through hair. Those shots eat the margin of the whole category.

## Why Nobody Has Built This
Boutiques have neither the data science staff nor the volume to build models, and the plates are client property under strict security rules, so no vendor can pool data with another. The supervisor's scan is fast enough that nobody has tried to capture it.

## What to Build
A plate-reading estimator that runs inside the vendor's secure environment. It takes each breakdown line with its plate, extracts camera motion, occlusion, edge complexity and the area to be replaced, and predicts hours by task with a confidence band, trained on the vendor's own finished shots. It flags shots whose predicted effort is far above their category so the producer can price them separately or exclude them.

## Target Customer
Owners and VFX producers at boutique vendors bidding episodic packages.

## Impact If Built
Pricing the hardest tenth of shots separately instead of averaging them into the category could move an episodic package from break-even to a positive margin (estimate), without raising the rate on the easy shots that win the bid.
