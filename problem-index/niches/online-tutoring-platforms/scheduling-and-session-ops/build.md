# Build: Cancellation Prediction and Slot Recovery

**Niche:** [[niches/online-tutoring-platforms/scheduling-and-session-ops/profile|Scheduling, Cancellation & Session Ops]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict which bookings will be cancelled or missed, intervene before they are, and fill the slot when they still are.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #confidence-intervals #evaluation-metrics #time-series-forecasting #automation #worker-facing
**Contested on:** Whether a cancellation can be predicted early enough to prevent it or to refill the slot.

## The Problem

A tutor holds a Tuesday evening slot. At six o'clock, for a seven o'clock session, the family cancels. The tutor has prepared, has turned down other work for that hour, and cannot fill it.

Cancellations and no-shows are not random. They cluster: certain families, certain lead times, certain days, the week after a school holiday, the session booked three weeks in advance, the family who has cancelled twice already. Every one of these signals is in the platform's booking history and none is used.

Nor is the slot recovered. When a cancellation does happen, there is frequently a family somewhere who would take that hour — a student on a waiting list, a family wanting an extra session before an exam, a first-time booker browsing. The platform has both sides and matches neither.

## Why Nobody Has Built This

Cancellations are treated as a policy question rather than an operational one, and the policy team's concern is how much to charge rather than how many to prevent.

The tutor bears the cost, so the platform's own metrics barely register it. A cancelled session is a small refund and a rescheduling; it does not appear as a loss anywhere in the platform's accounting, which is why nobody has assessed its magnitude.

And slot recovery requires a real-time matching capability that the booking system, built around forward scheduling, does not have. A slot that becomes free in ninety minutes is a different product surface from a calendar three weeks out.

## What to Build

A prediction layer feeding intervention and recovery.

**Predict cancellation and no-show at booking and again as the session approaches.** Features: the family's own history, lead time, day and time, session number in the relationship, whether it was rescheduled before, time since last session, school calendar proximity, and whether the booking was made by a parent or a student. A gradient-boosted classifier on this is straightforward and the labels are abundant.

**Intervene where intervention works.** A high-risk booking gets a confirmation request 48 hours out rather than a reminder two hours out. This alone converts a meaningful share of would-be no-shows into either an attended session or an early cancellation the tutor can act on — and the second outcome is nearly as valuable as the first. Measure which intervention works for which pattern rather than sending everyone the same reminder.

**Warn the tutor.** A tutor who knows on Sunday that Tuesday's slot has a 40% cancellation risk can hold it more loosely, offer it conditionally elsewhere, or prepare less intensively. This costs the platform nothing and is the most immediately valuable output.

**Recover the slot.** When a cancellation happens, offer the freed hour to families likely to want it: students with the same tutor who have been increasing frequency, families on a waiting list, students approaching an exam, and — as a last resort — a discounted first session to a browsing new family. A push notification within minutes of the cancellation fills a share of slots that currently go empty, and the machinery is a small matching job over existing data.

**Track the cost.** Cancelled and missed session hours, by family, by tutor, by lead time, with the compensation paid and unpaid. No platform knows this number, which is why the policy has never been evaluated.

## Target Customer

Platform operations, where the internal case is tutor retention and slot utilisation. Tutor supply is the binding constraint in most markets at peak times, and unfilled cancelled slots are supply the platform already had and lost.

## Impact If Built

A meaningful share of cancellations get prevented by a better-timed intervention, and a share of the rest get refilled. Tutors get warning instead of a message at six o'clock. And the platform finds out what cancellations actually cost, which is the precondition for a policy that reflects it.
