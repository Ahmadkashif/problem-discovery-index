# The Payment That Was Always Going to Fail

**Niche:** [[niches/bnpl-providers/the-consumer-with-six-plans/profile|The Consumer With Six Plans]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Four instalments fall in the same week against a card that will not cover them, the provider knows the amount and the date, and the first anyone says anything is a failed payment and a fee.
**Tags:** #time-series-forecasting #change-point-detection #evaluation-metrics #compliance #quick-win #revenue-impact #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to give a consumer a view of what they have actually committed to across providers — and whoever does that serves the only party who could see all of it and has no tool for it.

## The Problem
The provider knows the amount and the date of every payment it will take. In many cases it can also see, from the consumer's repayment pattern and their behaviour with previous plans, that the payment is at risk. It takes the payment anyway, it fails, a fee is charged, the card may be declined elsewhere, and the consumer's difficulty is compounded by exactly the mechanism that was supposed to make the purchase manageable. A warning two days earlier, offering to move the date or split the payment, would have cost nothing and prevented most of it.

## Why It's Still Broken
The payment is scheduled and taken automatically because that is the product's mechanism, and nothing in the process pauses to ask whether it will succeed — the automation was built for the happy path and the failure path is a fee. Late fees are revenue in some models, which makes the warning commercially ambiguous. Predicting the failure requires modelling the consumer's position that the provider only partly sees. And the consumer's fee is not counted as a harm anywhere.

## What a Fix Looks Like
Warn before taking the payment. Predict payment failure from the consumer's own history, prior failed attempts, the timing relative to their income pattern and the plan's position in the sequence, which is well-posed on the provider's own data and is the foundation of the fix. Warn with enough notice to act, which is a day or two rather than an hour, and is the difference between a fee and a solution. Offer the specific options — move the date, split the payment, pause — at the moment of the warning, since a warning without an option is a notification of an approaching problem. Move the payment to align with the consumer's income timing, which the provider can infer and which resolves a large share of failures at no cost to anyone. Suppress the retry that will also fail, since repeated failed attempts multiply fees and card declines. Waive the fee where the provider's own scheduling caused the collision, which is fair and is currently not distinguished. Look at the consumer's whole position with this provider before taking any payment, since a provider with three plans for one consumer is causing its own collisions. Be honest about the fee revenue conflict, since a product that prevents fees reduces income in some models and the decision should be deliberate. Report the failed payment rate and the fees charged as consumer outcome metrics, not only as revenue. And measure whether warned consumers end up better off, because that is the test of whether this is a genuine fix or a notification.

## Who Feels the Pain
Consumers charged fees for a collision the provider scheduled; people whose card is declined at a shop because four payments landed together; and providers whose complaints and regulatory exposure come from a preventable failure.

## Impact If Fixed
The automation was built for the happy path and the failure path is a fee, so nothing pauses to ask whether the payment will succeed. Predicting failure from the provider's own data and warning two days early with a concrete option turns a fee into a rescheduled payment.
