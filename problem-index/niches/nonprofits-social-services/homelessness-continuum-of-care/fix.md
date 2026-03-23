# Duplicate Client Records Across Agencies

**Niche:** [[niches/nonprofits-social-services/homelessness-continuum-of-care/profile|Homelessness Continuum of Care]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Fix (Pain Point)
**One-liner:** 15-25% of client records in HMIS are duplicates because individuals experiencing homelessness provide different names, dates of birth, or SSN fragments at different agencies, inflating counts and fracturing service history.
**Tags:** #bert #named-entity-recognition #nlp #data-integration #compliance

## The Problem
People experiencing homelessness interact with multiple agencies across a CoC — outreach teams, shelters, health clinics, rapid rehousing providers. At each intake, they may provide slightly different identifying information (nickname vs. legal name, estimated date of birth, partial SSN). HMIS deduplication algorithms rely on exact or near-exact matching of name/DOB/SSN, which fails for this population. The result: a single person has 2-4 records in HMIS, their service history is fragmented, and the CoC overcounts its homeless population in the Point-in-Time count.

## Why It's Still Broken
Standard record matching (Soundex, Jaro-Winkler on name fields) produces too many false positives in a population where common names are prevalent and demographic data is often estimated. More sophisticated matching (biometric, photo) raises privacy and consent concerns with a population that is already surveilled by multiple systems. HMIS vendors provide basic deduplication tools, but they flag potential duplicates without resolving them — the HMIS administrator must manually review each flagged pair and decide whether to merge, a process that can take 500+ hours per year for a large CoC.

## What a Fix Looks Like
A probabilistic record linkage system that goes beyond name/DOB matching to incorporate service interaction patterns (two records that always appear at the same shelter on the same nights are likely the same person), physical descriptors captured during outreach, and consent-based client confirmation. The system auto-merges high-confidence duplicates, queues medium-confidence pairs for administrator review with side-by-side comparison, and prevents future duplicates by suggesting likely matches during intake.

## Who Feels the Pain
Case managers who open a client record and find incomplete service history, not realizing the client has been served by three other agencies under a different name spelling — leading to duplicated assessments and missed service connections.

## Impact If Fixed
Reduces duplicate records by 70%, gives case managers complete client histories across the CoC, improves Point-in-Time count accuracy by 10-15%, and saves 300+ hours per year of manual deduplication work per CoC.
