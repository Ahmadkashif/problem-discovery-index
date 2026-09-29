# Niche Analysis — Chiropractic Practices

**Parent Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Personal Injury / Auto Accident | 🔵 High Market Share | $6B | Medium | PI Chiropractor / Clinic Owner |
| 2 | Cash-Pay Wellness & Maintenance | 🔵 High Market Share | $4B | Low-Medium | Wellness-Focused DC |
| 3 | Palpation & Tactile Assessment Digitization | 🟠 Low Digitized | $500M | Low | DC with 10+ Years Experience |
| 4 | Pediatric & Family Chiropractic | 🟠 Low Digitized | $1.5B | Low | Pediatric-Certified DC |
| 5 | Geriatric & Senior Care | 🟣 Underserved Audience | $1.2B | Low | DC Near Senior Communities |
| 6 | Athlete & Sports Performance | 🟣 Underserved Audience | $2B | Medium | Sports-Certified DC (CCSP/DACBSP) |
| 7 | Insurance Billing & Documentation | ⚡ Highly Automatable | $3B | Medium | Billing Manager / Clinic Owner |
| 8 | Treatment Plan Compliance Tracking | ⚡ Highly Automatable | $1B | Low-Medium | DC / Office Manager |

## Why These Niches

Personal injury and cash-pay wellness are the two dominant revenue models — PI practices earn high per-case revenue through attorney-referred accident cases, while cash-pay practices build recurring revenue through maintenance care. Palpation digitization is the highest-potential ML opportunity in the entire industry — experienced chiropractors develop tactile diagnostic abilities over decades that are currently impossible to transfer to new practitioners or validate objectively. Pediatric and geriatric chiropractic are structurally underserved demographics with unique clinical requirements. Insurance billing and treatment plan compliance are the two highest-ROI automation targets, consuming 30-40% of practice overhead.

## Niches
- [[niches/chiropractic-practices/personal-injury/profile|🔵 Personal Injury / Auto Accident]]
- [[niches/chiropractic-practices/cash-pay-wellness/profile|🔵 Cash-Pay Wellness & Maintenance]]
- [[niches/chiropractic-practices/palpation-digitization/profile|🟠 Palpation & Tactile Assessment Digitization]]
- [[niches/chiropractic-practices/pediatric-family/profile|🟠 Pediatric & Family Chiropractic]]
- [[niches/chiropractic-practices/geriatric-senior/profile|🟣 Geriatric & Senior Care]]
- [[niches/chiropractic-practices/sports-performance/profile|🟣 Athlete & Sports Performance]]
- [[niches/chiropractic-practices/insurance-billing/profile|⚡ Insurance Billing & Documentation]]
- [[niches/chiropractic-practices/treatment-compliance/profile|⚡ Treatment Plan Compliance Tracking]]


