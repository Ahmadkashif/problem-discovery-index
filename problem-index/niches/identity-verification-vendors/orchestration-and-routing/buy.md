# Payment Routing and Cascading

**Niche:** [[niches/identity-verification-vendors/orchestration-and-routing/profile|Orchestration & Routing]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payments built smart routing that learns which processor approves which transaction, and identity orchestration routes on a static rule table.
**Tags:** #gradient-boosting #evaluation-metrics #workflow-orchestration #confidence-intervals #revenue-impact #automation #causal-inference #data-integration
**Contested on:** Every serious competitor in this niche is fighting to send each applicant to the verification path that will actually verify them — and whoever measures which path works for which kind of person owns the decision layer above every individual vendor.

## The Problem
Payment orchestration solved the structurally identical problem: several providers, different strengths by card type, geography and issuer, and a routing decision per transaction. The answer was smart routing — models trained on authorisation outcomes, retry cascades ordered by expected success, and continuous measurement of each provider by segment. It is standard and it demonstrably improves approval rates. Identity orchestration has the same architecture and routes on a rule table.

## What Already Exists
Smart payment routing with learned provider selection; retry and cascade logic with ordering; per-provider performance measurement by segment; cost-aware routing; and failover testing practice.

## The Customization Gap
The adaptation is to a decision about a person with no outcome on failure. It requires: (1) success defined as verifying a legitimate applicant rather than as an approval, which cannot be observed directly for rejections and is the substantive difficulty — payment routing has an unambiguous outcome and this does not; (2) segments defined by applicant and document characteristics rather than by card and issuer, which are richer and more sensitive; (3) a cascade whose cost is borne partly by the applicant in time and effort, so more attempts is not freely better; (4) vendors whose data-sharing terms constrain comparison; and (5) fairness considerations in routing, since sending certain populations down worse paths is a real risk that payment routing does not carry.

## Target Customer
Platform and policy leadership, customers with multi-vendor stacks, payment orchestration vendors adjacent to the space, and verification vendors.

## Impact If Solved
Payment routing solved the identical architecture with an observable outcome. The adaptation is defining success without an outcome on failure, which makes the exploration sample the critical dependency.
