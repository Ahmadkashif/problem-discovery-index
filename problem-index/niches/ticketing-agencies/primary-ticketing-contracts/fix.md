# The Fee Rebate Nobody Can Reconcile

**Niche:** [[niches/ticketing-agencies/primary-ticketing-contracts/profile|Primary Ticketing for Venues, Tours & Teams]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** A venue is paid a share of ticket fees under a tiered schedule and checks the cheque against a statement the ticketer produced.
**Tags:** #descriptive-statistics #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to win a venue's or rights holder's exclusive primary ticketing contract, now that the DOJ settlement caps fees at 15% and opens venues to rival ticketers. A tour onsale and a team's season-ticket base are won on different evidence, by different buyers, on different clocks. Decomposed into contested sub-niches below.

## The Problem
Fee rebates are calculated per ticket, by price band, event type and channel, with exclusions for comps, promoter-controlled shows and resale. The venue receives a monthly or per-event statement and a payment. Finance staff spot-check a few events in spreadsheets; the rest are accepted.

## Why It's Still Broken
The venue has the contract and the ticketer has the data. Seat-level exports are available but large and formatted for the ticketer's reporting, and venue finance teams are small. Underpayments are found, if at all, at contract renewal or in an audit.

## What a Fix Looks Like
Load the contract's fee schedule once, ingest the seat-level sales export monthly, recompute the rebate per event, and flag variances with the tickets that explain them.

## Who Feels the Pain
Venue controllers, university athletics business offices and venue management companies' finance teams.

## Impact If Fixed
Rebate errors of even a fraction of a percent on millions of tickets are found monthly rather than years later (estimate).
