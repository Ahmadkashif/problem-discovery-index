# Product Configurators From Insurance

**Niche:** [[niches/embedded-finance-platforms/programme-configuration/profile|Programme Configuration]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Insurance built product configuration platforms that encode regulatory constraints per jurisdiction and generate compliant products from templates, and embedded finance configures by hand.
**Tags:** #workflow-orchestration #optimization-fundamentals #sets-and-logic #compliance #automation #data-integration #evaluation-metrics #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to turn the twenty programme archetypes that keep getting rebuilt by hand into configurable starting points that carry their bank-specific constraints with them — and whoever does it takes launch time from months to days.

## The Problem
Insurance faces the same structure: a product must be assembled from components, must satisfy rules that differ by state, must be filed and approved before sale, and is mostly a variation on products already sold. The industry built configuration platforms with product templates, rules engines encoding regulatory constraints per jurisdiction, validation before filing, and libraries of approved forms. Embedded finance has the identical shape — components, per-bank constraints, approval before launch, recurring archetypes — and configures each programme by hand.

## What Already Exists
Insurance product configuration and rating platforms; rules engines with jurisdictional constraint libraries; form and template repositories tied to filings; pre-filing validation; and product versioning tied to regulatory change.

## The Customization Gap
The adaptation swaps the jurisdiction for the sponsor bank. It requires: (1) constraints defined by a private counterparty rather than published by a regulator, so the constraint library must be built by observation and negotiation rather than read off a statute — this is the substantive adaptation and is why nobody has done it; (2) constraints that change when a bank's risk appetite changes, with no filing to signal it; (3) programmes operated by the customer rather than the configuring party, so the template must be legible to a developer; (4) compliance monitoring as part of the product definition rather than as a separate function; and (5) launch measured in weeks rather than in filing cycles, which raises the value of configuration-time validation.

## Target Customer
Platform implementation teams, sponsor bank programme review functions, and configuration platform vendors for whom banking-as-a-service is an unentered adjacency.

## Impact If Solved
Insurance solved this shape with published constraints. The adaptation is building the constraint library from a private counterparty's policy rather than a statute, which is exactly the part currently living in people's heads.
