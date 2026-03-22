# Selection Deadline Management

**Niche:** [[niches/general-contractors/residential-custom-home/profile|Residential Custom Home Builders]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Builders stop losing weeks on the schedule because clients missed tile or cabinet selection deadlines that were buried in a spreadsheet nobody checked.
**Tags:** #decision-trees #feature-engineering #automation #workflow-orchestration #worker-facing

## The Problem
Custom home clients must make finish selections — tile, countertops, fixtures, cabinetry, flooring, hardware, lighting, appliances — by specific dates tied to the construction schedule. If bathroom tile isn't selected by week 8, the tile order can't ship in time for installation at week 14, which delays the plumber, which delays drywall, which pushes the entire completion date. Builders currently track these deadlines in spreadsheets or their own memory. Clients don't see the deadlines until the builder calls them in a panic. The result: 70-80% of custom home schedule delays are client-caused, primarily from late selections.

## Why It's Still Broken
Buildertrend and CoConstruct show clients their selection options but don't enforce or even prominently display deadlines. The deadline logic is construction-specific — it requires understanding that a tile selection has a 4-6 week lead time, so the selection deadline is derived backward from the installation date on the schedule. No client-facing tool performs this backward calculation automatically. Builders set these deadlines manually based on experience, and the deadlines shift as the schedule shifts — but nobody updates the selection deadline spreadsheet when the framing schedule moves by two weeks.

## What a Fix Looks Like
A selection deadline engine that derives client decision deadlines from the construction schedule and material lead times. When the schedule shows tile installation at week 14 and the tile supplier quotes a 5-week lead time plus 1-week buffer, the system sets a client selection deadline at week 8 and sends escalating reminders at 14 days, 7 days, 3 days, and on the deadline date. When the construction schedule shifts, all downstream selection deadlines recalculate automatically. The client sees a single dashboard: "You have 3 selections due this week, 5 due in the next two weeks" with direct links to make each selection. The builder sees which clients are at risk of causing delays before it happens.

## Who Feels the Pain
Project coordinators and superintendents who chase clients for selections while simultaneously managing subcontractor schedules. They spend 3-5 hours per week on selection follow-up calls and emails. When a client is late, the superintendent must re-sequence trades on the jobsite — a stressful, time-consuming coordination task that ripples across multiple subcontractors.

## Impact If Fixed
Reduces client-caused schedule delays by 40-60%, recovering 2-4 weeks on the average custom home build timeline. Eliminates 3-5 hours per week of manual selection follow-up per active project. Prevents the cascading subcontractor re-scheduling that occurs when selections arrive late and trades must be resequenced.
