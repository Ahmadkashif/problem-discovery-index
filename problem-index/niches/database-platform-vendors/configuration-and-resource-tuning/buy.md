# Bayesian Optimisation Over a Parameter Space

**Niche:** [[niches/database-platform-vendors/configuration-and-resource-tuning/profile|Configuration & Resource Tuning]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Optimising an expensive black-box function over a moderate parameter space is exactly what Bayesian optimisation was built for, and database configuration is set from a formula.
**Tags:** #bayesian-optimization #gaussian-processes #optimization-fundamentals #monte-carlo-methods #confidence-intervals #evaluation-metrics #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to replace a decade of blog posts with a configuration derived from this workload on this hardware — and whoever does that takes the platform team, because the defaults suit almost nobody and the guidance available was written for different machines.

## The Problem
A moderate number of parameters, an objective that can only be evaluated by running the system, each evaluation expensive, and interactions between the parameters — this is the standard setting for Bayesian optimisation, which has mature libraries, a substantial literature and published results on database tuning specifically. The practice in the field is a formula based on memory size.

## What Already Exists
Bayesian optimisation libraries with Gaussian process and tree-based surrogates; published database knob tuning research with reported improvements; transfer learning for warm-starting optimisation from related tasks; multi-objective optimisation for the throughput-against-latency trade-off; and workload replay tooling in several engines.

## The Customization Gap
The adaptation is to a production system that cannot be freely experimented on. It requires: (1) warm starting from the fleet, since a cold Bayesian optimisation needs many evaluations and each is expensive, while a prior built from thousands of similar workloads reduces it dramatically — this is the adaptation that makes the approach practical and is available only to a vendor with a fleet; (2) evaluation on a replayed workload rather than on production, which requires capture and replay fidelity good enough that the optimum transfers, and validating that transfer is part of the work; (3) safety constraints as hard bounds, because some parameter combinations risk instability or data loss and an optimiser exploring freely will eventually find one; (4) multi-objective treatment with an explicit trade-off, since throughput and tail latency conflict and the customer must choose rather than the optimiser assuming; and (5) non-stationarity, because the workload drifts and an optimum found three months ago may no longer be one, which argues for continuous low-rate refinement rather than a one-off campaign.

## Target Customer
Managed database vendors, database engine vendors, tuning and monitoring product vendors, and large platform teams.

## Impact If Solved
The method is standard, the published results are real, and the practice is a formula. Fleet warm-starting is what makes the evaluation budget acceptable, and hard safety constraints are what make it deployable against production systems.
