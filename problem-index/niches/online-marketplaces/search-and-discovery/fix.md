# Ranking Optimised for the Click

**Niche:** [[niches/online-marketplaces/search-and-discovery/profile|Search & Discovery]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Ranking trained on clicks learns to show what gets clicked, which concentrates all exposure on a small share of inventory and starves everything else of the impressions it would need to ever be clicked.
**Tags:** #logistic-regression #gradient-boosting #evaluation-metrics #confidence-intervals #probability-distributions #revenue-impact #hypothesis-testing #quick-win
**Contested on:** Not terminal — the contest differs by whether a catalogue exists, and the decomposition is recorded in the profile.

## The Problem
A ranking model learns from clicks. Listings that rank highly get clicks; listings that never rank get none; the model observes this and concludes the latter are unattractive. Within months a small share of the inventory absorbs most of the exposure, and a listing's chance of ever being seen depends mostly on whether it was seen early. Sellers of good inventory that started slowly cannot recover. The feedback loop is well understood in the recommendation literature, it operates on every marketplace, and the metrics all improve while it happens because the model is getting better at predicting a distribution it created.

## Why It's Still Broken
The loop improves every metric the team is measured on, which makes it self-justifying. Correcting for exposure bias requires counterfactual estimation that adds complexity for no visible metric gain. Deliberately showing less-clicked inventory looks like degrading relevance. And the harm is distributed across sellers who leave rather than concentrated in a complaint.

## What a Fix Looks Like
Break the loop deliberately. Report exposure distribution across the inventory — what share of listings receive what share of impressions — which is one query, is usually shocking, and is the number that makes the problem arguable at all. Correct training for exposure bias using the propensity machinery the recommendation field developed, so the model learns from what would have been clicked rather than from what was shown. Reserve a share of impressions for exploration, which is a small cost in immediate conversion and is the direct remedy — and is what gives a good listing that started slowly a route back. Boost new listings deliberately for a defined window, since a cold start is not a signal of quality and treating it as one is the loop's entry point. Report the metric that matters for the marketplace — share of inventory ever seen — alongside relevance, because the two pull in different directions and only one is currently reported. Measure the long-run effect of exploration rather than its immediate cost, since the loop's damage compounds and the exploration's benefit does too. Diversify result sets, which serves buyers and spreads exposure simultaneously. And track seller retention against exposure received, which is the link between a ranking decision and the supply the business runs on.

## Who Feels the Pain
Sellers whose good inventory never got a first impression; buyers shown the same popular items repeatedly; and operators whose supply churn is caused by a ranking system nobody suspects.

## Impact If Fixed
The exposure distribution is one query and is usually shocking, and it is what makes the feedback loop arguable. Reserving impressions for exploration is the direct remedy and gives a slow-starting listing a route back that the loop otherwise forecloses permanently.
