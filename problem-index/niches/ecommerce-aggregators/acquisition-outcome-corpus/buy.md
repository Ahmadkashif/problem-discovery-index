# Quasi-Experimental Methods

**Niche:** [[niches/ecommerce-aggregators/acquisition-outcome-corpus/profile|Acquisition Outcome Corpus]]
**Industry:** [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Economics built a whole toolkit for estimating effects from interventions that were not randomised, and this sector has the cleanest natural experiment in commerce and no analyst.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #time-series-forecasting #evaluation-metrics #monte-carlo-methods #probability-distributions #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to turn dozens of brands observed before and after acquisition into an empirical account of what drives marketplace performance — and whoever does that underwrites and operates better than anybody, because nothing else in the sector produces that evidence.

## The Problem
Estimating what an intervention caused when it was not randomised is exactly what quasi-experimental methods do. Difference-in-differences compares treated and untreated units before and after. Synthetic control constructs a counterfactual from unaffected units. Event studies estimate effects around a known date. Staggered adoption designs handle treatments applied at different times to different units — which is precisely the structure of a portfolio of acquisitions migrated in sequence.

## What Already Exists
Difference-in-differences with staggered treatment timing; synthetic control methods for constructing counterfactual units; event study methodology around known intervention dates; panel data methods with unit and time effects; and the applied literature on pre-trend testing and robustness.

## The Customization Gap
The adaptation is to a small number of units in a market where untreated comparisons are competitors. It requires: (1) control units drawn from competing listings that were not acquired, which are observable through public marketplace data and are the natural comparison group — constructing that control set is the specific work and it is available to anyone collecting the data; (2) staggered timing exploited deliberately, since acquisitions and migrations happen on different dates and that variation is what identifies the effects; (3) synthetic control per listing, which suits a small number of units far better than a panel regression and is the right tool at this scale; (4) pre-trend testing taken seriously, since acquired brands may have been selected partly on trajectory and a naive comparison attributes the selection to the treatment; and (5) results reported with the humility a small sample requires, since the temptation to over-read forty observations is what would turn a good analysis into a new playbook that is equally unexamined.

## Target Customer
Aggregator analytics functions, their investors, and the applied economics community for whom this is an unusually clean and unstudied natural experiment.

## Impact If Solved
The structure is a staggered-adoption design and the sector has no analyst. Control listings are observable in public marketplace data, which makes the counterfactual constructible by anyone collecting it, and synthetic control is the right tool at this number of units.
