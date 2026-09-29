# The Dashboard Shows the Drop and Cannot Say Why

**Industry:** [[game-analytics-vendors|Game Analytics Vendors]]
**Type:** High Impact
**One-liner:** Retention falls, and separating a build regression from a content update from an acquisition mix shift from a genre-wide seasonal pattern is done by an analyst forming hypotheses, while the vendor holds the data from thousands of comparable games and shows none of it.
**Tags:** #causal-inference #change-point-detection #time-series-forecasting #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #gradient-boosting

## The Problem
A live game's key metrics move constantly, and the question is always the same: is this real, is this us, and what do we do. The dashboard can segment the movement by platform, cohort, acquisition source, country and version, which narrows the search and does not answer it, because the plausible causes are confounded with each other and several of them are invisible in the analytics system entirely.

Build regressions, content updates, configuration changes, acquisition source mix, price or offer changes, competitor launches, platform-level events and seasonality all move retention, and they routinely happen in the same week. A studio that shipped an update, ran a promotion and changed its acquisition mix on the same Tuesday has no way to attribute the Wednesday movement, and this is the normal state rather than an unusual one.

Half the causes are not in the analytics system. Build contents live in version control, configuration changes in a live operations platform, acquisition mix in the measurement partner, competitor activity nowhere. So even a rigorous analyst is working with a partial picture and reasoning about the rest.

The comparison that would settle most of it is unavailable to the studio and available to the vendor. Whether every game in this genre saw the same movement that week is the first question any experienced analyst asks and the one they cannot answer, because they see one game. A vendor with thousands of titles could answer it in a query, and the product does not.

The cost of the gap is decisions made on guesses. Studios roll back builds that were fine, chase acquisition sources that were not the problem, and change designs in response to a seasonal pattern — and because the attribution was never established, the next movement starts the same cycle.

## Why It's Unsolved
The cross-studio corpus is commercially awkward. Vendors hold data under customer agreements that vary in what aggregate use they permit, and several customers would object to their performance informing a competitor's benchmark even in anonymised aggregate. Negotiating that is a legal and communications project as much as a technical one, and it has been easier to leave the corpus unused.

The causal question needs data the vendor does not have. Build history, configuration changes and acquisition mix sit in other systems, and integrating them is work the vendor has not prioritised because the analytics product is sold on dashboards rather than on answers.

Games also make clean causal inference unusually hard. Builds bundle many changes, updates ship globally rather than staged, and experimentation infrastructure sits in a different platform than analytics — so the natural experiments that would isolate causes are rarely constructed and frequently impossible after the fact.

And the demand has historically been met by hiring an analyst. Studios large enough to care have data teams, and the vendor's product has been positioned as the substrate those teams query rather than as the thing that answers the question.

## What a Solution Looks Like
Answer the market question first, because it is the cheapest and most valuable. A genre-conditioned benchmark showing whether comparable games moved the same way that week converts the majority of panics into a known market event, and it requires only aggregation the vendor is uniquely positioned to perform. Anonymisation and cohort-size thresholds make it defensible to customers whose data contributes.

Decompose the movement into observable components. Cohort mix, acquisition source mix, version distribution, platform mix, content state and seasonality are all measurable, and reporting how many points of the change each accounts for — with an honest unexplained residual — turns a mystery into an accounting statement. Most movements resolve entirely at this step.

Integrate the causes. Build metadata, configuration change logs and acquisition data are three integrations that convert the vendor's product from a description into an explanation, and every customer already has all three in systems with APIs.

Build for causal inference rather than only reporting. Staged rollout support, holdout cohorts maintained by default, and experiment assignment recorded alongside events mean the natural experiments exist when they are needed, rather than being unavailable after the fact.

## Impact If Solved
Every studio running a live game asks this question weekly and answers it by inference. A market comparison alone would resolve most instances and is a query away for the vendor and impossible for the customer. Adding decomposition and the three integrations that bring the causes into the same system turns an analytics product from a substrate that data teams query into the thing that answers the question — which is a different and considerably more defensible business than selling dashboards in a category where general-purpose product analytics tools are competing on price.
