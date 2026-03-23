# Tutor Diagnostic Consistency Across Sessions

**Niche:** [[niches/tutoring-centers/math-specialty-franchises/profile|Math Specialty Franchises]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Fix (Pain Point)
**One-liner:** A student sees Tutor A on Monday and Tutor B on Thursday — each diagnoses a different root cause for the same math struggles, pulling the student in two remediation directions simultaneously and wasting both sessions.
**Tags:** #data-integration #workflow-orchestration #worker-facing #tacit-knowledge-ml

## The Problem
Math tutoring centers schedule students with multiple tutors due to availability constraints and tutor scheduling. A student struggling with algebra sees Tutor A on Monday, who identifies a fraction gap and assigns fraction remediation. On Thursday, the student sees Tutor B, who didn't read Tutor A's notes (or they weren't recorded), assesses the student independently, identifies an order-of-operations gap, and starts a different remediation path. The student spends a week receiving contradictory instruction. Parents notice ("last time they said it was fractions, now they're saying it's something else") and lose confidence. This diagnostic inconsistency is invisible to center directors unless a parent complains.

## Why It's Still Broken
Tutoring centers lack a shared diagnostic model per student. Session notes — when they exist — are free-text descriptions that subsequent tutors either don't read or interpret differently. No system captures the diagnostic reasoning (what was tested, what errors were observed, what root cause was identified) in a structured format that transfers between tutors. Franchise curriculum systems track what worksheet the student is on but not why they're on it — losing the diagnostic context that informed the assignment. The problem compounds with tutor turnover: when a tutor who diagnosed a student leaves, their diagnostic reasoning is completely lost.

## What a Fix Looks Like
A structured student diagnostic profile that every tutor reviews before each session and updates after: (1) current diagnosis — the identified root-cause skill gap and the reasoning behind it (what error patterns were observed, what was tested and ruled out); (2) current remediation plan — what skill is being targeted and what progress has been made; (3) session-by-session log of assessment observations in structured format (skill tested, accuracy, error type, next step); (4) alerts when a new tutor's session observations contradict the current diagnosis — triggering a re-diagnostic discussion rather than a silent plan change. All tutors working with a student operate from the same diagnostic profile, maintaining remediation continuity regardless of scheduling.

## Who Feels the Pain
Students who receive inconsistent instruction from different tutors, parents who lose confidence when tutoring direction changes without explanation, and center directors who discover diagnostic inconsistency only through parent complaints.

## Impact If Fixed
Eliminates wasted sessions from contradictory remediation directions — estimated at 10-15% of total session hours in multi-tutor centers. Increases parent confidence by demonstrating a consistent, documented approach across all tutors. Preserves diagnostic continuity through tutor turnover — the student's diagnostic profile survives even when the tutor who created it leaves.
