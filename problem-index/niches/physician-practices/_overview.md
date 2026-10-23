# Niche Analysis — Physician Practices

**Parent Industry:** [[industries/physician-practices|Physician Practices]]

## Niche Selection

A physician practice earns its money in fifteen-minute visits and the procedures, tests and drugs ordered from them, and loses it in the paperwork payers put around each one. The binding constraints are physician time (a fixed number of visit slots), payer friction (39 prior authorizations per physician per week at ~13 hours, AMA 2024) and federal rules reset every year (the CY2026 fee schedule's -2.5% efficiency adjustment, MIPS at 75 points, 511 Shared Savings ACOs). Ownership has moved fast, with 82% of physicians employed by hospitals or corporate entities by January 2026 (PAI–Avalere). The eight niches below split the industry by what vendors and practice teams actually compete over. Market sizes are estimates of tooling, services and staff spend within each niche, not practice revenue.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Ambient Documentation & Office Visit Coding | 🔵 High Market Share | ~$2B | Medium-High | CMIO / medical group president |
| 2 | Primary Care in Value-Based Contracts (ACOs & MA Risk) | 🔵 High Market Share | ~$3B | Medium | ACO executive director / group CMO |
| 3 | Referral Intake in Specialty Practices | 🟠 Low Digitized | ~$1B | Low | Practice administrator / director of patient access |
| 4 | Chronic & Advanced Primary Care Management Programs | 🟠 Low Digitized | ~$1.5B | Low-Medium | Director of care management |
| 5 | Nurse Practitioners & Physician Assistants in Physician Offices | 🟣 Underserved Audience | ~$0.6B | Medium | Medical group COO |
| 6 | Independent Pediatric Practices | 🟣 Underserved Audience | ~$0.4B | Low-Medium | Pediatric practice owner / administrator |
| 7 | Prior Authorization at the Ordering Practice | ⚡ Highly Automatable | ~$5B | Medium | Director of revenue cycle / authorization manager |
| 8 | MIPS & Quality Measure Reporting | ⚡ Highly Automatable | ~$0.8B | Medium-High | Practice quality manager |

## Why These Niches

The two market-share niches are where the practice's revenue is decided. Office E/M visits are the core of most practices' billing, and ambient scribes are the fastest-moving spend in the industry. With athenahealth now bundling its scribe free, the contest has moved from writing the note to defending the code. Value-based contracts carry the largest pools of money at stake: the Shared Savings Program's 511 ACOs earned $4.1B in shared savings for 2024 (CMS), on top of MA capitation. The two low-digitized niches are where fax and phone still run the work: inbound referrals to specialists, and the monthly calls behind chronic and advanced primary care management billing. The two underserved audiences are the 217,640 NPs and PAs in physicians' offices (BLS), whose billing and supervision rules the tools ignore, and independent pediatricians, who run two vaccine inventories under VFC with adult-centric software. The two automatable niches are the most rule-bound work in the office: assembling prior authorization evidence against published criteria, and reporting MIPS measures from data the practice already holds.

## Niches

- [[niches/physician-practices/ambient-documentation-visit-coding/profile|🔵 Ambient Documentation & Office Visit Coding]]
- [[niches/physician-practices/value-based-primary-care-contracts/profile|🔵 Primary Care in Value-Based Contracts (ACOs & MA Risk)]]
- [[niches/physician-practices/specialty-referral-intake/profile|🟠 Referral Intake in Specialty Practices]]
- [[niches/physician-practices/chronic-care-management-programs/profile|🟠 Chronic & Advanced Primary Care Management Programs]]
- [[niches/physician-practices/nps-pas-in-physician-offices/profile|🟣 Nurse Practitioners & Physician Assistants in Physician Offices]]
- [[niches/physician-practices/independent-pediatric-practices/profile|🟣 Independent Pediatric Practices]]
- [[niches/physician-practices/ordering-practice-prior-authorization/profile|⚡ Prior Authorization at the Ordering Practice]]
  - [[niches/physician-practices/imaging-procedure-authorization/profile|🎯 Imaging & Procedure Authorization]]
  - [[niches/physician-practices/medical-benefit-drug-access/profile|🎯 Medical-Benefit Drug Access (Buy-and-Bill & Infusions)]]
- [[niches/physician-practices/mips-quality-reporting/profile|⚡ MIPS & Quality Measure Reporting]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Prior Authorization at the Ordering Practice** is not. Writing its sentence produced two contests with different winners. Scans and procedures are won by first-pass approval: parse the payer's or radiology benefit manager's criteria, find each fact in the chart, and avoid the peer-to-peer. Infused and injected drugs are won before the authorization: confirm medical versus pharmacy benefit and site of care, prove step therapy, line up manufacturer and foundation funding, and keep authorized units in step with billed units. Staff, vendors (Commure, Cair Health and SuperDial on one side; hubs, SamaCare, Mandolin and Infinitus on the other) and the cost of failure (a denied scan versus an unfunded five-figure dose) differ. It decomposes into **Imaging & Procedure Authorization** and **Medical-Benefit Drug Access**.

Three terminal calls were close. **Ambient Documentation & Office Visit Coding** could split into note quality and coding accuracy. It stays one niche because EHR bundling has made note drafting a commodity, and every vendor now competes on whether the note supports the code. **Primary Care in Value-Based Contracts** could split into MSSP and MA risk. The rules differ, but the work (attribution, gaps, risk capture) and the buyer are the same, and the contest is one year-end settlement. **Chronic & Advanced Primary Care Management Programs** overlaps niche 2, since enablers run care management too. It stays separate because its contest is monthly billability under fee-for-service codes, while niche 2's is the year-end savings settlement.

Five candidates were considered and rejected. **Credentialing and payer enrolment** is the same work and contest as [[niches/behavioral-health-clinics/credentialing-operations/profile|⚡ Credentialing & Payer Enrollment Operations]], with verification firms at [[niches/behavioral-health-clinics/credentialing-verification-orgs/profile|🔍 Credentialing Verification Organizations]] (42). The advanced-practice-specific part sits in niche 5. **Front-desk phones and scheduling** belong to [[niches/scheduling-booking-platforms/no-show-and-attendance/profile|🔵 No-Show & Attendance]] and [[niches/answering-services/medical-after-hours/profile|🔵 Medical After-Hours Answering]]. The practice's own phone queue appears as worker-life 1 and agent 2. **Private-equity MSO integration** is a buyer segment present in every niche. Its integration contest splits into EHR conversion, already [[niches/healthcare-practice-software/ehr-data-migration-services/profile|⚡ EHR Data Migration & Conversion]], and payer re-enrolment, and its analytics is Pass 2 pocket 14. **Payer contract modelling** is low-impact 2. As a niche its contest repeats [[niches/medical-billing/payment-posting-reconciliation/profile|⚡ Payment Posting & Reconciliation]] and [[niches/general-hospitals/payer-contract-modelling-underpayments/profile|🎯 Payer Contract Modelling & Underpayment Recovery]]. **Eligibility and patient estimates** repeat [[niches/urgent-care/insurance-verification-coding/profile|⚡ Insurance Verification & Coding]] and [[niches/general-hospitals/patient-access-auth-estimates/profile|⚡ Patient Access: Prior Authorization, Eligibility & Estimates]].

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. This pass sweeps seven positions in the value chain: aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry. It looks for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`. Pockets already profiled under other industries are linked in the prose below rather than profiled again.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Office-Based Specialty Registries & QCDRs | Association | 20-150 | 43 | ⚠️ Kill switch |
| 10 | Drug Coverage Policy & Prior-Authorization Criteria Databases | Data vendor | 30-150 | 40 | Below threshold |
| 11 | Medical Practice Cost & Operations Benchmarks | Association | 20-60 | 38 | Below threshold |
| 12 | Manufacturer Hub & Field Reimbursement Services | Supplier | 20-100 | 38 | ⚠️ Kill switch |
| 13 | Electronic Prior Authorization Networks | Payer & intermediary | 20-100 | 37 | ⚠️ Kill switch |
| 14 | Private-Equity Specialty Platforms & Physician MSO Analytics | Aggregator/rollup | 20-150 | 36 | ⚠️ Kill switch |
| 15 | Shared Savings ACO Enablement Analytics | Aggregator/rollup | 30-300 | 35 | ⚠️ Kill switch |
| 16 | Medicare Physician Payment & MIPS Measure Contractors | Regulatory | 30-150 | 34 | ⚠️ Kill switch |
| 17 | Physician Practice Sell-Side M&A Advisors | Specialist advisory | 10-40 | 32 | ⚠️ Kill switch |
| 18 | AMA RUC & Specialty Society RVU Surveys | Association | 10-25 | 28 | Below threshold |
| 19 | Independent Physician Associations & Clinically Integrated Networks | Aggregator/rollup | <10 each | — | Fails gate |
| 20 | MAC Medical Directors & Local Coverage Policy | Regulatory | <10 each | — | Fails gate |

## Why These Pockets

No pocket qualifies. The practice itself is not a qualifier, and neither are the organisations that own practices. Their insight is spent on care, deals and margin, never invoiced, and almost everything they analyse is PHI. The private-equity platforms (36), the ACO enablers (35) and hospital owners all fail on the same two counts. The data-rich pockets around the practice are fenced the same way: the office-based specialty registries (43) and the hub operators (38) hold identified records or client-owned programme data, and the ePA networks (37) process transactions they cannot reuse. Much of the physician-practice insight layer is already in the vault and scores the same way:

- Revenue cycle is [[niches/medical-billing/rcm-platform-analytics/profile|🔍 Revenue Cycle Platform Analytics]] (55, kill switch), [[niches/medical-billing/healthcare-clearinghouses/profile|🔍 Healthcare Claims Clearinghouses]] (52, kill switch), [[niches/medical-billing/denial-management-analytics-vendors/profile|🔍 Denial Management Analytics Vendors]] (48), [[niches/medical-billing/coding-audit-compliance-firms/profile|🔍 Coding Audit & Compliance Firms]] (46) and the EHR vendors at [[niches/medical-billing/practice-management-ehr-data/profile|🔍 Practice Management & EHR Data Teams]] (45, kill switch).
- Licensed criteria publishers (MCG, InterQual, ODG) are indexed at [[niches/acupuncture-practices/conservative-care-guideline-publishers/profile|🔍 Conservative-Care Treatment Guideline Publishers]] (54). The radiology and specialty benefit managers that apply criteria to outpatient requests (EviCore, Carelon) sit in [[niches/health-insurance-carriers/utilization-management/profile|🔵 Utilization Management & Prior Authorization]]. Payer reimbursement and HTA consultancies are indexed at [[niches/medical-device-mfg/reimbursement-hta-strategy/profile|🔍 Reimbursement & Health Technology Assessment Strategy]] (51). Medicare's auditors are [[niches/medical-billing/cms-program-integrity/profile|🔍 Federal Programme Integrity Contractors]] (49).
- Code sets and clinical content qualify where they carry no PHI: [[niches/medical-billing/medical-coding-content-publishers/profile|🔍 Medical Coding Content Publishers]] (54) and [[niches/urgent-care/clinical-reference-decision-support/profile|🔍 Clinical Reference & Decision Support Content Publishers]] (54).
- Physician pay is [[niches/hr-consultants/compensation-survey-publishers/profile|🔍 Compensation Survey Publishers]] (54) and [[niches/general-hospitals/physician-fmv-valuation/profile|🔍 Physician Compensation & Fair Market Value Advisory]] (46, kill switch). Payer rate negotiation is [[niches/urgent-care/payer-contracting-advisory/profile|🔍 Payer Contracting & Rate Negotiation Advisory]] (45), and negotiated rates are [[niches/medical-billing/price-transparency-data-vendors/profile|🔍 Healthcare Price Transparency Data]] (49).
- Physician malpractice is written by the same insurers and benchmarked by the same databases as [[niches/general-hospitals/hospital-malpractice-claims-benchmarking/profile|🔍 Hospital Malpractice Claims Benchmarking]] (40, kill switch). CAHPS for MIPS surveys sit with [[niches/health-insurance-carriers/cahps-hos-survey-vendors/profile|🔍 CAHPS & HOS Survey Vendors]] (37).
- Physician directories and referral-leakage analytics are [[niches/directory-and-list-publishers/hcp-reference-directories/profile|🔍 Healthcare Professional Reference Directories for Life Sciences]] (37) and [[niches/general-hospitals/service-line-forecasting-data/profile|🔍 Service-Line Demand Forecasting & Strategy Data]] (40). Ambient scribe vendors are [[niches/document-preparation-services/clinical-speech-ambient-vendors/profile|🔍 Clinical Speech Recognition & Ambient Documentation Vendors]] (27).
- State reviewers of private-equity physician deals include the agencies at [[niches/general-hospitals/state-hospital-cost-oversight/profile|🔍 State Hospital Cost & Price Oversight Agencies]] (31).

The coordinator asked for nine angles to be tested, and each lands on a pocket that fails. Prior authorization meets the drug coverage policy databases (40, clean but no outside clock), the ePA networks (37, whose insight product alone scores ~36) and the already-indexed criteria publishers (54). MIPS meets the registries (43) and CMS's measure contractors (34). ACO and MSSP work meets the enablers (35) and PE rollups the platforms (36). The fee schedule meets the RUC (28), which has a hard federal clock but nothing invoiced and a single buyer. Ambient, referral leakage, no-shows and credentialing are already profiled elsewhere (links above).

The two nearest misses fail in opposite ways. The registries (43) own the deepest office-based clinical corpus and submit MIPS data against a federal deadline, but they work on identified EHR extracts, as the hospital registries (41) do. Their clean half, the de-identified real-world evidence Verana sells, would score only ~44–46 alone because it runs on its own calendar. The drug coverage policy databases (40) are clean, sell the insight itself and sit on the payer-policy reading behind this industry's prior-authorization MVP, but the policies are public and no outside party sets a deadline on the vendor's work. The practical lesson for placement is the one in the hub: the buyers worth approaching are the vendors hiring forward deployed engineers to sell into practices, not the practices.

## Niches — Pass 2
- [[niches/physician-practices/specialty-society-office-registries/profile|🔍 Office-Based Specialty Registries & QCDRs]]
- [[niches/physician-practices/drug-coverage-policy-databases/profile|🔍 Drug Coverage Policy & Prior-Authorization Criteria Databases]]
- [[niches/physician-practices/practice-cost-operations-benchmarks/profile|🔍 Medical Practice Cost & Operations Benchmarks]]
- [[niches/physician-practices/manufacturer-hub-reimbursement-services/profile|🔍 Manufacturer Hub & Field Reimbursement Services]]
- [[niches/physician-practices/epa-network-transaction-data/profile|🔍 Electronic Prior Authorization Networks]]
- [[niches/physician-practices/pe-specialty-platform-analytics/profile|🔍 Private-Equity Specialty Platforms & Physician MSO Analytics]]
- [[niches/physician-practices/mssp-aco-enablement-analytics/profile|🔍 Shared Savings ACO Enablement Analytics]]
- [[niches/physician-practices/physician-payment-measure-contractors/profile|🔍 Medicare Physician Payment & MIPS Measure Contractors]]
- [[niches/physician-practices/practice-sell-side-ma-advisors/profile|🔍 Physician Practice Sell-Side M&A Advisors]]
- [[niches/physician-practices/ama-ruc-rvu-surveys/profile|🔍 AMA RUC & Specialty Society RVU Surveys]]
- [[niches/physician-practices/ipas-clinically-integrated-networks/profile|🔍 Independent Physician Associations & Clinically Integrated Networks]]
- [[niches/physician-practices/mac-medical-directors-lcds/profile|🔍 MAC Medical Directors & Local Coverage Policy]]
