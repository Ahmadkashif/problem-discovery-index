# Federated Query and Distributed Governance

**Niche:** [[niches/data-marketplace-brokers/in-ecosystem-data-sharing/profile|In-Ecosystem Data Sharing]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Federated query engines and distributed access control have decades of work on querying across administrative boundaries, and data sharing implemented it as a per-platform feature.
**Tags:** #data-integration #graph-theory #compliance #convex-optimization #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to make external data appear inside the buyer's own platform with governance and lineage intact and nothing copied — and whoever does that takes the account, because the buyer has already chosen the platform and is choosing between its marketplace and friction.

## The Problem
Querying data that lives under someone else's administration, with their access policies and your query planner, is the problem federated and distributed databases have studied for decades — including cost estimation across boundaries, pushdown of predicates to the remote side, and the consistency and trust questions that arise when the remote party is not you. Data sharing solved a useful special case inside each platform and inherited none of the general work.

## What Already Exists
Federated query engines with cross-source planning and predicate pushdown; distributed and multi-database transaction and consistency models; attribute-based access control with policy evaluation across domains; data virtualisation platforms; and open table formats that make a dataset readable by multiple engines without copying.

## The Customization Gap
The adaptation is to a boundary that is commercial as well as administrative. It requires: (1) query cost and permitted-use policy evaluated together, since a query may be technically executable and contractually forbidden and no federated engine models that — this coupling is the distinctive requirement; (2) open table formats as the sharing substrate rather than proprietary primitives, which would make cross-platform sharing a property of the format rather than a partnership negotiation and is the most consequential available change; (3) policy composition where the provider's and consumer's rules both apply, with a defined precedence, which distributed access control addresses and no marketplace states clearly; (4) cost attribution across the boundary, since the query runs on someone's compute and the current arrangements are inconsistent; and (5) auditability that satisfies both parties' compliance obligations from one record, which neither side can currently produce alone.

## Target Customer
Cloud data platforms, data providers publishing across ecosystems, enterprise governance functions, and the federated query and open table format communities.

## Impact If Solved
Federated query and distributed access control solved the general problem and sharing implemented a per-platform special case. Open table formats as the substrate would make cross-platform sharing a property of the format rather than a partnership to negotiate.
