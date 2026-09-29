# Accessorial Write-Offs With No Cause Code

**Niche:** [[niches/freight-tech-platforms/freight-document-accessorial-billing/profile|Document & Accessorial Billing]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Carriers and brokers write off denied accessorial charges routinely and record the write-off as an amount, so nobody knows what share was denied for missing evidence, late submission, or a genuine disagreement about whether the charge was owed.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #revenue-impact #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in freight billing is fighting to get an accessorial charge paid on first submission against a specific shipper's evidence rules — and whoever holds first-pass payment rate highest takes the account.

## The Problem
A billing department writes off accessorial charges every month. The total is known and appears in the financials. The composition is not: how much was denied because the notification window was missed, how much because the evidence was incomplete, how much because the customer disputed that the event occurred, and how much was never billed at all because nobody got to it. Each of those has a different remedy — a process change, a capture change, a customer conversation, or staffing — and the aggregate figure supports none of them. So the company complains about detention in general and changes nothing in particular.

## Why It's Still Broken
Write-offs are an accounting event and accounting needs the amount, not the reason. Recording a cause takes a clerk an extra moment on a task they are already behind on, with no benefit to them. And the reasons that would be most actionable are the ones least comfortable to record, because "we missed the notification window" names an internal failure while "the customer denied it" does not.

## What a Fix Looks Like
Require a cause on every write-off, from a short list, and make it one tap. Denied for missing or insufficient evidence, denied for late submission, denied on the merits, never submitted, partially paid. Attach the shipper, the lane and the accessorial type. Within a quarter the company has the decomposition it has never had, and the decomposition almost always shows that a large share is procedural and concentrated in specific customers and specific accessorial types. That immediately prioritises the work: encode the rules for the customers where the losses concentrate first. Report first-pass payment rate by shipper and by accessorial type as a standing metric, which is the number this niche is contested on and which nobody currently computes. Where a customer's denial rate is high and the evidence was good, that is a commercial conversation with evidence rather than a grievance.

## Who Feels the Pain
Billing clerks working denials with no pattern view; drivers whose detention is never recovered; and owners who know accessorial leakage is significant and cannot locate it.

## Impact If Fixed
A cause code on a write-off costs a tap and produces the first honest picture of where accessorial revenue goes. It reliably shows that most of the loss is procedural and fixable rather than disputed, which reframes a problem the industry treats as intractable into a process problem with a short list of causes.
