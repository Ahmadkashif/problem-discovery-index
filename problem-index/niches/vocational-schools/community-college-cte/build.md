# CTE-Specific Competency Layer for Enterprise SIS

**Niche:** [[niches/vocational-schools/community-college-cte/profile|Community College CTE Divisions]]
**Industry:** [[industries/vocational-schools|Vocational Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A competency tracking system that sits alongside (not inside) the college's enterprise SIS, capturing hands-on skills assessment data that Banner and PeopleSoft cannot model — without requiring IT department customization of the core SIS.
**Tags:** #data-integration #workflow-orchestration #automation #worker-facing

## The Problem
CTE faculty at community colleges assess students on competency dimensions that their institution's SIS cannot represent — welding positions, electrical code knowledge by NEC article, automotive diagnostic procedures by ASE area. They record these assessments on paper skill sheets or personal spreadsheets because the SIS data model (designed for credit-hour courses with letter grades) has no concept of multi-dimensional competency matrices. When accreditors or Perkins auditors ask for competency-level data, program directors spend weeks reconstructing it from paper records.

## Why Nobody Has Built This
Community colleges have institutional IT governance that blocks CTE divisions from deploying their own SIS modifications. Any solution must work alongside the existing SIS without requiring database changes, API access, or IT department involvement. Private trade school SIS platforms (Campus Cafe, SONIS) serve this need for independent schools but aren't designed to coexist with Banner/PeopleSoft or feed data into institutional reporting pipelines. The market is large but fragmented — each state has different CTE reporting requirements, and each college has different SIS configurations.

## What to Build
A lightweight, cloud-based competency management platform that CTE faculty access independently of the college SIS. Instructors enter competency assessments via mobile device from the shop floor. The system models trade-specific competency frameworks (NCCER, AWS, ASE) as configurable skill matrices. Data exports feed into institutional Perkins reporting and accreditation self-studies. Student competency records produce portable skills transcripts for employer verification. The platform operates as a standalone SaaS requiring no IT department integration — just faculty browser access.

## Target Customer
CTE deans and program directors at community colleges with 200+ CTE students who are frustrated by the inability to track competency-level data within their institutional SIS and spend weeks assembling competency evidence for Perkins reporting and accreditation.

## Impact If Built
Eliminates 40-80 hours of annual manual data assembly for Perkins and accreditation reporting per program. Gives CTE faculty a 2-minute mobile assessment workflow replacing paper skill sheets. Produces employer-facing skills transcripts that differentiate community college CTE graduates in the job market.
