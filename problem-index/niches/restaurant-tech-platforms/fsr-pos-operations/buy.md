# Retail Demand Forecasting Methods Applied to the Cover Count

**Niche:** [[niches/restaurant-tech-platforms/fsr-pos-operations/profile|Full-Service Restaurant POS & Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Demand forecasting for retail and grocery is a mature discipline with commercial products, published methods and decades of practice, and restaurant technology has adopted approximately none of it.
**Tags:** #time-series-forecasting #exponential-smoothing #gradient-boosting #recurrent-forecasting #confidence-intervals #evaluation-metrics #feature-engineering #hypothesis-testing
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
Grocery chains forecast item-level demand per store per day, handle intermittent demand, model promotion lift and cannibalisation, and have done so for twenty years with well-documented methods. Restaurants face a structurally similar problem — item-level demand, strong seasonality, perishability, substitution between items — and the industry's practice is a manager looking at last Saturday. The methods did not fail here; they were never tried, because restaurant technology grew out of payments and point of sale rather than out of supply chain.

## What Already Exists
Forecasting libraries and platforms are abundant and mostly free or cheap: gradient boosting on engineered calendar and weather features, hierarchical reconciliation so item forecasts sum to the daypart and location totals, intermittent demand methods for slow-moving items, and modern probabilistic forecasting frameworks all have mature open implementations. Weather APIs are commodity. Local event data is available. The retail forecasting literature on promotion effects and cannibalisation is directly applicable.

## The Customization Gap
The adaptation is to the restaurant's specific structure, which differs from grocery in ways that matter. It requires: (1) forecasting at the daypart rather than the day, because a restaurant's decisions are made per shift and a daily total hides the thing being scheduled against; (2) hierarchical reconciliation across item, category, daypart and location, since operators act on all four levels and inconsistent numbers destroy trust faster than inaccurate ones; (3) modelling the menu as a substitution structure rather than as independent items, because eighty-sixing one dish reallocates demand to its neighbours in predictable ways that no per-item model captures; (4) handling the industry's constant menu churn, where items are added, removed and repriced continuously, so a model must forecast an item with three weeks of history from comparable items; and (5) forecasting in the units of the decision — covers per hour for labour, prep quantities per item for the kitchen — rather than in dollars, which is what every existing restaurant report does and what no operator can act on directly.

## Target Customer
Restaurant platform vendors who would rather adapt a mature discipline than invent one, and the multi-unit operators sophisticated enough to build it themselves if nobody sells it.

## Impact If Solved
Adapting retail forecasting is substantially faster than building from first principles and arrives with known failure modes, evaluation practice and a literature on the exact problems — promotions, cannibalisation, intermittency — that restaurant demand presents. The daypart and decision-unit adaptations are where the value is and are the parts a generic product will never supply.
