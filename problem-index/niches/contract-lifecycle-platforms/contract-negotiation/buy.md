# Negotiation Research Nobody Has Operationalised

**Niche:** [[niches/contract-lifecycle-platforms/contract-negotiation/profile|Contract Negotiation]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Negotiation has a substantial empirical literature on anchoring, concession patterns and reservation values, and contract negotiation software has never encoded any of it.
**Tags:** #bayesian-inference #gradient-boosting #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #causal-inference
**Contested on:** Every serious competitor here is fighting to get to an agreed contract faster and on better terms — and that contest splits between removing the routine edits and knowing which positions are achievable, which is why this niche is not terminal and is decomposed below.

## The Problem
There is decades of empirical work on how negotiations resolve: the effect of the opening position, how concessions are read, how information asymmetry shifts outcomes, how time pressure changes reservation values. There is also, inside every CLM system, a complete record of thousands of negotiations with their opening positions, their exchanges and their outcomes. Neither the research nor the record informs what a lawyer does on a Tuesday.

## What Already Exists
Negotiation and bargaining research in economics and psychology; sequential decision modelling; Bayesian updating for inference about a counterparty's reservation value; outcome modelling with standard supervised methods; and survival analysis for cycle time. CLM systems hold the exchange history. The commercial negotiation analytics that exist are descriptive summaries rather than anything built on this.

## The Customization Gap
The adaptation is to clause-level positions in a repeated commercial setting. It requires: (1) a representation of a position on a provision that is comparable across contracts — a liability cap as a multiple of fees rather than as a number, an exclusivity as a scope and duration — since without normalisation there is no corpus, only anecdotes; (2) counterparty modelling from their own negotiation history, since the useful inference is about this counterparty rather than about negotiators in general, and large counterparties appear in many customers' records; (3) an outcome definition beyond signed, because a contract signed on poor terms is not a success and the objective must weigh terms and cycle time together; (4) honest treatment of confounding, since the deals where a company holds firm are systematically different from those where it concedes, and a naive analysis will conclude that holding firm works; and (5) presentation as evidence rather than instruction, because counsel will not accept a recommendation and will very much accept being told what happened the last forty times this position was taken.

## Target Customer
CLM vendors with a multi-customer corpus, legal operations functions, and the negotiation analytics vendors currently selling descriptive dashboards.

## Impact If Solved
An empirical literature and a complete transactional record both exist and neither reaches the negotiating table. Position normalisation is the foundational work, and honest handling of confounding is what separates evidence from a dashboard that confirms whatever counsel already believed.
