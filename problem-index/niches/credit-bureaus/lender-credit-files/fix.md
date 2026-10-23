# Retro Results Nobody Can Reproduce Six Months Later

**Niche:** [[niches/credit-bureaus/lender-credit-files/profile|Consumer Credit Files for Lending]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Fix (Pain Point)
**One-liner:** When a lender revisits why it chose a bureau, the archive sample, attribute versions and model code behind the decision are gone.
**Tags:** #evaluation-metrics #feature-engineering #hypothesis-testing #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to win the lender's retro study — the archive test in which each bureau's file and attributes are scored against the lender's own booked and declined applicants — and whoever shows the most lift on that population takes the account.

## The Problem
A retro study is run on a sample drawn by one analyst, with attributes in the version the bureau shipped that month, modelled in notebooks that are not kept. A year later the lender's model-risk team or a new chief credit officer asks why the primary bureau changed, or a bureau asks for a re-test after adding data. Nobody can rebuild the original comparison, so the decision is re-argued from memory.

## Why It's Still Broken
Retros are run as one-off projects by different teams on each side, and attribute libraries are versioned for production, not for the archive pulls used in sales.

## What a Fix Looks Like
Every retro gets a manifest: sample definition and seed, archive date, attribute library version, model specifications and metric outputs, stored by both lender and bureau and re-runnable on request. A re-test after a data change then compares like with like.

## Who Feels the Pain
Lender model-risk reviewers and credit officers defending a vendor decision; bureau sales analysts asked to repeat work they cannot find.

## Impact If Fixed
A bureau decision that can be audited and re-tested, and re-tests that measure the data change rather than a new sample.
