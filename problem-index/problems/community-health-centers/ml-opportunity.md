# Machine Learning Opportunities — Community Health Centers

**Industry:** [[community-health-centers|Community Health Centers]]
**Derived from:** [[problems/community-health-centers/high-impact|High Impact]], [[problems/community-health-centers/low-impact-1|Low Impact 1]], [[problems/community-health-centers/low-impact-2|Low Impact 2]], [[problems/community-health-centers/worker-life-1|Worker Life 1]], [[problems/community-health-centers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Care Team's Read of Who Is About to Drop Out of Care
#tacit-knowledge-ml #gradient-boosting #survival-analysis #transformers #causal-inference #evaluation-metrics #worker-facing

**Problem statement:** Experienced community health workers and nurse care managers sense which high-risk patients are about to fall out of care, and show it only by whom they call first, how hard they try and what they arrange. The ML problem is to learn that prioritisation, joined to the outcomes that follow, and rank each morning's outreach queue so a worker sees the patients she would otherwise have missed, with a reason and the action that worked for similar patients.

**ML task:** Patient-level discrete-time survival (time to loss of care, 90- and 180-day horizons) with calibrated risk tiers, plus uplift estimation of outreach actions (call, ride, interpreter, eligibility help) from observational data
**Input data:** Appointment history (kept, cancelled, no-show, lead time), in-house pharmacy fills and days overdue, transport and interpreter requests, eligibility responses with coverage end dates, chronic-measure trends (blood pressure, HbA1c), social-needs screens, outreach logs (who was contacted, in what order, channel, attempts, barrier found), worker note text in English and Spanish, and admission and emergency alerts from HIE feeds
**Target:** Loss of care (no kept visit within the measure's clinical interval), with secondary targets of uncontrolled at next reading, coverage lost at renewal and emergency visit within 90 days; for uplift, the change in the probability of a kept visit attributable to each outreach action
**Evaluation metric:** Recall of eventual drop-outs among patients the worker did not prioritise, at a fixed daily queue size (for example, five per worker), alongside precision at that size and calibration by site, language and payer. AUROC alone misleads, because the base rate is high in some panels and low in others. Costs are asymmetric: a missed drop-out is a year of uncontrolled disease and lost PPS revenue, while a false flag costs one call.
**Scope:** The data-collection challenge comes first. The worker's read is never charted as a prediction, so the system must log her prioritisation and parse her notes, and outcomes must be joined from scheduling, pharmacy, state eligibility files and HIE feeds. The labelling challenge is that outreach prevents the outcome that would label it. Contacted patients who stayed look like false positives, so uplift needs comparison with similar uncontacted patients, using inverse propensity weighting or natural experiments such as staff absences. Workers also vary with themselves after a loss and in the weeks before the UDS deadline. The deployment challenge is speed. The queue must beat the worker's own list, explain itself in her words and run on a phone between home visits. Team: 2 ML engineers, a data engineer for eligibility and HIE feeds, and a CHW supervisor as product lead. Expect 8–12 months to a validated silent run in one multi-site center, then a stepped rollout by care team.
**Data availability:** All of it sits with the center under HIPAA. Outreach logs are often in spreadsheets or care-management modules and need a structured capture step before training. HCCNs and FQHC-led ACOs hold pooled data for several centers under member agreements. A demo can use Synthea patients with simulated outreach and attrition, which shows the pipeline but not the real signal.

---

## 2. CY2026 UDS Readiness Checker (Two-Week MVP)
#large-language-models #descriptive-statistics #hypothesis-testing #evaluation-metrics #compliance #quick-win

**Problem statement:** Compute a health center's CY2026 UDS tables from patient-level records under the revised tables OMB approved on 3 September 2026 (ICR 202606-0915-002), find the mapping errors and implausible values that HRSA's review will flag, and benchmark each measure against the center's history and HRSA's public tables before the February 2027 submission.

**ML task:** Rules engine for table logic, LLM-assisted mapping of local codes, templates and free-text screening fields to the new lines (6A lines 9a, 20g, 26g and 35–42, and the 2026 eCQM value sets if the final manual adopts the alignment proposed in the December 2025 notice, FR 2025-22443; final manual not seen), and statistical anomaly detection on each table cell against peer and prior-year distributions
**Input data:** EHR extracts or FHIR bundles (patients, encounters, diagnoses, procedures, observations, screenings), patient support logs, staffing and cost files, the center's 2025 UDS submission, HRSA's public national and state UDS tables, the approved 2026 UDS tables, the 2026 UDS manual when published, and CMS's 2026 eCQM specifications
**Target:** Completed tables with each cell traceable to patient records; a ranked list of probable errors (unmapped codes, cross-table mismatches, cells outside the peer distribution) with the patients and fields behind each
**Evaluation metric:** On synthetic data with injected errors: recall of injected errors at a manageable review list (for example, the top 25 flags), and exact agreement with a hand-built reference on every table cell. In live use: the number of HRSA edit flags left unresolved at review, compared with the prior year.
**Scope:** The two-week MVP needs one engineer. Generate 20,000 Synthea patients (FHIR, Apache-2.0) with a health-center-like payer and income mix, compute Tables 3A, 4, 6A, 6B and 7 under the CY2026 changes, inject ten typical mapping errors, and flag them against HRSA's 2025 national and state distributions. A production version adds EHR connectors and the financial tables and takes 2–3 engineers about 4–6 months. HRSA put UDS+ patient-level submission on hold in April 2025 (search summary), so the UDS+ FHIR file is an optional export, not the goal.
**Data availability:** Synthea and HRSA's public UDS data are free. The approved 2026 tables are posted with OMB ICR 202606-0915-002; the proposed change list is in Federal Register notice 2025-22443, and the final 2026 manual was not seen. Real validation needs one or two partner centers, or an HCCN, under a BAA.

---

## 3. Medicaid Coverage-Loss Prediction at Renewal and Work Verification
#logistic-regression #gradient-boosting #survival-analysis #evaluation-metrics #revenue-impact

**Problem statement:** For each Medicaid patient, predict the probability of losing coverage at the next six-month renewal or work-requirement check from January 2027, and which kind of help (document collection, an exemption review or address correction) would most likely prevent it, so eligibility workers spend their hours where coverage is most at risk.

**ML task:** Calibrated binary classification of coverage loss by the next renewal date, with time-to-lapse survival modelling and a reason code per patient
**Input data:** Eligibility (270/271) responses and state renewal dates, address and phone change history, returned mail, prior gaps in coverage, age, eligibility group, documented conditions relevant to exemptions, employment information recorded at intake, visit frequency and language
**Target:** Coverage lost at or within 60 days of the renewal or verification date (yes/no); time to lapse; primary barrier class
**Evaluation metric:** Recall among patients who lose coverage, at the caseload the eligibility team can work each week, plus calibration. Recall matters more than precision: an unnecessary call costs minutes, while a missed lapse costs the patient's coverage and the center's PPS revenue.
**Scope:** 1–2 data scientists, 3–4 months, using the 2023–2024 unwinding as training history. Expect drift, because the 2027 rules differ by state and the first cycle has no labels. Start with a rules-plus-logistic baseline and retrain after the first renewal cycle.
**Data availability:** Eligibility responses and visit data are center-owned. Renewal outcomes appear in later eligibility checks. State-level unwinding data is public for benchmarking.

---

## 4. Medicaid Wraparound Underpayment and Payer-Change Detection
#gradient-boosting #change-point-detection #feature-engineering #evaluation-metrics #revenue-impact #automation

**Problem statement:** For every Medicaid managed care visit, compute the PPS amount due and compare it with plan payment plus wrap received. Then detect when a plan's payment behaviour changes, such as a new bundling rule, a lower behavioral rate or a dropped same-day visit, before months of underpayment accumulate.

**ML task:** Regression of expected plan payment per claim, residual-based underpayment scoring, and change-point detection on payment ratios by plan, code family and site
**Input data:** Claims and 835 remittances, the center's PPS rates and effective dates, state wrap rules and encounter definitions, wrap claims and state settlements, plan contracts, change-in-scope filings
**Target:** Underpaid amount per visit; the date and plan of each detected payment-pattern change; a year-end settlement estimate
**Evaluation metric:** Precision of underpayment flags confirmed on review (staff time is the constraint) and dollars recovered per flag. For change points, detection delay in weeks against changes later confirmed by the plan.
**Scope:** 1 data scientist and a reimbursement analyst, 3–4 months per state. The state encounter rules are the hard part, and they must be encoded with effective dates.
**Data availability:** Center-owned remittance and claims history, usually several years of it. State PPS rules are public in state plans and provider manuals.

---

## 5. Sliding-Fee Income Document Reading and Tier Proposal
#transformers #large-language-models #cnns #evaluation-metrics #compliance #automation

**Problem statement:** Read the income documents patients photograph or bring (pay stubs, tax returns, benefit letters, employer letters, self-declarations), extract household income and size, and propose the sliding-fee tier under the center's board-approved schedule, with the evidence attached and anything uncertain flagged.

**ML task:** Document classification, layout-aware key-value extraction and rule application, with confidence scores and a human review queue
**Input data:** Phone photos and scans of income documents in English and Spanish, intake answers, the center's sliding fee schedule and documentation policy, the current federal poverty guidelines
**Target:** Document type, pay period, gross income, annualised household income, household size, proposed tier and documentation expiry date
**Evaluation metric:** Field-level exact match on income and pay period; tier accuracy against staff determinations on a blinded sample; share of cases auto-proposed with no correction. Over-discounting and under-discounting both matter, because each is a site-visit finding.
**Scope:** 1–2 engineers, 2–3 months on a commercial document model plus center-specific rules. Pay stubs vary widely and many patients' income is cash, so the self-declaration path must stay first-class.
**Data availability:** Centers hold years of scanned documents, but most are unlabelled and contain PHI. A demo can use synthetic pay stubs.
