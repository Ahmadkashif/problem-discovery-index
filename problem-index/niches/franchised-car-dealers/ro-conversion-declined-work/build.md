# A Finding-Level Record of What Customers Approve

**Niche:** [[niches/franchised-car-dealers/ro-conversion-declined-work/profile|Repair Order Conversion & Declined Work]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Stores record that an inspection was sent, not which finding, photo, price and message the customer approved or declined, so presentation is never learned.
**Tags:** #gradient-boosting #causal-inference #survival-analysis #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get inspection findings approved while the car is still in the bay, and whoever lifts approved labour hours per repair order from multipoint-inspection findings takes the account.

## The Problem
Two advisors send the same brake finding; one gets approval at a high rate, the other doesn't. The difference — photo, measurement shown, price framing, timing, phone call versus text — is invisible because approvals are logged per repair order, not per finding.

## Why Nobody Has Built This
Inspection vendors store media and send links; approval data sits in the DMS; the join and the experiment design are nobody's product.

## What to Build
A finding-level ledger (item, measurement, photo or video, price, channel, advisor, time to response, approved or declined, and return within 180 days for declined items) with uplift models that recommend how and when to present each finding, and survival models of declined-item return.

## Target Customer
Fixed ops directors at groups with consistent inspection tools across stores.

## Impact If Built
Each advisor gets evidence of what works; lifting approved hours by ~0.1 per repair order (estimate) across ~1,500 monthly repair orders adds ~150 billed hours a month.
