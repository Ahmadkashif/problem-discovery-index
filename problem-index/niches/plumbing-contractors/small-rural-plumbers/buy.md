# Lightweight FSM with Well Pump and Septic System Templates

**Niche:** [[niches/plumbing-contractors/small-rural-plumbers/profile|Small & Rural Plumbers]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Jobber and Housecall Pro handle scheduling and invoicing for field service businesses but know nothing about well pumps, septic systems, or agricultural plumbing — a rural-plumbing template layer on top of an existing FSM would make these tools useful for the 80,000+ small rural plumbing shops that currently use paper.
**Tags:** #data-integration #workflow-orchestration #quick-win #worker-facing

## The Problem
Lightweight FSM platforms like Jobber ($50-100/month) and Housecall Pro ($65-130/month) are priced right for solo plumbers but are industry-agnostic — they handle scheduling, quoting, invoicing, and payment processing for any field service business. They have no concept of plumbing-specific workflows, let alone rural plumbing specialties. When a rural plumber creates a job in Jobber for "well pump replacement," the system treats it identically to "install ceiling fan" — no prompts for well depth, pump specifications, pressure tank details, or wire sizing. The plumber gets generic scheduling and invoicing but zero workflow support for the technical aspects of their work. The result: plumbers either don't use FSM tools (too generic to be worth the time) or use them only for invoicing, ignoring the scheduling and job management features.

## What Already Exists
Jobber and Housecall Pro provide scheduling, dispatching, quoting, invoicing, and payment processing. Both have API access and template customization. Jobber's "forms" feature allows custom fields on jobs, but creating a well pump replacement form with the right fields (well depth, casing diameter, pump HP, wire gauge, pressure tank size, static water level) requires the plumber to build it from scratch — which they won't do.

## The Customization Gap
The gap is pre-built job templates for common rural plumbing tasks, integrated into an existing FSM platform via API or native plugin: (1) well pump replacement template (captures well depth, pump specs, pressure tank size, wire gauge, generates a pump specification sheet for the customer), (2) septic system inspection template (captures tank condition, scum/sludge measurements, drain field status, generates jurisdiction-appropriate inspection report), (3) water heater installation template (captures fuel type, capacity, venting requirements, generates warranty registration checklist), (4) gas line installation template (captures BTU load, pipe run, sizing calculation, generates pressure test documentation). Each template auto-populates the invoice with appropriate line items and generates customer-facing documentation. Built as a Jobber or Housecall Pro marketplace app, priced at $19-29/month on top of the FSM subscription.

## Target Customer
Solo and two-person rural plumbing shops who tried Jobber or Housecall Pro and abandoned it because the generic interface added work without reducing it, or who never adopted FSM software because it didn't speak their language.

## Impact If Solved
Converts 30-40% of rural plumbers who currently use paper-based systems into FSM users by making the tool immediately useful for their specific job types. Reduces job documentation time by 50-70% through pre-built templates that capture the right data with minimal typing. Generates professional customer-facing reports (well pump specs, septic inspection results) that increase customer trust and justify premium pricing in rural markets where competition is minimal.
