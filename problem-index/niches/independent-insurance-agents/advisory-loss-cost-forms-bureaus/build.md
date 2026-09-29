# Classification Systems Built for 1970 Carrying Today's Loss Data

**Niche:** [[niches/independent-insurance-agents/advisory-loss-cost-forms-bureaus/profile|Advisory Loss Cost & Policy Form Bureaus]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every commercial risk in America is priced through a classification scheme whose categories were drawn decades ago and have never been tested against the loss data that flows through them.
**Tags:** #k-means-clustering #gradient-boosting #tabular-ml #evaluation-metrics #causal-inference

## The Problem
A commercial policy is priced by putting the business in a class — a code describing what it does — and applying the loss cost published for that class in that state. The classification system is the skeleton of commercial insurance pricing, and it is also the oldest thing in it. Many classes were defined when the economy looked entirely different, and they persist because carriers' systems, agents' habits, and decades of filed rates are built on them.

The consequences are visible to everyone in the industry and addressed by no one. Classes that lump together businesses with genuinely different risk. Classes so thin the loss cost rests on a handful of claims. New kinds of business that do not fit anywhere and get assigned to whatever is closest. Classification disputes at premium audit, which are common precisely because the categories do not describe how businesses actually operate.

The organization has, uniquely, the data to know which classes are working: the aggregated premium and loss experience of the industry, class by class, state by state, year after year. It uses it to compute loss costs *within* the existing classes. It has never used it to ask whether the classes are the right ones.

## Why Nobody Has Built This
Stability is a genuine product feature. Carriers have filed rates, rating engines, and reserving history keyed to these codes; agents quote in them; regulators approve filings in them. Reclassifying breaks every one of those simultaneously, so the institutional answer to "should this class be split" has always been that the cost exceeds the benefit.

That answer has never been tested, because nobody has quantified the benefit. Doing so is a data exercise the organization is uniquely able to run and has no process for.

The work is also organized around production. Actuarial capacity is consumed by the filing calendar — every line, every state, every cycle — and reviewing the classification system is nobody's deliverable.

## What to Build
A standing empirical review of the classification system, on the data already flowing in.

**Measure within-class heterogeneity.** For each class, how much loss experience varies across risks that share the code, after controlling for size and state. High dispersion means the class is carrying distinct populations at one price — which is a cross-subsidy, a selection opportunity for any carrier that spots it, and a quantifiable defect.

**Test proposed splits against out-of-sample experience.** Where a class looks heterogeneous, candidate subdivisions can be evaluated on whether they actually predict loss on held-out years. That turns a permanent debate into an answerable question.

**Find the classes that should merge.** Thin classes produce unstable loss costs that swing with a single large claim. Identifying which thin classes are statistically indistinguishable from neighbours is the same analysis run in the opposite direction, and it improves the stability of published costs immediately.

**Detect emerging business types.** Risks that consistently produce classification disputes at audit, or whose experience diverges sharply from their assigned class, are the signal that the economy has produced something the scheme does not describe. Premium audit results are the natural source and they exist.

**Publish the diagnostics.** Carriers, regulators, and agents would all benefit from knowing which classes are credible and which are thin and volatile. That is a product in itself, and it is a by-product of the analysis.

## Target Customer
Chief Actuary or SVP of Analytics at the advisory organization. The pressure is competitive rather than internal: carriers with scale increasingly build their own segmentation from their own data and depart from advisory classes, and the advisory system's relevance depends on it being demonstrably better than what a large carrier can do alone.

## Impact If Built
Commercial insurance pricing accuracy across the entire US market runs through this scheme. Classes that mix genuinely different risks produce cross-subsidies that fall on the businesses least able to shop — small commercial accounts placed by independent agents, which is the population this whole industry serves. Nobody else in the market has the data to fix it, and the organization has been collecting it for a century.
