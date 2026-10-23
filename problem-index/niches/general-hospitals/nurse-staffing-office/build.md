# Shift Offers Priced by Who Will Actually Say Yes

**Niche:** [[niches/general-hospitals/nurse-staffing-office/profile|Nurse Staffing Office & Contingent Labour]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hospitals post open shifts with flat incentive bonuses and escalate to agency when nobody bites, without knowing which of their own nurses would have taken the shift at what price.
**Tags:** #logistic-regression #gradient-boosting #causal-inference #time-series-forecasting #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to fill tomorrow's open shifts from the hospital's own nurses before agency and travel staff are called, and whoever covers the most shifts at core rates without breaching ratios takes the account.

## The Problem
An open night shift on a step-down unit is posted with a $10-an-hour incentive. Nobody takes it, so at 16:00 the bonus doubles and at 18:00 the office calls the agency at ~$91+ an hour. The hospital's own history shows which nurses pick up which shifts, on which days, after how much rest and at what incentive. It is never modelled.

## Why Nobody Has Built This
Scheduling systems record shifts worked, not offers declined. Incentive programmes are set by policy and union contract. Pricing a nurse's willingness raises fairness questions that vendors avoid.

## What to Build
A model of shift acceptance probability per nurse, given unit, skill, shift, day, recent hours, fatigue rules and incentive level, trained on offer-response logs captured from the shift app. It forecasts gaps 72 hours out from census and call-out patterns. Offers go out early, in order of likelihood, at the lowest incentive that fills the shift in time. Fairness and fatigue caps are hard constraints, and the rules are published to nurses.

## Target Customer
Directors of staffing and CNOs at systems spending heavily on travel and agency nurses.

## Impact If Built
Converting ~10–20% of agency-filled shifts to internal fills (estimate) saves the gap between ~$91 an hour and core plus incentive. That is millions a year for a mid-sized system.
