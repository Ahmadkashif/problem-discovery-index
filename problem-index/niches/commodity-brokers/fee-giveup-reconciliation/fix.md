# The Exchange Fee Change Applied a Month Late

**Niche:** [[niches/commodity-brokers/fee-giveup-reconciliation/profile|Exchange Fee, Give-Up & Brokerage Reconciliation]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** An exchange announces a fee change, the back office updates its tables weeks later, and a month of customer statements is wrong.
**Tags:** #large-language-models #feature-engineering #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to match every exchange, clearing, NFA and give-up fee to the trade that incurred it before month-end invoices are paid, and whoever recovers the most mis-billed fees before payment takes the account.

## The Problem
Fee notices arrive by email and website posting, are read by whoever has time, and are configured manually. A missed or late change means under-recovered pass-throughs or overcharged customers. Both are discovered at month-end, and both are corrected by adjustment.

## Why It's Still Broken
Nobody owns monitoring fee notices across every exchange and clearing house the FCM uses, and the configuration step is manual.

## What a Fix Looks Like
Automated monitoring of exchange and clearing-house fee notices. Each change is extracted into a proposed fee-table update with its effective date and routed to operations for approval before it takes effect.

## Who Feels the Pain
Futures operations teams, customers receiving adjusted statements, and IBs whose payouts shift after the fact.

## Impact If Fixed
Fee tables change on the effective date rather than weeks later, which removes a recurring source of statement corrections.
