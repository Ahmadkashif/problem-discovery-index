# Conversion Uplift Ranking Trained on Past Conversions

**Niche:** [[niches/outdoor-advertising-companies/digital-billboard-conversions/profile|Digital Billboard Conversions]]
**Industry:** [[industries/outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every large operator has converted hundreds of faces and holds the before-and-after revenue for each one, and none uses that record to rank the next hundred candidates.
**Tags:** #tacit-knowledge-ml #gradient-boosting #causal-inference #cnns #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to pick the static faces whose conversion multiplies revenue rather than adding a little, and that will still clear the permit, and whoever predicts post-conversion yield before the ~$200,000 is spent wins the capital budget.

## The Problem
Conversion candidates are chosen by market managers who know their corridors, then approved on a payback spreadsheet that assumes a revenue multiple. The multiple is the whole question. A face on a congested interstate approach with strong local category demand may earn several times its static revenue as a digital face selling six or eight advertisers; a face in a soft market may add a fraction and pull buyers off the operator's existing digital faces nearby. The operator has run this experiment hundreds of times and has the outcome of each in its billing system.

## Why Nobody Has Built This
The data sits in three places that rarely meet: billing by face, structure and permit records in real estate, and site attributes in nobody's system. Display vendors build ROI tools to sell screens, not to tell an operator not to buy one. And the managers who pick candidates have no reason to invite a model to second-guess them.

## What to Build
An uplift model that, for every static face eligible under its permit, predicts post-conversion revenue relative to its static history and to the market's digital inventory. It is trained on the operator's past conversions with matched unconverted faces as controls. Features: traffic, speed and dwell, read side and angle, imagery-derived read time and obstruction, local advertiser categories, Geopath impressions, existing digital faces within the market and their sell-through. Output: a ranked candidate list with expected uplift, a cannibalisation estimate and the comparable conversions behind each estimate. The manager's own score is captured at approval so the two can be graded later.

## Target Customer
Regional VPs of real estate and digital at operators converting dozens of faces a year; display manufacturers' financing arms as a channel to mid-sized operators.

## Impact If Built
Better conversion choices compound for a decade. Moving even one in ten conversions from a weak face to a strong one shifts millions in revenue per year at a large operator and keeps ~$200,000 of capital per face out of loops the sales team can't fill.
