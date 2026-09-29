# Autonomous Operation Research Nobody Has Shipped

**Niche:** [[niches/database-platform-vendors/managed-database-services/profile|Managed Database Services]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Self-tuning databases have been an active research area for twenty-five years with real results, and managed services ship the same defaults to every customer.
**Tags:** #bayesian-optimization #gradient-boosting #optimization-fundamentals #convex-optimization #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to run a database well enough that the customer never thinks about it — and that contest is fought on latency in one market and on query cost at scale in another, which is why this niche is not terminal and is decomposed below.

## The Problem
Automated index selection, self-tuning configuration, workload-driven physical design and automatic partitioning have been researched since the late nineties, with published algorithms, advisor tools shipped in several commercial databases, and a recent wave of learned approaches. Managed services largely ship the engine's defaults, offer a sizing choice, and leave the rest to the customer — which is the least the research would support.

## What Already Exists
Index and physical design advisors in several commercial engines; automated knob tuning research including Bayesian optimisation approaches with published results; workload forecasting; learned query optimisation research; and the self-driving database literature. Substantial published work and several open implementations.

## The Customization Gap
The adaptation is to a multi-tenant managed service where a wrong change is a customer incident. It requires: (1) safety as the primary constraint rather than optimality, since the research optimises performance and a managed service must first not break anything — which means preferring reversible changes, staged application and automatic reversion over the best configuration found; (2) fleet priors, because tuning a single database from its own workload is slow and a vendor observing thousands of similar workloads can start from a strong prior, which is the advantage they uniquely have and do not use; (3) workload stability assessment, since tuning to a workload that is about to change is worse than leaving defaults, and detecting stability is a precondition rather than a refinement; (4) an explicit objective chosen by the customer, because tuning for throughput, tail latency or cost produces different configurations and the research usually assumes one; and (5) explainability, since a customer whose database was changed automatically will ask what changed and why during the next incident, and an unexplainable change will cause the whole capability to be disabled.

## Target Customer
Managed database vendors, database engine vendors, and the platform teams operating large fleets internally.

## Impact If Solved
Twenty-five years of tuning research exists and the services ship defaults, which is a striking gap for a product whose value proposition is operation. Fleet priors are the vendor's unique advantage and safety-first application is what makes the research deployable.