---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the operator layer and found practices of 1-10 people; research functions do not exist at that altitude. This pass sweeps seven positions in the value chain — aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry — looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`.

Scoped to where chiropractic's economics are actually decided — auto injury and workers' compensation adjudication. The CAM network managers and conservative-care guideline publishers that also govern this industry were logged under `acupuncture-practices` and are not duplicated.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Auto Injury Claims Data & Medical Review Analytics | Payer & intermediary | 200-800 | **54** | ✅ Indexed |
| 10 | Independent Medical Examination Firms | Specialist advisory | 500-3,000 | 51 | ⚠️ Kill switch |
| 11 | Healthcare Cost Benchmark Data Organizations | Data vendor | 50-200 | **50** | ✅ Indexed |
| 12 | Chiropractic Board Examination & Practice Analysis | Association research arm | 30-80 | 44 | Below threshold |
| 13 | Spinal Imaging Analysis Vendors | Supplier | 15-60 | 44 | ⚠️ Kill switch |
| 14 | Chiropractic Franchise & DSO Analytics | Aggregator/rollup | 15-60 | 40 | Below threshold |
| 15 | Chiropractic Coding & Compliance Publishers | Specialist advisory | 10-40 | 39 | Below threshold |
| 16 | Insurance Fraud Investigation Bureaus | Regulatory | 100-400 | 37 | Below threshold |
| 17 | Chiropractic Malpractice Underwriting Research | Payer & intermediary | 10-40 | 34 | Below threshold |
| 18 | Chiropractic Practice Management Vendor Data Teams | Supplier | 10-40 | 34 | ⚠️ Kill switch |
| 19 | Chiropractic Academic Research Centres | Association research arm | 15-50 | 32 | ⚠️ Kill switch |
| 20 | Chiropractic Continuing Education Providers | Supplier | 2-10 | — | ✗ Fails gate |
| 21 | State Chiropractic Licensing Boards | Regulatory | 2-10 | — | ✗ Fails gate |

## Why These Pockets

Chiropractic's revenue is largely decided by people arguing about whether a course of care was necessary and what it was worth, and both qualifiers sit on the deciding side of that argument.

The more interesting finding is a compliance one. Behavioral health showed that HIPAA kills most healthcare-adjacent pockets; this industry shows precisely where the exception lies. Property and casualty insurers are not HIPAA covered entities, so the auto injury claims data vendors — who hold a contributed all-industry claims repository covering effectively the whole US P&C market — clear a gate that fires on almost everything else touching medical information. That is a structural distinction worth carrying forward: the insurance side of healthcare data is accessible in a way the clinical side is not. The benchmark organizations qualify for the parallel reason, holding de-identified claims contributed expressly for publication.

Their gaps are the same shape as elsewhere but sharper because the outputs are adversarially tested. Provider profiling scores drive denials, investigations, and referrals, and nobody measures how often the flagged provider turned out to be doing anything wrong, because the adjudicated outcome is never joined back to the flag — in a product category already litigated on exactly that ground. Benchmark figures are cited in arbitration under federal surprise billing rules years after publication, and reconstructing what produced a given figure is manual archaeology rather than a stored property.

The kill switch on IME firms is worth stating plainly, because at 51 it would otherwise index and it is structurally the closest healthcare analogue to forensic litigation support in accounting: the written opinion is unambiguously the invoice, the clock is a court schedule, and the accumulated record of which opinions survived cross-examination is a genuine proprietary asset. It is unavailable because the working corpus is identified clinical records under both HIPAA and litigation privilege.

## Niches — Pass 2
- [[niches/chiropractic-practices/auto-injury-claims-data/profile|🔍 Auto Injury Claims Data & Medical Review Analytics]]
- [[niches/chiropractic-practices/ime-report-firms/profile|🔍 Independent Medical Examination Firms]]
- [[niches/chiropractic-practices/healthcare-cost-benchmark-nonprofits/profile|🔍 Healthcare Cost Benchmark Data Organizations]]
- [[niches/chiropractic-practices/nbce-board-psychometrics/profile|🔍 Chiropractic Board Examination & Practice Analysis]]
- [[niches/chiropractic-practices/spinal-imaging-ai-vendors/profile|🔍 Spinal Imaging Analysis Vendors]]
- [[niches/chiropractic-practices/chiropractic-franchise-analytics/profile|🔍 Chiropractic Franchise & DSO Analytics]]
- [[niches/chiropractic-practices/chiropractic-coding-compliance-publishers/profile|🔍 Chiropractic Coding & Compliance Publishers]]
- [[niches/chiropractic-practices/insurance-fraud-investigation-bureaus/profile|🔍 Insurance Fraud Investigation Bureaus]]
- [[niches/chiropractic-practices/chiropractic-malpractice-underwriting/profile|🔍 Chiropractic Malpractice Underwriting Research]]
- [[niches/chiropractic-practices/chiropractic-ehr-data-teams/profile|🔍 Chiropractic Practice Management Vendor Data Teams]]
- [[niches/chiropractic-practices/chiropractic-research-centers/profile|🔍 Chiropractic Academic Research Centres]]
- [[niches/chiropractic-practices/chiro-ce-content-providers/profile|🔍 Chiropractic Continuing Education Providers]]
- [[niches/chiropractic-practices/state-chiropractic-boards/profile|🔍 State Chiropractic Licensing Boards]]
