# Blend Plans Checked Against the Kiln Specification Before the Tank Fills

**Niche:** [[niches/hazardous-waste-firms/cement-kiln-fuel-blending/profile|Fuel Blending for Cement Kilns]]
**Industry:** [[industries/hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A blender commits tank space and intake based on a spreadsheet estimate of what the finished fuel will measure, and learns whether it met the kiln's specification only from the final sample.
**Tags:** #gaussian-processes #bayesian-inference #optimization-fundamentals #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn generators' high-heat-value wastes into fuel that meets a cement kiln's permit and contract specification, and whoever delivers the largest share of blended loads inside the kiln's specification takes the account.

## The Problem
Each intake load is characterised by its profile and a fingerprint sample, both with wide uncertainty. The blender decides which loads go into which tank and when to release a batch, and the batch either meets the kiln's limits or becomes an off-spec problem that costs money to fix or re-route.

## Why Nobody Has Built This
Blending plants are few and mid-sized, the data sits in a LIMS and a spreadsheet, and the experienced blend planner's judgement of which generators' material "runs heavy" has never been written down.

## What to Build
A planner that carries each intake load's specification parameters as a distribution (profile values, fingerprint results and that generator's history), predicts the finished batch's parameters with uncertainty as loads are assigned, and flags assignments likely to push a batch outside the kiln's limits. The planner proposes; the plant's own procedures and sampling decide release.

## Target Customer
Fuel-blending plant managers at independent blenders and consolidators, and kiln alternative-fuels managers who share specifications and acceptance data.

## Impact If Built
Cutting off-spec batches from ~5% to ~2% (estimate) on a plant shipping ~40,000 tons of fuel a year (estimate) avoids ~1,200 tons of rework or re-routing, ~$0.5–1M a year (estimate).
