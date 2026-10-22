# The Denominator Effect Discovered at the Board Meeting

**Niche:** [[niches/pension-funds/commitment-pacing-liquidity/profile|Commitment Pacing & Liquidity Planning]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Fix (Pain Point)
**One-liner:** After a market drop the private allocation sits above its range, and the board learns it from the quarterly report a month or more after it happened.
**Tags:** #time-series-forecasting #monte-carlo-methods #evaluation-metrics #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to forecast the programme's capital calls, distributions and NAV under stress well enough to set next year's commitment budget, and whoever keeps the plan inside its allocation ranges through a drawdown without forced sales of liquid assets takes the account.

## The Problem
Private NAVs are reported a quarter late. When public markets fall, the plan's reported private allocation rises mechanically, often past the policy range. Commitments already approved keep calling capital. The board then debates pausing commitments or selling secondaries on numbers that are already stale.

## Why It's Still Broken
Pacing is an annual study, and allocation compliance is measured on reported NAVs. Nobody owns a live estimate of the private allocation between quarter-ends.

## What a Fix Looks Like
A monthly nowcast of private NAV using each fund's last reported value rolled forward with public-market proxies and known cash flows. It shows the projected allocation against the range over the next eight quarters, and how much each pending commitment would move it. Breach probabilities go to the CIO before the board packet closes.

## Who Feels the Pain
CIOs explaining range breaches; boards asked to approve commitments during a drawdown; staff selling liquid assets to fund calls.

## Impact If Fixed
The plan sees a breach coming a quarter early and adjusts commitment timing deliberately instead of reacting in public.
