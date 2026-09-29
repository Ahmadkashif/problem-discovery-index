# Diagnosing Early-Cycle Churn

**Industry:** [[subscription-commerce|Subscription Commerce]]
**Type:** High Impact
**One-liner:** Most cancellations happen within the first three deliveries for specific, fixable reasons, and the industry reports a monthly churn rate and buys more acquisition.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #revenue-impact

## The Problem
Subscription commerce economics are simple and unforgiving. A customer acquired for a certain cost becomes profitable after some number of deliveries. If they cancel before that point, the acquisition was a loss.

A large share cancel exactly there. The concentration in the first three cycles is well known inside these companies and is treated as a fact of the category rather than as a diagnosable problem.

The reasons are specific. The first box did not match the impression created at sign-up. The cadence is wrong — a monthly delivery of something consumed every seven weeks accumulates, and accumulation is the most reliable predictor of cancellation in replenishment categories. An item arrived damaged or late and the recovery was poor. The customer could not tell what the subscription was doing for them relative to buying the same things individually. The onboarding never explained how to skip, so pausing meant cancelling.

Each of those is a different fix and the company cannot tell which applies. Churn is reported as a monthly percentage, cancellation surveys collect a dropdown answer chosen to end an interaction, and the response is to increase acquisition spend to fill the leak.

## Why It's Unsolved
Cancellation reasons collected at the exit are unreliable in a well-understood way. The customer has decided, wants to finish, and picks the least confrontational option — which is why "too expensive" dominates every cancellation survey regardless of what actually happened.

The real cause usually precedes the cancellation by weeks. A box that disappointed in cycle one produces a cancellation in cycle three, and nothing connects them, because the systems that record what was shipped and the systems that record cancellations are analysed separately.

Cadence mismatch is invisible without consumption data the company does not have. The company knows what it shipped and not what was used, and inferring consumption from skip behaviour and reorder timing requires deliberate analysis nobody funds.

The organisational split entrenches it. Retention sits with marketing, product quality sits with merchandising, fulfilment sits with operations, and early churn is caused by all three — so it belongs to nobody and is reported as a marketing metric.

## What a Solution Looks Like
Survival modelling on the delivery sequence rather than on calendar time. The unit that matters is the delivery, not the month, and hazard by delivery number with covariates for what was in each box is the correct frame and is rarely used.

Cause attribution from the operational record. Whether a customer received a damaged item, a late delivery, a repeat of something they already had, or a box heavily divergent from their stated preferences is all in the data, and each is testable as a churn driver with real effect sizes.

Cadence inference from behaviour. Skip patterns, swap behaviour and reorder timing reveal actual consumption rate, and a mismatch between shipping cadence and consumption is both the most common cause of accumulation-driven cancellation and the easiest to fix — by proposing a different cadence rather than waiting for a cancellation.

Intervention testing rather than intuition. Whether a proactive cadence change, a make-good on a damaged item or an onboarding explanation actually reduces churn is measurable by experiment, and this category runs remarkably few.

## Impact If Solved
Early-cycle churn determines whether acquisition spend produces profit or loss, and it is currently treated as an inherent property of the model rather than as a set of specific, diagnosable, fixable failures. Attributing it to operational causes and intervening before cycle three is the difference between a business that compounds and one that refills a bucket.
