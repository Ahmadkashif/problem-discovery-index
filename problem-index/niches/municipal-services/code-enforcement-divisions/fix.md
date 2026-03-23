# Missed Follow-Up Deadlines and Abandoned Cases

**Niche:** [[niches/municipal-services/code-enforcement-divisions/profile|Code Enforcement Divisions]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Fix (Pain Point)
**One-liner:** Officers track re-inspection dates in their heads or on handwritten calendars, resulting in 20–30% of cases going dormant because nobody followed up.
**Tags:** #workflow-orchestration #compliance #worker-facing #quick-win

## The Problem
Every code enforcement case has a legally prescribed timeline: after a violation notice is issued, the property owner has a specified period (typically 10–30 days) to come into compliance. If they don't, the officer must re-inspect and escalate — issue a citation, schedule a hearing, or file a lien. In practice, officers managing 50–200 simultaneous cases lose track of which properties are due for re-inspection. Cases go dormant for months. Property owners learn that violations have no consequences, which undermines the entire enforcement program. When residents complain that "nothing ever happens," they're describing this specific failure mode.

## Why It's Still Broken
Officers resist digital tools that feel like micromanagement. Paper-based reminder systems (sticky notes, desk calendars) don't scale past 20 active cases. Supervisors lack visibility into case pipelines and only discover abandoned cases when a citizen complains about the same property again. The few departments that have tried Outlook calendar reminders found them inadequate because a reminder doesn't include case context — the officer has to look up the file, find the photos, remember the history. There's no system that bundles the reminder with the case record and the required next action.

## What a Fix Looks Like
A simple case dashboard (web + mobile) that shows every officer their active cases sorted by next-action-due date, with red/yellow/green status based on how close the deadline is. Clicking a case shows the full history: original complaint, photos, notices sent, and the specific next step required (re-inspect, escalate, close). Automated text/email reminders fire 3 days and 1 day before each deadline. Supervisors see a department-wide view with dormant-case alerts. No complex setup — import existing cases from a CSV, start using it today.

## Who Feels the Pain
Code enforcement officers who feel overwhelmed by caseloads they can't track, and supervisors who take political heat when visible violations persist for months.

## Impact If Fixed
Reducing abandoned cases from 25% to 5% increases effective enforcement capacity by 20% without hiring. Average case resolution drops from 6 months to 2.5 months. Citizen satisfaction scores for code enforcement improve by 30–40 points in annual surveys.
