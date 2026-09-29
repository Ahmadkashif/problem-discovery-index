# Separating the Player From the Game

**Niche:** [[niches/game-user-acquisition-firms/player-content-decomposition/profile|Player-Content Decomposition]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lifetime value is treated as a property of the player and is mostly a property of what the game shipped afterwards.
**Tags:** #causal-inference #bayesian-linear-regression #confidence-intervals #evaluation-metrics #hypothesis-testing #time-series-forecasting #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to separate what a cohort was worth from what the game did to it afterwards — and whoever separates them takes the account.

## The Problem
A cohort acquired in March and a cohort acquired in September may be identical in composition and realise very different value, because the content between March and September was better. UA is held to the payback number for both. The entire discipline is organised around a quantity it is measured on and only partly controls, and no evidence exists to apportion it — so the argument between UA and product is conducted entirely on assertion.

## Why Nobody Has Built This
It requires joining UA cohort data to the product organisation's release history, which no one owns. The decomposition implies changing what each function is accountable for, which both may resist. Neither side has the evidence to propose it. And the discipline's whole vocabulary treats lifetime value as a player attribute.

## What to Build
Decompose the realised value across cohorts and content periods. Model realised cohort value as a function of cohort composition and the content the cohort encountered, which is the core and is estimable because many comparable cohorts have met many different content cadences. Join UA cohort records to the product release, event and monetisation history, which is the integration that makes everything possible. Estimate a content effect per period so a cohort's outcome can be adjusted for what it met, since that adjusted number is what UA should actually be measured on. Identify which content types move cohort value most, which is a direct input to product investment decisions. Hold cohort composition constant when comparing content periods, and vice versa, which is the whole point of the decomposition. Report the uncertainty honestly, as the two effects are partly confounded and overclaiming would destroy the exercise. Make the output usable by both functions rather than by UA alone, because the value comes from ending an argument rather than winning it. Forecast the content dependency into payback projections instead of assuming a flat future. Feed it back into what UA is measured on, which is the organisational change the evidence enables. And present it as shared measurement rather than as apportioning blame.

## Target Customer
UA leadership and product leadership jointly, mobile publishers, portfolio management functions, and analytics and measurement vendors.

## Impact If Built
The discipline is measured on a quantity it only partly controls, and no evidence exists to apportion it. Decomposing realised cohort value into composition and content effects is estimable and would end an argument conducted entirely on assertion.
