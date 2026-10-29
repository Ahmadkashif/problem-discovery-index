# Air Disputes Lost to Ineligibility Before Anyone Reads the Offer

**Niche:** [[niches/ambulance-services/air-medical-out-of-network-payment/profile|Air Medical Transport & Out-of-Network Payment]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** Nearly half of air ambulance disputes are challenged as ineligible, usually over a missed window, a state-law plan or a wrong batch, and each one found ineligible costs fees and months before it is thrown out.
**Tags:** #logistic-regression #workflow-orchestration #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get paid for flights flown to patients whose health plans do not contract with the operator, and whoever collects the most per out-of-network transport after independent dispute resolution takes the account.

## The Problem
In Q2 2025, plans challenged 47% of air ambulance disputes as ineligible, against 39% across all services, and 2,184 of the 14,972 air disputes closed that quarter were closed as ineligible (CMS supplemental tables). Common causes are initiating before open negotiation has run 30 business days or after the 4-business-day window, disputing a claim governed by a state process rather than the federal one, and batching flights that cannot be batched.

## Why It's Still Broken
Eligibility depends on facts the revenue team does not hold in one place: plan type (self-funded or fully insured), the state of the plan, the dates of the initial payment and remittance, and the open-negotiation notice. These sit across the billing system, payer correspondence and email, and the person filing works from a checklist.

## What a Fix Looks Like
An eligibility screen run on each flight before filing. It determines plan type and governing law from the eligibility response and plan documents, computes each statutory window from the remittance date, checks batching rules, and blocks filings that will fail. A model trained on the operator's past ineligibility findings ranks the borderline ones for a human check.

## Who Feels the Pain
Revenue-cycle staff at air operators, who see months of work dismissed; chief financial officers, who pay fees on disputes that never reach a decision; and patients' plans, which spend time contesting filings that should not exist.

## Impact If Fixed
Halving ineligible closures from the Q2 2025 level of 2,184 would avoid ~1,100 dismissed air disputes a quarter, with their administrative fees and the months each one sits open.
