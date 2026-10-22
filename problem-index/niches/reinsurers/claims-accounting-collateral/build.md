# Statements of Account Checked Against the Contract

**Niche:** [[niches/reinsurers/claims-accounting-collateral/profile|Reinsurance Claims, Technical Accounting & Collateral]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every quarter a reinsurer recomputes hundreds of cedents' statements by hand to find the small differences that age balances past the 90-day line.
**Tags:** #large-language-models #k-nearest-neighbors #feature-engineering #descriptive-statistics #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to agree each cedent's ceded balance, loss and collateral position against the contract terms before the quarter-end, and whoever keeps the fewest balances past 90 days takes the account.

## The Problem
Statements arrive in each cedent's layout. Technical accountants check share, commission, period allocation and reinstatement basis, then query differences through brokers. The same cedents make the same errors each quarter.

## Why Nobody Has Built This
Treaty systems hold the terms but not the incoming documents; accounting tools reconcile ledgers, not documents against contract logic; and volumes per reinsurer are modest next to primary claims.

## What to Build
A reader that turns each statement into a standard structure, recomputes the expected figures from the contract terms, labels each difference by type, drafts the query with the clause and expected figure attached, and tracks each cedent's recurring error pattern for a fix at source.

## Target Customer
Heads of reinsurance operations and technical accounting at reinsurers with several hundred active treaties.

## Impact If Built
Quarter-end reconciliation becomes review rather than recomputation, and aged balances fall before they cost either side.
