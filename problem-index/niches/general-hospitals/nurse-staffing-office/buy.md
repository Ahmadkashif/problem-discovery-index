# Ride-Hailing Dispatch Adapted to the Float Pool

**Niche:** [[niches/general-hospitals/nurse-staffing-office/profile|Nurse Staffing Office & Contingent Labour]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Gig marketplaces match supply to demand in minutes with dynamic incentives; a hospital float pool is a closed gig marketplace with licences, competencies and fatigue rules.
**Tags:** #optimization-fundamentals #gradient-boosting #evaluation-metrics #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to fill tomorrow's open shifts from the hospital's own nurses before agency and travel staff are called, and whoever covers the most shifts at core rates without breaching ratios takes the account.

## The Problem
Float pools and per-diem nurses are the hospital's flexible supply, but they are dispatched by phone tree and group text, often hours late.

## What Already Exists
Ride-hailing and delivery dispatch match workers to jobs with surge pricing and acceptance prediction. External per-diem marketplaces apply the model to nurses outside the hospital (that field is described at [[niches/skilled-nursing-facilities/per-diem-shift-marketplaces/profile|Per-Diem Shift Marketplaces & Agency Labour]]), and some hospitals run internal versions.

## The Customization Gap
Hospital adaptation needs:

- matching on licence, unit competency, orientation status and float eligibility, not just availability;
- fatigue limits and union seniority rules as hard constraints;
- ratio and skill-mix requirements per unit and shift;
- integration with the timekeeping system so incentive pay is paid correctly;
- an audit trail for regulators and labour relations.

## Target Customer
Staffing offices at systems with internal float pools of 50+ nurses.

## Impact If Solved
Faster, constraint-aware dispatch fills shifts ~2–4 hours earlier (estimate), before the escalation to agency is triggered. Each shift kept internal saves the gap between core pay and travel rates that average $91 an hour (NSI 2026).
