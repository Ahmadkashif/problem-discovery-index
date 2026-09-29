# Retrying on a Schedule Somebody Chose

**Niche:** [[niches/payment-processors/decline-recovery/profile|Decline Recovery]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every decline triggers a retry decision worth real revenue, the outcome arrives two days later in a settlement file, and almost nobody joins the two.
**Tags:** #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact #monte-carlo-methods #causal-inference #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to know which declines are worth retrying, from which issuer, on what schedule — and whoever learns that from settlement outcomes recovers revenue everyone else abandons.

## The Problem
A subscription renewal is declined for insufficient funds. The dunning configuration retries in three days, then seven, then twelve, then gives up. Those numbers came from a blog post or a default. For this issuer, this cardholder's pay cycle and this decline reason, the optimal schedule may be entirely different — the day after payday may succeed where day three fails, and a fourth attempt may be worth far more than the first three. Every one of those retries has a recorded outcome. The data to answer this properly is generated continuously, at enormous volume, and is used to bill for the attempts rather than to decide them.

## Why Nobody Has Built This
Retry schedules are exposed as merchant configuration, which makes them the merchant's decision and therefore nobody's responsibility to improve — the control surface determined the ownership. The outcome sits in settlement, two days later, in a different system. Merchants ask for control and default to convention. And the revenue recovered by a better schedule is invisible because the counterfactual is never run.

## What to Build
Learn the recovery policy from outcomes. Model the probability of success for each candidate retry, conditioned on issuer, decline reason, attempt number, elapsed time, transaction characteristics and the cardholder's own history, which is the core and is well-posed with the volume available. Learn the timing explicitly as a distribution rather than a schedule, since the optimal moment varies by decline reason and is frequently tied to a pay cycle the processor can infer. Decide when to stop, because continuing to retry a decline that will not succeed costs fees, irritates the issuer and risks the merchant's standing — optimal stopping is the underused half of this problem. Combine credential refresh with retry intelligently, since refreshing first changes the success probability substantially for some decline reasons and not at all for others, and it is currently applied uniformly. Use the cardholder's behaviour across merchants, which is the processor's unique advantage and is invisible to any single merchant. Experiment by randomising schedules at small scale, which the processor can do and which converts an observational estimate into a causal one. Account for the customer experience, since repeated declines and unexpected late charges have a cost the recovery rate does not capture. Report recovered revenue against the baseline schedule, which is the claim and should be demonstrable per merchant. Handle the subscription and the one-off case differently, as persistence is worth far more in one than the other. And expose it as an outcome rather than as a configuration, so the processor owns the number.

## Target Customer
Processors and platform acquirers, subscription businesses whose revenue depends on recovery, and the dunning and recovery vendors serving them.

## Impact If Built
The control surface determined the ownership, so the schedule is a merchant setting and nobody's job to improve. Modelling success probability per issuer and decline reason, with optimal stopping, turns folklore into recovered revenue that can be demonstrated against a baseline.
