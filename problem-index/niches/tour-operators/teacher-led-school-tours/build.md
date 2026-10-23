# An Enrolment Forecast for Every Teacher's Group

**Niche:** [[niches/tour-operators/teacher-led-school-tours/profile|Teacher-Led School Tours]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators know how many students each teacher has enrolled today, not how many will travel or which groups need help now.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #causal-inference #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a teacher's interest into a departure that reaches its enrolment minimum, with parents paying in instalments over a year, and whoever converts the most teacher sign-ups into groups that actually travel takes the account.

## The Problem
A school tour operator may have thousands of teacher sign-ups in a season (estimate). Enrolment builds after each parent night, stalls, and sometimes reverses as parents drop out. Sales reps spread their attention evenly or follow the loudest teacher. Groups that will miss minimum are found at the enrolment deadline, when the only options are cancelling or merging with another school.

## Why Nobody Has Built This
The data needed sits with the operator: teacher history, parent-night date and attendance, enrolment curve, deposit and instalment behaviour, school demographics, and approval status. Operators have treated it as a sales report. Generic CRM forecasting predicts deals, not group enrolment against a minimum.

## What to Build
A model that, for each group, forecasts final enrolment and the probability of reaching minimum. It also estimates the effect of interventions on the curve: a second parent night, a co-leader from another school, a payment-plan extension, measured from the operator's own history. Reps get a weekly list of groups where help changes the outcome. Inventory planners get expected group counts for air and hotel commitments.

## Target Customer
Sales operations and inventory leaders at school tour operators.

## Impact If Built
More groups reach minimum and fewer are cancelled at the deadline. Teachers who travel once tend to lead again (estimate), so each saved group compounds into future seasons.
