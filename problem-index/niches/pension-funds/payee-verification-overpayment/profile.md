# Payee Verification & Overpayment Prevention

**Parent Industry:** [[industries/pension-funds|Pension Funds]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to stop payments to dead or impersonated payees before each monthly payroll runs, and whoever stops the most improper payments before the cutoff without holding a living retiree's check takes the account.

## Profile
**Market Size:** ~$150M a year of death-audit services, account and identity verification, fraud controls and overpayment recovery staff across US pension payrolls (estimate)
**Share of Parent Industry:** ~1% of pension funds' non-investment-management operating spend (estimate)
**Digital Adoption:** Medium — death matching is automated by vendors, change-request verification is a manual callback
**Target Buyer:** Director of Benefits Operations / Retiree Payroll Manager
**Automation Potential:** Very high for matching and risk scoring; holds and recoveries need a person

## What Makes This a Distinct Niche
Public plans paid $418.25B in benefits in 2025, and private DB plans paid $260.5B in 2023, almost all as monthly annuities. Two failure modes leak money. The first is payments that continue after a death nobody reported, especially for payees abroad, which turn into overpayments clawed back from surviving family. The second is payments redirected by fraudsters who change bank details: New Hampshire blocked six faxed attempts in July 2025, Massachusetts has issued alerts, and a former PBGC contractor admitted redirecting participants' pensions. The work is high-volume, rules-based and governed by a hard clock, the payroll cutoff. That makes it the most automatable control in benefits administration.

## Current Tools & Gaps
Death-audit vendors match payee files against death records (see [[niches/funeral-homes/death-verification-data-providers/profile|🔍 Death Verification Data Providers]]). Proof-of-life letters cover payees abroad. Change requests are verified by callback and notarisation. The gaps: change requests are not risk-scored, so every request gets the same check or none; links between requests (shared phone numbers, banks, fax origins) go unseen; and overpayment recovery is a separate team acting months later.

## Problems
- [[niches/pension-funds/payee-verification-overpayment/build|🔨 Build: Change-Request Risk Scoring Before Payroll Cutoff]]
- [[niches/pension-funds/payee-verification-overpayment/buy|🛒 Buy: Bank Account-Takeover Models Adapted to Pension Payroll]]
- [[niches/pension-funds/payee-verification-overpayment/fix|🔧 Fix: Overpayments Recovered From Widows Months After a Death]]
