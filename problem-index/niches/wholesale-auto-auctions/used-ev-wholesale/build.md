# A Battery Health Estimate From a Five-Minute Scan

**Niche:** [[niches/wholesale-auto-auctions/used-ev-wholesale/profile|Used EVs at Wholesale]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A full battery capacity test takes hours of charging and discharging; a lane needs a battery figure in minutes, with a stated confidence.
**Tags:** #gradient-boosting #gaussian-processes #feature-engineering #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to put a battery figure on a used EV's condition report that buyers will bid on and not dispute, and whoever has the lowest battery-related arbitration rate on EV units sold takes the account.

## The Problem
An inspector can read the battery management system's own estimate where the OEM exposes it, read the dashboard range, or skip the battery. None of these is comparable across makes. The BMS estimate can be optimistic, and dashboard range depends on the last driver. Buyers discount EVs for the uncertainty.

## Why Nobody Has Built This
Battery data access differs by OEM. Ground truth needs slow capacity tests on a sample. And until 2026 EV wholesale volume was too small for auctions to invest.

## What to Build
A five-minute scan through the OBD port reading BMS data: cell voltages and spread, temperatures, the BMS state-of-health estimate, charge cycles and fast-charge counts where available. A model calibrated on a sample of full capacity tests by model and year produces a state-of-health estimate with an uncertainty interval, and a grade the condition report can show. Every graded car is then tracked through claims and resale, so the grade is checked against outcomes.

## Target Customer
Inspection leaders at the national auctions; captives certifying off-lease EVs before upstream sale.

## Impact If Built
If a trusted grade narrows the discount buyers apply to uncertain EVs by $300–800 a unit (estimate), the gain at ~16% of ~220,000 off-lease returns a month is $10–28M a month across the market.
