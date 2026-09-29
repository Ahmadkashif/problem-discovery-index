# Seller Onboarding and Listing Quality

**Industry:** [[online-marketplaces|Online Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Listing flows are polished and well tested, and new sellers produce their worst listings during the exact window in which they decide whether the marketplace works for them.
**Tags:** #cnns #bert #gradient-boosting #evaluation-metrics #confidence-intervals #k-nearest-neighbors #worker-facing #revenue-impact

## The Problem
A new seller lists an item. Their photographs are poorly lit and shot against a cluttered background. The title omits the brand. The description assumes context. The category is nearly right. The price is a guess.

The listing performs badly, which is the correct response of a system doing its job on thin data. The seller sees no views and concludes the marketplace has no buyers.

This is the highest-stakes moment in the seller lifecycle. A seller whose first few listings sell becomes a source of supply for years; one whose first listings sit becomes churn. The marketplace knows exactly what distinguishes a listing that will sell from one that will not, and mostly does not tell the seller at the point where it would matter.

Where guidance exists it is generic — best practice articles, tips about lighting — rather than specific feedback on this listing. A seller does not need to know that good photographs matter; they need to know that this photograph is too dark and this title is missing the brand name that eighty per cent of buyers search for in this category.

## What Already Exists
Listing flows are well designed and mobile-optimised at every major marketplace. Image quality assessment is technically mature. Some platforms offer listing quality scores and completeness prompts. Pricing suggestions based on comparable sales exist where comparables exist. Seller education content is abundant. Background removal and image enhancement tools are widely available and sometimes built in.

## The Customisation Gap
Feedback is generic where it needs to be specific. A completeness prompt tells a seller a field is empty; it does not tell them that in this category, listings without this attribute sell at half the rate.

The prediction exists and is not surfaced. The marketplace can estimate a listing's probability of selling from its attributes, images, price and category before it publishes, and can attribute the shortfall to specific fixable causes. That is a straightforward model on abundant data and it is the single most useful thing the platform could tell a new seller.

Pricing guidance fails exactly where it is needed. Comparable-based suggestions work for commodity items and are silent on unique inventory, which is where sellers are least equipped to price and most likely to get it wrong in both directions.

Photography is the highest-leverage fixable input and is treated as the seller's problem. Automated enhancement, background removal and shot-by-shot guidance are available technology and are inconsistently offered.

## Impact If Solved
New seller retention determines supply growth, and it is decided in the first few listings by quality issues the platform can identify and fix before publication. Specific, predictive, category-aware feedback at the point of listing converts a seller's worst work into their adequate work, at the only moment when it changes whether they stay.
