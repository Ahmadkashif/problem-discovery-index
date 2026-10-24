# Pre-Bill Audit Scoring for Every Residential Day

**Niche:** [[niches/idd-group-homes/residential-habilitation-billing/profile|Residential Habilitation Billing & ISP Documentation]]
**Industry:** [[industries/idd-group-homes|IDD Group Homes]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agencies learn which billed days were unsupported only when an auditor samples them, months after the claim was paid.
**Tags:** #transformers #bert #gradient-boosting #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to make every billed residential day stand up to a state or Medicaid Fraud Control Unit audit, and whoever keeps the share of billed days recouped on audit lowest takes the account.

## The Problem
A residential claim is valid on its face: right code, right units, valid authorisation. Whether the day behind it is supported depends on the note, which a claim scrubber never reads. State quality reviews and fraud-control audits sample days, and unsupported days are recouped, in some states extrapolated across the sample (estimate). The agency's own compliance staff review a small sample by hand.

## Why Nobody Has Built This
Record-system vendors generate claims from attendance and leave documentation quality to the agency. Billing outsourcers check eligibility and codes. Each state's documentation standard is different, and the labelled data (which days auditors rejected) sits in agencies' compliance files as letters.

## What to Build
A scoring layer that reads every note and attendance record before billing. It retrieves the person's ISP outcomes, classifies which outcomes and strategies each note addresses, checks attendance and leave rules, and assigns each day a probability of audit failure with reason codes. Days above a threshold go back to the house manager with the fix needed. Monthly reports show outcome coverage per person and failure risk by house and DSP. The model is trained per state on the agency's own past review findings.

## Target Customer
Compliance directors and billing managers at agencies with 20+ homes, and the record-system vendors who could embed the score.

## Impact If Built
If an agency recoups ~1% of billed days today (estimate), halving that on ~73,000 resident-days a year at ~$300 a day (estimate) protects ~$110,000 a year. Note quality would also improve where auditors look first.
