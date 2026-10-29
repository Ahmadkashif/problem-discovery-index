# Patients Leaving Detox Before a Downstream Bed Opens

**Niche:** [[niches/psychiatric-hospitals/inpatient-detox-addiction-hospitals/profile|Inpatient Detox & Addiction Hospitals]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** Patients finish medically managed withdrawal before the residential programme has a bed or the payer has authorised it, and many leave the unit against advice in the gap.
**Tags:** #survival-analysis #logistic-regression #workflow-orchestration #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to carry patients through medically managed withdrawal into continuing treatment, and whoever has the highest share of detox discharges starting the next level of care within seven days takes the account.

## The Problem
Withdrawal is managed in four days; the residential bed opens on day seven. The payer will not pay detox days once withdrawal scores are low, so the patient goes home to wait, and often does not come back.

## Why It's Still Broken
Detox and residential care are separate providers, paid under separate authorizations, with no shared view of beds or timing.

## What a Fix Looks Like
Start placement at admission, forecast the discharge day from withdrawal scores, and hold a bed or arrange a bridge (medication for opioid use disorder, daily outpatient visits, recovery housing) that starts the day after discharge.

## Who Feels the Pain
Patients and families, aftercare coordinators and addiction physicians.

## Impact If Fixed
If ~20% of detox patients leave against advice (estimate) and bridging cuts that by a quarter, a unit admitting 1,500 patients a year keeps ~75 more in care through discharge.
