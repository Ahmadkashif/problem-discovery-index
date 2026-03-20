# Enrollment Yield Prediction and Family Retention

**Industry:** [[k12-private-schools|K-12 Private Schools]]
**Type:** High Impact
**One-liner:** The day after this is solved, a head of school knows by February which accepted families will actually enroll and which current families are at risk of leaving — turning enrollment season from a guessing game into a managed pipeline.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #maximum-likelihood-estimation #bias-variance-tradeoff #revenue-impact

## The Problem
Private schools accept more students than they have seats, hoping yield rates hold steady — but yield swings of even 5-10% create budget crises or overcrowded classrooms. Admissions directors rely on anecdotal signals (campus visit enthusiasm, speed of document submission, sibling enrollment) to guess which families will convert. Retention is equally opaque: a family that quietly tours a competitor in November withdraws in April, and the school scrambles to fill the seat from a depleted waitlist.

## Why It's Unsolved
The data exists — inquiry timestamps, campus visit attendance, financial aid requests, re-enrollment form submission dates, parent volunteer hours, tuition payment timeliness — but it lives across 3-5 disconnected systems (FACTS, Finalsite, Google Forms, email). No private school has a data engineering team to unify it. The sample sizes are small (200-800 families per school), making off-the-shelf churn models unreliable without careful feature engineering and cross-school transfer learning. Schools also fear that a "retention risk score" feels transactional in a community that prides itself on relationships.

## What a Solution Looks Like
A unified family engagement model ingests SIS, billing, admissions CRM, and communication data to produce two scores per family: yield probability (for applicants) and attrition risk (for enrolled families). Admissions directors see a ranked list of accepted families with yield scores and recommended touchpoints (e.g., "schedule a coach meeting — this family's primary driver is athletics"). Retention dashboards flag at-risk families by October so the division head can intervene before the re-enrollment deadline.

## Impact If Solved
A 500-student school charging $25K tuition loses $625K for every 5% unexpected attrition. Accurate yield prediction eliminates over-acceptance risk and waitlist mismanagement. Schools that can predict and prevent attrition stabilize revenue and reduce the desperation-driven discounting that erodes net tuition revenue across the sector.
