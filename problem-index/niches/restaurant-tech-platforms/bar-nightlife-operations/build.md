# Variance Attributed to Product, Shift and Station

**Niche:** [[niches/restaurant-tech-platforms/bar-nightlife-operations/profile|Bar & Nightlife Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every bar knows its beverage variance is somewhere in the double digits and no bar knows how it splits between over-pouring, unrung drinks, spillage and comps, because the count is weekly and the attribution is nonexistent.
**Tags:** #bayesian-inference #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics #descriptive-statistics #revenue-impact #change-point-detection
**Contested on:** Every serious competitor in beverage operations software is fighting to reconcile what was poured against what was sold, at a granularity and a cost that a bar will actually sustain — and whoever closes that variance takes the account.

## The Problem
The weekly count says the bar depleted the equivalent of $18,400 of product and rang $15,900 against it. The owner knows there is a problem and has no way to act on it. Was it the Friday night bartender pouring heavily, a well spirit consistently over-poured by everyone, unrung drinks at the service station, or a case that never arrived? Each explanation implies a different response and the data cannot distinguish them, so the response is a general speech to staff that changes the number for two weeks. This is the permanent condition of the segment.

## Why Nobody Has Built This
The measurement cadence is the constraint: a weekly count produces one observation per product per week, which cannot support attribution to shift or station no matter what is done with it. Increasing the cadence means counting more often, which nobody will do, or instrumenting pours, which means hardware on every bottle with real cost and maintenance. Vendors have therefore optimised the count rather than changing what is being measured. There is also a social dimension that products have handled clumsily: any attribution of variance to shifts and stations is an accusation aimed at named people, and a product that generates those accusations carelessly will be sabotaged by the staff it monitors.

## What to Build
Attribution from the data that already exists, treated properly as a statistical problem. Weekly depletion by product, combined with sales by product by shift and by station, supports an inference about where the loss is concentrated — not with certainty from one week, but with accumulating confidence over months, which is exactly what a hierarchical model is for. Estimate a pour-size factor per product per station and per shift pattern, with intervals, and report only what the data actually supports rather than ranking bartenders on noise. Where hardware exists — draft flow meters are cheap and well-established for beer — use it to anchor the estimates for those products and let the inference for spirits borrow structure from the anchored ones. Present findings as patterns to investigate with the uncertainty visible, and be explicit that a wide interval on one bartender is not evidence about that person.

## Target Customer
Bar groups and beverage-led restaurant groups with multiple stations or locations, and the beverage inventory vendors who currently deliver a variance percentage and stop.

## Impact If Built
Beverage variance at the scale most bars carry is one of the largest recoverable cost items in hospitality, and attribution is the whole difference between knowing there is a problem and fixing one. Closing even part of the gap on a high-margin category moves a bar's profitability more than any labour or food improvement available to it.
