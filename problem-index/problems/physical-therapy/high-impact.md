# Authorization Lifecycle Automation

**Industry:** [[physical-therapy|Physical Therapy]]
**Type:** High Impact
**One-liner:** PT clinics never deliver a visit without valid authorization again — every patient's authorization status, remaining visits, and upcoming expiration is tracked automatically, and extension requests are triggered before limits are hit.
**Tags:** #gradient-boosting #feature-engineering #cross-validation #evaluation-metrics #revenue-impact #compliance #ai-agent

## The Problem
Most insurance payers require prior authorization for physical therapy, typically approving 10-12 visits at a time. When those visits are used, the clinic must request a concurrent review (extension) with updated clinical documentation proving ongoing medical necessity. Tracking where each patient stands — how many authorized visits remain, when the authorization expires, whether an extension has been submitted — is a manual process spread across spreadsheets, EHR fields, and sticky notes. When tracking fails, the clinic delivers visits without valid authorization and eats the cost (typically $100-$200 per visit). A mid-size clinic with 200 active patients can lose $5,000-$15,000 monthly to authorization-related denials.

## Why It's Unsolved
Authorization rules vary dramatically by payer, plan, and even by diagnosis. United Healthcare might require auth after visit 1, while Blue Cross might not require it until visit 12. Some payers use third-party utilization management companies (EviCore, Cohere Health) with their own portals and submission requirements. The data needed to track authorization status lives across the EHR (visit count), the payer portal (authorization details), and sometimes a separate UM vendor portal. No single system aggregates this information reliably.

## What a Solution Looks Like
An authorization management system that pulls authorization data from payer and UM vendor portals, tracks visit counts against authorized limits in real-time, alerts staff 2-3 visits before an authorization expires, pre-populates extension request forms with clinical data from the EMR, and blocks scheduling of unauthorized visits. Inputs: payer authorization data, EMR visit history, clinical progress notes. Outputs: real-time authorization dashboard, automated extension requests, scheduling alerts.

## Impact If Solved
Eliminates $5,000-$15,000 monthly in authorization-related revenue leakage per clinic. Saves the front-desk/auth coordinator 8-12 hours per week of manual tracking and phone calls. Prevents treatment interruptions that harm patient outcomes.
