# A Payer Behaviour Ledger Joining Denials, Contracts and Outcomes

**Niche:** [[niches/general-hospitals/revenue-cycle-denials-contract-yield/profile|Revenue Cycle: Denials & Payer Contract Yield]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A hospital negotiates each payer contract every two to three years without a record of what that payer did to it under the last one: which claims it denied, which it underpaid, which appeals it lost and what that cost.
**Tags:** #gradient-boosting #large-language-models #causal-inference #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to collect what the hospital is owed on each claim. Clinical denials are won by whoever builds the strongest chart-and-policy argument before the appeal deadline, and contract yield by whoever models every payer's contract terms against every remittance. Decomposed into contested sub-niches.

## The Problem
Denials live in the denial worklist, underpayments in the contract-management module, appeals and outcomes in a spreadsheet or a vendor portal, and the contracts themselves in a shared drive. When the managed-care team sits down to renegotiate with a national payer, it has the rate tables and anecdotes. What it lacks is a dollar figure for the payer's behaviour: avoidable denials, overturn rates by denial type, days to payment, underpaid lines by clause, and administrative cost per claim.

## Why Nobody Has Built This
Each vendor owns one slice. Denial tools report denials, contract modellers report variances, and outsourced revenue-cycle firms report to their own fee terms. Contracts are unstructured PDFs with amendments, so linking a clause to a remittance line needs document AI that only recently became cheap enough.

## What to Build
A ledger that extracts contract terms and amendments into a structured model, links every 835 line to the clause that should have priced it, and joins denials to appeals and final payment. It estimates the cost of each payer behaviour, including staff time per appeal, using Premier's $80-per-MA-appeal figure as a prior until the hospital's own time data arrives. It produces a negotiation pack per payer and a monthly behaviour scorecard.

## Target Customer
VPs of managed care and revenue cycle at systems with 3+ hospitals and $1B+ net patient revenue.

## Impact If Built
Turning anecdote into a dollarised record of payer behaviour gives the hospital contract language worth ~0.5–1% of net revenue from that payer (estimate), such as bans on retrospective DRG downgrades after authorisation and prompt-pay terms.
