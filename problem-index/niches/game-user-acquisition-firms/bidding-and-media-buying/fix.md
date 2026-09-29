# The Source That Stopped Working at Scale

**Niche:** [[niches/game-user-acquisition-firms/bidding-and-media-buying/profile|Bidding & Media Buying]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The source performed beautifully at a small budget, the team scaled it, and the users arriving at the higher spend were worth far less.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #confidence-intervals #time-series-forecasting #revenue-impact #causal-inference #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to allocate spend across networks whose own optimisers they cannot see, against a predicted value they do not trust — and whoever buys better takes the account.

## The Problem
A source is tested at a modest budget, performs well, and is scaled. At the higher spend the network must reach further into its audience, and the users arriving are systematically worse. Payback falls, the team concludes the source declined, and the real cause — that they passed the point where that source's good audience was exhausted — is never identified. The pattern repeats across sources and is treated as bad luck each time.

## Why It's Still Broken
Nobody measures the saturation curve — a source whose quality is only ever reported as an average across the current spend level cannot reveal that quality falls with volume, and the test result at low spend is assumed to hold. Scaling is done in steps that are too large. The network does not disclose audience depth. And the decline is attributed to the source rather than to the spend level.

## What a Fix Looks Like
Measure quality against spend level, which is data already sitting in the history. Plot cohort quality against daily spend per source, which is the fix and usually shows the knee immediately. Scale in measured steps with a hold at each level rather than doubling, since the curve can only be learned by walking it. Record the spend level alongside every cohort's outcome, which most reporting does not do and which makes the analysis possible at all. Compare the test-level result against the scaled result explicitly rather than treating them as the same source. Identify the spend level at which each source's quality degrades and treat it as a capacity limit. Reallocate above that limit rather than continuing to push a saturated source. Revisit the limit periodically, as audience depth changes with the network and the market. Report source quality by spend band rather than as a single figure. Distinguish saturation from a genuine decline, since the remedies differ entirely. And apply the same analysis to geographies and creatives, where the same effect occurs.

## Who Feels the Pain
UA teams scaling into worse users; publishers whose payback deteriorates as they grow; media buyers blamed for a structural effect; and every budget increase that bought less than the test predicted.

## Impact If Fixed
A source whose quality is only ever reported as an average across current spend cannot reveal that quality falls with volume. Plotting cohort quality against spend level shows the knee in data already held.
