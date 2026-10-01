# A Point-in-Time Record of Every Decision

**Niche:** [[niches/financial-data-vendors/fundamentals-and-estimates/profile|Fundamentals & Estimates Data]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The vendor stores each number's current value and sometimes its history, but not the decision that produced it — who mapped it, under which policy, against which alternative.
**Tags:** #data-integration #evaluation-metrics #large-language-models #k-nearest-neighbors #tacit-knowledge-ml #compliance #revenue-impact
**Contested on:** Not terminal as stated — competitors here are fighting either to standardise a new filing correctly within hours and explain every derived number, or to hold the broadest contributed broker estimates and clean them into a trusted consensus; these are different contests with different winners, stated separately in the sub-niches.

## The Problem
Fundamentals and estimates are the result of millions of human decisions per year: a mapping, an exclusion, an override, a restatement accepted. The vendor keeps the outcome and, for its point-in-time products, when the value became known. It rarely keeps the decision as a record — the collector, the policy version, the source passage, the alternative considered, the confidence. Without it the vendor cannot explain a number, measure its own consistency, or train a model on its own expertise.

## Why Nobody Has Built This
Collection tools were built for throughput, and every extra field logged is time taken in earnings season. Audit logs exist for compliance but were never designed for analysis. And the decision record's value accrues to modelling and client service, not to the operations team that would have to produce it.

## What to Build
A decision ledger under both product lines: every value linked to the action that set it, the actor, the evidence span, the policy version and any superseded value. Capture passively from the tools wherever possible rather than asking analysts to annotate. Expose it three ways — to client service as lineage, to content leadership as consistency metrics, and to modelling teams as training data — and shared between the fundamentals and estimates sub-niches, which otherwise do not share infrastructure.

## Target Customer
Chief content officers and heads of content technology at fundamentals and estimates vendors.

## Impact If Built
The vendor's real asset is accumulated collection judgement, and it currently survives only as numbers. A decision ledger is the prerequisite for every model, every explanation and every consistency claim the vendor would like to make.
