# Buy: Appointment Scheduling Adapted to a Contractor's Held Slot

**Niche:** [[niches/online-tutoring-platforms/scheduling-and-session-ops/profile|Scheduling, Cancellation & Session Ops]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Appointment scheduling products manage a business's calendar; here the calendar belongs to a contractor whose held slot is their inventory and whose cancellation policy someone else writes.
**Tags:** #gradient-boosting #time-series-forecasting #evaluation-metrics #workflow-orchestration #data-integration #confidence-intervals #automation #worker-facing
**Contested on:** Whether scheduling infrastructure built for a business's own calendar can serve a marketplace of independent providers.

## The Problem

Appointment scheduling is thoroughly solved. Booking, calendar sync, time zones, reminders, rescheduling, waitlists, no-show tracking and payment on booking are available from many vendors, and the healthcare and salon segments have well-developed no-show prediction and recovery.

The products assume the calendar belongs to the business. A tutoring marketplace's calendars belong to thousands of independent contractors, each with their own availability across possibly several platforms, whose cancellation terms are set by the marketplace rather than by them, and for whom a held-then-cancelled slot is an uncompensated loss rather than an idle chair in a business they own.

## What Already Exists

Calendly, Acuity, Cal.com and the scheduling category. Healthcare appointment systems with mature no-show prediction and overbooking logic. Waitlist and slot-recovery features from the salon and clinic segment. Calendar sync, time zone handling and reminder infrastructure. Video conferencing with recording. Nothing here needs building.

## The Customization Gap

**The provider's availability spans platforms the system cannot see.** A tutor working on three marketplaces is double-bookable, and each platform's calendar is authoritative only over its own bookings. Cross-platform availability sync through the tutor's own calendar is the practical answer and no marketplace implements it, so tutors manage it manually and occasionally fail.

**The cancellation policy is a marketplace rule, not a provider setting.** Scheduling products let the business set its terms. Here the terms are set centrally, vary by jurisdiction and segment, and allocate cost between two parties neither of whom is the platform. That is a policy engine with an allocation model, not a settings page.

**No-show prediction exists in healthcare and has never been ported.** Clinic systems predict no-shows well and use it for overbooking and targeted reminders. The identical capability applied here would prevent a large share of cancellations, and the education segment has simply never looked at the healthcare literature.

**Slot recovery has to work across the marketplace, not within one calendar.** A salon fills a cancelled slot from its own waitlist. Here the freed hour could go to any family on the platform with an appetite for it, which is a marketplace matching problem the scheduling product has no concept of.

**Compensation has to be attached to the calendar event.** A cancelled session may trigger partial payment to the tutor, a credit to the family, or neither, depending on notice and history. Scheduling systems handle charges, not two-sided allocations with policy-dependent splits.

## Target Customer

Tutoring platforms building or replacing their scheduling layer, who need to know which parts to buy. Also the scheduling vendors, for whom multi-provider marketplaces with centrally-set policy are a recognisable and unserved pattern spanning several service verticals.

## Impact If Solved

The calendar, reminder, time zone and video machinery gets bought, and the cross-platform availability, the policy engine, the no-show prediction ported from healthcare, the marketplace-wide slot recovery and the two-sided compensation get built. Concretely: fewer cancellations, more of them refilled, and a tutor whose three calendars do not collide.
