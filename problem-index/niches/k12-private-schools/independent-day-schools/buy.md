# Admissions CRM-to-SIS Data Flow for Yield Management

**Niche:** [[niches/k12-private-schools/independent-day-schools/profile|Independent Day Schools (Non-Sectarian)]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Admissions CRMs (Ravenna, SchoolAdmin) and SIS platforms (Veracross, FACTS) both exist but do not share family data bi-directionally — the admissions director cannot see enrolled family engagement data, and the SIS does not track admissions pipeline metrics.
**Tags:** #data-integration #workflow-orchestration #automation #revenue-impact

## The Problem
The admissions director builds a pipeline of 300 applicant families in the admissions CRM. She needs to know which currently enrolled families have siblings who should be recruited, which admitted families' parents are alumni (increasing yield probability), and which families applied in prior years but did not enroll (possible re-engagement targets). This data exists in the SIS and advancement database but is not accessible from the admissions CRM. The director manually exports and cross-references spreadsheets.

## What Already Exists
Ravenna and SchoolAdmin provide admissions CRM with inquiry tracking, application management, and yield analytics. Veracross and FACTS SIS manage student records, family demographics, and enrollment data. Both types of systems offer APIs or data export capabilities.

## The Customization Gap
The integration must understand school-specific relationships: a "family" in the SIS may map to 2-3 "applicant households" in the admissions CRM (divorced parents, guardians). Sibling relationships must be traced across systems. Alumni status must be pulled from the advancement database and surfaced in the admissions CRM. Yield scoring models need features from both systems (application behavior from CRM + enrolled sibling data from SIS + giving history from advancement). Building this integration requires understanding the data models of school-specific systems, not generic CRM-to-database connectors.

## Target Customer
Admissions directors at independent day schools receiving 200+ applications per year who spend 5-10 hours per week manually cross-referencing admissions and enrollment data.

## Impact If Solved
Reduces admissions data compilation from 5-10 hours per week to under 1 hour. Enables yield scoring models that incorporate enrollment history and family engagement, improving yield prediction accuracy by 15-20 percentage points. Identifies 20-30 sibling recruitment opportunities per admission cycle that are currently missed.
