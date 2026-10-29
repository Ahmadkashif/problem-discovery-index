# Psychiatric Leakage and Bed-Need Model for a Partner System

**Niche:** [[niches/psychiatric-hospitals/health-system-psychiatric-jvs/profile|Health-System Joint Ventures & Hospital-Based Psychiatric Units]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A health system cannot say how many of its psychiatric patients it sends to other hospitals, by age group and diagnosis, so it sizes JV beds on a consultant's one-off study.
**Tags:** #time-series-forecasting #gradient-boosting #descriptive-statistics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to run a health system's inpatient psychiatric capacity for it, and whoever keeps the largest share of the system's psychiatric admissions in the system's own beds takes the account.

## The Problem
Adolescents, older adults with dementia and patients with medical complexity are the ones most often transferred out, and each transfer is lost revenue and a long ED stay. The data sits in the system's ED records, transfer centre logs and the JV's admissions log, never joined.

## Why Nobody Has Built This
The JV operator sees only who it admits, and the system sees only who left its ED. Bed-need studies are one-off consulting reports.

## What to Build
A monthly model that joins ED psychiatric encounters, transfers out with destination, the JV's admissions and declines with reasons, and payer mix. It reports leakage by age band, diagnosis and payer and forecasts bed need by unit type for the next 12–36 months. Demonstrations run on synthetic encounter data.

## Target Customer
Health-system strategy and service-line leaders, JV boards, and chains pitching new JVs.

## Impact If Built
If a system sending ~1,200 psychiatric patients a year elsewhere keeps 20% more of them in its JV (estimate), it adds ~240 admissions, roughly ~2,400 patient days at ~10 days each.
