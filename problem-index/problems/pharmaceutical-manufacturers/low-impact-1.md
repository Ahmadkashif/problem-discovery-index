# Batch Record Review by Exception

**Industry:** [[pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Electronic batch record systems promise review by exception, but most plants still review every page of a paper or hybrid record because the exception rules that would make that safe were never written for their products.
**Tags:** #cnns #transfer-learning #autoencoders #feature-engineering #compliance #automation #workflow-orchestration

## The Problem
Before a batch can be released, QA must review the executed batch production record under 21 CFR 211.188 and 211.192: every weighing, every in-process check, every signature and second-person verification, every alarm and every deviation reference. An oral-solid record runs to roughly 100–500 pages and a sterile record to more (estimate). At a plant on paper or hybrid records, which still describes much of the generic and CDMO base (estimated at 60–70% of plants), a reviewer reads each page, checks each calculation, and sends corrections back to production for good documentation practice fixes. A record can bounce two or three times. Review time sits directly on release time, and release time is inventory.

## What Already Exists
Manufacturing execution and eBR systems (Körber PAS-X, Emerson Syncade, Siemens Opcenter, and newer frontline platforms such as Tulip, Apprentice.io's Tempo, Leucine and Seal) enforce entries at the point of execution, check limits in real time and can generate an exceptions report so QA reviews only what went outside the expected path. Document capture and OCR tools digitise paper records. Generic process-mining and BI tools can trend cycle times.

## The Customisation Gap
Review by exception is only as good as the exception rules, and those rules are product- and site-specific. Someone has to define, for each master batch record, which excursions are critical, which are covered by an approved alarm response, which in-process results trend toward a limit without crossing it, and which manual entries (handwritten times, corrected weights, late signatures) need a human look. Plants migrating from paper carry thousands of legacy records whose handwriting, strike-throughs and attachments no generic OCR model reads reliably, and whose history is the only way to set sensible limits. QA also needs the exceptions linked to open deviations and to the stability and complaint record for that product, which sits in other systems. None of this ships with the eBR. It is configuration and validation work done per product, and most plants never finish it, so they keep reviewing every page in the electronic system too.

## Impact If Solved
If QA reviewed only flagged entries on records whose exception rules were validated, review time per batch could fall from 2–8 hours to under one, and release lead time by two to four days (estimates), freeing working capital at every plant. QA reviewers would spend their attention on the handful of entries that actually change the release decision.
