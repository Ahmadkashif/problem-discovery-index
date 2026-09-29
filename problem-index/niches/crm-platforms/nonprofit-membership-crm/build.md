# Lapse Prediction From Giving Behaviour

**Niche:** [[niches/crm-platforms/nonprofit-membership-crm/profile|Nonprofit & Membership CRM]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Donor retention is the sector's dominant economic problem, a lapsing donor's giving pattern degrades visibly for a year or more beforehand, and the database that holds every gift offers no warning.
**Tags:** #survival-analysis #gradient-boosting #change-point-detection #confidence-intervals #evaluation-metrics #logistic-regression #revenue-impact #cross-validation
**Contested on:** Every serious competitor in donor and member software is fighting to attribute a gift or a renewal to what actually caused it — and whoever answers that credibly takes the development office.

## The Problem
A donor gave annually for eleven years, usually in December, in an amount that grew slowly. Two years ago the gift came in March instead and was smaller. Last year it came after a second reminder. This year it has not come. The development office notices in January when the year-end totals are reconciled, sends a lapsed-donor appeal, and mostly does not get them back — because a donor who has drifted for two years has a reason, and a generic letter in January does not address it. Every signal was in the database: the timing drift, the amount decline, the increased number of solicitations required, the declining event attendance, the unopened emails.

## Why Nobody Has Built This
Nonprofit software is bought by organisations with small budgets and little technical capacity, and the vendors have competed on breadth of function — gift entry, receipting, event management, grant tracking — rather than on analysis. Retention is discussed constantly in the sector and addressed with practice guidance rather than with instruments. And the products that do segment tend to do it by recency, frequency and amount thresholds, which is a 1980s direct mail technique applied to a problem where the trajectory rather than the level is the signal.

## What to Build
A lapse risk estimate per donor from their own giving trajectory, with a prescribed action. Risk is modelled from the pattern relative to that donor's own established behaviour — timing drift, amount trend, solicitations required per gift, channel changes, event and volunteer engagement, communication response — rather than from an absolute recency threshold, since a donor who always gave once a year in December and still does is not at risk and a monthly donor who missed two months is. Survival methods handle the censoring, since active donors are the population of interest. The output is a short prioritised list with a suggested action: a call from a board member, a programme update on the thing they fund, an invitation, or simply a thank-you with no ask — which is the intervention the sector's own practice literature most recommends and which nobody times well because nobody knows when to make it. Effectiveness is measured against a holdout, which is the only way a small organisation can tell whether its retention effort does anything.

## Target Customer
Nonprofit and association software vendors, development offices at organisations large enough to act on a list, and the consultancies advising the sector on retention.

## Impact If Built
Donor retention rates in the sector are low enough that retention improvement is worth more than acquisition improvement to almost every organisation, and the intervention window — a year or more of visible drift — is unusually generous. For a development office with three staff, a prioritised list of twenty donors to call this month is a materially different instrument from a lapsed-donor mailing in January.
