# Exception-Only Review

**Niche:** [[niches/portrait-photography-studios/culling-editing-retouching/profile|Culling, Editing & Retouching]]
**Industry:** [[industries/portrait-photography-studios|Portrait Photography Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** AI tools already cull and edit a wedding in minutes; what nobody provides is an honest list of the fifty decisions the photographer should actually look at.
**Tags:** #cnns #transfer-learning #evaluation-metrics #semantic-segmentation #worker-facing #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to reproduce a photographer's own culling and editing choices on a 2,000–5,000-frame wedding closely enough that the photographer stops checking every frame, and whoever earns that trust takes the subscription.

## The Problem
Photographers using AI culling still scroll every frame, because they don't know which of the model's choices to trust. The time saved in processing is spent again in review.

## Why Nobody Has Built This
Vendors compete on headline accuracy and speed, not on calibration, and admitting uncertainty looks like weakness in a demo. Calibration also needs the photographer's corrections fed back per wedding, which most tools collect only loosely.

## What to Build
Per-photographer models whose confidence is calibrated on that photographer's own corrections: an exception list ranked by expected disagreement (borderline duplicates, key moments with soft focus, unusual light where the edit profile is unreliable, faces flagged for retouch), with everything else auto-accepted. Each correction updates the profile and the calibration, and the tool reports the photographer's real touch rate over time.

## Target Customer
Wedding and portrait photographers delivering roughly 20–40 weddings or 100+ sessions a year (estimate).

## Impact If Built
Review shrinks from every frame to a short list, turning a week of post-production into an afternoon and making delivery in days possible.
