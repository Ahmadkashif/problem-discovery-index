# Data Replication and Reconciliation Practice

**Niche:** [[niches/headless-commerce-vendors/catalogue-price-consistency/profile|Catalogue & Price Consistency]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Distributed systems and financial reconciliation both solved detecting and correcting divergence between copies, and composable commerce relies on each copy synchronising correctly.
**Tags:** #data-integration #hypothesis-testing #evaluation-metrics #automation #compliance #confidence-intervals #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to make every service's copy of the catalogue agree about the price a customer will be charged — and whoever does that removes the category's most visible failure, because the copies disagree and the customer notices.

## The Problem
Keeping replicas consistent, detecting when they are not, and reconciling them is thoroughly studied. Distributed systems formalised consistency models and built anti-entropy mechanisms that compare replicas and repair them rather than assuming replication worked. Financial operations built daily reconciliation as a discipline precisely because systems that should agree do not. Composable commerce replicates the catalogue into six services and relies on each replication path working, with no comparison and no repair.

## What Already Exists
Consistency models with explicit staleness bounds; anti-entropy and read-repair mechanisms; change data capture with guaranteed delivery; reconciliation practice from financial operations with break investigation workflows; checksum and digest comparison for large datasets; and eventual consistency monitoring.

## The Customization Gap
The adaptation is to replicas held by different companies with different data models. It requires: (1) comparison across heterogeneous representations, since each service stores the catalogue in its own shape and a checksum comparison is unavailable — comparing the answers to the same question rather than the stored data is the substitution and is what makes it tractable; (2) the customer-visible answer as the unit of comparison, since the internal state may legitimately differ while the surfaced price must not; (3) repair without write access, since the retailer frequently cannot correct a vendor's copy and the remedy is a re-trigger or a cache invalidation; (4) staleness bounds stated in the contract, since an anti-entropy mechanism needs a target and no vendor agreement specifies one; and (5) reconciliation at a cadence matched to price volatility, which for promotional retail is minutes rather than daily.

## Target Customer
Retail data engineering, platform vendors, integrators, and the distributed systems and reconciliation communities.

## Impact If Solved
Anti-entropy exists because replication silently fails and this architecture assumes it does not. Comparing the answers to the same question rather than the stored representations is what makes the check work across six different data models.
