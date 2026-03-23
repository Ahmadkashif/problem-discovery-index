# Prerequisite Skill Graph for Math Diagnosis

**Niche:** [[niches/tutoring-centers/math-specialty-franchises/profile|Math Specialty Franchises]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A visual prerequisite knowledge graph that shows exactly where a student's math understanding breaks down — tracing errors on current-grade material back to the specific prerequisite skill gap 2-3 grade levels below, so the tutor fixes the root cause instead of re-teaching the surface topic.
**Tags:** #bayesian-network #multiclass-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A 7th grader struggles with proportional reasoning. The surface diagnosis is "needs help with ratios." An experienced tutor probes deeper: the student can set up proportions correctly but consistently errors when cross-multiplying with fractions — revealing a 5th-grade fraction multiplication gap. A different student with the same surface symptom makes different errors: they can multiply fractions but don't understand the concept of equivalent ratios — a 6th-grade conceptual gap. These students need different remediation paths. New tutors (and franchise worksheet systems) treat both as "needs more ratio practice," missing the root cause and wasting weeks on ineffective remediation.

## Why Nobody Has Built This
Math prerequisite dependency graphs are well-documented in learning science literature (Common Core standards define prerequisite chains explicitly), but translating them into a diagnostic assessment tool requires: (1) structuring assessments to probe prerequisite skills, not just current-grade skills; (2) building a Bayesian inference model that identifies the most likely root-cause gap from observable error patterns; (3) training the model on expert tutor diagnostic reasoning, which is tacit — experts disagree on root cause 25% of the time. Franchise systems have curriculum sequences but not diagnostic graphs — they advance students linearly through content rather than diagnosing and targeting specific prerequisite gaps.

## What to Build
A K-12 math prerequisite knowledge graph with 200-300 specific skill nodes, each connected to its prerequisite skills. When a student takes a diagnostic assessment, a Bayesian inference engine traces errors backward through the prerequisite chain to identify the deepest-level gap with highest probability. Output: a visual knowledge map showing green (mastered), yellow (partially mastered), and red (missing) skills, with the recommended remediation starting point highlighted. Tutors see: "This student's algebra struggles trace back to fraction operations — start remediation at multiplying fractions (5th grade), not proportional reasoning (7th grade)."

## Target Customer
Franchise owners and center directors at math tutoring centers with 50+ active students who want diagnostic accuracy comparable to their best tutor — available to every tutor on every shift.

## Impact If Built
Reduces average remediation time per student by 30-40% by targeting root-cause gaps instead of surface symptoms. Makes every tutor diagnostically effective from their first week — eliminating the 3-6 month ramp-up during which new tutors provide suboptimal diagnosis. Increases student retention by accelerating visible progress — the primary driver of parent satisfaction and continued enrollment.
