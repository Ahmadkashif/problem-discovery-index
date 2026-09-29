# Build: A Rejection Standard With Appeal and Compensation

**Niche:** [[niches/crowdsourcing-platforms/error-cost-allocation/profile|Error Cost Allocation]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Define what may be rejected, require a reason, provide an appeal, and compensate time lost to broken tasks — as platform rules rather than as requester discretion.
**Tags:** #compliance #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #worker-facing #revenue-impact
**Contested on:** Whether a platform will constrain the rights of the party paying it.

## The Problem

The work was done, the payment is withheld, no reason is given, the approval rate drops, and better-paid work closes off — with no appeal to anyone.

A rejection does three things at once: it takes the labour without paying, it damages a qualification score that gates future earnings, and it is unreviewable. The requester may reject because the work was genuinely poor, because their instructions were unclear, because the item was ambiguous, because they rejected the whole batch to save review effort, or for no reason they would articulate. The worker cannot tell which, cannot contest it, and often cannot even contact the requester.

Meanwhile the platform holds everything needed to distinguish these cases: the submission, the instructions, the other workers' answers to the same item, and the requester's rejection rate against the population.

## Why Nobody Has Built This

The requester pays. A platform that constrains rejection rights is constraining its customer, in a market where a requester can post the same batch on a competitor with a looser rule. That is the whole explanation and it is sufficient.

There is a genuine concern underneath it: some rejection is legitimate and necessary, because a fraction of submissions are automated or careless, and a platform that made rejection hard would flood requesters with junk. That argues for a standard and an appeal, not for unconstrained discretion.

And the affected party has no leverage. Crowdworkers are dispersed, anonymous, classified as contractors everywhere, and individually replaceable.

## What to Build

A rule set, an adjudication capability and a compensation mechanism.

**Define what may be rejected.** Submitted work that fails an objective, pre-stated criterion. Not: disagreement with the majority on an item where competent workers split; not answers consistent with a reasonable reading of ambiguous instructions; not a whole batch rejected without item-level review. Publishing this standard is the foundational act and it costs nothing technically.

**Require a reason from a fixed list**, attached to the specific items. This alone eliminates a large share of casual rejection, because it converts a costless action into a small one.

**Provide an appeal that is actually adjudicable.** The platform holds the submission, the instructions and the other responses to the same item. An appeal can be decided on that evidence — did this answer fall within a reasonable reading — without contacting the requester and without a lengthy process. Most appeals resolve on a single question and the evidence is already in the database.

**Monitor requester rejection behaviour.** Rejection rate by requester against the population, adjusted for task type. A requester rejecting at ten times the median is either posting impossible tasks or rejecting indiscriminately, and either warrants intervention. This is a percentile lookup and no platform surfaces it.

**Compensate time lost to broken tasks.** A task that errors, times out or is withdrawn mid-completion is the requester's failure and the worker's unpaid time. Automatic compensation from a requester-funded pool, triggered by the platform's own telemetry, requires no claim and no adjudication.

**Cap the approval-rate consequence.** A rejection should not permanently gate a worker's access. Ageing the metric, capping the effect of a single requester, and excluding appealed-and-overturned rejections are all rule changes with no technical content.

**Then differentiate on it.** A platform with a published rejection standard and a working appeal is making a claim about fairness that its competitors cannot match, and the academic and enterprise segments — where ethics boards and procurement ask — are where that claim is worth money.

## Target Customer

Platforms serving academic and enterprise requesters, where ethics review boards and supplier standards already ask these questions and where the reputational position is commercially valuable. Also worker organisations and the researchers whose published work on this market is the main source of external pressure.

## Impact If Built

Withheld payment for completed work acquires a standard, a reason and an appeal. Time lost to broken tasks stops being free to the party who broke them. Requesters who reject indiscriminately become visible and answerable. And a market whose central unfairness is a rule choice gets a different rule.
