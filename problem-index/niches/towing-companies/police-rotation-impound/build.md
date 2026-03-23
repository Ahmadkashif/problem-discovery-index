# Dispatch-to-Impound-to-Auction Workflow Platform

**Niche:** [[niches/towing-companies/police-rotation-impound/profile|Police Rotation & Impound Operators]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool connects the police tow dispatch, impound intake, lien filing, owner notification, and auction pipeline into one workflow — operators use 3-4 disconnected systems with manual handoffs.
**Tags:** #workflow-orchestration #automation #compliance #data-integration

## The Problem
A police-rotation tow creates a chain of events spanning days to months: (1) dispatch receives police call, (2) driver tows vehicle to impound lot, (3) lot attendant logs vehicle and photographs condition, (4) office manager runs title search and mails registered owner notification, (5) storage fees accrue daily, (6) if unclaimed after statutory hold period, office files lien, (7) after lien matures, vehicle goes to auction or salvage. Each step is handled in a different system — dispatch in Towbook, lot inventory in a spreadsheet or TOPS, title search via a state DMV portal, notifications via certified mail, and lien filing via courthouse forms. The handoff points are where balls get dropped: a vehicle gets impounded but never entered in the lot system, a notification gets mailed but the return receipt isn't tracked, a lien deadline passes because nobody calendared it.

## Why Nobody Has Built This
The workflow spans dispatch (operations), lot management (physical asset tracking), title/lien processing (legal compliance), and billing (finance) — four domains that software vendors typically serve separately. Building an end-to-end platform requires integrating with state DMV systems (for title searches), USPS (for certified mail tracking), courthouse e-filing systems (for liens), and auction platforms (for vehicle disposition). Each state has different rules, making the compliance layer a 50-state problem. The market (~10,000 impound-operating towing companies) is small enough that no single vendor has invested in the full workflow.

## What to Build
An integrated platform that tracks a police-tow vehicle from dispatch through auction: auto-creates an impound record when a police tow is dispatched, prompts lot intake documentation (photos, condition report, VIN scan), triggers automatic title search via state DMV API, generates and tracks owner notifications with certified mail integration, calendars jurisdiction-specific hold periods and lien deadlines, auto-generates lien filings, and manages auction listing when the vehicle becomes eligible. Single vehicle timeline view shows every step with status, dates, and next required action.

## Target Customer
Towing companies operating impound lots with 50-500 vehicles under police rotation contracts, currently managing the dispatch-to-auction pipeline across 3-4 disconnected systems.

## Impact If Built
Eliminates missed deadlines that cost $500-$2,000 per vehicle in eaten storage costs. Reduces administrative time per impound vehicle from 2-3 hours total to 30-45 minutes. For a lot processing 200 vehicles/year, saves $10,000-$25,000 in administrative costs and prevented losses.
