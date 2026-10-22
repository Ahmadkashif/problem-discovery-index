# A Baseline That Reconciles Itself

**Niche:** [[niches/logistics-consultants/network-design-strategy/profile|Distribution Network Design & Strategy]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The baseline of every network study is reconciled to the client's ledger by an analyst hunting for missing cost, when the gap could be decomposed by cost bucket and matched to the causes past engagements already found.
**Tags:** #gradient-boosting #k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #data-integration #tacit-knowledge-ml #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a client's raw shipment, order and invoice data into a baseline the CFO accepts as the real cost of today's network, and whoever closes that reconciliation fastest gets to run the scenarios that decide the footprint.

## The Problem
The baseline model is built from cleaned shipments, order lines, freight invoices and warehouse cost, then compared with the general ledger. It rarely ties first time. A gap of several percent (estimate) can come from unbilled carriers, intercompany transfers modelled as customer shipments, a month of missing invoices, fuel and accessorials never allocated back to shipments, or warehouse cost booked to the wrong facility. Finding it is a search, done by the most junior person on the team, against a readout date.

## Why Nobody Has Built This
Network design platforms treat the baseline as an input the user supplies, not a reconciliation they help perform. ETL vendors clean tables without knowing what a freight ledger should contain. And the knowledge of where gaps usually hide is held by senior modellers who learned it engagement by engagement and never wrote it down.

## What to Build
A reconciliation engine that compares model cost to ledger cost by bucket (outbound freight by mode, inbound freight, warehouse labour, occupancy, accessorials) and by month and facility, ranks the unexplained gaps, and proposes causes using rules and precedent from past engagements: "parcel cost 9% under ledger in Q3; on similar studies this was address-correction and residential surcharges never allocated." Each confirmed cause becomes a labelled example for the next study.

## Target Customer
Specialist logistics consultancies of 20–500 people and strategy firms' supply chain practices that run several network studies a year.

## Impact If Built
If reconciliation shrinks from two to three weeks to a few days (estimate), the scenario phase starts sooner, and the firm that reaches a trusted baseline first controls the conversation about the footprint.
