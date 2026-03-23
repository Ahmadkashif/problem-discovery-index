# Pre-Release to Post-Release Vocational Continuity Platform

**Niche:** [[niches/vocational-schools/prison-reentry-vocational/profile|Prison Reentry Vocational Programs]]
**Industry:** [[industries/vocational-schools|Vocational Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that carries a student's vocational training record, competency assessments, and credential progress from inside the facility through release to community reentry — so the skills gained behind the wall are verifiable and actionable on the other side.
**Tags:** #data-integration #workflow-orchestration #worker-facing #compliance

## The Problem
An incarcerated individual completes 400 hours of welding training, passes multiple competency assessments, and is months into an AWS certification track. On release day, they walk out with a paper certificate or nothing at all. The community reentry organization has no record of their training. The workforce development agency starts them over with a new assessment. Employers can't verify the skills claimed on an application. The investment in vocational training — $5,000-$15,000 per participant in correctional program costs — is wasted when the training record doesn't survive the transition from corrections to community.

## Why Nobody Has Built This
The corrections-to-community transition crosses institutional boundaries that don't share data: DOC facilities, community-based reentry organizations, state workforce development agencies, and employers. Security restrictions inside facilities prevent cloud-based systems from operating during the training phase. Each state DOC has different record systems, policies, and data sharing agreements (or lack thereof). The population is hard to track post-release — address and phone number changes, reluctance to engage with institutions, parole/probation supervision creating privacy concerns.

## What to Build
A portable digital training record that begins inside the facility (populated offline, synced when data export is permitted) and persists through release as a credential wallet accessible to the individual, reentry case managers, workforce agencies, and prospective employers. The record includes competency assessments mapped to industry certification frameworks (AWS, NCCER, ASE), training hours by topic, instructor evaluations, and any certifications earned. Post-release, the platform connects the individual to community training programs that can continue their credential path from where they left off, rather than restarting.

## Target Customer
Corrections education coordinators and community reentry program directors who manage vocational training programs funded by Second Chance Act grants, DOJ reentry initiatives, or state workforce development funds — all of which require documented employment outcomes.

## Impact If Built
Eliminates the credential gap that causes 60-70% of correctional vocational graduates to start over with basic assessments upon release. Reduces time-to-employment post-release by 4-8 weeks by providing verifiable skill records to employers. Improves grant-required placement rate documentation — currently the weakest link in reentry program reporting.
