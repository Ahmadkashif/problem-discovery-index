# A Matched-System Availability Score for Every Branch on Every Peak Day

**Niche:** [[niches/plumbing-and-hvac-distributors/residential-hvac-equipment-distribution/profile|Residential HVAC Equipment Distribution to Dealers]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Distributors measure SKU fill rate; dealers buy complete systems, and nobody measures whether a branch could have sold one on the day it was needed.
**Tags:** #time-series-forecasting #gradient-boosting #monte-carlo-methods #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to have the dealer's brand of complete, AHRI-matched system — now in R-454B or R-32 — on the branch shelf on the day a no-cool call becomes a replacement, and whoever keeps the highest in-stock rate on complete matched systems through the peak weeks takes the account.

## The Problem
A dealer replacing a 3-ton split system needs the condenser, the matching A2L-rated coil, often a furnace or air handler, a line set and accessories, all from one certified combination. A branch can show 95% SKU fill and still fail the dealer, because the coil that completes the match is out. Distributors report fill rates by SKU, so the misses that cost dealers are invisible.

## Why Nobody Has Built This
ERPs plan items, not systems, and AHRI's matched-combination tables sit outside them. Lost sales at the counter are rarely logged, and the transition replaced most model numbers in 2025, breaking whatever history existed.

## What to Build
A system-level availability engine: load the AHRI matches for the brands carried, compute for each branch and day how many common matched systems by tonnage and efficiency tier were completable from stock (and from a transfer within hours), forecast the next weeks' coverage from weather and demand, and alert the branch and purchasing managers to the missing component. A two-week demo works on public AHRI combinations and synthetic branch stock.

## Target Customer
Operations and purchasing leaders at OEM-aligned and independent HVAC distributors with ten or more branches.

## Impact If Built
If ~5–15% of peak-day residential system requests now fail for one missing component (estimate), lifting completable-system coverage by a few points keeps those replacements, worth tens of thousands of dollars a day at a busy branch, and keeps the dealer from trying another brand.
