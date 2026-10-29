# Coverage Finder for Every Self-Pay Run

**Niche:** [[niches/ambulance-services/face-sheet-insurance-discovery/profile|Face-Sheet Retrieval & Insurance Discovery]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An ambulance run with a name and a birth date but no insurance is worked by hand, when the receiving hospital usually registered the patient's coverage within the hour.
**Tags:** #gradient-boosting #k-nearest-neighbors #data-integration #automation #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to find billable coverage for patients carried with no insurance details, and whoever converts the highest share of transports opened as self-pay into paid insured claims takes the account.

## The Problem
For 911 transports the hospital face sheet is the best source of insurance, but it is requested per patient from each hospital's registration or health information department. Eligibility searches on partial demographics return no match or the wrong person. Medicaid coverage granted after the hospital stay, retroactive to the transport date, is missed if nobody checks again.

## Why Nobody Has Built This
Hospitals' registration systems are not built to send data to ambulance companies, and each hospital has its own process. Insurance discovery vendors sell to hospitals, whose self-pay balances are larger.

## What to Build
A coverage finder that fetches face sheets automatically from receiving hospitals through their interfaces, a health information exchange or a hospital data-exchange feed. It matches patients on fuzzy demographics with a confidence score, runs eligibility searches across likely payers ranked by a model of local payer mix and age, and re-checks Medicaid eligibility at 30, 60 and 90 days. The run moves from self-pay to insured as soon as coverage is confirmed.

## Target Customer
Ambulance billing firms and operators with large 911 volumes into many hospitals.

## Impact If Built
If 20% of 911 transports open as self-pay (an estimate) and the finder converts a quarter more of them into insured claims, an operator with 60,000 911 transports a year gains ~3,000 billable claims.
