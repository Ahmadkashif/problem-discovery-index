# Platform Migration Practice

**Niche:** [[niches/customer-data-platforms/the-platform-architecture/profile|The Platform Architecture]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise software has established practice for migrating between platform architectures, and customer data migrations are improvised because nobody will admit the architecture changed.
**Tags:** #data-integration #workflow-orchestration #compliance #evaluation-metrics #automation #descriptive-statistics #confidence-intervals #graph-theory
**Contested on:** This niche is not terminal — the packaged platform and the warehouse-native stack compete on different things for different buyers, and they are stated separately in the sub-niches.

## The Problem
Migrating between platform architectures is a known enterprise discipline: parallel running, reconciliation between old and new, phased cutover by workload, rollback plans, and validation that the new system produces the same answers. It is applied routinely to core systems because the cost of getting it wrong is severe. Customer data platform migrations — which move identity graphs, consent records, segment definitions and live activations — are frequently improvised, because the category treats the architectural shift as a vendor preference rather than as a platform migration.

## What Already Exists
Migration methodology with parallel running and reconciliation; phased cutover by workload; data validation and equivalence testing; rollback planning; and dual-run cost management.

## The Customization Gap
The adaptation is to migrating a probabilistic identity graph and live customer-facing activations. It requires: (1) validating equivalence of a graph whose correctness is unmeasured in either system, so the usual does-the-new-system-match test has no basis — establishing what equivalence even means here is the substantive problem; (2) live activations that cannot be paused, since suppression and journeys are customer-facing and a gap is a compliance incident rather than a delay; (3) consent and retention state that must transfer with provable fidelity, which is a legal requirement rather than a data quality preference; (4) segment definitions expressed in one platform's language that must be re-expressed and proven equivalent, which is where silent behaviour changes hide; and (5) a migration frequently driven by cost, so a lengthy parallel run undermines the business case that motivated it.

## Target Customer
Data platform and marketing operations leadership, systems integrators, and migration tooling vendors for whom customer data platforms are an unserved case.

## Impact If Solved
Enterprise migration practice validates that the new system gives the same answers, and here neither system's identity graph has a known correctness. Transferring consent state with provable fidelity is a legal requirement that improvised migrations routinely miss.
