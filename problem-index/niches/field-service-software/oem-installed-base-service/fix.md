# The Field Failure Engineering Never Hears About

**Niche:** [[niches/field-service-software/oem-installed-base-service/profile|OEM Service on Its Own Installed Base]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** A manufacturer's technicians see every way its machines fail in the field, record it as a parts line on a work order, and the engineers designing the next model never learn anything from it.
**Tags:** #bert #large-language-models #descriptive-statistics #evaluation-metrics #hypothesis-testing #change-point-detection #compliance #worker-facing
**Contested on:** Every serious competitor in OEM service software is fighting to convert telemetry and engineering knowledge from the manufacturer's own installed base into a dispatched action before the customer notices a fault — and whoever converts most reliably takes the account.

## The Problem
A technician finds the same fitting cracked on the same model for the eleventh time this year. He replaces it, closes the work order with a part number and a short note, and drives to the next call. He has told his supervisor twice. Nobody in engineering knows, because the route from a field observation to a design review is a person deciding to escalate, and the work order system's free-text note field is read by nobody. The manufacturer's most valuable feedback loop — millions of hours of its own product observed failing in real conditions — terminates in a parts consumption report.

## Why It's Still Broken
Work order text is written for billing and for the next technician, not for analysis, so it is brief and inconsistent. Warranty analytics, where it exists, reads claims rather than field notes and covers only the warranty period, which excludes most of a machine's life. And organisationally, service and engineering report into different structures with different metrics, so nobody is accountable for the flow between them. The escalation path that exists depends on an individual technician deciding something is worth the effort of reporting, which selects for the dramatic rather than the frequent.

## What a Fix Looks Like
Read the work orders and count. Classify field notes and parts consumption into failure modes per model and per component, which is ordinary text work on data the manufacturer already holds in volume, and watch for rate changes — a failure mode rising in a model year, or concentrated in a production batch, or appearing in one climate. Route confirmed patterns into the quality and engineering process automatically with the evidence and the affected population attached, rather than depending on escalation. Close the loop back to technicians, because the reason field reporting decays everywhere is that nothing visible happens; a technician who sees that their observation triggered a design change reports the next one. Give the same view to the reliability model in the build note, since confirmed failure modes are exactly the labels it needs.

## Who Feels the Pain
Technicians who have reported the same thing repeatedly and been thanked; engineers designing a successor model without knowing how the current one actually fails; and customers who buy the next generation with the same fitting in it.

## Impact If Fixed
Classifying field notes is inexpensive and typically surfaces failure modes that nobody in engineering had visibility of, several of them concentrated enough to be worth a design or supplier change. It also converts the technician's observation from an anecdote into evidence, which is both better engineering and a meaningful change in how the field workforce is treated.
