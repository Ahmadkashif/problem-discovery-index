# Visible Before the Missed Payment

**Niche:** [[niches/bnpl-providers/hardship-prediction/profile|Hardship Prediction]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A consumer heading into difficulty is visible in their repayment pattern weeks before they miss a payment, and hardship is identified when they disclose it.
**Tags:** #change-point-detection #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #revenue-impact #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to identify a consumer heading into difficulty before the missed payment rather than after it — and whoever does that intervenes while it still helps and while the regulator is still watching rather than acting.

## The Problem
The signals are there. Payments that used to clear on the first attempt now clear on the second. The interval between new plans shortens. Basket values drop and plan counts rise. The consumer starts taking plans for essentials rather than discretionary purchases. Any one of those is weak and together they are a clear trajectory, visible weeks before the first missed payment. The provider's process identifies hardship when the consumer telephones to disclose it, which is after the missed payment, after the fee, and after the point at which a small intervention would have worked.

## Why Nobody Has Built This
Hardship is treated as a state the consumer declares rather than a trajectory the provider can observe, which is a framing inherited from lending processes designed around disclosure — the concept was borrowed and the observability was not. Intervening before a default means offering forbearance to someone who has not asked and might have been fine, which feels commercially odd. There is a fear that proactive contact implies a judgement about the customer. And nobody has measured what the early intervention would be worth.

## What to Build
Predict the trajectory and intervene early. Model the progression toward difficulty from the provider's own repayment behaviour, which is well-posed, uses data already held, and produces a signal weeks ahead of the event. Use the signals that precede the miss rather than the miss itself — retry-clearing, shortening intervals, changing basket composition, plan count growth — which are the leading indicators and are currently used for nothing. Intervene proportionately and early, with a payment date change, a pause or a plan, rather than waiting for the fee. Make the offer without requiring disclosure, which is the fix note's subject and is the difference between help that reaches people and help that exists. Design the contact carefully, since a badly worded proactive message about financial difficulty is intrusive and the framing determines whether this helps or offends. Stop offering new plans to consumers on the trajectory, which is the obvious and commercially uncomfortable action and is the one that most protects them. Connect to the accumulation view where it exists, since the provider's own signal is partial and the consumer's total position is the real question. Measure the intervention's effect on outcomes rather than on recovery, since the point is fewer people in difficulty. Anticipate the regulatory expectation, which is moving toward proactive identification of vulnerability and will arrive whether or not the sector moves first. And report predicted hardship as an operating metric, because a sector that can state how many of its customers are heading into difficulty is in a very different position from one that cannot.

## Target Customer
Collections and product leadership at instalment providers, the consumers heading into difficulty, and the regulators whose expectations of proactive identification are forming.

## Impact If Built
Hardship was borrowed as a concept the consumer declares, and the observability was not borrowed with it. Retry-clearing, shortening intervals and changing basket composition are leading indicators sitting in the provider's own data and used for nothing.
