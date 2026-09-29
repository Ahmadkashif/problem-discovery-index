# The Field as a Running Randomised Trial

**Niche:** [[niches/agtech-platforms/row-crop-farm-management/profile|Row Crop Farm Management]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every modern planter and sprayer can vary its rate by location on command, and a randomised strip trial written into the prescription would answer on this farm what a research plot in another state currently answers by extrapolation.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #bayesian-inference #gradient-boosting #evaluation-metrics #cross-validation #revenue-impact
**Contested on:** Every serious competitor in row crop software is fighting to tell a grower which of their input decisions actually changed the yield on their own ground — and whoever produces credible on-farm effect estimates takes the account.

## The Problem
A grower spends a substantial sum on a fungicide application across every acre. The season is good and the yield is good. Whether the fungicide contributed anything, and whether it contributed enough to justify its cost on this ground, is unknown — and will be unknown next year, and the year after, because the same decision is made the same way every season. A neighbour swears by it. The retailer's trial plot showed a response. The weather that year was different. The equipment that applied it could have applied it to eighty percent of the field in a randomised pattern and answered the question definitively, at no additional cost, and nobody asked it to.

## Why Nobody Has Built This
The platforms are owned by or aligned with companies that sell inputs and equipment, and a capability that reliably tells growers which inputs do not pay on their ground is commercially uncomfortable — which is the most honest explanation for why the best-instrumented industry in agriculture has no on-farm trial capability. Beyond that, the analysis is genuinely non-trivial: yield is spatially autocorrelated, fields have systematic variation in soil and drainage that dwarfs most treatment effects, and a naive comparison of strips will find effects that are entirely topography. Doing it properly requires spatial methods, which is a real requirement and a poor excuse for twenty years of not trying.

## What to Build
Trial design, execution and analysis inside the prescription workflow. The grower selects a question — this nitrogen rate against that one, fungicide against none, two seed populations — and the system generates a randomised strip design that respects the equipment's width, the field's shape and the operational realities of planting and spraying, written directly into the prescription file the machine already consumes. At harvest, yield is attributed to treatment with spatial methods that account for the field's own variation. The output is an effect estimate with an interval and a direct economic translation: this treatment returned this much per acre, plus or minus this much, on this field. Results accumulate across seasons and fields, and across the platform's grower base, so a question that is underpowered on one farm in one year becomes answerable across many — which is the only route to credible answers on the effects that are real and small.

## Target Customer
Growers of 1,000+ acres who make substantial input decisions annually, independent agronomists advising them, and any platform willing to build a capability whose findings will sometimes disadvantage input sellers.

## Impact If Built
Input spend is the largest controllable cost in row crop agriculture and is allocated on evidence from other people's fields. A grower who can measure effects on their own ground reallocates spend toward what works there, which on a large operation is a substantial annual number. The cross-farm accumulation is the larger prize: a platform running thousands of randomised trials a season would generate better agronomic evidence than the plot-trial system that currently produces the industry's recommendations.
