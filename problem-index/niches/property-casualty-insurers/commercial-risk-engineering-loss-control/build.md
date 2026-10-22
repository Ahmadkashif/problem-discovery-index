# Recommendations Graded Against Later Losses

**Niche:** [[niches/property-casualty-insurers/commercial-risk-engineering-loss-control/profile|Commercial Risk Engineering & Loss Control]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers issue thousands of loss control recommendations a year and cannot say which ones, when completed, actually reduce losses.
**Tags:** #tacit-knowledge-ml #causal-inference #survival-analysis #large-language-models #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a field engineer's survey into recommendation-level risk data an underwriter will price on, and whoever can show that completed recommendations lower loss takes the account.

## The Problem
An engineer recommends sprinkler upgrades, a hot-work permit system, a fleet camera programme, guarding on a press. Some are completed, some ignored, some waived at renewal to keep the account. The carrier holds every recommendation and every subsequent claim, but the two are never joined, so it cannot tell insureds, underwriters or its own engineers which recommendations are worth insisting on. Senior engineers have strong views about which hazards really drive losses. Those views are tacit and vary from engineer to engineer.

## Why Nobody Has Built This
Recommendations are prose in reports, completion status is unreliable, and losses are rare per account, so the analysis needs a large book, careful matching and patience. Survey firms see the reports but not the losses; underwriters see the losses but not the recommendations.

## What to Build
Extract every historical recommendation into a coded hazard and control taxonomy. Join it to completion records and to subsequent claim frequency and severity, and estimate each control's effect with matched comparisons that adjust for which insureds choose to comply. Feed the results back as a ranked list of recommendations with evidence, and capture senior engineers' hazard judgements so they can be tested.

## Target Customer
Heads of risk engineering and commercial chief underwriting officers at middle-market and large commercial carriers.

## Impact If Built
Engineers spend visits on the controls that matter, underwriters price compliance with evidence, and insureds get recommendations they can be persuaded to complete.
