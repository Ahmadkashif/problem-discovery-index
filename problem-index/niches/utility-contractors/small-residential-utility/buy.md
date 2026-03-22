# Small Contractor Tools Adapted for Utility Work

**Niche:** [[niches/utility-contractors/small-residential-utility/profile|Small Residential Utility]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Jobber and ServiceTitan handle scheduling and invoicing for small service businesses but don't understand utility construction workflows — permit tracking, 811 locate coordination, utility inspection scheduling, and meter set coordination are all managed outside the platform through phone calls.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
Small utility contractors try Jobber or ServiceTitan because they need scheduling and invoicing, but these tools treat every job as a single-visit service call. A utility connection is a multi-day, multi-visit project with dependencies: you can't construct until you have the locate and the permit; you can't backfill until you pass inspection; you can't invoice final payment until the meter is set. Jobber's job model doesn't support this workflow — the contractor creates the "job" but manages the 8-12 intermediate steps outside the platform.

## What Already Exists
Jobber handles scheduling, dispatching, quoting, and invoicing for field service businesses. ServiceTitan handles the same with more sophistication. Both support multi-visit jobs and custom fields. Neither has utility-specific workflow templates.

## The Customization Gap
A utility construction workflow template for Jobber/ServiceTitan that: (1) structures each service connection as a multi-phase project with dependent milestones (permit → locate → pre-construction → construct → inspect → meter set); (2) includes utility-specific checklist items at each phase — 811 ticket number, permit number, utility specification document, inspection results; (3) automates scheduling dependencies — when the locate is marked complete, auto-schedule the construction date based on crew availability; (4) tracks permit expiration and 811 locate validity windows (locates expire after 10-30 days depending on state); and (5) generates utility-specific invoicing — some contracts are fixed-price, others are time-and-materials with utility-specified rates.

## Target Customer
Small utility contractors (3-15 employees) currently using Jobber or ServiceTitan for their scheduling and invoicing but managing utility-specific workflows manually. Jobber/ServiceTitan as platforms seeking to serve the utility contractor segment.

## Impact If Solved
Brings utility-specific workflow management into the tool the contractor already uses for scheduling and invoicing, eliminating the parallel manual tracking system. Reduces missed steps (expired locates, expired permits) by 50-70% through automated tracking. Saves 5-10 hours per week for the contractor's office manager in coordination management.
