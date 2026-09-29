# An Operating Point Chosen by Trial

**Niche:** [[niches/vector-search-vendors/dedicated-retrieval-infrastructure/profile|Dedicated Retrieval Infrastructure]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Index parameters trade recall against memory, build time and latency in ways the vendor understands precisely and the customer discovers by running experiments for a week.
**Tags:** #convex-optimization #bayesian-optimization #evaluation-metrics #k-nearest-neighbors #graph-theory #confidence-intervals #dimensionality-reduction #norms-and-inner-products
**Contested on:** Every serious competitor in this sub-niche is fighting to hold a required recall and tail latency at the lowest cost per vector at billion scale — and whoever does that takes the account, because the buyer is running the arithmetic against self-hosting and will act on it.

## The Problem
A platform team indexes six hundred million vectors. They must choose a graph connectivity parameter, a build-time search width, a query-time search width, a quantisation scheme and a sharding factor. Each affects recall, memory, build duration and query latency, and the interactions are not monotonic. The documentation gives one example configuration. The team runs a fortnight of experiments on a subset, extrapolates badly because the behaviour is scale-dependent, and settles on something that works. Nobody knows how far it is from the frontier, and the vendor — who has run these parameters across thousands of corpora — knows and does not say.

## Why Nobody Has Built This
Publishing the frontier exposes how much cheaper a well-configured deployment is than a default one, which reduces consumption revenue on usage-based pricing. The relationship is corpus-dependent, so a general table would be wrong and a per-corpus tool is a real build. Parameter tuning is treated as solutions engineering rather than product, which means it is delivered per account and never generalised. And customers do not know to ask, because they have no reference for how much is on the table.

## What to Build
Give the customer the frontier for their own data. Measure the recall-latency-cost surface on a sample of the customer's corpus and their own query distribution, which is a short automated sweep and produces the curve that a fortnight of manual experimentation approximates badly. Let the customer state a target — hold this recall, or this tail latency, at minimum cost — and configure to it, since that is how the requirement actually arrives and the translation into parameters is the vendor's expertise. Report the quantisation trade explicitly: memory saved against recall lost, on this corpus, because quantisation is the largest cost lever available and its accuracy cost is corpus-dependent and rarely measured. Extrapolate from sample to full scale with stated uncertainty, since the scale dependence is what makes manual experimentation unreliable. Re-tune automatically as the corpus grows and shifts, because a configuration chosen at a hundred million vectors is wrong at six hundred million and nothing prompts a revisit. Report the gap between the current configuration and the frontier as a standing number, which is both an honest signal and the strongest possible argument against self-hosting. And publish the methodology so the customer can verify it, since this buyer evaluates everything.

## Target Customer
Platform and infrastructure teams running large retrieval workloads, and the vendors competing against those teams' own engineering.

## Impact If Built
The vendor knows the parameter-to-outcome mapping across thousands of corpora and the customer approximates it with a fortnight of experiments. Reporting the gap between the current configuration and the frontier is the strongest available argument against self-hosting.
