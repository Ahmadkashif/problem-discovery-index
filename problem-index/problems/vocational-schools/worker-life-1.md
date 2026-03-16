# Instructor Hands-On Assessment Subjectivity and Documentation Burden

**Industry:** [[vocational-schools|Vocational Schools]]
**Type:** Worker Life Changing
**One-liner:** Trade instructors get freed from hours of rubric paperwork and gain a consistent, defensible record of what their students can actually do with their hands.
**Tags:** #cnn #multiclass-classification #computer-vision #worker-facing #tacit-knowledge-ml

## The Problem
A welding instructor watches 20 students perform a 6G pipe weld and must grade each one on bead consistency, penetration, undercut, porosity, and body positioning — filling out a multi-page rubric for each student, often from memory after the session because stopping to document interrupts the teaching flow. An electrical instructor evaluates panel wiring by visual inspection, checking termination tightness, wire routing, labeling compliance, and code adherence across 15 student stations. These assessments happen 3-5 times per week per cohort. Instructors — who became teachers because they love the trade, not paperwork — spend 8-12 hours per week on assessment documentation. Worse, the assessments are subjective: two instructors grading the same weld will disagree 30-40% of the time on sub-criteria, creating inconsistency that accreditors and employers notice.

## Why It Matters to the Worker
Instructors are former journeymen and master tradespeople who left higher-paying field work to teach because they care about passing on their craft. The documentation burden is the #1 cited reason for instructor turnover at vocational schools — they didn't sign up to be data entry clerks. The subjectivity problem is personally frustrating: experienced instructors know a good weld when they see one (they've internalized thousands of visual patterns over decades), but translating that tacit judgment into a 1-5 rubric score with written justification feels reductive and dishonest. They want to teach, demonstrate, and mentor — not grade paperwork.

## What a Solution Looks Like
A camera-based system (mounted at workstations or worn by instructors) captures student performance during hands-on tasks. A CNN model trained on expert-labeled examples classifies performance across competency dimensions (e.g., weld quality: acceptable/marginal/unacceptable; wire routing: compliant/non-compliant). The instructor reviews model-generated assessments on a tablet, approving or adjusting scores with one tap rather than writing from scratch. The system produces timestamped, visual evidence of each assessment — defensible documentation that satisfies accreditors and gives students specific, consistent feedback.

## Impact If Solved
Reclaims 6-10 hours per week of instructor time for actual teaching and mentoring. Reduces inter-rater disagreement from 30-40% to under 10%. Creates a visual portfolio for each student that employers can review, making the school's graduates more credible in hiring decisions.
