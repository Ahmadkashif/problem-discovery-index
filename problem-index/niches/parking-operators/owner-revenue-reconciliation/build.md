# A Session-to-Deposit Reconciliation Engine

**Niche:** [[niches/parking-operators/owner-revenue-reconciliation/profile|Owner Revenue Reconciliation & Reporting]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators reconcile managed facilities at summary level each month, so a missing ~2% of revenue shows up as a vague variance rather than as the transactions that caused it.
**Tags:** #autoencoders #gaussian-mixture-models #change-point-detection #large-language-models #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to account for every dollar a managed facility collects, and whoever shows the smallest unreconciled gap between recorded parking sessions and deposited revenue at the owner's audit takes the account.

## The Problem
A garage's revenue arrives through five or six channels, each with its own timing and fees. Analysts tie totals to the bank and explain differences in a sentence. Lost tickets waived, voids by one cashier, validations redeemed but never invoiced, bookings with no exit and gate raises with no reason all vanish into a single variance line.

## Why Nobody Has Built This
PARCS vendors report their own transactions, marketplaces report theirs, and accounting systems see deposits. Nobody sits across all three at session level. Each management contract has its own reimbursable-expense and fee rules, which defeats generic close software.

## What to Build
An engine that ingests PARCS sessions, channel bookings and payouts, monthly billing, validations, card settlements and deposits, and matches them at session level. Contract terms are parsed once into rules for expenses and fees. Unmatched items are classified (timing, fee, void, waiver, raise, no-show booking, unbilled validation), and shift-level anomaly scores route suspicious patterns to revenue control. The output is the owner statement with every variance traced to transactions.

## Target Customer
Revenue-control and accounting leaders at operators with 100+ managed facilities; owners' internal audit teams as a second buyer.

## Impact If Built
At ~1–3% leakage on cash-handling facilities (estimate), a region collecting $100M of gross revenue for owners recovers or prevents ~$1–3M a year, and the month-end close drops from ~10 days to ~3 for each analyst (estimate).
