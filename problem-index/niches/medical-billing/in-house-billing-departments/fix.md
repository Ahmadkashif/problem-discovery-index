# Aged AR Recovery for Practices Without Billing Expertise

**Niche:** [[niches/medical-billing/in-house-billing-departments/profile|In-House Billing Departments]]
**Industry:** [[industries/medical-billing|Medical Billing]]
**Type:** Fix (Pain Point)
**One-liner:** Practices with in-house billing accumulate AR over 90 days at 2-3x the rate of outsourced billing operations because denied claims go unworked — an automated aged AR recovery workflow would surface and resolve the $30,000-80,000 in recoverable revenue sitting uncollected in a typical small practice's aging report.
**Tags:** #logistic-regression #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact #worker-facing #automation

## The Problem
In a practice with in-house billing, the billing staff processes new claims daily but rarely circles back to work aged accounts receivable. The reasons are structural: (1) New claims feel more urgent because there's a timely filing deadline (typically 90-365 days depending on payer). (2) Aged claims are harder to work because the staff doesn't remember the case, the patient may have changed insurance, and the payer may have closed the claim window. (3) Nobody has trained the staff on how to prioritize aged AR — which claims are still recoverable and which should be written off? (4) The practice manager reviews the AR aging report monthly, sees $120,000 over 90 days, feels overwhelmed, and focuses on something more tractable. The result: recoverable revenue sits in the aging report until it passes the filing deadline and becomes permanently unrecoverable. Professional billing companies maintain AR over 90 days at 5-8% of total AR; in-house billing departments average 15-25%.

## Why It's Still Broken
PM systems generate aging reports sorted by dollar amount or patient name, not by recovery probability. A $500 claim at 95 days with a correctable coding error (high recovery probability) gets the same visual weight as a $500 claim at 180 days with a timely filing deadline that passed (zero recovery probability). Without prioritization, staff either work the list top-to-bottom (inefficient) or cherry-pick the largest balances (may not be the most recoverable). No PM system provides recovery guidance — the aging report says "$500 outstanding, 95 days" but doesn't say "this claim was denied CO-16, the missing field is the referring physician NPI, here's how to correct and resubmit."

## What a Fix Looks Like
An aged AR recovery module that connects to the practice's PM and generates a prioritized action queue: (1) Recovery scoring — a logistic regression model predicting recovery probability for each aged claim based on payer, denial reason (if denied), claim age, remaining filing deadline, claim value, and historical recovery rates for similar claims at this practice. (2) Prioritized worklist — ranks aged claims by expected recovery value (probability × amount), so staff work the highest-value items first. (3) Recovery actions — for each claim, provides the specific next step: "Resubmit with corrected modifier" or "Call Aetna at [number] to request reconsideration, reference claim #[X]" or "Write off — timely filing deadline passed on [date]." (4) Auto-write-off recommendations — identifies claims that are definitively unrecoverable (filing deadline passed, provider not credentialed with payer at time of service, patient has no active coverage) and recommends write-off with documentation for the practice's records.

## Who Feels the Pain
The practice manager who sees a growing AR aging report but doesn't know which claims are recoverable or how to recover them, and the billing staff who avoid the aging report because working aged claims feels futile without guidance.

## Impact If Fixed
Recovers 30-50% of the aged AR that in-house billing departments currently write off by default. For a practice with $80,000 in AR over 90 days, recovering 40% captures $32,000 — often in a single focused campaign. Ongoing, maintaining AR over 90 days at 10% instead of 20% improves cash flow by $40,000-60,000/year for a typical 3-physician practice. Staff report reduced anxiety about the aging report when they have clear, prioritized actions instead of an overwhelming, undifferentiated list.
