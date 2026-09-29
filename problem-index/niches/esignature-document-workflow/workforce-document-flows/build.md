# Who Has Not Signed the Current Version

**Niche:** [[niches/esignature-document-workflow/workforce-document-flows/profile|Workforce Document Flows]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every company can show that an employee signed a handbook and almost none can show that every current employee signed the current handbook, which is the question an auditor or a plaintiff's lawyer actually asks.
**Tags:** #graph-theory #descriptive-statistics #logistic-regression #bert #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to prove, on demand and for the whole workforce, that every required document is signed against its current version by the right person at the right time — and whoever can produce that evidence in a minute takes the account.

## The Problem
A company revises its handbook in March. HR sends the acknowledgement to a distribution list exported in February. Forty people who joined between the export and the send never receive it; six who transferred into a state with an additional required disclosure receive the generic version; two contractors reclassified as employees are on neither list. Everyone who signs is recorded as compliant. Two years later, in a wage claim, counsel asks for proof that the claimant acknowledged the arbitration provision in force at the time of hire, and the answer requires someone to reconstruct which handbook version was current on a date, whether the claimant's signature was against that version, and whether the send list included them — from a signature archive, an HR export and a folder of PDFs.

## Why Nobody Has Built This
The signature platform knows about envelopes and not about populations; the HR system knows about populations and not about document versions; and the join between them is a CSV export that somebody does quarterly. Each vendor's model of the problem stops at its own boundary, and the gap is exactly where the compliance question lives. Version awareness is the specific missing concept: platforms store a signed PDF as an artefact rather than as an instance of a versioned document, so "signed the current version" is not a query the data model can express. And the failure is invisible until a claim, which is years later and is somebody else's problem by then.

## What to Build
A currency ledger over the workforce document estate. Every required document modelled as a versioned object with an effective date and an applicability rule — which classifications, locations, jurisdictions and employment types must sign it, expressed as a rule rather than as a list. The population derived continuously from the HR system rather than exported, so a joiner, transfer or reclassification triggers the requirement automatically on the day it applies. Every signature recorded against a document version rather than a file, which makes "current" computable. From that, the two outputs that matter: a live gap list — who is missing what, why, and since when — and point-in-time evidence, which answers what this person was required to sign on this date, what they signed, which version it was, and when. Material change detection on revisions is the useful refinement: a formatting change does not warrant re-acknowledging the whole workforce and a change to the arbitration clause does, and distinguishing them is a document comparison problem rather than a judgement call left to whoever made the edit.

## Target Customer
HR operations and compliance leaders at multi-state employers, and the signature and HR platform vendors on either side of the gap — for whom this is the integration that makes the pair worth more than the sum.

## Impact If Built
The gap is structural rather than procedural: no product on either side can express "signed the current version", so no amount of diligence closes it. Point-in-time evidence turns a multi-day reconstruction into a query, and that reconstruction happens at exactly the moment when the company is least able to afford it.
