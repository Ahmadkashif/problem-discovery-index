# Stale Candidate Database and Reactivation Prioritization

**Niche:** [[niches/staffing-agencies/candidate-matching-ranking/profile|Candidate-to-Requisition Matching & Ranking]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** 80-90% of candidates in a staffing agency's ATS are inactive, and recruiters have no way to identify which dormant candidates are most likely to re-engage — so they ignore the database and source externally.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #automation

## The Problem
A staffing agency with 100K candidate records may have only 5K-10K active candidates (placed or in active communication). The remaining 90K+ records represent workers who completed past assignments, registered but were never placed, or went silent months or years ago. This dormant database is the agency's most valuable untapped asset — it contains pre-screened, previously placed workers — but recruiters ignore it because they have no way to distinguish the 5% who would re-engage from the 95% who have moved on. Instead, recruiters spend time and money sourcing new candidates from job boards ($5-$15 per click on Indeed), duplicating the cost of acquisition for workers already in the database.

## Why It's Still Broken
ATS platforms display candidates sorted by last activity date, which surfaces people who recently updated their profile but tells nothing about dormant candidates' likelihood of re-engagement. A candidate who last worked 6 months ago but has a historically high response rate and lives near current open job orders is a much better reactivation target than one who last worked 2 months ago but has a history of no-showing. The predictive signals (historical reliability, responsiveness, skill-demand alignment, life circumstance indicators) exist in the data but are never combined into a reactivation score.

## What a Fix Looks Like
A reactivation scoring model that ranks the dormant candidate pool by predicted probability of accepting and starting a new assignment within 30 days of outreach. Features include: historical placement count and reliability score, time since last placement, communication responsiveness history (average response time to recruiter messages), skill alignment with current open job orders, local labor market demand for the candidate's skill set, and seasonal patterns (candidates who historically return in Q1). The system generates a daily reactivation call list for each recruiter, prioritized by score, with suggested outreach messages referencing specific open roles that match the candidate's profile.

## Who Feels the Pain
Recruiters who spend 30-40% of their time sourcing new candidates on job boards while 90K pre-screened candidates sit dormant in the ATS, and agency owners paying $50K-$200K/year in job board fees to re-acquire workers they already have.

## Impact If Fixed
Reduces external sourcing costs by 25-40% ($50K-$100K annually per branch), reactivates 3-5% of the dormant database per quarter (representing 100-500 ready-to-place candidates), and improves time-to-fill by giving recruiters warm leads instead of cold sourcing.
