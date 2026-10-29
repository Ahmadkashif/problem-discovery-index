# Niche Analysis — Psychiatric Hospitals

**Parent Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]

## Niche Selection

A psychiatric hospital earns a per diem for each day a patient in crisis needs a locked bed, and it has to prove that need twice: to managed-care reviewers every one to three days, and to auditors and prosecutors afterwards. It also carries duties no other hospital has. It holds patients against their will on statutory clocks, it restrains and secludes under minute-by-minute federal rules, and its restraint and seclusion hours are published for every facility. The binding constraints are behavioral PHI (with 42 CFR Part 2 on detox units), staff safety, scrutiny of length of stay since 2024, and three clocks: the IPF-PAI (voluntary from 1 October 2027, mandatory from 1 July 2028), the 20% outlier cap for IPFs with 50 or more stays in cost reporting periods beginning on or after 1 October 2027, and the 2-point IPFQR penalty (Federal Register 2026-15588). The eight niches below split the industry by what vendors and hospital teams compete over. Market sizes are estimates of tooling, services and staff spend within each niche, not hospital revenue.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Continued-Stay Review & Medical-Necessity Defence | 🔵 High Market Share | ~$1.0B | Low-Medium | Director of utilization review / chief compliance officer |
| 2 | Health-System Joint Ventures & Hospital-Based Psychiatric Units | 🔵 High Market Share | ~$0.6B | Medium | Health-system chief strategy officer / JV board |
| 3 | Psychiatric Intake, ED Referrals & Medical Clearance | 🟠 Low Digitized | ~$0.4B | Low | Director of intake and admissions |
| 4 | Observation Rounds, Seclusion & Restraint Records | 🟠 Low Digitized | ~$2B | Low | Chief nursing officer |
| 5 | Inpatient Detox & Addiction Hospitals | 🟣 Underserved Audience | ~$0.3B | Low-Medium | Addiction medicine director |
| 6 | Child & Adolescent Inpatient Psychiatry | 🟣 Underserved Audience | ~$0.3B | Low | Medical director, child and adolescent services |
| 7 | IPFQR Reporting & IPF-PAI Submission | ⚡ Highly Automatable | ~$0.15B | Medium | Director of quality and performance improvement |
| 8 | Involuntary-Hold & Commitment Paperwork | ⚡ Highly Automatable | ~$0.2B | Low | Medical director / risk manager |

## Why These Niches

Continued-stay review takes the first market-share slot because every day of revenue depends on it and every serious investigation of the industry has turned on it: Acadia's $19.9M settlement in 2024 and the DOJ Criminal Division investigation it disclosed both concern admissions, length of stay and billing (10-K). Health-system joint ventures take the second, because that is where new beds are being built; Acadia opened five JV hospitals with health systems in 2025 alone. The two low-digitized niches run on fax machines and clipboards: referrals from emergency departments that must be medically cleared before a unit without a medical floor accepts them, and the 15-minute observation sheets and restraint logs behind the HBIPS hours CMS publishes. The two underserved audiences are patients the tools were not built for: people in medically managed withdrawal, whose records carry Part 2 and whose outcome happens after discharge, and children and adolescents, whose families and schools are part of every decision. The two automatable niches are the most rule-bound work in the building: CMS quality reporting, which gains a standardised assessment in October 2027, and the legal paperwork of involuntary holds.

## Niches

- [[niches/psychiatric-hospitals/continued-stay-utilization-review/profile|🔵 Continued-Stay Review & Medical-Necessity Defence]]
  - [[niches/psychiatric-hospitals/managed-care-concurrent-review/profile|🎯 Managed-Care Concurrent Review of Psychiatric Days]]
  - [[niches/psychiatric-hospitals/medicare-recertification-audit-defence/profile|🎯 Medicare Recertification, Active-Treatment Records & Audit Defence]]
