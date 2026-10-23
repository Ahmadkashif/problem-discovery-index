# Freight Load Matching Adapted to Patient Placement

**Niche:** [[niches/general-hospitals/case-management-post-acute-placement/profile|Case Management & Post-Acute Placement]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Freight brokers match loads to carriers using acceptance history, lane fit and response times; a patient discharge is a load with clinical constraints and a family's preferences.
**Tags:** #gradient-boosting #optimization-fundamentals #evaluation-metrics #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to get a medically ready patient accepted and authorised for the right post-acute bed on the day they are ready, and whoever removes the most avoidable days per case manager takes the account.

## The Problem
Placing a patient is a two-sided matching problem run by phone: the hospital has a patient with needs and a deadline, and facilities have beds, capabilities and preferences.

## What Already Exists
Freight brokerage platforms rank carriers by likelihood to accept, price and reliability, and automate tendering and follow-up. CarePort and Aidin digitise referral sending and responses.

## The Customization Gap
Healthcare adaptation needs:

- Patient-choice and anti-steering rules, so recommendations rank, never exclude, and record the family's selection.
- Clinical capability matching (dialysis, trach care, wound vac, behavioural support).
- Payer network and MA authorisation status as gating constraints.
- Quality data from CMS Care Compare shown alongside acceptance odds.
- HIPAA-compliant packet exchange.

## Target Customer
Case management leaders at systems already using a referral platform who want it to rank and chase, not just send.

## Impact If Solved
A referral network that learns from every send turns the case manager's phone list into a ranked, self-chasing queue. That cuts calls per placement by ~30–50% (estimate) and acceptance time by ~0.5–1 day for hard-to-place patients (estimate).
