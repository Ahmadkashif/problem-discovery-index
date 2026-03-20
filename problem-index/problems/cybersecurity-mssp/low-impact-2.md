# Client Security Posture & Gap Analysis

**Industry:** [[cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Security posture assessments exist as frameworks and checklists, but scoring a specific client's actual risk across their unique combination of tools, configs, and threat exposure is still a manual spreadsheet exercise.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #descriptive-statistics #compliance

## The Problem
MSSPs conduct security posture assessments during client onboarding and at quarterly or annual review cycles. An analyst reviews the client's firewall configs, endpoint protection coverage, patch management cadence, access control policies, vulnerability scan results, and incident history, then scores each control domain and identifies gaps. This assessment typically lives in a spreadsheet or slide deck, takes 8-15 hours per client, and produces inconsistent results depending on which analyst performs it. Between reviews, the posture drifts as configs change, new assets appear, and new vulnerabilities emerge — but the assessment stays static until the next cycle.

## What Already Exists
Security rating services like BitSight and SecurityScorecard provide external-facing posture scores based on internet-visible signals. CIS Benchmarks and NIST CSF provide standardized frameworks. Vulnerability management tools like Qualys and Tenable give patch-level visibility. But none of these integrate the MSSP's internal view — the SIEM alert patterns, the EDR detection coverage, the actual incident response history, and the client's business context — into a unified, continuously updated risk score.

## The Customisation Gap
An MSSP-specific posture scoring system needs to ingest telemetry from the client's actual deployed stack (which varies per client), weight control domains by the client's industry-specific threat model (a healthcare client has different risk priorities than a fintech client), incorporate the MSSP's own incident history for that client, and output actionable gap priorities — not just a letter grade. The scoring model must be explainable because the vCISO presents it to the client's board. Existing external rating tools measure the wrong signals (they see the outside; the MSSP sees the inside).

## Impact If Solved
Turns a periodic 8-15 hour manual assessment into a continuously updated dashboard, letting vCISOs walk into quarterly reviews with real-time data instead of stale snapshots. Improves upsell conversion by 20-30% because gap analysis directly maps to services the MSSP can provide.
