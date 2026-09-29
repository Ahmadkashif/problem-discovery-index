# The Follower Count Is Doing All the Work

**Niche:** [[niches/live-commerce-platforms/cold-start-stream-ranking/profile|Cold-Start Stream Ranking]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Distribution tracks follower count, follower count tracks past distribution, and the loop closes on a small set of established hosts while the marketplace calls it relevance.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #revenue-impact #quick-win #survival-analysis #compliance
**Contested on:** Every serious competitor in this niche is fighting to rank a stream that has existed for four minutes against streams with hours of accumulated signal — and whoever gets the first minutes right decides which sellers survive.

## The Problem
Follower count is the strongest feature in the model because it is the only durable one, and it is downstream of the distribution the platform itself gave. A host who was surfaced last year has followers, so they are surfaced this year, so they gain followers. A new seller with better inventory and a better conversion rate is ranked below them indefinitely. The system reports high engagement and is measuring its own feedback loop. Nobody has run the counterfactual, because the counterfactual requires deliberately giving distribution to sellers the model does not favour.

## Why It's Still Broken
The loop is invisible in the metric it optimises — concentration and relevance look identical from inside an engagement number. Feature importance is not routinely examined for endogeneity. Breaking the loop costs measurable short-term engagement for a diffuse long-term supply gain, which is a trade no team is rewarded for. And the sellers harmed by it are the ones with no standing to complain.

## What a Fix Looks Like
Measure the loop, then break it deliberately. Report distribution concentration directly — what share of impressions goes to the top percentile of sellers, and how that has moved — which is a one-query diagnostic that almost no platform publishes internally and which usually surprises the team that runs it. Decompose the ranker's feature importance and separate the endogenous features from the exogenous ones, since follower count is a record of past platform decisions rather than an observation about the world. Run a held-out exploration arm where a slice of traffic ignores follower count entirely, which is the only way to get the counterfactual and is cheap at a small allocation. Score sellers on rates rather than totals — conversion, retention, repeat purchase — since rates are comparable across scale and totals are not, and this alone repositions a large number of small sellers correctly. Normalise early signal by impressions delivered, so a stream that converted well on two hundred impressions is not beaten by one that converted poorly on two hundred thousand. Set an explicit floor on distribution to unproven sellers and treat its cost as supply acquisition spend with a measured return. Track the composition of the top sellers over time, since a set that never changes is the symptom. And report concentration alongside engagement permanently, because a diagnostic run once is a diagnostic that stops being run.

## Who Feels the Pain
New and small sellers ranked on a proxy for the platform's own past choices; the marketplace losing supply diversity; and viewers shown a narrowing set of the same shows.

## Impact If Fixed
Follower count is downstream of distribution the platform itself gave, so the model is measuring its own feedback loop and calling it relevance. Concentration share is a one-query diagnostic, and a small no-follower-feature exploration arm buys the counterfactual cheaply.
