# Scheduling, Cancellation & Session Ops

**Parent Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether the policies governing a cancelled or missed session are set against the cost they impose or against the platform's conversion rate.

## Profile
**Market Size:** ~$640M — 8% of US online tutoring
**Share of Parent Industry:** ~8%
**Digital Adoption:** High — booking and video work well; the policies around them do not
**Target Buyer:** Platform operations and product leadership
**Automation Potential:** Very high — the policy is a rule and the prediction is well-posed

## What Makes This a Distinct Niche

A cancelled session two hours before the slot is an hour of a tutor's evening that is now worth nothing, and the policy that governs it was written for the platform's conversion rate.

Scheduling infrastructure in this industry is good. Calendars, time zones, booking, reminders, video and payment all work. What is contested is the policy layer sitting on top: how much notice a cancellation requires, what a no-show costs, who bears a technical failure, whether a tutor can decline a booking without penalty, and how a repeatedly-cancelling family is handled.

These policies are written by growth teams optimising booking conversion, and every one of them resolves the same way — in favour of the party who might not book. The cost lands on the tutor, who has held the slot, prepared for it, and cannot fill it at two hours' notice.

## Current Tools & Gaps

Calendar and booking systems with time zone handling, automated reminders, rescheduling flows, video delivery with recording, and payment on completion. Cancellation windows exist, usually twelve or twenty-four hours, sometimes with partial compensation. No-show policies exist and are inconsistently enforced.

The gaps are prediction and allocation. Cancellations and no-shows are highly predictable from booking history, lead time, family patterns and time of day, and nobody predicts them — so nobody warns the tutor, offers the slot elsewhere, or intervenes with a reminder that would have worked. And the cost allocation is set by growth rather than by who imposed it, which is why the tutor absorbs a family's habitual late cancellations indefinitely.

## Problems
- [[niches/online-tutoring-platforms/scheduling-and-session-ops/build|🔨 Build: Cancellation Prediction and Slot Recovery]]
- [[niches/online-tutoring-platforms/scheduling-and-session-ops/buy|🛒 Buy: Appointment Scheduling Adapted to a Contractor's Held Slot]]
- [[niches/online-tutoring-platforms/scheduling-and-session-ops/fix|🔧 Fix: The Policy Was Written for the Conversion Rate]]
