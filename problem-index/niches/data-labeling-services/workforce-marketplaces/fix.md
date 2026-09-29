# Paying for Speed on Tasks That Need Care

**Niche:** [[niches/data-labeling-services/workforce-marketplaces/profile|Workforce Marketplaces]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** The piece rate was designed for volume work and is applied to expert judgement, where it pays people to decide quickly on tasks whose entire value is that somebody thought carefully.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #worker-facing #quick-win #revenue-impact
**Contested on:** Every serious competitor here is fighting to put the right capable contributor on the right task within days of a contract being signed — and whoever does that takes the delivery, because sourcing and matching at speed is now the binding constraint rather than labour supply.

## The Problem
An expert is paid per completed assessment. A careful assessment of a complex reasoning trace takes eleven minutes; a plausible one takes three. The pay is identical. The reviewer catches some of the difference and not all of it, because distinguishing a fast correct judgement from a fast careless one is exactly the hard problem. The rational contributor behaviour under this structure is to work quickly, and the quality mechanism is then asked to detect the consequence — which is an expensive way to address an incentive the vendor chose.

## Why It's Still Broken
Piece rates were correct for volume work, where the task is short, the quality is checkable and the throughput is the product, and they were carried into expert work without revisiting the assumption. Hourly payment introduces a different problem — paying for time without output — which is the reason the industry has resisted it, and the middle positions have not been designed. The cost of the misaligned incentive lands in quality, which is attributed to contributors rather than to the pay structure. And changing pay structures is commercially consequential enough that nobody experiments.

## What a Fix Looks Like
Pay for what the task actually requires. Set the piece rate from the observed careful completion time rather than from a target throughput, which at least makes careful work economically viable — the rate is frequently set against an optimistic duration that only careless work achieves. Use hybrid structures on expert work: a guaranteed rate for time with a quality component, which is what professional assessment work uses elsewhere and which the industry has not tried. Pay for correction and rationale explicitly, since the rationale is frequently the product at this tier and is currently unpaid effort. Remove the penalty on slow careful work, which the current structure imposes implicitly. Measure the relationship between time taken and assessed quality per task type, which establishes what careful actually costs and is a straightforward analysis over data the platform holds — and which usually shows a clear threshold. Test alternative structures on a subset, which is an experiment the platform can run and nobody has. And report the quality-per-cost outcome rather than cost-per-task, since a cheaper task that must be redone or reviewed is not cheaper.

## Who Feels the Pain
Expert contributors paid the same for careful and careless work; customers receiving data produced under an incentive to be quick; and vendors spending on review to detect a problem their pay structure creates.

## Impact If Fixed
The time-versus-quality relationship is computable from platform data and would establish what careful work actually costs, which is currently assumed. Paying for the rationale rather than treating it as unpaid effort aligns the incentive with the product at the tier where the rationale is the product.
