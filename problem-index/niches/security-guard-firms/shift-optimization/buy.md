# Automated Callout Backfill System

**Niche:** [[niches/security-guard-firms/shift-optimization/profile|Guard Scheduling & Shift Optimization]]
**Industry:** [[industries/security-guard-firms|Security Guard Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Shift marketplace apps let workers pick up open shifts, but they don't filter by security-specific qualifications, site training requirements, or labor law constraints.
**Tags:** #automation #workflow-orchestration #worker-facing

## The Problem
Guard callouts happen 5-15 times per week at a mid-size security company. Each callout triggers a manual phone tree: the operations manager checks who's available, qualified for the site, not in overtime, and rested enough for the shift. They start calling guards at 10pm, working down the list until someone accepts. This process takes 30-90 minutes per callout and fails 10-20% of the time (no replacement found, shift goes uncovered). The operations manager's personal phone becomes the callout hotline, burning them out.

## What Already Exists
Shift marketplace apps (ShiftKey, InstaWork, Wonolo) connect workers with open shifts. Workforce management platforms (Deputy, When I Work) allow open shift broadcasting. Neither filters by security guard licensing (active guard card), site-specific training completion, armed/unarmed qualification, overtime status, or rest period compliance. Broadcasting an open shift to all guards — including those who aren't qualified, are in overtime, or haven't completed site orientation — wastes everyone's time.

## The Customization Gap
The backfill system needs security-specific logic: when a callout is reported, automatically identify all guards who (1) hold valid guard cards, (2) are qualified for that site's requirements, (3) haven't exceeded weekly overtime thresholds, (4) meet rest period requirements, and (5) are available. Send the open shift to qualified guards in priority order (closest to site, lowest overtime, highest reliability score). Auto-confirm the first acceptance and update the schedule. If no guard accepts within the time window, escalate to the supervisor.

## Target Customer
Security operations managers handling 5+ callouts per week who spend 5-10 hours weekly on phone-tree backfill and still can't cover 10-15% of callout shifts.

## Impact If Solved
Reduces callout backfill time from 60 minutes to 5 minutes per event, improves fill rate from 85% to 97%, eliminates the operations manager's midnight phone-tree burden, and ensures every replacement meets site qualification requirements.
