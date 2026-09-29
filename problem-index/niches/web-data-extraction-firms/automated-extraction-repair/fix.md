# A Fix Deployed Without Verification

**Niche:** [[niches/web-data-extraction-firms/automated-extraction-repair/profile|Automated Extraction Repair]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Whether repaired by a person in ten minutes or by a model in ten seconds, the fix is deployed once the extraction stops failing — which is the same standard that lets a plausible wrong field into production.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #probability-distributions #automation #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to repair a broken extractor without a person, verified, at fleet scale — and whoever does that takes the account, because repair is now mechanically feasible and is still being done by hand.

## The Problem
An engineer fixes a broken extractor, sees values coming through, and closes the ticket. The values are from the wrong element — the sale price rather than the list price — which is exactly the silent failure the original break at least made loud. The verification standard for a repair is that data flows again, which is the same standard that fails to detect semantic breakage in the first place. Automating repair without raising that standard would industrialise the problem: fixes deployed in seconds, each carrying the same risk, across a fleet, with nobody looking.

## Why It's Still Broken
The definition of fixed is inherited from the definition of broken, and both are structural. Comparing against the pre-break distribution requires retaining it and doing the comparison, which nobody has built. Engineers under queue pressure verify by eye on one page. And the failure surfaces weeks later at a customer, far from the ticket that was closed.

## What a Fix Looks Like
Raise the bar for what counts as repaired. Compare the repaired extraction's value distribution against the pre-break distribution and require agreement before the fix is accepted, which is the single most effective check available, costs nothing, and applies equally to human and automatic repairs. Check the internal consistency relationships that held before the break, since those are strong and cheap constraints. Verify against another source collecting the same entity where one exists, which is close to definitive. Require a sample of repaired records to be confirmed by a model reading the page, which is affordable per repair and is the direct check. Record the pre-break distribution automatically at break detection, since it is needed for verification and is otherwise lost. Backfill or flag the period between break and repair, because the customer's data for those days is wrong regardless of how good the fix is and currently nothing tells them. Report a verified-repair rate rather than a ticket-closure rate, which changes what the team is measured on. And apply the same gate to automatic repairs from the first day, because automating an unverified process is the one way this gets dramatically worse.

## Who Feels the Pain
Customers receiving a confidently wrong field after a repair; engineers whose closed tickets reopen weeks later as data quality incidents; and the firms about to automate a process whose verification standard cannot support it.

## Impact If Fixed
Distribution comparison against the pre-break baseline is free and is the most effective check available, and it applies equally to human and automatic repair. Capturing that baseline at break detection is the step that must exist before repair is automated at all.
