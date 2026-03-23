# Shop-Side Photo Damage Assessment with Repair Scope Prediction

**Niche:** [[niches/auto-body-shops/photo-based-estimating/profile|Photo-Based Damage Estimating]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No shop-facing AI tool assesses collision damage from photos and predicts full repair scope including likely hidden damage — the insurer-side tools (Tractable, Solera) are designed to minimize estimates, not ensure complete repair.
**Tags:** #cnn #semantic-segmentation #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
When a customer sends photos of collision damage for a remote estimate, an experienced estimator can identify: the bumper cover needs replacement (the crack pattern indicates stress beyond repair), the headlight bracket is likely broken (the headlight is sitting 3mm low), and the fender will need R&R plus paint (the crease line extends past the crown of the panel). A junior estimator sees "bumper is cracked, headlight looks okay, fender has a dent" and writes an estimate $1,500-$3,000 below the actual repair cost. This visual damage assessment from photos is tacit knowledge — the experienced estimator reads subtle cues (panel gaps, reflection line breaks, paint stress marks) that are invisible to the untrained eye.

## Why Nobody Has Built This
Insurer-side AI tools (Tractable, Solera's AI) are designed to generate the lowest defensible estimate from customer photos — they serve the insurer, not the shop. Building a shop-side tool requires training on the full repair scope (not the minimized insurer estimate) as ground truth. This data lives in shop repair files: the final repair cost (after supplements) correlated with the initial damage photos. No one has aggregated this shop-side dataset because shops don't share repair data across their competitive networks.

## What to Build
A shop-facing damage assessment AI that analyzes customer-submitted or shop-taken photos and generates a repair scope estimate that includes: (1) visible damage with repair vs. replace recommendations, (2) predicted hidden damage based on impact pattern analysis, (3) required adjacent panel operations (blend, R&I), and (4) total estimated repair cost range. The model is trained on shop-final repair costs, not insurer initial estimates, so it reflects actual repair scope rather than minimized payouts.

## Target Customer
Body shop estimators who process 10-30 photo-based estimates per week and want to provide accurate quotes without the vehicle being on-site.

## Impact If Built
Increases photo-based estimate accuracy from 60-70% to 85-90% of final repair cost, reducing supplement cycles and improving customer experience. Enables shops to provide reliable remote estimates, capturing customers earlier in the repair decision process and increasing close rates by 20-30%.
