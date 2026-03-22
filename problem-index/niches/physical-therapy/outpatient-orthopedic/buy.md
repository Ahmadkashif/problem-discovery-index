# Practice Analytics Layer for PT EMRs

**Niche:** [[niches/physical-therapy/outpatient-orthopedic/profile|Outpatient Orthopedic PT Clinics]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** WebPT handles documentation and billing — but no tool gives a PT clinic owner operational BI showing visits per day, cancellation rates, revenue per visit, payer mix trends, and clinician productivity comparisons.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #data-integration #revenue-impact

## The Problem
PT clinic owners run multi-clinician practices generating $1M-$10M in annual revenue but operate with less business intelligence than a single-location coffee shop. They cannot pull a report showing: revenue per visit by payer and CPT code, clinician utilization rates (scheduled vs. completed visits), cancellation and no-show rates by day of week and time slot, payer mix concentration risk, or average visits per case by diagnosis. Every one of these metrics requires manual data export from WebPT or Prompt, followed by spreadsheet manipulation that takes hours and produces stale answers.

## What Already Exists
General-purpose BI tools (Tableau, Power BI, Looker) can visualize any data but require a data engineer to build connectors and transform PT-specific data models. WebPT has basic reporting — visits per day, revenue summaries — but lacks comparative analytics, trend detection, and clinician-level benchmarking. Prompt/Clinicient offers some practice reports but no predictive or alerting capability. Healthcare analytics platforms (Phreesia, Azara) target primary care and hospital systems, not outpatient PT.

## The Customization Gap
The missing piece is PT-specific business logic layered onto existing EMR data. A general BI tool doesn't know that a PT visit has multiple billable units calculated by the 8-minute rule, that cancellation patterns correlate with authorization expiry, or that payer mix shifts toward Medicare require different staffing models (PTAs can treat Medicare patients but with supervision requirements). The analytics layer needs to understand PT-specific concepts: units per visit, eval-to-discharge episode tracking, outcome measure completion rates, authorization utilization, and the distinction between new evaluations (high-revenue) and follow-up treatment visits (volume-dependent). It must also benchmark across clinicians fairly — adjusting for case mix complexity, not just raw visit counts.

## Target Customer
Clinic owners and practice managers at outpatient orthopedic PT practices (2-10 clinicians) who currently run their practices on gut feel and monthly billing summaries rather than real-time operational data.

## Impact If Solved
Surfaces 5-15% revenue leakage from under-coded visits, undetected cancellation patterns, and payer mix imbalances. Reduces practice owner time on manual reporting by 4-6 hours per week. Enables data-driven clinician performance conversations that improve utilization rates by 10-20% across the practice.