- [[niches/psychiatric-hospitals/health-system-psychiatric-jvs/profile|🔵 Health-System Joint Ventures & Hospital-Based Psychiatric Units]]
- [[niches/psychiatric-hospitals/intake-ed-referrals-medical-clearance/profile|🟠 Psychiatric Intake, ED Referrals & Medical Clearance]]
- [[niches/psychiatric-hospitals/observation-seclusion-restraint/profile|🟠 Observation Rounds, Seclusion & Restraint Records]]
- [[niches/psychiatric-hospitals/inpatient-detox-addiction-hospitals/profile|🟣 Inpatient Detox & Addiction Hospitals]]
- [[niches/psychiatric-hospitals/child-adolescent-inpatient/profile|🟣 Child & Adolescent Inpatient Psychiatry]]
- [[niches/psychiatric-hospitals/ipfqr-ipf-pai-reporting/profile|⚡ IPFQR Reporting & IPF-PAI Submission]]
- [[niches/psychiatric-hospitals/involuntary-hold-commitment-paperwork/profile|⚡ Involuntary-Hold & Commitment Paperwork]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Continued-Stay Review & Medical-Necessity Defence** is not. Its sentence produced two contests with different winners. Managed-care concurrent review is won by the lowest share of reviewed days denied, argued by UR coordinators and attendings on the phone every one to three days, with UR software, outsourced UR firms and revenue cycle AI vendors competing to help. Medicare recertification and audit defence is won by the lowest share of audited paid days recouped, built by compliance teams, coding auditors and healthcare lawyers on the record an auditor reads a year later. Staff, vendors and failure mode (a denied day now against a recouped day and possible False Claims Act exposure later) differ. It decomposes into **Managed-Care Concurrent Review of Psychiatric Days**, which hosts the first half of the two-week MVP, and **Medicare Recertification, Active-Treatment Records & Audit Defence**. The payer's side of the first is [[niches/health-insurance-carriers/inpatient-post-acute-review/profile|🎯 Inpatient & Post-Acute Concurrent Review]], and the acute hospital's version is [[niches/general-hospitals/clinical-denials-status-appeals/profile|🎯 Clinical Denials & Inpatient Status Appeals]].

Three terminal calls were close. **Health-System Joint Ventures** could split into JV development and unit management. It stays one niche because both are judged by the partner system on the same outcome, how many of its psychiatric patients stay in its own beds. Distinct psychiatric units inside general hospitals are a boundary case, named here and kept on IPF-specific work. **Psychiatric Intake** overlaps the bed registries in Pass 2 pocket 10. The registry is the state's data product; the niche is the hospital's accept-or-decline contest, won on medical transfers back, not on how fast the phone is answered. **Observation, Seclusion & Restraint** could have been framed on self-harm injuries instead of restraint hours. Restraint and seclusion hours were chosen because they are published per facility, measured the same way everywhere and tied to the industry's tacit-knowledge problem; ligature risk sits in its Pass 2 pocket and ML entry 5. The win condition counts restraint and seclusion as one unit: HBIPS-2 hours plus HBIPS-3 hours per 1,000 patient hours, so a unit cannot win by trading one for the other.

Five candidates were considered and rejected. **ED boarding of psychiatric patients** is the general hospital's problem and a wait-time contest, which fails the filter as a win condition; its useful half is niche 3. **Psychiatric nurse and technician staffing** repeats [[niches/staffing-agencies/healthcare-travel-staffing/profile|🔵 Healthcare Travel & Per Diem Staffing]] and [[niches/general-hospitals/nurse-staffing-office/profile|🟠 Nurse Staffing Office & Contingent Labour]], with the same fill-rate contest; workplace violence is carried by worker-life 1 and [[niches/security-guard-firms/hospital-healthcare/profile|🟣 Hospital & Healthcare Security]]. **Behavioral EHR selection** (Netsmart, Qualifacts, Kipu) is the vendor contest at [[niches/healthcare-practice-software/behavioral-health-ehr/profile|🟠 Behavioral Health & SUD Practice Software]]. **Geriatric psychiatry units** were a close alternative to youth units; their dementia overlap sits with [[niches/skilled-nursing-facilities/long-stay-dementia-residents/profile|🟣 Long-Stay Residents Living with Dementia]]. **Privately run forensic units** serve state contracts with a single government buyer, so they stay in prose, as do state-run psychiatric hospitals. Telepsychiatry coverage of units and EDs belongs to [[niches/telehealth-platforms/the-contract-clinician/profile|🟣 The Contract Clinician]].

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. This pass sweeps seven positions in the value chain: aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry. It looks for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`. Pockets already profiled under other industries are linked in the prose below rather than profiled again.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Behavioral Hospital Chain Corporate Analytics | Aggregator/rollup | 20-60 | 31 | ⚠️ Kill switch |
| 10 | Psychiatric Bed Registries & Bed-Placement Platforms | Data vendor | 10-30 | 27 | ⚠️ Kill switch |
| 11 | Patient Observation & Virtual Sitting Vendors | Supplier | 10-30 | 27 | ⚠️ Kill switch |
| 12 | IPF PPS & Behavioral Payment Policy Consultancies | Specialist advisory | <10 on IPF | — | Fails gate |
| 13 | De-escalation & Restraint-Reduction Training Providers | Supplier | <10 research and evaluation | — | Fails gate |
| 14 | Outsourced Behavioral Utilization Review & RCM Services | Specialist advisory | production only | — | Fails gate |
| 15 | IPFQR & ORYX Measure Abstraction Vendors | Supplier | <10 non-production | — | Fails gate |
| 16 | Behavioral Environment-of-Care & Ligature-Risk Consultancies | Specialist advisory | <10 | — | Fails gate |
| 17 | Behavioral Health Facility Liability Underwriting | Payer & intermediary | <10 per carrier | — | Fails gate |
| 18 | Behavioral Health Patient Safety Organizations | Association | <10 | — | Fails gate |
| 19 | Psychiatric Hospital Association Survey (NABH) | Association | <10 | — | Fails gate |

## Why These Pockets

No pocket qualifies, and the hospitals themselves fail the gate. Their analysts produce UR packets, quality submissions and board dashboards that are spent on payment and compliance, never invoiced, and every record is behavioral PHI, with Part 2 on top for detox. The chains above them (31) hold the largest psychiatric inpatient corpus outside the payers and fail on both counts. The vendors who touch that data for a fee meet the same wall: state-contract bed registries (27) hold hospitals' bed and referral records as client data, and observation vendors (27) hold patient video under business associate agreements. Those three are the only pockets that clear the gate. Everything else fails it. Per-case UR staff, abstractors and curriculum writers are production. The policy consultancies' IPF work is done by a few analysts inside firm-wide Medicare teams. And no ligature consultancy, behavioral PSO, liability carrier or association has 10 analysts on psychiatric hospitals.

Much of this industry's insight layer is already in the vault and scores the same way:

- Payers and criteria: [[niches/behavioral-health-clinics/behavioral-managed-care-policy/profile|🔍 Behavioral Managed Care Clinical Policy Units]] (46, kill switch), [[niches/behavioral-health-clinics/level-of-care-criteria-publishers/profile|🔍 Level-of-Care Criteria Publishers]] (42), [[niches/behavioral-health-clinics/parity-compliance-analysis/profile|🔍 Mental Health Parity Compliance Analysis]] (45, kill switch) and [[niches/health-insurance-carriers/independent-review-organizations/profile|🔍 Independent Review Organizations]] (fails gate). Stage E caveat: the criteria publishers' Q4 4 rests on their own edition cycle, which the current clock ruling scores 2 (~38).
- Hospital-side review and revenue: [[niches/general-hospitals/physician-advisor-utilization-review/profile|🔍 Physician Advisor & Utilization Review Services]] (44, kill switch, with Q4 capped at 3 because its 24–72-hour windows bind single reviews), [[niches/general-hospitals/hospital-reimbursement-consultancies/profile|🔍 Hospital Reimbursement & Cost Report Consultancies]] (48, kill switch) and [[niches/medical-billing/denial-management-analytics-vendors/profile|🔍 Denial Management Analytics Vendors]] (48, kill switch; Stage E caveat: its Q4 5 rests on per-claim deadlines, which the current clock ruling caps at 3, ~44). Prior authorization at the ordering practice is [[niches/physician-practices/ordering-practice-prior-authorization/profile|⚡ Prior Authorization at the Ordering Practice]]. The shared revenue cycle vendors hiring engineers (AKASA, Candid Health, Trellis AI) belong to that field.
- Quality and safety: [[niches/general-hospitals/cms-quality-measure-contractors/profile|🔍 CMS Hospital Quality Measure Contractors]] (34, kill switch), [[niches/general-hospitals/hospital-quality-ratings-publishers/profile|🔍 Hospital Quality Ratings Publishers]] (33), [[niches/general-hospitals/hcahps-patient-experience-vendors/profile|🔍 Hospital Patient Experience Survey Vendors (HCAHPS)]] (45, kill switch), [[niches/behavioral-health-clinics/behavioral-accreditation-bodies/profile|🔍 Behavioral Health Accreditation Bodies]] (44) and [[niches/general-hospitals/hospital-malpractice-claims-benchmarking/profile|🔍 Hospital Malpractice Claims Benchmarking]] (40, kill switch).
- Software, staffing and research: [[niches/behavioral-health-clinics/behavioral-ehr-content-teams/profile|🔍 Behavioral Health EHR Clinical Content Teams]] (35, kill switch), [[niches/behavioral-health-clinics/behavioral-mso-analytics/profile|🔍 Behavioral Health MSO Analytics]] (38, verdict logged as below threshold), [[niches/behavioral-health-clinics/credentialing-verification-orgs/profile|🔍 Credentialing Verification Organizations]] (42), [[niches/it-staffing-firms/contingent-workforce-msp-vms/profile|🔍 Contingent Workforce MSP & VMS Programmes]] (55, indexed) for travel psychiatric nurses, and [[niches/behavioral-health-clinics/psychiatric-endpoint-quality-vendors/profile|🔍 Psychiatric Trial Endpoint Quality Vendors]] (56, kill switch), whose acute-schizophrenia trials often enrol inpatients (recalled); Stage E caveat: its switch rests on computer-system validation, which is not a switch type, and the real candidate switch is sponsors' trial data. The one behavioral pocket in the scorecard index is [[niches/behavioral-health-clinics/psychological-assessment-publishers/profile|🔍 Psychological Assessment Publishers]] (50, indexed; ~48 under Stage E, logged 2026-10-25), whose norms sit one step back from the patient.

Regulators were swept and kept in prose. CMS, state survey agencies, state mental health authorities and the DOJ and OIG are government bodies, and NRI's state hospital data serves state agencies only. The FY2027 rule shapes three of the pockets without lifting any of them. Its outlier cap, which applies only to IPFs with 50 or more stays and only to discharges in cost reporting periods beginning on or after 1 October 2027, is expected to touch about 0.8% of providers in a typical year (Federal Register 2026-15588), so it creates advisory work but little volume. The IPF-PAI adds abstraction and submission work for vendors whose staff are production. The chains' 10-K and 10-Q dates set their only outside clock, which caps them at Q4 3.

No clean pocket clears the gate here. The nearest clean pocket is already profiled: [[niches/health-insurance-carriers/medicare-health-policy-advisory/profile|🔍 Medicare & Health Policy Advisory Firms]] (46, below threshold), whose firm-wide teams also read the IPF rules, alongside [[niches/general-hospitals/hospital-reimbursement-consultancies/profile|🔍 Hospital Reimbursement & Cost Report Consultancies]] (48, kill switch) for facility cost-report work. Counted as an IPF pocket, the same firms have only a few analysts on psychiatric payment, so pocket 12 fails the gate rather than scoring on the firm-wide count. For placement, the lesson matches the hub: the buyers worth approaching are the revenue cycle vendors hiring engineers to sell into hospitals, not the hospitals or the pockets above them.

## Niches — Pass 2
- [[niches/psychiatric-hospitals/behavioral-chain-corporate-analytics/profile|🔍 Behavioral Hospital Chain Corporate Analytics]]
- [[niches/psychiatric-hospitals/psychiatric-bed-registry-platforms/profile|🔍 Psychiatric Bed Registries & Bed-Placement Platforms]]
- [[niches/psychiatric-hospitals/patient-observation-virtual-sitting-vendors/profile|🔍 Patient Observation & Virtual Sitting Vendors]]
- [[niches/psychiatric-hospitals/ipf-payment-policy-consultancies/profile|🔍 IPF PPS & Behavioral Payment Policy Consultancies]]
- [[niches/psychiatric-hospitals/de-escalation-restraint-reduction-training/profile|🔍 De-escalation & Restraint-Reduction Training Providers]]
- [[niches/psychiatric-hospitals/outsourced-behavioral-ur-services/profile|🔍 Outsourced Behavioral Utilization Review & RCM Services]]
- [[niches/psychiatric-hospitals/ipfqr-abstraction-vendors/profile|🔍 IPFQR & ORYX Measure Abstraction Vendors]]
- [[niches/psychiatric-hospitals/ligature-risk-environment-consultancies/profile|🔍 Behavioral Environment-of-Care & Ligature-Risk Consultancies]]
- [[niches/psychiatric-hospitals/behavioral-facility-liability-underwriting/profile|🔍 Behavioral Health Facility Liability Underwriting]]
- [[niches/psychiatric-hospitals/behavioral-patient-safety-organizations/profile|🔍 Behavioral Health Patient Safety Organizations]]
- [[niches/psychiatric-hospitals/psychiatric-hospital-association-survey/profile|🔍 Psychiatric Hospital Association Survey (NABH)]]
