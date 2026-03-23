# Pre-Collection Medical Debt Verification Engine

**Niche:** [[niches/collections-agencies/medical-debt-collectors/profile|Medical Debt Collectors]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automates the pre-collection verification workflow for medical debt — insurance eligibility check, charity care screening, itemized statement reconciliation, and No Surprises Act compliance — before an agent makes the first call.
**Tags:** #workflow-orchestration #automation #compliance #data-integration #revenue-impact

## The Problem
When a medical debt placement arrives, the agency must verify that insurance was properly exhausted, that the patient does not qualify for charity care, that the balance matches the itemized statement, and that the debt complies with the No Surprises Act (for out-of-network emergency services). These verification steps require accessing 3-4 separate systems (clearinghouse for insurance, provider portal for itemized statements, income estimation for charity care, state surprise billing registry) and take 15-30 minutes per account. Skipping verification risks collecting on debts that should be written off — exposing the agency to regulatory action and client termination.

## Why Nobody Has Built This
Medical debt verification sits at the intersection of healthcare billing (clearinghouse integration, CPT/ICD code validation) and collections (account management, compliance tracking) — two domains with separate technology ecosystems and vendor relationships. Building the verification engine requires healthcare billing expertise, collections platform integration, and real-time clearinghouse API access — a combination that neither healthcare IT vendors nor collections tech vendors have pursued because it crosses their domain boundaries.

## What to Build
An automated pre-collection verification pipeline that runs on every new medical debt placement: (1) checks insurance eligibility through clearinghouse APIs, (2) flags potential charity care eligibility based on debtor income estimation, (3) reconciles the placed balance against the itemized statement, (4) checks No Surprises Act applicability based on procedure codes and provider network status, and (5) outputs a verification status (clear to collect, pending verification, do not collect) with supporting documentation. Only accounts marked "clear to collect" enter the agent work queue.

## Target Customer
Medical debt collection agencies processing 5,000+ new placements per month who currently dedicate 2-3 FTEs entirely to pre-collection verification.

## Impact If Built
Automates 80% of pre-collection verification, recovering 2-3 FTEs worth of capacity ($80K-$120K annually). Reduces regulatory exposure from collecting on ineligible debts. Increases collection efficiency by ensuring agents work only on verified, collectible accounts.
