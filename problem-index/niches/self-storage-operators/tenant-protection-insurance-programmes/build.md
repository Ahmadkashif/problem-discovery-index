# Facility-Level Loss Pricing for Protection Plans

**Niche:** [[niches/self-storage-operators/tenant-protection-insurance-programmes/profile|Tenant Protection & Tenant Insurance Programmes]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Protection plans are priced the same at a gated, camera-covered climate-controlled building and at an open drive-up lot in a flood zone, though their losses differ several-fold.
**Tags:** #gradient-boosting #survival-analysis #bayesian-inference #feature-engineering #evaluation-metrics #revenue-impact #compliance
**Contested on:** Every serious competitor in this niche is fighting to attach tenant protection or tenant insurance at move-in under each state's insurance rules, and whoever earns the most protection margin per occupied unit takes the account.

## The Problem
An operator running its own protection plan sets one price per coverage tier, $10 a month for $2,500 in the case California's court reviewed, across every store. Losses come mostly from burglary, water and weather. These depend on the building (interior hallways or drive-up), the access system (individual smart locks or a shared gate), the roof and drainage, and the neighbourhood. The operator carries those losses on its own balance sheet, store by store, without a model of them.

## Why Nobody Has Built This
Insurance-licensed programmes price through state rate filings, which move slowly. Operator-run plans are priced by marketing, not actuaries. Claims records sit with administrators, and access and facility data sit with the operator. Nobody joins them.

## What to Build
A loss model per facility and unit type. It joins claims history (cause, amount, date) to building attributes, access-control type, smart-lock events, local crime and flood exposure, and to the unit's size and coverage level. A Bayesian hierarchical model pools small stores toward their region, and a frequency-severity model sets the expected loss per occupied unit. The output is a price or coverage recommendation per store for operator-run plans, and loss evidence for the rate filings insurance programmes must make. It also flags stores where a security upgrade pays for itself in avoided claims.

## Target Customer
VPs of ancillary revenue at operators running their own protection plans; programme heads at administrators such as Storable Insurance, MiniCo and SBOA.

## Impact If Built
At ~60% attachment and ~$12 a month (estimate), protection earns ~$43,000 a year at a 500-unit store. Moving loss ratios at the worst 10% of stores from ~40% to ~25% (estimate) adds ~$6,000 a store a year there. Pricing the safest stores more keenly could also lift attachment.
