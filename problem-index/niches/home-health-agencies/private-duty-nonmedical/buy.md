# Workforce Turnover Prediction on Scheduling Platforms

**Niche:** [[niches/home-health-agencies/private-duty-nonmedical/profile|Private-Duty Non-Medical Home Care]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ClearCare and AxisCare handle scheduling but don't predict which caregivers are about to quit — layering turnover risk scoring and burnout detection on existing scheduling data could cut the 60%+ annual turnover rate.
**Tags:** #logistic-regression #gradient-boosting #feature-engineering #evaluation-metrics #time-series-forecasting #worker-facing #revenue-impact

## The Problem
Home health aide turnover exceeds 60% annually across the private-duty industry, with the average aide lasting less than 9 months. Each departure costs the agency $2,500-$4,000 in recruitment, background checks, training, and lost revenue during the vacancy. Agencies learn an aide is leaving when they submit their two-week notice — or more often, simply stop showing up. By then it's too late for intervention. The behavioral signals of impending turnover (declining shift acceptance rates, increasing late clock-ins, shorter shift durations, more last-minute call-outs) are all captured in scheduling platforms but never analyzed.

## What Already Exists
ClearCare (WellSky Personal Care), AxisCare, and HHAeXchange all capture scheduling data — clock-in/out times, shift acceptance/rejection, call-outs, no-shows, overtime hours, and geographic coverage. These platforms report on past attendance but provide no predictive analytics. Generic HR analytics tools (Visier, Workday) exist but don't connect to home care scheduling systems and don't understand the hourly, shift-based workforce model.

## The Customization Gap
The scheduling platforms already have the raw data needed to predict turnover: shift acceptance rates trending down, increasing call-out frequency, shrinking geographic willingness, and declining hours worked per week are all strong signals. What's missing is a logistic regression or gradient-boosted model trained on historical aide tenure data that scores each active caregiver's turnover risk weekly, surfaces the top risk factors driving each score, and triggers manager interventions (schedule adjustment, raise consideration, case reassignment) before the aide reaches the decision to leave.

## Target Customer
Private-duty home care agencies with 30+ active aides, especially franchise operations and multi-location agencies where managers can't personally track every caregiver's engagement level.

## Impact If Solved
Identifying at-risk aides 4-6 weeks before departure and intervening successfully even 25% of the time would reduce annual turnover from 65% to approximately 50%, saving a 100-aide agency $100K-$150K annually in direct turnover costs and eliminating the revenue loss from unfilled shifts during vacancy periods.
