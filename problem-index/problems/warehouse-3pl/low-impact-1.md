# Inventory Discrepancy Detection and Cycle Count Targeting

**Industry:** [[warehouse-3pl|Warehouse & 3PL]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic inventory management systems track theoretical inventory levels, but don't identify which specific locations have the highest probability of physical-vs-system discrepancy — enabling targeted cycle counts that concentrate counting effort where errors are most likely.
**Tags:** #gradient-boosting #binary-classification #anomaly-detection #tabular-ml

## The Problem

Warehouse inventory accuracy is maintained through cycle counting — physically counting a subset of inventory locations regularly to catch discrepancies between the WMS system count and physical count. The traditional approach is to count every location on a rotating schedule, regardless of discrepancy risk. This is inefficient: low-risk locations waste count labor; high-risk locations aren't counted frequently enough.

Discrepancy risk varies systematically: locations with high pick velocity have more opportunity for put-away errors; SKUs with multiple units of measure (each/case/pallet) have higher miscounting error rates; receiving locations have higher post-receiving discrepancy rates than established storage locations.

## What Already Exists

WMS platforms have cycle count scheduling tools that generate count lists by zone or rotation. No system uses the location's risk profile to prioritize count frequency.

## The Customisation Gap

A discrepancy-targeting tool needs: (1) historical cycle count results per location (when counted, was there a discrepancy?); (2) location risk features (pick velocity, SKU type, unit-of-measure complexity, days since last count, recent pick/put-away transaction volume); (3) a binary classification model predicting discrepancy probability for each location; (4) a daily count list prioritized by discrepancy probability within the available counting labor budget. The risk-based count prioritization is the differentiator vs. rotation schedules.

## Impact If Solved

Improves inventory accuracy with the same or less cycle count labor. Concentrates counts on highest-risk locations — finding discrepancies earlier and reducing the cumulative error that leads to shipment errors and client disputes.
