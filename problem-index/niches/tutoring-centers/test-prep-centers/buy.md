# Adaptive Practice Assignment Engine

**Niche:** [[niches/tutoring-centers/test-prep-centers/profile|Test Prep Centers (SAT/ACT/GRE)]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Adaptive learning platforms exist broadly but aren't tailored to test prep's specific goal — maximizing score improvement within a fixed preparation timeline rather than achieving general mastery.
**Tags:** #bayesian-network #recommendation #tabular-ml #automation #worker-facing

## The Problem
After each tutoring session, tutors assign practice problems for the student to complete before the next session. Experienced tutors select problems at the right difficulty level for each student's current skill — too easy wastes time, too hard causes frustration. They also vary question types to address specific weaknesses identified during the session. New tutors (40-60% annual turnover) assign problems from generic problem sets without adapting to the individual student's skill profile, producing inefficient practice that doesn't target the student's actual gaps.

## What Already Exists
Adaptive learning platforms (Khan Academy, IXL, ALEKS) adjust difficulty based on student responses for general academic subjects. Test prep platforms (UWorld, Magoosh) provide practice questions organized by topic and difficulty. Spaced repetition tools (Anki) optimize review timing. None of these integrate with the in-person tutoring workflow: the tutor identifies a specific skill gap during the session, and the platform assigns targeted practice problems at the right difficulty to address that gap for homework.

## The Customization Gap
The gap is a practice assignment engine that: (1) maps to the specific skill taxonomy of each standardized test (SAT Math has ~30 specific skills, ACT Science has ~15); (2) selects questions at the optimal difficulty for the student's current proficiency on each skill (not too easy, not too hard — the zone of proximal development); (3) allows the tutor to mark specific skills for targeted practice after each session; (4) tracks accuracy and speed on assigned problems to update the student's skill profile; (5) integrates with center scheduling systems to account for time available between sessions. The customization is test-specific skill mapping and difficulty calibration — not general adaptive learning.

## Target Customer
Test prep center directors and lead tutors who want consistent, data-driven practice assignments across all tutors rather than relying on each tutor's individual problem selection judgment.

## Impact If Solved
Increases practice efficiency by 30-40% through difficulty-appropriate problem selection. Standardizes homework assignment quality across all tutors regardless of experience level. Provides continuous skill proficiency updates from homework performance, making in-session diagnostic time more productive.
