# Family Burden Dashboard with Missed Shift Tracking

**Niche:** [[niches/home-health-agencies/pediatric-home-health/profile|Pediatric Home Health]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Parents of medically complex children become unpaid 24/7 caregivers when nursing shifts go unfilled — but no system tracks missed shift patterns, cumulative family burden, or connects families to respite resources before burnout becomes crisis.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #worker-facing #data-integration #automation

## The Problem
When a pediatric home health nurse calls out and no backup is found, the parent covers the shift — performing tracheostomy suctioning, ventilator monitoring, medication administration, and feeding throughout the night while also managing their other children, their job, and their own health. Missed shifts happen 15-25% of the time. For a child authorized for 16 hours/day of nursing, missing even 2 shifts per week means the parent is providing 24-32 additional hours of skilled medical care. This burden is invisible to the agency: there's no system tracking which families are absorbing the most unfilled shifts, no cumulative burden score, and no automated connection to respite care services that could provide relief.

## Why It's Still Broken
Agencies track missed shifts as a staffing metric (% of shifts filled) but not as a family burden metric. The data exists — scheduling systems know which shifts went unfilled for which patient — but no one aggregates it at the family level over time. Respite care resources (state Medicaid respite programs, nonprofit organizations, faith-based respite services) exist but families don't know about them, and agencies don't have a systematic way to identify which families need referrals. The agency's operational focus is on filling shifts, not on measuring the downstream impact when they can't.

## What a Fix Looks Like
A family burden dashboard that: (1) tracks unfilled shifts per patient over rolling 30/60/90-day windows, (2) calculates a cumulative family burden score based on unfilled hours, shift timing (overnight vs. daytime), and consecutive unfilled days, (3) triggers alerts when a family's burden score exceeds configurable thresholds, (4) auto-generates referrals to applicable respite care programs (state Medicaid respite, nonprofit organizations, VA caregiver support for military families) based on the family's eligibility, and (5) reports to the agency's management team which patients have the highest unfilled shift rates so staffing recruitment can be prioritized.

## Who Feels the Pain
Parents and family caregivers of medically complex children who absorb 20-40+ hours per week of unpaid skilled nursing when shifts go unfilled. Clinical directors who don't realize the severity of specific families' situations until a crisis occurs — a parent's health collapse, a child's emergency room visit triggered by exhausted caregiving.

## Impact If Fixed
Identifying high-burden families 4-6 weeks before crisis and connecting them to respite resources would reduce family caregiver burnout-related ER visits and child welfare referrals. For the agency, reducing the correlation between unfilled shifts and patient disenrollment (families who leave due to unreliable coverage) would protect $200K-$500K in annual revenue per 10 retained patients.
