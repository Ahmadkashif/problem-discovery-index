# Within Policy and Still Wrong

**Niche:** [[niches/spend-management-platforms/card-misuse-detection/profile|Card Misuse Detection]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The spend that costs companies most passes every rule, because the rules check limits and categories and the problem is intent.
**Tags:** #gradient-boosting #graph-theory #change-point-detection #evaluation-metrics #confidence-intervals #compliance #automation #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to find the spend that is within policy and still wrong — and whoever detects insider misuse without accusing honest employees takes the risk the rule engine was never built to see.

## The Problem
The transactions that cost companies real money are not the ones that breach a limit. They are the personal purchases dressed as business ones, the expense claimed twice through different channels, the consistently inflated category, the vendor that happens to be owned by the person approving the invoices, the subscription that continues after the employee left. Every one sits inside policy. The platform sees the full behavioural context — who, when, where, how often, compared to peers — and models none of it.

## Why Nobody Has Built This
Fraud was framed as an external threat because that is where the card networks focused, so internal misuse was left to controllers' intuition — the product inherited the network's threat model rather than the customer's. Accusing employees is uncomfortable and false positives are costly in a way they are not for card fraud. The rule engine's success at policy enforcement made it look like the risk was covered. And nobody measures what is missed, so the problem is invisible.

## What to Build
Model behaviour rather than rules. Build a behavioural profile per employee and per role, which is the core and is what makes the deviation interpretable rather than merely unusual. Compare against peers in similar roles, since a salesperson's travel pattern is only judgeable against other salespeople and this comparison is the strongest signal available. Detect duplicate claims across channels — card, reimbursement, invoice — because the same expense submitted twice through different routes is common and current duplicate detection only catches exact matches. Examine vendor relationships for conflicts, as a supplier connected to an employee is a graph problem the platform can run and nobody does. Detect the subscription that outlives its owner, which is pure waste, entirely mechanical, and present at almost every customer. Flag the pattern rather than the transaction, since a single item is rarely conclusive and a pattern over months usually is. Rank by materiality so investigation effort goes where the money is. Present findings as questions rather than accusations, because the human cost of a false accusation is the reason this has not been built and the framing is what makes it deployable. Support the investigation with evidence assembled, as the controller currently starts from nothing. Report what was found and what it was worth, which is how the capability justifies itself. And keep the employee's privacy in view, since behavioural monitoring of staff needs a defensible basis.

## Target Customer
Card operations and risk leadership, customer controllers and internal audit, and fraud vendors whose models target external threats.

## Impact If Built
The product inherited the card network's threat model rather than the customer's, so internal misuse was left to intuition. Peer-relative behavioural profiles and cross-channel duplicate detection find the spend that passes every rule.
