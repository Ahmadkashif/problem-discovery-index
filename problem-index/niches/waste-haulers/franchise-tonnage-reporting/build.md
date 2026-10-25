# Jurisdiction-Tagged Loads From Stop to Scale Ticket

**Niche:** [[niches/waste-haulers/franchise-tonnage-reporting/profile|Franchise Tonnage, Diversion & Compliance Reporting]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A truck collects in three towns and dumps once, and the hauler splits that load's tons across the towns by rule of thumb because no system records which stops filled it.
**Tags:** #linear-regression #bayesian-inference #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to produce franchise and state reports straight from scale tickets and stop data, and whoever's reported tonnages reconcile to disposal-site scale records with the smallest variance takes the account.

## The Problem
Franchise reports and state disposal reports need tons by jurisdiction and stream. Scale tickets record a load's weight at the gate; routes record stops. Linking them requires knowing which stops went into which load, and estimating weight per stop when one load serves several jurisdictions.

## Why Nobody Has Built This
Scale-house and routing systems come from different vendors; small haulers' trucks lack on-board scales; and cities accepted rough allocations until diversion targets and EPR reimbursement made the numbers matter.

## What to Build
A load ledger linking each scale ticket to the stops serviced since the last dump (from GPS and arm cycles), with weight allocated by a model of per-stop weight by stream, area and season, calibrated where on-board scales or single-jurisdiction loads exist. Reports for each contract and state are generated from the ledger with the method documented.

## Target Customer
Compliance directors at haulers with many contracts and routes crossing jurisdiction lines.

## Impact If Built
Replacing manual allocation for 25 contracts saves ~400–600 analyst hours a month (estimate) and gives each city a reconciled figure it can audit.
