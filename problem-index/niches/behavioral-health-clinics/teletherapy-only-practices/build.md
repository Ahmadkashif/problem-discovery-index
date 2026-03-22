# Multi-State Licensure Compliance Engine

**Niche:** [[niches/behavioral-health-clinics/teletherapy-only-practices/profile|Teletherapy-Only Practices]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A real-time compliance layer that verifies, at every session start, that the therapist is licensed to treat the patient in the patient's current physical state — and blocks the session if they're not.
**Tags:** #logistic-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #automation #compliance #data-integration

## The Problem
A teletherapist licensed in 5 states must verify, at every single session, that the patient is physically located in a state where the therapist holds an active license. Today this is done verbally — the therapist asks "Where are you right now?" and documents the answer in free text. There is no automated check against the therapist's license registry, no enforcement mechanism, and no audit trail that would survive a state board inquiry. One missed verification — a patient who drove to an unlicensed state and didn't mention it — can trigger license revocation, malpractice exposure, and insurance clawback.

## Why Nobody Has Built This
The problem sits at the intersection of three fragmented data sources: state licensing board databases (50+ boards, each with different APIs or no API at all), interstate compact membership rosters (PSYPACT, ASWB mobility, Counseling Compact — each with different eligibility rules and participation lists), and real-time patient geolocation. No EHR vendor has incentive to build this because their core customers are brick-and-mortar practices where the therapist and patient are in the same room. The teletherapy-only segment is growing fast but still a minority of the behavioral health market.

## What to Build
A compliance engine that: (1) maintains a continuously updated registry of each therapist's active licenses and interstate compact memberships across all 50 states, (2) verifies the patient's physical location at session start via IP geolocation cross-referenced with patient attestation, (3) performs a real-time license-to-location match and either clears or blocks the session, and (4) generates a timestamped audit trail for every verification decision. The engine exposes an API that integrates with existing EHRs and telehealth platforms, plus a standalone dashboard for practice owners to monitor compliance across their entire clinician roster.

## Target Customer
Virtual practice owners with 3-8 therapists licensed across multiple states, and teletherapy startups scaling to 20+ clinicians where manual compliance tracking becomes operationally impossible.

## Impact If Built
Eliminates the single largest legal risk in teletherapy operations. Reduces compliance overhead from 10-15 minutes of manual checking per therapist per day to zero. Enables confident expansion into new states without proportional compliance staffing.
