# Project Scheduling & Management

**Parent Industry:** [[industries/general-contractors|General Contractors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $5-8B (embedded across all GC segments as a business function)
**Share of Parent Industry:** Touches all segments — scheduling and daily management are universal
**Digital Adoption:** Medium — CPM scheduling software (Microsoft Project, Primavera) is used for large projects but most GCs schedule through experience and spreadsheets; daily reporting is largely manual
**Target Buyer:** Project manager, superintendent, or GC owner managing active construction projects
**Automation Potential:** Very High — schedule delay prediction, weather impact modeling, and daily report generation are all data-rich problems with clear automation targets

## What Makes This a Distinct Niche
Project scheduling in construction is uniquely challenging because the schedule is a living document that changes daily based on weather, subcontractor performance, material delivery, inspections, and change orders. A CPM (Critical Path Method) schedule is created at project start and immediately begins degrading — the schedule says drywall starts Monday but the framing crew fell behind by 3 days, which pushes drywall to Thursday, which pushes painting to the following Monday, which puts the move-in date at risk. Experienced superintendents can mentally model these delay cascades — they know that a 2-day framing delay actually creates a 5-day project delay because the drywall crew can't mobilize mid-week and the painter needs a 3-day lead time for material delivery. Junior PMs can't do this — they update the schedule line by line without understanding the cascading consequences. Meanwhile, superintendents spend 30-45 minutes daily on field reports that are administratively necessary but operationally painful — describing what happened today, what's planned tomorrow, and what's blocking progress.

## Current Tools & Gaps
Microsoft Project and Oracle Primavera P6 handle CPM scheduling but are complex, expensive, and static — they show the plan but don't model what happens when the plan changes. Procore has scheduling features but focuses on schedule-as-documentation rather than schedule-as-prediction. No tool takes real-time field data (daily reports, weather forecasts, sub performance history) and predicts schedule impact: "Based on the rain forecast for Tuesday-Wednesday and the current framing pace, the project completion date has shifted from April 15 to April 22." Daily reporting tools (Raken, Fieldlens) capture field data but don't connect it to schedule analysis. The superintendent writes the daily report and separately updates the schedule — two disconnected tasks that should inform each other.

## Problems
- [[niches/general-contractors/project-scheduling-management/build|🔨 Build: Schedule Delay Cascade Predictor]]
- [[niches/general-contractors/project-scheduling-management/buy|🛒 Buy: Predictive Scheduling with Weather & Sub Performance]]
- [[niches/general-contractors/project-scheduling-management/fix|🔧 Fix: Daily Report Automation]]
