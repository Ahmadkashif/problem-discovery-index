# Subsidy-Aware Parent Billing Automation

**Industry:** [[childcare-centers|Childcare Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A single family's monthly invoice can involve a state subsidy, an employer FSA, a sibling discount, a part-time schedule adjustment, and a late-pickup surcharge — and the center's billing software handles maybe two of those correctly.
**Tags:** #gradient-boosting #regression #tabular-ml #workflow-orchestration

## The Problem
Childcare billing is far more complex than standard recurring invoicing. A single family's charges may combine: a base tuition rate that varies by age group and schedule type (full-time, part-time, drop-in); a state childcare subsidy (CCDF vouchers) that reimburses at a different rate than tuition, pays on a different cadence, and requires separate attendance documentation; an employer-sponsored dependent care FSA with its own reimbursement rules; sibling discounts (often 5-15% on the second child); and ad-hoc charges like late pickup fees ($1-5/minute), registration fees, and supply fees. Directors or bookkeepers spend 8-15 hours per month reconciling these layered payment sources, chasing subsidy reimbursements from state agencies, and manually calculating parent copays.

## What Already Exists
Procare and brightwheel offer recurring billing, autopay, and basic subsidy tracking. QuickBooks and Xero handle general invoicing. These tools can set a recurring tuition charge and process credit card payments, covering the simplest billing scenario.

## The Customisation Gap
No general billing tool understands the interaction between subsidy payment schedules and parent copay calculations — when a state subsidy payment is delayed, the parent's copay temporarily covers the gap, and the reconciliation when the subsidy arrives requires manual journal entries. The variable-schedule problem (families attending Mon/Wed/Fri one week, Tue/Thu the next) breaks recurring billing templates entirely. Sibling discount rules that interact with subsidy caps (some states cap subsidy reimbursement, and discounts must be applied in the right order relative to the cap) require childcare-specific logic that no general accounting system encodes. A purpose-built billing engine needs to model the full payment waterfall: tuition → subsidy coverage → copay calculation → discount application → ad-hoc charges → payment allocation → reconciliation.

## Impact If Solved
Directors reclaim 8-15 hours per month from billing reconciliation. Subsidy reimbursement delays drop as attendance documentation is auto-generated in the format each state requires. Parent billing disputes decrease because invoices are transparent and itemized. Cash flow becomes predictable because the system forecasts when subsidy payments will arrive based on historical state agency payment patterns.
