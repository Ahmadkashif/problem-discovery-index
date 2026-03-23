# Cleaner No-Show Detection and Automatic Reassignment

**Niche:** [[niches/short-term-rentals/turnover-and-cleaning-operations/profile|Turnover & Cleaning Operations]]
**Industry:** [[industries/short-term-rentals|Short-Term Rentals]]
**Type:** Fix (Pain Point)
**One-liner:** When a cleaner no-shows on a turnover day, the operations manager discovers it 30-60 minutes into the cleaning window — by text message or missed checklist update — leaving 2-4 hours to find a replacement before guests arrive, a scramble that produces 3-5 guest-impacting incidents per month at a 50-property operation.
**Tags:** #automation #workflow-orchestration #worker-facing #quick-win

## The Problem
STR cleaning teams have 20-30% annual turnover rates, and daily no-show rates of 3-5% (illness, car trouble, personal emergencies). A cleaning coordinator managing 18 turnovers discovers at 11:30 AM that Cleaner C hasn't started their 11 AM assignment. The coordinator texts Cleaner C (no response), then scrambles to find a replacement — calling through their backup list while managing 17 other turnovers. By the time a replacement arrives, starts, and finishes, the guest check-in is delayed by 1-2 hours. This scenario repeats 3-5 times per month for a 50-property operation, each time risking a negative review.

## Why It's Still Broken
Breezeway and Turno send task assignments to cleaners but don't detect non-starts in real time. The coordinator relies on the cleaner's first checklist photo upload to confirm they've started — if the photo doesn't come, the coordinator notices the gap 15-30 minutes later (or doesn't, until the guest messages about an unready property). No cleaning platform has GPS-based arrival detection or non-start alerting that triggers automatic reassignment from a pre-configured backup pool.

## What a Fix Looks Like
An attendance and reassignment system that: (1) detects cleaner non-arrival at the expected start time (GPS proximity check or checklist non-start alert at T+10 minutes); (2) texts the assigned cleaner for status confirmation (arriving late vs. can't make it); (3) if no response within 10 minutes, automatically contacts backup cleaners from a pre-ranked backup list; (4) assigns the first available backup and sends them the property details and checklist; (5) notifies the operations manager only after reassignment is in progress, not at the point of crisis.

## Who Feels the Pain
Operations managers and cleaning coordinators who handle 2-5 no-show scrambles per month — each consuming 30-60 minutes of crisis management and risking guest-facing incidents.

## Impact If Fixed
Guest-impacting incidents from cleaner no-shows drop from 3-5 per month to under 1. Operations manager crisis management time drops from 3-5 hours/month to near zero (system handles reassignment automatically). Average delay from no-show incidents drops from 1-2 hours to 15-30 minutes (backup cleaner notified immediately instead of after 30-60 minute discovery delay).
