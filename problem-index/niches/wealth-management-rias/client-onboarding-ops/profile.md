# Client Onboarding & Account Operations

**Parent Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1.5-2.5B services market
**Share of Parent Industry:** Embedded operational cost (~1-3% of RIA revenue goes to onboarding and account operations)
**Digital Adoption:** Low-Medium — custodian portals (Schwab Advisor Center, Fidelity WealthCentral) are the primary interface, but the process of opening accounts, transferring assets, and maintaining account records remains heavily manual and paper-driven
**Target Buyer:** Operations manager or client service associate at an RIA handling new account setup and custodian interactions
**Automation Potential:** High — account opening follows standardized custodial forms with defined fields, and asset transfers follow ACAT/non-ACAT protocols with trackable status codes

## What Makes This a Distinct Niche
Client onboarding at an RIA involves 15-30 discrete steps: collecting client information, running anti-money laundering (AML) checks, preparing custodial account applications (which differ by custodian and account type), obtaining wet or electronic signatures, submitting ACAT transfer requests, tracking transfer status, setting up billing, configuring portfolio models, and establishing the client in CRM, planning, and reporting systems. Each step requires data entry into a different system. A single new client household with 4 accounts (joint taxable, two IRAs, a trust) generates 60-100 individual form fields and tasks across 3-5 platforms. Operations staff at multi-advisor RIAs spend 40-60% of their time on onboarding and account maintenance.

## Current Tools & Gaps
Custodian portals handle account applications, but each custodian has a different interface and workflow. PreciseFP and Knudge collect client information electronically. DocuSign handles signatures. None of these tools orchestrate the full workflow — the operations manager maintains a spreadsheet tracking which forms have been submitted, which accounts are pending, and which transfers are in flight.

## Problems
- [[niches/wealth-management-rias/client-onboarding-ops/build|🔨 Build: End-to-End Client Onboarding Orchestrator]]
- [[niches/wealth-management-rias/client-onboarding-ops/buy|🛒 Buy: Multi-Custodian Account Application Unifier]]
- [[niches/wealth-management-rias/client-onboarding-ops/fix|🔧 Fix: ACAT Transfer Tracking and Exception Resolution]]
