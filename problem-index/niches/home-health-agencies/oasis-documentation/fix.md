# OASIS Timing Compliance and Window Tracking

**Niche:** [[niches/home-health-agencies/oasis-documentation/profile|OASIS Assessment & Clinical Documentation]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** OASIS assessments must be completed within specific CMS-mandated windows — but tracking which patients need assessments and when across a census of hundreds is a manual calendar exercise that causes preventable claim denials when windows are missed.
**Tags:** #automation #compliance #workflow-orchestration #data-integration #quick-win

## The Problem
CMS mandates OASIS completion within precise windows: the start-of-care assessment within 5 days of admission, recertification assessments within the last 5 days of each 60-day episode, transfer assessments within 2 days of a transfer, and discharge assessments within 2 days of discharge. Missing these windows renders the assessment non-compliant, which can cause claim denials for the entire episode. With a census of 200+ patients, each on different 60-day certification cycles, tracking which patients need OASIS assessments this week — and assigning a qualified OASIS clinician to complete them within the window — is a scheduling puzzle that clinical managers solve with spreadsheets, wall calendars, and memory.

## Why It's Still Broken
Home health EMRs track the OASIS due date as a field in the patient record, but they don't surface a centralized "OASIS compliance dashboard" that shows all upcoming assessment windows across the census, prioritized by urgency, with clinician assignment. The information exists in the system but isn't presented as an actionable workflow. Clinical managers manually pull reports, cross-reference with the schedule, and hope nothing falls through the cracks. The problem intensifies during staff shortages and holiday periods when fewer OASIS-qualified clinicians are available and assessment windows don't pause.

## What a Fix Looks Like
An automated OASIS scheduling system that: (1) calculates every patient's next OASIS assessment window based on their certification period, (2) displays a rolling 14-day compliance dashboard showing all upcoming assessment windows sorted by deadline proximity, (3) auto-assigns OASIS assessments to qualified clinicians based on geographic proximity and schedule availability, (4) sends escalating alerts as assessment windows approach (7 days, 3 days, 1 day before window close), (5) blocks late assessments from submission with a manager override workflow that documents the reason for late completion, and (6) reports OASIS timing compliance rates by clinician and month for quality management.

## Who Feels the Pain
Clinical managers and DONs who spend 3-5 hours per week manually tracking OASIS compliance windows. Billing staff who discover 2-3 months later that a missed OASIS window caused a claim denial for a $3,000-$5,000 episode. OASIS clinicians who get urgent last-minute assignments because nobody realized the window was closing.

## Impact If Fixed
Eliminating missed OASIS windows — which typically affect 3-5% of assessments — would prevent $150K-$400K in annual claim denials for a mid-size agency. Automating the tracking and assignment workflow would reclaim 3-5 clinical manager hours per week and reduce the stress of manual compliance monitoring.
