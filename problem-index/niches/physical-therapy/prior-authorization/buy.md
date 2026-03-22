# Proactive Authorization Management for PT EMRs

**Niche:** [[niches/physical-therapy/prior-authorization/profile|Prior Authorization & Concurrent Review]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PT EMRs get authorization intelligence that acts before authorization expires — not just static fields storing authorization numbers, but proactive alerting and workflow automation that prevents unauthorized visits.
**Tags:** #decision-trees #feature-engineering #evaluation-metrics #automation #compliance #workflow-orchestration

## The Problem
Every PT EMR has an "authorization" section in the patient record — fields for authorization number, approved visits, start date, end date. These are data entry fields, not intelligence. The EMR stores what the staff manually enters but doesn't calculate remaining visits dynamically (visit count changes with each completed session), doesn't alert when authorization is approaching expiration, doesn't flag when a patient is scheduled for a visit beyond their authorized quantity, and doesn't prompt the therapist to document information needed for an extension request before the extension is needed. The authorization module in current PT EMRs is a digital sticky note — it records information but doesn't act on it.

## What Already Exists
WebPT's authorization tracking stores authorization data and shows remaining visits in the patient record. Clinicient/Prompt has similar basic tracking. Some practice management add-ons (Raintree, Bestpt) include authorization alerts at the visit level. But none of these: (1) proactively alert staff 2-3 visits before authorization expires, (2) auto-calculate the optimal time to initiate an extension request based on visit frequency, (3) pre-populate extension request clinical narratives with data from the patient's treatment record, or (4) track extension request status through the approval workflow. Authorization management tools in medical billing (Infinitus, Olive AI) handle prior auth for medical procedures but don't understand PT-specific authorization patterns (10-12 visit cycles, concurrent review criteria, functional improvement requirements).

## The Customization Gap
The EMR already has the data needed — visit history, outcome scores, treatment plan goals, functional improvement trends. The gap is a proactive authorization logic layer that: (1) monitors each patient's visit count against their authorized quantity and alerts staff at a configurable threshold (e.g., 3 visits remaining), (2) blocks scheduling of visits beyond authorized quantity without staff override (preventing accidental unauthorized sessions), (3) triggers extension request workflows with pre-populated clinical data at the optimal time, (4) formats the clinical narrative to match payer-specific concurrent review criteria (EviCore wants different data than Cohere Health), and (5) tracks extension requests through submission, pending, approved, and denied states with automated follow-up reminders. This is PT-specific logic layered on existing EMR data — not a new system, but an intelligence layer that transforms passive data storage into proactive authorization management.

## Target Customer
PT clinic billing managers and front desk staff who currently manage authorization timing manually and want their EMR to handle the proactive aspects — alerting, workflow triggering, and clinical data pre-population — rather than just storing authorization numbers.

## Impact If Solved
Eliminates 80-90% of unauthorized visit occurrences by building proactive prevention into the scheduling and documentation workflow. Reduces staff time on authorization management by 5-8 hours per week per clinic by automating the manual calculation and monitoring that currently happens on spreadsheets. Reduces extension request denial rates by ensuring clinical documentation meets payer-specific criteria before submission.
