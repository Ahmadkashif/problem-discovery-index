# Catastrophe-Model Data Quality Scoring Run During Collection

**Niche:** [[niches/self-insured-benefit-pools/member-property-schedules/profile|Member Property Schedules & Reinsurance Submissions]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Brokers score a statement of values for catastrophe-model completeness after the pool submits it, when it is too late to fix.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver a complete, current, reinsurer-grade schedule of every member's buildings, contents, vehicles and infrastructure before the property renewal, and whoever's schedule draws the fewest valuation loadings and exclusions from property reinsurers takes the account.

## The Problem
Reinsurers and brokers run the pool's schedule through catastrophe models that need construction, occupancy, year built, roof and stories. Missing fields trigger conservative defaults and higher prices.

## What Already Exists
Brokers' and modelling vendors' data-quality scoring and geocoding tools for property schedules, used on submission files.

## The Customization Gap
Pools need the same scoring run member by member and line by line during collection, with plain-language prompts a town clerk can answer ("what is the roof made of?"), public-occupancy codes mapped to model codes, and a running pool-level completeness score that shows which members to chase before the renewal deadline.

## Target Customer
Pool underwriting managers and the reinsurance brokers who prepare their submissions.

## Impact If Solved
A complete schedule at submission, and fewer default assumptions inflating property reinsurance cost.
