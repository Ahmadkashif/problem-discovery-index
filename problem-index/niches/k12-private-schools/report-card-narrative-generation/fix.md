# Narrative Quality Inconsistency Across Teachers

**Niche:** [[niches/k12-private-schools/report-card-narrative-generation/profile|Report Card Narrative Generation]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Fix (Pain Point)
**One-liner:** Parents receiving report cards notice dramatic quality differences between teachers — one writes three specific paragraphs per subject, another writes one vague sentence — but schools have no systematic way to ensure narrative quality before cards go home.
**Tags:** #bert #text-classification #nlp #worker-facing #compliance

## The Problem
A parent paying $30K in tuition receives a report card from their child's English teacher: a detailed, specific paragraph referencing particular essays and discussion contributions. The math teacher's narrative reads: "Johnny is doing well in math. Keep up the good work!" The quality gap undermines the school's brand promise of individualized attention. Division heads review narratives before they go home, but reading 200-400 narratives and providing feedback to teachers who need revisions is a 15-20 hour process that bottlenecks the reporting cycle.

## Why It's Still Broken
Schools lack a rubric for narrative quality — "specific," "warm," "growth-oriented" are described in a style guide but not operationalized in a way that enables automated quality checking. Division heads review subjectively, and their feedback is inconsistent. Some teachers interpret the style guide strictly and others loosely. Time pressure at the end of reporting periods means quality review is often rushed or skipped for on-time teachers, with only egregiously poor narratives flagged.

## What a Fix Looks Like
An automated narrative quality checker that evaluates each comment against defined criteria: minimum length, specificity (references to actual student work or behavior, not generic praise), growth framing (identifies at least one growth area constructively), alignment with the school's style guide (vocabulary, tone), and uniqueness (flags narratives that are identical or near-identical to another student's comment from the same teacher). Teachers receive quality scores and specific improvement suggestions before submitting. Division heads review only narratives flagged below the quality threshold.

## Who Feels the Pain
Division heads who spend 15-20 hours reviewing narratives per reporting cycle, and parents who lose trust in the school when report card quality is inconsistent across teachers.

## Impact If Fixed
Reduces division head review time from 15-20 hours to 3-5 hours per cycle (reviewing only flagged narratives instead of all). Raises the quality floor across all teachers, reducing parent complaints about report card quality by an estimated 40-60%. Provides teachers with immediate, consistent feedback rather than subjective end-of-cycle edits.
