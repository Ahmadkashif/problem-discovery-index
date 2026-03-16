# Multi-Subject, Multi-Tutor, Multi-Student Scheduling Optimization

**Industry:** [[tutoring-centers|Tutoring Centers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic scheduling tools handle appointment booking but can't optimize for the tutoring-specific constraint set — tutor subject qualifications, student-tutor continuity preferences, room capacity by session type, sibling coordination, and the revenue impact of schedule gaps that leave tutors idle between sessions.
**Tags:** #reinforcement-learning #regression #tabular-ml #workflow-orchestration

## The Problem

A tutoring center with 80 active students, 12 part-time tutors, and 4 tutoring rooms must produce a weekly schedule that satisfies: each student's preferred days/times (typically 2-3 sessions per week), tutor subject qualifications (not every tutor can teach every subject at every level), student-tutor continuity (switching tutors mid-program disrupts rapport and forces re-diagnosis), sibling coordination (parents want both children scheduled at the same time), room capacity constraints (group sessions vs. 1-on-1), and tutor availability windows (part-time workers have variable availability week to week). A schedule change for one student cascades through the constraint network.

Center directors currently build schedules manually in spreadsheets or basic calendar tools, spending 3-5 hours per week on schedule maintenance. The result is suboptimal: tutors sit idle during mid-afternoon gaps, popular time slots (4-6 PM weekdays) are overbooked while morning slots go unfilled, and student-tutor matches are made by availability rather than pedagogical fit.

## What Already Exists

Scheduling platforms like TutorCruncher and Teachworks provide calendar-based booking and basic conflict detection. Acuity Scheduling and Calendly handle appointment self-service. None of these tools perform constraint optimization — they flag conflicts after the fact rather than generating optimal schedules that maximize tutor utilization, student-tutor continuity, and revenue per available hour.

## The Customisation Gap

Tutoring scheduling is a multi-objective constraint satisfaction problem with soft and hard constraints. Hard constraints: tutor availability, room capacity, subject qualification. Soft constraints: student-tutor continuity (high weight), sibling coordination (medium weight), preferred time slots (medium weight), tutor utilization (minimize idle gaps between sessions). The optimization must also account for rolling enrollment — new students join and existing students change availability continuously, requiring re-optimization without disrupting stable assignments. A reinforcement learning approach that learns scheduling policies from historical schedule quality (measured by tutor utilization rate, continuity score, and parent satisfaction) outperforms static optimization because the constraint weights are center-specific and shift over time.

## Impact If Solved

Recovers 3-5 hours per week of center director time currently spent on manual scheduling. Increases tutor utilization from typical 65-70% to 80-85% by eliminating idle gaps. Improves student-tutor continuity scores, directly supporting retention. For a center with 12 tutors at $25/hour, improving utilization by 15% recovers approximately $45,000 annually in productive tutoring hours.
