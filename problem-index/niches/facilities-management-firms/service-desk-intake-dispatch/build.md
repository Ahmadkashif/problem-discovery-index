# First-Time-Right Dispatch Without a Triager

**Niche:** [[niches/facilities-management-firms/service-desk-intake-dispatch/profile|Service Desk Intake & Dispatch]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every closed ticket already records the right trade, asset and priority, and new tickets are still classified by a person reading them.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a vague occupant request into a correctly classified, prioritised and dispatched work order inside the SLA response clock, and whoever gets dispatch right the first time without a human triager takes the account.

## The Problem
"It's freezing in here," "water on the floor by the lifts," "the badge reader isn't working": each needs a site, an asset, a trade, a priority under that client's definitions, and the right technician or subcontractor. Coordinators do it by hand, under a clock, and the errors become wrong-trade dispatches, missed SLAs and arguments in the monthly review.

## Why Nobody Has Built This
Intake modules were built for forms, not language, and priority definitions differ by contract. Until recently, text classification good enough to dispatch without review needed per-client model building nobody would fund.

## What to Build
An intake agent that reads or listens to every request, asks the one clarifying question that settles priority ("is water actively leaking?"), classifies trade, asset and priority under the contract's own definitions, checks the asset's recent history for a repeat, and dispatches by skill, location and SLA, sending low-confidence and safety-critical cases to a coordinator. It trains on the provider's closed tickets and learns each contract's definitions from the corrections coordinators make.

## Target Customer
Service desk leaders at IFM providers and corporate help desks with high request volumes.

## Impact If Built
Most requests dispatched without a human touch, faster response on true emergencies and fewer wrong-trade callouts (estimate: half or more of coordinator triage time).
