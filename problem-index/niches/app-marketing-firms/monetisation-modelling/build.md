# The Number Every Decision Divides By

**Niche:** [[niches/app-marketing-firms/monetisation-modelling/profile|Monetisation Modelling]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lifetime value sums three quite different revenue processes into one figure that every acquisition decision divides by, and it is computed by extrapolation and rarely checked.
**Tags:** #survival-analysis #time-series-forecasting #bayesian-inference #confidence-intervals #probability-distributions #evaluation-metrics #revenue-impact #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to establish what a user is actually worth over their life, across purchases, subscriptions and advertising revenue — and whoever does that correctly sets the number every acquisition decision divides by.

## The Problem
A user's value comes from in-app purchases, which are extremely skewed with a small number of users producing most of the revenue; from subscriptions, which renew with their own retention curve and churn dynamics; and from advertising impressions, whose value depends on a mediation stack, seasonal rate fluctuation and how many sessions the user has. These are summed into one figure by extrapolating a cohort curve. Every acquisition decision divides by that figure. The tail is systematically underestimated by averaging, the three processes are frequently modelled as one, and nobody has checked the figure against realised value at the horizons used for payback.

## Why Nobody Has Built This
The figure sits with product or monetisation while the decisions that use it sit with acquisition, so nobody owns the accuracy of the thing both depend on — the split ownership is the structural cause. Curve extrapolation is simple, familiar and produces a plausible number. The revenue distribution's skew makes averages misleading in ways that require deliberate treatment. And validation requires waiting out the horizon, which nobody does.

## What to Build
Model the three processes separately and validate the sum. Model purchase, subscription and advertising revenue with their own dynamics rather than as one curve, which is the core — they have different retention structures, different seasonality and different tails, and summing before modelling discards all of it. Handle the purchase tail explicitly, since a small fraction of users produce most of the revenue and a model fitted to the average is wrong about exactly the users that matter. Model advertising revenue from sessions and rates rather than allocating it evenly, which is the crudest part of most implementations and is directly improvable. Produce a distribution rather than a point, so the payback decision can account for the uncertainty that a skewed revenue process genuinely carries. Validate against realised value at the payback horizon, which is the check nobody runs and is what would establish whether the denominator has been right. Differentiate by acquisition source, since users from different channels have genuinely different value curves and a global figure misprices every channel. Update as the app's monetisation changes, because a curve fitted to last year's pricing is wrong after a change and nobody re-fits. Reconcile with finance's own revenue recognition, since the two numbers should agree and frequently do not. Provide the figure with its uncertainty to the acquisition team, so bidding can reflect what is known. And report prediction error at the payback horizon, since that single figure tells the business whether its entire acquisition economics is calibrated.

## Target Customer
Product and monetisation leadership, user acquisition teams whose decisions divide by this figure, and analytics vendors whose lifetime value features extrapolate a curve.

## Impact If Built
The figure sits with one team and the decisions with another, so nobody owns the accuracy of what both depend on. Modelling purchases, subscriptions and advertising separately preserves the different tails and dynamics that summing before modelling discards.
