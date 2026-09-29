# Change Data Capture Practice

**Niche:** [[niches/customer-data-platforms/warehouse-native-composable/profile|Warehouse-Native Composable]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data engineering solved incremental change propagation with exactly-once semantics, and audience syncs frequently recompute everything and hope.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #change-point-detection #compliance #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to activate from a warehouse the vendor never touches, at the reliability and latency a customer-facing use case needs — and whoever does that takes the organisations that already own their data.

## The Problem
Propagating changes from one system to another incrementally, reliably and without duplication is a solved problem. Change data capture, log-based replication, exactly-once processing, idempotent writes and watermarking are standard infrastructure with mature implementations. Composable activation frequently works by recomputing an audience on a schedule and diffing the result, which is expensive, slow, and produces membership churn that downstream destinations handle badly.

## What Already Exists
Log-based change data capture; exactly-once and idempotent processing; watermarking and incremental computation; stream processing frameworks; and replication monitoring with lag measurement.

## The Customization Gap
The adaptation is to changes defined by a query result rather than by a row edit. It requires: (1) detecting membership change in a derived set, since a customer entering an audience may result from a change to any of a dozen underlying tables or from the passage of time — this derived-change problem is not what row-level capture solves and is the substantive difference; (2) destinations with widely varying update semantics, some accepting deltas and some requiring full lists, which forces per-destination strategies; (3) warehouse cost as a first-order constraint, since recomputation is billed and the efficient approach is financially rather than technically motivated; (4) latency requirements that differ by use case, where suppression needs minutes and a lookalike audience needs a day; and (5) correctness that must be provable for consent-driven exclusions, where a missed change is a compliance failure rather than a delay.

## Target Customer
Composable activation vendors, data platform teams, and streaming infrastructure vendors for whom audience activation is an adjacent market.

## Impact If Solved
Change capture solves row-level propagation and here the change is in a derived query result driven by a dozen tables or by time passing. Warehouse cost makes efficiency financially rather than technically motivated, and consent exclusions make missed changes a compliance failure.
