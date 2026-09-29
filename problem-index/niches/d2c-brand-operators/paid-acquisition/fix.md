# Retargeting Counted as Acquisition

**Niche:** [[niches/d2c-brand-operators/paid-acquisition/profile|Paid Acquisition]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Advertising shown to people who already know the brand, already visited, or already bought is reported in the same acquisition figure as advertising that reached somebody new, which flatters the number and misdirects the budget.
**Tags:** #causal-inference #evaluation-metrics #descriptive-statistics #confidence-intervals #revenue-impact #hypothesis-testing #quick-win #logistic-regression
**Contested on:** Every serious competitor in this sub-niche is fighting to buy an incremental new customer for less than the next brand bidding on the same impression — and whoever does that survives, because the auction price rises structurally and the margin between cost and value is the whole business.

## The Problem
A brand reports a blended return on ad spend that looks acceptable. Inside it, a large share of the conversions came from people who had already visited the site, were already on the email list, or had already bought — reached again by retargeting and by broad campaigns that the platform's optimisation naturally steers toward the easiest conversions. Those people would mostly have bought anyway. The genuinely new-customer acquisition, which is the only part that grows the business, performs far worse than the blended figure and is invisible inside it. The brand scales spend on the blended number and the new customer count does not move.

## Why It's Still Broken
Blended reporting is the default and separating new from returning requires joining platform data to the customer database. The platform's optimisation legitimately seeks the cheapest conversion, which is a known customer, so the drift toward retargeting is automatic unless actively prevented. The blended figure is the one everybody reports and comparing to it is how teams are judged. And the harm — spend growing while new customers do not — takes quarters to become obvious.

## What a Fix Looks Like
Separate the two and report them apart. Split all acquisition reporting into new-customer and existing-customer conversions using the brand's own order history, which is a join the brand can make and which immediately reveals the composition of a number everybody has been scaling — this is the fix and it takes days. Report cost per new customer as the primary acquisition metric, since that is what the spend is for and the blended figure is not it. Exclude existing customers from prospecting campaigns actively, which the platforms support and which many brands do not configure. Measure retargeting incrementally with a holdout, since it is the easiest incrementality test to run and routinely shows the smallest effect of any channel. Budget retargeting separately, so it competes with retention rather than with acquisition — because it is retention wearing an acquisition costume. Feed new-customer conversions as the optimisation signal for prospecting campaigns, so the platform optimises toward the objective rather than toward the cheapest conversion available. Report new customer count and cost as the headline growth metrics. And check the split whenever performance improves suddenly, since a sudden improvement is frequently the mix shifting rather than the performance changing.

## Who Feels the Pain
Brands scaling spend against a number whose composition they have not examined; growth leads defending a blended figure that is doing worse than it appears; and investors funding growth that is partly re-buying existing customers.

## Impact If Fixed
The split is a join the brand can make in days and it reveals the composition of the number everybody scales. Feeding new-customer conversions as the prospecting signal stops the platform optimising toward the cheapest conversion, which is always somebody who already knew the brand.
