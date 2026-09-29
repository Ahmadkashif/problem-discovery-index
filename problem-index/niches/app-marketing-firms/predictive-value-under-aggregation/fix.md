# Nulled Out Exactly Where It Matters

**Niche:** [[niches/app-marketing-firms/predictive-value-under-aggregation/profile|Predictive Value Under Aggregation]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The privacy threshold nulls the campaign identifier when volume is low, which is precisely the condition of every new campaign, so the signal disappears exactly when a decision is being made.
**Tags:** #confidence-intervals #bayesian-inference #evaluation-metrics #hypothesis-testing #monte-carlo-methods #quick-win #descriptive-statistics #revenue-impact
**Contested on:** This niche is not terminal — designing what the bits encode and predicting value from them are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A new campaign launches at modest volume to test it. Because the volume is low, the privacy threshold suppresses the campaign identifier in the returning signal, so the team receives postbacks they cannot attribute to the campaign. They cannot tell whether it is working. The standard response is to spend more to clear the threshold, which means committing budget precisely to the campaigns they know least about. The suppression is not random — it is systematically concentrated on new, small and experimental activity, which is the population every allocation decision most needs information about.

## Why It's Still Broken
Suppression is handled as missing data rather than as a knowable mechanism, which discards the fact that it is triggered by an observable condition — the missingness is deterministic in volume and is treated as though it were random. Teams respond by spending to clear the threshold, which works and is expensive, so the workaround prevents the fix. The bias in what survives suppression is rarely quantified. And it affects new campaigns, whose failure is attributed to the campaign.

## What a Fix Looks Like
Model the suppression rather than absorbing it. Treat suppression as informative, since a nulled postback tells you the campaign was below the threshold, which is itself information and is currently thrown away. Estimate what the suppressed population is worth by borrowing from comparable campaigns, which is a hierarchical estimate and is the honest alternative to no information at all. Design campaign structure to manage threshold exposure deliberately — consolidating where it helps and accepting suppression where the information is not worth the concentration — which is a planning decision nobody frames explicitly. Report the share of spend whose signal is suppressed, which most teams have never computed and which frequently turns out to be a large share of their experimental budget. Quantify the bias in the surviving data, since decisions are being made on a non-random subset and nobody states the direction. Use alternative signals for the suppressed population, including on-device measurement where permitted and aggregate modelling. Stage new campaigns to reach a threshold quickly where the test justifies it, and where it does not, plan to learn differently. Warn before launching a campaign whose structure guarantees suppression, which is a check nobody runs. Combine suppressed and unsuppressed evidence with appropriate weights rather than ignoring one. And measure the cost of the workaround, because spending to clear a threshold is a real budget line that exists purely to obtain information.

## Who Feels the Pain
Teams spending to buy visibility rather than results; new campaigns judged on absent evidence; and smaller advertisers for whom suppression is the permanent condition rather than an early-stage one.

## Impact If Fixed
The missingness is deterministic in volume and is treated as though it were random, which discards the information a nulled postback carries. Hierarchical borrowing from comparable campaigns is the honest alternative to spending budget purely to clear a threshold.
