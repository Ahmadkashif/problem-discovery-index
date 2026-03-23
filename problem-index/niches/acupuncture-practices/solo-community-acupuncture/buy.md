# Scheduling Tool Adapted for Group-Room Sliding-Scale Model

**Niche:** [[niches/acupuncture-practices/solo-community-acupuncture/profile|Solo Community Acupuncture Practitioners]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic scheduling tools like Acuity and Calendly handle time-slot booking but cannot model group-room capacity, overlapping treatments, or sliding-scale payment at booking.
**Tags:** #automation #quick-win #worker-facing

## The Problem
Community acupuncture doesn't follow a one-patient-one-slot model. A practitioner might have 8 recliners and stagger patients every 10-15 minutes, with each patient staying 30-60 minutes. A booking tool needs to model room capacity (not provider availability), handle variable-length stays, and allow patients to self-select their sliding-scale rate at booking. No standard scheduling tool does this.

## What Already Exists
Acuity Scheduling, Square Appointments, and Calendly handle appointment booking. Jane App and Cliniko handle healthcare scheduling. All model appointments as "one provider, one time slot, one patient." None support a capacity-based model where 6-8 patients overlap in one room, and none integrate sliding-scale pricing where the patient chooses their rate from a range.

## The Customization Gap
The scheduling engine needs to shift from provider-availability to room-capacity logic: "this room has 8 chairs, 5 are occupied from 2:00-2:45, so 3 slots are open starting at 2:00 and 8 slots open at 2:45." It also needs integrated sliding-scale payment selection at booking time, so patients prepay at their chosen rate without awkward in-person negotiations. This is a UX and booking-engine logic problem, not a fundamental technology gap.

## Target Customer
Community acupuncturists currently using Google Calendar or paper sign-ups who lose 5-10 patients/week to scheduling friction.

## Impact If Solved
Reduces no-show rates by 20-30% through proper booking confirmation, increases daily patient volume by 10-15% through optimized chair utilization, and eliminates the in-person sliding-scale conversation that many patients find uncomfortable.
