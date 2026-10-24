# Exception Rules Learned From Years of QA Corrections

**Niche:** [[niches/pharmaceutical-manufacturers/batch-record-review-release/profile|Batch Record Review & Release by Exception]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every correction a QA reviewer ever wrote on a batch record is a label for what review by exception should catch, and nobody has used them to write the rules.
**Tags:** #cnns #transfer-learning #autoencoders #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to cut QA's review of each executed batch record to the entries that need a human, and whoever releases the highest share of batches with no documentation error found after release takes the account.

## The Problem
Review by exception fails at most plants because the exception rules (which entries, ranges, sequences and manual corrections need a human look) are never fully written for each product. QA keeps reviewing every page, even in an eBR.

## Why Nobody Has Built This
eBR vendors ship the mechanism and leave the rules to the customer. The best evidence for the rules, years of QA corrections on executed records, sits on paper scans and in review logs nobody has digitised.

## What to Build
Read the plant's archive of executed records and QA review comments (handwriting recognition tuned to cleanroom forms), learn per product and step which entries were corrected or questioned and which values sat near limits, and propose an exception rule set with the evidence behind each rule. Then score new records against it, so the reviewer sees flagged entries plus a sample of unflagged ones to keep the system honest.

## Target Customer
QA operations directors at generic and CDMO plants moving from paper to eBR, or stuck with an eBR whose review by exception was never switched on.

## Impact If Built
If review time fell from several hours to under one per record (estimate), a plant releasing 2,000 batches a year would free several QA reviewers and cut days from release lead time.
