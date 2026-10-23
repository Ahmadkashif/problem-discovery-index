# Authorisation-Lapse Prediction and Packet Assembly

**Niche:** [[niches/assisted-living-communities/medicaid-waiver-billing/profile|Medicaid Waiver Billing & Level-of-Care Reassessments]]
**Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Waiver authorisations lapse quietly, and the community finds out when the claim is denied.
**Tags:** #large-language-models #gradient-boosting #survival-analysis #workflow-orchestration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep each waiver resident's authorisation current and the month's claim paid on first submission, and whoever files every reassessment and reauthorisation before it lapses takes the account.

## The Problem
A reassessment depends on the state assessor's or care manager's schedule, a physician form, an updated service plan and sometimes a financial redetermination. Any piece can stall, and the business office learns of it when a claim comes back.

## Why Nobody Has Built This
Every state and every managed care plan has its own forms, portals and timelines, and the volume per community is small. EHRs track the resident, not the authorisation's critical path.

## What to Build
A tracker that reads each resident's authorisation, service plan and assessment documents, builds the timeline to the next lapse, and predicts which ones are at risk from the history of each plan and care manager. It assembles the reassessment packet with an LLM: current service plan, physician form, recent care notes and incidents. It nudges the right person 60, 30 and 10 days out, and checks each month's claim against the authorisation before submission.

## Target Customer
Business office managers and revenue cycle directors at operators with ~10%+ waiver residents; billing outsourcers.

## Impact If Built
If a community with 20 waiver residents loses ~1–2 resident-months of payment a year to lapses (estimate), at ~$2,000–3,000 a month for services (estimate) prevention recovers ~$2,000–6,000 per community a year, more at Medicaid-heavy operators.
