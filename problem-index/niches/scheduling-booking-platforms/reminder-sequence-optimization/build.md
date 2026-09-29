# A Universal Feature Nobody Has Ever Tested

**Niche:** [[niches/scheduling-booking-platforms/reminder-sequence-optimization/profile|Reminder Sequence Optimisation]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Appointment reminders are shipped by every vendor, configured by every operator, and have never been evaluated against an alternative by anyone in the industry.
**Tags:** #hypothesis-testing #confidence-intervals #causal-inference #cross-validation #evaluation-metrics #descriptive-statistics #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to establish what a reminder should actually say, when, and through which channel, for whom — and whoever produces that evidence takes the category, because a feature deployed in every product has never been tested by anybody.

## The Problem
Twenty-four hours before, by text, with a standard wording. That is the industry's answer to the most expensive problem its customers have, and it is a convention rather than a finding. Nobody knows whether forty-eight hours works better for bookings made months ahead, whether a reminder requiring a reply outperforms one that does not, whether a second message adds anything, or whether including a cancellation link reduces no-shows by enabling a cancellation that frees the slot or increases them by putting the idea in someone's head. Every one of these is answerable with an experiment that would take a fortnight at the volumes these platforms carry.

## Why Nobody Has Built This
Reminders were an early feature that worked well enough, and features that work well enough are not revisited. The category commoditised quickly and competes on price and simplicity, which does not fund an experimentation programme. Individual operators cannot run their own experiments — a salon has nowhere near the volume to detect a three-point difference — and the vendors who do have the volume have never treated the question as theirs. There is also a mild disincentive: establishing that the current default is suboptimal is an admission about every prior year.

## What to Build
An experimentation programme over reminders, run by the vendor across its estate, with the results delivered to operators as defaults rather than as configuration. Test the obvious dimensions systematically: timing against lead time and appointment hour, one message against two, channel by sector and by customer age where known, wording variants including explicit confirmation requests, and the cancellation-link question, which is the one operators argue about most and which has a determinable answer. Stratify by sector, since a dental appointment and a personal training session are different behaviours and a pooled result will be wrong for both. Move to contextual policies once the main effects are established — the right reminder depends on the booking, and the same machinery that powers the no-show risk score selects the message. Report per-operator effects honestly, including where the effect is indistinguishable from zero, since a vendor that reports only its wins will not be believed twice. And publish the general findings, because in a category this commoditised, being the vendor who established what actually works is a durable position that a feature list is not.

## Target Customer
The platform vendors themselves, who alone have the volume; and operators, who receive the answer as a better default rather than as another setting to configure.

## Impact If Built
A feature universal across the category has never been evaluated, and the experiments are cheap, fast and unambiguous at platform volumes. The findings improve attendance for every customer simultaneously, which is a form of leverage no per-account feature has.
