# Subcontracting by Default Because Nobody Counts Utilisation

**Niche:** [[niches/facilities-management-firms/self-delivery-subcontract-mix/profile|Self-Delivery vs Subcontract Delivery Mix]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Technician time is booked to the account, so nobody knows whether in-house staff had room for the job that just went to a subcontractor.
**Tags:** #descriptive-statistics #time-series-forecasting #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide, service by service and region by region, whether its own technicians or a subcontractor will do the work more cheaply at the contracted SLA, and whoever builds enough self-delivery density to keep margin off the pass-through line takes the account.

## The Problem
Site technicians record a day's hours against the account code, not against work orders, so utilisation is unknown. When a reactive call comes in and the coordinator is unsure who is free, calling the subcontractor is the safe choice for the SLA. Repeated across a year, the account pays markup on work its own people could have done.

## Why It's Still Broken
Timekeeping exists for payroll and client billing, which need hours per account and nothing finer. Asking technicians to clock work orders feels like surveillance and adds close-out burden.

## What a Fix Looks Like
Derive utilisation from what the CMMS already records: work-order start and completion times on the technician's phone, plus travel inferred from site sequence, reconciled weekly against payroll hours. Show coordinators live availability by trade at dispatch, and show the account a monthly view of subcontracted jobs that fell inside idle in-house capacity.

## Who Feels the Pain
Account directors paying markup they could avoid, coordinators making dispatch calls blind, and technicians whose spare capacity is invisible until someone decides they are surplus.

## Impact If Fixed
A visible, measured basis for each subcontract call, and a recoverable slice of pass-through spend on accounts with in-house teams (estimate: several percent of subcontracted reactive work).
