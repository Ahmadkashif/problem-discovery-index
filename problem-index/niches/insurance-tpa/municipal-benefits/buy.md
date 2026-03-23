# GASB 75 Retiree Liability Tracker

**Niche:** [[niches/insurance-tpa/municipal-benefits/profile|Municipal & Public Entity Benefits]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Financial reporting tools handle GASB 75 disclosures, but none connect to TPA claims data to provide real-time OPEB liability estimates that update as retiree claims and mortality experience change.
**Tags:** #linear-regression #time-series-forecasting #tabular-ml #compliance

## The Problem
Municipalities must report their Other Post-Employment Benefits (OPEB) liability under GASB 75 — the present value of promised retiree health benefits. This liability often exceeds $50M-$500M for mid-size cities and is a major factor in municipal credit ratings. Currently, actuarial firms perform biennial valuations using census data snapshots, but the liability changes continuously as retirees age, claims patterns shift, and healthcare costs trend. Municipal finance directors have no visibility into how their OPEB liability is tracking between actuarial valuations.

## What Already Exists
Actuarial firms (Milliman, Buck, Cheiron) perform GASB 75 valuations as professional service engagements costing $30K-$100K biennially. Government financial reporting platforms like OpenGov and Tyler Technologies (Munis) handle financial statement preparation but don't model actuarial liabilities. Neither provides real-time liability tracking.

## The Customization Gap
The gap is a dashboard that sits between the TPA's claims data and the municipality's financial reporting system, continuously updating the estimated OPEB liability based on actual retiree experience — new retirements, deaths, claims trends, and healthcare cost inflation. It should reconcile to the most recent actuarial valuation and project forward, alerting finance directors when the liability materially deviates from the valuation assumptions.

## Target Customer
Municipal finance directors and city managers in entities with OPEB liabilities exceeding $20M, particularly those facing credit rating pressure from unfunded retiree benefit obligations.

## Impact If Solved
Provides municipalities with continuous visibility into a liability that often represents 20-40% of their total long-term obligations. Enables proactive funding decisions and benefit design changes that can reduce the liability by 10-20% over a 5-year period.
