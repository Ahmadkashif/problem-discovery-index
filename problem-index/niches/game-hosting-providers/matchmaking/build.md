# A Matchmaker With a Validated Objective

**Niche:** [[niches/game-hosting-providers/matchmaking/profile|Matchmaking]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The matchmaker optimises weights somebody guessed, against an outcome nobody measured.
**Tags:** #optimization-fundamentals #causal-inference #survival-analysis #confidence-intervals #evaluation-metrics #hypothesis-testing #markov-decision-processes #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to trade match quality against wait time against latency without knowing what any of the three costs in whether the player comes back — and whoever establishes that currency takes the account.

## The Problem
A matchmaker decides, thousands of times a minute, whether to start a match now with the players available or wait for a better composition, and which region to place it in. Every one of those decisions is a trade between three quantities with hand-set weights. The industry has the complete record of what happened after every such decision — whether the match was close, whether players left early, whether they queued again — and has never used it to establish what the trade actually costs.

## Why Nobody Has Built This
Queue time is visible on a dashboard and match quality's cost is not, so the incentives point one way. The outcome data sits with the provider and the retention data sits with the studio. Changing a matchmaker is risky and the current one is not obviously broken. And nobody has been asked to justify the weights.

## What to Build
Establish the currency, then optimise against it. Estimate the retention cost of a mismatched match, a long queue and excess latency in a common unit, which is the core — three quantities traded against each other with no common unit is not an optimisation, it is a guess. Use the complete session record to measure what followed each decision rather than surveying anyone, since the behavioural evidence is already collected. Handle the self-selection carefully, because players who accept long queues differ from those who do not and the naive comparison inverts the answer. Set policy from the measured costs rather than from hand-tuned weights, which is what converts the matchmaker into something defensible. Adapt to population size and time of day, as the right trade in a thin population at four in the morning is not the right trade at peak. Model latency tolerance by game mode rather than applying one threshold, since a turn-based mode and a shooter have entirely different curves. Optimise over the queue as a whole rather than greedily per match, which is where the available gain concentrates. Run holdouts continuously so the policy stays validated as the population changes. Report the trade explicitly to the studio rather than hiding it in a config. And expose the measured costs even to studios that keep their own matchmaker, since the evidence is separable from the engine.

## Target Customer
Game hosting and multiplayer platform vendors, studios operating multiplayer titles, matchmaking service providers, and games analytics firms.

## Impact If Built
Three quantities traded against each other with no common unit is not an optimisation, it is a guess. Estimating each one's retention cost from the session record turns hand-set weights into a validated policy.
