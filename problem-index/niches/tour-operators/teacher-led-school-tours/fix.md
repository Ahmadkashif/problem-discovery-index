# The Instalment Default Nobody Sees Until Final Payment

**Niche:** [[niches/tour-operators/teacher-led-school-tours/profile|Teacher-Led School Tours]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Fix (Pain Point)
**One-liner:** A family stops paying in month five of a fourteen-month plan, and the group finds out it is below minimum at final payment.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a teacher's interest into a departure that reaches its enrolment minimum, with parents paying in instalments over a year, and whoever converts the most teacher sign-ups into groups that actually travel takes the account.

## The Problem
Instalment plans make school trips affordable, and they also hide attrition. A missed payment triggers an automated reminder and little else. Families drop out quietly, and the group's real size is known only when final payment is due. By then hotel numbers and air names are close to fixed.

## Why It's Still Broken
Payment data lives in the billing system, enrolment counts in the leader portal and minimum numbers in operations. Nothing joins them into a group-level risk view, so a missed payment is treated as a billing event, not an enrolment one.

## What a Fix Looks Like
A simple early-warning score per family from payment history: missed or late instalments, card failures, plan changes. It rolls up to a group-level "likely to travel" count shown to the rep and the teacher months ahead. Families at risk get offers that fit the operator's terms, such as a plan change or a fundraising kit, before they drop out.

## Who Feels the Pain
Teacher-leaders whose group collapses late, operations staff reworking inventory, and the students who lose a trip because others dropped out.

## Impact If Fixed
Attrition is seen months earlier, giving time to recruit replacements or merge groups before inventory deadlines (estimate).
