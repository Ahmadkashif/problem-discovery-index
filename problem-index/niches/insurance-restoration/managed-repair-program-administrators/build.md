# Estimate Audit by Sampling When the Overscopes Are Predictable

**Niche:** [[niches/insurance-restoration/managed-repair-program-administrators/profile|Managed Repair Programme Administrators]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Auditors review a fraction of estimates chosen by threshold and rotation, over a corpus that would tell them exactly which ones to open.
**Tags:** #gradient-boosting #anomaly-detection #binary-classification #evaluation-metrics #revenue-impact

## The Problem
The administrator's core function is checking that the estimates network contractors submit are right. Audit capacity is finite and estimate volume is enormous, so review is triggered by dollar thresholds, random sampling, and periodic contractor rotation. Everything else is paid as submitted.

The corpus that would improve this is the administrator's own. Millions of estimates across thousands of contractors, with the audit findings that followed, the adjustments made, the supplements requested later, the reopen rate, and in many cases the final settled amount. It contains, for every job type in every geography, what a correct estimate looks like — and for every contractor, the shape of how they deviate from it.

None of that drives selection. An estimate from a contractor with a two-year history of the same line item pattern gets the same probability of review as one from a contractor with a clean record, unless a dollar threshold happens to catch it.

## Why Nobody Has Built This
Audit exists as a quality control function measured on throughput and turnaround, because the SLA clock applies to the audit as much as to the repair. Reviewing enough estimates fast enough is the job, and improving which estimates get reviewed is nobody's deliverable.

Findings are also stored as case outcomes rather than as data. An audit produces an adjustment on a specific estimate, filed against that claim. There is no assembled dataset joining estimate characteristics to audit results, so the question of what predicts a finding has never been askable.

And the political framing discourages it. In a network where contractors are partners, "targeting" reads badly, and random selection is the defensible posture. That is an argument for building the model carefully and explaining it, not for allocating scarce audit capacity by lottery.

## What to Build
Risk-based audit selection on the administrator's own findings history.

**Assemble the label set.** Every audit conducted, whether it produced an adjustment, the size and type of adjustment, and the characteristics of the estimate — job type, loss cause, geography, line item mix, contractor, dollar value, and how the estimate compares to peers on similar jobs.

**Model the probability and size of a finding.** Expected recovery, not just probability, is the right target — an audit likely to find $200 and one likely to find $12,000 should not be ranked together.

**Compare each estimate to its true peer group.** The strongest signal is how this estimate's line items compare to other estimates for the same damage type, property, and geography. Peer comparison is what an experienced auditor does by eye and what the corpus can do exhaustively.

**Score contractors on trajectory, not just level.** A contractor whose estimates have drifted upward over six months is a different case from one who has always run high, and the intervention differs.

**Measure the unaudited population.** Sampling audits at random within low-risk strata is how you learn whether the model is missing something — and it is the honest answer to the fairness objection, since coverage is maintained everywhere.

## Target Customer
Chief Operating Officer or VP of Network Performance at a managed repair administrator. The commercial case is direct: the carrier pays for accuracy, audit capacity is the constraint on delivering it, and expected recovery per audit hour is the metric the whole function should be run on.

## Impact If Built
The same audit team finds materially more, which is money returned to carriers and ultimately to policyholders. Just as important for the operator layer, contractors who estimate honestly stop being audited at the same rate as those who do not — which is the fairness argument the current random approach only appears to satisfy.
