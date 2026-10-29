# Round-Trip Trigger and Renewal Tracker for Every Repetitive Patient

**Niche:** [[niches/ambulance-services/rsnat-pcs-prior-authorization/profile|PCS & RSNAT Prior Authorization for Scheduled Transports]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nobody counts each Medicare patient's round trips against the fourth-trip trigger in real time, so prepayment review arrives as a surprise.
**Tags:** #large-language-models #logistic-regression #workflow-orchestration #compliance #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep each repetitive patient's Medicare transports paid without prepayment review, and whoever has the fewest RSNAT claim lines denied per 1,000 scheduled round trips takes the account.

## The Problem
A patient becomes "repetitive" from the transport pattern, not from a diagnosis. A new dialysis patient discharged from hospital may ride three times in a week before anyone flags them. Once the fourth round trip in 30 days passes without a request, claims go to prepayment review, where denials for missing documentation dominate.

## Why Nobody Has Built This
Scheduling sits in CAD, eligibility and PCS in the billing system, and the MAC decision in a letter. Billing firms see the claim after the transport, too late for the trigger. Prior-auth vendors sell to ordering clinicians, not ambulance suppliers.

## What to Build
A tracker fed by the schedule that counts each Medicare beneficiary's round trips on a rolling 30-day basis and opens a request when the pattern qualifies. It assembles the packet with the PCS and clinician notes, checks completeness, submits by esMD, records the affirmation number against each scheduled run, and warns 10 days before each 60-day or 40-trip window closes. A model trained on the operator's decision letters scores each packet's chance of affirmation before submission.

## Target Customer
Billing directors at independent operators with dialysis contracts, and ambulance billing firms serving them.

## Impact If Built
For an operator with 300 repetitive patients, catching every fourth-trip trigger and renewal on time would keep roughly 1,800 affirmation cycles a year (an estimate) out of prepayment review. That matters because 84% of FY2024 RSNAT prepayment denials were for documents never sent (CMS).
