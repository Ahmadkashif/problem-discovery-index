# Process Mining From Operations Analytics

**Niche:** [[niches/saas-implementation-partners/pattern-extraction/profile|Pattern Extraction]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Process mining reconstructs how organisations actually work from system logs, and nobody has pointed it at how partners actually configure.
**Tags:** #graph-theory #k-means-clustering #data-integration #evaluation-metrics #descriptive-statistics #dimensionality-reduction #automation #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to find out what hundreds of past implementations of the same platform actually have in common — and whoever extracts that takes the account.

## The Problem
Process mining built a mature discipline around exactly this move: take the traces a system already produces, reconstruct the underlying structure, discover the variants, quantify how often each occurs, and compare one organisation against many. The tooling is commercial and widely deployed against enterprise systems — frequently the same systems these partners implement. It has been pointed at how customers work and never at how the partners configure.

## What Already Exists
Automatic structure discovery from system traces; variant analysis with frequency; conformance comparison against a reference model; cross-organisation benchmarking; and visualisation of discovered structures.

## The Customization Gap
The adaptation is to configuration metadata rather than event logs. It requires: (1) the input being a static configuration rather than a sequence of events, so discovery is structural comparison rather than trace reconstruction — this is the substantive difference and changes the algorithms entirely; (2) artefacts spread across hundreds of separately owned tenants rather than one organisation's system; (3) client confidentiality requiring abstraction before comparison; (4) platform version differences that make the same intent look different in metadata; and (5) the output serving a consultant designing a new configuration rather than an analyst improving an existing process.

## Target Customer
Implementation partners, delivery leadership, platform vendors, and process mining and analytics vendors.

## Impact If Solved
Process mining reconstructs structure from traces and quantifies variants as mature commercial practice. Static configuration metadata across separately owned tenants is what makes the discovery structural rather than sequential.
