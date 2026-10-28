# Every Prescription Tested, Not a Sample

**Niche:** [[niches/community-health-centers/340b-duplicate-discount-audit/profile|Medicaid Duplicate-Discount Prevention & HRSA 340B Audit]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A health center's 340B self-audit checks 50 prescriptions a quarter, while HRSA's auditor can pick any of the tens of thousands it dispensed.
**Tags:** #gradient-boosting #feature-engineering #descriptive-statistics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to keep every 340B purchase defensible against diversion and Medicaid duplicate-discount findings, and whoever has the fewest adverse findings per HRSA 340B audit takes the account.

## The Problem
Sampling finds systematic errors late. A single mis-set contract pharmacy or a plan that changed its carve-in status can generate months of duplicate discounts before a sample catches it.

## Why Nobody Has Built This
Testing every prescription needs the chart (patient relationship, prescriber, site), the administrator's eligibility decision, the pharmacy claim and the Medicaid status joined together. They sit in four systems.

## What to Build
A continuous test of every 340B prescription against the patient definition, provider and site eligibility, the Exclusion File and each plan's carve status. Anomaly scoring ranks pharmacies and prescribers by error rate, and an evidence pack is built for any prescription an auditor might pick.

## Target Customer
Compliance officers at centers with 10+ contract pharmacies or an upcoming HRSA audit.

## Impact If Built
Catching a mis-set pharmacy three months earlier avoids repaying, at ~$300 of savings a prescription (estimate), $90,000 on 300 prescriptions.
