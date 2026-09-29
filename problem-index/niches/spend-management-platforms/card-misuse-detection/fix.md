# The Duplicate That Is Not Identical

**Niche:** [[niches/spend-management-platforms/card-misuse-detection/profile|Card Misuse Detection]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The same hotel stay is on the card and in a reimbursement claim, for slightly different amounts, and nothing checks across the two.
**Tags:** #quick-win #automation #evaluation-metrics #compliance #descriptive-statistics #graph-theory #data-integration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to find the spend that is within policy and still wrong — and whoever detects insider misuse without accusing honest employees takes the risk the rule engine was never built to see.

## The Problem
Duplicate detection looks for identical transactions in the same channel. Real duplicates are rarely identical: a hotel charged to the card and also claimed as a reimbursement, a conference paid by one employee and expensed by another, a subscription billed to a card and invoiced to accounts payable, the same taxi split between two claims. The amounts differ slightly, the channels differ, the dates are near but not equal, and nothing looks across the boundaries. Most of it is honest error, all of it is money, and none of it is found.

## Why It's Still Broken
Duplicate detection was implemented within each channel as each was built, so nothing ever looked across them — the check inherited the system boundary rather than the business question. Near-matching requires tolerance thresholds nobody set. The amounts are individually small. And nobody totalled them, so the aggregate is unknown.

## What a Fix Looks Like
Match across channels with tolerance. Run duplicate detection across card, reimbursement and payables together, which is the fix and is where essentially all real duplicates live. Match on near amounts, near dates and merchant similarity rather than on exact equality, because exact duplicates are the rare case. Include the vendor invoice channel, since subscriptions billed both ways are common and entirely invisible today. Group by trip or event, as travel duplicates cluster and the cluster is more detectable than any single item. Report the total value found, which is the number that justifies the work and does not currently exist. Present matches for confirmation rather than auto-rejecting, since most are honest error and the relationship matters. Detect the recurring duplicate, because a subscription paid twice every month is the highest-value find and the easiest. Check across employees as well as within, as the same expense claimed by two people is a known pattern nothing looks for. Tune tolerance to keep false positives manageable, since a controller will abandon a noisy report. And run it continuously rather than at close, so the correction happens before the payment.

## Who Feels the Pain
Companies paying twice for the same thing; controllers who suspect it and cannot find it; employees making honest errors that go uncorrected; and auditors who find it a year later.

## Impact If Fixed
The duplicate check inherited the system boundary rather than the business question, so nothing ever looked across channels. Near-matching across card, reimbursement and payables is where every real duplicate lives and the total has never been measured.
