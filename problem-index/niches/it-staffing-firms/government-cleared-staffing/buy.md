# LCAT-to-Candidate Matching for Contract Vehicles

**Niche:** [[niches/it-staffing-firms/government-cleared-staffing/profile|Government & Cleared IT Staffing]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bullhorn and JobDiva model jobs as free-text descriptions, but government contracts define roles as rigid Labor Categories (LCATs) with specific education, experience, and certification requirements that must be matched exactly.
**Tags:** #text-classification #nlp #data-integration #compliance

## The Problem
Government IT contracts specify roles through Labor Categories — structured definitions requiring exact combinations of degree type, years of experience, specific certifications, and sometimes clearance levels. A "Systems Engineer III" LCAT might require a BS in engineering + 8 years experience + CISSP, with no flexibility. Recruiters manually compare candidate resumes against LCAT requirements, often across 20-50 LCATs per contract vehicle, to find which categories a candidate qualifies for. Misclassifying a candidate into the wrong LCAT can trigger audit findings and contract penalties.

## What Already Exists
Bullhorn, JobDiva, and Ceipal provide resume parsing and skill matching, but they match against free-text job descriptions, not structured LCAT specifications. GovWin and Bloomberg Government provide contract intelligence but no candidate-matching capability. Some large primes have built internal LCAT databases, but these are proprietary and not available to smaller staffing firms.

## The Customization Gap
The adaptation requires ingesting structured LCAT definitions from contract vehicles (often PDF tables or Word documents), parsing them into queryable requirement sets (degree + years + certs + clearance), and matching candidates against these structured criteria rather than keyword similarity. The system must handle LCAT equivalency rules (e.g., "Master's degree may substitute for 2 years of experience") and track which contract vehicles each candidate qualifies for across all their LCAT positions.

## Target Customer
Small-to-mid-size cleared IT staffing firms (50-500 employees) holding positions on 5-20 government contract vehicles who manage LCAT compliance with spreadsheets.

## Impact If Solved
Cuts LCAT matching time from 2-3 hours per candidate to 10 minutes, and eliminates 90% of LCAT misclassification audit findings. For a firm placing 100 cleared contractors annually, saves 200-300 recruiter hours and avoids $50K-$150K in compliance penalties.
