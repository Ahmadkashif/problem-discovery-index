# Predictive Scheduling with Weather & Sub Performance

**Niche:** [[niches/general-contractors/project-scheduling-management/profile|Project Scheduling & Management]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Microsoft Project and Primavera calculate schedules from fixed predecessor logic — but real construction schedules are driven by weather forecasts, sub availability, and inspector schedules that no static CPM tool integrates.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #data-integration #workflow-orchestration

## The Problem
A superintendent builds a CPM schedule showing concrete pour on March 10, but the 10-day weather forecast shows rain March 8-12. The superintendent mentally adjusts: concrete moves to March 13, which pushes framing to March 18 (because the framing crew needs the slab to cure for 3 days minimum in March temperatures), which pushes everything downstream. This mental adjustment happens weekly — every weather event, every sub delay, every inspector availability change triggers a cascade recalculation that the superintendent performs in their head and communicates through phone calls. The formal schedule in MS Project or Primavera is updated weekly or biweekly and is always 3-10 days behind reality. The project owner and construction manager see the stale schedule and make decisions based on outdated information.

## What Already Exists
Microsoft Project and Primavera P6 are the standard CPM scheduling tools, capable of modeling complex predecessor/successor logic, float calculations, and resource leveling. But they're static models — the schedule reflects the plan at the time it was last updated, not current reality. Procore integrates scheduling with daily logs and RFIs but doesn't predict impact. ALICE Technologies offers AI scheduling for large infrastructure but targets $100M+ projects with dedicated planning teams, not the $1-50M GC market. Weather services (Weather.com, OpenWeather) provide forecasts but don't integrate with construction schedules. No tool connects the three data streams (schedule, weather, sub performance) that drive actual project timing.

## The Customization Gap
A predictive scheduling layer would extend existing CPM tools with: (1) weather overlay — connecting activity weather sensitivity tags (exterior work can't happen in rain, concrete can't pour below 35F, roofing can't install above 35mph wind) to rolling weather forecasts, automatically flagging and rescheduling affected activities; (2) sub performance profiles — learning from daily reports and past projects how each subcontractor actually performs versus their committed schedule (the electrician is typically 1.5 days late on rough-in), and incorporating that variance into the forward schedule; (3) inspector availability integration — connecting to building department scheduling systems (or manual input of available inspection dates) to replace the schedule's assumption of "inspection happens next day" with actual lead times. These three data integrations transform a static plan into a living forecast.

## Target Customer
Superintendents and project managers at GCs ($5M-$100M annual revenue) who maintain CPM schedules in MS Project or Primavera but update them infrequently because the update process doesn't incorporate real-world variables (weather, sub performance, inspector availability).

## Impact If Solved
Transforms the project schedule from a stale planning document into a real-time forecasting tool, providing all stakeholders with accurate completion projections. Reduces schedule update effort from 2-4 hours per week (manual CPM adjustment) to near-zero by auto-incorporating field data. Enables proactive risk management — the superintendent sees next week's weather impact on the schedule before it happens, not after.
