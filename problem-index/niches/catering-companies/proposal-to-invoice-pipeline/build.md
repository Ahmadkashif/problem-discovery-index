# Event-Level P&L Automation

**Niche:** [[niches/catering-companies/proposal-to-invoice-pipeline/profile|Proposal-to-Invoice Financial Pipeline]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automatically generates a per-event P&L by linking proposal pricing, purchasing invoices, labor timesheets, and rental costs to individual events — making event-level profitability invisible.
**Tags:** #data-integration #automation #workflow-orchestration #revenue-impact

## The Problem
A mid-size caterer doing 400 events/year knows their annual profit but cannot tell you which events made money and which lost money. The proposal says $45/head; the actual food cost was $18 or $24 (they do not know which); labor was 6 hours or 10 hours (they did not track by event); rentals were $800 or $1,200 (the invoice covered two events). Per-event P&L requires linking data from 4-5 systems — CRM (proposal), accounting (invoices), scheduling (labor hours), rental platforms (equipment costs) — and this linkage does not exist.

## Why Nobody Has Built This
The data integration challenge is the barrier. Each data source uses different identifiers: the CRM calls it "Johnson Wedding," QuickBooks records the vendor invoice without an event reference, the staff timesheet shows hours worked on "Saturday" without specifying which event. Matching these records requires either manual attribution (which takes 30-60 minutes per event and nobody does it) or a system that assigns event IDs at the proposal stage and carries them through every downstream transaction.

## What to Build
An event financial management system that assigns a unique event ID at proposal creation and tags all downstream transactions to that ID: purchasing (ingredients purchased for this event), labor (hours worked on this event's prep and service), rentals (equipment rented for this event), and overhead allocation. Post-event, the system generates an automatic P&L showing revenue, itemized costs, and margin — with comparison to the original proposal estimate, highlighting where the quote was off.

## Target Customer
Catering company owners doing 200+ events/year who currently calculate profitability at the company level (quarterly P&L) and have never seen per-event margins.

## Impact If Built
Per-event P&L visibility enables caterers to identify and reprice the 20-30% of events that are underwater — recovering $100K-$500K in annual margin for a $3M operation. The proposal-vs-actual comparison trains the sales team to quote more accurately over time.
