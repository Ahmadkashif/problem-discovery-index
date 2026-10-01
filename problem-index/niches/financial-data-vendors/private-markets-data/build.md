# Confidence on Every Private Record

**Niche:** [[niches/financial-data-vendors/private-markets-data/profile|Private Markets Data]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A private valuation inferred from a press release and one confirmed by the company sit side by side in the database looking equally certain.
**Tags:** #bayesian-inference #gradient-boosting #evaluation-metrics #confidence-intervals #data-integration #revenue-impact
**Contested on:** Not terminal as stated — competitors are fighting either to find and resolve every private financing round and valuation first, or to hold accurate cash-flow-level performance for the most private funds; different sources, buyers and winners, stated separately in the sub-niches.

## The Problem
Private records vary enormously in provenance: GP-confirmed, inferred from a pension disclosure, estimated from a news report, carried forward from last quarter. Clients see a number. When a deal team or an LP builds a benchmark on it, the weak records are invisible.

## Why Nobody Has Built This
Provenance is tracked loosely by researchers, and exposing it reveals how much of the coverage is inferred — commercially awkward in a coverage race.

## What to Build
Record provenance per field, model the probability that each record is correct from its source type and history of later confirmation or correction, and expose confidence to clients with filters. Use confirmed-later records as labels.

## Target Customer
Heads of private-markets research and product.

## Impact If Built
Turns coverage from a count into a measured quality and lets clients use the weak records knowingly rather than unknowingly.
