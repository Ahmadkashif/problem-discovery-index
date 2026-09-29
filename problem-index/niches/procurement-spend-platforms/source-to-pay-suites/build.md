# Spend Under Management Measured Honestly

**Niche:** [[niches/procurement-spend-platforms/source-to-pay-suites/profile|Source-to-Pay Suites]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Procurement's headline metric is the share of spend under management, every organisation defines it differently and generously, and nobody measures what the unmanaged remainder is costing.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #causal-inference #revenue-impact #compliance #data-integration
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A procurement function reports 78% of spend under management. The definition includes any spend with a contracted supplier, whether or not the transaction went through a controlled process, whether or not the contracted price was applied, and whether or not procurement was involved in the decision. The 22% remainder is described as tail spend and is not analysed. What nobody computes is the thing the metric is a proxy for: what the organisation is paying above what it would pay if the spend were properly managed, by category, which is the number that would tell procurement where to spend its own effort and would tell finance what the function is worth.

## Why Nobody Has Built This
Spend under management is a definitional metric that each organisation constructs favourably, and the vendors report whatever definition the customer configures, because a lower number is a worse story for both parties. Measuring the cost of unmanaged spend requires a counterfactual — what this would have cost under a contract — which needs the cross-customer price data that this industry's own analysis section identifies as the great unexploited asset. And savings measurement in procurement is a long-standing exercise in negotiated definitions rather than in measurement, which has left the whole function without a credible efficacy number.

## What to Build
Replace the definitional metric with a measured one. For every transaction, determine whether a contracted alternative existed and at what price — which requires the contract price data the compliance niche describes and the classification the first niche provides. The gap between paid and available is the cost of unmanaged spend, computed per category and per business unit, which is a real number rather than a definitional one. Where no contracted alternative exists, the comparison is against the platform's cross-customer price distribution for the same item and comparable volumes, stated as a benchmark with its uncertainty. From that, procurement gets the thing it has never had: a ranked list of where the money is going unnecessarily, which is also a ranked list of where its own effort is worth most. The savings claim becomes measured rather than negotiated, which is uncomfortable in the first year and is the only route to the function being taken seriously by finance.

## Target Customer
Chief procurement officers whose savings numbers are disputed by finance, procurement platform vendors, and the finance organisations trying to assess what the procurement function returns.

## Impact If Built
Procurement's credibility problem with finance is entirely a measurement problem — savings are asserted against baselines the function itself chooses. A measured cost of unmanaged spend, computed transaction by transaction against contracted and benchmark prices, is both a more honest number and a better prioritisation instrument than the definitional metric it replaces.
