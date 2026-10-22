# An Estimate That Knows Which Parts of the Record Are Unverified

**Niche:** [[niches/pension-funds/benefit-estimates-final-calculations/profile|Benefit Estimates & Final Calculations]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Members plan their retirement on an estimate computed from a record nobody has verified, then receive a different final number.
**Tags:** #gradient-boosting #confidence-intervals #feature-engineering #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to produce an estimate that matches the final benefit and a final benefit that never needs recalculating, and whoever issues final calculations within the plan's service standard with the fewest post-retirement recalculations takes the account.

## The Problem
An estimate prints a single monthly figure. Behind it may be an unreconciled leave of absence, a service purchase still being paid, a salary spike that a compensation review will cut, or a period of part-time service recorded as full-time. The member resigns, and the final calculation comes in lower.

## Why Nobody Has Built This
Estimate engines are built to calculate, not to judge the quality of their inputs. The history that would show which record features lead to estimate–final differences sits in the PAS, but no one has joined estimates to finals at scale.

## What to Build
An estimate that carries a verification status for each input and a range for the result. A model trained on past estimate–final pairs predicts which members' records are likely to change and by how much. Before the member commits to a date, those records go to an analyst for verification, so the final calculation starts from a checked record.

## Target Customer
Member services directors at statewide systems; DB administrators for corporate plans issuing lump-sum and annuity elections.

## Impact If Built
Fewer members retire on a number that later shrinks, fewer post-retirement recalculations and appeals, and analysts' verification work moves ahead of the retirement date instead of behind it.
