# Data Subject Request Fulfilment

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** Low Digitized
**Contested on:** Whether a deletion is verified across every system that holds the data, or confirmed across the systems someone remembered and could reach.

## Profile

**Market Size:** ~$1.05B
**Share of Parent Industry:** ~15%
**Digital Adoption:** Moderate — workflow automated, execution manual
**Target Buyer:** Privacy operations, data engineering, customer support
**Automation Potential:** High for orchestration, low where systems cannot delete

## What Makes This a Distinct Niche

An individual asks for their data to be deleted, or for a copy of it. The workflow platform receives the request, verifies identity, routes tasks to system owners, tracks responses and produces a confirmation within the statutory window.

Everything except the middle works well. The middle is where the request meets infrastructure that was not built for it. A data warehouse with no row-level deletion path. Backups that are immutable by design, which is a security property nobody wants to give up. Application logs holding user identifiers and never intended to be queried by person. Analytics events already aggregated. Third-party processors who must be asked and who respond on their own schedule. Derived data in models and caches.

So the platform orchestrates a request that ends at an engineer writing a script. And the confirmation sent to the individual covers the systems that responded, which is not the same as the systems that hold their data — a distinction the individual cannot see and the organisation frequently cannot measure.

## Current Tools & Gaps

Request intake portals with identity verification, workflow routing to system owners, task tracking against statutory deadlines, templated responses and audit logs. Some connectors performing deletion automatically in common SaaS systems. Processor notification workflow. Access request assembly from connected systems.

The gaps concentrate in execution and verification. Coverage is unmeasured, so nobody knows what proportion of the individual's data the fulfilment actually reached. Deletion is requested rather than verified — almost no platform re-checks afterwards that the data is gone. Backups are handled by policy statements about eventual expiry rather than by any technical mechanism. Derived data in models, aggregates and caches is largely ignored. Processor confirmations are taken at face value. And identity verification is weak enough in places to be its own risk, since a successful fraudulent access request discloses a person's data to an attacker.

## Problems

- [[niches/privacy-tech-vendors/request-fulfilment/build|🔨 Build: Verified Deletion, Not Requested Deletion]]
- [[niches/privacy-tech-vendors/request-fulfilment/buy|🛒 Buy: Orchestration and Reconciliation From Data Engineering]]
- [[niches/privacy-tech-vendors/request-fulfilment/fix|🔧 Fix: Confirmed Across the Systems That Answered]]
