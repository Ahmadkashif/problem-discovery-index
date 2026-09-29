# Yield Attribution and On-Farm Trial Design

**Industry:** [[agtech-platforms|Agtech Platforms]]
**Type:** High Impact
**One-liner:** Turn the instrumented field into a running experiment — randomised strips written into the prescription, yield measured at harvest, effects estimated per farm — so a grower learns what actually works on their own ground instead of what worked at a research plot in another state.
**Tags:** #causal-inference #hypothesis-testing #gradient-boosting #confidence-intervals #feature-engineering #evaluation-metrics #bayesian-inference #revenue-impact

## The Problem
A grower makes input decisions every season that commit a large share of the operation's working capital: seed variety and population, fertility programme and nitrogen rate, seed treatments, fungicide and its timing, growth regulators. Each is a real cost against an uncertain return.

The evidence base for those decisions is remarkably thin. Manufacturer trials run on research farms in conditions that may not resemble this field. Retailer plot trials are small, unreplicated and rarely blind. A neighbour's experience is one observation with no counterfactual. University extension trials are the best of it and are few, dated and geographically sparse.

Meanwhile the equipment in the field is capable of running a proper experiment without anyone getting out of the cab. A planter with section control can vary population by strip. A rate controller can vary nitrogen. A sprayer can leave check strips. The combine measures yield continuously with position. The prescription file that tells the machine what to do is written on a computer before the pass begins.

Every ingredient of a randomised trial is present — treatment assignment, blinding by geography, replication across strips, and precise outcome measurement — and it is almost never assembled. Prescriptions are written to apply the agronomist's recommendation uniformly, the yield map is looked at as a picture, and the season ends with no more evidence than it started with.

## Why It's Unsolved
Nobody's incentive points at it. Input manufacturers fund the trials and have no interest in a grower discovering that a product did nothing on their ground. Retailers sell the products and provide the agronomy, which is a conflict everyone understands and tolerates. Platform vendors are frequently owned by or partnered with input companies. The grower would benefit and has neither the statistical training nor the time.

There are real technical obstacles too, and they are the interesting part. Yield monitor data is noisy in specific ways — flow delay through the combine, header width errors, moisture calibration drift, operator behaviour at headlands — and comparing strips without correcting for these produces confident nonsense. Soil variation within a field is often larger than the treatment effect, which is exactly why randomisation and blocking matter and exactly why casual side-by-side comparisons mislead.

And the effect sizes are genuinely small. A treatment worth having might move yield a few per cent, which requires more replication than a single field-season provides — meaning the analysis has to pool across seasons and across farms, which requires the platform rather than the grower.

## What a Solution Looks Like
Trial design built into prescription writing. When a grower is deciding whether a product is worth it, the platform proposes a strip trial — randomised, replicated, blocked on the soil variation it already knows about — and writes it into the prescription file. The machine executes it as a normal pass.

At harvest, yield data is cleaned properly: flow delay corrected, headland passes excluded, moisture normalised, edge effects removed. Then the treatment effect is estimated with an honest interval, and the answer is reported in the only unit that matters — return per acre, given this year's input and grain prices, on this farm.

Pooling is what makes small effects detectable. One farm's single-season trial is underpowered; five hundred farms running comparable trials is a proper multi-environment experiment, and it also reveals where an effect holds and where it does not, which is the question a grower is actually asking.

## Impact If Solved
Input spend is one of the largest controllable costs in row crop agriculture and is committed annually against evidence that is thin, conflicted and often irrelevant to the specific field. Giving growers real evidence from their own ground — and a pooled evidence base across comparable operations — is the largest available improvement to farm profitability, and it uses machinery that is already in the field doing the work anyway.
