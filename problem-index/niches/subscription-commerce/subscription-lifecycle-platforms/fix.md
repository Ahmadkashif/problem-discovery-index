# A Cadence Chosen at Sign-Up and Never Revisited

**Niche:** [[niches/subscription-commerce/subscription-lifecycle-platforms/profile|Subscription Lifecycle Platforms]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** A customer picks every four weeks from a dropdown before they have used the product once, and that guess governs every delivery for the life of the subscription.
**Tags:** #time-series-forecasting #gradient-boosting #evaluation-metrics #confidence-intervals #revenue-impact #descriptive-statistics #quick-win #causal-inference
**Contested on:** Not terminal — the contest differs by whether the customer chose the contents, and the decomposition is recorded in the profile.

## The Problem
At sign-up a customer is asked how often they want deliveries and picks the default, before having any idea how long the product lasts them. If the answer is wrong the consequences are predictable: too frequent and product accumulates, the value feels poor and they cancel; too infrequent and they run out, buy elsewhere, and discover they do not need the subscription. The platform will happily change the cadence and nobody ever does, because changing it requires the customer to notice the problem, diagnose it correctly and find the setting — three steps that a cancellation avoids.

## Why It's Still Broken
The cadence is a sign-up field rather than an ongoing decision, which is a data model choice with large consequences. Prompting a customer to change it looks like inviting them to reduce frequency and therefore revenue, which is the same fear that buries the flexibility tools. Consumption is unobserved in most categories, which makes the correct cadence feel unknowable — though the behavioural signals are usually sufficient. And the failure presents as churn rather than as a cadence problem.

## What a Fix Looks Like
Treat cadence as a prediction that updates. Estimate the right cadence per subscriber from whatever consumption signal exists — reorder behaviour before subscribing, skips, swaps, returns, engagement, and in some categories direct usage data — and propose a change proactively, which is the fix and which reframes cadence from a setting to a recommendation. Ask explicitly after the second delivery whether the timing is right, which is a single question at the moment the customer can answer it and is not asked by anybody. Read a skip as a cadence signal rather than as a lost charge, since a customer skipping every other delivery has told you their cadence is wrong in the clearest possible terms and the system records a revenue event. Offer cadence change prominently in the cancel flow ahead of a discount, since the cadence is frequently the actual problem and a cheaper subscription does not fix it. Default to a conservative cadence at sign-up rather than the most frequent, and measure the retention effect, since the revenue-maximising default at sign-up is frequently the churn-maximising one over a year. Report cadence mismatch as a diagnosed churn cause. Test cadence changes for their effect on lifetime value rather than on next-month revenue. And let the customer express the decision in their terms — I have too much, I run out — rather than in weeks.

## Who Feels the Pain
Customers accumulating product they did not need or running out of what they rely on; operators losing subscribers to a dropdown choice made before any information existed; and retention teams offering discounts for a timing problem.

## Impact If Fixed
A skip is the clearest possible statement that the cadence is wrong and is recorded as a lost charge. Asking one question after the second delivery, at the moment the customer can answer it, is asked by nobody and diagnoses the problem directly.
