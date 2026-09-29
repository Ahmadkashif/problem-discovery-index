# Build: Prioritisation by Harm-if-Delayed

**Niche:** High-Volume Queue Operations
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A queue ordering that ranks items by how much harm each additional minute of delay causes, rather than by age, report count or category.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #evaluation-metrics #confidence-intervals #markov-decision-processes #automation #compliance
**Contested on:** Whether the operation is priced and run on decisions completed per hour, or on whether the right decisions were reached fast enough on the items where speed mattered.

## The Problem

A review queue is worked in an order that has almost nothing to do with where delay causes harm. Most operations order by age, sometimes with coarse category buckets and a separate lane for a handful of severe classifications. The rest is first in, first out.

That ordering is wrong in a specific and expensive way. The harm caused by a delayed decision varies across the queue by orders of magnitude and varies over time for the same item. A livestream in progress is a different object at minute two than at minute forty. A piece of coordinated inauthentic content in the first hour of a spreading campaign is worth far more to remove than the same content once it has been seen by everyone it will reach. A borderline advertisement causes essentially the same harm whether it is reviewed in ten minutes or ten hours.

So the operation spends its scarce capacity uniformly across a queue where the value of speed is wildly non-uniform, hits its contractual turnaround, and has no idea whether it reached the items that mattered in time. Nobody measures harm-weighted latency, so nobody optimises it, and a vendor that did would have no way to prove it.

## Why Nobody Has Built This

**The contract measures unweighted turnaround.** Service levels are specified as a percentage of items handled within a window, often with a couple of severity tiers. An operation optimising a harm-weighted objective could improve real outcomes while appearing worse on the contractual metric, which is a commercially impossible position.

**Harm-if-delayed requires outcome data nobody returns.** Estimating how much damage an extra hour causes means observing what happened — views accrued, shares, reports generated, downstream incidents. That is platform telemetry, and it does not reach the vendor, which is the same wall that blocks [[niches/content-moderation-services/decision-quality/profile|🔵 Decision Quality Measurement]].

**Prioritisation is platform-side.** In most arrangements the queue is composed and ordered by the client, and the vendor supplies capacity against it. The party with the telemetry to build this has no labour cost incentive to; the party with the operational incentive has neither the data nor the control.

**Velocity prediction is genuinely hard.** The signal that matters — is this about to spread — must be estimated in the first minutes from very little, on an adversarial distribution where the actors are actively trying to look ordinary. It is a real forecasting problem, not a scheduling tweak.

**Reordering has a fairness cost.** Systematically deprioritising low-harm items means some wait a very long time, and the reporter of a low-harm item experiences that as being ignored. A workable system needs an aging floor, which complicates the optimisation and the contract.

## What to Build

**Estimate harm accrual rate, not category.** For each item, a predicted rate at which harm accumulates while it remains live — driven by current and projected exposure, content category, the actor's history, and whether the material is in a spreading pattern. The output is not a severity label but a curve, because the whole point is that the value of acting changes over time.

**Order by marginal harm averted per reviewer-minute.** Combine the accrual rate with the expected handling time, which is itself predictable from the item's characteristics. An item that accrues harm quickly and resolves in twenty seconds should be ahead of one that accrues slowly and takes four minutes, and no current system reasons this way at all.

**Predict velocity early.** The highest-value component: identify in the first minutes the small number of items that are about to reach a very large audience. Early engagement dynamics, sharing topology, actor coordination signals and the historical distribution of similar items. Being right about a handful of these per day is worth more than a percentage point of overall throughput.

**Aging floors and fairness constraints.** A guaranteed maximum wait per tier so low-harm items cannot starve, expressed as explicit constraints on the optimisation rather than left to emerge.

**Measure harm-weighted latency and make it the number.** Total harm accrued while items awaited decision, reported alongside contractual turnaround. This is the metric the industry lacks, and publishing it — even imperfectly — is what makes the case for changing the contract.

**Build it where the data is, or negotiate the telemetry.** Realistically this requires either platform-side deployment or a contractual right to exposure telemetry on queued items. The vendor-only version is a useful approximation built from category, actor history and handling time, and the gap between it and the full version is the argument for the data.

## Target Customer

Platform trust and safety leadership, who own both the telemetry and the risk, and for whom the argument is not cost but exposure: the current ordering means the worst incidents are handled at the same pace as everything else.

Vendors as the second buyer, where the pitch is a differentiated service offering — a harm-weighted service level is something no competitor can currently claim — provided the contract is restructured to reward it.

## Impact If Built

The queue starts being worked in the order that matters. Capacity is fixed; the ordering is free, which makes this one of the few interventions that improves outcomes without increasing cost.

Velocity prediction addresses the failure mode that produces the industry's worst public incidents — material that spread enormously while sitting in a queue behind unremarkable items.

And harm-weighted latency gives platforms and vendors a shared objective that corresponds to what the operation is actually for, replacing a turnaround average that can be met comfortably while the important cases are missed.
