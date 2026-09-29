# Pricing That Rewards a Slow Build

**Niche:** [[niches/ci-cd-platforms/pipeline-execution-platforms/profile|Pipeline Execution Platforms]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Pipelines are billed by the minute of wall clock, which means the vendor earns more from a slow build than a fast one and the customer's interest and the vendor's are opposed.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor here is fighting to be where an organisation's pipelines actually run — and that contest is fought on economics in one market and on control in another, which is why this niche is not terminal and is decomposed below.

## The Problem
A platform team spends a quarter making the pipeline forty percent faster. Their vendor's revenue from the account falls correspondingly. The vendor is not sabotaging anything, but every product decision they face — whether to build better caching, whether to make parallelism easier, whether to skip unchanged work — has a revenue cost attached, and the features that would help the customer most are the ones that reduce the bill. The result is a category where caching is a configuration the customer maintains and duration is the customer's problem.

## Why It's Still Broken
Per-minute pricing is simple, transparent and was the obvious model when the product was rented machines. It has become misaligned as the product moved from compute to orchestration. Nobody has offered an alternative because the alternatives are harder to explain and the incumbents have no reason to introduce the comparison. And customers do not experience it as a pricing problem — they experience it as slow pipelines — so the pressure does not arrive in a form the vendor must answer.

## What a Fix Looks Like
Change what is being sold, or at minimum measure the misalignment honestly. Price on pipelines executed, changes delivered or seats rather than on minutes, which aligns the vendor with making them fast and is the structural fix. Where per-minute pricing remains, publish the efficiency metrics anyway — cache hit rate, redundant work, queue time against execution time — since a vendor that reports how much of the customer's spend was unnecessary is making a credible claim no competitor can match. Report cost per change delivered rather than minutes consumed, which is the unit that means something to the buyer and reframes the comparison between vendors. Separate queue time from execution time in billing, because a customer paying for time spent waiting for a runner is paying for the vendor's capacity planning. Offer a shared cache by default rather than as a configured feature, which is the single largest saving and is currently opt-in with a template. And let customers see the counterfactual: what this month would have cost with the improvements available, which is the argument for making them.

## Who Feels the Pain
Platform teams whose vendor is structurally uninterested in their build duration; developers waiting on pipelines nobody is incentivised to shorten; and finance functions paying for redundant work nobody reports.

## Impact If Fixed
The misalignment explains why caching is a customer configuration rather than a platform responsibility, and changing the unit of sale changes what the vendor builds. Reporting redundant work honestly is the strongest available competitive claim for anyone willing to make it.
