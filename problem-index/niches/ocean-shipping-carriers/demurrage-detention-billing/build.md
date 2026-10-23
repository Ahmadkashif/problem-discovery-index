# A Free-Time Clock Rebuilt From Every Source

**Niche:** [[niches/ocean-shipping-carriers/demurrage-detention-billing/profile|Demurrage & Detention Billing and Disputes]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every D&D invoice rests on a free-time clock that must reflect contract terms, terminal availability, holds and the carrier's own delays, and today it is rebuilt by hand when challenged.
**Tags:** #large-language-models #logistic-regression #feature-engineering #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to bill every chargeable container day inside the FMC's 30-day window on an invoice that survives dispute, and whoever collects the highest share of billed demurrage and detention without waiver takes the account.

## The Problem
The billing system counts days from discharge to gate-out and from gate-out to empty return. The FMC rule requires more: the invoice must state free time, its start and end, the availability date and the basis for charging the billed party, and certify that the carrier's own performance did not cause the charge. Terminal closures, appointment shortages, customs holds and late vessels can all stop or shift the clock.

## Why Nobody Has Built This
The evidence spans the carrier's equipment system, terminal operating systems, appointment portals, customs data and vessel operations, owned by different parties. Before 2024 an approximate invoice was good enough.

## What to Build
A clock engine that ingests contract and tariff terms, container events, terminal closures and appointment availability, holds and vessel delays. It computes chargeable days with every pause explained and generates the invoice with all 46 CFR 541 elements inside the 30-day window. When a dispute arrives it classifies the reason, attaches the evidence and drafts the reply. Portcast (Singapore, Senior ML Engineer) and project44 (Chicago, Senior FDE) hold the milestone data this needs and are hiring (checked 2026-10-24).

## Target Customer
Billing and equipment heads at ocean carriers and NVOCCs in US trades. Marine terminal operators bill their own demurrage under the same rule, and that work belongs to the queued port-terminal-operators industry.

## Impact If Built
If ~5% of ~$50M a year of US D&D billing (estimate) is lost to late, incomplete or overturned invoices, recovering most of it is ~$2M a year per carrier (estimate). Disputes are also resolved inside 30 days with evidence attached.
