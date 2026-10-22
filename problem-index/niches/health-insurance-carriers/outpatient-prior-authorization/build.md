# Approve-on-Sight for Outpatient Requests

**Niche:** [[niches/health-insurance-carriers/outpatient-prior-authorization/profile|Outpatient Prior Authorization & Gold-Carding]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An experienced nurse approves most outpatient requests on sight from patterns in the packet; no system has learned that read from the plan's own decisions.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn an outpatient authorization request into a determination inside the 72-hour and seven-day clocks without a fax or a phone call, and whoever auto-approves the largest share of requests a nurse would have approved, with no rise in overturned denials or later-audited approvals, takes the account.

## The Problem
Auto-approval today runs on hand-written rules: approve this code for this diagnosis if these fields are present. The rules cover the simplest cases and miss the much larger set that an experienced reviewer approves in a minute because the therapy note, the imaging report and the referring practice's history together make the case obvious. Those requests wait in the same queue as the doubtful ones.

## Why Nobody Has Built This
Training data needs the plan's own determinations joined to the documents that drove them, and the documents are faxed images in a UM platform the plan does not control. Vendors with models train on many plans' data under delegation agreements and are cautious about anything that looks like automated decision-making.

## What to Build
Criterion-level extraction from attachments with page citations; a model trained on the plan's history of first-review approvals that estimates whether an experienced reviewer would approve; and an operating point set by the medical director. Above it, the case is approved with the evidence attached, or confirmed by a nurse in seconds where policy requires. Below it, the case goes to review with the missing evidence named. A monthly audit samples auto-approvals for senior re-review, so the threshold is tuned on measured error rather than vendor assurance. The model never denies.

## Target Customer
UM leaders at MA, Medicaid and commercial plans running high-volume imaging, musculoskeletal and specialty-drug programmes in-house.

## Impact If Built
Nurse time moves from confirming obvious approvals to reading genuinely doubtful cases. Median decision times fall from days to under 24 hours for fast-tracked requests (estimate), and the audited approval record becomes evidence for gold-carding and for regulators.
