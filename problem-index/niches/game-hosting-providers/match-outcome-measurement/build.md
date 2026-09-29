# What a Bad Match Actually Costs

**Niche:** [[niches/game-hosting-providers/match-outcome-measurement/profile|Match Outcome Measurement]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The complete record of every multiplayer session exists and nobody has asked it the one question the whole system is built around.
**Tags:** #causal-inference #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #descriptive-statistics #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to put a number on what a mismatched match, a long queue and excess latency each cost in whether the player queues again — and whoever produces that number takes the account.

## The Problem
A multiplayer platform records every match: the composition, the skill spread, the wait that preceded it, the latency each player experienced, how one-sided the result was, who left before the end, and who queued again afterwards. Everything needed to estimate the cost of a poor experience is in that record. Nobody has run the analysis, so the entire matchmaking layer operates against an objective that has never been checked against player behaviour.

## Why Nobody Has Built This
The session data sits with the provider and the retention data with the studio, and nobody has joined them. The analysis requires causal care that a dashboard team is not staffed for. Nobody has asked for it. And the answer might embarrass the current configuration.

## What to Build
Measure the three costs separately, carefully, from data that already exists. Estimate the effect of match quality, queue time and latency on subsequent play, each net of the others, which is the core — they move together in the raw data and any naive estimate confounds all three. Handle self-selection explicitly, since players tolerant of long queues are systematically different and the unadjusted comparison gets the direction wrong. Model the hazard of a player not returning rather than a binary churn flag, as the timing carries most of the information. Produce a latency tolerance curve per game mode rather than a single threshold, which is immediately actionable for region policy. Quantify the effect of a run of poor matches rather than a single one, because the damage accumulates and single-match analysis understates it. Separate the losing player's experience from the winning player's, since a one-sided match costs the two sides very differently. Report in retention and revenue terms rather than in match quality units, which is what makes it usable outside the platform team. Validate against a deliberate small experiment where the platform will run one. Publish the method so the numbers can be trusted by both parties. And deliver it as a standalone report a studio can act on without changing any code.

## Target Customer
Studios operating multiplayer titles, hosting and multiplayer platform vendors, games analytics firms, and matchmaking service providers.

## Impact If Built
Match quality, queue time and latency move together in the raw data, so any naive estimate confounds all three. Separating them causally from the existing session record answers the question the whole matchmaking layer is built around.
