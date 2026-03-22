# Lobby-to-Room Transition Bottleneck Elimination

**Niche:** [[niches/urgent-care/patient-flow-optimization/profile|Patient Flow Optimization]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Fix (Pain Point)
**One-liner:** UC clinics eliminate the single biggest flow bottleneck — the 10-20 minute gap between a patient being ready for a room and actually getting into one — by automating room turnover tracking and patient-to-room assignment.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #automation #worker-facing

## The Problem
The lobby-to-room transition is the most common bottleneck in urgent care flow. A patient completes triage and is ready to be roomed, but no room is available — or worse, rooms are available but nobody knows it because the previous patient was discharged 5 minutes ago and the room status has not been updated. The MA walks the hallway checking rooms physically, finds one that is empty but needs cleaning, radios for housekeeping, waits for room prep, then walks back to the lobby to call the patient. This cycle takes 10-20 minutes per patient transition. At a clinic with 40 patients per day, lobby-to-room transition time accounts for 400-800 minutes of total patient wait time daily — more than any other single workflow step. The problem is not room capacity (most UCs have 6-10 exam rooms for 30-50 daily patients) but room status visibility and turnover coordination.

## Why It's Still Broken
EHR systems track patient status (registered, triaged, in room, with provider, discharged) but do not track room status independently. A room becomes "available" when the patient is discharged in the system, but the room may still need cleaning, or the provider may be using it to chart on the previous patient. There is no system that monitors both patient readiness (triaged, waiting for room) and room readiness (clean, stocked, actually empty) simultaneously and auto-assigns the best match. Whiteboards and patient tracking boards show room assignments after they are made — they do not facilitate the assignment process itself. Room turnover is managed through informal coordination: MAs peek into rooms, charge nurses track occupancy mentally, and housekeeping responds to verbal or radio requests.

## What a Fix Looks Like
An automated room management system that: tracks room status in real time (occupied, patient discharged/provider charting, needs cleaning, clean/ready, out of service); integrates with the EHR to know when a patient is discharged from a room (triggering a cleaning request); notifies housekeeping via mobile device when a room needs turnover; marks the room as ready when housekeeping confirms completion; auto-assigns the next triaged patient to the nearest ready room based on patient needs (procedure rooms for lacerations, standard rooms for evaluations); and alerts the MA to room the patient. Time from patient-discharge-to-room-ready is measured and optimized. The charge nurse sees a real-time room status board showing all rooms with their current state and next assigned patient, replacing mental tracking and hallway walkthroughs.

## Who Feels the Pain
MAs who spend 20-30% of their shift physically checking room availability and coordinating room assignments. Patients who sit in the lobby watching empty rooms while waiting to be called. Charge nurses who mentally track room status for 6-10 rooms across 40+ patients per day. Providers who lose productive time waiting for their next patient to be roomed.

## Impact If Fixed
Reduces average lobby-to-room transition time from 12-18 minutes to 3-5 minutes. Decreases total door-to-door time by 8-15 minutes per patient — the single highest-impact flow improvement available. Reclaims 2-3 hours per day of MA time from room-checking to patient care. Reduces LWBS rate by 15-25% through faster visible progress (patients in rooms stop watching the lobby clock).
