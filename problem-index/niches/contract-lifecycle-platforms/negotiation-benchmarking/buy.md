# Benchmarking Products Built Everywhere Else

**Niche:** [[niches/contract-lifecycle-platforms/negotiation-benchmarking/profile|Negotiation Benchmarking]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Compensation, procurement pricing and advertising rates are all benchmarked by vendors pooling customer data under established governance, and contract terms are not.
**Tags:** #descriptive-statistics #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #k-means-clustering #causal-inference #compliance
**Contested on:** Every serious competitor here is fighting to tell a legal team what terms are actually achievable — with this counterparty, at this deal size, in this industry — and whoever assembles that corpus holds a position no single company can replicate.

## The Problem
Pooling sensitive customer data to produce benchmarks is a solved commercial and governance pattern: compensation benchmarking, procurement price benchmarking, media rate benchmarking and payroll benchmarking all work this way, with established norms about aggregation thresholds, anonymisation and contribution reciprocity. Contract terms — where the demand is obvious and constant — have no equivalent, and the obstacle is that nobody has done the governance work rather than that the pattern is unproven.

## What Already Exists
The benchmarking product pattern with its established governance conventions; statistical disclosure control methods with a formal literature; hierarchical Bayesian estimation for small cells, which is exactly the situation when slicing by counterparty and deal size; differential privacy where stronger guarantees are wanted; and the entire commercial playbook for contribute-to-receive data cooperatives.

## The Customization Gap
The adaptation is to legally privileged and commercially sensitive material. It requires: (1) an extraction layer that produces normalised positions and never content, so what enters the corpus is a structured fact rather than text — which is the technical precondition for the governance story being true rather than asserted; (2) disclosure control calibrated to a setting where a single counterparty may dominate a cell, since revealing what one named company agreed to is exactly the harm to avoid and naive thresholds will not prevent it; (3) hierarchical estimation, because the useful slices are small and pooling with shrinkage is what makes them reportable at all; (4) a contribution model that is fair and visible, since customers will reasonably ask what they get and what they give; and (5) a governance statement written for general counsel, who are the buyers and are professionally sceptical, which means the design must be defensible on its own terms rather than reassuring.

## Target Customer
CLM vendors with large installed bases, legal data providers, industry associations, and the benchmarking vendors already operating this model in adjacent categories.

## Impact If Solved
The pattern is proven repeatedly in adjacent markets and the demand here is unambiguous, which leaves governance design as the binding constraint. Normalised-positions-only extraction and disclosure control sized for dominant counterparties are the two things that make it defensible.
