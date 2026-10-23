# A Should-Cost for Every Reactive Job

**Niche:** [[niches/facilities-management-firms/subcontractor-invoice-validation/profile|Subcontractor Invoice Validation & Pass-Through Billing]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An invoice under the not-to-exceed passes, even when the same job on the same kind of asset usually costs half as much.
**Tags:** #gradient-boosting #gaussian-mixture-models #k-nearest-neighbors #large-language-models #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to validate every subcontractor invoice against its work order, rate card and not-to-exceed before it is rebilled to the client, and whoever catches the overbilling before the client's audit does takes the account.

## The Problem
NTEs are set high so routine work does not need approval, and subcontractors learn to bill near them. A rule check confirms the invoice is under the limit and matches the rate card, and says nothing about whether four hours and a compressor contactor was a reasonable bill for that call.

## Why Nobody Has Built This
Validation tools check rules, not reasonableness. A should-cost needs job-level history joined across work orders, invoices and assets, which sits in separate systems, and the providers that hold the history have treated AP as a cost centre rather than a data asset.

## What to Build
A model of expected cost per job, from trade, asset class and age, region, time of day, reported problem and resolution, trained on the provider's own paid-invoice history. Each new invoice is extracted into lines, checked against the rules and scored against its should-cost, with outliers routed to a coordinator with the comparison ("median for this job type here: 1.5 hours"). Subcontractor-level drift is reported monthly.

## Target Customer
Account finance and procurement leads at IFM providers with large pass-through volumes.

## Impact If Built
Overbilling is caught where rules cannot see it, subcontractor pricing is managed on evidence, and the provider's pass-through stands up to client audit (estimate: a low single-digit percentage of reactive pass-through spend).
