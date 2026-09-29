# Lifetime Value Assumed Rather Than Measured

**Niche:** [[niches/d2c-brand-operators/growth-and-retention-stack/profile|Growth & Retention Stack]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Acquisition decisions are justified by a lifetime value figure that is an assumption multiplied by a first order, and the brand has the cohort data that would replace it with a measurement.
**Tags:** #survival-analysis #confidence-intervals #revenue-impact #descriptive-statistics #hypothesis-testing #gradient-boosting #quick-win #evaluation-metrics
**Contested on:** Not terminal — the contest differs by whether the customer has bought before, and the decomposition is recorded in the profile.

## The Problem
A brand justifies a customer acquisition cost of sixty dollars with a lifetime value of a hundred and eighty. The hundred and eighty comes from an average order value multiplied by an assumed repeat rate over an assumed lifetime, numbers chosen two years ago when the brand was smaller and its customers were different. Actual cohorts from the last eighteen months are in the order database and show a materially lower figure, varying enormously by acquisition channel. Nobody has computed it, so the brand continues acquiring customers at a loss it could measure, with confidence derived from a multiplication.

## Why It's Still Broken
The assumed figure is convenient and supports the spending everyone wants to do. Computing it properly requires cohort analysis with survival methods on censored data, which is slightly beyond a spreadsheet. Recent cohorts have not yet lived long enough to observe their full value, which is used as a reason not to estimate rather than as a reason to estimate with a model. And a lower number would require cutting spend, which nobody proposes voluntarily.

## What a Fix Looks Like
Measure it from the cohorts. Compute realised cohort value by acquisition month and channel from the order history, which the brand holds, which takes days rather than months, and which frequently changes the entire acquisition strategy — this is the fix. Use survival methods to project immature cohorts rather than waiting or guessing, since the censoring is the reason the measurement is avoided and it is exactly what those methods handle. Report by acquisition channel and campaign, because the variation is large and the average conceals that one channel is profitable and another is not. Report contribution margin rather than revenue, which requires the order-level margin work and which frequently halves the figure. Discount future value, since a dollar in year three is not a dollar now and undiscounted lifetime value systematically overstates. Report the confidence interval, since early cohorts are small and a point estimate invites over-confidence in both directions. Track the assumed figure against the realised one and report the gap, which is the accountability that stops the assumption drifting free again. And bound acquisition spend by measured payback period rather than by a ratio to an assumed lifetime value, since payback is observable and lifetime value is projected.

## Who Feels the Pain
Brands acquiring customers at a measurable loss; investors funding growth against an assumption; and the retention teams blamed for a repeat rate that acquisition's channel mix determined.

## Impact If Fixed
The data to replace the assumption with a measurement is in the order database and takes days. Survival projection of immature cohorts removes the excuse for not measuring, and reporting by channel exposes that the average conceals a profitable channel and an unprofitable one.
