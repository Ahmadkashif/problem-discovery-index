# Price Transparency Rate Data Adapted to Underpayment Detection

**Niche:** [[niches/general-hospitals/payer-contract-modelling-underpayments/profile|Payer Contract Modelling & Underpayment Recovery]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Normalised Transparency in Coverage and hospital price files are sold for negotiation and network design, but they can also tell a hospital when its own payer paid it less than the rate that payer published.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to compute, for every remittance line, what each payer's contract says the hospital should have been paid, and whoever catches the most underpaid dollars inside the contract's dispute window takes the account.

## The Problem
Payers publish negotiated rates for every in-network provider, and hospitals now publish median and percentile allowed amounts from their own remittances (CMS-1834-FC, enforced from 1 April 2026). The hospital's own rates are in the payer's file. If the remittance does not match the published rate, one of the two is wrong.

## What Already Exists
Turquoise Health, Serif Health and others normalise the files and sell rate benchmarking for contract negotiation. Both were hiring engineers on their own boards on 24 October 2026.

## The Customization Gap
Underpayment detection needs the hospital's own rows matched by NPI, TIN and plan, with billing-code and modifier logic aligned to how the hospital actually bills. Effective dates must line up with dates of service. Payer files that misstate rates (a known data-quality problem) must be separated from real underpayments, and the output must be a per-claim dispute list, not a market chart.

## Target Customer
Patient financial services directors at hospitals already licensing rate data for negotiation.

## Impact If Solved
A licence bought for the negotiation every 2–3 years starts earning monthly. It catches systematic short-pays that rule-based modules miss because the contract terms were keyed wrong, worth ~0.1–0.3% of commercial net revenue (estimate).
