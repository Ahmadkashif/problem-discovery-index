# One Necessity Record for the Reviewer and the Auditor

**Niche:** [[niches/psychiatric-hospitals/continued-stay-utilization-review/profile|Continued-Stay Review & Medical-Necessity Defence]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A psychiatric day is argued to a payer by phone and defended to an auditor from the chart months later, and no product keeps one cited record of why each day was necessary that serves both.
**Tags:** #large-language-models #transformers #evaluation-metrics #compliance #automation #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to get each psychiatric day the record supports paid and kept paid. But managed-care concurrent review is won by the lowest share of reviewed days denied, while Medicare recertification and audit defence is won by the lowest share of audited paid days recouped, with different staff, vendors and failure modes. Decomposed into contested sub-niches below.

## The Problem
The UR coordinator's call summary lives in a payer portal or her notebook. The psychiatrist's recertification is a signed form. The progress notes say something else again. When an auditor or prosecutor later asks why day 14 was necessary, the hospital reconstructs the answer from all three.

## Why Nobody Has Built This
UR tools serve the payer call, compliance tools serve the audit, and both were designed for medical stays. Until LLMs could cite prose reliably, extracting behavioral necessity evidence needed a person reading every note.

## What to Build
A daily necessity ledger per patient: the criteria met that day with cited note spans, the legal status, the treatment plan's active goals, what the payer was told and decided, and recertification status. Payer packets and audit files are both generated from it, so they cannot disagree. The sub-niches below carry the two halves.

## Target Customer
Chains' central UR and compliance teams, and freestanding hospitals of 80+ beds.

## Impact If Built
If one ledger cuts a coordinator's review prep by ~20 minutes and an audit file's assembly from ~3 hours to ~30 minutes (estimate), a 100-bed hospital saves ~1,500 staff hours a year.
