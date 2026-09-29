# Segments From Three Numbers

**Niche:** [[niches/d2c-brand-operators/first-party-customer-corpus/profile|First-Party Customer Corpus]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Customer segmentation in this category is recency, frequency and monetary value in buckets, a technique from the era of postal catalogues, applied to a dataset that contains far more.
**Tags:** #k-means-clustering #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #quick-win #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to turn the one dataset the advertising platforms do not have into predictions the brand can act on — and whoever does that takes the advantage, because it is the only asymmetry a small brand holds against a platform.

## The Problem
A brand's messaging platform offers segments built on how recently a customer bought, how often, and how much they spent. Those three numbers were the state of the art when the input was a mail-order card file, and they are what almost every brand in this category uses. The customer record also contains what they bought, in what sequence, what they returned, what they contacted support about, which channel acquired them, what they browsed and what they ignored. All of it predicts behaviour better than three summary statistics, and the segmentation ignores every bit of it.

## Why It's Still Broken
The three-number segmentation is built into the messaging tools, requires no work, and produces segments that are visibly sensible, which makes it feel adequate. Richer segmentation requires modelling, which requires somebody to do it. The segments are also interpretable, which is genuinely valuable and is used to justify not replacing them. And nobody has demonstrated the gap, because that would require running both.

## What a Fix Looks Like
Use the rest of the record. Add product and category history to the segmentation, since what somebody bought predicts what they will buy far better than how much they spent — this is the largest and easiest improvement and requires no new data. Replace bucketed recency with a modelled probability of being active, which the buy-till-you-die models supply and which is a strictly better version of the same idea. Include returns and support history, since a customer with a poor experience needs a different treatment and is currently indistinguishable from a happy one. Segment by predicted behaviour rather than by past behaviour, because the decision is about the future and the three numbers describe the past. Keep interpretability by naming and describing the resulting segments rather than by restricting the inputs, which is how the interpretability objection is actually answered. Measure the improvement by running the old and new segmentation against each other, since the gap is demonstrable in a single campaign and is what justifies the change. Push the richer segments into the ad platforms as well as the messaging tool, so acquisition benefits too. And update them continuously, since a segment computed quarterly is stale for exactly the customers whose state changed.

## Who Feels the Pain
Brands sending irrelevant messages to customers whose preferences are in their own database; customers receiving them; and retention teams whose targeting options are a technique older than the internet.

## Impact If Fixed
Product and category history predicts far better than three summary statistics and requires no new data, which makes it the largest easy improvement available. Naming the resulting segments answers the interpretability objection without restricting the inputs.
