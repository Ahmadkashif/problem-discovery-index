# Move-Specific CRM and Booking Pipeline

**Industry:** [[moving-companies|Moving Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic CRMs can track leads but cannot handle the move-specific booking lifecycle — survey scheduling, binding/non-binding quote variants, deposit collection, crew assignment, and post-move follow-up in one flow.
**Tags:** #llm #text-generation #nlp #workflow-orchestration

## The Problem
A moving company's sales cycle is unlike almost any other service business: a lead comes in via phone, web form, or marketplace (HireAHelper, Yelp, Angi), requires an in-home or virtual survey before quoting, involves complex quote structures (binding, non-binding, not-to-exceed, hourly vs. flat rate), and needs crew/truck assignment that changes daily. Most companies use Salesforce, HubSpot, or a spreadsheet, then duct-tape survey scheduling through Calendly, quoting through Word templates, and payment through Square or Stripe — none of which talk to each other.

## What Already Exists
General-purpose CRMs (HubSpot, Jobber, ServiceTitan) handle lead capture and invoicing but have no concept of a "move" as a structured object with origin/destination addresses, cube sheet, access conditions, special items, valuation coverage selection, and binding estimate regulations. SmartMoving is the closest vertical solution but its lead management is rigid, its quote templates don't handle interstate regulatory requirements cleanly, and its UX was designed in 2015.

## The Customisation Gap
The CRM needs to treat each move as a multi-phase project: lead qualification (move size, distance, date flexibility), survey scheduling with automatic slot management, quote generation that understands FMCSA binding estimate rules for interstate moves and state-level requirements for intrastate, deposit and payment milestones tied to move phases, and automated follow-up sequences that reference specific move details (e.g., "Your 3-bedroom move from Austin to Denver on June 14th"). An LLM layer could draft personalized follow-up emails and handle inbound customer questions about packing, insurance, and timing by referencing the specific move record.

## Impact If Solved
Reduces the lead-to-booking conversion cycle from 5-7 days to 1-2 days for local moves. Eliminates 3-5 hours per week of manual data re-entry between survey notes, quote documents, and scheduling calendars for a typical sales coordinator.
