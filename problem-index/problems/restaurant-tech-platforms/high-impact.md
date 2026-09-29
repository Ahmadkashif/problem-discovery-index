# Store-Level Demand Forecasting for Labour and Prep

**Industry:** [[restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** High Impact
**One-liner:** The platform forecasts covers and item-level demand by daypart for each location, so a manager schedules and preps against a real prediction instead of last week plus intuition.
**Tags:** #time-series-forecasting #gradient-boosting #exponential-smoothing #feature-engineering #cross-validation #evaluation-metrics #confidence-intervals #temporal-fusion-transformers #revenue-impact

## The Problem
Two decisions determine whether a restaurant makes money in a given week, and both are forecasts. How many people to schedule, against a labour cost that runs thirty to thirty-five per cent of revenue and cannot be adjusted once the shift starts. And how much of each item to prep, against food cost around thirty per cent, where over-prepping is waste and under-prepping is a sold-out item and a walked customer.

Managers make both by looking at the same week last year, the last few weeks, and whatever they know about the weather and what is happening locally. They are frequently wrong in ways that are expensive and invisible: a slightly overstaffed Tuesday and a slightly understaffed Saturday net out on the P&L into a margin nobody can trace.

Every labour platform in the category claims a forecast. Operators overwhelmingly do not trust them, and the reason is specific: the forecasts are naive extrapolations from that location's own recent history, presented without uncertainty, that miss exactly the days managers most need help with. A forecast that is right on an ordinary Tuesday and wrong on the first warm Saturday in March has negative value, because the manager still has to check it, and if they are checking it they may as well do it themselves.

## Why It's Unsolved
A single restaurant is a small-sample problem. One location has a few years of history, heavily disrupted, with the pandemic sitting in the middle of it. The events that matter most — a home game, a festival, a school holiday, a road closure, the first genuinely warm evening — are individually rare at one site. There is not enough data at one location to learn their effect, which is precisely why the operator's intuition is hard to beat locally and precisely why pooling across locations should win.

Pooling is hard for a real reason: restaurants are heterogeneous. A brunch-heavy neighbourhood café and a suburban steakhouse respond to weather in opposite directions. A naive pooled model averages them into uselessness. Doing it properly requires learning location archetypes and letting the effect of each driver vary by archetype, which is more modelling than any vendor in the category has attempted.

The industry is also unusually punishing about accuracy. A manager who follows a forecast and gets caught short during a rush will never open it again. Trust is lost once, permanently, and the feature has already burned it at most vendors — which means the bar for a second attempt is higher than the bar for a first.

## What a Solution Looks Like
A hierarchical forecast that borrows strength across locations while respecting that they differ. Covers and item-level demand predicted by daypart, several days ahead, with a genuine prediction interval rather than a point number. External drivers — weather at the actual location, local events, school calendars, paydays, holidays — enter as features whose effects are learned across the whole customer base and applied according to the location's archetype.

The output should attach to the decision rather than sit in a report: a proposed schedule that already reflects the forecast and the labour target, and a prep sheet with quantities by item. And it should be honest about uncertainty, because the manager's real question is not "how many covers" but "how badly could this go, and which way."

## Impact If Solved
Labour and food together are roughly two thirds of a restaurant's cost structure, both committed in advance against a guess. A few points of improvement on either is the difference between a viable independent restaurant and a closed one, in a sector with famously thin margins. It is also the only capability in the category that a competitor cannot copy by shipping a feature, because it rests on a pooled demand corpus.
