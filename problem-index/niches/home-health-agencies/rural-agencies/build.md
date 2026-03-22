# Telehealth-Visit Hybrid Clinical Triage Platform

**Niche:** [[niches/home-health-agencies/rural-agencies/profile|Rural Home Health Agencies]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Determine which home health visits must be in-person (wound care, IV therapy) vs. which can be telehealth (medication management, education) to maximize patient coverage with limited rural clinicians who drive 30-60+ miles per visit.
**Tags:** #decision-trees #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #automation #worker-facing #revenue-impact

## The Problem
A rural home health nurse with 6 patients scheduled across a 120-mile radius can physically see 4-5 patients in a day. The remaining patients either get rescheduled (delaying care) or the nurse works a 12-hour day with 3+ hours of driving. Some of those visits could safely be conducted via telehealth — a medication management check, a disease education session, a fall risk reassessment — but the clinical triage decision of "which visits MUST be in-person today?" is made by experienced clinicians based on tacit judgment: the patient's stability trajectory, the specific care tasks ordered, and whether the patient or family can reliably operate a telehealth device. No tool supports this clinical decision.

## Why Nobody Has Built This
CMS reimbursement for home health telehealth visits has been inconsistent and restrictive until recent policy changes. Agencies were reluctant to build telehealth workflows when reimbursement was uncertain. The clinical triage logic is genuinely complex: a wound care visit is always in-person, but a "medication management" visit might need to be in-person if the patient has cognitive decline that makes telehealth unreliable. This requires encoding clinical judgment rules that vary by patient acuity, care plan, and patient/caregiver capability — a decision tree that experienced nurses make intuitively but that has never been formalized.

## What to Build
A clinical triage engine that takes the day's scheduled visits, each patient's current care plan (ordered services, visit frequency), recent clinical status (last visit notes, vital sign trends, wound status), and patient telehealth capability assessment, then recommends which visits should be in-person vs. telehealth. The model trains on historical visit data — identifying which visit types, for which patient profiles, were successfully converted to telehealth without adverse outcomes (hospitalization, wound deterioration, medication errors). For in-person visits, the system optimizes the route; for telehealth visits, it schedules video sessions with pre-visit questionnaires sent to the patient's device.

## Target Customer
Rural Medicare-certified home health agencies where average drive time between patients exceeds 25 minutes, particularly agencies in states that have adopted CMS telehealth reimbursement flexibility.

## Impact If Built
Converting 20-30% of rural home health visits to telehealth would increase effective patient capacity by 25-40% per clinician without additional driving. For a rural agency with 5 clinicians seeing 25 patients/day total, this means covering 32-35 patients daily — the difference between maintaining a viable census in a county where the next nearest agency is 50 miles away.
