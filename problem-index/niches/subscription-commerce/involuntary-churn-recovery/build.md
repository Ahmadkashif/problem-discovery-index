# The Subscriber Who Never Chose to Leave

**Niche:** [[niches/subscription-commerce/involuntary-churn-recovery/profile|Involuntary Churn Recovery]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A large share of cancellations are payment failures from subscribers who wanted to stay, the tooling is installed nearly everywhere, and the recovery rates between operators running the same tools differ by a factor.
**Tags:** #gradient-boosting #markov-chains #evaluation-metrics #confidence-intervals #revenue-impact #automation #hypothesis-testing #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to recover the subscriber whose card failed rather than the one who chose to leave — and whoever does that keeps the revenue, because a payment failure is a large, mechanical share of churn from customers who never decided anything.

## The Problem
A subscriber's card is replaced after a fraud alert. The next charge fails. The dunning sequence sends three emails on days one, four and seven, all of which go to a promotions folder. On day fourteen the subscription is cancelled. The subscriber notices two months later when the deliveries stopped, is mildly annoyed, and does not resubscribe. Nothing about this was a decision. The retry timing, the channel, the message and the update flow were all defaults nobody examined, and the same failure with a different configuration would have recovered.

## Why Nobody Has Built This
Dunning is installed once during setup and then sits, because it works well enough to look solved. The recovery rate is reported as a number with nothing to compare it to, so a mediocre one looks acceptable. Involuntary churn is pooled into the churn figure, so its size is unknown. And payment operations is nobody's product surface.

## What to Build
Optimise the recovery rather than running the default. Learn the retry schedule from outcomes rather than using a fixed sequence, since the probability of a successful retry varies enormously by decline reason, card type, time since failure and day of month, and a learned schedule materially outperforms a fixed one — this is the highest-return piece and is straightforwardly modellable. Use the decline reason to choose the response, since an expired card needs an update and an insufficient funds decline needs a retry at a different time, and sending the same message to both wastes half the attempts. Reach the subscriber where they will see it, which means messaging channels as well as email and an in-product prompt, because the recovery frequently fails on delivery of the message rather than on the subscriber's willingness. Make the update experience frictionless on a phone, since that is where the subscriber will do it and a poor form is the last avoidable loss. Extend the grace period to what the data supports rather than to a default, holding the subscription alive while recovery is still plausible. Measure recovery rate against a benchmark and against the theoretical maximum, so a mediocre implementation is visible. Update cards proactively where the network supports it, which recovers failures before they happen. And treat the recovered subscriber as a service moment rather than a collections one, since the tone of these messages affects whether they stay afterwards.

## Target Customer
Every subscription operator, payment and billing platform vendors, and the finance functions who do not know how much is being lost here.

## Impact If Built
Recovery rates differ by a factor between operators running the same installed tools, because every lever is left at a default. A learned retry schedule conditioned on decline reason is the highest-return piece and is straightforwardly modellable.
