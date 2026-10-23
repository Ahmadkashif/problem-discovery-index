# Everything Raised as Priority 1

**Niche:** [[niches/facilities-management-firms/service-desk-intake-dispatch/profile|Service Desk Intake & Dispatch]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Occupants learn that "urgent" gets a faster response, coordinators err on the side of caution, and the priority-1 queue fills with routine work.
**Tags:** #bert #large-language-models #evaluation-metrics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a vague occupant request into a correctly classified, prioritised and dispatched work order inside the SLA response clock, and whoever gets dispatch right the first time without a human triager takes the account.

## The Problem
When a large share of tickets arrive flagged as emergencies, technicians are pulled off planned work for jobs that could wait, true emergencies queue behind false ones, and the response-time KPI is missed on tickets that never needed a four-hour response.

## Why It's Still Broken
Downgrading a priority puts the coordinator at risk if they are wrong, while upgrading costs them nothing. Contract priority definitions are prose, and nobody measures how often the assigned priority turns out to be wrong.

## What a Fix Looks Like
Score each ticket's priority from its text and the asset's criticality, show the coordinator the suggested priority with the contract definition it rests on, and measure reclassification afterwards: what the technician found against what was raised. Report false emergencies by requester and site, so the client can address the habit at its source.

## Who Feels the Pain
Coordinators, technicians pulled off planned maintenance, and facility managers explaining response misses on tickets that were never urgent.

## Impact If Fixed
The emergency queue holds emergencies, planned work gets done, and response KPIs measure what they were meant to.
