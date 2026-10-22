# One Ledger From Carrier Statement to Rep Paycheck

**Niche:** [[niches/wireless-retail-agents/commission-reconciliation-chargebacks/profile|Commission Reconciliation & Chargebacks]]
**Industry:** [[industries/wireless-retail-agents|Wireless Retail Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The dealer reconciles carrier statements in one system and claws back rep commissions in another, so a recovered dispute is rarely repaid to the rep, and a rep's clawback can't be traced to a carrier line.
**Tags:** #large-language-models #random-forests #feature-engineering #data-integration #workflow-orchestration #compliance #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor here is fighting to make each activation's commission end up where it belongs. Toward the carrier, that means recovering short-paid lines before dispute windows close, a contest won by statement-matching coverage. Toward the rep, it means netting chargebacks into pay with an audit trail that survives wage law, a contest won by payroll-grade explainability. These are two contests with different winners. Decomposed into contested sub-niches below.

## The Problem
A chargeback arrives on the carrier statement, and someone decides whether it's valid, disputes it or accepts it, and separately someone in payroll deducts it from a rep. When the dispute succeeds three weeks later, the rep's deduction usually stands, because the two processes don't share a record.

## Why Nobody Has Built This
Reconciliation vendors sell to finance and incentive-compensation vendors sell to sales operations and HR. Each covers one half of the chain, and dealers have been too small a segment for either to build the other half.

## What to Build
A single activation-level ledger. Each line carries its expected commission (from the plan), actual payment and chargebacks (from statements), dispute status and outcome, and the rep allocation and payroll effect. Disputes that succeed reverse the rep's deduction automatically, and every rep-pay adjustment links to the carrier line that caused it.

## Target Customer
Controllers and directors of commissions at chains of 50+ stores; packaged for master agents serving prepaid dealers.

## Impact If Built
One source of truth for the money that defines the business, fewer wage disputes, and a clean audit trail if a rep or regulator challenges a clawback.
