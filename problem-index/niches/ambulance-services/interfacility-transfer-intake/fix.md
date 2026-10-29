# The Same Ward Ordering BLS for Patients on Drips

**Niche:** [[niches/ambulance-services/interfacility-transfer-intake/profile|Interfacility Transfer Intake & Level-of-Care Matching]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** One hospital unit keeps requesting basic crews for patients on infusions, every crew that arrives has to cancel or call for an upgrade, and nobody tells the unit.
**Tags:** #logistic-regression #data-integration #workflow-orchestration #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a hospital's or nursing facility's transport request into the right crew at the door, and whoever has the lowest share of interfacility transports billed at a different level of service from the one dispatched takes the account.

## The Problem
Level mismatches cluster. A few units or facilities account for most of them, because their staff describe patients in a way the call-taker misreads, or because they request the cheapest level by habit. Crews know which ones; the operator's data does not.

## Why It's Still Broken
Upgrades and cancellations are logged as CAD comments and ePCR narrative, not as coded events tied to the requesting unit. Account managers hear about them as anecdotes.

## What a Fix Looks Like
Code every mismatch at the time it happens: the crew taps "level wrong at pickup" with the reason, and the coder marks "billed below dispatched". Report by requesting unit monthly to the operator's account manager and the hospital's transfer-centre director, with the specific questions that would have caught each one.

## Who Feels the Pain
Crews sent to patients they cannot carry; patients waiting longer for the right crew; hospitals with beds blocked; and operators eating the cost of wasted runs.

## Impact If Fixed
If three units cause half of a hospital's mismatches and feedback cut theirs by half (an estimate), a hospital generating 100 mismatched runs a year would see ~25 fewer.
