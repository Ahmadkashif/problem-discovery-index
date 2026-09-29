# Deposit Screening

**Parent Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Category:** 🔵 High Market Share
**Contested on:** Every serious competitor in this niche is fighting to decide correctly whether arriving funds are criminal proceeds — and the contest splits cleanly enough that it is not terminal.

## Profile
**Market Size:** ~$3.8B US
**Share of Parent Industry:** ~25% of category revenue
**Digital Adoption:** Medium — vendor scores plus manual review
**Target Buyer:** Exchange compliance leadership
**Automation Potential:** High — inference and evaluation, both unexploited

## What Makes This a Distinct Niche
Funds arrive at an exchange from an on-chain address. A blockchain analytics vendor characterises that address and its history; above a threshold the exchange holds the funds and investigates. This single decision touches every customer's money, drives the support queue, determines the exchange's regulatory posture, and has never been measured. It is the largest contest in the category — but it is two contests, because inferring what an address is and evaluating whether the resulting decision was right are different problems with different winners.

### Contested sub-niches
- [[niches/crypto-exchanges/address-attribution/profile|🎯 Address Attribution & Taint Propagation]]
- [[niches/crypto-exchanges/screening-decision-quality/profile|🎯 Screening Decision Quality]]

## Current Tools & Gaps
Blockchain analytics feeds, address risk scores, threshold rules, case management and manual investigation. The gaps: attribution bought rather than built, from a vendor whose labels originate at exchanges; taint propagation by heuristics that are contested and undocumented; thresholds set years ago and never evaluated; and no measurement of the control's precision because outcomes almost never return.

## Problems
- [[niches/crypto-exchanges/deposit-screening/build|🔨 Build: The Control Nobody Has Evaluated]]
- [[niches/crypto-exchanges/deposit-screening/buy|🛒 Buy: Transaction Monitoring for a Public Ledger]]
- [[niches/crypto-exchanges/deposit-screening/fix|🔧 Fix: Frozen With No Explanation]]
