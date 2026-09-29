# Build: A Decision Record That Can Be Reconstructed

**Niche:** [[niches/recruiting-tech-vendors/compliance-and-records/profile|Compliance, Records & Audit Trail]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Record what decided each outcome — the score, the threshold, the model version, the reviewer and the stated basis — so any decision can be reconstructed years later.
**Tags:** #compliance #data-integration #workflow-orchestration #evaluation-metrics #descriptive-statistics #confidence-intervals #automation #hypothesis-testing
**Contested on:** Whether an employer will create a durable record of why it rejected people.

## The Problem

An employer is asked to explain a rejection. It might be a regulator under a new automated-decision regime, a plaintiff, an internal audit or a candidate exercising a right.

The record shows: application received, status changed to rejected, date, reason code "other". The screening filter that removed the candidate has been reconfigured four times since. The match model has been retrained. The reviewer has left. Nothing reconstructible remains.

This is not a data retention failure — the application is retained, as required. It is that the decision's basis was never captured, and every element that would capture it is available at the moment the decision is made.

## Why Nobody Has Built This

A durable record of reasons is a record that can be examined, which is precisely the discomfort. Retention obligations require keeping applications and have never required keeping reasons, so the minimum has been met and the additional artefact is a liability nobody has wanted.

Automated decisions specifically were not conceived as decisions requiring a record. A filter is a query; a match score is a number in a field; neither was designed as an event with a justification.

And the configuration history — which filter was live, at what threshold, on what date — is overwritten in most systems, which makes even a willing reconstruction impossible.

## What to Build

A decision event record with everything needed to reconstruct it.

**Log the decision as an event, not a status.** Who or what decided, when, on what basis, at which stage, with the candidate and requisition identified. The status field records the outcome; the event records the decision.

**Capture the automated basis in full.** Score, threshold, model or ruleset identifier and version, the specific criteria that failed, and the features that drove a score where a model produced one. This is the element that matters most under the new regimes and is the one most commonly absent.

**Version the configuration immutably.** Filters, knockout questions, thresholds, scoring weights and requirement lists, with effective dates, so the configuration live on any past date is recoverable. Overwriting these is the single most common reason a decision cannot be reconstructed.

**Structure the human basis.** Which stated requirement was unmet, or which comparative judgement was made, from a taxonomy specific to the requisition rather than from six generic options. A reviewer selecting from the requisition's own requirements is both more informative and easier than a free-text note.

**Retain the record beyond the application.** Statutory application retention is short relative to when questions arrive. The decision record is small and should outlive it, subject to a considered retention policy.

**Make it queryable for the analyses that will be asked for.** Decisions by stage, by reason, by group, by automated versus human, over time. When a regulator, an auditor or an internal reviewer asks, the answer should be a query rather than a project.

**Use it internally first.** The same record powers the rejection audit, the screening diagnosis and the bias analysis. Framing it as an operational asset rather than as a compliance burden is what gets it built.

## Target Customer

Employers' legal and compliance functions in jurisdictions where automated employment decision obligations have arrived, and ATS vendors, who must supply the record and whose current audit trails do not. The regulatory direction makes this a requirement rather than an option on a timescale that is already visible.

## Impact If Built

A decision from two years ago can be reconstructed — what decided it, on what basis, under which configuration. The obligations arriving under automated-decision regimes become answerable with a query. And the same record makes the rejection audit and the bias analysis possible, which is the reason to build it beyond compliance.
