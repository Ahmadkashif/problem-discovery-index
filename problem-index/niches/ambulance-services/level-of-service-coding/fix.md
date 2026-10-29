# Crew Addendum Requests Sent Days After the Run

**Niche:** [[niches/ambulance-services/level-of-service-coding/profile|Level-of-Service Coding & Medical-Necessity Review]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** The coder finds the gap a week after the run and asks the crew to add to the chart from memory, an addendum that is weak evidence and resented work.
**Tags:** #bert #transformers #workflow-orchestration #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to code each transport at the level its chart supports, and whoever keeps the most collected dollars per transport after denials and audit recoupments takes the account.

## The Problem
When a narrative does not support the level or the necessity, billing sends a query back to the crew. By then the crew has run thirty more calls. The addendum is written from memory, sometimes under pressure to support a higher level, and auditors give late addenda little weight.

## Why It's Still Broken
Coding happens after billing receives the chart, often at an outside firm. The ePCR checks only that required fields are filled, not whether the narrative supports the level.

## What a Fix Looks Like
Run the necessity and level check when the crew closes the chart. If the narrative does not support what was done, prompt the crew then, with the specific missing element (why the patient could not sit, what the ALS assessment found), while they still remember.

## Who Feels the Pain
Crews answering queries on days off; coders waiting on addenda; billing firms holding claims; and compliance officers worried about late, leading queries.

## Impact If Fixed
If 15% of charts now draw a query (an estimate) and checking at chart close removes half of them, an operator with 50,000 transports a year avoids ~3,750 late queries.
