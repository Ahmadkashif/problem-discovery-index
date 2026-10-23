# Contracts Read Straight Into the Pricing Engine

**Niche:** [[niches/general-hospitals/payer-contract-modelling-underpayments/profile|Payer Contract Modelling & Underpayment Recovery]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every expected-payment engine is only as good as the contract terms an analyst keyed into it, and nobody checks those terms against the PDF and its amendments after go-live.
**Tags:** #large-language-models #transformers #evaluation-metrics #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to compute, for every remittance line, what each payer's contract says the hospital should have been paid, and whoever catches the most underpaid dollars inside the contract's dispute window takes the account.

## The Problem
A system with 40 commercial contracts, each with exhibits and five years of amendments, has a managed-care analyst who keys rate tables into the contract-management module. Misloaded terms are the commonest source of both missed underpayments and false variances (recalled). When a payer's amendment changes the implant carve-out, the module keeps the old term until someone notices.

## Why Nobody Has Built This
Contract language is idiosyncratic, the engine's configuration schema is vendor-specific, and extraction errors are costly. Until LLMs, document AI could not reliably read reimbursement methodology clauses.

## What to Build
An extractor that reads contracts and amendments into a structured reimbursement model (methodology by service line, rates, carve-outs, outlier and stop-loss terms, lesser-of clauses, effective dates) with clause citations. It diffs that model against the engine's configuration and flags mismatches, then back-tests the corrected terms on twelve months of 835s to size what was missed.

## Target Customer
Managed-care and revenue integrity leaders at multi-hospital systems; contingency recovery firms wanting faster set-up per client.

## Impact If Built
Correcting misloaded terms recovers underpayments retroactively within dispute windows and stops false variances that waste analyst time, worth ~0.3–0.5% of commercial net revenue (estimate).
