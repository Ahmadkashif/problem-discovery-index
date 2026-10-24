# The Record That Bounces Between QA and Production

**Niche:** [[niches/pharmaceutical-manufacturers/batch-record-review-release/profile|Batch Record Review & Release by Exception]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** A paper batch record goes to QA, comes back with correction requests, goes back again, and the batch sits in quarantine for each round trip.
**Tags:** #cnns #transfer-learning #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to cut QA's review of each executed batch record to the entries that need a human, and whoever releases the highest share of batches with no documentation error found after release takes the account.

## The Problem
QA finds a missing initial, an uncorrected strike-through or an unexplained time gap, and returns the record to production. Production fixes it days later. A second pass finds something else.

## Why It's Still Broken
The checks happen only at the end, after the record leaves the suite, and nobody tracks which steps generate most of the corrections.

## What a Fix Looks Like
Check each page as it is completed: a scan or tablet capture at the end of each step flags missing and illegible entries while the operator is still there, and a weekly report shows which steps and forms generate most corrections so the form or procedure can be fixed.

## Who Feels the Pain
Operators called back to correct paperwork; QA reviewers re-reading the same record; planners waiting on release.

## Impact If Fixed
Removing most second-round returns would cut two to five days of quarantine per affected batch and about a third of documentation deviations (both estimates).
