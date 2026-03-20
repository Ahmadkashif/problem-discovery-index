# Intelligent Visit Scheduling and Route Optimization

**Industry:** [[home-health-agencies|Home Health Agencies]]
**Type:** High Impact
**One-liner:** Field clinicians are automatically routed through optimized daily schedules that balance patient acuity, visit windows, clinician skills, and drive time — eliminating the scheduling coordinator bottleneck that currently burns 3-4 hours of manual puzzle-solving every morning.
**Tags:** #optimization-fundamentals #gradient-descent #convex-optimization #numerical-methods #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact #ai-agent

## The Problem
Home health scheduling coordinators build daily visit schedules for 20-80 field clinicians across a geographic territory, matching each patient's ordered visit frequency, clinician certification requirements (wound care, IV therapy, pediatric), continuity-of-care preferences (patients do better with the same nurse), payer-mandated visit windows, and real-time disruptions (patient cancellations, clinician call-outs, hospital admissions). Most do this manually using the EHR's basic calendar view supplemented by spreadsheets and institutional knowledge. The result: suboptimal routes that waste 60-90 minutes of drive time per clinician per day, missed visits that trigger compliance violations, and coordinators who are the single point of failure for the entire operation.

## Why It's Unsolved
The constraint space is enormous — it's a multi-variable optimization problem that changes daily with cancellations, new admissions, and call-outs. Off-the-shelf route optimization tools (built for delivery trucks) don't understand clinical constraints: you can't send an LPN to do a skilled nursing assessment, you can't split a wound care visit across two nurses, and Medicare requires specific visit patterns tied to the plan of care. Home health EHR vendors have attempted scheduling optimization but struggle with real-time re-optimization when the day's plan breaks down at 10am.

## What a Solution Looks Like
A scheduling engine that ingests the patient census (with acuity, visit orders, location, payer rules), clinician roster (with certifications, availability, location), and produces an optimized daily schedule with turn-by-turn routing. When disruptions occur, it re-optimizes in real-time, suggesting reassignments with the least impact on patient care continuity and compliance. Inputs: EHR patient/clinician data, GPS, payer rules. Outputs: optimized daily routes pushed to clinician mobile devices.

## Impact If Solved
Reduces clinician windshield time by 30-45 minutes per day (across a 50-clinician agency, that's 40+ additional patient visits per day). Eliminates 2-3 FTE scheduling coordinator positions or redeploys them to patient-facing work. Cuts missed-visit compliance violations by 60-80%.
