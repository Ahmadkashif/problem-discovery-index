# Instructor Assessment Inconsistency Across Evaluators

**Niche:** [[niches/vocational-schools/welding-programs/profile|Welding & Skilled Trades Programs]]
**Industry:** [[industries/vocational-schools|Vocational Schools]]
**Type:** Fix (Pain Point)
**One-liner:** Two instructors grading the same weld coupon give different scores — and neither knows it — creating unreliable competency records that undermine accreditation, employer trust, and student progression decisions.
**Tags:** #cnn #multiclass-classification #computer-vision #tacit-knowledge-ml #compliance

## The Problem
Inter-rater reliability among welding instructors is typically 0.60-0.75 (Cohen's kappa), meaning two instructors evaluating the same student's work disagree on quality assessment 25-40% of the time. Students in the morning section may pass with work that would fail in the afternoon section under a different instructor. This inconsistency compounds across a program — a student assessed as "job-ready" by one instructor may not meet employer expectations, damaging the school's placement outcomes and reputation.

## Why It's Still Broken
Calibration sessions — where instructors jointly evaluate sample work to align their standards — are expensive (consuming 4-8 hours of multiple instructors' time) and their effects decay within weeks as individual bias reasserts. No permanent artifact of "what a passing weld looks like at this school" exists; the standard lives in each instructor's head and shifts with their mood, fatigue, and personal style. Schools have no measurement of the inconsistency itself — they don't know the kappa between their instructors because no system captures structured assessment data from multiple evaluators on the same work.

## What a Fix Looks Like
A structured digital assessment workflow where each instructor scores welds against the same rubric dimensions in a tablet-based interface, with periodic calibration checks where the same weld image is presented to multiple instructors. The system computes inter-rater agreement metrics by instructor pair and dimension, identifies specific areas of divergence (e.g., "Instructors A and B agree on bead width but disagree on porosity severity"), and triggers targeted calibration when agreement drops below threshold. Over time, the accumulated scored images create a visual reference library of "what each score looks like" — anchoring subjective assessment to concrete examples.

## Who Feels the Pain
Students who receive inconsistent evaluations that don't reflect their actual skill level, and program directors who discover assessment inconsistency only when accreditors audit competency documentation or when employer feedback reveals graduates with uneven preparation.

## Impact If Fixed
Improves inter-rater reliability from 0.60-0.75 to 0.80+ kappa, reducing student grievances over perceived unfair grading by 30-50%. Strengthens accreditation self-study evidence with documented assessment consistency metrics. Reduces employer complaints about graduate skill variability by establishing a verifiable, consistent competency standard.
