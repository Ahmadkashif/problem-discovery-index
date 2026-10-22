# Lapse Prediction Before the Eligibility Run

**Niche:** [[niches/self-insured-benefit-pools/hour-bank-eligibility/profile|Hour-Bank Eligibility & Self-Pay at Health and Welfare Funds]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Members learn their coverage lapsed when a claim is denied; the fund office could see most lapses coming from late or short employer reports.
**Tags:** #gradient-boosting #logistic-regression #change-point-detection #feature-engineering #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to decide every member's coverage for next month from hours reported late and by hand, and whoever pays the fewest claims for people who were not eligible while cutting off nobody who was takes the account.

## The Problem
Each month the eligibility run terminates members whose hours and bank fall short. Many are short only because an employer reported late or partially. The fund sends a notice after the fact, the member finds out at a provider, and staff spend days reinstating coverage once the report arrives.

## Why Nobody Has Built This
Fund administration systems post what arrives and run rules; they do not model what should have arrived. TPAs bill per member or per transaction and are not paid to prevent calls.

## What to Build
A model of each employer's expected remittance (timing, members, hours) from its own history, flagging late, missing or short reports days before the eligibility cutoff. Each at-risk member is linked to the employer whose report would restore coverage, with drafted outreach to the employer's bookkeeper and a pre-lapse notice to the member explaining self-pay options.

## Target Customer
Fund administrators and TPAs of construction, trucking, hospitality and entertainment health funds.

## Impact If Built
Fewer wrongful lapses, fewer denied prescriptions and far fewer reinstatement calls in the first week of each month.
