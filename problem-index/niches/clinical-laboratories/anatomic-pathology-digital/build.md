# Case Prioritisation Before the Pathologist Opens the Slide

**Niche:** [[niches/clinical-laboratories/anatomic-pathology-digital/profile|Anatomic Pathology & the Digital Transition]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pathologists read benign and malignant cases in the order they were cut, and the immunostains a malignant case needs are ordered only after it is read.
**Tags:** #transformers #cnns #contrastive-learning #transfer-learning #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to raise the cases each pathologist signs out per day, and whoever raises it with no rise in amended reports takes the account.

## The Problem
A pathologist's day is a tray or worklist of cases in accession order. Most biopsies are benign or routine; a minority need careful review, extra levels or immunostains, which add a day when ordered after the first read. Urgent cases are flagged only if the clinician wrote "rush".

## Why Nobody Has Built This
AI products in pathology have been cleared organ by organ for detection, not for running the whole worklist. Triage needs a model across the lab's full case mix, integrated with the AP LIS and the stain lab, and validated as a lab procedure.

## What to Build
Use a pathology foundation model to score each scanned case for likelihood of malignancy or atypia and for probable stain needs. Re-order the worklist so significant cases are read first, pre-order likely stains in parallel for pathologist confirmation, and route suspected low-risk cases to a faster review mode. Measure, per pathologist, cases signed out per day and amended-report rates before and after.

## Target Customer
Pathology groups and reference labs that already scan routinely, starting with high-volume specimen types such as GI, prostate, skin and breast biopsies.

## Impact If Built
If stain pre-ordering saves a day on the ~15% of cases that need stains and triage lifts throughput 10% (estimates), a 20-pathologist group gains the output of two pathologists in a specialty with a 28.5% vacancy rate.
