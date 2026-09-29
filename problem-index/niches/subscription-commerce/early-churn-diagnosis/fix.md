# The Reason Collected in a Dropdown

**Niche:** [[niches/subscription-commerce/early-churn-diagnosis/profile|Early Churn Diagnosis]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** Cancellation reasons are gathered from a dropdown on the cancel page, chosen by a customer who wants to leave quickly, with options written by the company — and the resulting data is used to plan the retention strategy.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #confidence-intervals #causal-inference #worker-facing #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to know why the first three deliveries fail — and whoever does that takes the economics, because that is where nearly all the churn happens and the reasons are specific and fixable.

## The Problem
The cancel page offers five reasons: too expensive, not using it, taking a break, quality, other. A customer leaving because the box never matched what they expected picks not using it. One leaving because the cadence was wrong picks too expensive, because it felt like too much money for products they had not finished. One leaving because a delivery arrived broken and the replacement took three weeks picks other and does not type anything. The company reports that price is the leading reason and adds a cheaper tier, which does not address any of the three. The measurement instrument was designed for speed of exit and is being used as a research finding.

## Why It's Still Broken
The dropdown is the only research instrument in the flow and its output is the only reason data the company has, so it is used. The options were written by whoever built the page. A customer at the cancel page is minimising effort and will pick the first plausible option. And the resulting distribution is stable, which reads as reliable rather than as consistently biased.

## What a Fix Looks Like
Infer the reason from behaviour and validate the stated one. Classify each cancellation from observed behaviour — delivery timing against consumption signals, skips and swaps, support contacts, delivery incidents, the gap between sign-up preferences and contents — which is available for every canceller and does not depend on them telling you anything, and is the fix. Compare the behavioural classification against the stated reason to calibrate the dropdown, which tells the company how much to trust the data they already have and is a one-off analysis with lasting value. Rewrite the options from the behavioural findings rather than from intuition, so the instrument at least offers the reasons that actually occur. Ask after the cancellation rather than during it, when the customer has no reason to hurry and sometimes will explain. Interview a sample properly, since a dozen conversations with recent cancellers routinely surface causes no dropdown would contain. Weight the reasons by the revenue behind them, since the reason most cited and the reason costing the most are frequently different. Report reasons by delivery number, because the first-delivery canceller and the eighteen-month canceller leave for unrelated reasons and pooling them produces an average that describes nobody. And stop planning retention strategy from the dropdown alone, which is the practice this fix exists to end.

## Who Feels the Pain
Operators building strategy on a biased instrument; product teams whose real defects are invisible in the reason data; and customers whose specific problem is recorded as not using it.

## Impact If Fixed
The instrument was designed for a fast exit and is used as research. Behavioural classification is available for every canceller without asking them anything, and calibrating the dropdown against it is a one-off analysis that tells the company how much their existing data is worth.
