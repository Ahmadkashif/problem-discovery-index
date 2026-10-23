# An Independent Reconciliation of the Provider's Own Data

**Niche:** [[niches/facilities-management-firms/client-side-contract-manager/profile|The Client-Side IFM Contract Manager]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The client owns the contract and often the CMMS, and still cannot test a single KPI or invoice without asking the provider.
**Tags:** #descriptive-statistics #hypothesis-testing #large-language-models #data-integration #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give the occupier an independent read of whether its IFM contract is delivering what it was priced to deliver, and whoever can reconcile the provider's own work orders and pass-through invoices to the SLA schedule without the provider's help takes the account.

## The Problem
Contract managers receive a monthly KPI pack and a monthly invoice, both from the provider. Testing them means pulling raw work orders, applying the contract's KPI definitions, matching invoices to work orders and rate cards, and spotting priority manipulation or duplicate billing. That is analyst work a one- or two-person team cannot do every month.

## Why Nobody Has Built This
Providers have no reason to build it, and consultants sell periodic audits by the hour. Client-side teams are small and buy rarely. The data is technically accessible but scattered across the provider's systems.

## What to Build
A client-side service that ingests the contract (SLA definitions, responsibility matrix, rate cards, markup terms), connects read-only to the work-order and invoice data the client is entitled to, and each month recomputes every KPI, tests for priority reclassification and ticket splitting, matches pass-through invoices to work orders and rates, and benchmarks reactive volume and cost against the client's own history. It flags discrepancies with the tickets behind them for the quarterly review.

## Target Customer
Heads of real estate and FM contract managers at corporate occupiers, universities, health systems and public owners with outsourced IFM.

## Impact If Built
The client governs on its own numbers, disputes rest on evidence, and recovered overbilling and fee-at-risk adjustments can pay for the service many times over (estimate).
