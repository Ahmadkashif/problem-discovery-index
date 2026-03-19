# Feasibility — Supplier Invoice Reconciliation Against PO and Receiving

**Industry:** [[food-distributors|Food Distributors]]
**Problem:** [[problems/food-distributors/low-impact-2|Supplier Invoice Reconciliation Against PO and Receiving]]
**Problem type:** Low Impact

**Problem summary:** Generic AP automation chokes on catch-weight pricing, grade adjustments, and promotional allowances — the three things that make every food distribution invoice uniquely complex.

## Solution Approach
Adapt AP automation with food-distribution-specific templates and rules to handle catch-weight pricing, grade substitutions, promotional allowances, and freight/temperature surcharges by reconciling supplier contracts, POs, and receiving logs. Build deterministic rules with exception queues so AP can resolve discrepancies without rekeying data.

## Open Source Data
Open data adds little here; accuracy comes from the distributor's own PO, invoice, receiving, and contract data, plus any supplier EDI feeds.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
