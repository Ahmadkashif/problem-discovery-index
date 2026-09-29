# Build: Automate the Checking, Teach the Judgement

**Niche:** The Audit Associate
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Automate evidence requesting and rule-based checking so the associate's time moves to the judgement work, and give them feedback while they are still working rather than four days later.
**Tags:** #bert #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration #worker-facing #data-integration
**Contested on:** Whether the entry-level role is professional training or evidence checking at high utilisation.

## The Problem

An associate's week is dominated by two activities that require nothing they were hired for.

The first is evidence logistics. Composing requests, sending them, chasing them, receiving files in whatever format the client sent, and organising them. A large share of engagement elapsed time is waiting for evidence and a large share of associate time is managing the waiting.

The second is rule checking. A control says access reviews occur quarterly with documented reviewer sign-off. The associate opens each sampled review and checks that it has a date in the right quarter and a named reviewer. This is a rule evaluated against a document, performed by a person, twenty-five times.

What is left — is this control adequately designed, is this exception material, does this description match what the system actually does — is the part that would constitute professional training and is done by managers and partners.

So the role is structured so that the training content is the smallest part of it, in a profession where the entry-level pipeline is the constraint on capacity and attrition at that level is a recognised problem.

## Why Nobody Has Built This

**Fixed fees make automation investment hard to justify per engagement.** The saving accrues across engagements and the cost falls on the firm's technology budget.

**The associate's hours are the flex.** When an engagement overruns, the overrun lands on their time, which means the firm does not experience the inefficiency as a cost.

**Automating the mechanical part reduces billable hours.** A firm billing for associate time has an awkward incentive, though the fixed-fee structure means the saving is actually the firm's.

**Judgement work requires supervision capacity.** Moving associates onto judgement work requires managers with time to supervise, and managers are the other constrained resource.

**Evidence formats are heterogeneous.** Clients send screenshots, PDFs and exports in every conceivable arrangement, which makes automated checking harder than it appears without a platform integration.

**Nobody measures the associate's hours properly.** Time beyond the fee is not recorded, so the inefficiency does not appear in any system the firm runs.

## What to Build

**Automate evidence requesting and chasing.** Requests generated from the audit programme, sent, tracked, escalated automatically. This removes a substantial share of associate administrative time and shortens the engagement.

**Evaluate rule-based tests automatically where the data is connected.** Controls testable as rules over a connected population should be, which is the same capability as full-population testing and serves the associate directly.

**Extract from unstructured evidence.** Where evidence arrives as documents, extract the fields the test needs and present them for confirmation rather than requiring a person to read each one.

**Give feedback immediately.** Review comments while the associate is still working the control rather than four days later, so a mistake is corrected once rather than repeated across a dozen tests. This is a workflow change and is the single largest improvement to the learning experience.

**Move the judgement earlier in the career.** With the mechanical work automated, associates can be given control design assessment and description review under supervision, which is the training the role claims to provide.

**Record the actual hours.** Time worked against fee, honestly, so the overrun currently absorbed by associates appears in the firm's own reporting and can be managed.

**Structure the learning deliberately.** Rotation across control domains, exposure to the judgement conversations, and a named supervisor — rather than assignment to whatever engagement needs bodies.

## Target Customer

Firm operations and practice leadership, where the argument is the entry-level pipeline: the constraint on this industry's capacity is people who stay, and the current role design is a recognised contributor to why they do not.

Audit technology teams, for whom evidence automation is the clearest efficiency target and the one that also improves the job.

Associates themselves, who are not the buyer and whose retention is the outcome the buyer cares about.

## Impact If Built

The role becomes what it is sold as. Automating the mechanical majority is the only way to move associates onto judgement work, and judgement work is what makes the job a profession rather than a queue.

Immediate review feedback instead of a four-day queue is a workflow change with no cost that would materially improve both learning and quality.

And recording the actual hours against the fee would make the overrun visible in the firm's own numbers, which is the precondition for anybody managing it.
