# Class Schedule Construction

**Industry:** [[fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every platform in the category builds and publishes class schedules well, and the schedule itself is set by instructor availability and habit rather than by demand nobody has measured.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #feature-engineering #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
A studio's revenue is bounded by its schedule. Each class occupies a room for an hour with an instructor being paid, and either fills or does not. A grid with the wrong classes at the wrong times leaves capacity unsold at peak and pays instructors to teach four people at ten in the morning.

The grid is usually inherited. It was set when the studio opened, adjusted when an instructor left, and has otherwise persisted. Changes are made cautiously because regular members organise their lives around specific slots and react badly to disruption — which is a real constraint, and also the reason schedules ossify.

The information needed to do better is entirely present. The platform knows which classes filled, which had waitlists, which ran nearly empty, who attended what and when, which members were turned away, and what the studio's members' attendance patterns look like across the week.

What it produces is a booking page.

## What Already Exists
Class scheduling, booking, waitlists, capacity limits and instructor assignment are core functionality in every platform and work well. Waitlist management is standard. Reporting shows historical attendance per class. Some platforms surface utilisation summaries.

## The Customisation Gap
Nothing forecasts demand for a class that does not yet exist. The useful question — if we put a class of this type at this time with this instructor, how many would attend — requires learning from the pooled behaviour of comparable studios, because a single studio has never run that class at that time and has no data on it.

The waitlist is the clearest wasted signal in the category. A full class with eight people waiting is unambiguous evidence of unmet demand at that slot, and it is treated as a queue to manage rather than as a measurement.

Instructor effect is the second gap and the most sensitive. Attendance varies substantially by who is teaching, the platform can measure it, and no vendor has been willing to surface it because it is an employee performance metric attached to people who are frequently contractors with their own followings. There is a defensible version — modelling which instructor and class-type combinations draw well, used for scheduling rather than for ranking people — and it has not been built.

The third is cannibalisation: adding a class often moves existing members rather than attracting new ones, and distinguishing the two requires modelling member-level substitution, which nobody does.

## Impact If Solved
The schedule is the studio's production plan and it is set by habit. Fitting it to measured demand raises utilisation on fixed rent and fixed instructor cost, which is the most direct margin lever available to a business with almost no variable costs.
