# A Variance Bridge the Operator Did Not Write

**Niche:** [[niches/renewable-power-producers/financial-owners-asset-managers/profile|Financial Owners & Third-Party Asset Managers]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A fund that owns forty plants learns why each missed budget from the operator's own commentary, and has no independent way to split the miss into weather, availability, curtailment, price and degradation.
**Tags:** #causal-inference #linear-regression #gaussian-processes #feature-engineering #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to explain each month's production and revenue variance against the budget, and whoever leaves the smallest unexplained share of that variance takes the account.

## The Problem
Operators explain shortfalls in prose, and weather is the easiest explanation. The owner cannot tell a bad wind month from a poorly run plant without the interval data and a resource benchmark.

## Why Nobody Has Built This
Owners rarely get raw SCADA or metering by contract, independent resource data per site costs money, and asset performance vendors sell to the operator who controls the plant.

## What to Build
A bridge computed each month from metered output, ISO settlement data and an independent resource dataset (reanalysis or satellite irradiance) that splits the variance against budget into resource, availability, curtailment by type, node-to-hub basis, price and residual performance, with confidence bands, and compares operators across the owner's portfolio on the same basis.

## Target Customer
Heads of energy asset management at infrastructure funds and insurers owning 1–10 GW through several operators.

## Impact If Built
Shrinking the unexplained share of monthly variance from ~40% to ~10% (estimate) lets an owner of 3 GW spot an underperforming operator a year earlier, worth ~1% of revenue, ~$3–4M a year at that scale.
