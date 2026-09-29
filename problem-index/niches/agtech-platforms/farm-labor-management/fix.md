# The Minimum Wage Make-Up Computed From Reconstructed Hours

**Niche:** [[niches/agtech-platforms/farm-labor-management/profile|Farm Labour Management]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Piece-rate earnings must be topped up to at least minimum wage for the hours worked, the calculation depends on accurate hours, and in much of agriculture the hours are written down after the fact by a crew leader.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in farm labour software is fighting to make piece-rate pay, hours and compliance provable to the worker as well as to the regulator — and whoever makes the record trusted by both sides takes the operation.

## The Problem
A worker on piece rate has a slow day — the block was light, the fruit was poor, the weather stopped work twice. Their piece earnings fall below minimum wage for the hours they were present, and the employer owes the difference. Whether that is calculated correctly depends entirely on the hours record, which was written on a sheet by a crew leader who recorded a start and an end for the crew rather than for each person, and which does not capture the rest breaks and non-productive time that the calculation also requires. This is where wage and hour exposure in agriculture concentrates, it is the most commonly litigated area in the sector, and it is a measurement problem rather than an intent problem in the large majority of cases.

## Why It's Still Broken
Crew-level rather than individual hours recording is the practice because it is what a paper process supports, and it is precisely what makes the calculation unverifiable. Rest and recovery periods, non-productive time and heat-related breaks are separately compensable in several jurisdictions and are recorded, if at all, by attestation. Payroll providers compute from whatever hours they are given. And the parties who would benefit from accurate records — the workers — are the party with the least ability to insist on them.

## What a Fix Looks Like
Measure the hours individually and compute the make-up transparently. Individual clock-in and clock-out, with breaks recorded as they happen rather than assumed, gives the denominator the calculation actually requires — which is a device at the field edge and a badge, not a system. Rest and recovery periods and other separately compensable time are captured as distinct categories rather than folded into a day. The make-up calculation is then computed per pay period and shown to the worker with its arithmetic: these hours, this piece total, this rate, this top-up. Flag the days where make-up was required as a standing report, because a block or a crew leader generating frequent make-up is a signal about the work rather than the worker — light fruit, poor conditions, an unrealistic rate — and is information the operation should act on. Retain everything, since the employer's defence in a wage dispute is a contemporaneous record and the current defence is frequently a reconstruction.

## Who Feels the Pain
Workers whose top-up depends on hours they cannot verify; employers with genuine exposure arising from a paper process rather than from intent; and crew leaders asked to be the record-keeper for a calculation with legal consequences.

## Impact If Fixed
Individual hours capture is inexpensive and directly addresses the area of agricultural employment with the most litigation and the least reliable documentation. Showing the worker the arithmetic is the part that makes the record trusted rather than merely kept, and the make-up frequency report turns a compliance artefact into an operational signal the employer can use.
