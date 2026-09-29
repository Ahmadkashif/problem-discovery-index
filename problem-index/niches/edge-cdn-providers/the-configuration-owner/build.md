# Nobody Dares Remove a Line

**Niche:** [[niches/edge-cdn-providers/the-configuration-owner/profile|The Configuration Owner]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The engineer who owns the CDN configuration has no way to know whether a change improved anything, so the rule set accumulates and nobody dares remove a line.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #graph-theory #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let the person who owns the rule set know whether a change helped — and whoever does that takes them, because without it the rule set only ever grows and nobody dares remove a line.

## The Problem
The configuration has three hundred and forty rules. About sixty were added for reasons documented in a ticket system that has since been replaced. An engineer wants to remove a rule that appears to do nothing, and cannot establish whether anything depends on it, so it stays. They add a rule to fix a problem, deploy it, and cannot tell whether it helped because the global hit rate moved by a fraction of a percent for reasons including their change, a traffic mix shift and a release. Two years of this produces a rule set that is slower to evaluate, impossible to reason about, and contains conflicting rules whose interaction determines behaviour nobody intended.

## Why Nobody Has Built This
The configuration is the provider's product surface and its expressiveness has been the axis of competition, while what happens as a result has been the customer's concern. Measuring a change's effect requires either a controlled comparison, which means applying the change to a fraction of traffic, or careful observational analysis, and no provider offers the first or performs the second. Rule usage telemetry is straightforward and has not been surfaced. And the asymmetry of removal — visible failure against invisible risk — is the same one that grows every rule set, dashboard estate and alert catalogue in this vault.

## What to Build
Measure changes and give the rule set a lifecycle. Apply a configuration change to a fraction of traffic and compare outcomes against the rest, which the edge can do trivially and no provider offers, and which converts every configuration decision from a guess into an experiment. Report per-rule match counts, last-matched dates and the effect each rule has on the responses it touches, which is the usage data that makes removal defensible. Detect shadowing and conflicts statically, since a rule that can never match because an earlier one always matches first is determinable from the rule set alone and is a common source of confusion. Record intent with each rule — who added it, why, and under what conditions it should be reconsidered — since its absence is the main reason nobody will remove anything. Make removal reversible and time-boxed, disabling rather than deleting for a period, which turns an irreversible-feeling decision into an experiment. Report the rule set's evaluation cost, since a long rule set adds latency to every request and nobody has quantified it. And attribute every change to the metric movement that followed, so the owner accumulates evidence rather than anxiety.

## Target Customer
The engineers who own CDN configurations, platform teams, and the providers themselves, for whom an unmeasurable configuration surface caps how much value their product can deliver.

## Impact If Built
Fractional application at the edge is technically trivial and would make every configuration change measurable, which is the capability the whole niche lacks. Per-rule usage data and reversible time-boxed removal together break the accumulation that every one of these rule sets exhibits.
