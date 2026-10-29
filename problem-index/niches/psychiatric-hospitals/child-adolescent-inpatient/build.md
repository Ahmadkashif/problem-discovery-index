# Youth Readmission Risk With Family and School Inputs

**Niche:** [[niches/psychiatric-hospitals/child-adolescent-inpatient/profile|Child & Adolescent Inpatient Psychiatry]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Youth readmissions turn on things adult models never see, such as whether the family came to sessions, whether school re-entry is planned and whether a first outpatient visit is booked, and no tool scores discharge readiness on them.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #causal-inference #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to stabilise children and adolescents in crisis and return them to their families, and whoever has the lowest 30-day readmission rate for discharged youths takes the account.

## The Problem
A 14-year-old is discharged on day eight, calmer, to a home where nothing has changed and a school that has not been told, with a first appointment five weeks away. She is back in the ED in three weeks.

## Why Nobody Has Built This
Readmission models are built on adult claims, and the family and school facts live in social work notes and phone logs.

## What to Build
Capture family-session attendance, guardian engagement, safety-plan completion, school contact and the booked first visit as structured fields; train a readmission and time-to-readmission model on youth discharges; and give the team a pre-discharge checklist ranked by what most lowered readmission for similar youths. Development uses synthetic records.

## Target Customer
Child and adolescent medical directors at chains and children's hospitals, and Medicaid plans paying for youth readmissions.

## Impact If Built
If 30-day youth readmissions fall from ~15% to ~12% (estimate), a unit discharging 800 youths a year prevents ~24 readmissions, ~240 bed days at ~10 days each.
