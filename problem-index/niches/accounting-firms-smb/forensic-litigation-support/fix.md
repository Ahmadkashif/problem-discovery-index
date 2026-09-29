# Exhibit Rebuilds When the Underlying Data Changes
**Niche:** [[niches/accounting-firms-smb/forensic-litigation-support/profile|Forensic Accounting & Litigation Support]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A supplemental production lands two weeks before the expert disclosure deadline, and every exhibit tied to the damages model has to be rebuilt and re-tied by hand.
**Tags:** #workflow-orchestration #data-integration #automation #evaluation-metrics #worker-facing #quick-win

## The Problem
Expert reports carry exhibits — schedules, tables, charts — generated from the damages model. Late productions and amended claims are normal, not exceptional, and each one changes the model. Because exhibits are built as static artefacts pasted into a report, every change means regenerating each exhibit, re-checking every in-text figure that references it, and re-verifying internal consistency across a document that may carry two hundred numbers. It happens under deadline, which is exactly when errors get made, and a numerical inconsistency between text and exhibit is a gift to opposing counsel.

## Why It's Still Broken
The model lives in spreadsheets and the report lives in a word processor, with no live link between them. Practices have tried linked objects and abandoned them as fragile across versions and reviewers. So the link is a person, and the reconciliation is manual under time pressure.

## What a Fix Looks Like
Make every figure in the report a reference to the model rather than a copy of it. Exhibits and in-text figures resolve from a single computed source, so a model change propagates on regeneration and a consistency pass flags any figure that no longer reconciles. The reviewer sees a diff of what changed between versions rather than re-reading the document. Nothing about the modelling changes — only the binding between model and document.

## Who Feels the Pain
Experts and analysts rebuilding exhibits against a disclosure deadline, and the testifying expert whose credibility rests on the report being internally consistent.

## Impact If Fixed
Removes a predictable late-stage fire drill and eliminates the class of error most damaging on cross-examination. Late productions stop threatening the schedule.
