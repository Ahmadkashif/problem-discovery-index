# Severity Scoring on Every Edit Diff

**Niche:** [[niches/document-preparation-services/transcript-qa-accuracy-scoring/profile|Transcript QA & Accuracy Scoring]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Transcript quality is graded on a small sample by a second person, though every report already carries a machine draft, an edited final and a severity rubric a model could apply to all of them.
**Tags:** #bert #transformers #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to produce an accuracy score that the client, the vendor and the editor all accept as the basis for service credits and pay, and whoever scores every transcript by error severity, not a hand-checked sample, at auditor-level agreement takes the account.

## The Problem
A QA auditor re-listens to a random handful of an editor's reports each period, marks errors by category and computes a score. That score sets incentive pay and sometimes continued employment, and the vendor's aggregate decides service credits with the health system. A few reports per editor is a noisy basis for decisions that large, and critical errors in the unsampled reports are never seen.

## Why Nobody Has Built This
Severity is contextual (a dropped "no" is critical, a dropped "the" is not) and auditors disagree. QA sits inside thin-margin vendors, and nobody wanted to put a model's number on someone's pay.

## What to Build
A classifier that runs on every report. It aligns draft, edited final and, where audited, the auditor's corrected version, classifies each residual difference into the client's severity scheme (AHDI categories in medicine, style rules elsewhere) and computes the score under the contracted method. It routes uncertain or high-severity cases to a human auditor and publishes per-editor scores with confidence intervals. Agreement with auditors is measured continuously against auditors' agreement with each other.

## Target Customer
Directors of Quality at documentation vendors and transcription platforms; health systems commissioning independent audits.

## Impact If Built
Every report scored, critical errors found wherever they occur, and pay and service credits based on enough evidence to be fair.
