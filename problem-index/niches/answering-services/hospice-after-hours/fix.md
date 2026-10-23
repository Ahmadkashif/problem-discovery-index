# The Family Who Called 911 While Waiting

**Niche:** [[niches/answering-services/hospice-after-hours/profile|Hospice & Home Health After-Hours Lines]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Fix (Pain Point)
**One-liner:** A frightened family waits twenty minutes for the on-call nurse to call back, gives up, dials 911, and the patient who chose to die at home goes to a hospital.
**Tags:** #time-series-forecasting #survival-analysis #workflow-orchestration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to tell, at 2 a.m., which family calls need a hospice nurse in the home and which a nurse can settle by phone, inside the agency's response standard, and whoever sends a nurse to every visit that needs one and to none that don't takes the account.

## The Problem
Hospice lines share the answering service's queue with every other account. The operator relays the message to the on-call nurse, who may be driving or on another visit, and the family hears nothing until the callback. The longer the silence, the more likely the family calls emergency services.

## Why It's Still Broken
The service measures its own answer time, not the time to nurse callback, and the agency rarely sees callback times at all. Nobody owns the gap between the relay and the call.

## What a Fix Looks Like
Hospice calls jump the queue. The operator tells the family when to expect the call and what to do meanwhile. Time to nurse callback is tracked live, with automatic escalation to a backup nurse at the agency's threshold, and the agency gets a weekly callback-time report.

## Who Feels the Pain
Families at the bedside; hospices facing unwanted transfers; on-call nurses blamed for delays they could not see.

## Impact If Fixed
Faster callbacks keep families from calling 911, which keeps patients where they chose to be.
