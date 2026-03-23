# Constraint-Optimized Tutoring Schedule Generator

**Niche:** [[niches/tutoring-centers/scheduling-enrollment-ops/profile|Scheduling & Enrollment Operations]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A schedule optimization engine that generates weekly tutoring schedules maximizing tutor-student subject match, room utilization, and skill-level grouping — replacing the 3-5 hours per week center directors spend manually juggling a constraint puzzle in spreadsheets.
**Tags:** #reinforcement-learning #recommendation #automation #workflow-orchestration

## The Problem
A center director with 80 students, 12 tutors, and 4 rooms spends 3-5 hours every Monday rebuilding the weekly schedule. Constraints: Tutor A can teach math and reading but only works Mon/Wed/Fri; Student B needs math tutoring Tue/Thu after 4pm; Room 3 is the only room with lab equipment for science; Students C, D, and E are all at the same math level and can share a small group session (better economics and learning outcomes) but Student C is only available on Tuesdays while D and E are available on Thursdays. The director solves this in a spreadsheet, optimizing sequentially (fill tutor slots one by one) rather than globally. The result is suboptimal: 30-40% of sessions have imperfect tutor-subject matches, small group potential is under-exploited, and one room sits empty while another is double-booked.

## Why Nobody Has Built This
Tutoring scheduling is a multi-objective constraint satisfaction problem with soft constraints (preferences) and hard constraints (availability). Generic scheduling platforms optimize for appointment booking (matching one person to one time slot), not multi-dimensional matching (person to group to room to subject to continuity). Building a tutoring-specific optimizer requires encoding domain-specific constraints that vary by center — each center has different room configurations, tutor specialties, and small group policies. The market (independent tutoring centers) is fragmented with low per-customer revenue potential, discouraging investment.

## What to Build
A constraint-based schedule optimizer that: (1) ingests tutor profiles (availability, subject expertise, group teaching capability), student profiles (subject needs, skill level, schedule preferences, continuity requirements), and room inventory (capacity, equipment); (2) generates an optimized weekly schedule maximizing subject-match quality, room utilization, and small group formation while respecting all hard constraints; (3) handles changes incrementally — when a student reschedules or a tutor calls out, the system re-optimizes the affected slots without disrupting the rest of the schedule; (4) provides a capacity projection showing how many additional students the center can accept before hitting scheduling constraints.

## Target Customer
Center directors at tutoring centers with 50+ active students and 8+ tutors who spend 3+ hours per week on manual schedule management and want to grow enrollment without hitting scheduling capacity limits.

## Impact If Built
Reduces weekly schedule management from 3-5 hours to 30 minutes. Improves tutor-subject match rate from 60-70% to 90%+. Increases small group session utilization by 30-50%, improving center economics (group sessions generate 2-3x the revenue per tutor-hour vs. individual sessions). Enables capacity growth of 20-30% without adding tutors or rooms by optimizing existing resource utilization.
