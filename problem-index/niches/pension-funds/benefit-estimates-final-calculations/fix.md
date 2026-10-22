# The Final Calculation Waiting on One Employer's Last Payroll

**Niche:** [[niches/pension-funds/benefit-estimates-final-calculations/profile|Benefit Estimates & Final Calculations]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Fix (Pain Point)
**One-liner:** A retiree receives an estimated payment for months because the final calculation waits on the last employer's final payroll report and leave cash-out.
**Tags:** #time-series-forecasting #workflow-orchestration #worker-facing #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce an estimate that matches the final benefit and a final benefit that never needs recalculating, and whoever issues final calculations within the plan's service standard with the fewest post-retirement recalculations takes the account.

## The Problem
Many systems pay a provisional benefit while the final calculation waits for the employer's last reports: final pay, leave payouts and contribution adjustments. The member's case sits in a queue, and an analyst checks it periodically to see if the data has arrived.

## Why It's Still Broken
The dependency on employer reporting is not tracked as a dependency. Cases are queued by date received, not by what they are waiting for, and employers are not told that a specific member's retirement is waiting on their file.

## What a Fix Looks Like
Track each pending final calculation's missing inputs by employer, chase employers automatically with the member named, and release cases to an analyst the moment the last input posts. Report average time-to-final by employer to the employer services team.

## Who Feels the Pain
Retirees on provisional payments; calculation analysts managing queues; counselors fielding "where is my final" calls.

## Impact If Fixed
Final calculations finish when the data arrives rather than when someone next looks, and the employers causing delays are visible.
