# Real-Time Credential-Treatment Compliance Engine

**Niche:** [[niches/med-spas/protocol-compliance/profile|Treatment Protocol & Compliance Management]]
**Industry:** [[industries/med-spas|Med Spas]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system validates in real time that the staff member performing a med spa treatment holds the required credential for that treatment type in that state — violations are discovered only during audits or adverse event investigations.
**Tags:** #automation #compliance #data-integration #workflow-orchestration

## The Problem
A med spa in Texas schedules an esthetician to perform a chemical peel — which is within her scope. But the scheduling system doesn't know that she cannot perform a deep TCA peel (medical procedure) versus a superficial glycolic peel (esthetic procedure) in Texas without physician supervision. The system also doesn't know that her laser safety certification expired last month, making her ineligible to operate the practice's IPL device until renewal. These credential-treatment mismatches happen regularly and are invisible until a state board complaint, insurance audit, or patient adverse event triggers scrutiny.

## Why Nobody Has Built This
Building this requires encoding: (1) every state's scope-of-practice rules for every credential type (esthetician, RN, NP, PA, MD/DO), (2) treatment classification by procedure type and risk level per state, (3) supervision requirements by state and credential combination, and (4) certification/training prerequisites per device and procedure. This is a massive rule-base that changes with every legislative session and requires ongoing legal/regulatory maintenance. No med spa software vendor has justified this investment.

## What to Build
A compliance engine integrated with scheduling that: (1) validates each appointment against the assigned provider's credentials, scope of practice (state-specific), and current certifications, (2) flags violations before the appointment occurs ("Jessica cannot perform deep peels in TX — reschedule to Dr. Smith or downgrade to superficial peel"), (3) tracks certification expirations and blocks scheduling for expired credentials, and (4) generates audit-ready compliance reports showing credential-treatment validation for every treatment performed.

## Target Customer
Multi-provider med spas with 4+ staff members and mixed credential levels where scope-of-practice violations are a realistic risk.

## Impact If Built
Prevents scope-of-practice violations that could result in $10,000-100,000 in fines, license suspension, or malpractice exposure. Provides the first proactive (not reactive) compliance system for med spa operations.
