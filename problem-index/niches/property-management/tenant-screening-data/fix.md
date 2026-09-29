# The Outcome Arrives Every Month and Goes Into an Accounting System

**Niche:** [[niches/property-management/tenant-screening-data/profile|Tenant Screening Data & Scoring]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Fix (Pain Point)
**One-liner:** Every rent payment is a graded answer to a prediction the bureau made, and it is recorded as a ledger entry nobody joins back.
**Tags:** #evaluation-metrics #data-integration #automation #compliance #workflow-orchestration

## The Problem
The screening decision and its consequence live in the same building and never meet. The bureau produced a score and a recommendation. The manager approved or declined. Then, for approved applicants, twelve to thirty-six months of monthly evidence accumulates in a property management system: paid on time, paid late, partial payment, notice served, balance at move-out, lease renewed or not.

That is a graded answer, arriving every month, at scale, with no ambiguity about what happened. It goes into an accounting ledger and is used for accounting.

Nothing joins it back. Not to the score, not to the screening criteria the manager set, not to the specific records that drove the decision. The consequences are concrete and they hurt both sides of the transaction:

The manager cannot answer the most basic question about their own screening policy — whether their criteria are too tight, costing them qualified residents and vacancy days, or too loose. They set a minimum score by convention or by what the last portfolio used.

The bureau cannot improve its model, cannot demonstrate its validity, and cannot defend it when challenged.

And overrides — where a manager approved someone the score said to decline, or declined someone it approved — are the single most informative event in the entire system, because they are the closest thing to a randomised trial anyone will ever get here. They happen daily and are recorded nowhere as overrides.

## Why It's Still Broken
The data is the manager's, sits in a platform the bureau does not control, and the manager has no obvious incentive to hand over the record of how their residents performed.

There is genuine privacy sensitivity. Rent payment history is consumer financial data, and reporting it to a bureau — even to validate a model — has real FCRA implications about what becomes a consumer report and what a consumer may dispute.

And the bureau's caution is rational in a narrow sense. A measured record of score performance by subgroup is a document a regulator or a plaintiff would want. Not measuring is legally safer today and technically ruinous over time.

## What a Fix Looks Like
**Store the decision, fully.** Score, recommendation, criteria applied, records relied on, and what the manager actually did — approve, decline, approve with conditions. Without the last field, no override can ever be identified.

**Capture outcomes at defined checkpoints.** Twelve months, at renewal, at move-out. Three structured snapshots per lease are enough for validation and far easier to negotiate than a live ledger feed.

**Make override capture a one-click part of the leasing workflow.** The leasing agent already decides; a single field recording that they went against the recommendation, and why, costs seconds and produces the most valuable data in the system.

**Give the manager the report first.** Approval rate, outcome rate, and vacancy cost by score band for their portfolio — so they can see whether their threshold is right. This is the exchange that makes outcome reporting worth doing, and it is a product the bureau could sell today.

**Design the privacy posture deliberately.** De-identified, aggregated outcome reporting for model validation is achievable without turning every rent payment into a disputable consumer report. That distinction needs to be settled with counsel at the start, not treated as a reason to do nothing.

## Who Feels the Pain
Applicants declined by criteria nobody has validated; owners carrying vacancy from thresholds set by convention; property managers who cannot evaluate their own screening policy; and the bureau's data scientists, who are fitting a model of rent payment without observing rent payment.

## Impact If Fixed
This is the precondition for everything else in this pocket — outcome-linked scoring, subgroup validation, and any defence of the model as the regulatory environment tightens. It is also immediately useful on its own: a property manager who can see outcome rates by score band for their own portfolio can set a threshold on evidence for the first time.
