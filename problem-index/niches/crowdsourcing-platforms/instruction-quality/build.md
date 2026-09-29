# Build: Pre-Launch Review and Early Defect Detection

**Niche:** [[niches/crowdsourcing-platforms/instruction-quality/profile|Instruction & Task Design Quality]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Read the instructions for ambiguity before the batch posts, and detect a defective task from its first fifty submissions while it can still be stopped.
**Tags:** #large-language-models #hypothesis-testing #confidence-intervals #evaluation-metrics #change-point-detection #descriptive-statistics #automation #transformers
**Contested on:** Whether instruction ambiguity can be detected without running the task on people.

## The Problem

A requester writes instructions, posts a batch of two thousand items, and finds out the instructions were ambiguous when the agreement statistics come back poor — by which point the money is spent, the data is compromised, and a set of workers have been rejected for reading the instructions differently than the majority.

The defect was detectable at two earlier points. Before posting, by reading the instructions for constructions that admit two readings, for categories whose boundaries are unspecified, for edge cases not addressed, and for terms whose meaning depends on context the worker does not have. And within the first fifty submissions, from the response distribution splitting along an interpretable line, the completion time variance, the questions arriving, and the abandonment rate.

Neither check exists.

## Why Nobody Has Built This

The pre-launch check was not feasible cheaply until recently. Reading a set of instructions and identifying the ways a stranger might misread them is a judgement task, and it is now a routine one for a language model.

The early detection check requires nobody to build a model at all — it is monitoring, on data already flowing — and it has not been built because task quality is treated as the requester's responsibility and platform product effort goes into the requester-facing posting flow and the payment mechanics.

There is also a mild disincentive: a platform that stops bad batches early collects less on those batches. This is small and real, and it is outweighed by the disputes and churn that bad batches cause.

## What to Build

A pre-launch reviewer and an early-batch monitor.

**Review the instructions before posting.** A model reads the instructions and the item set and returns specific concerns: this category boundary is unspecified, this term is ambiguous in context, this edge case is not covered, this instruction contradicts that one, this attention check conflicts with the main instruction. Each concern pointed at the exact sentence, offered as a suggestion the requester can accept or dismiss in seconds.

**Simulate the misreading.** Have the model attempt the task under each plausible reading of an ambiguous instruction and report where the readings diverge. This is far more convincing to a requester than an abstract warning — showing them two defensible and contradictory answers to their own item is what makes them rewrite it.

**Monitor the first fifty submissions.** Response distribution shape, agreement, completion time distribution, abandonment rate, question volume, and how each compares to this requester's history and to comparable tasks. Deviation on any of these within the first tranche is a defect signal.

**Pause rather than warn.** When the signal is strong, hold the batch, notify the requester, and pay the workers who completed the affected items. A warning email arriving while two thousand items continue to be completed protects nobody.

**Locate the defect, do not just flag it.** Which item, which category boundary, which instruction — from the response pattern. A requester told "your batch has a problem" will guess; one told "items in category C are being split 55/45 along an interpretable line, and here are three examples" will fix it in ten minutes.

**Learn across requesters.** Instruction patterns that reliably produce confusion, per task type, accumulated across the platform. This becomes design guidance far better than any template and is an asset only the platform can build.

## Target Customer

Platforms serving academic and ML requesters, where data quality is the purchase criterion and a pre-launch reviewer is a strong differentiator. Also requesters directly — researchers and ML teams who have been burned by a bad batch — and the survey and experiment tooling vendors.

## Impact If Built

Ambiguous instructions get caught before the batch posts, or within the first fifty submissions when it can still be stopped. The requester gets better data for the same money. And the workers who would have been rejected for reading the instructions reasonably do not get rejected, because the instruction is fixed instead.
