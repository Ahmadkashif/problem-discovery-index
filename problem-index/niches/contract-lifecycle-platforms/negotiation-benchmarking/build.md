# The Question Answered From One Lawyer's Memory

**Niche:** [[niches/contract-lifecycle-platforms/negotiation-benchmarking/profile|Negotiation Benchmarking]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a position is achievable is the question in-house counsel asks most often, and it is answered from the recall of whoever has been at the company longest.
**Tags:** #bayesian-inference #gradient-boosting #logistic-regression #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor here is fighting to tell a legal team what terms are actually achievable — with this counterparty, at this deal size, in this industry — and whoever assembles that corpus holds a position no single company can replicate.

## The Problem
Counsel is negotiating with a large enterprise customer who has refused a mutual liability cap. The question is whether to hold. The general counsel's view is that this counterparty never moves on it. That view comes from three negotiations over six years, two of which involved a different counterparty team and one of which was a much smaller deal. Elsewhere in the vendor's customer base, that same counterparty has agreed to a mutual cap on a meaningful share of comparable agreements. Nobody can see this, so the position is conceded and the company carries the exposure.

## Why Nobody Has Built This
Cross-customer analysis of contract data is the most sensitive thing a CLM vendor could propose, and no vendor has done the work to articulate a form of it that legal buyers would accept — so it is avoided rather than designed, which leaves the asset idle. Normalising positions across contracts is also a genuine data problem: a liability cap expressed as a fixed sum, as a multiple of fees, and as fees paid in the preceding twelve months are three different objects that must become comparable before any corpus exists. And the vendors' commercial instinct has been to sell workflow, which is easier to demonstrate than evidence.

## What to Build
The corpus, governed properly, and the answer built on it. Normalise positions into comparable form per provision — a cap as a multiple, an exclusivity as scope and duration, a notice period in days — which is the foundational work and is what turns thousands of contracts into a dataset. Aggregate outcomes by counterparty, industry, deal size and geography, with minimum cohort thresholds so that nothing identifiable is ever exposed. Address the confounding honestly, since the deals where a position was held are systematically different from those where it was conceded, and the useful statement is about comparable deals rather than about all of them. Model the counterparty specifically where volume allows, because that is the question actually being asked and large counterparties appear across many customers. Report the cost of holding a position in cycle time as well as its success rate, since that trade-off is the decision. And build the governance into the product rather than into a contract: aggregate only, thresholds enforced, terms only and never content, customer opt-in, and a public statement of exactly what is analysed — because in this category the governance is the product's licence to exist.

## Target Customer
General counsel and commercial leadership, and the CLM vendors with a large installed base, for whom this is the only genuinely non-replicable asset they hold.

## Impact If Built
The corpus answers the question the legal function asks most and can be answered by nobody else, which is a rare position. Position normalisation is the enabling work and the governance design is what determines whether the product can exist at all.
