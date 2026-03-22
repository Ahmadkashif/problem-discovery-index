# Real-Time 340B Split Billing and Compliance Audit Platform

**Niche:** [[niches/pharmacy-independents/340b-contract-pharmacy/profile|340B Contract Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform that determines 340B eligibility at point of sale — not retrospectively — showing the pharmacist immediately whether a prescription qualifies for 340B pricing and generating audit-ready documentation for every claim in real time.
**Tags:** #logistic-regression #gradient-boosting #feature-engineering #evaluation-metrics #compliance #data-integration #revenue-impact

## The Problem
340B contract pharmacies currently operate in a "dispense first, determine eligibility later" model. The pharmacy fills the prescription using regular wholesale inventory, submits the claim to the PBM, and days or weeks later the TPA retrospectively identifies which claims qualified for 340B pricing and processes virtual inventory replenishment. This creates three problems: (1) the pharmacy has no point-of-sale visibility into whether a prescription is 340B-eligible, preventing real-time margin optimization, (2) retrospective eligibility determination means errors compound for weeks before discovery, and (3) audit documentation is assembled after the fact rather than generated contemporaneously — the weakest possible audit posture. When HRSA audits a contract pharmacy arrangement, they require proof that each 340B claim was for a patient of the covered entity with a prescription from an associated provider. Pharmacies relying on TPA retrospective models often cannot produce this documentation claim-by-claim.

## Why Nobody Has Built This
Real-time 340B eligibility determination requires access to the covered entity's patient registry (which entity controls and shares selectively), the provider roster (which changes as locums and new hires rotate), and the entity's qualifying outpatient drug list. These data sources sit in different systems (the entity's EHR, the entity's HRSA registration, the TPA's platform) and are not designed for real-time API access. Additionally, manufacturer restrictions on 340B contract pharmacy arrangements (imposed by companies like Eli Lilly, AstraZeneca, Novartis since 2020) add another layer of complexity — certain drugs are excluded from 340B contract pharmacy dispensing by specific manufacturers, and the list changes frequently. Building a real-time eligibility engine requires aggregating and continuously updating these data sources — a significant integration challenge that TPAs have not prioritized because their retrospective model is simpler and generates sufficient revenue.

## What to Build
A cloud platform that integrates with: (1) the covered entity's patient registry via EHR API or secure data feed, (2) the PMS adjudication workflow to intercept claims at point of sale, (3) manufacturer restriction databases updated in real time, and (4) HRSA's covered entity and provider databases. At the moment of adjudication, the system determines: Is this patient registered with the covered entity? Was this prescription written by an associated provider? Is this NDC eligible under the contract (not manufacturer-restricted)? If all criteria are met, the system flags the claim as 340B-eligible, routes it through 340B purchasing, and generates a timestamped audit record documenting the eligibility basis. A logistic regression model trained on historical audit outcomes scores each claim's audit risk, flagging edge cases (patient registered but not seen recently, provider on the roster but not yet credentialed) for pharmacist review.

## Target Customer
Independent pharmacies with 340B contract pharmacy arrangements generating $100,000+ in annual 340B savings, and FQHC pharmacy directors managing multiple contract pharmacy relationships who need centralized compliance visibility.

## Impact If Built
Shifts 340B eligibility determination from retrospective to real-time, increasing 340B capture rates by 10-20% (an additional $10,000-50,000/year in savings per pharmacy). Generates contemporaneous audit documentation that reduces HRSA audit risk from high to low — critical given that adverse audit findings can result in repayment demands exceeding $500,000 and program termination.
