# Configuration & Resource Tuning

**Parent Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to replace a decade of blog posts with a configuration derived from this workload on this hardware — and whoever does that takes the platform team, because the defaults suit almost nobody and the guidance available was written for different machines.

## Profile
**Market Size:** ~$1.6B US attributable to database tuning, configuration and performance services
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** Low — tuning is specialist work or is not done
**Target Buyer:** Platform engineering and database teams
**Automation Potential:** Very High — this is a well-posed optimisation with an observable objective

## What Makes This a Distinct Niche
Every engine ships hundreds of tunable parameters with defaults chosen to be safe on unknown hardware, which means they suit almost no production workload. The guidance available to a team without a specialist is a decade of blog posts written for different hardware, different versions and different workloads, offering formulas that were reasonable in 2014. The consequences are ordinary and expensive: memory allocation that leaves most of the machine unused, parallelism settings that cause contention, checkpoint and write settings that produce latency spikes, and autovacuum thresholds that let bloat accumulate. This is a distinct contested surface because it is a genuinely well-posed optimisation problem — a parameter space, an observable objective, and a workload that can be replayed — and because the vendors operating fleets have exactly the evidence that would solve it and use it for capacity planning.

## Current Tools & Gaps
Configuration calculators based on formulas, engine documentation, advisor features in some commercial engines, and consultancy. The gaps: the calculators use hardware-derived formulas that ignore the workload entirely, which is the main variable; nothing measures the effect of a change, so tuning is done once and never validated; parameter interactions are significant and no formula captures them; the safe-change path is missing, so teams avoid tuning production even where the gain is large; and the fleet evidence that would give a strong starting point is unused.

## Problems
- [[niches/database-platform-vendors/configuration-and-resource-tuning/build|🔨 Build: Defaults That Suit Almost No Workload]]
- [[niches/database-platform-vendors/configuration-and-resource-tuning/buy|🛒 Buy: Bayesian Optimisation Over a Parameter Space]]
- [[niches/database-platform-vendors/configuration-and-resource-tuning/fix|🔧 Fix: Tuned Once and Never Measured]]
