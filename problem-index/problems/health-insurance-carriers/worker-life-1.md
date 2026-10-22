# The Quality Nurse in HEDIS Chase Season

**Industry:** [[health-insurance-carriers|Health Insurance Carriers]]
**Type:** Worker Life Changing
**One-liner:** From January to June, quality nurses read thousands of retrieved medical records looking for one blood pressure reading or one screening date per member. What they would get back is the season, and the clinical judgement the job was supposed to use.
**Tags:** #transformers #bert #large-language-models #evaluation-metrics #worker-facing #automation #workflow-orchestration

## The Problem
Some HEDIS quality measures can be reported from claims, but the "hybrid" measures, such as blood pressure control, diabetes HbA1c control, prenatal and postpartum care and childhood immunisations, allow plans to add evidence found in medical records for a sample of members. Each year, after the measurement year closes on 31 December, a plan draws samples (commonly a few hundred members per measure per product, estimate) and sends chart requests to thousands of provider offices. Retrieved records come back as faxes, scanned PDFs and EHR exports. Quality nurses, many of them temporary staff hired for the season, then read each one for the specific qualifying evidence: the most recent blood pressure in the measurement year, taken in the right setting, with both numbers recorded, or a dated retinal exam result.

Every hit has to survive the NCQA-licensed auditor's medical record review validation. A failed sample can force the plan to report a measure from administrative data alone, which usually means a lower rate. The audited results are due to NCQA in June and feed Medicare Star Ratings and state Medicaid quality programmes worth substantial bonus money.

## Why It Matters to the Worker
The work is tedious and high-stakes at the same time. A nurse may review ~20–40 charts a day (estimate), scrolling through 200-page records for a single value. Productivity is measured, overtime is expected as June approaches, and an abstraction error that the auditor catches reflects on the nurse personally. The job uses almost none of the clinical training that brought them into quality work: improving care for the members whose measures are failing.

Many of these nurses are on seasonal contracts, which means the same chase every year with no carry-over of what they learned about which practices file which results where.

## What a Solution Looks Like
Document models that read each retrieved record, find the candidate evidence for each sampled measure (readings, dates, test results, exclusions) and present it to the nurse with the page and line highlighted. The nurse confirms, corrects or rejects in seconds instead of searching. Records with no qualifying evidence are flagged early, so the plan can request a second record from another provider while there is still time. Every confirmed hit is stored with its source, ready for the auditor's over-read.

## Impact If Solved
If the nurse's role moved from searching to confirming, a plan could abstract its hybrid samples with ~40%–60% fewer seasonal abstractors (estimate) and finish weeks before the June deadline. Most of all, quality nurses would get their spring back for outreach to members with open care gaps, which is what actually moves the measure.
