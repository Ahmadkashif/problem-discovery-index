# The Validation Nobody Invoices

**Niche:** [[niches/parking-operators/monthly-accounts-validations/profile|Monthly Accounts, Access Cards & Validations]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Retail, restaurant and medical tenants stamp or code their customers' parking free, and a share of those validations is never billed back to the tenant.
**Tags:** #feature-engineering #data-integration #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to keep a facility's monthly-contract capacity sold and paid, and whoever bills and collects the highest share of that capacity each month takes the account.

## The Problem
Validation programmes mix stamps, stickers, printed codes and app vouchers. At month end the coordinator counts redemptions per tenant from PARCS reports and invoices the tenant. Programmes change, codes are shared, and some redemptions match no active agreement, so they are absorbed as lost revenue.

## Why It's Still Broken
Validation agreements are made by the owner's leasing team, redemptions are recorded by the PARCS, and invoices are produced by the operator. Nobody owns the match.

## What a Fix Looks Like
Load every validation agreement (tenant, type, value, cap) into one table, map each redemption to an agreement automatically, flag redemptions with no agreement or above cap, and draft the tenant invoices. Unmatched codes are disabled at the gate.

## Who Feels the Pain
Monthly-account coordinators, operator revenue control and owners whose statements show revenue they cannot trace.

## Impact If Fixed
If 5% of validation value goes unbilled (estimate), a garage redeeming $300K of validations a year recovers ~$15K, at the cost of a one-time agreement load.
