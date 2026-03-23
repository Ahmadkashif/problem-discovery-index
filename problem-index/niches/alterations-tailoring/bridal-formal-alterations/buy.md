# Multi-Fitting Scheduling System

**Niche:** [[niches/alterations-tailoring/bridal-formal-alterations/profile|Bridal & Formal Wear Alterations]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Appointment scheduling tools like Acuity and Calendly exist but don't model dependent multi-session fitting sequences where each appointment is contingent on construction work being completed between sessions.
**Tags:** #workflow-orchestration #automation #quick-win

## The Problem
A bridal gown alteration requires 2-4 fitting sessions spaced 2-4 weeks apart, with construction work between each. Fitting 2 can't be scheduled until the alterations from fitting 1 are complete. But brides book fitting 2 at the end of fitting 1, without knowing whether the seamstress will have the construction done in time. If the seamstress falls behind on other projects, fitting 2 must be rescheduled — bumping the entire timeline. There's no scheduling system that understands these dependencies and accounts for the seamstress's construction workload between fittings.

## What Already Exists
Acuity Scheduling, Calendly, and Square Appointments handle appointment booking with configurable availability. Vagaro and Boulevard offer salon/spa scheduling with multi-appointment services. But none model the concept of dependent sequential appointments with work-in-progress constraints: the second appointment can't happen until the work from the first appointment is complete, and the seamstress's capacity to complete that work depends on her other project load.

## The Customization Gap
The scheduling system needs to model fitting sequences (fitting 1 → construction period → fitting 2 → construction period → final fitting) with minimum intervals between fittings based on construction complexity. The seamstress's construction workload should factor into fitting availability — if she has 25 gowns in progress and 3 need major construction this week, she shouldn't offer fitting appointments for those gowns until the work is done. The system should auto-suggest the next fitting date based on construction estimate and current workload.

## Target Customer
Bridal seamstresses and alteration departments managing 10+ concurrent bridal projects where fitting rescheduling disrupts 20-30% of appointments, frustrating brides and creating timeline cascading.

## Impact If Solved
Reduces fitting rescheduling from 20-30% to under 5%, ensures construction work is complete before the bride arrives (eliminating the embarrassing "it's not ready yet" moment), and gives brides confidence in the timeline through visible, realistic scheduling.
