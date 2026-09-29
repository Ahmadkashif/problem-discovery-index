# Scheduling, No-Shows and Cancellation Policy

**Industry:** [[online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A cancelled session two hours before the slot is an hour of a tutor's evening that is now worth nothing, and the policy that governs it was written for the platform's conversion rate.
**Tags:** #gradient-boosting #time-series-forecasting #survival-analysis #confidence-intervals #convex-optimization #evaluation-metrics #worker-facing #revenue-impact

## The Problem
Tutoring is scheduled in discrete slots and the tutor's inventory is their evening. A slot held open for a student who cancels at short notice cannot be resold, and the tutor has usually also prepared for it.

Cancellation policies vary and generally favour the demand side, because the platform is competing for students and a strict policy deters booking. Late cancellations may carry a partial fee or none; no-shows may be compensated after a waiting period; and disputes about whether a session occurred resolve inconsistently.

Prediction is entirely absent. No-show and late cancellation risk is highly predictable from booking lead time, student history, time of day, subject, whether the session was booked by a parent or a student, and proximity to school holidays — and nothing surfaces it, so a tutor cannot fill a likely gap and the platform cannot prompt a confirmation.

Scheduling itself is manual and poorly supported. Tutors managing availability across time zones, recurring slots, exam-season surges and their own other commitments do so in a calendar interface designed for simple booking rather than for someone running a small business in fragments of evenings.

## What Already Exists
All platforms provide calendar-based booking with availability windows, reminders and rescheduling. Cancellation policies with fee structures are standard. Video classrooms handle delivery and attendance. Recurring booking is supported. Some platforms offer automatic reminder sequences and a few provide waitlists to fill cancelled slots.

## The Customisation Gap
Risk prediction is the obvious missing piece. Flagging a booking as high risk of cancellation, prompting an earlier confirmation, and offering the slot to a waitlist as soon as the risk crosses a threshold converts a lost evening into a filled one. The signals are all in the platform's own booking history.

Compensation policy should reflect the tutor's actual loss, which is the slot plus the preparation, and it should be graduated by notice period rather than applying a single cliff at a fixed number of hours. That is a policy design informed by prediction rather than a technical problem, and the data exists to set it defensibly.

Demand-aware scheduling is the third gap. Tutors currently set availability by guess; showing expected booking probability by slot, subject and season — exam periods in particular produce enormous predictable surges — would let a tutor allocate their scarce evening hours where they will actually be booked.

And the dispute resolution needs evidence. Whether a session occurred, for how long and who joined is recorded by the video system, and adjudicating attendance disputes from that record rather than from competing accounts is straightforward and is not consistently done.

## Impact If Solved
Late cancellations and no-shows are a direct and uncompensated loss to tutors who have both held the slot and prepared for it, and they are highly predictable from data the platform holds. Risk-based confirmation and waitlist filling recover much of the lost inventory, graduated compensation reflects the actual loss rather than a policy cliff, and demand-aware availability planning lets a part-time tutor put their limited hours where the bookings are.
