# Tenant Access Coordination for Unit Audits

**Niche:** [[niches/energy-auditors/multifamily-retrofit-auditors/profile|Multifamily Retrofit Auditors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Fix (Pain Point)
**One-liner:** Auditors schedule visits to individual apartments but 30-40% of tenants are unavailable or unresponsive, requiring multiple site visits to complete the sample.
**Tags:** #automation #worker-facing #quick-win

## The Problem
Auditing 15 units in a 100-unit building requires scheduling individual appointments with 15 tenants — each with different work schedules, language preferences, and levels of cooperation. Property management sends a building-wide notice ("Energy audit team visiting units on March 15-16"), but tenants ignore it, forget, or refuse access. On audit day, the auditor arrives to find 5 of 15 scheduled units inaccessible: 3 tenants are not home, 1 refuses entry, and 1 did not receive the notice. The auditor must select replacement units from whoever is available, potentially biasing the sample. If insufficient units are accessible, the auditor must schedule a return visit — adding a full day of field time ($1,500-$3,000 in cost) for what should have been 2-3 additional unit audits.

## Why It's Still Broken
Tenant communication is the property manager's responsibility, but property managers have limited incentive to prioritize audit access coordination — the audit benefits the building's energy performance, not the manager's daily operations. Auditors have no direct relationship with tenants and no communication channel to reach them. Multilingual buildings add language barriers: a notice in English does not reach Spanish-speaking or Mandarin-speaking tenants. The property manager sends a single notice and considers their obligation fulfilled, regardless of whether tenants actually received and understood it.

## What a Fix Looks Like
A tenant coordination tool that: generates multilingual access request notices (email, SMS, printed door notice) personalized with the specific date, time window, and purpose of the visit; tracks tenant confirmations with automated reminders at 7 days, 3 days, and 1 day before; identifies backup units that match the sampling criteria if primary selections are unavailable; and provides the auditor with a real-time dashboard on audit day showing confirmed, unresponsive, and refused units with recommended alternates. The tool integrates with property management systems (Yardi, AppFolio) to pull tenant contact information and unit details.

## Who Feels the Pain
Field auditors who arrive at buildings to find 30-40% of scheduled units inaccessible, requiring return visits that cost $1,500-$3,000 each. Property managers who field tenant complaints about unannounced visits when the notice was inadequate. Audit firms whose project timelines slip by weeks due to access coordination failures.

## Impact If Fixed
Increases first-visit unit access rates from 60-70% to 85-90%, reducing return visits by 50-60%. Saves $1,500-$3,000 per avoided return visit and compresses project timelines by 1-2 weeks per building.
