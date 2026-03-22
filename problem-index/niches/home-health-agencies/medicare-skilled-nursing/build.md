# Patient Deterioration Early Warning System

**Niche:** [[niches/home-health-agencies/medicare-skilled-nursing/profile|Medicare-Certified Skilled Nursing Agencies]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict patient hospitalizations from visit-to-visit vital sign trends, OASIS functional scores, and medication changes before clinical signs become obvious.
**Tags:** #gradient-boosting #time-series-forecasting #survival-analysis #feature-engineering #evaluation-metrics #tacit-knowledge-ml #data-integration #compliance #worker-facing

## The Problem
Experienced home health nurses develop intuition for when a patient is "going downhill" — subtle changes in skin color, appetite, cognition, and vital sign trajectories that individually seem minor but together signal impending hospitalization. This tacit clinical judgment takes years to develop and can't be taught from a textbook. When a patient is hospitalized within 30 days of a home health episode, the agency's Star Rating drops, PDGM payments may be clawed back, and the patient suffers an avoidable acute care event.

## Why Nobody Has Built This
Hospital early warning systems (NEWS, MEWS) rely on continuous monitoring data — ICU-level vital signs sampled every few minutes. Home health visits happen 2-3 times per week, producing sparse, irregularly-sampled data points. No one has built a deterioration model that works with visit-frequency data (blood pressure once every 3 days, weight once a week, functional status every 60 days). The data lives across OASIS assessments, visit notes, medication lists, and lab results that are rarely integrated in a single system.

## What to Build
A risk scoring engine that ingests visit-to-visit vital sign trends, OASIS functional assessment trajectories, medication change events, and diagnosis complexity to produce a daily hospitalization risk score for each patient on the census. The model would use gradient-boosted survival analysis trained on historical episode data with known hospitalization outcomes, flagging patients whose risk trajectory is accelerating. Clinicians see a dashboard of patients ranked by risk with the specific contributing factors highlighted, enabling early intervention visits.

## Target Customer
Medicare-certified home health agencies with 200+ active patients who are under CMS Star Rating pressure and need to reduce their hospitalization rates to maintain reimbursement levels and referral relationships with hospitals participating in bundled payment models.

## Impact If Built
A 15-20% reduction in avoidable hospitalizations would improve the agency's Star Rating by 0.5-1.0 stars, protect PDGM episode payments, and save $3,000-$12,000 per avoided hospitalization. For a mid-size agency with 500 active patients, this translates to $500K-$1M in annual value through retained revenue and avoided penalties.
