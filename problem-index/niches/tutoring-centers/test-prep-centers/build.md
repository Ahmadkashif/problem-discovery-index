# Skill-Level Score Prediction and Gap Targeting

**Niche:** [[niches/tutoring-centers/test-prep-centers/profile|Test Prep Centers (SAT/ACT/GRE)]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A model that predicts a student's test score from their current skill profile across 30-40 specific competency dimensions — identifying exactly which 3-5 skills to target for maximum score gain, rather than the generic "study more math" guidance most tutors provide.
**Tags:** #bayesian-network #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
A student scoring 1200 on the SAT wants to reach 1350. Their tutor assigns more practice tests and reviews missed questions. But the 150-point gap isn't distributed evenly — 80 points may be recoverable from 3 specific math skills (systems of equations, data analysis, quadratic functions) while the remaining 70 points are spread across 15 reading/writing skills where marginal improvement is harder. An experienced test prep tutor intuits this priority ranking from years of working with similar score profiles, but a new tutor assigns practice uniformly across all areas, wasting weeks on low-yield topics.

## Why Nobody Has Built This
Building a skill-level score prediction model requires question-level response data from thousands of students mapped to standardized skill taxonomies — data that test prep centers don't collect in structured form. College Board provides section-level scores but not question-level performance by skill. Practice platforms track question accuracy but don't model the relationship between skill mastery and score outcomes. The missing piece is a student knowledge model that maps granular skill proficiency to expected score, enabling "if this student masters systems of equations (currently at 40% proficiency), their predicted math score increases from 620 to 660."

## What to Build
A Bayesian knowledge model covering the 30-40 specific skills tested on the SAT/ACT/GRE, trained on question-level response data from practice tests. For each student: (1) estimate proficiency on each skill from practice question responses; (2) predict test score from current skill profile; (3) compute score sensitivity to each skill — which skills have the highest score-gain-per-study-hour; (4) generate a prioritized study plan targeting the 3-5 highest-yield skills for the student's target score. Tutors see a skills dashboard showing "the fastest path from 1200 to 1350 is: systems of equations (+30 pts), data analysis (+25 pts), quadratic functions (+25 pts)."

## Target Customer
Test prep center owners and lead tutors at centers with 50+ active test prep students who want data-driven curriculum targeting instead of uniform practice assignment.

## Impact If Built
Increases average score improvement per student by 30-50% by concentrating study time on highest-yield skills. Reduces average time-to-target-score by 3-5 weeks. Provides concrete evidence of tutoring value to parents: "your child needs 40 more hours of focused practice on these 4 specific skills to reach their target score" instead of "keep studying."
