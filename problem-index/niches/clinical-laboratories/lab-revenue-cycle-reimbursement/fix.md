# The Denial Worked Long After the Ordering Office Forgot the Patient

**Niche:** [[niches/clinical-laboratories/lab-revenue-cycle-reimbursement/profile|Lab Revenue Cycle & Reimbursement]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** A lab finds out a requisition was missing a diagnosis code six weeks later, when the denial arrives and nobody at the ordering office remembers the patient.
**Tags:** #large-language-models #workflow-orchestration #automation #revenue-impact #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to collect what each requisition is owed. But routine tests and molecular or genetic tests are won on different things. Routine testing is a volume game of a few dollars a line, won by whoever recovers the most net dollars per thousand claims through the 2027 fee schedule reset. Molecular testing is a coverage game of hundreds or thousands of dollars a test, won by whoever gets paid on the highest share of tests performed through authorization, Z-codes and appeals. Staff, vendors and win conditions differ, so the niche is decomposed into contested sub-niches below.

## The Problem
Denials for missing or non-covered diagnosis codes, missing insurance and missing signatures are worked from a queue weeks after the test. Staff fax or phone the ordering office, wait days, and often write the line off because the amount is smaller than the cost of chasing it.

## Why It's Still Broken
The information gap is created at the ordering office and discovered in billing, and the two are separated by accessioning, testing and claim submission. Accessioners are measured on throughput, not on billing completeness, so they register what arrives. No one owns the requisition end to end.

## What a Fix Looks Like
Check billing completeness at accessioning against the payer's rules for each test, and send one structured request to the ordering office the same day through its EHR inbox or portal, with the patient's name, the test and the exact missing item. Track responses by office so client services can retrain the worst offenders.

## Who Feels the Pain
Billing staff working stale denials, client services fielding repeat calls, ordering offices pestered weeks later, and patients who receive bills for tests their insurer should have paid.

## Impact If Fixed
Same-day requests get answered far more often than six-week-old ones. Recovering half of the write-offs that are now abandoned as not worth chasing would be worth ~0.5–1% of revenue (estimate) for a typical regional lab.
