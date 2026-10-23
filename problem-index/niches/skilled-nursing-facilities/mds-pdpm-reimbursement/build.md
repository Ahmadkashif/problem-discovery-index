# An Evidence Map for Every PDPM Item

**Niche:** [[niches/skilled-nursing-facilities/mds-pdpm-reimbursement/profile|MDS Assessment & PDPM Reimbursement]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Before an MDS is transmitted, nobody can see in one place which chart entries support each payment-driving item and which items have no support at all.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to turn what the floor documents into MDS coding that captures each resident's full PDPM and Medicaid case-mix, and whoever captures the most case-mix that still survives Medicare and Medicaid MDS audits takes the account.

## The Problem
An MDS coordinator closing a 5-day assessment works from the hospital discharge summary, therapy evaluations, three days of CNA ADL flowsheets, nurse notes and the medication record. She hunts for evidence of each comorbidity on the NTA list, each swallowing or cognitive item that drives SLP, and each nursing item. When a code is challenged months later, the evidence has to be rebuilt from the chart by whoever is in the job then.

## Why Nobody Has Built This
EHR vendors calculate PDPM from coded items rather than auditing the items themselves. Hospital CDI vendors target physician documentation and DRGs, not the RAI Manual. Consultancies sell the audit as hours and have little reason to automate it. Until LLMs, extracting evidence from SNF documentation, much of it templated checkboxes and short free text, was not reliable enough to trust.

## What to Build
A pre-transmission layer that, for every open assessment, reads the chart within each item's look-back window and proposes codes with linked evidence spans. It marks items coded without support, items supported but not coded, and Section GG scores that conflict across disciplines. It suggests the assessment reference date that captures the highest supportable acuity, and an Interim Payment Assessment when the resident's condition changes. Each suggestion carries the RAI Manual rule it applied. Measure it on under-coding and over-coding separately, against senior MDS nurses on a double-coded sample.

## Target Customer
Directors of clinical reimbursement at chains of 10–200 facilities, who carry case-mix targets and audit exposure across buildings; secondarily, independents through their consultants.

## Impact If Built
Captured case-mix moves only where it is defensible. A ~1–2% net correction (estimate) is worth ~$18,000–36,000 a year on the ~$1.8M of fee-for-service Part A revenue an average freestanding SNF receives (MedPAC; derived). Each coordinator handles ~20–30% more assessments a week (estimate), and audit responses become a retrieval rather than a reconstruction, which matters more now that CMS is asking about upcoding.
