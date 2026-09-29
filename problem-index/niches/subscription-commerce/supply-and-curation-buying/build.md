# Buying for Subscribers Who May Not Be There

**Niche:** [[niches/subscription-commerce/supply-and-curation-buying/profile|Supply & Curation Buying]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A subscription buy commits inventory months ahead for a subscriber base whose size and composition at delivery is unknown, and merchandisers do it from last month's count and a judgement.
**Tags:** #time-series-forecasting #probability-distributions #convex-optimization #confidence-intervals #survival-analysis #revenue-impact #evaluation-metrics #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to buy the right quantity of the right things for a subscriber base whose size and composition at delivery is unknown — and whoever does that protects the margin, because the buy is committed months before the base that receives it is known.

## The Problem
A merchandiser buys for the June box in March. They use the current subscriber count, add a growth assumption, and pick items they think will appeal. By June the base is eleven percent smaller than assumed, because the winter cohort churned faster than the previous year's, and skewed toward a segment whose stated preferences do not match two of the five items. The surplus has no other channel because the box is the only route to market. The margin on the June box is consumed by the write-off, and both errors — the count and the composition — were forecastable from data the company had in March.

## Why Nobody Has Built This
Subscriber forecasting requires the churn model the category does not have, so the buy is anchored on a current count. Preference data is thin and not in a form a merchandiser can use for a buy. The merchandiser's expertise is product and supplier relationships rather than forecasting, and nobody supports them with the analysis. And the write-off appears as a cost of goods variance rather than as a planning failure.

## What to Build
Forecast the base and buy against the distribution. Project the subscriber base at the delivery date from cohort survival and acquisition plans, with an interval rather than a point, since the quantity decision depends on the uncertainty and a point estimate cannot inform a commitment — this projection is the foundation and it falls out of the churn work directly. Project the composition as well as the count, since the mix of preference segments changes as cohorts churn differentially and a buy matched to today's mix is wrong for June's. Optimise the buy against the asymmetric costs of short and long, which is the newsvendor arithmetic and is immediate once the distribution and the costs are stated. Use the preference model to inform what to buy, not only what to put in which box, which connects the curation capability to the buying decision for the first time. Build flexibility into supplier terms — options, staged commitments, later cut-offs — which is negotiable and is worth more than a small unit price reduction in this structure. Plan the surplus disposition in advance, since a channel arranged before the surplus exists recovers far more than one improvised afterwards. Evaluate every past buy against what subscribers actually kept, which is the feedback the merchandiser has never received. And report buy accuracy as a standing metric, since it is a major margin driver and is currently visible only as a variance.

## Target Customer
Merchandising and procurement functions, subscription operators, and the finance functions funding the working capital.

## Impact If Built
The buy is committed against a count that will be wrong and a preference mix that will have shifted, both forecastable from data held at the time. A subscriber projection with an interval, plus the newsvendor arithmetic on asymmetric costs, turns a judgement into a decision.
