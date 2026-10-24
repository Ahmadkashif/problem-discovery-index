# An Analogy Engine for Bases of Estimate

**Niche:** [[niches/defense-systems-manufacturers/cost-proposal-pricing-boe/profile|Cost-Type Proposal Pricing & Bases of Estimate]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Estimators pick analogies for each work element from memory and old proposals, when the company's actuals could show which past jobs really resemble the new one and what they cost.
**Tags:** #k-nearest-neighbors #bayesian-linear-regression #large-language-models #confidence-intervals #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce cost volumes whose bases of estimate survive government evaluation, and whoever's proposals draw the fewest questioned hours in DCAA and DCMA review takes the account.

## The Problem
For each element in the work breakdown structure, an estimator needs a defensible basis: a past job of similar content, its actual hours, and the adjustments for size and complexity. Finding that job means searching proposal archives and asking colleagues. The analogy chosen is often the one the estimator remembers, not the closest, and government evaluators question hours whose analogy doesn't hold up.

## Why Nobody Has Built This
Actuals sit in the cost system by charge number, and charge numbers don't describe work content. Past bases of estimate are documents, not data. Pricing tools were built to add up estimates, not to find them, and proposal data is competition-sensitive and often export-controlled, which keeps generic vendors out.

## What to Build
Index every closed job's work content (from statements of work, work package descriptions and past bases of estimate) against its actual hours and materials. For a new element, retrieve the closest analogies, fit a hierarchical model of hours on size and complexity drivers with an uncertainty range, and draft the basis-of-estimate narrative with citations to the actuals. Record government evaluation findings against each analogy so weak ones stop being used.

## Target Customer
Directors of estimating and pricing at primes and tier-1s preparing development, production and sole-source proposals.

## Impact If Built
Fewer questioned hours on a large production proposal is worth millions of dollars at negotiation (estimate), and estimators spend their time on the elements without a good analogy.
