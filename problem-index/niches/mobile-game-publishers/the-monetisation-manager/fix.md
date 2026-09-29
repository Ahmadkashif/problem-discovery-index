# The Top Spender Nobody Checked On

**Niche:** [[niches/mobile-game-publishers/the-monetisation-manager/profile|The Monetisation Manager]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** One account spent more in a month than most players spend in a lifetime, the revenue chart showed a good month, and nobody looked at the account.
**Tags:** #quick-win #change-point-detection #descriptive-statistics #evaluation-metrics #compliance #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to give the person tuning monetisation an instrument that says whether the small group producing most of the revenue is all right — and whoever builds it takes the account.

## The Problem
Extreme individual spending shows up in aggregate revenue as a good result. No alert fires, no review happens, and the account continues to receive the most aggressive offer treatment because that is what the targeting model concluded. Sometimes the account belongs to someone with money and an enthusiasm. Sometimes it does not, and the first anyone hears is a chargeback, a complaint, a press enquiry or a regulator.

## Why It's Still Broken
Nothing in the stack is looking for an individual — a monitoring system built entirely on aggregates cannot raise an individual case, so the only outlier detection in the business is pointed at fraud rather than at harm. Revenue concentration is treated as a feature. There is no defined threshold and no owner. And reviewing an account feels intrusive without a framework to do it inside.

## What a Fix Looks Like
Detect the individual outlier and define what happens next. Alert on individual spending far outside the player's own established pattern, which is the fix and is straightforward anomaly detection on data already held. Set explicit review thresholds with a named owner, because an alert with no owner is not a control. Flag rapid escalation rather than only absolute level, since the trajectory is the more reliable signal. Reduce offer pressure automatically on flagged accounts pending review, as continuing to target them is the indefensible part. Check for shared-device and minor-payer indications, which is where the worst cases concentrate. Review abrupt cessation after heavy spending, since that pattern usually means something went wrong. Surface age and payment method signals that are already collected. Record every review and its outcome, which is what demonstrates the control is real. Make the intervention supportive rather than accusatory in tone, which determines whether it helps. And report the count of flagged accounts to leadership monthly, so the number cannot be quietly ignored.

## Who Feels the Pain
Players who spent far more than they meant to; monetisation managers who would have acted with an alert; publishers facing chargebacks, coverage and scrutiny; and support teams handling it afterwards.

## Impact If Fixed
A monitoring system built entirely on aggregates cannot raise an individual case, so the only outlier detection in the business is pointed at fraud rather than at harm. Alerting on deviation from a player's own pattern is standard anomaly detection pointed somewhere new.
