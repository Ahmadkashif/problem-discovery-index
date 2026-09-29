# A Statement That Can Be Traced

**Niche:** [[niches/music-distribution-platforms/royalty-accounting-and-reconciliation/profile|Royalty Accounting & Reconciliation]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The artist is paid a number that neither they nor, in the hardest cases, the distributor can trace back to the streams that produced it.
**Tags:** #data-integration #evaluation-metrics #automation #confidence-intervals #compliance #descriptive-statistics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn dozens of incompatible statement formats into a payment an artist can trace back to a stream — and whoever makes a royalty statement explainable takes the trust the whole category runs on.

## The Problem
Money arrives from many services, in many currencies, across many territories, at many rates, with deductions applied at several points, on schedules that differ by service and by month. It is ingested, transformed, allocated across a catalogue, split among rights holders and paid out. Somewhere in that chain the artist's individual stream became a fraction of a cent, and reconstructing the path from one to the other is difficult inside the distributor and impossible outside it.

## Why Nobody Has Built This
Royalty systems were built to compute a payable amount, so traceability was not a requirement — a pipeline designed to produce a correct total need not retain how it got there, and nothing since has forced it to. Statement formats change without notice. Artists have no leverage to demand explanation. And the cost of full lineage is real while the benefit is trust, which nobody has priced.

## What to Build
Keep the lineage and make the statement legible. Retain line-level lineage from source statement to artist payment, which is the core and is what makes every other claim about accuracy checkable. Reconcile received revenue against expected revenue from reported streams, since the gap is where errors and deductions hide and nobody computes it systematically. Normalise the incoming formats into one internal model rather than handling each downstream, as format-specific handling is where silent breakage lives. Detect ingestion failures and format changes automatically, because a service changing a column is currently discovered through a number that looks wrong. Explain the statement to the artist in terms they can follow — streams, territories, rates, deductions, splits — which is the product and no competitor offers it. Show the deductions explicitly, since opaque deductions are the single largest source of distrust. Handle currency and tax visibly, as they move numbers materially and are never explained. Detect anomalies against the artist's own history, so an underpayment is caught rather than accepted. Let an artist query a specific figure and get an answer, which is what turns an assertion into an account. And publish the reconciliation methodology, because a distributor whose maths is inspectable is the one artists will choose.

## Target Customer
Royalty operations leadership, artists and rights holders, labels and publishers using distributors, and royalty accounting vendors.

## Impact If Built
A pipeline designed to produce a correct total need not retain how it got there, and nothing has forced it to. Line-level lineage plus a reconciliation against expected revenue turns an unverifiable payment into an account an artist can check.
