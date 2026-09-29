# Niche Analysis — Physical Therapy

**Parent Industry:** [[industries/physical-therapy|Physical Therapy]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Outpatient Orthopedic PT Clinics | High Market Share | $25-28B | Medium | Clinic owner-PT or clinic director |
| 2 | Hospital-Based Outpatient PT | High Market Share | $12-15B | Medium-High | Rehab department director within a hospital/health system |
| 3 | Home-Based PT Providers | Low Digitized | $4-6B | Low | Home health agency PT director or independent PT contractor |
| 4 | Cash-Pay / Direct-Access PT | Low Digitized | $3-5B | Low | Cash-pay PT practice owner (often solo or 2-3 PTs) |
| 5 | Pelvic Floor PT Specialists | Underserved Audience | $2-3B | Low | Pelvic floor PT specialist (often solo or small group) |
| 6 | Pediatric PT Providers | Underserved Audience | $3-4B | Low | Pediatric PT practice owner or early intervention agency director |
| 7 | Prior Authorization & Concurrent Review | Highly Automatable | $2-4B (embedded) | Low-Medium | Authorization specialist, front desk coordinator, billing manager |
| 8 | Home Exercise Program (HEP) Delivery & Compliance | Highly Automatable | $2-3B (embedded) | Medium | Clinic owner-PT, treating therapists |

## Why These Niches

Physical therapy is not a monolithic market — it fragments along clinical specialty (orthopedic vs. pelvic floor vs. pediatric), care setting (clinic vs. hospital vs. home), payment model (insurance-billed vs. cash-pay), and operational function (clinical delivery vs. authorization management vs. HEP compliance). These 8 niches cover the full span: the two largest revenue segments (outpatient orthopedic and hospital-based), the two most digitally neglected (home-based PT and cash-pay practices), the two most underserved by existing tools (pelvic floor and pediatric), and the two highest-ROI automation targets (prior authorization and HEP compliance). Excluded: sports performance training (overlaps with fitness), occupational therapy (distinct licensure and billing), and inpatient acute rehab (hospital-operated, different economics entirely).

## Niches
- [[niches/physical-therapy/outpatient-orthopedic/profile|🔵 Outpatient Orthopedic PT Clinics]]
- [[niches/physical-therapy/hospital-based-outpatient/profile|🔵 Hospital-Based Outpatient PT]]
- [[niches/physical-therapy/home-based-pt/profile|🟠 Home-Based PT Providers]]
- [[niches/physical-therapy/cash-pay-direct-access/profile|🟠 Cash-Pay / Direct-Access PT]]
- [[niches/physical-therapy/pelvic-floor-specialists/profile|🟣 Pelvic Floor PT Specialists]]
- [[niches/physical-therapy/pediatric-pt/profile|🟣 Pediatric PT Providers]]
- [[niches/physical-therapy/prior-authorization/profile|⚡ Prior Authorization & Concurrent Review]]
- [[niches/physical-therapy/hep-compliance/profile|⚡ Home Exercise Program (HEP) Delivery & Compliance]]


---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the operator layer and found firms of 1-15 people; research functions do not exist at that altitude. This pass sweeps seven positions in the value chain — aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry — looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Conservative-Care Treatment Guideline Publishers | Data vendor | 100-400 | 54 | ↔ Cross-referenced |
| 10 | Rehabilitation Coding & Documentation Content | Supplier | 200-800 | 54 | ↔ Cross-referenced |
| 11 | Physical Medicine Utilization Management Networks | Payer & intermediary | 500-2,000 | 51 | ⚠️ Kill switch |
| 12 | Disability Duration & Return-to-Work Guidelines | Data vendor | 100-500 | 48 | Below threshold |
| 13 | Physical Therapy Outcomes Registries | Data vendor | 100-500 | 47 | ⚠️ Kill switch |
| 14 | Workers' Compensation Physical Medicine Networks | Payer & intermediary | 200-1,000 | 46 | ⚠️ Kill switch |
| 15 | Physical Therapy Licensure Examination Bodies | Regulatory | 60-200 | 44 | Below threshold |
| 16 | Prior Authorization Automation Vendors | Supplier | 100-600 | 42 | ⚠️ Kill switch |
| 17 | Rehabilitation EMR Analytics | Supplier | 100-500 | 41 | ⚠️ Kill switch |
| 18 | Remote Therapeutic Monitoring & Home Exercise | Supplier | 60-300 | 39 | ⚠️ Kill switch |
| 19 | Therapy Practice Rollup Corporate Analytics | Aggregator/rollup | 100-500 | 38 | ⚠️ Kill switch |
| 20 | Rehabilitation Equipment Clinical Affairs | Supplier | 30-150 | 31 | Below threshold |
| 21 | Physical Therapy Education Accreditation | Regulatory | 5-20 | — | ✗ Fails gate |

## Why These Pockets

No qualifiers, and this is now the fifth industry in the sweep where the reason is the same wall. Seven of thirteen pockets carry a live HIPAA kill switch, and they include every position where the data is genuinely valuable. The two pockets in this industry that stand outside the perimeter — conservative-care guideline publishers and rehabilitation coding content — are both already indexed under other industries, because content about treatment and content about billing are not patient data and are therefore the only businesses in healthcare that escape.

The fenced pockets are worth recording precisely because of what they hold. Utilization management networks reach 51 and hold millions of authorisation decisions joined to submitted functional measures and subsequent utilisation — the largest body of conservative-care decision data anywhere. They deny care, and reviewer-to-reviewer variance on identical clinical facts has never been measured. Outcomes registries at 47 hold millions of episodes with functional status captured at multiple points, which is one of very few large longitudinal functional datasets in existence, and they use it to report percentile ranks rather than to answer how much therapy a given patient actually needs — the exact question the authorisation apparatus above them is guessing at. Workers' compensation networks at 46 are the only setting in this industry where therapy is linked to a hard economic outcome, days until return to work, and that linkage cannot leave the perimeter.

Pass 1's four named pains each map onto a fenced pocket. Prior authorisation tracking maps onto the automation vendors, who hold the difference between published payer policy and actual approval behaviour and sell submission plumbing. Outcome measurement maps onto the registries. Home exercise adherence — described as a black hole — maps onto the remote therapeutic monitoring vendors, who filled the hole with data and have not turned it into an answer, while depending for their existence on a billing code that could be revised. Documentation burden maps onto the rehabilitation EMR vendors, who hold every therapy note ever written and generate compliance rules from a checklist.

The closest thing to an escape is disability duration guideline publishing at 48: aggregate reference content derived from very large workers' compensation and disability claim populations, sold outside the perimeter the source data sits behind. It is held back by a small editorial function and a product that describes typical durations rather than predicting them for a specific case.

## Niches — Pass 2
- [[niches/physical-therapy/conservative-care-guidelines-crossref/profile|🔍 Conservative-Care Treatment Guideline Publishers]]
- [[niches/physical-therapy/rehab-coding-content-crossref/profile|🔍 Rehabilitation Coding & Documentation Content Publishers]]
- [[niches/physical-therapy/pt-utilization-management-networks/profile|🔍 Physical Medicine Utilization Management Networks]]
- [[niches/physical-therapy/disability-duration-guideline-publishers/profile|🔍 Disability Duration & Return-to-Work Guideline Publishers]]
- [[niches/physical-therapy/pt-outcomes-registry-benchmarking/profile|🔍 Physical Therapy Outcomes Registries & Benchmarking]]
- [[niches/physical-therapy/workers-comp-physical-medicine-networks/profile|🔍 Workers' Compensation Physical Medicine Networks]]
- [[niches/physical-therapy/pt-licensure-examination-body/profile|🔍 Physical Therapy Licensure Examination Bodies]]
- [[niches/physical-therapy/prior-authorization-automation/profile|🔍 Prior Authorization Automation Vendors]]
- [[niches/physical-therapy/rehab-emr-analytics/profile|🔍 Rehabilitation EMR Analytics]]
- [[niches/physical-therapy/remote-therapeutic-monitoring-vendors/profile|🔍 Remote Therapeutic Monitoring & Home Exercise Vendors]]
- [[niches/physical-therapy/pt-rollup-corporate-analytics/profile|🔍 Therapy Practice Rollup Corporate Analytics]]
- [[niches/physical-therapy/rehab-equipment-clinical-affairs/profile|🔍 Rehabilitation Equipment Clinical Affairs]]
- [[niches/physical-therapy/pt-education-accreditation/profile|🔍 Physical Therapy Education Accreditation]]
