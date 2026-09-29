# Build: Generated From the Record

**Niche:** Report Production & Distribution
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Render every report variant from the structured engagement record, with a machine-readable companion, delivered through a controlled channel that tracks where it went.
**Tags:** #bert #evaluation-metrics #compliance #data-integration #automation #workflow-orchestration #confidence-intervals
**Contested on:** Whether the report is generated from the engagement record or assembled by hand from last year's document.

## The Problem

The engagement record holds everything the report needs. Every control tested, the population and sample, the result, the exceptions with their detail, the scope, the period, the criteria.

The report is assembled from it by hand. The control matrix is transcribed and reconciled. Exception descriptions are written from workpaper notes. The system description goes through rounds with the client. And the whole thing is checked against the workpapers by a reviewer to ensure the report says what the testing found.

That reconciliation — does the report accurately reflect the engagement record — is a mechanical check performed by a senior person, and it is exactly the kind of check that a generated report makes unnecessary because the report is the record.

The second problem is distribution. A SOC 2 report is confidential, is restricted in its use, and circulates to hundreds of the client's customers, each of whom receives a PDF by email and forwards it onward. The firm that issued it has no idea where it is. And every recipient extracts its content by hand because there is no machine-readable form.

## Why Nobody Has Built This

**The report format is a document.** The standard prescribes a written report, so the artefact is prose and generation from structured data has to produce prose.

**The system description is the client's.** A substantial part of the report is management's document, which cannot be generated from the auditor's record and must be integrated.

**Partial generation already exists.** Larger firms generate parts, which reduces the felt pain and stops short of the reconciliation saving.

**Distribution is the client's problem.** The firm issues to the client and the client distributes, so tracking is outside the firm's relationship.

**Machine-readable companions would help the reader, who is not the customer.** A structured export benefits the relying party, who did not commission the report.

**Nobody counts the production time.** Assembly and reconciliation hours are absorbed into the engagement, so the saving has no number attached.

## What to Build

**Render the report from the engagement record.** Control matrix, test descriptions, results and exceptions generated directly, so the report cannot diverge from what was tested and the reconciliation check disappears.

**Generate every variant from one record.** Type 1, Type 2, bridge letters and any client-specific format rendered from the same source, so a late change propagates everywhere rather than requiring each document to be updated.

**Integrate the client's description properly.** Management's section imported and version-tracked, with the auditor's required amendments recorded — which also produces the challenge record described in the scope niche.

**Issue a machine-readable companion.** Scope, exclusions, carve-outs, controls, exceptions and complementary user entity controls as structured data alongside the PDF. This is what would let the relying party actually use the report, and issuing it is a decision rather than a project.

**Deliver through a controlled channel.** A portal with access grants rather than an email attachment, so the firm and the client know who has it, and so a superseded report can be marked as such.

**Track distribution.** Where the report went, which is currently unknown to everyone, and which matters for a confidential document circulating to hundreds of parties.

**Support supersession.** When a report is reissued or a bridge letter is available, holders of the previous version should be able to find out — which is impossible with an emailed PDF.

## Target Customer

Audit firm operations and quality leadership, for whom generated reports remove a manual reconciliation performed by senior reviewers and eliminate a class of error.

Clients, who distribute these reports to hundreds of customers and have no control over where they go.

Relying parties, who would use a machine-readable companion immediately and are the ones the report exists for.

## Impact If Built

Generation from the record removes the reconciliation between report and workpapers, which is a mechanical check currently performed by the most expensive people on the engagement.

A machine-readable companion is a decision rather than a build and would transform what every relying party can extract — which is the largest downstream improvement available in this industry for the smallest effort.

And controlled distribution with supersession would give a confidential document circulating to hundreds of parties the basic handling it currently lacks entirely.
