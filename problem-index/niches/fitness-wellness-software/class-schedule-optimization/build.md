# The Grid Designed From Measured Demand

**Niche:** [[niches/fitness-wellness-software/class-schedule-optimization/profile|Class Schedule Optimisation]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A studio's class grid commits its entire cost structure and is set by instructor availability and the owner's habits, while the platform has measured exactly when people want to train since the day the studio opened.
**Tags:** #time-series-forecasting #gradient-boosting #optimization-fundamentals #combinatorics-and-counting #confidence-intervals #evaluation-metrics #revenue-impact #transfer-learning
**Contested on:** Every serious competitor in studio scheduling is fighting to build a grid from measured demand rather than from instructor availability and habit — and whoever raises revenue per class hour most takes the account.

## The Problem
A studio runs twenty-eight classes a week. The Tuesday 12:15 averages four attendees and has since it was added because an instructor was free. The Wednesday 6:30 runs full with a waitlist of nine every week. The Saturday 8am is full and the Saturday 11am is empty. The owner knows some of this and has never quantified any of it, and changing the grid means a conversation with instructors whose schedules depend on it, so the grid persists. The cost of the four-person class is the instructor's pay and the room; the cost of the nine-person waitlist is nine members who wanted to attend and could not, several of whom will eventually go somewhere they can.

## Why Nobody Has Built This
Scheduling products were built to publish a grid rather than to design one, and demand modelling requires treating bookings as a censored observation — a full class does not tell you how many wanted in, which is exactly the information a grid decision needs. Handling that properly requires waitlist and attempted-booking data, which is either not captured or not used. And schedule changes are socially expensive, so owners avoid them, which means there is little demand for a tool that recommends them until the recommendation comes with enough evidence to justify the conversation.

## What to Build
A demand model by time slot and format, and a grid recommendation against it. Demand is estimated with the censoring handled — waitlists, attempted bookings on full classes and the platform's cross-studio patterns for comparable formats and neighbourhoods together give an estimate of true demand rather than of observed attendance. Revenue per class hour is computed per slot against instructor cost, which is the number that should govern and that no studio currently sees. Recommendations are specific and incremental: move this class thirty minutes, replace this format at this hour with that one, add a second class at the hour with a persistent waitlist, remove the one that has averaged four for a year. Each comes with the expected effect and the evidence, which is what makes the instructor conversation possible. Changes are tracked and evaluated afterwards, so the studio learns rather than guesses — and a change that did not work is reversed on evidence rather than on nerve.

## Target Customer
Studio platforms, multi-location operators with programming teams, and independent owners whose grid has not changed in three years.

## Impact If Built
Revenue per class hour varies by a large factor across a typical grid and the variation is not random — it is a small number of slots that are wrong. Fixing those is the cheapest revenue improvement available to a studio, and it requires no new members, no price change and no additional space. The waitlist finding in particular usually identifies demand the studio is refusing every week.
