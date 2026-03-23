# Patient Continuity Tracking Without Charting Overhead

**Niche:** [[niches/acupuncture-practices/solo-community-acupuncture/profile|Solo Community Acupuncture Practitioners]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Community acupuncturists see so many patients per day that they cannot remember individual treatment histories, but full charting would consume more time than the treatments themselves.
**Tags:** #llm #text-generation #nlp #worker-facing #quick-win

## The Problem
A community acupuncturist treating 35-50 patients daily cannot retain individual patient histories — which points were needled last visit, what worked, what didn't. Traditional SOAP documentation takes 5-8 minutes per patient, but the entire treatment interaction is only 10-15 minutes. Practitioners either skip documentation entirely (risking continuity failures and liability exposure) or spend their evenings catching up on notes, adding 2-3 unpaid hours daily.

## Why It's Still Broken
The documentation standards in acupuncture were designed for the private-practice model where a practitioner sees 8-12 patients daily and has time for detailed charting. Community acupuncture's 4-5x higher volume makes this standard impossible to maintain. No one has built a documentation tool optimized for "capture the minimum needed for continuity in under 30 seconds per patient."

## What a Fix Looks Like
A voice-or-tap documentation tool that captures: chief complaint (from a quick-select menu of common conditions), points needled (tap on a body map), patient response (improved/same/worse), and any notes (15-second voice memo auto-transcribed). Total input time under 30 seconds. Before the next visit, the practitioner gets a 2-line summary: "Last visit: GB-34, LI-4, ST-36 for lower back pain — patient reported 40% improvement. Suggested follow-up: add BL-40."

## Who Feels the Pain
Solo community acupuncturists who either work 2-3 extra hours daily on notes or operate with no documentation, relying on memory for 200+ active patients.

## Impact If Fixed
Eliminates 10-15 hours/week of after-hours documentation, reduces treatment continuity errors, and provides basic liability protection through minimal-but-structured records.
