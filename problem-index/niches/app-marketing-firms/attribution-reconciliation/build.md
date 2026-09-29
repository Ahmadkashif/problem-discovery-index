# Four Sources and a Monday Deadline

**Niche:** [[niches/app-marketing-firms/attribution-reconciliation/profile|Attribution Reconciliation]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every network reports its own installs, the measurement partner reports different ones, the aggregated signal reports something late, finance reports the revenue, and the manager allocates a seven-figure budget across the disagreement every Monday.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #workflow-orchestration #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to produce one allocation from four sources that each report a different number — and whoever does that credibly replaces a weekly judgement call on a seven-figure budget.

## The Problem
Monday morning. The networks' dashboards show install counts that sum to more than the app store reports. The measurement partner shows fewer, allocated differently, under its own last-touch rules. The aggregated platform signal for last week has not fully arrived and will be incomplete when it does. Finance shows revenue that does not obviously correspond to any of it. The manager must decide where a seven-figure budget goes this week. They apply a set of mental adjustments learned over years, produce an allocation, and cannot fully explain it to anyone including themselves.

## Why Nobody Has Built This
Each source is built to report its own view and none is built to reconcile, so the reconciliation belongs to the person with the deadline and no tooling — the work falls to whoever is accountable rather than to whoever is equipped. Self-attribution is commercially advantageous to the networks and they have no reason to make deduplication easy. The measurement partner's rules are its product. And the manager's mental adjustments work well enough to prevent the problem being named.

## What to Build
Build the reconciliation as a system. Normalise definitions across sources first — install, attribution window, view-through treatment, time zone — since a large part of the apparent disagreement is definitional and resolving it mechanically removes noise before any judgement is needed. Deduplicate self-attributed claims against the measurement partner's record with a stated rule, which is the fix note's subject. Anchor everything to the store's own install count and finance's revenue, because those are the two figures that are not anyone's claim and they bound the rest. Model the aggregated signal's lag so the current week's incomplete data is projected rather than treated as a low number, which is a standard and entirely avoidable error in weekly decisions. Reconcile continuously rather than weekly, so the allocation is not a Monday scramble. Produce one allocation recommendation with its reasoning, which is the deliverable and is what the manager currently constructs mentally. Show the residual that cannot be reconciled, because naming it is more honest than absorbing it and it is a real measure of how much is unknown. Encode the manager's learned adjustments explicitly so they survive the person and can be examined. Feed the result into incrementality testing, connecting to that niche, since reconciliation establishes what was claimed and only an experiment establishes what was caused. And report the reconciled series over time, since a consistent method matters more than a perfect one for tracking whether anything is improving.

## Target Customer
User acquisition managers and their leadership, agencies allocating client budgets, and the measurement vendors sitting between the sources.

## Impact If Built
The reconciliation falls to whoever is accountable rather than whoever is equipped, and no source is built to reconcile. Normalising definitions removes much of the disagreement mechanically, and anchoring to the store count and finance revenue bounds everything that remains.
