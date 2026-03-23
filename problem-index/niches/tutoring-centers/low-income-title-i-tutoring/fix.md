# Tutor-Student Assignment Optimization at Scale

**Niche:** [[niches/tutoring-centers/low-income-title-i-tutoring/profile|Low-Income / Title I Tutoring Providers]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Fix (Pain Point)
**One-liner:** High-dosage tutoring programs assign 500-5,000 students to tutors using spreadsheet-based matching — ignoring subject expertise alignment, student-tutor continuity, and schedule feasibility, producing poor matches that reduce tutoring effectiveness.
**Tags:** #gradient-boosting #recommendation #tabular-ml #automation #worker-facing

## The Problem
A high-dosage tutoring program serving 2,000 students across 15 schools must assign each student to a tutor for 3 sessions per week. Constraints include: tutor subject expertise (math vs. reading vs. both), school location (tutors travel to schools), student schedule availability (pull-out during which class period), group size limits (1:3 or 1:4 ratios), student-tutor continuity (keeping the same pairing for the semester), and tutor capacity (hours per week). The program coordinator solves this manually in a spreadsheet — a constraint satisfaction problem that takes 2-3 weeks at the start of each semester and produces suboptimal assignments because the coordinator optimizes sequentially (school by school) rather than globally.

## Why It's Still Broken
Generic scheduling optimization tools don't model the specific constraints of school-based tutoring: class period schedules, pull-out coordination with teachers, multi-school tutor routing, small-group formation by skill level, and the research-backed requirement for student-tutor continuity. High-dosage tutoring is a recent phenomenon (scaled dramatically post-2020), so the market is young and the operational tooling hasn't caught up. Many program coordinators are former teachers without technical backgrounds, so they default to familiar tools (spreadsheets) even for problems that are clearly beyond spreadsheet capability.

## What a Fix Looks Like
A constraint-based assignment optimization system that: (1) ingests the student roster (school, grade, subject need, schedule, skill level), tutor roster (availability, subject expertise, school assignments, capacity), and program constraints (ratio limits, continuity requirements, dosage targets); (2) generates globally optimal tutor-student assignments that maximize subject-expertise match, maintain student-tutor continuity, and minimize tutor travel between schools; (3) handles mid-semester changes (new students, tutor departures, schedule modifications) by reoptimizing incrementally rather than from scratch; (4) produces printable schedules for each school site and each tutor.

## Who Feels the Pain
Program coordinators who spend 2-3 weeks at the start of each semester building assignments in spreadsheets, then spend 2-3 hours per week managing changes and substitutions, and tutors who are assigned students outside their subject expertise or travel unnecessarily between schools.

## Impact If Fixed
Reduces semester-start assignment from 2-3 weeks to 1-2 days. Improves subject-expertise match rate from 60-70% (spreadsheet-constrained) to 85-95% (optimized), directly improving tutoring effectiveness. Eliminates tutor burnout from unnecessary travel by optimizing school assignments. Handles mid-semester changes in minutes instead of hours.
