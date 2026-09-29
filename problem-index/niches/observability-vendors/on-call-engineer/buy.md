# Shift Work Research and Workload Distribution

**Niche:** [[niches/observability-vendors/on-call-engineer/profile|The On-Call Engineer]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Healthcare, aviation and emergency services have decades of research on shift design, fatigue and handover, and software on-call rotas are designed by dividing a calendar by the number of volunteers.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #survival-analysis #evaluation-metrics #optimization-fundamentals #worker-facing #compliance
**Contested on:** Every serious competitor that takes this seriously is fighting to make on-call sustainable — fewer pages, better ones, fairly distributed, with the context attached — and whoever does that takes the engineering organisation, because on-call burden is a leading cause of the attrition that leadership actually feels.

## The Problem
Professions that have run on-call for a century have studied it: how long a shift can be before error rates rise, how much recovery time is required after a disturbed night, what makes a handover safe, how to distribute burden fairly across a team. There is a substantial literature and, in several industries, regulation. Software on-call rotations are designed by taking a calendar, dividing it by the number of people willing, and adjusting when somebody complains.

## What Already Exists
Fatigue and shift work research from healthcare, aviation and emergency services; structured handover protocols with demonstrated effect on error rates; rostering optimisation from workforce management with mature solvers; workload balancing methods; and burnout measurement instruments with validation behind them. All published, most of it free.

## The Customization Gap
The adaptation is to a rota where the work arrives unpredictably and is mostly absent. It requires: (1) measuring interruption rather than shift length, since an on-call week with two pages and one with forty are the same duration and entirely different experiences, and duration-based rules imported from other industries miss the variable that matters; (2) weighting night-time and sleep-disrupting pages far more heavily than daytime ones, which matches the fatigue literature and is not reflected in any current tooling; (3) rostering that balances expected page load rather than calendar days, using the historical distribution per service and per period, which is a straightforward optimisation and would materially change most rotas; (4) handover structured around what is unresolved and what is degraded rather than as a free-text message, borrowing directly from clinical handover protocols where the evidence is strongest; and (5) recovery treated as an entitlement after a disturbed night, which is normal in other industries and essentially absent in this one.

## Target Customer
Engineering leadership and site reliability functions, incident response and on-call platform vendors, and the workforce management vendors for whom this is an adjacent application.

## Impact If Solved
A mature body of shift-work research exists and has not been applied to a profession that runs continuous on-call. Interruption-weighted load and page-load-balanced rostering are the two adaptations, and structured handover is the change with the strongest external evidence behind it.
