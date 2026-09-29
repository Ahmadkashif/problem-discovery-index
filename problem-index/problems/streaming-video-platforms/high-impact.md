# No Title Has a Price

**Industry:** [[streaming-video-platforms|Streaming Video Platforms]]
**Type:** High Impact
**One-liner:** A platform spends billions a year on content and cannot say what any individual title contributed in subscribers, so it substitutes hours viewed, which measures consumption rather than cause.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
A platform commissions a series for two hundred million dollars. It launches. Over the following months the platform observes hours viewed, completion rates, the proportion of subscribers who watched, and the signups that occurred during the launch window.

None of that is the number the decision required. The question is how many subscribers joined because of this title and would not otherwise have joined, and how many cancellations it prevented among subscribers who would otherwise have left. Everything else is consumption by people who were already there.

The standard proxies systematically mislead in a known direction. Hours viewed rewards long series watched by loyal subscribers with nothing else to do, which is the population least at risk of leaving. Completion rate rewards titles that hold attention among people who already chose them. Signups during a launch window conflate the title with the marketing campaign, the seasonal pattern, and whatever else launched that month.

The measure that matters is incremental, and increments require counterfactuals. What would this subscriber have done without this title? They might have watched something else on the same platform and stayed exactly as long. A title that is beloved and entirely substitutable has a viewing figure and no value.

The consequences run through every decision. Renewal is decided on viewing thresholds whose relationship to retention is assumed rather than measured. Licensing is negotiated without a valuation, which means rights holders and platforms are both guessing. Marketing budget is allocated by anticipated audience rather than by measured incremental effect. And the entire category of narrow, distinctive content that holds a small segment nobody else serves is undervalued by every proxy in use — which is precisely the content a differentiated service depends on.

The industry knows this. The proxies persist because they are available, because they are comparable across titles, and because the people whose decisions would be judged by a better number have limited enthusiasm for one.

## Why It's Unsolved
Randomisation is nearly impossible at the title level. A platform cannot withhold a major title from a random half of its subscribers; the content is the product, the launch is public, and the commercial and contractual objections are immediate.

Natural experiments are thin. Staggered international releases, regional rights variations and phased rollouts provide some variation, and the regions differ in ways that confound the comparison.

The causal structure is genuinely difficult. A subscriber's decision to stay reflects the whole catalogue, their household, competing services, price changes and the season. Isolating one title's contribution requires assumptions that can be argued with, which makes the estimate politically contestable in a way a viewing number is not.

Subscription decisions are lumpy and lagged. Someone joins for a title and cancels four months later after watching a hundred other things; attributing that lifetime across the catalogue is a genuine allocation problem with no obviously correct answer.

And the organisational incentive is misaligned. Content executives are evaluated on outcomes that a credible incrementality measure would reframe, and they are usually the people who decide whether to build one.

## What a Solution Looks Like
Use the experiments that are actually available. Recommendation placement, artwork, homepage promotion, notification targeting and merchandising are all randomisable without withholding content from anyone, and each produces variation in exposure that supports genuine causal estimation of a title's effect on retention.

Exploit natural variation deliberately. Staggered releases, regional windowing differences, rights expirations and title removals are quasi-experiments that occur constantly and are analysed by nobody. A title leaving the catalogue is an especially clean test: what happens to the subscribers who watched it.

Model retention with the catalogue, not around it. Survival modelling on subscriber tenure with time-varying viewing covariates gives a defensible estimate of which viewing predicts continued subscription, and the honest version reports where the estimate rests on assumptions.

Measure substitutability. The critical question for any title is what its viewers would have watched instead, which is estimable from viewing behaviour when a similar title is unavailable — and it is the difference between a popular title and a valuable one.

Segment the analysis. A title that holds a small segment with no alternative can be worth more than a broadly watched one, and only segmented incrementality shows this. Aggregate hours viewed is precisely the metric that conceals it.

Publish uncertainty. The correct output is an interval and a stated method, because a contestable number that is roughly right beats a precise number that measures the wrong quantity.

## Impact If Solved
This is the largest unpriced cost base in modern media: tens of billions of dollars of annual content spend allocated on consumption proxies that systematically misvalue exactly the differentiated content the strategy requires. The data is the best any industry has ever had and the experimental design is the worst part of it. A platform that measures incremental title value credibly changes what it commissions, what it renews, and what it pays — which is the entire business.
