# The Most Observed Customer in Commerce

**Niche:** [[niches/subscription-commerce/subscriber-observation-corpus/profile|Subscriber Observation Corpus]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A subscription business observes the same customer repeatedly against a known expectation, which almost no other commerce model does, and uses it to draw a cohort chart.
**Tags:** #gradient-boosting #survival-analysis #bayesian-inference #confidence-intervals #evaluation-metrics #causal-inference #revenue-impact #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to use the repeated observation of the same customer against a known expectation — and whoever does that wins the category, because no other commerce model gets that view and this one throws it away.

## The Problem
A subscriber has fourteen deliveries, three skips, two swaps, one return, one late delivery, a support contact about the cadence, and a stated set of preferences from sign-up that the deliveries can be compared against. That is a longitudinal record with a stated expectation and repeated observations of the same person under a controlled treatment — a structure a market researcher would pay heavily to construct, generated for free by every subscriber every month. The company draws a cohort retention curve, reports it, and plans a campaign.

## Why Nobody Has Built This
The events live in separate systems — billing, fulfilment, support, the messaging platform — and nobody joined them. The platforms report cohorts because that is the recognised subscription metric and stop there. Most operators have no analytical function, and the ones that do point it at acquisition. And the value of the corpus is not obvious until somebody has assembled it, which nobody has.

## What to Build
Join the record and predict from it. Assemble the subscriber event record — sign-up expectation, every delivery with timing, contents and condition, every flexibility action, return, complaint and rating — into one longitudinal object, which is the precondition and is a data integration exercise rather than a modelling one. Predict cancellation per subscriber weeks ahead, which the early churn niche uses and which is the corpus's highest-value output. Estimate consumption and preference per subscriber, which the two sub-niches use. Measure the expectation gap directly, comparing the sign-up promise against the delivered experience, which is a comparison unique to this model and is made by nobody. Detect systemic problems from the individual records, since a cluster of subscribers with the same delivery issue is an operational finding the individual tickets do not reveal. Identify the subscribers worth intervening on rather than those most likely to leave, which is the uplift framing and is the difference between spending on the doomed and changing an outcome. Feed everything back into acquisition, since knowing which acquisition sources produce subscribers who reach delivery four is the most useful thing the corpus can tell the growth team. And keep it small and interpretable, because these are modest datasets where a straightforward model acted upon beats a sophisticated one reported.

## Target Customer
Subscription operators of every size, their retention and merchandising functions, and the platform vendors whose cohort charts are the category's analytical ceiling.

## Impact If Built
The structure is a longitudinal panel with a stated expectation and repeated controlled observations, generated for free and used to draw a curve. The expectation gap between what sign-up promised and what arrived is a comparison unique to this model and is measured by nobody.
