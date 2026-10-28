# Medicaid Wraparound Payments Reconciled by Spreadsheet

**Industry:** [[community-health-centers|Community Health Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic revenue cycle software posts what a Medicaid managed care plan paid, but a health center is owed its full PPS rate per qualifying visit, and the gap is tracked by a reimbursement manager in a spreadsheet that the state settles months later.
**Tags:** #gradient-boosting #feature-engineering #descriptive-statistics #change-point-detection #data-integration #revenue-impact #automation

## The Problem
Federal law entitles a health center to its Medicaid prospective payment system (PPS) rate, a per-visit amount set from the center's own historic costs and inflated each year (Social Security Act §1902(bb), recalled). Medicaid was 45.8% of health center revenue in 2025, $25.4B (UDS via KFF). Most Medicaid patients are now in managed care, and the plan pays its own negotiated rate. Where that is less than the PPS rate, the state owes the difference as a wraparound payment, paid per claim, monthly or through an annual reconciliation, depending on the state.

The reimbursement manager has to know, for every Medicaid managed care visit, whether it qualifies as a billable PPS encounter, the rate that applies on that date, what the plan paid, what wrap was claimed and received, and what the state will settle. Same-day medical and behavioral visits, dental, and services by staff who do not count as billable providers all follow state-specific rules. A change in the center's services, such as adding dental or behavioral health, entitles it to a change-in-scope rate adjustment. States set thresholds and filing windows: 3% and 90 days after fiscal year end in Colorado, 4% and 60 days in Nevada (search summary). Requests that are not filed are revenue lost.

## What Already Exists
Every health center EHR has a practice management and billing module (NextGen, eClinicalWorks, athenaOne, OCHIN Epic), and revenue cycle vendors and outsourcers work denials and posting. Medicaid managed care plans issue remittances, and some states run wrap claims through their MMIS. Consultancies prepare the annual Medicare cost report and change-in-scope applications. The general claims-analytics layer is profiled at [[niches/healthcare-practice-software/ambulatory-rcm-modules/profile|🔵 Ambulatory Revenue Cycle Modules]], and denial vendors at [[niches/medical-billing/denial-management-analytics-vendors/profile|🔍 Denial Management Analytics Vendors]].

## The Customisation Gap
The health center layer is a PPS-due ledger:

- each visit classified as a PPS encounter or not under the state's definition, with the rate in force that day;
- plan payment, wrap claimed, wrap received and the outstanding balance, by plan and month;
- alerts when a plan changes its payment pattern, such as a new code bundling rule or a lower rate on behavioral visits, which shows up first as a step change in remittances;
- a running estimate of the year-end settlement and of change-in-scope eligibility whenever service mix shifts.

The urgency rises for CY2026, because HRSA removes the wraparound and reconciliation columns from UDS Table 9D (the OMB-approved 2026 UDS tables (ICR 202606-0915-002, approved 3 September 2026)). The center will no longer report the figure, so it must track it for itself.

## Impact If Solved
If wrap shortfalls run at ~1–3% of Medicaid revenue (estimate), a center with $20M of Medicaid revenue recovers $200,000–$600,000 a year. The reimbursement manager also gets back ~2 days a month of spreadsheet reconciliation (estimate).
