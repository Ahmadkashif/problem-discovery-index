# Hospital CDI Platforms Retooled for the RAI Manual

**Niche:** [[niches/skilled-nursing-facilities/mds-pdpm-reimbursement/profile|MDS Assessment & PDPM Reimbursement]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clinical documentation integrity software already reads charts and queries clinicians in hospitals; skilled nursing needs the same engine pointed at MDS items instead of DRGs.
**Tags:** #large-language-models #bert #transformers #compliance #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn what the floor documents into MDS coding that captures each resident's full PDPM and Medicaid case-mix, and whoever captures the most case-mix that still survives Medicare and Medicaid MDS audits takes the account.

## The Problem
SNFs have the same documentation-to-payment gap hospitals had a decade ago, without the tools. Physician and nurse practitioner documentation in the building is sparse, and diagnoses that drive PDPM often appear only in the hospital record. Nobody sends a structured query when a diagnosis is implied but not stated.

## What Already Exists
Hospital CDI and computer-assisted coding platforms such as Solventum 360 Encompass, Optum CAC and Iodine read physician documentation, suggest ICD-10 codes, prioritise records for CDI specialists and generate compliant physician queries.

## The Customization Gap
The adaptation needs: (1) MDS items, not only ICD-10 codes, as targets, with RAI Manual look-back periods per item; (2) PDPM clinical category mapping and the NTA comorbidity list; (3) Section GG "usual performance" logic across nursing and therapy; (4) state Medicaid PDPM variants and their documentation rules; (5) queries routed to the facility's attending physicians and nurse practitioners, who are rarely on site; and (6) integration into PointClickCare or MatrixCare assessment screens rather than a hospital CDI worklist.

## Target Customer
Chains whose clinical reimbursement teams already run hospital-style query processes by email, and CDI vendors looking for a post-acute market.

## Impact If Solved
A proven documentation-integrity method reaches a payment system where one coded item moves both the Medicare and Medicaid rate. If queries close half the comorbidity gaps coordinators find (estimate), the facility captures part of a ~1–2% case-mix correction, ~$18,000–36,000 a year on average fee-for-service Part A revenue (MedPAC; derived), in both payers' rates.
