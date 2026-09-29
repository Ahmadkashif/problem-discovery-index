# The Curve Extended by Eye

**Niche:** [[niches/app-marketing-firms/monetisation-modelling/profile|Monetisation Modelling]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The six-month value is a thirty-day cohort curve extended by a multiplier somebody derived once, applied to every channel and every cohort identically.
**Tags:** #confidence-intervals #evaluation-metrics #hypothesis-testing #descriptive-statistics #quick-win #survival-analysis #revenue-impact #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to establish what a user is actually worth over their life, across purchases, subscriptions and advertising revenue — and whoever does that correctly sets the number every acquisition decision divides by.

## The Problem
Thirty-day revenue per user is multiplied by a factor to estimate six-month value. The factor was derived from an older cohort, possibly before a monetisation change, and is applied identically to users from every channel, every geography and every acquisition source. Channels genuinely differ in how their users mature — some acquire users who monetise early and churn, others acquire slow-building high-retention users — and a single multiplier prices the first too highly and the second too cheaply, systematically, in every allocation decision the team makes.

## Why It's Still Broken
The multiplier is simple, produces a number quickly and has never obviously failed — a single factor that is approximately right on average conceals being badly wrong per channel, which is exactly where it is used. Deriving per-channel factors requires cohort data nobody has assembled. The error is a systematic misallocation rather than a visible failure. And nobody has compared the projection to the realised value.

## What a Fix Looks Like
Derive the extrapolation per segment and check it. Compute the actual thirty-day to six-month ratio per channel from cohorts old enough to have one, which is the fix, uses data the team already has, and almost always reveals differences large enough to change allocation. Report the variation across channels, since the finding is that a single multiplier cannot be right for all of them and seeing the spread is what makes that concrete. Update the factors as new cohorts mature, rather than using one derived years ago. Recompute after any monetisation change, because that is what invalidates them and the trigger is known. Attach uncertainty, since a factor estimated from a few cohorts carries real error and the payback decision should reflect it. Differentiate by geography and platform as well as by channel, where the data supports it. Compare projected against realised for past cohorts as a standing report, which is the validation and is a day's work. Model the curve shape rather than using a single multiplier, since channels differ in the shape of maturation and not only in the level. Explain the change to finance, since payback numbers will move and the reason should be understood as a correction rather than a decline. And report the allocation difference the correction produces, because that figure justifies doing it properly.

## Who Feels the Pain
Teams systematically overpaying for fast-monetising churning users and underpaying for slow-building ones; finance receiving payback numbers built on a stale factor; and channels priced wrongly in a consistent direction for years.

## Impact If Fixed
A single factor that is approximately right on average is badly wrong per channel, which is exactly where it is applied. Computing the ratio per channel from matured cohorts uses data already held and reliably reveals differences large enough to change allocation.
