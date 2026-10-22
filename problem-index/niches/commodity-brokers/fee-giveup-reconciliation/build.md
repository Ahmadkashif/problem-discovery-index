# Expected Cost per Trade Computed at the Fill

**Niche:** [[niches/commodity-brokers/fee-giveup-reconciliation/profile|Exchange Fee, Give-Up & Brokerage Reconciliation]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nobody computes what a futures trade should have cost until the invoices arrive, so fee errors are found weeks late or never.
**Tags:** #large-language-models #gaussian-mixture-models #random-forests #feature-engineering #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to match every exchange, clearing, NFA and give-up fee to the trade that incurred it before month-end invoices are paid, and whoever recovers the most mis-billed fees before payment takes the account.

## The Problem
Fee schedules are published as exchange notices and contract amendments, client rate cards are negotiated individually, and give-up fees depend on agreements between executing and clearing brokers. The expected cost of each trade exists only implicitly, in the head of an operations analyst.

## Why Nobody Has Built This
Back-office systems apply fees as configured but don't audit them; invoices arrive in different formats from each party; and turning fee notices into machine-readable rules was too labour-intensive.

## What to Build
A fee engine that reads exchange fee notices, rate cards and give-up agreements into effective-dated rules, computes each trade's expected fees at the fill, and matches them against statement lines and invoices as they arrive. Breaks are flagged with causes and amounts, and anything that does not fit the rules is flagged for review.

## Target Customer
Futures operations heads at FCMs and executing brokers, and operations teams at funds and commercials paying brokerage.

## Impact If Built
Fee breaks are caught before payment, and the dollars recovered and hours saved both scale with volume.
