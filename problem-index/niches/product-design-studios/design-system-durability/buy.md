# Drift Detection From Infrastructure as Code

**Niche:** [[niches/product-design-studios/design-system-durability/profile|Design System Durability]]
**Industry:** [[industries/product-design-studios|Product Design Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Infrastructure as code made configuration drift a detected and reported condition, and design systems drift silently.
**Tags:** #automation #workflow-orchestration #data-integration #compliance #evaluation-metrics #graph-theory #change-point-detection #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to deliver a design system that does not begin drifting from the client's production code the week the studio leaves — and whoever makes it durable takes the account.

## The Problem
Infrastructure engineering confronted exactly this shape of problem: a declared desired state, a real running state, and continuous divergence between them. The answer was drift detection — continuously compare what is declared against what exists, report the difference, and either reconcile automatically or raise it for a decision. The pattern is standard, the tooling is commodity, and nobody would now run infrastructure without it. Design systems are a declared desired state with no detection at all.

## What Already Exists
Declared desired state versus actual state comparison; continuous drift detection and reporting; automatic reconciliation where safe; policy enforcement on divergence; and compliance dashboards for state alignment.

## The Customization Gap
The adaptation is to a desired state expressed in a design tool and an actual state expressed in rendered interfaces. It requires: (1) comparison between a visual design definition and a code implementation, where no shared machine-readable representation exists — this is the substantive difference and is the whole technical problem; (2) legitimate divergence, since a product frequently needs something the system does not have and that is not a fault; (3) no ability to auto-reconcile, because the resolution is a design decision; (4) a client with no equivalent of a platform team to own it; and (5) drift that includes new components created outside the system rather than only modified ones.

## Target Customer
Design studios, client design system teams, in-house design organisations, and design and frontend tooling vendors.

## Impact If Solved
Infrastructure made drift a detected and reported condition and nobody runs without it now. No shared machine-readable representation between a design definition and a rendered interface is the technical problem to solve.
