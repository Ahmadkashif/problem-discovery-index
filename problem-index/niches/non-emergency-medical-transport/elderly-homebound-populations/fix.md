# Caregiver Coordination for Homebound Patient Pickups

**Niche:** [[niches/non-emergency-medical-transport/elderly-homebound-populations/profile|Elderly Homebound Populations]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Fix (Pain Point)
**One-liner:** Elderly homebound patients often cannot get to the door or prepare for pickup without a caregiver present, but NEMT scheduling does not coordinate with caregiver availability.
**Tags:** #automation #worker-facing #quick-win

## The Problem
Many elderly homebound patients depend on a family caregiver or home health aide to help them prepare for transport — getting dressed, gathering medical records, navigating to the door. When the NEMT vehicle arrives and the caregiver is not there (running late, unaware of the transport time, schedule conflict), the driver faces a dilemma: wait (falling behind on the route), attempt to assist a patient they do not know (liability risk), or mark a no-show and leave (patient misses the appointment). Caregiver-absence no-shows account for an estimated 5-8% of elderly NEMT trips — distinct from patient no-shows and preventable with basic coordination.

## Why It's Still Broken
NEMT scheduling treats the patient as the sole contact, but for homebound elderly patients, the caregiver is often the functional decision-maker and logistics coordinator. NEMT dispatch systems store one phone number per patient — usually the patient's — and send reminders to that number. The caregiver's contact information, availability windows, and preparation time requirements are not captured in any system. Home health aide schedules (managed by a separate home health agency) are never coordinated with NEMT pickup times, even when the aide is essential for the patient to be ready.

## What a Fix Looks Like
A multi-contact notification system that sends trip reminders to both the patient and the caregiver (family member and/or home health aide), with timing adjusted for preparation needs: if a patient requires 30 minutes of caregiver assistance to prepare, the caregiver alert fires 45 minutes before pickup. The system stores caregiver contact information and availability windows, flagging trips where no caregiver is available during the preparation period. For patients with home health aides, the system requests aide schedule data from the home health agency and flags conflicts before the trip is confirmed.

## Who Feels the Pain
Elderly patients who miss medical appointments because their caregiver was not present to help them prepare, NEMT drivers who arrive at homes where the patient cannot get to the door without assistance, and dispatchers who manage caregiver-related trip failures that are preventable with basic communication.

## Impact If Fixed
Reduces caregiver-absence no-shows by 60-70% (saving $15K-$40K annually per provider in wasted driver time and rebooking costs), ensures elderly patients do not miss critical medical appointments due to coordination failures, and reduces driver idle time by 20-30 minutes per day on elderly-heavy routes.
