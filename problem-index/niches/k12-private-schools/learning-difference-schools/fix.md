# Therapeutic Service Documentation Fragmentation

**Niche:** [[niches/k12-private-schools/learning-difference-schools/profile|Learning Difference & Special Needs Schools]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Fix (Pain Point)
**One-liner:** Each therapist (speech, OT, counseling) maintains session notes in their own system or paper files — teachers cannot see therapeutic progress, and progress reports require manual compilation from 3-5 separate sources.
**Tags:** #data-integration #workflow-orchestration #worker-facing #quick-win

## The Problem
A student at an LD school receives speech therapy twice per week, occupational therapy once per week, and executive function coaching weekly. Each provider maintains separate session notes: the speech therapist uses a therapy-specific app, the OT maintains a binder, and the executive function coach tracks in a spreadsheet. When the student's classroom teacher wants to know what strategies the OT is reinforcing (so she can prompt them in the classroom), she must ask the OT directly. When the progress report is due, the learning specialist must collect notes from 3-5 providers, synthesize them, and write a unified narrative — a process that takes 2-3 hours per student.

## Why It's Still Broken
Each therapeutic discipline has its own documentation standards and preferred tools. Speech therapists trained on specific documentation software resist switching to a school-wide system. OTs have different session note formats than counselors. The school does not mandate a single documentation system because it does not have one that accommodates all disciplines. The result is that therapeutic and academic documentation exist in parallel universes that are only joined during progress reporting — when someone manually compiles everything.

## What a Fix Looks Like
A lightweight shared documentation layer where each therapist enters a brief session summary (goal addressed, activity, outcome, strategies reinforced) in a standardized format accessible to the student's full team. The system does not replace discipline-specific documentation tools but adds a shared summary layer that teachers and learning specialists can see. Progress report generation pulls from this shared layer, auto-populating the therapeutic sections with structured data rather than requiring manual compilation.

## Who Feels the Pain
Learning specialists who spend 2-3 hours per student compiling progress reports from fragmented therapeutic documentation, and classroom teachers who implement accommodation strategies in isolation from the therapeutic team's current focus.

## Impact If Fixed
Reduces progress report compilation time by 50-60% per student. Enables real-time coordination between classroom teachers and therapists — when the OT introduces a new regulation strategy on Tuesday, the teacher can reinforce it on Wednesday. Improves the quality of progress reports by ensuring therapeutic progress is accurately and consistently represented.
