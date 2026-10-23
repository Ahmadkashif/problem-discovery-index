# Estimates That Disagree With the Hospital's Own Price File

**Niche:** [[niches/general-hospitals/patient-access-auth-estimates/profile|Patient Access: Prior Authorization, Eligibility & Estimates]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** The estimate a patient receives at scheduling, the machine-readable file the hospital publishes and the amount the payer allows are computed by three different systems, and they rarely agree.
**Tags:** #descriptive-statistics #data-integration #compliance #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get every scheduled service verified, authorised and priced before the patient arrives, and whoever clears the most scheduled cases with no human touch and no downstream authorisation denial takes the account.

## The Problem
Since 1 April 2026, CMS enforces hospital price files that carry median and 10th/90th percentile allowed amounts from the hospital's own remittances, with an attestation naming a senior official (CMS-1834-FC). Patient estimates come from a separate estimator using contract tables. When the two differ, the hospital has published one number and quoted another.

## Why It's Still Broken
The price file is owned by compliance or finance and built once a year, often by a vendor. The estimator is owned by patient access, and contract terms are maintained in a third module. Nobody reconciles them.

## What a Fix Looks Like
One source of truth for expected allowed amounts by payer and service, built from remittances and contract terms, that feeds both the price file and the estimator. A monthly variance report flags services where the quote and the published file diverge.

## Who Feels the Pain
Compliance officers who now sign attestations; patient access staff explaining a bill to an angry patient; CFOs exposed to complaints and penalties.

## Impact If Fixed
Consistent numbers reduce compliance risk under a rule CMS has enforced since 1 April 2026 (CMS-1834-FC). They also cut billing complaints about surprise balances by ~20–30% (estimate).
