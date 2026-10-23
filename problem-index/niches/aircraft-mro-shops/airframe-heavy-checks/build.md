# Non-Routine Load Forecast Before Induction

**Niche:** [[niches/aircraft-mro-shops/airframe-heavy-checks/profile|Airframe Heavy Checks & Base Maintenance]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Heavy checks are quoted on the routine package plus a rule-of-thumb allowance, when the shop's own history could forecast the non-routine load by zone for this aircraft.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #confidence-intervals #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to absorb a check's non-routine findings without moving the redelivery date, and whoever forecasts the non-routine load before the panels come off takes the account.

## The Problem
Quoting estimators and planners add a non-routine allowance based on aircraft age and their own experience: this operator's aircraft come in corroded, that type always needs floor-beam work at this check. The allowance is a single number. When findings exceed it, the date slips and the change orders begin.

## Why Nobody Has Built This
Non-routine cards are written in free text, coded inconsistently by zone and cause, and rarely tied back to aircraft history from the previous check, which may have been done at a different MRO. Each base sees a few dozen checks per type per year, which feels too few for a model until history from several years is pooled.

## What to Build
A forecast at quote and induction of non-routine hours and parts by zone and ATA chapter, with a range, trained on the base's past checks. Features include aircraft type, age, cycles, operator, route environment, previous check findings from the records, and repair history. Free-text card descriptions are classified into consistent finding types first. As cards are raised, the forecast updates and shows the planner which zones are running hot. The estimator's adjustments to the forecast are logged, so their tacit allowance becomes visible and testable.

## Target Customer
Base maintenance directors and quoting teams at heavy-check MROs; airline maintenance planning departments sending aircraft out.

## Impact If Built
Quoting non-routine work within ±15% instead of ±40% (estimate) would let a base slot checks more tightly and cut late redeliveries. On a narrowbody C-check, every day saved is worth ~$10,000–$30,000 in customer lost revenue and slot value (estimate).
