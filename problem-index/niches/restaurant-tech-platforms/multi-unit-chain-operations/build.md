# A Comparability Layer Under the Consolidated Report

**Niche:** [[niches/restaurant-tech-platforms/multi-unit-chain-operations/profile|Multi-Unit Chains — Making Units Comparable]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Above-store reporting consolidates forty units into one number and none of the products underneath establish that the forty inputs mean the same thing, so the consolidated number is precise and not comparable.
**Tags:** #hypothesis-testing #descriptive-statistics #k-means-clustering #confidence-intervals #evaluation-metrics #feature-engineering #compliance #data-integration
**Contested on:** Every serious competitor selling to multi-unit restaurant operators is fighting to make forty locations' numbers mean the same thing, so that an underperforming unit can be identified rather than argued about — and whoever makes units genuinely comparable takes the account.

## The Problem
Unit 23 shows food cost three points above the group. The operations director calls. The general manager explains that unit 23 is the only one recording waste properly, that the neighbouring units bury it in inventory variance, and that the item mapping for two high-volume dishes was changed by a district manager in the spring. He is probably right. Nobody can settle it, so the meeting ends inconclusively and the real question — whether unit 23 is actually worse — is never answered. This exchange happens weekly in every multi-unit operator in the country.

## Why Nobody Has Built This
Above-store products were built to consolidate, and consolidation is a reporting problem that looks finished once the numbers add up. Establishing comparability requires the vendor to assert that a unit's data is wrong, which is a harder product posture and creates support conversations nobody wants. It also requires modelling what a comparable measurement means for each metric — a different answer for waste, labour, item mix and comps — which is domain work rather than engineering. And the customer has not asked, because the customer's mental model is that the report is the truth and the argument is about operations.

## What to Build
A comparability layer that scores every unit's data on each metric before anything is consolidated, and publishes the score alongside the number. Waste reporting completeness is estimable from the relationship between theoretical and actual usage, and a unit reporting implausibly little waste is detectable statistically. Item mapping drift is detectable by comparing each unit's item catalogue against the group's canonical one and against its own history. Labour category application is comparable across units with similar volume and service model. Comp and void practice is a distribution that can be compared. The output is not a scolding but a weighting: a variance from a unit with poor data quality on that metric is flagged as uninterpretable rather than treated as a finding, and the data quality issue becomes the action item instead of the phantom performance issue.

## Target Customer
Multi-unit restaurant groups and franchise systems above roughly fifteen units, and the above-store reporting vendors whose consolidated numbers are currently precise about inconsistent inputs.

## Impact If Built
Above-store teams stop spending their week adjudicating whether variances are real, which is most of what they currently do, and start acting on the ones that are. The comparability score is also the thing that makes every other above-store analytic trustworthy — forecasting, benchmarking and target setting across units are all built on an assumption of comparability that nobody has checked.
