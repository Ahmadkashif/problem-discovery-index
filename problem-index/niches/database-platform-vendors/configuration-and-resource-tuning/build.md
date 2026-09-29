# Defaults That Suit Almost No Workload

**Niche:** [[niches/database-platform-vendors/configuration-and-resource-tuning/profile|Configuration & Resource Tuning]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every engine ships hundreds of tunable parameters with defaults that suit almost no workload, and the guidance available is a decade of blog posts written for different hardware.
**Tags:** #bayesian-optimization #gradient-boosting #optimization-fundamentals #monte-carlo-methods #confidence-intervals #evaluation-metrics #automation #cross-validation
**Contested on:** Every serious competitor here is fighting to replace a decade of blog posts with a configuration derived from this workload on this hardware — and whoever does that takes the platform team, because the defaults suit almost nobody and the guidance available was written for different machines.

## The Problem
A team deploys a database on a machine with a large amount of memory. The default configuration allocates a small fraction of it, because the default must be safe on a laptop. The team searches, finds a widely cited article, applies its formulas, and improves things. The article was written for a different version on spinning disks, several of its recommendations are now counterproductive, and none of it accounts for the fact that this workload is write-heavy with long transactions. The configuration is now better than default and substantially worse than achievable, and nobody will revisit it until something breaks.

## Why Nobody Has Built This
Formula-based calculators were the available answer when the only inputs were hardware specifications, and they persist because they are simple and better than defaults. Doing it properly requires the workload, which means either replaying it or experimenting on production, and neither has been packaged safely. The parameters interact substantially, which defeats the one-at-a-time reasoning most guidance uses. And the managed service vendors, who observe thousands of workload-and-configuration pairs with their outcomes, use that corpus for capacity planning rather than for a tuning prior.

## What to Build
Derive the configuration from the workload, starting from fleet evidence. Characterise the workload from what the engine already records — read and write mix, transaction duration distribution, working set size relative to memory, concurrency, query shapes — which is the input every formula-based calculator ignores and is the dominant variable. Start from a fleet-derived prior: this workload resembles a large population the vendor has observed, and their configurations and outcomes are a far better starting point than a formula, which is the managed vendors' unique and unused advantage. Refine by experiment where it is safe, using a replayed workload on a clone for the risky parameters and staged production application with automatic reversion for the safe ones, which is what makes tuning possible for a team that will not experiment on production. Model the interactions rather than tuning one parameter at a time, since the significant gains come from combinations and sequential adjustment finds a local optimum at best. State the objective explicitly, because tuning for throughput, tail latency or recovery time produces different configurations and the current guidance assumes one silently. Re-evaluate as the workload changes, since a configuration tuned to last year's workload is the situation most estates are already in. And report the measured effect of every change, which is what the whole practice currently lacks.

## Target Customer
Platform teams operating databases without a specialist, managed service vendors, and the database monitoring and tuning vendors.

## Impact If Built
The problem is well posed with an observable objective and the practice is folklore, which is an unusual gap. Workload characterisation is the missing input and fleet priors are the shortcut that makes good configuration reachable without a long experimental campaign.
