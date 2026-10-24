# The Engine Hours Nobody Downloaded

**Niche:** [[niches/powersports-and-boat-dealers/trade-in-appraisal-condition/profile|Trade-In Appraisal & Condition Assessment]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** Many modern outboards record hours by RPM band and fault history, and most trade appraisals still use the hour gauge and the owner's word.
**Tags:** #feature-engineering #data-integration #quick-win #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a used boat or machine at the moment of trade, and whoever has the smallest gap between the trade allowance plus reconditioning and the price the unit actually brings takes the account.

## The Problem
An outboard that spent its hours at wide-open throttle, or logged overheat and low-oil-pressure faults, is a different trade from one with the same hours at cruise. The data is in the engine's control module (recalled), readable with the OEM's diagnostic tool, but the download happens in the service bay, not at the trade desk.

## Why It's Still Broken
Diagnostic tools sit with technicians; appraisals happen in the lot with the customer waiting; and nobody has put the download into the appraisal step or the result into the appraisal record.

## What a Fix Looks Like
Make the engine download a standard appraisal step for engines that support it, by a technician on call or a portable reader, and attach the RPM-band hours and fault history to the appraisal with a plain-language summary of what they mean for value.

## Who Feels the Pain
Used-unit managers who overpay for hard-run engines; technicians who find the problem after the deal closed.

## Impact If Fixed
Catching ~1 hard-run or fault-logged outboard in 20 trades (estimate) avoids a powerhead or lower-unit repair of ~$3,000–10,000 per unit (estimate).
