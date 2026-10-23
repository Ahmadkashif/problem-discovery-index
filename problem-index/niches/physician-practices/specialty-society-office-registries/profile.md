# Office-Based Specialty Registries & QCDRs

**Parent Industry:** [[industries/physician-practices|Physician Practices]]
**Category:** Insight Layer
**Value-Chain Position:** Association research arms

## What They Do
Specialty societies run registries that pull data directly from member practices' EHRs, report MIPS quality measures for members as Qualified Clinical Data Registries, and return benchmark dashboards. The American Academy of Ophthalmology's IRIS Registry holds data on more than 75M patients and 450M visits. The neurologists' Axon and urologists' AQUA registries are smaller, and dermatology (DataDerm) and gastroenterology (GIQuIC) run their own (Verana's 2022 figures, search summary). Verana Health, the data partner for IRIS and Axon, curates over 90M de-identified patients and sells real-world evidence to life-science companies (Verana, 2023). This is the office-based counterpart of the hospital registries at [[niches/general-hospitals/clinical-outcomes-registries/profile|🔍 Clinical Outcomes Registries]] (41).

## Insight Function
**Size:** ~20-150 data scientists, epidemiologists and registry analysts per registry programme and its data partner (estimate)
**Output:** MIPS submissions for members, benchmark dashboards, research publications, de-identified real-world datasets and studies for drug and device makers
**Proprietary data:** Longitudinal office records, including imaging-linked ophthalmology visits, at a scale no claims set matches
**Clock:** MIPS data submission closes on 31 March after the performance year (CMS-1832-F, 90 FR 49604), a hard date on the registry's submission work; real-world evidence releases and studies run on the data partner's and clients' calendars
**Buyer:** Registry director at the society, or head of data science at the data partner

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **43/60** |

**Kill switches:** **HIPAA**, on the registry-submission half. The registries extract identifiable patient records from member EHRs under business associate and participation agreements to report MIPS, and that half sets the pocket's verdict. Scored consistently with the hospital registries (41, kill switch). The de-identified real-world-evidence half that Verana sells is clean under the product-rights ruling. Scored alone it falls below threshold at ~44–46 (Q1 5, Q2 3, Q3 5, Q4 2, Q5 2–3), because its releases run on its own calendar and no outside party sets a deadline on that work.
**Verdict:** Logged — kill switch. The deepest office-based clinical corpus in the industry, held by a handful of societies, behind PHI.
