# Post-Release Employment Outcome Tracking

**Niche:** [[niches/vocational-schools/prison-reentry-vocational/profile|Prison Reentry Vocational Programs]]
**Industry:** [[industries/vocational-schools|Vocational Schools]]
**Type:** Fix (Pain Point)
**One-liner:** Reentry vocational programs are funded based on employment outcomes they cannot verify — released individuals are the hardest population to track, and failed tracking looks identical to failed placement in grant reports.
**Tags:** #data-integration #automation #compliance #quick-win

## The Problem
Federal and state grants funding correctional vocational programs (Second Chance Act, DOJ's Ready to Work, state workforce development allocations) require documented employment outcomes: what percentage of program completers obtained employment within 90/180 days of release, in what industry, at what wage, and for how long they retained employment. Tracking these outcomes for formerly incarcerated individuals is extraordinarily difficult — they change phone numbers, addresses, and sometimes names; many distrust institutional contact; parole officers have limited employment verification capacity; and employer verification requires knowing where the individual works, which is often unknown.

## Why It's Still Broken
The data exists in siloed state systems — unemployment insurance wage records, state workforce agency job placement records, parole/probation case management systems — but reentry programs cannot access it. Privacy regulations (42 CFR Part 2 for substance abuse treatment records, state-specific DOC data sharing restrictions) prevent easy cross-system queries. Manual tracking by reentry case managers achieves 30-50% verification rates, with the remainder reported as "unknown" — making programs appear less effective than they are and threatening future funding.

## What a Fix Looks Like
A multi-source verification system that: (1) establishes data-sharing agreements with state UI wage record systems to verify employment status without revealing employer details to the program; (2) integrates with parole/probation case management systems where employment status is routinely collected; (3) uses automated multi-channel outreach (text, email, WhatsApp) to program completers with one-tap employment verification responses; (4) produces grant-compliant outcome reports with clear documentation of verified vs. unverified cases. The system prioritizes passive verification (wage record matching) over active outreach, reducing the burden on both staff and formerly incarcerated individuals.

## Who Feels the Pain
Reentry program directors who risk losing grant funding due to underreported employment outcomes, and case managers who spend 10-15 hours per week on phone-based employment verification with low response rates.

## Impact If Fixed
Increases verified employment outcome rates by 15-30 percentage points through passive data matching — accurately reflecting program effectiveness instead of penalizing tracking difficulty. Reduces case manager verification workload by 50-70%. Strengthens grant renewal applications with reliable, multi-source outcome data.
