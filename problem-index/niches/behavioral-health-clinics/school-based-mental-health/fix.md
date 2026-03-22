# Multi-School Caseload Visibility Dashboard

**Niche:** [[niches/behavioral-health-clinics/school-based-mental-health/profile|School-Based Mental Health Providers]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Fix (Pain Point)
**One-liner:** Districts and therapists get real-time visibility into caseloads, waitlists, and attendance across all schools — replacing the spreadsheets and blind spots that let at-risk students fall through the cracks.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #worker-facing #data-integration

## The Problem
A school-based mental health provider contracted by a district may serve 3-5 schools, rotating between buildings on different days. They track their own caseload on personal spreadsheets or in their heads. The district mental health coordinator has no unified view of: how many students are actively receiving services at each school, which students are on waitlists and how long they've been waiting, which students have stopped attending sessions (a safeguarding concern — a student who suddenly stops showing up may be in crisis), and whether caseloads are equitably distributed across buildings relative to student need. When a therapist leaves or goes on medical leave, no one has a clear picture of which students need to be reassigned. At the district level, there's no data to answer the school board's question: "Are we meeting student mental health needs?"

## Why It's Still Broken
Therapist caseload data lives in each individual therapist's records — whether that's a personal spreadsheet, a clinical EHR the district can't access (HIPAA), or notes in the school SIS that aren't structured for aggregation. Districts have tried building dashboards in Google Sheets or Power BI, but these require manual data entry by therapists who are already overwhelmed with documentation. School SIS platforms (PowerSchool, Infinite Campus) track student demographics but don't have modules for mental health caseload management. The data fragmentation is structural: clinical records (HIPAA) and educational records (FERPA) live in separate systems with different access rules, and no one has built the bridge.

## What a Fix Looks Like
A lightweight caseload management layer — not a full EHR, but a structured tracking tool — where therapists log student status (active, waitlist, discharged, no-show streak) and the district coordinator sees an aggregated dashboard across all schools and all therapists. Key views: students per school, waitlist length and wait time by school, session attendance trends with automated alerts when a student misses 3+ consecutive sessions, caseload per therapist vs. recommended maximum (typically 35-50 students), and equity metrics (caseload relative to school-level indicators like free/reduced lunch percentage). The tool must be FERPA-compliant (educational records context) and show only de-identified aggregate data at the district level unless the viewer has appropriate access rights. Input must be minimal — a therapist updates a student's status with 2-3 clicks after each session, not a full documentation entry.

## Who Feels the Pain
School-based therapists who are flying blind on their own caseload patterns and have no way to flag when they're over capacity. District mental health coordinators who can't answer basic questions about service delivery equity. School principals who want to know if their students are being served. And most critically, students on waitlists or students who stopped attending sessions — they're the ones who suffer when no one notices.

## Impact If Fixed
Districts gain immediate visibility into service gaps — which schools are underserved, which therapists are over-caseloaded, which students have been waiting longest. Automated no-show alerts catch at-risk students within days instead of months. Therapist caseload equity improves because redistribution decisions are based on data, not guesswork. The dashboard also provides the data districts need to justify additional mental health funding to school boards.
