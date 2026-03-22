# Caseload Imbalance Visibility

**Niche:** [[niches/behavioral-health-clinics/intake-triage-matching/profile|Intake Triage & Patient-Clinician Matching]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Fix (Pain Point)
**One-liner:** In a 15-therapist practice, some clinicians are overbooked toward burnout while others have 5-10 open slots per week — and nobody has a real-time view of the imbalance because the data is scattered across calendars, EHRs, and the intake coordinator's memory.
**Tags:** #data-integration #workflow-orchestration #worker-facing #revenue-impact #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics

## The Problem
Caseload imbalance in multi-clinician behavioral health practices is invisible and self-reinforcing. Intake coordinators route patients based on who they remember has openings, which biases toward familiar, senior clinicians and away from new hires. The result: senior therapists carry 30+ active clients (burnout risk, declining session quality, waitlisted new patients) while newer clinicians have 15-20 clients and open capacity. Nobody has a real-time view of caseload distribution by clinician, insurance type, and acuity level. The EHR shows individual clinician schedules but doesn't aggregate into a practice-wide capacity dashboard. The financial impact compounds: overloaded clinicians generate more revenue per clinician but reduce overall practice capacity, while underutilized clinicians represent sunk cost (salary, benefits, office space) without proportional revenue.

## Why It's Still Broken
EHRs track appointments per clinician but don't model "caseload" as a concept — a clinician seeing 25 clients weekly for individual therapy has a different load than one seeing 12 couples (24 people) and 5 groups (40 people). Insurance mix matters too: a clinician credentialed with high-reimbursement payers is more valuable per session-hour than one credentialed only with Medicaid. No EHR computes effective caseload weighted by session type, acuity, and reimbursement rate. The intake coordinator sees individual calendars but can't see the aggregate pattern, and practice owners only discover imbalance when a clinician gives burnout notice or when monthly revenue reports show unexplained variance. A regression model can predict optimal caseload targets per clinician based on session type mix, acuity distribution, and historical burnout/turnover patterns.

## What a Fix Looks Like
A caseload balance dashboard that pulls appointment data from the EHR and displays real-time capacity across all clinicians, segmented by: total active clients, weekly session count, insurance mix, acuity distribution (high-acuity clients require more between-session documentation and crisis response capacity), and open slots by day/time. The dashboard highlights imbalances with visual heat maps and provides intake coordinators with a "recommended next clinician" nudge when routing new patients. A gradient-boosted model predicts each clinician's sustainable maximum caseload based on their session type mix and historical patterns, flagging clinicians approaching burnout thresholds before they self-report.

## Who Feels the Pain
Overloaded clinicians experiencing burnout without organizational awareness, new-hire clinicians struggling to build caseload because intake coordinators default to familiar colleagues, and practice owners losing revenue to invisible capacity waste.

## Impact If Fixed
Distributes caseload to achieve 85-95% capacity utilization across all clinicians (vs. typical 60-70% for new hires and 110%+ for senior clinicians), reducing therapist burnout turnover by 20-30% and recovering 10-15% in practice-wide revenue from better capacity utilization — worth $100K-300K annually for a 15-therapist practice.
