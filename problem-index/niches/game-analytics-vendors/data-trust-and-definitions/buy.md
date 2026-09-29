# Metric Layers From Business Intelligence

**Niche:** [[niches/game-analytics-vendors/data-trust-and-definitions/profile|Data Trust & Metric Definitions]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Business intelligence built semantic layers so a metric means one thing everywhere, and game studios define theirs per tool.
**Tags:** #data-integration #workflow-orchestration #evaluation-metrics #automation #compliance #sets-and-logic #descriptive-statistics #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to make one number mean one thing across every tool and every team, and whoever establishes that takes the account.

## The Problem
Business intelligence solved this with the semantic layer: metrics are defined once in a central model, every downstream tool computes from that definition, lineage traces any figure to its source, and changes to a definition are versioned and visible. The pattern is mature, the tooling is commercial, and organisations far smaller than a game studio run on it. Game analytics stacks define metrics separately in each tool and reconcile in meetings.

## What Already Exists
Central semantic and metric layers; single-definition-many-consumers architecture; column and metric lineage; definition versioning and change tracking; and certified dataset concepts.

## The Customization Gap
The adaptation is to a stack whose primary tool is a third-party analytics platform with its own fixed definitions. It requires: (1) a vendor platform that computes its own metrics and cannot be made to consume an external definition, so reconciliation rather than replacement is the realistic approach — this is the substantive difference; (2) event-sourced metrics where the definition depends on session and boundary rules specific to games; (3) platform revenue reporting with fees, currencies and timing that finance defines differently; (4) publisher reporting obligations with externally imposed definitions; and (5) studios with no data governance function to own the layer.

## Target Customer
Studio data and analytics leadership, publishers, game analytics vendors, and semantic layer and BI vendors.

## Impact If Solved
BI solved single-definition-many-consumers with mature commercial tooling. A third-party platform that computes its own metrics and cannot consume an external definition makes reconciliation, not replacement, the realistic path.
