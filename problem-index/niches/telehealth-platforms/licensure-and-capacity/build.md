# Build: Demand Forecasting and Licence Portfolio Optimisation

**Niche:** [[niches/telehealth-platforms/licensure-and-capacity/profile|Licensure, Credentialing & Capacity Matching]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Forecast demand by state and hour, and decide which clinicians should acquire which additional licences as an investment portfolio rather than a guess.
**Tags:** #time-series-forecasting #convex-optimization #monte-carlo-methods #confidence-intervals #evaluation-metrics #dynamic-programming #revenue-impact #automation
**Contested on:** Whether state-level demand is forecastable finely enough to plan a licence portfolio against.

## The Problem

A platform's capacity is not a number of clinicians; it is a matrix of clinicians by states they can practise in, against demand that varies by state and hour. The matrix is sparse — most clinicians hold two or three licences — and the sparsity is what produces the characteristic failure: clinicians sitting idle while patients in a different state wait.

The licence portfolio is the long-term lever and it is managed by intuition. Each additional state licence costs money, takes weeks to months, and is worth something only if that state has demand at hours that clinician works. Platforms fund licences, and the choice of which clinicians and which states is made without a model of the return.

The short-term lever is incentives, and that is equally unmodelled: a rate bump goes out broadly rather than to the clinicians licensed in the state that is short.

## Why Nobody Has Built This

Capacity planning grew out of scheduling spreadsheets and never became an analytical function, because for a long time the binding constraint was total clinician supply rather than its state distribution. As platforms have grown and demand has become more geographically differentiated, the distribution has become the constraint and the tooling has not caught up.

The licence portfolio problem is also genuinely multi-period and stochastic — a licence bought today pays off over years against demand that will change — which makes it harder than a staffing roster and easy to defer.

And the supply side is self-scheduling, so a plan is a probability rather than a schedule, which discourages planning at all.

## What to Build

A forecast, an assignment model and a portfolio optimiser.

**Forecast demand by state and hour.** Strong daily, weekly and seasonal structure, plus respiratory season, weather, holidays and marketing activity. This is standard forecasting with abundant history and it is the foundation; per-state rather than aggregate is the requirement, and the small states are where the error matters most.

**Forecast supply, not just schedule it.** Contractor availability is a behaviour, not a roster: which clinicians log on, for how long, given the rate, the day and their history. Modelling this — including the response to incentive rates — turns capacity planning from wishful assignment into a probabilistic plan.

**Optimise the licence portfolio.** For each candidate clinician-state pair, the expected value is the additional coverage it provides at the hours that clinician actually works, in the states that are short, over the licence's life, weighted by the probability the clinician stays. Against a cost and a lead time of weeks to months. This is a multi-period optimisation under uncertainty and it is exactly the kind of decision currently made by feel, with each licence costing real money.

**Target incentives.** When a state is projected short at a given hour, the incentive should reach the clinicians licensed there who have historically worked those hours and are responsive to rate — not the whole pool. This is a targeting problem with an obvious model and a directly measurable saving.

**Plan the compacts deliberately.** Interstate compacts materially change the portfolio arithmetic, and participation decisions for individual clinicians should be evaluated as part of the same optimisation rather than treated as an administrative matter.

**Simulate service levels.** Given the forecast, the supply model and the licence matrix, what is the probability of breaching the wait-time target in each state each hour. A Monte Carlo over the plan is what turns a roster into a risk statement, and it tells leadership where the exposure is before it materialises.

## Target Customer

Platform workforce operations and clinical staffing leadership, where the saving is direct — idle clinician hours and breached service levels are both measurable costs — and where the licence spend is a real budget line currently allocated on judgement.

## Impact If Built

Capacity planning becomes a forecast and an optimisation rather than a spreadsheet. The licence budget gets allocated to the clinician-state pairs that actually relieve the constraint. Incentives reach the people who can act on them. And leadership can state the probability of missing service levels by state before the week starts.
