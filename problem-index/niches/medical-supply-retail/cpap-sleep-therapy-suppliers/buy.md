# Compliance Risk Monitoring and Early Intervention

**Niche:** [[niches/medical-supply-retail/cpap-sleep-therapy-suppliers/profile|CPAP & Sleep Therapy Suppliers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** CPAP manufacturer platforms show compliance data, but none predict which patients will fail compliance before the 90-day deadline or trigger automated intervention workflows when usage patterns deteriorate.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #automation

## The Problem
Medicare requires CPAP patients to demonstrate compliance (4+ hours/night on 70%+ of nights) within the first 90 days. Suppliers check compliance data weekly in ResMed AirView or Philips Care Orchestrator, looking for patients who are trending below threshold. But by the time a patient shows non-compliance at day 60, it's often too late to intervene — they've developed poor usage habits and the equipment retrieval process begins. The compliance data shows current usage but doesn't predict future compliance trajectory. A patient using 5.2 hours/night at day 14 is fine, but a patient whose nightly usage has declined from 6 hours to 4.5 hours over the past week is at high risk — and current tools don't flag this trend.

## What Already Exists
ResMed AirView and Philips Care Orchestrator provide daily compliance dashboards with current usage metrics. Brightree can generate compliance reports. Some suppliers use manual spreadsheet tracking to monitor patients in the compliance window.

## The Customization Gap
The missing capability is predictive compliance scoring: at any point during the 90-day window, predict the probability that this patient will achieve Medicare compliance by day 90, based on usage trajectory (not just current usage), mask leak patterns (high leak drives discomfort and abandonment), pressure change events, and patient engagement signals (did they attend their follow-up appointment?). When a patient's predicted compliance probability drops below 70%, trigger automated intervention: first a coaching call from the respiratory therapist, then a mask adjustment appointment, then escalation to the prescribing physician. This requires combining device telemetry data with a predictive model trained on thousands of patient compliance outcomes.

## Target Customer
CPAP suppliers with 100+ patients in the active 90-day compliance window who want to shift from reactive compliance checking to proactive risk intervention.

## Impact If Solved
Reducing compliance failure from 18% to 10% on 500 new patients per year saves 40 equipment retrievals ($800-1,500 each = $32K-60K in direct costs) plus retains 40 patients for resupply revenue ($400-600/year each = $16K-24K in annual recurring revenue). Total impact: $48K-84K/year for a mid-size supplier.
