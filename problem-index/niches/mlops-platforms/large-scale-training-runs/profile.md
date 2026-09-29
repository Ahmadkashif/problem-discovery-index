# Large-Scale Training Runs

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to tell an infrastructure team, while a sixty-day distributed run is still going, whether it is healthy and what to do about it — and whoever does that takes the account, because the run costs more than every tool in the stack combined.

## Profile
**Market Size:** ~$330M US and growing faster than the rest of the category
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** Low — most teams run bespoke telemetry
**Target Buyer:** ML infrastructure and training platform teams
**Automation Potential:** High — the signals are present and the interpretation is learnable

## What Makes This a Distinct Niche
One training job occupies hundreds or thousands of accelerators for weeks, costs more than the annual budget of the tooling observing it, and cannot simply be rerun. The questions are operational rather than comparative: is the loss curve's current behaviour an instability that will not recover or a transient; is throughput down because of a straggling rank, a degraded interconnect or a data loader; will this checkpoint restore cleanly; is the job on track for the compute budget it was granted. The telemetry volume is orders of magnitude beyond the classical workload — thousands of ranks emitting per step — and the incumbent platforms' ingest paths were not designed for it. Most serious teams have written their own, which is the clearest possible signal of an unserved market.

## Current Tools & Gaps
Framework-level profilers, cluster monitoring, custom dashboards, and the tracking platforms operating well outside their design point. The gaps: no per-rank health view that identifies the slow or degraded one among a thousand; no early warning on a diverging loss curve, which is where the money is lost; no checkpoint validation until a restore is attempted; no cost-to-completion projection against the granted budget; and no accumulated knowledge of what a given failure signature means, despite these failures recurring across every organisation running these jobs.

## Problems
- [[niches/mlops-platforms/large-scale-training-runs/build|🔨 Build: A Diverging Loss Curve at Hour Forty]]
- [[niches/mlops-platforms/large-scale-training-runs/buy|🛒 Buy: Distributed Systems Observability]]
- [[niches/mlops-platforms/large-scale-training-runs/fix|🔧 Fix: The Checkpoint Nobody Tested]]
