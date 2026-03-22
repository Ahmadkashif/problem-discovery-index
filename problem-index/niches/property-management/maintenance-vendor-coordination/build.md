# Intelligent Maintenance Dispatch

**Niche:** [[niches/property-management/maintenance-vendor-coordination/profile|Maintenance & Vendor Coordination]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An AI-powered maintenance dispatch system that auto-triages work orders by urgency, matches to the optimal vendor by trade, availability, price, and performance rating, dispatches automatically, and tracks completion — reducing the 15-30 minutes of coordinator time per work order to 1-2 minutes of oversight.
**Tags:** #bert #gradient-boosting #automation #workflow-orchestration #worker-facing

## The Problem
The maintenance dispatch workflow has four manual steps that should be automated. Step 1, triage: the coordinator reads the tenant's description and classifies urgency (emergency, urgent, routine, cosmetic) — this is a text classification task. Step 2, vendor matching: the coordinator selects a vendor based on trade specialty (plumbing, electrical, HVAC, general), geographic proximity to the property, availability, pricing, and past performance — this is a recommendation task. Step 3, dispatch: the coordinator calls or texts the vendor, communicates the scope, and coordinates a time with the tenant — this is a communication automation task. Step 4, follow-up: the coordinator checks 24-48 hours later whether the vendor showed up and completed the work — this is a tracking automation task.

## Why Nobody Has Built This
Each step independently is solvable, but the integration challenge is significant: triage requires NLP on tenant descriptions, vendor matching requires a scored recommendation model, dispatch requires communication automation (texting vendors and tenants), and follow-up requires status tracking with escalation logic. Building all four layers and integrating them into a seamless workflow that the maintenance coordinator trusts enough to step back from is a product challenge. The trust barrier is real: maintenance coordinators have been burned by vendors who don't show up, and they're reluctant to remove themselves from the dispatch loop.

## What to Build
An end-to-end dispatch automation platform: (1) triage: a BERT-based text classifier reads the tenant's maintenance request and classifies urgency + trade, with confidence scores — high-confidence classifications are auto-processed, low-confidence ones are flagged for coordinator review; (2) vendor matching: a recommendation model scores available vendors by trade match, proximity, availability (from vendor calendar integration), pricing (from historical invoices), and performance (completion rate, callback rate, tenant satisfaction) — the top-ranked vendor is recommended with explanation; (3) auto-dispatch: the system sends the work order to the matched vendor via their preferred communication channel (text, email, or vendor portal), coordinates a time with the tenant via text, and confirms the appointment; (4) completion tracking: the system monitors for vendor completion (did they mark the work order done? did the tenant confirm?) and escalates if the vendor doesn't respond within the SLA window.

## Target Customer
Property management companies managing 200+ units spending 20+ hours per week on maintenance coordination. The immediate market: PM companies using AppFolio or Yardi who want to automate the coordination layer on top of their existing work order system.

## Impact If Built
Reduces maintenance coordination time from 15-30 minutes per work order to 1-2 minutes of oversight, saving the coordinator 15-30 hours per week. Improves vendor selection by using performance data (callback rates, completion times, tenant ratings) that coordinators currently don't track systematically. Reduces maintenance response time by 30-50% through instant automated dispatch versus coordinator-mediated scheduling. Could be priced at $3-5 per work order or $2-4/unit/month.
