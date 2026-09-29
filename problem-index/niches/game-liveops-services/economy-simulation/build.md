# Run the Change Before Shipping It

**Niche:** [[niches/game-liveops-services/economy-simulation/profile|Economy Simulation]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A live game is the closest thing to a controlled economic laboratory that exists, and its operators never simulate anything.
**Tags:** #monte-carlo-methods #markov-decision-processes #time-series-forecasting #confidence-intervals #causal-inference #evaluation-metrics #optimization-fundamentals #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to tell a designer what the economy will look like in three months if they ship a proposed change — and whoever makes that forecast trustworthy takes the account.

## The Problem
Changing an economy parameter in a live game is an irreversible experiment on millions of people whose consequences appear over months. Designers make these changes weekly, with no forward model, and find out what happened when the drift becomes visible. The telemetry needed to simulate the population's response — earning rates, spending patterns, progression pace, price sensitivity by cohort — is complete, and the simulation would convert the decision from an intuition applied after the fact into something evaluated before it ships.

## Why Nobody Has Built This
Simulation requires modelling player behaviour rather than just accounting for flows, which is a step beyond what any live ops platform attempts. The cost of not doing it arrives slowly and is attributed elsewhere. Designers do not trust models they cannot inspect. And nobody has validated such a forecast publicly, so there is no proof it works.

## What to Build
Simulate the population, not just the ledger. Model heterogeneous player cohorts with measured earning, spending and progression behaviour rather than an average player, which is the core — the average player does not exist and every economic mistake in these games comes from designing for them. Include behavioural response to price and reward changes, since a population that adapts is the difference between a projection and a simulation. Propagate the change forward over months with uncertainty bands, as a point forecast on a three-month horizon will be wrong and pretending otherwise destroys trust. Model entry and exit, because new players arriving into a mature economy are where the damage concentrates. Report the distributional outcome, not just the aggregate, since a change that improves the mean and ruins the median is the classic failure. Let the designer vary parameters interactively, which is what makes it a design tool rather than a report. Validate every forecast against what actually happened and publish the record, which is the only route to being believed. Show which assumption drives each result, as an inspectable model is a usable one. Support comparing several candidate changes rather than assessing one. And keep the model's structure visible to the designer rather than presenting a black box.

## Target Customer
Live game operators, economy design teams, live ops platform vendors, and simulation and modelling consultancies.

## Impact If Built
The average player does not exist and every economic mistake in these games comes from designing for them. A heterogeneous cohort simulation with behavioural response makes a weekly irreversible experiment into a decision that can be evaluated first.
