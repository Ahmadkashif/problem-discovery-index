# The Loss Nobody Attributes Back

**Niche:** [[niches/payment-processors/merchant-underwriting/profile|Merchant Underwriting]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** A merchant approved in March generates a loss in November, the loss is recorded against the merchant, and nothing connects it to the underwriting decision or the person who made it.
**Tags:** #evaluation-metrics #data-integration #confidence-intervals #compliance #quick-win #descriptive-statistics #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to decide whether a business is safe to process for, against the same registries everyone else uses, and to learn from the outcome — and whoever closes that loop stops grading a decision against losses it never attributes back.

## The Problem
An acquirer's loss report shows chargeback and fraud losses by merchant and by month. It does not show which underwriting decisions produced them, which underwriter approved, what the application looked like, or which signals were present at the time and were discounted. The underwriting function is therefore grading itself on a number it cannot decompose. It tightens broadly when losses rise, which declines good merchants along with bad ones, and it has no way to identify which specific judgement was wrong because the judgement and the loss are never in the same record.

## Why It's Still Broken
The decision and the loss are separated by months and by organisational boundary, and a join across both is nobody's responsibility — the same ownership gap that runs through every decisioning problem in this cluster. Losses are managed as a portfolio number rather than as feedback. Attribution would identify individual decisions as wrong, which is uncomfortable. And the broad tightening response works well enough to keep losses acceptable while the cost falls on merchants nobody counts.

## What a Fix Looks Like
Join the loss to the decision. Record every underwriting decision with its evidence, its score, its reserve terms and its decider, which is the prerequisite and is a small change at the point the decision is made. Attribute every subsequent loss back to the approving decision, which turns a portfolio number into feedback and is the fix. Report loss rate by application characteristic, by score band and by underwriter, which reveals immediately where the judgement is failing and where it is unnecessarily tight. Measure the other direction too, by tracking approved-near-threshold merchants who performed well, since the invisible error is the merchants declined who would have been fine. Report the vintage curve, since losses emerge over months and a recent cohort's apparent quality is an artefact of time. Use the attribution to tighten specifically rather than broadly, which is where the merchant experience and the loss rate both improve. Feed confirmed outcomes into the model, since these are the labels and they are currently discarded. Give underwriters their own outcome record, connecting to that niche, because they currently never learn. Separate loss from the merchant's own failure, since a business that went under is a different lesson from one that was fraudulent from the start. And report underwriting accuracy to the board, because an acquirer whose central risk decision is unmeasured is carrying an exposure it cannot describe.

## Who Feels the Pain
Merchants declined by a broad tightening caused by losses they had nothing to do with; underwriters graded on a portfolio number they cannot influence specifically; and acquirers unable to improve the decision that determines their losses.

## Impact If Fixed
The decision and the loss are separated by months and an organisational boundary, so the function grades itself on a number it cannot decompose. Attributing losses back to approving decisions turns a portfolio figure into feedback and lets tightening be specific rather than broad.
