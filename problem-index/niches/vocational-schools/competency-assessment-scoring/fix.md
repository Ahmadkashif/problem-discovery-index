# Assessment Data Loss Between Instructor Shifts

**Niche:** [[niches/vocational-schools/competency-assessment-scoring/profile|Competency Assessment & Scoring]]
**Industry:** [[industries/vocational-schools|Vocational Schools]]
**Type:** Fix (Pain Point)
**One-liner:** When a morning instructor assesses a student's welding progress and the afternoon instructor picks up with the same student, neither has access to the other's observations — assessment continuity is lost at every shift change and instructor substitution.
**Tags:** #data-integration #worker-facing #automation #workflow-orchestration

## The Problem
Vocational programs often have multiple instructors teaching different sections or shifts — a morning welding instructor and an afternoon welding instructor, a primary instructor and a substitute when the primary is absent, or a theory instructor and a lab instructor for the same students. Each instructor maintains their own assessment notes (paper or personal spreadsheet), creating isolated data silos. When a student shows up for the afternoon session, the afternoon instructor has no visibility into the morning instructor's assessment of that student's work. This forces re-evaluation, wastes time, and produces inconsistent longitudinal records.

## Why It's Still Broken
Assessment data is personal to each instructor — stored in their own notebook, clipboard, or laptop file. There is no shared assessment platform where multiple instructors contribute to a single student competency record. The SIS records course grades (a single number entered at the end of the term) but not ongoing competency observations. Schools that have tried shared spreadsheets find that instructors don't update them in real time from the shop floor, so the data is always stale or incomplete.

## What a Fix Looks Like
A shared, real-time competency record per student that all instructors for that program can view and update from the shop floor. When Instructor A scores a student's morning weld, Instructor B sees the score, the photo evidence, and any notes before the afternoon session begins. The system maintains a single timeline of competency observations per student, regardless of which instructor recorded them. Instructor handoff becomes data-driven: "Student has been struggling with vertical position for 3 sessions — morning instructor notes suggest adjusting travel speed" rather than a hallway conversation that may or may not happen.

## Who Feels the Pain
Afternoon and substitute instructors who start each session with zero context about student progress observed by other instructors, and students who are re-assessed on skills they already demonstrated in a previous session because the assessment data didn't transfer.

## Impact If Fixed
Eliminates 15-30 minutes per session of redundant re-assessment when students see different instructors. Ensures that assessment continuity survives instructor absences, shift changes, and staff turnover. Produces a single, comprehensive competency record per student that reflects all instructor observations — not just the primary instructor's partial view.
