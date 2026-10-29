# Units Held at the Hospital Wall Missing From the Coverage Map

**Niche:** [[niches/ambulance-services/system-status-deployment/profile|System Status Management & 911 Unit Deployment]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** A unit waiting an hour to hand a patient to an overcrowded emergency department shows "at hospital" in CAD, and the posting plan treats it as about to clear.
**Tags:** #survival-analysis #gradient-boosting #data-integration #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep an available ambulance within reach of every zone of a county 911 contract around the clock, with the unit-hours the contract funds, and whoever has the fewest priority-1 calls arriving when the zone has no available unit (level-zero calls) per 1,000 priority-1 responses takes the account.

## The Problem
Ambulance patient offload delay, the time a crew waits at the hospital before the ED takes over the patient, removes units from coverage unpredictably. CAD records arrival and clear times but does not predict when a unit at a given hospital will be free, so controllers discover the hole only when the next priority-1 call arrives in a zone with no unit available.

## Why It's Still Broken
The delay is caused by the hospital, which has no contractual duty to the ambulance operator, and the information about ED crowding lives in the hospital's systems. Operators record wall time after the fact for complaints to the county, not for live planning.

## What a Fix Looks Like
Predict each unit's remaining time at hospital from its history at that ED by hour and day, the number of other units already waiting, and any crowding signal the hospital shares. Show it on the coverage map, so controllers move units before the hole opens and the operator has evidence for the county's wall-time discussions.

## Who Feels the Pain
Controllers making blind moves; crews stuck in hallways; operators answering to the county for zones left empty by hospital delays; and county EMS agencies trying to quantify the problem.

## Impact If Fixed
If a contract with 5,000 priority-1 responses a month runs at 40 level-zero calls per 1,000 (an estimate), it has ~200 level-zero calls a month. If a quarter follow a hole left by wall time (an estimate) and predicted clear times prevent a fifth of those, ~10 fewer calls a month, ~120 a year, would arrive with no unit free.
