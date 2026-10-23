# Internal Equipment Rates Recomputed From Real Use

**Niche:** [[niches/heavy-civil-contractors/equipment-fleet-telematics-utilization/profile|Equipment Fleet Telematics & Utilisation]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Heavy civil firms charge jobs and bids an hourly rate per machine class set once a year from accounting averages; telematics can recompute it from each unit's real hours, idle share, fuel and repairs.
**Tags:** #linear-regression #survival-analysis #k-means-clustering #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn mixed-OEM telematics into equipment hours posted to job cost codes and hourly rates estimators bid with, and the vendor whose posted hours and rates match audited job cost most closely takes the account.

## The Problem
If the fleet's real utilisation is lower than the rate assumes, every bid under-recovers ownership cost; if higher, the firm prices itself out. Nobody knows which, by class.

## Why Nobody Has Built This
Rates are an accounting exercise, telematics an equipment-department tool, and the estimating system just stores the number.

## What to Build
A rate engine that joins telematics hours and idle share, fuel, repair and depreciation records by unit and class, models expected hours over remaining life, and recomputes ownership and operating rates quarterly, writing them to the estimating system with the change explained. A demo can run on synthetic fleet data and public cost-recovery methods.

## Target Customer
CFOs and equipment managers at fleets of ~100–1,000 units (estimate).

## Impact If Built
If rates move ~5–10% closer to real cost on the classes that dominate bids (estimate), the firm stops winning work below cost or losing it on overhead it doesn't have.
