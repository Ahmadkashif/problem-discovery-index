# An Incident-to Eligibility Check at Scheduling

**Niche:** [[niches/physician-practices/nps-pas-in-physician-offices/profile|Nurse Practitioners & Physician Assistants in Physician Offices]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether an NP or PA visit can bill at 100% is decided by facts known when the visit is booked (new problem or not, physician on site or not, payer rules), but practices find out at coding, when it is too late to change the schedule.
**Tags:** #decision-trees #logistic-regression #data-integration #compliance #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to bill each NP and PA visit under the right rule (incident-to under the physician or the clinician's own NPI), with the state's supervision or collaboration terms met, and whoever captures the most compliant revenue per advanced practice clinician takes the account.

## The Problem
Medicare incident-to requires an established patient and plan of care, no new problem addressed, and a supervising physician physically present in the suite. A visit that breaks any of these must bill under the NP's or PA's own NPI at 85%. Practices either bill incident-to wrongly, creating overpayment exposure, or bill everything at 85% and leave revenue behind. Commercial payers have their own rules.

## Why Nobody Has Built This
Schedulers do not know the rules, coders see the visit afterwards, and EHR templates do not ask. The data needed is in the schedule (who is on site), the chart (is this a new problem) and the payer table, and no product joins them.

## What to Build
A rules engine with a learned layer. At booking, it reads the reason for visit, the patient's plan of care, the payer and the physicians on site that session, and predicts whether the visit will qualify. After the visit, it checks the note for a new problem before the claim drops and routes the claim to the right NPI. The model learns from coder corrections.

## Target Customer
Primary care and specialty groups where NPs and PAs see 30% or more of visits.

## Impact If Built
Correctly billing the qualifying share of visits at 100% rather than 85% is worth ~$10,000–$20,000 a year per full-time NP or PA (estimate), while removing incident-to overpayment exposure.
