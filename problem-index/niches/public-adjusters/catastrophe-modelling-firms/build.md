# Fifty Years of Model Runs Against Fifty Years of Actual Losses, Never Compared

**Niche:** [[niches/public-adjusters/catastrophe-modelling-firms/profile|Catastrophe Modelling Firms]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The industry's capital is set by models whose forecasts are never scored against the events that followed, because everyone agrees the sample is too small to score them.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #causal-inference #monte-carlo-methods

## The Problem
A catastrophe model produces an exceedance probability curve: the chance of losing more than a given amount in a year. Insurers hold capital against it, reinsurers price against it, regulators accept rate filings built on it, and catastrophe bond investors trade it.

Then events happen. Hurricanes make landfall, wildfires burn, hailstorms cross cities, and losses are settled. Every one is a realisation from the distribution the model described.

The comparison is not made systematically. There is post-event work — how the modelled footprint compared to the observed one, how estimated industry loss compared to reported — but it is done event by event, largely for client communication, and it is not assembled into a standing record of forecast performance across events, perils, regions and model versions.

The reason offered is that catastrophe is rare and the sample is too small to validate a hundred-year return period. That is true for the tail, and it has been allowed to excuse not validating anything. The body of the distribution — attritional and mid-sized events, which happen constantly — is entirely testable. Severe convective storm alone produces dozens of events a year in the United States and has grown into one of the largest sources of insured loss, and its models are among the least examined.

There is a second, larger gap. The models' vulnerability functions — how much damage a given wind speed does to a given building type — are calibrated on claims contributed by carriers, and the same carriers settle claims through a repair estimating platform and a managed repair network whose data describes exactly what was damaged and what it cost. Vulnerability is the most uncertain component of the model chain, and the richest available evidence about it sits in the claims layer this industry runs on.

## Why Nobody Has Built This
Model credibility is the product, and a published performance record is a hostage. If a model's five-year record shows it under-predicted severe convective storm loss, every client renegotiates, every rate filing built on it is questioned, and every competitor uses it in a sales cycle.

The regulatory and rating agency framework also rewards documented methodology rather than demonstrated accuracy. Model reviews examine scientific basis, assumptions and change documentation. Nobody in that process asks how the previous version performed.

And attribution is genuinely hard. When modelled and actual losses diverge, the cause could be the hazard model, the vulnerability functions, the exposure data the client supplied, demand surge, or claims handling. Untangling that is real work, and the absence of the question has meant nobody funded it.

## What to Build
A standing forecast performance system, treated as a scientific asset rather than a disclosure risk.

**Archive every forecast.** Model version, exposure snapshot, assumptions, and the full output distribution, at the moment of the run. Retrospective reconstruction is impossible; this has to start being recorded.

**Score the body of the distribution.** Frequency and severity of modelled events against observed, by peril and region, over the many mid-sized events that occur every year. Probability integral transforms and proper scoring rules are the standard machinery for grading a probabilistic forecast, and they apply directly.

**Decompose the error.** Separate hazard, vulnerability and exposure contributions to divergence. This is the analytically hard part and the part that actually improves the model, because it says which component to fix.

**Recalibrate vulnerability against claim-level evidence.** Damage ratios by construction type, age and hazard intensity, fitted on settled claim data at line-item resolution rather than on aggregate loss. The estimating and managed repair layers hold this; obtaining it is a commercial negotiation and it is the single largest available improvement to model accuracy.

**Report uncertainty about the model, not just within it.** Clients receive a distribution that expresses event uncertainty and says nothing about how uncertain the distribution itself is. A model with a quantified epistemic error is more useful for capital decisions than one presented as exact, and it is a defensible thing to publish precisely because the alternative — implied precision — is indefensible.

## Target Customer
Chief Research Officer or Chief Science Officer at a catastrophe modelling firm. The strategic argument is that model differentiation is currently a scientific-credibility contest with no scoreboard, and the firm that introduces one on terms it sets is in a much stronger position than the firm that has one imposed after a bad event.

## Impact If Built
Hundreds of billions of dollars of insurance capital and reinsurance pricing rest on these curves, and the systematic biases in them are unmeasured. A validated performance record — with error attributed to hazard, vulnerability or exposure — would improve capital allocation across the entire property insurance system, and it would be the first defensible accuracy claim anyone in the category could make.
