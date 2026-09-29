# Integration Patterns From Enterprise Architecture

**Niche:** [[niches/saas-implementation-partners/integration-architecture/profile|Integration Architecture]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise integration patterns were catalogued decades ago and every engagement designs from scratch anyway.
**Tags:** #data-integration #graph-theory #workflow-orchestration #compliance #evaluation-metrics #sets-and-logic #automation #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to connect the same dozen enterprise systems without designing the integration from scratch on every engagement — and whoever industrialises that takes the account.

## The Problem
Enterprise integration patterns are among the best-documented bodies of knowledge in software. The canonical catalogue of messaging patterns, idempotency, retry, dead-letter handling, saga and compensation, and event versioning has existed for decades and is taught. Integration platforms implement them as primitives. Implementation partners connecting the same systems repeatedly work from the general catalogue and reconstruct the specific application every time.

## What Already Exists
Catalogued messaging and integration patterns; idempotency, retry and compensation primitives; reconciliation and exception handling patterns; contract testing between systems; and event schema versioning.

## The Customization Gap
The adaptation is from general patterns to specific system pairs with specific data models. It requires: (1) the useful unit being a concrete mapping between two named platforms' object models rather than an abstract pattern — this is the substantive difference, and the abstraction level of the canonical catalogue is exactly why it does not save time; (2) endpoints that are SaaS products whose APIs change on the vendor's schedule; (3) client data models that vary at the field level while the shape stays constant; (4) governance and audit requirements that vary by client and industry; and (5) the knowledge of how each pattern fails in production, which exists nowhere written.

## Target Customer
Implementation partners, solution architects, integration platform vendors, and enterprise architecture tooling providers.

## Impact If Solved
Integration patterns are catalogued, taught and implemented as platform primitives. The abstraction level is exactly why the catalogue saves no time; a concrete mapping per named system pair is what has to exist.
