# Exchange Fee, Give-Up & Brokerage Reconciliation

**Parent Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to match every exchange, clearing, NFA and give-up fee to the trade that incurred it before month-end invoices are paid, and whoever recovers the most mis-billed fees before payment takes the account.

## Profile
**Market Size:** ~$200M a year in fee reconciliation software, outsourced operations and staff time across FCMs and their institutional clients (estimate)
**Share of Parent Industry:** ~6% of technology and services spend (estimate)
**Digital Adoption:** Medium — every input is electronic, but matching across exchange invoices, clearing statements, executing-broker bills and give-up agreements is still largely spreadsheet work
**Target Buyer:** Head of futures operations / brokerage fee manager at an FCM, or the operations lead at a fund paying executing and clearing brokers
**Automation Potential:** Very high

## What Makes This a Distinct Niche
A single futures trade can generate an exchange fee, a clearing fee, an NFA assessment, an executing broker's commission, a clearing FCM's commission and, if executed by one firm and cleared by another, a give-up fee under a give-up agreement. Each is billed by a different party on a different cycle and schedule, and fee schedules change during the year. CME alone cleared a record 28.1 million contracts a day in 2025. The FCM passes some fees through to customers, absorbs others and is invoiced for others, and its institutional clients reconcile the same trades from the other side. The work is high-volume, rule-bound and pure data, which is why it is automatable. It is still done by hand because the rules live in contracts and fee notices rather than in systems.

## Current Tools & Gaps
Back-office fee tables in FIS and ION, industry utilities from FIA Tech for give-up agreements and brokerage reconciliation, generic reconciliation tools, Excel. The gaps: fee schedules maintained by hand after each exchange notice, rate-card exceptions per client held in email, and breaks discovered after invoices are paid.

## Problems
- [[niches/commodity-brokers/fee-giveup-reconciliation/build|🔨 Build: Expected Cost per Trade Computed at the Fill]]
- [[niches/commodity-brokers/fee-giveup-reconciliation/buy|🛒 Buy: Telecom Expense Auditing Adapted to Futures Fees]]
- [[niches/commodity-brokers/fee-giveup-reconciliation/fix|🔧 Fix: The Exchange Fee Change Applied a Month Late]]
