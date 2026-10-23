# Earned-Value Cost Control for a Service Contract

**Niche:** [[niches/facilities-management-firms/corporate-ifm-portfolios/profile|Corporate Occupier IFM Portfolios]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Construction and defence programmes have tracked cost against planned work for decades; IFM accounts priced on planned work never compare the two.
**Tags:** #descriptive-statistics #time-series-forecasting #data-integration #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to run a corporate portfolio at a margin the contract price can bear. That splits into two contests with different winners: pricing a portfolio whose real maintenance load nobody has measured before the bid closes, and deciding, service by service and region by region, what to self-deliver and what to subcontract once the account is live. Decomposed into contested sub-niches below.

## The Problem
An IFM price is built from planned work: PM task hours per asset, an expected reactive volume, subcontract allowances and a management overhead. Once the account is live, nobody tracks actual work against that plan. The account is managed on total cost against budget, which hides offsetting errors until they stop offsetting.

## What Already Exists
Earned-value management and project cost-control tools used on construction programmes and federal projects (Primavera-based cost control, Deltek Cobra and similar) compare planned value, earned value and actual cost by work package and forecast cost at completion.

## The Customization Gap
A service contract has no completion and no single schedule. The adaptation treats each contract year as the baseline. Work packages become service lines by site, planned value becomes the priced PM hours and the reactive allowance, earned value becomes the work completed against them, and the forecast is the cost at contract-year end and at renewal. It must take its actuals from CMMS work orders and AP invoices rather than timesheets coded to project tasks, and handle client-approved scope changes as baseline revisions.

## Target Customer
Provider account finance teams on fixed-price and hybrid IFM accounts.

## Impact If Solved
A drifting account is visible in month three instead of at year-end, while there is still time to re-scope, re-price or change delivery.
