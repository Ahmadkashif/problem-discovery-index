# The Waitlist Nobody Treats as Data

**Niche:** [[niches/fitness-wellness-software/class-schedule-optimization/profile|Class Schedule Optimisation]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Fix (Pain Point)
**One-liner:** A waitlist is the clearest possible statement that demand exceeds supply at a specific hour, every platform has one, and it is used to fill cancellations rather than to tell the studio anything.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #time-series-forecasting #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in studio scheduling is fighting to build a grid from measured demand rather than from instructor availability and habit — and whoever raises revenue per class hour most takes the account.

## The Problem
The Wednesday 6:30 has been running at capacity with a waitlist for eight months. The waitlist does its job — when someone cancels, the next person gets in. What it does not do is tell anyone that this studio has been turning away several members a week from the same class for the better part of a year, which is both lost revenue and a retention risk, since a member who cannot get into the class they want will eventually find somewhere they can. The studio's reporting shows the class as full, which reads as success.

## Why It's Still Broken
The waitlist was built as a fill mechanism and is reported as one, so the number of people who joined it and never got in is not surfaced anywhere. Members who check a class, see it full and do not join the waitlist are invisible entirely, which means even the waitlist understates the demand. And a full class looks like a good outcome in every report a studio owner reads, which removes any prompt to investigate.

## What a Fix Looks Like
Report the waitlist as demand. Persistent unmet demand by class and time slot, showing how many members joined a waitlist and did not get in, over what period, and who they were — since the same members appearing repeatedly on the same waitlist is a specific and actionable retention risk, not a statistic. Capture the members who viewed a full class and did not join the waitlist, which is a small instrumentation change and roughly doubles the visible signal. Alert when unmet demand at a slot persists beyond a threshold, which is the prompt to add a class or a room that currently never comes. And connect it to retention: members repeatedly unable to attend their preferred class churn at a higher rate, which is measurable in the platform's own data and is the argument that converts a scheduling observation into an urgent one.

## Who Feels the Pain
Members who have been on a waitlist for the same class for months; owners whose full classes look like success and are partly refused business; and instructors teaching to a full room while the studio turns people away.

## Impact If Fixed
Unmet demand reporting is a report over data every platform already stores and is the single cheapest input to the grid decision. Linking it to the churn of the affected members is what makes it urgent rather than interesting, and that link is computable today from the platform's own records.
