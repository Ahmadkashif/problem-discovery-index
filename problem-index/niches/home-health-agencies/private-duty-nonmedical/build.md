# Caregiver-Patient Compatibility Matching Engine

**Niche:** [[niches/home-health-agencies/private-duty-nonmedical/profile|Private-Duty Non-Medical Home Care]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Match home health aides to clients based on personality, language, skill level, schedule compatibility, and geography — replacing the coordinator's mental Rolodex that breaks down at scale.
**Tags:** #gradient-boosting #random-forests #feature-engineering #evaluation-metrics #tacit-knowledge-ml #worker-facing #revenue-impact

## The Problem
Scheduling coordinators at private-duty agencies develop deep personal knowledge of their caregiver pool — who works well with dementia patients, who speaks Haitian Creole, who can handle a client with behavioral issues, who lives near a particular neighborhood. This tacit knowledge enables good matches but lives entirely in the coordinator's head. When coordinators leave (and they do, frequently), the matching quality collapses. Agencies with 50+ aides and 80+ clients cannot maintain this personal-knowledge approach, leading to poor matches, client complaints, and caregiver turnover driven by assignments they find stressful or incompatible.

## Why Nobody Has Built This
Caregiver-patient matching requires capturing soft attributes — personality compatibility, communication style, cultural alignment — that aren't structured data in any existing system. Scheduling platforms track availability and geography, not whether a particular aide has the patience for a client with late-stage Alzheimer's. Building a matching model requires instrumenting match outcomes (client satisfaction, aide retention on case, complaints, re-assignments) and correlating them with caregiver and client attributes, which means building the data collection layer before the ML layer.

## What to Build
A compatibility scoring system that takes caregiver profiles (skills, languages, personality assessments, work history, geographic preferences) and client profiles (care needs, personality, household environment, cultural preferences, pet ownership) and produces ranked match recommendations with compatibility scores. The model trains on historical assignment outcomes — measuring which pairings lasted vs. which were quickly reassigned, which generated complaints vs. compliments, and which correlated with aide retention vs. turnover. Coordinators review and accept/reject recommendations, creating a feedback loop.

## Target Customer
Private-duty home care agencies with 40+ active caregivers and 60+ clients, particularly multi-location franchisees (Home Instead, Comfort Keepers, BrightSpring) where coordinator knowledge doesn't transfer across locations.

## Impact If Built
Reducing caregiver-client mismatch rates by 30-40% would lower caregiver turnover by an estimated 10-15 percentage points (from 65% to 50-55%), saving $2,500-$4,000 per avoided turnover event in recruitment and training costs. For a 100-aide agency, this represents $75K-$150K in annual savings plus improved client satisfaction and referral rates.
