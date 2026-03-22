# 8-Minute Rule Compliance and Revenue Optimization Engine

**Niche:** [[niches/physical-therapy/hospital-based-outpatient/profile|Hospital-Based Outpatient PT]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hospital-based PTs get real-time guidance on CMS 8-minute rule unit counting during documentation — eliminating under-coding that loses revenue and over-coding that triggers audits.
**Tags:** #decision-trees #feature-engineering #evaluation-metrics #compliance #revenue-impact #automation

## The Problem
The CMS 8-minute rule governs how timed PT services are converted to billable units in outpatient hospital settings. A single session may include therapeutic exercise, manual therapy, neuromuscular re-education, and gait training — each tracked in minutes and converted to units using complex remainder rules. The therapist must count total timed minutes, allocate them across service codes, determine which codes qualify for an additional unit based on remainder minutes, and ensure the total units don't exceed what the time supports. Under-coding is common because therapists are conservative to avoid audit risk — studies estimate 8-15% revenue leakage from under-counting units. Over-coding triggers Medicare audits, recoupment, and compliance penalties. No tool provides real-time guidance during documentation.

## Why Nobody Has Built This
The 8-minute rule logic itself is well-defined but its application is context-dependent — it interacts with the specific combination of service codes documented in each session, the total treatment time, and payer-specific variations (some commercial payers use different unit-counting rules than CMS). Building this into Epic or Cerner requires working within those platforms' extension frameworks (Epic App Orchard, Cerner Open), which have long certification timelines and limited market access. Standalone tools can't access documentation data in real time because hospital EMRs don't expose session-in-progress data through standard APIs. The market is also split across health systems with different EMR configurations, making a universal solution difficult.

## What to Build
A real-time compliance assistant that integrates with the therapist's documentation workflow in Epic or Cerner. As the therapist enters timed service codes and minutes for a session, the tool: (1) calculates optimal unit allocation across all timed codes using 8-minute rule logic, (2) flags when the therapist's manual unit count differs from the calculated optimum, (3) identifies when additional remainder minutes justify an extra unit that the therapist would otherwise leave on the table, (4) provides a pre-submission compliance check showing the session's total units with supporting time documentation, and (5) generates an audit-ready time log. Post-session analytics show the rehab department's aggregate coding accuracy and estimated revenue impact of under-coding patterns.

## Target Customer
Rehab department directors and compliance officers at hospital-based outpatient PT departments who need to maximize legitimate reimbursement while maintaining CMS compliance — typically managing 10-50 therapists across one or more hospital locations.

## Impact If Built
Recovers 8-15% of lost revenue from systematic under-coding — worth $200K-$1M annually for a mid-sized hospital rehab department. Eliminates audit risk from over-coding by providing documented time-to-unit justification for every session. Reduces therapist documentation time by 3-5 minutes per session by automating the unit calculation that therapists currently do mentally.
