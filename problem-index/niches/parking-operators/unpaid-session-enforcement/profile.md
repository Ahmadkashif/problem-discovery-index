# Unpaid-Session Recovery & Private-Property Enforcement

**Parent Industry:** [[industries/parking-operators|Parking Operators]]
**Category:** Highly Automatable
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn unpaid parking sessions into collected revenue. That produces two contests with different winners: making payment happen before the car leaves, won by camera and PARCS platforms on the share of sessions paid without a notice, and recovering the sessions that slip through by mailed notice, won by notice processors on the share of notice value collected under each state's rules. Decomposed into contested sub-niches below.

## Profile
**Market Size:** ~$900M a year in enforcement staff, camera and PARCS enforcement features, notice-processing fees and collections (estimate)
**Share of Parent Industry:** ~8% of operator receipts (estimate)
**Digital Adoption:** Medium — camera capture and notice generation are digital; dispute handling and state-rule checks are manual
**Target Buyer:** Operator VP of operations or revenue; owners of gateless lots; notice-processing firms
**Automation Potential:** High for matching and notice generation; limited by state law

## What Makes This a Distinct Niche
Gateless entry trades the gate arm for a promise to pay. Some share of drivers do not pay, at ~5–15% of sessions at unattended lots without enforcement (estimate), and the operator must either collect at the exit or chase afterwards. The law now governs both routes. Maine's 2025 chapter 350 sets notice content, a 10-business-day minimum and treble damages, and applies the state's prohibition on plate recognition at lots open to the public, subject to that statute's exceptions. DPPA suits challenge registered-owner lookups, including Crostarosa v. LAZ Parking, Asura and PRRS, where a January 2026 order kept LAZ and Asura in court. The plate-reader camera work itself mirrors the repossession industry's [[niches/repossession-services/lpr-camera-operations/profile|Licence-Plate Camera Operations]], but here the plates are read only at the operator's own facilities.

## Current Tools & Gaps
Camera platforms (Metropolis, FLASH, Rekor, Genetec AutoVu, Asura), pay-by-plate apps, notice processors such as PRRS, and collections agencies. Gaps: no single ledger of unpaid sessions from exit to notice to payment; misreads found only when disputed; state rules checked by memory.

## Problems
- [[niches/parking-operators/unpaid-session-enforcement/build|🔨 Build: An Unpaid-Session Ledger From Gate to Notice]]
- [[niches/parking-operators/unpaid-session-enforcement/buy|🛒 Buy: Card Retry and Account Updating Adapted to Parking Sessions]]
- [[niches/parking-operators/unpaid-session-enforcement/fix|🔧 Fix: Leakage Counted Only When a Notice Is Mailed]]
