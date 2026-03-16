# Student Job Placement Prediction and Employer Matching

**Industry:** [[vocational-schools|Vocational Schools]]
**Type:** High Impact
**One-liner:** Every graduating cohort gets matched to open positions ranked by fit, and at-risk students get intervention before they fall off the placement funnel.
**Tags:** #gradient-boosting #ranking #binary-classification #tabular-ml #revenue-impact

## The Problem
Vocational schools' entire value proposition is employment outcomes — accreditors (ACCSC, COE) mandate minimum placement rates (typically 70%+), Title IV funding depends on gainful employment metrics, and prospective students choose programs based on job placement stats. Yet most schools have no systematic way to predict which students are at risk of non-placement or to match graduates with the right employers. Career services coordinators work from static employer lists and personal relationships, manually matching students to openings based on geography and program completion alone, missing fit signals like specific skill strengths, employer culture, shift preferences, and transportation constraints.

## Why It's Unsolved
The data is fragmented across disconnected systems: attendance in the SIS, grades in the LMS, hands-on evaluations on paper rubrics, employer relationships in a coordinator's personal contacts, and placement outcomes in spreadsheets updated months after graduation. Building a predictive model requires joining all of these into a single student feature set, which no existing vocational SIS supports natively. Employer demand data is also sparse — most schools have relationships with 50-200 local employers and no structured feed of open positions, making the matching side of the problem as hard as the prediction side.

## What a Solution Looks Like
A model ingests student features (attendance patterns, competency scores by skill area, program progress, demographics, financial aid status) and outputs two things: (1) a binary placement risk score triggering early intervention workflows for at-risk students, and (2) a ranked list of employer-student matches using a learning-to-rank model trained on historical placement success, employer retention data, and skill-to-job-requirement alignment. Career services coordinators see a dashboard of prioritized actions: which students need intervention this week, and which employer matches to pursue first.

## Impact If Solved
A 10-percentage-point improvement in placement rates protects accreditation standing and can increase enrollment yield by 15-20% (placement rate is the #1 factor in prospective student decision-making for trade programs). For a 500-student school charging $15K average tuition, that enrollment lift is $1.1-1.5M in annual revenue.
