# Number Porting, SIM Changes & Account Takeover Defence

**Parent Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to approve every legitimate port-out, eSIM transfer and SIM change in seconds while stopping the takeover attempts hidden among them, and whoever delivers the lowest fraud at the least customer friction takes the account-security budget.

## Profile
**Market Size:** ~$800M a year in identity verification, fraud decisioning, authentication and care time spent on SIM and port requests across carriers (estimate)
**Share of Parent Industry:** under 1% of carrier revenue (estimate)
**Digital Adoption:** High — every request is a digital event; decisions are still rules plus care agents' discretion
**Target Buyer:** VP Fraud & Identity / Chief Information Security Officer
**Automation Potential:** Very high — decisions are high-volume, repeatable and labelled by later fraud outcomes

## What Makes This a Distinct Niche
A phone number is the recovery key for bank, email and crypto accounts, so taking it over through a fraudulent SIM swap or port-out is a standard attack. Customers also legitimately change SIMs and carriers millions of times a year, and eSIM makes a change a software event that can complete in seconds. The FCC's November 2023 SIM-swap and port-out order (WC Docket 21-341) requires carriers to authenticate customers before a SIM change or port-out and to notify them immediately, but a July 2024 bureau order (DA 24-649) deferred compliance with all of its rules until OMB approval and a Federal Register compliance-date notice, and no such notice had appeared by October 2026. The work is a high-volume, adversarial, labelled decision, the most automatable in the carrier. This niche is the account holder's side: deciding whether a number or SIM may leave. Getting a ported line working at a dealer counter is [[niches/wireless-retail-agents/activation-and-port-in-processing/profile|⚡ Activation & Port-In Processing]] under wireless retail agents, and an MVNO's port orders are [[niches/telecom-resellers/number-porting-provisioning/profile|🟠 Number Porting & Provisioning Desk]] under telecom resellers.

## Current Tools & Gaps
Port-out PINs and account passcodes, carrier authentication apps, identity vendors (Prove, Socure, the credit bureaus), bank-grade fraud platforms, and care scripts. The gaps: risk scored per channel rather than across the account's recent history; care agents able to override controls under social engineering; and fraud outcomes not fed back to decisions.

## Problems
- [[niches/wireless-carriers/porting-sim-account-security/build|🔨 Build: Cross-Channel Takeover Risk for Every SIM and Port Request]]
- [[niches/wireless-carriers/porting-sim-account-security/buy|🛒 Buy: Payment-Fraud Decisioning Applied to SIM Changes]]
- [[niches/wireless-carriers/porting-sim-account-security/fix|🔧 Fix: The Port-Out PIN a Care Agent Can Reset]]
