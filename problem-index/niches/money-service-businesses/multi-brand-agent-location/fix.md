# Sweep Debits the Agent Cannot Reconcile

**Niche:** [[niches/money-service-businesses/multi-brand-agent-location/profile|The Multi-Brand Agent Location]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** The amount each brand debits from the store's account rarely matches the day's settlement report, because commissions, cancellations, refunds and fees are netted on different days, so the owner cannot tell an error from a timing difference.
**Tags:** #feature-engineering #descriptive-statistics #data-integration #worker-facing #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep the agent's single bank account solvent across every brand's ACH sweep, so the store never has a returned debit, and whoever makes its sweeps most predictable for the agent takes the account.

## The Problem
At the end of each day the clerk prints each brand's settlement report. A day or two later each transmitter debits the store's account. The debit nets the day's collections against commissions, cancelled transfers, refunds paid at the counter, and sometimes equipment or compliance fees charged on their own schedule. When the amounts do not match, the owner calls each brand's agent support line, or does not and hopes the next sweep corrects it.

## Why It's Still Broken
Each transmitter designs its settlement report for its own reconciliation, not the agent's. Reports and debits use different cut-off times and descriptors, and no agent-side tool joins three brands' reports to one bank statement.

## What a Fix Looks Like
A per-brand settlement statement that lists every item the next debit will contain, with the debit date and amount stated in advance; a standard descriptor on the debit that matches the statement; and, for transmitters competing for multi-brand counters, an agent view that imports the store's bank feed and flags any debit that differs from its statement.

## Who Feels the Pain
Store owners reconciling by hand after closing, agent support teams fielding calls, and treasury teams chasing returns caused by debits the owner did not expect.

## Impact If Fixed
Owners know what will leave their account and when, unexplained debits fall, and the brand that makes its sweeps predictable earns the front of the counter.
