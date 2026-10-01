# Error Rates Measured by the Team Being Measured

**Niche:** [[niches/financial-data-vendors/content-operations-research/profile|Fundamentals & Estimates Content Operations]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Content accuracy is reported from internal QA samples graded against internal policy, and nobody estimates the error rate clients actually experience.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor's content organisation is fighting to add issuers, fields and history per analyst-hour without losing accuracy — and whoever turns collection judgement into a reusable asset first gets coverage growth that no longer scales with headcount.

## The Problem
Vendors quote accuracy figures drawn from QA re-keying. That measures whether a value matches policy, not whether policy produced the right economic answer, and the sample is drawn and graded by the same organisation. The external evidence — client tickets, later corrections, disagreement with competing vendors on the same field — is never assembled into an independent estimate.

## Why It's Still Broken
The internal number is flattering and familiar. Cross-vendor comparison requires licensing competitor data. And client tickets are a biased sample — raised by attentive clients on prominent issuers.

## What a Fix Looks Like
Treat cross-vendor disagreement on identical fields as a screening signal and adjudicate a random sample of disagreements. Model ticket propensity so client-reported errors can be reweighted into a population estimate. Report error by field, sector and issuer size with intervals. Feed the worst cells to methodology and collection.

## Who Feels the Pain
Clients making decisions on numbers of unknown reliability, and content leaders unable to show that investment in quality changes anything.

## Impact If Fixed
An honest, externally anchored accuracy estimate is both the management tool the content organisation lacks and a sales asset no competitor has.
