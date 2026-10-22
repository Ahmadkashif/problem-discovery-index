# Unchecked Drawings Forced Into Submittal

**Niche:** [[niches/drafting-services/structural-steel-detailing/profile|Structural Steel Detailing]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Fix (Pain Point)
**One-liner:** The general contractor wants the steel submittal by Friday, so the fabricator tells the detailer to send the drawings before the checker has seen them, and the errors come back as "revise and resubmit" or as field fixes.
**Tags:** #large-language-models #evaluation-metrics #workflow-orchestration #compliance #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to deliver checked, approval-ready shop and erection drawings inside the fabricator's schedule with the fewest errors reaching the shop floor, and whoever can prove the lowest field-fix rate per ton takes the fabricator's account.

## The Problem
AISC 303 gives the owner's side 14 days to review steel approval documents, and every schedule downstream assumes the fabricator submits on time. When the schedule slips, the pressure lands on the last step before submittal, which is checking. NISD-linked guidance names the pattern: contractor pressure pushes fabricators to force detailers to submit unchecked, possibly incomplete drawings. The engineer's reviewer then becomes the checker, the drawings come back with corrections, and the schedule gets worse.

## Why It's Still Broken
Checking capacity is fixed by the number of senior people, the submittal date is fixed by someone else, and nothing records which sheets went out unchecked. Nobody upstream sees the cost, because the resubmittal is booked as normal review.

## What a Fix Looks Like
Make the check status of every sheet visible and recorded in the transmittal itself: checked, partially checked, unchecked, with the reason. Pair it with a triage that ranks unchecked sheets by risk, so the checker's last hours go to the sheets most likely to fail. Report resubmittal rates by check status, so fabricators and general contractors can see what forcing unchecked submittals costs them.

## Who Feels the Pain
Detailers and checkers working weekends before a submittal; fabricators paying for resubmittals and field fixes; engineers of record doing the detailer's checking for free.

## Impact If Fixed
Fewer resubmittal cycles inside the 14-day window, and a record that shows forcing unchecked drawings is slower, not faster.
