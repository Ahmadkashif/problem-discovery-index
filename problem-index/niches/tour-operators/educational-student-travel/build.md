# Air Blocks Committed Against Groups Still Recruiting

**Niche:** [[niches/tour-operators/educational-student-travel/profile|Educational & Student Group Travel]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Educational operators commit group air, hotels and guides for a whole season against school and university groups that are still recruiting, and size those commitments by rule of thumb.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #time-series-forecasting #revenue-impact #evaluation-metrics
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to be the organiser an educational institution trusts with its students abroad", but that splits into two contests with different winners. One is turning a K-12 teacher's sign-up into a trip that reaches its enrolment minimum, with parents paying in instalments. The other is getting a university's faculty-led programme through risk, academic and procurement review at a per-student price that holds. Decomposed into contested sub-niches below.

## The Problem
A teacher or professor signs up to lead a trip 12-18 months out (estimate) and then recruits students. Some groups fill fast. Others stall at four students, lose approval, or collapse when the leader changes school. The operator must book flights, hotels and guides for the season before most groups have finished recruiting. Air in particular is committed in group blocks with name deadlines.

## Why Nobody Has Built This
The large educational operators hold the data and treat enrolment analytics as internal sales operations. Smaller operators have too few groups to model alone. The signals that matter, such as a teacher's history, school characteristics, enrolment pace and payment-plan behaviour, are spread across CRM, payments and approval records.

## What to Build
A season-level inventory planner built on group-survival estimates. For each signed-up group, school or university, it estimates the probability of travelling, the expected final size and the date by which the outcome will be known. Inputs are leader history, enrolment and deposit pace, instalment defaults, institution type and approval status. It then aggregates those groups by destination, week and gateway airport into the number of air seats, hotel rooms and guide days to commit, with the penalty exposure of each commitment level. Group-level coaching for sales reps is a separate tool, set out under the teacher-led sub-niche.

## Target Customer
Heads of sales operations and inventory at educational tour operators, from the largest brands to regional specialists running a few hundred groups a year.

## Impact If Built
Committing air and hotel space against realistic group counts cuts name-deadline and attrition penalties on unused space without leaving late-filling groups stranded (estimate).
