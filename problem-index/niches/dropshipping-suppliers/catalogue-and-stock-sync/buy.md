# Data Integration Practice

**Niche:** [[niches/dropshipping-suppliers/catalogue-and-stock-sync/profile|Catalogue & Stock Synchronisation]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Change data capture, event streaming and reconciliation are standard practice in every serious data platform, and supplier stock sync runs on a polling job and hope.
**Tags:** #data-integration #workflow-orchestration #automation #change-point-detection #evaluation-metrics #compliance #descriptive-statistics #confidence-intervals
**Contested on:** This niche is not terminal — knowing whether the item still exists and making the listing worth buying are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Keeping two systems in agreement is one of the most thoroughly worked problems in data engineering. Change data capture, event streaming, idempotent processing, reconciliation jobs, freshness monitoring and alerting on staleness are all standard, well-tooled and widely deployed. Dropshipping platforms, whose entire function is keeping many pairs of systems in agreement, mostly run scheduled full-feed pulls with no freshness measurement and no reconciliation at all.

## What Already Exists
Change data capture and event streaming infrastructure; idempotent and exactly-once processing patterns; reconciliation frameworks comparing source and target state; data freshness and staleness monitoring; and schema drift detection.

## The Customization Gap
The adaptation is to sources that are outside the platform's control and largely uncooperative. It requires: (1) change capture without supplier participation, since most suppliers publish a flat file on a schedule and cannot be asked to emit events — which makes inference from successive snapshots the only route and is the central engineering problem; (2) freshness measured per supplier, per product, against volatility rather than against a global service level, because the tolerable staleness of a slow-moving item and a flash-selling one differ by orders of magnitude; (3) reconciliation against outcomes, not just against the source, as a failed order is evidence no feed will ever give; (4) schema and identifier drift as a routine condition rather than an incident, since supplier feeds change shape without notice and the standard alerting model assumes rarity; and (5) cost structures that work across thousands of low-value feeds, where per-source engineering attention is not economic.

## Target Customer
Dropshipping and sourcing platforms, ecommerce integration vendors, and data infrastructure vendors for whom uncooperative external sources are an unserved case.

## Impact If Solved
Suppliers cannot be asked to emit events, so inferring change from successive snapshots is the whole engineering problem. Reconciling against order outcomes brings in evidence no feed can supply, and per-product freshness targets replace a global schedule that is wrong for everything.
